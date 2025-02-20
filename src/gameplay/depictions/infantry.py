"""Infantry depiction editing."""
from typing import Any, Dict

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_infantry_depictions(source_path: Any, ammo_db: Dict[str, Any], depiction_data: Dict[str, Any]) -> None:
    # this function is so limited and could easily break if the unit edits are not formatted correctly
    """Edit GeneratedDepictionInfantry.ndf.
    
    Args:
        source_path: NDF file containing infantry depictions
        ammo_db: Ammunition database
        depiction_data: Depiction data from game database
    """
    logger.info("Editing GeneratedDepictionInfantry.ndf")
    
    unit_edits = load_unit_edits()
    
    for unit_name, edits in unit_edits.items():
        if "WeaponDescriptor" not in edits:
            continue
            
        weapon_changes = edits["WeaponDescriptor"].get("equipmentchanges", {})
        if "add" in weapon_changes:
            
            # Get weapon info (salvo_index, weapon_name), e.g:
            # "add": [
            #     (2, "MMG_inf_M240B_7_62mm"),
            #     (3, "RocketInf_M72A3_LAW_66mm"),
            # ]
            # todo: handle multiple changes for a single unit (example dosn't work right now xD trolololol)
            turret_index = weapon_changes["add"][0][0] # [change_1][salvo_index] turret index?? not sure trololol
            weapon_name = weapon_changes["add"][0][1] # [change_1][weapon_name]
            
            # Get depiction data for weapon
            if weapon_name in ammo_db["renames_new_old"]:
                old_name = ammo_db["renames_new_old"][weapon_name] 
                if old_name in depiction_data["animation_weapon_map"]:
                    weapon_data = {
                        "weapon_alt_mesh": depiction_data["all_weapon_meshes"][old_name],
                        "fire_effect": depiction_data["all_fire_effects"][old_name],
                        "animation_tag": depiction_data["animation_weapon_map"][old_name]
                    }
                else:
                    weapon_data = {}
                    logger.warning(f"No animation tag found for {old_name}")
            else:
                weapon_data = {
                    "weapon_alt_mesh": depiction_data["all_weapon_meshes"][weapon_name],
                    "fire_effect": depiction_data["all_fire_effects"][weapon_name],
                    "animation_tag": depiction_data["animation_weapon_map"][weapon_name]
                }
            
            try:
                # Add weapon mesh alternative
                _add_weapon_mesh(source_path, unit_name, turret_index, weapon_data["weapon_alt_mesh"])
                
                # Add weapon fire effect
                _add_fire_effect(source_path, unit_name, turret_index, weapon_data["fire_effect"])
                
                # Add conditional animation tag if it exists
                if "animation_tag" in weapon_data:
                    _add_animation_tag(source_path, unit_name, turret_index, weapon_data["animation_tag"])
                
            except Exception as e:
                logger.error(f"Failed to edit depictions for {unit_name}: {str(e)}")


def _add_weapon_mesh(source_path: Any, unit_name: str, turret_index: int, mesh: str) -> None:
    """Add weapon mesh alternative to unit."""
    try:
        weapon_alts = source_path.by_n(f"AllWeaponAlternatives_{unit_name}").v
        new_entry = (
            f"TDepictionDescriptor("
            f"    SelectorId = ['MeshAlternative_{turret_index + 1}']"
            f"    MeshDescriptor = $/GFX/DepictionResources/Modele_{mesh}"
            f")"
        )
        
        for i, obj in enumerate(weapon_alts):
            if is_obj_type(obj.v, "TMeshlessDepictionDescriptor"):
                weapon_alts.insert(i, new_entry)
                obj.v.by_m("ReferenceMeshForSkeleton").v = f"$/GFX/DepictionResources/Modele_{mesh}"
                logger.info(f"Added mesh alternative {mesh} to {unit_name}")
                break
                
    except Exception as e:
        logger.error(f"Failed to add weapon mesh for {unit_name}: {str(e)}")


def _add_fire_effect(source_path: Any, unit_name: str, turret_index: int, fire_effect: str) -> None:
    """Add weapon fire effect to unit."""
    try:
        weapon_subdepictions = source_path.by_n(f"AllWeaponSubDepiction_{unit_name}").v
        operators_list = weapon_subdepictions.by_m("Operators").v
        
        new_entry = (
            f'DepictionOperator_WeaponInstantFireInfantry('
            f'    FireEffectTag = ["{fire_effect}"]'
            f'    WeaponShootDataPropertyName = "WeaponShootData_0_{turret_index + 1}"'
            f')'
        )
        operators_list.add(new_entry)
        logger.info(f"Added fire effect for {unit_name} turret {turret_index}")
        
    except Exception as e:
        logger.error(f"Failed to add fire effect for {unit_name}: {str(e)}")


def _add_animation_tag(source_path: Any, unit_name: str, turret_index: int, tag: str) -> None:
    """Add conditional animation tag to unit."""
    try:
        soldier_depiction = source_path.by_n(f"TacticDepiction_{unit_name}_Soldier").v
        operators_list = soldier_depiction.by_m("Operators").v
        
        for obj in operators_list:
            if is_obj_type(obj.v, "DepictionOperator_SkeletalAnimation2_Default"):
                # Check if ConditionalTags exists
                if obj.v.by_m("ConditionalTags", False) is not None:
                    conditional_tags = obj.v.by_m("ConditionalTags")
                else:
                    # Create ConditionalTags if it doesn't exist using ndf.convert
                    obj.v.add(ndf.convert("ConditionalTags = []"))
                    conditional_tags = obj.v.by_m("ConditionalTags")
                
                # Add the new tag
                conditional_tags.v.add(
                    f"('{tag}', 'MeshAlternative_{turret_index + 1}')"
                )
                logger.info(f"Added animation tag for {unit_name} turret {turret_index}")
                break
                
    except Exception as e:
        logger.error(f"Failed to add animation tag for {unit_name}: {str(e)}")
