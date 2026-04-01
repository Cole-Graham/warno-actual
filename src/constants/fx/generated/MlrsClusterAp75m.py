"""Constants for MLRS cluster AP impact effects at 75 m."""

# TRandomHappening definition for MLRS cluster AP (75 m)
FxImpactMlrsClusterAp75m_ = """TRandomHappening
(
    Alternatives = 
    [
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_75m_1
        ),
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_75m_2
        ), 
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_75m_3
        )
    ]
)"""
