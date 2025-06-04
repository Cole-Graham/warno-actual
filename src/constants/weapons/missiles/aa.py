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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
                "PorteeMaximaleTBAGRU": 2800,
                "PorteeMaximaleHAGRU": 2625,
                "PhysicalDamages": 5.0,
                "TempsDeVisee": 1.2,
            },
        },
        "BaseSupplyCost": 50,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["MTLB_Strela10M3_SOV"]
            },
        },
    },

    ("SAM_Strela10", "SAM", None, False): { # 213
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 2450,
                "TempsDeVisee": 1.2,
            },
        },
        "BaseSupplyCost": 40,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 25.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 25,
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
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 3.5,
            }
        },
        "BaseSupplyCost": 25,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
                "PhysicalDamages": 5.0,
                "PorteeMaximaleTBAGRU": 2800,
                "PorteeMaximaleHAGRU": 3500,
                "TempsDeVisee": 1.2,
            },
        },
        "BaseSupplyCost": 60,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
                "PhysicalDamages": 5.0,
                "PorteeMaximaleTBAGRU": 3150,
                "PorteeMaximaleHAGRU": 3850,
                "TempsDeVisee": 1.2,
            },
        },
        "BaseSupplyCost": 60,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
                "PorteeMaximaleTBAGRU": 3150,
                "PorteeMaximaleHAGRU": 2800,
                "TempsDeVisee": 1.2,
            },
        },
        "BaseSupplyCost": 60,
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
            "parent_membr": {
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 1.2,

            }
        },
        "BaseSupplyCost": 35,
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
            "parent_membr": {
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 2.4,
            }
        },
        "BaseSupplyCost": 35,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["Ka_50_AA_SOV", "Mi_24V_AA_SOV", "Mi_24V_SOV"],
            },
        },
    },

    ("SAM_I_Hawk", "SAM", None, False): { # 193
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 3325,
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
            },
        },
        # "BaseSupplyCost": 150,
        "BaseSupplyCost": 100,
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

    ("SAM_Igla", "MANPAD", None, False): { # 192
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "parent_membr": {
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 1.2,
                "SupplyCost": 35,
            },
        },
    },
    
    ("SAM_Igla_HAGRU", "MANPAD", "SAM_Igla", True): { # 192
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "parent_membr": {
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 3.5,
                "SupplyCost": 35,
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
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 35,
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
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 2.4,
            }
        },
        "BaseSupplyCost": 35,
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
            "token": "UHRYBRDGDI",
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 2100,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 35,
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
            "token": "UHRYBRDGDI",
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 2100,
                "TempsDeVisee": 2.4,
            }
        },
        "BaseSupplyCost": 35,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["AH1F_ATAS_US", "AH64_Apache_ATAS_US", "OH58_CS_US"]
            },
        },
    },

    ("SAM_9M330_Tor", "SAM", None, False): { # 179
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 3325,
                "PorteeMaximaleHAGRU": 3675,
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 80,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
            "units": {
                8: ["Tor_SOV"],
            },
        },
    },
    
    ("SAM_ROLAND_2", "SAM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2800,
                "PorteeMaximaleHAGRU": 3500,
                "TempsDeVisee": 1.2,
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
            },
        },
        "BaseSupplyCost": 60,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
            "units": {
                2: ["Roland_2_FR"],
            },
        },
    },
    
    ("SAM_ROLAND_3", "SAM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 3150,
                "PorteeMaximaleHAGRU": 4375,
                "TempsDeVisee": 1.2,
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
            },
        },
        "BaseSupplyCost": 80,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
            "units": {
                2: ["Roland_3_FR"],
            },
        },
    },

    ("SAM_9M336", "SAM", None, False): { # 178
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2800,
                "PorteeMaximaleHAGRU": 5250,
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
            }
        },
        # "BaseSupplyCost": 130,
        "BaseSupplyCost": 100,
        "WeaponDescriptor": {
            "SalvoLengths": [3],
            "units": {
                3: ["2K12_KUB_DDR", "2K12_KUB_SOV", "2K12_KUB_POL"],
            },
        },
    },

    ("SAM_9M311_Tunguska", "SAM", None, False): { # 177
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 3150,
                "PorteeMaximaleHAGRU": 2800,
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoFx": 3.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 75,
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
            "parent_membr": {
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 1.2,
                "SupplyCost": 35,
            }
        },
    },
    
    ("MANPAD_igla_HAGRU", "MANPAD", "MANPAD_igla", True): { # 174
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "parent_membr": {
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 3.5,
                "SupplyCost": 35,

            }
        },
    },

    ("MANPAD_Strela2M", "MANPAD", None, False): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 14.0,
                "TempsDeVisee": 1.2,
                "SupplyCost": 25,
            }
        },
    },
    
    ("MANPAD_Strela2M_HAGRU", "MANPAD", "MANPAD_Strela2M", True): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 14.0,
                "TempsDeVisee": 3.5,
                "SupplyCost": 25,
            }
        },
    },

    ("SAM_Strela2M", "MANPAD", None, False): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 25,
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
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 3.0,
            }
        },
        "BaseSupplyCost": 25,
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
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 1.2,
                "SupplyCost": 25,
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
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 3.5,
                "SupplyCost": 25,
            }
        },
    },
    
    ("Mistral", "MANPAD", None, False): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2800,
                "PorteeMaximaleHAGRU": 2100,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 1.2,
                "SupplyCost": 35,
            }
        },
    },
    
    ("Mistral_HAGRU", "MANPAD", "Mistral", True): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2800,
                "PorteeMaximaleHAGRU": 2100,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 3.5,
                "SupplyCost": 35,
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
            },
            "display": "FIM-92C Stinger",
            "token": "GPRDGRDYEA",
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 1.2,
                "SupplyCost": 35,
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
            },
            "display": "FIM-92C Stinger",
            "token": "GPRDGRDYEA",
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 3.5,
                "SupplyCost": 35,
            }
        },
    },
    
    ("MANPAD_Blowpipe", "MANPAD", None, False): {
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2100,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 1.2,
                "SupplyCost": 20,
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
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2100,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 7.0,
                "TempsDeVisee": 3.5,
                "SupplyCost": 20,
            }
        },
    },
    
    ("Javelin_LML", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "TimeBetweenTwoFx": 1.2,
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 12.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 25,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "TimeBetweenTwoFx": 1.2,
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TimeBetweenTwoSalvos": 12.0,
                "TempsDeVisee": 3.0,
            }
        },
        "BaseSupplyCost": 25,
        "WeaponDescriptor": {
            "SalvoLengths": [3],
            "units": {
                3: ["DCA_Javelin_LML_UK", "Supacat_ATMP_Javelin_LML_UK"],
            },
        },
    },

    ("MANPAD_FIM43", "MANPAD", None, False): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_tbagru",
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 14.0,
                "TempsDeVisee": 1.2,
                "SupplyCost": 25,
            }
        },
    },

    ("MANPAD_FIM43_HAGRU", "MANPAD", "MANPAD_FIM43", True): { # 171
        "Ammunition": {
            "arme": {
                "DamageFamily": "DamageFamily_manpad_hagru",
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1750,
                "TimeBetweenTwoSalvos": 14.0,
                "TempsDeVisee": 3.5,
                "SupplyCost": 25,
            }
        },
    },
}
# fmt: on
