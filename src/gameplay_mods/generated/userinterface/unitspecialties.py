"""Functions for modifying UnitSpecialties.ndf"""

from typing import List, Tuple

from src.dics.ui.traits import NEW_TRAITS, TRAIT_EDITS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_ui_unitspecialties(source_path) -> None:
    """GameData/Generated/UserInterface/UnitSpecialties.ndf"""
    logger.info("Modifying unit specialties")

    # Add new traits
    trait_map = source_path.by_n("UnitSpecialties").v.by_m("Descriptors").v
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
                f"))"
            )
        else:
            obj_entry = (
                f'("{trait}", TUnitSpecialtyDescriptor('
                f'    SpecialtyTextureName = "Texture_Speciality_Icon_{trait}"'
                f'    SpecialtyHintTitleToken = "{data["title"][0]}"'
                f'    SpecialtyHintBodyToken = "{data["description"][0]}"'
                f"))"
            )

        trait_map.add(obj_entry)
        logger.info(f"Added trait: {trait}")

    # Update existing specialties
    for trait, data in TRAIT_EDITS.items():
        if data["extended"]["token"]:
            trait_map.by_k(f'"{trait}"').v.by_m("SpecialtyHintExtendedToken").v = f'"{data["extended"]["token"]}"'
            logger.info(f"Updated extended token for {trait}")

    _write_trait_texts()


def _write_trait_texts() -> None:
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
        
        extended = data.get("extended", None)
        if extended is not None:
            extended_token, extended_text = extended
            if extended_token and extended_text:
                entries.append((extended_token, extended_text))

    # Add specialty entries
    for trait, data in TRAIT_EDITS.items():
        extended_token = data["extended"]["token"]
        extended_text = data["extended"]["text"]
        if extended_token:
            entries.append((extended_token, extended_text))

    write_dictionary_entries(entries, dictionary_type="units")
