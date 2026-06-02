"""Deploy capacity descriptors and tag conditions."""

DEPLOY_CONDITIONS = [
    # Deploy_ok_1
    (
        'ConditionTagRaisedInUnit_Deploy_ok_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{69205aef-849d-44e7-9343-fbc6c570903d}'
        '    Tag             = "Deploy_ok"'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_Deploy_ok_1 is TConditionNot'
        '('
        '    ConditionToInverse = ConditionTagRaisedInUnit_Deploy_ok_1'
        '    DescriptorId    = GUID:{34e0d875-877a-40a8-860b-71bb0c18d3a9}'
        ')'
    ),
]

DEPLOY_CAPACITY = (
    'export Capacite_Deploy is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{ad71a869-ab57-475a-96cb-c8f411ab3502}'
    '    Name             = "Deploy"'
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 3.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = ~/UnitEffect_Deploy'
    '    CapacityDuration       = -1.00'
    '    TargetInBuilding       = False'
    '    TargetInTransport      = False'
    '    TargetInSelf           = False'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = []'
    '    ForbiddenTargetTags = []'
    '    Conditions = ['
    '        ~/ConditionTagNotRaisedInUnit_Deploy_ok_1,'
    '    ]'
    ')'
)

DEPLOY_OK_CAPACITY = (
    'export Capacite_Deploy_ok is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{312173e8-9fbe-4ca6-adc2-703e8c1f944a}'
    '    Name             = "Deploy_ok"'
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 15.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = ~/UnitEffect_Ajoute_Tag_Deploy_ok'
    '    CapacityDuration       = -1.00'
    '    TargetInBuilding       = False'
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
