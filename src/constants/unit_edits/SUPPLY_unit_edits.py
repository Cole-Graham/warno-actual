"""supply unit edits."""

# from typing import Any, Dict

# fmt: off
from re import M

from src.utils.logging_utils import setup_logger


SUPPLY_TIERS = {
    "wheeled": {
        "tier_1": {
            "SupplyCapacity": 500.0,
            "CommandPoints": 15,
            "Divisions": {
                "default": {
                    "cards": 1,
                },
            },
            "SupplyDescriptor": "RunnerSupply",
            "availability": [8, 0, 0, 0],
        },
        "tier_2": {
            "SupplyCapacity": 675.0,
            "CommandPoints": 25,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "SquadSupply",
            "availability": [6, 0, 0, 0],
        },
        "tier_3": {
            "SupplyCapacity": 850.0,
            "CommandPoints": 35,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "SquadSupply",
            "availability": [5, 0, 0, 0],
        },
        "tier_4": {
            "SupplyCapacity": 1300.0,
            "CommandPoints": 40,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "PrimarySupply",
            "availability": [3, 0, 0, 0],
        },
        "tier_5": {
            "SupplyCapacity": 1500.0,
            "CommandPoints": 55,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "PrimarySupply",
            "availability": [3, 0, 0, 0],
        },
        "tier_6": {
            "SupplyCapacity": 2000.0,
            "CommandPoints": 70,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "PrimarySupply",
            "availability": [2, 0, 0, 0],
        },
        "tier_7": {
            "SupplyCapacity": 2300.0,
            "CommandPoints": 80,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "DvisionalSupply",
            "availability": [2, 0, 0, 0],
        },
        "tier_8": {
            "SupplyCapacity": 2750.0,
            "CommandPoints": 90,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "DvisionalSupply",
            "availability": [2, 0, 0, 0],
        },
    },
    
    "mechanized": {
        "tier_1": {
            "SupplyCapacity": 925.0,
            "CommandPoints": 30,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "SquadSupply",
            "availability": [6, 0, 0, 0],
        },
        "tier_2": {
            "SupplyCapacity": 1400.0,
            "CommandPoints": 45,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "PrimarySupply",
            "availability": [4, 0, 0, 0],
        },
        "tier_3": {
            "SupplyCapacity": 1600.0,
            "CommandPoints": 55,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "PrimarySupply",
            "availability": [4, 0, 0, 0],
        },
        "tier_4": {
            "SupplyCapacity": 2300.0,
            "CommandPoints": 75,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "DvisionalSupply",
            "availability": [3, 0, 0, 0],
        },
    },
    
    "helicopter": {
        "tier_1": {
            "SupplyCapacity": 500.0,
            "CommandPoints": 25,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "RunnerHeloSupply",
            "availability": [7, 0, 0, 0],
        },
        "tier_2": {
            "SupplyCapacity": 750.0,
            "CommandPoints": 40,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "PrimaryHeloSupply",
            "availability": [5, 0, 0, 0],
        },
        "tier_3": {
            "SupplyCapacity": 850.0,
            "CommandPoints": 45,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "PrimaryHeloSupply",
            "availability": [4, 0, 0, 0],
        },
        "tier_4": {
            "SupplyCapacity": 1100.0,
            "CommandPoints": 55,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "PrimaryHeloSupply",
            "availability": [3, 0, 0, 0],
        },
        "tier_5": {
            "SupplyCapacity": 2400.0,
            "CommandPoints": 95,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "DvisionalHeloSupply",
            "availability": [2, 0, 0, 0],
        },
        "tier_6": {
            "SupplyCapacity": 3000.0,
            "CommandPoints": 130,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "SupplyDescriptor": "DvisionalHeloSupply",
            "availability": [2, 0, 0, 0],
        },
    },
}

SUPPLY_UNITS_BY_TIER = {
    "wheeled": [
        # tier1
        ("M274_Mule_supply_US", "tier_1"),
        ("Supacat_ATMP_supply_UK", "tier_1"),
        ("Faun_Kraka_Log_RFA", "tier_1"),
        ("UAZ_469_supply_SOV", "tier_1"),
        ("UAZ_469_supply_VDV_SOV", "tier_1"),
        ("LUAZ_967M_supply_SOV", "tier_1"),
        ("UAZ_469_supply_Para_POL", "tier_1"),
        
        # tier 2
        ("Gama_Goat_supply_US", "tier_2"),
        ("CUCV_US", "tier_2"),
        ("Rover_101FC_supply_UK", "tier_2"),
        ("LAV_L_US", "tier_2"),
        
        # tier 3
        ("Unimog_S_404_RFA", "tier_3"),
        ("GAZ_66_supply_SOV", "tier_3"),
        ("GAZ_66_POL", "tier_3"),
        ("GAZ_66B_supply_POL", "tier_3"),
        ("LO_1800_supply_DDR", "tier_3"),
        ("BAV_485_Naval_supply_SOV", "tier_3"),
        ("BAV_485_Supply_POL", "tier_3"),
        ("VLRA_supply_FR", "tier_3"),
        ("TRM_2000_supply_FR", "tier_3"),
        
        # tier 4
        ("M35_supply_US", "tier_4"),
        
        # tier 5
        ("Ural_4320_DDR", "tier_5"),
        ("Ural_4320_SOV", "tier_5"),
        ("ZIL_131_supply_Naval_SOV", "tier_5"),
        ("Star_266_supply_POL", "tier_5"),
        ("Berliet_GBC_8KT_supply_FR", "tier_5"),
        ("Bedford_MJ_4t_UK", "tier_5"),
        
        # tier 6
        ("Alvis_Stalwart_UK", "tier_6"),
        ("DaimlerBenz_Typ1017_supply_RFA", "tier_6"),
        ("Berliet_GBU_15_supply_FR", "tier_6"),
        ("M812_supply_US", "tier_6"),
        ("MAZ_535A_supply_SOV", "tier_6"),
        
        # tier 7
        ("TRM_10000_supply_FR", "tier_7"),
        ("T813_DDR", "tier_7"),
        ("KrAZ_255B_supply_SOV", "tier_7"),
        ("KrAZ_255B_supply_POL", "tier_7"),
        ("KrAZ_255B_supply_DDR", "tier_7"),
        ("AEC_Militant_UK", "tier_7"),
        ("MAN_Kat_6x6_RFA", "tier_7"),
        
        # tier 8
        ("T815_supply_DDR", "tier_8"),
        ("HEMTT_US", "tier_8"),
        ("Bedford_TM_6x6_supply_UK", "tier_8"),
    ],
    
    "mechanized": [
        # tier 1
        ("M113A1G_supply_RFA", "tier_1"),
        ("M113A2_supply_US", "tier_1"),
        ("FV432_supply_UK", "tier_1"),
        ("MTLB_supply_DDR", "tier_1"),
        ("MTLB_supply_SOV", "tier_1"),
        
        # tier 2
        ("M992A2_supply_US", "tier_2"),
        
        # tier 3
        ("M548A2_supply_US", "tier_3"),
        
        # tier 4
        ("PTS_2_Naval_supply_SOV", "tier_4"),
        ("PTS_M_supply_POL", "tier_4"),
        ("PTS_M_supply_DDR", "tier_4"),
    ],
    
    "helicopter": [
        # tier 1
        ("UH1D_Supply_RFA", "tier_1"),
        ("UH1H_supply_US", "tier_1"),
        
        # tier 2
        ("UH60A_Supply_US", "tier_2"),
        ("Westland_Wessex_supply_UK", "tier_2"),
        
        # tier 3
        ("Puma_UK", "tier_3"),
        ("Puma_FR", "tier_3"),
        ("CH46E_SeaKnight_supply_US", "tier_3"),

        # tier 4
        ("Mi_8TZ_SOV", "tier_4"),
        ("Mi_14PS_supply_SOV", "tier_4"),
        ("Mi_8_supply_DDR", "tier_4"),
        ("Mi_8_supply_POL", "tier_4"),
        
        # tier 5
        ("CH47D_Chinook_supply_UK", "tier_5"),
        ("CH47_Super_Chinook_US", "tier_5"),
        ("CH53_Sea_Stallion_supply_US", "tier_5"),
        ("CH53G_RFA", "tier_5"),
        
        # tier 6
        ("CH54B_Tarhe_supply_US", "tier_6"),
        ("Mi_6_POL", "tier_6"),
        ("Mi_6_SOV", "tier_6"),
    ],
}

# Units in this dictionary do not need to be defined in the SUPPLY_UNITS_BY_TIER constant or vice-versa.
# The key will be added automatically if it is missing, you can also set completely custom values for
# any unit here if you want (such as for unique supply units like Mi-26).
# You can also over-ride one or more values of the standard by setting it in this dictionary.
supply_unit_edits = {
    # motorised supply
    "M274_Mule_supply_US": {},
    
    "Supacat_ATMP_supply_UK": {},

    "Faun_Kraka_Log_RFA": {},
    
    "UAZ_469_supply_SOV": {},
    
    "UAZ_469_supply_VDV_SOV": {},
    
    "LUAZ_967M_supply_SOV": {},
    
    "UAZ_469_supply_Para_POL": {  # Desant. UAZ-469 Zaop.
        "GameName": {
            "display": "SPADO. UAZ-469 ZAOP.",
        },
    },
    
    "Gama_Goat_supply_US": {},
    
    "CUCV_US": {},
    
    "Rover_101FC_supply_UK": {
        "tow_only": True,
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "SpecialtiesList": {
            "add_specs": ["'_transport2'"],
        },
    },
    
    "Unimog_S_404_RFA": {
        "tow_only": True,
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "SpecialtiesList": {
            "add_specs": ["'_transport2'"],
        },
    },
    
    "GAZ_66_supply_SOV": {
        "UpgradeFromUnit": "LUAZ_967M_supply_SOV",
    },
    
    "GAZ_66_POL": {},
    
    "GAZ_66B_supply_POL": {  # GAZ-66B Zaop.
        "tow_only": True,
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "SpecialtiesList": {
            "add_specs": ["'_transport2'"],
        },
    },
    
    "LO_1800_supply_DDR": {},
    
    "BAV_485_Naval_supply_SOV": {
        "UpgradeFromUnit": None,
    },
    
    "BAV_485_Supply_POL": {
        "UpgradeFromUnit": None,
    },

    "VLRA_supply_FR": {},
    
    "TRM_2000_supply_FR": {
        "tow_only": True,
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "SpecialtiesList": {
            "add_specs": ["'_transport2'"],
        },
    },
    
    "M35_supply_US": {
        "tow_only": True,
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "SpecialtiesList": {
            "add_specs": ["'_transport2'"],
        },
    },
    
    "Ural_4320_DDR": {},
    
    "Ural_4320_SOV": {
        "UpgradeFromUnit": "MTLB_supply_SOV",
    },
    
    "ZIL_131_supply_Naval_SOV": {},
    
    "Star_266_supply_POL": {
        "UpgradeFromUnit": "GAZ_66B_supply_POL",
    },

    "Berliet_GBC_8KT_supply_FR": {},
    
    "Bedford_MJ_4t_UK": {
        "tow_only": True,
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "SpecialtiesList": {
            "add_specs": ["'_transport2'"],
        },
    },
    
    "Alvis_Stalwart_UK": {},

    "DaimlerBenz_Typ1017_supply_RFA": {},

    "Berliet_GBU_15_supply_FR": {},
    
    "M812_supply_US": {}, # M813A1 SUPPLY
    
    "MAZ_535A_supply_SOV": {
        "UpgradeFromUnit": "Ural_4320_SOV",
    },

    "TRM_10000_supply_FR": {
        "GameName": {
            "display": "TRM-10000 LOG.",
        },
    },
    
    "T813_DDR": {},
    
    "KrAZ_255B_supply_SOV": {
        "UpgradeFromUnit": "MAZ_535A_supply_SOV",
    },
    
    "KrAZ_255B_supply_POL": {},

    "KrAZ_255B_supply_DDR": {},
    
    "AEC_Militant_UK": {},
    
    "MAN_Kat_6x6_RFA": {},
    
    "T815_supply_DDR": {},
    
    "HEMTT_US": {},
    
    "Bedford_TM_6x6_supply_UK": {},
    
    "Kalmar_supply_SOV": {
        "CommandPoints": 220,
        "SupplyCapacity": 8400.0,
        "SupplyDescriptor": "DvisionalSupply",
        "availability": [1, 0, 0, 0],
         "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    },

    "LARC_60_supply_US": {
        "CommandPoints": 220,
        "SupplyCapacity": 8400.0,
        "SupplyDescriptor": "DvisionalSupply",
        "availability": [1, 0, 0, 0],
         "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    }, 
    
    # mechanized supply
    "M113A1G_supply_RFA": {},
    
    "M113A2_supply_US": {
        "UpgradeFromUnit": "M1038_Humvee_supply_US",
    },
    
    "FV432_supply_UK": {},
    
    "MTLB_supply_DDR": {
        "GameName": {
            "display": "MT-LB MUN.",
        },
    },
    
    "MTLB_supply_SOV": {
        "UpgradeFromUnit": "GAZ_66_supply_SOV",
    },
    
    "M992A2_supply_US": {},
    
    "M548A2_supply_US": {},
    
    "PTS_2_Naval_supply_SOV": {},

    "PTS_M_supply_POL": {
        "UpgradeFromUnit": "BAV_485_Supply_POL",
    },

     "PTS_M_supply_DDR": {},
    
    # helo supply
    "UH1D_Supply_RFA": {},
    
    "UH1H_supply_US": {},
    
    "UH60A_Supply_US": {},
    
    "Westland_Wessex_supply_UK": {},
    
    "Puma_UK": {},
    
    "Puma_FR": {},
    
    "Mi_8TZ_SOV": {
        "GameName": {
            "display": "Mi-8MT GRUZ.",
        },
    },
    
    "Mi_14PS_supply_SOV": {},
    
    "Mi_8_supply_DDR": {},
    
    "Mi_8_supply_POL": {},
    
    "CH47D_Chinook_supply_UK": {},
    
    "CH47_Super_Chinook_US": {
        "UpgradeFromUnit": "UH60A_Supply_US"
    },
    
    "CH53G_RFA": {},
    
    "CH54B_Tarhe_supply_US": {
        "UpgradeFromUnit": "CH47_Super_Chinook_US",
    },
    
    "Mi_6_POL": {},
    
    "Mi_6_SOV": {
        "GameName": {
            "display": "Mi-6A GRUZ.",
        },
        "UpgradeFromUnit": "Mi_8TZ_SOV"
    },
    
    "Mi_26_SOV": {
        "GameName": {
            "display": "Mi-26 GRUZ.",
        },
        "SupplyCapacity": 4200.0,
        "CommandPoints": 170,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "DvisionalHeloSupply",
        "availability": [2, 0, 0, 0],
    },
}

# --- auto-populate tier values and validate one-offs at import time ---

_logger = setup_logger(__name__)
_REQUIRED_SUPPLY_KEYS = {"SupplyCapacity", "CommandPoints", "Divisions", "SupplyDescriptor", "availability"}

_tiered_unit_names = set()
for _category, _units in SUPPLY_UNITS_BY_TIER.items():
    for _unit_name, _tier in _units:
        _tiered_unit_names.add(_unit_name)
        _tier_config = SUPPLY_TIERS.get(_category, {}).get(_tier)
        if _tier_config is None:
            _logger.warning(f"No tier config for {_unit_name} ({_category}/{_tier})")
            continue
        if _unit_name not in supply_unit_edits:
            supply_unit_edits[_unit_name] = {}
        for _key, _value in _tier_config.items():
            if _key not in supply_unit_edits[_unit_name]:
                supply_unit_edits[_unit_name][_key] = _value

for _unit_name, _edits in supply_unit_edits.items():
    if _unit_name not in _tiered_unit_names:
        _missing = _REQUIRED_SUPPLY_KEYS - set(_edits.keys())
        if _missing:
            _logger.warning(f"One-off supply unit '{_unit_name}' missing required keys: {_missing}")
