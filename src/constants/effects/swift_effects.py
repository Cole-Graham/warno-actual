"""Swift-related unit effect descriptors."""

NO_SWIFT_EFFECT = (
    'export UnitEffect_Ajoute_Tag_no_Swift is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{b6297278-9491-43a5-b56f-e22cd3bff976}'
    "    NameForDebug       = 'Ajoute_Tag_no_Swift'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["no_Swift"]'
    '        )'
    '    ]'
    ')'
)

SWIFT_OK_EFFECT = (
    'export UnitEffect_Ajoute_Tag_Swift_ok is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{03e612af-f96d-48a8-898e-d344b1f949fa}'
    "    NameForDebug       = 'Ajoute_Tag_Swift_ok'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["Swift_ok"]'
    '        )'
    '    ]'
    ')'
)

SWIFT_EFFECT = (
    'export UnitEffect_Swift is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{a51d1463-efcc-40d8-b497-ea2eb44c06cf}'
    "    NameForDebug       = 'Swift'"
    '    EffectsDescriptors = ['
    '        TUnitEffectIncreaseSpeedDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Pourcentage'
    '            BonusSpeedBaseInPercent   = 50'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_swift"'
    '        )'
    '    ]'
    ')'
)
