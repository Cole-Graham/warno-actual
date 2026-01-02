"""Precompute deck pack namespace mappings for unit edits and new command units."""

from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits
from src.utils.config_utils import get_mod_src_path
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def build_deck_pack_mappings(mod_source_path: Path) -> Dict[str, Dict[str, str]]:
    """Precompute deck pack namespace mappings for unit edits and reference updates."""
    logger.info("Building deck pack namespace mappings")

    # Parse existing deck packs with structured categorization
    deck_pack_data = _parse_deck_pack_data(mod_source_path)

    # Load unit edits
    unit_edits = load_unit_edits()
    # unit_edits.update(supply_unit_edits)

    # Build two separate types of mappings
    deck_pack_modifications = {}  # For modifying DeckPacks.ndf (only XP/number changes)
    reference_mappings = {}  # For updating Decks.ndf references (donor -> new unit)

    # Process existing unit edits - only XP/number changes, never unit name changes
    _build_unit_edit_mappings_from_structured_data(unit_edits, deck_pack_data, deck_pack_modifications)

    # Process new command units - only for reference replacement
    _build_command_unit_reference_mappings(deck_pack_data, reference_mappings)

    logger.info(
        f"Built {len(deck_pack_modifications)} deck pack modifications and {len(reference_mappings)} reference mappings"
    )

    # Return separated mappings
    return {"deck_pack_modifications": deck_pack_modifications, "reference_mappings": reference_mappings}


def build_deck_pack_data(mod_source_path: Path) -> Dict[str, Any]:
    """Build deck pack data for use in runtime functions."""
    logger.info("Building deck pack data")

    # Parse existing deck packs with structured categorization
    deck_pack_data = _parse_deck_pack_data(mod_source_path)

    logger.info(f"Built deck pack data for {len(deck_pack_data['base_units'])} base units")
    return deck_pack_data


def _parse_deck_pack_data(mod_source_path: Path) -> Dict[str, Any]:
    """Parse existing DeckPacks.ndf with structured categorization of transport vs non-transport deck packs.
    
    Parses ALL deck packs from game files. Uses unit_edits to identify base unit names,
    but includes all deck packs regardless of whether they're in unit_edits.

    Returns:
        Dict with structured deck pack data:
        {
            "base_units": {
                "Engineers_DDR": {
                    "simple_packs": ["Descriptor_Deck_Pack_Engineers_DDR_0_1", ...],
                    "transport_packs": ["Descriptor_Deck_Pack_Engineers_DDR_BTR_70_DDR_0_1", ...],
                    "number_xp_combinations": {1: [0, 1], 100: [1, 3]}
                }
            },
            "all_namespaces": ["Descriptor_Deck_Pack_...", ...]
        }
    """
    logger.info("Parsing deck pack data with transport categorization")

    data = {"base_units": {}, "all_namespaces": []}

    try:
        # Parse DeckPacks.ndf
        mod = ndf.Mod(str(mod_source_path), "None")
        ndf_path = "GameData/Generated/Gameplay/Decks/DeckPacks.ndf"
        
        # Check if file exists
        full_path = mod_source_path / ndf_path
        if not full_path.exists():
            logger.error(f"DeckPacks.ndf not found at {full_path}")
            return data
        
        try:
            source = mod.parse_src(ndf_path)
        except Exception as parse_error:
            logger.error(f"Failed to parse {ndf_path}: {parse_error}", exc_info=True)
            return data
        
        if source is None:
            logger.error(f"Failed to parse {ndf_path} - parse_src returned None")
            return data

        # Load unit edits to know which are base units (used for identifying base unit names)
        unit_edits = load_unit_edits()
        # unit_edits.update(supply_unit_edits)
        base_unit_names = set(unit_edits.keys())

        for deck_pack in source:
            if not hasattr(deck_pack, "namespace"):
                continue

            # Only process DeckPackDescriptor entries
            if not deck_pack.namespace.startswith("Descriptor_Deck_Pack_"):
                continue

            namespace = deck_pack.namespace
            data["all_namespaces"].append(namespace)

            # Parse namespace: Descriptor_Deck_Pack_*_XP_Number
            parts = namespace.split("_")
            if len(parts) < 4:
                continue

            try:
                number = int(parts[-1])
                xp = int(parts[-2])
                unit_with_possible_transport = "_".join(parts[3:-2])

                # Find the base unit name
                base_unit = None
                is_transport_variant = False

                for unit_name in base_unit_names:
                    if unit_with_possible_transport == unit_name:
                        # Exact match - simple deck pack
                        base_unit = unit_name
                        is_transport_variant = False
                        break
                    elif unit_with_possible_transport.startswith(unit_name + "_"):
                        # Transport variant - base unit plus transport name
                        base_unit = unit_name
                        is_transport_variant = True
                        break

                if base_unit:
                    # Initialize base unit entry if not exists
                    if base_unit not in data["base_units"]:
                        data["base_units"][base_unit] = {
                            "simple_packs": [],
                            "transport_packs": [],
                            "number_xp_combinations": {},
                        }

                    unit_data = data["base_units"][base_unit]

                    # Categorize by transport vs simple
                    if is_transport_variant:
                        unit_data["transport_packs"].append(namespace)
                    else:
                        unit_data["simple_packs"].append(namespace)

                    # Track (number, xp) combinations for the base unit
                    if number not in unit_data["number_xp_combinations"]:
                        unit_data["number_xp_combinations"][number] = []
                    if xp not in unit_data["number_xp_combinations"][number]:
                        unit_data["number_xp_combinations"][number].append(xp)

            except (ValueError, IndexError) as e:
                logger.warning(f"Failed to parse deck pack namespace {namespace}: {e}")
                continue

        # Sort XP levels for each combination
        for unit_name, unit_data in data["base_units"].items():
            for number in unit_data["number_xp_combinations"]:
                unit_data["number_xp_combinations"][number].sort()

        logger.info(f"Parsed {len(data['all_namespaces'])} total deck packs for {len(data['base_units'])} base units")

    except Exception as e:
        logger.error(f"Failed to parse deck pack data: {e}", exc_info=True)

    return data


def _build_unit_edit_mappings_from_structured_data(
    unit_edits: Dict[str, Any], deck_pack_data: Dict[str, Any], mappings: Dict[str, str]
) -> None:
    """Build mappings for existing unit edits using structured deck pack data."""

    for base_unit, unit_data in deck_pack_data["base_units"].items():
        if base_unit not in unit_edits or "availability" not in unit_edits[base_unit]:
            continue

        availability = unit_edits[base_unit]["availability"]
        available_xp_levels = [i for i, avail in enumerate(availability) if avail > 0]

        if not available_xp_levels:
            continue

        # Process deck packs grouped by Number (like the old logic)
        # Group all packs (simple + transport) by their Number value
        number_groups = {}  # number -> [namespaces]
        all_unit_packs = unit_data["simple_packs"] + unit_data["transport_packs"]

        for namespace in all_unit_packs:
            parts = namespace.split("_")
            if len(parts) >= 4:
                try:
                    number = int(parts[-1])
                    if number not in number_groups:
                        number_groups[number] = []
                    number_groups[number].append(namespace)
                except (ValueError, IndexError):
                    continue

        # Process each Number group separately (like old logic)
        for number, namespaces in number_groups.items():
            # Get existing XP levels for this number group
            existing_xp_levels = []
            namespace_by_xp = {}  # xp -> [namespaces]

            for namespace in namespaces:
                parts = namespace.split("_")
                if len(parts) >= 4:
                    try:
                        current_xp = int(parts[-2])
                        existing_xp_levels.append(current_xp)
                        if current_xp not in namespace_by_xp:
                            namespace_by_xp[current_xp] = []
                        namespace_by_xp[current_xp].append(namespace)
                    except (ValueError, IndexError):
                        continue

            # Smart mapping logic: find which XP levels to keep, update, and create
            available_xp_set = set(available_xp_levels)
            existing_xp_set = set(existing_xp_levels)

            # Find which existing packs already match target XP levels (keep unchanged)
            packs_to_keep = available_xp_set.intersection(existing_xp_set)

            # Find which existing packs need to be updated
            packs_to_update = existing_xp_set - available_xp_set

            # Find which target XP levels need new packs
            missing_xp_levels = sorted(available_xp_set - existing_xp_set)

            logger.debug(
                f"Unit {base_unit} (Number={number}): Keep XP {sorted(packs_to_keep)}, Update XP {sorted(packs_to_update)} -> missing XP {missing_xp_levels}"
            )

            # Map each pack that needs updating to the best available XP level
            missing_xp_list = missing_xp_levels.copy()
            for current_xp in sorted(packs_to_update):
                if current_xp not in namespace_by_xp:
                    continue

                # Handle multiple namespaces with the same XP level
                namespaces_for_xp = namespace_by_xp[current_xp]

                # Find the best target XP level for this existing XP (same for all namespaces)
                target_xp = _find_best_target_xp(current_xp, available_xp_levels, missing_xp_list)

                if target_xp is not None and target_xp != current_xp:
                    # Create mappings for all namespaces with this XP level
                    for namespace in namespaces_for_xp:
                        # Parse namespace and create mapping
                        parts = namespace.split("_")
                        unit_with_possible_transport = "_".join(parts[3:-2])

                        # Create mapping preserving the full namespace structure
                        old_namespace = namespace
                        new_namespace = f"Descriptor_Deck_Pack_{unit_with_possible_transport}_{target_xp}_{number}"
                        mappings[old_namespace] = new_namespace
                        logger.debug(f"Created mapping: {old_namespace} -> {new_namespace}")

                    # Remove this target from missing list after processing all namespaces for this XP level
                    if target_xp in missing_xp_list:
                        missing_xp_list.remove(target_xp)

        logger.debug(
            f"Processed mappings for {base_unit}: {len(unit_data['simple_packs'])} simple + {len(unit_data['transport_packs'])} transport packs"
        )


def _find_best_target_xp(current_xp: int, available_xp_levels: list, missing_xp_levels: list) -> int:
    """Find the best target XP level for an existing pack that needs updating.

    Strategy:
    1. Prefer missing XP levels (levels that need new packs)
    2. Among missing levels, prefer the one closest to current_xp
    3. If current_xp > all available, use highest available
    4. If current_xp < all available, use lowest available
    """
    if not available_xp_levels:
        return None

    # If there are missing XP levels, prioritize them
    if missing_xp_levels:
        # Find the missing XP level closest to current_xp
        closest_missing = min(missing_xp_levels, key=lambda x: abs(x - current_xp))
        return closest_missing

    # No missing levels - this shouldn't happen in normal mapping, but handle gracefully
    # Find the available XP level closest to current_xp
    closest_available = min(available_xp_levels, key=lambda x: abs(x - current_xp))
    return closest_available


def _build_command_unit_reference_mappings(deck_pack_data: Dict[str, Any], mappings: Dict[str, str]) -> None:
    """Build reference mappings for new command units (donor -> new unit references for Decks.ndf)."""
    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]

        # Only process command units
        if "NewName" not in edits or "availability" not in edits:
            continue

        new_unit_name = edits["NewName"]
        if "_CMD2_" not in new_unit_name:
            continue

        # Skip if donor has no existing deck packs
        if donor_name not in deck_pack_data["base_units"]:
            continue

        availability = edits["availability"]

        # Find all available XP levels for the new command unit
        available_xp_levels = []
        for i, avail in enumerate(availability):
            if avail > 0:
                available_xp_levels.append(i)

        if not available_xp_levels:
            continue

        # Get donor deck pack data
        donor_data = deck_pack_data["base_units"][donor_name]

        # Create reference mappings from all donor deck packs to new unit deck packs
        # This is ONLY for updating references in Decks.ndf, NOT for modifying DeckPacks.ndf
        all_donor_packs = donor_data["simple_packs"] + donor_data["transport_packs"]

        for donor_namespace in all_donor_packs:
            # Parse donor namespace
            parts = donor_namespace.split("_")
            if len(parts) < 4:
                continue

            try:
                number = int(parts[-1])
                donor_xp = int(parts[-2])

                # Find best matching XP level for new unit
                if donor_xp in available_xp_levels:
                    target_xp = donor_xp  # Direct match
                elif available_xp_levels:
                    # Use closest available XP level
                    target_xp = min(available_xp_levels, key=lambda x: abs(x - donor_xp))
                else:
                    continue

                # Create new unit namespace for reference replacement
                # Replace donor name with new unit name in the namespace
                donor_unit_part = "_".join(parts[3:-2])  # Everything between prefix and _XP_Number
                new_unit_part = donor_unit_part.replace(donor_name, new_unit_name, 1)
                new_namespace = f"Descriptor_Deck_Pack_{new_unit_part}_{target_xp}_{number}"

                # This mapping is ONLY for Decks.ndf reference updates
                mappings[donor_namespace] = new_namespace

            except (ValueError, IndexError):
                continue

        logger.debug(f"Added reference mappings for new command unit {new_unit_name}")
