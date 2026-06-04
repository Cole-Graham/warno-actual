"""CLI helpers shared by run_patcher.py and run_patcher_with_bat.py."""

from __future__ import annotations

import argparse
from typing import Any

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def parse_patcher_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="WARNO mod patcher")
    parser.add_argument(
        "--rebuild-db",
        action="store_true",
        help=(
            "Force data_config.build_database and update_master_metadata to true "
            "for this run (overrides config.YAML)"
        ),
    )
    return parser.parse_args(argv)


def apply_rebuild_db_override(config_data: dict[str, Any], args: argparse.Namespace) -> None:
    if not args.rebuild_db:
        return
    data_config = config_data.setdefault("data_config", {})
    data_config["build_database"] = True
    data_config["update_master_metadata"] = True
    logger.info("--rebuild-db: forcing build_database and update_master_metadata")
