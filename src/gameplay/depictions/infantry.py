"""Infantry depiction editing."""

from typing import Any, Dict

from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger('infantry_depictions')

def edit_infantry_depictions(source: Any, unit_db: Dict[str, Any]) -> None:
    """Edit infantry depictions."""
    logger.info("Editing infantry depictions")
    
    # Get depiction data from database
    depiction_data = unit_db.get("depiction_data", {})
    unit_edits = load_unit_edits()
    
    if not depiction_data:
        logger.error("No depiction data found in database")
        return
        
    weapons_processed = set()
    units_processed = set()
    
    for unit, edits in unit_edits.items():
        if not "WeaponDescriptor" in edits:
            continue
            
        if not "equipmentchanges" in edits["WeaponDescriptor"]:
            continue
            
        if "add" in edits["WeaponDescriptor"]["equipmentchanges"]:
            weapon_changes = edits["WeaponDescriptor"]["equipmentchanges"]["add"]
            
            # Track what we're processing
            units_processed.add(unit)
            for _, weapon_name in weapon_changes:
                weapons_processed.add(weapon_name)
                
            _add_weapon_depiction(source, unit, weapon_changes, depiction_data)
    
    # Log summary statistics
    logger.info(f"Processed {len(units_processed)} units with weapon changes")
    logger.info(f"Modified {len(weapons_processed)} unique weapons")
    
    # Validate coverage
    total_weapons = sum(1 for d in depiction_data.values() for _ in d)
    if total_weapons > len(weapons_processed):
        logger.warning(
            f"Only processed {len(weapons_processed)} weapons out of {total_weapons} "
            "available in depiction data"
        )
    
    # Log any missing data
    _validate_depiction_data(depiction_data, weapons_processed)

def _validate_depiction_data(depiction_data: Dict, processed_weapons: set) -> None:
    """Validate completeness of depiction data."""
    for weapon in processed_weapons:
        missing_data = []
        
        if weapon not in depiction_data['weapon_meshes']:
            missing_data.append('mesh')
        if weapon not in depiction_data['fire_effects']:
            missing_data.append('fire effect')
        if weapon not in depiction_data['conditional_tags']:
            missing_data.append('animation tag')
            
        if missing_data:
            logger.warning(
                f"Weapon {weapon} is missing {', '.join(missing_data)} data"
            )

def _add_weapon_depiction(source: Any, unit: str, weapon_data: list, depiction_data: Dict) -> None:
    """Add weapon depiction for a unit."""
    turret_index = weapon_data[0][0] 
    weapon_name = weapon_data[0][1]
    
    try:
        # Get depiction data for this weapon
        mesh_info = depiction_data['weapon_meshes'].get(weapon_name, {})
        effect_info = depiction_data['fire_effects'].get(weapon_name, {})
        tag_info = depiction_data['conditional_tags'].get(weapon_name, {})
        
        if not mesh_info:
            logger.warning(f"No mesh data found for weapon {weapon_name}")
            return
            
        # Add weapon alternative
        weapon_alts = source.by_n(f"AllWeaponAlternatives_{unit}").v
        new_entry = (
            f"TDepictionDescriptor("
            f"    SelectorId = ['MeshAlternative_{turret_index + 1}']"
            f"    MeshDescriptor = {mesh_info['mesh']}"
            f")"
        )
        
        for i, obj in enumerate(weapon_alts):
            if obj.v.type == "TMeshlessDepictionDescriptor":
                weapon_alts.insert(i, new_entry)
                obj.v.by_m("ReferenceMeshForSkeleton").v = mesh_info['mesh']
                logger.info(f"Added {weapon_name} mesh to {unit}")
                break
                
        # Add weapon subdepiction
        _add_weapon_subdepiction(source, unit, turret_index, weapon_name, effect_info)
        
        # Update soldier depiction
        _update_soldier_depiction(source, unit, turret_index, weapon_name, tag_info)
        
        # Log validation info
        if unit not in mesh_info['units']:
            logger.warning(f"Unit {unit} not found in existing mesh mappings for {weapon_name}")
        
    except Exception as e:
        logger.error(f"Failed to add weapon depiction for {unit}: {str(e)}")

def _add_weapon_subdepiction(source: Any, unit: str, turret_index: int, weapon_name: str, effect_info: Dict) -> None:
    """Add weapon subdepiction operator."""
    if not effect_info:
        logger.warning(f"No fire effect data found for weapon {weapon_name}")
        return
        
    weapon_subdepictions = source.by_n(f"AllWeaponSubDepiction_{unit}").v
    operators_list = weapon_subdepictions.by_m("Operators").v
    
    new_entry = (
        f'DepictionOperator_WeaponInstantFireInfantry('
        f'    FireEffectTag = ["{effect_info["effect"]}"]'
        f'    WeaponShootDataPropertyName = "WeaponShootData_0_{turret_index + 1}"'
        f')'
    )
    
    operators_list.add(new_entry)
    logger.debug(f"Added weapon subdepiction for {unit}")

def _update_soldier_depiction(source: Any, unit: str, turret_index: int, weapon_name: str, tag_info: Dict) -> None:
    """Update soldier depiction with new weapon."""
    if not tag_info:
        logger.warning(f"No tag data found for weapon {weapon_name}")
        return
        
    soldier_depiction = source.by_n(f"TacticDepiction_{unit}_Soldier").v
    operators_list = soldier_depiction.by_m("Operators").v
    
    for obj in operators_list:
        if obj.v.type == "DepictionOperator_SkeletalAnimation2_Default":
            obj.v.by_m("ConditionalTags").v.add(
                f"('{tag_info['tag']}', 'MeshAlternative_{turret_index + 1}')"
            )
            logger.debug(f"Updated soldier depiction for {unit}")
            break 