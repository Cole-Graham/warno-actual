"""Dedicated supply-transport clone units for tow_only supply trucks."""

from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

from src.constants.supply_module import specialty_for_supply_descriptor
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits

SUPPLY_TRANSPORT_ORDERS = [
    "EOrderType/Stop",
    "EOrderType/Move",
    "EOrderType/FollowFormation",
    "EOrderType/FollowUnit",
    "EOrderType/QuickMove",
    "EOrderType/Reverse",
    "EOrderType/SupplyUnit",
    "EOrderType/AskForSupply",
    "EOrderType/AIStop",
    "EOrderType/AISupply",
    "EOrderType/UnloadFromTransport",
    "EOrderType/UnloadAtPosition",
    "EOrderType/Load",
]

_FACTION_META = {
    "US": {"Faction": "NATO", "Nation": "US"},
    "UK": {"Faction": "NATO", "Nation": "UK"},
    "RFA": {"Faction": "NATO", "Nation": "RFA"},
    "FR": {"Faction": "NATO", "Nation": "FR"},
    "POL": {"Faction": "PACT", "Nation": "POL"},
    "SOV": {"Faction": "PACT", "Nation": "SOV"},
}

# Per-donor config: index for NEW_UNITS key, GUIDs, optional stat/name overrides.
SUPPLY_TRANSPORT_VARIANT_CONFIG: Dict[str, Dict[str, Any]] = {
    "Rover_101FC_supply_UK": {
        "index": 0,
        "UnitId": 50096,
        "guids": {
            "GUID": "18882db3-6aca-49ac-b93a-3401fabc9884",
            "InfantrySquadModuleGUID": "275f100b-b565-496a-9d17-d334d001bc2c",
            "ShowroomGUID": "8c415f2f-8f15-4979-9e80-5d987096721c",
            "CadavreGUID": "2d273faa-39f1-4c72-b0cb-d79540d92468",
        },
        "game_name": {"display": "#AA ROVER 101FC SUPPLY", "token": "XPVHTUWRLW"},
        "command_points": 15,
        "supply_capacity": 475.0,
    },
    "Unimog_S_404_RFA": {
        "index": 0,
        "UnitId": 50097,
        "guids": {
            "GUID": "a3a2d5af-c506-4c2d-a71e-88a2790c9ff7",
            "InfantrySquadModuleGUID": "8005a6fd-0888-4210-896f-04205dffa085",
            "ShowroomGUID": "569faf48-54a7-4f2c-8ef8-fc9f71cc1021",
            "CadavreGUID": "1de5afe0-95a4-4fb2-83d0-a82f041a3c67",
        },
        "game_name": {"display": "#AA UNIMOG S404 MÜN.", "token": "UNIMOGTRNS"},
    },
    "TRM_2000_supply_FR": {
        "index": 0,
        "UnitId": 50098,
        "guids": {
            "GUID": "df1b69cb-ca17-45c0-a065-15313a55f60e",
            "InfantrySquadModuleGUID": "53d70b92-17ce-4093-9282-458e317ee061",
            "ShowroomGUID": "3121a3d2-99fa-46ce-8eaf-fb041934e74b",
            "CadavreGUID": "50be6e98-5fb1-4786-84c1-b4c9f081f88a",
        },
        "game_name": {"display": "#AA TRM-2000 SUPPLY", "token": "TRMTWOKTRN"},
    },
    "M35_supply_US": {
        "index": 0,
        "UnitId": 50099,
        "guids": {
            "GUID": "d9d3d487-0d4f-4b68-b600-812f2040a81f",
            "InfantrySquadModuleGUID": "6febd635-1faf-4964-8507-c6b56cb17f11",
            "ShowroomGUID": "3ca13a56-a1d8-410a-9b77-6840bdb36f32",
            "CadavreGUID": "b5d2a986-47a2-49e7-8b4b-62ac9fa7e613",
        },
        "game_name": {"display": "#AA M35 SUPPLY", "token": "KMEWARZXUT"},
        "command_points": 20,
        "supply_capacity": 650.0,
        "unite_tag": "UNITE_M35_supply_US",
    },
    "Bedford_MJ_4t_UK": {
        "index": 0,
        "UnitId": 50100,
        "guids": {
            "GUID": "5ebd99b9-5331-4ff6-b55b-00fd1f992a64",
            "InfantrySquadModuleGUID": "3e90e589-52b4-4917-907d-9943032a5cb1",
            "ShowroomGUID": "3c10dd88-b2f0-40cd-b89a-85b21f18850f",
            "CadavreGUID": "a76bf537-47da-467a-9142-eb7d012583e6",
        },
        "game_name": {"display": "#AA BEDFORD MJ SUPPLY", "token": "BEDFTRNSUK"},
    },
    "KrAZ_255B_supply_SOV": {
        "index": 0,
        "UnitId": 50101,
        "guids": {
            "GUID": "b0e3b005-337e-43dc-863a-bae034bb94cf",
            "InfantrySquadModuleGUID": "dbccbb47-0892-4c88-9bd0-f554f2c44adb",
            "ShowroomGUID": "331bccef-dcd2-483d-8eb0-5ab8b252a601",
            "CadavreGUID": "2e0ebec6-65de-42fd-9d04-589246a90720",
        },
        "game_name": {"display": "#AA KrAZ-255B SNAB.", "token": "AAKRAZTRAN"},
    },
}


def make_supply_transport_name(donor_name: str) -> str:
    """Return the NewName for a supply-transport clone."""
    if donor_name == "Bedford_MJ_4t_UK":
        return "Bedford_MJ_4t_supply_trans_UK"

    faction = donor_name.rsplit("_", 1)[-1]
    stem = donor_name[: -(len(faction) + 1)]
    if stem.endswith("_supply"):
        return f"{stem}_trans_{faction}"
    return f"{stem}_supply_trans_{faction}"


def compute_transport_stats(
    base_command_points: int,
    *,
    command_points_override: Optional[int] = None,
    supply_capacity_override: Optional[float] = None,
) -> Tuple[float, int]:
    """Return (supply_capacity, command_points) targeting ~33 supply per CP."""
    trans_cp = (
        command_points_override
        if command_points_override is not None
        else max(15, round(base_command_points * 0.5 / 5) * 5)
    )
    if trans_cp % 5 != 0:
        raise ValueError(f"Transport command points must be a multiple of 5, got {trans_cp}")

    trans_capacity = (
        supply_capacity_override
        if supply_capacity_override is not None
        else round(trans_cp * 33 / 25) * 25
    )
    return float(trans_capacity), trans_cp


def build_supply_transport_new_unit(donor_name: str) -> Dict[str, Any]:
    """Build a NEW_UNITS entry dict for a dedicated supply-transport variant."""
    if donor_name not in SUPPLY_TRANSPORT_VARIANT_CONFIG:
        raise KeyError(f"No supply transport config for {donor_name}")

    config = SUPPLY_TRANSPORT_VARIANT_CONFIG[donor_name]
    donor_edits = supply_unit_edits.get(donor_name, {})
    new_name = make_supply_transport_name(donor_name)
    faction_suffix = donor_name.rsplit("_", 1)[-1]
    meta = _FACTION_META[faction_suffix]

    game_name = config["game_name"]
    token = game_name["token"]
    if any(char.isdigit() for char in token):
        raise ValueError(
            f"GameName token for {donor_name} must not contain digits: {token!r}",
        )

    base_cp = int(donor_edits["CommandPoints"])
    supply_capacity, command_points = compute_transport_stats(
        base_cp,
        command_points_override=config.get("command_points"),
        supply_capacity_override=config.get("supply_capacity"),
    )
    supply_descriptor = donor_edits["Supply"]["SupplyDescriptor"]
    unite_tag = config.get("unite_tag", f"UNITE_{new_name}")
    supply_specialty = specialty_for_supply_descriptor(supply_descriptor)

    return {
        **config["guids"],
        "UnitId": config["UnitId"],
        "NewName": new_name,
        "GameName": game_name,
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                unite_tag,
                "Unite",
                "Vehicule",
                "Vehicule_Transport",
                "Vehicule_Logistique",
            ],
        },
        "CommandPoints": command_points,
        "Supply": {
            "SupplyCapacity": supply_capacity,
            "SupplyDescriptor": supply_descriptor,
        },
        "SpecialtiesList": ["_transport2", supply_specialty],
        "orders": SUPPLY_TRANSPORT_ORDERS,
        "tow_only": True,
        "is_infantry": False,
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": True,
        **meta,
    }


def build_supply_transport_new_units() -> Dict[Tuple[str, int], Dict[str, Any]]:
    """Return all supply-transport NEW_UNITS entries keyed by (donor, index)."""
    entries: Dict[Tuple[str, int], Dict[str, Any]] = {}
    for donor_name, config in SUPPLY_TRANSPORT_VARIANT_CONFIG.items():
        entries[(donor_name, config["index"])] = build_supply_transport_new_unit(donor_name)
    return entries
