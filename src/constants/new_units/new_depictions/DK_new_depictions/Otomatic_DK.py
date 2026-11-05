from typing import Any, Dict

# fmt: off
otomatic_dk: Dict[str, Any] = {
    "unit_name": "Otomatic_DK",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        # Donor (Leopard_1A3_DK) operators, minus the machine guns (both MG3 turrets are
        # removed in DK_new_units.py): index 10 = Turret_4_Aim (loader MG turret), 13 =
        # Leopard_1A3_DK_Weapon4 (its muzzle FX). The coax MG lived in the donor's turret-2
        # SubDepiction, which DK_new_units.py removes. Removes apply highest index first.
        # Weapon1/2 fire from fx_tourelle1_tir_01, Weapon6 (smoke) from fx_tourelle5_tir_01/02.
        # 76mm muzzle FX borrowed from existing units: the Danish M41 Walker's 76mm (AT) and
        # the 57mm Bofors (AA). Swap once there are dedicated OTO Melara 76mm effects.
        (None, "TacticVehicleDepictionRegistration"): {
            "Operators": {
                10: ("remove", None),
                13: ("remove", None),
            },
            "Actions": (
                'MAP['
                '            ( "weapon_effet_tag1", Weapon_Canon_AP_76mm_M32A1_Walker ),'
                '            ( "weapon_effet_tag2", Weapon_DCA_1_canon_Bofors_57mm ),'
                '            ( "weapon_effet_tag6", Weapon_SMOKE_Vehicle_Grenadex8 ),'
                '        ]'
                '        + DepictionAction_Stress_And_Wrecked'
                '        + DepictionAction_MovementFX_Tracked'
                '        + DepictionAction_CriticalFX_Tank'
            ),
        },
    },
    # HIGH 32.1k / MID 10.0k / LOW 4.0k tris. Source: Downloads/rfa_dk_models/.../DK/DCA/OTOMATIC/
    # OTOMATIC.fbx, prepped with /v/warno-actual-tools/prep_model_from_rd_addon.py (bones lowercased,
    # Roue_Elev_* empties dropped, non-_A alpha unlinked; its empty tourelle_04 bones are now unused
    # since the MG3s were removed). MID/LOW made from HIGH with WACE's tools/wt2warno/lod_collapse.py
    # (drop small shells, edge-collapse; same nodes in every LOD).
    "Otomatic_DK_ndf": {
        "directory": "Char",
        "ndf_code": """
            export Modele_Otomatic_DK is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/dk/otomatic_dk/Otomatic_DK.fbx"
            )

            export Modele_Otomatic_DK_MID is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/dk/otomatic_dk/Otomatic_DK_MID.fbx"
            )

            export Modele_Otomatic_DK_LOW is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/dk/otomatic_dk/Otomatic_DK_LOW.fbx"
            )""",
    },
}
# fmt: on
