"""editing MimeticImpactMapping.ndf"""

from src.utils.logging_utils import setup_logger
from src import ndf
from src.utils.ndf_utils import find_obj_by_type
from src.constants.fx import FxImpactSolBombODABRPO_

logger = setup_logger(__name__)

def edit_gen_gp_gfx_mimeticimpactmapping(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/MimeticImpactMapping.ndf"""
    logger.info("Editing MimeticImpactMapping.ndf")

    _edit_mimetic_registration(source_path)

def _edit_mimetic_registration(source_path) -> None:
    """Edit TMimeticWorldHappeningRegistration"""
    
    mimetic_registration = find_obj_by_type(source_path, "TMimeticWorldHappeningRegistration")
    if not mimetic_registration:
        logger.error("TMimeticWorldHappeningRegistration not found")
        return
    
    happenings_map = mimetic_registration.v.by_m("Happenings")
    if not happenings_map:
        logger.error("Happenings map not found")
        return
    
    # ============================================================================
    # Effects using NEW .ndf files (require TRandomHappening definition)
    # ============================================================================
    # These effects use custom FX .ndf files that are copied to GameData/Fx/Generated/
    # and need their TRandomHappening definitions added to this file before registration.
    
    # Add TRandomHappening definition for ODAB RPO (uses new fx_impact_sol_Bomb_ODAB_RPO_*.ndf files)
    fx_impact_sol_bomb_odab_rpo = ndf.convert(f"FxImpactSolBombODABRPO_ is {FxImpactSolBombODABRPO_}")
    source_path.add(fx_impact_sol_bomb_odab_rpo)
    logger.info("Added FxImpactSolBombODABRPO_ TRandomHappening definition (new .ndf files)")
    
    # Register ODAB RPO in happenings map
    bombe_odab_rpo_value = ndf.convert(
        f"TImpactHappening( Happenings = MAP["
        f"    ( EImpactSurface/Ground , TCompositeHappening( SubHappenings = [ FxImpactSolBombODABRPO_, $/GFX/Sound/SoundHappening_ImpactRoquettes_Buratino_lourdeSol ] ) ),"
        f"    ( EImpactSurface/Water , TCompositeHappening( SubHappenings = [ FxImpactEauHeTresgros2, $/GFX/Sound/SoundHappening_Impact_HE_Gros_Eau ] ) ),"
        f"    ( EImpactSurface/Air , FxImpactSolBombODABRPO_ ),"
        f"    ( EImpactSurface/Wall , TCompositeHappening( SubHappenings = [ FxImpactSolBombODABRPO_, $/GFX/Sound/SoundHappening_ImpactRoquettes_Buratino_lourdeSol ] ) ),"
        f"    ( EImpactSurface/Vehicle , TCompositeHappening( SubHappenings = [ FxImpactSolBombODABRPO_, $/GFX/Sound/SoundHappening_ImpactRoquettes_Buratino_lourdeSol ] ) ),"
        f"    ( EImpactSurface/FlyingVehicle , TCompositeHappening( SubHappenings = [ FxImpactSolBombODABRPO_, $/GFX/Sound/SoundHappening_ImpactRoquettes_Buratino_lourdeSol ] ) ),"
        f"    ( EImpactSurface/Missile , $/GFX/Sound/SoundHappening_ImpactRoquettes_Buratino_lourdeSol ),"
        f"    ( EImpactSurface/Ricochet , nil ),"
        f"])"
    )
    
    happenings_map.v.add(("'BombeODABRPO'", bombe_odab_rpo_value))
    logger.info("Added BombeODABRPO to happenings map")
    
    # ============================================================================
    # Effects using EXISTING vanilla FX .ndf files (no TRandomHappening definition needed)
    # ============================================================================
    # These effects reference TRandomHappening constants that already exist in the base game.
    # We only need to register them in the happenings map.
    
    # Register grad incendiary rocket (uses existing vanilla FxImpactSolHEM270110Mm130MmCluster_)
    grad_incendiary_rocket_value = ndf.convert(
        f"TImpactHappening( Happenings = MAP["
        f"    ( EImpactSurface/Ground , TCompositeHappening( SubHappenings = [ FxImpactSolHEM270110Mm130MmCluster_, $/GFX/Sound/SoundHappening_FULDA_Bombe_Napalm_sol ] ) ),"
        f"    ( EImpactSurface/Water , TCompositeHappening( SubHappenings = [ FxImpactEauHEGros, $/GFX/Sound/SoundHappening_Impact_HE_Gros_Eau ] ) ),"
        f"    ( EImpactSurface/Air , FxOuvertureRoquetteNapalm_ ),"
        f"    ( EImpactSurface/Wall , TCompositeHappening( SubHappenings = [ FxImpactSolHEM270110Mm130MmCluster_, $/GFX/Sound/SoundHappening_FULDA_Bombe_Napalm_sol ] ) ),"
        f"    ( EImpactSurface/Vehicle , TCompositeHappening( SubHappenings = [ FxImpactSolHEM270110Mm130MmCluster_, $/GFX/Sound/SoundHappening_FULDA_Bombe_Napalm_sol ] ) ),"
        f"    ( EImpactSurface/FlyingVehicle , TCompositeHappening( SubHappenings = [ FxImpactSolHEM270110Mm130MmCluster_, $/GFX/Sound/SoundHappening_FULDA_Bombe_Napalm_sol ] ) ),"
        f"    ( EImpactSurface/Missile , $/GFX/Sound/SoundHappening_FULDA_Bombe_Napalm_sol ),"
        f"    ( EImpactSurface/Ricochet , nil ),"
        f"])"
    )
    
    happenings_map.v.add(("'Roquette110Mm130MmClusterNapalm'", grad_incendiary_rocket_value))
    logger.info("Added grad_incendiary_rocket to happenings map (vanilla FX)")