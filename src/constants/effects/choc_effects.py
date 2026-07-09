"""Choc (CQC) capacity-related unit effects."""

CHOC_INRANGE_TAG_EFFECT = (
    'export UnitEffect_Ajoute_Tag_choc_inrange is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{dad475cc-e650-44a7-8d0a-c02d63bda5ad}'
    "    NameForDebug       = 'Ajoute_Tag_choc_inrange'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["choc_inrange"]'
    '        )'
    '    ]'
    ')'
)

CHOC_INRANGE_FEEDBACK_EFFECT = (
    'export UnitEffect_Choc_inrange is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{807f1659-979b-4b18-bf80-f5fe7cb474ce}'
    "    NameForDebug       = 'Choc_inrange'"
    '    EffectsDescriptors = ['
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_shock_inrange"'
    '        )'
    '    ]'
    ')'
)
