"""Functions for modifying unit optics."""

from typing import List, Tuple

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# SEAD units and their anti-radiation optics ranges
SEAD_UNITS: List[Tuple[str, float]] = [
    ("Buccaneer_S2B_SEAD_UK", 1700.0),  # Martel 5250m
    ("EF111_Raven_US", 2150.0),  # EW
    ("F16E_SEAD_US", 2150.0),  # AGM-88 5950m
    ("F4_Wild_Weasel_US", 1850.0),  # AGM-45 5000m
    ("Jaguar_SEAD2_FR", 1850.0),  # Armat 5775mm
    ("Jaguar_SEAD_FR", 1700.0),  # Martel 5250m
    ("MiG_25BM_SOV", 2150.0),  # Kh-58U 6300m
    ("MiG_27M_sead_SOV", 1850.0),  # Kh-28 5425m
    ("Mirage_IV_SEAD_FR", 1700.0),  # Marterl 5250m
    ("Su_22_SEAD_DDR", 1850.0),  # Kh-28 5425m
    ("Su_24MP_EW_SOV", 2150.0),  # EW
    ("Su_24MP_SOV", 1850.0),  # Kh-28 5425m
    ("Tornado_ADV_SEAD_UK", 2000.0),  # ALARM 5600m
]


def edit_antirad_optics(source_path) -> None:
    """Edit anti-radiation optics in UniteDescriptor.ndf."""
    logger.info("Modifying anti-radiation optics")
    
    for unit_descr in source_path:
        for unit, optics in SEAD_UNITS:
            if unit_descr.namespace.removeprefix("Descriptor_Unit_") != unit:
                continue
                
            modules_list = unit_descr.v.by_m("ModulesDescriptors").v
            for module in modules_list:
                if not hasattr(module.v, 'type'):
                    continue
                    
                if module.v.type != "TScannerConfigurationDescriptor":
                    continue
                
                # Update optics ranges
                module.v.by_m("PorteeVisionGRU").v = "7000"
                special_optics_map = module.v.by_m("SpecializedOpticalStrengths").v
                special_optics_map.by_k("EVisionUnitType/AntiRadar").v = str(optics)
                
                logger.info(
                    f"Updated {unit} optics: ground=7000m, anti-radar={optics}m"
                )
                break 