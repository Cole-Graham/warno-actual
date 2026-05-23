"""Tests for ammunition consumption validation."""

import unittest
from unittest.mock import MagicMock

from src.gameplay_mods.generated.gameplay.gfx.ammunition_.handlers.ammo_consumption_validation import (
    _base_weapon_namespace,
    validate_ammunition_consumption,
)


def _mock_descr(
    namespace: str,
    *,
    shots: str | None = None,
    affichage: str | None = None,
    simultaneous: str | None = None,
) -> MagicMock:
    descr = MagicMock()
    descr.n = namespace

    def by_m(name: str, strict: bool = True):
        values = {
            "ShotsCountPerSalvo": shots,
            "AffichageMunitionParSalve": affichage,
            "SimultaneousShotsCount": simultaneous,
        }
        value = values.get(name)
        if value is None:
            return None
        member = MagicMock()
        member.v = value
        return member

    descr.v.by_m = by_m
    return descr


class TestBaseWeaponNamespace(unittest.TestCase):
    def test_strips_strength_and_quantity_suffixes(self):
        self.assertEqual(
            _base_weapon_namespace("Ammo_FM_AK_74_strength10_x5"),
            "Ammo_FM_AK_74",
        )

    def test_strips_salvo_length_suffix(self):
        self.assertEqual(
            _base_weapon_namespace("Ammo_RocketArt_thermobaric_127mm_salvolength21"),
            "Ammo_RocketArt_thermobaric_127mm",
        )


class TestValidateAmmunitionConsumption(unittest.TestCase):
    def test_matching_values_no_warning(self):
        logger = MagicMock()
        source_path = [
            _mock_descr(
                "Ammo_RocketArt_thermobaric_127mm_salvolength21",
                shots="21",
                affichage="42",
                simultaneous="2",
            ),
        ]

        failed = validate_ammunition_consumption(source_path, logger)

        self.assertFalse(failed)
        logger.warning.assert_not_called()

    def test_mismatch_warns(self):
        logger = MagicMock()
        source_path = [
            _mock_descr(
                "Ammo_RocketArt_thermobaric_127mm_salvolength21",
                shots="21",
                affichage="21",
                simultaneous="2",
            ),
        ]

        failed = validate_ammunition_consumption(source_path, logger)

        self.assertTrue(failed)
        self.assertEqual(logger.warning.call_count, 2)
        first_call = logger.warning.call_args_list[0].args
        self.assertEqual(first_call[0], "%s: AffichageMunitionParSalve=%s but expected %s "
            "(ShotsCountPerSalvo=%s * SimultaneousShotsCount=%s)")
        self.assertEqual(first_call[1], "Ammo_RocketArt_thermobaric_127mm")
        self.assertEqual(first_call[3], 42)

    def test_groups_salvo_variants(self):
        logger = MagicMock()
        source_path = [
            _mock_descr(
                f"Ammo_RocketAir_S5_57mm_salvolength{salvo}",
                shots="32",
                affichage="16",
                simultaneous="2",
            )
            for salvo in (8, 16, 32)
        ]

        failed = validate_ammunition_consumption(source_path, logger)

        self.assertTrue(failed)
        self.assertEqual(logger.warning.call_count, 2)
        self.assertEqual(
            logger.warning.call_args_list[0].args[1],
            "Ammo_RocketAir_S5_57mm",
        )

    def test_skips_non_rocket_ammo(self):
        logger = MagicMock()
        source_path = [
            _mock_descr(
                f"Ammo_FM_AK_74_strength{strength}_x{quantity}",
                shots="6",
                affichage="30",
            )
            for strength in range(5, 17)
            for quantity in (4, 5)
        ]

        failed = validate_ammunition_consumption(source_path, logger)

        self.assertFalse(failed)
        logger.warning.assert_not_called()

    def test_defaults_simultaneous_to_one(self):
        logger = MagicMock()
        source_path = [
            _mock_descr(
                "Ammo_Test",
                shots="12",
                affichage="12",
            ),
        ]

        failed = validate_ammunition_consumption(source_path, logger)

        self.assertFalse(failed)
        logger.warning.assert_not_called()

    def test_skips_when_required_members_missing(self):
        logger = MagicMock()
        source_path = [
            _mock_descr("Ammo_NoShots", affichage="10"),
            _mock_descr("Ammo_NoAffichage", shots="10"),
        ]

        failed = validate_ammunition_consumption(source_path, logger)

        self.assertFalse(failed)
        logger.warning.assert_not_called()


if __name__ == "__main__":
    unittest.main()
