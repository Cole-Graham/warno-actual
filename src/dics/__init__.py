from src.dics.rda_unit_edits import rda_unit_edits
from src.dics.sov_unit_edits import sov_unit_edits
from src.dics.usa_unit_edits import usa_unit_edits


def load_unit_edits():
    """Load and merge all unit edit dictionaries."""
    merged_edits = {}
    merged_edits.update(rda_unit_edits)
    merged_edits.update(usa_unit_edits)
    merged_edits.update(sov_unit_edits)
    return merged_edits 