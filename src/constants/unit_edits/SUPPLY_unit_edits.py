"""supply unit edits."""

# from typing import Any, Dict

# fmt: off
from re import M

from src.utils.logging_utils import setup_logger


SUPPLY_TIERS = {
    "wheeled": {
        "tier_1": {
            "Supply": {
                "SupplyCapacity": 500.0,
                "SupplyDescriptor": "RunnerSupply",
            },
            "CommandPoints": 15,
            "Divisions": {
                "default": {
                    "cards": 1,
                },
            },
            "availability": [8, 0, 0, 0],
        },
        "tier_2": {
            "Supply": {
                "SupplyCapacity": 675.0,
                "SupplyDescriptor": "SquadSupply",
            },
            "CommandPoints": 25,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [6, 0, 0, 0],
        },
        "tier_3": {
            "Supply": {
                "SupplyCapacity": 850.0,
                "SupplyDescriptor": "SquadSupply",
            },
            "CommandPoints": 35,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [5, 0, 0, 0],
        },
        "tier_4": {
            "Supply": {
                "SupplyCapacity": 1300.0,
                "SupplyDescriptor": "PrimarySupply",
            },
            "CommandPoints": 40,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [3, 0, 0, 0],
        },
        "tier_5": {
            "Supply": {
                "SupplyCapacity": 1500.0,
                "SupplyDescriptor": "PrimarySupply",
            },
            "CommandPoints": 55,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [3, 0, 0, 0],
        },
        "tier_6": {
            "Supply": {
                "SupplyCapacity": 2000.0,
                "SupplyDescriptor": "PrimarySupply",
            },
            "CommandPoints": 70,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [2, 0, 0, 0],
        },
        "tier_7": {
            "Supply": {
                "SupplyCapacity": 2300.0,
                "SupplyDescriptor": "DvisionalSupply",
            },
            "CommandPoints": 80,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [2, 0, 0, 0],
        },
        "tier_8": {
            "Supply": {
                "SupplyCapacity": 2750.0,
                "SupplyDescriptor": "DvisionalSupply",
            },
            "CommandPoints": 90,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [2, 0, 0, 0],
        },
    },
    
    "mechanized": {
        "tier_1": {
            "Supply": {
                "SupplyCapacity": 925.0,
                "SupplyDescriptor": "SquadSupply",
            },
            "CommandPoints": 30,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [6, 0, 0, 0],
        },
        "tier_2": {
            "Supply": {
                "SupplyCapacity": 1400.0,
                "SupplyDescriptor": "PrimarySupply",
            },
            "CommandPoints": 45,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [4, 0, 0, 0],
        },
        "tier_3": {
            "Supply": {
                "SupplyCapacity": 1600.0,
                "SupplyDescriptor": "PrimarySupply",
            },
            "CommandPoints": 55,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [4, 0, 0, 0],
        },
        "tier_4": {
            "Supply": {
                "SupplyCapacity": 2300.0,
                "SupplyDescriptor": "DvisionalSupply",
            },
            "CommandPoints": 75,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [3, 0, 0, 0],
        },
    },
    
    "helicopter": {
        "tier_1": {
            "Supply": {
                "SupplyCapacity": 500.0,
                "SupplyDescriptor": "RunnerHeloSupply",
            },
            "CommandPoints": 25,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [7, 0, 0, 0],
        },
        "tier_2": {
            "Supply": {
                "SupplyCapacity": 750.0,
                "SupplyDescriptor": "PrimaryHeloSupply",
            },
            "CommandPoints": 40,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [5, 0, 0, 0],
        },
        "tier_3": {
            "Supply": {
                "SupplyCapacity": 850.0,
                "SupplyDescriptor": "PrimaryHeloSupply",
            },
            "CommandPoints": 45,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [4, 0, 0, 0],
        },
        "tier_4": {
            "Supply": {
                "SupplyCapacity": 1100.0,
                "SupplyDescriptor": "PrimaryHeloSupply",
            },
            "CommandPoints": 55,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [3, 0, 0, 0],
        },
        "tier_5": {
            "Supply": {
                "SupplyCapacity": 2400.0,
                "SupplyDescriptor": "DvisionalHeloSupply",
            },
            "CommandPoints": 95,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
            "availability": [2, 0, 0, 0],
        },
        "tier_6": {
            "Supply": {
                "SupplyCapacity": 3000.0,
                "SupplyDescriptor": "DvisionalHeloSupply",
            },
            "CommandPoints": 130,
            "Divisions": {
                "default": {
                    "cards": 2,
                },
            },
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

        # tier 4
        ("CH46E_SeaKnight_supply_US", "tier_4"),
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

_SUPPLY_TOW_CAPABLE_EDITS = {
    "tow_only": True,
    "orders": {
        "add_orders": [
            "EOrderType/UnloadFromTransport",
            "EOrderType/UnloadAtPosition",
            "EOrderType/Load",
        ],
    },
    "SpecialtiesList": {
        "add_specs": ["'_transport2'"],
    },
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
    
    "CUCV_US": {
        "GameName": {
            "display": "#TRANSTWO M1008 CUCV SUPPLY",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
    "Rover_101FC_supply_UK": {
        "GameName": {
            "display": "#TRANSTWO ROVER 101FC SUPPLY",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },

    "LAV_L_US": {
        "GameName": {
            "display": "#TRANSTWO USMC LAV-L",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
    "Unimog_S_404_RFA": {
        "GameName": {
            "display": "#TRANSTWO UNIMOG S404 MÜN.",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
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
        "UpgradeFromUnit": "GAZ_66B_supply_POL",
    },

    "VLRA_supply_FR": {},
    
    "TRM_2000_supply_FR": {
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
    "M35_supply_US": {
        "GameName": {
            "display": "#TRANSTWO M35 SUPPLY",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
    "Ural_4320_DDR": {},
    
    "Ural_4320_SOV": {
        "UpgradeFromUnit": "MTLB_supply_SOV",
    },
    
    "ZIL_131_supply_Naval_SOV": {},
    
    "Star_266_supply_POL": {
        "UpgradeFromUnit": "BAV_485_Supply_POL",
    },

    "Berliet_GBC_8KT_supply_FR": {},
    
    "Bedford_MJ_4t_UK": {
        "GameName": {
            "display": "#TRANSTWO BEDFORD MJ SUPPLY",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
    "Alvis_Stalwart_UK": {},

    "DaimlerBenz_Typ1017_supply_RFA": {
        "GameName": {
            "display": "#TRANSTWO MB 1017 MÜN.",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },

    "Berliet_GBU_15_supply_FR": {},
    
    "M812_supply_US": { # M813A1 SUPPLY
        "GameName": {
            "display": "#TRANSTWO M813A1 SUPPLY",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
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
        "GameName": {
            "display": "#TRANSTWO KRAS-255B GRUZ.",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
        "UpgradeFromUnit": "MAZ_535A_supply_SOV",
    },
    
    "KrAZ_255B_supply_POL": {},

    "KrAZ_255B_supply_DDR": {},
    
    "AEC_Militant_UK": {
        "GameName": {
            "display": "#TRANSTWO MILITANT Mk.3",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
    "MAN_Kat_6x6_RFA": {
        "GameName": {
            "display": "#TRANSTWO MAN KAT 6x6 MÜN.",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
    "T815_supply_DDR": {},
    
    "HEMTT_US": {
        "GameName": {
            "display": "#TRANSTWO HEMTT",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
    "Bedford_TM_6x6_supply_UK": {
        "GameName": {
            "display": "#TRANSTWO BEDFORD TM SUPPLY",
        },
        **_SUPPLY_TOW_CAPABLE_EDITS,
    },
    
    "Kalmar_supply_SOV": {
        "CommandPoints": 220,
        "Supply": {
            "SupplyCapacity": 8400.0,
            "SupplyDescriptor": "DvisionalSupply",
        },
        "availability": [1, 0, 0, 0],
         "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    },

    "LARC_60_supply_US": {
        "CommandPoints": 220,
        "Supply": {
            "SupplyCapacity": 8400.0,
            "SupplyDescriptor": "DvisionalSupply",
        },
        "availability": [1, 0, 0, 0],
         "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "UpgradeFromUnit": "LAV_L_US",
    }, 
    
    # mechanized supply
    "M113A1G_supply_RFA": {
        "GameName": {
            "display": "M113A1 MÜN.",
        },
    },
    
    "M113A2_supply_US": {
        "GameName": {
            "display": "M113A2 SUPPLY",
        },
        "UpgradeFromUnit": "M1038_Humvee_supply_US",
    },
    
    "FV432_supply_UK": {
        "GameName": {
            "display": "FV432 CARGO",
        },
    },
    
    "MTLB_supply_DDR": {
        "GameName": {
            "display": "MT-LB MÜN.",
        },
    },
    
    "MTLB_supply_SOV": {
        "UpgradeFromUnit": "GAZ_66_supply_SOV",
    },
    
    "M992A2_supply_US": {
        "GameName": {
            "display": "M992A2",
        },
    },
    
    "M548A2_supply_US": {
        "GameName": {
            "display": "M548A2",
        },
    },
    
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
        "Supply": {
            "SupplyCapacity": 4200.0,
            "SupplyDescriptor": "DvisionalHeloSupply",
        },
        "CommandPoints": 170,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [2, 0, 0, 0],
    },
}

# --- auto-populate tier values and validate one-offs at import time ---

_logger = setup_logger(__name__)
_REQUIRED_UNIT_KEYS = {"CommandPoints", "Divisions", "availability", "Supply"}
_REQUIRED_SUPPLY_MODULE_KEYS = {"SupplyCapacity", "SupplyDescriptor"}

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
            if _key == "Supply":
                supply_unit_edits[_unit_name].setdefault("Supply", {})
                for _sk, _sv in _value.items():
                    if _sk not in supply_unit_edits[_unit_name]["Supply"]:
                        supply_unit_edits[_unit_name]["Supply"][_sk] = _sv
            elif _key not in supply_unit_edits[_unit_name]:
                supply_unit_edits[_unit_name][_key] = _value

for _unit_name, _edits in supply_unit_edits.items():
    if _unit_name not in _tiered_unit_names:
        _missing = _REQUIRED_UNIT_KEYS - set(_edits.keys())
        if _missing:
            _logger.warning(f"One-off supply unit '{_unit_name}' missing required keys: {_missing}")
        else:
            _supply_missing = _REQUIRED_SUPPLY_MODULE_KEYS - set(_edits.get("Supply", {}).keys())
            if _supply_missing:
                _logger.warning(
                    f"One-off supply unit '{_unit_name}' missing required Supply keys: {_supply_missing}",
                )
