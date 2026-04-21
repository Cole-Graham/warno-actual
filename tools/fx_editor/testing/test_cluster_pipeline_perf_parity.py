"""Parity tests for FX editor cluster perf follow-ups: merged TAction walk, thinning, preview pool."""

from __future__ import annotations

import sys
import unittest
from collections import defaultdict
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


if _has_ndf_parse():
    from concurrent.futures import ProcessPoolExecutor

    from src import ndf
    from tools.fx_editor.batch_variation_jobs import _cluster_preview_job
    from tools.fx_editor.call_scale import _collect_taction_call_rows
    from tools.fx_editor.radius_falloff import burst_indices_kept_by_spatial_independent_thinning
    from tools.fx_editor.scatter_model import load_scatter_calibration_yaml
    from tools.fx_editor.scatter_variation import preview_cluster_variation
    from tools.fx_editor.size_batch import (
        compute_tactioncall_count_variant_t,
        compute_variant_t_and_collect_taction_rows,
    )


@unittest.skipUnless(_has_ndf_parse(), 'ndf_parse not installed')
class ClusterPipelinePerfParityTests(unittest.TestCase):
    def test_merged_variant_t_and_rows_match_two_pass(self) -> None:
        """``compute_variant_t_and_collect_taction_rows`` matches separate variant_t + row collection."""
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        root = ndf.convert(p.read_text(encoding='utf-8'))
        if not isinstance(root, ndf.model.List):
            self.skipTest('Unexpected NDF root')

        v_sep = compute_tactioncall_count_variant_t(root)
        v_merged, rows_merged = compute_variant_t_and_collect_taction_rows(root)
        self.assertEqual(v_sep, v_merged)

        flat = _collect_taction_call_rows(root)
        by_vfx_sep: defaultdict[str, list] = defaultdict(list)
        for vfx, parent, row in flat:
            by_vfx_sep[vfx].append((parent, row))
        self.assertEqual(set(by_vfx_sep.keys()), set(rows_merged.keys()))
        for vfx in rows_merged:
            s_sep = {(id(pa), id(ro)) for pa, ro in by_vfx_sep[vfx]}
            s_m = {(id(pa), id(ro)) for pa, ro in rows_merged[vfx]}
            self.assertEqual(s_sep, s_m, msg=f'vfx={vfx!r}')

    def test_spatial_thinning_deterministic_and_golden(self) -> None:
        """SplitMix64 thinning: stable across calls; frozen set catches accidental algorithm drift."""
        mults = [0.15 + (i % 7) * 0.11 for i in range(47)]
        k1 = burst_indices_kept_by_spatial_independent_thinning(mults)
        k2 = burst_indices_kept_by_spatial_independent_thinning(mults)
        self.assertEqual(k1, k2)
        expected = {
            1,
            4,
            5,
            6,
            10,
            11,
            13,
            17,
            18,
            20,
            25,
            26,
            27,
            30,
            31,
            32,
            33,
            34,
            35,
            40,
            41,
            44,
            45,
            46,
        }
        self.assertEqual(k1, expected)

    def test_preview_roundtrip_false_vs_true_same_scale_stats(self) -> None:
        """Preview with/without NDF round-trip: same burst counts; change lists match when both succeed."""
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        ref_m, anchor_r = load_scatter_calibration_yaml()
        source_m = 35.0
        target_m = 75.0
        wait_max = 8.0
        a = preview_cluster_variation(
            p,
            source_m,
            target_m,
            ref_m,
            anchor_r,
            wait_max,
            pre_emit_roundtrip=False,
            post_emit_roundtrip=False,
        )
        b = preview_cluster_variation(
            p,
            source_m,
            target_m,
            ref_m,
            anchor_r,
            wait_max,
            pre_emit_roundtrip=True,
            post_emit_roundtrip=True,
        )
        self.assertIsNone(a.get('error'), msg=a)
        self.assertIsNone(b.get('error'), msg=b)
        self.assertEqual(a['n0'], b['n0'])
        self.assertEqual(a['n_target'], b['n_target'])
        self.assertEqual(len(a.get('changes', [])), len(b.get('changes', [])))
        self.assertEqual(len(a.get('call_changes', [])), len(b.get('call_changes', [])))

    def test_cluster_preview_process_pool_two_workers(self) -> None:
        """``ProcessPoolExecutor`` can run two cluster preview jobs (pickle + import path)."""
        p = _vanilla_cluster_path()
        if not p.exists():
            self.skipTest('No vanilla cluster NDF in repo')
        ref_m, anchor_r = load_scatter_calibration_yaml()
        source_m = 35.0
        wait_max = 8.0
        base = {
            'path': str(p.resolve()),
            'source_m': source_m,
            'ref_m': ref_m,
            'anchor_r': anchor_r,
            'wait_max': wait_max,
            'include_declaration_params': True,
            'scale_size': True,
            'scale_count': True,
            'effect_named_flags': None,
            'effect_count_scale_pct': None,
            'effect_call_scale_pct': None,
            'effect_call_batch_scale_min': None,
            'effect_call_batch_scale_max': None,
            'param_radius_falloff_by_vfx': None,
            'call_radius_falloff_by_vfx': None,
            'consistent_call_density': False,
            'pre_emit_roundtrip': False,
            'post_emit_roundtrip': False,
        }
        jobs = [
            {**base, 'target_m': 50.0},
            {**base, 'target_m': 75.0},
        ]
        with ProcessPoolExecutor(max_workers=2) as ex:
            results = list(ex.map(_cluster_preview_job, jobs))
        self.assertEqual(len(results), 2)
        for r in results:
            self.assertNotIn('traceback', r)
            self.assertIsNone(r.get('error'), msg=r)
            self.assertGreater(r.get('n_target', 0), 0)


if __name__ == '__main__':
    unittest.main()
