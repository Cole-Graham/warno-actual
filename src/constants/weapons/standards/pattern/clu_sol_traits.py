"""CLU SOL damage families → WeaponTraits.ndf descriptor keys (TraitsToken list).

Used when patching ammunition: replace legacy ``cluster`` with family-specific traits and drop ``HEAT``.
"""

from typing import Dict

# Arme.Family value (as in NDF / ammunition constants) → trait key in WeaponTraits.ndf
CLU_SOL_DAMAGE_FAMILY_TO_TRAIT: Dict[str, str] = {
    "DamageFamily_clu_sol_ap": "clusterHEAT",
    "DamageFamily_clu_sol_hefrag": "clusterHEFrag",
}

# NDF list element forms for TraitsToken
CLU_SOL_TRAIT_TOKEN_CLUSTER = "'cluster'"
CLU_SOL_TRAIT_TOKEN_HEAT = "'HEAT'"
