import importlib
from pathlib import Path
from typing import Dict

from src.utils.logging_utils import setup_logger

from .weapon_edits.build_mg_categories import build_mg_categories

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
        'UK_unit_edits': 'uk_unit_edits',
        'USA_unit_edits': 'usa_unit_edits'
    }
    
    # Load dictionaries
    dics_path = Path(__file__).parent
    for file in dics_path.glob("*unit_edits.py"):
        module_name = f"src.dics.{file.stem}"
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
    return merged_edits 

def build_weapon_db(source_files):
    """Build weapon database from source files."""
    ammo_file = source_files["GameData/Generated/Gameplay/Gfx/Ammunition.ndf"]
    
    # Build MG categories
    mg_categories = build_mg_categories(ammo_file)
    
    # Build other weapon data... 