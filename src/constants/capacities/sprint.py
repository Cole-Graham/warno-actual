SPRINT_CAPACITY = (
    'export Capacite_Sprint is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{76a483af-5f44-4ad2-a4c2-8caef5e5f828}'
    '    Name             = "Sprint"'
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_ennemi'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 875'
    '    CastTime            = 0.00'
    '    CheckVisibility     = False'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = nil'
    '    SelfEffect           = ~/UnitEffect_Sprint'
    '    CapacityDuration   = -1.00'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = ["AllUnits"]'
    '    ForbiddenTargetTags = []'
    '    Conditions = ['
    '        ~/ConditionInMovement,'
    '        ~/ConditionTagNotRaisedInUnit_NoSprint_Morale,'
    '    ]'
    ')'
)

# UnitEffect_NoSprint_Morale: Unit_packStun value 0 (clears at 0.01+ stun); GroundUnits_packSupp 0.6/0.75/0.8

SPRINT_CONDITIONS = [
    (
        'ConditionTagRaisedInUnit_NoSprint_Morale is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{5f57fe1c-240e-4a9e-8844-0ab1d84a4836}'
        '    Tag             = "NoSprint_Morale"'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_NoSprint_Morale is TConditionNot'
        '('
        '    ConditionToInverse = ConditionTagRaisedInUnit_NoSprint_Morale'
        '    DescriptorId    = GUID:{6112f303-03b6-4993-b047-7cb4f9ddd8d1}'
        ')'
    ),
]
