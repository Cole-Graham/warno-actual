# UI descriptor reference (WARNO VIP sourcemod)

Reference for **BUCK UI descriptor classes** used by Warno Actual UI mods. Source of truth: **`sourcemod vip/CommonData/UserInterface/Use/Common/Templates/`** (NDF templates → RTTI types like `TBUCKListDescriptor`). Enums: **`sourcemod vip/CommonData/UserInterface/Use/UICommonEnum.ndf`**.

`TUIFramePropertyRTTI` / `TRTTILength` are engine RTTI types (not defined in shipped templates); members below are taken from template comments, `BUCKContainerDescriptorTemplate.ndf`, and consistent vanilla usage.

---

## How templates map to types

| Template name | `is` type (NDF / generation) |
|---------------|------------------------------|
| `BUCKContainerDescriptor` | `TBUCKContainerDescriptor` |
| `BUCKListDescriptor` | `TBUCKListDescriptor` |
| `BUCKListElementDescriptor` | `TBUCKListElementDescriptor` |
| `BUCKListElementSpacer` | `BUCKListElementDescriptor` (spacer instance) |
| `BUCKTextDescriptor` | `BUCKCommonTextDescriptor` |
| `BUCKButtonDescriptor` | `TBUCKButtonDescriptor` |
| … | See [Template index](#template-index) |

In mod Python, you usually edit parsed objects whose `.type` matches the template name (e.g. `"BUCKListDescriptor"`).

---

## Shared base: `TBUCKContainerDescriptor`

**Template:** `BUCKContainerDescriptorTemplate.ndf`  
**Use:** General-purpose box; children in `Components`; free 2D positioning via `ComponentFrame`.

### Identification

| Member | Type | Required | Description |
|--------|------|----------|-------------|
| `ElementName` | string | optional | Local name for C++ lookup among siblings |
| `UniqueName` | string | optional | Global name via BUCK bank |
| `RequiredTags` | LIST&lt;string&gt; | optional | Instantiate only if tags active |
| `ForbiddenTags` | LIST&lt;string&gt; | optional | Skip if tag active |

### Layout & input

| Member | Type | Default | Description |
|--------|------|---------|-------------|
| `ComponentFrame` | `TUIFramePropertyRTTI` | **required** | Size and position (see below) |
| `MagnifierMultiplication` | float | `0.0` | Scale self + children (&gt; 0) |
| `GridAlign` | bool | `false` | Snap layout box to integer pixels |
| `FitStyle` | int (`ContainerFitStyle`) | `None` | Resize to children / parent |
| `ChildFitToContent` | bool | `false` | Which child drives fit |
| `ClipContent` | bool | `false` | Clip overflowing children |
| `IsClippable` | bool | `true` | Skip draw when fully clipped |
| `PointerEventsToAllow` | int | `None` | Mouse event filter |
| `HidePointerEvents` | bool | `false` | Block mouse hit area |

### Chrome

| Member | Type | Description |
|--------|------|-------------|
| `HasBackground` | bool | Draw background |
| `BackgroundBlockColorToken` | string | Color token |
| `HasBorder` | bool | Draw border |
| `BordersToDraw` | int (`TBorderSide`) | Left/top/right/bottom flags |
| `BorderThicknessToken` | string | |
| `BorderLineColorToken` | string | |
| `BackgroundLocalRenderLayer` | int | Z-order for background |
| `BorderLocalRenderLayer` | int | Z-order for border |
| `ComponentStateLocked` | bool | Ignore dynamic state updates |

### Tree

| Member | Type | Description |
|--------|------|-------------|
| `Components` | LIST&lt;TBUCKContainerDescriptor&gt; | Child widgets |
| `FitToMaximumSize` | — | Present on instance; `nil` in template |

**Constraints:** Use containers when you need **overlap** or **independent x/y placement**. Preferred replacement for “list + child offsets” hacks.

---

## `TUIFramePropertyRTTI` (frame / placement)

Attached as `ComponentFrame = TUIFramePropertyRTTI ( … )` on descriptors.

### Size (typical members)

| Member | Type | Description |
|--------|------|-------------|
| `RelativeWidthHeight` | vec2 | Size relative to parent (0–1) |
| `MagnifiableWidthHeight` | vec2 | Size × UI magnifier / resolution scale |
| `PixelWidthHeight` | vec2 | Fixed pixels (when used in vanilla) |

### Position / anchor

| Member | Type | Description |
|--------|------|-------------|
| `AlignementToFather` | vec2 | Anchor point on **parent** (0–1) |
| `AlignementToAnchor` | vec2 | Anchor point on **this** widget (0–1) |
| `MagnifiableOffset` | vec2 | Offset × magnifier |
| `RelativeOffset` | vec2 | Relative offset (when used) |
| `PixelOffset` | vec2 | Pixel offset (when used) |

**vec2 axis:** `[horizontal, vertical]` = **[x, y]**.

### VIP list rule (critical)

Generation validates **each `Elements` slot**: the **`ComponentDescriptor.ComponentFrame`** of a `BUCKListElementDescriptor`. That container is positioned by the list on the list’s **main axis**; do **not** set main-axis values on `AlignementToFather`, `AlignementToAnchor`, or `MagnifiableOffset` there.

- **Horizontal list (`Axis = Horizontal`):** no non-default **x** (index 0) on the slot frame.
- **Vertical list (`Axis = Vertical`):** no non-default **y** (index 1) on the slot frame.

**Not checked as list slots:** widgets nested inside `ComponentDescriptor.Components`, the list’s own `ComponentFrame`, `BackgroundComponents`, `ForegroundComponents`, or containers outside `Elements`.

Cross-axis values on slot frames remain valid (e.g. vertical list slot `AlignementToFather = [0.5, 0.0]` — **x** free; **y** forbidden).

---

## `TRTTILength` (margins & spacers)

Used for `FirstMargin`, `InterItemMargin`, `LastMargin`, spacer `MinSize`, text padding, etc.

```ndf
TRTTILength( Magnifiable = 4.0 )
TRTTILength( Pixel = 10.0 )
TRTTILength()   // empty / default
```

| Field | Description |
|-------|-------------|
| `Magnifiable` | Scaled length |
| `Pixel` | Fixed pixel length |

`TRTTILength4` — four sides (e.g. `TextPadding` on text).

---

## `TBUCKListDescriptor` / `BUCKListDescriptor`

**Template:** `BUCKListDescriptorTemplate.ndf`  
**Purpose:** 1D layout of children along **Axis**; **no overlap** along main axis (VIP generation enforces this).

### List-specific members

| Member | Type | Required | Description |
|--------|------|----------|-------------|
| `Axis` | int (`ListAxis`) | **yes** | `Horizontal` (0) or `Vertical` (1) |
| `BreadthComputationMode` | int | default `ComputeBreadthFromFrameProperty` | Secondary-axis sizing |
| `Elements` | LIST&lt;TBUCKListElementDescriptor&gt; | optional | Row/column items (**use this**, not `Components`) |
| `BackgroundComponents` | LIST&lt;container&gt; | optional | Behind items; primary-axis relative size allowed |
| `ForegroundComponents` | LIST&lt;container&gt; | optional | On top of items; use for **overlays** |
| `FirstMargin` | TRTTILength | optional | Before first element |
| `InterItemMargin` | TRTTILength | optional | Between elements |
| `LastMargin` | TRTTILength | optional | After last element |

### Inherited from container

`ElementName`, `UniqueName`, `ComponentFrame`, `FitStyle`, `ChildFitToContent`, backgrounds/borders, tags, etc.

### `Components` on lists

Template sets `Components = []` — **do not** put layout children in `Components`; use **`Elements`**.

### Layout recipes (EUG)

| Goal | Approach |
|------|----------|
| Space between items | `InterItemMargin` / `FirstMargin` / `LastMargin` |
| Push right group to end | `BUCKListElementDescriptor( ExtendWeight = 1.0, ComponentDescriptor = … )` between groups |
| Overlay on list | `ForegroundComponents = [ … ]` |
| Overlap / custom 2D | Parent **`BUCKContainerDescriptor`** or **`BUCKLocalLayerContainerDescriptor`**, not list offsets |

### Example (vanilla vertical HUD stack)

From `sourcemod vip/GameData/UserInterface/Use/InGame/UIInGameResources.ndf`:

```ndf
BUCKListDescriptor
(
    Axis = ~/ListAxis/Vertical
    InterItemMargin = TRTTILength( Magnifiable = 4.0 )
    Elements =
    [
        BUCKListElementDescriptor
        (
            ComponentDescriptor = BUCKContainerDescriptor
            (
                UniqueName = "SpecificInGameHUDTimePanelViewMainContainer"
                ComponentFrame = TUIFramePropertyRTTI ( RelativeWidthHeight = [1.0, 0.0] )
                FitStyle = ~/ContainerFitStyle/FitToContentVertically
            )
        ),
        // …
    ]
)
```

---

## `TBUCKListElementDescriptor` / `BUCKListElementDescriptor`

**Purpose:** One slot in a list.

| Member | Type | Description |
|--------|------|-------------|
| `ComponentDescriptor` | TBUCKContainerDescriptor | **Single** child widget |
| `MinSize` | TRTTILength | Minimum size along list primary axis |
| `ExtendWeight` | float | Share of remaining **primary-axis** space (&gt; 0) |

**Constraints (template comment):**

- **`BUCKListElementDescriptor.Components`** is forced to `[]` — do **not** put layout children there; use **`ComponentDescriptor`** (one `BUCKContainerDescriptor` per slot).
- That **`ComponentDescriptor` container may have `Components = [ … ]`** (e.g. `UISpecificOutGameFriendListView.ndf`: `Components = [boutonInviteFriend]` inside the slot’s `ComponentDescriptor`).
- Slot **`ComponentDescriptor.ComponentFrame`** must not set **primary-axis** alignment/offset (see VIP list rule above). Nested containers inside `ComponentDescriptor.Components` are not list slots.
- Slot frame must not set **primary-axis relative size** unless the element uses `ExtendWeight`.

---

## `BUCKListElementSpacer`

**Template:** `BUCKListElementSpacerTemplate.ndf`  
**Type:** `BUCKListElementDescriptor` with only `MinSize`.

```ndf
BUCKListElementSpacer( Magnifiable = 8.0 )
BUCKListElementSpacer( Pixel = 10.0 )
```

Adds fixed gap along list axis. **Negative values unconfirmed** — do not rely on for overlap.

---

## `TBUCKLocalLayerContainerDescriptor`

**Template:** `BUCKLocalLayerContainerDescriptorTemplate.ndf`  
**Purpose:** Stack children with `LocalRenderLayer` ordering.

| Member | Type | Required | Description |
|--------|------|----------|-------------|
| `NbLayersToLock` | int | **yes** | ≥ max child `LocalRenderLayer` |
| `Components` | LIST&lt;container&gt; | optional | Layered children |

**Use for:** unit label overlays (name + HP + morale), any “paint on top” HUD cluster.

**Example (vanilla):** `UnitLabelUnitBUCKComponentDescriptorNameOnly` in `UISpecificUnitLabelViewNameOnly.ndf` wraps `UpperLabel` + bottom components.

---

## `BUCKTextDescriptor` / `BUCKCommonTextDescriptor`

**Template:** `BUCKTextDescriptorTemplate.ndf`

### Text-specific (in addition to container frame)

| Member | Type | Description |
|--------|------|-------------|
| `ParagraphStyle` | `TParagraphStyle` | Alignment, line height, max lines |
| `TextStyle` | string | Style guide token |
| `TypefaceToken` | string | Font token |
| `TextDico` / `TextToken` | string | Localization |
| `TextSize` / `TextColor` | string | Style overrides |
| `HorizontalFitStyle` / `VerticalFitStyle` | int (`FitStyle`) | `UserDefined` = use `ComponentFrame` |
| `BigLineAction` | int | Overflow behavior |
| `ColorMode` | int | Text color vs context |
| `TextPadding` | TRTTILength4 | |
| `Hint` | TBUCKHintableAreaDescriptor | Tooltip |
| `Rotation` | int | Degrees |
| `TextFormatScript` | bank | Formatting script |
| `LocalRenderLayer` | int | Draw order (text template) |

---

## `TBUCKButtonDescriptor` / `BUCKButtonDescriptor`

**Template:** `BUCKButtonDescriptorTemplate.ndf`  
Extends sensitive area + container.

| Member | Type | Description |
|--------|------|-------------|
| `IsTogglable` | bool | Toggle button |
| `DefaultToggleValue` | bool | Initial toggle state |
| `CannotDeselect` | bool | Radio-like behavior |
| `RadioButtonManager` | object | Mutual exclusion group |
| `BackgroundTexture` / texture tokens | strings | Visual states (see full template) |
| `Components` | list | Child visuals (icons, text) |

`ComponentStateLocked` defaults **true** on buttons.

---

## `TBUCKTextureDescriptor` / `BUCKTextureDescriptor`

**Template:** `BUCKTextureDescriptorTemplate.ndf`

Common members: `TextureToken`, `TextureColorToken`, `ComponentFrame`, `Components` (hints), fit styles. Used for icons, command points, division icons.

---

## `TBUCKGaugeDescriptor` / gauge family

**Template:** `BUCKGaugeDescriptorTemplate.ndf`, `BUCKGaugeValueDescriptor`  
Used in score panels, morale/HP via specialized descriptors (`TMoraleGaugeDescriptor`, etc. in game NDF).

---

## Other container patterns

| Template | Type | Notes |
|----------|------|-------|
| `BUCKGridDescriptor` | grid layout | `ForegroundComponents`, cell descriptors |
| `BUCKRackDescriptor` | rack/tabs | |
| `BUCKScrollingContainerDescriptor` | scroll area | Scrollbar `ComponentFrame` separate from content |
| `BUCKMultiListDescriptor` | multiple columns | |
| `BUCKWithTabsDescriptor` | tabbed UI | |
| `BUCKDroppableContainerDescriptor` | drag-drop | |
| `BUCKAnimatedContainerDescriptor` | animations | |
| `BUCKGenericOffscreenContainerDescriptor` | offscreen render | |

For showroom/armory, mods often touch **`BUCKSpecificScrollingContainerDescriptor`** (game-specific subtype) inside list elements.

---

## Enums (`UICommonEnum.ndf`)

| Enum | Values (subset) |
|------|-----------------|
| `ListAxis` | `Horizontal` = 0, `Vertical` = 1 |
| `BreadthComputationMode` | `ComputeBreadthFromFrameProperty`, `ComputeBreadthFromLargestChild`, `ComputeBreadthFromLargestBetweenFatherAndChildren` |
| `FitStyle` | `UserDefined`, `FitToParent`, `FitToContent`, `MaxBetweenUserDefinedAndContent`, … |
| `BigLineAction` | `CutByDots`, `MultiLine`, … |
| `TBorderSide` | `Left`, `Right`, `Top`, `Bottom`, `All`, … |

`ContainerFitStyle` is referenced as `~/ContainerFitStyle/...` (defined elsewhere in UI constants).

---

## View / screen descriptors

Game screens (e.g. `UISpecificUnitLabelViewDescriptorNameOnly`) are **not** in Common templates; they live under `GameData/UserInterface/Use/` and point at `MainComponentDescriptor` / `MainComponentContainerUniqueName`.

When debugging generation errors:

1. Note `ElementName` / `UniqueName` from the error.
2. Find the namespace in the matching `UISpecific*.ndf`.
3. Map file path via [`src/editors.py`](../src/editors.py).

---

## Template index

All under `sourcemod vip/CommonData/UserInterface/Use/Common/Templates/`:

| File | Primary type |
|------|----------------|
| `BUCKContainerDescriptorTemplate.ndf` | `TBUCKContainerDescriptor` |
| `BUCKListDescriptorTemplate.ndf` | `TBUCKListDescriptor`, `TBUCKListElementDescriptor` |
| `BUCKListElementSpacerTemplate.ndf` | Spacer element |
| `BUCKLocalLayerContainerDescriptorTemplate.ndf` | `TBUCKLocalLayerContainerDescriptor` |
| `BUCKTextDescriptorTemplate.ndf` | `BUCKCommonTextDescriptor` |
| `BUCKCommonTextDescriptorTemplate.ndf` | common text base |
| `BUCKButtonDescriptorTemplate.ndf` | `TBUCKButtonDescriptor` |
| `BUCKTextureDescriptorTemplate.ndf` | texture |
| `BUCKGaugeDescriptorTemplate.ndf` | gauge |
| `BUCKCheckBoxDescriptorTemplate.ndf` | checkbox |
| `BUCKCheckBoxListDescriptorTemplate.ndf` | checkbox list |
| `BUCKEditableTextDescriptorTemplate.ndf` | editable text |
| `BUCKDropdownDescriptorTemplate.ndf` | dropdown |
| `BUCKGridDescriptorTemplate.ndf` | grid |
| `BUCKRackDescriptorTemplate.ndf` | rack |
| `BUCKTreeViewDescriptorTemplate.ndf` | tree |
| `BUCKScrollingContainerDescriptorTemplate.ndf` | scrolling |
| `BUCKMultiListDescriptorTemplate.ndf` | multi list |
| `BUCKWithTabsDescriptorTemplate.ndf` | tabs |
| `BUCKHintDescriptorTemplate.ndf` | hint |
| `BUCKHintableAreaDescriptorTemplate.ndf` | hintable area |
| `BUCKSensibleAreaDescriptorTemplate.ndf` | hit area |
| `BUCKVideoDescriptorTemplate.ndf` | video |
| `BUCKGradientDescriptorTemplate.ndf` | gradient |
| `BUCKPolygonDescriptorTemplate.ndf` | polygon |
| `BUCKTypingTextDescriptorTemplate.ndf` | typing effect |
| `BUCKTextureAnimationDescriptorTemplate.ndf` | texture anim |
| `BUCKChronoAnimatedTextureDescriptorTemplate.ndf` | chrono texture |
| `BUCKStateUpdaterDescriptorTemplate.ndf` | state updater |
| `BUCKDroppableContainerDescriptorTemplate.ndf` | droppable |
| `BUCKDraggableContainerDescriptorTemplate.ndf` | draggable |
| `BUCKAnimatedContainerDescriptorTemplate.ndf` | animated |
| `BUCKGenericOffscreenContainerDescriptorTemplate.ndf` | offscreen |

---

## Mod authoring checklist

1. Prefer **`Elements`** on lists, **`Components`** on containers.
2. If you need overlap → **container / local layer / `ForegroundComponents`**, not list child offsets on the main axis.
3. If you need gap → **margins or spacer**, not negative overlap (unless EUG confirms).
4. Edit **list’s** `ComponentFrame` for moving the whole row/column; edit **parent container** for 2D positioning.
5. After changes, generate against **`sourcemod vip`** before shipping.

---

## Related docs

- Migration plan: [`UI_vip_migration_plan.md`](UI_vip_migration_plan.md)
- Errors + Discord context: [`UI_generation_errors.txt`](UI_generation_errors.txt)
- Project conventions: [`../AGENTS.md`](../AGENTS.md)
