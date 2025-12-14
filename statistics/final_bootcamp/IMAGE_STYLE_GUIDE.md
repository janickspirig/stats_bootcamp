# Statistics Bootcamp Image Style Guide

Applies to: `statistics/final_bootcamp/images/*.png` (generated via `statistics/tools/generate_images.py`)

This guide defines a **single “bootcamp style”** so images feel like one cohesive set, are easy to scan during exam prep, and remain maintainable to regenerate.

## Style principles

- **One message per image**: the viewer should know what to look at within 3 seconds.
- **Semantic color**: colors should *mean* something, not just decorate.
- **Prefer callouts** over dense text: explanations should be attached to the object they describe.
- **Avoid fragile typography**: do not rely on special Unicode symbols that render inconsistently.

## Tokens (single source of truth)

### Color palette
Canonical palette is the existing `COLORS` dict in `statistics/tools/generate_images.py`.

Semantic usage guidelines:
- **Blue (`primary` / `normal`)**: baseline/reference, “H₀ distribution”, normal curve
- **Red (`warning` / `negative`)**: rejection regions, “wrong”, Type I error, negative direction
- **Green (`accent` / `positive`)**: correct/decision confirmation, power/benefit, positive direction
- **Purple (`secondary`)**: secondary concept or alternate distribution (e.g., leptokurtic)
- **Gray (`neutral` / `dark` / `light`)**: axes, footers, neutral annotations

### Typography
Use the global `plt.rcParams` already defined in `generate_images.py`:
- **Title**: bold, single line, top-centered
- **Subtitle**: smaller, neutral gray, used for context (“df=15”, “two-tailed”, etc.)
- **Axis labels**: consistent size, sentence case
- **Callout text**: slightly smaller than axis labels; left-aligned
- **Footers**: smallest text, neutral gray

### Strokes and fills (defaults)
- **Primary curves/lines**: linewidth 3
- **Secondary lines (guides, dashed)**: linewidth 2, alpha 0.8
- **Shaded regions**: alpha 0.20–0.30
- **Borders on boxes**: linewidth 2
- **Arrows**: linewidth 2 with consistent arrowstyle (`->`)

## Canonical canvas families (standardization target)

To reduce “random” sizes and aspect ratios, prefer these families:

1) **Standard (3:2-ish)** — default
- Use for most single plots and diagrams.
- Target aspect: **1.40–1.70**

2) **Wide (16:9-ish)** — comparisons/multi-panel
- Use for 2–3 panels side-by-side.
- Target aspect: **1.75–2.10**

3) **Tall (diagnostics/coverage)** — only when necessary
- Use when vertical stacking is essential.
- Target aspect: **1.10–1.25**

Hard rule:
- Avoid “banner” canvases **> 2.5** unless there is no alternative (prefer re-layout).

## Layout patterns (templates)

### 1) SinglePlotWithCallouts (reference: `kurtosis_types.png`)
- Single main plot
- 2–4 callout boxes with arrows pointing to curves/regions
- Optional small bottom-right “Advanced Topic” tag

### 2) SinglePlotWithDecisionCallout (reference: `t_test_rejection_region_example.png`)
- One distribution curve
- Rejection region(s) shaded in red
- Test statistic line emphasized
- Decision callout box on right (“REJECT H₀” / “Do not reject H₀”)
- Interpretation footer at bottom

### 3) MultiPanelGrid
- Shared title at top
- Each panel has a short subtitle
- Legends either shared or identical style/position
- Consistent axes labeling policy across panels

### 4) Diagram/FlowchartCard
- Standard node shapes (rounded rectangles + diamonds)
- Consistent connector style (line width, arrowheads)
- Minimize whitespace; ensure readable font size at typical screen widths

### 5) VennWithFormulaFooter
- Two circles with consistent fill alpha
- Key formula in a standard “formula box”
- Optional numeric example in footer

## Annotation primitives (standard blocks)

### Callout box (preferred)
Use for explanations attached to a visual element.
- White fill, colored border, rounded corners
- Left-aligned text, 3–5 lines max
- Arrow points to the feature being explained

### Decision box
Use for final decision statements.
- Green border for positive confirmation; red border for rejection emphasis
- Use explicit phrasing: **REJECT H₀** / **Do not reject H₀**

### Tip/footer box
Use for rules of thumb and “what to remember”.
- Neutral gray border, light gray fill
- Centered at bottom or as a footer line

## What to avoid (common failure modes)

- **Unicode arrows/symbols** in text that may render as boxes or disappear (use vector arrows instead).
- **Tiny footer text**: if it matters, it must be readable.
- **Overlapping labels**: prefer repositioning + callouts over squeezing.
- **Inconsistent legends**: set a default and only override when necessary.

## Regeneration workflow

All images should be regenerable from:
- `python3 statistics/tools/generate_images.py` (all)
- `python3 statistics/tools/generate_images.py --only <filename>` (single)

Inventory audit helper:
- `python3 statistics/tools/audit_images.py --format md --out statistics/final_bootcamp/image_inventory.md`


