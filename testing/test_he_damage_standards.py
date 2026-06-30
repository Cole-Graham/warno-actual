"""Tests for canon HE damage standard caliber resolution."""

import unittest
from unittest.mock import MagicMock

from src.constants.weapons.standards import CANON_HE_DAMAGE_BY_CALIBER
from src.gameplay_mods.generated.gameplay.gfx.ammunition_.handlers.standards import (
    _base_weapon_name_from_ammo_namespace,
    _build_ammunition_caliber_edits,
    apply_he_damage_standards,
)


class TestHeDamageCaliberResolution(unittest.TestCase):
    def test_base_weapon_name_strips_ammo_prefix_and_salvo_suffix(self):
        self.assertEqual(
            _base_weapon_name_from_ammo_namespace("Ammo_Canon_HE_125_mm_2A46_salvolength2"),
            "Canon_HE_125_mm_2A46",
        )

    def test_caliber_edits_include_spg9_he_fix(self):
        edits = _build_ammunition_caliber_edits()
        self.assertEqual(edits["Canon_HE_73_mm_SPG9"], "'BQEOKGFQRX'")

    def test_apply_he_damage_uses_constants_caliber_not_vanilla(self):
        descr = MagicMock()
        descr.namespace = "Ammo_Canon_HE_73_mm_SPG9"
        physical_damages = MagicMock()
        physical_damages.v = "0.85"

        def by_m(member_name: str, strict: bool = True):
            values = {
                "Name": "'SOME_TOKEN'",
                "MinMaxCategory": "MinMax_CanonAP",
                "PiercingWeapon": "False",
                "Caliber": "'DYWXTLDKWR'",
                "PhysicalDamages": physical_damages,
            }
            value = values.get(member_name)
            if value is None:
                return None
            if member_name == "PhysicalDamages":
                return physical_damages
            member = MagicMock()
            member.v = value
            return member

        descr.v.by_m = by_m

        apply_he_damage_standards([descr], MagicMock())

        self.assertEqual(physical_damages.v, "0.85")

    def test_apply_he_damage_uses_vanilla_caliber_when_no_edit(self):
        descr = MagicMock()
        descr.namespace = "Ammo_Canon_HE_120_mm_2A46"
        physical_damages = MagicMock()
        physical_damages.v = "1.0"

        def by_m(member_name: str, strict: bool = True):
            values = {
                "Name": "'SOME_TOKEN'",
                "MinMaxCategory": "MinMax_CanonAP",
                "PiercingWeapon": "False",
                "Caliber": "'DYWXTLDKWR'",
                "PhysicalDamages": physical_damages,
            }
            value = values.get(member_name)
            if value is None:
                return None
            if member_name == "PhysicalDamages":
                return physical_damages
            member = MagicMock()
            member.v = value
            return member

        descr.v.by_m = by_m

        apply_he_damage_standards([descr], MagicMock())

        self.assertEqual(
            physical_damages.v,
            str(CANON_HE_DAMAGE_BY_CALIBER["'DYWXTLDKWR'"]),
        )


if __name__ == "__main__":
    unittest.main()
