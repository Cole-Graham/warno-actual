"""Choc (CQC) capacity descriptors and tag conditions."""

from src.constants import CQC_RANGE

CHOC_CONDITIONS = [
    (
        'ConditionTagRaisedInUnit_choc_inrange_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{54cac133-a2a0-44a5-becf-259d5fbbd5b7}'
        '    Tag             = "choc_inrange"'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_choc_inrange_1 is TConditionNot'
        '('
        '    ConditionToInverse = ConditionTagRaisedInUnit_choc_inrange_1'
        '    DescriptorId    = GUID:{f8abe140-1f80-4710-adc6-fced87b39041}'
        ')'
    ),
]

CHOC_INRANGE_CAPACITY = (
    'export Capacite_Choc_inrange is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{0de840a7-2689-4d97-86a0-4e4051546008}'
    '    Name             = "Choc_inrange"'
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_ennemi'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    f'    RangeGRU            = {CQC_RANGE}'
    '    CastTime            = 0.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = True'
    '    TargetEffect         = nil'
    '    SelfEffect           = ~/UnitEffect_Ajoute_Tag_choc_inrange'
    '    CapacityDuration       = -1.00'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = ["GroundUnits"]'
    '    ForbiddenTargetTags = []'
    ')'
)

CHOC_INRANGE_FEEDBACK_CAPACITY = (
    'export Capacite_Choc_inrange_feedback is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{ed4da52a-032e-47c0-8346-5aec07c42c2f}'
    '    Name             = "Choc_inrange_feedback"'
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 0.00'
    '    CheckVisibility     = False'
    '    CanBeCastFromTransport  = True'
    '    TargetEffect         = ~/UnitEffect_Choc_inrange'
    '    CapacityDuration       = -1.00'
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
    '        ~/ConditionTagRaisedInUnit_choc_inrange_1,'
    '        ~/ConditionTagNotRaisedInUnit_choc_ok,'
    '        ~/ConditionInMovement,'
    '    ]'
    ')'
)
