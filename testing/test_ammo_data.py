"""Tests for ammunition database building helpers."""

import unittest
from unittest.mock import MagicMock

from src.data.ammo_data import _localized_token_field, build_ammo_properties


class TestLocalizedTokenField(unittest.TestCase):
    def test_maps_token_to_localized_value(self):
        lookup = {"SHBINZZBDX": "M242 Bushmaster"}
        self.assertEqual(
            _localized_token_field("'SHBINZZBDX'", lookup),
            {"Token": "SHBINZZBDX", "Value": "M242 Bushmaster"},
        )

    def test_falls_back_to_token_when_missing_from_lookup(self):
        self.assertEqual(
            _localized_token_field("'UNKNOWN'", {}),
            {"Token": "UNKNOWN", "Value": "UNKNOWN"},
        )

    def test_none_member_returns_none(self):
        self.assertIsNone(_localized_token_field(None, {}))
        self.assertIsNone(_localized_token_field("'None'", {}))


def _mock_ammo_descr(
    namespace: str,
    *,
    name: str | None = None,
    type_category: str | None = None,
    caliber: str | None = None,
    min_max_category: str = "MinMax_AutocanonHE",
) -> MagicMock:
    descr = MagicMock()
    descr.n = namespace

    def by_m(member_name: str, strict: bool = True):
        values = {
            "Name": name,
            "TypeCategoryName": type_category,
            "Caliber": caliber,
            "MinMaxCategory": min_max_category,
            "RadiusSplashPhysicalDamagesGRU": "5",
            "HasDeploymentTime": "False",
            "PhysicalDamages": "0.55",
            "MaximumRangeHelicopterGRU": "1500",
            "MaximumRangeAirplaneGRU": "0",
            "MaximumRangeGRU": "1750",
        }
        value = values.get(member_name)
        if value is None:
            return None
        member = MagicMock()
        member.v = value
        return member

    descr.v.by_m = by_m
    return descr


class TestBuildAmmoProperties(unittest.TestCase):
    def test_includes_name_type_category_and_caliber(self):
        descr = _mock_ammo_descr(
            "Ammo_AutoCanon_HE_25mm_M242_Bushmaster_Late",
            name="'SHBINZZBDX'",
            type_category="'YSSCMQVTWR'",
            caliber="'IQVKWJHLNK'",
        )
        lookup = {
            "SHBINZZBDX": "M242 Bushmaster",
            "YSSCMQVTWR": "AUTOCANNON",
            "IQVKWJHLNK": "25mm",
        }

        props = build_ammo_properties([descr], lookup)
        entry = props["Ammo_AutoCanon_HE_25mm_M242_Bushmaster_Late"]

        self.assertEqual(entry["Name"], {"Token": "SHBINZZBDX", "Value": "M242 Bushmaster"})
        self.assertEqual(entry["TypeCategoryName"], {"Token": "YSSCMQVTWR", "Value": "AUTOCANNON"})
        self.assertEqual(entry["Caliber"], {"Token": "IQVKWJHLNK", "Value": "25mm"})
        self.assertEqual(entry["PhysicalDamages"], 0.55)
        self.assertEqual(entry["MaximumRangeGRU"], 1750)


if __name__ == "__main__":
    unittest.main()
