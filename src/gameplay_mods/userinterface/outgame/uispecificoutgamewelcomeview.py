"""Functions for modifying UI outgame welcome view."""

from datetime import datetime
from typing import List, Tuple

from src import ModConfig
from src import ndf
from src.dics.ui.unit_info_panel import UNIT_INFO_PANEL_DATA
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type

logger = setup_logger(__name__)


def edit_ui_outgame_uispecificoutgamewelcomeview(source_path) -> None:
    """GameData/UserInterface/Use/OutGame/UISpecificOutGameWelcomeView.ndf"""
    logger.info("Modifying outgame welcome view")

    _welcome_descriptor(source_path)

def _welcome_descriptor(source_path) -> None:
    """Write welcome descriptor to dictionary file."""
    
    welcome_descriptor = source_path.by_namespace("UISpecificOutGameWelcomeDescriptor")
    components_list = welcome_descriptor.v.by_m("Components")
    
    versioning_display = ndf.convert(
        f'BUCKTextDescriptor'
        f'('
        f'    ElementName = "MainMenuTitleDoD"'
        f'    ComponentFrame = TUIFramePropertyRTTI'
        f'    ('
        f'        MagnifiableWidthHeight = [1500.0, 90.0]'
        f'        AlignementToAnchor = [0.5, 0.15]'
        f'        AlignementToFather = [0.5, 0.15]'
        f'    )'
        f'    ParagraphStyle = TParagraphStyle'
        f'    ('
        f'        VerticalAlignment = ~/UIText_VerticalCenter'
        f'        Alignment = ~/UIText_Center'
        f'    )'
        f'    TextColor = "ListeExcel/Cartouche"'
        f'    TextSize  = "50"'
        f'    TextStyle = "Default"'
        f'    TypefaceToken = "UIMainFont"'
        f'    TextDico = ~/LocalisationConstantes/dico_interface_outgame'
        f'    TextToken = "menuLabel"'
        f'    Components ='
        f'    ['
        f'        BUCKSpecificHintableArea'
        f'        ('
        f'            HintTitleToken = "menuVers"'
        f'            HintBodyToken = "menuAuth"'
        f'            DicoToken = ~/LocalisationConstantes/dico_interface_outgame'
        f'        ),'
        f'    ]'
        f')'
    )
    
    components_list.v.add(versioning_display)
    
    game_version = ModConfig.get_instance().config_data['build_config']['gameplay_version']
    author = ModConfig.get_instance().config_data['build_config']['author']
    # Build date in format YY-MM-DD (ISO 8601)
    build_date = datetime.now().strftime("%Y-%m-%d")
    
    entries = [
        ("menuLabel", "WARNO ACTUAL"),
        ("menuVers", f"Version {game_version} ({build_date})"),
        ("menuAuth", f"Developed by {author}"),
    ]

    write_dictionary_entries(entries, dictionary_type="outgame")
