"""aa missile definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("SAM_Strela10M3_salvolength4", "SAM", None, False): { # 214
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 2.5,
                "TempsEntreDeuxFx": 2.5,
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

    ("SAM_Strela10_salvolength4", "SAM", None, False): { # 213
        "Ammunition": {
            "parent_membr": {
                "TempsEntreDeuxTirs": 2.5,
                "TempsEntreDeuxFx": 2.5,
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 2450,
                "TempsDeVisee": 1.2,
            },
        },
        "BaseSupplyCost": 40,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["MTLB_Strela10_DDR", "MTLB_Strela10_SOV"]
            },
        },
    },

    ("SAM_Strela1_salvolength4", "SAM", None, False): { # 212
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 40,
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1750,
                "TempsEntreDeuxSalves": 7.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 25,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
            "units": {
                4: ["BRDM_Strela_1_DDR", "BRDM_Strela_1_SOV"]
            },
        },
    },
    
    ("SAM_RAPIER", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 2.5,
                "TempsEntreDeuxFx": 2.5,
                "PhysicalDamages": 5.0,
                "PorteeMaximaleTBAGRU": 3500,
                "PorteeMaximaleHAGRU": 2800,
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
    
    ("SAM_RAPIER_FSA_salvolength4", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 2.5,
                "TempsEntreDeuxFx": 2.5,
                "PhysicalDamages": 5.0,
                "PorteeMaximaleTBAGRU": 3850,
                "PorteeMaximaleHAGRU": 3150,
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
                "TempsEntreDeuxTirs": 2.5,
                "TempsEntreDeuxFx": 2.5,
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
            "parent_membr": {
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 35,
        "WeaponDescriptor": {
            "SalvoLengths": [4, 1],
        },
    },

    ("SAM_I_Hawk_salvolength3", "SAM", None, False): { # 193
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 3325,
                "SupplyCost": 450,
            }
        },
    },

    ("SAM_Igla", "MANPAD", None, False): { # 192
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 1.2,
                "SupplyCost": 35,
            },
        },
    },

    ("SAM_FIM92_Stinger_salvolength8", "MANPAD", None, False): { # 187
        "Ammunition": {
            "displayname": "FIM-92C Stinger",
            "nametoken": "AKFXZOAXUI",
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
            "SalvoLengths": [8],
        },
    },
    
    ("SAM_FIM92_Stinger_salvolength4", "MANPAD", None, False): { # 187
        "Ammunition": {
            "displayname": "FIM-92C Stinger",
            "nametoken": "PKCEMABZUN",
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
        },
    },
    
    ("SAM_FIM92_Stinger_CS", "MANPAD", None, False): { # 185
        "Ammunition": {
            "displayname": "FIM-92C Stinger",
            "nametoken": "UHRYBRDGDI",
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
            "SalvoLengths": [4, 1],
        },
    },

    ("SAM_9M330_Tor_salvolength8", "SAM", None, False): { # 179
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 3325,
                "PorteeMaximaleHAGRU": 3675,
                "TempsDeVisee": 1.2,
                "SupplyCost": 640,
            }
        },
    },

    ("SAM_9M336_salvolength3", "SAM", None, False): { # 178
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2800,
                "PorteeMaximaleHAGRU": 5250,
            }
        },
    },

    ("SAM_9M311_Tunguska_salvolength8", "SAM", None, False): { # 177
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 3150,
                "PorteeMaximaleHAGRU": 2800,
                "TempsDeVisee": 1.2,
                "SupplyCost": 480,
            }
        },
    },

    ("MANPAD_igla", "MANPAD", None, False): { # 174
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleHAGRU": 1925,
                "TempsEntreDeuxSalves": 7.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 35,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
    },

    ("MANPAD_Strela2M", "MANPAD", None, False): { # 171
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1750,
                "TempsEntreDeuxSalves": 7.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 25,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
    },
    
    ("Javelin", "MANPAD", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TempsEntreDeuxSalves": 7.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 25,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
    },
    
    ("MANPAD_FIM92", "MANPAD", None, False): { # 170
        "Ammunition": {
            "hit_roll": {
                "Idling": 65,
            },
            "displayname": "FIM-92C Stinger",
            "nametoken": "GPRDGRDYEA",
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TempsEntreDeuxSalves": 7.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 35,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
    },
    
    ("MANPAD_Blowpipe", "MANPAD", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2100,
                "PorteeMaximaleHAGRU": 1750,
                "TempsEntreDeuxSalves": 7.0,
                "TempsDeVisee": 1.2,
            }
        },
        "BaseSupplyCost": 20,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
    },
    
    ("Javelin_LML", "SAM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.2,
                "TempsEntreDeuxFx": 1.2,
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 1925,
                "TempsEntreDeuxSalves": 12.0,
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
}
# fmt: on
