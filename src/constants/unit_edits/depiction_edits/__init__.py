"""Unit edits for depiction files."""

# from .FR_depiction_edits import ()
from .POL_depiction_edits import (
    engineers_cmd_pol,
    mortier_2b9_vasilek_para_pol,
)
from .RDA_depiction_edits import (
    mi_24p_s8_at_ddr,
)
# from .RFA_depiction_edits import ()
from .SOV_depiction_edits import (
    mi_8tv_gunship_sov,
    mi_24p_sov,
    mortier_2b9_vasilek_nonpara_sov,
    mortier_2b9_vasilek_sov,
    mtlb_vasilek_sov,
)
# from .UK_depiction_edits import ()
from .USA_depiction_edits import (
    ranger_us,
    scout_us,
)

__all__ = [
    # POL
    "engineers_cmd_pol",
    "mortier_2b9_vasilek_para_pol",
    
    # RDA
    "mi_24p_s8_at_ddr",
    
    # SOV
    "mi_8tv_gunship_sov",
    "mi_24p_sov",
    "mortier_2b9_vasilek_nonpara_sov",
    "mortier_2b9_vasilek_sov",
    "mtlb_vasilek_sov",
    
    # USA
    "ranger_us",
    "scout_us",
]