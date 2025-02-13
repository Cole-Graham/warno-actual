"""Functions for modifying division UI elements."""

from src.constants.ui.divisions import GRAY_EMBLEMS, DIVISION_EMBLEMS
from src.utils.logging_utils import setup_logger

from src import ModConfig

logger = setup_logger(__name__)


def hide_divisions(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/Divisions.ndf
    Hide divisions from the UI by setting InterfaceOrder to -1 in Divisions.ndf."""
    logger.info("Modifying InterfaceOrder for hidden divisions in Divisions.ndf ")

    divs_not_released = [
        "BEL_16e_Mecanisee",
        "FR_11e_Para",
        "FR_152e_Infanterie",
        "FR_5e_Blindee",
        "NATO_Garnison_Berlin",
        "NL_4e_Divisie",
        # "POL_20_Pancerna",
        "POL_4_Zmechanizowana",
        "POL_Korpus_Desantowy",
        "RDA_4_MSD",
        # "RDA_7_Panzer",
        "RDA_9_Panzer",
        "RDA_KdA_Bezirk_Erfurt",
        "RDA_Rugen_Gruppierung",
        "RFA_2_PzGrenadier",
        "RFA_5_Panzer",
        "RFA_TerrKdo_Sud",
        # "SOV_119IndTkBrig",
        "SOV_25_Tank",
        # "SOV_27_Gds_Rifle",
        "SOV_35_AirAslt_Brig",
        "SOV_39_Gds_Rifle",
        "SOV_56_AirAslt_Brig",
        "SOV_6IndMSBrig",
        # "SOV_76_VDV",
        "SOV_79_Gds_Tank",
        "UK_1st_Armoured",
        # "UK_2nd_Infantry",
        "UK_4th_Armoured",
        "UK_5th_Airborne_Brigade",
        "US_101st_Airmobile",
        "US_11ACR",
        "US_24th_Inf",
        "US_35th_Inf",
        # "US_3rd_Arm",
        # "US_82nd_Airborne",
        # "US_8th_Inf",
        "US_9th_Mot",
        "WP_Unternehmen_Zentrum",
        # "UK_BAOR",
    ]

    config = ModConfig.get_instance()

    divs_to_hide = divs_not_released if not config.config_data['build_config']['write_dev'] \
        else config.config_data['hide_divs']

    for division in divs_to_hide:
        div = source_path.by_n(f"Descriptor_Deck_Division_{division}")
        div.v.by_m("InterfaceOrder").v = "999.0"


def edit_division_emblems(source_path) -> None:
    """Edit division emblems in DivisionTextures.ndf."""
    logger.info("Modifying/Adding division emblem textures in DivisionTextures.ndf")
    
    for division in GRAY_EMBLEMS:
        namespace_prefix = "Texture_Division_Emblem_"
        texture_obj = source_path.by_n(namespace_prefix + division).v
        filename = f'"GameData:/Assets/2D/Interface/UseOutGame/Division/Emblem/{division}_gray.png"'
        texture_obj.by_m("FileName").v = filename
        logger.info(f"Changed {division} texture to {filename.split('/')[-1]}")
        
    for emblem_namespace, data in DIVISION_EMBLEMS.items():
        _dir = data["texture_dir"]
        texture = data["texture"]
        namespace_prefix = "Texture_Division_Emblem_"
        new_entry = (
            f'{namespace_prefix}{emblem_namespace} is TUIResourceTexture_Common'
            '('
            f'  FileName = "GameData:{_dir}/{texture}"'
            ')'
        )
        
        texturebank_obj = source_path.by_n("DivisionAdditionalTextureBank")
        texturebank_index = texturebank_obj.index
        source_path.insert(texturebank_index, new_entry)
        
        textures_map = texturebank_obj.v.by_m("Textures")
        new_entry = (
            '('
            f'"{namespace_prefix}{emblem_namespace}",'
            f'MAP[(~/ComponentState/Normal, ~/{namespace_prefix}{emblem_namespace})]'
            ')'
        )
        textures_map.v.add(new_entry)
        logger.info(f"Added new texture: {namespace_prefix}{emblem_namespace}")
