"""Tests for scatter extract/emit (requires ndf_parse)."""

import sys
import unittest
from pathlib import Path

# Repo root: tools/fx_editor/testing/ → parents[3]
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

try:
    import ndf_parse  # noqa: F401
except ImportError:
    raise unittest.SkipTest('ndf_parse not installed')

from src import ndf
from tools.fx_editor.scatter_emit import (
    build_cluster_emit_template_indices,
    distinct_placeable_template_first_indices,
    emit_scatter_into_actions,
    find_actions_list,
    format_ndf,
    list_placeable_tsimultaneous_templates,
)
from tools.fx_editor.scatter_extract import (
    extract_scatter_from_file,
    extract_scatter_from_parsed,
    extract_scatter_points_with_vfx,
)
from tools.fx_editor.scatter_model import ScatterBurst, ScatterProject, load_scatter_calibration_yaml


def _vanilla_cluster_path() -> Path:
    p = ROOT / 'fx_impact_sol_HE_M270_227mm_Cluster_1.ndf'
    if p.exists():
        return p
    return ROOT / 'src' / 'constants' / 'fx' / 'generated' / 'fx_impact_mlrs_cluster_ap_35m_1.ndf'


class ScatterEmitTests(unittest.TestCase):
    def test_emit_mobile_three_bursts_roundtrip(self) -> None:
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        root = ndf.convert(p.read_text(encoding='utf-8'))
        ref, anchor = load_scatter_calibration_yaml()
        proj = ScatterProject(
            reference_gameplay_radius_m=ref,
            anchor_max_ndf_radius=anchor,
            emit_mode='mobile_position',
            template_list_row_index=0,
            bursts=[
                ScatterBurst(0, 0),
                ScatterBurst(60, 0),
                ScatterBurst(0, -60),
            ],
        )
        n = emit_scatter_into_actions(proj, root)
        self.assertEqual(n, 3)
        al = find_actions_list(root)
        self.assertIsNotNone(al)
        self.assertEqual(len(al), 3)
        ndf.convert(format_ndf(root))
        ex = extract_scatter_from_parsed(root)
        self.assertEqual(ex.count, 3)

    def test_extract_max_radius_positive(self) -> None:
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        ex = extract_scatter_from_file(p)
        self.assertGreater(ex.max_radius_from_origin(), 1000)

    def test_extract_primary_vfx_is_first_taction_in_simultaneous(self) -> None:
        """TSimultaneousAction with Big_ground + DestroyVeget uses Big_ground as group label."""
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        root = ndf.convert(p.read_text(encoding='utf-8'))
        if not isinstance(root, ndf.model.List):
            self.skipTest('Unexpected NDF root')
        pts = extract_scatter_points_with_vfx(root)
        self.assertGreater(len(pts), 0)
        self.assertEqual(pts[0].primary_vfx, 'Big_ground_Impact_Simple')
        self.assertEqual(pts[0].source, 'mobile_position')

    def test_cluster_template_indices_cover_distinct_patterns(self) -> None:
        """Small area-scaled n must still schedule one burst per distinct placeable pattern."""
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        root = ndf.convert(p.read_text(encoding='utf-8'))
        if not isinstance(root, ndf.model.List):
            self.skipTest('Unexpected NDF root')
        al = find_actions_list(root)
        self.assertIsNotNone(al)
        templates = list_placeable_tsimultaneous_templates(al)
        self.assertGreater(len(templates), 3)
        first = distinct_placeable_template_first_indices(templates)
        self.assertGreater(len(first), 3)
        n_eff, idx = build_cluster_emit_template_indices(1, templates)
        self.assertGreaterEqual(n_eff, len(first))
        self.assertEqual(len(idx), n_eff)
        self.assertEqual(idx[: len(first)], first)


if __name__ == '__main__':
    unittest.main()
