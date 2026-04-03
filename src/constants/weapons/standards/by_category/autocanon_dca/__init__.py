"""Autocannon DCA ammunition category standards (one module per category string).

``hit_roll`` is applied in Ammunition.ndf editing; ``experience_unit`` is applied to
``TExperienceModuleDescriptor`` on every unit whose ``WeaponDescriptor`` mounts DCA ammo.
"""

from ..types import DcaCategoryStandardEntry

# Applied to all weapons whose ammunition dictionary key uses category "DCA" (autocanon_dca.py).
DCA_STANDARDS: DcaCategoryStandardEntry = {
    "hit_roll": {
        "DistanceToTarget": False,
    },
    "experience_unit": {
        "ExperienceMultiplierBonusOnKill": 0.1,
    },
}

__all__ = [
    "DCA_STANDARDS",
]
