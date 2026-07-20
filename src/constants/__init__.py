"""Root constants module."""

from .gdconstantes import TANDEM_MODIFIER
from .supply_constants import NEW_SUPPLY_CONSTANTS

CQC_RANGE = 200
FOB_CONSTANTS = {
    "health": 40,
    "supply": 6500,
    "command_points": 75,
    "names": {
        "FOBBEL": "MUNITIEDEPOT",
        "FOBBRZ": "tbd",
        "FOBCAN": "FIELD SUPPLY POINT",  # canada
        "FOBCZ": "tbd",  # czechoslovakia
        "FOBCOL": "tbd",
        "FOBCUB": "tbd",
        "FOBDDR": "FELDDEPOT",
        "FOBDK": "FELT FORSYNINGSPUNKT",
        "FOBESP": "tbd",  # spain
        "FOBFR": "DÉPÔT DE MUNITION",
        "FOBNL": "MUNITIEDEPOT",  # supposedly preferred over munitie stoortplats
        "FOBPOL": "PUNKT ZAOPATRZENIA",
        "FOBRFA": "FELDDEPOT",
        "FOBSOV": "SKLAD SNABZHENIYA",
        "FOBTCH": "tbd",
        "FOBUK": "FIELD SUPPLY POINT",
        "FOBUS": "FIELD SUPPLY POINT",
        "FOBVEN": "tbd",
    },
}
TFR_STEALTH_BONUS = 1.5

__all__ = [
    "CQC_RANGE",
    "FOB_CONSTANTS",
    "NEW_SUPPLY_CONSTANTS",
    "TANDEM_MODIFIER",
    "TFR_STEALTH_BONUS",
]
