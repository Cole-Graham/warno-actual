"""Modify weapon traits in WeaponTraits.ndf."""

from src.constants.weapons import WEAPON_TRAITS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_weapon_traits(source_path) -> None:
    """GameData/Generated/UserInterface/WeaponTraits.ndf"""
    logger.info("Editing weapon traits")

    dic_entries = {}

    trait_descriptors_map = source_path.by_n("WeaponTraits").v.by_m("Descriptors")
    for trait_name, edits in WEAPON_TRAITS.items():
        trait_descriptor = trait_descriptors_map.v.by_k(f'"{trait_name}"')
        if not trait_descriptor:
            logger.warning(f"Trait descriptor {trait_name} not found")
            continue

        for edit_key, edit_value in edits.items():
            if edit_key == "body_token":
                trait_descriptor.v.by_m("TraitHintBodyToken").v = '"' + edit_value + '"'
                dic_entries.update({edit_value: edits["body"]})

    write_dictionary_entries(dic_entries.items(), dictionary_type="ingame")
