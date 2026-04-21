"""Tests for scatter wait redistribution and timeline extraction (requires ndf_parse for timeline file test)."""

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

from tools.fx_editor.scatter_timing import redistribute_anchor_waits
from tools.fx_editor.scatter_analyze import analyze_effect_groups
from tools.fx_editor.scatter_timeline import build_timeline_events, timeline_end_time_s


def _vanilla_cluster_path() -> Path:
    """Prefer game vanilla M270 cluster NDF; mlrs ``*_35m_*`` is generated fixture fallback only."""
    for rel in (
        'fx_impact_sol_HE_M270_227mm_Cluster_1.ndf',
        'src/constants/fx/generated/fx_impact_sol_HE_M270_227mm_Cluster_1.ndf',
    ):
        p = ROOT / rel
        if p.exists():
            return p
    return ROOT / 'src' / 'constants' / 'fx' / 'generated' / 'fx_impact_mlrs_cluster_ap_35m_1.ndf'


class ScatterTimingTests(unittest.TestCase):
    def test_redistribute_n3_bounds(self) -> None:
        w = redistribute_anchor_waits(0.2, 0.75, 3)
        self.assertEqual(len(w), 3)
        self.assertAlmostEqual(w[0], 0.2)
        self.assertAlmostEqual(w[2], 0.75)
        # Anchor waits are rounded to hundredths for NDF output (0.475 → 0.48).
        self.assertAlmostEqual(w[1], 0.48, places=2)

    def test_redistribute_n5_interval(self) -> None:
        w = redistribute_anchor_waits(0.2, 1.5, 5)
        self.assertEqual(len(w), 5)
        self.assertAlmostEqual(w[0], 0.2)
        self.assertAlmostEqual(w[4], 1.5)
        self.assertAlmostEqual(w[2], 0.85)

    def test_redistribute_n1(self) -> None:
        w = redistribute_anchor_waits(0.2, 2.0, 1)
        self.assertEqual(w, [0.2])


class ScatterTimelineTests(unittest.TestCase):
    def test_timeline_events_from_cluster_ndf(self) -> None:
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        root = ndf.convert(p.read_text(encoding='utf-8'))
        if not isinstance(root, ndf.model.List):
            self.skipTest('Unexpected NDF root')
        ev = build_timeline_events(root)
        self.assertGreater(len(ev), 0)
        self.assertGreater(timeline_end_time_s(ev), 0.0)

    def test_timeline_events_spread_across_time(self) -> None:
        """Burst indices align with scatter points; times are not all at t_max."""
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        root = ndf.convert(p.read_text(encoding='utf-8'))
        if not isinstance(root, ndf.model.List):
            self.skipTest('Unexpected NDF root')
        ev = build_timeline_events(root)
        times = [e.t_s for e in ev]
        self.assertGreater(len(set(round(t, 4) for t in times)), 1, 'expected multiple distinct event times')
        self.assertLess(min(times), max(times))

    def test_effect_groups_from_cluster_ndf(self) -> None:
        """TSimultaneousAction rows that share the same per-branch VFX pattern are grouped."""
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        root = ndf.convert(p.read_text(encoding='utf-8'))
        if not isinstance(root, ndf.model.List):
            self.skipTest('Unexpected NDF root')
        groups = analyze_effect_groups(root)
        self.assertGreater(len(groups), 0)
        top = max(groups, key=lambda g: g.count)
        self.assertGreaterEqual(top.count, 2)


if __name__ == '__main__':
    unittest.main()
