"""Infantry depiction editing."""
from typing import Any, Dict

from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_infantry_depictions(source: Any, depiction_data: Dict[str, Any]) -> None:
    """Edit GeneratedDepictionInfantry.ndf.
    
    Args:
        source: NDF file containing infantry depictions
        depiction_data: Depiction data from game database
    """
    logger.info("Editing GeneratedDepictionInfantry.ndf")
    
    unit_edits = load_unit_edits()
    
    for unit_name, edits in unit_edits.items():
        if "WeaponDescriptor" not in edits:
            continue
            
        weapon_changes = edits["WeaponDescriptor"].get("equipmentchanges", {})
        if "add" not in weapon_changes:
            continue
            
        # Get weapon info
        turret_index = weapon_changes["add"][0][0]
        weapon_name = weapon_changes["add"][0][1]
        
        # Get depiction data for weapon
        if weapon_name not in depiction_data["modele"]:
            logger.warning(f"No depiction data found for weapon: {weapon_name}")
            continue
            
        weapon_data = {
            "modele": depiction_data["modele"][weapon_name]["mesh"],
            "fire_effect": depiction_data["fire_effect"][weapon_name]["effect"],
            "conditionaltag": depiction_data["conditionaltag"][weapon_name]["tag"]
        }
        
        try:
            # Add weapon mesh alternative
            _add_weapon_mesh(source, unit_name, turret_index, weapon_data["modele"])
            
            # Add weapon fire effect
            _add_fire_effect(source, unit_name, turret_index, weapon_data["fire_effect"])
            
            # Add conditional animation tag
            _add_animation_tag(source, unit_name, turret_index, weapon_data["conditionaltag"])
            
        except Exception as e:
            logger.error(f"Failed to edit depictions for {unit_name}: {str(e)}")

def _add_weapon_mesh(source: Any, unit_name: str, turret_index: int, mesh: str) -> None:
    """Add weapon mesh alternative to unit."""
    try:
        weapon_alts = source.by_n(f"AllWeaponAlternatives_{unit_name}").v
        new_entry = (
            f"TDepictionDescriptor("
            f"    SelectorId = ['MeshAlternative_{turret_index + 1}']"
            f"    MeshDescriptor = {mesh}"
            f")"
        )
        
        for i, obj in enumerate(weapon_alts):
            if is_obj_type(obj.v, "TMeshlessDepictionDescriptor"):
                weapon_alts.insert(i, new_entry)
                obj.v.by_m("ReferenceMeshForSkeleton").v = mesh
                logger.info(f"Added mesh {mesh} to {unit_name}")
                break
                
    except Exception as e:
        logger.error(f"Failed to add weapon mesh for {unit_name}: {str(e)}")

def _add_fire_effect(source: Any, unit_name: str, turret_index: int, fire_effect: str) -> None:
    """Add weapon fire effect to unit."""
    try:
        weapon_subdepictions = source.by_n(f"AllWeaponSubDepiction_{unit_name}").v
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

def _add_animation_tag(source: Any, unit_name: str, turret_index: int, tag: str) -> None:
    """Add conditional animation tag to unit."""
    try:
        soldier_depiction = source.by_n(f"TacticDepiction_{unit_name}_Soldier").v
        operators_list = soldier_depiction.by_m("Operators").v
        
        for obj in operators_list:
            if is_obj_type(obj.v, "DepictionOperator_SkeletalAnimation2_Default"):
                obj.v.by_m("ConditionalTags").v.add(
                    f"('{tag}', 'MeshAlternative_{turret_index + 1}')"
                )
                logger.info(f"Added animation tag for {unit_name} turret {turret_index}")
                break
                
    except Exception as e:
        logger.error(f"Failed to add animation tag for {unit_name}: {str(e)}") 