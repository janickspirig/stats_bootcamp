---
title: "Feedback Action Items (Implementation Tracker)"
category: "Statistics Bootcamp"
module: 99
order: 99
---

# Feedback Action Items (Implementation Tracker)

This file tracks implementation work derived from:
- `statistics/final_bootcamp/feedback_students.md`

Constraint: **Keep bootcamp fully English** (no German terminology additions).

---

## Priority 1 (highest grade impact)

- [ ] **Standardize hypothesis testing** (5-step template everywhere)
  - [ ] Update `09_hypothesis_testing_basics/testing_framework.md` to be the single canonical template page.
  - [ ] Ensure every test page links back to the template and follows the same structure.
  - [ ] Add explicit decision-rule wording (“Reject H₀” / “Do not reject H₀”) and α vs α/2 reminders.
  - [ ] Add **β / power** worked examples in `09_hypothesis_testing_basics/error_types.md`.

- [ ] **Descriptive statistics: add missing Übungsblatt-style content**
  - [ ] Add **MAD (Mean Absolute Deviation)** coverage + table column `|xᵢ - x̄|` in `02_descriptive_statistics/variance_stddev.md`.
  - [ ] Add at least 1 frequency table problem to `exercises/exercise_1.md`.
  - [ ] Add MAD formula + (optional) computational shortcuts to `reference/formula_glossary.md`.

- [ ] **Regression: make it Übungsblatt-style**
  - [ ] Expand `12_regression_analysis/fitting_regression.md` with a raw-score (“Σxᵢ, Σyᵢ, Σxᵢyᵢ, Σxᵢ², …”) method + deviation method.
  - [ ] Add the link between correlation and regression slope: \( \hat{\\beta}_1 = r \\cdot (s_y / s_x) \).

---

## Priority 2 (high ROI)

- [ ] **Probability: add missing exam operations**
  - [ ] Add **odds**: Odds(A) = P(A) / P(A′) + drills in `04_probability_fundamentals/probability_rules.md`.
  - [ ] Add **set difference**: P(A \\ B) = P(A) − P(A ∩ B) + Venn-region guidance in `04_probability_fundamentals/probability_rules.md`.

- [ ] **Sampling/CI: remove common traps**
  - [ ] Add a strict SD vs SE vs σ/√n comparison table + mini-quiz in `07_sampling_distributions/standard_error.md`.
  - [ ] Add 3–4 fully worked sample-size problems (identify z, σ/E → substitute → compute → round up) in `08_estimation_confidence_intervals/sample_size.md`.

---

## Priority 3 (structure & repetition)

- [ ] Add lightweight standard blocks (where missing):
  - [ ] “Checklist: When to use / Assumptions / What to report”
  - [ ] “Common mistakes” (3–5 bullets) + link to `reference/common_mistakes.md`
  - [ ] One explicit “Business interpretation” sentence after calculations

- [ ] Expand **exercise drill density** to match Übungsblatt feel (target 8–10 problems per exercise):
  - [ ] `exercises/exercise_1.md`
  - [ ] `exercises/exercise_2.md`
  - [ ] `exercises/exercise_3a.md`
  - [ ] `exercises/exercise_3b.md`
  - [ ] `exercises/exercise_4.md`
  - [ ] `exercises/exercise_5.md`
  - [ ] `exercises/exercise_6.md`


