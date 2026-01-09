"""NDF Parsing Functions for DPM Visualizer."""

import ast
import sys
from pathlib import Path
from typing import Any, Dict, List

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import is_obj_type, is_valid_turret, strip_quotes


def parse_infantry_units(mod_src_path: Path) -> Dict[str, Dict[str, Any]]:
    """Parse infantry units from UniteDescriptor.ndf.
    
    Returns:
        Dictionary mapping unit names to unit info
    """
    unit_data = {}
    ndf_path = "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"
    
    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)
        
        for unit_row in parse_source:
            if not hasattr(unit_row, "namespace"):
                continue
            
            unit_name = unit_row.namespace.replace("Descriptor_Unit_", "")
            
            # Extract unit info
            unit_info = extract_unit_info(unit_row)
            if unit_info:
                # Check if it's an infantry unit
                is_infantry = (
                    unit_info.get("unit_role") == "infantry" or
                    "Infanterie" in unit_info.get("tags", []) or
                    unit_info.get("is_infantry", False)
                )
                
                if is_infantry:
                    unit_data[unit_name] = unit_info
        
        # Parse veterancy options from DivisionRules.ndf
        parse_veterancy_from_division_rules(mod_src_path, unit_data)
        
        # Parse ExperienceLevels.ndf to map packs to veterancy effects
        pack_to_effects_map = parse_experience_levels(mod_src_path)
        
        # Parse EffetsSurUnite.ndf to get accuracy bonuses from effects
        effect_bonuses = parse_veterancy_effect_bonuses(mod_src_path)
        
        # Apply veterancy bonuses to units based on their ExperienceLevelsPackDescriptor
        apply_veterancy_bonuses_to_units(unit_data, pack_to_effects_map, effect_bonuses)
                    
    except Exception as e:
        print(f"Error parsing infantry units: {e}")
        raise
    
    return unit_data


def parse_veterancy_from_division_rules(mod_src_path: Path, unit_data: Dict[str, Dict[str, Any]]) -> None:
    """Parse available veterancy levels from DivisionRules.ndf multi_Rule entries.
    
    Updates unit_data with available_veterancy_levels based on NumberOfUnitInPackXPMultiplier.
    """
    ndf_path = "GameData/Generated/Gameplay/Decks/DivisionRules.ndf"
    
    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)
        
        # Track veterancy levels for each unit across all divisions
        unit_veterancy_map: Dict[str, set] = {}
        
        for deck_descr in parse_source:
            if not hasattr(deck_descr, "n"):
                continue
            
            # Only process entries ending in multi_Rule
            if not deck_descr.n.endswith("multi_Rule"):
                continue
            
            unit_rule_list = deck_descr.v.by_m("UnitRuleList", None)
            if not unit_rule_list:
                continue
            
            for rule_obj in unit_rule_list.v:
                if not isinstance(rule_obj.v, ndf.model.Object):
                    continue
                
                # Get unit descriptor
                unit_descr = rule_obj.v.by_m("UnitDescriptor", None)
                if not unit_descr:
                    continue
                
                # Extract unit name from descriptor
                unit_descr_str = strip_quotes(unit_descr.v)
                if not unit_descr_str.startswith("$/GFX/Unit/Descriptor_Unit_"):
                    continue
                
                unit_name = unit_descr_str.replace("$/GFX/Unit/Descriptor_Unit_", "")
                
                # Skip if not an infantry unit we care about
                if unit_name not in unit_data:
                    continue
                
                # Get XP multiplier
                xp_multiplier = rule_obj.v.by_m("NumberOfUnitInPackXPMultiplier", None)
                if not xp_multiplier:
                    continue
                
                # Parse multiplier - could be a string, list, or NDF List with ListRow objects
                xp_multi_value = xp_multiplier.v
                xp_multi_list = None
                
                try:
                    # Check if it's a string that needs parsing
                    if isinstance(xp_multi_value, str):
                        xp_multi_str = strip_quotes(xp_multi_value)
                        xp_multi_list = ast.literal_eval(xp_multi_str)
                    elif isinstance(xp_multi_value, list):
                        # Check if it's an NDF List with ListRow objects
                        if len(xp_multi_value) > 0 and hasattr(xp_multi_value[0], 'value'):
                            # Extract values from ListRow objects
                            xp_multi_list = [float(strip_quotes(row.value)) for row in xp_multi_value]
                        else:
                            # Already a simple list
                            xp_multi_list = [float(x) for x in xp_multi_value]
                    elif hasattr(xp_multi_value, '__iter__'):
                        # Try to iterate and extract values
                        try:
                            xp_multi_list = [float(strip_quotes(getattr(row, 'value', row))) for row in xp_multi_value]
                        except (AttributeError, ValueError):
                            # Fallback: try to convert to string and parse
                            xp_multi_str = str(xp_multi_value)
                            xp_multi_list = ast.literal_eval(xp_multi_str)
                    else:
                        # Try to convert to string and parse
                        xp_multi_str = str(xp_multi_value)
                        xp_multi_list = ast.literal_eval(xp_multi_str)
                    
                    if xp_multi_list is None:
                        continue
                    
                    # Determine available veterancy levels (indices where multiplier > 0)
                    available_levels = [i for i, mult in enumerate(xp_multi_list) if mult > 0]
                    
                    # Add to set for this unit (union across all divisions)
                    if unit_name not in unit_veterancy_map:
                        unit_veterancy_map[unit_name] = set()
                    unit_veterancy_map[unit_name].update(available_levels)
                    
                except (ValueError, SyntaxError, TypeError, AttributeError) as e:
                    print(f"Warning: Failed to parse XP multiplier for {unit_name}: {type(xp_multi_value).__name__}, error: {e}")
                    continue
        
        # Update unit_data with available veterancy levels
        for unit_name, available_levels_set in unit_veterancy_map.items():
            if unit_name in unit_data:
                # Sort and convert to list
                unit_data[unit_name]["available_veterancy_levels"] = sorted(list(available_levels_set))
                # If no levels found, default to [0]
                if not unit_data[unit_name]["available_veterancy_levels"]:
                    unit_data[unit_name]["available_veterancy_levels"] = [0]
        
        # Set default for units not found in division rules
        for unit_name, unit_info in unit_data.items():
            if "available_veterancy_levels" not in unit_info or not unit_info["available_veterancy_levels"]:
                unit_info["available_veterancy_levels"] = [0, 1, 2, 3]  # Default to all levels
                    
    except Exception as e:
        print(f"Warning: Failed to parse veterancy from DivisionRules: {e}")


def parse_experience_levels(mod_src_path: Path) -> Dict[str, Dict[int, List[str]]]:
    """Parse ExperienceLevels.ndf to map ExperienceLevelsPackDescriptor to veterancy effects.
    
    Returns:
        Dictionary mapping pack_name -> level_index -> list of effect names
        e.g., {"ExperienceLevelsPackDescriptor_XP_pack_SF_v2": {1: ["UnitEffect_xp_trained_SF"], ...}}
    """
    ndf_path = "GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf"
    pack_to_effects: Dict[str, Dict[int, List[str]]] = {}
    
    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)
        
        for pack_row in parse_source:
            if not hasattr(pack_row, "namespace"):
                continue
            
            pack_name = pack_row.namespace
            
            # Only process ExperienceLevelsPackDescriptor objects
            if not pack_name.startswith("ExperienceLevelsPackDescriptor_"):
                continue
            
            # Get ExperienceLevelsDescriptors array
            xp_descriptors = pack_row.v.by_m("ExperienceLevelsDescriptors", None)
            if not xp_descriptors:
                continue
            
            level_effects_map: Dict[int, List[str]] = {}
            
            # Iterate through levels (0-based index)
            for level_index, xp_descr in enumerate(xp_descriptors.v):
                if not isinstance(xp_descr.v, ndf.model.Object):
                    continue
                
                # Get LevelEffectsPacks
                level_effects_packs = xp_descr.v.by_m("LevelEffectsPacks", None)
                if not level_effects_packs:
                    continue
                
                effect_names = []
                for effect_pack in level_effects_packs.v:
                    # Extract effect name from reference (e.g., "$/GFX/EffectCapacity/UnitEffect_xp_trained_SF")
                    effect_ref = strip_quotes(effect_pack.v)
                    if "UnitEffect_xp_" in effect_ref:
                        # Extract just the effect name
                        effect_name = effect_ref.split("/")[-1]
                        effect_names.append(effect_name)
                
                if effect_names:
                    level_effects_map[level_index] = effect_names
            
            if level_effects_map:
                pack_to_effects[pack_name] = level_effects_map
                
    except Exception as e:
        print(f"Warning: Failed to parse ExperienceLevels.ndf: {e}")
    
    return pack_to_effects


def parse_veterancy_effect_bonuses(mod_src_path: Path) -> Dict[str, Dict[str, float]]:
    """Parse veterancy bonuses from EffetsSurUnite.ndf.
    
    Converts multiplicative accuracy bonuses to equivalent flat bonuses for application compatibility.
    The application can then apply them as either multiplicative or flat based on user settings.
    
    Returns:
        Dictionary mapping effect_name -> {"accuracy_bonus": float, "reload_speed_multiplier": float}
        - accuracy_bonus: as decimal flat bonus (e.g., 0.12 for 12%)
          - If ModifierType_Multiplicatif: converts multiplier (e.g., 1.12) to flat bonus (0.12)
          - If ModifierType_Additionnel: uses value directly as percentage (e.g., 12 -> 0.12)
        - reload_speed_multiplier: multiplier for time between salvos (e.g., 0.8 means 20% faster)
    """
    ndf_path = "GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf"
    effect_bonuses: Dict[str, Dict[str, float]] = {}
    
    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)
        
        for effect_row in parse_source:
            if not hasattr(effect_row, "namespace"):
                continue
            
            effect_name = effect_row.namespace
            
            # Only process veterancy effects
            if not effect_name.startswith("UnitEffect_xp_"):
                continue
            
            # Parse effects to find bonuses
            effects_list = effect_row.v.by_m("EffectsDescriptors", None)
            if not effects_list:
                continue
            
            accuracy_bonus = 0.0
            reload_speed_multiplier = 1.0  # Default: no change
            
            for effect in effects_list.v:
                if not isinstance(effect.v, ndf.model.Object):
                    continue
                
                effect_type = effect.v.type
                
                # Look for TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor (accuracy bonus)
                if effect_type == "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor":
                    modifier_value = effect.v.by_m("ModifierValue", None)
                    modifier_type = effect.v.by_m("ModifierType", None)
                    if modifier_value:
                        try:
                            value = float(modifier_value.v)
                            mod_type = strip_quotes(modifier_type.v) if modifier_type else None
                            
                            if mod_type == "ModifierType_Multiplicatif":
                                # Multiplicative bonus: convert to equivalent flat bonus
                                # When ModifierType is Multiplicatif, ModifierValue is a multiplier
                                # Example: if ModifierValue is 1.0105, that means multiply by 1.0105 (1.05% increase)
                                # We convert to flat: (multiplier - 1.0) = 0.0105
                                # For storage, we store this as a decimal flat bonus (0.0105 for 1.05%)
                                if value > 1.0:
                                    # Multiplier > 1.0: convert to flat bonus
                                    accuracy_bonus = value - 1.0
                                elif value <= 0.0:
                                    accuracy_bonus = 0.0
                                else:
                                    # Value between 0 and 1: this shouldn't happen for multiplicative bonuses
                                    # But if it does, assume it's already a flat bonus (though this is unusual)
                                    accuracy_bonus = value
                            elif mod_type == "ModifierType_Additionnel":
                                # Flat bonus: ModifierValue is a percentage (e.g., 12 means 12%)
                                # ModifierType_Additionnel means it's added directly
                                accuracy_bonus = value / 100.0
                            elif mod_type is None:
                                # ModifierType is None - check if value looks like a multiplier
                                if value > 1.0:
                                    # Looks like a multiplier (e.g., 1.0105), convert to flat
                                    accuracy_bonus = value - 1.0
                                else:
                                    # Assume it's a percentage (e.g., 1.05 means 1.05%)
                                    accuracy_bonus = value / 100.0
                            else:
                                # Unknown modifier type - check if value looks like a multiplier
                                if value > 1.0:
                                    # Looks like a multiplier, convert to flat
                                    accuracy_bonus = value - 1.0
                                else:
                                    # Assume it's a percentage
                                    accuracy_bonus = value / 100.0
                        except (ValueError, TypeError) as e:
                            print(f"Warning: Failed to parse accuracy bonus for {effect_name}: {e}")
                            pass
                
                # Look for TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor (reload speed bonus)
                elif effect_type == "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor":
                    modifier_value = effect.v.by_m("ModifierValue", None)
                    if modifier_value:
                        try:
                            # ModifierValue is a multiplier (e.g., 0.8 means 20% faster reload)
                            # ModifierType_Multiplicatif means it multiplies the time
                            reload_speed_multiplier = float(modifier_value.v)
                        except (ValueError, TypeError):
                            pass
            
            # Store the bonuses if there are any
            if accuracy_bonus > 0 or reload_speed_multiplier != 1.0:
                effect_bonuses[effect_name] = {
                    "accuracy_bonus": round(accuracy_bonus, 2),
                    "reload_speed_multiplier": reload_speed_multiplier,
                }
                
    except Exception as e:
        print(f"Warning: Failed to parse veterancy bonuses from EffetsSurUnite: {e}")
    
    return effect_bonuses


def parse_shock_bonuses(mod_src_path: Path) -> Dict[str, float]:
    """Parse shock bonuses from EffetsSurUnite.ndf (UnitEffect_Choc).
    
    Returns:
        Dictionary with shock bonus values:
        - "damage_multiplier": float (e.g., 1.15 for +15%)
        - "salvo_reload_multiplier": float (e.g., 0.85 for 15% faster)
        - "shot_time_multiplier": float (e.g., 0.85 for 15% faster)
        - "aim_time_multiplier": float (e.g., 0.85 for 15% faster)
    """
    ndf_path = "GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf"
    shock_bonuses: Dict[str, float] = {
        "damage_multiplier": 1.15,  # Default fallback values
        "salvo_reload_multiplier": 0.85,
        "shot_time_multiplier": 0.85,
        "aim_time_multiplier": 0.85,
    }
    
    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)
        
        for effect_row in parse_source:
            if not hasattr(effect_row, "namespace"):
                continue
            
            effect_name = effect_row.namespace
            
            # Look for UnitEffect_Choc
            if effect_name != "UnitEffect_Choc":
                continue
            
            # Parse effects to find bonuses
            effects_list = effect_row.v.by_m("EffectsDescriptors", None)
            if not effects_list:
                continue
            
            for effect in effects_list.v:
                if not isinstance(effect.v, ndf.model.Object):
                    continue
                
                effect_type = effect.v.type
                modifier_value = effect.v.by_m("ModifierValue", None)
                modifier_type = effect.v.by_m("ModifierType", None)
                
                if not modifier_value:
                    continue
                
                try:
                    value = float(modifier_value.v)
                    mod_type = strip_quotes(modifier_type.v) if modifier_type else None
                    
                    # TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor with ModifierType_Pourcentage
                    if effect_type == "TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor":
                        if mod_type == "ModifierType_Pourcentage":
                            # Value is percentage (e.g., 15 means +15%), convert to multiplier
                            shock_bonuses["damage_multiplier"] = 1.0 + (value / 100.0)
                    
                    # TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor with ModifierType_Multiplicatif
                    elif effect_type == "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor":
                        if mod_type == "ModifierType_Multiplicatif":
                            # Value is multiplier (e.g., 0.85 means 15% faster)
                            shock_bonuses["salvo_reload_multiplier"] = value
                    
                    # TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor with ModifierType_Pourcentage
                    elif effect_type == "TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor":
                        if mod_type == "ModifierType_Pourcentage":
                            # Value is percentage change (e.g., -15 means 15% faster)
                            # Convert to multiplier: if -15%, then multiplier = 1 - 0.15 = 0.85
                            if value < 0:
                                shock_bonuses["shot_time_multiplier"] = 1.0 + (value / 100.0)
                            else:
                                shock_bonuses["shot_time_multiplier"] = 1.0 + (value / 100.0)
                    
                    # TBonusWeaponAimtimeEffectDescriptor with ModifierType_Multiplicatif
                    elif effect_type == "TBonusWeaponAimtimeEffectDescriptor":
                        if mod_type == "ModifierType_Multiplicatif":
                            # Value is multiplier (e.g., 0.85 means 15% faster aiming)
                            shock_bonuses["aim_time_multiplier"] = value
                            
                except (ValueError, TypeError):
                    pass
            
            # Found UnitEffect_Choc, break
            break
                
    except Exception as e:
        print(f"Warning: Failed to parse shock bonuses from EffetsSurUnite: {e}")
    
    return shock_bonuses


def parse_shock_range(mod_src_path: Path) -> float:
    """Parse shock range from CapaciteList.ndf (Capacite_Choc RangeGRU).
    
    Returns:
        Shock range in meters (default 100.0 if not found)
    """
    ndf_path = "GameData/Generated/Gameplay/Gfx/CapaciteList.ndf"
    shock_range = 100.0  # Default fallback value
    
    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)
        
        for capacite_row in parse_source:
            if not hasattr(capacite_row, "namespace"):
                continue
            
            capacite_name = capacite_row.namespace
            
            # Look for Capacite_Choc
            if capacite_name != "Capacite_Choc":
                continue
            
            # Get RangeGRU value
            range_gru = capacite_row.v.by_m("RangeGRU", None)
            if range_gru:
                try:
                    shock_range = float(range_gru.v)
                except (ValueError, TypeError):
                    pass
            
            # Found Capacite_Choc, break
            break
                
    except Exception as e:
        print(f"Warning: Failed to parse shock range from CapaciteList: {e}")
    
    return shock_range


def parse_militia_bonuses(mod_src_path: Path) -> Dict[str, float]:
    """Parse militia bonuses from EffetsSurUnite.ndf (UnitEffect_militia).
    
    Returns:
        Dictionary with militia bonus values:
        - "reload_speed_multiplier": float (e.g., 1.20 means 20% slower reload)
        - "aim_time_multiplier": float (e.g., 1.20 means 20% slower aiming)
    """
    ndf_path = "GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf"
    militia_bonuses: Dict[str, float] = {
        "reload_speed_multiplier": 1.20,  # Default fallback values
        "aim_time_multiplier": 1.20,
    }
    
    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)
        
        for effect_row in parse_source:
            if not hasattr(effect_row, "namespace"):
                continue
            
            effect_name = effect_row.namespace
            
            # Look for UnitEffect_militia
            if effect_name != "UnitEffect_militia":
                continue
            
            # Parse effects to find bonuses
            effects_list = effect_row.v.by_m("EffectsDescriptors", None)
            if not effects_list:
                continue
            
            for effect in effects_list.v:
                if not isinstance(effect.v, ndf.model.Object):
                    continue
                
                effect_type = effect.v.type
                modifier_value = effect.v.by_m("ModifierValue", None)
                modifier_type = effect.v.by_m("ModifierType", None)
                
                if not modifier_value:
                    continue
                
                try:
                    value = float(modifier_value.v)
                    mod_type = strip_quotes(modifier_type.v) if modifier_type else None
                    
                    # TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor with ModifierType_Multiplicatif
                    if effect_type == "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor":
                        if mod_type == "ModifierType_Multiplicatif":
                            # Value is multiplier (e.g., 1.20 means 20% slower reload)
                            militia_bonuses["reload_speed_multiplier"] = value
                    
                    # TBonusWeaponAimtimeEffectDescriptor with ModifierType_Multiplicatif
                    elif effect_type == "TBonusWeaponAimtimeEffectDescriptor":
                        if mod_type == "ModifierType_Multiplicatif":
                            # Value is multiplier (e.g., 1.20 means 20% slower aiming)
                            militia_bonuses["aim_time_multiplier"] = value
                            
                except (ValueError, TypeError):
                    pass
            
            # Found UnitEffect_militia, break
            break
                
    except Exception as e:
        print(f"Warning: Failed to parse militia bonuses from EffetsSurUnite: {e}")
    
    return militia_bonuses


def apply_veterancy_bonuses_to_units(
    unit_data: Dict[str, Dict[str, Any]], 
    pack_to_effects_map: Dict[str, Dict[int, List[str]]],
    effect_bonuses: Dict[str, Dict[str, float]]
) -> None:
    """Apply veterancy bonuses to unit data based on their ExperienceLevelsPackDescriptor.
    
    Maps each unit's pack to the effects from ExperienceLevels.ndf, then looks up bonuses.
    """
    for unit_name, unit_info in unit_data.items():
        # Get the ExperienceLevelsPackDescriptor name from unit
        xp_pack_name = unit_info.get("experience_levels_pack", None)
        if not xp_pack_name:
            continue
        
        # Look up the pack in pack_to_effects_map
        if xp_pack_name not in pack_to_effects_map:
            continue
        
        level_effects_map = pack_to_effects_map[xp_pack_name]
        veterancy_accuracy_bonus_map: Dict[int, float] = {}
        veterancy_reload_speed_multiplier_map: Dict[int, float] = {}
        
        # For each level, find the effect and get its bonuses
        for level, effect_names in level_effects_map.items():
            # Find the first effect that has bonuses
            for effect_name in effect_names:
                if effect_name in effect_bonuses:
                    bonuses = effect_bonuses[effect_name]
                    veterancy_accuracy_bonus_map[level] = bonuses.get("accuracy_bonus", 0.0)
                    veterancy_reload_speed_multiplier_map[level] = bonuses.get("reload_speed_multiplier", 1.0)
                    break
        
        # Store veterancy bonuses for this unit
        unit_info["veterancy_accuracy_bonuses"] = veterancy_accuracy_bonus_map
        unit_info["veterancy_reload_speed_multipliers"] = veterancy_reload_speed_multiplier_map


def extract_unit_info(unit_row: Any) -> Dict[str, Any]:
    """Extract relevant information from a unit row."""
    unit_info = {
        "is_infantry": False,
        "tags": [],
        "unit_role": None,
        "display_name": None,
        "veterancy_pack": "simple_v3",  # Default to simple_v3 for infantry
        "available_veterancy_levels": [0, 1, 2, 3],  # Default 4 levels
        "has_shock_trait": False,  # Shock trait (_choc) from SpecialtiesList
        "has_militia_trait": False,  # Militia trait (militia) from TCapaciteModuleDescriptor
        "price": None,  # Command points price from TProductionModuleDescriptor
        "strength": None,  # Unit strength (HP) from TBaseDamageModuleDescriptor
    }
    
    try:
        modules_list = unit_row.v.by_m("ModulesDescriptors").v
        
        for module in modules_list:
            if not isinstance(module.v, ndf.model.Object):
                continue
            
            module_type = module.v.type
            
            if module_type == "TTagsModuleDescriptor":
                tagset = module.v.by_m("TagSet").v
                unit_info["tags"] = [strip_quotes(tag.v) for tag in tagset]
            
            elif module_type == "TUnitUIModuleDescriptor":
                # Extract display name
                name_token = module.v.by_m("NameToken", None)
                if name_token:
                    unit_info["display_name"] = strip_quotes(name_token.v)
                
                # Extract unit role
                unit_role = module.v.by_m("UnitRole", None)
                if unit_role:
                    unit_info["unit_role"] = strip_quotes(unit_role.v)
                
                # Extract SpecialtiesList to check for Shock trait (_choc)
                specialties_list = module.v.by_m("SpecialtiesList", None)
                if specialties_list:
                    specialties = [strip_quotes(spec.v) for spec in specialties_list.v]
                    if '_choc' in specialties:
                        unit_info["has_shock_trait"] = True
            
            # Check for ExperienceLevelsPack reference
            elif module_type == "TExperienceModuleDescriptor":
                xp_pack = module.v.by_m("ExperienceLevelsPackDescriptor", None)
                if xp_pack:
                    pack_name = strip_quotes(xp_pack.v)
                    # Remove ~/ prefix if present
                    if pack_name.startswith("~/"):
                        pack_name = pack_name[2:]
                    # Store the full pack name for lookup
                    unit_info["experience_levels_pack"] = pack_name
                    
                    # Also determine pack type from name for backwards compatibility
                    if "SF_v2" in pack_name or "_sf" in pack_name.lower():
                        unit_info["veterancy_pack"] = "SF_v2"
                    elif "artillery" in pack_name.lower():
                        unit_info["veterancy_pack"] = "artillery"
                    elif "helico" in pack_name.lower():
                        unit_info["veterancy_pack"] = "helico"
                    elif "avion" in pack_name.lower():
                        unit_info["veterancy_pack"] = "avion"
                    else:
                        unit_info["veterancy_pack"] = "simple_v3"
            
            # Extract strength from TBaseDamageModuleDescriptor
            elif module_type == "TBaseDamageModuleDescriptor":
                max_damages = module.v.by_m("MaxPhysicalDamages", None)
                if max_damages:
                    try:
                        unit_info["strength"] = int(max_damages.v)
                    except (ValueError, TypeError, AttributeError):
                        pass
            
            # Extract price from TProductionModuleDescriptor
            elif module_type == "TProductionModuleDescriptor":
                production_resources = module.v.by_m("ProductionRessourcesNeeded", None)
                if production_resources:
                    # ProductionRessourcesNeeded is a MAP
                    # Look for Resource_CommandPoints entry using by_k()
                    try:
                        cmd_points_key = "$/GFX/Resources/Resource_CommandPoints"
                        cmd_points_value = production_resources.v.by_k(cmd_points_key)
                        if cmd_points_value:
                            try:
                                unit_info["price"] = int(cmd_points_value.v)
                            except (ValueError, TypeError, AttributeError):
                                pass
                    except (AttributeError, TypeError, KeyError):
                        pass
            
            # Check for militia capacity from TCapaciteModuleDescriptor
            elif module_type == "TCapaciteModuleDescriptor":
                default_skill_list = module.v.by_m("DefaultSkillList", None)
                if default_skill_list:
                    try:
                        for skill in default_skill_list.v:
                            skill_ref = strip_quotes(skill.v)
                            # Check if skill reference contains Capacite_militia
                            if "Capacite_militia" in skill_ref:
                                unit_info["has_militia_trait"] = True
                                break
                    except (AttributeError, TypeError, ValueError):
                        pass
        
        # Determine veterancy pack from tags if not found in module
        if unit_info["veterancy_pack"] == "simple_v3":
            tags = unit_info.get("tags", [])
            # Check if unit has SF tags
            if any("_sf" in tag.lower() or "sf" in tag.lower() for tag in tags):
                unit_info["veterancy_pack"] = "SF_v2"
        
        # Set available veterancy levels based on pack type
        # All infantry packs have 4 levels (0-3)
        unit_info["available_veterancy_levels"] = [0, 1, 2, 3]
                    
    except Exception as e:
        print(f"Error extracting unit info: {e}")
        return {}
    
    return unit_info


def parse_weapon_descriptors(mod_src_path: Path) -> Dict[str, Dict[str, Any]]:
    """Parse weapon descriptors from WeaponDescriptor.ndf.
    
    Returns:
        Dictionary mapping weapon descriptor names to weapon data
    """
    weapon_data = {}
    ndf_path = "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf"
    
    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        source = mod.parse_src(ndf_path)
        
        for weapon_descr in source:
            if not hasattr(weapon_descr, "namespace"):
                continue
            
            weapon_name = weapon_descr.namespace
            if not weapon_name.startswith("WeaponDescriptor_"):
                continue
            
            try:
                turret_data = _gather_turret_data(weapon_descr)
                salvo_data = _gather_salvo_data(weapon_descr)
                
                if turret_data or salvo_data:
                    weapon_data[weapon_name] = {
                        "turrets": turret_data,
                        "salvos": salvo_data,
                    }
            except Exception as e:
                print(f"Failed to gather data for {weapon_name}: {e}")
                continue
                
    except Exception as e:
        print(f"Error parsing weapon descriptors: {e}")
        raise
    
    return weapon_data


def _gather_turret_data(weapon_descr: Any) -> Dict[str, Any]:
    """Gather turret and weapon data from a weapon descriptor."""
    turret_data = {}
    
    try:
        turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    except Exception:
        return turret_data
    
    salvo_data = _gather_salvo_data(weapon_descr)
    
    for turret in turret_list:
        if not is_valid_turret(turret.v):
            continue
        
        try:
            yul_bone = int(turret.v.by_m("YulBoneOrdinal").v)
            turret_data[str(turret.index)] = {
                "yul_bone": yul_bone,
                "weapons": _gather_mounted_weapons(turret, salvo_data),
            }
        except Exception as e:
            print(f"Failed to gather data for turret: {e}")
            continue
    
    return turret_data


def _gather_mounted_weapons(turret: Any, salvo_data: Dict[str, int]) -> Dict[str, Any]:
    """Gather mounted weapon data from a turret."""
    weapon_data = {}
    
    try:
        mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList").v
    except Exception:
        return weapon_data
    
    for weapon in mounted_wpns:
        if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
            continue
        
        try:
            ammo_val = weapon.v.by_m("Ammunition").v
            if not ammo_val.startswith("$/GFX/Weapon/Ammo_"):
                continue
            
            ammo_name = ammo_val.split("$/GFX/Weapon/Ammo_", 1)[1]
            salvo_index = int(weapon.v.by_m("SalvoStockIndex").v)
            weapon_quantity = int(weapon.v.by_m("NbWeapons").v)
            
            weapon_data[ammo_name] = {
                "salvo_index": salvo_index,
                "salvos": salvo_data.get(str(salvo_index), 0),
                "quantity": weapon_quantity,
            }
        except Exception as e:
            print(f"Failed to gather data for weapon: {e}")
            continue
    
    return weapon_data


def _gather_salvo_data(weapon_descr: Any) -> Dict[str, int]:
    """Gather salvo data from a weapon descriptor."""
    try:
        salves_list = weapon_descr.v.by_m("Salves").v
        return {str(salvo.index): int(salvo.v) for salvo in salves_list}
    except Exception:
        return {}


def parse_ammunition_properties(mod_src_path: Path) -> Dict[str, Dict[str, Any]]:
    """Parse ammunition properties from Ammunition.ndf.
    
    Returns:
        Dictionary mapping ammunition names to their properties
    """
    ammo_data = {}
    ndf_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
    
    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        source = mod.parse_src(ndf_path)
        
        for ammo_descr in source:
            if not hasattr(ammo_descr, "namespace"):
                continue
            
            ammo_name = ammo_descr.namespace.replace("Ammo_", "")
            properties = {}
            
            try:
                # Extract damage family from Arme
                arme_obj = ammo_descr.v.by_m("Arme", None)
                if arme_obj:
                    damage_family = arme_obj.v.by_m("Family", None)
                    if damage_family:
                        properties["damage_family"] = strip_quotes(damage_family.v)
                
                # Extract Idling accuracy
                hit_roll = ammo_descr.v.by_m("HitRollRuleDescriptor", None)
                if hit_roll:
                    modifiers = hit_roll.v.by_m("BaseHitValueModifiers", None)
                    if modifiers and len(modifiers.v) > 1:
                        idling_val = modifiers.v[1].v
                        if isinstance(idling_val, tuple) and len(idling_val) > 1:
                            # Second element is the Idling value (0-100)
                            properties["idling"] = float(idling_val[1]) / 100.0  # Convert 0-100 to 0.0-1.0
                        elif isinstance(idling_val, (int, float)):
                            properties["idling"] = float(idling_val) / 100.0
                
                # Extract parent member properties
                membr = ammo_descr.v.by_m
                
                max_range = membr("MaximumRangeGRU", None)
                if max_range:
                    properties["max_range"] = float(max_range.v)
                
                physical_damages = membr("PhysicalDamages", None)
                if physical_damages:
                    properties["physical_damages"] = float(physical_damages.v)
                
                suppress_damages = membr("SuppressDamages", None)
                if suppress_damages:
                    properties["suppress_damages"] = float(suppress_damages.v)
                
                nb_tir_par_salves = membr("NbTirParSalves", None)
                if nb_tir_par_salves:
                    properties["nb_tir_par_salves"] = int(nb_tir_par_salves.v)
                
                time_between_salvos = membr("TimeBetweenTwoSalvos", None)
                if time_between_salvos:
                    properties["time_between_salvos"] = float(time_between_salvos.v)
                
                time_between_shots = membr("TimeBetweenTwoShots", None)
                if time_between_shots:
                    properties["time_between_shots"] = float(time_between_shots.v)
                
                aiming_time = membr("AimingTime", None)
                if aiming_time:
                    properties["aiming_time"] = float(aiming_time.v)
                
                affichage_munition_par_salve = membr("AffichageMunitionParSalve", None)
                if affichage_munition_par_salve:
                    properties["affichage_munition_par_salve"] = float(affichage_munition_par_salve.v)
                
                if properties:
                    ammo_data[ammo_name] = properties
                    
            except Exception as e:
                print(f"Error extracting properties for {ammo_name}: {e}")
                continue
                
    except Exception as e:
        print(f"Error parsing ammunition: {e}")
        raise
    
    return ammo_data

