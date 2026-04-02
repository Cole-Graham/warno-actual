"""Constants for MLRS cluster AP impact effects at 100 m."""

# TRandomHappening definition for MLRS cluster AP (100 m)
FxImpactMlrsClusterAp100m_ = """TRandomHappening
(
    Alternatives = 
    [
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_100m_1
        ),
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_100m_2
        ), 
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_100m_3
        )
    ]
)"""
