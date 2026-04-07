"""Functions for modifying TerrainSpeedFactors.ndf (infantry / vehicle terrain speed MAPs)."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Same gameplay intent as former Terrains.ndf SpeedModifierInfantry on TGameplayTerrain (now per-type factors).
INFANTRY_TERRAIN_SPEED_OVERRIDES = {
    "~/ETerrainType/ForetLegere": 1.0,
    "~/ETerrainType/PetitBatiment": 1.0,
    "~/ETerrainType/Batiment": 1.0,
    "~/ETerrainType/Ruin": 0.7,
}


def edit_gameplay_constantes_terrainspeedfactors(source_path) -> None:
    """GameData/Gameplay/Constantes/TerrainSpeedFactors.ndf"""
    logger.info("Editing TerrainSpeedFactors (infantry speed factors)")

    infantry = source_path.by_n("InfantryTerrainSpeedFactors")
    speed_map = infantry.v.by_m("SpeedFactorPerTerrainType").v

    for terrain_key, factor in INFANTRY_TERRAIN_SPEED_OVERRIDES.items():
        row = speed_map.by_key(terrain_key, False)
        if row is None:
            logger.warning("Terrain speed row not found for %s", terrain_key)
            continue
        row.v = str(factor)
        logger.info("Set infantry speed factor %s = %s", terrain_key, factor)
