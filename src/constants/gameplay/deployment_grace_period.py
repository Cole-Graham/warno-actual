"""Deployment grace period constants for GamePhaseDescriptorTactical.ndf."""

DEPLOYMENT_GRACE_PERIOD_NOT_SPECIFIED = {
    "timer_seconds": 60,
    "steps": [
        (80, 6),
        (120, 5),
        (160, 4),
        (200, 3),
        (240, 2),
        (-1, 1),
    ],
}
