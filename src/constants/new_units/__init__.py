"""New unit definitions."""

from .new_depictions import NEW_DEPICTIONS
from .POL_new_units import POL_NEW_UNITS
from .RDA_new_units import RDA_NEW_UNITS
from .RFA_new_units import RFA_NEW_UNITS
from .SOV_new_units import SOV_NEW_UNITS
from .UK_new_units import UK_NEW_UNITS
from .USA_new_units import USA_NEW_UNITS

# Combine all new unit definitions
NEW_UNITS = {
    **SOV_NEW_UNITS, 
    **RDA_NEW_UNITS,
    **RFA_NEW_UNITS,
    **POL_NEW_UNITS,
    **UK_NEW_UNITS,
    **USA_NEW_UNITS,
}

__all__ = [
    "NEW_UNITS",
    "NEW_DEPICTIONS",
]
