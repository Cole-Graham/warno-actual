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
                f"Precision Guided Bombs (PGBs) come in two forms: laser-guided and electro-optical. "
                f"Laser-guided bombs are more accurate but require active designation at the moment of impact, "
                f"although by spacing out the bombs the pilot can (in theory) rapidly switch the laser to effectively "
                f"guide onto multiple targets within a limited radius. Electro-optical bombs are less accurate but can "
                f"be used to attack multiple targets across a much wider area.\n\n"
                f"#styleGreen{{- The main advantage of Electro-optical bombs is that you can queue up multiple fire position "
                f"commands at once, while laser-guided bombs require you to manually switch targets as each bomb is launched.}}"
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
    "reflexpriorityoff": True,
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
        f"warheads.\n\n"
        f"#styleGreen{{- Penetration is increased by +2 against ERA-equipped "
        f"units.}}"
    ),
}

# New traits: keys match WeaponTraits.ndf descriptor names; tokens must stay stable for INTERFACE_INGAME.csv.
NEW_WEAPON_TRAITS = {
    "clusterHEAT": {
        "title": "Cluster HEAT",
        "description": (
            f"The Cluster HEAT variant of cluster munitions uses shaped-charge warheads and is "
            f"better equipped to kill enemy tanks than generic cluster loads.\n\n"
            f"- Damage vs. infantry is #styleGreen{{AP * 4}} / 10"
        ),
        "trait_texture_name": "Texture_Trait_Icon_clusterHEAT",
        "trait_hint_title_token": "QXRMTXAMMH",
        "trait_hint_body_token": "QKNCSNTPJJ",
    },
    "clusterHEFrag": {
        "title": "Cluster HE-Frag",
        "description": (
            f"The Cluster HE-Frag variant is dedicated to destroying light vehicles and soft "
            f"targets such as enemy infantry.\n\n"
            f"- Damage vs. infantry is #styleTurquoise{{AP * 6}} / 10"
        ),
        "trait_texture_name": "Texture_Trait_Icon_clusterHEFrag",
        "trait_hint_title_token": "IXIZSDQCRB",
        "trait_hint_body_token": "CHKYZZDHSF",
    },
    "biglyHE": {
        "title": "Devastating",
        "description": (
            "Ignores armor, always stuns."
        ),
        "trait_texture_name": "Texture_Trait_Icon_biglyHE",
        "trait_hint_title_token": "QETCXGYBML",
        "trait_hint_body_token": "MILSGYGXLP",
    },
    "reflexpriorityoff": {
        "title": "Priority targeting disabled",
        "description": (
            "This weapon will not disable automatic firing when prioritizing a target "
            "with right click. This is necessary for the functionality of strike planes with "
            "particular kinds of mixed weapon loadouts.\n\nIf the prioritized target is out of range "
            "and there is another compatible target in range, the weapon will ignore the priority "
            "target order and fire at the target that is already in range."
        ),
        "trait_texture_name": "Texture_Trait_Icon_reflexpriorityoff",
        "trait_hint_title_token": "NBIXHLYGDV",
        "trait_hint_body_token": "QYOLCIOFMH",
    },
}

# BUCKTextureBank.ndf: ``Texture_Trait_Icon_*`` for mod weapon traits (see traits section; same
# directory as vanilla ``Texture_Trait_Icon_*`` entries).
_WEAPON_TRAIT_ICON_DIR = "GameData:/Assets/2D/Interface/Common/traits"

ADDITIONAL_WEAPON_TRAIT_ICON_TEXTURES = (
    ("Texture_Trait_Icon_clusterHEAT", "cluster-heat.png"),
    ("Texture_Trait_Icon_clusterHEFrag", "cluster-hefrag.png"),
    ("Texture_Trait_Icon_biglyHE", "bigly-he.png"),
    ("Texture_Trait_Icon_reflexpriorityoff", "reflexpriorityoff.png"),
)
