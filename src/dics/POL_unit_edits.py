pol_unit_edits = {
    #POL ARTILLERY
    "Mortier_2B9_Vasilek_Para_POL": {
        "CommandPoints": 45,
        "availability": 4,
        "orders": {
            "add_orders": ["ShootOnPositionSmoke", "ShootOnPositionWithoutCorrectionSmoke"],
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.5],
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "MountedWeapons": {
                        "add": {
                            "Mortier_Vasilek_indirect_82mm_towed": {
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE_towed",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm_towed'",
                                "HandheldEquipmentKey": "'MeshAlternative_3'",
                                "ShowDispersion": False,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                                "WeaponShootDataPropertyName": ['WeaponShootData_0_3'],
                            },
                        },
                    },
                },
            },
        },
    },
    #POL DCA
    "DCA_ZU_23_2_POL": {
        "CommandPoints": 20,
        "category": "Logistic",
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "POL_4_Zmechanizowana": {
                "cards": 2,
            },
            "POL_20_Pancerna": {
                "cards": 1,
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 4,
    },
}