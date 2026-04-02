"""Constants for MLRS cluster AP impact effects at 35 m."""

# TRandomHappening definition for MLRS cluster AP (35 m)
FxImpactMlrsClusterAp35m_ = """TRandomHappening
(
    Alternatives = 
    [
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_35m_1
        ),
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_35m_2
        ), 
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_35m_3
        )
    ]
)"""
