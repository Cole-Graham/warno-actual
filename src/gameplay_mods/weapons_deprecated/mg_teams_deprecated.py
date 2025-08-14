"""Functions for modifying MG team weapons."""

from typing import Any, Dict

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


# def edit_mg_team_weapons(source: Any, game_db: Dict[str, Any]) -> None:
#     """Edit MG team weapon properties."""
#     ammo_db = game_db["ammunition"]

#     for weapon_descr in source:
#         name = weapon_descr.n

#         if name in ammo_db["mg_categories"]["coax_mmgs"]:
#             _modify_coax_mmg(weapon_descr, name)
#         elif name in ammo_db["mg_categories"]["hmg_teams"]:
#             _modify_hmg_team(weapon_descr, name, ammo_db["mg_categories"]["hmg_exceptions"])
#         elif name in ammo_db["mg_categories"]["mmg_teams"]:
#             _modify_mmg_team(weapon_descr, name)
#         elif name in ammo_db["mg_categories"]["hmg_turrets"]:
#             _modify_hmg_turret(weapon_descr, name)
#         elif name in ammo_db["mg_categories"]["mmg_turrets"]:
#             _modify_mmg_turret(weapon_descr, name)


# def _modify_coax_mmg(weapon_descr, name: str) -> None:
#     """Apply coax MMG modifications."""
#     membr = weapon_descr.v.by_m

#     membr("MaximumRangeGRU").v = "1050"
#     logger.info(f"Changed {name} ground range to 1050")

#     _apply_common_mods(
#         weapon_descr,
#         name,
#         {
#             "hit_roll": {
#                 "Idling": 45,
#                 "Moving": 30,
#             },
#             "PhysicalDamages": "0.08",
#             "SuppressDamages": "24",
#             "TimeBetweenTwoSalvos": "2.0",
#             "NbTirParSalves": "5",
#             "SupplyCost": "1.0",
#             "AffichageMunitionParSalve": "25",
#         },
#     )


# def _modify_mmg_team(weapon_descr, name: str) -> None:
#     """Apply MMG team modifications."""
#     membr = weapon_descr.v.by_m

#     membr("MaximumRangeGRU").v = "1050"
#     logger.info(f"Changed {name} ground range to 1050")

#     if membr("MaximumRangeHelicopterGRU", False):
#         membr("MaximumRangeHelicopterGRU").v = "875"
#         logger.info(f"Changed {name} helo range to 875")

#     _apply_common_mods(
#         weapon_descr,
#         name,
#         {
#             "PhysicalDamages": "0.08",
#             "SuppressDamages": "24",
#             "TimeBetweenTwoSalvos": "2.0",
#             "NbTirParSalves": "5",
#             "SupplyCost": "1.0",
#             "AffichageMunitionParSalve": "25",
#         },
#     )


# def _modify_mmg_turret(weapon_descr, name: str) -> None:
#     """Apply MMG turret modifications."""
#     membr = weapon_descr.v.by_m

#     membr("MaximumRangeGRU").v = "1050"
#     if membr("MaximumRangeHelicopterGRU", False):
#         membr("MaximumRangeHelicopterGRU").v = "875"

#     _apply_common_mods(
#         weapon_descr,
#         name,
#         {
#             "PhysicalDamages": "0.08",
#             "SuppressDamages": "24",
#             "TimeBetweenTwoSalvos": "2.0",
#             "NbTirParSalves": "5",
#             "SupplyCost": "1.0",
#             "AffichageMunitionParSalve": "25",
#         },
#     )


# def _modify_hmg_team(weapon_descr, name: str, exceptions: list) -> None:
#     """Apply HMG team modifications."""
#     membr = weapon_descr.v.by_m

#     membr("MaximumRangeGRU").v = "1225"
#     logger.info(f"Changed {name} ground range to 1225")

#     if membr("MaximumRangeHelicopterGRU", False) and name not in exceptions:
#         membr("MaximumRangeHelicopterGRU").v = "1050"
#         logger.info(f"Changed {name} helo range to 1050")

#     # Apply other modifications...
#     _apply_common_mods(
#         weapon_descr,
#         name,
#         {
#             "Arme": {
#                 "Family": "DamageFamily_12_7",
#             },
#             "PhysicalDamages": "0.28",
#             "SuppressDamages": "84",
#             "TimeBetweenTwoSalvos": "2.4",
#             "NbTirParSalves": "5",
#             "SupplyCost": "3.0",
#             "AffichageMunitionParSalve": "25",
#         },
#     )


# def _modify_hmg_turret(weapon_descr, name: str) -> None:
#     """Apply HMG turret modifications."""
#     membr = weapon_descr.v.by_m

#     membr("MaximumRangeGRU").v = "1225"
#     membr("MaximumRangeHelicopterGRU").v = "1050"

#     _apply_common_mods(
#         weapon_descr,
#         name,
#         {
#             "Arme": {
#                 "Family": "DamageFamily_12_7",
#             },
#             "PhysicalDamages": "0.14",
#             "SuppressDamages": "42",
#             "TimeBetweenTwoSalvos": "2.4",
#             "NbTirParSalves": "5",
#             "SupplyCost": "2.0",
#             "AffichageMunitionParSalve": "25",
#         },
#     )


# def _apply_common_mods(weapon_descr, name: str, mods: dict) -> None:
#     """Apply common modifications to a weapon."""
#     membr = weapon_descr.v.by_m

#     for key, value in mods.items():
#         if key == "Arme":
#             arme_membr = membr("Arme")
#             arme_membr.v.by_m("Family").v = value["Family"]
#         elif key == "hit_roll":
#             hitroll_obj = membr("HitRollRuleDescriptor").v
#             modifiers = hitroll_obj.by_m("BaseHitValueModifiers").v
#             if "Idling" in value:
#                 modifiers[1].v = (modifiers[1].v[0], str(value["Idling"]))
#             if "Moving" in value:
#                 modifiers[2].v = (modifiers[2].v[0], str(value["Moving"]))
#         else:
#             membr(key).v = value
#             logger.info(f"Changed {name} {key} to {value}")

#     # Apply standard hit roll
#     if "hit_roll" not in mods:
#         hitroll_obj = membr("HitRollRuleDescriptor").v
#         hitroll_list = hitroll_obj.by_m("BaseHitValueModifiers").v
#         roll_membr_list = list(hitroll_list[1].v)
#         roll_membr_list[1] = "35"
#         hitroll_list[1].v = tuple(roll_membr_list)
#         logger.info(f"Changed {name} accuracy: {roll_membr_list}")
