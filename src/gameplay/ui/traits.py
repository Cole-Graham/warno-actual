"""Functions for modifying unit traits and specialties."""

from typing import List, Tuple

from src import ModConfig  # noqa
from src.dics.ui.traits import NEW_TRAITS, TRAIT_EDITS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def write_trait_texts() -> None:
    """Write trait texts to UNITS.csv dictionary file."""
    # config = ModConfig.get_instance().config_data
    entries: List[Tuple[str, str]] = []
    
    # Add trait entries
    for trait, data in NEW_TRAITS.items():
        title_token, title = data["title"]
        if title_token and title:
            entries.append((title_token, title))
            
        description_token, description = data["description"]
        if description_token and description:
            entries.append((description_token, description))
            
    # Add specialty entries
    for trait, data in TRAIT_EDITS.items():
        extended_token = data["extended"]["token"]
        extended_text = data["extended"]["text"]
        if extended_token:
            entries.append((extended_token, extended_text))
    
    write_dictionary_entries(entries, dictionary_type="units")


def edit_specialty_icons(source) -> None:
    """Edit specialty icon textures in SpecialityIconTextures.ndf."""
    logger.info("Adding new trait textures")
    
    for trait, data in NEW_TRAITS.items():
        texture = data["texture"]
        texture_dir = data.get("texture_dir", "/Assets/2D/Interface/Common/UnitsIcons/Specialties")
        
        obj_entry = (
            f'Texture_Speciality_Icon_{trait} is TUIResourceTexture_Common'
            f'('
            f'    FileName = "GameData:{texture_dir}/{texture}"'
            f')'
        )
        map_entry = (
            f'("Texture_Speciality_Icon_{trait}", MAP ['
            f'(~/ComponentState/Normal, '
            f'~/Texture_Speciality_Icon_{trait})]),'
        )
        
        # Find insertion point and add entries
        for i, row in enumerate(source):
            if row.namespace.startswith("Texture_"):
                continue
                
            append_index = i
            textures_map_obj = source.by_n("UnitSpecialityAdditionalTextureBank").v
            textures_map = textures_map_obj.by_member("Textures").v
            textures_map.add(map_entry)
            source.insert(append_index, obj_entry)
            logger.info(f"Added {trait} texture")
            break


def edit_specialties(source) -> None:
    """Edit specialties in UnitSpecialties.ndf."""
    logger.info("Modifying unit specialties")
    
    # Add new traits
    trait_map = source.by_n("UnitSpecialties").v.by_m("Descriptors").v
    for trait, data in NEW_TRAITS.items():
        if data["title"][0] is None:  # Skip entries only used for textures
            continue
            
        if "extended" in data:
            obj_entry = (
                f'("{trait}", TUnitSpecialtyDescriptor('
                f'    SpecialtyTextureName = "Texture_Speciality_Icon_{trait}"'
                f'    SpecialtyHintTitleToken = "{data["title"][0]}"'
                f'    SpecialtyHintBodyToken = "{data["description"][0]}"'
                f'    SpecialtyHintExtendedToken = "{data["extended"][0]}"'
                f'))'
            )
        else:
            obj_entry = (
                f'("{trait}", TUnitSpecialtyDescriptor('
                f'    SpecialtyTextureName = "Texture_Speciality_Icon_{trait}"'
                f'    SpecialtyHintTitleToken = "{data["title"][0]}"'
                f'    SpecialtyHintBodyToken = "{data["description"][0]}"'
                f'))'
            )
            
        trait_map.add(obj_entry)
        logger.info(f"Added trait: {trait}")
    
    # Update existing specialties
    for trait, data in TRAIT_EDITS.items():
        if data["extended"]["token"]:
            trait_map.by_k(f'"{trait}"').v.by_m("SpecialtyHintExtendedToken").v = \
                f'"{data["extended"]["token"]}"'
            logger.info(f"Updated extended token for {trait}")
            
    write_trait_texts()
