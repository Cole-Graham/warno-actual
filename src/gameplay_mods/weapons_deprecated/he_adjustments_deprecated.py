"""HE adjustments for canons."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


# def edit_he_damage(source_path, game_db):  # noqa
#     """Edit HE damage for weapons in Ammunition.ndf"""
    
#     damage_map = {
#         "'BMQJOXODMC'": "1.25",  # 105mm
#         "'DYWXTLDKWR'": "1.5",   # 120mm
#         "'GPFACVPVNW'": "1.6",   # 125mm
#     }
    
#     exceptions = [
#         "Ammo_Canon_HE_73_mm_SPG9",
#         "Ammo_Canon_HE_73_mm_SPG9_TOWED",
#     ]
    
#     for ammo_descr in source_path:
#         namespace = ammo_descr.namespace
#         if namespace in exceptions:
#             continue
        
#         if ammo_descr.v.by_m("Name", False) is None:
#             logger.debug(f"No name found for {namespace}")
#             continue
        
#         name_membr = ammo_descr.v.by_m("Name").v
#         if name_membr == "'None'":
#             continue
        
#         minmax_category = ammo_descr.v.by_m("MinMaxCategory").v
#         if minmax_category != "MinMax_CanonAP":
#             continue
        
#         piercing_bool = ammo_descr.v.by_m("PiercingWeapon").v
#         if piercing_bool == "True":
#             continue
        
#         caliber_membr = ammo_descr.v.by_m("Caliber").v
#         if caliber_membr in damage_map:
#             ammo_descr.v.by_m("PhysicalDamages").v = damage_map[caliber_membr]
#             logger.info(f"Changed {namespace} HE damage to {damage_map[caliber_membr]}")
