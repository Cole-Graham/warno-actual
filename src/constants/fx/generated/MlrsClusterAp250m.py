"""Constants for MLRS cluster AP impact effects at 250 m."""

# TRandomHappening definition for MLRS cluster AP (250 m)
FxImpactMlrsClusterAp250m_ = """TRandomHappening
(
    Alternatives = 
    [
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_250m_1
        ),
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_250m_2
        ), 
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_250m_3
        )
    ]
)"""
