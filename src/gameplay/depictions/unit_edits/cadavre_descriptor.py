from typing import Any

from src.constants.unit_edits import load_unit_edits
from src import ndf

def unit_edits_cadavre_descriptor(source_path: Any) -> None:
    """Edit unit cadavre descriptor in UnitCadavreDescriptor.ndf"""
    ndf_file = "UnitCadavreDescriptor.ndf"
    
    # Load all depiction edits
    unit_edits = load_unit_edits()

    for unit_name, edits in unit_edits.items():
        add_orders = edits.get("orders", {}).get("add_orders", [])
        if add_orders and "UnloadFromTransport" in add_orders:
            
            cadavre_descriptor = source_path.by_n(f"Descriptor_UnitCadavre_{unit_name}")
            
            modules_list = cadavre_descriptor.v.by_m("ModulesDescriptors")
            for module in modules_list.v:
                if isinstance(module.v, ndf.model.Object):
                    module_type = module.v.type
                    if module_type == "UnitCadavreModuleDescriptor":
                        stolen_descriptors = module.v.by_m("ModuleDescriptorsToSteal")
                        stolen_descriptors.v.add(f"~/Descriptor_Unit_{unit_name}/Transporter")
                    
            modules_list.v.add(f"~/Descriptor_Unit_{unit_name}/Transporter")

