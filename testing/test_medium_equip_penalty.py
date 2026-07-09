"""Tests for medium/heavy equipment penalty capacities and effects."""

import unittest

from src.constants.capacities import (
    MEDIUM_EQUIP_PENALTY_CAPACITY,
    MEDIUM_EQUIP_PENALTY_CONDITIONS,
    MEDIUM_EQUIP_PENALTY_SF_CAPACITY,
)
from src.constants.effects import (
    MEDIUM_EQUIP_PENALTY_COHESION_FLOOR_VALUE,
    MEDIUM_EQUIP_PENALTY_EFFECT,
    MEDIUM_EQUIP_PENALTY_FLOOR_DAMAGE_LEVEL,
    MEDIUM_EQUIP_PENALTY_FLOOR_TAG_EFFECT,
    MEDIUM_EQUIP_PENALTY_SF_EFFECT,
    MEDIUM_EQUIP_PENALTY_SF_SUPPRESS_DAMAGE,
    MEDIUM_EQUIP_PENALTY_SUPPRESS_DAMAGE,
    MEDIUM_EQUIP_PENALTY_TICK_SECONDS,
    MEDIUM_EQUIP_PENALTY_TRAIT_SUPPRESS_LINE,
)
from src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers.tcapacite import (
    _resolve_medium_equip_penalty_capacity,
    _unit_has_specialty,
)


class TestMediumEquipPenalty(unittest.TestCase):
    def test_penalty_capacity_ticks_while_moving_and_blocks_on_floor_tag(self) -> None:
        self.assertIn("CapacityStackPolicy_always", MEDIUM_EQUIP_PENALTY_CAPACITY)
        self.assertIn(f"CastTime            = {MEDIUM_EQUIP_PENALTY_TICK_SECONDS:.2f}", MEDIUM_EQUIP_PENALTY_CAPACITY)
        self.assertIn("CapacityDuration   = 0.10", MEDIUM_EQUIP_PENALTY_CAPACITY)
        self.assertIn("~/ConditionInMovement", MEDIUM_EQUIP_PENALTY_CAPACITY)
        self.assertIn("~/ConditionTagNotRaisedInUnit_Medium_Equip_Penalty_floor_1", MEDIUM_EQUIP_PENALTY_CAPACITY)
        self.assertNotIn("Medium_Equip_Penalty_ok", MEDIUM_EQUIP_PENALTY_CAPACITY)
        self.assertNotIn("BonusDamage", MEDIUM_EQUIP_PENALTY_CAPACITY)

    def test_sf_penalty_capacity_matches_standard_conditions(self) -> None:
        self.assertIn("UnitEffect_Medium_Equip_Penalty_SF", MEDIUM_EQUIP_PENALTY_SF_CAPACITY)
        self.assertIn("~/ConditionInMovement", MEDIUM_EQUIP_PENALTY_SF_CAPACITY)
        self.assertIn("~/ConditionTagNotRaisedInUnit_Medium_Equip_Penalty_floor_1", MEDIUM_EQUIP_PENALTY_SF_CAPACITY)
        self.assertIn(f"CastTime            = {MEDIUM_EQUIP_PENALTY_TICK_SECONDS:.2f}", MEDIUM_EQUIP_PENALTY_SF_CAPACITY)

    def test_penalty_effect_inflicts_suppress_damage(self) -> None:
        self.assertIn("TEffectInflictDamageDescriptor", MEDIUM_EQUIP_PENALTY_EFFECT)
        self.assertIn(f"DamageValue = {MEDIUM_EQUIP_PENALTY_SUPPRESS_DAMAGE}", MEDIUM_EQUIP_PENALTY_EFFECT)
        self.assertIn("EDamageType/Suppress", MEDIUM_EQUIP_PENALTY_EFFECT)
        self.assertNotIn("TUnitEffectIncreaseDamageTakenDescriptor", MEDIUM_EQUIP_PENALTY_EFFECT)

    def test_sf_penalty_effect_inflicts_higher_suppress_damage(self) -> None:
        self.assertIn("TEffectInflictDamageDescriptor", MEDIUM_EQUIP_PENALTY_SF_EFFECT)
        self.assertIn(f"DamageValue = {MEDIUM_EQUIP_PENALTY_SF_SUPPRESS_DAMAGE}", MEDIUM_EQUIP_PENALTY_SF_EFFECT)
        self.assertIn("Medium_Equip_Penalty_SF", MEDIUM_EQUIP_PENALTY_SF_EFFECT)

    def test_floor_tag_effect_raises_cohesion_floor_tag(self) -> None:
        self.assertIn('"Medium_Equip_Penalty_floor"', MEDIUM_EQUIP_PENALTY_FLOOR_TAG_EFFECT)
        self.assertIn("TUnitEffectRaiseTagDescriptor", MEDIUM_EQUIP_PENALTY_FLOOR_TAG_EFFECT)

    def test_floor_damage_level_descriptor(self) -> None:
        self.assertIn(f"Value = {MEDIUM_EQUIP_PENALTY_COHESION_FLOOR_VALUE}", MEDIUM_EQUIP_PENALTY_FLOOR_DAMAGE_LEVEL)
        self.assertIn("UnitEffect_GroundUnit_Cohesion_Normal", MEDIUM_EQUIP_PENALTY_FLOOR_DAMAGE_LEVEL)
        self.assertIn("UnitEffect_Ajoute_Tag_Medium_Equip_Penalty_floor", MEDIUM_EQUIP_PENALTY_FLOOR_DAMAGE_LEVEL)

    def test_conditions_export_floor_tag_pair_only(self) -> None:
        self.assertEqual(len(MEDIUM_EQUIP_PENALTY_CONDITIONS), 2)
        conditions_text = "\n".join(MEDIUM_EQUIP_PENALTY_CONDITIONS)
        self.assertIn("ConditionTagRaisedInUnit_Medium_Equip_Penalty_floor_1", conditions_text)
        self.assertIn("ConditionTagNotRaisedInUnit_Medium_Equip_Penalty_floor_1", conditions_text)
        self.assertNotIn("Medium_Equip_Penalty_ok", conditions_text)

    def test_trait_suppress_line_uses_constants(self) -> None:
        self.assertIn(str(MEDIUM_EQUIP_PENALTY_SUPPRESS_DAMAGE), MEDIUM_EQUIP_PENALTY_TRAIT_SUPPRESS_LINE)
        self.assertIn(str(100 - int(MEDIUM_EQUIP_PENALTY_COHESION_FLOOR_VALUE * 100)), MEDIUM_EQUIP_PENALTY_TRAIT_SUPPRESS_LINE)
        self.assertIn("while moving", MEDIUM_EQUIP_PENALTY_TRAIT_SUPPRESS_LINE)
        self.assertNotIn("after stopping", MEDIUM_EQUIP_PENALTY_TRAIT_SUPPRESS_LINE)

    def test_unit_has_specialty_from_database_or_edits(self) -> None:
        unit_data = {"specialties": ["_sf", "infantry_equip_medium"]}
        self.assertTrue(_unit_has_specialty(unit_data, "unit_edits", {}, "_sf"))
        self.assertFalse(_unit_has_specialty(unit_data, "unit_edits", {}, "_para"))
        edits = {"SpecialtiesList": {"add_specs": ["'_sf'"]}}
        self.assertTrue(_unit_has_specialty(None, "unit_edits", edits, "_sf"))

    def test_resolve_medium_equip_penalty_capacity_for_sf_units(self) -> None:
        unit_data = {"specialties": ["_sf", "infantry_equip_medium"]}
        self.assertEqual(
            _resolve_medium_equip_penalty_capacity("Medium_Equip_Penalty", unit_data, "unit_edits", {}),
            "Medium_Equip_Penalty_SF",
        )
        self.assertEqual(
            _resolve_medium_equip_penalty_capacity(
                "$/GFX/EffectCapacity/Capacite_Medium_Equip_Penalty",
                unit_data,
                "unit_edits",
                {},
            ),
            "$/GFX/EffectCapacity/Capacite_Medium_Equip_Penalty_SF",
        )
        self.assertEqual(
            _resolve_medium_equip_penalty_capacity("Medium_Equip_Penalty", None, "unit_edits", {}),
            "Medium_Equip_Penalty",
        )


if __name__ == "__main__":
    unittest.main()
