"""Unit trait and specialty constants."""

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
        "title": ("VVLHQSOXCW", "Swift"),
        "description": ("ULULIILHXH", (
            f"Fewer soldiers and light equipment allow this unit to maintain cohesion "
            "while marching at a faster pace.\n"
            f"\n"
            f"33% movement speed bonus while above 90% morale."
        )),
        "texture": "swift.png",
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
                f"\n\nFor 10 seconds if below 90% cohesion and within 875m of enemies, "
                f"Shock units will activate a sprint ability. They will move 50% faster, "
                f"receive -50% suppression damage, and -20% physical damage. "
                f"(multiplicative, percentage, percentage)"
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