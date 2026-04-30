"""Tuning knobs for the auto-generated SPAAG air-targeting ammo clones.

Each weapon whose final damage family is ``DamageFamily_he_dca`` (see
``src/data/constants_precomputation.build_he_dca_weapons``) is auto-cloned at
``Ammunition.ndf`` edit time into a sibling ``Ammo_<base>_AIR`` descriptor that
uses ``DamageFamily_he_dca_airtargets`` and a reduced ``SuppressDamages``
(``W_AIR``). The new air ammo carries the air-only damage family that is
ignored by every non-aerial resistance family (see
``BlindagesToIgnoreForDamageFamilies`` in WeaponConstantes), so it deals damage
only to aircraft.

``W_AIR = round(W * ratio)`` where ``W`` is the post-edit vanilla
``SuppressDamages`` and ``ratio`` falls back to ``SPAAG_AIR_W_RATIO_DEFAULT``
unless a per-weapon override is set in ``SPAAG_AIR_W_RATIO_OVERRIDES``.

The default ``2/3`` is the median of the per-SPAAG ideal ratios that align
each cannon's vanilla suppress-stun timing with the new airplane stun pack
threshold (``r * Mt = 175`` written suppress, with ``Mt = 250`` set in
``DamageModules.ndf``). It scales naturally with caliber/RoF, so most SPAAGs
need no override -- add an entry only if a specific cannon plays badly with
the default after in-game testing.
"""

from typing import Dict


SPAAG_AIR_W_RATIO_DEFAULT: float = 2.0 / 3.0
"""Default ratio used to derive ``W_AIR = round(W * ratio)`` from the vanilla
post-edit ``SuppressDamages`` of every ``DamageFamily_he_dca`` weapon."""


SPAAG_AIR_W_RATIO_OVERRIDES: Dict[str, float] = {}
"""Per-weapon overrides for the air-ammo suppress ratio.

Keys are base ``weapon_name`` (no ``Ammo_`` prefix, no salvo suffix). Add an
entry like ``"DCA_1_canon_S60_57mm": 0.55`` if a specific SPAAG needs a
different ratio after in-game testing.
"""
