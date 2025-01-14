"""Functions for modifying weapon damage families."""

from src.constants.weapons.damage_edits import (
    DAMAGE_EDITS,
    FMBALLE_INFANTRY_EDITS,
    FMBALLE_ROWS,
    INFANTRY_ARMOR_EDITS,
)
from src.constants.weapons.damage_values import (
    DPICM_DAMAGES,
    FULL_BALL_DAMAGE,
    SNIPER_DAMAGE,
)
from src.constants.weapons.weapon_descriptions import weapon_descriptions
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def add_damage_families_to_list(source) -> None:
    """Add new damage families to DamageResistanceFamilyList.ndf."""
    logger.info("Adding new damage families to list")
    
    # Count existing families
    i = -1  # Damage families counter
    j = -1  # Resistance families counter
    for row in source:
        if row.namespace.startswith("DamageFamily_"):
            i += 1
        elif row.namespace.startswith("ResistanceFamily_"):
            j += 1
    
    # Add new families
    infanterie_wa_family = f"ResistanceFamily_infanterieWA is {j + 1}"
    sniper_family = f"DamageFamily_sniper is {i + 1}"
    full_ball_family = f"DamageFamily_full_balle is {i + 2}"
    dpicm_family = f"DamageFamily_dpicm is {i + 3}"
    
    source.insert(j + 1, infanterie_wa_family)
    source.add(sniper_family)
    source.add(full_ball_family)
    source.add(dpicm_family)
    
    logger.info(f"Added families: {infanterie_wa_family}, {sniper_family}, {full_ball_family}, {dpicm_family}")


def add_damage_families_to_impl(source) -> None:
    """Add new damage families to DamageResistanceFamilyListImpl.ndf."""
    logger.info("Adding new damage families to implementation")
    
    # Define new families
    families = {
        "resistance": ['"ResistanceFamily_infanterieWA"'],
        "damage": [
            '"DamageFamily_sniper"',
            '"DamageFamily_full_balle"',
            '"DamageFamily_dpicm"'
        ]
    }
    
    # Add resistance families
    resistance_values = source.by_n("Generated_ResistanceFamily_Enum").v.by_m("Values").v
    for family in families["resistance"]:
        resistance_values.add(family)
        logger.info(f"Added resistance family: {family}")
    
    # Add damage families
    damage_values = source.by_n("Generated_DamageFamily_Enum").v.by_m("Values").v
    for family in families["damage"]:
        damage_values.add(family)
        logger.info(f"Added damage family: {family}")


def apply_damage_families(source, ammo_db: dict) -> None:
    """Apply damage family modifications to weapons."""
    for weapon_descr in source:
        if weapon_descr.n in ammo_db["full_ball_weapons"]:
            arme_obj = weapon_descr.v.by_m("Arme").v
            arme_obj.by_m("Family").v = "DamageFamily_full_balle"
            logger.info(f"Changed {weapon_descr.n} to DamageFamily_full_balle")
            
        elif weapon_descr.n in ammo_db["sniper_weapons"]:
            arme_obj = weapon_descr.v.by_m("Arme").v
            arme_obj.by_m("Family").v = "DamageFamily_sniper"
            logger.info(f"Changed {weapon_descr.n} to DamageFamily_sniper")
            
            # Update description token
            type_cat = weapon_descr.v.by_m("TypeCategoryName").v
            for weapon_type, ((cat_hash, desc_hash), _) in weapon_descriptions.items():
                if type_cat == cat_hash:
                    weapon_descr.v.by_m("WeaponDescriptionToken").v = f"'{desc_hash}'"
                    logger.info(f"Changed {weapon_descr.n} description to {weapon_type} ({desc_hash})")
                    break 


def add_damage_resistance_values(source) -> None:
    """Add damage resistance values to DamageResistance.ndf."""
    logger.info("Adding damage resistance values")
    
    # Get resistance params
    resist_params_obj = source.by_n("DamageResistanceParams").v
    
    # Add family definitions
    damage_family_list = resist_params_obj.by_m("DamageFamilyDefinitionList").v
    families = {
        "sniper": "TDamageTypeFamilyDefinition(Family=DamageFamily_sniper MaxIndex=1)",
        "full_ball": "TDamageTypeFamilyDefinition(Family=DamageFamily_full_balle MaxIndex=1)",
        "dpicm": "TDamageTypeFamilyDefinition(Family=DamageFamily_dpicm MaxIndex=4)",
    }
    
    for family_name, family_def in families.items():
        damage_family_list.add(family_def)
        logger.info(f"Added {family_name} family definition")
    
    # Add damage values
    values_list = resist_params_obj.by_m("Values").v
    values_list.add(
        str(SNIPER_DAMAGE),
        str(FULL_BALL_DAMAGE),
        *[str(dpicm) for dpicm in DPICM_DAMAGES]
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


def apply_damage_family_edits(source) -> None:
    """Apply damage family edits to DamageResistance.ndf."""
    logger.info("Applying damage family edits")
    
    # Get damage params
    damage_params_obj = source.by_n("DamageResistanceParams").v
    
    # Add new infantry resistance family
    resistance_list = damage_params_obj.by_m("ResistanceFamilyDefinitionList").v
    resistance_list.add(
        "TResistanceTypeFamilyDefinition(Family=ResistanceFamily_infanterieWA MaxIndex=13)")
    logger.info("Added infantry resistance family")
    
    # Extend damage array with new columns
    damage_array = damage_params_obj.by_m("Values").v
    for row in damage_array:
        for _ in range(13):
            row.v.add("0.0")
    logger.info("Extended damage array with 13 new columns")
    
    # Apply damage edits
    for weapon_type, data in DAMAGE_EDITS.items():
        apply_damage_array_edits(damage_array, data["row"], data["edits"])
        logger.info(f"Applied damage edits for {weapon_type}") 


def edit_infantry_armor(source) -> None:
    """Edit infantry armor values in DamageResistance.ndf."""
    logger.info("Editing infantry armor values")
    
    damage_params_obj = source.by_n("DamageResistanceParams").v
    damage_array = damage_params_obj.by_m("Values").v

    # Apply infantry armor edits
    for i, row in enumerate(damage_array):
        if i in INFANTRY_ARMOR_EDITS:
            damage_ratio, damage_family = INFANTRY_ARMOR_EDITS[i]
            for column in range(49, 62):  # WA Infantry columns
                row.v.replace(column, str(damage_ratio))
                logger.info(f"Edited row {i}, family {damage_family}, column {column} to {damage_ratio}")

    # Apply FMballe infantry damage edits
    for row_index in FMBALLE_ROWS:
        apply_damage_array_edits(damage_array, row_index, FMBALLE_INFANTRY_EDITS)
        logger.info(f"Applied FMballe infantry edits to row {row_index}") 