"""Top-level editor organization."""

from typing import Any, Callable, Dict, List

from gd_constants import edit_game_constants

from .effects import (
    edit_capacite_list,
    edit_shock_effects,
    edit_shock_effects_packs_list,
    edit_shock_units,
)
from .terrains import edit_terrains
from .ui.unit_info_panel import edit_unit_info_panel
from .unit_descriptor import (
    edit_antirad_optics,
    edit_auto_cover,
    edit_forward_deploy,
    edit_infantry_armor_wa,
    edit_team_supply,
)
from .veterancy import (
    edit_veterancy_effects,
    edit_veterancy_hints,
)
from .weapons.ammunition import edit_ammunition
from .weapons.damage_families import (
    add_damage_families_to_impl,
    add_damage_families_to_list,
    add_damage_resistance_values,
    apply_damage_families,
    apply_damage_family_edits,
    edit_infantry_armor,
)
from .weapons.missiles import edit_missiles
from .weapons.mortar_mods import add_radio_tag_to_mortars, edit_smoke_duration
from .weapons.unit_edits import edit_units


def get_editors(game_db: Dict[str, Any]) -> Dict[str, List[Callable]]:
    """Get all game file editors."""
    return {
        # Game constants
        "GameData/Gameplay/Constantes/GDConstantes.ndf": [
            lambda source: edit_game_constants(source),
        ],
        # Weapon-related files
        "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf": [
            lambda source: edit_units(source),
            lambda source: add_radio_tag_to_mortars(source, game_db),
            lambda source: edit_shock_units(source),
        ],
        "GameData/Generated/Gameplay/Gfx/Ammunition.ndf": [
            lambda source: edit_ammunition(source, game_db),
            lambda source: apply_damage_families(source, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf": [
            lambda source: edit_missiles(source, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf": [
            lambda source: edit_smoke_duration(source),
        ],
        # Damage system files
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyList.ndf": [
            lambda source: add_damage_families_to_list(source),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf": [
            lambda source: add_damage_families_to_impl(source),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistance.ndf": [
            lambda source: add_damage_resistance_values(source),
            lambda source: apply_damage_family_edits(source),
            lambda source: edit_infantry_armor(source),
        ],
        
        # Unit descriptor files
        "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf": [
            lambda source: edit_antirad_optics(source),
            lambda source: edit_forward_deploy(source),
            lambda source: edit_infantry_armor_wa(source),
            lambda source: edit_auto_cover(source),
        ],
        
        # Effects and veterancy files
        "GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf": [
            lambda source: edit_shock_effects(source),
            lambda source: edit_veterancy_effects(source),
        ],
        "GameData/Generated/Gameplay/Gfx/EffectsPacksList.ndf": [
            lambda source: edit_shock_effects_packs_list(source),
        ],
        "GameData/Generated/Gameplay/Gfx/CapaciteList.ndf": [
            lambda source: edit_capacite_list(source),
        ],
        "GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf": [
            lambda source: edit_veterancy_hints(source),
        ],
        
        # Other game files
        "GameData/Gameplay/Terrains/Terrains.ndf": [
            lambda source: edit_terrains(source),
        ],
        "GameData/Gameplay/Unit/Tactic/Team.ndf": [
            lambda source: edit_team_supply(source),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitInfoPanelView.ndf": [
            lambda source: edit_unit_info_panel(source),
        ],
    } 