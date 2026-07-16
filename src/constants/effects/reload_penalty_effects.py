"""Moving salvo reload penalty unit effect."""

RELOAD_PENALTY_SALVO_MULTIPLIER = 1.15

RELOAD_PENALTY_EFFECT = (
    'export UnitEffect_Reload_Penalty is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{4ecff57e-de01-4cc4-9622-16e53de6f3eb}'
    "    NameForDebug       = 'Reload_Penalty'"
    '    EffectsDescriptors = ['
    '        TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    f'            ModifierValue = {RELOAD_PENALTY_SALVO_MULTIPLIER}'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_reload_penalty"'
    '        ),'
    '    ]'
    ')'
)
