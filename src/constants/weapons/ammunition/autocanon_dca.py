"""DCA AutoCanon weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {

    ("DCA_4_canon_Maxson_towed_12_7mm", "DCA", None, False): { # 4 50 cals firing at 500 rpm, for combined 2000 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.43,
                "TimeBetweenTwoSalvos": 20.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 240,
                "AffichageMunitionParSalve": 800,
            },
        },
    },

    ("DCA_4_canon_Maxson_SP_12_7mm", "DCA", None, False): { # 4 50 cals firing at 500 rpm, for combined 2000 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.43,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 240,
                "AffichageMunitionParSalve": 800,
            },
        },
    },

    ("DCA_4_canon_ZPU4_towed_14_5mm", "DCA", None, False): { # 4 14.5's firing at 600 rpm, for combined 2400 rpm, each ammo box has 2500 rounds?
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.58,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 5,
                "AffichageMunitionParSalve": 20,
            },
        },
    },

    ("DCA_2_canon_ZPU4_14_5mm", "DCA", None, False): { # 2 14.5's firing at 600 rpm, for combined 1200 rpm, each ammo box has 2500 rounds?
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.29,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 5,
                "AffichageMunitionParSalve": 10,
            },
        },
    },

    ("DCA_4_canon_ZPU4_14_5mm", "DCA", None, False): { # 4 14.5's firing at 600 rpm, for combined 2400 rpm, each ammo box has 2500 rounds?
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.58,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 5,
                "AffichageMunitionParSalve": 20,
            },
        },
    },

    ("DCA_1_canon_FK20_20mm_TOWED", "DCA", None, False): { # 20mm with 1000 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.334,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.6,
                "ShotsCountPerSalvo": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
    },

    ("DCA_1_canon_FK20_20mm", "DCA", None, False): { # 20mm with 1000 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.334,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.6,
                "ShotsCountPerSalvo": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
    },

     ("DCA_2_canon_FK20_20mm", "DCA", None, False): { # twin 20mm with combined 2000 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.668,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.6,
                "ShotsCountPerSalvo": 15,
                "AffichageMunitionParSalve": 50,
            },
        },
    },
    
    ("DCA_1_canon_53T2_20mm", "DCA", None, False): { # 20mm with 740 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.25,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 12,
            },
        },
    },

    ("DCA_1_canon_53T2_20mm_TOWED", "DCA", None, False): { # 20mm with 740 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.25,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 12,
            },
        },
    },

    ("DCA_2_canon_76T2_20mm", "DCA", None, False): { # Twin 20mm at 1500 combined RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.5,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 25,
            },
        },
    },

    ("DCA_4_canons_AZP_23_Amur_23mm_Afghan", "DCA", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
                "Moving": 5,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 1.38,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 5,
                "AffichageMunitionParSalve": 30,
            },
        },
    },
    
    ("DCA_4_canons_AZP_23_Amur_23mm_late", "DCA", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
                "Moving": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2100,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 1.38,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 60,
            },
        },
    },
    
    ("DCA_4_canons_AZP_23_Amur_23mm_PSNR", "DCA", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
                "Moving": 5,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 1.38,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 5,
                "AffichageMunitionParSalve": 30,
            },
        },
    },
    
    ("DCA_4_canons_APZ23_23mm", "DCA", None, False): { # 274
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
                "Moving": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2100,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 1.38,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 60,
            },
        },
    },
    
    ("DCA_2_canon_ZU23_2_23mm_TOWED", "DCA", None, False): { # Twin 23mm with combined 2000 cyclic rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.77,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 33,
            },
        },
    },

    ("DCA_2_canon_ZU23_2_23mm", "DCA", None, False): { # Twin 23mm with combined 2000 cyclic rpm
        "Ammunition": {
             "hit_roll": {
                "Idling": 10,
                "Moving": 5,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.77,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 33,
            },
        },
    },

    ("DCA_2_canon_Jod_SP_23mm", "DCA", None, False): { # Twin 23mm with combined 2000 cyclic rpm
        "Ammunition": {
             "hit_roll": {
                "Idling": 10,
                "Moving": 5,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.77,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 33,
            },
        },
    },

    ("DCA_2_canon_Jod_towed_23mm", "DCA", None, False): { # Twin 23mm with combined 2000 cyclic rpm
        "Ammunition": {
             "hit_roll": {
                "Idling": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.77,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 33,
            },
        },
    },

    ("DCA_2_canon_2M3_25mm", "DCA", None, False): { # Twin 25mm at 450 rpm each, for combined 900 rpm
        "Ammunition": {
             "hit_roll": {
                "Idling": 10,
                "Moving": 5,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.35,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 15,
            },
        },
    },
    
    ("DCA_2_canons_2A38M_30mm", "DCA", None, False): { # Tunguska, twin 30mm at like 4200 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
                "Moving": 10,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "PhysicalDamages": 2.1,
                "SuppressDamages": 60,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 70,
            },
        },
    },
    
    ("DCA_2_canons_HS_831_30mm", "DCA", None, False): { # Twin 30mm that fires at 600 rpm each, for a combined 1200rpm, AMX-13 DCA
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
                "Moving": 5,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "PhysicalDamages": 0.6,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 20,
                "AffichageMunitionParSalve": 40,
            },
        },
    },

    ("DCA_2_canons_HS_831_30mm_TOWED", "DCA", None, False): { # Single 30mm that fires at 600 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "PhysicalDamages": 0.3,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 20,
                "AffichageMunitionParSalve": 20,
            },
        },
    },

    ("DCA_2_canons_Oerlikon_GDF_35mm", "DCA", None, False): { # Gepard, 35mm at 1200 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
                "Moving": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "PhysicalDamages": 0.7,
                "AimingTime": 1.2,
                "TimeBetweenTwoSalvos": 0.5,
                "ShotsCountPerSalvo": 20,
                "AffichageMunitionParSalve": 40,
            },
        },
    },

    ("DCA_2_canons_Oerlikon_GDF_002_35mm", "DCA", None, False): { # Skyguard, 35mm at 1200 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "PhysicalDamages": 0.7,
                "AimingTime": 1.2,
                "TimeBetweenTwoSalvos": 0.5,
                "ShotsCountPerSalvo": 18,
                "AffichageMunitionParSalve": 36,
            },
        },
        "WeaponDescriptor": {
            "Salves": 7,
        },
    },
    
    ("DCA_2_canon_Bofors_40mm", "DCA", None, False): { # Twin 40mm L60 Bofors, 280 combined RPM, Salvo length is the total ammo
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "ShotsCountPerSalvo": 340,
                "AffichageMunitionParSalve": 340,
                "TimeBetweenTwoSalvos": 10.0,
            },
        },
    },
    
    ("DCA_1_canon_Bofors_40mm", "DCA", None, False): { # Single 40mm L70 Bofors, 240 RPM, Salvo length is the total ammo
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.3,
                "TimeBetweenTwoFx": 0.3,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "ShotsCountPerSalvo": 180,
                "AffichageMunitionParSalve": 180,
                "TimeBetweenTwoSalvos": 10.0,
            },
        },
    },

    ("DCA_1_canon_Bofors_40mm_L60", "DCA", None, False): { # Single 40mm L60 Bofors, 140 RPM, Salvo length is the total ammo
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "TimeBetweenTwoFx": 0.4,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "ShotsCountPerSalvo": 120,
                "AffichageMunitionParSalve": 120,
                "TimeBetweenTwoSalvos": 10.0,
            },
        },
    },
    
    ("DCA_1_canon_S60_57mm", "DCA", None, False): { # Single 57mm, 120 RPM, Salvo length is the total ammo
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 0.5,
                "TimeBetweenTwoFx": 0.5,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2275,
                "ShotsCountPerSalvo": 200,
                "AffichageMunitionParSalve": 200,
                "TimeBetweenTwoSalvos": 10.0,
                "SupplyCost": 8.0,
            },
        },
    },
    
    ("DCA_2_canons_S60_57mm", "DCA", None, False): { # Twin 57mm, 240 RPM, Salvo length is the total ammo
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 0.3,
                "TimeBetweenTwoFx": 0.3,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2275,
                "ShotsCountPerSalvo": 400,
                "AffichageMunitionParSalve": 400,
                "TimeBetweenTwoSalvos": 10.0,
                "SupplyCost": 16.0,
            },
        },
    },
}
# fmt: on
