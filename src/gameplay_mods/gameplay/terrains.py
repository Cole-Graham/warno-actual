"""Functions for modifying Terrains.ndf"""

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes, find_obj_by_type, is_obj_type

logger = setup_logger(__name__)


def edit_gameplay_terrains(source_path) -> None:
    """GameData/Gameplay/Terrains/Terrains.ndf"""
    logger.info("Editing terrain properties")

    # New damage families: append full (DamageFamily, resistance MAP) rows to terrains.
    # Existing families: patch resistance values on rows already present in vanilla.
    # Kept as two dicts because the NDF operations differ (add vs in-place edit).
    damage_family_additions = {
        "12_7": {
            "ForetDense": 0.5,
            "ForetLegere": 0.65,
            "PetitBatiment": 0.5,
            "Batiment": 0.5,
            "Ruin": 0.55,
        },
        "14_5": {
            "ForetDense": 0.5,
            "ForetLegere": 0.65,
            "PetitBatiment": 0.5,
            "Batiment": 0.5,
            "Ruin": 0.55,
        },
        "sa_intermediate": {
            "ForetDense": 0.5,
            "ForetLegere": 0.65,
            "PetitBatiment": 0.5,
            "Batiment": 0.5,
            "Ruin": 0.55,
        },
        "sa_full": {
            "ForetDense": 0.5,
            "ForetLegere": 0.65,
            "PetitBatiment": 0.5,
            "Batiment": 0.5,
            "Ruin": 0.55,
        },
        "thermobarique": {
            "ForetDense": 1.0,
            "ForetLegere": 1.0,
            "PetitBatiment": 1.0,
            "Batiment": 1.0,
            "Ruin": 1.0,
        },
        "pgb_bomb": {
            "ForetDense": 0.5,
            "ForetLegere": 0.65,
            "PetitBatiment": 0.5,
            "Batiment": 0.5,
            "Ruin": 0.55,
        },
        "roquette_ap": {
            "ForetDense": 0.5,
            "ForetLegere": 0.65,
            "PetitBatiment": 0.5,
            "Batiment": 0.5,
            "Ruin": 0.55,
        },
    }

    damage_family_edits = {
        "howz": {
            "PetitBatiment": 0.25,
            "Batiment": 0.25,
        },
        "howz_bombe": {
            "PetitBatiment": 0.25,
            "Batiment": 0.25,
        },
    }

    # SpeedModifierInfantry moved to GameData/Gameplay/Constantes/TerrainSpeedFactors.ndf
    # (InfantryTerrainSpeedFactors); see constantes/terrainspeedfactors.py
    other_modifications = {
        "ForetLegere": {
            "DissimulationModifierGroundAir": 12,
            "DissimulationModifierGroundGround": 12,
            "ConcealmentBonus": 2.5,
        },
        "PetitBatiment": {
            "ConcealmentBonus": 3.25,
        },
        "Batiment": {
            "ConcealmentBonus": 3.25,
        },
        "Ruin": {
            "DissimulationModifierGroundAir": 48,
            "ConcealmentBonus": 2.5,
        },
    }

    tgameplayterrainsregistration_template = find_obj_by_type(
        source_path, "TGameplayTerrainsRegistration")

    terrains_list = tgameplayterrainsregistration_template.v.by_m("Terrains")

    # First: for every terrain, each (DamageFamily, inner MAP) row — if there is
    # ResistanceFamily_infanterie, ensure ResistanceFamily_infanterieWA exists with the same value.
    for terrain_obj in terrains_list.v:
        if not is_obj_type(terrain_obj.v, "TGameplayTerrain"):
            continue

        damage_modifier_map = terrain_obj.v.by_m("DamageModifierPerFamilyAndResistance", False)
        if damage_modifier_map is None:
            continue

        logger.info("Ensuring infanterieWA mirrors for %s", terrain_obj.namespace)

        for damage_entry in damage_modifier_map.v:
            res_map = damage_entry.v
            inf_resistance = res_map.by_k("ResistanceFamily_infanterie", False)
            if inf_resistance is None:
                continue
            if res_map.by_k("ResistanceFamily_infanterieWA", False) is not None:
                continue

            res_map.add(f"(ResistanceFamily_infanterieWA, {inf_resistance.v})")
            logger.info(
                "Added ResistanceFamily_infanterieWA to %s on %s with value %s",
                damage_entry.k,
                terrain_obj.namespace,
                inf_resistance.v,
            )

    for damage_family, terrain_modifiers in damage_family_additions.items():
        for terrain_name, modifier in terrain_modifiers.items():
            terrain_obj = terrains_list.v.find_by_cond(
                lambda o, terrain_name=terrain_name: is_obj_type(o.v, "TGameplayTerrain") and
                strip_quotes(o.v.by_m("Name").v) == terrain_name, strict=False)

            if not terrain_obj:
                logger.warning(f"Terrain {terrain_name} not found")
                continue

            damage_modifier_map = terrain_obj.v.by_m("DamageModifierPerFamilyAndResistance")

            damage_family_key = f"DamageFamily_{damage_family}"
            if damage_modifier_map.v.by_k(damage_family_key, False) is not None:
                logger.error(
                    "%s already has modifiers on %s; skipping addition",
                    damage_family_key,
                    terrain_name,
                )
                continue

            damage_modifier_map.v.add(
                f"({damage_family_key}, MAP ["
                f"(ResistanceFamily_infanterie,{modifier}),"
                f"(ResistanceFamily_infanterieWA,{modifier})])",
            )
            logger.info(
                f"Added {damage_family} damage modifier {modifier} to {terrain_name} "
                "(infanterie + infanterieWA)",
            )

    for damage_family, terrain_modifiers in damage_family_edits.items():
        for terrain_name, modifier in terrain_modifiers.items():
            terrain_obj = terrains_list.v.find_by_cond(
                lambda o, terrain_name=terrain_name: is_obj_type(o.v, "TGameplayTerrain") and
                strip_quotes(o.v.by_m("Name").v) == terrain_name, strict=False)

            if not terrain_obj:
                logger.warning(f"Terrain {terrain_name} not found")
                continue

            damage_modifier_map = terrain_obj.v.by_m("DamageModifierPerFamilyAndResistance", False)
            if damage_modifier_map is None:
                logger.warning(
                    f"No DamageModifierPerFamilyAndResistance on {terrain_name}",
                )
                continue

            damage_entry = damage_modifier_map.v.by_k(f"DamageFamily_{damage_family}", False)
            if damage_entry is None:
                logger.warning(
                    f"DamageFamily_{damage_family} not found on {terrain_name}",
                )
                continue

            res_map = damage_entry.v
            for res_entry in res_map:
                res_entry.v = str(modifier)
                logger.info(
                    f"Updated {damage_family} {res_entry.k} damage modifier to {modifier} "
                    f"on {terrain_name}",
                )

    for terrain_name, modifier in other_modifications.items():
        terrain_obj = terrains_list.v.find_by_cond(
            lambda o, terrain_name=terrain_name: is_obj_type(o.v, "TGameplayTerrain") and
            strip_quotes(o.v.by_m("Name").v) == terrain_name, strict=False)

        if not terrain_obj:
            logger.warning(f"Terrain {terrain_name} not found")
            continue

        for modifier_name, modifier_value in modifier.items():
            terrain_obj.v.by_m(modifier_name).v = str(modifier_value)
            logger.info(f"Updated {terrain_name} {modifier_name} to {modifier_value}")
