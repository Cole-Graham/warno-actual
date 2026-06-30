# Infantry small arms vs strength validation

This document describes the precompute validation in
[`src/data/infantry_small_arms_strength_validation.py`](../../src/data/infantry_small_arms_strength_validation.py).
It runs during constants precomputation (alongside the patcher) and logs errors when
edited or new infantry squads have inconsistent small-arms quantities.

## Purpose

For infantry squads in `unit_edits` or `NEW_UNITS`, the validator checks:

```text
small_arms_total == strength - occupied_slots
```

- **`strength`** — effective squad size from unit edits or vanilla `unit_data`.
- **`small_arms_total`** — sum of `NbWeapons` for **countable** small-arms mounts (rifles,
  SMGs, shotguns, sniper rifles, squad MGs).
- **`occupied_slots`** — soldiers whose primary weapon prevents also carrying a rifle
  (emplaced recoilless / SPG-9 crew, flamethrower primary).

Weapon **teams** (HMG, dedicated AT, emplaced RCL crews with no rifles) are **skipped**
based on resolved loadout, not unit name.

## What counts as countable small arms

Weapons in the `small_arms` constants category, plus vanilla ammo with small-arms damage
families or `MinMax_inf_sniper`, unless excluded by:

- Team weapon prefixes (`MMG_team_`, `HMG_team_`)
- Constants categories: `light_at`, `medium_at`, `heavy_at`, `recoilless`, `ATGM`,
  `AGL`, `napalm`, `fire`, MANPAD / AA categories
- `MinMax_MMG_HMG` or `MinMax_FLAME` on the ammo descriptor

Precomputed output: `constants_precomputation/countable_small_arms_weapons.json`.

## Mount roles (loadout semantics)

Each resolved mount is classified before validation:

| Role | Meaning |
|------|---------|
| `countable` | Counts toward `small_arms_total` |
| `team_mg` | HMG/MMG team weapon (`MMG_team_*` or `MinMax_MMG_HMG`) |
| `occupied` | `MinMax_CanonAP` or `MinMax_FLAME` — displaces a rifle slot |
| `specialist` | AT, ATGM, RPG, recoilless, MANPAD, etc. — excluded from sum |
| `unknown` | Unclassified mod ammo — fail-open (unit stays in validation) |

Classification order: `countable` → `team_mg` → `occupied` → `specialist` → `unknown`.

## Weapon team skip

A unit is **skipped** (not validated) when:

1. It passes the infantry squad filter (`UnitRole` / tags in edits or `unit_data`), and
2. Resolved mounts have **no** `countable` weapons, and
3. Every mount is `team_mg`, `occupied`, or `specialist` (no `unknown`).

Examples:

| Unit | Outcome |
|------|---------|
| `HMGteam_MG3_RFA` | Skip — only `team_mg` |
| `RCL_L6_Wombat_UK` | Skip — only `occupied` RCL ammo |
| `ATteam_Milan_1_UK` | Skip — only `specialist` ATGM |
| `DShV_Metis_SOV` | **Validate** — rifles + RPK + portable Metis |
| `Engineers_Dragon_US` | **Validate** — M16×strength + Dragon |
| Rifle squad + RPG | **Validate** — RPG is `specialist`, rifles are `countable` |

**Portable ATGM** (`MinMax_ATGM`, e.g. Metis, Dragon) does **not** occupy a rifle slot and
does **not** imply weapon team when rifles are present. The same `ATGM` constants category
covers both portable and dedicated-team missiles; skip vs validate depends only on whether
any `countable` mount exists.

## Occupied slots (per turret)

`occupied_slots` uses turret-grouped mounts:

- **`MinMax_CanonAP` per turret:** `max(qty)` across mounts on that turret (dual AP+HE ammo
  on one crew counts as one soldier).
- **`MinMax_FLAME` per turret:** `sum(qty)` (multiple flamethrower soldiers stay distinct).
- **`MinMax_ATGM`:** never occupies a slot.

## Mount resolution

`resolve_infantry_mounts_by_turret()` builds post-edit loadouts from `game_db["weapons"]`,
applying:

- `WeaponDescriptor.turrets.remove`
- `equipmentchanges.replace`, `quantity`, `insert`

For `replace`, a **list** under one `old_weapon` applies **one entry per matching mount**
(in turret order), not once per turret — e.g. donor with two `RocketInf_RPG7VR_64mm`
turrets and `[SAW replace, RPG29 replace]` yields one SAW mount and one RPG29 mount.

Known gap: deep `turrets.MountedWeapons` insert/replace not in `equipmentchanges` may be
missed if the ammo is absent from vanilla `weapons_db`.

## Escape hatches

- **`INFANTRY_SMALL_ARMS_STRENGTH_SKIP_UNITS`** in the validation module — explicit skip set.
- **`UNITS_SKIP_STRENGTH_VARIANTS`** from `small_arms_quantity_validation` — strength-variant
  ammo naming.

## Fixing validation errors

1. Check `WeaponDescriptor.equipmentchanges.quantity` in `unit_edits` / `NEW_UNITS`.
2. Confirm strength matches intended headcount.
3. For flamethrower or emplaced-gun squads, ensure `occupied_slots` math matches design.
4. If the unit is intentionally a weapon team shaped like infantry in edits, add to
   `INFANTRY_SMALL_ARMS_STRENGTH_SKIP_UNITS`.

## Related files

| File | Role |
|------|------|
| [`infantry_small_arms_strength_validation.py`](../../src/data/infantry_small_arms_strength_validation.py) | Validation logic |
| [`constants_precomputation.py`](../../src/data/constants_precomputation.py) | Wires precompute + calls validator |
| [`small_arms_quantity_validation.py`](../../src/data/small_arms_quantity_validation.py) | Separate check: valid strength suffixes on ammo names |
| [`testing/test_infantry_small_arms_strength_validation.py`](../../testing/test_infantry_small_arms_strength_validation.py) | Unit tests |
