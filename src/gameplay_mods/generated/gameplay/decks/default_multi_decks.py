"""Create default multiplayer decks and their deck packs from constants."""

from typing import Any, Dict, List, Optional, Tuple

from src import ndf
from src.constants.generated.gameplay.decks import load_default_multi_decks, load_new_divisions
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

DEFAULT_CATEGORY_ORDER = (
    "Logistic",
    "Infantry",
    "Artillery",
    "Tanks",
    "Recon",
    "AA",
    "Helicopters",
    "Air",
)

UNIT_DESCRIPTOR_PREFIX = "Descriptor_Unit_"
PACK_DESCRIPTOR_PREFIX = "Descriptor_Deck_Pack_"
MULTI_DECK_PACK_NUMBER = 1


def strip_unit_descriptor(unit_ref: str) -> str:
    if unit_ref.startswith(UNIT_DESCRIPTOR_PREFIX):
        return unit_ref[len(UNIT_DESCRIPTOR_PREFIX):]
    return unit_ref


def parse_entry(entry: Dict) -> Tuple[str, Dict]:
    unit_ref = next(iter(entry))
    return unit_ref, entry[unit_ref]


def flatten_categories(categories: Dict) -> List[Dict]:
    if not categories:
        return []

    entries: List[Dict] = []
    for category in DEFAULT_CATEGORY_ORDER:
        cat_entries = categories.get(category)
        if not cat_entries:
            continue
        entries.extend(cat_entries)

    for category, cat_entries in categories.items():
        if category in DEFAULT_CATEGORY_ORDER or not cat_entries:
            continue
        entries.extend(cat_entries)

    return entries


def entry_to_pack_namespace(entry: Dict, number: int = MULTI_DECK_PACK_NUMBER) -> str:
    """Build a _multi deck pack namespace (always ``…_{vet}_1`` in vanilla)."""
    unit_ref, opts = parse_entry(entry)
    unit_name = strip_unit_descriptor(unit_ref)
    vet = opts["vet"]
    transport_ref = opts.get("transport")
    if transport_ref:
        transport_name = strip_unit_descriptor(transport_ref)
        return f"{PACK_DESCRIPTOR_PREFIX}{unit_name}_{transport_name}_{vet}_{number}"
    return f"{PACK_DESCRIPTOR_PREFIX}{unit_name}_{vet}_{number}"


def build_deck_pack_ndf(
    namespace: str,
    unit_name: str,
    vet: int,
    transport_name: Optional[str] = None,
    number: int = 1,
) -> str:
    if vet > 0:
        xp_line = f"    Xp = {vet}"
    else:
        xp_line = ""

    if transport_name:
        transport_line = f"    Transport = $/GFX/Unit/Descriptor_Unit_{transport_name}"
    else:
        transport_line = ""

    member_lines = [line for line in (xp_line, transport_line) if line]
    members = "\n".join(member_lines)
    if members:
        members = f"{members}\n"

    return (
        f"{namespace} is DeckPackDescriptor\n"
        f"(\n"
        f"{members}"
        f"    Unit = $/GFX/Unit/Descriptor_Unit_{unit_name}\n"
        f"    Number = {number}\n"
        f")"
    )


def resolve_default_deck_pack_reference(namespace: str, game_db: Dict[str, Any]) -> str:
    """Return the pack namespace for default _multi decks unchanged.

    Skips both ``deck_pack_modifications`` and ``reference_mappings``. Those
    maps exist to retarget vanilla deck rows; default decks name the exact unit
    descriptor and vet, so we always create or reuse ``…_{vet}_1`` for that unit.
    """
    del game_db
    return namespace


def find_donor_pack(source_path: Any, unit_name: str, transport_name: Optional[str] = None) -> Any:
    unit_ref = f"$/GFX/Unit/Descriptor_Unit_{unit_name}"
    transport_ref = (
        f"$/GFX/Unit/Descriptor_Unit_{transport_name}" if transport_name else None
    )

    fallback = None
    for deck_pack in source_path:
        if not hasattr(deck_pack, "namespace"):
            continue
        if not deck_pack.namespace.startswith(PACK_DESCRIPTOR_PREFIX):
            continue

        unit_member = deck_pack.v.by_m("Unit", False)
        if not unit_member or unit_member.v != unit_ref:
            continue

        transport_member = deck_pack.v.by_m("Transport", False)
        has_transport = transport_member is not None and transport_member.v is not None

        if transport_name:
            if has_transport and transport_member.v == transport_ref:
                return deck_pack
            if fallback is None:
                fallback = deck_pack
        elif not has_transport:
            return deck_pack
        elif fallback is None:
            fallback = deck_pack

    return fallback


def _apply_pack_descriptor(
    deck_pack: Any,
    namespace: str,
    unit_name: str,
    vet: int,
    transport_name: Optional[str],
    number: int,
) -> None:
    deck_pack.namespace = namespace
    deck_pack.n = namespace
    deck_pack.v.by_m("Unit").v = f"$/GFX/Unit/Descriptor_Unit_{unit_name}"

    transport_member = deck_pack.v.by_m("Transport", False)
    if transport_name:
        transport_ref = f"$/GFX/Unit/Descriptor_Unit_{transport_name}"
        if transport_member:
            transport_member.v = transport_ref
        else:
            deck_pack.v.insert(1, f"Transport = {transport_ref}")
    elif transport_member:
        deck_pack.v.remove_by_member("Transport")

    if vet > 0:
        xp_member = deck_pack.v.by_m("Xp", False)
        if xp_member:
            xp_member.v = str(vet)
        else:
            deck_pack.v.insert(1, f"Xp = {vet}")
    else:
        xp_member = deck_pack.v.by_m("Xp", False)
        if xp_member:
            deck_pack.v.remove_by_member("Xp")

    number_member = deck_pack.v.by_m("Number", False)
    if number_member:
        number_member.v = str(number)
    else:
        deck_pack.v.add(f"Number = {number}")


def _find_pack_by_namespace(source_path: Any, namespace: str) -> Any:
    for deck_pack in source_path:
        if hasattr(deck_pack, "namespace") and deck_pack.namespace == namespace:
            return deck_pack
    return None


def _multi_pack_matches_spec(deck_pack: Any, vet: int) -> bool:
    number_member = deck_pack.v.by_m("Number", False)
    number = int(number_member.v) if number_member and number_member.v else None
    if number != MULTI_DECK_PACK_NUMBER:
        return False

    xp_member = deck_pack.v.by_m("Xp", False)
    if vet == 0:
        return xp_member is None
    return xp_member is not None and int(xp_member.v) == vet


def _new_divisions_by_cfg_name() -> Dict[str, Dict]:
    by_cfg_name: Dict[str, Dict] = {}
    for div_data in load_new_divisions().values():
        cfg_name = div_data.get("cfg_name")
        if cfg_name:
            by_cfg_name[cfg_name] = div_data
    return by_cfg_name


def _entry_pack_parts(
    entry: Dict,
    number: int = MULTI_DECK_PACK_NUMBER,
) -> Tuple[str, str, int, Optional[str], int]:
    unit_ref, opts = parse_entry(entry)
    unit_name = strip_unit_descriptor(unit_ref)
    vet = opts["vet"]
    transport_name = None
    if "transport" in opts:
        transport_name = strip_unit_descriptor(opts["transport"])
    namespace = entry_to_pack_namespace(entry, number=number)
    return namespace, unit_name, vet, transport_name, number


def ensure_default_multi_deck_packs(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Create DeckPackDescriptor rows required by default multiplayer decks."""
    default_decks = load_default_multi_decks()
    if not default_decks:
        return

    packs_created = 0
    packs_reused = 0
    packs_fixed = 0

    for cfg_name, categories in default_decks.items():
        entries = flatten_categories(categories)
        if not entries:
            logger.debug(f"Skipping deck packs for {cfg_name}: no cards defined")
            continue

        for entry in entries:
            namespace, unit_name, vet, transport_name, number = _entry_pack_parts(entry)
            resolved_namespace = resolve_default_deck_pack_reference(namespace, game_db)

            existing_pack = _find_pack_by_namespace(source_path, resolved_namespace)
            if existing_pack and _multi_pack_matches_spec(existing_pack, vet):
                packs_reused += 1
                continue

            if existing_pack:
                _apply_pack_descriptor(
                    existing_pack,
                    resolved_namespace,
                    unit_name,
                    vet,
                    transport_name,
                    number,
                )
                packs_fixed += 1
                logger.debug(f"Fixed default deck pack {resolved_namespace}")
                continue

            donor_pack = find_donor_pack(source_path, unit_name, transport_name)
            if donor_pack:
                new_deck_pack = donor_pack.copy()
                _apply_pack_descriptor(
                    new_deck_pack,
                    resolved_namespace,
                    unit_name,
                    vet,
                    transport_name,
                    number,
                )
                source_path.add(new_deck_pack)
            else:
                ndf_str = build_deck_pack_ndf(
                    resolved_namespace,
                    unit_name,
                    vet,
                    transport_name,
                    number,
                )
                source_path.add(ndf_str)

            packs_created += 1
            logger.debug(f"Created default deck pack {resolved_namespace}")

    logger.info(
        f"Default multiplayer deck packs: {packs_created} created, {packs_reused} reused, "
        f"{packs_fixed} fixed"
    )


def capture_multi_deck_donor(source_path: Any) -> Any:
    for deck_obj in source_path:
        if hasattr(deck_obj, "namespace") and deck_obj.namespace.endswith("_multi"):
            return deck_obj
    return None


def add_default_multi_decks(source_path: Any, donor_deck: Any, game_db: Dict[str, Any]) -> None:
    """Add default multiplayer TDeckDescriptor entries after vanilla multi decks are removed."""
    default_decks = load_default_multi_decks()
    if not default_decks:
        return

    divisions_by_cfg_name = _new_divisions_by_cfg_name()
    decks_created = 0

    for cfg_name, categories in default_decks.items():
        entries = flatten_categories(categories)
        if not entries:
            logger.warning(f"Skipping default deck for {cfg_name}: empty loadout")
            continue

        div_data = divisions_by_cfg_name.get(cfg_name)
        if not div_data:
            logger.warning(f"Skipping default deck for {cfg_name}: division metadata not found")
            continue

        div_name_tokens = div_data.get("div_name")
        if not isinstance(div_name_tokens, tuple) or len(div_name_tokens) < 2:
            logger.warning(f"Skipping default deck for {cfg_name}: missing div_name token")
            continue

        pack_namespaces = [
            resolve_default_deck_pack_reference(entry_to_pack_namespace(entry), game_db)
            for entry in entries
        ]

        deck_namespace = f"Descriptor_Deck_{cfg_name}_multi"
        if donor_deck:
            new_deck = donor_deck.copy()
        else:
            new_deck = ndf.convert(
                f"{deck_namespace} is TDeckDescriptor\n"
                f"(\n"
                f'    DeckDivision = $/GFX/Division/Descriptor_Deck_Division_{cfg_name}_multi\n'
                f'    DeckName = "{div_name_tokens[1]}"\n'
                f"    DeckPackList = []\n"
                f")"
            )

        new_deck.namespace = deck_namespace
        new_deck.n = deck_namespace
        new_deck.v.by_m("DeckDivision").v = (
            f"$/GFX/Division/Descriptor_Deck_Division_{cfg_name}_multi"
        )
        new_deck.v.by_m("DeckName").v = f'"{div_name_tokens[1]}"'

        deck_pack_list = new_deck.v.by_m("DeckPackList")
        for pack_ref in list(deck_pack_list.v):
            deck_pack_list.v.remove(pack_ref)
        for pack_namespace in pack_namespaces:
            deck_pack_list.v.add(f"~/{pack_namespace}")

        source_path.add(new_deck)
        decks_created += 1
        logger.info(
            f"Created default multiplayer deck {deck_namespace} with {len(pack_namespaces)} packs"
        )

    logger.info(f"Created {decks_created} default multiplayer decks")
