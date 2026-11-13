"""Mounted-weapon identity overlay: donor copy, trait edit, salvo fallback."""

import unittest

from src.data.mounted_weapon_identity import (
    copy_identity,
    resolve_identity,
    store_identity_value,
)


class TestMountedWeaponIdentity(unittest.TestCase):
    def test_copy_then_trait_edit_does_not_change_donor(self):
        ammo_db = {
            "mounted_identity": {
                "Ammo_Donor": {"TraitsToken": ["'STAT'", "'HEAT'"], "Name": "'DONOR'"},
            },
        }
        copy_identity(ammo_db, "Ammo_Donor", "Ammo_New_salvolength4")
        edited = resolve_identity(ammo_db, "Ammo_New_salvolength4")
        store_identity_value(edited, "TraitsToken", ["STAT", "TANDEM"])

        self.assertEqual(
            ammo_db["mounted_identity"]["Ammo_Donor"]["TraitsToken"],
            ["'STAT'", "'HEAT'"],
        )
        self.assertEqual(edited["TraitsToken"], ["'STAT'", "'TANDEM'"])
        self.assertEqual(edited["Name"], "'DONOR'")

    def test_salvolength_without_own_record_uses_base(self):
        ammo_db = {
            "mounted_identity": {
                "Ammo_RocketInf_RPG7": {"Caliber": "'RPG'", "TraitsToken": ["'HEAT'"]},
            },
        }
        resolved = resolve_identity(ammo_db, "Ammo_RocketInf_RPG7_salvolength6")
        self.assertEqual(resolved["Caliber"], "'RPG'")
        self.assertEqual(resolved["TraitsToken"], ["'HEAT'"])


if __name__ == "__main__":
    unittest.main()
