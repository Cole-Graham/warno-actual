"""Parity tests for Call spatial falloff: precomputed mults vs recompute, trim indices."""

import sys
import unittest
from pathlib import Path

# Repo root: tools/fx_editor/testing/ → parents[3]
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))


def _has_ndf_parse() -> bool:
    try:
        import ndf_parse  # noqa: F401
        return True
    except ImportError:
        return False


if _has_ndf_parse():
    from src import ndf
    from tools.fx_editor.call_scale import scale_effect_calls
    from tools.fx_editor.radius_falloff import (
        RADIUS_FALLOFF_SAMPLES,
        burst_indices_removed_by_spatial_trim,
        compute_call_spatial_burst_mults,
        compute_call_spatial_trim_removed_indices,
        ensure_spatial_trim_keeps_one_burst_per_vfx,
    )
    from tools.fx_editor.scatter_model import load_scatter_calibration_yaml


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


@unittest.skipUnless(_has_ndf_parse(), 'ndf_parse not installed')
class CallSpatialParityTests(unittest.TestCase):
    def test_trim_removed_matches_burst_indices_removed(self) -> None:
        """Precomputed ``mults`` path matches direct ``burst_indices_removed_by_spatial_trim``."""
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        root = ndf.convert(p.read_text(encoding='utf-8'))
        if not isinstance(root, ndf.model.List):
            self.skipTest('Unexpected NDF root')
        ref_m, anchor_r = load_scatter_calibration_yaml()
        target_m = 75.0
        falloff = {'Big_ground_Impact_Simple': [100.0] * RADIUS_FALLOFF_SAMPLES}
        mults = compute_call_spatial_burst_mults(
            root,
            falloff,
            target_m,
            ref_m,
            anchor_r,
            None,
        )
        direct = burst_indices_removed_by_spatial_trim(mults)
        expect = ensure_spatial_trim_keeps_one_burst_per_vfx(root, direct)
        via_fn = compute_call_spatial_trim_removed_indices(
            root,
            falloff,
            target_m,
            ref_m,
            anchor_r,
            None,
            layout_burst_count=len(mults),
            mults=mults,
        )
        self.assertIsNotNone(via_fn)
        self.assertEqual(expect, via_fn)

    def test_scale_effect_calls_precomputed_mults_matches_recompute(self) -> None:
        """``spatial_burst_mults`` yields same changes as internal recompute (dry-run)."""
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        root = ndf.convert(p.read_text(encoding='utf-8'))
        if not isinstance(root, ndf.model.List):
            self.skipTest('Unexpected NDF root')
        ref_m, anchor_r = load_scatter_calibration_yaml()
        target_m = 75.0
        falloff = {'Big_ground_Impact_Simple': [100.0] * RADIUS_FALLOFF_SAMPLES}
        mults = compute_call_spatial_burst_mults(
            root,
            falloff,
            target_m,
            ref_m,
            anchor_r,
            None,
        )
        kwargs = dict(
            dry_run=True,
            scale_factor=1.0,
            call_radius_falloff_by_vfx=falloff,
            target_radius_m=target_m,
            ref_m=ref_m,
            anchor_r=anchor_r,
            burst_gameplay_xy_m=None,
        )
        c1 = scale_effect_calls(root, None, **kwargs)
        c2 = scale_effect_calls(root, None, spatial_burst_mults=mults, **kwargs)
        self.assertEqual(c1, c2)


if __name__ == '__main__':
    unittest.main()
