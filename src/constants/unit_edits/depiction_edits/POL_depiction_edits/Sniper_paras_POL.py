"""Sniper_paras_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
sniper_paras_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Sniper_paras_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("TacticDepiction_Sniper_paras_POL_Alternatives", None): (
            f'[\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "01"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Sniper_paras_POL\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "02"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Sniper_paras_POL_02\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "03"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Sniper_paras_POL_02\n'
            f'    ),'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_Sniper_paras_POL\n'
            f'    )\n'
            f']'
        ),
        
        ("TacticDepiction_Sniper_paras_POL_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "02_03",
        },
        
        ("TacticDepiction_Sniper_paras_POL_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "02_03",
        },
        
        (None, "TTransportedInfantryEntry"): {
            "Count": 3,
            "Meshes": [
                "Sniper_paras_POL",
                "Sniper_paras_POL_02",
                "Sniper_paras_POL_02",
            ],
            "UniqueCount": 2,
        },
    }
}
# fmt: on
