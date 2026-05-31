"""Shared constants for TSupplyModuleDescriptor unit edits."""

from __future__ import annotations

from typing import Optional

SUPPLY_DESCRIPTOR_SPECIALTIES = {
    "RunnerSupply": "_supply_runner",
    "RunnerHeloSupply": "_supply_runner_helo",
    "SquadSupply": "_supply_squad",
    "PrimarySupply": "_supply_primary",
    "PrimaryHeloSupply": "_supply_primary_helo",
    "DvisionalSupply": "_supply_divisional",
    "DvisionalHeloSupply": "_supply_divisional_helo",
}


def specialty_for_supply_descriptor(descriptor: str) -> Optional[str]:
    """Return UI specialty tag for a supply descriptor short name."""
    return SUPPLY_DESCRIPTOR_SPECIALTIES.get(descriptor)
