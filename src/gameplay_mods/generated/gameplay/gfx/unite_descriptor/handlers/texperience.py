"""Edit TExperienceModuleDescriptor for existing and new units"""

import re
from typing import Any, Dict, Optional

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.weapons.ammunition import raw_ammunitions
from src.constants.weapons.standards import DCA_STANDARDS
from src.utils.ndf_utils import find_obj_by_type

_DCA_AMMO_BASE_NAMES = frozenset(k[0] for k in raw_ammunitions if k[1] == "DCA")


def _strip_ammo_quantity_suffix(ammo_name: str) -> str:
    m = re.match(r"^(.+)_x\d+$", ammo_name)
    return m.group(1) if m else ammo_name


def _weapon_data_has_dca_ammo(weapon_data: dict, dca_base_names: frozenset) -> bool:
    for turret in weapon_data.get("turrets", {}).values():
        for ammo_name in turret.get("weapons", {}):
            base = _strip_ammo_quantity_suffix(ammo_name)
            if base in dca_base_names:
                return True
    return False


def _weapon_descriptor_key_for_lookup(unit_name: str, weapons_db: dict) -> str | None:
    """Resolve ``WeaponDescriptor_*`` key in ``game_db['weapons']`` (donor for new units)."""
    key = f"WeaponDescriptor_{unit_name}"
    if key in weapons_db:
        return key
    for donor_key, edits in NEW_UNITS.items():
        if edits.get("NewName") == unit_name:
            donor_ws = f"WeaponDescriptor_{donor_key[0]}"
            if donor_ws in weapons_db:
                return donor_ws
            return None
    return None


def _unit_has_explicit_xp_multiplier(unit_name: str, unit_edits: dict) -> bool:
    if "multiplier" in unit_edits.get(unit_name, {}).get("XP", {}):
        return True
    for edits in NEW_UNITS.values():
        if edits.get("NewName") == unit_name and "multiplier" in edits.get("XP", {}):
            return True
    return False


def apply_dca_experience_unit_standard_for_unit(
    logger,
    game_db: Dict[str, Any],
    unit_name: str,
    modules_list: Any,
    unit_edits: Optional[Dict[str, Any]] = None,
) -> None:
    """Apply DCA ``experience_unit`` to one unit's modules (baseline before unit_edits / new_units)."""
    if unit_edits is None:
        unit_edits = load_unit_edits()
    if _unit_has_explicit_xp_multiplier(unit_name, unit_edits):
        return

    experience = DCA_STANDARDS["experience_unit"]
    mult_s = str(experience["ExperienceMultiplierBonusOnKill"])
    weapons_db = game_db.get("weapons") or {}

    xp_mod = find_obj_by_type(modules_list.v, "TExperienceModuleDescriptor")
    if not xp_mod:
        return

    ws_key = _weapon_descriptor_key_for_lookup(unit_name, weapons_db)
    if not ws_key:
        return
    wdata = weapons_db[ws_key]
    if not _weapon_data_has_dca_ammo(wdata, _DCA_AMMO_BASE_NAMES):
        return

    xp_mod.v.by_m("ExperienceMultiplierBonusOnKill").v = mult_s
    logger.info(
        f"DCA experience_unit: ExperienceMultiplierBonusOnKill = {mult_s} ({unit_name})",
    )


def apply_dca_experience_unit_standard(logger, source_path, game_db) -> None:
    """Set DCA category ``experience_unit`` on all units whose weapon loadout includes DCA ammo."""
    unit_edits = load_unit_edits()

    for unit_row in source_path:
        if not hasattr(unit_row, "namespace"):
            continue
        if not unit_row.namespace.startswith("Descriptor_Unit_"):
            continue
        unit_name = unit_row.namespace.replace("Descriptor_Unit_", "")
        modules_list = unit_row.v.by_m("ModulesDescriptors")
        apply_dca_experience_unit_standard_for_unit(
            logger, game_db, unit_name, modules_list, unit_edits,
        )


def handle_experience_module(
    logger,
    game_db,
    unit_data,
    edit_type,
    unit_name,
    edits,
    module,
    *args,
) -> None:
    """Handle TExperienceModuleDescriptor for existing and new units"""
    
    _edit_xp(logger, unit_data, edit_type, unit_name, edits, module)
    _set_multiplicative_xp_pack(logger, unit_data, edit_type, unit_name, edits, module)
    _set_helico_SF_xp_pack(logger, unit_data, edit_type, unit_name, edits, module)

def _edit_xp(logger, unit_data, edit_type, unit_name, edits, module) -> None:
    """Edit the XP pack for the unit"""
    
    if edits.get("XP", {}).get("pack", False):
        pack_name = edits["XP"]["pack"]
        module.v.by_m("ExperienceLevelsPackDescriptor").v = (
            f"~/ExperienceLevelsPackDescriptor_XP_pack_{pack_name}"
        )
        logger.info(f"Set {unit_name} XP pack to {pack_name}")
        
    if edits.get("XP", {}).get("multiplier", False):
        module.v.by_m("ExperienceMultiplierBonusOnKill").v = f"{edits['XP']['multiplier']}"
        
            
def _set_multiplicative_xp_pack(logger, unit_data, edit_type, unit_name, edits, module) -> None:
    """Set the multiplicative accuracy XP pack for infantry units"""
    if edit_type == "new_units":
        required_tags = ["Infanterie"]
        invalid_tags = ["Infanterie_AA", "Infanterie_AT"]
        new_unit_tags = edits["TagSet"]["overwrite_all"]
        if all(tag in new_unit_tags for tag in required_tags):
            if not any(tag in new_unit_tags for tag in invalid_tags):
                xp_pack = module.v.by_m("ExperienceLevelsPackDescriptor")
                if xp_pack.v.endswith("SF_v2"):
                    xp_pack.v = "~/ExperienceLevelsPackDescriptor_XP_pack_SF_v2_multiplicative"
                    logger.info(f"Set {unit_name} XP pack to {xp_pack.v}")
                elif xp_pack.v.endswith("simple_v3"):
                    xp_pack.v = "~/ExperienceLevelsPackDescriptor_XP_pack_simple_v3_multiplicative"
                    logger.info(f"Set {unit_name} XP pack to {xp_pack.v}")
    
    elif edit_type == "unit_edits":
        required_tags = ["Infanterie"]
        invalid_tags = ["Infanterie_AA", "Infanterie_AT"]
        tags = unit_data["tags"]
        if all(tag in tags for tag in required_tags):
            if not any(tag in tags for tag in invalid_tags):
                xp_pack = module.v.by_m("ExperienceLevelsPackDescriptor")
                if xp_pack.v.endswith("SF_v2"):
                    xp_pack.v = "~/ExperienceLevelsPackDescriptor_XP_pack_SF_v2_multiplicative"
                    logger.info(f"Set {unit_name} XP pack to {xp_pack.v}")
                elif xp_pack.v.endswith("simple_v3"):
                    xp_pack.v = "~/ExperienceLevelsPackDescriptor_XP_pack_simple_v3_multiplicative"
                    logger.info(f"Set {unit_name} XP pack to {xp_pack.v}")

def _set_helico_SF_xp_pack(logger, unit_data, edit_type, unit_name, edits, module) -> None:
    """Set the multiplicative accuracy XP pack for helicopter units"""
    required_tags = {"Helo"}
    required_specialties = {"_sf"}

    if edit_type == "new_units":
        tags = set(edits.get("TagSet", {}).get("overwrite_all", []))
        specialties = set(edits.get("SpecialtiesList", []))
    elif edit_type == "unit_edits":
        tags = set(unit_data.get("tags", []))
        specialties = set(unit_data.get("specialties", []))
    else:
        return

    if required_tags.issubset(tags) and required_specialties.issubset(specialties):
        xp_pack = module.v.by_m("ExperienceLevelsPackDescriptor")
        if xp_pack.v.endswith("SF_v2"):
            xp_pack.v = "~/ExperienceLevelsPackDescriptor_XP_pack_helico_SF"
            logger.info(f"Set {unit_name} XP pack to {xp_pack.v}")