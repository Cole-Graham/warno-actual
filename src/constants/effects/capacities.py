"""Effect and capacity constants."""

# Effect definitions
NO_CHOC_MOVE_EFFECT = (
    'export UnitEffect_Ajoute_Tag_no_Choc_Move is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{bf1daa2b-1708-4702-80ff-4c7dfd76c2d7}'
    "    NameForDebug       = 'Ajoute_Tag_no_Choc_Move'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["no_Choc_Move"]'
    '        )'
    '    ]'
    ')'
)

NO_CHOC_MOVE_MORALE_EFFECT = (
    'export UnitEffect_Ajoute_Tag_no_Choc_Move_Morale is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{d44b363a-f062-4d38-b16d-b6f78bde17c9}'
    "    NameForDebug       = 'Ajoute_Tag_no_Choc_Move_Morale'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["no_Choc_Move_Morale"]'
    '        )'
    '    ]'
    ')'
)

CHOC_MOVE_OK_EFFECT = (
    'export UnitEffect_Ajoute_Tag_Choc_Move_ok is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{1748af97-f02d-4f04-8367-a5fb43f93f7c}'
    "    NameForDebug       = 'Ajoute_Tag_Choc_Move_ok'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["Choc_Move_ok"]'
    '        )'
    '    ]'
    ')'
)

CHOC_MOVE_EFFECT = (
    'export UnitEffect_Choc_Move is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{c3dbf0eb-c573-47b6-ba19-2d17ad3f9f24}'
    "    NameForDebug       = 'Choc_Move'"
    '    EffectsDescriptors = ['
    '        TUnitEffectIncreaseDamageTakenDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    '            BonusDamage = 0'
    '            DamageType  = EDamageType/Suppress'
    '        ),'
    '        TEffectInflictSuppressDamageDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Additionnel'
    '            SuppressDamageValue = 40'
    '        ),'
    '        TUnitEffectIncreaseDamageTakenDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Pourcentage'
    '            BonusDamage = -20'
    '            DamageType  = EDamageType/Physical'
    '        ),'
    '        TUnitEffectIncreaseSpeedDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    '            BonusSpeedBaseInPercent   = 2.0'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_shock_move"'
    '        ),'
    '    ]'
    ')'
)

CHOC_MOVE_GSR_EFFECT = (
    'export UnitEffect_Choc_Move_GSR is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{177c48af-2b7d-4d09-bae7-4d2d2628f946}'
    "    NameForDebug       = 'Choc_move_GSR'"
    '    EffectsDescriptors = ['
    '        TUnitEffectIncreaseSpeedDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    '            BonusSpeedBaseInPercent   = 1.50'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_shock_move"'
    '        )'
    '    ]'
    ')'
)

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
    '            ModifierType = ~/ModifierType_Multiplicatif'
    '            BonusSpeedBaseInPercent   = 1.50'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_swift"'
    '        )'
    '    ]'
    ')'
)

NO_CHOC_MOVE_CAPACITY = (
    'export Capacite_no_Choc_Move is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{d9387c72-50d7-4781-929b-f3d08c3ea241}'
    '    Name             = "no_Choc_Move"'
    '    NameToken        = "None"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TypeCible            = ~/CapaciteTypeCible_soi'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    TargetWoundedFilter  = ~/CapaciteWoundedFilterType_tout'
    '    AreaShape            = ~/CapaciteTypeCible_soi'
    '    RadiusGRU           = 1'
    '    RangeGRU            = 1'
    '    CastTime            = 0.00'
    '    Cooldown            = 0.00'
    '    CheckVisibility     = True'
    '    AllowReflexDuringCast   = True'
    '    CanBeCastFromTransport  = True'
    '    TargetEffect         = nil'
    '    TargetEffectDuration = 0.00'
    '    SelfEffect         = ~/UnitEffect_Ajoute_Tag_no_Choc_Move'
    '    SelfEffectDuration   = -1.00'
    '    MaxTargetNb            = 1'
    '    MultiplyCost           = False'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    Price = MAP[]'
    '    TagsCiblePossible = ['
    '    ]'
    '    Conditions = ['
    '        ~/ConditionNotInMovement,'
    '    ]'
    ')'
)

CHOC_MOVE_CAPACITY = (
    'export Capacite_Choc_Move is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{76a483af-5f44-4ad2-a4c2-8caef5e5f828}'
    '    Name             = "Choc_Move"'
    '    NameToken        = "None"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TypeCible            = ~/CapaciteTypeCible_soi'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    TargetWoundedFilter  = ~/CapaciteWoundedFilterType_tout'
    '    AreaShape            = ~/CapaciteAreaShape_soi'
    '    RadiusGRU           = 1'
    '    RangeGRU            = 1'
    '    CastTime            = 1.00'
    '    Cooldown            = 30.00'
    '    CheckVisibility     = False'
    '    AllowReflexDuringCast   = True'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = nil'
    '    TargetEffectDuration = -1.00'
    '    SelfEffect       = ~/UnitEffect_Choc_Move'
    '    SelfEffectDuration   = 100.00'
    '    MaxTargetNb            = -1'
    '    MultiplyCost           = False'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    Price = MAP[]'
    '    TagsCiblePossible = ['
    '        "GroundUnits",'
    '    ]'
    '    TagsCibleExcluded = []'
    '    Conditions = ['
    # '        ~/ConditionTagRaisedInUnit_choc_move_ok_1,'
    '        ~/ConditionTagNotRaisedInUnit_no_choc_move_1,'
    '        ~/ConditionTagNotRaisedInUnit_no_choc_move_morale_1,'
    '    ]'
    ')'
)

CHOC_MOVE_GSR_CAPACITY = (
    'export Capacite_Choc_move_GSR is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{0b012c07-67cd-4691-9fc2-9b388e9eae25}'
    '    Name             = "Choc_move_GSR"'
    '    NameToken        = "None"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TypeCible            = ~/CapaciteTypeCible_unite'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_ennemi'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    TargetWoundedFilter  = ~/CapaciteWoundedFilterType_tout'
    '    AreaShape            = ~/CapaciteAreaShape_circulaire'
    '    RadiusGRU           = 875'
    '    RangeGRU            = 875'
    '    CastTime            = 1.00'
    '    Cooldown            = 30.00'
    '    CheckVisibility     = False'
    '    AllowReflexDuringCast   = True'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = nil'
    '    TargetEffectDuration = -1.00'
    '    SelfEffect       = ~/UnitEffect_Choc_Move_GSR'
    '    SelfEffectDuration   = 100.00'
    '    MaxTargetNb            = -1'
    '    MultiplyCost           = False'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    Price = MAP[]'
    '    TagsCiblePossible = ['
    '        "GroundUnits",'
    '    ]'
    '    TagsCibleExcluded = []'
    '    Conditions = ['
    '        ~/ConditionTagNotRaisedInUnit_Panique_1,'
    '        ~/ConditionTagRaisedInUnit_GroundUnit_Engaged_1'
    '    ]'
    ')'
)

SWIFT_CAPACITY = (
    'export Capacite_Swift is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{ab45713f-c4b5-42a5-8396-c8668894aafb}'
    '    Name             = "Swift"'
    '    NameToken        = "None"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TypeCible            = ~/CapaciteTypeCible_soi'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    TargetWoundedFilter  = ~/CapaciteWoundedFilterType_tout'
    '    AreaShape            = ~/CapaciteAreaShape_soi'
    '    RadiusGRU           = 1'
    '    RangeGRU            = 1'
    '    CastTime            = 2.00'
    '    Cooldown            = 0.00'
    '    CheckVisibility     = False'
    '    AllowReflexDuringCast   = True'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = ~/UnitEffect_Swift'
    '    TargetEffectDuration = -1.00'
    '    SelfEffectDuration   = 0.00'
    '    MaxTargetNb            = -1'
    '    MultiplyCost           = False'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    Price = MAP[]'
    '    TagsCiblePossible = ['
    '        "GroundUnits",'
    '    ]'
    '    TagsCibleExcluded = ['
    '    ]'
    '    Conditions = ['
    '        ~/ConditionTagNotRaisedInUnit_no_swift_1,'
    '        ~/ConditionTagRaisedInUnit_swift_ok_1,'
    '    ]'
    ')'
)

NO_SWIFT_CAPACITY = (
    'export Capacite_no_Swift is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{546d38fd-a25d-4d03-aa10-7e74b1de0645}'
    '    Name             = "no_Swift"'
    '    NameToken        = "None"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TypeCible            = ~/CapaciteTypeCible_unite'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    TargetWoundedFilter  = ~/CapaciteWoundedFilterType_tout'
    '    AreaShape            = ~/CapaciteAreaShape_soi'
    '    RadiusGRU           = 1'
    '    RangeGRU            = 1'
    '    CastTime            = 0.00'
    '    Cooldown            = 0.00'
    '    CheckVisibility     = False'
    '    AllowReflexDuringCast   = True'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = nil'
    '    TargetEffectDuration = -1.00'
    '    SelfEffect       = ~/UnitEffect_Ajoute_Tag_no_Swift'
    '    SelfEffectDuration   = -1.00'
    '    MaxTargetNb            = -1'
    '    MultiplyCost           = False'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    Price = MAP[]'
    '    TagsCiblePossible = ['
    '    ]'
    '    TagsCibleExcluded = ['
    '    ]'
    '    Conditions = ['
    '        ~/ConditionNotInMovement,'
    '    ]'
    ')'
)

CONDITIONS = [
    (
        'ConditionTagNotRaisedInUnit_no_choc_move_1 is TConditionTagNotRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{d7157b12-61e5-4090-809d-c2f54739ed8b}'
        '    Tag             = "no_Choc_Move"'
        '    Amount          = 1'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_no_choc_move_morale_1 is TConditionTagNotRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{6112f303-03b6-4993-b047-7cb4f9ddd8d1}'
        '    Tag             = "no_Choc_Move_Morale"'
        '    Amount          = 1'
        ')'
    ),
    (
        'ConditionTagRaisedInUnit_choc_move_ok_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{6ef8cc00-c4c8-46a6-b8b4-4cac97dfeac8}'
        '    Tag             = "Choc_Move_ok"'
        '    Amount          = 1'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_no_swift_1 is TConditionTagNotRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{d7af0230-ed77-4499-870e-ef4da99b42e7}'
        '    Tag             = "no_Swift"'
        '    Amount          = 1'
        ')'
    ),
    (
        'ConditionTagRaisedInUnit_swift_ok_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{93c106c4-6147-4927-aaab-a58496cfdec9}'
        '    Tag             = "Swift_ok"'
        '    Amount          = 1'
        ')'
    ),
]
