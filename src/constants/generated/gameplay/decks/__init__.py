"""Deck edit constants."""

import importlib
from pathlib import Path
from typing import Dict

from src.constants.generated.gameplay.decks.default_multi_decks import load_default_multi_decks
from src.utils.logging_utils import setup_logger

__all__ = ["load_default_multi_decks"]

logger = setup_logger('decks')

category_to_factory_mapping = {
    "artillery": "Factory/Art",
    "aa": "Factory/DCA",
    "heli": "Factory/Helis",
    "infantry": "Factory/Infantry",
    "logistic": "Factory/Logistic",
    "planes": "Factory/Planes",
    "recon": "Factory/Recons",
    "tank": "Factory/Tanks",
}

def load_deck_edits() -> Dict:
    """Load and merge all deck edit dictionaries."""
    merged_edits = {}
    
    logger.info("Loading deck edit dictionaries...")
    
    # Dictionary name mapping
    dict_names = {
        'DDR_decks': 'ddr_decks',
        'FR_decks': 'fr_decks',
        'POL_decks': 'pol_decks',
        'RDA_decks': 'rda_decks',
        'RFA_decks': 'rfa_decks',
        'SOV_decks': 'sov_decks',
        'US_decks': 'us_decks',
    }
    
    # Load dictionaries
    dics_path = Path(__file__).parent
    for file in dics_path.glob("*decks.py"):
        module_name = f"src.constants.generated.gameplay.decks.{file.stem}"
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
        module_name = f"src.constants.generated.gameplay.decks.{file.stem}"
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

_NEW_DIVISIONRULES_PKG = (
    "src.constants.generated.gameplay.decks.new_divisions.new_divisionrules"
)
_COALITION_GENERAL_KINDS = (
    "airborne",
    "armored",
    "mechanized",
    "motorized",
    "global",
)


def _resolve_coalition_division(div_key: str, div_data: Dict) -> Dict:
    """Fill ``division_rules`` from each coalition member's rule module.

    ``coalition`` is a tuple of nation prefixes (``RDA``, ``POL``, ``TCH``).
    Kinds come from ``coalition_rule_kinds`` when set. Otherwise ``general``
    uses every standard kind, and any other division key is split on ``_``
    with ``global`` always included. Missing ``{MEMBER}_{kind}_newdivisionrules``
    attributes are skipped. The source division dict is not mutated.
    """
    members = div_data.get("coalition")
    if not members:
        return div_data

    explicit_kinds = div_data.get("coalition_rule_kinds")
    if explicit_kinds:
        kinds = tuple(explicit_kinds)
    else:
        div_type = div_key.split("_", 1)[1] if "_" in div_key else "general"
        if div_type == "general":
            kinds = _COALITION_GENERAL_KINDS
        else:
            kinds_list = []
            for part in div_type.split("_"):
                if part and part not in kinds_list:
                    kinds_list.append(part)
            if "global" not in kinds_list:
                kinds_list.append("global")
            kinds = tuple(kinds_list)

    combined = []
    seen = set()
    for member in members:
        module_name = f"{_NEW_DIVISIONRULES_PKG}.{member}_newdivisionrules"
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            logger.warning(f"No division rules module for coalition member {member}")
            continue
        for kind in kinds:
            attr = f"{member}_{kind}_newdivisionrules"
            rules = getattr(module, attr, None)
            if not isinstance(rules, dict):
                logger.warning(
                    f"Coalition member {member} has no {attr} for division {div_key}"
                )
                continue
            if id(rules) in seen:
                continue
            seen.add(id(rules))
            combined.append(rules)

    resolved = dict(div_data)
    resolved["division_rules"] = combined
    logger.info(
        f"Combined {len(combined)} division rule tables for coalition division {div_key}"
    )
    return resolved


def load_new_divisions() -> Dict:
    """Load and merge all new division dictionaries."""
    merged_divisions = {}
    
    # Dictionary name mapping.
    # RDA, POL, and TCH *_new_divs stay importable, but they are not emitted.
    # NSWP divisions declare ``coalition`` and this loader concatenates each
    # member's *_newdivisionrules tables.
    dict_names = {
        'NSWP_new_divs': 'nswp_new_divs',
        'RFA_new_divs': 'rfa_new_divs',
        'SOV_new_divs': 'sov_new_divs',
        'US_new_divs': 'us_new_divs',
        'UK_new_divs': 'uk_new_divs',
    }
    
    logger.info("Loading new division dictionaries...")
    
    dics_path = Path(__file__).parent / "new_divisions"
    for file in dics_path.glob("*new_divs.py"):
        module_name = f"src.constants.generated.gameplay.decks.new_divisions.{file.stem}"
        logger.debug(f"Processing {file.stem}")
        
        try:
            module = importlib.import_module(module_name)
            dict_name = dict_names.get(file.stem)
            if dict_name and hasattr(module, dict_name):
                for div_key, div_data in getattr(module, dict_name).items():
                    if not isinstance(div_data, dict):
                        logger.warning(f"Skipping non-division entry {div_key} in {file.stem}")
                        continue
                    merged_divisions[div_key] = _resolve_coalition_division(div_key, div_data)
                logger.info(f"Loaded new divisions from {file.stem}")
            elif str(file.stem) in dict_names:
                logger.warning(f"No dictionary mapping found for {file.stem} or dictionary {dict_name} not found in module")
                
        except Exception as e:
            logger.error(f"Failed to load {file.stem}: {str(e)}")
            
    logger.info(f"Loaded edits for {len(merged_divisions)} new divisions total")
    
    return merged_divisions
