"""Functions for modifying UI text scripts."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_ui_style_defaulttextformatscript(source_path) -> None:
    """GameData/UserInterface/Style/DefaultTextFormatScript.ndf"""
    logger.info("Adding gameplay text scripts to DefaultTextFormatScript.ndf")
    append_end = 0
    append_row = 0
    commands_map = source_path.by_n("DefaultTextFormatScript").v.by_m("Commands").v
    ldr_tag = 'LDR'
    ldr_entry = (
        f'(\n'
        f'    "{ldr_tag}",\n'
        f'    TTFSCommand_UISymbol\n'
        f'    (\n'
        f'        TextureToken = "Texture_Speciality_Icon_cmd_small"\n'
        f'        BBMin=[0.0, -0.75, 0]\n'
        f'        BBMax=[1.0, 0.1, 0]\n'
        f'        ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend\n'
        f'        UseTextColor = true\n'
        f'    )\n'
        f')'
    )
    ldr_star_tag = 'LDRSOV'
    ldr_star_entry = (
        f'(\n'
        f'    "{ldr_star_tag}",\n'
        f'    TTFSCommand_UISymbol\n'
        f'    (\n'
        f'        TextureToken = "Texture_Speciality_Icon_cmd_star_small"\n'
        f'        BBMin=[0.0, -0.75, 0]\n'
        f'        BBMax=[1.0, 0.1, 0]\n'
        f'        ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend\n'
        f'        UseTextColor = true\n'
        f'    )\n'
        f')'
    )
    light_equip_tag = 'LEQUIP'
    light_equip_entry = (
        f'(\n'
        f'    "{light_equip_tag}",\n'
        f'    TTFSCommand_UISymbol\n'
        f'    (\n'
        f'        TextureToken = "Texture_Speciality_Icon_infantry_equip_light"\n'
        f'        BBMin=[0.0, -0.8, 0]\n'
        f'        BBMax=[1.0, 0.2, 0]\n'
        f'        ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend\n'
        f'        UseTextColor = true\n'
        f'    )\n'
        f')'
    )
    medium_equip_tag = 'MEQUIP'
    medium_equip_entry = (
        f'(\n'
        f'    "{medium_equip_tag}",\n'
        f'    TTFSCommand_UISymbol\n'
        f'    (\n'
        f'        TextureToken = "Texture_Speciality_Icon_mequip_label"\n'
        f'        BBMin=[0.0, -0.8, 0]\n'
        f'        BBMax=[1.0, 0.2, 0]\n'
        f'        ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend\n'
        f'        UseTextColor = true\n'
        f'    )\n'
        f')'
    )
    heavy_equip_tag = 'HEQUIP'
    heavy_equip_entry = (
        f'(\n'
        f'    "{heavy_equip_tag}",\n'
        f'    TTFSCommand_UISymbol\n'
        f'    (\n'
        f'        TextureToken = "Texture_Speciality_Icon_hequip_label"\n'
        f'        BBMin=[0.0, -0.8, 0]\n'
        f'        BBMax=[1.0, 0.2, 0]\n'
        f'        ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend\n'
        f'        UseTextColor = true\n'
        f'    )\n'
        f')'
    )
    veryheavy_equip_tag = 'VHEQUIP'
    veryheavy_equip_entry = (
        f'(\n'
        f'    "{veryheavy_equip_tag}",\n'
        f'    TTFSCommand_UISymbol\n'
        f'    (\n'
        f'        TextureToken = "Texture_Speciality_Icon_infantry_equip_veryheavy"\n'
        f'        BBMin=[0.0, -0.8, 0]\n'
        f'        BBMax=[1.0, 0.2, 0]\n'
        f'        ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend\n'
        f'        UseTextColor = true\n'
        f'    )\n'
        f')'
    )
    third_arm_tag = '3RDARM'
    third_arm_entry = (
        f'(\n'
        f'    "{third_arm_tag}",\n'
        f'    TTFSCommand_UISymbol\n'
        f'    (\n'
        f'        TextureToken = "Texture_Division_Emblem_3rd_arm_small"\n'
        f'        BBMin=[0.0, -0.8, 0]\n'
        f'        BBMax=[1.0, 0.2, 0]\n'
        f'        ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend\n'
        f'    )\n'
        f')'
    )
    eighth_inf_tag = '8THINF'
    eighth_inf_entry = (
        f'(\n'
        f'    "{eighth_inf_tag}",\n'
        f'    TTFSCommand_UISymbol\n'
        f'    (\n'
        f'        TextureToken = "Texture_Division_Emblem_8th_inf_small"\n'
        f'        BBMin=[0.0, -0.8, 0]\n'
        f'        BBMax=[1.0, 0.2, 0]\n'
        f'        ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend\n'
        f'    )\n'
        f')'
    )
    # wa_logo_tag = 'WAMAP'
    # wa_logo_entry = (
    #     f'(\n'
    #     f'    "{wa_logo_tag}",\n'
    #     f'    TTFSCommand_UISymbol\n'
    #     f'    (\n'
    #     f'        TextureToken = "Texture_Speciality_Icon_wa_logo_small"\n'
    #     f'        BBMin=[0.0, -0.8, 0]\n'
    #     f'        BBMax=[1.0, 0.2, 0]\n'
    #     f'        ShaderDescriptor = $/M3D/Shader/MaterialInterface2D_Blend\n'
    #     f'    )\n'
    #     f')'
    # )
    for row_count, map_row in enumerate(commands_map, start=1):
        key = '"HOWZ"'
        if map_row.key == key:
            append_row = row_count - 1
        if map_row.key == '"defense"':
            append_end = row_count
            
    logger.info(f"Appending #{ldr_tag} entry to DefaultTextFormatScript.ndf")
    logger.info(f"Appending #{ldr_star_tag} entry to DefaultTextFormatScript.ndf")
    logger.info(f"Appending #{light_equip_tag} entry to DefaultTextFormatScript.ndf")
    logger.info(f"Appending #{medium_equip_tag} entry to DefaultTextFormatScript.ndf")
    logger.info(f"Appending #{heavy_equip_tag} entry to DefaultTextFormatScript.ndf")
    logger.info(f"Appending #{veryheavy_equip_tag} entry to DefaultTextFormatScript.ndf")
    logger.info(f"Appending #{third_arm_tag} entry to DefaultTextFormatScript.ndf")
    logger.info(f"Appending #{eighth_inf_tag} entry to DefaultTextFormatScript.ndf")
    # print(f"Appending #{wa_logo_tag} entry to DefaultTextFormatScript.ndf")
    # commands_map.insert(append_end, wa_logo_entry)
    commands_map.insert(append_end, light_equip_entry)
    commands_map.insert(append_end, medium_equip_entry)
    commands_map.insert(append_end, heavy_equip_entry)
    commands_map.insert(append_end, veryheavy_equip_entry)
    commands_map.insert(append_end, eighth_inf_entry)
    commands_map.insert(append_end, third_arm_entry)
    commands_map.insert(append_row, ldr_entry)
    commands_map.insert(append_row, ldr_star_entry)
    
    # Define new texture commands to add
    new_entries = [
        ('WAMAP', 'OutgameTexture_Mod_wa_logo_small'),
        ('RDMAP', 'OutgameTexture_Mod_rd_map_small'),
    ]
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
