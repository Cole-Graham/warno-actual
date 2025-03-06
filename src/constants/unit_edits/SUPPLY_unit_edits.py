"""supply unit edits."""

# from typing import Any, Dict

# fmt: off
supply_unit_edits = {
    # motorised supply
    "M274_Mule_supply_US": {
        "SupplyCapacity": 500.0,
        "CommandPoints": 20,
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
        "CommandPoints": 20,
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
        "CommandPoints": 20,
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
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SupplyDescriptor": "RunnerSupply",
        "availability": [8, 0, 0, 0],
    },
    "Gama_Goat_supply_US": {
        "SupplyCapacity": 675.0,
        "CommandPoints": 30,
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
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [6, 0, 0, 0],
    },
    "Unimog_S_404_RFA": {
        "SupplyCapacity": 850.0,
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [4, 0, 0, 0],
    },
    "GAZ_66_supply_SOV": {
        "SupplyCapacity": 850.0,
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [4, 0, 0, 0],
    },
    "GAZ_66_POL": {
        "SupplyCapacity": 850.0,
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [4, 0, 0, 0],
    },
    "VLRA_supply_FR": {
        "SupplyCapacity": 850.0,
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [4, 0, 0, 0],
    },
    "TRM_2000_supply_FR": {
        "SupplyCapacity": 850.0,
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [4, 0, 0, 0],
    },
    "M35_supply_US": {
        "SupplyCapacity": 1250.0,
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimarySupply",
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
    "T813_DDR": {
        "SupplyCapacity": 2000.0,
        "CommandPoints": 65,
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
        "CommandPoints": 65,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "PrimarySupply",
        "availability": [2, 0, 0, 0],
    },
    "M812_Supply_US": {
        "SupplyCapacity": 2000.0,
        "CommandPoints": 65,
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
        "CommandPoints": 70,
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
        "CommandPoints": 70,
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
        "CommandPoints": 85,
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
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [4, 0, 0, 0],
    },
    "M113A2_supply_US": {
        "SupplyCapacity": 925.0,
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [4, 0, 0, 0],
    },
    "MTLB_supply_DDR": {
        "SupplyCapacity": 925.0,
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [4, 0, 0, 0],
    },
    "MTLB_supply_SOV": {
        "SupplyCapacity": 925.0,
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SupplyDescriptor": "SquadSupply",
        "availability": [4, 0, 0, 0],
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
        "availability": [3, 0, 0, 0],
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
        "availability": [4, 0, 0, 0],
    },
    "Mi_8TZ_SOV": {
        "SupplyCapacity": 1100.0,
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
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
        "availability": [3, 0, 0, 0],
    },
    "CH47D_Chinook_supply_UK": {
        "SupplyCapacity": 2000.0,
        "CommandPoints": 80,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [3, 0, 0, 0],
    },
    "CH47_Super_Chinook_US": {
        "SupplyCapacity": 2400.0,
        "CommandPoints": 80,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [3, 0, 0, 0],
    },
    "CH53G_RFA": {
        "SupplyCapacity": 2400.0,
        "CommandPoints": 80,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [3, 0, 0, 0],
    },
    "Mi_6_POL": {
        "SupplyCapacity": 3000.0,
        "CommandPoints": 130,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [2, 0, 0, 0],
    },
    "Mi_6_SOV": {
        "SupplyCapacity": 3000.0,
        "CommandPoints": 130,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [2, 0, 0, 0],
    },
    "Mi_26_SOV": {
        "SupplyCapacity": 4200.0,
        "CommandPoints": 190,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [2, 0, 0, 0],
    },
}
