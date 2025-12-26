"""Calculation Functions for DPM Visualizer."""

import re
from typing import Any, Dict, List, Optional, Tuple

from .constants import RANGE_MODIFIERS_TABLE


def calculate_accuracy(
    range_m: float,
    weapon_max_range: float,
    base_accuracy: float,
    successive_hits: int,
    veterancy_level: int = 0,
    veterancy_accuracy_bonus: float = 0.0,
    range_modifiers_table: Optional[List[Tuple[float, float]]] = None,
    use_multiplicative_vet_bonus: bool = True,
) -> float:
    """Calculate accuracy at a given range with modifiers.
    
    Args:
        range_m: Current range in meters
        weapon_max_range: Maximum range of the weapon in meters
        base_accuracy: Base accuracy (0.0-1.0)
        successive_hits: Number of successive hits (0-5)
        veterancy_level: Veterancy level (0-3)
        veterancy_accuracy_bonus: Accuracy bonus from veterancy effects (percentage, e.g., 0.12 for 12%)
        range_modifiers_table: Optional range modifiers table. If None, uses RANGE_MODIFIERS_TABLE.
        use_multiplicative_vet_bonus: If True, apply veterancy bonus multiplicatively (base * (1 + bonus)).
                                      If False, apply as flat bonus (base + bonus), capped at 1.0.
        
    Returns:
        Final accuracy (0.0-1.0), capped at 1.0
    """
    # Use provided table or default to global RANGE_MODIFIERS_TABLE
    modifiers_table = range_modifiers_table if range_modifiers_table is not None else RANGE_MODIFIERS_TABLE
    
    # If range exceeds max range, return 0%
    if range_m > weapon_max_range:
        return 0.0
    
    # Convert range to fraction of max range
    range_fraction = range_m / weapon_max_range
    
    # Cap successive hits bonus to maximum of 5 hits
    successive_hit_bonus = 1 + min(successive_hits, 5) * 0.03  # 3% per hit, up to 5 hits (15%)
    
    # Apply veterancy accuracy bonus from EffetsSurUnite.ndf
    if use_multiplicative_vet_bonus:
        base_accuracy_with_vet = base_accuracy * (1 + veterancy_accuracy_bonus)
    else:
        # Flat bonus: add directly and cap at 1.0
        base_accuracy_with_vet = min(base_accuracy + veterancy_accuracy_bonus, 1.0)
    
    # Special case: if rangeFraction is exactly 1.0, no interpolation needed
    # At max range, use base accuracy with veterancy and successive hit bonus but no range modifier bonus
    if range_fraction >= 1.0:
        final_accuracy = base_accuracy_with_vet * successive_hit_bonus
        return min(final_accuracy, 1.0)
    
    # Find the two range steps between which the current rangeFraction falls
    lower_bound = None
    upper_bound = None
    
    for i in range(len(modifiers_table) - 1):
        current = modifiers_table[i]
        next_entry = modifiers_table[i + 1]
        
        if range_fraction >= current[0] and range_fraction <= next_entry[0]:
            lower_bound = current
            upper_bound = next_entry
            break
    
    if lower_bound is None or upper_bound is None:
        # Fallback: use closest entry
        if range_fraction < modifiers_table[0][0]:
            lower_bound = upper_bound = modifiers_table[0]
        else:
            lower_bound = upper_bound = modifiers_table[-1]
    
    # Perform linear interpolation between lowerBound and upperBound
    lower_range_step = lower_bound[0]
    lower_multiplier = lower_bound[1]  # This is the multiplier (e.g., 3.0 means 300% of base)
    upper_range_step = upper_bound[0]
    upper_multiplier = upper_bound[1]  # This is the multiplier
    
    # Special handling: if upper_bound is (1.00, 0), treat it as multiplier 1.0 (no bonus)
    # The 0 is just a marker, not an actual multiplier value
    if upper_range_step == 1.0 and upper_multiplier == 0:
        upper_multiplier = 1.0
    
    # Convert multipliers to percentage increases for interpolation
    lower_accuracy_bonus = lower_multiplier - 1  # Convert multiplier to percentage increase
    upper_accuracy_bonus = upper_multiplier - 1  # Convert multiplier to percentage increase
    
    if upper_range_step == lower_range_step:
        interpolated_bonus = lower_accuracy_bonus
    else:
        interpolated_bonus = lower_accuracy_bonus + (
            (range_fraction - lower_range_step) *
            ((upper_accuracy_bonus - lower_accuracy_bonus) / (upper_range_step - lower_range_step))
        )
    
    # Final accuracy calculation: (base accuracy + veterancy bonus) * (1 + interpolated percentage bonus) * successive hit bonus
    final_accuracy = base_accuracy_with_vet * (1 + interpolated_bonus) * successive_hit_bonus
    
    # Return the final accuracy capped at 100%
    return min(final_accuracy, 1.0)


def extract_base_weapon_name(ammo_name: str) -> str:
    """Extract base weapon name by removing strength and quantity suffixes.
    
    Examples:
        FM_M16_strength6_x2 -> FM_M16
        FM_FAMAS_x4 -> FM_FAMAS
        Sniper_FRF1 -> Sniper_FRF1
    """
    # Remove strength suffix (e.g., _strength6)
    ammo_name = re.sub(r'_strength\d+', '', ammo_name)
    # Remove quantity suffix (e.g., _x2)
    ammo_name = re.sub(r'_x\d+$', '', ammo_name)
    # Remove salvolength suffix (e.g., _salvolength10)
    ammo_name = re.sub(r'_salvolength\d+', '', ammo_name)
    return ammo_name


def calculate_shots_per_minute(ammo_props: Dict[str, Any], reload_speed_multiplier: float = 1.0) -> float:
    """Calculate shots per minute from ammunition properties.
    
    Args:
        ammo_props: Ammunition properties dictionary
        reload_speed_multiplier: Multiplier for time between salvos (e.g., 0.8 means 20% faster)
    """
    nb_tir_par_salves = ammo_props.get("nb_tir_par_salves", 1)
    time_between_salvos = ammo_props.get("time_between_salvos", 1.0)
    time_between_shots = ammo_props.get("time_between_shots", None)
    aiming_time = ammo_props.get("aiming_time", 0.0)
    
    # Apply reload speed multiplier (multiplier < 1.0 means faster reload)
    time_between_salvos = time_between_salvos * reload_speed_multiplier
    
    if time_between_shots is not None:
        # Calculate time per salvo (aiming_time only happens before first salvo, not included here)
        time_per_salvo = time_between_shots * (nb_tir_par_salves - 1)
        # Total cycle time between salvos (aiming_time is only for the first salvo, so not in cycle)
        total_cycle_time = time_per_salvo + time_between_salvos
    else:
        # Use time between salvos as cycle time
        total_cycle_time = time_between_salvos
    
    # Calculate shots per minute
    # Note: aiming_time only affects the first salvo, so for sustained fire rate it's not included
    if total_cycle_time > 0:
        shots_per_minute = (60.0 / total_cycle_time) * nb_tir_par_salves
    else:
        shots_per_minute = 0.0
    
    return shots_per_minute


def calculate_dpm(
    ammo_props: Dict[str, Any],
    weapon_quantity: int,
    successive_hits: int,
    range_step: float = 25.0,
    veterancy_level: int = 0,
    veterancy_accuracy_bonus: float = 0.0,
    reload_speed_multiplier: float = 1.0,
    range_modifiers_table: Optional[List[Tuple[float, float]]] = None,
    use_multiplicative_vet_bonus: bool = True,
) -> List[Tuple[float, float]]:
    """Calculate DPM at different ranges.
    
    Args:
        ammo_props: Ammunition properties dictionary
        weapon_quantity: Number of weapons
        successive_hits: Number of successive hits (0-5)
        range_step: Range step size in meters (default 25.0)
        veterancy_level: Veterancy level (0-3)
        veterancy_accuracy_bonus: Accuracy bonus from veterancy effects (percentage, e.g., 0.12 for 12%)
        reload_speed_multiplier: Multiplier for time between salvos (e.g., 0.8 means 20% faster)
        range_modifiers_table: Optional range modifiers table. If None, uses RANGE_MODIFIERS_TABLE.
        
    Returns:
        List of (range, DPM) tuples
    """
    max_range = ammo_props.get("max_range", 0.0)
    base_accuracy = ammo_props.get("idling", 0.0)
    physical_damages = ammo_props.get("physical_damages", 0.0)
    shots_per_minute = calculate_shots_per_minute(ammo_props, reload_speed_multiplier)
    
    if max_range <= 0 or base_accuracy <= 0 or physical_damages <= 0:
        return []
    
    dpm_data = []
    current_range = 0.0
    
    while current_range <= max_range:
        accuracy = calculate_accuracy(
            current_range,
            max_range,
            base_accuracy,
            successive_hits,
            veterancy_level,
            veterancy_accuracy_bonus,
            range_modifiers_table,
            use_multiplicative_vet_bonus,
        )
        dpm = accuracy * physical_damages * shots_per_minute * weapon_quantity
        dpm_data.append((current_range, dpm))
        current_range += range_step
    
    # Only add max range point if it's significantly different from the last point
    # (prevents vertical jumps when last point is already very close to max_range)
    if dpm_data:
        last_range = dpm_data[-1][0]
        if abs(max_range - last_range) > range_step * 0.1:  # Only add if difference > 10% of step size
            accuracy = calculate_accuracy(
                max_range,
                max_range,
                base_accuracy,
                successive_hits,
                veterancy_level,
                veterancy_accuracy_bonus,
                range_modifiers_table,
                use_multiplicative_vet_bonus,
            )
            dpm = accuracy * physical_damages * shots_per_minute * weapon_quantity
            dpm_data.append((max_range, dpm))
    
    return dpm_data
