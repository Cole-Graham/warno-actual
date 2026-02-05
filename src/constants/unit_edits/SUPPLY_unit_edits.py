"""supply unit edits."""

# from typing import Any, Dict

# fmt: off
supply_unit_edits = {
    # motorised supply
    "M274_Mule_supply_US": {
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
    
    "UAZ_469_supply_SOV": {
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
    
    "UAZ_469_supply_VDV_SOV": {
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
    
    "LUAZ_967M_supply_SOV": {
        "SupplyCapacity": 500,
        "CommandPoints": 15,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SupplyDescriptor": "RunnerSupply",
        "availability": [8, 0, 0, 0],
    },
    
    "UAZ_469_supply_Para_POL": {  # Desant. UAZ-469 Zaop.
        "SupplyCapacity": 500.0,
        "CommandPoints": 15,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SupplyDescriptor": "RunnerSupply",
        "availability": [8, 0, 0, 0],
        "GameName": {
            "display": "SPADO. UAZ-469 ZAOP.",
        },
    },
    
    "Gama_Goat_supply_US": {
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
    
    "CUCV_US": {
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
    
    "Rover_101FC_supply_UK": {
        "SupplyCapacity": 675.0,
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [6, 0, 0, 0],
        "tow_only": None,
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "SpecialtiesList": {
            "add_specs": ["'_transport2'"],
        },
    },
    
    "Unimog_S_404_RFA": {
        "SupplyCapacity": 850.0,
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [5, 0, 0, 0],
        "tow_only": None,
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "SpecialtiesList": {
            "add_specs": ["'_transport2'"],
        },
    },
    
    "GAZ_66_supply_SOV": {
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
    
    "GAZ_66_POL": {
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
    
    "GAZ_66B_supply_POL": {  # GAZ-66B Zaop.
        "GameName": {
            "display": "SPADO. GAZ-66B ZAOP.",
        },
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
    
    "VLRA_supply_FR": {
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
    
    "TRM_2000_supply_FR": {
        "SupplyCapacity": 850.0,
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [5, 0, 0, 0],
    },
    
    "M35_supply_US": {
        "SupplyCapacity": 1250.0,
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimarySupply",
        "tow_only": None,
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "SpecialtiesList": {
            "add_specs": ["'_transport2'"],
        },
        "availability": [3, 0, 0, 0],
    },
    
    "Ural_4320_DDR": {
        "SupplyCapacity": 1750.0,
        "CommandPoints": 55,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimarySupply",
        "availability": [2, 0, 0, 0],
    },
    
    "Ural_4320_SOV": {
        "SupplyCapacity": 1750.0,
        "CommandPoints": 55,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimarySupply",
        "availability": [2, 0, 0, 0],
    },
    
    "Star_266_supply_POL": {
        "SupplyCapacity": 1750.0,
        "CommandPoints": 55,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimarySupply",
        "availability": [2, 0, 0, 0],
        "UpgradeFromUnit": "GAZ_66B_supply_POL",
    },
    
    "Bedford_MJ_4t_UK": {
        "SupplyCapacity": 1750.0,
        "CommandPoints": 55,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimarySupply",
        "availability": [2, 0, 0, 0],
    },
    
    "Alvis_Stalwart_UK": {
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
    
    "M812_supply_US": { # M813A1 SUPPLY
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
    
    "T813_DDR": {
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
    
    "KrAZ_255B_supply_SOV": {
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
    
    "KrAZ_255B_supply_POL": {
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
    
    "MAN_Kat_6x6_RFA": {
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
    
    "T815_supply_DDR": {
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
    
    "HEMTT_US": {
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
    
    # mechanized supply
    "M113A1G_supply_RFA": {
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
    
    "M113A2_supply_US": {
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
    
    "MTLB_supply_DDR": {
        "GameName": {
            "display": "MT-LB MUN.",
        },
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
    
    "MTLB_supply_SOV": {
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
    
    "M548A2_supply_US": {
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
    
    # helo supply
    "UH1D_Supply_RFA": {
        "SupplyCapacity": 500.0,
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "RunnerHeloSupply",
        "availability": [7, 0, 0, 0],
        "is_small": True,
    },
    
    "UH1H_supply_US": {
        "SupplyCapacity": 500.0,
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "RunnerHeloSupply",
        "availability": [7, 0, 0, 0],
        "is_small": True,
    },
    
    "UH60A_Supply_US": {
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
    
    "Puma_UK": {
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
    
    "Puma_FR": {
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
    
    "Mi_8TZ_SOV": {
        "GameName": {
            "display": "Mi-8MT GRUZ.",
        },
        "SupplyCapacity": 1100.0,
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimaryHeloSupply",
        "availability": [3, 0, 0, 0],
    },
    
    "Mi_8_supply_DDR": {
        "SupplyCapacity": 1100.0,
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimaryHeloSupply",
        "availability": [3, 0, 0, 0],
    },
    
    "Mi_8_supply_POL": {
        "SupplyCapacity": 1100.0,
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimaryHeloSupply",
        "availability": [3, 0, 0, 0],
    },
    
    "CH47D_Chinook_supply_UK": {
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
    
    "CH47_Super_Chinook_US": {
        "SupplyCapacity": 2400.0,
        "CommandPoints": 95,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "DvisionalHeloSupply",
        "availability": [2, 0, 0, 0],
        "UpgradeFromUnit": "UH60A_Supply_US"
    },
    
    "CH53G_RFA": {
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
    
    "CH54B_Tarhe_supply_US": {
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
    
    "Mi_6_POL": {
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
    
    "Mi_6_SOV": {
        "GameName": {
            "display": "Mi-6A GRUZ.",
        },
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
