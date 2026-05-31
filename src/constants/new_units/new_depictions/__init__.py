"""New depictions for new units"""

from .FR_new_depictions import FR_NEW_DEPICTIONS
from .POL_new_depictions import POL_NEW_DEPICTIONS
from .RDA_new_depictions import RDA_NEW_DEPICTIONS
from .RFA_new_depictions import RFA_NEW_DEPICTIONS
from .SOV_new_depictions import SOV_NEW_DEPICTIONS
from .UK_new_depictions import UK_NEW_DEPICTIONS
from .US_new_depictions import US_NEW_DEPICTIONS
from ._supply_transport import towed_supply_vehicle_depiction
from src.constants.supply_transport_variants import SUPPLY_TRANSPORT_VARIANT_CONFIG, make_supply_transport_name

SUPPLY_TRANSPORT_DEPICTIONS = {
    make_supply_transport_name(donor).lower(): towed_supply_vehicle_depiction(
        make_supply_transport_name(donor),
    )
    for donor in SUPPLY_TRANSPORT_VARIANT_CONFIG
}

# Combine all faction depictions
NEW_DEPICTIONS = {
    **FR_NEW_DEPICTIONS,
    **POL_NEW_DEPICTIONS,
    **RDA_NEW_DEPICTIONS,
    **RFA_NEW_DEPICTIONS,
    **UK_NEW_DEPICTIONS,
    **SOV_NEW_DEPICTIONS,
    **US_NEW_DEPICTIONS,
    **SUPPLY_TRANSPORT_DEPICTIONS,
}

__all__ = ["NEW_DEPICTIONS"]
