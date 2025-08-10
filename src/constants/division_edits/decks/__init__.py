"""Deck edit constants."""

import importlib
from pathlib import Path
from typing import Dict

from src.utils.logging_utils import setup_logger

logger = setup_logger('decks')


def load_deck_edits() -> Dict:
    """Load and merge all deck edit dictionaries."""
    merged_edits = {}
    
    logger.info("Loading deck edit dictionaries...")
    
    # Dictionary name mapping
    dict_names = {
        'US_decks': 'us_decks',
    }
    
    # Load dictionaries
    dics_path = Path(__file__).parent
    for file in dics_path.glob("*decks.py"):
        module_name = f"src.constants.division_edits.decks.{file.stem}"
        logger.debug(f"Processing {file.stem}")
        
        try:
            module = importlib.import_module(module_name)
            dict_name = dict_names.get(file.stem)
            if dict_name and hasattr(module, dict_name):
                merged_edits.update(getattr(module, dict_name))
                logger.info(f"Loaded deck edits from {file.stem}")
                
        except Exception as e:
            logger.error(f"Failed to load {file.stem}: {str(e)}")
            
    logger.info(f"Loaded edits for {len(merged_edits)} decks total")
    
    return merged_edits

def load_strategic_deck_edits() -> Dict:
    """Load and merge all strategic deck edit dictionaries."""
    merged_edits = {}
    
    logger.info("Loading strategic deck edit dictionaries...")
    
    # Dictionary name mapping
    dict_names = {
        'US_strategic_decks': 'us_strategic_decks',
    }
    
    # Load dictionaries
    dics_path = Path(__file__).parent
    for file in dics_path.glob("*strategic_decks.py"):
        module_name = f"src.constants.division_edits.decks.{file.stem}"
        logger.debug(f"Processing {file.stem}")
        
        try:
            module = importlib.import_module(module_name)
            dict_name = dict_names.get(file.stem)
            if dict_name and hasattr(module, dict_name):
                merged_edits.update(getattr(module, dict_name))
                logger.info(f"Loaded strategic deck edits from {file.stem}")
                
        except Exception as e:
            logger.error(f"Failed to load {file.stem}: {str(e)}")
            
    logger.info(f"Loaded edits for {len(merged_edits)} strategic decks total")
    
    return merged_edits