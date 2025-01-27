"""Adjusting standard stats for weapons."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_aim_times(source_path):
    """Edit aim times for weapons."""
    for ammo_descr in source_path:
        
        has_category = False
        has_aim_time = False
        if ammo_descr.v.by_m("TypeCategoryName", False) != None:
            has_category = True
        if ammo_descr.v.by_m("TempsDeVisee", False) != None:
            has_aim_time = True

        if has_aim_time and has_category:
            ammo_type = ammo_descr.v.by_m("TypeCategoryName").v
            aim_time = ammo_descr.v.by_m("TempsDeVisee").v
            if ammo_type == "'FIQMEQMUTK'": # Tank Gun
                if aim_time == "3.0":
                    ammo_descr.v.by_m("TempsDeVisee").v = "1.5"
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} aim time to 1.5")
                    continue
                else:
                    continue

            if ammo_type == "'NZWXQNJFDX'": # Rocket Launcher
                if aim_time == "2.0":
                    ammo_descr.v.by_m("TempsDeVisee").v = "0.75"
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} aim time to 0.75")
                    continue
                else:
                    continue
            
            if ammo_type == "'GUQUYPXNMN'": # HMG
                if aim_time == "2.5":
                    unit_type = "HMG Vehicle"
                    ammo_descr.v.by_m("TempsDeVisee").v = "1.0"
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} aim time to 1.0 ({unit_type})")
                    continue
                else:
                    continue

            if ammo_type == "'BBQBDWUTJX'": # MMG
                if aim_time == "2.0":
                    unit_type = "MMG Vehicle"
                    ammo_descr.v.by_m("TempsDeVisee").v = "1.0"
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} aim time to 1.0 ({unit_type})")


def edit_weapon_ranges(source_path):
    """Edit weapon ranges."""
    
    members_to_check = {
        "PorteeMaximaleGRU": {
            1200: 1225,
        },
        "PorteeMaximaleTBAGRU": {
            2475: 2450,
        },
        "PorteeMaximaleHAGRU": {
            1950: 1925,
        },
    }
    
    for weapon_descr in source_path:
        member = weapon_descr.v.by_m
        for range_type, data in members_to_check.items():
            if member(range_type, False) == None:
                continue
            
            for old_range, new_range in data.items():
                if member(range_type).v == str(old_range):
                    member(range_type).v = str(new_range)
                    logger.info(f"(Ammunition.ndf) Changed {weapon_descr.namespace} "
                                f"{range_type} from {old_range} to {new_range}")
                    continue
            
            
