
def apply_fire_descriptors(source_path, logger, game_db=None) -> None:
    """Change fire descriptors in Ammunition.ndf"""
    from src.data.mounted_weapon_identity import identity_map

    ammo_db = (game_db or {}).get("ammunition") or {}
    identity = identity_map(ammo_db)

    for ammo_descr in source_path:

        is_napalm = False
        is_bomb = False

        traits_list = identity.get(ammo_descr.namespace, {}).get("TraitsToken") or []
        if any("'napalm'" in trait for trait in traits_list):
            is_napalm = True

        minmax_category = ammo_descr.v.by_m("MinMaxCategory", None)
        if minmax_category and minmax_category.v == "MinMax_Bombe":
            is_bomb = True

        if is_napalm and is_bomb:
            ammo_descr.v.by_m("FireDescriptor").v = "Descriptor_Fire_NapalmMoyenBomb"
            logger.info(f"Changed fire descriptor for {ammo_descr.namespace} to " "Descriptor_Fire_NapalmMoyenBomb")

            ammo_descr.v.by_m("Arme").v.by_m("Family").v = "DamageFamily_nplm_bomb"
            logger.info(f"Changed {ammo_descr.namespace} to DamageFamily_nplm_bomb")