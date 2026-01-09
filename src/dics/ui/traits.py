"""Unit trait and specialty constants."""

from src.constants import NEW_SUPPLY_CONSTANTS


def get_ratio_color(ratio: float) -> str:
    """Map supply ratio to color tag based on thresholds.
    
    Args:
        ratio: The supply ratio value from NEW_SUPPLY_CONSTANTS
        
    Returns:
        Color tag string for use in trait descriptions
    """
    if ratio < 1.0:
        return "moral_color_bad_2"
    elif ratio >= 3.0:
        return "styleTurquoise"
    elif ratio >= 2.0:
        return "styleGreen"
    else:  # ratio >= 1.0 and < 2.0
        return "style1"


runner_configs = NEW_SUPPLY_CONSTANTS["RunnerSupply"]
for key, value in runner_configs.items():
    if key == "DefaultSupplyRangeGRU":
        runner_range = value
    elif key == "FuelSupplyBySecond":
        runner_fuel = value * 30
        runner_fuel_percentage = f"({int(value * 100)}%)"
        runner_fuel_color = get_ratio_color(value)
    elif key == "HealthSupplyBySecond":
        runner_health = float(value/10)
        runner_health_percentage = f"({int(value * 100)}%)"
        runner_health_color = get_ratio_color(value)
    elif key == "AmmunitionSupplyBySecond":
        runner_ammo = value * 60
        runner_ammo_percentage = f"({int(value * 100)}%)"
        runner_ammo_color = get_ratio_color(value)
    elif key == "CriticsSupplyBySecond":
        runner_critics = value * 10
        runner_critics_percentage = f"({int(value * 100)}%)"
        runner_critics_color = get_ratio_color(value)

squad_configs = NEW_SUPPLY_CONSTANTS["SquadSupply"]
for key, value in squad_configs.items():
    if key == "DefaultSupplyRangeGRU":
        squad_range = value
    elif key == "FuelSupplyBySecond":
        squad_fuel = value * 30
        squad_fuel_percentage = f"({int(value * 100)}%)"
        squad_fuel_color = get_ratio_color(value)
    elif key == "HealthSupplyBySecond":
        squad_health = float(value/10)
        squad_health_percentage = f"({int(value * 100)}%)"
        squad_health_color = get_ratio_color(value)
    elif key == "AmmunitionSupplyBySecond":
        squad_ammo = value * 60
        squad_ammo_percentage = f"({int(value * 100)}%)"
        squad_ammo_color = get_ratio_color(value)
    elif key == "CriticsSupplyBySecond":
        squad_critics = value * 10
        squad_critics_percentage = f"({int(value * 100)}%)"
        squad_critics_color = get_ratio_color(value)

primary_configs = NEW_SUPPLY_CONSTANTS["PrimarySupply"]
for key, value in primary_configs.items():
    if key == "DefaultSupplyRangeGRU":
        primary_range = value
    elif key == "FuelSupplyBySecond":
        primary_fuel = value * 30
        primary_fuel_percentage = f"({int(value * 100)}%)"
        primary_fuel_color = get_ratio_color(value)
    elif key == "HealthSupplyBySecond":
        primary_health = float(value/10)
        primary_health_percentage = f"({int(value * 100)}%)"
        primary_health_color = get_ratio_color(value)
    elif key == "AmmunitionSupplyBySecond":
        primary_ammo = value * 60
        primary_ammo_percentage = f"({int(value * 100)}%)"
        primary_ammo_color = get_ratio_color(value)
    elif key == "CriticsSupplyBySecond":
        primary_critics = value * 10
        primary_critics_percentage = f"({int(value * 100)}%)"
        primary_critics_color = get_ratio_color(value)

divisional_configs = NEW_SUPPLY_CONSTANTS["DvisionalSupply"] # Dvisional because 'Div' is reserved in NDF
for key, value in divisional_configs.items():
    if key == "DefaultSupplyRangeGRU":
        divisional_range = value
    elif key == "FuelSupplyBySecond":
        divisional_fuel = value * 30
        divisional_fuel_percentage = f"({int(value * 100)}%)"
        divisional_fuel_color = get_ratio_color(value)
    elif key == "HealthSupplyBySecond":
        divisional_health = float(value/10)
        divisional_health_percentage = f"({int(value * 100)}%)"
        divisional_health_color = get_ratio_color(value)
    elif key == "AmmunitionSupplyBySecond":
        divisional_ammo = value * 60
        divisional_ammo_percentage = f"({int(value * 100)}%)"
        divisional_ammo_color = get_ratio_color(value)
    elif key == "CriticsSupplyBySecond":
        divisional_critics = value * 10
        divisional_critics_percentage = f"({int(value * 100)}%)"
        divisional_critics_color = get_ratio_color(value)

runner_helo_configs = NEW_SUPPLY_CONSTANTS["RunnerHeloSupply"]
for key, value in runner_helo_configs.items():
    if key == "DefaultSupplyRangeGRU":
        runner_helo_range = value
    elif key == "FuelSupplyBySecond":
        runner_helo_fuel = value * 30
        runner_helo_fuel_percentage = f"({int(value * 100)}%)"
        runner_helo_fuel_color = get_ratio_color(value)
    elif key == "HealthSupplyBySecond":
        runner_helo_health = float(value/10)
        runner_helo_health_percentage = f"({int(value * 100)}%)"
        runner_helo_health_color = get_ratio_color(value)
    elif key == "AmmunitionSupplyBySecond":
        runner_helo_ammo = value * 60
        runner_helo_ammo_percentage = f"({int(value * 100)}%)"
        runner_helo_ammo_color = get_ratio_color(value)
    elif key == "CriticsSupplyBySecond":
        runner_helo_critics = value * 10
        runner_helo_critics_percentage = f"({int(value * 100)}%)"
        runner_helo_critics_color = get_ratio_color(value)

primary_helo_configs = NEW_SUPPLY_CONSTANTS["PrimaryHeloSupply"]
for key, value in primary_helo_configs.items():
    if key == "DefaultSupplyRangeGRU":
        primary_helo_range = value
    elif key == "FuelSupplyBySecond":
        primary_helo_fuel = value * 30
        primary_helo_fuel_percentage = f"({int(value * 100)}%)"
        primary_helo_fuel_color = get_ratio_color(value)
    elif key == "HealthSupplyBySecond":
        primary_helo_health = float(value/10)
        primary_helo_health_percentage = f"({int(value * 100)}%)"
        primary_helo_health_color = get_ratio_color(value)
    elif key == "AmmunitionSupplyBySecond":
        primary_helo_ammo = value * 60
        primary_helo_ammo_percentage = f"({int(value * 100)}%)"
        primary_helo_ammo_color = get_ratio_color(value)
    elif key == "CriticsSupplyBySecond":
        primary_helo_critics = value * 10
        primary_helo_critics_percentage = f"({int(value * 100)}%)"
        primary_helo_critics_color = get_ratio_color(value)

divisional_helo_configs = NEW_SUPPLY_CONSTANTS["DvisionalHeloSupply"]
for key, value in divisional_helo_configs.items():
    if key == "DefaultSupplyRangeGRU":
        divisional_helo_range = value
    elif key == "FuelSupplyBySecond":
        divisional_helo_fuel = value * 30
        divisional_helo_fuel_percentage = f"({int(value * 100)}%)"
        divisional_helo_fuel_color = get_ratio_color(value)
    elif key == "HealthSupplyBySecond":
        divisional_helo_health = float(value/10)
        divisional_helo_health_percentage = f"({int(value * 100)}%)"
        divisional_helo_health_color = get_ratio_color(value)
    elif key == "AmmunitionSupplyBySecond":
        divisional_helo_ammo = value * 60
        divisional_helo_ammo_percentage = f"({int(value * 100)}%)"
        divisional_helo_ammo_color = get_ratio_color(value)
    elif key == "CriticsSupplyBySecond":
        divisional_helo_critics = value * 10
        divisional_helo_critics_percentage = f"({int(value * 100)}%)"
        divisional_helo_critics_color = get_ratio_color(value)   


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
            f"struggle to maintain cohesion under fire."
        )),
        "extended": ("UQBVPVHSOX", (
            f"- Increased suppression damage taken while moving (33%)"
        )),
        "texture": "medium_equipment.png",
    },
    
    "mequip_label": { # label for medium equipment texture (#MEQUIP)
        "title": (None, None),
        "description": (None, (
            None
        )),
        "texture": "mequip_label.png",
    },
    
    "infantry_equip_heavy": {
        "title": ("CAOTQXVHXH", "Heavy Equipment"),
        "description": ("XLMSCEWDLB", (
            f"These infantry are burdened by powerful yet heavy equipment, "
            f"hampering their mobility on the battlefield."
        )),
        "extended": ("ZGBDBQRXQA", (
            f"- Increased suppression damage taken while moving (33%)\n"
            f"- Reduced movement speed (-6 Km/h)"
        )),
        "texture": "heavy_equipment.png",
    },
    
    "hequip_label": { # label for heavy equipment texture (#HEQUIP)
        "title": (None, None),
        "description": (None, (
            None
        )),
        "texture": "hequip_label.png",
    },
    
    "infantry_equip_veryheavy": {
        "title": ("AXLDYZOVCJ", "Immobile Weapon Systems"),
        "description": ("DJTBXQWLVR", (
            f"These infantry employ heavy weapons meant for defending entrenched "
            f"positions. Keep a transport nearby if you foresee the need to "
            f"reposition this unit in a hurry, and be proactive about avoiding "
            f"enemy artillery if their position is revealed."
        )),
        "extended": ("EFCIVTGYYW", (
            f"- Reduced movement speed (-12 Km/h)"
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
            '#style1{- Supply Range: }' + f'#moral_color_bad_2{{{runner_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#{runner_fuel_color}{{{runner_fuel}}}'
            + '#style1{ per second}' + f' #{runner_fuel_color}{{{runner_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#{runner_health_color}{{{runner_health}}}'
            + '#style1{ per second}' + f' #{runner_health_color}{{{runner_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#{runner_ammo_color}{{{runner_ammo}}}'
            + '#style1{ per second}' + f' #{runner_ammo_color}{{{runner_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#{runner_critics_color}{{{runner_critics}}}'
            + '#style1{ per second}' + f' #{runner_critics_color}{{{runner_critics_percentage}}}'
        )),
        "texture": "runner_supply.png",
    },
    
    "_supply_squad": {
        "title": ("JZDIXEPDQC", "Squad"),
        "description": ("NNCAFAFCWS", (
            '#style1{- Supply Range: }' + f'#style1{{{squad_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#{squad_fuel_color}{{{squad_fuel}}}'
            + '#style1{ per second}' + f' #{squad_fuel_color}{{{squad_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#{squad_health_color}{{{squad_health}}}'
            + '#style1{ per second}' + f' #{squad_health_color}{{{squad_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#{squad_ammo_color}{{{squad_ammo}}}'
            + '#style1{ per second}' + f' #{squad_ammo_color}{{{squad_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#{squad_critics_color}{{{squad_critics}}}'
            + '#style1{ per second}' + f' #{squad_critics_color}{{{squad_critics_percentage}}}'
        )),
        "texture": "squad_supply.png",
    },
    
    "_supply_primary": {
        "title": ("VVLHQSOXCW", "Primary"),
        "description": ("ULULIILHXH", (
            '#style1{- Supply Range: }' + f'#styleGreen{{{primary_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#{primary_fuel_color}{{{primary_fuel}}}'
            + '#style1{ per second}' + f' #{primary_fuel_color}{{{primary_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#{primary_health_color}{{{primary_health}}}'
            + '#style1{ per second}' + f' #{primary_health_color}{{{primary_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#{primary_ammo_color}{{{primary_ammo}}}'
            + '#style1{ per second}' + f' #{primary_ammo_color}{{{primary_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#{primary_critics_color}{{{primary_critics}}}'
            + '#style1{ per second}' + f' #{primary_critics_color}{{{primary_critics_percentage}}}'
        )),
        "texture": "primary_supply.png",
    },
    
    "_supply_divisional": {
        "title": ("FEDLBRSWYR", "Divisional"),
        "description": ("GHPEPQIELW", (
            '#style1{- Supply Range: }' + f'#styleTurquoise{{{divisional_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#{divisional_fuel_color}{{{divisional_fuel}}}'
            + '#style1{ per second}' + f' #{divisional_fuel_color}{{{divisional_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#{divisional_health_color}{{{divisional_health}}}'
            + '#style1{ per second}' + f' #{divisional_health_color}{{{divisional_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#{divisional_ammo_color}{{{divisional_ammo}}}'
            + '#style1{ per second}' + f' #{divisional_ammo_color}{{{divisional_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#{divisional_critics_color}{{{divisional_critics}}}'
            + '#style1{ per second}' + f' #{divisional_critics_color}{{{divisional_critics_percentage}}}'
        )),
        "texture": "divisional_supply.png",
    },
    
    "_supply_runner_helo": {
        "title": ("HQWRTYZXCV", "Runner (Helicopter)"),
        "description": ("BNMJKLPQRS", (
            '#style1{- Supply Range: }' + f'#styleGreen{{{runner_helo_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#{runner_helo_fuel_color}{{{runner_helo_fuel}}}'
            + '#style1{ per second}' + f' #{runner_helo_fuel_color}{{{runner_helo_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#{runner_helo_health_color}{{{runner_helo_health}}}'
            + '#style1{ per second}' + f' #{runner_helo_health_color}{{{runner_helo_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#{runner_helo_ammo_color}{{{runner_helo_ammo}}}'
            + '#style1{ per second}' + f' #{runner_helo_ammo_color}{{{runner_helo_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#{runner_helo_critics_color}{{{runner_helo_critics}}}'
            + '#style1{ per second}' + f' #{runner_helo_critics_color}{{{runner_helo_critics_percentage}}}'
        )),
        "texture": "runner_supply.png",
    },
    
    "_supply_primary_helo": {
        "title": ("ANDUVIMEHT", "Primary (Helicopter)"),
        "description": ("GUISMXYQPZ", (
            '#style1{- Supply Range: }' + f'#styleTurquoise{{{primary_helo_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#{primary_helo_fuel_color}{{{primary_helo_fuel}}}'
            + '#style1{ per second}' + f' #{primary_helo_fuel_color}{{{primary_helo_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#{primary_helo_health_color}{{{primary_helo_health}}}'
            + '#style1{ per second}' + f' #{primary_helo_health_color}{{{primary_helo_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#{primary_helo_ammo_color}{{{primary_helo_ammo}}}'
            + '#style1{ per second}' + f' #{primary_helo_ammo_color}{{{primary_helo_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#{primary_helo_critics_color}{{{primary_helo_critics}}}'
            + '#style1{ per second}' + f' #{primary_helo_critics_color}{{{primary_helo_critics_percentage}}}'
        )),
        "texture": "primary_supply.png",
    },
    
    "_supply_divisional_helo": {
        "title": ("HDNGUIMAOX", "Divisional (Helicopter)"),
        "description": ("UGJYTIVNGL", (
            '#style1{- Supply Range: }' + f'#styleTurquoise{{{divisional_helo_range}m}}'
            '\n#style1{- Fuel Supply: }' + f'#{divisional_helo_fuel_color}{{{divisional_helo_fuel}}}'
            + '#style1{ per second}' + f' #{divisional_helo_fuel_color}{{{divisional_helo_fuel_percentage}}}'
            '\n#style1{- Health Supply: }' + f'#{divisional_helo_health_color}{{{divisional_helo_health}}}'
            + '#style1{ per second}' + f' #{divisional_helo_health_color}{{{divisional_helo_health_percentage}}}'
            '\n#style1{- Ammunition Supply: }' + f'#{divisional_helo_ammo_color}{{{divisional_helo_ammo}}}'
            + '#style1{ per second}' + f' #{divisional_helo_ammo_color}{{{divisional_helo_ammo_percentage}}}'
            '\n#style1{- Crit Repair Rate:: }' + f'#{divisional_helo_critics_color}{{{divisional_helo_critics}}}'
            + '#style1{ per second}' + f' #{divisional_helo_critics_color}{{{divisional_helo_critics_percentage}}}'
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
                f"\n\nWithin 875m of enemies, activate a sprint ability: When in combat "
                f"and above 40% cohesion, Shock units will activate a sprint ability. "
                f"While active, shock infantry move 100% faster, and receive -50% suppression damage"
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
