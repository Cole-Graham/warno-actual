"""Weapon description mappings."""

WEAPON_DESCRIPTIONS = {
    "sniper_rifle": (("'GGSLNBFHEX'", "NKQSGYXRYE"), (
        f"Sniper rifles have a low rate of fire, but their precision negates the "
        f"defensive bonus for enemies in cover. The precision of Sniper Rifles also has a "
        f"dramatic psychological effect on the enemy, causing a large amount of suppression."
    ))
}

WEAPON_DESCRIPTION_EDITS = {
    "pgb": {
        "category": (
            "EBKQBGCEHE",
            "PRECISION GUIDED BOMB"
        ),
        "description": (
            "VIFCZPOOHH",
            (
                "Precision Guided Bombs (PGBs) come in two forms: laser-guided and electro-optical. "
                "Laser-guided bombs are more accurate but require active designation at the moment of impact, "
                "although by spacing out the bombs the pilot can (in theory) rapidly switch the laser to effectively "
                "guide onto multiple targets within a limited radius. Electro-optical bombs are less accurate but can "
                "be used to attack multiple targets across a much wider area.\n\n"
                "Tip: The main advantage of Electro-optical bombs is that you can queue up multiple fire position "
                "commands at once, while laser-guided bombs require you to manually switch targets as each bomb is launched."
            )
        ),
    },
}

# WeaponTraits.ndf: ShowAsFilterInShowroom per descriptor key (armory filter chips).
# Keys that are not in NEW_WEAPON_TRAITS are patched on existing vanilla descriptors.
SHOW_AS_FILTER = {
    "cluster": False,
    "clusterHEAT": True,
    "clusterHEFrag": True,
    "biglyHE": True,
}

WEAPON_TRAIT_EDITS = {
    "thermobaric": (
        f"Thermobaric weapons are specialized at destroying infantry and soft targets. "
        f"They are relatively ineffective against armored units compared to conventional "
        f"high explosive weapons, and do not damage buildings."
    ),
    "TANDEM": (
        f"The tandem-charged HEAT round is specifically designed to "
        f"penetrate explosive reactive armor (ERA) using dual-charge "
        f"warheads. Penetration is increased by +2 against ERA-equipped "
        f"units."
    ),
}

# New traits: keys match WeaponTraits.ndf descriptor names; tokens must stay stable for INTERFACE_INGAME.csv.
NEW_WEAPON_TRAITS = {
    "clusterHEAT": {
        "title": "Cluster HEAT",
        "description": (
            "The Cluster HEAT variant of cluster munitions uses shaped-charge warheads and is "
            "better equipped to kill enemy tanks than generic cluster loads. It favors armored "
            "targets over light vehicles and infantry. Damage vs. infantry is AP * 4 / 10"
        ),
        "trait_texture_name": "Texture_Trait_Icon_clusterHEAT",
        "trait_hint_title_token": "QXRMTXAMMH",
        "trait_hint_body_token": "QKNCSNTPJJ",
    },
    "clusterHEFrag": {
        "title": "Cluster HE-Frag",
        "description": (
            "The Cluster HE-Frag variant is dedicated to destroying light vehicles and soft "
            "targets such as enemy infantry. Damage vs. infantry is AP * 6 / 10"
        ),
        "trait_texture_name": "Texture_Trait_Icon_clusterHEFrag",
        "trait_hint_title_token": "IXIZSDQCRB",
        "trait_hint_body_token": "CHKYZZDHSF",
    },
    "biglyHE": {
        "title": "Devastating",
        "description": (
            "Ignores armor"
        ),
        "trait_texture_name": "Texture_Trait_Icon_biglyHE",
        "trait_hint_title_token": "QETCXGYBML",
        "trait_hint_body_token": "MILSGYGXLP",
    },
}
