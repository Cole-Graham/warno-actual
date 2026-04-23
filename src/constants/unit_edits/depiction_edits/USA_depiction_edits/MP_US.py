"""MP_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
mp_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MP_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_MP_US", None): {  # (namespace, object type)
            # row: (edit type, [(property, value), ...]); inserts run ascending by index, then edits
            # Vanilla: [0]=M16/WA_1, [1]=M60/WA_2, [2]=Meshless
            # Target:  [0]=M16A1/WA_1, [1]=M16/WA_2, [2]=M60/WA_3, [3]=M72A4/WA_4, [4]=Meshless(M72A4 ref)
            0: ("insert", [("SelectorId", "WeaponAlternative_1"), ("MeshDescriptor", "M16A1")]),
            3: ("insert", [("SelectorId", "WeaponAlternative_4"), ("MeshDescriptor", "M72A4")]),
            1: ("edit", [("SelectorId", "WeaponAlternative_2")]),
            2: ("edit", [("SelectorId", "WeaponAlternative_3")]),
            4: ("edit", [("ReferenceMeshForSkeleton", "M72A4")]),
        },

        ("AllWeaponSubDepiction_MP_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                # Vanilla: [0]=FM_M16/_0_1, [1]=MMG_M60/_0_2
                # Target:  [0]=FM_M16A1/_0_1, [1]=FM_M16/_0_2, [2]=MMG_M60/_0_3, [3]=LAW/_0_4
                0: ("insert", [("FireEffectTag", "FM_M16A1"), ("WeaponShootDataPropertyName", "WeaponShootData_0_1")]),
                3: ("insert", [("FireEffectTag", "RocketInf_M72A3_LAW_66mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_4")]),
                1: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },

        ("TacticDepiction_MP_US_Alternatives", None): (
            "[\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"01\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_US\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"02\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_US_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"03\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_US\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"04\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_US_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"05\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_US\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"06\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_NatGuard_LAW_US\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"07\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_NatGuard_LAW_US_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"08\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_NatGuard_LAW_US_03\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_Low]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_US_LOW\n"
            "    ),\n"
            "    TMeshlessDepictionDescriptor\n"
            "    (\n"
            "        SelectorId = [\"none\"]\n"
            "        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_MP_US\n"
            "    )\n"
            "]"
        ),

        ("TacticDepiction_MP_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "08_08",  # {unique_count}_{surrogates_count} — matches selector_tactic.NEW_SELECTOR_TACTIC_OBJECTS
            "Operators": {
                0: ("edit", [("mmg", "WeaponAlternative_3")]),
                1: ("insert", [("bazooka", "WeaponAlternative_4")]),
            },
        },

        ("TacticDepiction_MP_US_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "08_08",
        },

        (None, "TTransportedInfantryEntry"): {
            "Count": 8,
            "Meshes": [
                "MP_US",
                "MP_US_02",
                "MP_US",
                "MP_US_02",
                "MP_US",
                "NatGuard_LAW_US",
                "NatGuard_LAW_US_02",
                "NatGuard_LAW_US_03",
            ],
            "UniqueCount": 8,
        },
    },
}
# fmt: on
