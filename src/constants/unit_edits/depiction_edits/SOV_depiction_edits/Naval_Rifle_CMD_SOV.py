"""Naval_Rifle_CMD_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
naval_rifle_cmd_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Naval_Rifle_CMD_SOV",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("TacticDepiction_Naval_Rifle_CMD_SOV_Alternatives", None): (
            f'[\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "01"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_CMD_Naval_SOV\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "02"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_CMD_Naval_SOV_02\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "03"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_CMD_Naval_SOV_03\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "04"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_CMD_Naval_SOV_04\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "05"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_CMD_Naval_SOV_02\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "06"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_CMD_Naval_SOV_03\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "07"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_CMD_Naval_SOV_04\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_Low]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Engineers_CMD_Naval_SOV_LOW\n'
            f'    ),\n'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_Engineers_CMD_Naval_SOV\n'
            f'    )\n'
            f']'
        ),
    }
}
# fmt: on
