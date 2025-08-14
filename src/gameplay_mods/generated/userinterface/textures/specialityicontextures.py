"""Functions for modifying SpecialityIconTextures.ndf"""

from src.dics.ui.traits import NEW_TRAITS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_ui_specialityicontextures(source_path) -> None:
    """GameData/Generated/UserInterface/Textures/SpecialityIconTextures.ndf"""
    logger.info("Adding new trait textures")

    for trait, data in NEW_TRAITS.items():
        texture = data["texture"]
        texture_dir = data.get("texture_dir", "/Assets/2D/Interface/Common/UnitsIcons/Specialties")

        obj_entry = (
            f"Texture_Speciality_Icon_{trait} is TUIResourceTexture_Common"
            f"("
            f'    FileName = "GameData:{texture_dir}/{texture}"'
            f")"
        )
        map_entry = (
            f'("Texture_Speciality_Icon_{trait}", MAP ['
            f"(~/ComponentState/Normal, "
            f"~/Texture_Speciality_Icon_{trait})]),"
        )

        # Find insertion point and add entries
        for i, row in enumerate(source_path):
            if row.namespace.startswith("Texture_"):
                continue

            append_index = i
            textures_map_obj = source_path.by_n("UnitSpecialityAdditionalTextureBank").v
            textures_map = textures_map_obj.by_member("Textures").v
            textures_map.add(map_entry)
            source_path.insert(append_index, obj_entry)
            logger.info(f"Added {trait} texture")
            break
