"""Tests for SPAAG _AIR mount channel rewiring and depiction operators."""

import logging
import unittest

from src import ndf
from src.gameplay_mods.generated.gameplay.gfx.depictions.he_dca_air_depiction import (
    apply_he_dca_air_depiction_weapons,
)
from src.gameplay_mods.generated.gameplay.gfx.weapon_descriptor.handlers.he_dca_air_mounts import (
    apply_he_dca_air_mounts,
)
from src.utils.ndf_utils import strip_quotes

_WEAPON_DESCR_NDF = """
export WeaponDescriptor_M163_PIVADS_US is TWeaponManagerModuleDescriptor
(
    Salves = [21]
    TurretDescriptorList =
    [
        TTurretTwoAxisDescriptor
        (
            MountedWeaponDescriptorList =
            [
                TMountedWeaponDescriptor
                (
                    AmmoBoxIndex = 0
                    Ammunition = $/GFX/Weapon/Ammo_Gatling_M61_Vulcan_20mm_late
                    AnimateOnlyOneSoldier = False
                    EffectTag = "FireEffect_Gatling_M61_Vulcan_20mm_late"
                    HandheldEquipmentKey = "WeaponAlternative_1"
                    NbWeapons = 1
                    ShowDispersion = False
                    WeaponActiveAndCanShootPropertyName = "WeaponActiveAndCanShoot_1"
                    WeaponIgnoredPropertyName = "WeaponIgnored_1"
                    WeaponShootDataPropertyName = ["WeaponShootData_0_1"]
                )
            ]
            YulBoneOrdinal = 1
        )
    ]
)
"""

_DEPICTION_NDF = """
DepictionOperator_M163_PIVADS_US_Weapon1 is DepictionOperator_WeaponContinuousFire
(
    FireEffectTag = "weapon_effet_tag1"
    Anchors = ["fx_tourelle1_tir_01"]
    WeaponShootDataPropertyName = "WeaponShootData_0_1"
    WeaponActiveAndCanShootPropertyName = "WeaponActiveAndCanShoot_1"
    NbFX = 1
)

unnamed TacticVehicleDepictionRegistration
(
    BlackHoleKey = 'M163_PIVADS_US'
    Selector = SpecificMechanicalDepictionSelector
    Alternatives = Alternatives_M163_PIVADS_US
    Operators =
    [
        DepictionOperator_CropFlattening,
        DepictionOperator_M163_PIVADS_US_Weapon1,
        DepictionOperator_EjectableProps_Vehicle
    ]
    Actions = MAP[
                ( "weapon_effet_tag1", Weapon_Gatling_M61_Vulcan_20mm_late ),
            ]
            + DepictionAction_Stress_And_Wrecked
)
"""

_GAME_DB = {
    "ammunition": {
        "he_dca_weapons": {
            "Gatling_M61_Vulcan_20mm_late": "DamageFamily_he_dca",
        },
    },
}


class _FakeSourcePath:
    def __init__(self, rows):
        self._rows = rows

    def __iter__(self):
        return iter(self._rows)


class TestHeDcaAirMounts(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger("test_he_dca_air")
        self.weapon_descr = ndf.convert(_WEAPON_DESCR_NDF)[0]
        self.source_path = _FakeSourcePath([self.weapon_descr])
        self.game_db = {
            "ammunition": dict(_GAME_DB["ammunition"]),
            "he_dca_air_depiction_channels": {},
        }

    def _mounted_list(self):
        turret = self.weapon_descr.v.by_m("TurretDescriptorList").v[0]
        return turret.v.by_m("MountedWeaponDescriptorList").v

    def test_adds_air_mount_with_distinct_shoot_channel(self):
        apply_he_dca_air_mounts(self.source_path, self.logger, self.game_db)

        mounts = self._mounted_list()
        self.assertEqual(len(mounts), 2)

        ground = mounts[0].v
        air = mounts[1].v
        self.assertEqual(
            ground.by_m("Ammunition").v,
            "$/GFX/Weapon/Ammo_Gatling_M61_Vulcan_20mm_late",
        )
        self.assertEqual(
            air.by_m("Ammunition").v,
            "$/GFX/Weapon/Ammo_Gatling_M61_Vulcan_20mm_late_AIR",
        )
        self.assertEqual(ground.by_m("AmmoBoxIndex").v, air.by_m("AmmoBoxIndex").v)
        self.assertEqual(
            ground.by_m("HandheldEquipmentKey").v,
            air.by_m("HandheldEquipmentKey").v,
        )
        self.assertNotEqual(
            str(ground.by_m("WeaponShootDataPropertyName").v),
            str(air.by_m("WeaponShootDataPropertyName").v),
        )
        self.assertIn(
            "WeaponShootData_0_2",
            str(air.by_m("WeaponShootDataPropertyName").v),
        )
        self.assertEqual(
            strip_quotes(str(air.by_m("WeaponActiveAndCanShootPropertyName").v)),
            "WeaponActiveAndCanShoot_2",
        )
        self.assertEqual(
            strip_quotes(str(air.by_m("WeaponIgnoredPropertyName").v)),
            "WeaponIgnored_2",
        )
        self.assertEqual(
            strip_quotes(str(air.by_m("EffectTag").v)),
            "FireEffect_Gatling_M61_Vulcan_20mm_late_AIR",
        )

        channels = self.game_db["he_dca_air_depiction_channels"]
        self.assertIn("M163_PIVADS_US", channels)
        self.assertEqual(len(channels["M163_PIVADS_US"]), 1)
        rec = channels["M163_PIVADS_US"][0]
        self.assertEqual(rec["ground_shoot"], "WeaponShootData_0_1")
        self.assertEqual(rec["air_shoot"], "WeaponShootData_0_2")
        self.assertEqual(rec["air_active"], "WeaponActiveAndCanShoot_2")

    def test_second_run_is_idempotent(self):
        apply_he_dca_air_mounts(self.source_path, self.logger, self.game_db)
        apply_he_dca_air_mounts(self.source_path, self.logger, self.game_db)
        self.assertEqual(len(self._mounted_list()), 2)
        channels = self.game_db["he_dca_air_depiction_channels"]["M163_PIVADS_US"]
        self.assertEqual(len(channels), 1)

    def test_rewires_shared_channel_on_existing_air(self):
        # Pre-seed a shared-channel AIR mount (legacy auto-wire behavior).
        apply_he_dca_air_mounts(self.source_path, self.logger, self.game_db)
        air = self._mounted_list()[1].v
        air.by_m("WeaponShootDataPropertyName").v = "['WeaponShootData_0_1']"
        air.by_m("WeaponActiveAndCanShootPropertyName").v = (
            "'WeaponActiveAndCanShoot_1'"
        )

        apply_he_dca_air_mounts(self.source_path, self.logger, self.game_db)
        air = self._mounted_list()[1].v
        self.assertIn(
            "WeaponShootData_0_2",
            str(air.by_m("WeaponShootDataPropertyName").v),
        )


class TestHeDcaAirDepiction(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger("test_he_dca_air_depiction")
        # Real ndf List supports by_n / insert / find_by_cond / row.index
        self.source_path = ndf.convert(_DEPICTION_NDF)
        self.game_db = {
            "he_dca_air_depiction_channels": {
                "M163_PIVADS_US": [
                    {
                        "ground_shoot": "WeaponShootData_0_1",
                        "air_shoot": "WeaponShootData_0_2",
                        "air_active": "WeaponActiveAndCanShoot_2",
                        "ground_ammo_ns": "Gatling_M61_Vulcan_20mm_late",
                    },
                ],
            },
        }

    def _registration(self):
        for row in self.source_path:
            if getattr(row.v, "type", None) == "TacticVehicleDepictionRegistration":
                return row
        return None

    def test_adds_air_operator_and_actions_entry(self):
        apply_he_dca_air_depiction_weapons(
            self.source_path, self.game_db, self.logger
        )

        air_op = self.source_path.by_n(
            "DepictionOperator_M163_PIVADS_US_Weapon1_AIR", False
        )
        self.assertIsNotNone(air_op)
        self.assertEqual(
            air_op.v.type, "DepictionOperator_WeaponContinuousFire"
        )
        self.assertEqual(
            strip_quotes(str(air_op.v.by_m("FireEffectTag").v)),
            "weapon_effet_tag2",
        )
        self.assertIn(
            "WeaponShootData_0_2",
            str(air_op.v.by_m("WeaponShootDataPropertyName").v),
        )
        self.assertEqual(
            strip_quotes(
                str(air_op.v.by_m("WeaponActiveAndCanShootPropertyName").v)
            ),
            "WeaponActiveAndCanShoot_2",
        )

        reg = self._registration()
        ops = [str(r.v) for r in reg.v.by_m("Operators").v]
        self.assertIn("DepictionOperator_M163_PIVADS_US_Weapon1_AIR", ops)
        ground_idx = ops.index("DepictionOperator_M163_PIVADS_US_Weapon1")
        air_idx = ops.index("DepictionOperator_M163_PIVADS_US_Weapon1_AIR")
        self.assertEqual(air_idx, ground_idx + 1)

        actions = str(reg.v.by_m("Actions").v)
        self.assertIn("weapon_effet_tag2", actions)
        self.assertIn("Weapon_Gatling_M61_Vulcan_20mm_late", actions)
        # Same FX asset reused; two tag entries
        self.assertEqual(actions.count("Weapon_Gatling_M61_Vulcan_20mm_late"), 2)

    def test_second_run_is_idempotent(self):
        apply_he_dca_air_depiction_weapons(
            self.source_path, self.game_db, self.logger
        )
        apply_he_dca_air_depiction_weapons(
            self.source_path, self.game_db, self.logger
        )
        air_ops = [
            r
            for r in self.source_path
            if (getattr(r, "namespace", None) or "").endswith("_AIR")
        ]
        self.assertEqual(len(air_ops), 1)
        actions = str(self._registration().v.by_m("Actions").v)
        self.assertEqual(actions.count("weapon_effet_tag2"), 1)


_SUBDEPICTION_NDF = """
DepictionOperator_Faun_Kraka_20mm_RFA_Weapon1 is DepictionOperator_WeaponContinuousFire
(
    FireEffectTag = "weapon_effet_tag1"
    Anchors = ["fx_tourelle1_tir_01"]
    WeaponShootDataPropertyName = "WeaponShootData_0_1"
    WeaponActiveAndCanShootPropertyName = "WeaponActiveAndCanShoot_1"
    NbFX = 1
)

unnamed TacticVehicleDepictionRegistration
(
    BlackHoleKey = 'Faun_Kraka_20mm_RFA'
    Selector = SpecificMechanicalDepictionSelector
    Alternatives = Alternatives_Faun_Kraka_20mm_RFA
    Operators =
    [
        DepictionOperator_CropFlattening,
        DepictionOperator_EjectableProps_Vehicle
    ]
    Actions = MAP[
            ]
            + DepictionAction_Stress_And_Wrecked
    SubDepictions = [
        TSubDepiction
        (
            Anchors = ["base_tourelle_01"]
            Depiction = TDepictionDescriptor
            (
                Operators = [
                    DepictionOperator_Turret_1_Aim,
                    DepictionOperator_Faun_Kraka_20mm_RFA_Weapon1,
                ]
                Actions = MAP[
                    ( "weapon_effet_tag1", Weapon_DCA_1_canon_FK20_20mm ),
                ]
            )
        ),
    ] + HumanSubDepictions_Faun_Kraka_20mm_RFA
)
"""


class TestHeDcaAirDepictionSubDepictions(unittest.TestCase):
    """Faun_Kraka-style: weapon FX lives under SubDepictions, not top-level."""

    def setUp(self):
        self.logger = logging.getLogger("test_he_dca_air_subdepiction")
        self.source_path = ndf.convert(_SUBDEPICTION_NDF)
        self.game_db = {
            "he_dca_air_depiction_channels": {
                "Faun_Kraka_20mm_RFA": [
                    {
                        "ground_shoot": "WeaponShootData_0_1",
                        "air_shoot": "WeaponShootData_0_2",
                        "air_active": "WeaponActiveAndCanShoot_2",
                        "ground_ammo_ns": "DCA_1_canon_FK20_20mm",
                    },
                ],
            },
        }

    def _registration(self):
        for row in self.source_path:
            if getattr(row.v, "type", None) == "TacticVehicleDepictionRegistration":
                return row
        return None

    def test_wires_air_into_nested_subdepiction(self):
        apply_he_dca_air_depiction_weapons(
            self.source_path, self.game_db, self.logger
        )

        air_op = self.source_path.by_n(
            "DepictionOperator_Faun_Kraka_20mm_RFA_Weapon1_AIR", False
        )
        self.assertIsNotNone(air_op)
        self.assertEqual(
            strip_quotes(str(air_op.v.by_m("FireEffectTag").v)),
            "weapon_effet_tag2",
        )

        reg = self._registration()
        top_ops = [str(r.v) for r in reg.v.by_m("Operators").v]
        self.assertNotIn(
            "DepictionOperator_Faun_Kraka_20mm_RFA_Weapon1_AIR", top_ops
        )

        sub = str(reg.v.by_m("SubDepictions").v)
        self.assertIn("DepictionOperator_Faun_Kraka_20mm_RFA_Weapon1_AIR", sub)
        self.assertIn("weapon_effet_tag2", sub)
        self.assertEqual(sub.count("Weapon_DCA_1_canon_FK20_20mm"), 2)

        # Top-level Actions stays empty of weapon tags
        top_actions = str(reg.v.by_m("Actions").v)
        self.assertNotIn("weapon_effet_tag2", top_actions)


if __name__ == "__main__":
    unittest.main()
