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
    lower_percentage = lower_bound[1]  # Percentage value from table (e.g., 300 = 300%)
    upper_range_step = upper_bound[0]
    upper_percentage = upper_bound[1]  # Percentage value from table
    
    # The game's C++ code does: base * (1 + value/100)
    # Test case: base 30%, veterancy +5% multiplicative = 31.5%, at 0.67 range with value 30
    # Game result: 40-41% = 31.5% * (1 + 30/100) = 31.5% * 1.3 = 40.95% ✓
    # So the table values are bonus percentages that get added to 1.0
    lower_bonus = lower_percentage / 100.0  # e.g., 300 -> 3.0 bonus → base * (1 + 3.0) = base * 4.0
    upper_bonus = upper_percentage / 100.0  # e.g., 30 -> 0.3 bonus → base * (1 + 0.3) = base * 1.3
    # Interpolate bonuses directly
    if upper_range_step == lower_range_step:
        interpolated_bonus = lower_bonus
    else:
        interpolated_bonus = lower_bonus + (
            (range_fraction - lower_range_step) *
            ((upper_bonus - lower_bonus) / (upper_range_step - lower_range_step))
        )
        # print(f"range_m: {range_m}")
        # print(f"range_fraction: {range_fraction}")
        # print(f"lower_range_step: {lower_range_step}")
        # print(f"range_fraction - lower_range_step: {range_fraction - lower_range_step}")
        # print(f"interpolated_bonus: {interpolated_bonus}")
        # print(f"--------------------------------")
    
    # Final accuracy calculation: (base accuracy + veterancy bonus) * (1 + interpolated percentage bonus) * successive hit bonus
    final_accuracy = base_accuracy_with_vet * (1 + interpolated_bonus) * successive_hit_bonus
    # print(f"{min(final_accuracy, 1.0):.2f}")
    # print(f"_______________________________")
    
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


def calculate_shots_per_minute(ammo_props: Dict[str, Any], reload_speed_multiplier: float = 1.0, shot_time_multiplier: float = 1.0) -> float:
    """Calculate shots per minute from ammunition properties.
    
    Args:
        ammo_props: Ammunition properties dictionary
        reload_speed_multiplier: Multiplier for time between salvos (e.g., 0.8 means 20% faster)
        shot_time_multiplier: Multiplier for time between shots (e.g., 0.85 means 15% faster)
    """
    shots_count_per_salvo = ammo_props.get("shots_count_per_salvo", 1)
    time_between_salvos = ammo_props.get("time_between_salvos", 1.0)
    time_between_shots = ammo_props.get("time_between_shots", None)
    aiming_time = ammo_props.get("aiming_time", 0.0)
    
    # Apply reload speed multiplier (multiplier < 1.0 means faster reload)
    time_between_salvos = time_between_salvos * reload_speed_multiplier
    
    if time_between_shots is not None:
        # Apply shot time multiplier to time between shots
        time_between_shots = time_between_shots * shot_time_multiplier
        # Calculate time per salvo (aiming_time only happens before first salvo, not included here)
        time_per_salvo = time_between_shots * (shots_count_per_salvo - 1)
        # Total cycle time between salvos (aiming_time is only for the first salvo, so not in cycle)
        total_cycle_time = time_per_salvo + time_between_salvos
    else:
        # Use time between salvos as cycle time
        total_cycle_time = time_between_salvos
    
    # Calculate shots per minute
    # Note: aiming_time only affects the first salvo, so for sustained fire rate it's not included
    if total_cycle_time > 0:
        shots_per_minute = (60.0 / total_cycle_time) * shots_count_per_salvo
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
    has_shock_trait: bool = False,
    shock_range: float = 100.0,
    shock_bonuses: Optional[Dict[str, float]] = None,
    has_militia_trait: bool = False,
    militia_bonuses: Optional[Dict[str, float]] = None,
    has_reservist_trait: bool = False,
    reservist_bonuses: Optional[Dict[str, float]] = None,
    damage_ratio_multiplier: float = 1.0,
    damage_type: str = "Physical",
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
        has_shock_trait: Whether the unit has the Shock trait (_choc)
        shock_range: Range threshold for shock bonuses to activate (default 100m)
        has_militia_trait: Whether the unit has the Militia trait (militia)
        militia_bonuses: Dictionary with militia bonus multipliers (reload_speed_multiplier, aim_time_multiplier)
        has_reservist_trait: Whether the unit has the Reservist trait (reservist)
        reservist_bonuses: Dictionary with reservist bonus multipliers (reload_speed_multiplier, aim_time_multiplier)
        damage_type: Type of damage to use ("Physical" or "Suppression")
        
    Returns:
        List of (range, DPM) tuples
    """
    max_range = ammo_props.get("max_range", 0.0)
    base_accuracy = ammo_props.get("idling", 0.0)
    
    # Get the appropriate damage value based on damage type
    if damage_type == "Suppression":
        base_damages = ammo_props.get("suppress_damages", 0.0)
    else:
        base_damages = ammo_props.get("physical_damages", 0.0)
    
    # Base shots per minute calculation (will be recalculated with shock bonuses if applicable)
    # This line is not used, but kept for reference
    
    if max_range <= 0 or base_accuracy <= 0 or base_damages <= 0:
        return []
    
    # Shock bonuses (from UnitEffect_Choc, parsed from game files):
    # Default values if not provided
    if shock_bonuses is None:
        shock_bonuses = {
            "damage_multiplier": 1.15,
            "salvo_reload_multiplier": 0.85,
            "shot_time_multiplier": 0.85,
            "aim_time_multiplier": 0.85,
        }
    
    # Extract shock multipliers
    SHOCK_DAMAGE_MULTIPLIER = shock_bonuses.get("damage_multiplier", 1.15)
    SHOCK_SALVO_RELOAD_MULTIPLIER = shock_bonuses.get("salvo_reload_multiplier", 0.85)
    SHOCK_SHOT_TIME_MULTIPLIER = shock_bonuses.get("shot_time_multiplier", 0.85)
    SHOCK_AIM_TIME_MULTIPLIER = shock_bonuses.get("aim_time_multiplier", 0.85)
    
    # Note: reload_speed_multiplier in calculate_shots_per_minute multiplies time (lower = faster)
    # Shock multipliers also multiply time (lower = faster), so we multiply directly
    # For aim time, we convert to speed multiplier (inverse) since it affects accuracy calculation
    SHOCK_AIM_TIME_SPEED_MULTIPLIER = 1.0 / SHOCK_AIM_TIME_MULTIPLIER if SHOCK_AIM_TIME_MULTIPLIER > 0 else 1.0
    
    # Militia bonuses (from UnitEffect_militia, parsed from game files):
    # Default values if not provided
    if militia_bonuses is None:
        militia_bonuses = {
            "reload_speed_multiplier": 1.20,
            "aim_time_multiplier": 1.20,
        }
    
    # Extract militia multipliers
    MILITIA_RELOAD_MULTIPLIER = militia_bonuses.get("reload_speed_multiplier", 1.20)
    MILITIA_AIM_TIME_MULTIPLIER = militia_bonuses.get("aim_time_multiplier", 1.20)
    
    # Note: militia multipliers multiply time (higher = slower)
    # For aim time, we convert to speed multiplier (inverse) since it affects accuracy calculation
    MILITIA_AIM_TIME_SPEED_MULTIPLIER = 1.0 / MILITIA_AIM_TIME_MULTIPLIER if MILITIA_AIM_TIME_MULTIPLIER > 0 else 1.0
    
    # Reservist bonuses (from UnitEffect_reservist, parsed from game files):
    # Default values if not provided
    if reservist_bonuses is None:
        reservist_bonuses = {
            "reload_speed_multiplier": 1.20,
            "aim_time_multiplier": 1.20,
        }
    
    # Extract reservist multipliers
    RESERVIST_RELOAD_MULTIPLIER = reservist_bonuses.get("reload_speed_multiplier", 1.20)
    RESERVIST_AIM_TIME_MULTIPLIER = reservist_bonuses.get("aim_time_multiplier", 1.20)
    
    # Note: reservist multipliers multiply time (higher = slower)
    # For aim time, we convert to speed multiplier (inverse) since it affects accuracy calculation
    RESERVIST_AIM_TIME_SPEED_MULTIPLIER = 1.0 / RESERVIST_AIM_TIME_MULTIPLIER if RESERVIST_AIM_TIME_MULTIPLIER > 0 else 1.0
    
    dpm_data = []
    current_range = 0.0
    
    while current_range <= max_range:
        # Check if shock bonuses apply (within shock_range)
        is_shock_range = has_shock_trait and current_range <= shock_range
        
        # Apply reload multipliers (shock, militia, and reservist)
        effective_reload_multiplier = reload_speed_multiplier
        effective_shot_time_multiplier = 1.0
        
        # Apply shock reload multipliers if in shock range
        if is_shock_range:
            # Apply salvo reload multiplier directly (multiplies time, lower = faster)
            # If reload_speed_multiplier is 1.0 and SHOCK_SALVO_RELOAD_MULTIPLIER is 0.85,
            # then effective_reload_multiplier = 0.85 (15% faster)
            effective_reload_multiplier = effective_reload_multiplier * SHOCK_SALVO_RELOAD_MULTIPLIER
            # Apply shot time multiplier separately (also multiplies time, lower = faster)
            effective_shot_time_multiplier = SHOCK_SHOT_TIME_MULTIPLIER
        
        # Apply militia reload multiplier (applies at all ranges, multiplies time, higher = slower)
        if has_militia_trait:
            effective_reload_multiplier = effective_reload_multiplier * MILITIA_RELOAD_MULTIPLIER
        
        # Apply reservist reload multiplier (applies at all ranges, multiplies time, higher = slower)
        if has_reservist_trait:
            effective_reload_multiplier = effective_reload_multiplier * RESERVIST_RELOAD_MULTIPLIER
        
        # Recalculate shots per minute with bonuses if applicable
        shots_per_minute = calculate_shots_per_minute(ammo_props, effective_reload_multiplier, effective_shot_time_multiplier)
        
        # Calculate accuracy (shock, militia, and reservist aim time bonuses affect accuracy)
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
        
        # Apply shock aim time multiplier to accuracy (faster aiming = better accuracy)
        if is_shock_range:
            # Faster aim time means more accurate, apply as multiplicative bonus
            accuracy = min(1.0, accuracy * SHOCK_AIM_TIME_SPEED_MULTIPLIER)
        
        # Apply militia aim time multiplier to accuracy (slower aiming = less accurate)
        if has_militia_trait:
            # Slower aim time means less accurate, apply as multiplicative penalty
            accuracy = accuracy * MILITIA_AIM_TIME_SPEED_MULTIPLIER
        
        # Apply reservist aim time multiplier to accuracy (slower aiming = less accurate)
        if has_reservist_trait:
            # Slower aim time means less accurate, apply as multiplicative penalty
            accuracy = accuracy * RESERVIST_AIM_TIME_SPEED_MULTIPLIER
        
        # Apply shock damage multiplier (only applies to physical damage, not suppression)
        effective_damage = base_damages
        if is_shock_range and damage_type == "Physical":
            effective_damage = base_damages * SHOCK_DAMAGE_MULTIPLIER
        
        # Apply damage ratio multiplier (for infantry vs infantry strength differences)
        # Ensure damage_ratio_multiplier is valid (default to 1.0 if invalid)
        if damage_ratio_multiplier is None or not isinstance(damage_ratio_multiplier, (int, float)) or damage_ratio_multiplier < 0:
            damage_ratio_multiplier = 1.0
        effective_damage = effective_damage * damage_ratio_multiplier
        
        dpm = accuracy * effective_damage * shots_per_minute * weapon_quantity
        dpm_data.append((current_range, dpm))
        current_range += range_step
    
    # Only add max range point if it's significantly different from the last point
    # (prevents vertical jumps when last point is already very close to max_range)
    if dpm_data:
        last_range = dpm_data[-1][0]
        if abs(max_range - last_range) > range_step * 0.1:  # Only add if difference > 10% of step size
            # Check if shock bonuses apply at max range
            is_shock_range = has_shock_trait and max_range <= shock_range
            
            # Apply reload multipliers (shock, militia, and reservist)
            effective_reload_multiplier = reload_speed_multiplier
            effective_shot_time_multiplier = 1.0
            
            # Apply shock reload multipliers if in shock range
            if is_shock_range:
                # Apply salvo reload multiplier directly (multiplies time, lower = faster)
                effective_reload_multiplier = effective_reload_multiplier * SHOCK_SALVO_RELOAD_MULTIPLIER
                # Apply shot time multiplier separately
                effective_shot_time_multiplier = SHOCK_SHOT_TIME_MULTIPLIER
            
            # Apply militia reload multiplier (applies at all ranges, multiplies time, higher = slower)
            if has_militia_trait:
                effective_reload_multiplier = effective_reload_multiplier * MILITIA_RELOAD_MULTIPLIER
            
            # Apply reservist reload multiplier (applies at all ranges, multiplies time, higher = slower)
            if has_reservist_trait:
                effective_reload_multiplier = effective_reload_multiplier * RESERVIST_RELOAD_MULTIPLIER
            
            # Recalculate shots per minute with bonuses if applicable
            shots_per_minute = calculate_shots_per_minute(ammo_props, effective_reload_multiplier, effective_shot_time_multiplier)
            
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
            
            # Apply shock aim time multiplier to accuracy
            if is_shock_range:
                accuracy = min(1.0, accuracy * SHOCK_AIM_TIME_SPEED_MULTIPLIER)
            
            # Apply militia aim time multiplier to accuracy (slower aiming = less accurate)
            if has_militia_trait:
                accuracy = accuracy * MILITIA_AIM_TIME_SPEED_MULTIPLIER
            
            # Apply reservist aim time multiplier to accuracy (slower aiming = less accurate)
            if has_reservist_trait:
                accuracy = accuracy * RESERVIST_AIM_TIME_SPEED_MULTIPLIER
            
            # Apply shock damage multiplier (only applies to physical damage, not suppression)
            effective_damage = base_damages
            if is_shock_range and damage_type == "Physical":
                effective_damage = base_damages * SHOCK_DAMAGE_MULTIPLIER
            
            # Apply damage ratio multiplier (for infantry vs infantry strength differences)
            # Ensure damage_ratio_multiplier is valid (default to 1.0 if invalid)
            if damage_ratio_multiplier is None or not isinstance(damage_ratio_multiplier, (int, float)) or damage_ratio_multiplier < 0:
                damage_ratio_multiplier = 1.0
            effective_damage = effective_damage * damage_ratio_multiplier
            
            dpm = accuracy * effective_damage * shots_per_minute * weapon_quantity
            dpm_data.append((max_range, dpm))
    
    return dpm_data
