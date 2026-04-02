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
            f'['
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_1"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_G3A4\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_2"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_MG3\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_3"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Panzerfaust_3\n'
            f'    ),\n'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_Panzerfaust_3\n'
            f'    )\n'
            f']'
        ),

        ("TacticDepiction_Jager_PzF3_RFA_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "02_03" # {unique_count}_{count}
        },
        
        (None, "TTransportedInfantryEntry"): {
            "Count": 3,
            "Meshes": [
                "Jager_RFA",
                "Jager_RFA_02",
                "Jager_RFA_03",
            ],
            "UniqueCount": 2,
        },
    },
}

# fmt: on
