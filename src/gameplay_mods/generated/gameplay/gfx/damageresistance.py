"""Functions for modifying weapon damage families."""

from typing import Any, Dict

from src.constants.weapons import (
    KE_AND_HEAT_ROW_COUNT,
    VANILLA_LAST_ROW,
    VANILLA_LAST_COLUMN,
    DAMAGE_EDITS,
    DPICM_DAMAGES,
    FMBALLE_INFANTRY_EDITS,
    FMBALLE_ROWS,
    SA_FULL_DAMAGE_RATIOS,
    SA_INTERMEDIATE_DAMAGE_RATIOS,
    SA_INF_ARMOR_DAMAGE_RATIOS,
    INFANTRY_ARMOR_EDITS,
    SNIPER_DAMAGE,
    NPLM_BOMB_DAMAGE,
    PGB_BOMB_DAMAGE,
    MANPAD_HAGRU_DAMAGE,
    MANPAD_TBAGRU_DAMAGE,
    TWELVE_SEVEN_MM_DAMAGE,
    FOURTEEN_FIVE_MM_DAMAGE,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_gfx_damageresistance(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/DamageResistance.ndf"""
    logger.info("Editing DamageResistance.ndf")
    
    _apply_damage_family_edits(source_path)
    _add_damage_resistance_values(source_path)
    _edit_infantry_armor(source_path)


def edit_gen_gp_gfx_damageresistancefamilylist(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyList.ndf"""
    
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
    # full_ball_family = f"DamageFamily_full_balle is {i + 2}"
    dpicm_family = f"DamageFamily_dpicm is {i + 2}"
    # kpvt_family = f"DamageFamily_kpvt is {i + 4}"
    nplm_bomb_family = f"DamageFamily_nplm_bomb is {i + 3}"
    pgb_bomb_family = f"DamageFamily_pgb_bomb is {i + 4}"
    manpad_hagru_family = f"DamageFamily_manpad_hagru is {i + 5}"
    manpad_tbagru_family = f"DamageFamily_manpad_tbagru is {i + 6}"
    sa_intermediate_family = f"DamageFamily_sa_intermediate is {i + 7}"
    sa_full_family = f"DamageFamily_sa_full is {i + 8}"
    twelve_seven_mm_family = f"DamageFamily_12_7 is {i + 9}"
    fourteen_five_mm_family = f"DamageFamily_14_5 is {i + 10}"

    source_path.insert(j + 1, infanterie_wa_family)
    source_path.add(sniper_family)
    # source_path.add(full_ball_family)
    source_path.add(dpicm_family)
    # source_path.add(kpvt_family)
    source_path.add(nplm_bomb_family)
    source_path.add(pgb_bomb_family)
    source_path.add(manpad_hagru_family)
    source_path.add(manpad_tbagru_family)
    source_path.add(sa_intermediate_family)
    source_path.add(sa_full_family)
    source_path.add(twelve_seven_mm_family)
    source_path.add(fourteen_five_mm_family)

    logger.info(
        f"Added families: \n"
        f"{infanterie_wa_family}\n"
        f"{sniper_family}\n"
        # f"{full_ball_family}\n"
        f"{dpicm_family}\n"
        # f"{kpvt_family}\n")
        f"{nplm_bomb_family}\n"
        f"{pgb_bomb_family}\n"
        f"{manpad_hagru_family}\n"
        f"{manpad_tbagru_family}\n"
        f"{sa_intermediate_family}\n"
        f"{sa_full_family}\n"
        f"{twelve_seven_mm_family}\n"
        f"{fourteen_five_mm_family}\n"
    )


def edit_gen_gp_gfx_damageresistancefamilylistimpl(source_path) -> None:
    """Add new damage families to DamageResistanceFamilyListImpl.ndf."""
    
    logger.info("Adding new damage families to implementation")
    # Define new families
    families = {
        "resistance": ['"ResistanceFamily_infanterieWA"'],
        "damage": [
            '"DamageFamily_sniper"',
            # '"DamageFamily_full_balle"',
            '"DamageFamily_dpicm"',
            # '"DamageFamily_kpvt"',
            '"DamageFamily_nplm_bomb"',
            '"DamageFamily_pgb_bomb"',
            '"DamageFamily_manpad_hagru"',
            '"DamageFamily_manpad_tbagru"',
            '"DamageFamily_sa_intermediate"',
            '"DamageFamily_sa_full"',
            '"DamageFamily_12_7"',
            '"DamageFamily_14_5"',
        ],
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
        

def _add_damage_resistance_values(source_path) -> None:
    """Add damage resistance values to DamageResistance.ndf."""
    logger.info("Adding damage resistance values")

    # Get resistance params
    resist_params_obj = source_path.by_n("DamageResistanceParams").v

    # Add family definitions
    damage_family_list = resist_params_obj.by_m("DamageFamilyCounts").v
    families = {
        "sniper": ("(DamageFamily_sniper, 2)"),
        # "full_ball": ("(DamageFamily_full_balle, 1)"),
        "dpicm": ("(DamageFamily_dpicm, 4)"),
        # "kpvt": ("(DamageFamily_kpvt, 1)"),
        "nplm_bomb": ("(DamageFamily_nplm_bomb, 1)"),
        "pgb_bomb": ("(DamageFamily_pgb_bomb, 1)"),
        "manpad_hagru": ("(DamageFamily_manpad_hagru, 1)"),
        "manpad_tbagru": ("(DamageFamily_manpad_tbagru, 1)"),
        "sa_intermediate": ("(DamageFamily_sa_intermediate, 13)"),
        "sa_full": ("(DamageFamily_sa_full, 13)"),
        "12_7": ("(DamageFamily_12_7, 1)"),
        "14_5": ("(DamageFamily_14_5, 1)"),
    }

    for family_name, family_def in families.items():
        damage_family_list.add(family_def)
        logger.info(f"Added {family_name} family definition")

    values_list = resist_params_obj.by_m("Values").v

    # Check array dimensions match expected constants
    last_row_index = len(values_list) - 1
    last_column_index = len(values_list[0].v) - 1

    if last_row_index != VANILLA_LAST_ROW or last_column_index != VANILLA_LAST_COLUMN:
        logger.warning(
            f"DAMAGE ARRAY DIMENSIONS DIFFER FROM EXPECTED!!! Expected "
            f"{VANILLA_LAST_ROW + 1} rows, {VANILLA_LAST_COLUMN + 1} columns, "
            f"got {last_row_index + 1} rows, {last_column_index + 1} columns"
        )

    # Add damage values
    values_list.add(
        *[str(sniper) for sniper in SNIPER_DAMAGE],
        *[str(dpicm) for dpicm in DPICM_DAMAGES],
        str(NPLM_BOMB_DAMAGE),
        str(PGB_BOMB_DAMAGE),
        str(MANPAD_HAGRU_DAMAGE),
        str(MANPAD_TBAGRU_DAMAGE),
        *[str(SA_INTERMEDIATE_DAMAGE_RATIOS + list(sa_damage)) for sa_damage in SA_INF_ARMOR_DAMAGE_RATIOS],
        *[str(SA_FULL_DAMAGE_RATIOS + list(sa_damage)) for sa_damage in SA_INF_ARMOR_DAMAGE_RATIOS],
        str(TWELVE_SEVEN_MM_DAMAGE),
        str(FOURTEEN_FIVE_MM_DAMAGE),
    )
    logger.info("Added damage values")
    
    
def _apply_damage_family_edits(source_path) -> None:
    """Apply damage family edits to DamageResistance.ndf."""
    logger.info("Applying damage family edits")

    # Get damage params
    damage_params_obj = source_path.by_n("DamageResistanceParams").v

    # Add new infantry resistance family
    resistance_list = damage_params_obj.by_m("ResistanceFamilyCounts").v
    resistance_list.add("(ResistanceFamily_infanterieWA, 13)")
    logger.info("Added infantryWA resistance family")

    damage_array = damage_params_obj.by_m("Values").v

    # Extend damage array with new columns
    for row in damage_array:
        for _ in range(13):
            row.v.add("0.0")
    logger.info("Extended damage array with 13 new columns")

    # Apply damage edits
    for weapon_type, data in DAMAGE_EDITS.items():
        _apply_damage_array_edits(damage_array, data["row"], data["edits"])
        logger.info(f"Applied damage edits for {weapon_type}")
        
        
def _apply_damage_array_edits(damage_array, row: int, column_edits: dict) -> None:
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


def _edit_infantry_armor(source_path) -> None:
    """Edit infantry armor values in DamageResistance.ndf."""
    logger.info("Editing infantry armor values")

    damage_params_obj = source_path.by_n("DamageResistanceParams").v
    damage_array = damage_params_obj.by_m("Values").v
    
    # Validate INFANTRY_ARMOR_EDITS is proper length
    if len(INFANTRY_ARMOR_EDITS) + KE_AND_HEAT_ROW_COUNT != VANILLA_LAST_ROW:
        logger.warning(
            f"INFANTRY_ARMOR_EDITS IS NOT THE CORRECT LENGTH!!!\n"
            f"Expected {VANILLA_LAST_ROW} rows, got:\n"
            f"INFANTRY_ARMOR_EDITS: {len(INFANTRY_ARMOR_EDITS)}\n"
            f"KE_AND_HEAT_ROW_COUNT: {KE_AND_HEAT_ROW_COUNT}\n"
            f"TOTAL: {len(INFANTRY_ARMOR_EDITS) + KE_AND_HEAT_ROW_COUNT}\n"
        )

    # Apply infantry armor edits
    for i, row in enumerate(damage_array):
        if i in INFANTRY_ARMOR_EDITS:
            damage_ratio, damage_family = INFANTRY_ARMOR_EDITS[i]
            # WA Infantry columns (49-61): 13 strength levels from 14 to 2
            for column in range(49, 62):  # range is exclusive of end value
                row.v.replace(column, str(damage_ratio))
                logger.info(f"Edited row {i}, family {damage_family}, column {column} to {damage_ratio}")

    # Apply FMballe infantry damage edits
    # for row_index in FMBALLE_ROWS:
    #     apply_damage_array_edits(damage_array, row_index, FMBALLE_INFANTRY_EDITS)
    #     logger.info(f"Applied FMballe infantry edits to row {row_index}")