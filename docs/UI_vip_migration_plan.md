# UI mod VIP migration plan

Migration guide for **Warno Actual UI** (`src/ui_mods/`) from **live sourcemod** to **VIP dev sourcemod** (and the eventual public release). Based on `docs/UI_generation_errors.txt`, VIP/live `sourcemod` trees (gitignored locally), mod editor code, and [EUG] developer notes embedded in the error log.

---

## Executive summary

| Finding | Detail |
|--------|--------|
| **Root cause** | VIP mod generation now **fails at NDF compile time** on a rule that previously existed only as an internal runtime assertion. |
| **Not a schema rename** | `BUCKListDescriptorTemplate.ndf` is **byte-identical** between `sourcemod/` and `sourcemod vip/` (verified May 2026). Templates did not change; **validation did**. |
| **Error class** | Single category: **`TBUCKListDescriptor` main-axis child positioning** — list children must not set the **primary-axis** component of `AlignementToFather`, `AlignementToAnchor`, or `MagnifiableOffset`. |
| **Scope in repo** | **13** Python files under `src/ui_mods/` touch these properties (~70+ edit sites). Additional risk in `src/gameplay_mods/userinterface/` (2 files). |
| **Strategic fix** | Stop using **lists for overlap / fine placement**; use **`BUCKContainerDescriptor`**, **`BUCKLocalLayerContainerDescriptor`**, or list **`ForegroundComponents`** per Eugen guidance. |

---

## Error categorization

All logged fatals share the same pattern:

```text
Invalid property in object '<anonymous> (TBUCKListDescriptor)':
A '{horizontal|vertical}' list doesn't allow its children to manage their '{x|y}' axis.
Component index N (ElementName '…', UniqueName '…') … field '{AlignementToFather|AlignementToAnchor|MagnifiableOffset}'.
```

| Category | Present in log? | Notes |
|----------|-----------------|-------|
| Unknown / renamed NDF properties | No | — |
| Removed descriptor classes | No | — |
| List main-axis validation (new at generation) | **Yes** | Only breaking category observed |
| Missing file name in error | **Yes** | Workaround: map `ElementName` / `UniqueName` → editor NDF path via `src/editors.py` |

### Primary axis mapping

| List `Axis` | Main axis | Forbidden on **list element children** (index 0 of vec2) |
|-------------|-----------|-----------------------------------------------------------|
| `~/ListAxis/Horizontal` (0) | **x** | Non-default `AlignementToFather[0]`, `AlignementToAnchor[0]`, `MagnifiableOffset[0]` |
| `~/ListAxis/Vertical` (1) | **y** | Same for index **1** |

**Secondary axis** (cross-axis alignment and offsets) remains valid on list children unless other rules apply.

**List’s own `ComponentFrame`** is not a child of itself — offsets on `UpperLabel`, `PointsCommandement`, etc. are still allowed on the **list root** when the list is positioned inside a parent **container**.

---

## Confirmed errors → mod code → fix

| Source NDF (from log / UniqueName) | Editor | Violation | Mod behavior today |
|-----------------------------------|--------|-----------|-------------------|
| `UIInGameResources.ndf` | `ingame.py` | Horizontal list child `SpecificInGameHUDTimePanelViewMainContainer`: `AlignementToFather` **x** | Inserts new top `BUCKListDescriptor` with time panel at `[0.5, 0.0]`; also patches vertical HUD column children with **y** offsets |
| (same) | `ingame.py` | Vertical column: `UISpecificMiniMapInfoViewMainContainer`, `UICommonBeaconPanelViewMainContainer`, `SpecificInGameHUDScoreViewMainContainer` — **y** on `MagnifiableOffset` / `AlignementToFather` | `MagnifiableOffset = [0.0, 10.0]`, `AlignementToFather = [0.1688, …]` |
| `UISpecificUnitLabelViewNameOnly.ndf` | `name_only.py` | `UpperLabel` vertical list: children `UnitNameAndRightListNameOnly`, `CarriedUnitNameList` — **y** `MagnifiableOffset` | Overlays HP/morale via offsets; inserts `UnitLabelUnitIconNameOnly` element |
| `UISpecificUnitLabelView.ndf` | `view.py` | `UpperLabel` child `UnitIcon` — **y** `MagnifiableOffset` | Similar overlay pattern on full label view |
| `UISpecificSkirmishProductionMenuView.ndf` | `production_menu.py` | `PointsCommandement` horizontal: `CommandPoints`, `CommmandPointsIncomeText` — **x** `AlignementToAnchor` | Sets `[4.0, 0.5]` and `[-0.25, 0.5]` (vanilla uses **0.0** on x — may pass; mod values trigger check) |
| `UISpecificShowroomDeckCreatorScreenComponent.ndf` | `deck_creator.py` | Horizontal top bar child `AffichageNomDuDeck` — **x** `AlignementToFather` | Sets `[-0.10, 0.5]` on deck name block |

**Note:** Vanilla VIP already uses list children with **0.0** on the main axis in places (e.g. `PointsCommandement` textures). The check targets **non-default / explicit main-axis control**, not merely presence of the property.

### Likely additional failures (not in short log)

These files use the same patterns and will fail on VIP once earlier errors are fixed:

| File | Risk |
|------|------|
| `showroom/armory.py` | `FiltersPanelList` is **vertical** — child `AlignementToFather = [0.5, 0.025]` sets **y** |
| `showroom/deck_creator.py` | `DeckEditorSaveAndCoButtons` `AlignementToFather/Anchor = [0.90, 0.5]` inside horizontal top bar |
| `ingame/launch_button.py`, `cube_action.py`, `offmap_airplane.py` | List or nested list alignment edits |
| `common/views/unit_button.py`, `common/views/chat.py` | Nested `BUCKListDescriptor` frames |
| `hud/selection_panel/*`, `hud/replay.py`, `outgame/login.py`, etc. | Any `Elements` child frame edits — audit required |

---

## VIP vs live diff (evidence)

| Path | Live vs VIP |
|------|-------------|
| `CommonData/UserInterface/Use/Common/Templates/BUCKListDescriptorTemplate.ndf` | **No diff** |
| `CommonData/UserInterface/Use/Common/Templates/BUCKListElementSpacerTemplate.ndf` | Not compared line-by-line; spacer API unchanged in log |
| `GameData/UserInterface/Use/InGame/UIInGameResources.ndf` | Layout differs (VIP adds vertical HUD stack); **same list rules apply** |
| Engine / `Components.ndfbin` | Validation enforced at **generation** in VIP only (per [EUG] Asfal) |

**Conclusion:** Treat VIP **templates + enums** as authoritative for *what you may write*; treat VIP **generation** as authoritative for *what will compile*.

---

## [EUG] guidance (from error log)

**Asfal (2026-05-14 / follow-up):**

1. Lists own placement along their **main axis** — children must not fight the list on that axis.
2. **Padding:** `BUCKListElementSpacer`, `FirstMargin` / `InterItemMargin` / `LastMargin` on the list.
3. **Left/right in one row:** `ExtendWeight = 1.0` on a spacer element between left- and right-aligned groups.
4. **Overlap / free layout:** use **`BUCKContainerDescriptor`** (or layers), not vertical/horizontal lists.
5. **Stack on top of a list:** `ForegroundComponents` on `BUCKListDescriptor`.
6. **Negative spacer overlap:** not confirmed — ask EUG before relying on it.
7. **Better errors / hot reload:** may improve later; do not block migration on this.

**Gustavitch:** More NDF validation is intentional; fixes improve long-term stability.

---

## Architectural migration patterns

### Pattern A — HUD column spacing (minimap / beacon / score)

**VIP rule scope:** generation checks **direct list slots** — each `BUCKListElementDescriptor`’s **`ComponentDescriptor.ComponentFrame`**. That frame is laid out by the parent `BUCKListDescriptor` on its main axis; **y** offsets/alignments on a **vertical** list slot fail (see `UI_generation_errors.txt`: `UISpecificMiniMapInfoViewMainContainer` + `MagnifiableOffset[1]`). A nested `BUCKContainerDescriptor` inside `ComponentDescriptor.Components` is **not** a list slot and is outside this check.

**Do not** put main-axis offsets on the list slot frame. **`BUCKListElementDescriptor` itself has `Components = []`** in the template (“Ne pas utiliser l'attribut Components !!! Utiliser ComponentDescriptor !!!”). Put widgets in **`ComponentDescriptor`** (a `BUCKContainerDescriptor`), which **may** have `Components = [ … ]` (vanilla example: `UISpecificOutGameFriendListView.ndf` invite button).

**Before (mod today — fails VIP):** `ingame.py` patches the vertical HUD column and sets y-axis properties on the **list slot** container frame:

```python
# src/ui_mods/style/ingame/ingame.py — vertical stack Elements loop
elif unique_name == '"UISpecificMiniMapInfoViewMainContainer"':
    component_descriptor.by_m("ComponentFrame").v.add("MagnifiableOffset = [0.0, 10.0]")
elif unique_name == '"UICommonBeaconPanelViewMainContainer"':
    component_descriptor.by_m("ComponentFrame").v.add("AlignementToFather = [0.1688, 0.3]")
elif unique_name == '"SpecificInGameHUDScoreViewMainContainer"':
    frame.add("AlignementToFather = [0.1688, 0.0]")
    frame.add("MagnifiableOffset = [0.0, 10.0]")
```

Vanilla VIP leaves those slot frames list-compliant (`RelativeWidthHeight = [1.0, 0.0]` only). The minimap **view content** is not inline in `UIInGameResources.ndf`; `UISpecificMiniMapInfoView.ndf` binds `BUCKSpecificMiniMapInfoMainComponentDescriptor` (children: `PanelRoundedCorner`, `~/MinimapPanelDescriptor`, `UISpecificHUDAlertPanelMainContainer`) into `MainComponentContainerUniqueName = "UISpecificMiniMapInfoViewMainContainer"`.

**After — prefer list-level spacing:**

```ndf
BUCKListDescriptor
(
    Axis = ~/ListAxis/Vertical
    InterItemMargin = TRTTILength( Magnifiable = 4.0 )   // increase for global column gap
    // or BUCKListElementSpacer( Magnifiable = 10.0 ) before the minimap element
    Elements = [ /* … */ ]
)
```

**After — when you need per-item y nudge and margins are not enough:** list-compliant **outer shell** + **inner** container with the offset (keep `UniqueName` on the inner node for view binding):

```ndf
BUCKListElementDescriptor
(
    ComponentDescriptor = BUCKContainerDescriptor
    (
        ComponentFrame = TUIFramePropertyRTTI ( RelativeWidthHeight = [1.0, 0.0] )
        FitStyle = ~/ContainerFitStyle/FitToContentVertically
        Components =
        [
            BUCKContainerDescriptor
            (
                UniqueName = "UISpecificMiniMapInfoViewMainContainer"
                ComponentFrame = TUIFramePropertyRTTI
                (
                    RelativeWidthHeight = [1.0, 0.0]
                    MagnifiableOffset = [0.0, 10.0]   // OK here: nested inside slot, not the slot frame
                )
                FitStyle = ~/ContainerFitStyle/FitToContentVertically
            )
        ]
    )
)
```

Cross-axis tweaks on the **slot** frame (e.g. beacon/score `AlignementToFather[0] = 0.1688` with `RelativeWidthHeight[0] = 0.8312`) remain valid on a vertical list.

### Pattern B — Replace list with layer container (name-only HP/morale overlay)

**Before:** `UpperLabelNameOnly` = vertical `BUCKListDescriptor` + per-element y offsets + zero-size icon trick.

**After:**

```ndf
private UpperLabelNameOnly is BUCKLocalLayerContainerDescriptor
(
    ElementName = "UpperLabel"
    NbLayersToLock = 6   // match max LocalRenderLayer in children
    ComponentFrame = TUIFramePropertyRTTI ( /* list-level frame only */ )
    Components =
    [
        ~/UnitNameAndRightListNameOnly,
        /* Morale/HP as siblings with absolute-style frames, or */
    ]
)
```

Or keep a **minimal vertical list** for true stack layout (name, carried units) and put **gauges + icon overlay** in `ForegroundComponents` on that list.

### Pattern C — Horizontal bar: `ExtendWeight` instead of x-alignment

For deck creator top bar (`DeckEditorTopBar` horizontal list):

- Remove `AlignementToFather = [-0.10, 0.5]` from `AffichageNomDuDeck` element.
- Use existing vanilla pattern: left block `ExtendWeight = 1.0`, center deck name, right `DeckEditorTopBarRightContent` with `ExtendWeight = 1.0`.
- Apply visual nudge via **`FirstMargin` / `InterItemMargin`** on the horizontal list, or an inner **container** inside the list element.

### Pattern D — Production menu command points

For `PointsCommandement` children:

- Remove `AlignementToAnchor` x overrides on texture/text (`[4.0, 0.5]`, `[-0.25, 0.5]`).
- Use `InterItemMargin`, `FirstMargin`/`LastMargin`, or wrap icon+text in a **horizontal micro-container** (itself one list element) where internal alignment is free.

### Pattern E — `UIInGameResources` top bar refactor

Current mod **removes** vanilla time panel from vertical stack and **reinserts** horizontal top list with centered time panel (`AlignementToFather/Anchor` x = 0.5) — direct conflict.

**Plan:**

1. Reconcile with VIP vanilla layout in `sourcemod vip/.../UIInGameResources.ndf` (vertical HUD column still exists).
2. Implement M81 top bar using **`BUCKContainerDescriptor`** overlay on `ForegroundComponents` of `InGameMainContainerResource`, not a competing horizontal list child with x-alignment.
3. Keep vertical stack children **list-compliant** (no y-offset on element frames); adjust **`InterItemMargin`** on the vertical list or outer container offset only.

---

## Phased implementation plan

### Phase 0 — Tooling and baseline (1–2 days)

1. Set `directories.base_game: "sourcemod vip"` in `config/config.YAML` (already used for VIP UI builds).
2. Add a repo script (suggested: `tools/audit_ui_list_axis.py`) that:
   - Parses generated/patched NDF under the UI mod output path, **or**
   - Statically scans `src/ui_mods/**/*.py` for `Alignement*` / `MagnifiableOffset` edits inside functions that touch `.by_member("Elements")`.
3. Build **ElementName → NDF path** index from `src/editors.py` `get_editors()` map.
4. Capture **screenshots** per feature (name-only HP, top bar, production menu) on **live** build as regression reference.

### Phase 1 — Unblock generation (P0, known log errors)

| Order | File | Task |
|-------|------|------|
| 1 | `ingame.py` | Fix horizontal time panel + vertical HUD column violations |
| 2 | `name_only.py` | Restructure `UpperLabelNameOnly` overlay (Pattern B) |
| 3 | `view.py` | Align full label view with name-only approach |
| 4 | `production_menu.py` | Revert/adjust command point x-anchors |
| 5 | `deck_creator.py` | Fix `AffichageNomDuDeck` horizontal parent constraint |

**Exit criterion:** VIP UI mod generation completes without fatal `TBUCKListDescriptor` errors.

### Phase 2 — Proactive audit (P1)

Audit and fix remaining 8 `src/ui_mods` files + gameplay UI editors:

- `armory.py`, `launch_button.py`, `cube_action.py`, `offmap_airplane.py`
- `unit_button.py`, `chat.py`
- `selection_panel.py`, `weapon.py`, `replay.py`, `login.py`, `starting_information.py`, `beacons.py`, `common.py`

**Exit criterion:** audit script clean; smoke test all major screens.

### Phase 3 — Hardening (P2)

1. Document per-feature layout approach in module docstrings (link to `UI_descriptor_reference.md`).
2. Optional: helper `clear_main_axis_frame(component_frame, axis: Literal["x","y"])` in `src/utils/ui_frame_utils.py` to prevent regressions.
3. When EUG ships UI debug/hot reload, adopt for iteration.

---

## File-by-file change notes

### `src/ui_mods/style/ingame/ingame.py` — **P0**

- **Lines ~55–66:** Remove y-axis `MagnifiableOffset` from vertical stack **slot** frames (`UISpecificMiniMapInfoViewMainContainer`, `SpecificInGameHUDScoreViewMainContainer`); keep or rework cross-axis `AlignementToFather[0]` on beacon/score. Prefer `InterItemMargin` / spacer; else nested inner container (Pattern A).
- **Lines ~69–129:** Rebuild top bar without horizontal list children using x-centering; use container overlay or `ExtendWeight` layout.
- **Line ~38:** `SpecificLaunchBattleMainComponentDescriptor` `MagnifiableOffset` — OK if parent is **not** a list on y (verify parent type in VIP NDF).

### `src/ui_mods/style/ingame/hud/unit_label/name_only.py` — **P0**

- **`_update_unit_name_and_right_list` / `_update_upper_label`:** Major rewrite — layer container or foreground overlay.
- **`_add_carried_unit_frame`:** y-offset on list element — move into container.
- **`TMoraleGaugeDescriptor` `AlignementToAnchor`:** gauge may not be list child in new structure; place in container.

### `src/ui_mods/style/ingame/hud/unit_label/view.py` — **P0**

- **`_update_icon_and_right_label`:** y `MagnifiableOffset` on nested horizontal list frame.
- **`_update_upper_label`:** y offset on vertical list root frame (likely OK); child `UnitIcon` insert — same overlay model as name-only.

### `src/ui_mods/style/ingame/hud/production_menu.py` — **P0**

- **`_update_command_points_texture/text`:** Remove x `AlignementToAnchor` tweaks; use margins or inner container.
- **`_update_game_info_panel`:** `PanelInfoPartie` offset `[600.0, 4.0]` — verify parent is not list-main-axis on x.

### `src/ui_mods/style/showroom/deck_creator.py` — **P0**

- **`_update_deck_name_display`:** Remove `AlignementToFather = [-0.10, 0.5]` on `AffichageNomDuDeck` list root when it is horizontal list child; use `ExtendWeight` pattern from vanilla top bar.
- **`_update_save_buttons`:** `[0.90, 0.5]` x alignment — likely invalid in horizontal bar; use right `ExtendWeight` block.

### `src/ui_mods/style/showroom/armory.py` — **P1**

- **`_edit_filterspanellist`:** Vertical list children with `AlignementToFather` y ≠ 0.5 default — refactor scrolling containers.

### Other `src/ui_mods` — **P1/P2**

Apply audit script; fix any list `Elements` child with main-axis frame edits.

### `src/gameplay_mods/userinterface/`

- `uispecificoutgamewelcomeview.py`, `uispecificunitinfosingleweaponpanelview.py` — quick manual review (low hit count).

---

## Testing checklist

- [ ] VIP: `target: ui_only`, `base_game: sourcemod vip` — full mod **generation** succeeds (no `Components.ndfbin` fatal).
- [ ] In-game HUD: time panel, score, minimap info, beacon panel positions match live screenshots.
- [ ] Unit label: **full** and **name-only** — HP/morale overlay alignment at multiple reticle scales (`ReticleMagnifiableSize`).
- [ ] Skirmish production menu: command points icon/text alignment.
- [ ] Showroom: deck creator top bar, deck name, save buttons; armory filter racks + scrollbars.
- [ ] Outgame/login, chat offset, launch button, offmap panels (regression pass).
- [ ] Gameplay+UI combined build still runs editors that touch UI from gameplay target.

---

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Large visual regressions after structural refactor | Screenshot baseline per screen; change one feature branch at a time |
| Unknown additional violations in rarely used views | Phase 2 audit script + full generation loop |
| Eugen changes validation again before live release | Pin `sourcemod vip` snapshot; re-diff templates on each WARNO update |
| Negative spacer / overlap not supported | Use container/layer pattern; confirm with EUG if needed |

---

## Blockers / questions for user

1. **Negative `BUCKListElementSpacer`:** Needed for name-only overlap compression? Ask [EUG] Asfal — plan assumes **container/layer**, not negative spacers.
2. **VIP vs live gameplay split:** UI-only VIP build may still need gameplay constants from live — confirm your release pipeline (see `config.YAML` `gameplay_version` vs `base_game`).
3. **Scope:** Migrate only `warno-actual` repo UI editors, or also standalone Steam Workshop UI mod project (if separate)?
4. **Automation investment:** Approve a small `tools/audit_ui_list_axis.py` in repo (recommended) vs manual grep before each release.

---

## References

- Error log: [`docs/UI_generation_errors.txt`](UI_generation_errors.txt)
- Descriptor reference: [`docs/UI_descriptor_reference.md`](UI_descriptor_reference.md)
- Editor → NDF map: [`src/editors.py`](../src/editors.py) (`get_editors()`, UI section ~line 525+)
- VIP templates: `sourcemod vip/CommonData/UserInterface/Use/Common/Templates/`
- VIP enums: `sourcemod vip/CommonData/UserInterface/Use/UICommonEnum.ndf`
