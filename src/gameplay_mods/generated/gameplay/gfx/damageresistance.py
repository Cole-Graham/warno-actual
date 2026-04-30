"""Functions for modifying weapon damage families."""

from typing import Any, Dict

from src.constants.weapons import (
    KE_AND_HEAT_ROW_COUNT,
    VANILLA_LAST_ROW,
    VANILLA_LAST_COLUMN,
    AP_MISSILE_ROW_FIRST,
    AP_MISSILE_ROW_LAST,
    SEAD_MISSILE_WA_LEVEL_COUNT,
    SEAD_INFANTRY_ARMOR_LEVEL_ONE_COLUMN,
    SEAD_RATIO_VS_INFANTRY,
    SEAD_WA_INFANTRY_ARMOR_COLUMNS,
    DAMAGE_EDITS,
    CLU_SOL_HEFRAG,
    CLU_AP_INFANTRY_FINAL_MULTIPLIER,
    CLU_HEFRAG_INFANTRY_FINAL_MULTIPLIER,
    CLU_SOL_AP,
    CLU_SOL_AP_ROW_FIRST,
    CLU_SOL_AP_ROW_LAST,
    FMBALLE_INFANTRY_EDITS,
    FMBALLE_ROWS,
    SA_FULL_DAMAGE_RATIOS,
    SA_INTERMEDIATE_DAMAGE_RATIOS,
    SA_INF_ARMOR_DAMAGE_RATIOS,
    INFANTRY_ARMOR_EDITS,
    SNIPER_DAMAGE,
    SNIPER_DOUBLE_DAMAGE,
    SNIPER_TRIPLE_DAMAGE,
    NPLM_BOMB_DAMAGE,
    NPLM_BOMB_FLAMME_DAMAGE,
    PGB_BOMB_DAMAGE,
    MANPAD_HAGRU_DAMAGE,
    MANPAD_TBAGRU_DAMAGE,
    SAM_HAGRU_DAMAGE,
    SAM_TBAGRU_DAMAGE,
    A2A_HAGRU_DAMAGE,
    A2A_TBAGRU_DAMAGE,
    MISSILE_HE_BIGLY_DAMAGE,
    TWELVE_SEVEN_MM_DAMAGE,
    FOURTEEN_FIVE_MM_DAMAGE,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


# Vanilla DamageFamily_he_dca single-level row index in DamageResistanceParams.Values.
# Matches the "he_dca 1" entry in DAMAGE_EDITS in damage_values.py. Cloning this
# row at edit time keeps DamageFamily_he_dca_airtargets in lockstep with any
# tweaks we apply to he_dca (e.g. air armor 0/1/2 reductions in DAMAGE_EDITS).
_HE_DCA_ROW_INDEX = 119


def _clone_existing_damage_row(values_list, row_index: int) -> str:
    """Return the row at ``row_index`` formatted as a Python list literal string.

    Reads each cell directly from the live NDF array so the clone reflects
    every edit applied earlier in the run (column extension, family-specific
    edits). The returned string is suitable to pass to ``values_list.add(...)``.
    """
    src_row = values_list[row_index].v
    cells = [str(cell.v) for cell in src_row]
    return "[" + ", ".join(cells) + "]"


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

    # Add new resistancefamilies
    infanterie_wa_family = f"ResistanceFamily_infanterieWA is {j + 1}"
    
    # Add new damage families
    sniper_family = f"DamageFamily_sniper is {i + 1}"
    sniper_double_family = f"DamageFamily_sniper_double is {i + 2}"
    sniper_triple_family = f"DamageFamily_sniper_triple is {i + 3}"
    clu_sol_hefrag_family = f"DamageFamily_clu_sol_hefrag is {i + 4}"
    nplm_bomb_family = f"DamageFamily_nplm_bomb is {i + 5}"
    nplm_bomb_flamme_family = f"DamageFamily_nplm_bomb_flamme is {i + 6}"
    pgb_bomb_family = f"DamageFamily_pgb_bomb is {i + 7}"
    manpad_hagru_family = f"DamageFamily_manpad_hagru is {i + 8}"
    manpad_tbagru_family = f"DamageFamily_manpad_tbagru is {i + 9}"
    sam_hagru_family = f"DamageFamily_sam_hagru is {i + 10}"
    sam_tbagru_family = f"DamageFamily_sam_tbagru is {i + 11}"
    a2a_hagru_family = f"DamageFamily_a2a_hagru is {i + 12}"
    a2a_tbagru_family = f"DamageFamily_a2a_tbagru is {i + 13}"
    sa_intermediate_family = f"DamageFamily_sa_intermediate is {i + 14}"
    sa_full_family = f"DamageFamily_sa_full is {i + 15}"
    twelve_seven_mm_family = f"DamageFamily_12_7 is {i + 16}"
    fourteen_five_mm_family = f"DamageFamily_14_5 is {i + 17}"
    missile_he_bigly_family = f"DamageFamily_missile_he_bigly is {i + 18}"
    sead_missile_wa_family = f"DamageFamily_sead_missile_wa is {i + 19}"
    he_dca_airtargets_family = f"DamageFamily_he_dca_airtargets is {i + 20}"

    source_path.insert(j + 1, infanterie_wa_family)
    source_path.add(sniper_family)
    source_path.add(clu_sol_hefrag_family)
    source_path.add(nplm_bomb_family)
    source_path.add(nplm_bomb_flamme_family)
    source_path.add(pgb_bomb_family)
    source_path.add(manpad_hagru_family)
    source_path.add(manpad_tbagru_family)
    source_path.add(sam_hagru_family)
    source_path.add(sam_tbagru_family)
    source_path.add(a2a_hagru_family)
    source_path.add(a2a_tbagru_family)
    source_path.add(sa_intermediate_family)
    source_path.add(sa_full_family)
    source_path.add(twelve_seven_mm_family)
    source_path.add(fourteen_five_mm_family)
    source_path.add(missile_he_bigly_family)
    source_path.add(sead_missile_wa_family)
    source_path.add(sniper_double_family)
    source_path.add(sniper_triple_family)
    source_path.add(he_dca_airtargets_family)
    logger.info(
        f"Added families: \n"
        f"{infanterie_wa_family}\n"
        f"{sniper_family}\n"
        f"{clu_sol_hefrag_family}\n"
        f"{nplm_bomb_family}\n"
        f"{nplm_bomb_flamme_family}\n"
        f"{pgb_bomb_family}\n"
        f"{manpad_hagru_family}\n"
        f"{manpad_tbagru_family}\n"
        f"{sam_hagru_family}\n"
        f"{sam_tbagru_family}\n"
        f"{a2a_hagru_family}\n"
        f"{a2a_tbagru_family}\n"
        f"{sa_intermediate_family}\n"
        f"{sa_full_family}\n"
        f"{twelve_seven_mm_family}\n"
        f"{fourteen_five_mm_family}\n"
        f"{missile_he_bigly_family}\n"
        f"{sead_missile_wa_family}\n"
        f"{sniper_double_family}\n"
        f"{sniper_triple_family}\n"
        f"{he_dca_airtargets_family}\n"
    )


def edit_gen_gp_gfx_damageresistancefamilylistimpl(source_path) -> None:
    """Add new damage families to DamageResistanceFamilyListImpl.ndf."""
    
    logger.info("Adding new damage families to implementation")
    # Define new families
    families = {
        "resistance": ['"ResistanceFamily_infanterieWA"'],
        "damage": [
            '"DamageFamily_sniper"',
            '"DamageFamily_sniper_double"',
            '"DamageFamily_sniper_triple"',
            '"DamageFamily_clu_sol_hefrag"',
            '"DamageFamily_nplm_bomb"',
            '"DamageFamily_nplm_bomb_flamme"',
            '"DamageFamily_pgb_bomb"',
            '"DamageFamily_manpad_hagru"',
            '"DamageFamily_manpad_tbagru"',
            '"DamageFamily_sam_hagru"',
            '"DamageFamily_sam_tbagru"',
            '"DamageFamily_a2a_hagru"',
            '"DamageFamily_a2a_tbagru"',
            '"DamageFamily_sa_intermediate"',
            '"DamageFamily_sa_full"',
            '"DamageFamily_12_7"',
            '"DamageFamily_14_5"',
            '"DamageFamily_missile_he_bigly"',
            '"DamageFamily_sead_missile_wa"',
            '"DamageFamily_he_dca_airtargets"',
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
        "sniper_double": ("(DamageFamily_sniper_double, 2)"),
        "sniper_triple": ("(DamageFamily_sniper_triple, 2)"),
        "clu_sol_hefrag": ("(DamageFamily_clu_sol_hefrag, 16)"),
        "nplm_bomb": ("(DamageFamily_nplm_bomb, 1)"),
        "nplm_bomb_flamme": ("(DamageFamily_nplm_bomb_flamme, 1)"),
        "pgb_bomb": ("(DamageFamily_pgb_bomb, 1)"),
        "manpad_hagru": ("(DamageFamily_manpad_hagru, 1)"),
        "manpad_tbagru": ("(DamageFamily_manpad_tbagru, 1)"),
        "sam_hagru": ("(DamageFamily_sam_hagru, 1)"),
        "sam_tbagru": ("(DamageFamily_sam_tbagru, 1)"),
        "a2a_hagru": ("(DamageFamily_a2a_hagru, 1)"),
        "a2a_tbagru": ("(DamageFamily_a2a_tbagru, 1)"),
        "sa_intermediate": ("(DamageFamily_sa_intermediate, 13)"),
        "sa_full": ("(DamageFamily_sa_full, 13)"),
        "12_7": ("(DamageFamily_12_7, 1)"),
        "14_5": ("(DamageFamily_14_5, 1)"),
        "missile_he_bigly": ("(DamageFamily_missile_he_bigly, 1)"),
        "sead_missile_wa": (f"(DamageFamily_sead_missile_wa, {SEAD_MISSILE_WA_LEVEL_COUNT})"),
        "he_dca_airtargets": ("(DamageFamily_he_dca_airtargets, 1)"),
    }

    for family_name, family_def in families.items():
        damage_family_list.add(family_def)
        logger.info(f"Added {family_name} family definition")

    values_list = resist_params_obj.by_m("Values").v

    he_dca_row_clone = _clone_existing_damage_row(values_list, _HE_DCA_ROW_INDEX)

    # Check array dimensions match expected constants
    last_row_index = len(values_list) - 1
    last_column_index = len(values_list[0].v) - 1

    if last_row_index != VANILLA_LAST_ROW or last_column_index != VANILLA_LAST_COLUMN:
        logger.warning(
            f"DAMAGE ARRAY DIMENSIONS DIFFER FROM EXPECTED!!! Expected "
            f"{VANILLA_LAST_ROW + 1} rows, {VANILLA_LAST_COLUMN + 1} columns, "
            f"got {last_row_index + 1} rows, {last_column_index + 1} columns"
        )

    sead_missile_wa_rows = _build_sead_missile_wa_rows(values_list)

    # Add damage values
    # CLU_SOL_HEFRAG rows are full per-level vectors; scale only infantry + infantry_wa cells
    # (flat layout: cols 40–42 infantry, 49–61 infantry_wa — see CLU_SOL_HEFRAG_FAMILY_ORDER).
    hefrag_infantry_cols = set(range(40, 43)) | set(range(49, 62))
    hefrag_m = CLU_HEFRAG_INFANTRY_FINAL_MULTIPLIER
    hefrag_rows = []
    for clu_row in CLU_SOL_HEFRAG:
        scaled_row = [
            round(v * hefrag_m, 2) if i in hefrag_infantry_cols else v
            for i, v in enumerate(clu_row)
        ]
        hefrag_rows.append(str(scaled_row))

    values_list.add(
        *[str(sniper) for sniper in SNIPER_DAMAGE],
        *[str(sniper) for sniper in SNIPER_DOUBLE_DAMAGE],
        *[str(sniper) for sniper in SNIPER_TRIPLE_DAMAGE],
        *hefrag_rows,
        str(NPLM_BOMB_DAMAGE),
        str(NPLM_BOMB_FLAMME_DAMAGE),
        str(PGB_BOMB_DAMAGE),
        str(MANPAD_HAGRU_DAMAGE),
        str(MANPAD_TBAGRU_DAMAGE),
        str(SAM_HAGRU_DAMAGE),
        str(SAM_TBAGRU_DAMAGE),
        str(A2A_HAGRU_DAMAGE),
        str(A2A_TBAGRU_DAMAGE),
        *[str(SA_INTERMEDIATE_DAMAGE_RATIOS + list(sa_damage)) for sa_damage in SA_INF_ARMOR_DAMAGE_RATIOS],
        *[str(SA_FULL_DAMAGE_RATIOS + list(sa_damage)) for sa_damage in SA_INF_ARMOR_DAMAGE_RATIOS],
        str(TWELVE_SEVEN_MM_DAMAGE),
        str(FOURTEEN_FIVE_MM_DAMAGE),
        str(MISSILE_HE_BIGLY_DAMAGE),
        *[str(row) for row in sead_missile_wa_rows],
        he_dca_row_clone,
    )
    logger.info(
        "Added damage values "
        f"(including DamageFamily_sead_missile_wa rows: {len(sead_missile_wa_rows)}, "
        f"DamageFamily_he_dca_airtargets cloned from row {_HE_DCA_ROW_INDEX})"
    )
    
    
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

    # Vanilla clu_sol_ap rows: match CLU_SOL_HEFRAG except infantry / infantry_wa handling (see damage_values).
    # Scale infantry cols 40–42 by AP multiplier; cols 49–61 are overwritten by _edit_infantry_armor.
    ap_infantry_cols = set(range(40, 43))
    ap_m = CLU_AP_INFANTRY_FINAL_MULTIPLIER
    for row_idx, ap_row in zip(range(CLU_SOL_AP_ROW_FIRST, CLU_SOL_AP_ROW_LAST + 1), CLU_SOL_AP):
        dmg_row = damage_array[row_idx]
        for col, val in enumerate(ap_row):
            scaled = round(val * ap_m, 2) if col in ap_infantry_cols else val
            dmg_row.v.replace(col, str(scaled))
        logger.info(f"Applied clu_sol_ap full row for index {row_idx}")

        
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


def _build_sead_missile_wa_rows(damage_array) -> list[list[float]]:
    """Clone vanilla ap_missile levels and apply WA-SEAD infantry overrides."""
    sead_rows = []
    for row_idx in range(AP_MISSILE_ROW_FIRST, AP_MISSILE_ROW_LAST + 1):
        base_row = [float(value.v) for value in damage_array[row_idx].v]
        if row_idx != AP_MISSILE_ROW_LAST:
            base_row[SEAD_INFANTRY_ARMOR_LEVEL_ONE_COLUMN] = SEAD_RATIO_VS_INFANTRY
            for column in SEAD_WA_INFANTRY_ARMOR_COLUMNS:
                base_row[column] = SEAD_RATIO_VS_INFANTRY
        sead_rows.append(base_row)

    if len(sead_rows) != SEAD_MISSILE_WA_LEVEL_COUNT:
        logger.warning(
            "DamageFamily_sead_missile_wa row count mismatch: "
            f"expected {SEAD_MISSILE_WA_LEVEL_COUNT}, got {len(sead_rows)}"
        )
    return sead_rows


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