"""Functions for modifying unit optics."""

from typing import List, Tuple

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# SEAD units and their anti-radiation optics ranges
# different radar optic strength is unnecessary if we don't want forest to matter.
# ground optic ranges are basically their missile range + 1000m, but I
# want to model them more accurately in the future (e.g. like the Weasel).
# SEAD_UNITS: List[Tuple[str, float]] = [
    # unit, ground_range, radar_optic_strength
#     ("Buccaneer_S2B_SEAD_UK", 6300, 1700.0),  # Martel 5250m
#     ("EF111_Raven_US", 8000, 2150.0),  # EW
#     ("F16E_SEAD_US", 7000,2150.0),  # AGM-88 5950m
#     # weasel had better radar apparently, so bumping its ground range.
#     ("F4_Wild_Weasel_US", 6825, 1850.0),  # AGM-45 5250m (should be 5000m)
#     ("Jaguar_SEAD2_FR", 6825, 1850.0),  # Armat 5775mm
#     ("Jaguar_SEAD_FR", 6300, 1700.0),  # Martel 5250m
#     ("MiG_25BM_SOV", 7350, 2150.0),  # Kh-58U 6300m
#     ("MiG_27M_sead_SOV", 6475,1850.0),  # Kh-28 5425m
#     ("Mirage_IV_SEAD_FR", 6300, 1700.0),  # Martel 5250m
#     ("Su_22_SEAD_DDR", 6475, 1850.0),  # Kh-28 5425m
#     ("Su_24MP_EW_SOV", 8000, 2150.0),  # EW
#     ("Su_24MP_SOV", 6475,1850.0),  # Kh-28 5425m
#     ("Tornado_ADV_SEAD_UK", 6650, 2000.0),  # ALARM 5600m
# ]

SEAD_UNITS: List[Tuple[str, float]] = [
    ("Buccaneer_S2B_SEAD_UK", 10000, 5000.0),  # Martel 5250m
    ("EF111_Raven_US", 10000, 5000.0),  # EW
    ("F16E_SEAD_US", 10000, 5000.0),  # AGM-88 5950m
    ("F4_Wild_Weasel_US", 10000, 5000.0),  # AGM-45 5250m (should be 5000m missile range probably)
    ("Jaguar_SEAD2_FR", 10000, 5000.0),  # Armat 5775mm
    ("Jaguar_SEAD_FR", 10000, 5000.0),  # Martel 5250m
    ("MiG_25BM_SOV", 10000, 5000.0),  # Kh-58U 6300m
    ("MiG_27M_sead_SOV", 10000, 5000.0),  # Kh-28 5425m
    ("Mirage_IV_SEAD_FR", 10000, 5000.0),  # Martel 5250m
    ("Su_22_SEAD_DDR", 10000, 5000.0),  # Kh-28 5425m
    ("Su_24MP_EW_SOV", 10000, 5000.0),  # EW
    ("Su_24MP_SOV", 10000, 5000.0),  # Kh-28 5425m
    ("Tornado_ADV_SEAD_UK", 10000, 5000.0),  # ALARM 5600m
]


def edit_antirad_optics(source_path) -> None:
    """Edit anti-radiation optics in UniteDescriptor.ndf."""
    logger.info("Modifying anti-radiation optics")
    
    for unit_descr in source_path:
        for unit, ground_range, radar_optic_strength in SEAD_UNITS:
            if unit_descr.namespace.removeprefix("Descriptor_Unit_") != unit:
                continue
                
            modules_list = unit_descr.v.by_m("ModulesDescriptors").v
            for module in modules_list:
                if not hasattr(module.v, 'type'):
                    continue
                    
                if module.v.type != "TScannerConfigurationDescriptor":
                    continue
                
                # Update optics ranges
                module.v.by_m("PorteeVisionGRU").v = str(ground_range)
                special_optics_map = module.v.by_m("SpecializedOpticalStrengths").v
                special_optics_map.by_k("EVisionUnitType/AntiRadar").v = "5000.0"
                
                logger.info(
                    f"Updated {unit} optics: ground={ground_range}m, anti-radar=5000m"
                )
                break 