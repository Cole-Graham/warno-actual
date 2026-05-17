"""Medium equip penalty capacity-related unit effects."""

MEDIUM_EQUIP_PENALTY_EFFECT = (
    'export UnitEffect_Medium_Equip_Penalty is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{0ba81a5a-8c30-4501-91c6-b1b3df271393}'
    "    NameForDebug       = 'Medium_Equip_Penalty'"
    '    EffectsDescriptors = ['
    '        TUnitEffectIncreaseDamageTakenDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    '            BonusDamage = 1.33'
    '            DamageType  = ~/EDamageType/Suppress'
    '        ),'
    '    ]'
    ')'
)
