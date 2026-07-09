"""Tests for satchel AT companion mount auto-wiring."""

import logging
import unittest

from src import ndf
from src.gameplay_mods.generated.gameplay.gfx.weapon_descriptor.handlers.satchel_at_companion_mounts import (
    apply_satchel_at_companion_mounts,
)

_WEAPON_DESCR_NDF = """
export WeaponDescriptor_Test_US is TWeaponManagerModuleDescriptor
(
    Salves = [6]
    TurretDescriptorList =
    [
        TTurretInfanterieDescriptor
        (
            MountedWeaponDescriptorList =
            [
                TMountedWeaponDescriptor
                (
                    AmmoBoxIndex = 2
                    Ammunition = $/GFX/Weapon/Ammo_Grenade_Satchel_Charge
                    AnimateOnlyOneSoldier = True
                    EffectTag = 'FireEffect_Grenade_Satchel_Charge'
                    HandheldEquipmentKey = 'WeaponAlternative_3'
                    NbWeapons = 1
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_3'
                    WeaponIgnoredPropertyName = 'WeaponIgnored_3'
                    WeaponShootDataPropertyName = ['WeaponShootData_0_3']
                )
            ]
            YulBoneOrdinal = 3
        )
    ]
)
"""


class _FakeSourcePath:
    def __init__(self, rows):
        self._rows = rows

    def __iter__(self):
        return iter(self._rows)


class TestSatchelAtCompanionMounts(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger("test_satchel_at")
        self.weapon_descr = ndf.convert(_WEAPON_DESCR_NDF)[0]
        self.source_path = _FakeSourcePath([self.weapon_descr])

    def _mounted_list(self):
        turret = self.weapon_descr.v.by_m("TurretDescriptorList").v[0]
        return turret.v.by_m("MountedWeaponDescriptorList").v

    def test_adds_at_companion_with_same_turret_properties(self):
        apply_satchel_at_companion_mounts(self.source_path, self.logger, {})

        mounts = self._mounted_list()
        self.assertEqual(len(mounts), 2)

        donor = mounts[0].v
        companion = mounts[1].v
        self.assertEqual(
            donor.by_m("Ammunition").v,
            "$/GFX/Weapon/Ammo_Grenade_Satchel_Charge",
        )
        self.assertEqual(
            companion.by_m("Ammunition").v,
            "$/GFX/Weapon/Ammo_Grenade_Satchel_Charge_AT",
        )
        self.assertEqual(donor.by_m("AmmoBoxIndex").v, companion.by_m("AmmoBoxIndex").v)
        self.assertEqual(
            donor.by_m("HandheldEquipmentKey").v,
            companion.by_m("HandheldEquipmentKey").v,
        )
        self.assertEqual(
            donor.by_m("WeaponActiveAndCanShootPropertyName").v,
            companion.by_m("WeaponActiveAndCanShootPropertyName").v,
        )
        self.assertEqual(
            donor.by_m("WeaponIgnoredPropertyName").v,
            companion.by_m("WeaponIgnoredPropertyName").v,
        )
        self.assertEqual(
            donor.by_m("EffectTag").v,
            companion.by_m("EffectTag").v,
        )

    def test_ignores_non_grenade_donors(self):
        ndf_with_rifle = """
export WeaponDescriptor_Test_US is TWeaponManagerModuleDescriptor
(
    Salves = [11]
    TurretDescriptorList =
    [
        TTurretInfanterieDescriptor
        (
            MountedWeaponDescriptorList =
            [
                TMountedWeaponDescriptor
                (
                    AmmoBoxIndex = 0
                    Ammunition = $/GFX/Weapon/Ammo_FM_M16_strength10_x8
                    AnimateOnlyOneSoldier = False
                    EffectTag = 'FireEffect_FM_M16'
                    HandheldEquipmentKey = 'WeaponAlternative_1'
                    NbWeapons = 8
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_1'
                    WeaponIgnoredPropertyName = 'WeaponIgnored_1'
                    WeaponShootDataPropertyName = ['WeaponShootData_0_1']
                )
            ]
            YulBoneOrdinal = 1
        )
    ]
)
"""
        weapon_descr = ndf.convert(ndf_with_rifle)[0]
        source_path = _FakeSourcePath([weapon_descr])

        apply_satchel_at_companion_mounts(source_path, self.logger, {})

        turret = weapon_descr.v.by_m("TurretDescriptorList").v[0]
        self.assertEqual(len(turret.v.by_m("MountedWeaponDescriptorList").v), 1)

    def test_second_run_is_idempotent(self):
        apply_satchel_at_companion_mounts(self.source_path, self.logger, {})
        apply_satchel_at_companion_mounts(self.source_path, self.logger, {})
        self.assertEqual(len(self._mounted_list()), 2)


if __name__ == "__main__":
    unittest.main()
