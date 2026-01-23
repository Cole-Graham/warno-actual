"""New divisions for Soviet Union."""

sov_new_divs = {
    "SOV_general": {
        "guid": "dd34674c-760f-4fb4-8e04-ea6ecd4e4611",
        "cfg_name": "SOV_national_general",
        "div_name": ("Soviet Union", "RRSXEMSDFX"),
        "div_power": "DC_PWR1",
        "description_title": ("USSR General", "KUQFMFFGRN"),
        "activation_points": 85,
        "combine_divisions": ["SOV_27_Gds_Rifle", "SOV_35_AirAslt_Brig", "SOV_76_VDV", "SOV_119IndTkBrig"],
        "type_texture": "infantryReg",
    },
    "SOV_airborne": {
        "guid": "80713664-b34e-4317-beed-6384e70cb553",
        "cfg_name": "SOV_national_airborne",
        "div_name": ("Soviet Union Airborne", "XWGQUXEHTC"),
        "div_power": "DC_PWR1",
        "description_title": ("USSR Airborne", "MSIEGMOULB"),
        "activation_points": 90,
        "combine_divisions": ["SOV_35_AirAslt_Brig", "SOV_76_VDV"],
        "type_texture": "infantryReg",
    },
}