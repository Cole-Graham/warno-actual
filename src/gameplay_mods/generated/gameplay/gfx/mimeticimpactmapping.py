"""editing MimeticImpactMapping.ndf"""

from src.utils.logging_utils import setup_logger
from src import ndf
from src.utils.ndf_utils import find_obj_by_type
from src.constants.fx import (
    FxImpactMlrsClusterAp100m_,
    FxImpactMlrsClusterAp125m_,
    FxImpactMlrsClusterAp150m_,
    FxImpactMlrsClusterAp175m_,
    FxImpactMlrsClusterAp200m_,
    FxImpactMlrsClusterAp225m_,
    FxImpactMlrsClusterAp250m_,
    FxImpactMlrsClusterAp35m_,
    FxImpactMlrsClusterAp75m_,
    FxImpactSolBombODABRPO_,
)

logger = setup_logger(__name__)


def _mlrs_cluster_ap_impact_happening(fx_constant: str) -> str:
    """TImpactHappening for MLRS cluster AP (same layout as RoquetteM26M270227MmCluster)."""
    return (
        f"TImpactHappening( Happenings = MAP["
        f"    ( EImpactSurface/Ground , TCompositeHappening( SubHappenings = [ {fx_constant}, $/GFX/Sound/SoundHappening_FULDA_Bombe_Cluster_sol ] ) ),"
        f"    ( EImpactSurface/Water , TCompositeHappening( SubHappenings = [ FxImpactEauHEGros, $/GFX/Sound/SoundHappening_FULDA_Bombe_Cluster_sol ] ) ),"
        f"    ( EImpactSurface/Air , TCompositeHappening( SubHappenings = [ FxOuvertureRoquetteCluster_, $/GFX/Sound/SoundHappening_ImpactCanon_petitSol ] ) ),"
        f"    ( EImpactSurface/Wall , TCompositeHappening( SubHappenings = [ {fx_constant}, $/GFX/Sound/SoundHappening_FULDA_Bombe_Cluster_sol ] ) ),"
        f"    ( EImpactSurface/Vehicle , TCompositeHappening( SubHappenings = [ {fx_constant}, $/GFX/Sound/SoundHappening_FULDA_Bombe_Cluster_sol ] ) ),"
        f"    ( EImpactSurface/FlyingVehicle , TCompositeHappening( SubHappenings = [ {fx_constant}, $/GFX/Sound/SoundHappening_FULDA_Bombe_Cluster_sol ] ) ),"
        f"    ( EImpactSurface/Missile , $/GFX/Sound/SoundHappening_FULDA_Bombe_Cluster_sol ),"
        f"    ( EImpactSurface/Ricochet , nil ),"
        f"])"
    )


_MLRS_CLUSTER_AP_NDF = (
    ("35", FxImpactMlrsClusterAp35m_),
    ("75", FxImpactMlrsClusterAp75m_),
    ("100", FxImpactMlrsClusterAp100m_),
    ("125", FxImpactMlrsClusterAp125m_),
    ("150", FxImpactMlrsClusterAp150m_),
    ("175", FxImpactMlrsClusterAp175m_),
    ("200", FxImpactMlrsClusterAp200m_),
    ("225", FxImpactMlrsClusterAp225m_),
    ("250", FxImpactMlrsClusterAp250m_),
)

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

    # MLRS cluster AP size variants (fx_impact_mlrs_cluster_ap_*m_*.ndf); keys: 'MLRSClusterAP35m', etc.
    for size_digits, fx_body in _MLRS_CLUSTER_AP_NDF:
        const_name = f"FxImpactMlrsClusterAp{size_digits}m_"
        ndf_name = ndf.convert(f"{const_name} is {fx_body}")
        source_path.add(ndf_name)
        map_key = f"'MLRSClusterAP{size_digits}m'"
        happening_value = ndf.convert(_mlrs_cluster_ap_impact_happening(const_name))
        happenings_map.v.add((map_key, happening_value))
        logger.info("Added %s TRandomHappening and %s to happenings map", const_name, map_key)

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