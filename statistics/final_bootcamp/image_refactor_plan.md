# Image Refactor Plan (Generator-level)

Scope: bring all images in `statistics/final_bootcamp/images/` closer to the “bootcamp style” defined in:
- [`statistics/final_bootcamp/IMAGE_STYLE_GUIDE.md`](statistics/final_bootcamp/IMAGE_STYLE_GUIDE.md)

Implementation location:
- [`statistics/tools/generate_images.py`](statistics/tools/generate_images.py)

This is a **concrete backlog**: which helpers to add, and which generator functions to adjust first.

## Phase A — Add shared style helpers (foundation)

Add these small helpers near the top of `generate_images.py` (after `save_figure`), then migrate generators incrementally:

- **`add_title(ax_or_fig, title, subtitle=None)`**
  - Standardizes title placement and subtitle styling.
- **`style_axes(ax, *, x_label=None, y_label=None, hide_y_ticks=True, hide_top_right=True)`**
  - Standardizes spines, tick sizes, label sizes, and common axis defaults.
- **`style_legend(ax, *, loc="upper left", frame=True)`**
  - Standardizes legend frame/padding/font.
- **`add_footer(fig, text, *, style="line"|"tip")`**
  - Standardizes rule-of-thumb/interpretation display.
- **`add_callout(ax, text, xy, xytext, color, *, rad=0.1, box_kind="callout"|"decision"|"warning")`**
  - Standardizes callout box + arrow props.
- **`avoid_unicode_symbols(text)`** (optional utility)
  - Replace problematic Unicode arrows/symbols with ASCII equivalents before rendering.

Why this first:
- It makes subsequent changes mechanical and consistent across 45 generators.

## Phase B — Normalize canvas families (biggest “cohesion win”)

Goal: reduce aspect ratio extremes and make the set feel uniform.

### B1) Convert “banner” images (>2.5 aspect) to canonical families
From the inventory (`image_inventory.md`):

- `generate_skewness_types` → `skewness_types.png` (aspect 3.197)
  - Increase height (avoid thin banner), or move from 1×3 to 2×2/stacked layout.
  - Replace inline “Tail -->” text with standardized callouts.

- `generate_rejection_regions` → `rejection_regions_left_right_two_tailed.png` (2.959)
  - Increase height and unify panel spacing.
  - Standardize per-panel subtitles and legend style.

- `generate_covariance_patterns` → `covariance_patterns.png` (2.880)
  - Increase height; move the small formula into a standard footer box.

- `generate_binomial_shapes` → `binomial_shapes.png` (2.671)
  - Increase height; ensure the “rule of thumb” footer is readable and standardized.

- `generate_test_selection_flowchart` → `test_selection_flowchart.png` (2.543)
  - Reduce excessive whitespace; increase font size; align connectors.

### B2) Fix low-res outliers
- `generate_discrete_distribution_flowchart` → `discrete_distribution_flowchart.png` (990×961)
  - Ensure it uses the same DPI/output settings and a larger figsize so it matches the set.

## Phase C — Fix known rendering/typography issues (quality)

Student review notes (from `statistics/final_bootcamp/image_review.md`) mention symbol rendering issues and occasional cutoffs/overlaps.

Concrete changes:
- Replace text-based arrows (“→”) in labels with **vector arrows** (`FancyArrowPatch`) or remove them.
- Replace special symbols that render as boxes (e.g. proportionality) with mathtext.
- For any “cut off” text: increase padding / use `bbox_inches="tight"` (already used) + avoid placing important labels near edges.

## Phase D — Standardize annotation/decision language across hypothesis testing plots

Hypothesis testing images should share:
- red rejection shading
- green decision callout when concluding
- consistent “Reject H₀ / Do not reject H₀” phrasing
- consistent α vs α/2 labeling

Prioritized hypothesis set:
- `generate_t_test_rejection_example` → `t_test_rejection_region_example.png`
- `generate_z_test_rejection_example` → `z_test_rejection_region_example.png`
- `generate_p_value_shaded` → `p_value_shaded_area_one_two_tailed.png`
- `generate_alpha_beta_power` → `alpha_beta_power_overlap.png`
- `generate_hypotheses_tail_direction` → `hypotheses_tail_direction_cheatsheet.png`

## Phase E — Diagrams/flowcharts standardization

Diagrams should share:
- node styling (rounded rectangles/diamonds)
- connector thickness and arrowheads
- consistent text sizes (readable at typical Notion width)

Priority:
- `generate_test_selection_flowchart`
- `generate_data_types_tree`
- `generate_module_progression`
- `generate_pooled_vs_welch`
- `generate_chi_square_expected_pipeline`

## Phase F — Add (optional) automated checks to prevent regression

You already have:
- `statistics/tools/audit_images.py` to produce `image_inventory.md`

Recommended additions (optional):
- A “contact sheet” generator to visually compare all images at once.
- A simple rule-based check:
  - flag aspect > 2.5
  - flag width < 2000 or height < 1200
  - flag non-regenerated files (if any) not in `GENERATORS`

## Definition of done (for the refactor execution phase)

After implementing the backlog above:
- All images fall into one of the canonical canvas families (Standard/Wide/Tall).
- No images use fragile Unicode arrows/symbols in key labels.
- Legends/titles/callouts/footers are visually consistent across the set.
- `audit_images.py` output shows no major outliers in resolution/aspect.


