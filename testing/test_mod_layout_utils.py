"""Tests for mod folder layout repair after ndf sync."""

import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.utils.mod_layout_utils import ensure_mod_folder_layout


class TestModLayoutUtils(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.warno_mods = Path(self.temp_dir) / "Mods"
        self.sourcemod = self.warno_mods / "sourcemod"
        self.dest_mod = self.warno_mods / "WARNO ACTUAL"
        self._create_sourcemod_layout()
        self._create_dest_layout_wrong_names()
        self.config = {
            "build_config": {"write_dev": False, "target": "gameplay"},
            "directories": {
                "warno_mods": str(self.warno_mods),
                "base_game": "sourcemod",
                "gameplay_dev": "WARNO ACTUAL dev",
                "gameplay_release": "WARNO ACTUAL",
                "ui_only_dev": "UI dev",
                "ui_only_release": "UI release",
            },
        }

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _create_sourcemod_layout(self):
        loc = self.sourcemod / "GameData" / "Localisation" / "sourcemod"
        loc.mkdir(parents=True)
        (loc / "LocalisationDicos.ndf").write_text(
            'FileName = "Localisation/sourcemod/UNITS.csv"\n',
            encoding="utf-8",
        )

        packs = self.sourcemod / "GameData" / "ResourcePacks" / "sourcemod"
        packs.mkdir(parents=True)
        (packs / "ResourcePacks.ndf").write_text(
            '\n'.join([
                'PackRelativePath = "MeshPack/sourcemod/Mesh_All.spk"',
                'PackRelativePath = "TextureProxy/sourcemod/Mesh_All.ndfbin"',
            ]) + "\n",
            encoding="utf-8",
        )
        mesh = self.sourcemod / "GameData" / "ResourcePacks" / "MeshPack" / "sourcemod"
        mesh.mkdir(parents=True)
        (mesh / "Mesh_All.spk").write_bytes(b"spk")
        proxy = self.sourcemod / "GameData" / "ResourcePacks" / "TextureProxy" / "sourcemod"
        proxy.mkdir(parents=True)
        (proxy / "Mesh_All.ndfbin").write_bytes(b"bin")

    def _create_dest_layout_wrong_names(self):
        loc = self.dest_mod / "GameData" / "Localisation" / "sourcemod"
        loc.mkdir(parents=True)
        shutil.copy2(
            self.sourcemod / "GameData" / "Localisation" / "sourcemod" / "LocalisationDicos.ndf",
            loc / "LocalisationDicos.ndf",
        )

        packs = self.dest_mod / "GameData" / "ResourcePacks" / "sourcemod"
        packs.mkdir(parents=True)
        shutil.copy2(
            self.sourcemod / "GameData" / "ResourcePacks" / "sourcemod" / "ResourcePacks.ndf",
            packs / "ResourcePacks.ndf",
        )
        mesh = self.dest_mod / "GameData" / "ResourcePacks" / "MeshPack" / "sourcemod"
        mesh.mkdir(parents=True)
        shutil.copy2(
            self.sourcemod / "GameData" / "ResourcePacks" / "MeshPack" / "sourcemod" / "Mesh_All.spk",
            mesh / "Mesh_All.spk",
        )
        proxy = self.dest_mod / "GameData" / "ResourcePacks" / "TextureProxy" / "sourcemod"
        proxy.mkdir(parents=True)
        shutil.copy2(
            self.sourcemod / "GameData" / "ResourcePacks" / "TextureProxy" / "sourcemod" / "Mesh_All.ndfbin",
            proxy / "Mesh_All.ndfbin",
        )

    def test_ensure_mod_folder_layout_rewrites_paths_and_moves_dirs(self):
        with patch("src.utils.mod_layout_utils.get_mod_src_path", return_value=self.sourcemod), patch(
            "src.utils.mod_layout_utils.get_mod_dst_path",
            return_value=self.dest_mod,
        ), patch(
            "src.utils.mod_layout_utils.get_mod_name",
            return_value="WARNO ACTUAL",
        ):
            ensure_mod_folder_layout(self.config)

        loc_ndf = self.dest_mod / "GameData" / "Localisation" / "WARNO ACTUAL" / "LocalisationDicos.ndf"
        self.assertTrue(loc_ndf.exists())
        self.assertIn("Localisation/WARNO ACTUAL/", loc_ndf.read_text(encoding="utf-8"))
        self.assertFalse(
            (self.dest_mod / "GameData" / "Localisation" / "sourcemod").exists(),
        )

        packs_ndf = self.dest_mod / "GameData" / "ResourcePacks" / "WARNO ACTUAL" / "ResourcePacks.ndf"
        self.assertTrue(packs_ndf.exists())
        packs_text = packs_ndf.read_text(encoding="utf-8")
        self.assertIn("MeshPack/WARNO ACTUAL/", packs_text)
        self.assertIn("TextureProxy/WARNO ACTUAL/", packs_text)
        self.assertNotIn("sourcemod", packs_text)

        self.assertTrue(
            (self.dest_mod / "GameData" / "ResourcePacks" / "MeshPack" / "WARNO ACTUAL" / "Mesh_All.spk").exists(),
        )
        self.assertTrue(
            (
                self.dest_mod / "GameData" / "ResourcePacks" / "TextureProxy" / "WARNO ACTUAL" / "Mesh_All.ndfbin"
            ).exists(),
        )


if __name__ == "__main__":
    unittest.main()
