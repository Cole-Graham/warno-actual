"""Swift capacity descriptors and tag conditions."""

SWIFT_CONDITIONS = [
    # no_swift_1
    (
        'ConditionTagRaisedInUnit_no_swift_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{ef2c4bdd-b1b1-4323-877d-be23d0e2f14a}'
        '    Tag             = "no_Swift"'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_no_swift_1 is TConditionNot'
        '('
        '    ConditionToInverse = ConditionTagRaisedInUnit_no_swift_1'
        '    DescriptorId    = GUID:{d7af0230-ed77-4499-870e-ef4da99b42e7}'
        ')'
    ),
    # swift_ok_1
    (
        'ConditionTagRaisedInUnit_swift_ok_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{93c106c4-6147-4927-aaab-a58496cfdec9}'
        '    Tag             = "Swift_ok"'
        ')'
    ),
]

SWIFT_CAPACITY = (
    'export Capacite_Swift is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{ab45713f-c4b5-42a5-8396-c8668894aafb}'
    '    Name             = "Swift"'
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 2.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = ~/UnitEffect_Swift'
    '    EffectDuration         = -1.00'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = False'
    '    TargetInSelf           = False'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = []'
    '    ForbiddenTargetTags = []'
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
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 0.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = True'
    '    TargetEffect       = ~/UnitEffect_Ajoute_Tag_no_Swift'
    '    EffectDuration       = -1.00'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = False'
    '    TargetInSelf           = False'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = []'
    '    ForbiddenTargetTags = []'
    '    Conditions = ['
    '        ~/ConditionNotInMovement,'
    '    ]'
    ')'
)
