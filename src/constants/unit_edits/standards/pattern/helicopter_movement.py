"""Pattern standard: THelicopterMovementModuleDescriptor manoeuvrability for helicopter units."""

from typing import TypedDict


class HelicopterMovementManoeuvrabilityPatternStandard(TypedDict):
    """Flat deltas for ``TorqueManoeuvrability`` and ``CyclicManoeuvrability``."""

    torque_flat_bonus: int
    cyclic_flat_bonus: int


HELICOPTER_MOVEMENT_MANOEUVRABILITY_PATTERN_STANDARD: HelicopterMovementManoeuvrabilityPatternStandard = {
    "torque_flat_bonus": 30,
    "cyclic_flat_bonus": 30,
}
