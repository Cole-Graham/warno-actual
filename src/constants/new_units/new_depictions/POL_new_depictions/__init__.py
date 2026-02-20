"""New depictions for POL units"""

from .AT_D48_85mm_Para_POL import at_d48_85mm_para_pol
from .HMGteam_AGS17_para_POL import hmgteam_ags17_para_pol
from .HMGteam_NSV_para_POL import hmgteam_nsv_para_pol
from .OT_64_SKOT_2_CMD_POL import ot_64_skot_2_cmd_pol

POL_NEW_DEPICTIONS = {
    "at_d48_85mm_para_pol": at_d48_85mm_para_pol,
    "hmgteam_ags17_para_pol": hmgteam_ags17_para_pol,
    "hmgteam_nsv_para_pol": hmgteam_nsv_para_pol,
    "ot_64_skot_2_cmd_pol": ot_64_skot_2_cmd_pol
}

__all__ = ["POL_NEW_DEPICTIONS"]
