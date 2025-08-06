"""Templates for adding weapons to turrets."""

# fmt: off
mounted_weapons = {
    "AutoCanon_AP_T20_20mm": ("""
        TMountedWeaponDescriptor
        (
            Ammunition                          = $/GFX/Weapon/Ammo_AutoCanon_AP_T20_20mm
            AnimateOnlyOneSoldier               = False
            DispersionRadiusOffColor            = RGBA[0,0,0,0]
            DispersionRadiusOffThickness        = -0.1
            DispersionRadiusOnColor             = RGBA[0,0,0,0]
            DispersionRadiusOnThickness         = -0.1
            EffectTag                           = 'FireEffect_AutoCanon_AP_M693_F1_20mm'
            HandheldEquipmentKey                = 'MeshAlternative_1'
            NbWeapons                           = 1
            SalvoStockIndex                     = 0
            ShowDispersion                      = False
            WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_1'
            WeaponIgnoredPropertyName           = 'WeaponIgnored_1'
            WeaponShootDataPropertyName         = ['WeaponShootData_0_1']
        )"""
    ),
    "AutoCanon_HE_T20_20mm": ("""
        TMountedWeaponDescriptor
        (
            Ammunition                          = $/GFX/Weapon/Ammo_AutoCanon_HE_T20_20mm
            AnimateOnlyOneSoldier               = False
            DispersionRadiusOffColor            = RGBA[0,0,0,0]
            DispersionRadiusOffThickness        = -0.1
            DispersionRadiusOnColor             = RGBA[0,0,0,0]
            DispersionRadiusOnThickness         = -0.1
            EffectTag                           = 'FireEffect_AutoCanon_HE_M693_F1_20mm'
            HandheldEquipmentKey                = 'MeshAlternative_2'
            NbWeapons                           = 1
            SalvoStockIndex                     = 0
            ShowDispersion                      = False
            WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_2'
            WeaponIgnoredPropertyName           = 'WeaponIgnored_2'
            WeaponShootDataPropertyName         = ['WeaponShootData_0_2']
        )"""
    ),
}
# fmt: on
