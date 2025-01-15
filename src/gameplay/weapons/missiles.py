"""Functions for editing missile weapons."""

from typing import Any, Dict, List, Tuple
from uuid import uuid4

from src.constants.weapons.missiles import missiles
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_MISSILES_REMOVALS,
    AMMUNITION_MISSILES_RENAMES,
)
from src.gameplay.weapons.vanilla_modifications import (
    apply_vanilla_renames,
    remove_vanilla_instances,
)
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

from .utils import get_supply_costs

logger = setup_logger(__name__)

def edit_missiles(source: Any, game_db: Dict[str, Any]) -> None:
    """Edit AmmunitionMissiles.ndf file."""
    logger.info("Editing missile weapons")
    ammo_db = game_db["ammunition"]
    
    # Handle vanilla modifications
    apply_vanilla_renames(source, AMMUNITION_MISSILES_RENAMES, ammo_db)
    remove_vanilla_instances(source, AMMUNITION_MISSILES_REMOVALS)
    
    # Track dictionary entries
    ingame_names = []
    calibers = []
    
    # First pass - remove existing entries that will be recreated
    for (weapon, category, donor, is_new), data in missiles.items():
        if data is None:
            continue
            
        # Remove existing entries that will be recreated
        if not is_new and "WeaponDescriptor" in data:
            if "SalvoLengths" in data["WeaponDescriptor"]:
                for i, length in enumerate(data["WeaponDescriptor"]["SalvoLengths"]):
                    if i != len(data["WeaponDescriptor"]["SalvoLengths"]) - 1:
                        entry = f"Ammo_{weapon}_x{length}"
                        for weapon_descr in source:
                            if weapon_descr.namespace == entry:
                                source.remove(weapon_descr)
                                logger.debug(f"Removed existing entry {entry}")
                                break
    
    # Second pass - process weapons
    for (weapon, category, donor, is_new), data in missiles.items():
        if data is None:
            continue
            
        try:
            # Get base descriptor
            base_descr = None
            for weapon_descr in source:
                if weapon_descr.namespace == f"Ammo_{weapon}":
                    base_descr = weapon_descr.copy()
                    break
                elif weapon_descr.namespace == f"Ammo_{donor}":
                    base_descr = weapon_descr.copy()
                    break
                    
            if not base_descr:
                logger.error(f"Could not find base descriptor for {weapon}")
                continue
                
            # Track dictionary entries
            if "Ammunition" in data:
                ammo_data = data["Ammunition"]
                if "displayname" in ammo_data and "nametoken" in ammo_data:
                    ingame_names.append((
                        weapon,
                        ammo_data["nametoken"],
                        ammo_data["displayname"]
                    ))
                
                if "parent_membr" in ammo_data and "Caliber" in ammo_data["parent_membr"]:
                    caliber_data = ammo_data["parent_membr"]["Caliber"]
                    if caliber_data[0] != "existing":
                        calibers.append((weapon, caliber_data[1], caliber_data[0]))
            
            # Handle salvo lengths and supply costs
            if "WeaponDescriptor" in data and "SalvoLengths" in data["WeaponDescriptor"]:
                _handle_salvo_variants(source, base_descr, weapon, data, is_new)
            
            logger.info(f"Processed missile {weapon}")
            
        except Exception as e:
            logger.error(f"Failed to edit missile {weapon}: {str(e)}")
    
    # Write dictionary entries
    if ingame_names or calibers:
        _write_missile_dictionary_entries(ingame_names, calibers)

def _handle_salvo_variants(source: Any, base_descr: Any, weapon: str, 
                         data: Dict, is_new: bool) -> None:
    """Handle salvo length variants for missile."""
    salvo_lengths = data["WeaponDescriptor"]["SalvoLengths"]
    
    # Get base supply cost
    supply_costs = get_supply_costs(missiles)
    base_cost = None
    for weapon_name, cost in supply_costs:
        if weapon_name == weapon:
            base_cost = cost
            break
    
    for i, length in enumerate(salvo_lengths):
        descr = base_descr.copy()
        
        # Generate new GUIDs for each variant
        descr.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
        hitroll_obj = descr.v.by_m("HitRollRuleDescriptor").v
        hitroll_obj.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
        
        # Set supply cost if available
        if base_cost is not None:
            descr.v.by_m("SupplyCost").v = str(int(base_cost) * length)
        
        # Set namespace
        if length == 1 and i == len(salvo_lengths) - 1:
            namespace = f"Ammo_{weapon}"
        else:
            namespace = f"Ammo_{weapon}_x{length}"
            
        descr.namespace = namespace
        
        # Apply edits
        if "Ammunition" in data:
            _apply_missile_edits(descr, data["Ammunition"], is_new)
        
        # Update salvo-specific values
        descr.v.by_m("NbTirParSalves").v = str(length)
        descr.v.by_m("AffichageMunitionParSalve").v = str(length)
        
        # Add to source
        if i > 0 or is_new:
            source.add(descr)
            logger.debug(f"Created variant {namespace}")

def _apply_missile_edits(descr: Any, data: Dict, is_new: bool) -> None:
    """Apply edits to missile descriptor."""
    membr = descr.v.by_m
    
    # Apply Arme edits
    if "Arme" in data:
        arme_data = data["Arme"]
        arme_obj = descr.v.by_m("Arme").v
        
        for arme_membr, arme_v in arme_data.items():
            if isinstance(arme_v, (float, int, bool)):
                arme_obj.by_m(arme_membr).v = str(arme_v)
            else:
                arme_obj.by_m(arme_membr).v = arme_v
    
    # Apply member edits
    if "parent_membr" in data:
        for key, value in data["parent_membr"].items():
            if key == "add":
                index = value[0]
                value = value[1]
                descr.v.insert(index, value)
            elif isinstance(value, (float, int, bool)):
                membr(key).v = str(value)
            elif isinstance(value, tuple) and key == "Caliber":
                membr(key).v = f"'{value[1]}'"
            else:
                membr(key).v = value
                
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
    roll_membrs = hitroll_obj.by_m("BaseHitValueModifiers").v
    
    for roll_type, hit_chance in hit_roll_data.items():
        if roll_type == "Idling":
            roll_membr_list = list(roll_membrs[1].v)
            roll_membr_list[1] = str(hit_chance)
            roll_membrs[1].v = tuple(roll_membr_list)
        elif roll_type == "Moving":
            roll_membr_list = list(roll_membrs[2].v)
            roll_membr_list[1] = str(hit_chance)
            roll_membrs[2].v = tuple(roll_membr_list)

def _write_missile_dictionary_entries(ingame_names: List, calibers: List) -> None:
    """Write missile dictionary entries."""
    entries = []
    
    # Add weapon names
    for weapon, token, display in ingame_names:
        entries.append((token, display))
        
    # Add caliber entries  
    for weapon, token, display in calibers:
        entries.append((token, display))
        
    if entries:
        write_dictionary_entries(entries, dictionary_type="units") 