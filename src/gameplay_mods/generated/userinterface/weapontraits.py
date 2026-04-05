"""Modify weapon traits in WeaponTraits.ndf."""

from typing import List, Tuple

from src.constants.weapons import NEW_WEAPON_TRAITS, SHOW_AS_FILTER, WEAPON_TRAIT_EDITS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes

logger = setup_logger(__name__)


def edit_gen_ui_weapontraits(source_path) -> None:
    """GameData/Generated/UserInterface/WeaponTraits.ndf"""
    logger.info("Editing weapon traits")

    dic_entries: List[Tuple[str, str]] = []

    descriptors_map = source_path.by_n("WeaponTraits").v.by_m("Descriptors").v

    for trait_key, show_filter in SHOW_AS_FILTER.items():
        if trait_key in NEW_WEAPON_TRAITS:
            continue
        descriptor = descriptors_map.by_k(f'"{trait_key}"', False)
        if descriptor:
            descriptor.v.by_m("ShowAsFilterInShowroom").v = str(show_filter)
            logger.info(
                "Set ShowAsFilterInShowroom = %s for existing trait %s",
                show_filter,
                trait_key,
            )
        else:
            logger.warning(
                "Trait descriptor %s not found (SHOW_AS_FILTER patch skipped)",
                trait_key,
            )

    for trait_key, data in NEW_WEAPON_TRAITS.items():
        title_token = data["trait_hint_title_token"]
        body_token = data["trait_hint_body_token"]
        texture_name = data["trait_texture_name"]
        show_filter = SHOW_AS_FILTER[trait_key]
        entry = (
            f'        (\n'
            f'            "{trait_key}",\n'
            f'            TWeaponTraitDescriptor\n'
            f'            (\n'
            f'                TraitTextureName = "{texture_name}"\n'
            f'                TraitHintTitleToken = "{title_token}"\n'
            f'                TraitHintBodyToken = "{body_token}"\n'
            f'                ShowAsFilterInShowroom = {show_filter}\n'
            f'            )\n'
            f'        ),'
        )
        descriptors_map.add(entry)
        dic_entries.append((title_token, data["title"]))
        dic_entries.append((body_token, data["description"]))
        logger.info("Added weapon trait descriptor %s", trait_key)

    for trait_name, description in WEAPON_TRAIT_EDITS.items():
        trait_descriptor = descriptors_map.by_k(f'"{trait_name}"', False)
        if not trait_descriptor:
            logger.warning(f"Trait descriptor {trait_name} not found")
            continue

        token = strip_quotes(trait_descriptor.v.by_m("TraitHintBodyToken").v)
        dic_entries.append((token, str(description)))

    write_dictionary_entries(dic_entries, dictionary_type="ingame")
