"""Functions for gathering deck data from game files."""

from pathlib import Path
from typing import Any, Dict, List  # noqa

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes

logger = setup_logger('deck_data')


def gather_deck_data(mod_src_path: Path) -> Dict[str, Any]:
    """Gather deck data from Decks.ndf.
    
    Returns:
        Dict with categories of decks:
        {
            "challenge": {
                "deck_name": {
                    "division": str,
                    "identifier": str,
                    "token": str,
                    "packs": List[str],
                    "combatgroup_list": {
                        combat_group.index": {
                            "group_name_token": str,
                            smart_group.index": {
                                "smart_group_name_token": str,
                                "pack_list": List[str]
                            },
                        },
                    },
                },
            },
            "multi": {
                "deck_name": {
                    "division": str,
                    "token": str,
                    "packs": List[str]
                }
            },
            "strategic": {
                "deck_name": {
                    "division": str,
                    "superior": str,
                    "identifier": str,
                    "packs": List[str],
                    "combat_groups": {
                        "combatgroup_descr_name": {
                            "token": str,
                            "IsHQ": bool,
                            "smart_group.index": {
                                "smart_group_name_token": str,
                                "IsHQ": bool,
                                "pack_list": List[str]
                            },
                        },
                    },
                }
            },
        }
    """
    logger.info("Gathering deck data from Decks.ndf")
    
    # Initialize deck data structure with categories
    deck_data = {
        "multi": {},
        "challenge": {},
        "strategic": {},
    }
    ndf_path = r"GameData/Generated/Gameplay/Decks/Decks.ndf"
    strategic_ndf_path = r"GameData/Generated/Gameplay/Decks/StrategicDecks.ndf"
    strategic_combat_groups_ndf_path = r"GameData/Generated/Gameplay/Decks/StrategicCombatGroups.ndf"
    
    try:
        # Just parsing input, no output needed
        mod = ndf.Mod(str(mod_src_path), "None")
        decks_source = mod.parse_src(ndf_path)
        strat_decks_source = mod.parse_src(strategic_ndf_path)
        strat_combat_groups_source = mod.parse_src(strategic_combat_groups_ndf_path)
        multi_decks = 0  # Counter for multi decks
        challenge_decks = 0  # Counter for challenge decks
        strategic_decks = 0  # Counter for strategic decks
        
        multi_decks, challenge_decks = _parse_challenge_and_multi_decks(
            decks_source, deck_data, multi_decks, challenge_decks)
        
        strategic_decks = _parse_strategic_decks(
            strat_decks_source, strat_combat_groups_source, deck_data, strategic_decks)
    
    except Exception as e:
        logger.error(f"Error gathering deck data: {str(e)}")
        raise
    
    logger.info(f"Gathered data for: {multi_decks} multiplayer decks, "
                f"{challenge_decks} challenge decks, and "
                f"{strategic_decks} strategic decks")
    return deck_data


def _parse_challenge_and_multi_decks(
    decks_source: Any,
    deck_data: Dict[str, Any],
    multi_decks: int,
    challenge_decks: int,
) -> Dict[str, Any]:
    for deck_row in decks_source:
        # Skip non-deck entries
        if not hasattr(deck_row, 'namespace'):
            continue
        
        # Process decks based on type
        if deck_row.namespace.endswith("_multi") or "RDA_Rugen_Gruppierung" in deck_row.namespace:
            deck_type = "multi"
        elif "challenge" in deck_row.namespace:
            deck_type = "challenge"
        else:
            logger.warning(f"Unknown deck type: {deck_row.namespace}")
            continue
        

        deck_name = deck_row.namespace.replace("Descriptor_Deck_", "")
        division = strip_quotes(deck_row.v.by_m("DeckDivision").v).replace(
                    "$/GFX/Division/Descriptor_Deck_Division_", "")
        packs = []
        for pack in deck_row.v.by_m("DeckPackList").v:  # noqa
            # Remove ~/ prefix from pack names
            pack_name = pack.v.replace("~/", "")
            packs.append(pack_name)
        
        try:        
            deck_token = strip_quotes(deck_row.v.by_m("DeckName").v)  # noqa
            
            if deck_type == "challenge":
                
                identifier = strip_quotes(deck_row.v.by_m("DeckIdentifier").v)  # noqa
                
                if any(sub_type in deck_name for sub_type in ["_Player", "_PLAYER"]):
                    sub_type = "player"
                elif any(sub_type in deck_name for sub_type in ["_Ally", "_ALLY"]):
                    sub_type = "ai_ally"
                elif "_IA" in deck_name:
                    sub_type = "ai_opponent"
                else:
                    sub_type = "ai_opponent" # Probably, but not sure
            
            try:
                # Get challenge deck combat group list
                def parse_combat_groups(deck_row: Any) -> Dict[str, Any]:
                    combatgroup_list = {}
                    for combat_group in deck_row.v.by_m("DeckCombatGroupList").v:  # noqa
                        if combat_group.v.by_m("Name", False):
                            group_name_token = strip_quotes(combat_group.v.by_m("Name").v)
                        else:
                            group_name_token = None
                        combatgroup_list[str(combat_group.index)] = {
                            "group_name_token": group_name_token,
                        }
                        for smart_group in combat_group.v.by_m("SmartGroupList").v:  # noqa
                            if smart_group.v.by_m("Name", False):
                                smart_group_name_token = strip_quotes(smart_group.v.by_m("Name").v)
                            else:
                                smart_group_name_token = None
                            combatgroup_list[str(combat_group.index)][str(smart_group.index)] = {
                                "smart_group_name_token": smart_group_name_token,
                                "pack_list": []
                            }
                            for pack in smart_group.v.by_m("PackIndexUnitNumberList").v:  # noqa
                                pack_index = pack.v[0]
                                unit_number = pack.v[1]
                                combatgroup_list[str(combat_group.index)][str(smart_group.index)]["pack_list"].append(
                                    (pack_index, unit_number)
                                )
                    return combatgroup_list
            except Exception as e:
                logger.error(f"e1: Failed to parse combat groups for {deck_type} deck {deck_name}: {str(e.__cause__)} {str(e)}")
                continue
            
            try:
                if deck_type == "challenge" and deck_row.v.by_m("DeckCombatGroupList", False):
                    deck_data[deck_type][deck_name] = {
                        "division": division,
                        "identifier": identifier,
                        "token": deck_token,
                        "packs": packs,
                        "combatgroup_list": parse_combat_groups(deck_row)
                    }
                    challenge_decks += 1
                    logger.debug(f"Gathered data for challenge deck: {deck_name}")
                elif deck_type == "challenge":
                    deck_data[deck_type][deck_name] = {
                        "division": division,
                        "identifier": identifier,
                        "token": deck_token,
                        "packs": packs,
                        "combatgroup_list": {}
                    }
                    challenge_decks += 1
            except Exception as e:
                logger.error(f"e2: Failed to parse combat groups for {deck_type} deck {deck_name}: {str(e)}")
                continue
            
            try:
                if deck_type in "multi":
                    deck_data[deck_type][deck_name] = {
                        "division": division,
                        "token": deck_token,
                        "packs": packs,
                    }
                    multi_decks += 1
                    logger.debug(f"Gathered data for multi deck: {deck_name}")
            except Exception as e:
                logger.error(f"e3: Failed to parse save data for multi {deck_type} deck {deck_name}: {str(e)}")
                continue
        
        except Exception as e:
            logger.error(f"main e: Failed to gather data for deck {deck_name}: {str(e)}")
            continue
        
    return multi_decks, challenge_decks


def _parse_strategic_decks(
    strat_decks_source: Any,
    strat_combat_groups_source: Any,
    deck_data: Dict[str, Any],
    strategic_decks: int,
) -> Dict[str, Any]:
    for deck_row in strat_decks_source:
        if not hasattr(deck_row, 'namespace'):
            continue
        
        deck_name = deck_row.namespace.replace("Descriptor_Deck_", "")
        division = strip_quotes(deck_row.v.by_m("DeckDivision").v).replace(
            "$/GFX/Division/Descriptor_Deck_Division_", "")
        if deck_row.v.by_m("Superior", False):
            superior = strip_quotes(deck_row.v.by_m("Superior").v)
        else:
            superior = None
        identifier = strip_quotes(deck_row.v.by_m("DeckIdentifier").v)
        
        packs = []
        for pack in deck_row.v.by_m("DeckPackList").v:
            packs.append(pack.v.replace("~/", ""))
        
        combat_group_descriptors = []
        for combat_group in deck_row.v.by_m("DeckCombatGroupList").v:
            combat_group_descriptors.append(combat_group.v.replace("~/", ""))
            
        combat_groups = _parse_strategic_combat_groups(
            strat_combat_groups_source, deck_data, strategic_decks, combat_group_descriptors)
        
        deck_data["strategic"][deck_name] = {
            "division": division,
            "superior": superior,
            "identifier": identifier,
            "packs": packs,
            "combat_groups": combat_groups
        }
        strategic_decks += 1
        logger.debug(f"Gathered data for strategic deck: {deck_name}")
    
    return strategic_decks


def _parse_strategic_combat_groups(
    strat_combat_groups_source: Any,
    deck_data: Dict[str, Any],
    strategic_decks: int,
    combat_group_descriptors: List[str],
) -> Dict[str, Any]:
    combat_groups = {}
    for combat_group in strat_combat_groups_source:
        if combat_group.namespace not in combat_group_descriptors:
            continue
        
        smart_groups = {}
        for smart_group in combat_group.v.by_m("SmartGroupList").v:
            logger.debug(f"Combat group: {combat_group.namespace}")
            if smart_group.v.by_m("Name", False):
                smart_group_name = strip_quotes(smart_group.v.by_m("Name").v)
            else:
                smart_group_name = None
            smart_groups[str(smart_group.index)] = {
                "smart_group_name_token": smart_group_name,
                "pack_list": []
            }
            if smart_group.v.by_m("IsHQ", False):
                smart_groups[str(smart_group.index)]["IsHQ"] = True
            else:
                smart_groups[str(smart_group.index)]["IsHQ"] = False
                
            for pack in smart_group.v.by_m("PackIndexUnitNumberList").v:
                pack_index = pack.v[0]
                unit_number = pack.v[1]
                smart_groups[str(smart_group.index)]["pack_list"].append(
                    (pack_index, unit_number)
                )
            
        combat_groups[combat_group.namespace] = {
            "group_name_token": strip_quotes(combat_group.v.by_m("Name").v),
            "smart_groups": smart_groups
        }
        
        if combat_group.v.by_m("IsHQ", False):
            combat_groups[combat_group.namespace]["IsHQ"] = True
        else:
            combat_groups[combat_group.namespace]["IsHQ"] = False
        
    return combat_groups