"""Soviet depiction edits."""

from .Engineers_CMD_Naval_SOV import engineers_cmd_naval_sov
from .HvyScout_SOV import hvyscout_sov
from .HvyScout_TTsko_SOV import hvyscout_ttsko_sov
from .Mi_8TV_Gunship_SOV import mi_8tv_gunship_sov
from .Mi_24P_SOV import mi_24p_sov
from .Mortier_2B9_Vasilek_Naval_SOV import mortier_2b9_vasilek_naval_sov
from .Mortier_2B9_Vasilek_nonPara_SOV import mortier_2b9_vasilek_nonpara_sov
from .Mortier_2B9_Vasilek_SOV import mortier_2b9_vasilek_sov
from .MotRifles_BTR_SOV import motrifles_btr_sov
from .MotRifles_BTR_TTsko_SOV import motrifles_btr_ttsko_sov
from .MP_SOV import mp_sov
from .MTLB_Vasilek_SOV import mtlb_vasilek_sov
from .Naval_Rifle_CMD_SOV import naval_rifle_cmd_sov
from .Sniper_Spetsnaz_SOV import sniper_spetsnaz_sov
from .VDV_Afgantsy_SOV import vdv_afgantsy_sov
# Needs custom model with two turrets
# from .Su_24M_clu_SOV import su_24m_clu_sov
# Need to edit the model to support adding smoke, on hold for now (temporarily increased armor in the meantime)
# from .TOS1_Buratino_SOV import tos1_buratino_sov

__all__ = [
    "engineers_cmd_naval_sov",
    "hvyscout_sov",
    "hvyscout_ttsko_sov",
    "mi_8tv_gunship_sov",
    "mi_24p_sov",
    "mortier_2b9_vasilek_naval_sov",
    "mortier_2b9_vasilek_sov",
    "mortier_2b9_vasilek_nonpara_sov",
    "motrifles_btr_sov",
    "motrifles_btr_ttsko_sov",
    "mp_sov",
    "mtlb_vasilek_sov",
    "naval_rifle_cmd_sov",
    "sniper_spetsnaz_sov",
    "vdv_afgantsy_sov",
    # "su_24m_clu_sov",
    # "tos1_buratino_sov",
]
