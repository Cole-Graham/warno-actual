"""Unit trait and specialty constants."""

from src.constants import NEW_SUPPLY_CONSTANTS

runner_configs = NEW_SUPPLY_CONSTANTS["RunnerSupply"]
for key, value in runner_configs.items():
    if key == "DefaultSupplyRangeGRU":
        if value == "SpecificDefaultSupplyRangeGRU":
            runner_range = "450"
        else:
            runner_range = value
    elif key == "FuelSupplyBySecond":
        runner_fuel = value * 30
        runner_fuel_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""
    elif key == "HealthSupplyBySecond":
        runner_health = float(value/10)
        runner_health_percentage = f"({int(value * 100/2)}%)" if value != 2.0 else ""
    elif key == "AmmunitionSupplyBySecond":
        runner_ammo = value * 60
        runner_ammo_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""
    elif key == "CriticsSupplyBySecond":
        runner_critics = value * 10
        runner_critics_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""

squad_configs = NEW_SUPPLY_CONSTANTS["SquadSupply"]
for key, value in squad_configs.items():
    if key == "DefaultSupplyRangeGRU":
        if value == "SpecificDefaultSupplyRangeGRU":
            squad_range = "450"
        else:
            squad_range = value
    elif key == "FuelSupplyBySecond":
        squad_fuel = value * 30
        squad_fuel_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""
    elif key == "HealthSupplyBySecond":
        squad_health = float(value/10)
        squad_health_percentage = f"({int(value * 100/2)}%)" if value != 2.0 else ""
    elif key == "AmmunitionSupplyBySecond":
        squad_ammo = value * 60
        squad_ammo_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""
    elif key == "CriticsSupplyBySecond":
        squad_critics = value * 10
        squad_critics_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""

primary_configs = NEW_SUPPLY_CONSTANTS["PrimarySupply"]
for key, value in primary_configs.items():
    if key == "DefaultSupplyRangeGRU":
        if value == "SpecificDefaultSupplyRangeGRU":
            primary_range = "450"
        else:
            primary_range = value
    elif key == "FuelSupplyBySecond":
        primary_fuel = value * 30
        primary_fuel_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""
    elif key == "HealthSupplyBySecond":
        primary_health = float(value/10)
        primary_health_percentage = f"({int(value * 100/2)}%)" if value != 2.0 else ""
    elif key == "AmmunitionSupplyBySecond":
        primary_ammo = value * 60
        primary_ammo_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""
    elif key == "CriticsSupplyBySecond":
        primary_critics = value * 10
        primary_critics_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""

divisional_configs = NEW_SUPPLY_CONSTANTS["DvisionalSupply"] # Dvisional because 'Div' is reserved in NDF
for key, value in divisional_configs.items():
    if key == "DefaultSupplyRangeGRU":
        if value == "SpecificDefaultSupplyRangeGRU":
            divisional_range = "450"
        else:
            divisional_range = value
    elif key == "FuelSupplyBySecond":
        divisional_fuel = value * 30
        divisional_fuel_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""
    elif key == "HealthSupplyBySecond":
        divisional_health = float(value/10)
        divisional_health_percentage = f"({int(value * 100/2)}%)" if value != 2.0 else ""
    elif key == "AmmunitionSupplyBySecond":
        divisional_ammo = value * 60
        divisional_ammo_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""
    elif key == "CriticsSupplyBySecond":
        divisional_critics = value * 10
        divisional_critics_percentage = f"({int(value * 100)}%)" if value != 1.0 else ""   


NEW_TRAITS = {
    "good_airoptics": {
        "title": ("QVLGHFHGMX", "Good Air Detection"),
        "description": ("XFHVTROSUP", (
            f"This unit has good optics for detecting aircraft, and can spot them from a "
            f"greater distance than most units. (7200m)"
        )),
        "texture": "good_airoptics.png",
    },

    "verygood_airoptics": {
        "title": ("LEJTSAZONO", "Very Good Air Detection"),
        "description": ("CPCAOEUBMO", (
            f"This unit has a powerful radar for detecting aircraft, and can spot them "
            f"from a greater distance than most units. (9200m)"
        )),
        "texture": "verygood_airoptics.png",
    },

    "infantry_equip_light": {
        "title": ("KLFMLCXTLI", "Light Equipment"),
        "description": ("NQPICCWPZM", (
            f"These infantry are lightly equipped, allowing them to move quickly and "
            f"reposition easily on the battlefield."
        )),
        "texture": "light_equipment.png",
    },
    
    "infantry_equip_medium": {
        "title": ("PWXOBNIDQC", "Medium Equipment"),
        "description": ("GUPAGRZAWI", (
            f"These infantry are moderately equipped, and while just as mobile, "
            f"carry less ammunition than their light counterparts."
        )),
        "texture": "medium_equipment.png",
    },
    
    "infantry_equip_heavy": {
        "title": ("CAOTQXVHXH", "Heavy Equipment"),
        "description": ("XLMSCEWDLB", (
            f"These infantry are burdened by powerful yet heavy equipment, "
            f"hampering their mobility on the battlefield."
        )),
        "texture": "heavy_equipment.png",
    },
    
    "infantry_equip_veryheavy": {
        "title": ("AXLDYZOVCJ", "Immobile Weapon Systems"),
        "description": ("DJTBXQWLVR", (
            f"These infantry employ heavy weapons meant for defending entrenched "
            f"positions. Keep a transport nearby if you foresee the need to "
            f"reposition this unit in a hurry, and be proactive about avoiding "
            f"enemy artillery if their position is revealed."
        )),
        "texture": "veryheavy_equipment.png",
    },
    
    "cmd_small": { # blufor leader text script texture (#LDR)
        "title": (None, None),
        "description": (None, (
            None
        )),
        "texture": "cmd_small.png",
    },

    "leader_sov": { # redfor leader trait texture
        "title": ("YNKZWZNLDT", None),
        "description": ("REIDQXMIMJ", (
            None
        )),
        "extended": ("CSUKPTRVAR", (
            None
        )),
        "texture": "cmd_star.png",
    },

    "cmd_star_small": { # redfor leader text script texture (#SOVLDR)
        "title": (None, None),
        "description": (None, (
            None
        )),
        "texture": "cmd_star_small.png",
    },

    "refundable_unit": {
        "title": ("WBMGTMRGUA", "Refundable"),
        "description": ("YYNHOSCAII", (
            f"This transport can be sold for 100% of its cost, and is priced to a higher "
            f"standard than IFVs and heavily armed APCs. Its armaments (if any) are not "
            f"intended to be cost effective when employed offensively, but they can be "
            f"used sparingly as a defensive tool or as a last resort."
        )),
        "texture": "refundable.png",
    },
    
    "dive_attack": {
        "title": ("ZQFMDKRRNG", "Dive Attack"),
        "description": ("NHDOKPRKOY", (
            f"This fighter bomber will dive to achieve maximum accuracy, but will be more "
            f"vulnerable to enemy fire."
        )),
        "texture": "dive_strategy.png",
    },
    
    "terrain_radar": {
        "title": ("USBMIZIYZJ", "Terrain-Following Radar"),
        "description": ("YVVMJNRCEB", (
            f"This bomber has a terrain-following radar, enabling it to fly extremely "
            f"low and avoid detection and targeting for longer, thus giving enemies less "
            f"time to react. This strategy also has its downsides, as the low altitude "
            f"makes it an easier target to hit."
            f"(1.5 stealth bonus)"
        )),
        "texture": "terrain_radar.png",
    },
    
    "_swift": {
        "title": ("XPEEKYWBUG", "Swift"),
        "description": ("IUYGGTVPGD", (
            f"Fewer soldiers and light equipment allow this unit to maintain cohesion "
            "while marching at a faster pace.\n"
            f"\n"
            f"50% movement speed bonus while above 90% morale."
        )),
        "texture": "swift.png",
    },
    
    "_supply_runner": {
        "title": ("FOQNHPUZUW", "Runner"),
        "description": ("UQVNPUWWQY", (
            '#style1{- Supply Range: }' + f'#moral_color_bad_3{{{runner_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#style1{{{runner_fuel}}}' + '#style1{ per second}' + f' #style1{{{runner_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#style1{{{runner_health}}}' + '#style1{ per second}' + f' #style1{{{runner_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#styleTurquoise{{{runner_ammo}}}' + '#style1{ per second}' + f' #styleTurquoise{{{runner_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#moral_color_bad_2{{{runner_critics}}}' + '#style1{ per second}' + f' #moral_color_bad_2{{{runner_critics_percentage}}}'
        )),
        "texture": "runner_supply.png",
    },
    
    "_supply_squad": {
        "title": ("JZDIXEPDQC", "Squad"),
        "description": ("NNCAFAFCWS", (
            '#style1{- Supply Range: }' + f'#moral_color_bad_2{{{squad_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#styleGreen{{{squad_fuel}}}' + '#style1{ per second}' + f' #styleGreen{{{squad_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#style1{{{squad_health}}}' + '#style1{ per second}' + f' #style1{{{squad_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#styleGreen{{{squad_ammo}}}' + '#style1{ per second}' + f' #styleGreen{{{squad_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#style1{{{squad_critics}}}' + '#style1{ per second}' + f' #style1{{{squad_critics_percentage}}}'
        )),
        "texture": "squad_supply.png",
    },
    
    "_supply_primary": {
        "title": ("VVLHQSOXCW", "Primary"),
        "description": ("ULULIILHXH", (
            '#style1{- Supply Range: }' + f'#style1{{{primary_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#style1{{{primary_fuel}}}' + '#style1{ per second}' + f' #style1{{{primary_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#style1{{{primary_health}}}' + '#style1{ per second}' + f' #style1{{{primary_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#style1{{{primary_ammo}}}' + '#style1{ per second}' + f' #style1{{{primary_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#style1{{{primary_critics}}}' + '#style1{ per second}' + f' #style1{{{primary_critics_percentage}}}'
        )),
        "texture": "primary_supply.png",
    },
    
    "_supply_divisional": {
        "title": ("FEDLBRSWYR", "Divisional"),
        "description": ("GHPEPQIELW", (
            '#style1{- Supply Range: }' + f'#styleTurquoise{{{divisional_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#style1{{{divisional_fuel}}}' + '#style1{ per second}' + f' #style1{{{divisional_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#moral_color_bad_2{{{divisional_health}}}' + '#style1{ per second}' + f' #moral_color_bad_2{{{divisional_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#moral_color_bad_2{{{divisional_ammo}}}' + '#style1{ per second}' + f' #moral_color_bad_2{{{divisional_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#styleTurquoise{{{divisional_critics}}}' + '#style1{ per second}' + f' #styleTurquoise{{{divisional_critics_percentage}}}'
        )),
        "texture": "divisional_supply.png",
    },
}

TRAIT_EDITS = {
    "_choc": {
        "extended": {
            "token": "NKHDAPIZBR",
            "text": (
                f"CQC Bonuses: While stationary, and if within "
                f"150m of enemies, gain the following bonuses: "
                f"\n- 15% bonus to aim time, shot reload, and salvo reload. (multiplicative)"
                f"\n- 15% bonus to physical damage. (flat)"
                f"\n\nFor 10 seconds if below 90% cohesion "
                f"Shock units will activate a sprint ability. They will move 100% faster, "
                f"receive no suppression damage, and -20% physical damage. "
                f"\nThis bonus has a 10 second duration, 35 second cooldown."
            )
        }
    },
    "_sniper": {
        "extended": {
            "token": "JUDUFDHTTW",
            "text": (
                f"Sniper units gain an extra level of Stealth, plus a 20% Accuracy "
                f"bonus when not moving (flat). This unit must remain still for at "
                f"least 10 seconds for this effect to trigger."
            )
        }
    }
}
