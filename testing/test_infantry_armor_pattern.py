"""Tests for infantry WA armor pattern helpers."""

import unittest
from unittest.mock import MagicMock, patch

from src.constants.unit_edits.standards.pattern.infantry_armor import (
    EXCLUDED_AT_TEAM_TAG,
    EXCLUDED_WEAPON_TEAM_PREFIXES,
    INFANTRY_ARMOR_PATTERN_STANDARD,
    INFANTRY_WA_ARMOR_FAMILY,
    VANILLA_INFANTRY_ARMOR_FAMILY,
    infantry_wa_armor_index,
    is_excluded_hmg_team_unit,
)
from src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers.infantry_armor import (
    _collect_tag_strings,
    apply_wa_armor_to_damage_module,
    should_apply_infantry_wa_armor,
)


class TestInfantryArmorPatternHelpers(unittest.TestCase):
    def test_index_formula(self):
        self.assertEqual(infantry_wa_armor_index(10), 5)
        self.assertEqual(infantry_wa_armor_index(8), 7)
        self.assertEqual(infantry_wa_armor_index(14), 1)
        self.assertEqual(infantry_wa_armor_index(15), 1)
        self.assertEqual(infantry_wa_armor_index(20), 1)
        self.assertEqual(infantry_wa_armor_index(5), 10)

    def test_excluded_hmg_teams_by_prefix(self):
        self.assertTrue(is_excluded_hmg_team_unit("HMGteam_M60_US"))
        self.assertTrue(is_excluded_hmg_team_unit("MMGteam_MG3_RFA"))
        self.assertFalse(is_excluded_hmg_team_unit("ATteam_TOW_US"))
        self.assertFalse(is_excluded_hmg_team_unit("RCL_L6_Wombat_UK"))
        self.assertFalse(is_excluded_hmg_team_unit("MANPAD_Stinger_C_US"))
        self.assertFalse(is_excluded_hmg_team_unit("Rifles_US"))
        self.assertEqual(
            tuple(INFANTRY_ARMOR_PATTERN_STANDARD["excluded_prefixes"]),
            EXCLUDED_WEAPON_TEAM_PREFIXES,
        )
        self.assertEqual(
            INFANTRY_ARMOR_PATTERN_STANDARD["excluded_at_team_tag"],
            EXCLUDED_AT_TEAM_TAG,
        )

    def test_should_apply_excludes_infanterie_at_tag(self):
        modules_list = MagicMock()
        with patch(
            "src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers"
            ".infantry_armor.live_tagset",
            return_value={"Infanterie", "Infanterie_AT"},
        ):
            self.assertFalse(
                should_apply_infantry_wa_armor(
                    "RCL_L6_Wombat_UK", modules_list, set(),
                ),
            )
            self.assertFalse(
                should_apply_infantry_wa_armor(
                    "ATteam_TOW_US", modules_list, set(),
                ),
            )

    def test_should_apply_includes_manpad_and_squads(self):
        modules_list = MagicMock()
        with patch(
            "src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers"
            ".infantry_armor.live_tagset",
            return_value={"Infanterie", "Infanterie_AA"},
        ):
            self.assertTrue(
                should_apply_infantry_wa_armor(
                    "MANPAD_Stinger_C_US", modules_list, set(),
                ),
            )
        with patch(
            "src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers"
            ".infantry_armor.live_tagset",
            return_value={"Infanterie"},
        ):
            self.assertTrue(
                should_apply_infantry_wa_armor(
                    "Rifles_US", modules_list, set(),
                ),
            )
            self.assertFalse(
                should_apply_infantry_wa_armor(
                    "Rifles_US", modules_list, {"Rifles_US"},
                ),
            )
            self.assertFalse(
                should_apply_infantry_wa_armor(
                    "HMGteam_M60_US", modules_list, set(),
                ),
            )

    def test_should_apply_requires_infanterie_tag(self):
        modules_list = MagicMock()
        with patch(
            "src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers"
            ".infantry_armor.live_tagset",
            return_value=set(),
        ):
            self.assertFalse(
                should_apply_infantry_wa_armor(
                    "Rifles_US", modules_list, set(),
                ),
            )

    def test_apply_wa_armor_rewrites_vanilla_and_skips_kinetic(self):
        def make_resistance(family: str):
            family_row = MagicMock()
            family_row.v = family
            index_row = MagicMock()
            index_row.v = "1"
            resistance = MagicMock()
            resistance.v.by_m.side_effect = lambda name, *a, **k: (
                family_row if name == "Family"
                else index_row if name == "Index"
                else None
            )
            return resistance, family_row, index_row

        parts = {}
        for part in (
            "ResistanceFront",
            "ResistanceSides",
            "ResistanceRear",
            "ResistanceTop",
        ):
            parts[part] = make_resistance(VANILLA_INFANTRY_ARMOR_FAMILY)

        parts["ResistanceTop"] = make_resistance("ResistanceFamily_Kinetic")

        blindage = MagicMock()
        blindage.v.by_m.side_effect = lambda name, *a, **k: (
            parts[name][0] if name in parts else None
        )

        damage_module = MagicMock()
        damage_module.v.by_m.side_effect = lambda name, *a, **k: (
            blindage if name == "BlindageProperties" else None
        )

        self.assertTrue(apply_wa_armor_to_damage_module(damage_module, 10))
        for part in ("ResistanceFront", "ResistanceSides", "ResistanceRear"):
            _, family_row, index_row = parts[part]
            self.assertEqual(family_row.v, INFANTRY_WA_ARMOR_FAMILY)
            self.assertEqual(index_row.v, "5")
        _, top_family, top_index = parts["ResistanceTop"]
        self.assertEqual(top_family.v, "ResistanceFamily_Kinetic")
        self.assertEqual(top_index.v, "1")

    def test_collect_tags_flattens_overwrite_all_nested_list(self):
        """TagSet.overwrite_all uses ndf.convert(str(list)) which nests a List."""
        from src import ndf

        nested = ndf.convert(
            str(["AllUnits", "Infanterie", "Infanterie_AT", "Unite"]),
        )
        tags = _collect_tag_strings(nested)
        self.assertEqual(
            tags,
            {"AllUnits", "Infanterie", "Infanterie_AT", "Unite"},
        )


if __name__ == "__main__":
    unittest.main()
