from .damage_families import (
    apply_damage_families,
)
from .fire_descriptors import (
    apply_fire_descriptors,
)
from .mortars import (
    add_corrected_shot_dispersion,
)
from .standards import (
    apply_aim_time_standards,
    apply_he_damage_standards,
    apply_weapon_range_standards,
    apply_bomb_damage_standards,
)
from .vanilla_renames import (
    remove_vanilla_instances,
    vanilla_renames_ammunition,
)

__all__ = [
    'add_corrected_shot_dispersion',
    'apply_aim_time_standards',
    'apply_bomb_damage_standards',
    'apply_damage_families',
    'apply_fire_descriptors',
    'apply_he_damage_standards',
    'apply_weapon_range_standards',
    'remove_vanilla_instances',
    'vanilla_renames_ammunition',
]