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
    '    EffectDuration   = 15.00'
    '    TargetInBuilding       = False'
    '    TargetInTransport      = False'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = ["AllUnits"]'
    '    ForbiddenTargetTags = []'
    '    Conditions = ['
    '        ~/ConditionTagNotRaisedInUnit_NoSprint,'
    '        ~/ConditionTagNotRaisedInUnit_NoSprint_Morale,'
    '    ]'
    ')'
)

SPRINT_ACTIVATED_CAPACITY = (
    'export Capacite_Sprint_Activated is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{4763a820-0c66-4aff-a5c8-bceb9a992b5a}'
    '    Name             = "Sprint_Activated"'
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 1'
    '    CastTime            = 0.00'
    '    CheckVisibility     = False'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = nil'
    '    SelfEffect       = ~/UnitEffect_Sprint_Activated'
    '    EffectDuration   = 45.00'
    '    TargetInBuilding       = False'
    '    TargetInTransport      = False'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = []'
    '    ForbiddenTargetTags = []'
    '    Conditions = ['
    '        ~/ConditionTagNotRaisedInUnit_NoSprint,'
    '        ~/ConditionTagNotRaisedInUnit_NoSprint_Morale,'
    '    ]'
    ')'
)

SPRINT_BEGIN_COOLDOWN_CAPACITY = (
    'export Capacite_Sprint_BeginCooldown is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{2e4a3e85-7747-4dea-8a55-24ee4a9683a0}'
    '    Name             = "SprintBeginCooldown"'
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 1'
    '    CastTime            = 15.00'
    '    CheckVisibility     = False'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = nil'
    '    SelfEffect       = ~/UnitEffect_NoSprint'
    '    EffectDuration   = 30.00'
    '    TargetInBuilding       = True'
    '    TargetInTransport      = True'
    '    TargetInSelf           = True'
    '    TargetMySelf           = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor      = RGBA[0,0,0,0]'
    '    DisplayRangeThickness  = 0.00'
    '    AllowedTargetTags = ['
    '        "GroundUnits",'
    '    ]'
    '    ForbiddenTargetTags = []'
    '    Conditions = ['
    # '        ~/ConditionTagRaisedInUnit_choc_move_ok_1,'
    '        ~/ConditionTagRaisedInUnit_SprintActivated,'
    '    ]'
    ')'
)

NO_SPRINT_CAPACITY = (
    'export Capacite_NoSprint is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{d9387c72-50d7-4781-929b-f3d08c3ea241}'
    '    Name             = "NoSprint"'
    '    StackPolicy          = ~/CapacityStackPolicy_never'
    '    Trigger        = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 0.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = True'
    '    TargetEffect         = ~/UnitEffect_NoSprint'
    '    EffectDuration   = -1.00'
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
    '        ~/ConditionNotInMovement,'
    '    ]'
    ')'
)

# UnitEffect_NoSprint_Morale is activated by DamageLevels (see DamageLevels.py)

SPRINT_OK_CAPACITY = ( # Not used currently
    'export Capacite_Sprint_ok is TCapaciteDescriptor'
    '('
    '    DescriptorId = GUID:{28b2ef52-3484-4820-b0e1-2103683706b2}'
    '    Name = "Sprint_ok"'
    '    StackPolicy = ~/CapacityStackPolicy_never'
    '    Trigger = ~/CapacityTriggerType_automatic'
    '    TargetTeamFilter = ~/CapaciteTargetFilter_ennemi'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU = 875'
    '    CastTime = 0.0'
    '    CheckVisibility = False'
    '    CanBeCastFromTransport = False'
    '    TargetEffect = nil'
    '    SelfEffect = ~/UnitEffect_Sprint_ok'
    '    EffectDuration = -1.00'
    '    TargetInBuilding = True'
    '    TargetInTransport = True'
    '    TargetInSelf = True'
    '    TargetMySelf = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never | ~/CapaciteFeedbackActivationMask_anyalliance'
    '    DisplayRangeColor = RGBA[0, 0, 0, 0]'
    '    DisplayRangeThickness = 0.00'
    '    AllowedTargetTags = []'
    '    ForbiddenTargetTags = []'
    ')'
)

SPRINT_CONDITIONS = [
    # NoSprint
    (
        'ConditionTagRaisedInUnit_NoSprint is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{c019e340-3b66-4128-a428-61f8a4941097}'
        '    Tag             = "NoSprint"'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_NoSprint is TConditionNot'
        '('
        '    ConditionToInverse = ConditionTagRaisedInUnit_NoSprint'
        '    DescriptorId    = GUID:{d7157b12-61e5-4090-809d-c2f54739ed8b}'
        ')'
    ),
    
    # NoSprint_Morale
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
    
    # Sprint_ok
    (
        'ConditionTagRaisedInUnit_Sprint_ok is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{6ef8cc00-c4c8-46a6-b8b4-4cac97dfeac8}'
        '    Tag             = "Sprint_ok"'
        ')'
    ),
    
    # SprintActivated
    (
        'ConditionTagRaisedInUnit_SprintActivated is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{37691a2f-3922-4ddb-bba8-ca8a167e675c}'
        '    Tag             = "SprintActivated"'
        ')'
    ),
]

# Capacite_Sprint is TCapaciteDescriptor
# {
#     CastTime = 0.00
#     EffectDuration = 15.00
#     SelfEffect = ~/UnitEffect_Choc_Sprint (sprint movement buff for infantry)
#     Conditions = [~/ConditionTagNotRaisedInUnit_NoSprint]
# }

# Capacite_Sprint_Activated is TCapaciteDescriptor
# {
#     CastTime = 0.00
#     EffectDuration = 60.00
#     SelfEffect = ~/UnitEffect_Sprint_Active (raises "SprintActivated" tag)
#     Conditions = [~/ConditionTagNotRaisedInUnit_NoSprint]
# } 

# Capacite_Sprint_BeginCooldown is TCapaciteDescriptor
# {
#      CastTime = 15.00
#      EffectDuration = 45.00
#      SelfEffect = ~/UnitEffect_SprintBeginCooldown (raises "SprintBeginCooldown" tag)
#      Conditions = [~/ConditionTagRaisedInUnit_SprintActivated]
# }

# Capacite_Sprint_Cooldown is TCapaciteDescriptor
# {
#     CastTime = 0.00
#     EffectDuration = 45.00
#     SelfEffect = ~/UnitEffect_Choc_No_Sprint (raises "NoSprint" tag to block sprint ability for 45 seconds)
#     Conditions = [~ConditionTagRaisedInUnit_SprintBeginCoolDown]
# }   