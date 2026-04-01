"""Functions for modifying the single-weapon unit info panel UI."""

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Expanded layout for AoE (matches WeaponDamage / WeaponSuppress styling in the same MAP).
_WEAPON_AREA_OF_EFFECT_NDF = """
WeaponDamageTypeAttribute
(
    ElementName = "WeaponAreaOfEffect" Token = "UIPT_AOE" ValueToken = "UIPW_METER" HintToken = "HIP_WAOE"
    Magnifiable_barre = 70
    HasBorder = true
    BordersToDraw = ~/TBorderSide/Bottom | ~/TBorderSide/Left | ~/TBorderSide/Right
    BackgroundBlockColorToken = 'Transparent'
    TextSize = '16'
    MagnifiableOffset = [0.0, -4.0]
    Scale = <Scale>
    FirstMargin = 0
    LastMargin = 5
    HasSousGroupeText = true
    IsSousGroupe = true
    TokenSousGroupe = 'UIPT_AOE'
)
""".strip()


def _weapon_area_of_effect_object():
    """Parse AoE descriptor as an NDF object (not a raw string blob)."""
    tree = ndf.convert(_WEAPON_AREA_OF_EFFECT_NDF.encode("utf-8"))
    return tree[0].v


def edit_ui_ingame_uispecificunitinfosingleweaponpanelview(source_path) -> None:
    """GameData/UserInterface/Use/InGame/UISpecificUnitInfoSingleWeaponPanelView.ndf"""
    logger.info("Modifying UISpecificUnitInfoSingleWeaponPanelViewDescriptor (WeaponAreaOfEffect)")

    descriptor = source_path.by_namespace("UISpecificUnitInfoSingleWeaponPanelViewDescriptor").v
    pool = descriptor.by_m("AttributeDescriptorsPool").v
    
    # WeaponSuppress
    pool.by_k('"WeaponSuppress"').v.by_m("BordersToDraw").v = "~/TBorderSide/Left | ~/TBorderSide/Right"
    
    # WeaponAreaOfEffect
    pool.by_k('"WeaponAreaOfEffect"').v = _weapon_area_of_effect_object()
    logger.info("Updated WeaponAreaOfEffect attribute descriptor")

    _edit_list_affichage(source_path)


def _edit_list_affichage(source_path) -> None:
    """Insert WeaponAreaOfEffect after WeaponSuppress in listeAffichage."""
    weapon_suppress = '"WeaponSuppress"'
    weapon_aoe = '"WeaponAreaOfEffect"'
    liste = source_path.by_namespace("listeAffichage").v
    for row in liste:
        if row.v == weapon_aoe:
            logger.info("listeAffichage already lists WeaponAreaOfEffect; skipping insert")
            return
    for idx, row in enumerate(liste):
        if row.v == weapon_suppress:
            liste.insert(idx + 1, weapon_aoe)
            logger.info("Inserted WeaponAreaOfEffect after WeaponSuppress in listeAffichage")
            return
    logger.warning("WeaponSuppress not found in listeAffichage; WeaponAreaOfEffect not inserted")
