"""New depictions for RDA units"""

from .HvyScout_RPG7VL_DDR import hvyscout_rpg7vl_ddr
from .MotSchutzen_RPG29_DDR import mot_schutzen_rpg29_ddr
from .MP_mech_DDR import mp_mech_ddr
from .Tunguska_2K22_DDR import tunguska_2k22_ddr

#from .AT_D44_85mm_FJ_DDR import at_d44_85mm_fj_ddr
#from .HMGteam_AGS17_FJ_DDR import hmgteam_ags17_fj_ddr
#from .HMGteam_NSV_FJ_DDR import hmgteam_nsv_fj_ddr

RDA_NEW_DEPICTIONS = {
    "hvyscout_rpg7vl_ddr": hvyscout_rpg7vl_ddr,
    # Key must match ``NewName.lower()`` (e.g. MotSchutzen -> motschutzen, not mot_schutzen).
    "motschutzen_rpg29_ddr": mot_schutzen_rpg29_ddr,
    "mp_mech_ddr": mp_mech_ddr,
    "tunguska_2k22_ddr": tunguska_2k22_ddr,
    #"at_d44_85mm_fj_ddr": at_d44_85mm_fj_ddr,
    #"hmgteam_ags17_fj_ddr": hmgteam_ags17_fj_ddr,
    #"hmgteam_nsv_fj_ddr": hmgteam_nsv_fj_ddr,
}

__all__ = ["RDA_NEW_DEPICTIONS"]
