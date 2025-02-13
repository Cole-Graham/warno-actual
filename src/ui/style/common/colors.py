"""Functions for modifying UI colors."""
from src.utils.logging_utils import setup_logger
# from src import ndf
# from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_colors(source_path) -> None:
    """Edit Colors.ndf.
    
    Args:
        source_path: NDF file containing color definitions
    """
    logger.info("Editing Colors.ndf")

    # Add new color definitions
    color_definitions = (
        f'M81_Artichoke       is [156,145,119,255]'        # Panel color
        f'M81_ArtichokeVeryLight is [219,204,168,255]'     # "..._boutonShortcutsM81"
        f'M81_ArtichokeVeryLight62 is [219,204,168,158]'   # "Flare Labels"
        f'M81_ArtichokeNearWhite is [255,240,225,255]'     # "..._boutonShortcutsM81"
        f'M81_ArtichokeTransparent is [156,145,119,128]'   # Weapon button status
        f'M81_Artichoke64          is [156,145,119,64]'    # Multiselection scroll bar background
        f'M81_DarkCharcoal    is [49,56,49,255]'           # Button / panel color
        f'M81_DarkCharcoalSelection is [148,168,148,210]'  # Button / panel color
        f'M81_DarkCharcoalClicked is [197,224,197,210]'    # Button / panel color
        f'M81_DarkCharcoalTransparent is [49,56,49,113]'   # Weapon Status
        f'M81_Ebony           is [80,101,77,255]'          # Button / panel color / panel color
        f'M81_EbonyDark       is [77,96,74,255]'           # BoutonTempsM81
        f'M81_EbonyLight      is [98,122,94,255]'          # BoutonTempsM81
        f'M81_EbonyVeryDark   is [67,84,64,255]'           # BoutonTempsM81
        f'M81_Quincy          is [101,89,73,255]'          # Panel / unit card color
        f'M81_VeryDarkCharcoal is [31,35,31,255]'          # Button color
        f'M81_MonochromeCRT   is [40,40,40,255]'           # Used for black screen of 1980s style monochrome computer displays
        f'M81_AppleII         is [51,255,51,255]'          # P1 GE phosphor green text for monochrome displays
        f'M81_AppleIIc        is [102,255,102,255]'        # P24 GE phosphor green text for monochrome displays
        f'M81_P3AmberOrange   is [255,176,0,255]'          # P3 amber phosphor text
        f'M81_P3AmberYellow   is [255,204,0,255]'          # P? amber phosphor text https://superuser.com/questions/361297/what-colour-is-the-dark-green-on-old-fashioned-green-screen-computer-displays
        f'M81_RedPhosphor     is [255,66,33,255]'          # Some cubeaction buttons
        f'M81_WhiteText95     is [242,242,242,255]'        # Some buttons, Weapon panel, etc.
        f'BlancEquipe         is [202,223,229,255]'        # Added as defined color for mod
        f'TypeG               is [36,110,36,255]'          # Playerhelper/cover
    )
    
    # Insert color definitions at start of file
    for line in reversed(color_definitions.split('\n')):
        if line:
            source_path.insert(1, line)
            logger.debug(f"Added color definition: {line}")
