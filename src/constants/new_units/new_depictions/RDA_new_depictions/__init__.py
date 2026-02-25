"""New depictions for RDA units"""

from .AT_D44_85mm_FJ_DDR import at_d44_85mm_fj_ddr
from .HMGteam_AGS17_FJ_DDR import hmgteam_ags17_fj_ddr
from .HMGteam_NSV_FJ_DDR import hmgteam_nsv_fj_ddr

RDA_NEW_DEPICTIONS = {
    "at_d44_85mm_fj_ddr": at_d44_85mm_fj_ddr,
    "hmgteam_ags17_fj_ddr": hmgteam_ags17_fj_ddr,
    "hmgteam_nsv_fj_ddr": hmgteam_nsv_fj_ddr,
}

__all__ = ["RDA_NEW_DEPICTIONS"]
