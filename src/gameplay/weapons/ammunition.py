"""Editor for Ammunition.ndf."""

from typing import Any, Dict, List, Tuple
from uuid import uuid4

from src import ndf
from src.constants.weapons.ammunition import weapons
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_REMOVALS,
    AMMUNITION_RENAMES,
)
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

from .damage_families import apply_damage_families
from .mg_teams import edit_mg_team_weapons
from .mortar_mods import add_corrected_shot_dispersion
from .utils import get_supply_costs
from .vanilla_modifications import apply_vanilla_renames, remove_vanilla_instances

logger = setup_logger(__name__)

def _generate_guid():
    """Generate a new GUID."""
    return str(uuid4())

def edit_ammunition(source, game_db: Dict[str, Any]) -> None:
    """Edit Ammunition.ndf file."""
    ammo_db = game_db["ammunition"]
    
    # First handle vanilla modifications
    apply_vanilla_renames(source, AMMUNITION_RENAMES, ammo_db)
    remove_vanilla_instances(source, AMMUNITION_REMOVALS)
    
    # Add mortar corrected shot
    add_corrected_shot_dispersion(source, game_db)
    
    # Modify MG team weapons
    edit_mg_team_weapons(source, game_db)
    
    # Apply damage family modifications
    apply_damage_families(source, game_db)
    
    # Track dictionary entries
    ingame_names = []
    calibers = []
    
    # Then apply weapon edits
    for (weapon_name, category, donor, is_new), data in weapons.items():
        if "Ammunition" not in data:
            continue
            
        try:
            ammo_data = data["Ammunition"]
            
            # Get donor descriptor for new weapons
            if is_new:
                donor_descr = source.by_n(f"Ammo_{donor}")
                if not donor_descr:
                    # Try without Ammo_ prefix
                    donor_descr = source.by_n(donor)
                    if not donor_descr:
                        logger.error(f"Could not find donor {donor} for {weapon_name}")
                        continue
                base_descr = donor_descr.copy()
                # Set namespace immediately for new weapons
                base_descr.namespace = f"Ammo_{weapon_name}"
            else:
                base_descr = source.by_n(f"Ammo_{weapon_name}")
                if not base_descr:
                    # Try without Ammo_ prefix
                    base_descr = source.by_n(weapon_name)
                    if not base_descr:
                        logger.error(f"Could not find weapon {weapon_name}")
                        continue
            
            # Track dictionary entries
            if "displayname" in ammo_data and "nametoken" in ammo_data:
                ingame_names.append((
                    weapon_name, 
                    ammo_data["nametoken"],
                    ammo_data["displayname"]
                ))
            
            if "parent_membr" in ammo_data and "Caliber" in ammo_data["parent_membr"]:
                caliber_data = ammo_data["parent_membr"]["Caliber"]
                if caliber_data[0] != "existing":
                    calibers.append((weapon_name, caliber_data[1], caliber_data[0]))
            
            # Apply edits to base descriptor
            _apply_weapon_edits(base_descr, ammo_data)
            
            # Handle weapon quantities
            if "NbWeapons" in data:
                _handle_weapon_quantities(source, base_descr, weapon_name, data["NbWeapons"])
            elif is_new:
                # For new single weapons, just append to source
                source.add(base_descr)
                
            logger.info(f"Processed weapon {weapon_name}")
            
        except Exception as e:
            logger.error(f"Failed to edit {weapon_name}: {str(e)}")
            
    # Write dictionary entries
    if ingame_names or calibers:
        _write_ammo_dictionary_entries(ingame_names, calibers)

def _apply_weapon_edits(descr: Any, data: Dict) -> None:
    """Apply edits from ammunition data to descriptor."""
    membr = descr.v.by_m
    
    logger.debug(f"Applying edits to {descr.n}")
    
    # Apply Arme edits
    if "Arme" in data:
        arme_data = data["Arme"]
        arme_obj = descr.v.by_m("Arme").v
        
        for arme_membr, arme_v in arme_data.items():
            if isinstance(arme_v, (float, int, bool)):
                arme_obj.by_m(arme_membr).v = str(arme_v)
            else:
                arme_obj.by_m(arme_membr).v = arme_v
    
    # Apply parent member edits
    if "parent_membr" in data:
        for key, value in data["parent_membr"].items():
            logger.debug(f"Setting {key} = {value}")
            if key == "add": # adding new member, e.g. [16, "PorteeMaximaleTBAGRU = 875"]
                index = value[0]
                value = value[1]
                descr.v.insert(index, value)
                continue
            elif isinstance(value, (float, int, bool)):
                membr(key).v = str(value)
            elif isinstance(value, tuple) and key == "Caliber":
                membr(key).v = f"'{value[1]}'"
            elif isinstance(value, list):
                # Convert list to NDF format
                list_str = "[" + ", ".join(f"'{item}'" for item in value) + "]"
                logger.debug(f"Converting list {list_str} to NDF")
                membr(key).v = ndf.convert(list_str.encode('utf-8'))[0].v
    
    # Apply hit roll edits
    if "hit_roll" in data:
        _apply_hit_roll_edits(descr, data["hit_roll"])
        
    # Apply texture
    if "Texture" in data:
        texture_file = f'"Texture_Interface_Weapon_{data["Texture"]}"'
        membr("InterfaceWeaponTexture").v = texture_file

def _apply_hit_roll_edits(descr: Any, hit_roll_data: Dict) -> None:
    """Apply hit roll edits to descriptor."""
    hitroll_obj = descr.v.by_m("HitRollRuleDescriptor").v
    
    if "BaseCriticModifier" in hit_roll_data:
        hitroll_obj.by_m("BaseCriticModifier").v = str(hit_roll_data["BaseCriticModifier"])
        
    modifiers = hitroll_obj.by_m("BaseHitValueModifiers").v
    if "Idling" in hit_roll_data:
        modifiers[1].v = (modifiers[1].v[0], str(hit_roll_data["Idling"]))
    if "Moving" in hit_roll_data:
        modifiers[2].v = (modifiers[2].v[0], str(hit_roll_data["Moving"]))

def _handle_weapon_quantities(source: Any, base_descr: Any, weapon_name: str, quantities: List[int]) -> None:
    """Handle multiple weapon quantities."""
    logger.debug(f"Handling quantities for {weapon_name}: {quantities}")
    
    # Get base supply cost
    supply_costs = get_supply_costs(weapons)
    base_cost = None
    for weapon, cost in supply_costs:
        if weapon == weapon_name:
            base_cost = cost
            break
    
    for i, quantity in enumerate(quantities):
        # Always make a copy to avoid modifying the original
        descr = base_descr.copy()
        
        # Generate new GUIDs for each variant
        descr.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
        hitroll_obj = descr.v.by_m("HitRollRuleDescriptor").v
        hitroll_obj.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
        
        # Set supply cost if available
        if base_cost is not None:
            descr.v.by_m("SupplyCost").v = str(int(base_cost) * quantity)
        
        if quantity == 1 and i == len(quantities) - 1:
            namespace = f"Ammo_{weapon_name}"
        else:
            namespace = f"Ammo_{weapon_name}_x{quantity}"
            
        logger.debug(f"Setting namespace to {namespace}")
        descr.namespace = namespace
        logger.debug(f"Adding new descriptor with namespace {namespace}")
        source.add(descr)

def _write_ammo_dictionary_entries(ingame_names: List, calibers: List) -> None:
    """Write ammunition dictionary entries."""
    entries = []
    
    # Add weapon names
    for weapon, token, display in ingame_names:
        entries.append((token, display))
        
    # Add caliber entries
    for weapon, token, display in calibers:
        entries.append((token, display))
        
    if entries:
        write_dictionary_entries(entries, dictionary_type="units") 