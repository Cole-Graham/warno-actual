"""Unit edit constants."""

import importlib
from pathlib import Path
from typing import Dict

from src.utils.logging_utils import setup_logger

logger = setup_logger('dics')


def load_unit_edits() -> Dict:
    """Load and merge all unit edit dictionaries."""
    merged_edits = {}
    
    logger.info("Loading unit edit dictionaries...")
    
    # Dictionary name mapping
    dict_names = {
        'FR_unit_edits': 'fr_unit_edits',
        'POL_unit_edits': 'pol_unit_edits',
        'RDA_unit_edits': 'rda_unit_edits',
        'RFA_unit_edits': 'rfa_unit_edits',
        'SOV_unit_edits': 'sov_unit_edits',
        # 'SUPPLY_unit_edits': 'supply_unit_edits', decided not to merge supply edits for now
        'UK_unit_edits': 'uk_unit_edits',
        'USA_unit_edits': 'usa_unit_edits'
    }
    
    # Load dictionaries
    dics_path = Path(__file__).parent
    for file in dics_path.glob("*unit_edits.py"):
        module_name = f"src.constants.unit_edits.{file.stem}"
        logger.debug(f"Processing {file.stem}")
        
        try:
            module = importlib.import_module(module_name)
            dict_name = dict_names.get(file.stem)
            if dict_name and hasattr(module, dict_name):
                merged_edits.update(getattr(module, dict_name))
                logger.info(f"Loaded unit edits from {file.stem}")
        except Exception as e:
            logger.error(f"Failed to load {file.stem}: {str(e)}")
    
    logger.info(f"Loaded edits for {len(merged_edits)} units total")

    # parse dictionary for shared/borrowed values in specific fields
    for unit in merged_edits:
        for field in ("CommandPoints",):
            if field in merged_edits[unit] and type(merged_edits[unit][field]) == str:
                ref_unit = merged_edits[unit].get(field, None)
                if ref_unit in merged_edits and field in merged_edits[ref_unit]:
                    merged_edits[unit][field] = merged_edits[ref_unit][field]
                    logger.info(f"Retrieved referenced \"{field}\" value for unit {unit} from unit {ref_unit}")
                else:
                    merged_edits[unit].pop(field)

    return merged_edits


def load_depiction_edits() -> Dict:
    """Load and merge all depiction edit dictionaries."""
    merged_edits = {}
    
    logger.info("Loading depiction edit dictionaries...")

    # Dictionary of faction modules to import
    faction_modules = {
        'POL': 'src.constants.unit_edits.depiction_edits.POL_depiction_edits',
        'SOV': 'src.constants.unit_edits.depiction_edits.SOV_depiction_edits',
        'UK': 'src.constants.unit_edits.depiction_edits.UK_depiction_edits',
        'USA': 'src.constants.unit_edits.depiction_edits.USA_depiction_edits',
        'FR': 'src.constants.unit_edits.depiction_edits.FR_depiction_edits',
        'RDA': 'src.constants.unit_edits.depiction_edits.RDA_depiction_edits',
        'RFA': 'src.constants.unit_edits.depiction_edits.RFA_depiction_edits',
    }
    
    # Import each faction's edits
    for faction, module_path in faction_modules.items():
        try:
            module = importlib.import_module(module_path)
            
            # Get all exported variables from __all__
            if hasattr(module, '__all__'):
                for var_name in module.__all__:
                    if hasattr(module, var_name):
                        unit_edits = getattr(module, var_name)
                        if "unit_name" in unit_edits:
                            unit_name = unit_edits["unit_name"]
                            merged_edits[unit_name] = unit_edits
                            logger.debug(f"Loaded depiction edits for {unit_name}")
                        else:
                            logger.warning(f"No unit_name found in {var_name} from {faction}")
            else:
                logger.debug(f"No __all__ defined in {faction} depiction edits")
                
        except ImportError:
            # Skip if faction module doesn't exist yet
            logger.debug(f"No depiction edits found for {faction}")
        except Exception as e:
            logger.error(f"Failed to load {faction} depiction edits: {str(e)}")
    
    logger.info(f"Loaded depiction edits for {len(merged_edits)} units total")
    return merged_edits
