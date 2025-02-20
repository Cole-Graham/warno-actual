"""New depictions for new units"""

from .POL_new_depictions import POL_NEW_DEPICTIONS
from .SOV_new_depictions import SOV_NEW_DEPICTIONS
from .UK_new_depictions import UK_NEW_DEPICTIONS
from .US_new_depictions import US_NEW_DEPICTIONS

# Combine all faction depictions
NEW_DEPICTIONS = {
    **POL_NEW_DEPICTIONS,
    **UK_NEW_DEPICTIONS,
    **SOV_NEW_DEPICTIONS,
    **US_NEW_DEPICTIONS,
    # Future faction depictions will be added here like:
    # etc.
}

__all__ = ["NEW_DEPICTIONS"]
