"""MP_DDR depiction edits.

Mixed-model strength-5 squad: 4 MP_DDR + 1 KdA_DDR (RPG-2 gunner).

WeaponDescriptor target (set in RDA_unit_edits.py):
    T0=PM_Skorpion(x4), T1=RocketInf_RPG2(x1 animate=True)

Mesh layout (KdA donor at the back so the engine pins the RPG-2 onto the
single KdA model and leaves the four MP_DDR models holding Skorpions):
    [MP_DDR, MP_DDR_02, MP_DDR, MP_DDR_02, KdA_DDR_03].
"""

from typing import Dict, Tuple, Union

# fmt: off
mp_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MP_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_MP_DDR", None): {
            # Vanilla: [0]=Skorpion/WA_1, [1]=Meshless(Skorpion ref)
            # Target:  [0]=Skorpion/WA_1, [1]=RPG2/WA_2, [2]=Meshless(RPG2 ref)
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "RPG2")]),
            2: ("edit", [("ReferenceMeshForSkeleton", "RPG2")]),
        },

        ("AllWeaponSubDepiction_MP_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                # Vanilla: [0]=PM_Skorpion/_0_1
                # Target:  [0]=PM_Skorpion/_0_1, [1]=RocketInf_RPG2/_0_2
                1: ("insert", [("FireEffectTag", "RocketInf_RPG2"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
            },
        },

        ("TacticDepiction_MP_DDR_Alternatives", None): (
            "[\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"01\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"02\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"03\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"04\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"05\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_KdA_DDR_03\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_Low]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR_LOW\n"
            "    ),\n"
            "    TMeshlessDepictionDescriptor\n"
            "    (\n"
            "        SelectorId = [\"none\"]\n"
            "        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_MP_DDR\n"
            "    )\n"
            "]"
        ),

        ("TacticDepiction_MP_DDR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "05_05",
            "Operators": {
                # Vanilla ConditionalTags: [(smg, WA_1)]
                # Target:                 [(smg, WA_1), (bazooka, WA_2)]
                1: ("insert", [("bazooka", "WeaponAlternative_2")]),
            },
        },

        ("TacticDepiction_MP_DDR_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "05_05",
        },

        (None, "TTransportedInfantryEntry"): {
            "Count": 5,
            "Meshes": [
                "MP_DDR",
                "MP_DDR_02",
                "MP_DDR",
                "MP_DDR_02",
                "KdA_DDR_03",
            ],
            "UniqueCount": 5,
        },
    },
}
# fmt: on
