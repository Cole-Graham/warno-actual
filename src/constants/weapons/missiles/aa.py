"""aa missile definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("SAM_Strela10M3", "SAM", None, False): { # 214
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2625,
                "PhysicalDamages": 5.0,
                "AimingTime": 1.2,
            },
        },
        "SupplyCost": 65.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["MTLB_Strela10M3_SOV"]
            },
        },
    },

    ("SAM_Strela10", "SAM", None, False): { # 213
        "Ammunition": {
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "AimingTime": 1.2,
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["MTLB_Strela10_DDR", "MTLB_Strela10_SOV", "MTLB_Strela10_POL"]
            },
        },
    },

    ("SAM_Strela1", "SAM", None, False): { # 212
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 40,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 25.0,
                "AimingTime": 1.2,
            }
        },
        "SupplyCost": 25.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["BRDM_Strela_1_DDR", "BRDM_Strela_1_SOV", "BRDM_Strela_1_POL"]
            },
        },
    },
    
    ("SAM_Strela1_HAGRU", "SAM", "SAM_Strela1", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 40,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.5,
            }
        },
        "SupplyCost": 25.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["BRDM_Strela_1_DDR", "BRDM_Strela_1_SOV", "BRDM_Strela_1_POL"]
            },
        },
    },
    
    ("SAM_RAPIER", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
                "PhysicalDamages": 5.0,
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 3500,
                "AimingTime": 1.2,
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8, 4],
            "units": {
                8: ["Tracked_Rapier_UK"],
                4: ["DCA_Rapier_UK"],
            },
        },
    },
    
    ("SAM_RAPIER_FSA", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
                "PhysicalDamages": 5.0,
                "MaximumRangeHelicopterGRU": 3150,
                "MaximumRangeAirplaneGRU": 3850,
                "AimingTime": 1.2,
            },
        },
        "SupplyCost": 65.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["DCA_Rapier_FSA_UK"],
            },
        },
    },

    ("SAM_MIM72G", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
                "MaximumRangeHelicopterGRU": 3150,
                "MaximumRangeAirplaneGRU": 2800,
                "AimingTime": 1.2,
            },
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["M48_Chaparral_MIM72F_US", "DCA_XM85_Chaparral_US"]
            },
        },
    },

    ("SAM_IglaV", "MANPAD", None, False): { # 196
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.2,
            }
        },
        "SupplyCost": 35.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["Ka_50_AA_SOV", "Mi_24V_AA_SOV", "Mi_24V_SOV"],
            },
        },
    },
    
    ("SAM_IglaV_HAGRU", "MANPAD", "SAM_IglaV", True): { # 196
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 2.4,
            }
        },
        "SupplyCost": 35.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["Ka_50_AA_SOV", "Mi_24V_AA_SOV", "Mi_24V_SOV"],
            },
        },
    },

    ("SAM_I_Hawk", "SAM", None, False): { # 193
        "Ammunition": {
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 3325,
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
            },
        },
        "SupplyCost": 150.0,
        "WeaponDescriptor": {
            "SalvoLengths": [3],
            "units": {
                3: [
                    "DCA_I_Hawk_BEL",
                    "DCA_I_Hawk_NL",
                    "DCA_I_Hawk_RFA",
                    "DCA_I_Hawk_US",
                    "DCA_I_Hawk_capture_DDR",
                ],
            },
        },
    },
    
    ("SAM_BLOODHOUND", "SAM", None, False): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_missile_he_bigly",
            },
            "hit_roll": {
                "Idling": 65,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 6125,
                "PhysicalDamages": 9.0,
                "SupplyCost": 180.0,
            },
        },
    },
    
    ("SAM_9M38M1", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 5950,
                "MaximumRangeHelicopterGRU": 2975,
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
            }
        },
        "SupplyCost": 150.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["Buk_9K37M_SOV"],
            },
        },
    },

    ("SAM_Igla", "MANPAD", None, False): { # 192
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 1.2,
                "SupplyCost": 35.0,
            },
        },
    },
    
    ("SAM_Igla_HAGRU", "MANPAD", "SAM_Igla", True): { # 192
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.5,
                "SupplyCost": 35.0,
            },
        },
    },

    ("SAM_FIM92_Stinger", "MANPAD", None, False): { # 187
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "display": "FIM-92C Stinger",
            "token": "AKFXZOAXUI",
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.2,
            }
        },
        "SupplyCost": 35.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
            "units": {
                8: ["M998_Avenger_US", "M998_Avenger_nonPara_US"],
            },
        },
    },
    
    ("SAM_FIM92_Stinger_HAGRU", "MANPAD", "SAM_FIM92_Stinger", True): { # 187
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "display": "FIM-92C Stinger",
            "token": "AKFXZOAXUI",
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 2.4,
            }
        },
        "SupplyCost": 35.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
            "units": {
                8: ["M998_Avenger_US", "M998_Avenger_nonPara_US"],
            },
        },
    },
    
    ("SAM_FIM92_Stinger_CS", "MANPAD", None, False): { # 185
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "display": "FIM-92C Stinger",
            "token": "AKFXZOAXUI",
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2100,
                "AimingTime": 1.2,
            }
        },
        "SupplyCost": 35.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["AH1F_ATAS_US", "AH64_Apache_ATAS_US", "OH58_CS_US"]
            },
        },
    },
    
    ("SAM_FIM92_Stinger_CS_HAGRU", "MANPAD", "SAM_FIM92_Stinger_CS", True): { # 185
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "display": "FIM-92C Stinger",
            "token": "AKFXZOAXUI",
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2100,
                "AimingTime": 2.4,
            }
        },
        "SupplyCost": 35.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["AH1F_ATAS_US", "AH64_Apache_ATAS_US", "OH58_CS_US"]
            },
        },
    },

    ("SAM_9M330_Tor", "SAM", None, False): { # 179
        "Ammunition": {
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 3325,
                "MaximumRangeAirplaneGRU": 3675,
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
                "AimingTime": 1.2,
            }
        },
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
            "units": {
                8: ["Tor_SOV"],
            },
        },
    },
    
    ("SAM_ROLAND_2", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 3500,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
            },
        },
        "SupplyCost": 65.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
            "units": {
                2: ["Roland_2_FR"],
            },
        },
    },
    
    ("SAM_ROLAND_3", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 3150,
                "MaximumRangeAirplaneGRU": 4375,
                "AimingTime": 1.2,
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
            },
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
            "units": {
                2: ["DCA_XMIM_115A_Roland_US", "Roland_3_FR"],
            },
        },
    },

    ("SAM_9M336", "SAM", None, False): { # 178
        "Ammunition": {
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 5250,
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
            }
        },
        "SupplyCost": 130.0,
        "WeaponDescriptor": {
            "SalvoLengths": [3],
            "units": {
                3: ["2K12_KUB_DDR", "2K12_KUB_SOV", "2K12_KUB_POL"],
            },
        },
    },
    
    ("SAM_9M33M2", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2975,
                "MaximumRangeAirplaneGRU": 4200,
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
            }
        },
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6],
            "units": {
                6: ["Osa_9K33M3_SOV", "Osa_9K33M3_TCH", "Osa_9K33M3_DDR", "Osa_9K33M3_POL"],
            },
        },
    },

    ("SAM_9M311_Tunguska", "SAM", None, False): { # 177
        "Ammunition": {
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 3150,
                "MaximumRangeAirplaneGRU": 2800,
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
                "AimingTime": 1.2,
            }
        },
        "SupplyCost": 85.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
            "units": {
                8: ["SAM_9M311_Tunguska_SOV"],
            },
        },
    },

    ("MANPAD_igla", "MANPAD", None, False): { # 174
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 1.2,
                "SupplyCost": 35.0,
            }
        },
    },
    
    ("MANPAD_igla_HAGRU", "MANPAD", "MANPAD_igla", True): { # 174
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.5,
                "SupplyCost": 35.0,

            }
        },
    },

    ("MANPAD_Strela2M", "MANPAD", None, False): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 14.0,
                "AimingTime": 1.2,
                "SupplyCost": 25.0,
            }
        },
    },
    
    ("MANPAD_Strela2M_HAGRU", "MANPAD", "MANPAD_Strela2M", True): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 14.0,
                "AimingTime": 3.5,
                "SupplyCost": 25.0,
            }
        },
    },
    
    ("SAM_Strela2", "MANPAD", None, False): { #
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 1.2,
            }
        },
        "SupplyCost": 25.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["W3W_Sokol_AA_POL", "Mi_2_AA_POL"],
            },
        },
    },
    
    ("SAM_Strela2_HAGRU", "MANPAD", "SAM_Strela2", True): { #
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.0,
            }
        },
        "SupplyCost": 25.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["W3W_Sokol_AA_POL", "Mi_2_AA_POL"],
            },
        },
    },

    ("SAM_Strela2M", "MANPAD", None, False): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 1.2,
            }
        },
        "SupplyCost": 25.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
            "units": {
                2: [
                    "DCA_ZUR_23_2S_JOD_POL",
                    "DCA_ZUR_23_2S_JOD_Para_POL",
                    "Hibneryt_KG_POL",
                    "OT_62_TOPAS_JOD_POL",
                ],
            },
        },
    },
    
    ("SAM_Strela2M_HAGRU", "MANPAD", "SAM_Strela2M", True): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.0,
            }
        },
        "SupplyCost": 25.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
            "units": {
                2: [
                    "DCA_ZUR_23_2S_JOD_POL",
                    "DCA_ZUR_23_2S_JOD_Para_POL",
                    "Hibneryt_KG_POL",
                    "OT_62_TOPAS_JOD_POL",
                ],
            },
        },
    },
    
    ("Javelin", "MANPAD", None, False): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "Idling": 50,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 1.2,
                "SupplyCost": 25.0,
            }
        },
    },
    
    ("Javelin_HAGRU", "MANPAD", "Javelin", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "Idling": 50,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.5,
                "SupplyCost": 25.0,
            }
        },
    },
    
    ("MANPAD_Starstreak", "MANPAD", "Javelin", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "Idling": 65,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2450,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 1.2,
                "SupplyCost": 40.0,
                "MissileDescriptor": "~/Descriptor_Missile_Starstreak_x3",
            },
            "Texture": "Starstreak_x3",
        },
    },
    
    ("MANPAD_Starstreak_HAGRU", "MANPAD", "Javelin", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "Idling": 65,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2450,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.5,
                "SupplyCost": 40.0,
                "MissileDescriptor": "~/Descriptor_Missile_Starstreak_x3",
            },
            "Texture": "Starstreak_x3",
        },
    },
    
    ("Mistral", "MANPAD", None, False): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2100,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 1.2,
                "SupplyCost": 35.0,
            }
        },
    },
    
    ("Mistral_HAGRU", "MANPAD", "Mistral", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2100,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.5,
                "SupplyCost": 35.0,
            }
        },
    },
    
    ("MANPAD_FIM92", "MANPAD", None, False): { # 170
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "Idling": 65,
                "DistanceToTarget": True,
            },
            "display": "FIM-92C Stinger",
            "token": "AKFXZOAXUI",
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 1.2,
                "SupplyCost": 35.0,
            }
        },
    },
    
    ("MANPAD_FIM92_HAGRU", "MANPAD", "MANPAD_FIM92", True): { # 170
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "Idling": 65,
                "DistanceToTarget": True,
            },
            "display": "FIM-92C Stinger",
            "token": "AKFXZOAXUI",
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.5,
                "SupplyCost": 35.0,
            }
        },
    },
    
    ("MANPAD_FIM92_A", "MANPAD", None, False): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "Idling": 50,
                "DistanceToTarget": True,
            },
            "display": "FIM-92A Stinger",
            "token": "HWTXIBRFHM",
        },
        "parent_membr": {
            "MaximumRangeHelicopterGRU": 2625,
            "MaximumRangeAirplaneGRU": 1925,
            "TimeBetweenTwoSalvos": 7.0,
            "AimingTime": 1.2,
            "SupplyCost": 30.0,
        },
    },
    
    ("MANPAD_FIM92_A_HAGRU", "MANPAD", "MANPAD_FIM92_A", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "Idling": 50,
                "DistanceToTarget": True,
            },
            "display": "FIM-92A Stinger",
            "token": "HWTXIBRFHM",
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.5,
                "SupplyCost": 30.0,
            },
        },
    },
    
    ("MANPAD_Blowpipe", "MANPAD", None, False): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "Idling": 40,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2100,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 1.2,
                "SupplyCost": 20.0,
            }
        },
    },
    
    ("MANPAD_Blowpipe_HAGRU", "MANPAD", "MANPAD_Blowpipe", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "Idling": 40,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2100,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "AimingTime": 3.5,
                "SupplyCost": 20.0,
            }
        },
    },
    
    ("Javelin_LML", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "TimeBetweenTwoFx": 1.2,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 12.0,
                "AimingTime": 1.2,
            }
        },
        "SupplyCost": 25.0,
        "WeaponDescriptor": {
            "SalvoLengths": [3],
            "units": {
                3: ["DCA_Javelin_LML_UK", "Supacat_ATMP_Javelin_LML_UK"],
            },
        },
    },
    
    ("Javelin_LML_HAGRU", "SAM", "Javelin_LML", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "Idling": 50,
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "TimeBetweenTwoFx": 1.2,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1925,
                "TimeBetweenTwoSalvos": 12.0,
                "AimingTime": 3.0,
            }
        },
        "SupplyCost": 25.0,
        "WeaponDescriptor": {
            "SalvoLengths": [3],
            "units": {
                3: ["DCA_Javelin_LML_UK", "Supacat_ATMP_Javelin_LML_UK"],
            },
        },
    },
    
    ("Starstreak", "SAM", None, False): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "TimeBetweenTwoFx": 1.2,
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2275,
                "TimeBetweenTwoSalvos": 12.0,
                "AimingTime": 1.2,
            },
        },
        "SupplyCost": 40.0,
        "WeaponDescriptor": {
            "SalvoLengths": [3],
            "units": {
                3: ["DCA_Starstreak_LML_UK"],
            },
        },
    },
    
    ("Starstreak_HAGRU", "SAM", "Starstreak", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "TimeBetweenTwoFx": 1.2,
                "MaximumRangeHelicopterGRU": 2800,
                "MaximumRangeAirplaneGRU": 2275,
                "TimeBetweenTwoSalvos": 12.0,
                "AimingTime": 3.0,
            },
        },
        "SupplyCost": 40.0,
        "WeaponDescriptor": {
            "SalvoLengths": [3],
            "units": {
                3: ["DCA_Starstreak_LML_UK"],
            },
        },
    },

    ("MANPAD_FIM43", "MANPAD", None, False): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 14.0,
                "AimingTime": 1.2,
                "SupplyCost": 25.0,
            }
        },
    },

    ("MANPAD_FIM43_HAGRU", "MANPAD", "MANPAD_FIM43", True): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "hit_roll": {
                "DistanceToTarget": True,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 1750,
                "TimeBetweenTwoSalvos": 14.0,
                "AimingTime": 3.5,
                "SupplyCost": 25.0,
            }
        },
    },
}
# fmt: on
