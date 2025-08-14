from typing import Any, Dict

from src.constants.weapons import WEAPON_DESCRIPTIONS
from src.utils.dictionary_utils import write_dictionary_entries

def apply_damage_families(source_path: Any, logger, game_db: Dict[str, Any]) -> None:
    """Apply damage family modifications to weapons in Ammunition/AmmunitionMissiles.ndf"""
    ammo_db = game_db["ammunition"]

    dictionary_entries = []
    for weapon_descr in source_path:
        # if weapon_descr.n in ammo_db["full_ball_weapons"]:
        #     arme_obj = weapon_descr.v.by_m("Arme")
        #     arme_obj.v.by_m("Family").v = "DamageFamily_sa_full"
        #     logger.info(f"Changed {weapon_descr.n} to DamageFamily_sa_full")

        # elif "KPVT" in weapon_descr.n or "14_5" in weapon_descr.n:
        #     if weapon_descr.v.by_m("WeaponCursorType").v == "Weapon_Cursor_MachineGun":
        #         arme_obj = weapon_descr.v.by_m("Arme")
        #         arme_obj.v.by_m("Family").v = "DamageFamily_kpvt"
        #         logger.info(f"Changed {weapon_descr.n} to DamageFamily_kpvt")

        if weapon_descr.n in ammo_db["sniper_weapons"]:
            arme_obj = weapon_descr.v.by_m("Arme")
            arme_obj.v.by_m("Family").v = "DamageFamily_sniper"
            logger.info(f"Changed {weapon_descr.n} to DamageFamily_sniper")

            # Update description token
            type_cat = weapon_descr.v.by_m("TypeCategoryName").v
            for weapon_type, ((cat_hash, desc_hash), dic_string) in WEAPON_DESCRIPTIONS.items():
                if type_cat == cat_hash:
                    weapon_descr.v.by_m("WeaponDescriptionToken").v = f"'{desc_hash}'"
                    logger.info(f"Changed {weapon_descr.n} description to {weapon_type} ({desc_hash})")
                    new_dic_entry = (desc_hash, dic_string)
                    if new_dic_entry not in dictionary_entries:
                        dictionary_entries.append(new_dic_entry)
                    break

    # Write dictionary entries
    if dictionary_entries:
        logger.info(f"Writing {len(dictionary_entries)} dictionary entries")
        write_dictionary_entries(dictionary_entries, dictionary_type="units")