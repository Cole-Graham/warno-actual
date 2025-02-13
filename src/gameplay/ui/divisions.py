"""Functions for modifying division UI elements."""

from src.constants.ui.divisions import GRAY_EMBLEMS, DIVISION_EMBLEMS
from src.utils.logging_utils import setup_logger

from src import ModConfig

logger = setup_logger(__name__)

# RDA_Rugen_Gruppierung doesn't have _multi suffix for some dumb ass reason
divs_not_released = [
    "BEL_16e_Mecanisee_multi",
    "FR_11e_Para_multi",
    "FR_152e_Infanterie_multi",
    "FR_5e_Blindee_multi",
    "NATO_Garnison_Berlin_multi",
    "NL_4e_Divisie_multi",
    # "POL_20_Pancerna_multi",
    "POL_4_Zmechanizowana_multi",
    "POL_Korpus_Desantowy_multi",
    "RDA_4_MSD_multi",
    # "RDA_7_Panzer_multi",
    "RDA_9_Panzer_multi",
    "RDA_KdA_Bezirk_Erfurt_multi",
    "RDA_Rugen_Gruppierung",
    "RFA_2_PzGrenadier_multi",
    "RFA_5_Panzer_multi",
    "RFA_TerrKdo_Sud_multi",
    # "SOV_119IndTkBrig_multi",
    "SOV_25_Tank_multi",
    # "SOV_27_Gds_Rifle_multi",
    "SOV_35_AirAslt_Brig_multi",
    "SOV_39_Gds_Rifle_multi",
    "SOV_56_AirAslt_Brig_multi",
    "SOV_6IndMSBrig_multi",
    # "SOV_76_VDV_multi",
    "SOV_79_Gds_Tank_multi",
    "UK_1st_Armoured_multi",
    # "UK_2nd_Infantry_multi",
    "UK_4th_Armoured_multi",
    "UK_5th_Airborne_Brigade_multi",
    "US_101st_Airmobile_multi",
    "US_11ACR_multi",
    "US_24th_Inf_multi",
    "US_35th_Inf_multi",
    # "US_3rd_Arm_multi",
    # "US_82nd_Airborne_multi",
    # "US_8th_Inf_multi",
    "US_9th_Mot_multi",
    "WP_Unternehmen_Zentrum_multi",
    # "UK_BAOR_multi",
]

def hide_divisions_divisions_ndf(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/Divisions.ndf
    Hide divisions from the UI by setting InterfaceOrder to -1 in Divisions.ndf."""
    logger.info("Modifying InterfaceOrder for hidden divisions in Divisions.ndf ")

    config = ModConfig.get_instance()

    divs_to_hide = divs_not_released if not config.config_data['build_config']['write_dev'] \
        else config.config_data['hide_divs']

    indices_to_remove = []
    for division in divs_to_hide:
        div_index = source_path.by_n(f"Descriptor_Deck_Division_{division}").index
        indices_to_remove.append(div_index)

    for index in sorted(indices_to_remove, reverse=True):
        source_path.remove(index)

def hide_divisions_decks_ndf(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/Decks.ndf
    Remove decks for hidden divisions in Decks.ndf."""
    logger.info("Removing decks for hidden divisions in Decks.ndf")

    config = ModConfig.get_instance()

    divs_to_hide = divs_not_released if not config.config_data['build_config']['write_dev'] \
        else config.config_data['hide_divs']

    indices_to_remove = []
    for division in divs_to_hide:
        deck_index = source_path.by_n(f"Descriptor_Deck_{division}").index
        indices_to_remove.append(deck_index)

    for index in sorted(indices_to_remove, reverse=True):
        source_path.remove(index)
        
def hide_divisions_deckserializer_ndf(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/DecksSerializer.ndf
    Remove division map rows in DecksSerializer.ndf for hidden divisions."""
    logger.info("Removing division map rows for hidden divisions in DecksSerializer.ndf")

    config = ModConfig.get_instance()

    divs_to_hide = divs_not_released if not config.config_data['build_config']['write_dev'] \
        else config.config_data['hide_divs']
    
    vanilla_serializer = source_path.find_by_cond(lambda serializer_obj: serializer_obj.index == 0)
    division_ids_map = vanilla_serializer.v.by_member("DivisionIds")
    for division in divs_to_hide:
        division_ids_map.v.remove_by_key(f"Descriptor_Deck_Division_{division}")

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
