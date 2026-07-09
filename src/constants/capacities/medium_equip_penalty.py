"""Medium equip penalty capacities and tag conditions."""

from src.constants.effects.medium_equip_penalty_effects import (
    MEDIUM_EQUIP_PENALTY_CAPACITY_DURATION,
    MEDIUM_EQUIP_PENALTY_TICK_SECONDS,
)

MEDIUM_EQUIP_PENALTY_CONDITIONS = [
    (
        'ConditionTagRaisedInUnit_Medium_Equip_Penalty_floor_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{d5e6f7a8-b9c0-4123-e456-789abcdef104}'
        '    Tag             = "Medium_Equip_Penalty_floor"'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_Medium_Equip_Penalty_floor_1 is TConditionNot'
        '('
        '    ConditionToInverse = ConditionTagRaisedInUnit_Medium_Equip_Penalty_floor_1'
        '    DescriptorId    = GUID:{e6f7a8b9-c0d1-4234-f567-89abcdef0215}'
        ')'
    ),
]

MEDIUM_EQUIP_PENALTY_CAPACITY = (
    'export Capacite_Medium_Equip_Penalty is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{0536d4b4-7512-4519-ae59-46cf0aaef066}'
    '    Name             = "Medium_Equip_Penalty"'
    '    StackPolicy          = ~/CapacityStackPolicy_always'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    f'    CastTime            = {MEDIUM_EQUIP_PENALTY_TICK_SECONDS:.2f}'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = True'
    '    TargetEffect         = ~/UnitEffect_Medium_Equip_Penalty'
    f'    CapacityDuration   = {MEDIUM_EQUIP_PENALTY_CAPACITY_DURATION:.2f}'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = []'
    '    ForbiddenTargetTags = []'
    '    Conditions = ['
    '        ~/ConditionInMovement,'
    '        ~/ConditionTagNotRaisedInUnit_Medium_Equip_Penalty_floor_1,'
    '    ]'
    ')'
)

MEDIUM_EQUIP_PENALTY_SF_CAPACITY = (
    'export Capacite_Medium_Equip_Penalty_SF is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{a8b9c0d1-e2f3-4056-b678-901abcdef437}'
    '    Name             = "Medium_Equip_Penalty_SF"'
    '    StackPolicy          = ~/CapacityStackPolicy_always'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    f'    CastTime            = {MEDIUM_EQUIP_PENALTY_TICK_SECONDS:.2f}'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = True'
    '    TargetEffect         = ~/UnitEffect_Medium_Equip_Penalty_SF'
    f'    CapacityDuration   = {MEDIUM_EQUIP_PENALTY_CAPACITY_DURATION:.2f}'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = []'
    '    ForbiddenTargetTags = []'
    '    Conditions = ['
    '        ~/ConditionInMovement,'
    '        ~/ConditionTagNotRaisedInUnit_Medium_Equip_Penalty_floor_1,'
    '    ]'
    ')'
)
