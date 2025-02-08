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
                    logger.warning(f"(Ammunition.ndf) {ammo_descr.namespace} aim time is not 3.0, likely changed by Eugen")
                    continue

            if ammo_type == "'NZWXQNJFDX'": # Rocket Launcher
                if aim_time == "1.5":
                    ammo_descr.v.by_m("TempsDeVisee").v = "1.0"
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} aim time to 1.0")
                    continue
                else:
                    logger.warning(f"(Ammunition.ndf) {ammo_descr.namespace} aim time is not 1.5, likely changed by Eugen")
                    continue
            
            if ammo_type == "'GUQUYPXNMN'": # HMG
                if aim_time == "2.5":
                    unit_type = "HMG Vehicle"
                    ammo_descr.v.by_m("TempsDeVisee").v = "1.0"
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} aim time to 1.0 ({unit_type})")
                    continue
                else:
                    logger.warning(f"(Ammunition.ndf) {ammo_descr.namespace} aim time is not 2.5, likely changed by Eugen")
                    continue


            if ammo_type == "'BBQBDWUTJX'": # MMG
                if aim_time == "2.2":
                    unit_type = "MMG Vehicle"
                    ammo_descr.v.by_m("TempsDeVisee").v = "1.0"
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} aim time to 1.0 ({unit_type})")
                    continue
                else:
                    logger.warning(f"(Ammunition.ndf) {ammo_descr.namespace} aim time is not 2.2, likely changed by Eugen")
                    continue


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
            
            
def bomb_damage_standards(source_path):
    """Edit bomb damage standards in Ammunition.ndf"""
    
    bombs = {
        "he_250kg": {
            "PhysicalDamages": 10,
            "RadiusSplashPhysicalDamagesGRU": 110,
            "RadiusSplashSuppressDamagesGRU": 147,
        },
        "he_500kg": {
            "PhysicalDamages": 15,
            "RadiusSplashPhysicalDamagesGRU": 150,
            "RadiusSplashSuppressDamagesGRU": 200,
        },
        "he_1000kg": {
            "PhysicalDamages": 20,
            "SuppressDamages": 750,
            "RadiusSplashPhysicalDamagesGRU": 170,
            "RadiusSplashSuppressDamagesGRU": 225,
        },
        "he_1250kg": {
            "PhysicalDamages": 25,
            "SuppressDamages": 990,
            "RadiusSplashPhysicalDamagesGRU": 200,
            "RadiusSplashSuppressDamagesGRU": 265,
        },
    }
    

    he_bomb_matching = {
        "250": ["250kg", "GBU_12"],
        "500": ["450kg","500kg", "513kg"],
        "1000": ["1000kg", "GBU_10", "GBU_27"],
        "1250": ["KAB_1500"],
    }
    

    for ammo_descr in source_path:
        
        ammo_name = ammo_descr.namespace
        # name_hash = ammo_descr.v.by_m("Name")
        traits_list = ammo_descr.v.by_m("TraitsToken")        
        if any("'HE'" in trait.v for trait in traits_list.v):
            
            if any(bomb in ammo_name for bomb in he_bomb_matching["250"]):
                for key, value in bombs["he_250kg"].items():
                    ammo_descr.v.by_m(key).v = str(value)
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} "
                                f"{key} to {value}")
            
            elif any(bomb in ammo_name for bomb in he_bomb_matching["500"]):
                for key, value in bombs["he_500kg"].items():
                    ammo_descr.v.by_m(key).v = str(value)
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} "
                                f"{key} to {value}")
            
            elif any(bomb in ammo_name for bomb in he_bomb_matching["1000"]):
                for key, value in bombs["he_1000kg"].items():
                    ammo_descr.v.by_m(key).v = str(value)
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} "
                                f"{key} to {value}")
            
            elif any(bomb in ammo_name for bomb in he_bomb_matching["1250"]):
                for key, value in bombs["he_1250kg"].items():
                    ammo_descr.v.by_m(key).v = str(value)
                    logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} "
                                f"{key} to {value}")
        
        else:
            continue

