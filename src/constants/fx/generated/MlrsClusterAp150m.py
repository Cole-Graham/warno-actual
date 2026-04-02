"""Constants for MLRS cluster AP impact effects at 150 m."""

# TRandomHappening definition for MLRS cluster AP (150 m)
FxImpactMlrsClusterAp150m_ = """TRandomHappening
(
    Alternatives = 
    [
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_150m_1
        ),
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_150m_2
        ), 
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_150m_3
        )
    ]
)"""
