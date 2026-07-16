"""RMP_UK depiction edits.

Mixed-model strength-8 RMP squad: 5 RMP_UK models + 3 Territorial_UK models.

WeaponDescriptor target (set in UK_unit_edits.py):
    T0=FM_L1A1_SLR(x3), T1=PM_Sterling(x3),
    T2=MMG_inf_L7A2_7_62mm(x2 animate=False), T3=RocketInf_M72A3_LAW_66mm(x1)

Mesh layout (5 RMP up front so SLR/Sterling/MMG go on RMP models, LAW on Territorial):
    [RMP, RMP_02, RMP, RMP_02, RMP, Territorial, Territorial_02, Territorial].
"""

from typing import Dict, Tuple, Union

# fmt: off
rmp_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "RMP_UK",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_RMP_UK", None): {
            # Vanilla: [0]=L2A3/WA_1 (Sterling), [1]=L1A1_SLR/WA_2 (SLR),
            #          [2]=M240B/WA_3 (MMG L7A2), [3]=Meshless(M240B)
            # Target:  [0]=L1A1_SLR/WA_1, [1]=L2A3/WA_2, [2]=M240B/WA_3,
            #          [3]=M72A4/WA_4 (LAW), [4]=Meshless(M72A4)
            3: ("insert", [("SelectorId", "WeaponAlternative_4"), ("MeshDescriptor", "M72A4")]),
            0: ("edit", [("MeshDescriptor", "L1A1_SLR")]),
            1: ("edit", [("MeshDescriptor", "L2A3")]),
            4: ("edit", [("ReferenceMeshForSkeleton", "M72A4")]),
        },

        ("AllWeaponSubDepiction_RMP_UK", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                # Vanilla: [0]=PM_Sterling/_0_1, [1]=FM_L1A1_SLR/_0_2, [2]=MMG_inf_L7A2_7_62mm/_0_3
                # Target:  [0]=FM_L1A1_SLR/_0_1, [1]=PM_Sterling/_0_2,
                #          [2]=MMG_inf_L7A2_7_62mm/_0_3, [3]=RocketInf_M72A3_LAW_66mm/_0_4
                3: ("insert", [("FireEffectTag", "RocketInf_M72_LAW_66mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_4")]),
                0: ("edit", [("FireEffectTag", "FM_L1A1_SLR")]),
                1: ("edit", [("FireEffectTag", "PM_Sterling")]),
            },
        },

        ("TacticDepiction_RMP_UK_Alternatives", None): (
            "[\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"01\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_RMP_UK\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"02\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_RMP_UK_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"03\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_RMP_UK\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"04\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_RMP_UK_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"05\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_RMP_UK\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"06\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Territorial_UK\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"07\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Territorial_UK_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"08\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Territorial_UK\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_Low]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_RMP_UK_LOW\n"
            "    ),\n"
            "    TMeshlessDepictionDescriptor\n"
            "    (\n"
            "        SelectorId = [\"none\"]\n"
            "        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_RMP_UK\n"
            "    )\n"
            "]"
        ),

        ("TacticDepiction_RMP_UK_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "08_08",
            "Operators": {
                # Vanilla ConditionalTags: [(smg, WA_1), (mmg, WA_3)]
                # Target: [(smg, WA_2), (mmg, WA_3), (bazooka, WA_4)]
                2: ("insert", [("bazooka", "WeaponAlternative_4")]),
                0: ("edit", [("smg", "WeaponAlternative_2")]),
            },
        },

        ("TacticDepiction_RMP_UK_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "08_08",
        },

        (None, "TTransportedInfantryEntry"): {
            "Count": 8,
            "Meshes": [
                "RMP_UK",
                "RMP_UK_02",
                "RMP_UK",
                "RMP_UK_02",
                "RMP_UK",
                "Territorial_UK",
                "Territorial_UK_02",
                "Territorial_UK",
            ],
            "UniqueCount": 8,
        },
    },
}
# fmt: on
