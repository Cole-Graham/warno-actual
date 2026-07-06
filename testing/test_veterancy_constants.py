"""Tests for veterancy constants builders and coverage."""

from __future__ import annotations

import unittest

from src.constants.effects.veterancy.build import (
    SEMANTIC_FIELD_TO_PATCH_KEYS,
    _effect_pack_for_level,
    _level_patches,
)
from src.constants.effects.veterancy.effect_packs import (
    EFFECT_PACK_BY_PACK_TYPE,
    HELO_ATTACK_EFFECT_GUIDS,
    MULTIPLICATIVE_INFANTRY_GUIDS,
    POST_PATCH_OVERRIDES,
)
from src.constants.effects.veterancy.levels import (
    AVION_VET_REBALANCE_ENABLED,
    EXTRA_LEVEL_ENTRIES,
    PACK_CONFIGS,
    PACK_LEVELS,
)
from src.constants.effects.veterancy.ui_text import build_veterancy_ui_bodies
from src.constants.effects.veterancy import (
    VETERANCY_BONUSES,
    VETERANCY_EFFECT_CHANGES,
    VETERANCY_HELO_ATTACK_EFFECT_CHANGES,
    VETERANCY_RUNTIME_EFFECT_CHANGES,
)


class TestVeterancyConstants(unittest.TestCase):
    def test_bonuses_have_tokens_and_bodies(self) -> None:
        for pack_type, levels in VETERANCY_BONUSES.items():
            for level_key, data in levels.items():
                self.assertTrue(data["body_token"], f"{pack_type}/{level_key} missing token")
                self.assertTrue(data["body"], f"{pack_type}/{level_key} missing body")

    def test_effect_change_keys_unique(self) -> None:
        all_keys = (
            list(VETERANCY_EFFECT_CHANGES)
            + list(VETERANCY_HELO_ATTACK_EFFECT_CHANGES)
            + list(VETERANCY_RUNTIME_EFFECT_CHANGES)
        )
        self.assertEqual(len(all_keys), len(set(all_keys)))

    def test_runtime_packs_excluded_from_main_changes(self) -> None:
        self.assertNotIn("UnitEffect_xp_elite_helo_SF", VETERANCY_EFFECT_CHANGES)
        self.assertIn("UnitEffect_xp_elite_helo_SF", VETERANCY_RUNTIME_EFFECT_CHANGES)
        runtime = VETERANCY_RUNTIME_EFFECT_CHANGES["UnitEffect_xp_elite_helo_SF"]
        self.assertEqual(runtime["TUnitEffectIncreaseSpeedDescriptor"], 30)
        self.assertEqual(
            runtime["TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor"],
            0.7,
        )

    def test_helo_attack_guids_complete(self) -> None:
        self.assertEqual(len(HELO_ATTACK_EFFECT_GUIDS), 4)
        for ns in EFFECT_PACK_BY_PACK_TYPE["helico_attack"]:
            self.assertIn(ns, HELO_ATTACK_EFFECT_GUIDS)

    def test_multiplicative_infantry_guids_complete(self) -> None:
        self.assertEqual(len(MULTIPLICATIVE_INFANTRY_GUIDS), 7)

    def test_semantic_fields_emit_patches(self) -> None:
        patchable_pack_types = ("simple_v3", "SF_v2", "artillery", "helico", "avion")
        for pack_type in patchable_pack_types:
            pack_config = PACK_CONFIGS[pack_type]
            for level_index, level in enumerate(PACK_LEVELS[pack_type]):
                effect_pack = _effect_pack_for_level(pack_type, level_index, level)
                if effect_pack is None:
                    continue
                patches = _level_patches(level, pack_config)
                if not patches:
                    continue
                effect_changes = VETERANCY_EFFECT_CHANGES.get(effect_pack, {})
                for field_name, patch_keys in SEMANTIC_FIELD_TO_PATCH_KEYS.items():
                    if getattr(level, field_name) is None:
                        continue
                    if field_name == "evasion_pct" and level.add_evasion_descriptor:
                        self.assertIn("add", effect_changes, f"{effect_pack} missing add evasion")
                        continue
                    matched = any(key in effect_changes for key in patch_keys)
                    self.assertTrue(
                        matched,
                        f"{effect_pack} missing patch for {field_name}",
                    )

    def test_stress_recovery_matches_ui(self) -> None:
        for pack_type, levels in PACK_LEVELS.items():
            if pack_type.endswith("_multiplicative"):
                continue
            pack_config = PACK_CONFIGS.get(pack_type)
            if pack_config is None:
                continue
            for level_index, level in enumerate(levels):
                if level.stress_recovery is None:
                    continue
                ui_entry = VETERANCY_BONUSES.get(pack_type, {}).get(level.level_key)
                if ui_entry is None:
                    continue
                self.assertIn(
                    str(level.stress_recovery).rstrip("0").rstrip("."),
                    ui_entry["body"].replace(" per second", ""),
                    msg=f"{level.level_key} stress recovery UI mismatch",
                )

    def test_simple_v3_elite_stress_recovery_resolved(self) -> None:
        elite = VETERANCY_EFFECT_CHANGES["UnitEffect_xp_elite"]
        self.assertEqual(elite["TUnitEffectHealOverTimeDescriptor"], 5.4)

    def test_sf_trained_matches_legacy_overrides(self) -> None:
        trained_sf = VETERANCY_EFFECT_CHANGES["UnitEffect_xp_trained_SF"]
        self.assertEqual(trained_sf["TUnitEffectHealOverTimeDescriptor"], 6.0)
        self.assertEqual(
            trained_sf["TUnitEffectIncreaseWeaponPrecisionArretDescriptor"],
            10,
        )

    def test_ui_bodies_cover_all_levels(self) -> None:
        ui_bodies = build_veterancy_ui_bodies()
        for pack_type, levels in PACK_LEVELS.items():
            for level in levels:
                self.assertIn(pack_type, ui_bodies)
                self.assertIn(
                    level.level_key,
                    ui_bodies[pack_type],
                    f"Missing UI body for {pack_type}/{level.level_key}",
                )

        for pack_type, extra_level in EXTRA_LEVEL_ENTRIES:
            self.assertIn(extra_level.level_key, ui_bodies[pack_type])

    def test_ui_values_match_level_constants(self) -> None:
        ui_bodies = build_veterancy_ui_bodies()
        trained = PACK_LEVELS["simple_v3"][1]
        body = ui_bodies["simple_v3"]["simple_v3_1"]
        self.assertIn(f"+{trained.accuracy_pct}%", body)
        self.assertIn(f"-{trained.aim_time_reduction_pct}%", body)
        self.assertIn(f"+{trained.stress_resistance_pct}%", body)
        self.assertIn("4.0", body)

    def test_extra_helico_sf_level_in_bonuses(self) -> None:
        self.assertIn("helico_SF_3", VETERANCY_BONUSES["helico"])
        self.assertIn("+30%", VETERANCY_BONUSES["helico"]["helico_SF_3"]["body"])

    def test_avion_vet_rebalance_toggle(self) -> None:
        veteran_avion = VETERANCY_EFFECT_CHANGES["UnitEffect_xp_veteran_avion"]
        elite_avion = VETERANCY_EFFECT_CHANGES["UnitEffect_xp_elite_avion"]
        avion_veteran_body = VETERANCY_BONUSES["avion"]["avion_2"]["body"]
        avion_elite_body = VETERANCY_BONUSES["avion"]["avion_3"]["body"]
        avion_rookie_body = VETERANCY_BONUSES["avion"]["avion_0"]["body"]

        remove_evasion_packs = {
            override.effect_pack
            for override in POST_PATCH_OVERRIDES
            if override.remove_evasion_descriptor
        }

        if AVION_VET_REBALANCE_ENABLED:
            self.assertEqual(
                veteran_avion["TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor"],
                9,
            )
            self.assertEqual(
                elite_avion["TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor"],
                18,
            )
            self.assertNotIn(
                "TUnitEffectBonusPrecisionWhenTargetedDescriptor",
                veteran_avion,
            )
            self.assertNotIn(
                "TUnitEffectBonusPrecisionWhenTargetedDescriptor",
                elite_avion,
            )
            self.assertIn("UnitEffect_xp_veteran_avion", remove_evasion_packs)
            self.assertIn("UnitEffect_xp_elite_avion", remove_evasion_packs)
            self.assertIn("+9%", avion_veteran_body)
            self.assertIn("+18%", avion_elite_body)
            self.assertNotIn("Evasive", avion_rookie_body)
            self.assertNotIn("Evasive", avion_veteran_body)
            self.assertNotIn("Evasive", avion_elite_body)
        else:
            self.assertEqual(
                veteran_avion["TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor"],
                4,
            )
            self.assertEqual(
                elite_avion["TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor"],
                8,
            )
            self.assertEqual(
                veteran_avion["TUnitEffectBonusPrecisionWhenTargetedDescriptor"],
                -4,
            )
            self.assertEqual(
                elite_avion["TUnitEffectBonusPrecisionWhenTargetedDescriptor"],
                -8,
            )
            self.assertNotIn("UnitEffect_xp_veteran_avion", remove_evasion_packs)
            self.assertNotIn("UnitEffect_xp_elite_avion", remove_evasion_packs)
            self.assertIn("+4%", avion_veteran_body)
            self.assertIn("+8%", avion_elite_body)
            self.assertIn("Evasive maneuvers", avion_rookie_body)
            self.assertIn("Evasive maneuvers", avion_veteran_body)
            self.assertIn("Evasive maneuvers", avion_elite_body)


if __name__ == "__main__":
    unittest.main()
