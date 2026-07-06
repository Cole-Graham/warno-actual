from src.constants.effects.medium_equip_penalty_effects import MEDIUM_EQUIP_PENALTY_FLOOR_DAMAGE_LEVEL
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_gfx_damagelevels(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/DamageLevels.ndf"""
    logger.info("Modifying damage levels")

    # edit GroundUnits_packSupp
    ground_units_pack_supp = source_path.by_n("DamageLevelsPackDescriptor_GroundUnits_packSupp")
    ground_damage_levels = ground_units_pack_supp.v.by_m("DamageLevelsDescriptors")
    new_guids = [
        "GUID:{bbac0511-7b05-4e67-b98c-10bf88155513}",
        "GUID:{1762d8ea-dff5-4a67-95aa-79da6ebe6f60}",
        "GUID:{81d85239-87d0-4ceb-a10f-87b7ad2b651e}",
        "GUID:{0af3ae31-ed12-4673-a74a-8ebf051d8e5a}",
        "GUID:{2d5b31c5-6e74-4241-acca-71231459751d}",
        "GUID:{e9acc10d-bf26-4ba7-ab16-a43b2904e6db}",
    ]
    guid_index = 0
    for level in ground_damage_levels.v:

        value = level.v.by_m("Value")
        effects_packs = level.v.by_m("EffectsPacks")
        if value.v == "0":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_NoSprint_Morale")
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_Swift_ok")
            # effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Cohesion_Loss_ok")

        elif value.v == "0.1":
            pass
            # effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_Cohesion_Loss_ok")

        elif value.v == "0.25":
            pass

        elif value.v == "0.5":
            pass

        elif value.v == "0.75":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_NoSprint_Morale")

        elif value.v == "0.8":
            effects_packs.v.add("$/GFX/EffectCapacity/UnitEffect_NoSprint_Morale")

    # Insert new damage level to trigger shock sprint at 99% cohesion and prevent at < 40%
    new_ground_damage_level1 = (
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
        # f'        $/GFX/EffectCapacity/UnitEffect_Cohesion_Loss_ok,'
        f'    ]'
        f')'
    )
    ground_damage_levels.v.insert(1, new_ground_damage_level1)
    
    new_ground_damage_level2 = (
        f'TDamageLevelDescriptor'
        f'('
        f'    DescriptorId = GUID:{{e21510c8-e8e8-42dc-bd79-6770b8dc298a}}'
        f'    Value = 0.6'
        f'    LocalizationToken = "mrl_2"'
        f'    MoralModifier = 99'
        f'    AnimationType = ESoldierSuppressStatus/Suppressed'
        f'    EffectsPacks = '
        f'    ['
        f'        $/GFX/EffectCapacity/UnitEffect_GroundUnit_Cohesion_Mediocre,'
        f'        $/GFX/EffectCapacity/UnitEffect_NoSprint_Morale'
        f'    ]'
        f')'
    )
    ground_damage_levels.v.insert(5, new_ground_damage_level2)

    floor_insert_index = None
    for i, level in enumerate(ground_damage_levels.v):
        if level.v.by_m("Value").v == "0.25":
            floor_insert_index = i + 1
            break
    if floor_insert_index is not None:
        ground_damage_levels.v.insert(floor_insert_index, MEDIUM_EQUIP_PENALTY_FLOOR_DAMAGE_LEVEL)
        logger.info("Inserted medium equip penalty cohesion floor at Value 0.33")
    else:
        logger.warning("Could not find Value 0.25 to insert medium equip penalty floor")
    
    # Edit airplanes damage levels
    airplanes_pack_supp = source_path.by_n("DamageLevelsPackDescriptor_Airplanes_packSupp")
    airplanes_damage_levels = airplanes_pack_supp.v.by_m("DamageLevelsDescriptors")
    
    # Remove stress damage from damage to airplanes
    for damage_level in airplanes_damage_levels.v:
        moral_modifier = damage_level.v.by_m("MoralModifier", False)
        if moral_modifier:
            damage_level.v.by_m("MoralModifier").v = "0"
        else:
            logger.warning(f"No moral modifier found for {damage_level.namespace}")
    
    
    airplanes_damage_level6 = airplanes_damage_levels.v[5]
    effects_packs6 = airplanes_damage_level6.v.by_m("EffectsPacks")
    # Remove forced evac (airplanes can be stunned instead)
    evac_effect = effects_packs6.v.find_by_cond(
        lambda row: row.v == "$/GFX/EffectCapacity/UnitEffect_evac_avion",
        strict=False,
    )
    if evac_effect:
        effects_packs6.v.remove(evac_effect)

    # Stunned tag for airplanes is raised exclusively by the new
    # DamageLevelsPackDescriptor_Unit_packStun_Airplanes (below). Triggering it
    # from the suppress pack drove the engine into a permanent-stun state because
    # stun-recovery only operates on the stun damage track.

    # Add new packStun_Airplanes
    new_airplanes_pack_stun = (
        f'export DamageLevelsPackDescriptor_Unit_packStun_Airplanes is TDamageLevelsPackDescriptor'
        f'('
        f'    DescriptorId = GUID:{{300f1721-8477-44f5-bab9-5b33f70f32df}}'
        f'    DamageLevelsDescriptors = ['
        f'        TDamageLevelDescriptor'
        f'        ('
        f'            DescriptorId = GUID:{{c9aa8a1f-266f-4fb4-a147-33d9a78b69e9}}'
        f'            Value = 0'
        f'            EffectsPacks = ['
        f'            ]'
        f'        ),'
        f'        TDamageLevelDescriptor'
        f'        ('
        f'            DescriptorId = GUID:{{47c82f3c-2ecb-49f2-b3e2-8cb686328f0d}}'
        f'            Value = 0.70'
        f'            EffectsPacks = ['
        f'                $/GFX/EffectCapacity/UnitEffect_Unit_Stunned,'
        f'            ]'
        f'        ),'
        f'    ]'
        f')'
    )
    source_path.add(new_airplanes_pack_stun)