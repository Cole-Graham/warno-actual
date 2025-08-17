"""MotRifles_RPG7V_TTsko_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
motrifles_rpg7v_ttsko_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MotRifles_RPG7V_TTsko_SOV",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_MotRifles_RPG7V_TTsko_SOV", None): ( # (namespace, object type)
            # # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            # 2: ("edit", [("MeshDescriptor", "RPG7V")]), # (selector_id or mesh)
            # 3: ("edit", [("ReferenceMeshForSkeleton", "RPG7V")]),
            '[\n'
            '    TDepictionVisual\n'
            '    (\n'
            '        SelectorId = ["MeshAlternative_1"]\n'
            '        MeshDescriptor = $/GFX/DepictionResources/Modele_AK74\n'
            '    ),\n'
            '    TDepictionVisual\n'
            '    (\n'
            '        SelectorId = ["MeshAlternative_2"]\n'
            '        MeshDescriptor = $/GFX/DepictionResources/Modele_RPK74\n'
            '    ),\n'
            '    TDepictionVisual\n'
            '    (\n'
            '        SelectorId = ["MeshAlternative_3"]\n'
            '        MeshDescriptor = $/GFX/DepictionResources/Modele_RPG7V\n'
            '    ),\n'
            '    TMeshlessDepictionDescriptor\n'
            '    (\n'
            '        SelectorId = ["none"]\n'
            '        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_RPG7V\n'
            '    )\n'
            ']'
        ),
    },
}
# fmt: on
