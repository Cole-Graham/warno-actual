"""Build insert turret templates from vanilla WeaponDescriptor for unit_edits equipment insert.

Extracts turret templates from unmodified vanilla data so inserts get correct ammunition
and other weapon fields, even when the donor unit has been patched (e.g. MMG replaced
with Satchel Charge).
"""

import json
from pathlib import Path
from typing import Any, Dict, List

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.utils.config_utils import get_mod_src_path
from src.utils.database_utils import ensure_db_directory
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type, is_valid_turret

logger = setup_logger(__name__)

NDF_PATH = "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf"


def _serialize_ndf_value(val: Any, member_name: str = "") -> str:
    """Serialize an NDF value to string format for valid ndf.convert() parsing."""
    if val is None:
        return "None"
    if isinstance(val, bool):
        return "True" if val else "False"
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, str):
        # Strip NDF quote wrappers (single or double) for re-serialization
        stripped = val
        if (len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"')):
            stripped = val[1:-1]
        if stripped.startswith("$") or stripped.startswith("RGBA"):
            return stripped
        if stripped in ("True", "False"):
            return stripped
        if stripped.lstrip("-").replace(".", "", 1).isdigit():
            return stripped
        return f"'{stripped}'"
    if hasattr(val, "__iter__") and not isinstance(val, str):
        raw = []
        for item in val:
            if hasattr(item, "v"):
                raw.append(_serialize_ndf_value(item.v, member_name))
            else:
                raw.append(_serialize_ndf_value(item, member_name))
        # RGBA fields: output RGBA[r,g,b,a] not [r,g,b,a]
        if member_name in ("DispersionRadiusOffColor", "DispersionRadiusOnColor") and len(raw) == 4:
            nums = [r.replace("'", "") for r in raw]
            return "RGBA[" + ",".join(nums) + "]"
        return "[" + ", ".join(raw) + "]"
    s = str(val)
    if s.startswith("$") or s.startswith("RGBA"):
        return s
    if s in ("True", "False"):
        return s
    if s.lstrip("-").replace(".", "", 1).isdigit():
        return s
    return f"'{s}'"


def _serialize_mounted_weapon(weapon_obj: Any, override_ammo_name: str | None = None) -> str:
    """Serialize a TMountedWeaponDescriptor to NDF string.

    Args:
        weapon_obj: The mounted weapon NDF object
        override_ammo_name: If set, use this for Ammunition instead of donor value
    """
    lines = ["TMountedWeaponDescriptor", "("]
    member_order = [
        "AmmoBoxIndex",
        "Ammunition",
        "AnimateOnlyOneSoldier",
        "DispersionRadiusOffColor",
        "DispersionRadiusOffThickness",
        "DispersionRadiusOnColor",
        "DispersionRadiusOnThickness",
        "EffectTag",
        "HandheldEquipmentKey",
        "NbWeapons",
        "ShowDispersion",
        "WeaponActiveAndCanShootPropertyName",
        "WeaponIgnoredPropertyName",
        "WeaponShootDataPropertyName",
    ]
    for mem in member_order:
        try:
            m = weapon_obj.v.by_m(mem)
            if override_ammo_name and mem == "Ammunition":
                val_str = f"$/GFX/Weapon/Ammo_{override_ammo_name}"
            else:
                val_str = _serialize_ndf_value(m.v, mem)
            lines.append(f"    {mem} = {val_str}")
        except Exception:
            pass
    lines.append(")")
    return "\n".join(lines)


def _serialize_turret(turret_obj: Any, mounted_index: int, override_ammo_name: str | None = None) -> str | None:
    """Serialize a TTurretInfanterieDescriptor containing one weapon to NDF string."""
    if not is_valid_turret(turret_obj.v):
        return None
    mounted_wpns = turret_obj.v.by_m("MountedWeaponDescriptorList")
    weapons = [w for w in mounted_wpns.v if is_obj_type(w.v, "TMountedWeaponDescriptor")]
    if not weapons:
        return None
    weapon = weapons[mounted_index] if mounted_index < len(weapons) else weapons[0]
    weapon_str = _serialize_mounted_weapon(weapon, override_ammo_name)
    weapon_indented = "\n".join(f"    {line}" for line in weapon_str.split("\n"))
    yul_bone = _serialize_ndf_value(turret_obj.v.by_m("YulBoneOrdinal").v, "YulBoneOrdinal")
    lines = [
        "TTurretInfanterieDescriptor",
        "(",
        "    MountedWeaponDescriptorList = ",
        "    [",
        weapon_indented,
        "    ]",
        f"    YulBoneOrdinal = {yul_bone}",
        ")",
    ]
    return "\n".join(lines)


def _collect_insert_weapons() -> List[str]:
    """Collect all weapon names used in unit_edits equipment insert."""
    weapons = []
    unit_edits = load_unit_edits()
    for unit, edits in unit_edits.items():
        wd = edits.get("WeaponDescriptor", {})
        eq = wd.get("equipmentchanges", {})
        insert_list = eq.get("insert", [])
        for _idx, ammo_name in insert_list:
            if ammo_name not in weapons:
                weapons.append(ammo_name)
    return weapons


def build_insert_turret_templates(
    config: Dict[str, Any],
    game_db: Dict[str, Any] | None = None,
    ammunition_renames: Dict[str, Dict[str, str]] | None = None,
) -> Dict[str, str]:
    """Build turret templates for weapons used in equipment insert.

    Parses vanilla WeaponDescriptor.ndf and extracts turret templates for each
    weapon that appears in unit_edits insert lists. Templates are stored as
    NDF strings keyed by weapon name. Uses ammunition_renames (renames_new_old)
    to resolve renamed weapons to their vanilla names for donor lookup.

    Args:
        config: Configuration dict with database_path
        game_db: Optional game database with weapons and ammunition
        ammunition_renames: Optional dict with renames_new_old (new->old) for
            resolving renamed weapons to vanilla names in weapon_locations

    Returns:
        Dict mapping weapon_name -> turret NDF string
    """
    templates = {}
    weapons_to_find = _collect_insert_weapons()
    if not weapons_to_find:
        return templates

    mod_source_path = get_mod_src_path(config)
    if not mod_source_path or not mod_source_path.exists():
        logger.warning("mod_source_path not available for insert turret templates")
        return templates

    weapon_db = (game_db or {}).get("weapons", {})
    if not weapon_db:
        logger.warning("weapon_db not available for insert turret templates")
        return templates

    try:
        mod = ndf.Mod(str(mod_source_path), "None")
        source = mod.parse_src(NDF_PATH)
    except Exception as e:
        logger.error(f"Failed to parse WeaponDescriptor for insert templates: {e}")
        return templates

    # Prefer ammunition_renames from constants precomputation (built in same run);
    # game_db ammo may not have constants renames merged yet.
    renames_new_old = {}
    if ammunition_renames:
        renames_new_old = ammunition_renames.get("renames_new_old", {})
    if not renames_new_old:
        ammo_db = (game_db or {}).get("ammunition", {})
        renames_new_old = ammo_db.get("renames_new_old", {})

    for weapon_name in weapons_to_find:
        if weapon_name in templates:
            continue
        lookup_names = [weapon_name, renames_new_old.get(weapon_name)]
        donor_name = None
        location = None

        for name in lookup_names:
            if not name:
                continue
            for descr_name, descr_data in weapon_db.items():
                if name in descr_data.get("weapon_locations", {}):
                    locs = descr_data["weapon_locations"][name]
                    if locs:
                        donor_name = descr_name
                        location = locs[0]
                        break
            if donor_name:
                break

        if not donor_name or not location:
            logger.debug(f"No donor found for insert template: {weapon_name}")
            continue

        donor_descr = source.by_namespace(donor_name, strict=False)
        if not donor_descr:
            logger.warning(f"Donor descriptor not found in vanilla source: {donor_name}")
            continue

        turret_idx = location["turret_index"]
        mounted_idx = location.get("mounted_index", 0)

        for turret in donor_descr.v.by_member("TurretDescriptorList").v:
            if turret.index == turret_idx:
                turret_str = _serialize_turret(turret, mounted_idx, override_ammo_name=weapon_name)
                if turret_str:
                    templates[weapon_name] = turret_str
                    logger.debug(f"Built insert template for {weapon_name} from {donor_name}")
                break

    return templates


def save_insert_turret_templates(templates: Dict[str, str], config: Dict[str, Any]) -> None:
    """Save insert turret templates to JSON file."""
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))
    out_file = constants_dir / "insert_turret_templates.json"
    try:
        with open(out_file, "w") as f:
            json.dump(templates, f, indent=2, sort_keys=True)
        logger.info(f"Saved {len(templates)} insert turret templates to {out_file}")
    except Exception as e:
        logger.error(f"Failed to save insert turret templates: {e}")
        raise


def load_insert_turret_templates(config: Dict[str, Any]) -> Dict[str, str]:
    """Load insert turret templates from JSON file (e.g. when not in game_db)."""
    db_path = Path(config["data_config"]["database_path"])
    out_file = db_path / "constants_precomputation" / "insert_turret_templates.json"
    if not out_file.exists():
        return {}
    try:
        with open(out_file) as f:
            return json.load(f)
    except Exception as e:
        logger.warning(f"Failed to load insert turret templates from {out_file}: {e}")
        return {}
