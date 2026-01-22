"""Script to parse and analyze damage resistance values from WARNO."""

import csv
import os
import sys
import winreg
from datetime import datetime
from pathlib import Path
from typing import Any, List, Tuple

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger('damage_parser')


def get_desktop_path() -> Path:
    """Get the actual Desktop path from Windows Registry."""
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                           r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders") as key:
            desktop_path = winreg.QueryValueEx(key, "Desktop")[0]
            logger.debug(f"Found Desktop path: {desktop_path}")
            return Path(desktop_path)
    except Exception as e:
        logger.error(f"Failed to get Desktop path from registry: {e}")
        # Fallback to environment variable
        return Path(os.path.expanduser("~/Desktop"))


def get_resistance_families(damage_params: Any) -> List[Tuple[str, int]]:
    """Get list of resistance families and their max indices."""
    resistance_families = []
    resistance_list = damage_params.by_m("ResistanceFamilyCounts").v
    
    for family_tuple in resistance_list:
        # Tuples are represented as list-like: (FamilyName, MaxIndex)
        # Try different access patterns to handle NDF parser variations
        try:
            if hasattr(family_tuple, 'v'):
                # NDF wrapper object - access via .v[index]
                family_name_raw = family_tuple.v[0]
                max_index = family_tuple.v[1]
                # Unwrap if nested
                if hasattr(family_name_raw, 'v'):
                    family_name_raw = family_name_raw.v
                if hasattr(max_index, 'v'):
                    max_index = max_index.v
            else:
                # Direct list/tuple access
                family_name_raw = family_tuple[0]
                max_index = family_tuple[1]
        except (AttributeError, IndexError, TypeError) as e:
            logger.error(f"Error accessing resistance family tuple: {e}")
            continue
        
        # Remove prefix from family name
        family_name = str(family_name_raw).replace("ResistanceFamily_", "")
        resistance_families.append((family_name, int(max_index)))
        logger.debug(f"Found resistance family: {family_name} with max index {max_index}")
        
    return resistance_families


def get_damage_families(damage_params: Any) -> List[Tuple[str, int]]:
    """Get list of damage families and their max indices."""
    damage_families = []
    damage_list = damage_params.by_m("DamageFamilyCounts").v
    
    for family_tuple in damage_list:
        # Tuples are represented as list-like: (FamilyName, MaxIndex)
        # Try different access patterns to handle NDF parser variations
        try:
            if hasattr(family_tuple, 'v'):
                # NDF wrapper object - access via .v[index]
                family_name_raw = family_tuple.v[0]
                max_index = family_tuple.v[1]
                # Unwrap if nested
                if hasattr(family_name_raw, 'v'):
                    family_name_raw = family_name_raw.v
                if hasattr(max_index, 'v'):
                    max_index = max_index.v
            else:
                # Direct list/tuple access
                family_name_raw = family_tuple[0]
                max_index = family_tuple[1]
        except (AttributeError, IndexError, TypeError) as e:
            logger.error(f"Error accessing damage family tuple: {e}")
            continue
        
        # Remove prefix from family name
        family_name = str(family_name_raw).replace("DamageFamily_", "")
        damage_families.append((family_name, int(max_index)))
        logger.debug(f"Found damage family: {family_name} with max index {max_index}")
        
    return damage_families


def get_damage_levels(damage_families: List[Tuple[str, int]], damage_array: Any) -> List[Tuple[int, str, int]]:
    """Generate list of damage levels with array indices."""
    damage_levels = []
    array_row_index = 0
    array_size = len(damage_array)
    
    for family, max_index in damage_families:
        damage_indices_left = int(max_index)
        damage_level = 1
        while damage_indices_left > 0 and array_row_index < array_size:
            damage_levels.append((array_row_index, family, damage_level))
            damage_level += 1
            damage_indices_left -= 1
            array_row_index += 1
            
    logger.debug(f"Generated {len(damage_levels)} damage levels from array of size {array_size}")
    return damage_levels


def get_armor_levels(resistance_families: List[Tuple[str, int]]) -> List[Tuple[int, str, int]]:
    """Generate list of armor levels with array indices."""
    armor_levels = []
    array_column_index = 0
    
    for family, max_index in resistance_families:
        resistance_indices_left = int(max_index)
        armor_level = 1
        while resistance_indices_left > 0:
            armor_levels.append((array_column_index, family, armor_level))
            armor_level += 1
            resistance_indices_left -= 1
            array_column_index += 1
            
    return armor_levels


def write_csv_data(damage_levels: List, armor_levels: List, damage_array: Any, output_path: Path) -> None:
    """Write damage resistance data to CSV file."""
    logger.info(f"Starting CSV write with {len(damage_levels)} damage levels and {len(armor_levels)} armor levels")
    
    csv_data = []
    
    # Create headers
    index_row = ["", "", "Column Index"]
    family_row = ["", "", "Resistance Family"]
    level_row = ["Row Index", "Damage Family", "Levels"] 
    
    # Add column indices, families and levels
    for col_index, resistance_family, armor_level in armor_levels:
        index_row.append(str(col_index))
        family_row.append(resistance_family)
        level_row.append(str(armor_level))
        
    logger.debug(f"Created headers with {len(family_row)} columns")
    csv_data.append(index_row)
    csv_data.append(family_row)
    csv_data.append(level_row)
    
    # Add data rows
    rows_added = 0
    for row_index, damage_family, damage_level in damage_levels:
        # Start row with index, family and level
        row = [str(row_index), damage_family, str(damage_level)]
        
        # Add damage values
        for column_index, _, _ in armor_levels:
            try:
                value = damage_array[row_index].v[column_index].v
                row.append(value)
            except Exception as e:
                logger.error(f"Error getting value at [{row_index}][{column_index}]: {str(e)}")
                row.append("ERROR")
        csv_data.append(row)
        rows_added += 1
        
    logger.info(f"Added {rows_added} data rows to CSV")
    
    # Write to file
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Created directory: {output_path.parent}")
        
        with open(output_path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)
            
        logger.info(f"Successfully wrote CSV data to {output_path}")
    except Exception as e:
        logger.error(f"Failed to write CSV file: {str(e)}")
        raise


def main() -> None:
    """Main entry point for damage resistance parser."""
    try:
        parse_vanilla = False
        
        # Define paths
        if parse_vanilla:
            MOD_SRC = Path(r"C:/Program Files (x86)/Steam/steamapps/common/WARNO/Mods/sourcemod")
            MOD_DST = Path(r"C:/Program Files (x86)/Steam/steamapps/common/WARNO/Mods/sourcemod")
        else:   
            MOD_SRC = Path(r"C:/Program Files (x86)/Steam/steamapps/common/WARNO/Mods/WARNO ACTUAL dev")
            MOD_DST = Path(r"C:/Program Files (x86)/Steam/steamapps/common/WARNO/Mods/WARNO ACTUAL dev")
        
        # Initialize mod
        mod = ndf.Mod(str(MOD_SRC), str(MOD_DST))
        
        logger.info("Parsing damage resistance data")

        # Parse source directly without context manager
        source = mod.parse_src(r"GameData/Generated/Gameplay/Gfx/DamageResistance.ndf")
        damage_params = source.by_n("DamageResistanceParams").v
        
        # Get damage array first
        damage_array = damage_params.by_m("Values").v

        # Get families and levels
        resistance_families = get_resistance_families(damage_params)
        damage_families = get_damage_families(damage_params)
        damage_levels = get_damage_levels(damage_families, damage_array)  # Pass damage_array
        armor_levels = get_armor_levels(resistance_families)
        
        # Write CSV output
        desktop_path = get_desktop_path() / "csv"
        if parse_vanilla:
            output_path = desktop_path / f"damage_resistance_analysis_vanilla_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        else:
            output_path = desktop_path / f"damage_resistance_analysis_modded_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        logger.info(f"Will write CSV to: {output_path}")

        write_csv_data(damage_levels, armor_levels, damage_array, output_path)
        
        # Print formatted output
        logger.info("\nDamage vs Resistance Analysis:")
        last_damage_family = None
        last_damage_level = None
        
        for (row_index, damage_family, damage_level, column_index, resistance_family, armor_level, value) in [(
            row_index, family, d_level, col_index, r_family, a_level, damage_array[row_index].v[col_index].v
        ) for row_index, family, d_level in damage_levels for col_index, r_family, a_level in armor_levels]:
            # rewrite this if statement for whatever armor types and levels you want to read
            if (0 <= column_index <= 48) or (column_index > 39):
                if damage_family != last_damage_family:
                    logger.info(f"\n{damage_family}:")
                    logger.info(f"    (row {row_index}) Level {damage_level}:")
                    logger.info(f"        vs. (col {column_index}) {resistance_family} {armor_level}: {value}")
                    last_damage_family = damage_family
                    last_damage_level = damage_level
                elif last_damage_level != damage_level:
                    logger.info(f"    (row {row_index}) Level {damage_level}:")
                    logger.info(f"        vs. (col {column_index}) {resistance_family} {armor_level}: {value}")
                    last_damage_level = damage_level
                else:
                    logger.info(f"        vs. (col {column_index}) {resistance_family} {armor_level}: {value}")
                    
    except Exception as e:
        logger.error(f"Error parsing damage resistance data: {str(e)}")
        raise


main()
