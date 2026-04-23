"""New depictions for RDA units"""

from .HvyScout_RPG7VL_DDR import hvyscout_rpg7vl_ddr
from .MP_mech_DDR import mp_mech_ddr

#from .AT_D44_85mm_FJ_DDR import at_d44_85mm_fj_ddr
#from .HMGteam_AGS17_FJ_DDR import hmgteam_ags17_fj_ddr
#from .HMGteam_NSV_FJ_DDR import hmgteam_nsv_fj_ddr

RDA_NEW_DEPICTIONS = {
    "hvyscout_rpg7vl_ddr": hvyscout_rpg7vl_ddr,
    "mp_mech_ddr": mp_mech_ddr,
    #"at_d44_85mm_fj_ddr": at_d44_85mm_fj_ddr,
    #"hmgteam_ags17_fj_ddr": hmgteam_ags17_fj_ddr,
    #"hmgteam_nsv_fj_ddr": hmgteam_nsv_fj_ddr,
}

__all__ = ["RDA_NEW_DEPICTIONS"]
