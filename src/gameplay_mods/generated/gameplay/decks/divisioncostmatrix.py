"""Functions for modifying division cost matrices."""

from typing import Any

from src.constants.division_edits.matrix_data import DIVISION_MATRICES
from src.constants.generated.gameplay.decks import load_new_divisions
from src.constants.generated.gameplay.decks.new_divisions import spec_matrices
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_decks_divisioncostmatrix(source) -> None:
    """GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf"""
    logger.info("Editing division cost matrices")
    matrix_names = _update_existing_matrices(source)
    _create_national_division_matrices(source, matrix_names)
    _apply_default_cost_multiplier(source, matrix_names)


def _update_existing_matrices(source: Any) -> list:
    """Update existing matrices from DIVISION_MATRICES.
    
    Args:
        source: The DivisionCostMatrix.ndf source object
        
    Returns:
        List of matrix names that were updated
    """
    matrix_names = []
    for division_name, matrix_data in DIVISION_MATRICES.items():
        try:
            matrix_name = f"MatrixCostName_{division_name}"
            matrix_names.append(matrix_name)
            index = source.by_n(matrix_name).index
            matrix_string = _create_matrix_string(matrix_name, matrix_data)
            source.replace(index, matrix_string)
            logger.info(f"Updated matrix for {matrix_name}")
        except Exception as e:
            logger.error(f"Failed to update matrix {division_name}: {str(e)}")
    return matrix_names


def _apply_default_cost_multiplier(source: Any, matrix_names: list) -> None:
    """Apply default cost multiplier to matrices not in matrix_names.
    
    Multiplies all values by 2 as default — for dev purposes — until we define it in DIVISION_MATRICES.
    
    Args:
        source: The DivisionCostMatrix.ndf source object
        matrix_names: List of matrix names that have been explicitly updated
    """
    # Get list of new division matrix names to skip
    new_divisions = load_new_divisions()
    new_division_matrix_names = set()
    for div_data in new_divisions.values():
        cfg_name = div_data.get("cfg_name")
        if cfg_name:
            matrix_name = f"MatrixCostName_{cfg_name}_multi"
            new_division_matrix_names.add(matrix_name)
    
    # Combine both lists of matrices to skip
    matrices_to_skip = set(matrix_names) | new_division_matrix_names
    
    for matrix_map in source:
        if matrix_map.n.endswith("_multi") and matrix_map.n not in matrices_to_skip:
            # multiply all values by 2 as default — for dev purposes — until we define it in DIVISION_MATRICES
            for matrix_row in matrix_map.v:
                factory_key = matrix_row.k
                card_cost_list = matrix_row.v
                for card_cost in card_cost_list:
                    if factory_key == "EFactory/Logistic":
                        card_cost.v = "2"
                    else:
                        card_cost.v = str(int(card_cost.v) * 2)


def _create_matrix_string(matrix_name: str, matrix_data: dict) -> str:
    """Create a matrix string in the NDF format.
    
    Args:
        matrix_name: The name of the matrix (e.g., 'MatrixCostName_US_national_general_multi')
        matrix_data: Dictionary mapping factory names to cost lists
        
    Returns:
        Formatted matrix string
    """
    # Build the matrix entries
    entries = []
    # Always include Defense as empty list
    if "EFactory/Defense" in matrix_data:
        defense_costs = matrix_data["EFactory/Defense"]
        defense_str = "[" + ", ".join(str(c) for c in defense_costs) + "]"
        entries.append(f"    (EFactory/Defense, {defense_str}),")
    else:
        entries.append("    (EFactory/Defense, []),")
    
    # Add entries for each factory in the matrix data
    for factory, costs in matrix_data.items():
        if factory == "EFactory/Defense":
            continue  # Already added above
        cost_str = "[" + ", ".join(str(c) for c in costs) + "]"
        entries.append(f"    ({factory}, {cost_str}),")
    
    # Join all entries
    entries_str = "\n".join(entries)
    
    # Build the complete matrix string
    matrix_str = (
        f"{matrix_name} is MAP\n"
        f"[\n"
        f"{entries_str}\n"
        f"]"
    )
    
    return matrix_str


def _create_national_division_matrices(source: Any, existing_matrix_names: list) -> None:
    """Create cost matrices for new national divisions based on spec_matrices."""
    new_divisions = load_new_divisions()
    
    if not new_divisions:
        logger.info("No new divisions to create matrices for")
        return
    
    logger.info("Creating cost matrices for national divisions")
    
    for div_key, div_data in new_divisions.items():
        cfg_name = div_data.get("cfg_name")
        if not cfg_name:
            logger.warning(f"No cfg_name specified for {div_key}, skipping matrix creation")
            continue
        
        matrix_name = f"MatrixCostName_{cfg_name}_multi"
        
        # Check if matrix already exists
        if matrix_name in existing_matrix_names:
            logger.debug(f"Matrix {matrix_name} already exists, skipping")
            continue
        
        try:
            # Check if matrix already exists in source
            existing_matrix = source.by_n(matrix_name, False)
            if existing_matrix:
                logger.debug(f"Matrix {matrix_name} already exists in source, skipping")
                continue
        except (AttributeError, KeyError):
            pass  # Matrix doesn't exist, which is expected
        
        # Extract division type from key
        if "_" in div_key:
            div_type = div_key.split("_", 1)[1]
        else:
            div_type = "general"
        
        # Get matrix specification for this division type
        if div_type not in spec_matrices:
            logger.warning(f"No spec_matrix found for division type '{div_type}' in {div_key}, skipping")
            continue
        
        spec_matrix = spec_matrices[div_type]
        
        matrix_data = spec_matrix
        
        # Find a donor matrix to copy structure from
        donor_matrix = None
        for existing_name in existing_matrix_names:
            if existing_name.endswith("_multi"):
                try:
                    donor_matrix = source.by_n(existing_name, False)
                    if donor_matrix:
                        break
                except (AttributeError, KeyError):
                    continue
        
        if not donor_matrix:
            logger.warning(f"Could not find donor matrix for {div_key}, skipping")
            continue
        
        # Create new matrix by copying donor
        new_matrix = donor_matrix.copy()
        new_matrix.namespace = matrix_name
        new_matrix.n = matrix_name
        
        # Modify the matrix entries to match the spec_matrix data
        try:
            matrix_map = new_matrix.v
            
            # Track which factories we've updated
            updated_factories = set()
            
            # Update existing entries that match our matrix_data
            for matrix_row in matrix_map:
                factory_key = matrix_row.k
                
                if factory_key in matrix_data:
                    # Update the cost list for this factory
                    new_costs = matrix_data[factory_key]
                    card_cost_list = matrix_row.v
                    
                    # Clear existing costs
                    existing_costs = list(card_cost_list)
                    for cost_obj in reversed(existing_costs):
                        card_cost_list.remove(cost_obj.index)
                    
                    # Add new costs
                    for cost_value in new_costs:
                        card_cost_list.add(str(cost_value))
                    
                    updated_factories.add(factory_key)
                elif factory_key == "EFactory/Defense":
                    # Ensure Defense is empty
                    card_cost_list = matrix_row.v
                    existing_costs = list(card_cost_list)
                    for cost_obj in reversed(existing_costs):
                        card_cost_list.remove(cost_obj.index)
                    updated_factories.add("EFactory/Defense")
            
            # Add any missing factories (shouldn't happen if donor has all factories, but be safe)
            # Note: This assumes matrix_map has an add method - if not, we'll skip missing factories
            for factory, costs in matrix_data.items():
                if factory not in updated_factories:
                    try:
                        # Try to add the factory entry
                        # This may not work depending on the NDF structure
                        logger.debug(f"Factory {factory} not found in donor, may need manual addition")
                    except Exception:
                        pass
            
            # Add the new matrix to source
            source.add(new_matrix)
            logger.info(f"Created matrix {matrix_name} for division type '{div_type}'")
        except Exception as e:
            logger.error(f"Failed to create matrix {matrix_name}: {str(e)}")
            import traceback
            logger.debug(traceback.format_exc())
    
    logger.info("Finished creating national division matrices")
