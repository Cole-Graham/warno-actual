"""DCA AutoCanon weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("DCA_4_canons_APZ23_23mm", "DCA", None, False): { # 274
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 25,
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 2275,
                "TempsDeVisee": 1.25,
            },
        },
    },

    ("DCA_2_canons_2A38M_30mm", "DCA", None, False): { # 262
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
                "Moving": 30,
            },
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2625,
                "PorteeMaximaleHAGRU": 2450,
                "TempsDeVisee": 1.25,
            },
        },
    },

    ("DCA_2_canon_ZU23_2_23mm_TOWED", "DCA", None, False): { # 261
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleGRU": 1225,
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 1.25,
            },
        },
    },

    ("DCA_2_canon_ZU23_2_23mm", "DCA", None, False): { # 260
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleGRU": 1225,
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 1.25,
            },
        },
    },

    ("DCA_2_canon_Jod_SP_23mm", "DCA", None, False): { # ???
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleGRU": 1225,
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 1.25,
            },
        },
    },

    ("DCA_2_canon_Jod_towed_23mm", "DCA", None, False): { # ???
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleGRU": 1225,
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 1925,
                "TempsDeVisee": 1.25,
            },
        },
    },
}
# fmt: on
