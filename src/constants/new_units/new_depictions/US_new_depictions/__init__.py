"""New depictions for US units"""

from .Cav_Scout_Dragon_M3A1_US import cav_scout_dragon_m3a1_us
from .Cav_Scout_Dragon_M3A2_US import cav_scout_dragon_m3a2_us
from .MANPAD_Stinger_C_Rifles_US import manpad_stinger_c_rifles_us

US_NEW_DEPICTIONS = {
    "cav_scout_dragon_m3a1_us": cav_scout_dragon_m3a1_us,
    "cav_scout_dragon_m3a2_us": cav_scout_dragon_m3a2_us,
    "manpad_stinger_c_rifles_us": manpad_stinger_c_rifles_us,
}

__all__ = ["US_NEW_DEPICTIONS"]
