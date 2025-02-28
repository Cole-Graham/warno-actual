"""UI info panel constants."""

UNIT_INFO_PANEL_DATA = {
    "AttributeDescriptorsPool": {
        "AttributeStrength": {
            "token": "PLDIIMHQJ",
            "hint": (
                "Indicates the number of soldiers in a squad or weapon team."
            ),
            "extended": (
                "The Strength value indicates the hit points of a unit. More "
                "soldiers in a squad means more resillience. Each damage point "
                "eliminates one soldier."
                "\n\nWith the exceptions of ATGM, Recoilless rifle, and Machine Gun teams, the "
                "smaller the infantry squad relative to the enemy targeting it, the less damage "
                "they take from small arms fire. The value is 4% per strength difference in squad "
                "size, up to a maximum of 48%."
                "\n\nLosing a soldier does NOT dynamically increase the level of damage reduction, "
                "In other words, a 12 strength squad at half health is still treated as if it "
                "had full health. This means sending in severely damaged squads in to help fight "
                "can be very inefficient, as opposed to pulling them back and reinforcing them "
                "supply."
            ),
        },
    },
}
