"""Functions for modifying infantry units."""

import json
from pathlib import Path
from typing import Dict

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Load unit data from database
DB_PATH = Path(__file__).parent.parent.parent / "data" / "database" / "unit_data.json"
with open(DB_PATH, 'r', encoding='utf-8') as f:
    UNIT_DB = json.load(f)


def edit_infantry_armor_wa(source) -> None:
    """Edit infantry armor in UniteDescriptor.ndf."""
    logger.info("Modifying infantry armor to WA type")
    
    for unit_row in source:
        # Get unit name from descriptor
        unit_name = unit_row.namespace.split("Descriptor_Unit_")[-1]
        if unit_name not in UNIT_DB:
            continue
            
        unit_data = UNIT_DB[unit_name]
        unit_strength = unit_data.get("strength", 0)
        if not unit_strength:
            continue
            
        modules_list = unit_row.v.by_m("ModulesDescriptors").v
        
        # Process each module
        for module in modules_list:
            if not hasattr(module.v, 'type'):
                continue
                
            if module.v.type != "TDamageModuleDescriptor":
                continue
                
            # Get blindage properties
            blindage_membr = module.v.by_m("BlindageProperties").v
            front_res_obj = blindage_membr.by_m("ResistanceFront").v
            
            if front_res_obj.by_m("Family").v != "ResistanceFamily_infanterie":
                continue
                
            # Update armor values for all sides
            armor_level = str(15 - unit_strength)
            for armor_side in ["Front", "Sides", "Rear", "Top"]:
                res_obj = blindage_membr.by_m(f"Resistance{armor_side}").v
                res_obj.by_m("Family").v = "ResistanceFamily_infanterieWA"
                res_obj.by_m("Index").v = armor_level
                
            logger.info(
                f"Updated {unit_name} infantry armor to WA type "
                f"with armor level {armor_level}"
            ) 