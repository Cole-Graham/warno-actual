"""Constants for MLRS cluster AP impact effects at 125 m."""

# TRandomHappening definition for MLRS cluster AP (125 m)
FxImpactMlrsClusterAp125m_ = """TRandomHappening
(
    Alternatives = 
    [
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_125m_1
        ),
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_125m_2
        ), 
        ImpactWrapper
        (
            Action = $/GFX/GameFx/fx_impact_mlrs_cluster_ap_125m_3
        )
    ]
)"""
