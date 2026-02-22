"""Engineers_Scout_Para_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
engineers_scout_para_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Engineers_Scout_Para_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {       
        ("TacticDepiction_Engineers_Scout_Para_POL_Alternatives", None): (
            f'[\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "01"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_paras_POL\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "02"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_paras_POL_02\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "03"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_paras_POL_03\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "04"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_paras_POL_04\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_Low]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_paras_POL_LOW\n'
            f'    ),\n'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_Engineers_paras_POL\n'
            f'    )\n'
            f']'
        ),
        
        (None, "TTransportedInfantryEntry"): {
            "Meshes": [
                "Engineers_paras_POL",
                "Engineers_paras_POL_02",
                "Engineers_paras_POL_03",
                "Engineers_paras_POL_04",
            ],
        }
    },
}
# fmt: on
