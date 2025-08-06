"""Functions for modifying unit effects."""

import ast  # noqa
import ndf_parse as ndf
from typing import List, Tuple  # noqa

from src import ModConfig  # noqa
from src.constants.effects.capacities import (
    CHOC_MOVE_CAPACITY,
    CHOC_MOVE_EFFECT,
    CHOC_MOVE_OK_EFFECT,
    CONDITIONS,
    DEPLOY_CAPACITY,
    DEPLOY_EFFECT,
    DEPLOY_OK_CAPACITY,
    DEPLOY_OK_EFFECT,
    NO_CHOC_MOVE_CAPACITY,
    NO_CHOC_MOVE_EFFECT,
    NO_CHOC_MOVE_MORALE_EFFECT,
    NO_SWIFT_CAPACITY,
    NO_SWIFT_EFFECT,
    SWIFT_CAPACITY,
    SWIFT_EFFECT,
    SWIFT_OK_EFFECT,
)
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes

logger = setup_logger(__name__)


def edit_damage_levels(source_path) -> None:
    """Edit damage levels in DamageLevels.ndf."""
    logger.info("Modifying damage levels")

    # edit GroundUnits_packSupp
    ground_units_pack_supp = source_path.by_n("DamageLevelsPackDescriptor_GroundUnits_packSupp")
    damage_levels = ground_units_pack_supp.v.by_m("DamageLevelsDescriptors")
    new_guids = [
        "GUID:{bbac0511-7b05-4e67-b98c-10bf88155513}",
        "GUID:{1762d8ea-dff5-4a67-95aa-79da6ebe6f60}",
        "GUID:{81d85239-87d0-4ceb-a10f-87b7ad2b651e}",
        "GUID:{0af3ae31-ed12-4673-a74a-8ebf051d8e5a}",
        "GUID:{2d5b31c5-6e74-4241-acca-71231459751d}",
        "GUID:{e9acc10d-bf26-4ba7-ab16-a43b2904e6db}",
    ]
    guid_index = 0
    for level in damage_levels.v:

        value = level.v.by_m("Value")
        effects_packs = level.v.by_m("EffectsPacks")
        if value.v == "0":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_no_Choc_Move_Morale")
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_Swift_ok")

        elif value.v == "0.1":
            pass

        elif value.v == "0.25":
            pass

        elif value.v == "0.5":
            pass

        elif value.v == "0.75":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_no_Choc_Move_Morale")

        elif value.v == "0.8":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_no_Choc_Move_Morale")


def edit_conditions(source_path) -> None:
    """Edit conditions in ConditionsList.ndf."""
    logger.info("Modifying conditions")

    for condition in CONDITIONS:
        source_path.add(condition)


def edit_shock_effects(source_path) -> None:
    """Edit effects in EffetsSurUnite.ndf."""
    logger.info("Modifying Shock Trait effects")

    # Add new shock effects
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "UnitEffect_Choc":
            source_path.insert(i, CHOC_MOVE_EFFECT)
            source_path.insert(i, NO_CHOC_MOVE_EFFECT)
            source_path.insert(i, NO_CHOC_MOVE_MORALE_EFFECT)
            source_path.insert(i, SWIFT_EFFECT)
            source_path.insert(i, NO_SWIFT_EFFECT)
            source_path.insert(i, CHOC_MOVE_OK_EFFECT)
            source_path.insert(i, SWIFT_OK_EFFECT)
            source_path.insert(i, DEPLOY_OK_EFFECT)
            source_path.insert(i, DEPLOY_EFFECT)
            logger.info("Added shock movement effects")
            break

    # Modify sniper effects
    sniper_obj = source_path.by_n("UnitEffect_sniper")
    effects_list = sniper_obj.v.by_m("EffectsDescriptors")

    for effect in effects_list.v:
        if not hasattr(effect.v, "type"):
            continue

        if effect.v.type == "TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor":
            effects_list.v.remove(effect.index)
            logger.info(f"Removed sniper damage bonus from {sniper_obj.v.parent_row.namespace}")
            break

    # Modify stress on miss
    stress_on_miss_objects = [
        ("UnitEffect_stressOnMiss_high", 140),
        ("UnitEffect_stressOnMiss_low", 80),
        ("UnitEffect_stressOnMiss_mid", 110),
    ]

    # Edit stress on miss effects
    for effect_name, suppress_damage in stress_on_miss_objects:
        stress_on_miss_obj = source_path.by_n(effect_name)
        effects_list = stress_on_miss_obj.v.by_m("EffectsDescriptors")
        for effect in effects_list.v:
            if not hasattr(effect.v, "type"):
                continue

            if effect.v.type == "TEffectInflictSuppressDamageDescriptor":
                effect.v.by_m("SuppressDamageValue").v = str(suppress_damage)
                logger.info(f"Updated {effect_name.replace('UnitEffect_', '')} effect to " f"{suppress_damage}")
                break


# I think Eugen removed this file?
# def edit_shock_effects_packs_list(source_path) -> None:
#     """Edit shock effects in EffectsPacksList.ndf."""
#     logger.info("Modifying Shock Trait effects in packs list")

#     choc_move = "~/UnitEffect_Choc_move"
#     choc_move_GSR = "~/UnitEffect_Choc_move_GSR"
#     choc_tag_no_move = "~/UnitEffect_Ajoute_Tag_no_Choc_move"

#     effectspacks_list = source_path.by_n("EffectsPacksList").v.by_m("EffectsPacks").v

#     for i, row in enumerate(effectspacks_list):
#         if row.v == "~/UnitEffect_Ajoute_Tag_snipe_ok":
#             gsr_ok_index = i
#         if row.v == "~/UnitEffect_Choc":
#             effectspacks_list.insert(gsr_ok_index, choc_tag_no_move)
#             logger.info("Added no_Choc_move effect to packs list")

#             effectspacks_list.insert(i + 1, choc_move)
#             effectspacks_list.insert(i + 1, choc_move_GSR)
#             logger.info("Added Choc_move and Choc_move_GSR effects to packs list")
#             break


def edit_capacite_list(source_path) -> None:
    """Edit capacities in CapaciteList.ndf."""
    logger.info("Modifying Trait effects in capacite list")

    # Edit capacities
    for capacite_descr in source_path:
        if capacite_descr.n == "Capacite_Choc":
            capacite_descr.v.by_m("RangeGRU").v = "100"
            logger.info("Updated Capacite_Choc range to 100")

        elif capacite_descr.n == "Capacite_electronic_warfare":
            capacite_descr.v.by_m("RangeGRU").v = "5000"
            logger.info("Updated Capacite_electronic_warfare range to 5000")

    # Add new capacities
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "Capacite_Choc":
            source_path.insert(i, CHOC_MOVE_CAPACITY)
            source_path.insert(i, NO_CHOC_MOVE_CAPACITY)
            source_path.insert(i, SWIFT_CAPACITY)
            source_path.insert(i, NO_SWIFT_CAPACITY)
            source_path.insert(i, DEPLOY_OK_CAPACITY)
            source_path.insert(i, DEPLOY_CAPACITY)
            logger.info("Added shock movement capacities")
            break


def edit_shock_units(source_path, game_db) -> None:
    """Add shock movement capabilities to shock units in UniteDescriptor.ndf."""
    logger.info("Adding shock movement capabilities to units")

    units_modified = 0

    for unit_name, unit_data in game_db["unit_data"].items():
        if "skills" not in unit_data or "specialties" not in unit_data:
            continue

        shock_attributes = [
            "Choc" in unit_data["skills"],
            "_gsr" not in unit_data["specialties"],
        ]

        shock_gsr_attributes = [
            "Choc" in unit_data["skills"],
            "_gsr" in unit_data["specialties"],
        ]

        if not any(shock_attributes) and not any(shock_gsr_attributes):
            continue

        unit_descr = source_path.by_n(f"Descriptor_Unit_{unit_name}")
        modules_list = unit_descr.v.by_m("ModulesDescriptors").v

        # TODO: GSR units no longer need special handling
        for descr_row in modules_list:
            if not hasattr(descr_row.v, "type"):
                continue

            if descr_row.v.type != "TCapaciteModuleDescriptor":
                continue

            default_skill_list = descr_row.v.by_m("DefaultSkillList").v

            if all(shock_attributes):
                default_skill_list.add("$/GFX/EffectCapacity/Capacite_Choc_Move")
                # skill_list.add("$/GFX/EffectCapacity/Capacite_Choc_Move_cooldown")
                default_skill_list.add("$/GFX/EffectCapacity/Capacite_no_Choc_Move")
                logger.info(f"Added shock movement capacities to {unit_name}")
                units_modified += 1

            elif all(shock_gsr_attributes):
                default_skill_list.add("$/GFX/EffectCapacity/Capacite_Choc_Move")
                # skill_list.add("$/GFX/EffectCapacity/Capacite_Choc_Move_cooldown")
                default_skill_list.add("$/GFX/EffectCapacity/Capacite_no_Choc_Move")
                # logger.info(f"Added GSR shock movement capacity to {unit_name}")
                units_modified += 1
                break

    logger.info(f"Total units modified: {units_modified}")


def add_swift_capacity(source_path) -> None:
    """Add swift capacity to units in UniteDescriptor.ndf"""
    logger.info("Adding swift capacity to units")

    unit_edits = load_unit_edits()

    for unit, data in unit_edits.items():

        add_swift = False

        if "SpecialtiesList" not in data:
            continue
        if "add_specs" not in data["SpecialtiesList"]:
            continue

        for trait in data["SpecialtiesList"]["add_specs"]:
            if trait == "'_swift'":
                add_swift = True
                break

        if not add_swift:
            continue

        unit_descr = source_path.by_n(f"Descriptor_Unit_{unit}")
        modules_list = unit_descr.v.by_m("ModulesDescriptors")
        found_capacite_module = False
        for module in modules_list.v:

            if not isinstance(module.v, ndf.model.Object):
                continue

            if module.v.type != "TCapaciteModuleDescriptor":
                continue

            default_skill_list = module.v.by_m("DefaultSkillList").v

            found_capacite_module = True

            default_skill_list.add("$/GFX/EffectCapacity/Capacite_Swift")
            default_skill_list.add("$/GFX/EffectCapacity/Capacite_no_Swift")
            logger.info(f"Added swift capacity to {unit}")
            break

        if not found_capacite_module:
            new_entry = (
                f"TCapaciteModuleDescriptor"
                f"("
                f"    DefaultSkillList = ["
                f"        $/GFX/EffectCapacity/Capacite_Swift,"
                f"        $/GFX/EffectCapacity/Capacite_no_Swift,"
                f"    ]"
                f")"
            )
            production_module_index = modules_list.v.find_by_cond(
                lambda x: isinstance(x.v, ndf.model.Object) and x.v.type == "TProductionModuleDescriptor"
            )
            modules_list.v.insert(production_module_index, new_entry)
            logger.info(f"(add_swift_capacity) Added capacity module to {unit}")
            logger.info(f"(add_swift_capacity) Added swift capacity to {unit}")


def edit_capacities(source_path) -> None:
    """Edit capacities in CapaciteList.ndf."""
    logger.info("Modifying unit capacities in UniteDescriptor.ndf")

    unit_edits = load_unit_edits()

    # Edit capacities
    for unit, data in unit_edits.items():
        if "capacities" not in data:
            continue

        found_capacite_module = False
        capacities_to_add = data["capacities"].get("add_capacities", [])
        capacities_to_remove = data["capacities"].get("remove_capacities", [])

        unit_descr = source_path.by_n(f"Descriptor_Unit_{unit}")
        modules_list = unit_descr.v.by_m("ModulesDescriptors")

        for module in modules_list.v:
            if not isinstance(module.v, ndf.model.Object):
                continue

            if module.v.type == "TProductionModuleDescriptor":
                insert_index = module.index

            if module.v.type != "TCapaciteModuleDescriptor":
                continue

            default_skill_list = module.v.by_m("DefaultSkillList").v
            found_capacite_module = True
            skill_prefix = "$/GFX/EffectCapacity/Capacite_"
            for skill in default_skill_list:
                if skill.v.replace(skill_prefix, "") in capacities_to_remove:
                    default_skill_list.remove(skill.index)
            for skill in capacities_to_add:
                default_skill_list.add(skill_prefix + skill)

        if not found_capacite_module:
            skill_prefix = "$/GFX/EffectCapacity/Capacite_"
            new_entry = (
                f"TCapaciteModuleDescriptor"
                f"("
                f"        DefaultSkillList = ["
                f'            {", ".join(skill_prefix + skill for skill in capacities_to_add)}'
                f"        ]"
                f")"
            )
            modules_list.v.insert(insert_index, new_entry)
            logger.info(f"(edit_capacities) Added capacity module to {unit}")
