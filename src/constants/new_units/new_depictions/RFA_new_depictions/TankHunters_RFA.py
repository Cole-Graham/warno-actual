"""TankHunters_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off

tankhunters_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "TankHunters_RFA",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_TankHunters_RFA", None): ( # (namespace, object type)
            # # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove", "replace")
            # 1: ("edit", [("MeshDescriptor", "Panzerfaust_3"), ("SelectorId", "WeaponAlternative_2")]),
            # 2: ("edit", [("MeshDescriptor", "Panzerfaust_3"), ("SelectorId", "WeaponAlternative_3")]),
            # 3: ("edit", [("ReferenceMeshForSkeleton", "Panzerfaust_3")]),
            f'['
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_1"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_G3A4\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_2"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Panzerfaust_3\n'
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

        ("TacticDepiction_TankHunters_RFA_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                1: ("insert", [("bazooka", "WeaponAlternative_3")]),
                0: ("edit", [("bazooka", "WeaponAlternative_2")]),
            },
            "Selector": "02_03", # {unique_count}_{count}
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