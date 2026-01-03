"""Airborne_Engineers_Flash_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
airborne_engineers_flash_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Airborne_Engineers_Flash_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Airborne_Engineers_Flash_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("edit", [("MeshDescriptor", "M249")]), # (selector_id or mesh)
        },

        ("AllWeaponSubDepiction_Airborne_Engineers_Flash_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "SAW_M249_5_56mm")]),
            },
        },
        
        ("TacticDepiction_Airborne_Engineers_Flash_US_Alternatives", None):
            """[
    TDepictionVisual
    (
        SelectorId = [LOD_High, '01']
        MeshDescriptor = $/GFX/DepictionResources/Modele_Airborne_Engineers_Flash_US
    ),
    TDepictionVisual
    (
        SelectorId = [LOD_High, '02']
        MeshDescriptor = $/GFX/DepictionResources/Modele_Airborne_Engineers_Flash_US_02
    ),
    TDepictionVisual
    (
        SelectorId = [LOD_High, '03']
        MeshDescriptor = $/GFX/DepictionResources/Modele_Airborne_Engineers_Flash_US_03
    ),
    TDepictionVisual
    (
        SelectorId = [LOD_High, '04']
        MeshDescriptor = $/GFX/DepictionResources/Modele_Airborne_Engineers_Flash_US_04
    ),
    TDepictionVisual
    (
        SelectorId = [LOD_High, '05']
        MeshDescriptor = $/GFX/DepictionResources/Modele_Airborne_Engineers_Flash_US_05
    ),
    TDepictionVisual
    (
        SelectorId = [LOD_High, '06']
        MeshDescriptor = $/GFX/DepictionResources/Modele_Airborne_Engineers_Flash_US_06
    ),
    TDepictionVisual
    (
        SelectorId = [LOD_Low]
        MeshDescriptor = $/GFX/DepictionResources/Modele_Airborne_Engineers_Flash_US_LOW
    ),
    TMeshlessDepictionDescriptor
    (
        SelectorId = ['none']
        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_Airborne_Engineers_Flash_US
    )
]""",

        ("TacticDepiction_Airborne_Engineers_Flash_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "04_06"
        },
        
        ("TacticDepiction_Airborne_Engineers_Flash_US_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "04_06"
        },
        
        (None, "TTransportedInfantryEntry"): {
            "Count": 6,
            "Meshes": [
                "Airborne_Engineers_Flash_US",
                "Airborne_Engineers_Flash_US_02",
                "Airborne_Engineers_Flash_US_03",
                "Airborne_Engineers_Flash_US_04",
                "Airborne_Engineers_Flash_US_05",
                "Airborne_Engineers_Flash_US_06",
            ],
            "UniqueCount": 4,
        },
    }
}
# fmt: on
