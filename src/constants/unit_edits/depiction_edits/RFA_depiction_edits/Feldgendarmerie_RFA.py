"""Feldgendarmerie_RFA depiction edits.

Mixed-model strength-8 squad: 3 HeimatschutzJager_RFA + 5 Feldgendarmerie_RFA.

WeaponDescriptor target (set in RFA_unit_edits.py):
    T0=PM_MP_5A3(x5), T1=FM_G3KA4(x2),
    T2=MMG_inf__MG3_7_62mm(x1 animate=True), T3=RocketInf_PzF_44(x1 animate=True)

Mesh layout (3 Heimat up front so the engine pins the donor MG3/G3KA4/PzF
weapons onto the Heimat front models, leaving the rear Feldgen models on
PM_MP_5A3):
    [Heimat, Heimat_02, Heimat_03,
     Feldgen, Feldgen_02, Feldgen_03, Feldgen_04, Feldgen_05].
"""

from typing import Dict, Tuple, Union

# fmt: off
feldgendarmerie_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Feldgendarmerie_RFA",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Feldgendarmerie_RFA", None): {
            # Vanilla: [0]=MP5A3/WA_1, [1]=Meshless(MP5A3 ref)
            # Target:  [0]=MP5A3/WA_1, [1]=G3A4/WA_2, [2]=MG3/WA_3,
            #          [3]=Panzerfaust_44/WA_4, [4]=Meshless(Panzerfaust_44 ref)
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "G3A4")]),
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "MG3")]),
            3: ("insert", [("SelectorId", "WeaponAlternative_4"), ("MeshDescriptor", "Panzerfaust_44")]),
            4: ("edit", [("ReferenceMeshForSkeleton", "Panzerfaust_44")]),
        },

        ("AllWeaponSubDepiction_Feldgendarmerie_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                # Vanilla: [0]=PM_MP_5A3/_0_1
                # Target:  [0]=PM_MP_5A3/_0_1, [1]=FM_G3KA4/_0_2,
                #          [2]=MMG_inf__MG3_7_62mm/_0_3, [3]=RocketInf_PzF_44/_0_4
                1: ("insert", [("FireEffectTag", "FM_G3KA4"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("insert", [("FireEffectTag", "MMG_inf__MG3_7_62mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
                3: ("insert", [("FireEffectTag", "RocketInf_PzF_44"), ("WeaponShootDataPropertyName", "WeaponShootData_0_4")]),
            },
        },

        ("TacticDepiction_Feldgendarmerie_RFA_Alternatives", None): (
            "[\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"01\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_HeimatschutzJager_RFA\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"02\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_HeimatschutzJager_RFA_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"03\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_HeimatschutzJager_RFA_03\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"04\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Feldgendarmerie_RFA\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"05\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Feldgendarmerie_RFA_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"06\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Feldgendarmerie_RFA_03\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"07\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Feldgendarmerie_RFA_04\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"08\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Feldgendarmerie_RFA_05\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_Low]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Feldgendarmerie_RFA_LOW\n"
            "    ),\n"
            "    TMeshlessDepictionDescriptor\n"
            "    (\n"
            "        SelectorId = [\"none\"]\n"
            "        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_Feldgendarmerie_RFA\n"
            "    )\n"
            "]"
        ),

        ("TacticDepiction_Feldgendarmerie_RFA_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "08_08",
            "Operators": {
                # Vanilla ConditionalTags: [(smg, WA_1)]
                # Target:                 [(smg, WA_1), (mmg, WA_3), (bazooka, WA_4)]
                1: ("insert", [("mmg", "WeaponAlternative_3")]),
                2: ("insert", [("bazooka", "WeaponAlternative_4")]),
            },
        },

        ("TacticDepiction_Feldgendarmerie_RFA_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "08_08",
        },

        (None, "TTransportedInfantryEntry"): {
            "Count": 8,
            "Meshes": [
                "HeimatschutzJager_RFA",
                "HeimatschutzJager_RFA_02",
                "HeimatschutzJager_RFA_03",
                "Feldgendarmerie_RFA",
                "Feldgendarmerie_RFA_02",
                "Feldgendarmerie_RFA_03",
                "Feldgendarmerie_RFA_04",
                "Feldgendarmerie_RFA_05",
            ],
            "UniqueCount": 8,
        },
    },
}
# fmt: on
