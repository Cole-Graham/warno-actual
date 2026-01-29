"""In-game UI components."""
from .hud import (
    edit_uiingamehudbeaconpanel,
    edit_uiingamehudreplayresource,
    edit_uispecifichudalertpanelview,
    edit_uispecificingameidleunitview,
    edit_uispecificminimapinfoview,
    edit_uispecificingameplayermissionlabelresources,
    edit_uispecifichudmultiselectionpanelview,
    edit_uispecificoffmapview,
    edit_uispecificoffmapairplaneview,
    edit_uispecificskirmishproductionmenuview,
    edit_uispecifichudscoreview,
    edit_uispecificshortcutsforselectionview,
    edit_uispecificingamehudtimepanelview,
    edit_uispecificunitselectionpanelview,
    edit_uispecificunitselectionweaponpanelview,
    edit_uispecificsmartgroupselectionpanelview,
    edit_uispecificunitlabelaggregationview,
    edit_uispecificunitlabelcommon,
    edit_uispecificunitlabelmultiselectionview,
    edit_uispecificunitlabelviewnameonly,
    edit_uispecificunitlabelview,
)
from .cube_action import edit_uiingamebuckcubeaction
from .default_container import edit_uiingamedefaultcontainer
from .engagement_rules import edit_uiingamebuckengagementrules
from .ingame import edit_uiingameresources
from .launch_button import edit_uiingamelaunchbattlebuttonresources
from .minimap import edit_uiingameminimap
from .orders import edit_orderdisplay
from .starting_information import edit_uispecificdisplaystartinginformationview

__all__ = [
    'edit_orderdisplay',
    'edit_uiingamebuckcubeaction',
    'edit_uiingamebuckengagementrules',
    'edit_uiingamedefaultcontainer',
    'edit_uiingamehudbeaconpanel',
    'edit_uiingamehudreplayresource',
    'edit_uiingamelaunchbattlebuttonresources',
    'edit_uiingameminimap',
    'edit_uiingameresources',
    'edit_uispecificdisplaystartinginformationview',
    'edit_uispecifichudalertpanelview',
    'edit_uispecifichudmultiselectionpanelview',
    'edit_uispecifichudscoreview',
    'edit_uispecificingamehudtimepanelview',
    'edit_uispecificingameidleunitview',
    'edit_uispecificingameplayermissionlabelresources',
    'edit_uispecificminimapinfoview',
    'edit_uispecificoffmapairplaneview',
    'edit_uispecificoffmapview',
    'edit_uispecificshortcutsforselectionview',
    'edit_uispecificskirmishproductionmenuview',
    'edit_uispecificunitlabelaggregationview',
    'edit_uispecificunitlabelcommon',
    'edit_uispecificunitlabelmultiselectionview',
    'edit_uispecificunitlabelviewnameonly',
    'edit_uispecificunitlabelview',
    'edit_uispecificunitselectionpanelview',
    'edit_uispecificsmartgroupselectionpanelview',
    'edit_uispecificunitselectionweaponpanelview'
]
