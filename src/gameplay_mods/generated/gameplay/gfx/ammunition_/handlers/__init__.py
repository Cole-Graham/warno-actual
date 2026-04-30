from .damage_families import (
    apply_damage_families,
)
from .fire_descriptors import (
    apply_fire_descriptors,
)
from .he_dca_air_clones import (
    apply_he_dca_air_ammo_clones,
)
from .mortars import (
    add_corrected_shot_dispersion,
)
from .bomb_category_standards import (
    apply_category_bomb_standards,
)
from .aa_missile_category_standards import (
    apply_category_aa_missile_standards,
)
from .sead_category_standards import (
    apply_category_sead_standards,
)
from .standards import (
    apply_aim_time_standards,
    apply_he_damage_standards,
    apply_weapon_range_standards,
    apply_bomb_damage_standards,
    apply_clu_sol_trait_standards,
    apply_infantry_mmg_cac_trait,
)
from .vanilla_renames import (
    remove_vanilla_instances,
    vanilla_renames_ammunition,
)

__all__ = [
    'add_corrected_shot_dispersion',
    'apply_category_aa_missile_standards',
    'apply_category_bomb_standards',
    'apply_category_sead_standards',
    'apply_aim_time_standards',
    'apply_bomb_damage_standards',
    'apply_clu_sol_trait_standards',
    'apply_damage_families',
    'apply_fire_descriptors',
    'apply_he_dca_air_ammo_clones',
    'apply_infantry_mmg_cac_trait',
    'apply_he_damage_standards',
    'apply_weapon_range_standards',
    'remove_vanilla_instances',
    'vanilla_renames_ammunition',
]