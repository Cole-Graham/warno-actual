"""Autocannon DCA ammunition category standards (one module per category string)."""

from ..types import DcaCategoryStandardEntry

# Applied to all weapons whose ammunition dictionary key uses category "DCA" (autocanon_dca.py).
DCA_STANDARDS: DcaCategoryStandardEntry = {
    "hit_roll": {
        "DistanceToTarget": False,
    },
}

__all__ = [
    "DCA_STANDARDS",
]
