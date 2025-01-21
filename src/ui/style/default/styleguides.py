"""Functions for modifying UI style guides."""
from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def _edit_componentstate(parent_key, key, componentstate, color):
    """Helper function to edit component state colors.
    
    Args:
        parent_key: Parent key in the map
        key: Key to find in the map
        componentstate: State to modify (Normal, Highlighted, etc)
        color: New color value
    """
    map_row = parent_key.by_k(key).v
    componentstate_row = map_row.by_k(f"~/ComponentState/{componentstate}").v
    componentstate_row.by_m("Color").v = color

# fmt: off
def edit_defaultstyleguides(source_path) -> None:
    """Edit DefaultStyleGuides.ndf.
    
    Args:
        source: NDF file containing style guide definitions
    """
    logger.info("Editing DefaultStyleGuides.ndf")
    
    for row in source_path:
        if row.namespace == "DefaultStyleGuide":
            # Handle line sizes map
            line_sizes_map = row.v.by_m("LineSizesMap").v
            line_sizes_map.insert(1, ('"1.5"', "MAP [ ( ~/ComponentState/Normal, TFloatRTTI ( Value = 1.5 ) ), ]"))
            
            # Handle block colors map
            block_colors_map = row.v.by_m("BlockColorsMap").v
            
            # Add M81 Woodland UI Colors
            new_lines = [
                ('"M81_Artichoke"',          'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,255] ) ), ]'),
                ('"M81_Artichoke191"',          'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,191] ) ), ]'),
                ('"M81_ArtichokeVeryLight"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [219,204,168,255] ) ), ]'),
                ('"M81_ArtichokeVeryLight62"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [219,204,168,158] ) ), ]'),
                ('"M81_ArtichokeNearWhite"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,240,225,255] ) ), ]'),
                ('"M81_ArtichokeTransparent"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,128] ) ), ]'),
                ('"M81_Artichoke64"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,64] ) ), ]'),
                ('"M81_DarkCharcoal"',    'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [49,56,49,255] ) ), ]'),
                ('"M81_DarkCharcoalSelection"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [148,168,148,210] ) ), ]'),
                ('"M81_DarkCharcoalClicked"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [197,224,197,210] ) ), ]'),
                ('"M81_DarkCharcoalTransparent"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [49,56,49,113] ) ), ]'),
                ('"M81_Ebony"',           'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [80,101,77,255] ) ), ]'),
                ('"M81_Ebony128"',            'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [80,101,77,128] ) ), ]'),
                ('"M81_EbonyDark"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [77,96,74,255] ) ), ]'),
                ('"M81_EbonyLight"',      'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [98,122,94,255] ) ), ]'),
                ('"M81_EbonyVeryDark"',   'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [67,84,64,255] ) ), ]'),
                ('"M81_Quincy"',          'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [101,89,73,255] ) ), ]'),
                ('"M81_VeryDarkCharcoal"',    'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [31,35,31,255] ) ), ]'),
                ('"M81_MonochromeCRT"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [40,40,40,255] ) ), ]'),
                ('"M81_AppleII"',             'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [51,255,51,255] ) ), ]'),
                ('"M81_AppleIIc"',            'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [102,255,102,255] ) ), ]'),
                ('"M81_AppleIIcTransparent"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [102,255,102,100] ) ), ]'),
                ('"M81_P3AmberOrange"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,176,0,255] ) ), ]'),
                ('"M81_P3AmberYellow"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,204,0,255] ) ), ]'),
                ('"M81_WhiteText95"',         'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [242,242,242,255] ) ), ]'),
            ]
            for line in new_lines:
                block_colors_map.insert(1, line)

            # Add BoutonTemps block
            bouton_temps = (
                f'("BoutonTemps",                    MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"Test"').index + 1
            block_colors_map.insert(index, bouton_temps)

            # Add BoutonTemps background and block
            boutontemps_backgroundm81 = (
                f'("BoutonTemps_BackgroundM81",                    MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                               ])'
            )
            boutontemps_blockm81 = (
                f'("BoutonTempsBlockM81",                    MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = [80,101,77,255]  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [49,56,49,255] ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [49,56,49,255] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [49,56,49,255] ) ), '
                f'                                   ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = [49,56,49,255] ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [122,190,167,78] ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"BoutonTemps_Background"').index + 1
            block_colors_map.insert(index, boutontemps_blockm81)
            block_colors_map.insert(index, boutontemps_backgroundm81)

            # Update CustomFlareText colors
            _edit_componentstate(block_colors_map, '"CustomFlareText"', 'Normal', 'M81_ArtichokeNearWhite')
            _edit_componentstate(block_colors_map, '"CustomFlareText"', 'Highlighted', 'M81_EbonyVeryDark')

            # Add BoutonTemps pawn block
            boutontemps_pawnblockm81 = (
                f'("BoutonTemps_pawnBlockM81",                    MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoal  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_DarkCharcoalSelection ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [31,35,31,255] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [31,35,31,255] ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color =  [31,35,31,255] ) ),'
                f'                                   ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [122,167,176,50] ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"BoutonTemps_pawn"').index + 1
            block_colors_map.insert(index, boutontemps_pawnblockm81)

            # Add BoutonFlares block
            boutonflaresblockm81 = (
                f'("BoutonFlaresBlockM81",            MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_Quincy ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_Artichoke ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [122,167,176,50] ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"BoutonFlares"').index + 1
            block_colors_map.insert(index, boutonflaresblockm81)

            # Add BoutonSelectionMultiple block
            boutonselectionmultipleblockm81 = (
                f'("BoutonSelectionMultipleBlockM81",        MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = [122,167,176,102]  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = BleuVariable ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = Blanc184 ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [22,133,173,255] ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = VertPomme ) ),'
                f'                                   ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = VertGris ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = BleuGris ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"BoutonSelectionMultiple"').index + 1
            block_colors_map.insert(index, boutonselectionmultipleblockm81)

            # Add OffMapUnitButtonName
            offmapunitbuttonnamem81 = (
                f'("OffMapUnitButtonNameM81",        MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoal  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [78,96,75,191] ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"OffMapUnitButtonName"').index + 1
            block_colors_map.insert(index, offmapunitbuttonnamem81)
            block_colors_map.remove_by_key('"OffMapUnitButtonName"')

            # Add M81 Production
            m81production = (
                f'("M81_Production",                  MAP ['
                f'                                   ( ~/ComponentState/Normal,                 TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Highlighted,            TColorRTTI( Color = M81_DarkCharcoalSelection ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"H2_bleu_5"').index + 1
            block_colors_map.insert(index, m81production)

            # Add NoirButton
            noirbutton = (
                f'("NoirButton",            MAP ['
                f'                           ( ~/ComponentState/Grayed,                 TColorRTTI( Color = Transparent ) ),'
                f'                           ( ~/ComponentState/Normal,                 TColorRTTI( Color = NoirPur ) ),'
                f'                           ( ~/ComponentState/Highlighted,            TColorRTTI( Color = NoirPur ) ),'
                f'                           ( ~/ComponentState/Clicked,                TColorRTTI( Color = NoirPur ) ),'
                f'                           ( ~/ComponentState/Toggled,                TColorRTTI( Color = NoirPur ) ),'
                f'                           ( ~/ComponentState/ToggleHighlighted,      TColorRTTI( Color = NoirPur ) ),'
                f'                       ])'
            )
            index = block_colors_map.by_k('"Fulda2_blanc15"').index + 1
            block_colors_map.insert(index, noirbutton)

            # Add DarkerGray30
            darkergray30 = ('"DarkerGray30"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = DarkerGray30 ) ), ]')
            index = block_colors_map.by_k('"DarkerGray"').index + 1
            block_colors_map.insert(index, darkergray30)

            # Update DropdownBlanc colors
            _edit_componentstate(block_colors_map, '"DropdownBlanc"', 'Normal', 'M81_ArtichokeVeryLight')
            _edit_componentstate(block_colors_map, '"DropdownBlanc"', 'Highlighted', 'M81_Artichoke')
            _edit_componentstate(block_colors_map, '"DropdownBlanc"', 'Toggled', 'M81_Artichoke')

            # Add ButtonHUD BigBorder M81CubeAction
            buttonhudbigborder_m81cubeaction = (
                f'("ButtonHUD/BigBorder_M81CubeAction",        MAP ['
                f'                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                            ( ~/ComponentState/Normal,                TColorRTTI( Color = BlancEquipe ) ),'
                f'                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc750 ) ),'
                f'                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                        ])'
            )
            index = block_colors_map.by_k('"ButtonHUD/BigBorder"').index + 1
            block_colors_map.insert(index, buttonhudbigborder_m81cubeaction)

            # Add AlertPanel Gradient1M81
            alertpanel_gradient1m81 = ('"AlertPanel/Gradient1M81"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,191] ) ), ]')
            index = block_colors_map.by_k('"AlertPanel/Gradient1"').index + 1
            block_colors_map.insert(index, alertpanel_gradient1m81)

            # Update DeckOverview colors
            _edit_componentstate(block_colors_map, '"DeckOverview/CaseGrisee/EditableText/Selected"', 'Normal', 'M81_ArtichokeVeryLight62')
            _edit_componentstate(block_colors_map, '"DeckOverview/CaseGrisee/EditableText/Selected"', 'Highlighted', 'M81_ArtichokeVeryLight62')

            # Add PanelScore ScoreBackgroundM81
            panelscore_scorebackgroundm81 = ('"PanelScore/ScoreBackgroundM81"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = M81_Artichoke ) ), ]')
            index = block_colors_map.by_k('"PanelScore/ScoreBackground"').index + 1
            block_colors_map.insert(index, panelscore_scorebackgroundm81)

            # Update SliderBasic colors
            _edit_componentstate(block_colors_map, '"SliderBasic/ThumbColor"', 'Normal', 'M81_ArtichokeVeryLight')
            _edit_componentstate(block_colors_map, '"SliderBasic/SliderBar"', 'Normal', 'M81_Ebony')

            # Add BoutonTimePanel colors
            boutontimepanelm81pause = (
                f'("BoutonTimePanelM81Pause",                                            MAP ['
                f'                                                            ( ~/ComponentState/Normal,      TColorRTTI( Color = [255,66,33,128] ) ),'
                f'                                                            ( ~/ComponentState/Highlighted, TColorRTTI( Color = [255,66,33,255] ) ),'
                f'                                                            ( ~/ComponentState/Clicked,     TColorRTTI( Color = [255,66,33,255] ) ),'
                f'                                                            ( ~/ComponentState/Toggled,     TColorRTTI( Color = [255,66,33,255] ) ),'
                f'                                                       ])'
            )
            boutontimepanelm81slow = (
                f'("BoutonTimePanelM81Slow",                                            MAP ['
                f'                                                            ( ~/ComponentState/Normal,      TColorRTTI( Color = [255,176,0,128] ) ),'
                f'                                                            ( ~/ComponentState/Highlighted, TColorRTTI( Color = [255,176,0,255] ) ),'
                f'                                                            ( ~/ComponentState/Clicked,     TColorRTTI( Color = [255,176,0,255] ) ),'
                f'                                                            ( ~/ComponentState/Toggled,     TColorRTTI( Color = [255,176,0,255] ) ),'
                f'                                                       ])'
            )
            boutontimepanelm81play = (
                f'("BoutonTimePanelM81Play",                                            MAP ['
                f'                                                            ( ~/ComponentState/Normal,      TColorRTTI( Color = [102,255,102,128] ) ),'
                f'                                                            ( ~/ComponentState/Highlighted, TColorRTTI( Color = [102,255,102,255] ) ),'
                f'                                                            ( ~/ComponentState/Clicked,     TColorRTTI( Color = [102,255,102,255] ) ),'
                f'                                                            ( ~/ComponentState/Toggled,     TColorRTTI( Color = [102,255,102,255] ) ),'
                f'                                                       ])'
            )
            boutontimepanelm81fast = (
                f'("BoutonTimePanelM81Fast",                                            MAP ['
                f'                                                           ( ~/ComponentState/Normal,      TColorRTTI( Color = [255,204,0,128] ) ),'
                f'                                                           ( ~/ComponentState/Highlighted, TColorRTTI( Color = [255,204,0,255] ) ),'
                f'                                                           ( ~/ComponentState/Clicked,     TColorRTTI( Color = [255,204,0,255] ) ),'
                f'                                                           ( ~/ComponentState/Toggled,     TColorRTTI( Color = [255,204,0,255] ) ),'
                f'                                                      ])'
            )
            index = block_colors_map.by_k('"BoutonTimePanel"').index + 1
            block_colors_map.insert(index, boutontimepanelm81fast)
            block_colors_map.insert(index, boutontimepanelm81play)
            block_colors_map.insert(index, boutontimepanelm81slow)
            block_colors_map.insert(index, boutontimepanelm81pause)

            # Update playerHelper colors
            _edit_componentstate(block_colors_map, '"playerHelper/Cover/Otan_line"', 'Normal', 'M81_AppleIIc')
            _edit_componentstate(block_colors_map, '"playerHelper/Cover/Otan_line"', 'Highlighted', 'M81_AppleIIc')
            _edit_componentstate(block_colors_map, '"playerHelper/Cover/Otan_line"', 'Toggled', 'M81_AppleIIc')

            _edit_componentstate(block_colors_map, '"playerHelper/Cover/Pact_line"', 'Normal', 'M81_P3AmberOrange')
            _edit_componentstate(block_colors_map, '"playerHelper/Cover/Pact_line"', 'Highlighted', 'M81_P3AmberOrange')
            _edit_componentstate(block_colors_map, '"playerHelper/Cover/Pact_line"', 'Toggled', 'M81_P3AmberOrange')

            # Add TacticButton highlightable block
            tacticbutton_highlightableblockm81 = (
                f'("TacticButton_highlightableBlockM81",          MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoal  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc184 ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = Blanc184 ) ),'
                f'                                   ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_DarkCharcoalTransparent ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"TacticButton_highlightable"').index + 1
            block_colors_map.insert(index, tacticbutton_highlightableblockm81)

            # Add TacticPanel block
            tacticpanelblockm81 = ('"TacticPanelBlockM81"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = M81_DarkCharcoalTransparent ) ), ]')
            index = block_colors_map.by_k('"TacticPanel"').index + 1
            block_colors_map.insert(index, tacticpanelblockm81)

            # Handle line colors map
            line_colors_map = row.v.by_m("LineColorsMap").v
            
            # Add M81 Woodland UI Colors
            new_lines = [
                ('"M81_Artichoke"',          'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,255] ) ), ]'),
                ('"M81_Artichoke191"',          'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,191] ) ), ]'),
                ('"M81_ArtichokeVeryLight"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [219,204,168,255] ) ), ]'),
                ('"M81_ArtichokeVeryLight62"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [219,204,168,158] ) ), ]'),
                ('"M81_ArtichokeNearWhite"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,240,225,255] ) ), ]'),
                ('"M81_ArtichokeTransparent"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,128] ) ), ]'),
                ('"M81_Artichoke64"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,64] ) ), ]'),
                ('"M81_DarkCharcoal"',    'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [49,56,49,255] ) ), ]'),
                ('"M81_DarkCharcoalSelection"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [148,168,148,210] ) ), ]'),
                ('"M81_DarkCharcoalClicked"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [197,224,197,210] ) ), ]'),
                ('"M81_DarkCharcoalTransparent"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [49,56,49,113] ) ), ]'),
                ('"M81_Ebony"',           'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [80,101,77,255] ) ), ]'),
                ('"M81_Ebony128"',            'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [80,101,77,128] ) ), ]'),
                ('"M81_EbonyDark"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [77,96,74,255] ) ), ]'),
                ('"M81_EbonyLight"',      'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [98,122,94,255] ) ), ]'),
                ('"M81_EbonyVeryDark"',   'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [67,84,64,255] ) ), ]'),
                ('"M81_Quincy"',          'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [101,89,73,255] ) ), ]'),
                ('"M81_VeryDarkCharcoal"',    'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [31,35,31,255] ) ), ]'),
                ('"M81_MonochromeCRT"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [40,40,40,255] ) ), ]'),
                ('"M81_AppleII"',             'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [51,255,51,255] ) ), ]'),
                ('"M81_AppleIIc"',            'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [102,255,102,255] ) ), ]'),
                ('"M81_AppleIIcTransparent"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [102,255,102,100] ) ), ]'),
                ('"M81_P3AmberOrange"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,176,0,255] ) ), ]'),
                ('"M81_P3AmberYellow"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,204,0,255] ) ), ]'),
                ('"M81_WhiteText95"',         'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [242,242,242,255] ) ), ]'),
            ]
            for line in new_lines:
                line_colors_map.insert(1, line)

            # Add UnitLabelBorder M81 Otan
            unitlabelborder_m81otan = (
                f'("UnitLabelBorder_M81_Otan",                            MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [210,210,210,128]  ) ),'
                f'                                                        (~/ComponentState/Highlighted,            TColorRTTI( Color = M81_WhiteText95  ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = [210,210,210,128]  ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = [210,210,210,128]) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_WhiteText95  ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = [210,210,210,128] ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = BleuVariable ) ),'
                f'                                                ])'
            )
            index = line_colors_map.by_k('"CyanFonceFulda"').index + 1
            line_colors_map.insert(index, unitlabelborder_m81otan)

            # Add BoutonTemps line
            boutontemps = (
                f'("BoutonTemps",                                        MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc184 ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [128,128,128,128] ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"Test"').index + 1
            line_colors_map.insert(index, boutontemps)

            # Add BoutonTemps line chat
            boutontempslinechatm81 = (
                f'("BoutonTempsLineChatM81",                                        MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc184 ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancEquipe ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = BlancEquipe ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = BlancEquipe ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [128,128,128,128] ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonTemps"').index + 1
            line_colors_map.insert(index, boutontempslinechatm81)

            # Add BoutonTemps M81 cube action line
            boutontempsm81cubeactionline = (
                f'("BoutonTempsM81CubeActionLine",                                        MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc184 ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonTempsLineChatM81"').index + 1
            line_colors_map.insert(index, boutontempsm81cubeactionline)

            # Add BoutonTemps line M81
            boutontempslinem81 = (
                f'("BoutonTempsLineM81",                                        MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_Ebony ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_EbonyLight ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_EbonyVeryDark ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_EbonyVeryDark ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_EbonyDark ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_Ebony ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [128,128,128,128] ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonTempsM81CubeActionLine"').index + 1
            line_colors_map.insert(index, boutontempslinem81)

            # Add BoutonTemps line multi M81
            boutontempslinemultim81 = (
                f'("BoutonTempsLineMultiM81",                                        MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_Artichoke ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = Blanc184 ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_EbonyVeryDark ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_EbonyDark ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_EbonyDark ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [128,128,128,128] ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonTempsLineM81"').index + 1
            line_colors_map.insert(index, boutontempslinemultim81)

            # Add BoutonTemps line airwing M81
            boutontempslineairwingm81 = (
                f'("BoutonTempsLineAirwingM81",                      MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc184 ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [128,128,128,128] ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonTempsLineMultiM81"').index + 1
            line_colors_map.insert(index, boutontempslineairwingm81)

            # Add ArmoryUnitButtonName M81
            armoryunitbuttonnamem81 = (
                f'("ArmoryUnitButtonNameM81",        MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = [101,89,73,220]  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [150,132,109,240] ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [101,89,73,210] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [119,105,87,220] ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [150,132,109,240] ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [25,25,25,150] ) ),'
                f'                               ])'
            )
            index = line_colors_map.by_k('"ArmoryUnitButtonName"').index + 1
            line_colors_map.insert(index, armoryunitbuttonnamem81)

            # Add ArmoryUnitButtonName M81 Artichoke
            armorunitbuttonnamem81artichoke = (
                f'("ArmoryUnitButtonNameM81Artichoke",        MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = [187,174,143,220]  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [226,210,174,240] ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [187,174,143,210] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [204,191,157,220] ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [226,210,174,240] ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [25,25,25,150] ) ),'
                f'                               ])'
            )
            index = line_colors_map.by_k('"ArmoryUnitButtonNameM81"').index + 1
            line_colors_map.insert(index, armorunitbuttonnamem81artichoke)

            # Add BoutonVignetteAchatArmory M81
            boutonvignetteachatarmorym81 = (
                f'("BoutonVignetteAchatArmoryM81",                           MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = Transparent  ) ),'
                f'                                                        (~/ComponentState/Highlighted,            TColorRTTI( Color = [219,204,168,255] ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = [193,180,149,255] ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = [156,145,119,255] ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [219,204,168,255] ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = [193,180,149,255] ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = Transparent ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonVignetteAchatArmory"').index + 1
            line_colors_map.insert(index, boutonvignetteachatarmorym81)

            # Add BoutonVignetteAchatArmory WACTUAL
            boutonvignetteachatarmoryWACTUAL = (
                f'("BoutonVignetteAchatArmoryWACTUAL",                           MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = Transparent  ) ),'
                f'                                                        (~/ComponentState/Highlighted,            TColorRTTI( Color = [40,154,40,255] ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = [36,110,36,255] ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = [25,76,25,255] ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [40,154,40,255] ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = [36,110,36,255] ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = Transparent ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonVignetteAchatArmoryM81"').index + 1
            line_colors_map.insert(index, boutonvignetteachatarmoryWACTUAL)

            # Update DeckCreator colors
            _edit_componentstate(line_colors_map, '"DeckCreator/AddUnitToDeck"', 'Normal', '[188,175,145,240]')
            _edit_componentstate(line_colors_map, '"DeckCreator/AddUnitToDeck"', 'Highlighted', '[219,204,168,220]')
            _edit_componentstate(line_colors_map, '"DeckCreator/AddUnitToDeck"', 'Clicked', '[80,101,77,220]')
            _edit_componentstate(line_colors_map, '"DeckCreator/AddUnitToDeck"', 'Grayed', 'M81_DarkCharcoal')

            _edit_componentstate(line_colors_map, '"DeckCreator/SlotLibre"', 'Normal', '[156,145,119,128]')
            _edit_componentstate(line_colors_map, '"DeckCreator/SlotSelectionne"', 'Normal', '[219,204,168,220]')

            # Update ConfirmButton border colors
            _edit_componentstate(line_colors_map, '"ConfirmButton/Border"', 'Grayed', 'M81_MonochromeCRT')
            _edit_componentstate(line_colors_map, '"ConfirmButton/Border"', 'Normal', '[36,110,36,255]')
            _edit_componentstate(line_colors_map, '"ConfirmButton/Border"', 'Highlighted', '[43,121,43,255]')
            _edit_componentstate(line_colors_map, '"ConfirmButton/Border"', 'Clicked', '[50,135,50,255]')
            _edit_componentstate(line_colors_map, '"ConfirmButton/Border"', 'Toggled', '[43,121,43,255]')

            # Add TimePanel button borders
            timepanel_buttonborderm81pause = (
                f'("TimePanel/ButtonBorderM81Pause",                          MAP [ '
                f'                                                          ( ~/ComponentState/Normal, TColorRTTI( Color = [255,66,33,191] ) ),'
                f'                                                          ( ~/ComponentState/Toggled, TColorRTTI( Color = [255,66,33,255] ) ),'
                f'                                                        ])'
            )
            timepanel_buttonborderm81slow = (
                f'("TimePanel/ButtonBorderM81Slow",                          MAP [ '
                f'                                                          ( ~/ComponentState/Normal, TColorRTTI( Color = [255,176,0,191] ) ),'
                f'                                                          ( ~/ComponentState/Toggled, TColorRTTI( Color = [255,176,0,255] ) ),'
                f'                                                        ])'
            )
            timepanel_buttonborderm81play = (
                f'("TimePanel/ButtonBorderM81Play",                          MAP [ '
                f'                                                          ( ~/ComponentState/Normal, TColorRTTI( Color = [102,255,102,191] ) ),'
                f'                                                          ( ~/ComponentState/Toggled, TColorRTTI( Color = [102,255,102,255] ) ),'
                f'                                                        ])'
            )
            timepanel_buttonborderm81fast = (
                f'("TimePanel/ButtonBorderM81Fast",                          MAP [ '
                f'                                                          ( ~/ComponentState/Normal, TColorRTTI( Color = [255,204,0,191] ) ),'
                f'                                                          ( ~/ComponentState/Toggled, TColorRTTI( Color = [255,204,0,255] ) ),'
                f'                                                        ])'
            )
            index = line_colors_map.by_k('"TimePanel/ButtonBorder"').index + 1
            line_colors_map.insert(index, timepanel_buttonborderm81fast)
            line_colors_map.insert(index, timepanel_buttonborderm81play)
            line_colors_map.insert(index, timepanel_buttonborderm81slow)
            line_colors_map.insert(index, timepanel_buttonborderm81pause)

            # Add TacticButton highlightable line
            tacticbutton_highlightablelinem81 = (
                f'("TacticButton_highlightableLineM81",          MAP ['
                f'                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_DarkCharcoalSelection ) ),'
                f'                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_DarkCharcoalClicked ) ),'
                f'                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_DarkCharcoalSelection ) ),'
                f'                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_DarkCharcoalClicked ) ),'
                f'                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [128,128,128,128] ) ),'
                f'                                   ])'
            )
            index = line_colors_map.by_k('"TacticButton_highlightable"').index + 1
            line_colors_map.insert(index, tacticbutton_highlightablelinem81)

            # Update TacticPanel color
            _edit_componentstate(line_colors_map, '"TacticPanel"', 'Normal', '[14,14,14,75]') 
            
                        # Handle text colors map
            text_colors_map = row.v.by_m("TextColorsMap").v
            
            # Add M81 Woodland UI Colors
            new_lines = [
                ('"M81_Artichoke"',          'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,255] ) ), ]'),
                ('"M81_Artichoke191"',          'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,191] ) ), ]'),
                ('"M81_ArtichokeVeryLight"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [219,204,168,255] ) ), ]'),
                ('"M81_ArtichokeVeryLight62"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [219,204,168,158] ) ), ]'),
                ('"M81_ArtichokeNearWhite"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,240,225,255] ) ), ]'),
                ('"M81_ArtichokeTransparent"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,128] ) ), ]'),
                ('"M81_Artichoke64"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,64] ) ), ]'),
                ('"M81_DarkCharcoal"',    'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [49,56,49,255] ) ), ]'),
                ('"M81_DarkCharcoalSelection"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [148,168,148,210] ) ), ]'),
                ('"M81_DarkCharcoalClicked"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [197,224,197,210] ) ), ]'),
                ('"M81_DarkCharcoalTransparent"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [49,56,49,113] ) ), ]'),
                ('"M81_Ebony"',           'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [80,101,77,255] ) ), ]'),
                ('"M81_Ebony128"',            'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [80,101,77,128] ) ), ]'),
                ('"M81_EbonyDark"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [77,96,74,255] ) ), ]'),
                ('"M81_EbonyLight"',      'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [98,122,94,255] ) ), ]'),
                ('"M81_EbonyVeryDark"',   'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [67,84,64,255] ) ), ]'),
                ('"M81_Quincy"',          'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [101,89,73,255] ) ), ]'),
                ('"M81_VeryDarkCharcoal"',    'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [31,35,31,255] ) ), ]'),
                ('"M81_MonochromeCRT"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [40,40,40,255] ) ), ]'),
                ('"M81_AppleII"',             'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [51,255,51,255] ) ), ]'),
                ('"M81_AppleIIc"',            'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [102,255,102,255] ) ), ]'),
                ('"M81_AppleIIcTransparent"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [102,255,102,100] ) ), ]'),
                ('"M81_P3AmberOrange"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,176,0,255] ) ), ]'),
                ('"M81_P3AmberYellow"',       'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,204,0,255] ) ), ]'),
                ('"M81_WhiteText95"',         'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [242,242,242,255] ) ), ]'),
                ('"M81_RedPhosphor"',         'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [255,66,33,255] ) ), ]'),
            ]
            for line in new_lines:
                text_colors_map.insert(1, line)

            # Add M81 RoE Default
            m81roe_default = (
                f'("M81_RoE_Default",                     MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"Debrief/UpdateProfile"').index + 1
            text_colors_map.insert(index, m81roe_default)

            # Update playerHelper text colors
            _edit_componentstate(text_colors_map, '"playerHelper/texte/Otan_element"', 'ToggleHighlighted', '[255,255,255,255]')

            # Add WeaponButton Overblock text
            weaponbutton_overblocktextm81 = (
                f'("WeaponButton/OverblockTextM81",      MAP ['
                f'                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = DarkerGray30 ) ),'
                f'                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_EbonyDark ) ),'
                f'                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_Ebony ) ),'
                f'                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = [30,30,30,120] ) ),'
                f'                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color =  [30,30,30,90] ) ),'
                f'                        ])'
            )
            index = text_colors_map.by_k('"WeaponButton/Overblock"').index + 1
            text_colors_map.insert(index, weaponbutton_overblocktextm81)

            # Add BoutonTemps text
            boutontemps = (
                f'("BoutonTemps",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = Blanc184 ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"BoutonTemps_Text"').index + 1
            text_colors_map.insert(index, boutontemps)

            # Add BoutonTemps text M81
            boutontempstextm81 = (
                f'("BoutonTempsTextM81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_ArtichokeVeryLight ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_ArtichokeNearWhite ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_Artichoke ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_Artichoke ) ),'
                f'                                            ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_Artichoke ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"BoutonTemps"').index + 1
            text_colors_map.insert(index, boutontempstextm81)

            # Add WeaponIcon M81
            weaponiconm81 = ('"WeaponIcon_M81"', 'MAP [( ~/ComponentState/Normal, TColorRTTI( Color = [199+20,184+20,148+20,255] ) ),]')
            index = text_colors_map.by_k('"MarronPanel_blanc"').index + 1
            text_colors_map.insert(index, weaponiconm81)

            # Add SM Feldgrau WACTUAL
            sm_feldgrauwactual = (
                f'("SM_FeldgrauWACTUAL",                         MAP ['
                f'                                        ( ~/ComponentState/Normal,                 TColorRTTI( Color = Feldgrau ) ),'
                f'                                        ( ~/ComponentState/Highlighted,            TColorRTTI( Color = [93,116,88,255] ) ),'
                f'                                        ( ~/ComponentState/Toggled,                TColorRTTI( Color = [101,128,96,255] ) ),'
                f'                                    ])'
            )
            index = text_colors_map.by_k('"SM_Feldgrau"').index + 1
            text_colors_map.insert(index, sm_feldgrauwactual)

            # Add TacticButton highlightable text
            tacticbutton_highlightabletextm81 = (
                f'("TacticButton_highlightableTextM81",              MAP ['
                f'                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = Blanc184 ) ),'
                f'                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc7 ) ),'
                f'                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancPur ) ),'
                f'                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = BlancEquipe ) ),'
                f'                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = BlancEquipe ) ),'
                f'                                    ])'
            )
            index = text_colors_map.by_k('"TacticButton_highlightable"').index + 1
            text_colors_map.insert(index, tacticbutton_highlightabletextm81)

            # Add TacticPanel text
            tacticpaneltextm81 = ('"TacticPanelTextM81"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = BlancEquipe ) ), ]')
            index = text_colors_map.by_k('"TacticPanel"').index + 1
            text_colors_map.insert(index, tacticpaneltextm81)

            # Update moral color
            _edit_componentstate(text_colors_map, '"moral_color_bad_1"', 'Normal', '[255,200,0,255]')

            # Update BoutonXP deck colors
            _edit_componentstate(text_colors_map, '"BoutonXP_deck"', 'Grayed', 'M81_DarkCharcoal')
            _edit_componentstate(text_colors_map, '"BoutonXP_deck"', 'Normal', 'M81_Ebony')
            _edit_componentstate(text_colors_map, '"BoutonXP_deck"', 'Highlighted', 'M81_EbonyLight')
            _edit_componentstate(text_colors_map, '"BoutonXP_deck"', 'Clicked', 'M81_EbonyVeryDark')
            _edit_componentstate(text_colors_map, '"BoutonXP_deck"', 'Toggled', 'M81_EbonyVeryDark')
            _edit_componentstate(text_colors_map, '"BoutonXP_deck"', 'ToggleHighlighted', 'M81_EbonyVeryDark')

            # Add BoutonXP deck chevron
            boutonxpdeck_chevronm81 = (
                f'("BoutonXP_deck_chevronM81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_ArtichokeNearWhite ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = BlancPur ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"BoutonXP_deck_chevron"').index + 1
            text_colors_map.insert(index, boutonxpdeck_chevronm81)

            # Add TransportedText M81
            transportedtextm81 = (
                f'("TransportedText_M81",                                MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_DarkCharcoalTransparent ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [14,28,31,255] ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = [14,28,31,255] ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [14,28,31,255] ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"text_couleur_bleunavy_secondaire"').index + 1
            text_colors_map.insert(index, transportedtextm81)

            # Update hint colors
            _edit_componentstate(text_colors_map, '"hint_fond_meilleureLecture"', 'Normal', '[12,55,16,255]')
            _edit_componentstate(text_colors_map, '"hint_titre_meilleureLecture"', 'Normal', '[12,56,16,255]')

            # Add new type colors
            new_lines = [
                ('"TypeF"',              'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [25,76,25,255] ) ), ]'),  # ForestGreenDark
                ('"TypeG"',              'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [36,110,36,255] ) ), ]'), # ForestGreen
                ('"TypeH"',              'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [40,154,40,255] ) ), ]'), # ForestGreenLight
                ('"TypeI"',              'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [20,132,93,171] ) ), ]'), # TypeC Equivalent
                ('"TypeJ"',              'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [12,55,16,255] ) ), ]'),  # ForestGreenVeryDark
            ]
            index = text_colors_map.by_k('"TypeA"').index
            for line in reversed(new_lines):
                text_colors_map.insert(index, line)

            # Update CouleurTexture boutonShortcuts colors
            _edit_componentstate(text_colors_map, '"CouleurTexture_boutonShortcuts"', 'Clicked', 'M81_AppleIIc')
            _edit_componentstate(text_colors_map, '"CouleurTexture_boutonShortcuts"', 'Toggled', 'M81_AppleIIc')
            _edit_componentstate(text_colors_map, '"CouleurTexture_boutonShortcuts"', 'ToggleHighlighted', 'M81_AppleIIc')
            _edit_componentstate(text_colors_map, '"CouleurTexture_boutonShortcuts"', 'ToggleClicked', 'M81_AppleIIc')

            # Remove and add CouleurBordure boutonShortcuts
            text_colors_map.remove_by_key('"CouleurBordure_boutonShortcuts"')
            couleurbordure_boutonshortcuts = (
                f'("CouleurBordure_boutonShortcuts", MAP ['
                f'                    ( ~/ComponentState/Normal,            TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                    ( ~/ComponentState/Clicked,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/Toggled,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleHighlighted, TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleClicked,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                ])'
            )
            index = text_colors_map.by_k('"CouleurFond_boutonShortcuts"').index + 1
            text_colors_map.insert(index, couleurbordure_boutonshortcuts)

            # Add CouleurBordure boutonShortcuts text
            couleurbordure_boutonshortcutstextm81 = (
                f'("CouleurBordure_boutonShortcutsTextM81", MAP ['
                f'                    ( ~/ComponentState/Normal,            TColorRTTI( Color = [140,140,140,170] ) ),'
                f'                    ( ~/ComponentState/Clicked,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/Toggled,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleHighlighted, TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleClicked,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                ])'
            )
            index = text_colors_map.by_k('"CouleurBordure_boutonShortcuts"').index + 1
            text_colors_map.insert(index, couleurbordure_boutonshortcutstextm81)

            # Add CouleurTexture boutonShortcuts text
            couleurtexture_boutonshortcutstextm81 = (
                f'("CouleurTexture_boutonShortcutsTextM81", MAP ['
                f'                    ( ~/ComponentState/Grayed,            TColorRTTI( Color = [255,255,255,80] ) ),'
                f'                    ( ~/ComponentState/Normal,            TColorRTTI( Color = M81_ArtichokeNearWhite ) ),'
                f'                    ( ~/ComponentState/Highlighted,       TColorRTTI( Color = Blanc2 ) ),'
                f'                    ( ~/ComponentState/Clicked,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/Toggled,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleHighlighted, TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleClicked,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                ])'
            )
            index = text_colors_map.by_k('"CouleurBordure_boutonShortcutsTextM81"').index + 1
            text_colors_map.insert(index, couleurtexture_boutonshortcutstextm81)

            # Add Fulda Turquoise WACTUAL
            fulda_turquoisewactual = (
                f'("Fulda_TurquoiseWACTUAL",            MAP ['
                f'                            ( ~/ComponentState/Grayed,                 TColorRTTI( Color = Transparent ) ),'
                f'                            ( ~/ComponentState/Normal,                 TColorRTTI( Color = Fulda_Turquoise ) ),'
                f'                            ( ~/ComponentState/Highlighted,            TColorRTTI( Color = Fulda_VertBleu ) ),'
                f'                            ( ~/ComponentState/Clicked,                TColorRTTI( Color = Fulda_Turquoise2 ) ),'
                f'                            ( ~/ComponentState/Toggled,                TColorRTTI( Color = Fulda_VertBleu ) ),'
                f'                            ( ~/ComponentState/ToggleHighlighted,      TColorRTTI( Color = Fulda_Turquoise2 ) ),'
                f'                        ])'
            )
            index = text_colors_map.by_k('"Fulda_Turquoise"').index + 1
            text_colors_map.insert(index, fulda_turquoisewactual)

            # Update ButtonHUD Text2 colors
            _edit_componentstate(text_colors_map, '"ButtonHUD/Text2"', 'Normal', 'BlancEquipe')
            _edit_componentstate(text_colors_map, '"ButtonHUD/Text2"', 'Highlighted', 'BlancEquipe')
            _edit_componentstate(text_colors_map, '"ButtonHUD/Text2"', 'Clicked', 'M81_AppleII')
            _edit_componentstate(text_colors_map, '"ButtonHUD/Text2"', 'Toggled', 'M81_AppleII')
            _edit_componentstate(text_colors_map, '"ButtonHUD/Text2"', 'ToggleHighlighted', 'M81_AppleIIc')

            # Add ButtonHUD Text2 airwing
            buttonhud_text2airwingm81 = (
                f'("ButtonHUD/Text2AirwingM81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"ButtonHUD/Text2"').index + 1
            text_colors_map.insert(index, buttonhud_text2airwingm81)

            # Add ButtonHUD Text2 toggle
            buttonhud_text2toggle = (
                f'("ButtonHUD/Text2_toggle",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"ButtonHUD/Text2AirwingM81"').index + 1
            text_colors_map.insert(index, buttonhud_text2toggle)

            # Add ButtonHUD Text2 M81 cube action
            buttonhud_text2m81cubeaction = (
                f'("ButtonHUD/Text2_M81CubeAction",                       MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"ButtonHUD/Text2_toggle"').index + 1
            text_colors_map.insert(index, buttonhud_text2m81cubeaction)

            # Add ButtonHUD Text2 WACTUAL
            buttonhud_text2wactual = (
                f'("ButtonHUD/Text2WACTUAL",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = Blanc184 ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc7 ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = [210,226,156,255] ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [210,226,156,255] ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"ButtonHUD/Text2_M81CubeAction"').index + 1
            text_colors_map.insert(index, buttonhud_text2wactual)

            # Add ButtonHUD Text2 pawn WACTUAL (completing the previous block)
            buttonhud_text2pawnwactual = (
                f'("ButtonHUD/Text2_pawnWACTUAL",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = [220,220,220,255] ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc7 ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = [210,226,156,255] ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [210,226,156,255] ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"ButtonHUD/Text2_pawn"').index + 1
            text_colors_map.insert(index, buttonhud_text2pawnwactual)

            # Add DeploymentPhase CancelTimer M81
            deploymentphase_canceltimerm81 = (
                f'("DeploymentPhase/CancelTimerM81",              MAP [ ( ~/ComponentState/Normal,      TColorRTTI( Color = M81_DarkCharcoal) ),'
                f'                                              ( ~/ComponentState/Highlighted, TColorRTTI( Color = BlancPur) ),'
                f'                                              ( ~/ComponentState/Clicked,     TColorRTTI( Color = BlancPur) ),'
                f'                                            ])'
            )
            index = text_colors_map.by_k('"DeploymentPhase/CancelTimer"').index + 1
            text_colors_map.insert(index, deploymentphase_canceltimerm81)

            # Add DeploymentPhase IdleUnit M81
            deploymentphase_idleunitm81 = (
                f'("DeploymentPhase/IdleUnitM81",                 MAP ['
                f'                                              ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                              ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                              ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                              ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                              ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                          ])'
            )
            index = text_colors_map.by_k('"DeploymentPhase/CancelTimerM81"').index + 1
            text_colors_map.insert(index, deploymentphase_idleunitm81)
# fmt: on