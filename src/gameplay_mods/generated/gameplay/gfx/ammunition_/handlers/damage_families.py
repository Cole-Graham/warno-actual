from typing import Any, Dict

from src.constants.weapons import WEAPON_DESCRIPTIONS, WEAPON_DESCRIPTION_EDITS
from src.utils.dictionary_utils import write_dictionary_entries

def apply_damage_families(source_path: Any, logger, game_db: Dict[str, Any]) -> None:
    """Apply damage family modifications to weapons in Ammunition.ndf & AmmunitionMissiles.ndf"""
    ammo_db = game_db["ammunition"]
    renames_new_old = ammo_db.get("renames_new_old", {})

    dictionary_entries = []
    for weapon_descr in source_path:
        # Check if weapon is a sniper weapon, accounting for vanilla instance renames
        weapon_name = weapon_descr.n
        is_sniper = weapon_name in ammo_db["sniper_weapons"]
        
        # If not found directly, check if this weapon was renamed and check the old name
        if not is_sniper and weapon_name in renames_new_old:
            old_name = renames_new_old[weapon_name]
            is_sniper = old_name in ammo_db["sniper_weapons"]

        if is_sniper:
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
    
    for weapon_type, edits in WEAPON_DESCRIPTION_EDITS.items():
        category_token = edits["category"][0]
        category_string = edits["category"][1]
        description_token = edits["description"][0]
        description_string = edits["description"][1]
        new_dic_entry = (category_token, category_string)
        if new_dic_entry not in dictionary_entries:
            dictionary_entries.append(new_dic_entry)
        new_dic_entry = (description_token, description_string)
        if new_dic_entry not in dictionary_entries:
            dictionary_entries.append(new_dic_entry)

    # Write dictionary entries
    if dictionary_entries:
        logger.info(f"Writing {len(dictionary_entries)} dictionary entries")
        write_dictionary_entries(dictionary_entries, dictionary_type="units")