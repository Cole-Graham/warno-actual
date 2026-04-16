"""Editor for UICommonUnitNameResources.ndf — tag-based TFS matchers."""

from typing import Any

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uicommonunitnameresources(source_path: Any) -> None:
    """Replace influence-map CMD matcher with tag-based matchers for CMD/LDR/LDRSOV."""
    logger.info("Editing UICommonUnitNameResources.ndf")

    obj = source_path.by_namespace("UICommonUnitNameResources").v
    tfs_list = obj.by_member("UnitMatchersForTFS").v

    # Row 0 is ("#CMD", THasInfluenceMapStrengthUnitMatcher()) — replace the entire row
    tfs_list.replace(
        0,
        '("#CMD", TAllUnitMatchers(Matchers = [TTagsMatcher(Tags = ["CMD_Unit"])]))',
    )

    # Insert #LDR and #LDRSOV rows right after #CMD (indices 1 and 2)
    tfs_list.insert(
        1,
        '("#LDR", TAllUnitMatchers(Matchers = [TTagsMatcher(Tags = ["LDR_Unit"])]))',
    )
    tfs_list.insert(
        2,
        '("#LDRSOV", TAllUnitMatchers(Matchers = [TTagsMatcher(Tags = ["LDR_SOV_Unit"])]))',
    )

    logger.info("Added CMD_Unit / LDR_Unit / LDR_SOV_Unit TFS matchers")
