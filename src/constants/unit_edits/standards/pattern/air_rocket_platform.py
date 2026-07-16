"""Pattern standard: remount dumbfire rockets to plane (avion) or helo ammo."""

from typing import TypedDict


AIR_ROCKET_DAMAGE_FAMILY = "DamageFamily_roquette_ap"


class AirRocketPlatformPair(TypedDict):
    """Helo/non-avion ammo name paired with its plane avion sibling."""

    helo_ammo: str
    avion_ammo: str


# Bare post-rename / constants names. Pairs must share the same salvo length.
# A ``_helo`` suffix is only a naming quirk for the non-avion (helo) side.
# Every pair has distinct helo and avion descriptors (authored in rocket.py).
AIR_ROCKET_PLATFORM_PAIRS: tuple[AirRocketPlatformPair, ...] = (
    # Vanilla / existing same-salvo pairs
    {
        "helo_ammo": "RocketAir_B8_80mm_salvolength40",
        "avion_ammo": "RocketAir_B8_80mm_avion_salvolength40",
    },
    {
        "helo_ammo": "RocketAir_S13_122mm_salvolength10",
        "avion_ammo": "RocketAir_S13_122mm_avion_salvolength10",
    },
    {
        "helo_ammo": "RocketAir_Hydra_70mm_salvolength14",
        "avion_ammo": "RocketAir_Hydra_70mm_x14_avion",
    },
    {
        "helo_ammo": "RocketAir_B8_80mm_salvolength10",
        "avion_ammo": "RocketAir_B8_80mm_Avion_salvolength10",
    },
    # Mod clones (same salvo)
    {
        "helo_ammo": "RocketAir_Zuni_1272mm_salvolength8",
        "avion_ammo": "RocketAir_Zuni_1272mm_avion_salvolength8",
    },
    {
        "helo_ammo": "RocketAir_Zuni_1272mm_salvolength16",
        "avion_ammo": "RocketAir_Zuni_1272mm_avion_salvolength16",
    },
    {
        "helo_ammo": "RocketAir_S5_57mm_salvolength32",
        "avion_ammo": "RocketAir_S5_57mm_avion_salvolength32",
    },
    {
        "helo_ammo": "RocketAir_B8_80mm_salvolength80",
        "avion_ammo": "RocketAir_B8_80mm_avion_salvolength80",
    },
    {
        "helo_ammo": "RocketAir_S13_122mm_salvolength20",
        "avion_ammo": "RocketAir_S13_122mm_avion_salvolength20",
    },
    {
        "helo_ammo": "RocketAir_SNEB_68mm_salvolength12",
        "avion_ammo": "RocketAir_SNEB_68mm_avion_salvolength12",
    },
    {
        "helo_ammo": "RocketAir_SNEB_68mm_salvolength38",
        "avion_ammo": "RocketAir_SNEB_68mm_avion_salvolength38",
    },
    {
        "helo_ammo": "RocketAir_122_JROF_L_122mm_salvolength4",
        "avion_ammo": "RocketAir_122_JROF_L_122mm_avion_salvolength4",
    },
    {
        "helo_ammo": "RocketAir_CRV7_70mm_salvolength38",
        "avion_ammo": "RocketAir_CRV7_70mm_avion_salvolength38",
    },
    {
        "helo_ammo": "RocketAir_HVAR_127mm_salvolength8",
        "avion_ammo": "RocketAir_HVAR_127mm_avion_salvolength8",
    },
    {
        "helo_ammo": "RocketAir_TBrandt_100mm_salvolength8",
        "avion_ammo": "RocketAir_TBrandt_100mm_avion_salvolength8",
    },
    # Same salvo: Eugen's _helo suffix is just the non-avion name.
    {
        "helo_ammo": "RocketAir_SNEB_68mm_x18_helo",
        "avion_ammo": "RocketAir_SNEB_68mm_avion_salvolength18",
    },
    # Former self-pairs — distinct helo / avion siblings in rocket.py
    {
        "helo_ammo": "RocketAir_Hydra_70mm_salvolength76",
        "avion_ammo": "RocketAir_Hydra_70mm_avion_salvolength76",
    },
    {
        "helo_ammo": "RocketAir_Hydra_70mm_salvolength38",
        "avion_ammo": "RocketAir_Hydra_70mm_x38_avion",
    },
    {
        "helo_ammo": "RocketAir_Hydra_70mm_salvolength114",
        "avion_ammo": "RocketAir_Hydra_70mm_x114_avion",
    },
    {
        "helo_ammo": "RocketAir_122_JROF_L_122mm_salvolength54",
        "avion_ammo": "RocketAir_122_JROF_L_122mm_x54_avion",
    },
    {
        "helo_ammo": "RocketAir_Grom_57mm_salvolength16",
        "avion_ammo": "RocketAir_Grom_57mm_avion_salvolength16",
    },
    {
        "helo_ammo": "RocketAir_S24_240mm_salvolength3",
        "avion_ammo": "RocketAir_S24_240mm_avion_salvolength3",
    },
    {
        "helo_ammo": "RocketAir_S25O_420mm_salvolength2",
        "avion_ammo": "RocketAir_S25O_420mm_avion_salvolength2",
    },
    {
        "helo_ammo": "RocketAir_SNEB_68mm_salvolength36",
        "avion_ammo": "RocketAir_SNEB_68mm_avion_salvolength36",
    },
    {
        "helo_ammo": "RocketAir_S24_240mm_salvolength2",
        "avion_ammo": "RocketAir_S24_240mm_avion_salvolength2",
    },
    {
        "helo_ammo": "RocketAir_S24_240mm_salvolength4",
        "avion_ammo": "RocketAir_S24_240mm_avion_salvolength4",
    },
    {
        "helo_ammo": "RocketAir_Hydra_70mm_salvolength19",
        "avion_ammo": "RocketAir_Hydra_70mm_avion_salvolength19",
    },
    {
        "helo_ammo": "RocketAir_Hydra_70mm_x31_M229",
        "avion_ammo": "RocketAir_Hydra_70mm_x31_M229_avion",
    },
    {
        "helo_ammo": "RocketAir_B8_80mm_salvolength20",
        "avion_ammo": "RocketAir_B8_80mm_avion_salvolength20",
    },
    {
        "helo_ammo": "RocketAir_S5_57mm_salvolength8",
        "avion_ammo": "RocketAir_S5_57mm_avion_salvolength8",
    },
    {
        "helo_ammo": "RocketAir_S5_57mm_salvolength16",
        "avion_ammo": "RocketAir_S5_57mm_avion_salvolength16",
    },
    {
        "helo_ammo": "RocketAir_S5_57mm_salvolength64",
        "avion_ammo": "RocketAir_S5_57mm_avion_salvolength64",
    },
    {
        "helo_ammo": "RocketAir_S5_57mm_salvolength96",
        "avion_ammo": "RocketAir_S5_57mm_avion_salvolength96",
    },
    {
        "helo_ammo": "RocketAir_JRRO_130_130mm_salvolength8",
        "avion_ammo": "RocketAir_JRRO_130_130mm_avion_salvolength8",
    },
)


def _name_has_helo_marker(ammo_name: str) -> bool:
    """True if the ammo namespace marks a helo/non-avion variant (``_helo``)."""
    lower = ammo_name.lower()
    return "_helo" in lower or lower.endswith("helo")


def build_air_rocket_platform_maps(
    pairs: tuple[AirRocketPlatformPair, ...] = AIR_ROCKET_PLATFORM_PAIRS,
) -> tuple[dict[str, str], dict[str, str], frozenset[str], frozenset[str]]:
    """Return helo→avion, avion→helo, helo names, avion names.

    Names with ``_helo`` / ``_Helo`` belong on the helo side only (non-avion).
    """
    helo_to_avion: dict[str, str] = {}
    avion_to_helo: dict[str, str] = {}
    for pair in pairs:
        helo = pair["helo_ammo"]
        avion = pair["avion_ammo"]
        if _name_has_helo_marker(avion) and helo != avion:
            raise ValueError(
                f"avion_ammo must not use a _helo marker: {avion!r} (pair helo={helo!r})",
            )
        helo_to_avion[helo] = avion
        avion_to_helo[avion] = helo
    return (
        helo_to_avion,
        avion_to_helo,
        frozenset(helo_to_avion),
        frozenset(avion_to_helo),
    )
