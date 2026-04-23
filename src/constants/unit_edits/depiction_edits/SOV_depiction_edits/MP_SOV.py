"""MP_SOV depiction edits.

Mixed-model strength-8 squad: 5 MP_SOV + 3 Reserve_SOV models.

WeaponDescriptor target (set in SOV_unit_edits.py):
    T0=FM_AK_74(x5), T1=SAW_RPK_74_5_56mm(x2 animate=True),
    T2=RocketInf_RPG7(x1 animate=True)

Mesh layout (5 MP_SOV up front so AK74 stays on MP models, RPK + RPG7
go onto the Reserve donor models):
    [MP_SOV, MP_SOV, MP_SOV, MP_SOV, MP_SOV,
     Reserve_SOV, Reserve_SOV_02, Reserve_SOV_03].

MP_SOV has only one unique high-LOD mesh, so the front five entries all reuse it.
"""

from typing import Dict, Tuple, Union

# fmt: off
mp_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MP_SOV",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_MP_SOV", None): {
            # Vanilla: [0]=AK74/WA_1, [1]=Meshless(AK74 ref)
            # Target:  [0]=AK74/WA_1, [1]=RPK74/WA_2, [2]=RPG7V/WA_3, [3]=Meshless(RPG7V ref)
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "RPK74")]),
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "RPG7V")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "RPG7V")]),
        },

        ("AllWeaponSubDepiction_MP_SOV", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                # Vanilla: [0]=FM_AK_74/_0_1
                # Target:  [0]=FM_AK_74/_0_1, [1]=SAW_RPK_74_5_56mm/_0_2,
                #          [2]=RocketInf_RPG7/_0_3
                1: ("insert", [("FireEffectTag", "SAW_RPK_74_5_56mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("insert", [("FireEffectTag", "RocketInf_RPG7"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },

        ("TacticDepiction_MP_SOV_Alternatives", None): (
            "[\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"01\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_SOV\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"02\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_SOV\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"03\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_SOV\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"04\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_SOV\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"05\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_SOV\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"06\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Reserve_SOV\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"07\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Reserve_SOV_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"08\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Reserve_SOV_03\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_Low]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_SOV_LOW\n"
            "    ),\n"
            "    TMeshlessDepictionDescriptor\n"
            "    (\n"
            "        SelectorId = [\"none\"]\n"
            "        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_MP_SOV\n"
            "    )\n"
            "]"
        ),

        ("TacticDepiction_MP_SOV_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "08_08",
            "Operators": {
                # Vanilla ConditionalTags: [] (no entries)
                # Target:                 [(mmg, WA_2), (bazooka, WA_3)]
                0: ("insert", [("mmg", "WeaponAlternative_2")]),
                1: ("insert", [("bazooka", "WeaponAlternative_3")]),
            },
        },

        ("TacticDepiction_MP_SOV_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "08_08",
        },

        (None, "TTransportedInfantryEntry"): {
            "Count": 8,
            "Meshes": [
                "MP_SOV",
                "MP_SOV",
                "MP_SOV",
                "MP_SOV",
                "MP_SOV",
                "Reserve_SOV",
                "Reserve_SOV_02",
                "Reserve_SOV_03",
            ],
            "UniqueCount": 8,
        },
    },
}
# fmt: on
