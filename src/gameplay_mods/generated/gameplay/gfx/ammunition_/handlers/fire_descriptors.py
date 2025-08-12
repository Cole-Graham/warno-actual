
def apply_fire_descriptors(source_path, logger) -> None:
    """Change fire descriptors in Ammunition.ndf"""

    for ammo_descr in source_path:

        is_napalm = False
        is_bomb = False

        traits_list = ammo_descr.v.by_m("TraitsToken")
        if any("'napalm'" in trait.v for trait in traits_list.v):
            is_napalm = True

        minmax_category = ammo_descr.v.by_m("MinMaxCategory", None)
        if minmax_category and minmax_category.v == "MinMax_Bombe":
            is_bomb = True

        if is_napalm and is_bomb:
            ammo_descr.v.by_m("FireDescriptor").v = "Descriptor_Fire_NapalmMoyenBomb"
            logger.info(f"Changed fire descriptor for {ammo_descr.namespace} to " "Descriptor_Fire_NapalmMoyenBomb")

            ammo_descr.v.by_m("Arme").v.by_m("Family").v = "DamageFamily_nplm_bomb"
            logger.info(f"Changed {ammo_descr.namespace} to DamageFamily_nplm_bomb")