"""Jager_PzF3_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
jager_pzf3_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Jager_PzF3_RFA",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Jager_PzF3_RFA", None): ( # (namespace, object type)
            # # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            # 2: ("edit", [("MeshDescriptor", "RPG7V")]), # (selector_id or mesh)
            # 3: ("edit", [("ReferenceMeshForSkeleton", "RPG7V")]),
            '[\n'
            '    TDepictionVisual\n'
            '    (\n'
            '        SelectorId = ["WeaponAlternative_1"]\n'
            '        MeshDescriptor = $/GFX/DepictionResources/Modele_G3A4\n'
            '    ),\n'
            '    TDepictionVisual\n'
            '    (\n'
            '        SelectorId = ["WeaponAlternative_2"]\n'
            '        MeshDescriptor = $/GFX/DepictionResources/Modele_MG3\n'
            '    ),\n'
            '    TDepictionVisual\n'
            '    (\n'
            '        SelectorId = ["WeaponAlternative_3"]\n'
            '        MeshDescriptor = $/GFX/DepictionResources/Modele_Panzerfaust_3\n'
            '    ),\n'
            '    TMeshlessDepictionDescriptor\n'
            '    (\n'
            '        SelectorId = ["none"]\n'
            '        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_Panzerfaust_3\n'
            '    )\n'
            ']'
        ),
    },
}
# fmt: on
