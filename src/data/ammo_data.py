"""Functions for building ammunition data from game files."""

import re
from pathlib import Path
from typing import Any, Dict, List

from src import ndf
from src.constants.weapons.standards.pattern.clu_sol_traits import CLU_SOL_DAMAGE_FAMILY_TO_TRAIT
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_MISSILES_RENAMES,
    AMMUNITION_RENAMES,
)
from src.utils.dictionary_utils import load_vanilla_units_lookup
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_valid_turret, strip_quotes

logger = setup_logger('ammo_data')


def get_vanilla_renames(mod: Any, ndf_path: Any) -> Dict[str, str]:
    """Get mapping of original weapon names to their new names.

    Returns:
        Dictionary mapping original names to renamed versions
    """
    renames = {}
    
    try:
        # Process renames from parsed source
        _process_renames(mod, ndf_path, renames)
            
        # Add static renames from ammunition and missiles modules
        for old_name, new_name in AMMUNITION_RENAMES:
            renames[old_name] = new_name
            
        for old_name, new_name in AMMUNITION_MISSILES_RENAMES:
            renames[old_name] = new_name
            
        return renames
        
    except Exception as e:
        logger.error(f"Error getting vanilla renames: {str(e)}")
        return {}


def _process_renames(mod: Any, ndf_path: Any, renames: Dict[str, str]) -> None:
    """Process renames from parsed NDF data."""
    # Build data for salvo weapon renames using same logic as build_salvo_weapons
    EXCLUDED_PREFIXES = ('Gatling', 'MMG', 'Pod')
    
    parse_source = mod.parse_src(ndf_path)

    for ammo_descr in parse_source:
        if not hasattr(ammo_descr, 'namespace'):
            continue
                
        name = ammo_descr.namespace.removeprefix('Ammo_')
        
        # Skip if name starts with any excluded prefix
        if any(name.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
            continue
                
        match = re.match(r'^(.+)_x(\d+)$', name)
        if match:
            base_name = match.group(1)
            salvo_num = match.group(2)
            new_name = f"{base_name}_salvolength{salvo_num}"
            renames[name] = new_name


def _arme_family_value(ammo_descr: Any) -> Any:
    """Return Arme.Family string if set, else None."""
    arme = ammo_descr.v.by_m("Arme", False)
    if arme is None:
        return None
    fam = arme.v.by_m("Family", False)
    if fam is None:
        return None
    v = fam.v
    if not isinstance(v, str):
        return None
    s = v.strip()
    if s.startswith("'") and s.endswith("'"):
        return s[1:-1]
    return s


def _build_clu_sol_trait_targets_from_ndf(parse_ammo_source, parse_ammo_missile_source) -> Dict[str, str]:
    """Map from parsed NDF only (vanilla Arme.Family in source files)."""
    targets: Dict[str, str] = {}
    for src in (parse_ammo_source, parse_ammo_missile_source):
        for ammo_descr in src:
            if not hasattr(ammo_descr, "namespace") or not ammo_descr.namespace:
                continue
            fam = _arme_family_value(ammo_descr)
            if fam is None or fam not in CLU_SOL_DAMAGE_FAMILY_TO_TRAIT:
                continue
            targets[ammo_descr.n] = CLU_SOL_DAMAGE_FAMILY_TO_TRAIT[fam]
    return targets


def _build_clu_sol_trait_targets_from_constants() -> Dict[str, str]:
    """Descriptors whose Family is set to CLU SOL only in ``raw_ammunitions`` (e.g. vanilla ``DamageFamily_cluster`` → patch)."""
    from src.constants.weapons.ammunition import raw_ammunitions

    targets: Dict[str, str] = {}
    for (weapon_name, _category, _donor, _is_new), data in raw_ammunitions.items():
        if data is None:
            continue
        ammo_block = data.get("Ammunition", {})
        arme = ammo_block.get("Arme", {})
        if not isinstance(arme, dict):
            continue
        fam = arme.get("Family")
        if fam is None or fam not in CLU_SOL_DAMAGE_FAMILY_TO_TRAIT:
            continue
        targets[f"Ammo_{weapon_name}"] = CLU_SOL_DAMAGE_FAMILY_TO_TRAIT[fam]
    return targets


def build_clu_sol_trait_targets(parse_ammo_source, parse_ammo_missile_source) -> Dict[str, str]:
    """Precompute Ammo_* namespace → WeaponTraits key for CLU SOL ammunition.

    Merges (1) NDF scan of existing ``DamageFamily_clu_sol_*`` rows with (2) constants that
    assign ``Arme.Family`` at patch time (e.g. ``KMGU_dispenser``: vanilla ``DamageFamily_cluster``
    in source → ``DamageFamily_clu_sol_ap`` from ``bomb.py``). Constants entries override NDF on conflict.
    """
    from_ndf = _build_clu_sol_trait_targets_from_ndf(parse_ammo_source, parse_ammo_missile_source)
    from_constants = _build_clu_sol_trait_targets_from_constants()
    return {**from_ndf, **from_constants}


def build_ammo_data(mod_src_path: Path, config: Dict[str, Any]) -> Dict[str, Any]:
    """Build ammunition database from source files."""
    logger.info("Building ammunition database")
    
    # ammo_data = {}
    ammo_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
    ammo_missile_path = "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf"
    weapon_descriptor_path = "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf"

    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        ammo_file = mod.parse_src(ammo_path)
        ammo_missile_file = mod.parse_src(ammo_missile_path)
        weapon_descriptor_file = mod.parse_src(weapon_descriptor_path)

        units_lookup = load_vanilla_units_lookup(config)

        # Build salvo weapons (from game files - base game data)
        salvo_weapons = build_salvo_weapons(ammo_file)
        salvo_weapons.update(build_salvo_weapons(ammo_missile_file))
        
        ammo_props = build_ammo_properties(ammo_file, units_lookup)
        ammo_props.update(build_ammo_properties(ammo_missile_file, units_lookup))

        return {
            "mg_categories": build_mg_categories(ammo_file),
            "full_ball_weapons": build_full_ball_weapons(ammo_file),
            "sniper_weapons": build_sniper_weapons(ammo_file),
            "radar_weapons": build_radar_weapons(ammo_file, ammo_missile_file),
            "salvo_weapons": salvo_weapons,
            "salves_map": build_ammo_salves_map(weapon_descriptor_file),
            "mortar_weapons": build_mortar_weapons(ammo_file),
            "ammo_properties": ammo_props,
            "missing_cac_tag": build_missing_cac_tag(ammo_file),
            "all_ammunition_and_missile": build_all_ammunition_and_missile_names(ammo_file, ammo_missile_file),
            "clu_sol_trait_targets": build_clu_sol_trait_targets(ammo_file, ammo_missile_file),
        }
        
    except Exception as e:
        logger.error(f"Error building ammunition database: {e}", exc_info=True)
        return {
            "mg_categories": {},
            "full_ball_weapons": [],
            "sniper_weapons": [],
            "radar_weapons": [],
            "salvo_weapons": {},
            "salves_map": {},
            "mortar_weapons": {},
            "ammo_properties": {},
            "missing_cac_tag": [],
            "all_ammunition_and_missile": [],
            "clu_sol_trait_targets": {},
        }

def build_all_ammunition_and_missile_names(parse_ammo_source, parse_ammo_missile_source) -> List[str]:
    """Build list of all ammunition and missile names from both files.
    
    Args:
        parse_ammo_source: Parsed Ammunition.ndf file
        parse_ammo_missile_source: Parsed AmmunitionMissiles.ndf file
    
    Returns:
        List of ammunition names without "Ammo_" prefix
    """
    all_names = []
    
    for ammo_descr in parse_ammo_source:
        if hasattr(ammo_descr, 'namespace') and ammo_descr.namespace:
            # Extract name without "Ammo_" prefix
            name = ammo_descr.namespace.removeprefix('Ammo_')
            if name:
                all_names.append(name)
    
    for ammo_descr in parse_ammo_missile_source:
        if hasattr(ammo_descr, 'namespace') and ammo_descr.namespace:
            # Extract name without "Ammo_" prefix
            name = ammo_descr.namespace.removeprefix('Ammo_')
            if name:
                all_names.append(name)
    
    return all_names


def _parse_numeric_member_value(value: Any) -> Any:
    """Parse NDF member string to int or float."""
    try:
        if isinstance(value, (int, float)):
            return value
        if isinstance(value, str):
            if "." in value:
                return float(value)
            return int(value)
    except (TypeError, ValueError):
        return None
    return None


def _localized_token_field(
    raw_value: Any,
    units_lookup: Dict[str, str],
) -> Dict[str, str] | None:
    """Map an NDF localization token member to {Token, Value}."""
    if raw_value is None:
        return None
    token = strip_quotes(str(raw_value))
    if not token or token == "None":
        return None
    return {"Token": token, "Value": units_lookup.get(token, token)}


def build_ammo_properties(
    parse_ammo_source,
    units_lookup: Dict[str, str] | None = None,
) -> Dict[str, Any]:
    """Build dictionary of ammunition properties from Ammunition.ndf or AmmunitionMissiles.ndf."""
    if units_lookup is None:
        units_lookup = {}
    ammo_properties = {}

    for ammo_descr in parse_ammo_source:

        if ammo_descr.v.by_m("MinMaxCategory", False) is not None:
            min_max_category = ammo_descr.v.by_m("MinMaxCategory", False).v
        else:
            min_max_category = None

        radius_membr = ammo_descr.v.by_m("RadiusSplashPhysicalDamagesGRU", False)
        radius_splash: Any = None
        if radius_membr is not None:
            radius_splash = _parse_numeric_member_value(radius_membr.v)

        has_deployment_membr = ammo_descr.v.by_m("HasDeploymentTime", False)
        has_deployment_time = (
            has_deployment_membr is not None and has_deployment_membr.v == "True"
        )

        phys_dmg_membr = ammo_descr.v.by_m("PhysicalDamages", False)
        physical_damages: Any = None
        if phys_dmg_membr is not None:
            physical_damages = _parse_numeric_member_value(phys_dmg_membr.v)

        helo_range_membr = ammo_descr.v.by_m("MaximumRangeHelicopterGRU", False)
        max_range_helicopter_gru: Any = None
        if helo_range_membr is not None:
            max_range_helicopter_gru = _parse_numeric_member_value(helo_range_membr.v)

        plane_range_membr = ammo_descr.v.by_m("MaximumRangeAirplaneGRU", False)
        max_range_airplane_gru: Any = None
        if plane_range_membr is not None:
            max_range_airplane_gru = _parse_numeric_member_value(plane_range_membr.v)

        ground_range_membr = ammo_descr.v.by_m("MaximumRangeGRU", False)
        max_range_gru: Any = None
        if ground_range_membr is not None:
            max_range_gru = _parse_numeric_member_value(ground_range_membr.v)

        family = _arme_family_value(ammo_descr)

        entry: Dict[str, Any] = {}
        for field_name, member_name in (
            ("Name", "Name"),
            ("TypeCategoryName", "TypeCategoryName"),
            ("Caliber", "Caliber"),
        ):
            membr = ammo_descr.v.by_m(member_name, False)
            if membr is None:
                continue
            localized = _localized_token_field(membr.v, units_lookup)
            if localized is not None:
                entry[field_name] = localized

        entry.update({
            "MinMaxCategory": min_max_category,
            "RadiusSplashPhysicalDamagesGRU": radius_splash,
            "HasDeploymentTime": has_deployment_time,
            "PhysicalDamages": physical_damages,
            "MaximumRangeGRU": max_range_gru,
            "MaximumRangeHelicopterGRU": max_range_helicopter_gru,
            "MaximumRangeAirplaneGRU": max_range_airplane_gru,
            "Family": family,
        })
        ammo_properties[ammo_descr.n] = entry

    return ammo_properties


def build_missing_cac_tag(parse_ammo_source) -> List[str]:
    """Build list of ammunition descriptors missing CAC for infantry MMGs."""
    missing_cac_tag = []
    
    def _parse_numeric_value(value):
        try:
            if isinstance(value, (int, float)):
                return value
            if "." in value:
                return float(value)
            return int(value)
        except (TypeError, ValueError):
            return None
    
    for ammo_descr in parse_ammo_source:
        minmax_category = ammo_descr.v.by_m("MinMaxCategory", False)
        if minmax_category is None or minmax_category.v != "MinMax_inf_MMG":
            continue
        
        min_range_membr = ammo_descr.v.by_m("MinimumRangeGRU", False)
        if min_range_membr is None:
            continue
        
        min_range_value = _parse_numeric_value(min_range_membr.v)
        if min_range_value != 0:
            continue
        
        traits_list = ammo_descr.v.by_m("TraitsToken", False)
        if traits_list is None:
            missing_cac_tag.append(ammo_descr.n)
            continue
        
        existing_traits = [trait.v for trait in traits_list.v]
        if "'CAC'" in existing_traits:
            continue
        
        missing_cac_tag.append(ammo_descr.n)
    
    return missing_cac_tag

def build_radar_weapons(parse_ammo_source, parse_ammo_missile_source) -> List[str]:
    """Build list of radar weapons from Ammunition.ndf and AmmunitionMissiles.ndf"""
    radar_weapons = []
    
    for ammo_descr in parse_ammo_source:
        traits_list = ammo_descr.v.by_m("TraitsToken")
        if "'RADAR'" in [t.v for t in traits_list.v]:
            radar_weapons.append(ammo_descr.n)
            
    for ammo_descr in parse_ammo_missile_source:
        traits_list = ammo_descr.v.by_m("TraitsToken")
        if "'RADAR'" in [t.v for t in traits_list.v]:
            radar_weapons.append(ammo_descr.n)

    return radar_weapons


def build_ammo_salves_map(parse_source) -> dict:
    """Build mapping of ammunition salves in WeaponDescriptor.ndf
    for ammunition.json (used for applying default salves during ammunition edits)"""
    salves_map = {}
    # salves_list = []
    
    for weapon_descr in parse_source:
        salves_map[weapon_descr.n] = {}
        salves = weapon_descr.v.by_m("Salves")
        
        salves_list = []
        salves_list.extend(int(value.v) for value in salves.v)
        salves_map[weapon_descr.n]['salves_list'] = salves_list
        salves_map[weapon_descr.n]['salves'] = {}
            
        turret_list = weapon_descr.v.by_m("TurretDescriptorList")
        for turret in turret_list.v:
            if not is_valid_turret(turret.v):
                logger.warning(f"Invalid turret: {turret.v}")
                continue
            
            mounted_weapons = turret.v.by_m("MountedWeaponDescriptorList")
            for weapon in mounted_weapons.v:
                ammunition = weapon.v.by_m("Ammunition").v.split('_', 1)[1]
                salvo_stock_index = weapon.v.by_m("AmmoBoxIndex").v
                salvos = salves.v[int(salvo_stock_index)].v
                
                data = [int(salvo_stock_index), int(salvos)]
                salves_map[weapon_descr.n]['salves'][ammunition] = data
    
    return salves_map


def build_mg_categories(parse_source) -> dict:
    """Build MG weapon categories from ammunition data.
    
    Args:
        parse_source: Ammunition.ndf file
    
    Returns:
        Dictionary of MG weapon categories
    """
    hmg_teams = []
    mmg_teams = []
    hmg_turrets = []
    mmg_turrets = []
    coax_mmgs = []
    
    for weapon_descr in parse_source:
        membr = weapon_descr.v.by_m
        
        # Get weapon characteristics
        is_rotary_cannon = membr("TypeCategoryName").v == "'ZJQCIJREVP'"
        is_rifle = membr("TypeCategoryName").v == "'MPRVLPMVZK'"
        is_inf_mmg = membr("TypeCategoryName").v == "'YSLEYULPVD'"
        is_battle_rifle = membr("TypeCategoryName").v == "'THRUBJLEUJ'"
        
        caliber = membr("Caliber").v
        traits_list = membr("TraitsToken").v
        
        # Check traits
        is_tripod = "'tripod'" in [t.v for t in traits_list]
        is_coax = "'coax'" in [t.v for t in traits_list]
        is_stabilized = membr("CanShootWhileMoving").v == "True"
        
        # Categorize weapon
        if is_tripod and not is_stabilized:
            if caliber == "'12_7mm'":
                hmg_teams.append(weapon_descr.n)
            elif caliber in ["'UZKJUPNFLB'", "'ARZDNMYCBF'"] and not (is_rifle or is_inf_mmg):
                mmg_teams.append(weapon_descr.n)
        else:
            if caliber == "'12_7mm'" and not is_rotary_cannon:
                if is_coax or is_stabilized:
                    hmg_turrets.append(weapon_descr.n)
            elif caliber in ["'UZKJUPNFLB'", "'ARZDNMYCBF'"] and not any([
                is_coax, is_rifle, is_inf_mmg, is_battle_rifle
            ]) and is_stabilized:
                mmg_turrets.append(weapon_descr.n)
            elif caliber in ["'UZKJUPNFLB'", "'ARZDNMYCBF'"] and is_coax:
                coax_mmgs.append(weapon_descr.n)

    return {
        "hmg_teams": hmg_teams,
        "mmg_teams": mmg_teams,
        "hmg_turrets": hmg_turrets,
        "mmg_turrets": mmg_turrets,
        "coax_mmgs": coax_mmgs,
        "hmg_exceptions": ["Ammo_HMG_team_12_7_mm_NSV_6U6"]
    } 


def build_full_ball_weapons(parse_source) -> list:
    """Build list of weapons that should use full ball damage."""
    full_ball = []
    
    for weapon in parse_source:
        if weapon.v.by_m("TypeCategoryName").v != "'GGSLNBFHEX'":
            if weapon.v.by_m("Caliber").v in ["'ARZDNMYCBF'", "'UZKJUPNFLB'"]:
                full_ball.append(weapon.n)
    
    return full_ball


def build_sniper_weapons(parse_source) -> list:
    """Build list of sniper weapons."""
    snipers = []
    
    for weapon in parse_source:
        if weapon.v.by_m("TypeCategoryName").v == "'GGSLNBFHEX'":
            snipers.append(weapon.n)
    
    return snipers 


def build_salvo_weapons(parse_source) -> Dict[str, str]:
    """Build mapping of vanilla salvo weapons to their new names.
    
    Returns:
        Dict mapping original names to salvolength names
    """
    salvo_weapons = {}
    
    # Prefixes to exclude from salvo renaming
    EXCLUDED_PREFIXES = ('Gatling', 'MMG', 'Pod')
    
    for weapon_descr in parse_source:
        if not hasattr(weapon_descr, 'namespace'):
            continue
            
        name = weapon_descr.namespace.removeprefix('Ammo_')
        
        # Skip if name starts with any excluded prefix
        if any(name.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
            continue
            
        match = re.match(r'^(.+)_x(\d+)$', name)
        if match:
            base_name = match.group(1)
            salvo_num = match.group(2)
            new_name = f"{base_name}_salvolength{salvo_num}"
            salvo_weapons[name] = new_name
            
    logger.info(f"Found {len(salvo_weapons)} vanilla salvo weapons to rename")
    return salvo_weapons


def build_mortar_weapons(parse_source) -> Dict[str, List[str]]:
    """Build lists of mortar weapons from ammunition data."""
    mortars = []
    smoke_mortars = []
    
    for ammo_descr in parse_source:
        if not hasattr(ammo_descr, 'namespace'):
            continue
        
        projectile_type = ammo_descr.v.by_m("ProjectileType").v
        if projectile_type != "EProjectileType/Artillerie":
            continue

        name = ammo_descr.namespace.removeprefix('Ammo_')
        if name.startswith('Mortier_'):
            if '_SMOKE' in name:
                smoke_mortars.append(name)

            else:
                mortars.append(name)
    
    return {
        "mortars": mortars,
        "smoke_mortars": smoke_mortars
    }
