from typing import Any, Dict
import re

from src.constants.weapons.ammunition import ammunitions

def apply_default_salves(source_path: Any, logger, game_db: Dict[str, Any], unit_edits: Dict[str, Any]) -> None:
    """Apply default salves to WeaponDescriptor.ndf"""

    ammo_db = game_db["ammunition"]
    
    # Not sure if needed
    # def _strip_identifiers(ammo_name: str) -> str:
    #     """Remove strength{N}, _xN, _salvolengthN from ammo name if present."""
    #     ammo_name = re.sub(r"_strength\d+", "", ammo_name)

    #     return ammo_name

    for (ammo_name, category, donor, is_new), data in ammunitions.items():
        if not (data.get("WeaponDescriptor") and "Salves" in data["WeaponDescriptor"]):
            continue

        old_name = ammo_db["renames_new_old"].get(ammo_name, None)
        default_salves = data["WeaponDescriptor"]["Salves"]

        for weapon_descr_name, weapon_descr_data in ammo_db["salves_map"].items():
            skip_weapon_descr_ammo_name = False
            unit_name = weapon_descr_name.replace("WeaponDescriptor_", "")

            # Check if this weapon should be skipped due to unit edits
            for unit, edits in unit_edits.items():
                if unit == unit_name and "WeaponDescriptor" in edits:
                    replacements = edits["WeaponDescriptor"].get("equipmentchanges", {}).get("replace", [])
                    salve_changes = edits["WeaponDescriptor"].get("Salves", {})
                    if replacements:
                        for replacement in replacements:
                            if len(replacement) == 4:
                                current, new, old_fire_effect, new_fire_effect = replacement
                            else:
                                current, new = replacement
                            if current == ammo_name:
                                skip_weapon_descr_ammo_name = True
                    if salve_changes:
                        for ammo, salve in salve_changes.items():
                            if ammo == ammo_name:
                                skip_weapon_descr_ammo_name = True

            if skip_weapon_descr_ammo_name:
                logger.debug(
                    f"Skipping {ammo_name} for {weapon_descr_name} because it is replaced or " f"has custom salves."
                )
                continue

            for weapon_ammo, salvo_indices in weapon_descr_data["salves"].items():

                if old_name and weapon_ammo == old_name:
                    logger.debug(f"ammo_name: {ammo_name}, old_name: {old_name}")
                    weapon_descr = source_path.by_n(weapon_descr_name)
                    salves = weapon_descr.v.by_m("Salves")
                    salves.v[salvo_indices[0]].v = str(default_salves)
                    logger.info(f"Applied default salves ({default_salves}) for {old_name} to {weapon_descr_name}")
                    break

                elif weapon_ammo == ammo_name:
                    logger.debug(f"ammo_name: {ammo_name}, old_name: {old_name}")
                    weapon_descr = source_path.by_n(weapon_descr_name)
                    salves = weapon_descr.v.by_m("Salves")
                    salves.v[salvo_indices[0]].v = str(default_salves)
                    logger.info(f"Applied default salves ({default_salves}) for {ammo_name} to {weapon_descr_name}")
                    break