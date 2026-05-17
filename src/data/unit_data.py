import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from src import ndf
from src.data.ammo_data import get_vanilla_renames
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import (
    get_modules_list,  # noqa
    is_obj_type,
    is_valid_turret,
    strip_quotes,
)

logger = setup_logger("unit_data")

# Engine walks UpgradeFrom ancestry; chains longer than this trigger "Infinite hierarchy" errors in-game.
UPGRADE_FROM_MAX_CHAIN_UNIT_COUNT = 10


def gather_unit_data(mod_src_path: Path) -> Dict[str, Any]:
    """Gather unit data from source files."""
    logger.info("Gathering unit data from UniteDescriptor.ndf")
    logger.info(f"Source path: {mod_src_path}")

    unit_data = {}
    ndf_path = "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"

    try:
        # Just parsing input, no output needed
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)

        for unit_row in parse_source:
            # Skip non-unit entries
            if not hasattr(unit_row, "namespace"):
                continue

            # Get unit name without prefix
            unit_name = unit_row.namespace.replace("Descriptor_Unit_", "")

            # Extract unit data
            unit_info = extract_unit_info(unit_row)
            if unit_info:
                unit_data[unit_name] = unit_info
                logger.debug(f"Gathered data for unit: {unit_name}")
            else:
                logger.debug(f"No data gathered for unit: {unit_name}")

    except Exception as e:
        logger.error(f"Error gathering unit data: {str(e)}")
        raise

    logger.info(f"Gathered data for {len(unit_data)} units")
    if not unit_data:
        logger.warning("No unit data was gathered!")

    return unit_data


def gather_ui_texture_reference(mod_src_path: Path) -> Dict[str, List[str]]:
    """Collect distinct UI / tactical-label texture strings from vanilla UniteDescriptor.ndf.

    Returns JSON-serializable dict with sorted unique lists per field (case-sensitive strings).
    """
    menu_icons: Set[str] = set()
    tactical_identified: Set[str] = set()
    tactical_unidentified: Set[str] = set()

    ndf_path = "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"
    logger.info("Gathering UI texture reference from UniteDescriptor.ndf")

    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)

        for unit_row in parse_source:
            if not hasattr(unit_row, "namespace"):
                continue

            modules_list = unit_row.v.by_m("ModulesDescriptors").v

            for module in modules_list:
                if not isinstance(module.v, ndf.model.Object):
                    continue

                module_type = module.v.type

                if module_type == "TTacticalLabelModuleDescriptor":
                    id_tex = module.v.by_m("IdentifiedTexture", False)
                    _accumulate_buck_texture_values(tactical_identified, id_tex)
                    unid_tex = module.v.by_m("UnidentifiedTexture", False)
                    _accumulate_buck_texture_values(tactical_unidentified, unid_tex)

                elif module_type == "TUnitUIModuleDescriptor":
                    menu = module.v.by_m("MenuIconTexture", False)
                    if menu is not None and menu.v:
                        s = strip_quotes(menu.v)
                        if s:
                            menu_icons.add(s)

        logger.info(
            "UI texture reference: menu=%s tactical_id=%s tactical_unid=%s",
            len(menu_icons),
            len(tactical_identified),
            len(tactical_unidentified),
        )

        return {
            "menu_icon_textures": sorted(menu_icons),
            "tactical_label_identified_textures": sorted(tactical_identified),
            "tactical_label_unidentified_textures": sorted(tactical_unidentified),
        }

    except Exception as e:
        logger.error("Error gathering UI texture reference: %s", e)
        raise


def _accumulate_buck_texture_values(target: Set[str], buck_member_row: Any) -> None:
    """Read string entries from IdentifiedTexture/UnidentifiedTexture TBUCK *Values* list."""
    if buck_member_row is None:
        return
    try:
        vals_wrap = buck_member_row.v.by_m("Values", False)
        if vals_wrap is None or not vals_wrap.v:
            return
        for entry in vals_wrap.v:
            raw = entry.v if hasattr(entry, "v") else entry
            s = strip_quotes(raw)
            if s:
                target.add(s)
    except Exception as ex:
        logger.debug("Could not parse buck texture Values: %s", ex)


def extract_unit_info(unit_row: Any) -> Dict[str, Any]:
    """Extract relevant information from a unit row."""
    try:
        modules_list = unit_row.v.by_m("ModulesDescriptors").v

        # Initialize default values
        unit_info = {
            "is_supply_unit": False,
            "is_helo_unit": False,
            "is_hmg_team": False,
            "is_at_team": False,
            "is_towable": False,
        }

        # Get unit name for context
        unit_name = unit_row.namespace.split("Descriptor_Unit_")[-1] if hasattr(unit_row, "namespace") else "Unknown"

        if "hmgteam" in unit_name.lower():
            unit_info["is_hmg_team"] = True
        elif "atteam" in unit_name.lower():
            unit_info["is_at_team"] = True

        for module in modules_list:

            if not isinstance(module.v, ndf.model.Object):
                continue

            module_type = module.v.type
            
            if module_type == "THelicopterMovementModuleDescriptor":
                unit_info["is_helo_unit"] = True
                continue

            if module_type == "TProductionModuleDescriptor":
                unit_info.update(_extract_production_data(module))

            elif module_type == "TTagsModuleDescriptor":
                unit_info.update(_extract_tags_data(module))

            elif module_type == "TUnitUIModuleDescriptor":
                unit_info.update(_extract_ui_data(module))

            elif module_type == "TBaseDamageModuleDescriptor":
                unit_info["strength"] = _extract_damage_data(module)

            elif module_type == "TDamageModuleDescriptor":
                unit_info["armor"] = _extract_armor_data(module)

            elif module_type == "TTransportableModuleDescriptor":
                is_towable = module.v.by_m("IsTowable", False)
                if is_towable is not None and is_towable.v == "True":
                    unit_info["is_towable"] = True

            elif module_type == "TSupplyModuleDescriptor":
                unit_info["is_supply_unit"] = True

            elif module_type == "AirplaneMovementDescriptor":
                airplane_movement = _extract_airplane_movement_data(module)
                unit_info["airplane_movement"] = airplane_movement
                if "AttackStrategiesDescriptorsSortedByPriority" in airplane_movement:
                    unit_info["attack_strategies"] = airplane_movement["AttackStrategiesDescriptorsSortedByPriority"]

            elif module_type == "TVisibilityModuleDescriptor":
                unit_info["visibility"] = _extract_stealth_data(module)

            elif module_type == "TScannerConfigurationDescriptor":
                unit_info["optics"] = _extract_optics_data(module, unit_name)

            elif module_type == "TCapaciteModuleDescriptor":
                skills = _extract_skills_data(module)
                if skills:
                    unit_info["skills"] = skills
                    logger.debug(f"Extracted skills: {skills}")

        return unit_info
    except Exception as e:
        logger.error(f"Error extracting unit info: {str(e)}")
        return {}


def _extract_skills_data(module: Any) -> List[str]:
    """Extract skills data from a module selector."""
    try:
        default_skill_list = module.v.by_m("DefaultSkillList").v
        if default_skill_list:
            return [skill.v.split("$/GFX/EffectCapacity/Capacite_")[1] for skill in default_skill_list]
    except Exception as e:
        logger.error(f"Error extracting skills data: {str(e)}")
        return []


def _extract_production_data(module: Any) -> Dict[str, Any]:
    """Extract production-related data (command points, etc.)."""
    data = {}
    try:
        resources = module.v.by_m("ProductionRessourcesNeeded", None)
        if resources is not None:
            for row in resources.v:
                # Handle key which might be a string or wrapped value
                resource_type = row.key.v if hasattr(row.key, "v") else row.key

                # Handle value which might be a string or wrapped value
                resource_value = row.value.v if hasattr(row.value, "v") else row.value
                resource_value = int(resource_value)

                if resource_type == "$/GFX/Resources/Resource_CommandPoints":
                    data["command_points"] = resource_value
                elif resource_type == "$/GFX/Resources/Resource_Tickets":
                    data["tickets"] = resource_value

            logger.debug(f"Extracted production data: {data}")
        else:
            logger.debug("No production resources found")

    except Exception as e:
        logger.debug(f"Error extracting production data for {module.namespace}: {str(e)}")
    return data


def _extract_tags_data(module: Any) -> Dict[str, Any]:
    """Extract unit tags data."""
    data = {}
    try:
        tagset = module.v.by_m("TagSet").v
        data["tags"] = [strip_quotes(tag.v) for tag in tagset]
    except Exception as e:
        logger.warning(f"Failed to extract tags data: {str(e)}")
    return data


def _extract_ui_data(module: Any) -> Dict[str, Any]:
    """Extract UI-related data (specialties, textures, etc.)."""
    data = {}
    try:
        # Get specialties
        specialties = module.v.by_m("SpecialtiesList").v
        if specialties:
            data["specialties"] = [strip_quotes(spec.v) for spec in specialties]
            
        name_token = module.v.by_m("NameToken").v
        if name_token:
            data["name_token"] = strip_quotes(name_token)

        # Get menu icon texture
        texture = module.v.by_m("MenuIconTexture").v
        if texture:
            data["menu_icon"] = strip_quotes(texture)

        # Get UpgradeFromUnit if present
        upgrade_from = module.v.by_m("UpgradeFromUnit", None)
        if upgrade_from is not None:
            # Extract unit name from "Descriptor_Unit_UnitName" format
            upgrade_from_value = upgrade_from.v
            if upgrade_from_value.startswith("Descriptor_Unit_"):
                data["upgrade_from_unit"] = upgrade_from_value.replace("Descriptor_Unit_", "")
            else:
                data["upgrade_from_unit"] = upgrade_from_value

    except Exception as e:
        logger.warning(f"Failed to extract UI data: {str(e)}")
    return data


def _extract_damage_data(module: Any) -> Dict[str, Any]:
    """Extract damage data from damage module."""
    data = {}
    try:
        data = int(module.v.by_m("MaxPhysicalDamages").v)
    except Exception as e:
        logger.warning(f"Failed to extract damage data: {str(e)}")
    return data


def _extract_armor_data(module: Any) -> Dict[str, Any]:
    """Extract armor data from damage module."""
    try:
        blindage = module.v.by_m("BlindageProperties").v
        return {
            "front": {
                "family": blindage.by_m("ResistanceFront").v.by_m("Family").v,
                "index": blindage.by_m("ResistanceFront").v.by_m("Index").v,
            },
            "sides": {
                "family": blindage.by_m("ResistanceSides").v.by_m("Family").v,
                "index": blindage.by_m("ResistanceSides").v.by_m("Index").v,
            },
            "rear": {
                "family": blindage.by_m("ResistanceRear").v.by_m("Family").v,
                "index": blindage.by_m("ResistanceRear").v.by_m("Index").v,
            },
            "top": {
                "family": blindage.by_m("ResistanceTop").v.by_m("Family").v,
                "index": blindage.by_m("ResistanceTop").v.by_m("Index").v,
            },
        }
    except Exception as e:
        logger.error(f"Error extracting armor data: {str(e)}")
        return {}


def _extract_stealth_data(module: Any) -> Dict[str, Any]:
    """Extract stealth data."""
    try:
        stealth_data = {}

        # Get base module values
        stealth = module.v.by_m("UnitConcealmentBonus", None)

        if stealth is not None:
            stealth_data["stealth_bonus"] = float(stealth.v)

        if stealth_data:
            logger.debug(f"Extracted visibility data: {stealth_data}")
        else:
            logger.debug("No visibility data found")

        return stealth_data

    except Exception as e:
        logger.debug(f"Error extracting visibility data: {str(e)}")
        return {}


def _extract_optics_data(module: Any, unit_name: str) -> Dict[str, Any]:
    """Extract optics configuration data."""
    try:
        optics_data = {}

        logger.debug(f"Extracting optics data for unit: {unit_name}")

        ranges_map = module.v.by_m("VisionRangesGRU", None)
        ground = ranges_map.v.by_k("EVisionUnitType/Standard", None)
        if ground is not None:
            optics_data["ground_range"] = float(ground.v)
            logger.debug(f"Found ground range: {optics_data['ground_range']}")

        strengths_map = module.v.by_m("OpticalStrengths", None)
        optics_data["strengths"] = {}
        for row in strengths_map.v:
            try:
                key = row.key.v if hasattr(row.key, "v") else row.key
                value = float(row.value.v if hasattr(row.value, "v") else row.value)
                optics_data["strengths"][key] = value
                logger.debug(f"Found strength: {key}={value}")
            except Exception as e:
                logger.debug(f"Error processing strength row for {unit_name}: {str(e)}")
                continue

        # Always return at least an empty dict
        logger.debug(f"Final optics data: {optics_data}")
        return optics_data

    except Exception as e:
        logger.error(f"Error extracting optics data for {unit_name}: {str(e)}")
        return {}


def gather_weapon_data(mod_src_path: Path) -> Dict[str, Any]:
    """Gather weapon data from WeaponDescriptor.ndf."""
    logger.info("Gathering weapon data from WeaponDescriptor.ndf")

    weapon_data = {}

    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        ammo_ndf_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
        ndf_path = "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf"
        weapon_renames = get_vanilla_renames(mod, ammo_ndf_path)
        logger.debug(f"Reading weapon data from: {mod_src_path / ndf_path}")
        source = mod.parse_src(ndf_path)

        weapon_count = 0
        for weapon_descr in source:
            weapon_count += 1
            if not hasattr(weapon_descr, "namespace"):
                logger.debug("Found entry without namespace")
                continue

            weapon_name = weapon_descr.namespace
            if not weapon_name.startswith("WeaponDescriptor_"):
                logger.debug(f"Skipping non-weapon entry: {weapon_name}")
                continue

            logger.debug(f"Processing weapon: {weapon_name}")
            try:
                turret_data = _gather_turret_data(weapon_descr)
                salvo_data = _gather_salvo_data(weapon_descr)
                location_data = _gather_weapon_locations(weapon_descr)
                index_data = _gather_weapon_indices(weapon_descr)
                mapping_data = _gather_salvo_mapping(weapon_descr)

                if any([turret_data, salvo_data, location_data, index_data, mapping_data]):
                    salves_list = _gather_salves_list(weapon_descr)
                    weapon_data[weapon_name] = {
                        "turrets": turret_data,
                        "salves_list": salves_list,
                        "weapon_locations": location_data,
                        "weapon_indices": index_data,
                        "salvo_mapping": mapping_data,
                    }
                    # Add rename information if this weapon gets renamed
                    base_name = weapon_name.replace("WeaponDescriptor_", "")
                    if base_name in weapon_renames:
                        weapon_data[weapon_name]["rename"] = weapon_renames[base_name]  # noqa
                        logger.debug(f"Added rename info for {weapon_name}: {weapon_renames[base_name]}")
                    logger.debug(f"Added data for {weapon_name}")
                else:
                    logger.warning(f"No data gathered for {weapon_name}")

            except Exception as e:
                logger.error(f"Failed to gather data for {weapon_name}: {str(e)}")
                continue

        logger.debug(f"Processed {weapon_count} entries in file")

    except Exception as e:
        logger.error(f"Failed to parse weapon file: {str(e)}")
        return weapon_data

    logger.info(f"Gathered data for {len(weapon_data)} weapons")
    return weapon_data


def _gather_turret_data(weapon_descr: Any) -> Dict[str, Any]:
    """Gather turret and weapon data from a weapon descriptor."""
    turret_data = {}

    salvo_data = _gather_salvo_data(weapon_descr)
    # turret_data["salvos"] = salvo_data

    try:
        turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    except Exception:  # noqa
        logger.warning(f"No TurretDescriptorList found in {weapon_descr.namespace}")
        return turret_data

    for turret in turret_list:
        if not is_valid_turret(turret.v):
            continue
        # is_dive_bomb = False
        # if turret.v.type == "TTurretBombardierDescriptor":
        #     if turret.v.by_m("FlyingAltitude")

        try:
            yul_bone = int(turret.v.by_m("YulBoneOrdinal").v)
            turret_data[str(turret.index)] = {
                "yul_bone": yul_bone,
                "weapons": _gather_mounted_weapons(turret, salvo_data),
            }
        except Exception as e:
            logger.warning(f"Failed to gather data for turret in {weapon_descr.namespace}: {str(e)}")
            continue
    return turret_data


def _gather_mounted_weapons(turret: Any, salvo_data: Dict[str, int]) -> Dict[str, Any]:
    """Gather mounted weapon data from a turret."""
    weapon_data = {}

    try:
        mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList").v
    except Exception:  # noqa
        logger.warning("No MountedWeaponDescriptorList found")
        return weapon_data

    for weapon in mounted_wpns:
        if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
            continue

        try:
            ammo_val = weapon.v.by_m("Ammunition").v
            if not ammo_val.startswith("$/GFX/Weapon/Ammo_"):
                continue

            ammo_name = ammo_val.split("$/GFX/Weapon/Ammo_", 1)[1]
            salvo_index = int(weapon.v.by_m("AmmoBoxIndex").v)
            weapon_quantity = int(weapon.v.by_m("NbWeapons").v)

            shoot_data_row = weapon.v.by_m("WeaponShootDataPropertyName", False)
            if shoot_data_row is None:
                shoot_data = []
            else:
                raw = shoot_data_row.v
                if isinstance(raw, str):
                    shoot_data = [strip_quotes(raw)]
                else:
                    shoot_data = [strip_quotes(item.v) for item in raw]

            handheld_row = weapon.v.by_m("HandheldEquipmentKey", False)
            handheld = strip_quotes(handheld_row.v) if handheld_row is not None else None

            active_row = weapon.v.by_m("WeaponActiveAndCanShootPropertyName", False)
            active = strip_quotes(active_row.v) if active_row is not None else None

            ignored_row = weapon.v.by_m("WeaponIgnoredPropertyName", False)
            ignored = strip_quotes(ignored_row.v) if ignored_row is not None else None

            animate_row = weapon.v.by_m("AnimateOnlyOneSoldier", False)
            animate_value = animate_row.v if animate_row is not None else None
            if isinstance(animate_value, str):
                animate_value = animate_value.strip().lower() in ("true", "'true'", '"true"')
            elif animate_value is None:
                pass
            else:
                animate_value = bool(animate_value)

            weapon_data[ammo_name] = {
                "salvo_index": salvo_index,
                "salves": salvo_data[str(salvo_index)],
                "quantity": weapon_quantity,
                "regex_quantity": _get_regex_weapon_quantity(ammo_name),
                "mounted_index": int(weapon.index),
                "handheld_equipment_key": handheld,
                "weapon_shoot_data_property_name": shoot_data,
                "weapon_active_and_can_shoot_property_name": active,
                "weapon_ignored_property_name": ignored,
                "animate_only_one_soldier": animate_value,
            }
        except Exception as e:
            logger.warning(f"Failed to gather data for weapon: {str(e)}")
            continue
    return weapon_data


def _gather_salvo_data(weapon_descr: Any) -> Dict[str, int]:
    """Gather salvo data from a weapon descriptor."""
    try:
        salves_list = weapon_descr.v.by_m("Salves").v
        return {str(salvo.index): int(salvo.v) for salvo in salves_list}
    except Exception:  # noqa
        logger.warning(f"Failed to gather salvo data for {weapon_descr.namespace}")
        return {}


def _gather_salves_list(weapon_descr: Any) -> List[int]:
    """Return the Salves list as a flat ordered list of ints (index = list position)."""
    try:
        salves_list = weapon_descr.v.by_m("Salves").v
        return [int(salvo.v) for salvo in salves_list]
    except Exception:  # noqa
        logger.warning(f"Failed to gather salves list for {weapon_descr.namespace}")
        return []


def _get_regex_weapon_quantity(ammo_name: str) -> int:
    """Extract quantity from weapon name if present."""
    pattern = r".*?_x(\d+)$"
    match = re.match(pattern, ammo_name)
    return int(match.group(1)) if match else 1


def _gather_weapon_indices(weapon_descr: Any) -> Dict[str, List[int]]:
    """Pre-compute weapon to salvo index mapping."""
    weapon_indices = {}

    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(turret.v):
            continue

        for weapon in turret.v.by_m("MountedWeaponDescriptorList").v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue

            ammo = weapon.v.by_m("Ammunition").v.split("$/GFX/Weapon/Ammo_", 1)[1]
            # base_name = ammo.split('_x', 1)[0]

            if ammo not in weapon_indices:
                weapon_indices[ammo] = []

            weapon_indices[ammo].append(int(weapon.v.by_m("AmmoBoxIndex").v))

    return weapon_indices


def _gather_salvo_mapping(weapon_descr: Any) -> Dict[Any, Any]:
    """Pre-compute weapon to salvo mapping."""
    salvo_mapping = {}

    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(turret.v):
            continue

        for weapon in turret.v.by_m("MountedWeaponDescriptorList").v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue

            ammo = weapon.v.by_m("Ammunition").v.split("$/GFX/Weapon/Ammo_", 1)[1]
            # base_name = ammo.split('_x', 1)[0]
            index = int(weapon.v.by_m("AmmoBoxIndex").v)

            # Always store indices as a list for consistency
            if ammo not in salvo_mapping:
                salvo_mapping[ammo] = []
            salvo_mapping[ammo].append(index)

    return salvo_mapping


def _gather_weapon_locations(weapon_descr: Any) -> Dict[Any, Any]:
    """Gather locations of all weapons in the descriptor.

    Returns:
        Dict mapping weapon names to their location data:
        {
            "weapon_name": {
                "turret_index": int,
                "mounted_index": int,
                "salvo_index": int
            }
        }
    """
    weapon_locations = {}

    for i, turret in enumerate(weapon_descr.v.by_member("TurretDescriptorList").v, start=0):
        if not is_valid_turret(turret.v):
            continue

        for weapon in turret.v.by_m("MountedWeaponDescriptorList").v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue

            mounted_index = weapon.index
            ammo = weapon.v.by_m("Ammunition").v.split("$/GFX/Weapon/Ammo_", 1)[1]
            # base_name = ammo.split('_x', 1)[0]

            # Instead of overwriting, append to a list for each ammo entry
            if ammo not in weapon_locations:
                weapon_locations[ammo] = []  # Initialize a list if it doesn't exist

            weapon_locations[ammo].append(
                {
                    "turret_index": i,
                    "mounted_index": mounted_index,
                    "salvo_index": int(weapon.v.by_m("AmmoBoxIndex").v),
                }
            )

    return weapon_locations


def _extract_airplane_movement_data(module: Any) -> Dict[str, Any]:
    """Extract all values from an AirplaneMovementDescriptor module.

    Keys are the raw NDF member names so the data is directly comparable
    to airplane_movement edit specs (see unite_descriptor/unitedescriptor.py).
    """
    data: Dict[str, Any] = {}

    scalar_members = (
        "AltitudeGRU",
        "AltitudeMinGRU",
        "SpeedInKmph",
        "AgilityRadiusGRU",
        "PitchAngleDegree",
        "RollAngleDegree",
        "RollSpeedDegreePerSecond",
        "EvacAngleDegree",
    )
    for member in scalar_members:
        row = module.v.by_m(member, False)
        if row is None:
            continue
        raw = row.v
        try:
            data[member] = int(raw)
        except (TypeError, ValueError):
            try:
                data[member] = float(raw)
            except (TypeError, ValueError):
                logger.warning(f"AirplaneMovementDescriptor.{member} has non-numeric value: {raw!r}")
                data[member] = raw

    strategies_row = module.v.by_m("AttackStrategiesDescriptorsSortedByPriority", False)
    if strategies_row is not None:
        data["AttackStrategiesDescriptorsSortedByPriority"] = [strategy.v for strategy in strategies_row.v]

    return data


def _detect_circular_chains(forward_mapping: Dict[str, str]) -> List[List[str]]:
    """Detect circular chains in the forward mapping.
    
    A circular chain occurs when following upgrade relationships leads back to a unit
    that was already visited in the chain.
    
    Example:
        If UnitA upgrades from UnitB, UnitB upgrades from UnitC, and UnitC upgrades from UnitA,
        this creates a circular chain: [UnitA, UnitB, UnitC, UnitA]
    
    Args:
        forward_mapping: Dictionary mapping unit names to their UpgradeFromUnit values
        
    Returns:
        List of circular chains, where each chain is a list of unit names forming the cycle
    """
    circular_chains = []
    visited = set()
    rec_stack = set()
    
    def find_cycle(unit: str, path: List[str]) -> None:
        """DFS to find cycles starting from a unit."""
        if unit in rec_stack:
            # Found a cycle - extract the cycle portion
            cycle_start = path.index(unit)
            cycle = path[cycle_start:] + [unit]
            # Only add if we haven't seen this exact cycle before
            if cycle not in circular_chains:
                circular_chains.append(cycle)
            return
        
        if unit in visited:
            return
        
        visited.add(unit)
        rec_stack.add(unit)
        path.append(unit)
        
        # Follow the upgrade relationship
        if unit in forward_mapping:
            upgrade_from = forward_mapping[unit]
            # Follow the chain - upgrade_from might not be in forward_mapping (could be base unit)
            # but we still want to detect if it creates a cycle back to something in our path
            if upgrade_from in rec_stack:
                # Found a cycle back to upgrade_from
                cycle_start = path.index(upgrade_from)
                cycle = path[cycle_start:] + [upgrade_from]
                if cycle not in circular_chains:
                    circular_chains.append(cycle)
            elif upgrade_from not in visited:
                # Continue DFS
                find_cycle(upgrade_from, path.copy())
        
        rec_stack.remove(unit)
    
    # Check all units in the forward mapping
    for unit in forward_mapping.keys():
        if unit not in visited:
            find_cycle(unit, [])
    
    return circular_chains


def _upgrade_parent_chain(
    unit: str,
    forward_mapping: Dict[str, str],
) -> List[str]:
    """Follow UpgradeFrom pointers (child -> immediate parent tier) until a base tier or repeated node.

    Uses forward_mapping: unit_with_upgrade_parent -> immediate_parent_name.
    """
    chain = []
    seen = set()
    cur: Optional[str] = unit
    while cur is not None:
        if cur in seen:
            break
        seen.add(cur)
        chain.append(cur)
        cur = forward_mapping.get(cur)
        if len(chain) > 800:
            logger.warning("_upgrade_parent_chain aborted at depth 800 (possible bug or cycle)")
            break
    return chain


def _detect_upgrade_chains_exceeding_max_length(
    forward_mapping: Dict[str, str],
    max_units: int,
) -> List[List[str]]:
    """Return offending ancestries (`child -> … -> oldest tier`), pruning strict suffix overlaps.

    When linear upgrade lines share one ancestry, only the deepest start produces the maximal path;
    shorter starts on the same line report suffix paths which would duplicate errors.
    """
    candidates: List[List[str]] = []
    seen_tuples: Set[tuple[str, ...]] = set()
    for start in sorted(forward_mapping.keys()):
        chain = _upgrade_parent_chain(start, forward_mapping)
        if len(chain) <= max_units:
            continue
        tup = tuple(chain)
        if tup in seen_tuples:
            continue
        seen_tuples.add(tup)
        candidates.append(chain)
    candidates.sort(key=len, reverse=True)
    pruned: List[List[str]] = []
    for ch in candidates:
        superset_exists = False
        for longer in pruned:
            if len(longer) > len(ch) and longer[len(longer) - len(ch) :] == ch:
                superset_exists = True
                break
        if not superset_exists:
            pruned.append(ch)
    return sorted(pruned, key=len, reverse=True)


def validate_upgrade_forward_mapping_chain_lengths(
    forward_mapping: Dict[str, str],
    *,
    max_units: int = UPGRADE_FROM_MAX_CHAIN_UNIT_COUNT,
) -> None:
    """Raise ValueError if any upgrade ancestry exceeds the engine limit."""
    offending = _detect_upgrade_chains_exceeding_max_length(forward_mapping, max_units)
    if not offending:
        return
    lines = []
    for chain in offending:
        lines.append(f"  ({len(chain)} units) {' -> '.join(chain)}")
    raise ValueError(
        f"UpgradeFrom hierarchy exceeds WARNO engine limit ({max_units} units per ancestry path).\n"
        + f"Found {len(offending)} path(s):\n"
        + "\n".join(lines),
    )


def _build_upgrade_chains(forward_mapping: Dict[str, str]) -> Dict[str, Any]:
    """Build upgrade chains from a forward mapping (unit -> upgrade_from).
    
    Groups units into chains where the base unit (lowest in chain) maps to
    a nested structure representing branches. Each direct child becomes a key,
    with its value being the chain continuing from that unit (or empty list if leaf).
    
    Example (linear chain):
        If UnitC upgrades from UnitB, and UnitB upgrades from UnitA,
        the result will be: {"UnitA": {"UnitB": ["UnitC"]}}
    
    Example (branching):
        If UnitB and UnitC both upgrade from UnitA, and UnitD upgrades from UnitB,
        the result will be: {"UnitA": {"UnitB": ["UnitD"], "UnitC": []}}
    
    Args:
        forward_mapping: Dictionary mapping unit names to their UpgradeFromUnit values
        
    Returns:
        Dictionary mapping base unit names to nested chain structures
    """
    # Build reverse mapping: upgrade_from -> [units that upgrade from it]
    reverse_mapping: Dict[str, List[str]] = {}
    
    for unit_name, upgrade_from in forward_mapping.items():
        if upgrade_from not in reverse_mapping:
            reverse_mapping[upgrade_from] = []
        reverse_mapping[upgrade_from].append(unit_name)
    
    # Find base units (units that are referenced as upgrade_from but don't upgrade from anything themselves)
    base_units = set()
    for upgrade_from in reverse_mapping.keys():
        if upgrade_from not in forward_mapping:
            base_units.add(upgrade_from)
    
    # Build chains starting from each base unit
    chain_mapping: Dict[str, Any] = {}
    
    def build_branch(unit: str, visited: set) -> Any:
        """Build a branch structure starting from a unit.
        
        Returns:
            - Empty list [] if unit has no children (leaf node)
            - Dict[str, Any] mapping each child to its branch if unit has children
        """
        if unit in visited:
            return []
        visited.add(unit)
        
        # Get all units that upgrade from this unit
        if unit not in reverse_mapping or not reverse_mapping[unit]:
            # Leaf node - no children
            return []
        
        # Branch node - create nested structure
        branch = {}
        for child_unit in reverse_mapping[unit]:
            child_branch = build_branch(child_unit, visited)
            branch[child_unit] = child_branch
        
        return branch
    
    for base_unit in base_units:
        branch = build_branch(base_unit, set())
        if branch:  # Only add if there are children
            chain_mapping[base_unit] = branch
            logger.debug(f"Built chain for {base_unit}: {branch}")
    
    return chain_mapping


def build_upgrade_from_mapping(unit_data: Dict[str, Any]) -> Dict[str, List[str]]:
    """Build UpgradeFrom mapping from vanilla unit data.
    
    Creates chains where the base unit (lowest in chain) maps to a list of
    all units that upgrade from it (directly or indirectly).
    
    Example:
        If UnitC upgrades from UnitB, and UnitB upgrades from UnitA,
        the result will be: {"UnitA": ["UnitB", "UnitC"]}
    
    Args:
        unit_data: Dictionary of unit data gathered from game files
        
    Returns:
        Dictionary mapping base unit names to nested chain structures
    """
    # First, build forward mapping (unit -> upgrade_from)
    forward_mapping = {}
    
    for unit_name, unit_info in unit_data.items():
        if "upgrade_from_unit" in unit_info:
            upgrade_from = unit_info["upgrade_from_unit"]
            if upgrade_from:  # Only add if not None/empty
                forward_mapping[unit_name] = upgrade_from
                logger.debug(f"Found UpgradeFrom relationship: {unit_name} -> {upgrade_from}")
    
    validate_upgrade_forward_mapping_chain_lengths(forward_mapping)

    # Validate for circular chains before building
    circular_chains = _detect_circular_chains(forward_mapping)
    if circular_chains:
        cycle_details = []
        for i, cycle in enumerate(circular_chains, 1):
            cycle_str = " -> ".join(cycle)
            cycle_details.append(f"  Circular chain {i}: {cycle_str}")
        error_msg = (
            f"Found {len(circular_chains)} circular chain(s) in vanilla upgrade relationships:\n"
            + "\n".join(cycle_details) +
            "\nCircular chains will be excluded from the mapping"
        )
        logger.error(error_msg)
    
    # Build chains from forward mapping
    chain_mapping = _build_upgrade_chains(forward_mapping)
    
    logger.info(
        f"Built UpgradeFrom mapping with {len(chain_mapping)} chains "
        f"containing {sum(len(chain) for chain in chain_mapping.values())} total units"
    )
    return chain_mapping


# Tag used for per-unit identity; excluded from all_tags dataset and validation
UNITE_TAG_PREFIX = "UNITE_"


def build_all_tags(unit_data: Dict[str, Any]) -> Dict[str, List[str]]:
    """Build list of all unique tags from unit data, excluding UNITE_* tags.

    UNITE_{unitname} tags are unique per unit and are not included in the
    dataset or validation.

    Returns:
        Dict with "all_tags": sorted list of unique tag strings.
    """
    all_tags: Set[str] = set()
    for unit_info in unit_data.values():
        for tag in unit_info.get("tags", []):
            if tag.startswith(UNITE_TAG_PREFIX):
                continue
            all_tags.add(tag)
    result = {"all_tags": sorted(all_tags)}
    logger.info(f"Gathered {len(all_tags)} unique tags (excluding {UNITE_TAG_PREFIX}*)")
    return result


def compare_tags_with_previous(
    current_tags: List[str],
    previous_tags: List[str],
) -> None:
    """Log warnings if tags were added or removed compared to previous build."""
    current_set = set(current_tags)
    previous_set = set(previous_tags)

    added = current_set - previous_set
    removed = previous_set - current_set

    if added:
        logger.warning(
            "Tags added in game data (new tags): %s",
            sorted(added),
        )
    if removed:
        logger.warning(
            "Tags removed from game data (no longer present): %s",
            sorted(removed),
        )


def validate_no_multiple_ancestors(chain_mapping: Dict[str, Any]) -> None:
    """Log a warning if any unit appears as a key under multiple parents in the chain mapping.

    This detects UpgradeFrom hierarchies where a unit has more than one ancestor
    (multiple parents), which indicates conflicting UpgradeFromUnit values.

    Args:
        chain_mapping: Nested dict from _build_upgrade_chains (base_unit -> {child: ...})
    """
    seen: Dict[str, List[str]] = {}

    def walk(node: Any, parent_path: str = "") -> None:
        if not isinstance(node, dict):
            return
        for key, value in node.items():
            if key in seen:
                seen[key].append(parent_path or "<root>")
            else:
                seen[key] = [parent_path or "<root>"]
            walk(value, key)

    for base, branch in chain_mapping.items():
        # Record the base itself
        if base in seen:
            seen[base].append("<root>")
        else:
            seen[base] = ["<root>"]
        walk(branch, base)

    duplicates = {unit: parents for unit, parents in seen.items() if len(parents) > 1}
    if duplicates:
        details = []
        for unit, parents in sorted(duplicates.items()):
            details.append(f"  {unit} appears under: {', '.join(parents)}")
        logger.warning(
            "Found %d unit(s) with multiple ancestors in UpgradeFrom hierarchy:\n%s\n"
            "Check conflicting UpgradeFromUnit values in unit_edits or new_units.",
            len(duplicates),
            "\n".join(details),
        )
