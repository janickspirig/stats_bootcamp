---
title: "Bootcamp Simulation Issues Report"
category: "Statistics Bootcamp"
module: 0
order: 99
---

# Bootcamp Simulation Issues Report

This report lists issues found while simulating the bootcamp experience as three student personas (Full Review / Focused Review / Cram).  
It includes **recommended fixes only** (no changes are applied automatically based on this report).

---

## Executive Summary

- The bootcamp content is generally coherent and navigable.
- New content is discoverable via module indexes (notably Module 09 β/power pages and Module 02 frequency tables).
- The main gaps are **checklist alignment** and a few **reference/exercise index** presentation details.

---

## Issues Found

### 1) Learning Goals Checklist missing new pages

- **Where**: `statistics/final_bootcamp/learning_goals.md`
- **Issue**: The checklist does not include newly added pages:
  - Module 02: `02_descriptive_statistics/frequency_tables.md`
  - Module 04: `04_probability_fundamentals/odds_ratio.md`
  - Module 09: `09_hypothesis_testing_basics/type_ii_error.md`, `09_hypothesis_testing_basics/power_analysis.md`
- **Impact**: Students using the checklist as their primary “what to master” tool won’t see these items, reducing discoverability and systematic studying.
- **Recommended fix**:
  - Add new checklist entries under the corresponding modules in `learning_goals.md`.

---

### 2) Reference “Cheat Sheets” link points to a directory (may not render as expected)

- **Where**: `statistics/final_bootcamp/reference/index.md`
- **Issue**: The page links to `cheat_sheets/` as if it were a file. Depending on the markdown renderer, directory links may not work.
- **Impact**: Students may click “Cheat Sheets” and land on a broken link / blank page.
- **Recommended fix (choose one)**:
  - Option A: Add a `statistics/final_bootcamp/reference/cheat_sheets/index.md` with links to the three cheat sheets.
  - Option B: Remove the directory link and only keep the three direct links.

---

### 3) Exercises index “Pages” column is now stale after exercise expansion

- **Where**: `statistics/final_bootcamp/exercises/index.md`
- **Issue**: The “Pages” numbers appear static and are likely outdated after adding many more problems. The new `Integration Exercise` row has the pages cell empty.
- **Impact**: Students may underestimate how long exercises take.
- **Recommended fix**:
  - Either remove the “Pages” column entirely, or update it to a time estimate instead (e.g., “~45–60 min”).

---

## Persona Notes (high level)

### Persona A (Full Review, 16+ hours)

- **Strength**: Module indexes expose the new pages well (Module 02 frequency tables; Module 09 β/power).
- **Issue surfaced**: Checklist alignment (see Issue #1).

### Persona B (Focused Review, 8–10 hours)

- **Strength**: Plan B in `00_start_here/study_path.md` clearly prioritizes Modules 08–11.
- **Note**: The “Ready to Start (8–10 hours)” entry points to Module 05; this is not wrong, but can feel inconsistent with the “Priority Modules” list (08–11).
- **Recommended fix (optional)**: Add a short note clarifying that Plan B can start at Module 05 for distributions refresh, or jump directly to Module 08 if distributions are already solid.

### Persona C (Cram, 4–6 hours)

- **Strength**: “Revision sprint (10 minutes)” in `statistics/final_bootcamp/index.md` has clear drill links.

---

## Suggested Fix Order (if you choose to implement later)

1. Update `learning_goals.md` to include newly added pages (highest student impact).
2. Add `reference/cheat_sheets/index.md` or remove the directory link.
3. Refresh `exercises/index.md` metadata (pages/time).


