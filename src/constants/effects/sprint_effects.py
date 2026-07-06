"""Sprint effect constants."""

CHOC_SPRINT_BONUSES = {
    "suppress_damage_multiplier": 0.50,
    "speed_bonus_percentage": 70,
}

SPRINT_EFFECT = (
    'export UnitEffect_Sprint is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{c3dbf0eb-c573-47b6-ba19-2d17ad3f9f24}'
    '    NameForDebug       = "Sprint"'
    '    EffectsDescriptors = ['
    '        TUnitEffectIncreaseDamageTakenDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    f'            BonusDamage = {1 - CHOC_SPRINT_BONUSES["suppress_damage_multiplier"]}'
    '            DamageType  = ~/EDamageType/Suppress'
    '        ),'
    '        TEffectInflictDamageDescriptor'
    '        ('
    '            DamageType = ~/EDamageType/Suppress'
    '            ModifierType = ~/ModifierType_Additionnel'
    '            DamageValue = 20' # Buffer to prevent suppression regeneration from instantly cancelling the effect
    '        ),'
    '        TUnitEffectIncreaseSpeedDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Pourcentage'
    f'            BonusSpeedBaseInPercent   = {CHOC_SPRINT_BONUSES["speed_bonus_percentage"]}'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_shock_move"'
    '        ),'
    '    ]'
    ')'
)

NO_SPRINT_MORALE_EFFECT = (
    'export UnitEffect_NoSprint_Morale is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{d44b363a-f062-4d38-b16d-b6f78bde17c9}'
    '    NameForDebug       = "NoSprint_Morale"'
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["NoSprint_Morale"]'
    '        )'
    '    ]'
    ')'
)
