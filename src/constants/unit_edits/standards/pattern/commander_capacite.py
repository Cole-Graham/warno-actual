"""Pattern standard: replace TCommanderModuleDescriptor with CMD/LDR Capacites."""

from typing import AbstractSet, Optional, TypedDict

CMD_UNIT_CAPACITY_NAME = "CMD_UNIT"
LDR_INF_CAPACITY_NAME = "LDR_INF"

CMD_UNIT_TAG = "CMD_Unit"
INFANTERIE_TAG = "Infanterie"
LDR_UNIT_TAGS: frozenset[str] = frozenset({"LDR_Unit", "LDR_SOV_Unit"})
LDR_SPECIALTIES: frozenset[str] = frozenset({"_leader", "leader_sov"})


class CommanderCapacitePatternStandard(TypedDict):
    """Short Capacite names + tag/specialty keys for CMD vs infantry LDR."""

    cmd_capacity: str
    ldr_inf_capacity: str
    cmd_unit_tag: str
    infanterie_tag: str
    ldr_unit_tags: frozenset[str]
    ldr_specialties: frozenset[str]


COMMANDER_CAPACITE_PATTERN_STANDARD: CommanderCapacitePatternStandard = {
    "cmd_capacity": CMD_UNIT_CAPACITY_NAME,
    "ldr_inf_capacity": LDR_INF_CAPACITY_NAME,
    "cmd_unit_tag": CMD_UNIT_TAG,
    "infanterie_tag": INFANTERIE_TAG,
    "ldr_unit_tags": LDR_UNIT_TAGS,
    "ldr_specialties": LDR_SPECIALTIES,
}


def resolve_commander_capacite_name(
    tags: AbstractSet[str],
    specialties: Optional[AbstractSet[str]] = None,
    std: Optional[CommanderCapacitePatternStandard] = None,
) -> str:
    """Return Capacite short name for a unit that still has TCommanderModuleDescriptor.

    Infantry leaders (Infanterie + LDR tag and/or _leader specialty, not CMD_Unit)
    get LDR_INF. Everything else (true CVs, vehicles, helos) gets CMD_UNIT.
    """
    rule = std or COMMANDER_CAPACITE_PATTERN_STANDARD
    specs = specialties or set()
    has_ldr_signal = bool(tags & rule["ldr_unit_tags"]) or bool(
        specs & rule["ldr_specialties"],
    )
    is_infantry_ldr = (
        rule["infanterie_tag"] in tags
        and has_ldr_signal
        and rule["cmd_unit_tag"] not in tags
    )
    if is_infantry_ldr:
        return rule["ldr_inf_capacity"]
    return rule["cmd_capacity"]
