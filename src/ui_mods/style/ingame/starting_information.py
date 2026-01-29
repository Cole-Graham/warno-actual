"""Functions for modifying UI HUD score view."""
from typing import Any

from src import ModConfig
from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

config = ModConfig.get_instance()
build_target = config.config_data['build_config']['target']

def edit_uispecificdisplaystartinginformationview(source_path) -> None:
    """Edit UISpecificDisplayStartingInformationView.ndf."""
    logger.info("Editing UISpecificDisplayStartingInformationView.ndf")
    
    _update_information_team_container(source_path)

def _update_information_team_container(source_path) -> None:
    # DisplayStartingInformationTeamContainer template
    startinginformationview = source_path.by_namespace("DisplayStartingInformationTeamContainer")
    elements = startinginformationview.v.by_member("Elements")
    if build_target == "gameplay":
        elements.v[0].v.by_m("ComponentDescriptor").v.by_m(
            "ComponentFrame").v.by_m("MagnifiableWidthHeight").v = "[36.0, 36.0]"