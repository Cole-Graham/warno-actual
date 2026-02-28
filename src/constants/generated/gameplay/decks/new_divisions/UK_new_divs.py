"""New divisions for UK."""

from .new_divisionrules import (
    UK_airborne_newdivisionrules,
    UK_armored_newdivisionrules,
    UK_global_newdivisionrules,
    # UK_marine_newdivisionrules,
    UK_mechanized_newdivisionrules,
    UK_motorized_newdivisionrules,
)

uk_new_divs = {
    "UK_general": {
        "division_id": 5017,
        "interface_order": 1050,
        "guid": "6ca2b6dc-bfbf-4389-9b97-13bc547feec0",
        "cfg_name": "UK_national_general",
        "div_name": ("UK", "DZKSDGNWEW"),
        "description_title": ("UK", "ZDARYIGJHE"),
        "summary_text": ("UK combined arms division.", "SUMUKGEN"),
        "history_text": ("UK national division.", "HISUKGEN"),
        "activation_points": 75,
        "standout_units": ["Challenger_1_Mk1_UK", "MCV_80_Warrior_UK", "Paratroopers_UK"],
        "division_rules": [
            UK_airborne_newdivisionrules,
            UK_armored_newdivisionrules,
            UK_global_newdivisionrules,
            UK_mechanized_newdivisionrules,
            UK_motorized_newdivisionrules,
        ],
        "rule_exclusions": [
            "HMGteam_M2HB_UK",
            "HMGteam_MAG_UK",
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 3, 3, 3, 3, 3],
        },
        "transport_overrides": {
            "Rifles_CMD2_UK": ["LandRover_UK", "FV432_UK", "MCV_80_Warrior_UK", "MCV_80_Warrior_MILAN_UK", "Lynx_AH_Mk1_UK", "Westland_Wessex_trans_UK"],
            "Gun_Group_UK": ["LandRover_UK", "FV432_SCAT_UK", "FV432_MILAN_UK", "MCV_80_Warrior_UK", "MCV_80_Warrior_MILAN_UK", "MCV_80_Warrior_MILAN_ERA_UK"],
            "LRRP_UK": ["LandRover_UK", "LandRover_Yeoman_UK", "Lynx_AH_Mk1_UK", "Lynx_AH_Mk7_SNEB_UK"],
        },
    },
    "UK_airborne": {
        "division_id": 5018,
        "interface_order": 1051,
        "guid": "cea9f13f-c1dc-46a2-84b0-20ada26427a8",
        "cfg_name": "UK_national_airborne",
        "div_name": ("UK Airborne", "GVGUREJCOJ"),
        "description_title": ("UK Airborne", "KAPLZCHEMU"),
        "summary_text": ("UK airborne division.", "SUMUKAIR"),
        "history_text": ("UK Airborne division.", "HISUKAIR"),
        "activation_points": 100,
        "standout_units": ["Paratroopers_UK", "FV101_Scorpion_para_UK", "Lynx_AH_Mk7_I_TOW_UK"],
        "division_rules": [
            UK_airborne_newdivisionrules,
            UK_global_newdivisionrules,
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 2, 3, 3, 3, 3],
        },
    },
    # airborne_marine 5019, 1052
    "UK_airborne_armored": {
        "division_id": 5020,
        "interface_order": 1053,
        "guid": "78a8c263-0b43-4906-b896-261c02ec51ac",
        "cfg_name": "UK_national_airborne_armored",
        "div_name": ("UK Airborne / Armored", "IQWVGFUNHZ"),
        "description_title": ("UK Airborne / Armored", "CQAQYRDQXE"),
        "summary_text": ("UK airborne and armored division.", "SUMUKAARM"),
        "history_text": ("UK Airborne / Armored division.", "HISUKAARM"),
        "activation_points": 85,
        "standout_units": ["Paratroopers_UK", "FV4201_Chieftain_Mk9_UK", "FV101_Scorpion_para_UK"],
        "division_rules": [
            UK_airborne_newdivisionrules,
            UK_armored_newdivisionrules,
            UK_global_newdivisionrules,
        ],
        "rule_exclusions": [
            "HMGteam_M2HB_UK",
            "HMGteam_MAG_UK",
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 3, 3, 3, 3, 3],
        },
    },
    "UK_airborne_mechanized": {
        "division_id": 5021,
        "interface_order": 1054,
        "guid": "88bbc172-b591-4395-b209-f74c11094792",
        "cfg_name": "UK_national_airborne_mechanized",
        "div_name": ("UK Airborne / Mechanized", "HRWRXWGYXN"),
        "description_title": ("UK Airborne / Mechanized", "QYZEUWAJVA"),
        "summary_text": ("UK airborne and mechanized division.", "SUMUKAMEC"),
        "history_text": ("UK Airborne / Mechanized division.", "HISUKAMEC"),
        "activation_points": 85,
        "standout_units": ["Paratroopers_UK", "MCV_80_Warrior_UK", "FV101_Scorpion_para_UK"],
        "division_rules": [
            UK_airborne_newdivisionrules,
            UK_global_newdivisionrules,
            UK_mechanized_newdivisionrules,
        ],
        "rule_exclusions": [
            "HMGteam_M2HB_UK",
            "HMGteam_MAG_UK",
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 3, 3, 3, 3, 3],
        },
        "transport_overrides": {
            "Rifles_CMD2_UK": ["LandRover_UK", "FV432_UK", "MCV_80_Warrior_UK", "MCV_80_Warrior_MILAN_UK", "Lynx_AH_Mk1_UK", "Westland_Wessex_trans_UK"],
        },
    },
    "UK_airborne_motorized": {
        "division_id": 5022,
        "interface_order": 1055,
        "guid": "a77f88e7-a344-49e1-885a-78cb9792b07d",
        "cfg_name": "UK_national_airborne_motorized",
        "div_name": ("UK Airborne / Motorized", "YHBYLGXCRV"),
        "description_title": ("UK Airborne / Motorized", "CBBGSQDTUR"),
        "summary_text": ("UK airborne and motorized division.", "SUMUKAMOT"),
        "history_text": ("UK Airborne / Motorized division.", "HISUKAMOT"),
        "activation_points": 85,
        "standout_units": ["Paratroopers_UK", "Saxon_UK", "LandRover_UK"],
        "division_rules": [
            UK_airborne_newdivisionrules,
            UK_global_newdivisionrules,
            UK_motorized_newdivisionrules,
        ],
        "rule_exclusions": [
            "HMGteam_M2HB_UK",
            "HMGteam_MAG_UK",
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 2, 3, 3, 3, 3],
        },
    },
    "UK_armored": {
        "division_id": 5023,
        "interface_order": 1056,
        "guid": "e69cee42-dee6-49bc-a088-de332ae3629f",
        "cfg_name": "UK_national_armored",
        "div_name": ("UK Armored", "ORZGPUEMBG"),
        "description_title": ("UK Armored", "WLGANPMFZK"),
        "summary_text": ("UK armored division.", "SUMUKARM"),
        "history_text": ("UK Armored division.", "HISUKARM"),
        "activation_points": 100,
        "standout_units": ["Challenger_1_Mk1_UK", "MCV_80_Warrior_UK", "FV438_Swingfire_UK"],
        "division_rules": [
            UK_armored_newdivisionrules,
            UK_global_newdivisionrules,
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 3, 3, 3, 3, 3],
        },
    },
    # armored_marine 5024, 1057
    "UK_armored_mechanized": {
        "division_id": 5025,
        "interface_order": 1058,
        "guid": "60d6e0ab-c9d7-4d37-9fc8-51b49b2f23fc",
        "cfg_name": "UK_national_armored_mechanized",
        "div_name": ("UK Armored / Mechanized", "WGQDHNQWMG"),
        "description_title": ("UK Armored / Mechanized", "QWLFDPBANW"),
        "summary_text": ("UK armored and mechanized division.", "SUMUKARMC"),
        "history_text": ("UK Armored / Mechanized division.", "HISUKARMC"),
        "activation_points": 85,
        "standout_units": ["Challenger_1_Mk1_UK", "MCV_80_Warrior_UK", "Rifles_UK"],
        "division_rules": [
            UK_armored_newdivisionrules,
            UK_global_newdivisionrules,
            UK_mechanized_newdivisionrules,
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 3, 3, 3, 3, 3],
        },
    },
    "UK_armored_motorized": {
        "division_id": 5026,
        "interface_order": 1059,
        "guid": "243bd49d-b2b1-4e5d-a412-e7888884cdda",
        "cfg_name": "UK_national_armored_motorized",
        "div_name": ("UK Armored / Motorized", "JLQJBAEBFF"),
        "description_title": ("UK Armored / Motorized", "HCDNSEBVUL"),
        "summary_text": ("UK armored and motorized division.", "SUMUKARMT"),
        "history_text": ("UK Armored / Motorized division.", "HISUKARMT"),
        "activation_points": 85,
        "standout_units": ["Challenger_1_Mk1_UK", "Saxon_UK", "FV4201_Chieftain_UK"],
        "division_rules": [
            UK_armored_newdivisionrules,
            UK_global_newdivisionrules,
            UK_motorized_newdivisionrules,
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 3, 3, 3, 3, 3],
        },
        "transport_overrides": {
            "Rifles_CMD2_UK": ["LandRover_UK", "FV432_UK", "MCV_80_Warrior_UK", "MCV_80_Warrior_MILAN_UK", "Lynx_AH_Mk1_UK", "Westland_Wessex_trans_UK"],
        },
    },
    # marine 5027, 1060
    # marine_mechanized 5028, 1061
    # marine_motorized 5029, 1062
    "UK_mechanized": {
        "division_id": 5031,
        "interface_order": 1063,
        "guid": "43436e18-7807-45b9-b315-2d9ba601a8e1",
        "cfg_name": "UK_national_mechanized",
        "div_name": ("UK Mechanized", "VOQUBOBJGC"),
        "description_title": ("UK Mechanized", "HLESWTHTAV"),
        "summary_text": ("UK mechanized division.", "SUMUKMEC"),
        "history_text": ("UK Mechanized division.", "HISUKMEC"),
        "activation_points": 100,
        "standout_units": ["MCV_80_Warrior_UK", "FV432_UK", "Rifles_UK"],
        "division_rules": [
            UK_global_newdivisionrules,
            UK_mechanized_newdivisionrules,
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 2, 3, 3, 3, 3],
        },
    },
    "UK_mechanized_motorized": {
        "division_id": 5032,
        "interface_order": 1064,
        "guid": "8a487fdc-bcd1-46b6-9d5c-c50df2d26fb3",
        "cfg_name": "UK_national_mechanized_motorized",
        "div_name": ("UK Mechanized / Motorized", "GYGDEZWQDD"),
        "description_title": ("UK Mechanized / Motorized", "RZDEWSAWMI"),
        "summary_text": ("UK mechanized and motorized division.", "SUMUKMECT"),
        "history_text": ("UK Mechanized / Motorized division.", "HISUKMECT"),
        "activation_points": 85,
        "standout_units": ["MCV_80_Warrior_UK", "FV432_UK", "Saxon_UK"],
        "division_rules": [
            UK_global_newdivisionrules,
            UK_mechanized_newdivisionrules,
            UK_motorized_newdivisionrules,
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 3, 3, 3, 3, 3],
        },
    },
    "UK_motorized": {
        "division_id": 5033,
        "interface_order": 1065,
        "guid": "d9dc821a-3417-45b0-8db1-01e3f45132d6",
        "cfg_name": "UK_national_motorized",
        "div_name": ("UK Motorized", "LYFYYREQUL"),
        "description_title": ("UK Motorized", "HZJLHETVPY"),
        "summary_text": ("UK motorized division.", "SUMUKMOT"),
        "history_text": ("UK Motorized division.", "HISUKMOT"),
        "activation_points": 100,
        "standout_units": ["Saxon_UK", "Guards_UK", "FV4201_Chieftain_UK"],
        "division_rules": [
            UK_motorized_newdivisionrules,
            UK_global_newdivisionrules,
        ],
        "matrix_overrides": {
            "EFactory/Logistic": [2, 2, 2, 2, 2, 3, 3, 3, 3],
        },
    },
}