"""One-off helper: rebuild the vanilla DB without running the patcher.

Loads config.YAML, forces ``data_config.build_database = True``, calls
``src.data.build_database`` so the JSON dumps under ``src/data/database/``
get refreshed (in particular ``weapons.json`` and ``depiction_data.json``).
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from src.data import build_database  # noqa: E402


def main() -> None:
    config_path = REPO_ROOT / "config" / "config.YAML"
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    config.setdefault("data_config", {})["build_database"] = True

    print(f"Rebuilding DB using sources at: "
          f"{config['directories']['warno_mods']}/{config['directories']['base_game']}")
    db = build_database(config)
    print(f"Done. Top-level keys: {sorted(db.keys())}")


if __name__ == "__main__":
    main()
