"""Functions for modifying weapon damage families."""

from typing import Any, Dict

from src.constants.weapons import (
    VANILLA_LAST_ROW,
    VANILLA_LAST_COLUMN,
    DAMAGE_EDITS,
    DPICM_DAMAGES,
    FMBALLE_INFANTRY_EDITS,
    FMBALLE_ROWS,
    FULL_BALL_DAMAGE,
    INFANTRY_ARMOR_EDITS,
    SNIPER_DAMAGE,
    WEAPON_DESCRIPTIONS,
    # KPVT_DAMAGE,
    NPLM_BOMB_DAMAGE,
    PGB_BOMB_DAMAGE,
    MANPAD_HAGRU_DAMAGE,
    MANPAD_TBAGRU_DAMAGE,
)
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_weapon_constantes(source_path):
    logger.info(f"--------- editing WeaponConstantes.ndf ---------")
    weapon_constantes_obj = source_path.by_n("WeaponConstantes").v
    
    # Add infantry WA to mimetic resistance map
    mimetic_res_map = weapon_constantes_obj.by_m("ResistanceToMimeticImpact").v
    mimetic_res_map.add(f"(ResistanceFamily_infanterieWA, EImpactSurface/Ground)")

    # Add full ball damage to blindages to ignore
    blindages_to_ignore = weapon_constantes_obj.by_m("BlindagesToIgnoreForDamageFamilies").v
    blindages_to_ignore.add(f"(DamageFamily_full_balle, [ResistanceFamily_blindage])")
    
    # Add manpad_hagru damage to blindages to ignore
    blindages_to_ignore.add("(DamageFamily_manpad_hagru, [ResistanceFamily_helico])")
    logger.info("Added manpad_hagru to blindages to ignore")
    
    # Add manpad_tbagru damage to blindages to ignore
    blindages_to_ignore.add("(DamageFamily_manpad_tbagru, [ResistanceFamily_avion])")
    logger.info("Added manpad_tbagru to blindages to ignore")


def add_damage_families_to_list(source_path) -> None:
    """Add new damage families to DamageResistanceFamilyList.ndf."""
    logger.info("Adding new damage families to list")
    
    # Count existing families
    i = -1  # Damage families counter
    j = -1  # Resistance families counter
    for row in source_path:
        if row.namespace.startswith("DamageFamily_"):
            i += 1
        elif row.namespace.startswith("ResistanceFamily_"):
            j += 1
    
    # Add new families
    infanterie_wa_family = f"ResistanceFamily_infanterieWA is {j + 1}"
    sniper_family = f"DamageFamily_sniper is {i + 1}"
    full_ball_family = f"DamageFamily_full_balle is {i + 2}"
    dpicm_family = f"DamageFamily_dpicm is {i + 3}"
    # kpvt_family = f"DamageFamily_kpvt is {i + 4}"
    nplm_bomb_family = f"DamageFamily_nplm_bomb is {i + 4}"
    pgb_bomb_family = f"DamageFamily_pgb_bomb is {i + 5}"
    manpad_hagru_family = f"DamageFamily_manpad_hagru is {i + 6}"
    manpad_tbagru_family = f"DamageFamily_manpad_tbagru is {i + 7}"

    source_path.insert(j + 1, infanterie_wa_family)
    source_path.add(sniper_family)
    source_path.add(full_ball_family)
    source_path.add(dpicm_family)
    # source_path.add(kpvt_family)
    source_path.add(nplm_bomb_family)
    source_path.add(pgb_bomb_family)
    source_path.add(manpad_hagru_family)
    source_path.add(manpad_tbagru_family)
    
    logger.info(f"Added families: \n"
                f"{infanterie_wa_family}\n"
                f"{sniper_family}\n"
                f"{full_ball_family}\n"
                f"{dpicm_family}\n"
                # f"{kpvt_family}\n")
                f"{nplm_bomb_family}\n"
                f"{pgb_bomb_family}\n"
                f"{manpad_hagru_family}\n"
                f"{manpad_tbagru_family}")
                

def add_damage_families_to_impl(source_path) -> None:
    """Add new damage families to DamageResistanceFamilyListImpl.ndf."""
    logger.info("Adding new damage families to implementation")
    
    # Define new families
    families = {
        "resistance": ['"ResistanceFamily_infanterieWA"'],
        "damage": [
            '"DamageFamily_sniper"',
            '"DamageFamily_full_balle"',
            '"DamageFamily_dpicm"',
            # '"DamageFamily_kpvt"',
            '"DamageFamily_nplm_bomb"',
            '"DamageFamily_pgb_bomb"',
            '"DamageFamily_manpad_hagru"',
            '"DamageFamily_manpad_tbagru"',
        ]
    }
    
    # Add resistance families
    resistance_values = source_path.by_n("Generated_ResistanceFamily_Enum").v.by_m("Values").v
    for family in families["resistance"]:
        resistance_values.add(family)
        logger.info(f"Added resistance family: {family}")
    
    # Add damage families
    damage_values = source_path.by_n("Generated_DamageFamily_Enum").v.by_m("Values").v
    for family in families["damage"]:
        damage_values.add(family)
        logger.info(f"Added damage family: {family}")


def apply_damage_families(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Apply damage family modifications to weapons in Ammunition/AmmunitionMissiles.ndf"""
    ammo_db = game_db["ammunition"]
    
    dictionary_entries = []
    for weapon_descr in source_path:
        if weapon_descr.n in ammo_db["full_ball_weapons"]:
            arme_obj = weapon_descr.v.by_m("Arme")
            arme_obj.v.by_m("Family").v = "DamageFamily_full_balle"
            logger.info(f"Changed {weapon_descr.n} to DamageFamily_full_balle")
        
        # elif "KPVT" in weapon_descr.n or "14_5" in weapon_descr.n:
        #     if weapon_descr.v.by_m("WeaponCursorType").v == "Weapon_Cursor_MachineGun":
        #         arme_obj = weapon_descr.v.by_m("Arme")
        #         arme_obj.v.by_m("Family").v = "DamageFamily_kpvt"
        #         logger.info(f"Changed {weapon_descr.n} to DamageFamily_kpvt")
            
        elif weapon_descr.n in ammo_db["sniper_weapons"]:
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


def add_damage_resistance_values(source_path) -> None:
    """Add damage resistance values to DamageResistance.ndf."""
    logger.info("Adding damage resistance values")
    
    # Get resistance params
    resist_params_obj = source_path.by_n("DamageResistanceParams").v
    
    # Add family definitions
    damage_family_list = resist_params_obj.by_m("DamageFamilyDefinitionList").v
    families = {
        "sniper": "TDamageTypeFamilyDefinition(Family=DamageFamily_sniper MaxIndex=2)",
        "full_ball": "TDamageTypeFamilyDefinition(Family=DamageFamily_full_balle MaxIndex=1)",
        "dpicm": "TDamageTypeFamilyDefinition(Family=DamageFamily_dpicm MaxIndex=4)",
        # "kpvt": "TDamageTypeFamilyDefinition(Family=DamageFamily_kpvt MaxIndex=1)",
        "nplm_bomb": "TDamageTypeFamilyDefinition(Family=DamageFamily_nplm_bomb MaxIndex=1)",   
        "pgb_bomb": "TDamageTypeFamilyDefinition(Family=DamageFamily_pgb_bomb MaxIndex=1)",
        "manpad_hagru": "TDamageTypeFamilyDefinition(Family=DamageFamily_manpad_hagru MaxIndex=1)",
        "manpad_tbagru": "TDamageTypeFamilyDefinition(Family=DamageFamily_manpad_tbagru MaxIndex=1)",
    }

    for family_name, family_def in families.items():
        damage_family_list.add(family_def)
        logger.info(f"Added {family_name} family definition")

    values_list = resist_params_obj.by_m("Values").v
    
    # Check array dimensions match expected constants
    last_row_index = len(values_list) - 1
    last_column_index = len(values_list[0].v) - 1

    if last_row_index != VANILLA_LAST_ROW or last_column_index != VANILLA_LAST_COLUMN:
        logger.warning(f"DAMAGE ARRAY DIMENSIONS DIFFER FROM EXPECTED!!! Expected "
                       f"{VANILLA_LAST_ROW + 1} rows, {VANILLA_LAST_COLUMN + 1} columns, "
                       f"got {last_row_index + 1} rows, {last_column_index + 1} columns")

    # Add damage values
    values_list.add(
        *[str(sniper) for sniper in SNIPER_DAMAGE],
        str(FULL_BALL_DAMAGE),
        *[str(dpicm) for dpicm in DPICM_DAMAGES],
        # str(KPVT_DAMAGE),
        str(NPLM_BOMB_DAMAGE),
        str(PGB_BOMB_DAMAGE),
        str(MANPAD_HAGRU_DAMAGE),
        str(MANPAD_TBAGRU_DAMAGE),
    )
    logger.info("Added damage values") 


def apply_damage_array_edits(damage_array, row: int, column_edits: dict) -> None:
    """Apply edits to specific columns in a damage array row."""
    for i, dmg_row in enumerate(damage_array):
        if i == row:
            for columns, value in column_edits.items():
                if isinstance(columns, tuple):
                    for column in range(columns[0], columns[1] + 1):
                        dmg_row.v.replace(column, str(value))
                        logger.info(f"Edited row {row}, column {column} to {value}")
                else:
                    column = columns
                    dmg_row.v.replace(column, str(value))
                    logger.info(f"Edited row {row}, column {column} to {value}")


def apply_damage_family_edits(source_path) -> None:
    """Apply damage family edits to DamageResistance.ndf."""
    logger.info("Applying damage family edits")
    
    # Get damage params
    damage_params_obj = source_path.by_n("DamageResistanceParams").v
    
    # Add new infantry resistance family
    resistance_list = damage_params_obj.by_m("ResistanceFamilyDefinitionList").v
    resistance_list.add(
        "TResistanceTypeFamilyDefinition(Family=ResistanceFamily_infanterieWA MaxIndex=13)")
    logger.info("Added infantryWA resistance family")
    
    damage_array = damage_params_obj.by_m("Values").v
    
    # Extend damage array with new columns
    for row in damage_array:
        for _ in range(13):
            row.v.add("0.0")
    logger.info("Extended damage array with 13 new columns")
    
    # Apply damage edits
    for weapon_type, data in DAMAGE_EDITS.items():
        apply_damage_array_edits(damage_array, data["row"], data["edits"])
        logger.info(f"Applied damage edits for {weapon_type}") 


def edit_infantry_armor(source_path) -> None:
    """Edit infantry armor values in DamageResistance.ndf."""
    logger.info("Editing infantry armor values")
    
    damage_params_obj = source_path.by_n("DamageResistanceParams").v
    damage_array = damage_params_obj.by_m("Values").v

    # Apply infantry armor edits
    for i, row in enumerate(damage_array):
        if i in INFANTRY_ARMOR_EDITS:
            damage_ratio, damage_family = INFANTRY_ARMOR_EDITS[i]
            # WA Infantry columns (49-61): 13 strength levels from 14 to 2
            for column in range(49, 62):  # range is exclusive of end value
                row.v.replace(column, str(damage_ratio))
                logger.info(f"Edited row {i}, family {damage_family}, column {column} to {damage_ratio}")

    # Apply FMballe infantry damage edits
    for row_index in FMBALLE_ROWS:
        apply_damage_array_edits(damage_array, row_index, FMBALLE_INFANTRY_EDITS)
        logger.info(f"Applied FMballe infantry edits to row {row_index}") 


# def edit_weapon_constants(source_path) -> None:
#     """Edit weapon constants in WeaponConstantes.ndf."""
#     logger.info("--------- editing WeaponConstantes.ndf ---------")
    
#     weapon_constantes_obj = source_path.by_n("WeaponConstantes").v
    
#     # Add infantry WA to mimetic resistance map
#     mimetic_res_map = weapon_constantes_obj.by_m("ResistanceToMimeticImpact").v
#     mimetic_res_map.add("(ResistanceFamily_infanterieWA, EImpactSurface/Ground)")
#     logger.info("Added infantryWA to mimetic resistance map")
    
#     # Add full ball damage to blindages to ignore
#     blindages_to_ignore = weapon_constantes_obj.by_m("BlindagesToIgnoreForDamageFamilies").v
#     blindages_to_ignore.add("(DamageFamily_full_balle, [ResistanceFamily_blindage])")
#     logger.info("Added full_balle to blindages to ignore") 
    
#     # Add manpad_hagru damage to blindages to ignore
#     blindages_to_ignore.add("(DamageFamily_manpad_hagru, [ResistanceFamily_helico])")
#     logger.info("Added manpad_hagru to blindages to ignore")
    
#     # Add manpad_tbagru damage to blindages to ignore
#     blindages_to_ignore.add("(DamageFamily_manpad_tbagru, [ResistanceFamily_avion])")
#     logger.info("Added manpad_tbagru to blindages to ignore")
