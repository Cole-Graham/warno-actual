"""Naval_Engineers_CMD_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
naval_engineers_cmd_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Naval_Engineers_CMD_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("TacticDepiction_Naval_Engineers_CMD_POL_Alternatives", None): (
            f'[\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "01"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Naval_Engineers_CMD_POL\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "02"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Naval_Engineers_CMD_POL_02\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "03"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Naval_Engineers_CMD_POL_02\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "04"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Naval_Engineers_CMD_POL\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "05"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Naval_Engineers_CMD_POL_02\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "06"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Naval_Engineers_CMD_POL_03\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_Low]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Naval_Engineers_CMD_POL_LOW\n'
            f'    ),'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_Naval_Engineers_CMD_POL\n'
            f'    )\n'
            f']'
        ),
        
        ("TacticDepiction_Naval_Engineers_CMD_POL_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "03_06",
        },
        
        ("TacticDepiction_Naval_Engineers_CMD_POL_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "03_06",
        },
        
        (None, "TTransportedInfantryEntry"): {
            "Count": 6,
            "Meshes": [
                "Naval_Engineers_CMD_POL",
                "Naval_Engineers_CMD_POL_02",
                "Naval_Engineers_CMD_POL_03",
                "Naval_Engineers_CMD_POL",
                "Naval_Engineers_CMD_POL_02",
                "Naval_Engineers_CMD_POL_03",
            ],
            "UniqueCount": 3,
        },
    }
}
# fmt: on
