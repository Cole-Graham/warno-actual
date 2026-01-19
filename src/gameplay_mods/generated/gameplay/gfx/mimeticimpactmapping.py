"""editing MimeticImpactMapping.ndf"""

from src.utils.logging_utils import setup_logger
from src import ndf
from src.utils.ndf_utils import find_obj_by_type

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
    logger.info("Added grad_incendiary_rocket to happenings map")