"""In-game UI icon constants for UseInGameTextures.ndf edits.

- **INGAME_ICONS**: new ``AdditionalTextureBank`` keys ``icone_<id>`` with inline
  ``TUIResourceTexture_Common`` (MAP-only; no top-level object unless another
  NDF file must reference it by name).
- **INGAME_ICON_EDITS**: patch **existing** vanilla ``TUIResourceTexture_Common``
  objects (e.g. cursors) by namespace; the bank MAP already references ``~/Name``
  and does not need duplicating.
"""

INGAME_ICONS = {
    "shock_move": {
        "texture_dir": "/Assets/2D/Interface/UseInGame/Icones",
        "texture": "shock_move_28x24.png",
        "insert_after": "icone_shock",  # Specifies where to insert in the list
    },
    "swift": {
        "texture_dir": "/Assets/2D/Interface/UseInGame/Icones",
        "texture": "swift.png",
        "insert_after": "icone_shock_move",  # Specifies where to insert in the list
    },
    "deploy": {
        "texture_dir": "/Assets/2D/Interface/UseInGame/Icones",
        "texture": "deploy.png",
        "insert_after": "icone_swift",  # Specifies where to insert in the list
    },
    "remote_controlled": {
        "texture_dir": "/Assets/2D/Interface/UseInGame/Icones",
        "texture": "remote_controlled.png",
        "insert_after": "icone_deploy",  # Specifies where to insert in the list
    },
}

INGAME_ICON_EDITS = {
    "Artillery": {
        "prefix": "Texture_Tactical_Cursor_",
        "new_texture_dir": "/Assets/2D/Interface/Common/TacticalCursors/",
        "new_texture": "artillery_wa.png",
    },
}
