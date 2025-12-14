# Image Specification — Statistics Bootcamp

This document is the **single source of truth** for all new images to be generated and integrated into the bootcamp.

## Generation Command

```bash
cd statistics/tools
python generate_images.py                    # Generate all images
python generate_images.py --only <filename>  # Generate a specific image
python generate_images.py --list             # List all image placeholders in markdown
```

---

## Image Specification Table

| Filename | Alt Text | Target Page | Insertion Point | Type |
|----------|----------|-------------|-----------------|------|
| `ci_repeated_samples_coverage.png` | Many confidence intervals from repeated samples showing 95% coverage | `08_estimation_confidence_intervals/point_vs_interval.md` | After "Confidence Level" section, right after the misconception callout | multi_interval |
| `t_vs_z_critical_values.png` | Comparison of t and z distributions showing wider t-distribution tails | `08_estimation_confidence_intervals/ci_mean.md` | After "When to Use z vs t" table | distribution_overlay |
| `ci_width_vs_n.png` | Margin of error decreasing as sample size increases | `08_estimation_confidence_intervals/sample_size.md` | In "Trade-offs" section | line_plot |
| `ci_for_proportion_normal_approx.png` | Normal approximation for sampling distribution of proportion | `08_estimation_confidence_intervals/ci_proportion.md` | After "Conditions for Validity" section | distribution_shading |
| `rejection_regions_left_right_two_tailed.png` | Rejection regions for left-tailed, right-tailed, and two-tailed tests | `09_hypothesis_testing_basics/testing_framework.md` | Just before Step 4 ("Make Decision") | three_panel |
| `p_value_shaded_area_one_two_tailed.png` | P-value as shaded area under the curve for one-tailed and two-tailed tests | `09_hypothesis_testing_basics/p_values.md` | After "Definition" and before "Decision Rule" | two_panel |
| `alpha_beta_power_overlap.png` | Type I error (alpha), Type II error (beta), and power shown on overlapping H0 and H1 distributions | `09_hypothesis_testing_basics/error_types.md` | After the decision table | distribution_overlap |
| `hypotheses_tail_direction_cheatsheet.png` | Cheatsheet mapping H1 direction to tail shading | `09_hypothesis_testing_basics/stating_hypotheses.md` | After section introducing one-/two-tailed alternatives | infographic |
| `z_test_rejection_region_example.png` | Z-test example showing test statistic location relative to critical value | `10_one_sample_tests/z_test_mean.md` | At end of worked example | single_distribution |
| `t_test_rejection_region_example.png` | T-test example showing test statistic location with heavier tails | `10_one_sample_tests/t_test_mean.md` | At end of worked example | single_distribution |
| `proportion_test_uses_p0_in_se.png` | Visual reminder that proportion tests use p0 (not p-hat) in SE | `10_one_sample_tests/z_test_proportion.md` | In "Common Mistakes" section | formula_highlight |
| `paired_vs_independent_design.png` | Comparison of paired vs independent sample designs | `11_two_sample_tests/index.md` | Early in module overview | infographic |
| `pooled_vs_welch_decision.png` | Decision flowchart for pooled vs Welch t-test | `11_two_sample_tests/independent_t_test.md` | Near "Key Takeaways" or after formulas | flowchart |
| `two_proportion_pooled_se_visual.png` | Visual showing pooled proportion used in SE under H0 | `11_two_sample_tests/two_proportion_test.md` | After "Common trap" about pooled proportion | formula_highlight |
| `chi_square_distribution_rejection_region.png` | Chi-square distribution with right-tail rejection region | `13_advanced_topics/chi_square.md` | After df definition + critical value step | single_distribution |
| `chi_square_expected_counts_pipeline.png` | Pipeline: Observed table → Expected table → (O-E)²/E | `13_advanced_topics/chi_square.md` | After expected frequency formula | infographic |
| `anova_between_within_intuition.png` | ANOVA intuition showing between-group vs within-group variation | `13_advanced_topics/anova.md` | After SSB/SSW definitions | scatter_groups |
| `f_distribution_rejection_region.png` | F-distribution with right-tail rejection region | `13_advanced_topics/anova.md` | Near "Decision" step | single_distribution |
| `mean_median_mode_outlier_hist.png` | Histogram with outlier showing mean pulled away from median | `02_descriptive_statistics/mean_median_mode.md` | After "Properties: Sensitive to outliers" | histogram |
| `ols_fit_and_residuals.png` | Scatter plot with fitted OLS line and residual segments | `12_regression_analysis/fitting_regression.md` | After OLS formula description | scatter_regression |

---

## Image Type Definitions

| Type | Description | Typical Size |
|------|-------------|--------------|
| `single_distribution` | Single distribution curve with shading/annotations | (10, 6) |
| `two_panel` | Side-by-side comparison (1×2 subplots) | (12, 5) |
| `three_panel` | Three distributions/scenarios (1×3 subplots) | (14, 4.5) |
| `distribution_overlay` | Multiple distributions on same axes | (10, 6) |
| `distribution_overlap` | Two distributions (H0/H1) with overlap showing α, β | (12, 7) |
| `multi_interval` | Multiple horizontal CI bars with vertical μ line | (10, 8) |
| `line_plot` | Simple line chart (e.g., SE vs n) | (10, 6) |
| `histogram` | Histogram with annotations | (10, 6) |
| `scatter_regression` | Scatter with fitted line and residuals | (10, 6) |
| `scatter_groups` | Grouped scatter showing between/within variation | (10, 6) |
| `infographic` | Conceptual diagram/flowchart | (12, 8) |
| `flowchart` | Decision tree/flowchart | (12, 8) |
| `formula_highlight` | Formula with visual emphasis on key parts | (10, 5) |

---

## Style Requirements (for consistency)

All new images must use the shared style system in `generate_images.py`:

1. **Colors**: Use `COLORS` dict (primary=#2563EB, accent=#059669, warning=#DC2626, etc.)
2. **Fonts**: Sans-serif (Helvetica Neue, Arial, DejaVu Sans), sizes per rcParams
3. **Axes**: Top/right spines off, clean look
4. **DPI**: 300
5. **Padding**: 0.15 (via `FIGURE_PADDING`)
6. **Titles**: Bold, 14-16pt
7. **Annotations**: Use arrows with arrowprops, text boxes where helpful
8. **Fills**: Alpha 0.2-0.4 for distribution fills

---

## Checklist Before Generating

- [ ] Function uses `COLORS` dict
- [ ] Uses `save_figure(fig, filename)` helper
- [ ] Figure size matches type definition
- [ ] Title is bold and descriptive
- [ ] Axes labels present and clear
- [ ] Legend has `frameon=True` if used
- [ ] No tiny fonts (minimum 9pt)

