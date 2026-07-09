"""Medium equip penalty capacity-related unit effects."""

MEDIUM_EQUIP_PENALTY_TICK_SECONDS = 1.0
MEDIUM_EQUIP_PENALTY_SUPPRESS_DAMAGE = 25
MEDIUM_EQUIP_PENALTY_SF_SUPPRESS_DAMAGE = 40
MEDIUM_EQUIP_PENALTY_CAPACITY_DURATION = 0.1
MEDIUM_EQUIP_PENALTY_COHESION_FLOOR_VALUE = 0.34

_medium_equip_penalty_tick_label = (
    "every second"
    if MEDIUM_EQUIP_PENALTY_TICK_SECONDS == 1
    else f"every {MEDIUM_EQUIP_PENALTY_TICK_SECONDS:g} seconds"
)
MEDIUM_EQUIP_PENALTY_TRAIT_SUPPRESS_LINE = (
    f"Accumulates {MEDIUM_EQUIP_PENALTY_SUPPRESS_DAMAGE} suppression damage "
    f"{_medium_equip_penalty_tick_label} while moving "
    f"(cannot reduce cohesion below {100 - (int(MEDIUM_EQUIP_PENALTY_COHESION_FLOOR_VALUE * 100))}%)"
)

MEDIUM_EQUIP_PENALTY_EFFECT = (
    'export UnitEffect_Medium_Equip_Penalty is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{0ba81a5a-8c30-4501-91c6-b1b3df271393}'
    "    NameForDebug       = 'Medium_Equip_Penalty'"
    '    EffectsDescriptors = ['
    '        TEffectInflictDamageDescriptor'
    '        ('
    '            DamageType = ~/EDamageType/Suppress'
    '            ModifierType = ~/ModifierType_Additionnel'
    f'            DamageValue = {MEDIUM_EQUIP_PENALTY_SUPPRESS_DAMAGE}'
    '        ),'
    '    ]'
    ')'
)

MEDIUM_EQUIP_PENALTY_SF_EFFECT = (
    'export UnitEffect_Medium_Equip_Penalty_SF is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{f7a8b9c0-d1e2-4f34-a567-890abcdef326}'
    "    NameForDebug       = 'Medium_Equip_Penalty_SF'"
    '    EffectsDescriptors = ['
    '        TEffectInflictDamageDescriptor'
    '        ('
    '            DamageType = ~/EDamageType/Suppress'
    '            ModifierType = ~/ModifierType_Additionnel'
    f'            DamageValue = {MEDIUM_EQUIP_PENALTY_SF_SUPPRESS_DAMAGE}'
    '        ),'
    '    ]'
    ')'
)

MEDIUM_EQUIP_PENALTY_FLOOR_TAG_EFFECT = (
    'export UnitEffect_Ajoute_Tag_Medium_Equip_Penalty_floor is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{b3c4d5e6-f7a8-4901-c234-56789abcdef2}'
    "    NameForDebug       = 'Ajoute_Tag_Medium_Equip_Penalty_floor'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["Medium_Equip_Penalty_floor"]'
    '        )'
    '    ]'
    ')'
)

MEDIUM_EQUIP_PENALTY_FLOOR_DAMAGE_LEVEL = (
    f'TDamageLevelDescriptor'
    f'('
    f'    DescriptorId = GUID:{{c4d5e6f7-a8b9-4012-d345-6789abcdef03}}'
    f'    Value = {MEDIUM_EQUIP_PENALTY_COHESION_FLOOR_VALUE}'
    f'    LocalizationToken = "mrl_3"'
    f'    MoralModifier = 99'
    f'    AnimationType = ESoldierSuppressStatus/Suppressed'
    f'    EffectsPacks = '
    f'    ['
    f'        $/GFX/EffectCapacity/UnitEffect_GroundUnit_Cohesion_Normal,'
    f'        $/GFX/EffectCapacity/UnitEffect_Ajoute_Tag_Medium_Equip_Penalty_floor,'
    f'    ]'
    f')'
)
