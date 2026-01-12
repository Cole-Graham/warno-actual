"""Modify weapon traits in WeaponTraits.ndf."""

from typing import List, Tuple

from src.constants.weapons import WEAPON_TRAIT_EDITS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes

logger = setup_logger(__name__)


def edit_gen_ui_weapontraits(source_path) -> None:
    """GameData/Generated/UserInterface/WeaponTraits.ndf"""
    logger.info("Editing weapon traits")

    dic_entries: List[Tuple[str, str]] = []

    trait_descriptors_map = source_path.by_n("WeaponTraits").v.by_m("Descriptors")
    for trait_name, description in WEAPON_TRAIT_EDITS.items():
        trait_descriptor = trait_descriptors_map.v.by_k(f'"{trait_name}"')
        if not trait_descriptor:
            logger.warning(f"Trait descriptor {trait_name} not found")
            continue
        
        token = strip_quotes(trait_descriptor.v.by_m("TraitHintBodyToken").v)
        dic_entries.append((token, str(description)))

    write_dictionary_entries(dic_entries, dictionary_type="ingame")
