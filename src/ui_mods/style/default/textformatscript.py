"""Functions for modifying UI text format scripts."""
# from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_defaulttextformatscript(source_path) -> None:
    """Edit DefaultTextFormatScript.ndf.
    
    Adds new text format commands for mod-specific textures.
    
    Args:
        source_path: NDF file containing text format script definitions
    """
    logger.info("Editing DefaultTextFormatScript.ndf")

    # Define new texture commands to add
    new_entries = [
        ('WAMAP', 'OutgameTexture_Mod_wa_logo_small'),
        ('RDMAP', 'OutgameTexture_Mod_rd_map_small'),
    ]

    # Get the commands map from the default script
    scripts_obj = source_path.by_namespace("DefaultTextFormatScript").v
    commands_map = scripts_obj.by_m("Commands").v

    # Add each new texture command
    for tag, texture_token in new_entries:
        new_entry = (
            f'("{tag}", TTFSCommand_UISymbol ('
            f'    TextureToken = "{texture_token}"'
            f'    BBMin = [0.0, -0.8, 0]'
            f'    BBMax = [1.0, 0.2, 0]'
            f'    ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend'
            f'))'
        )
        
        # Insert before "defense" entry
        index = commands_map.by_k('"defense"').index
        commands_map.insert(index, new_entry)
        logger.debug(f"Added text format command for {tag}")
