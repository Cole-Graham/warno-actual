"""DCA AutoCanon weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {

    ("DCA_4_canon_Maxson_towed_12_7mm", "DCA", None, False): { # 4 50 cals firing at 500 rpm, for combined 2000 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.42,
                "TimeBetweenTwoSalvos": 20.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 120,
                "AffichageMunitionParSalve": 800,
                "SupplyCost": 60.0,
            },
        },
    },

    ("DCA_4_canon_Maxson_SP_12_7mm", "DCA", None, False): { # 4 50 cals firing at 500 rpm, for combined 2000 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.42,
                "TimeBetweenTwoSalvos": 20.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 120,
                "AffichageMunitionParSalve": 800,
                "SupplyCost": 60.0,
            },
        },
    },

    ("DCA_4_canon_ZPU4_towed_14_5mm", "DCA", None, False): { # 4 14.5's firing at 600 rpm, for combined 2400 rpm, each ammo box has 2500 rounds?
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.60,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 56,
                "SupplyCost": 6.0,
            },
        },
    },

    ("DCA_2_canon_ZPU4_14_5mm", "DCA", None, False): { # 2 14.5's firing at 600 rpm, for combined 1200 rpm, each ammo box has 2500 rounds?
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.30,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 28,
                "SupplyCost": 3.0,
            },
        },
    },

    ("DCA_4_canon_ZPU4_14_5mm", "DCA", None, False): { # 4 14.5's firing at 600 rpm, for combined 2400 rpm, each ammo box has 2500 rounds?
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.60,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 56,
                "SupplyCost": 6.0,
            },
        },
    },

    ("DCA_1_canon_FK20_20mm_TOWED", "DCA", None, False): { # 20mm with 1000 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.34,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "TimeBetweenTwoSalvos": 1.6,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 23,
                "SupplyCost": 2.0,
            },
        },
    },

    ("DCA_1_canon_FK20_20mm", "DCA", None, False): { # 20mm with 1000 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.34,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 23,
                "SupplyCost": 2.0,
            },
        },
    },

     ("DCA_2_canon_FK20_20mm", "DCA", None, False): { # twin 20mm with combined 2000 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.68,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 46,
                "SupplyCost": 5.0,
            },
        },
    },
    
    ("DCA_1_canon_53T2_20mm", "DCA", None, False): { # 20mm with 740 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.25,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 17,
                "SupplyCost": 2.0,
            },
        },
    },

    ("DCA_1_canon_53T2_20mm_TOWED", "DCA", None, False): { # 20mm with 740 RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.25,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 17,
                "SupplyCost": 2.0,
            },
        },
    },

    ("DCA_2_canon_76T2_20mm", "DCA", None, False): { # Twin 20mm at 1500 combined RPM
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 0.5,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 34,
                "SupplyCost": 4.0,
            },
        },
    },

    ("DCA_4_canons_AZP_23_Amur_23mm_Afghan", "DCA", None, False): { # Afghanskii
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2275,
                "MaximumRangeAirplaneGRU": 1952,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 1.38,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 5,
                "AffichageMunitionParSalve": 60,
                "SupplyCost": 6.0,
            },
        },
    },
    
    ("DCA_4_canons_AZP_23_Amur_23mm_late", "DCA", None, False): { # Biryusa
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 2100,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 1.38,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 5,
                "AffichageMunitionParSalve": 60,
                "SupplyCost": 6.0,
            },
        },
    },
    
    ("DCA_4_canons_AZP_23_Amur_23mm_PSNR", "DCA", None, False): { # PSNR (only ground radar, i.e. stat clone of afghanskii)
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2275,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 1.38,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 5,
                "AffichageMunitionParSalve": 60,
                "SupplyCost": 6.0,
            },
        },
    },
    
    ("DCA_4_canons_APZ23_23mm", "DCA", None, False): { # Shilka
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2275,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 1.38,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 5,
                "AffichageMunitionParSalve": 60,
                "SupplyCost": 6.0,
            },
        },
    },
    
    ("DCA_2_canon_ZU23_2_23mm_TOWED", "DCA", None, False): { # Twin 23mm with combined 2000 cyclic rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.76,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 46,
                "SupplyCost": 5.0,
            },
        },
    },

    ("DCA_2_canon_ZU23_2_23mm", "DCA", None, False): { # Twin 23mm with combined 2000 cyclic rpm
        "Ammunition": {
             "hit_roll": {
                "Idling": 25,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.76,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 46,
                "SupplyCost": 5.0,
            },
        },
    },

    ("DCA_2_canon_Jod_SP_23mm", "DCA", None, False): { # Twin 23mm with combined 2000 cyclic rpm
        "Ammunition": {
             "hit_roll": {
                "Idling": 25,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.76,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 46,
                "SupplyCost": 5.0,
            },
        },
    },

    ("DCA_2_canon_Jod_towed_23mm", "DCA", None, False): { # Twin 23mm with combined 2000 cyclic rpm
        "Ammunition": {
             "hit_roll": {
                "Idling": 25,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.76,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 7,
                "AffichageMunitionParSalve": 46,
                "SupplyCost": 5.0,
            },
        },
    },

    ("DCA_2_canon_2M3_25mm", "DCA", None, False): { # Twin 25mm at 450 rpm each, for combined 900 rpm
        "Ammunition": {
             "hit_roll": {
                "Idling": 25,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.38,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 30,
                "SupplyCost": 3.0,
            },
        },
    },
    
    ("DCA_2_canons_2A38M_30mm", "DCA", None, False): { # Tunguska, twin 30mm at like 4200 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "PhysicalDamages": 2.1,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 6,
                "AffichageMunitionParSalve": 84,
                "SupplyCost": 24.0,
            },
        },
    },
    
    ("DCA_2_canons_HS_831_30mm", "DCA", None, False): { # Twin 30mm that fires at 600 rpm each, for a combined 1200rpm, AMX-13 DCA
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
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
                "SupplyCost": 12.0,
            },
        },
    },

    ("DCA_2_canons_HS_831_30mm_TOWED", "DCA", None, False): { # Single 30mm that fires at 600 rpm (2_canons name is mistake)
        "Ammunition": {
            "hit_roll": {
                "Idling": 20, # No FCS
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "PhysicalDamages": 0.3,
                "TimeBetweenTwoSalvos": 1.0,
                "AimingTime": 1.2,
                "ShotsCountPerSalvo": 10,
                "AffichageMunitionParSalve": 20,
                "SupplyCost": 6.0,
            },
        },
    },

    ("DCA_2_canons_Oerlikon_GDF_35mm", "DCA", None, False): { # Gepard, 35mm at 1200 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
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
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 20,
                "AffichageMunitionParSalve": 40,
                "SupplyCost": 18.0,
            },
        },
    },

    ("DCA_2_canons_Oerlikon_GDF_002_35mm", "DCA", None, False): { # Skyguard, 35mm at 1200 rpm
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "PhysicalDamages": 0.7,
                "AimingTime": 1.2,
                "TimeBetweenTwoSalvos": 1.0,
                "ShotsCountPerSalvo": 20,
                "AffichageMunitionParSalve": 40,
                "SupplyCost": 18.0,
            },
        },
        "WeaponDescriptor": {
            "Salves": 7,
        },
    },
    
    ("DCA_2_canon_Bofors_40mm", "DCA", None, False): { # M24 Duster -Twin 40mm L60 Bofors, 280 combined RPM, Salvo length is the total ammo
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "ShotsCountPerSalvo": 480,
                "AffichageMunitionParSalve": 480,
                "TimeBetweenTwoSalvos": 10.0,
                "SupplyCost": 360.0,
            },
        },
    },
    
    ("DCA_1_canon_Bofors_40mm", "DCA", None, False): { # Single 40mm L70 Bofors, 240 RPM, Salvo length is the total ammo
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
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
                "SupplyCost": 135.0,
            },
        },
    },
    
    ("DCA_1_canon_Bofors_40mm_radar", "DCA", "DCA_1_canon_Bofors_40mm", True): { # Single 40mm L70 Bofors, 240 RPM, Salvo length is the total ammo
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "add": [41, "Guidance = Guidance_Radar"],
                "TimeBetweenTwoShots": 0.3,
                "TimeBetweenTwoFx": 0.3,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "ShotsCountPerSalvo": 180,
                "AffichageMunitionParSalve": 180,
                "TimeBetweenTwoSalvos": 10.0,
                "SupplyCost": 135.0,
            },
        },
    },

    ("DCA_1_canon_Bofors_40mm_L60", "DCA", None, False): { # Single 40mm L60 Bofors, 140 RPM, Salvo length is the total ammo
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
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
                "SupplyCost": 120.0,
            },
        },
    },
    
    ("DCA_1_canon_S60_57mm", "DCA", None, False): { # Single 57mm, 120 RPM, Salvo length is the total ammo
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.5,
                "TimeBetweenTwoFx": 0.5,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2275,
                "PhysicalDamages": 1.0,
                "ShotsCountPerSalvo": 200,
                "AffichageMunitionParSalve": 200,
                "TimeBetweenTwoSalvos": 10.0,
                "SupplyCost": 8.0,
                "SupplyCost": 200.0,
            },
        },
    },
    
    ("DCA_2_canons_S60_57mm", "DCA", None, False): { # Twin 57mm, 240 RPM, Salvo length is the total ammo
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.3,
                "TimeBetweenTwoFx": 0.3,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2275,
                "PhysicalDamages": 1.0,
                "ShotsCountPerSalvo": 400,
                "AffichageMunitionParSalve": 400,
                "TimeBetweenTwoSalvos": 10.0,
                "SupplyCost": 400.0,
            },
        },
    },
    
    ("DCA_1_canon_S60_57mm_radar", "DCA", "DCA_1_canon_S60_57mm", True): { # Single 57mm, 120 RPM, PUAZO fire director and SON-9 fire-control radar
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
            },
            "parent_membr": {
                "add": [41, "Guidance = Guidance_Radar"],
                "TraitsToken": ['STAT', 'RADAR'],
                "TimeBetweenTwoShots": 0.5,
                "TimeBetweenTwoFx": 0.5,
                "AimingTime": 1.5,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2625,
                "PhysicalDamages": 1.0,
                "ShotsCountPerSalvo": 200,
                "AffichageMunitionParSalve": 200,
                "TimeBetweenTwoSalvos": 10.0,
                "SupplyCost": 8.0,
                "SupplyCost": 200.0,
            },
        },
    },
    
    ("DCA_1_canon_KS19_100mm_radar", "DCA", "DCA_1_canon_KS19_100mm", True): { # Single 100mm, 120 RPM, PUAZO fire director and SON-9 fire-control radar
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "add": [41, "Guidance = Guidance_Radar"],
                "TraitsToken": ['STAT', 'RADAR'],
                "AimingTime": 2.0,
                "MaximumRangeGRU": 1750,
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2625,
                "PhysicalDamages": 5.0,
                "ShotsCountPerSalvo": 60,
                "AffichageMunitionParSalve": 60,
                "TimeBetweenTwoSalvos": 10.0,
                "SupplyCost": 8.0,
                "SupplyCost": 240.0,
            },
        },
    },
    
    ("DCA_1_canon_KS30_130mm_radar", "DCA", "DCA_1_canon_KS30_130mm", True): { # Single 130mm, 120 RPM, PUAZO fire director and SON-9 fire-control radar
        "Ammunition": {
            "hit_roll": {
                "Idling": 40
            },
            "parent_membr": {
                "add": [41, "Guidance = Guidance_Radar"],
                "TraitsToken": ['STAT', 'RADAR'],
                "AimingTime": 2.0,
                "MaximumRangeGRU": 1750,
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2625,
                "PhysicalDamages": 7.0,
                "ShotsCountPerSalvo": 60,
                "AffichageMunitionParSalve": 60,
                "TimeBetweenTwoSalvos": 10.0,
                "SupplyCost": 360.0,
            },
        },
    },
}
# fmt: on
