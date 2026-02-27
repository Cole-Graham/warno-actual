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

CHOC_MOVE_COOLDOWN_EFFECT = (
    'export UnitEffect_Ajoute_Tag_Choc_Move_cooldown is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{27c08476-d0e0-48bc-8449-476e1873499b}'
    "    NameForDebug       = 'Ajoute_Tag_Choc_Move_cooldown'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["Choc_Move_cooldown"]'
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
    '            BonusDamage = 0.5'
    '            DamageType  = ~/EDamageType/Suppress'
    '        ),'
    '        TEffectInflictDamageDescriptor'
    '        ('
    '            DamageType = ~/EDamageType/Suppress'
    '            ModifierType = ~/ModifierType_Additionnel'
    '            DamageValue = 15' # Buffer to prevent suppression regeneration from instantly cancelling the effect
    '        ),'
    # '        TUnitEffectIncreaseDamageTakenDescriptor'
    # '        ('
    # '            ModifierType = ~/ModifierType_Pourcentage'
    # '            BonusDamage = -20'
    # '            DamageType  = ~/EDamageType/Physical'
    # '        ),'
    '        TUnitEffectIncreaseSpeedDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Pourcentage'
    '            BonusSpeedBaseInPercent   = 70'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_shock_move"'
    '        ),'
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

COHESION_LOSS_OK_EFFECT = (
    'export UnitEffect_Cohesion_Loss_ok is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{b72b0cca-de27-4284-b269-dfa441ee4e0d}'
    "    NameForDebug       = 'Cohesion_Loss_ok'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["Cohesion_Loss_ok"]'
    '        )'
    '    ]'
    ')'
)

MEDIUM_COHESION_LOSS_EFFECT = (
    'export UnitEffect_Medium_Cohesion_Loss is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{0ba81a5a-8c30-4501-91c6-b1b3df271393}'
    "    NameForDebug       = 'Med_Cohesion_Loss'"
    '    EffectsDescriptors = ['
    '        TUnitEffectIncreaseDamageTakenDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    '            BonusDamage = 1.33'
    '            DamageType  = ~/EDamageType/Suppress'
    '        ),'
    '    ]'
    ')'
)

MEDIUM_COHESION_LOSS_CAPACITY = (
    'export Capacite_Medium_Cohesion_Loss is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{0536d4b4-7512-4519-ae59-46cf0aaef066}'
    '    Name             = "Medium_Cohesion_Loss"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 5.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = True'
    '    TargetEffect         = ~/UnitEffect_Medium_Cohesion_Loss'
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
    '        ~/ConditionInMovement,'
    '    ]'
    ')'
)

NO_CHOC_MOVE_CAPACITY = (
    'export Capacite_no_Choc_Move is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{d9387c72-50d7-4781-929b-f3d08c3ea241}'
    '    Name             = "no_Choc_Move"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 0.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = True'
    '    TargetEffect         = ~/UnitEffect_Ajoute_Tag_no_Choc_Move'
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

CHOC_MOVE_OK_CAPACITY = (
    'export Capacite_Choc_Move_ok is TCapaciteDescriptor'
    '('
    '    DescriptorId = GUID:{28b2ef52-3484-4820-b0e1-2103683706b2}'
    '    Name = "Choc_Move_ok"'
    '    CumulEffect = ~/CapaciteCumulEffect_jamais'
    '    Declenchement = ~/CapaciteDeclenchementType_automatique'
    '    TargetTeamFilter = ~/CapaciteTargetFilter_ennemi'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU = 875'
    '    CastTime = 0.0'
    '    CheckVisibility = False'
    '    CanBeCastFromTransport = False'
    '    TargetEffect = nil'
    '    SelfEffect = ~/UnitEffect_Ajoute_Tag_Choc_Move_ok'
    '    EffectDuration = -1.00'
    '    TargetInBuilding = True'
    '    TargetInTransport = True'
    '    TargetInSelf = True'
    '    TargetMySelf = True'
    '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
    '    DisplayRangeColor = RGBA[0, 0, 0, 0]'
    '    DisplayRangeThickness = 0.00'
    '    AllowedTargetTags = []'
    '    ForbiddenTargetTags = []'
    ')'
)

# CHOC_MOVE_CAPACITY = (
#     'export Capacite_Choc_Move is TCapaciteDescriptor'
#     '('
#     '    DescriptorId     = GUID:{76a483af-5f44-4ad2-a4c2-8caef5e5f828}'
#     '    Name             = "Choc_Move"'
#     '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
#     '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
#     '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
#     '    InfluenceMapAlliance = ~/AllianceRelation/vide'
#     '    RangeGRU            = 0'
#     '    CastTime            = 1.00'
#     '    CheckVisibility     = False'
#     '    CanBeCastFromTransport  = False'
#     '    TargetEffect         = ~/UnitEffect_Choc_Move'
#     '    EffectDuration   = -1.00'
#     '    TargetInBuilding       = True'
#     '    TargetInTransport      = True'
#     '    TargetInSelf           = True'
#     '    TargetMySelf           = True'
#     '    FeedbackActivationMask = ~/CapaciteFeedbackActivationMask_never'
#     '    DisplayRangeColor      = RGBA[0,0,0,0]'
#     '    DisplayRangeThickness  = 0.00'
#     '    AllowedTargetTags = []'
#     '    ForbiddenTargetTags = []'
#     '    Conditions = ['
#     '        ~/ConditionTagRaisedInUnit_choc_move_ok_1,'
#     '        ~/ConditionTagNotRaisedInUnit_no_choc_move_1,'
#     '        ~/ConditionTagNotRaisedInUnit_no_choc_move_morale_1,'
#     # '        ~/ConditionTagNotRaisedInUnit_Choc_Move_cooldown,'
#     '    ]'
#     ')'
# )

CHOC_MOVE_CAPACITY = (
    'export Capacite_Choc_Move is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{76a483af-5f44-4ad2-a4c2-8caef5e5f828}'
    '    Name             = "Choc_Move"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_ennemi'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 875'
    '    CastTime            = 0.00'
    '    CheckVisibility     = False'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = nil'
    '    SelfEffect           = ~/UnitEffect_Choc_Move'
    '    EffectDuration   = -1.00'
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
    '        ~/ConditionTagNotRaisedInUnit_no_choc_move_1,'
    '        ~/ConditionTagNotRaisedInUnit_no_choc_move_morale_1,'
    # '        ~/ConditionTagNotRaisedInUnit_Choc_Move_cooldown,'
    '    ]'
    ')'
)

CHOC_MOVE_COOLDOWN_CAPACITY = (
    'export Capacite_Choc_Move_cooldown is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{2e4a3e85-7747-4dea-8a55-24ee4a9683a0}'
    '    Name             = "Choc_Move_cooldown"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 1'
    '    CastTime            = 1.00'
    '    CheckVisibility     = False'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = nil'
    '    SelfEffect       = ~/UnitEffect_Ajoute_Tag_Choc_Move_cooldown'
    '    EffectDuration   = 300.00'
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
    '        ~/ConditionTagRaisedInUnit_Choc_Move_active,'
    '    ]'
    ')'
)

SWIFT_CAPACITY = (
    'export Capacite_Swift is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{ab45713f-c4b5-42a5-8396-c8668894aafb}'
    '    Name             = "Swift"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
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
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
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

DEPLOY_CAPACITY = (
    'export Capacite_Deploy is TCapaciteDescriptor'
    '('
    '    DescriptorId     = GUID:{ad71a869-ab57-475a-96cb-c8f411ab3502}'
    '    Name             = "Deploy"'
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 3.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = ~/UnitEffect_Deploy'
    '    EffectDuration       = -1.00'
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
    '    CumulEffect          = ~/CapaciteCumulEffect_jamais'
    '    Declenchement        = ~/CapaciteDeclenchementType_automatique'
    '    TargetTeamFilter     = ~/CapaciteTargetFilter_joueur'
    '    InfluenceMapAlliance = ~/AllianceRelation/vide'
    '    RangeGRU            = 0'
    '    CastTime            = 15.00'
    '    CheckVisibility     = True'
    '    CanBeCastFromTransport  = False'
    '    TargetEffect         = ~/UnitEffect_Ajoute_Tag_Deploy_ok'
    '    EffectDuration       = -1.00'
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

CONDITIONS = [
    # no_choc_move_1
    (
        'ConditionTagRaisedInUnit_no_choc_move_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{c019e340-3b66-4128-a428-61f8a4941097}'
        '    Tag             = "no_Choc_Move"'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_no_choc_move_1 is TConditionNot'
        '('
        '    ConditionToInverse = ConditionTagRaisedInUnit_no_choc_move_1'
        '    DescriptorId    = GUID:{d7157b12-61e5-4090-809d-c2f54739ed8b}'
        ')'
    ),
    
    # no_choc_move_morale_1
    (
        'ConditionTagRaisedInUnit_no_choc_move_morale_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{5f57fe1c-240e-4a9e-8844-0ab1d84a4836}'
        '    Tag             = "no_Choc_Move_Morale"'
        ')'
    ),
    (
        'ConditionTagNotRaisedInUnit_no_choc_move_morale_1 is TConditionNot'
        '('
        '    ConditionToInverse = ConditionTagRaisedInUnit_no_choc_move_morale_1'
        '    DescriptorId    = GUID:{6112f303-03b6-4993-b047-7cb4f9ddd8d1}'
        ')'
    ),
    
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
    
    # choc_move_ok_1
    (
        'ConditionTagRaisedInUnit_choc_move_ok_1 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{6ef8cc00-c4c8-46a6-b8b4-4cac97dfeac8}'
        '    Tag             = "Choc_Move_ok"'
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
    
    # Choc_Move_active
    (
        'ConditionTagRaisedInUnit_Choc_Move_active is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{37691a2f-3922-4ddb-bba8-ca8a167e675c}'
        '    Tag             = "Choc_Move_active"'
        ')'
    ),
    
    # Cohesion_Higher_Than_80
    (
        'ConditionTagRaisedInUnit_Cohesion_Higher_Than_80 is TConditionTagRaisedInUnit'
        '('
        '    DescriptorId    = GUID:{74702d0d-af52-473a-90dc-ca8d53f86cb8}'
        '    Tag             = "Cohesion_Loss_ok"'
        ')'
    ),
]
