# Bootcamp Image Style Audit (45 images)

Scope: `statistics/final_bootcamp/images/*.png`

This audit focuses on **visual consistency** (typography, color semantics, layout patterns, callouts, legends, sizing) across the bootcamp image set and proposes concrete actions to standardize the “bootcamp look”.

## Executive summary (what to fix first)

- **Standardize canvas/aspect families**: current aspects range from **1.03 → 3.20** (median **1.52**). A small set of canonical figure sizes will make everything feel cohesive.
- **Fix low-res outliers**: at least one diagram is **much smaller** than the rest (`discrete_distribution_flowchart.png` at **990×961**).
- **Unify annotation primitives**: many images use different callout/box styles; some rely on Unicode symbols that render inconsistently.
- **Unify legend and title/subtitle conventions**: location + framing varies a lot; some titles are multi-line in inconsistent ways.

## Inventory (metadata)

Full inventory (dims/aspect + generator mapping): [`statistics/final_bootcamp/image_inventory.md`](statistics/final_bootcamp/image_inventory.md)

Key distribution:
- **Aspect ratio**: min **1.03**, median **1.52**, max **3.20**
- **Width (px)**: min **990**, median **2954**, max **4191**
- **Height (px)**: min **752**, median **1776**, max **3099**

### Outliers to prioritize

#### Very wide “banner” images (tend to feel like a different set)
- `skewness_types.png` (3.197)
- `rejection_regions_left_right_two_tailed.png` (2.959)
- `covariance_patterns.png` (2.880)
- `binomial_shapes.png` (2.671)
- `test_selection_flowchart.png` (2.543)

#### Low aspect / tall-ish images (fine, but should be in a defined family)
- `ci_repeated_samples_coverage.png` (1.152)
- `regression_diagnostics.png` (1.156)
- `clt_demonstration.png` (1.158)

#### Low resolution (must fix)
- `discrete_distribution_flowchart.png` (990×961)
- `test_selection_flowchart.png` (1912×752) is also noticeably smaller than the median width

## Style inconsistency clusters + concrete actions

### 1) Canvas size / aspect ratio is not standardized
**Symptoms**
- Mixed “wide banner” and “normal card” canvases in the same chapter.
- Some diagrams look cramped; others have excessive whitespace.

**Actions**
- Adopt **2–3 canonical aspect families** (see style guide proposal):
  - **Standard (3:2-ish)** for most plots/diagrams
  - **Wide (16:9-ish)** for multi-panel comparisons
  - **Tall (≈1.15)** only when needed (diagnostics/coverage)
- Convert “banner” plots (>2.5 aspect) to either:
  - **Wide** with larger height (improves readability), or
  - a **2×2 layout** instead of 1×3 if content allows

**Primary candidates**
- `skewness_types.png`, `rejection_regions_left_right_two_tailed.png`, `covariance_patterns.png`, `binomial_shapes.png`, `test_selection_flowchart.png`

### 2) Annotation/callout style varies across the set
**Symptoms**
- Some images use callout boxes with arrows (great).
- Others use free-floating text or different box styles.

**Actions**
- Standardize on **callout boxes with arrows** for explanations:
  - white fill, colored border, rounded corners, consistent padding
  - arrow thickness and curvature consistent
  - text alignment consistent (left-aligned multi-line)
- Define a small set of “semantic boxes”:
  - **Decision callout** (green border)
  - **Warning callout** (red border)
  - **Tip box/footer** (neutral gray)

**Primary candidates**
- Multi-panel plots that currently rely on inline text (e.g., `skewness_types.png`)
- Any plot with small bottom notes (convert to standard footer/tip)

### 3) Unicode/special character rendering issues
From the student review, there are multiple references to symbols rendering poorly (e.g. arrow symbols “→”, proportionality, etc.).

**Actions**
- Avoid Unicode arrows/symbols in text where possible.
- Prefer **vector primitives** (e.g. `FancyArrowPatch`, `ConnectionPatch`, custom check/X icons) and plain ASCII labels.
- For math, use consistent Matplotlib mathtext (e.g. `r"$\\hat{p}$"`), not copied Unicode variants.

**Primary candidates (from review)**
- Images with “missing arrow symbol” / “cut off text” notes in `image_review.md`

### 4) Legends and titles are inconsistent
**Symptoms**
- Legend positions vary (upper left/right), frames vary, some are absent.
- Titles/subtitles differ in capitalization and positioning.

**Actions**
- Adopt a convention:
  - **Title** always top centered (bold)
  - **Subtitle** optional, smaller, neutral gray (used for notes like “heavier tails than z”)
  - **Legend** default: upper-left with light frame; override only when it overlaps data
- For multi-panel: use one shared title and per-panel subtitles consistently.

### 5) “Footer” notes are inconsistent in size/placement
**Symptoms**
- Some footers are tiny and easy to miss (review mentions rule-of-thumb text being small).

**Actions**
- Standardize footers:
  - either a single-line neutral footer, or
  - a dedicated “Tip” rounded box centered at the bottom

**Primary candidates**
- `binomial_shapes.png`, `covariance_patterns.png` (footer text is small)

## Suggested standardized “Bootcamp style” (preview)

The recommended style is documented in:
- [`statistics/final_bootcamp/IMAGE_STYLE_GUIDE.md`](statistics/final_bootcamp/IMAGE_STYLE_GUIDE.md)

## Concrete next steps (implementation sequence)

1) **Create shared helpers** in `statistics/tools/generate_images.py` for title/subtitle, legend styling, callouts, and footers.
2) **Normalize canvas families**: update the worst aspect-ratio outliers first.
3) **Replace Unicode arrows/symbols** in affected images with vector primitives.
4) **Regenerate** images and do a quick “contact sheet” review for visual consistency.

The detailed refactor backlog (per image/function) is in:
- [`statistics/final_bootcamp/image_refactor_plan.md`](statistics/final_bootcamp/image_refactor_plan.md)


