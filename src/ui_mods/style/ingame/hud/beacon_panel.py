"""Functions for modifying UI HUD beacon panel view."""
# from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uiingamehudbeaconpanel(source_path) -> None:
    """Edit UIInGameHUDBeaconPanel.ndf.
    
    Args:
        source_path: NDF file containing HUD beacon panel view definitions
    """
    logger.info("Editing UIInGameHUDBeaconPanel.ndf")
    
    main_component = source_path.by_namespace("UIInGameBeaconPanelViewMainComponent")
    
    # change to horizontal list
#     main_component.v.by_m("Axis").v = "~/ListAxis/Horizontal"
    
#     max_score_icon = ("""
# BUCKListElementDescriptor
# (
#     ComponentDescriptor = BUCKTextureDescriptor
#     (
#         ElementName = 'IconeScoreMax'
#         ComponentFrame = TUIFramePropertyRTTI
#         (
#             MagnifiableWidthHeight = [32.0, 32.0]
#             AlignementToFather = [0.5, 0.0]
#             AlignementToAnchor = [0.5, 0.0]
#         )
#         TextureToken = 'icone_scoreVictoire'
#         TextureColorToken = 'BlancEquipe'
#         Components = 
#         [
#             BUCKSpecificHintableArea
#             (
#                 HintBodyToken = 'LR_score'
#                 DicoToken = ~/LocalisationConstantes/dico_interface_ingame
#             )
#         ]
#     )
# )"""
# )
#     main_component.v.by_member("Elements").v.add(max_score_icon)
    
#     max_score_text = ("""
# BUCKListElementDescriptor
# (
#     ComponentDescriptor = BUCKTextDescriptor
#     (
#         ElementName = 'ScoreToReachText'
#         ComponentFrame = TUIFramePropertyRTTI
#         (
#             RelativeWidthHeight = [0.0, 0.0]
#             AlignementToFather = [0.5, 0.0]
#             AlignementToAnchor = [0.5, 0.0]
#         )
#         ParagraphStyle = TParagraphStyle
#         (
#             Alignment = UIText_Center
#             VerticalAlignment = UIText_VerticalCenter
#             InterLine = 0
#         )
#         TextStyle = 'Default'
#         HorizontalFitStyle = ~/FitStyle/FitToContent
#         VerticalFitStyle = ~/FitStyle/FitToContent
#         TypefaceToken = 'UIMainFont'
#         BigLineAction = ~/BigLineAction/CutByDots
#         TextDico = ~/LocalisationConstantes/dico_interface_ingame
#         TextToken = 'WIP_8'
#         TextColor = 'BlancEquipe'
#         TextSize = '16'
#         Hint = BUCKSpecificHintableArea
#         (
#             ForbiddenTags = ['StrategicScenario']
#             DicoToken = ~/LocalisationConstantes/dico_interface_ingame
#             HintBodyToken = 'LR_score'
#         )
#     )
# )"""
# )
#     main_component.v.by_member("Elements").v.add(max_score_text)