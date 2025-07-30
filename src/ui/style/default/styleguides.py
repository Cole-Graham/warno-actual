"""Functions for modifying UI style guides."""
from src.utils.logging_utils import setup_logger
# from src import ndf
# from src.utils.ndf_utils import is_obj_type

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
        source_path: NDF file containing style guide definitions
    """
    logger.info("Editing DefaultStyleGuides.ndf")
    
    for row in source_path:
        if row.namespace == "DefaultStyleGuide":
            
            # Handle text styles map
            text_styles_map = row.v.by_m("TextStylesMap").v
            new_text_styles = [
                ('"ActivationPointTemp_M81"', "MAP [ ( ~/ComponentState/Normal, TextStyleActivationPointTemp_M81 ), ]"),
            ]
            for style_tuple in new_text_styles:
                text_styles_map.insert(1, style_tuple)
            
            # Handle line sizes map
            line_sizes_map = row.v.by_m("LineSizesMap").v
            line_sizes_map.insert(1, ('"1.5"', "MAP [ ( ~/ComponentState/Normal, TFloatRTTI ( Value = 1.5 ) ), ]"))
            
            # Handle block colors map
            block_colors_map = row.v.by_m("BlockColorsMap").v
            
            # Add M81 Woodland UI Colors
            new_block_colors = [
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
            for color_tuple in new_block_colors:
                block_colors_map.insert(1, color_tuple)

            # Add BoutonTemps background and block
            boutontemps_background_m81 = (
                f'("BoutonTemps_Background_M81",                    MAP ['
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
            block_colors_map.insert(index, boutontemps_background_m81)
            
            boutontemps_roe_m81 = (
                f'("BoutonTemps_ROE_M81",                    MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = [80,101,77,255]  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [49,56,49,255] ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [49,56,49,255] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [49,56,49,255] ) ), '
                f'                                   ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = [49,56,49,255] ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [122,190,167,78] ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"BoutonTemps_Background_M81"').index + 1
            block_colors_map.insert(index, boutontemps_roe_m81)

            # Update CustomFlareText colors
            _edit_componentstate(block_colors_map, '"CustomFlareText"', 'Normal', 'M81_ArtichokeNearWhite')
            _edit_componentstate(block_colors_map, '"CustomFlareText"', 'Highlighted', 'M81_EbonyVeryDark')

            # Add BoutonTemps pawn background
            boutontemps_pawn_background_m81 = (
                f'("BoutonTemps_pawn_Background_M81",                    MAP ['
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
            block_colors_map.insert(index, boutontemps_pawn_background_m81)

            # Add BoutonFlares background
            boutonflares_background_m81 = (
                f'("BoutonFlares_Background_M81",            MAP ['
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
            block_colors_map.insert(index, boutonflares_background_m81)

            # Add BoutonSelectionMultiple background
            boutonselectionmultiple_background_m81 = (
                f'("BoutonSelectionMultiple_Background_M81",        MAP ['
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
            block_colors_map.insert(index, boutonselectionmultiple_background_m81)

            # Add OffMapUnitButtonName
            offmapunitbuttonname_m81 = (
                f'("OffMapUnitButtonName_M81",        MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoal  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [78,96,75,191] ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"OffMapUnitButtonName"').index + 1
            block_colors_map.insert(index, offmapunitbuttonname_m81)
            # TODO: find out why this was being removed (probably not a good reason)
            # block_colors_map.remove_by_key('"OffMapUnitButtonName"')

            # Add M81 Production
            m81_production = (
                f'("M81_Production",                  MAP ['
                f'                                   ( ~/ComponentState/Normal,                 TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                   ( ~/ComponentState/Highlighted,            TColorRTTI( Color = M81_DarkCharcoalSelection ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"H2_bleu_5"').index + 1
            block_colors_map.insert(index, m81_production)

            # Add NoirButton
            # TODO: confirmed this is not needed
            # noirbutton = (
            #     f'("NoirButton",            MAP ['
            #     f'                           ( ~/ComponentState/Grayed,                 TColorRTTI( Color = Transparent ) ),'
            #     f'                           ( ~/ComponentState/Normal,                 TColorRTTI( Color = NoirPur ) ),'
            #     f'                           ( ~/ComponentState/Highlighted,            TColorRTTI( Color = NoirPur ) ),'
            #     f'                           ( ~/ComponentState/Clicked,                TColorRTTI( Color = NoirPur ) ),'
            #     f'                           ( ~/ComponentState/Toggled,                TColorRTTI( Color = NoirPur ) ),'
            #     f'                           ( ~/ComponentState/ToggleHighlighted,      TColorRTTI( Color = NoirPur ) ),'
            #     f'                       ])'
            # )
            # index = block_colors_map.by_k('"Fulda2_blanc15"').index + 1
            # block_colors_map.insert(index, noirbutton)

            # Add DarkerGray30
            darkergray30 = ('"DarkerGray30"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = DarkerGray30 ) ), ]')
            index = block_colors_map.by_k('"DarkerGray"').index + 1
            block_colors_map.insert(index, darkergray30)
            
            # Add DropdownBlanc M81
            dropdownblanc_m81 = (
                f'("DropdownBlanc_M81",              MAP ['
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = GrayMineShaft ) ),'
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_ArtichokeVeryLight ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_Artichoke ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_Artichoke ) ),'
                f'                               ])'
            )
            index = block_colors_map.by_k('"DropdownBlanc"').index + 1
            block_colors_map.insert(index, dropdownblanc_m81)

            # Add ButtonHUD BigBorder CubeAction M81
            buttonhudbigborder_cubeaction_m81 = (
                f'("ButtonHUD/BigBorder_CubeAction_M81",        MAP ['
                f'                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                            ( ~/ComponentState/Normal,                TColorRTTI( Color = BlancEquipe ) ),'
                f'                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc750 ) ),'
                f'                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                        ])'
            )
            index = block_colors_map.by_k('"ButtonHUD/BigBorder"').index + 1
            block_colors_map.insert(index, buttonhudbigborder_cubeaction_m81)

            # Add AlertPanel Gradient1M81
            alertpanel_gradient1_m81 = ('"AlertPanel/Gradient1_M81"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [156,145,119,191] ) ), ]')
            index = block_colors_map.by_k('"AlertPanel/Gradient1"').index + 1
            block_colors_map.insert(index, alertpanel_gradient1_m81)
            
            # Add DeckOverview CaseGrisee EditableText Selected m81
            deckoverview_casegrisee_editabletext_selected_m81 = (
                f'("DeckOverview/CaseGrisee/EditableText/Selected_M81",               MAP ['
                f'                                                            ( ~/ComponentState/Normal, TColorRTTI( Color = M81_ArtichokeVeryLight62 ) ),'
                f'                                                            ( ~/ComponentState/Highlighted, TColorRTTI( Color = M81_ArtichokeVeryLight62 ) ),'
                f'                                                        ])'
            )
            index = block_colors_map.by_k('"DeckOverview/CaseGrisee/EditableText/Selected"').index + 1
            block_colors_map.insert(index, deckoverview_casegrisee_editabletext_selected_m81)

            # Add PanelScore ScoreBackgroundM81
            panelscore_scorebackground_m81 = ('"PanelScore/ScoreBackground_M81"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = M81_Artichoke ) ), ]')
            index = block_colors_map.by_k('"PanelScore/ScoreBackground"').index + 1
            block_colors_map.insert(index, panelscore_scorebackground_m81)
            
            # Add SliderBasic m81
            sliderbasic_thumbcolor_m81 = ('"SliderBasic/ThumbColor_M81"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = M81_ArtichokeVeryLight ) ), ]')
            index = block_colors_map.by_k('"SliderBasic/ThumbColor"').index + 1
            block_colors_map.insert(index, sliderbasic_thumbcolor_m81)
            
            sliderbasic_sliderbar_m81 = ('"SliderBasic/SliderBar_M81"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = M81_Ebony ) ), ]')
            index = block_colors_map.by_k('"SliderBasic/SliderBar"').index + 1
            block_colors_map.insert(index, sliderbasic_sliderbar_m81)

            # Add BoutonTimePanel colors
            boutontimepanel_m81pause = (
                f'("BoutonTimePanel_M81Pause",                                            MAP ['
                f'                                                            ( ~/ComponentState/Normal,      TColorRTTI( Color = [255,66,33,128] ) ),'
                f'                                                            ( ~/ComponentState/Highlighted, TColorRTTI( Color = [255,66,33,255] ) ),'
                f'                                                            ( ~/ComponentState/Clicked,     TColorRTTI( Color = [255,66,33,255] ) ),'
                f'                                                            ( ~/ComponentState/Toggled,     TColorRTTI( Color = [255,66,33,255] ) ),'
                f'                                                       ])'
            )
            boutontimepanel_m81slow = (
                f'("BoutonTimePanel_M81Slow",                                            MAP ['
                f'                                                            ( ~/ComponentState/Normal,      TColorRTTI( Color = [255,176,0,128] ) ),'
                f'                                                            ( ~/ComponentState/Highlighted, TColorRTTI( Color = [255,176,0,255] ) ),'
                f'                                                            ( ~/ComponentState/Clicked,     TColorRTTI( Color = [255,176,0,255] ) ),'
                f'                                                            ( ~/ComponentState/Toggled,     TColorRTTI( Color = [255,176,0,255] ) ),'
                f'                                                       ])'
            )
            boutontimepanel_m81play = (
                f'("BoutonTimePanel_M81Play",                                            MAP ['
                f'                                                            ( ~/ComponentState/Normal,      TColorRTTI( Color = [102,255,102,128] ) ),'
                f'                                                            ( ~/ComponentState/Highlighted, TColorRTTI( Color = [102,255,102,255] ) ),'
                f'                                                            ( ~/ComponentState/Clicked,     TColorRTTI( Color = [102,255,102,255] ) ),'
                f'                                                            ( ~/ComponentState/Toggled,     TColorRTTI( Color = [102,255,102,255] ) ),'
                f'                                                       ])'
            )
            boutontimepanel_m81fast = (
                f'("BoutonTimePanel_M81Fast",                                            MAP ['
                f'                                                           ( ~/ComponentState/Normal,      TColorRTTI( Color = [255,204,0,128] ) ),'
                f'                                                           ( ~/ComponentState/Highlighted, TColorRTTI( Color = [255,204,0,255] ) ),'
                f'                                                           ( ~/ComponentState/Clicked,     TColorRTTI( Color = [255,204,0,255] ) ),'
                f'                                                           ( ~/ComponentState/Toggled,     TColorRTTI( Color = [255,204,0,255] ) ),'
                f'                                                      ])'
            )
            index = block_colors_map.by_k('"BoutonTimePanel"').index + 1
            block_colors_map.insert(index, boutontimepanel_m81fast)
            block_colors_map.insert(index, boutontimepanel_m81play)
            block_colors_map.insert(index, boutontimepanel_m81slow)
            block_colors_map.insert(index, boutontimepanel_m81pause)

            # Update playerHelper colors
            # TODO: confirm no longer needed
            # _edit_componentstate(block_colors_map, '"playerHelper/Cover/Otan_line"', 'Normal', 'M81_AppleIIc')
            # _edit_componentstate(block_colors_map, '"playerHelper/Cover/Otan_line"', 'Highlighted', 'M81_AppleIIc')
            # _edit_componentstate(block_colors_map, '"playerHelper/Cover/Otan_line"', 'Toggled', 'M81_AppleIIc')

            # _edit_componentstate(block_colors_map, '"playerHelper/Cover/Pact_line"', 'Normal', 'M81_P3AmberOrange')
            # _edit_componentstate(block_colors_map, '"playerHelper/Cover/Pact_line"', 'Highlighted', 'M81_P3AmberOrange')
            # _edit_componentstate(block_colors_map, '"playerHelper/Cover/Pact_line"', 'Toggled', 'M81_P3AmberOrange')

            # Add chat button color style (block)
            button_chatcolorstyle_all_m81 = (
                f'("ChatBUTTONColorStyle_All_M81",          MAP ['
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
            block_colors_map.insert(index, button_chatcolorstyle_all_m81)

            # Add chat panel color style (block)
            chatpanelcolorstyle_all_m81 = ('"ChatPANELColorStyle_All_M81"', 'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = M81_DarkCharcoalTransparent ) ), ]')
            index = block_colors_map.by_k('"TacticPanel"').index + 1
            block_colors_map.insert(index, chatpanelcolorstyle_all_m81)

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

            # Add UnitLabelBorder M81
            unitlabelborder_m81 = (
                f'("UnitLabelBorder_M81",                            MAP ['
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
            line_colors_map.insert(index, unitlabelborder_m81)

            # Add BoutonTemps line M81
            boutontemps_line_m81 = (
                f'("BoutonTemps_Line_M81",                                        MAP ['
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
            line_colors_map.insert(index, boutontemps_line_m81)

            # Add BoutonTemps line chat
            # TODO: confirm no longer needed
            # boutontemps_line_chat_m81 = (
            #     f'("BoutonTemps_Line_Chat_M81",                                        MAP ['
            #     f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [153,190,201,102] ) ),'
            #     f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc184 ) ),'
            #     f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancEquipe ) ),'
            #     f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = BlancEquipe ) ),'
            #     f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [153,190,201,102] ) ),'
            #     f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = BlancEquipe ) ),'
            #     f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [128,128,128,128] ) ),'
            #     f'                                                   ])'
            # )
            # index = line_colors_map.by_k('"BoutonTemps_Line_M81"').index + 1
            # line_colors_map.insert(index, boutontemps_line_chat_m81)

            # Add BoutonTemps M81 cube action line
            boutontemps_line_cubeaction_m81 = (
                f'("BoutonTemps_Line_CubeAction_M81",                                        MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc184 ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonTemps_Line_Chat_M81"').index + 1
            line_colors_map.insert(index, boutontemps_line_cubeaction_m81)

            # Add BoutonTemps line M81
            boutontemps_line_m81 = (
                f'("BoutonTemps_Line_M81",                                        MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_Ebony ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_EbonyLight ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_EbonyVeryDark ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_EbonyVeryDark ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_EbonyDark ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_Ebony ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [128,128,128,128] ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonTemps_Line_CubeAction_M81"').index + 1
            line_colors_map.insert(index, boutontemps_line_m81)
            
            # Add BoutonTemps roe border M81
            boutontemps_roe_border_m81 = (
                f'("BoutonTemps_ROE_Border_M81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_ArtichokeVeryLight ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_ArtichokeNearWhite ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_Artichoke ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_Artichoke ) ),'
                f'                                            ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_Artichoke ) ),'
                f'                                        ])'
            )
            index = line_colors_map.by_k('"BoutonTemps_Line_M81"').index + 1
            line_colors_map.insert(index, boutontemps_roe_border_m81)

            # Add BoutonTemps line airwing M81
            boutontemps_line_airwing_m81 = (
                f'("BoutonTemps_Line_Airwing_M81",                      MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [153,190,201,102] ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc184 ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [128,128,128,128] ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"BoutonTemps_ROE_Border_M81"').index + 1
            line_colors_map.insert(index, boutontemps_line_airwing_m81)
            
            offmapunitbuttonname_line_m81 = (
                f'("OffMapUnitButtonName_Line_M81",        MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoal  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [105,92,105,220] ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [78,96,75,191] ) ),'
                f'                               ])'
            )
            index = line_colors_map.by_k('"BoutonTemps_Line_Airwing_M81"').index + 1
            line_colors_map.insert(index, offmapunitbuttonname_line_m81)

            # Add ArmoryUnitButtonName M81
            armoryunitbuttonname_m81 = (
                f'("ArmoryUnitButtonName_M81",        MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = [101,89,73,220]  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [150,132,109,240] ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [101,89,73,210] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [119,105,87,220] ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [150,132,109,240] ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [25,25,25,150] ) ),'
                f'                               ])'
            )
            index = line_colors_map.by_k('"ArmoryUnitButtonName"').index + 1
            line_colors_map.insert(index, armoryunitbuttonname_m81)

            # Add ArmoryUnitButtonName M81 Artichoke
            armoryunitbuttonname_m81_artichoke = (
                f'("ArmoryUnitButtonName_M81_Artichoke",        MAP ['
                f'                                   ( ~/ComponentState/Normal,                TColorRTTI( Color = [187,174,143,220]  ) ),'
                f'                                   ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [226,210,174,240] ) ),'
                f'                                   ( ~/ComponentState/Clicked,               TColorRTTI( Color = [187,174,143,210] ) ),'
                f'                                   ( ~/ComponentState/Toggled,               TColorRTTI( Color = [204,191,157,220] ) ),'
                f'                                   ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [226,210,174,240] ) ),'
                f'                                   ( ~/ComponentState/Grayed,                TColorRTTI( Color = [25,25,25,150] ) ),'
                f'                               ])'
            )
            index = line_colors_map.by_k('"ArmoryUnitButtonNameM81"').index + 1
            line_colors_map.insert(index, armoryunitbuttonname_m81_artichoke)

            # Add BoutonVignetteAchatArmory M81
            boutonvignetteachatarmory_m81 = (
                f'("BoutonVignetteAchatArmory_M81",                           MAP ['
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
            line_colors_map.insert(index, boutonvignetteachatarmory_m81)

            # Add BoutonVignetteAchatArmory WACTUAL
            # TODO: confirm this is not needed
            # boutonvignetteachatarmoryWACTUAL = (
            #     f'("BoutonVignetteAchatArmoryWACTUAL",                           MAP ['
            #     f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = Transparent  ) ),'
            #     f'                                                        (~/ComponentState/Highlighted,            TColorRTTI( Color = [40,154,40,255] ) ),'
            #     f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = [36,110,36,255] ) ),'
            #     f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = [25,76,25,255] ) ),'
            #     f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [40,154,40,255] ) ),'
            #     f'                                                        ( ~/ComponentState/ToggleClicked,         TColorRTTI( Color = [36,110,36,255] ) ),'
            #     f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = Transparent ) ),'
            #     f'                                                   ])'
            # )
            # index = line_colors_map.by_k('"BoutonVignetteAchatArmoryM81"').index + 1
            # line_colors_map.insert(index, boutonvignetteachatarmoryWACTUAL)
            
            # Add DeckCreator/AddUnitToDeck m81
            deckcreator_addunittodeck_m81 = (
                f'("DeckCreator/AddUnitToDeck_M81",                           MAP ['
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [188,175,145,240] ) ),'
                f'                                                        (~/ComponentState/Highlighted,            TColorRTTI( Color = [219,204,168,220] ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = [80,101,77,220] ) ),'
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                                   ])'
            )
            index = line_colors_map.by_k('"DeckCreator/AddUnitToDeck"').index + 1
            line_colors_map.insert(index, deckcreator_addunittodeck_m81)
            
            # Add deckcreator/slotlibre m81
            deckcreator_slotlibre_m81 = (
                f'("DeckCreator/SlotLibre_M81",                               MAP [ ( ~/ComponentState/Normal,      TColorRTTI( Color = [156,145,119,128] ) ), ])'
            )
            index = line_colors_map.by_k('"DeckCreator/SlotLibre"').index + 1
            line_colors_map.insert(index, deckcreator_slotlibre_m81)
            
            # Add deckcreator/slotselectionne m81
            # TODO: confirm no longer used in vanilla warno (probably since armory UI overhaul)
            # deckcreator_slotselectionne_m81 = (
            #     f'("DeckCreator/SlotSelectionne_M81",                               MAP [ ( ~/ComponentState/Normal,      TColorRTTI( Color = [219,204,168,220] ) ), ])'
            # )
            # index = line_colors_map.by_k('"DeckCreator/SlotSelectionne"').index + 1
            # line_colors_map.insert(index, deckcreator_slotselectionne_m81)
            
            # Add confirmbutton/border m81
            confirmbutton_border_m81 = (
                f'("ConfirmButton/Border_M81",                                    MAP ['
                f'                                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_MonochromeCRT ) ),'
                f'                                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = [36,110,36,255] ) ),'
                f'                                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [43,121,43,255] ) ),'
                f'                                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = [50,135,50,255] ) ),'
                f'                                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = [43,121,43,255] ) ),'
                f'                                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = [43,121,43,255] ) ),'
                f'                                                    ])'
            )
            index = line_colors_map.by_k('"ConfirmButton/Border"').index + 1
            line_colors_map.insert(index, confirmbutton_border_m81)

            # Add TimePanel button borders
            timepanel_buttonborder_m81pause = (
                f'("TimePanel/ButtonBorder_M81Pause",                          MAP [ '
                f'                                                          ( ~/ComponentState/Normal, TColorRTTI( Color = [255,66,33,191] ) ),'
                f'                                                          ( ~/ComponentState/Toggled, TColorRTTI( Color = [255,66,33,255] ) ),'
                f'                                                        ])'
            )
            timepanel_buttonborder_m81slow = (
                f'("TimePanel/ButtonBorder_M81Slow",                          MAP [ '
                f'                                                          ( ~/ComponentState/Normal, TColorRTTI( Color = [255,176,0,191] ) ),'
                f'                                                          ( ~/ComponentState/Toggled, TColorRTTI( Color = [255,176,0,255] ) ),'
                f'                                                        ])'
            )
            timepanel_buttonborder_m81play = (
                f'("TimePanel/ButtonBorder_M81Play",                          MAP [ '
                f'                                                          ( ~/ComponentState/Normal, TColorRTTI( Color = [102,255,102,191] ) ),'
                f'                                                          ( ~/ComponentState/Toggled, TColorRTTI( Color = [102,255,102,255] ) ),'
                f'                                                        ])'
            )
            timepanel_buttonborder_m81fast = (
                f'("TimePanel/ButtonBorder_M81Fast",                          MAP [ '
                f'                                                          ( ~/ComponentState/Normal, TColorRTTI( Color = [255,204,0,191] ) ),'
                f'                                                          ( ~/ComponentState/Toggled, TColorRTTI( Color = [255,204,0,255] ) ),'
                f'                                                        ])'
            )
            index = line_colors_map.by_k('"TimePanel/ButtonBorder"').index + 1
            line_colors_map.insert(index, timepanel_buttonborder_m81fast)
            line_colors_map.insert(index, timepanel_buttonborder_m81play)
            line_colors_map.insert(index, timepanel_buttonborder_m81slow)
            line_colors_map.insert(index, timepanel_buttonborder_m81pause)

            # Add chat button color style (line)
            button_chatcolorstyle_all_m81 = (
                f'("ChatBUTTONColorStyle_All_M81",          MAP ['
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
            line_colors_map.insert(index, button_chatcolorstyle_all_m81)

            # Add chat panel color style (line)
            panel_chatcolorstyle_all_m81 = (
                f'("ChatPANELColorStyle_All_M81",          MAP ['
                f'                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoalSelection ) ),'
                f'                                   ])'
            )
            index = line_colors_map.by_k('"TacticPanel"').index + 1
            line_colors_map.insert(index, panel_chatcolorstyle_all_m81)
            
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
            
            # Add playerhelper/texte/Otan_element m81
            # TODO: find out why this was used in old version of WARNO (doesn't seem to be used anymore)
            # playerhelper_texte_otan_element_m81 = (
            #     f'("playerHelper/texte/Otan_element_M81",                      MAP ['
            #     f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
            #     f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = [255,255,255,255] ) ),'
            #     f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc7 ) ),'
            #     f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = Blanc7 ) ),'
            #     f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = Otan_fond ) ),'
            #     f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = 255,255,255,255 ) ),'
            #     f'                                        ])'
            # )
            # index = text_colors_map.by_k('"playerHelper/texte/Otan_element"').index + 1
            # text_colors_map.insert(index, playerhelper_texte_otan_element_m81)

            # Add WeaponButton/Overblock m81
            weaponbuttonoverblock_m81 = (
                f'("WeaponButton/Overblock_M81",      MAP ['
                f'                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = DarkerGray30 ) ),'
                f'                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_EbonyDark ) ),'
                f'                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_Ebony ) ),'
                f'                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = [30,30,30,120] ) ),'
                f'                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color =  [30,30,30,90] ) ),'
                f'                        ])'
            )
            index = text_colors_map.by_k('"WeaponButton/Overblock"').index + 1
            text_colors_map.insert(index, weaponbuttonoverblock_m81)

            # Add BoutonTemps text m81
            boutontemps_text_m81 = (
                f'("BoutonTemps_Text_M81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = Blanc184 ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"BoutonTemps_Text"').index + 1
            text_colors_map.insert(index, boutontemps_text_m81)

            # Add WeaponIcon text M81
            weaponicon_text_m81 = ('"WeaponIcon_Text_M81"', 'MAP [( ~/ComponentState/Normal, TColorRTTI( Color = [199+20,184+20,148+20,255] ) ),]')
            index = text_colors_map.by_k('"MarronPanel_blanc"').index + 1
            text_colors_map.insert(index, weaponicon_text_m81)

            # Add SM Feldgrau WACTUAL
            # TODO: confirm this is not needed
            # sm_feldgrauwactual = (
            #     f'("SM_FeldgrauWACTUAL",                         MAP ['
            #     f'                                        ( ~/ComponentState/Normal,                 TColorRTTI( Color = Feldgrau ) ),'
            #     f'                                        ( ~/ComponentState/Highlighted,            TColorRTTI( Color = [93,116,88,255] ) ),'
            #     f'                                        ( ~/ComponentState/Toggled,                TColorRTTI( Color = [101,128,96,255] ) ),'
            #     f'                                    ])'
            # )
            # index = text_colors_map.by_k('"SM_Feldgrau"').index + 1
            # text_colors_map.insert(index, sm_feldgrauwactual)

            # Add chat button color style (text)
            chatbuttoncolorstyle_all_m81 = (
                f'("ChatBUTTONColorStyle_All_M81",              MAP ['
                f'                                        ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = Blanc184 ) ),'
                f'                                        ( ~/ComponentState/Highlighted,           TColorRTTI( Color = Blanc7 ) ),'
                f'                                        ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancPur ) ),'
                f'                                        ( ~/ComponentState/Toggled,               TColorRTTI( Color = BlancEquipe ) ),'
                f'                                        ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = BlancEquipe ) ),'
                f'                                    ])'
            )
            index = text_colors_map.by_k('"TacticButton_highlightable"').index + 1
            text_colors_map.insert(index, chatbuttoncolorstyle_all_m81)

            # Add chat panel color style (text)
            chatpanelcolorstyle_all_m81 = (
                f'("ChatPANELColorStyle_All_M81",              MAP ['
                f'                                        ( ~/ComponentState/Normal,                TColorRTTI( Color = BlancEquipe ) ),'
                f'                                   ])'
            )
            index = text_colors_map.by_k('"TacticPanel"').index + 1
            text_colors_map.insert(index, chatpanelcolorstyle_all_m81)

            # Add m81 moral colors
            moral_color_bad_1_m81 = ('"moral_color_bad_1_M81"', 'MAP [( ~/ComponentState/Normal,                 TColorRTTI( Color = [255,200,0,255] ) ),]')
            moral_color_bad_4_m81 = ('"moral_color_bad_4_M81"', 'MAP [( ~/ComponentState/Normal,                 TColorRTTI( Color = [200,0,255,255] ) ),]')
            index1 = text_colors_map.by_k('"moral_color_bad_1"').index + 1
            index2 = text_colors_map.by_k('"moral_color_bad_4"').index + 1
            text_colors_map.insert(index1, moral_color_bad_1_m81)
            text_colors_map.insert(index2, moral_color_bad_4_m81)
            
            # Add BoutonXP deck m81
            boutonxp_deck_m81 = (
                f'("BoutonXP_deck_M81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_Ebony ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_EbonyLight ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_EbonyVeryDark ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_EbonyVeryDark ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_EbonyVeryDark ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"BoutonXP_deck"').index + 1
            text_colors_map.insert(index, boutonxp_deck_m81)
            
            # Add BoutonXP deck border m81
            # Currently same as chevron
            boutonxp_deck_border_m81 = (
                f'("BoutonXP_deck_border_M81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_ArtichokeNearWhite ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = BlancPur ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"BoutonXP_deck_border"').index + 1
            text_colors_map.insert(index, boutonxp_deck_border_m81)

            # Add BoutonXP deck chevron m81
            boutonxp_deck_chevron_m81 = (
                f'("BoutonXP_deck_chevron_M81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_VeryDarkCharcoal ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_DarkCharcoal ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_ArtichokeNearWhite ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = BlancPur ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = BlancPur ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"BoutonXP_deck_chevron"').index + 1
            text_colors_map.insert(index, boutonxp_deck_chevron_m81)

            # Add TransportedText M81
            transportedtext_m81 = (
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
            text_colors_map.insert(index, transportedtext_m81)
            
            # Add new type colors
            new_lines = [
                ('"M81_TypeG"',              'MAP [ ( ~/ComponentState/Normal, TColorRTTI( Color = [36,110,36,255] ) ), ]'), # ForestGreen
            ]
            index = text_colors_map.by_k('"TypeA"').index
            for line in reversed(new_lines):
                text_colors_map.insert(index, line)

            # Update CouleurTexture boutonShortcuts colors
            # _edit_componentstate(text_colors_map, '"CouleurTexture_boutonShortcuts"', 'Clicked', 'M81_AppleIIc')
            # _edit_componentstate(text_colors_map, '"CouleurTexture_boutonShortcuts"', 'Toggled', 'M81_AppleIIc')
            # _edit_componentstate(text_colors_map, '"CouleurTexture_boutonShortcuts"', 'ToggleHighlighted', 'M81_AppleIIc')
            # _edit_componentstate(text_colors_map, '"CouleurTexture_boutonShortcuts"', 'ToggleClicked', 'M81_AppleIIc')

            # Remove and add CouleurBordure boutonShortcuts
            # TODO: confirmed this removal was unnecessary
            # text_colors_map.remove_by_key('"CouleurBordure_boutonShortcuts"')
            
            # Add CouleurTexture boutonShortcuts text
            couleurtexture_boutonshortcuts_m81 = (
                f'("CouleurTexture_boutonShortcuts_M81", MAP ['
                f'                    ( ~/ComponentState/Grayed,            TColorRTTI( Color = [255,255,255,80] ) ),'
                f'                    ( ~/ComponentState/Normal,            TColorRTTI( Color = M81_ArtichokeNearWhite ) ),'
                f'                    ( ~/ComponentState/Highlighted,       TColorRTTI( Color = Blanc2 ) ),'
                f'                    ( ~/ComponentState/Clicked,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/Toggled,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleHighlighted, TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleClicked,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                ])'
            )
            index = text_colors_map.by_k('"CouleurTexture_boutonShortcuts"').index + 1
            text_colors_map.insert(index, couleurtexture_boutonshortcuts_m81)
            
            # Add CouleurBordure boutonShortcuts m81
            couleurbordure_boutonshortcuts_m81 = (
                f'("CouleurBordure_boutonShortcuts_M81", MAP ['
                f'                    ( ~/ComponentState/Normal,            TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                    ( ~/ComponentState/Clicked,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/Toggled,           TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleHighlighted, TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                    ( ~/ComponentState/ToggleClicked,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                ])'
            )
            index = text_colors_map.by_k('"CouleurBordure_boutonShortcuts"').index + 1
            text_colors_map.insert(index, couleurbordure_boutonshortcuts_m81)

            # Add CouleurBordure boutonShortcuts m81
            # couleurbordure_boutonshortcuts_m81 = (
            #     f'("CouleurBordure_boutonShortcuts_M81", MAP ['
            #     f'                    ( ~/ComponentState/Normal,            TColorRTTI( Color = [140,140,140,170] ) ),'
            #     f'                    ( ~/ComponentState/Clicked,           TColorRTTI( Color = M81_AppleIIc ) ),'
            #     f'                    ( ~/ComponentState/Toggled,           TColorRTTI( Color = M81_AppleIIc ) ),'
            #     f'                    ( ~/ComponentState/ToggleHighlighted, TColorRTTI( Color = M81_AppleIIc ) ),'
            #     f'                    ( ~/ComponentState/ToggleClicked,     TColorRTTI( Color = M81_AppleIIc ) ),'
            #     f'                ])'
            # )
            # index = text_colors_map.by_k('"CouleurBordure_boutonShortcuts"').index + 1
            # text_colors_map.insert(index, couleurbordure_boutonshortcuts_m81)

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
            
            # Add ButtonHUD Text2 m81
            buttonhudtext2_m81 = (
                f'("ButtonHUD/Text2_M81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"ButtonHUD/Text2"').index + 1
            text_colors_map.insert(index, buttonhudtext2_m81)
            
            # Add ButtonHUD Text2 airwing
            buttonhudtext2_airwing_m81 = (
                f'("ButtonHUD/Text2_Airwing_M81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"ButtonHUD/Text2_M81"').index + 1
            text_colors_map.insert(index, buttonhudtext2_airwing_m81)

            # Add ButtonHUD Text2 toggle
            buttonhudtext2_toggle_m81 = (
                f'("ButtonHUD/Text2_toggle_M81",                              MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [120,120,120,128] ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"ButtonHUD/Text2_Airwing_M81"').index + 1
            text_colors_map.insert(index, buttonhudtext2_toggle_m81)

            # Add ButtonHUD Text2 M81 cube action
            buttonhudtext2_cubeaction_m81 = (
                f'("ButtonHUD/Text2_CubeAction_M81",                       MAP ['
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = BlancEquipe ) ),'
                f'                                            ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_AppleII ) ),'
                f'                                            ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"ButtonHUD/Text2_toggle_M81"').index + 1
            text_colors_map.insert(index, buttonhudtext2_cubeaction_m81)
            
            # Add UnitAmountButton M81
            unitamountbutton_m81 = (
                f'("UnitAmountButton_M81",                              MAP ['
                f'                                            ( ~/ComponentState/Normal,                TColorRTTI( Color = [0, 0, 0, 255] ) ),'
                f'                                            ( ~/ComponentState/Highlighted,           TColorRTTI( Color = [180, 180, 180, 255] ) ),'
                f'                                            ( ~/ComponentState/Grayed,                TColorRTTI( Color = [80, 80, 80, 255] ) ),'
                f'                                        ])'
            )
            index = text_colors_map.by_k('"Noir_Grise"').index + 1
            text_colors_map.insert(index, unitamountbutton_m81)

            # Add DeploymentPhase CancelTimer M81
            deploymentphase_canceltimerm81 = (
                f'("DeploymentPhase/CancelTimer_M81",              MAP [ ( ~/ComponentState/Normal,      TColorRTTI( Color = M81_DarkCharcoal) ),'
                f'                                              ( ~/ComponentState/Highlighted, TColorRTTI( Color = BlancPur) ),'
                f'                                              ( ~/ComponentState/Clicked,     TColorRTTI( Color = BlancPur) ),'
                f'                                            ])'
            )
            index = text_colors_map.by_k('"DeploymentPhase/CancelTimer"').index + 1
            text_colors_map.insert(index, deploymentphase_canceltimerm81)

            # Add DeploymentPhase IdleUnit M81
            deploymentphase_idleunit_m81 = (
                f'("DeploymentPhase/IdleUnit_M81",                 MAP ['
                f'                                              ( ~/ComponentState/Grayed,                TColorRTTI( Color = M81_AppleIIc ) ),'
                f'                                              ( ~/ComponentState/Normal,                TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                              ( ~/ComponentState/Clicked,               TColorRTTI( Color = M81_P3AmberOrange ) ),'
                f'                                              ( ~/ComponentState/Toggled,               TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                              ( ~/ComponentState/ToggleHighlighted,     TColorRTTI( Color = M81_RedPhosphor ) ),'
                f'                                          ])'
            )
            index = text_colors_map.by_k('"DeploymentPhase/CancelTimer_M81"').index + 1
            text_colors_map.insert(index, deploymentphase_idleunit_m81)
# fmt: on
