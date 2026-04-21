"""New depictions for SOV units"""

from .HvyScout_RPG7VL_SOV import hvyscout_rpg7vl_sov
from .HvyScout_TTsko_RPG7VL_SOV import hvyscout_ttsko_rpg7vl_sov
from .MotRifles_RPG7VL_TTsko_SOV import motrifles_rpg7vl_ttsko_sov
from .VDV_Afgantsy_RPG7VL_SOV import vdv_afgantsy_rpg7vl_sov

SOV_NEW_DEPICTIONS = {
    "hvyscout_rpg7vl_sov": hvyscout_rpg7vl_sov,
    "hvyscout_ttsko_rpg7vl_sov": hvyscout_ttsko_rpg7vl_sov,
    "motrifles_rpg7vl_ttsko_sov": motrifles_rpg7vl_ttsko_sov,
    "vdv_afgantsy_rpg7vl_sov": vdv_afgantsy_rpg7vl_sov,
}

__all__ = ["SOV_NEW_DEPICTIONS"]
