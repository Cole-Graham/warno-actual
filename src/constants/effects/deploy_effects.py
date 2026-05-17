"""Deploy capacity-related unit effects."""

DEPLOY_OK_EFFECT = (
    'export UnitEffect_Ajoute_Tag_Deploy_ok is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{82ff2eb0-c219-44ce-bb81-8bdb09930966}'
    "    NameForDebug       = 'Ajoute_Tag_Deploy_ok'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["Deploy_ok"]'
    '        )'
    '    ]'
    ')'
)

DEPLOY_EFFECT = (
    'export UnitEffect_Deploy is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{be1fc256-a6db-487e-9803-b63a223c1ead}'
    "    NameForDebug       = 'Deploy'"
    '    EffectsDescriptors = ['
    '        TBonusWeaponAimtimeEffectDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    '            ModifierValue = 15'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_deploy"'
    '        ),'
    '    ]'
    ')'
)
