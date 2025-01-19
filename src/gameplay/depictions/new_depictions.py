"""Functions for creating depictions for new units."""

from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def create_infantry_depictions(source_path: Any) -> None:
    """Create infantry depiction entries in GeneratedDepictionInfantry.ndf."""
    logger.info("Creating infantry depiction entries")
    
    for donor, edits in NEW_UNITS.items():
        if not edits.get("is_infantry", False) or edits.get("is_ground_vehicle", False):
            continue
            
        unit_name = edits["NewName"]
        
        # Clone all required objects
        depictionsquad_obj = source_path.by_namespace(f"Gfx_{donor}").copy()
        depictionsquad_obj.namespace = f"Gfx_{unit_name}"
        
        weaponalternatives_obj = source_path.by_namespace(f"AllWeaponAlternatives_{donor}").copy()
        weaponalternatives_obj.namespace = f"AllWeaponAlternatives_{unit_name}"
        
        weaponsubdepictions_obj = source_path.by_namespace(f"AllWeaponSubDepiction_{donor}").copy()
        weaponsubdepictions_obj.namespace = f"AllWeaponSubDepiction_{unit_name}"
        weaponsubdepictions_obj.v.by_member("Alternatives").v = f"AllWeaponAlternatives_{unit_name}"
        
        weaponbackpack_obj = source_path.by_namespace(f"AllWeaponSubDepictionBackpack_{donor}").copy()
        weaponbackpack_obj.namespace = f"AllWeaponSubDepictionBackpack_{unit_name}"
        weaponbackpack_obj.v.by_member("Alternatives").v = f"AllWeaponAlternatives_{unit_name}"
        
        depictionalternatives_list = source_path.by_namespace(f"TacticDepiction_{donor}_Alternatives").copy()
        depictionalternatives_list.namespace = f"TacticDepiction_{unit_name}_Alternatives"
        
        soldierdepiction_obj = source_path.by_namespace(f"TacticDepiction_{donor}_Soldier").copy()
        soldierdepiction_obj.namespace = f"TacticDepiction_{unit_name}_Soldier"
        soldierdepiction_obj.v.by_member("Alternatives").v = f"TacticDepiction_{unit_name}_Alternatives"
        soldierdepiction_obj.v.by_member("SubDepictions").v = (
            f"[AllWeaponSubDepiction_{unit_name}, AllWeaponSubDepictionBackpack_{unit_name}]")
        
        ghostdepiction_obj = source_path.by_namespace(f"TacticDepiction_{donor}_Ghost").copy()
        ghostdepiction_obj.namespace = f"TacticDepiction_{unit_name}_Ghost"
        ghostdepiction_obj.v.by_member("Alternatives").v = f"TacticDepiction_{unit_name}_Alternatives"
        
        # Find insertion point
        for row_count, row in enumerate(source_path, start=0):
            if row.namespace == "InfantrySelectorTactic_00_01":
                append_row = row_count
                break
        
        # Create comment and new entries
        comment_title = f'// *****************************[ {unit_name} ]*****************************\n'
        new_entries = (
            comment_title,
            depictionsquad_obj,
            weaponalternatives_obj,
            weaponsubdepictions_obj,
            weaponbackpack_obj,
            depictionalternatives_list,
            soldierdepiction_obj,
            ghostdepiction_obj
        )
        
        # Insert new entries
        source_path.insert(append_row, new_entries)
        logger.info(f"Added depiction entries for {unit_name}")
        
        # Add mimetic map entries
        source_path.by_n("InfantryMimetic").v.add((f"'{unit_name}'", f"TacticDepiction_{unit_name}_Soldier"))
        source_path.by_n("InfantryMimeticGhost").v.add((f"'{unit_name}'", f"TacticDepiction_{unit_name}_Ghost"))
        
        # Add transported infantry catalog entry
        for row in source_path:
            if not isinstance(row.v, ndf.model.Object) or row.v.type != "TTransportedInfantryCatalogEntries":
                continue
                
            entry_list = row.v.by_member("Entries").v
            for entry in entry_list:
                if entry.v.by_member("Identifier").v == f'"{donor}"':
                    new_catalog_entry = entry.copy()
                    break
                    
            # Update meshes list
            new_mesh_list = [f"$/GFX/DepictionResources/Modele_{donor}"]
            for i in range(2, edits.get("alternatives_count", 1) + 1):
                new_mesh_list.append(f"$/GFX/DepictionResources/Modele_{donor}_{i:02}")
                
            new_meshes = ndf.model.List()
            for mesh in new_mesh_list:
                new_meshes.add(mesh)
                
            new_catalog_entry.v.by_member("Meshes").v = new_meshes
            new_catalog_entry.v.by_member("Count").v = str(edits.get("alternatives_count", 1))
            new_catalog_entry.v.by_member("Identifier").v = f'"{unit_name}"'
            
            entry_list.add(new_catalog_entry)
            logger.info(f"Added transported infantry catalog entry for {unit_name}")

def create_showroom_depictions(source_path: Any) -> None:
    """Create showroom entries in ShowRoomUnits.ndf."""
    logger.info("Creating showroom depiction entries")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits:
            continue
            
        unit_name = edits["NewName"]
        donor_unit = source_path.by_n(f"Descriptor_ShowRoomUnit_{donor}")
        if not donor_unit:
            logger.warning(f"Donor showroom unit {donor} not found")
            continue
            
        # Clone donor showroom unit
        new_unit = donor_unit.copy()
        new_unit.namespace = f"Descriptor_ShowRoomUnit_{unit_name}"
        
        # Update basic properties
        new_unit.v.by_member("DescriptorId").v = f"GUID:{{{edits['ShowroomGUID']}}}"
        new_unit.v.by_member("ClassNameForDebug").v = f"'ShowRoomUnit_{unit_name}'"
        
        # Update modules
        for module in new_unit.v.by_member("ModulesDescriptors").v:
            if not isinstance(module.v, ndf.model.Object):
                continue
                
            module_type = module.v.type
            
            if module_type == "TApparenceModuleDescriptor":
                if not edits.get("is_ground_vehicle", False):
                    module.v.by_member("Depiction").v = "$/GFX/Depiction/InfantryDepictionSquadShowroom"
                    
            elif module_type == "TInfantrySquadModuleDescriptor":
                if "SquadSize" in edits:
                    module.v.by_member("NbSoldatInGroupeCombat").v = str(edits["SquadSize"])
                module.v.by_member("InfantryMimeticName").v = f"'{unit_name}'"
                module.v.by_member("WeaponUnitFXKey").v = f"'{unit_name}'"
                
                # Update mimetic descriptor
                mimetic = module.v.by_member("MimeticDescriptor").v
                mimetic.by_member("DescriptorId").v = f"GUID:{{{edits['GroupeCombatGUID']}}}"
                mimetic.by_member("MimeticName").v = f"'{unit_name}'"
                
            elif module_type == "TInfantrySquadWeaponAssignmentModuleDescriptor":
                if "WeaponAssignment" in edits:
                    module.v.by_member("InitialSoldiersToTurretIndexMap").v = f"MAP {str(edits['WeaponAssignment'])}"
                    
            elif module_type == "TCameraShowroomModuleDescriptor":
                if edits.get("is_infantry", False):
                    module.v.by_member("SpawnType").v = "EShowroomSpawnType/Infantry"
                elif edits.get("is_ground_vehicle", False):
                    module.v.by_member("SpawnType").v = "EShowroomSpawnType/Vehicle"
                    
            elif module_type == "TTypeUnitModuleDescriptor":
                module.v.by_member("MotherCountry").v = f"'{edits['Nation']}'"
                if edits.get("is_infantry", False):
                    module.v.by_member("AcknowUnitType").v = "~/TAcknowUnitType_Inf"
                    module.v.by_member("TypeUnitFormation").v = "'Char'"
        
        # Add the new showroom unit
        source_path.add(new_unit)
        logger.info(f"Added showroom entry for {unit_name}")

def create_button_textures(source_path: Any) -> None:
    """Create button texture entries in ButtonTexturesUnites.ndf."""
    logger.info("Creating button texture entries")
    
    textures_map = source_path.by_n("UnitButtonTextureAdditionalBank").v.by_member("Textures").v
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits:
            continue
            
        unit_name = edits["NewName"]
        donor_texture_map = textures_map.by_key(f'"Texture_Button_Unit_{donor}"').v
        
        # Get the texture filename either from ButtonTexture override or donor unit
        if "ButtonTexture" in edits:
            # Use specified texture from another unit
            specific_texture_map = textures_map.by_key(f'"Texture_Button_Unit_{edits["ButtonTexture"]}"').v
            button_texture = specific_texture_map.by_key("~/ComponentState/Normal").v.by_member("FileName").v
        else:
            # Use donor unit's texture
            button_texture = donor_texture_map.by_key("~/ComponentState/Normal").v.by_member("FileName").v
        
        # Create new texture entry
        new_entry_key = f'"Texture_Button_Unit_{unit_name}"'
        new_entry_value = (
            f'MAP [('
            f'~/ComponentState/Normal, '
            f'TUIResourceTexture( FileName = {button_texture}'
            f'))]'
        )
        
        # Add to textures map
        textures_map.add((new_entry_key, new_entry_value))
        logger.info(f"Added button texture for {unit_name} using texture {button_texture}")

def create_cadavre_depictions(source_path: Any) -> None:
    """Create cadavre depiction entries in UniteCadavreDescriptor.ndf."""
    logger.info("Creating cadavre depiction entries")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or "CadavreGUID" not in edits:
            continue
            
        # Skip units that don't need cadavre depictions
        if edits.get("is_unarmed", False):
            continue
            
        unit_name = edits["NewName"]
        
        # Clone the donor's cadavre descriptor
        donor_cadavre = source_path.by_namespace(f"Descriptor_UnitCadavre_{donor}")
        if not donor_cadavre:
            logger.warning(f"Donor cadavre descriptor for {donor} not found")
            continue
            
        new_cadavre = donor_cadavre.copy()
        
        # Only update these three fields
        new_cadavre.namespace = f"Descriptor_UnitCadavre_{unit_name}"
        new_cadavre.v.by_member("DescriptorId").v = f"GUID:{{{edits['CadavreGUID']}}}"
        new_cadavre.v.by_member("ClassNameForDebug").v = f"'Unit_Cadavre{unit_name}'"
        
        # Add the new cadavre descriptor
        source_path.add(new_cadavre)
        logger.info(f"Added cadavre descriptor for {unit_name}")

def create_mimetic_depictions(source_path: Any) -> None:
    """Create mimetic depiction entries in MimeticDescriptor.ndf."""
    logger.info("Creating mimetic depiction entries")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or not edits.get("is_infantry", False):
            continue
            
        unit_name = edits["NewName"]
        
        # Create mimetic descriptor
        entry = (
            f"export Descriptor_Mimetic_{unit_name} is TMimeticDescriptor\n"
            f"(\n"
            f"    MimeticName = '{unit_name}'\n"
            f"    DescriptorId = GUID:{{{edits['GroupeCombatGUID']}}}\n"
            f"    IdleAnimation = $/GFX/DepictionResources/Anim_{unit_name}_idle\n"
            f"    MovementAnimation = $/GFX/DepictionResources/Anim_{unit_name}_move\n"
            f"    DeathAnimation = $/GFX/DepictionResources/Anim_{unit_name}_death\n"
            f")\n"
        )
        source_path.add(entry)
        logger.info(f"Added mimetic depiction for {unit_name}")

def create_ghost_depictions(source_path: Any) -> None:
    """Create ghost depiction entries in GeneratedDepictionGhosts.ndf."""
    logger.info("Creating ghost depiction entries")
    
    for donor, edits in NEW_UNITS.items():
        if not edits.get("is_ground_vehicle", False):
            continue
            
        unit_name = edits["NewName"]
        
        # Create ghost depiction entry
        entry = (
            f'GhostDepiction_{unit_name} is GhostVehicleDepictionTemplate'
            f'('
            f'    Alternatives = Alternatives_{unit_name}'
            f'    Selector = Selector_{unit_name}'
            f')'
        )
        source_path.add(entry)
        logger.info(f"Added ghost depiction for {unit_name}")

def create_alternatives_depictions(source_path: Any) -> None:
    """Create alternatives depiction entries in GeneratedDepictionAlternatives.ndf."""
    logger.info("Creating alternatives depiction entries")
    
    for donor, edits in NEW_UNITS.items():
        if not edits.get("is_ground_vehicle", False):
            continue
            
        unit_name = edits["NewName"]
        
        # Create alternatives entry using donor's models
        entry = (
            f'Alternatives_{unit_name} is ['
            f'    DepictionDescriptor_LOD_High( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor} ),'
            f'    DepictionDescriptor_LOD_Mid( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor}_MID ),'
            f'    DepictionDescriptor_LOD_Low( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor}_LOW ),'
            f']'
        )
        source_path.add(entry)
        logger.info(f"Added alternatives depiction for {unit_name}") 

def create_veh_human_depictions(source_path: Any) -> None:
    """Create human depiction entries for vehicles in GeneratedDepictionHumans.ndf."""
    logger.info("Creating human depiction entries for vehicles")
    
    for donor, edits in NEW_UNITS.items():
        if not (edits.get("is_ground_vehicle", False) and edits.get("is_infantry", False)):
            continue
            
        unit_name = edits["NewName"]
        
        # Find donor mesh names
        mesh_names = None
        for row in source_path:
            if row.namespace != f"HumanSubDepictions_{donor}":
                continue
                
            left_servant = row.v[0]
            right_servant = row.v[1]
            
            left_mesh = left_servant.v.by_m("MeshDescriptorHigh").v.split(
                "$/GFX/DepictionResources/MeshDescriptor_")[-1]
            right_mesh = right_servant.v.by_m("MeshDescriptorHigh").v.split(
                "$/GFX/DepictionResources/MeshDescriptor_")[-1]
                
            mesh_names = (left_mesh, right_mesh)
            break
            
        if not mesh_names:
            logger.warning(f"Could not find mesh names for {donor}")
            continue
            
        left_mesh, right_mesh = mesh_names
        
        # Create human depiction entries
        human_depiction = (
            f'HumanSubDepictions_{unit_name} is\n'
            f'[\n'
            f'    SubDepiction_ATGMServantLeft\n'
            f'    (\n'
            f'        MeshDescriptorHigh = $/GFX/DepictionResources/MeshDescriptor_{left_mesh}\n'
            f'        MeshDescriptorLow = $/GFX/DepictionResources/MeshDescriptor_{left_mesh}_LOW\n'
            f'    ),\n'
            f'    SubDepiction_ATGMServantRight\n'
            f'    (\n'
            f'        MeshDescriptorHigh = $/GFX/DepictionResources/MeshDescriptor_{right_mesh}\n'
            f'        MeshDescriptorLow = $/GFX/DepictionResources/MeshDescriptor_{right_mesh}_LOW\n'
            f'    )\n'
            f']\n'
        )
        
        showroom_depiction = (
            f'HumanSubDepictionsShowroom_{unit_name} is\n'
            f'[\n'
            f'    ShowroomSubDepiction_ATGMServantLeft\n'
            f'    (\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/MeshDescriptor_{left_mesh}\n'
            f'    ),\n'
            f'    ShowroomSubDepiction_ATGMServantRight\n'
            f'    (\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/MeshDescriptor_{right_mesh}\n'
            f'    )\n'
            f']\n'
        )
        
        # Find insertion point and add entries
        for row in source_path:
            if not is_obj_type(row.v, "TTransportedInfantryCatalogEntries"):
                continue
                
            source_path.insert(row.index, showroom_depiction)
            source_path.insert(row.index, human_depiction)
            logger.info(f"Added human depictions for {unit_name}")
            
            # Add catalog entry
            catalog_entry = (
                f'TTransportedInfantryEntry\n'
                f'(\n'
                f'    Count = {edits["alternatives_count"]}\n'
                f'    Identifier = "{unit_name}"\n'
                f'    Meshes =\n'
                f'    [\n'
                f'        $/GFX/DepictionResources/MeshDescriptor_{left_mesh},\n'
                f'        $/GFX/DepictionResources/MeshDescriptor_{right_mesh}\n'
                f'    ]\n'
                f'    UniqueCount = {edits["alternatives_count"]}\n'
                f')\n'
            )
            
            row.v.by_m("Entries").v.add(catalog_entry)
            logger.info(f"Added catalog entry for {unit_name}")
            break
                
def create_veh_depictions(source_path: Any) -> None:
    """Create vehicle depiction entries in GeneratedDepictionVehicles.ndf."""
    logger.info("Creating vehicle depiction entries")
    
    def get_base_namespace(namespace: str, prefix: str) -> str:
        """Extract the base namespace after the given prefix."""
        return namespace.split(f"{prefix}_")[-1].split("_")[0]

    def create_new_object(obj_row: Any, unit_name: str, is_weapon: bool, weapon_num: int = 0) -> Any:
        """Create a new depiction object with updated namespace."""
        new_obj = obj_row.copy()
        if is_weapon:
            new_obj.namespace = f"DepictionOperator_{unit_name}_Weapon{weapon_num}"
        else:
            new_obj.namespace = f"Gfx_{unit_name}_Autogen"
        return new_obj

    for donor, edits in NEW_UNITS.items():
        if not edits.get("is_ground_vehicle", False):
            continue
            
        unit_name = edits["NewName"]
        weapon_count = 0
        new_objects = []

        for obj_row in source_path:
            namespace = obj_row.namespace
            
            if "DepictionOperator_" in namespace:
                if donor == get_base_namespace(namespace, "DepictionOperator"):
                    weapon_count += 1
                    new_objects.append(create_new_object(obj_row, unit_name, True, weapon_count))
            
            elif "Gfx_" in namespace:
                if donor == get_base_namespace(namespace, "Gfx"):
                    new_objects.append(create_new_object(obj_row, unit_name, False))

        for obj in new_objects:
            logger.info(f"Adding new object to GeneratedDepictionVehicles.ndf: {obj.namespace}")
            source_path.add(obj)         
            
def create_aerial_ghost_depictions(source_path: Any) -> None:
    """Create aerial ghost depiction entries in GeneratedDepictionAerialGhosts.ndf."""
    logger.info("Creating aerial ghost depiction entries")
    
    for donor, edits in NEW_UNITS.items():
        if edits.get("is_aerial", False):
            unit_name = edits["NewName"]
            new_object_entry = (
                f'GhostDepiction_{unit_name} is GhostAerialDepictionTemplate\n'
                f'(\n'
                f'    Alternatives = Alternatives_{unit_name}\n'
                f'    Selector = SpecificAirplaneDepictionSelector\n'
                f')'
            )
            source_path.add(new_object_entry)
            logger.info(f"Added aerial ghost depiction for {unit_name}")
            
def create_veh_depiction_selectors(source_path: Any) -> None:
    """Create vehicle depiction selector entries in GeneratedDepictionSelectors.ndf."""
    logger.info("Creating vehicle depiction selector entries")
    
    for donor, edits in NEW_UNITS.items():
        if edits.get("is_ground_vehicle", False):
            unit_name = edits["NewName"]
            new_entry = f"Selector_{unit_name} is SpecificVehicleDepictionSelector"
            source_path.add(new_entry)
            logger.info(f"Added vehicle depiction selector for {unit_name}")

def create_veh_showroom_depictions(source_path: Any) -> None:
    """Create vehicle showroom depiction entries in GeneratedDepictionVehiclesShowroom.ndf."""
    logger.info("Creating vehicle showroom depiction entries")
    
    for donor, edits in NEW_UNITS.items():
        if edits.get("is_ground_vehicle", False):
            unit_name = edits["NewName"]
            new_depiction_obj = source_path.by_namespace(f"Gfx_{donor}_Showroom").copy()
            new_depiction_obj.namespace = f"Gfx_{unit_name}_Showroom"
            new_depiction_obj.v.by_member("Selector").v = f"Selector_{unit_name}"
            
            if edits.get("is_infantry", False):
                new_depiction_obj.v.by_member("SubDepictions").v = f"HumanSubDepictionsShowroom_{unit_name}"
                
            source_path.add(new_depiction_obj)
            logger.info(f"Added vehicle showroom depiction for {unit_name}")
