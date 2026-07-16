from typing import Any, Dict

# fmt: off
tunguska_2k22_ddr: Dict[str, Any] = {
    "unit_name": "Tunguska_2K22_DDR",
    "valid_files": ["MissileCarriage.ndf"],
    "DepictionVehicles_ndf": {
        # Auto-cloned Weapon2 still points at the SOV carriage; rebind to this unit's.
        ("DepictionOperator_Tunguska_2K22_DDR_Weapon2", "DepictionOperator_WeaponMissileCarriageFire"): {
            "Connoisseur": "MissileCarriage_Tunguska_2K22_DDR",
        },
    },
    "MissileCarriage_ndf": {
        "carriage": """
            export MissileCarriage_Tunguska_2K22_DDR is TMissileCarriageConnoisseur
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_Tunguska_2K22_DDR
                PylonSet = ~/DepictionPylonSet_Vehicle_Default
                WeaponInfos =
                [
                    TMissileCarriageWeaponInfo
                    (
                        MissileCount = 8
                        MissileType = eAAM
                        WeaponIndex = 2
                    ),
                ]
            )""",
        "carriage_showroom": """
            export MissileCarriage_Tunguska_2K22_DDR_Showroom is TMissileCarriageConnoisseur
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_Tunguska_2K22_DDR
                PylonSet = ~/DepictionPylonSet_Vehicle_Default_Showroom
                WeaponInfos = ~/MissileCarriage_Tunguska_2K22_DDR.WeaponInfos
            )""",
    },
    "Tunguska_2K22_DDR_ndf": {
        "directory": "Char",
        "ndf_code": """
            export Modele_Tunguska_2K22_DDR is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/ddr/char/Tunguska_2K22/Tunguska_2K22/Tunguska.fbx"
            )

            export Modele_Tunguska_2K22_DDR_MID is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/ddr/char/Tunguska_2K22/Tunguska_2K22_MID/Tunguska.fbx"
            )

            export Modele_Tunguska_2K22_DDR_LOW is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/ddr/char/Tunguska_2K22/Tunguska_2K22_LOW/Tunguska.fbx"
            )""",
    },
}
# fmt: on
