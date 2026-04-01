"""Constants for MLRS cluster AP impact effects at 200 m."""

# TRandomHappening definition for MLRS cluster AP (200 m)
FxImpactMlrsClusterAp200m_ = """TRandomHappening
(
    Alternatives = 
    [
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_200m_1
        ),
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_200m_2
        ), 
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_200m_3
        )
    ]
)"""
