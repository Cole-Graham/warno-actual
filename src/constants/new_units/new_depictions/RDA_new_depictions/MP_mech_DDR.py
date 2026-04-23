"""MP_mech_DDR depiction edits.

New mechanized MP unit cloned from MP_DDR donor with Reserve_DDR donor support
weapons + meshes (5 MP_DDR + 3 Reserve_DDR mixed-model squad).

WeaponDescriptor target (set in RDA_new_units.py):
    T0=PM_Skorpion(x5), T1=FM_KMS_72(x1 animate=True),
    T2=SAW_lMG_K_7_62mm(x1 animate=True), T3=RocketInf_RPG7(x1 animate=True)

Mesh layout (5 MP_DDR up front so the engine pins Skorpions to MP models and
the support weapons / RPG-7 land on Reserve donor models at the back):
    [MP_DDR, MP_DDR_02, MP_DDR, MP_DDR_02, MP_DDR,
     Reserve_DDR, Reserve_DDR_02, Reserve_DDR_03].
"""

from typing import Dict, Tuple, Union

# fmt: off
mp_mech_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MP_mech_DDR",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_MP_mech_DDR", None): {
            # Donor (MP_DDR): [0]=Skorpion/WA_1, [1]=Meshless(Skorpion ref)
            # Target: [0]=Skorpion/WA_1, [1]=RPK/WA_2, [2]=RPG7V/WA_3 (donor),
            #         wait — we need slot 1=KMS_72 mesh (=AK74), slot 2=RPK, slot 3=RPG7V
            # Final:  [0]=Skorpion/WA_1, [1]=AK74/WA_2, [2]=RPK/WA_3, [3]=RPG7V/WA_4,
            #         [4]=Meshless(RPG7V ref)
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "AK74")]),
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "RPK")]),
            3: ("insert", [("SelectorId", "WeaponAlternative_4"), ("MeshDescriptor", "RPG7V")]),
            4: ("edit", [("ReferenceMeshForSkeleton", "RPG7V")]),
        },

        ("AllWeaponSubDepiction_MP_mech_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                # Donor (MP_DDR): [0]=PM_Skorpion/_0_1
                # Target:  [0]=PM_Skorpion/_0_1, [1]=FM_KMS_72/_0_2,
                #          [2]=SAW_lMG_K_7_62mm/_0_3, [3]=RocketInf_RPG7/_0_4
                1: ("insert", [("FireEffectTag", "FM_KMS_72"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("insert", [("FireEffectTag", "SAW_lMG_K_7_62mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
                3: ("insert", [("FireEffectTag", "RocketInf_RPG7"), ("WeaponShootDataPropertyName", "WeaponShootData_0_4")]),
            },
        },

        ("TacticDepiction_MP_mech_DDR_Alternatives", None): (
            "[\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"01\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Reserve_DDR\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"02\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Reserve_DDR_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"03\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_Reserve_DDR_03\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"04\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"05\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"06\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"07\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR_02\n"
            "    ),\n"
            "    TDepictionVisual\n"
            "    (\n"
            "        SelectorId = [LOD_High, \"08\"]\n"
            "        MeshDescriptor = $/GFX/DepictionResources/Modele_MP_DDR\n"
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

        ("TacticDepiction_MP_mech_DDR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "08_08",
            "Operators": {
                # Donor (MP_DDR) ConditionalTags: [(smg, WA_1)]
                # Target:                         [(smg, WA_1), (mmg, WA_3), (bazooka, WA_4)]
                1: ("insert", [("mmg", "WeaponAlternative_3")]),
                2: ("insert", [("bazooka", "WeaponAlternative_4")]),
            },
        },

        ("TacticDepiction_MP_mech_DDR_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "08_08",
        },

        (None, "TTransportedInfantryEntry"): {
            "Count": 8,
            "Meshes": [
                "Reserve_DDR",
                "Reserve_DDR_02",
                "Reserve_DDR_03",
                "MP_DDR",
                "MP_DDR_02",
                "MP_DDR",
                "MP_DDR_02",
                "MP_DDR",
            ],
            "UniqueCount": 8,
        },
    },
}
# fmt: on
