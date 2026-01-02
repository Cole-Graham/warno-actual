from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_gfx_damagelevels(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/DamageLevels.ndf"""
    logger.info("Modifying damage levels")

    # edit GroundUnits_packSupp
    ground_units_pack_supp = source_path.by_n("DamageLevelsPackDescriptor_GroundUnits_packSupp")
    damage_levels = ground_units_pack_supp.v.by_m("DamageLevelsDescriptors")
    new_guids = [
        "GUID:{bbac0511-7b05-4e67-b98c-10bf88155513}",
        "GUID:{1762d8ea-dff5-4a67-95aa-79da6ebe6f60}",
        "GUID:{81d85239-87d0-4ceb-a10f-87b7ad2b651e}",
        "GUID:{0af3ae31-ed12-4673-a74a-8ebf051d8e5a}",
        "GUID:{2d5b31c5-6e74-4241-acca-71231459751d}",
        "GUID:{e9acc10d-bf26-4ba7-ab16-a43b2904e6db}",
    ]
    guid_index = 0
    for level in damage_levels.v:

        value = level.v.by_m("Value")
        effects_packs = level.v.by_m("EffectsPacks")
        if value.v == "0":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_no_Choc_Move_Morale")
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_Swift_ok")
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Cohesion_Loss_ok")

        elif value.v == "0.1":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Cohesion_Loss_ok")

        elif value.v == "0.25":
            pass

        elif value.v == "0.5":
            pass

        elif value.v == "0.75":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_no_Choc_Move_Morale")

        elif value.v == "0.8":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_no_Choc_Move_Morale")

    # Insert new damage level to trigger shock sprint at 99% cohesion and prevent at < 40%
    new_damage_level1 = (
        f'TDamageLevelDescriptor'
        f'('
        f'    DescriptorId = GUID:{{932c70e6-e41f-45ad-bd94-866aec4efeed}}'
        f'    Value = 0.01'
        f'    LocalizationToken = "mrl_4"'
        f'    MoralModifier = 99'
        f'    AnimationType = ESoldierSuppressStatus/Operational'
        f'    EffectsPacks = '
        f'    ['
        f'        $/GFX/EffectCapacity/UnitEffect_GroundUnit_Cohesion_High,'
        f'        $/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_Swift_ok,'
        f'        $/GFX/EffectCapacity/UnitEffect_Cohesion_Loss_ok,'
        f'    ]'
        f')'
    )
    damage_levels.v.insert(1, new_damage_level1)
    
    new_damage_level2 = (
        f'TDamageLevelDescriptor'
        f'('
        f'    DescriptorId = GUID:{{e21510c8-e8e8-42dc-bd79-6770b8dc298a}}'
        f'    Value = 0.6'
        f'    LocalizationToken = "mrl_2"'
        f'    MoralModifier = 99'
        f'    AnimationType = ESoldierSuppressStatus/Suppressed'
        f'    EffectsPacks = '
        f'    ['
        f'        $/GFX/EffectCapacity/UnitEffect_Precision_moins_45,'
        f'        $/GFX/EffectCapacity/UnitEffect_GroundUnit_Cohesion_Mediocre,'
        f'        $/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_no_Choc_Move_Morale'
        f'    ]'
        f')'
    )
    damage_levels.v.insert(5, new_damage_level2)