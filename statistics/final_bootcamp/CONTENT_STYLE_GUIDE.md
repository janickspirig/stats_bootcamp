# Statistics Bootcamp — Content Style Guide (final_bootcamp)

Applies to: `statistics/final_bootcamp/**/*.md`

This document is the **single source of truth** for how student-facing pages in the Statistics Bootcamp should be structured.

Why this matters:
- Students (and student-like AI agents) should be able to **scan any page** and instantly know where to find: objectives, core concepts, examples, practice, takeaways.
- Automated tools should be able to **validate structure** and prevent “template drift”.

---

## How to run the linter

From the repo root:

```bash
python3 statistics/tools/lint_final_bootcamp.py
python3 statistics/tools/lint_final_bootcamp.py --strict
```

- Default mode prints a report but exits **0**.
- `--strict` fails the run (exit **1**) if required rules are violated.

---

## Page types (contract)

Pages are classified by **path + frontmatter**.

### 1) Bootcamp root pages

Location: `statistics/final_bootcamp/`
- `index.md`
- `learning_goals.md`
- `faq.md` (if present)

These are navigational / meta pages. Keep them scannable and link-heavy.

### 2) Start-here pages

Location: `statistics/final_bootcamp/00_start_here/*.md`

Orientation content. These should follow the same Notion styling rules, but section requirements are more flexible than concept lessons.

### 3) Module index pages

Location: `statistics/final_bootcamp/<NN_module_name>/index.md` where `<NN_...>` matches `01_...` to `13_...`.

Purpose: a module overview and a hub linking to its lesson pages.

### 4) Reference pages

Location: `statistics/final_bootcamp/reference/*.md`

Reference pages prioritize lookup speed; they may not follow the concept lesson template.

### 5) Exercise pages

Location: `statistics/final_bootcamp/exercises/*.md`

Exercise pages are practice aggregations; structure may differ from concept lessons.

### 6) Concept lessons (default learning pages)

Location: `statistics/final_bootcamp/<NN_module_name>/*.md` (excluding `index.md`)

Identification rule:
- Frontmatter `title` starts with **`I can`**, **`I know`**, or **`I understand`**
- and the file is not a module `index.md`

Concept lessons must follow one of the two templates below:
- `page_type: concept` (default)
- `page_type: drill` (explicit practice-first variant)

---

## Required frontmatter (all pages)

Every page must include YAML frontmatter at the top:

- `title`: string
- `category`: `"Statistics Bootcamp"`
- `module`: number (0–13)
- `order`: number

Optional:
- `page_type`: `concept` | `drill`

Notes:
- If `page_type` is absent, assume `concept`.
- `page_type` is only meaningful for concept lessons.

---

## Canonical H2 section names (do not invent new names)

To reduce scanning friction, H2 section names are standardized.

### Canonical H2s

- `Table of Contents`
- `Learning Objectives`
- `Key Concepts`
- `Worked Example`
- `Practice Problems`
- `Common Mistakes to Avoid`
- `Key Takeaways`
- `Navigation`

Rules:
- Use these exact phrases (emoji prefixes are allowed, e.g. `## 📑 Table of Contents`).
- Do **not** use synonyms like “Key Formula(s)” as a top-level H2; place such content under `Key Concepts` or as H3s.

---

## Global rules (all pages)

### 1) H1 must exist

Each page must have exactly one H1 title (starts with `# `).

### 2) H1 should match frontmatter title

The H1 should match `title` (minor punctuation differences are OK, but avoid drifting titles).

### 3) Navigation is required

Every page must end with:

- `## Navigation`
- at least one markdown link in that section

Recommended formats:
- Concept lessons: `[← Previous](prev.md) | [Module Index](index.md) | [Next →](next.md)`
- Module index pages: `[← Previous Module](../NN_prev/index.md) | [🏠 Home](../index.md) | [Next Module →](../NN_next/index.md)`

### 4) TOC rule (strongly recommended, enforced in strict mode)

If a page has **more than 3 H2 sections**, it must include:

- `## 📑 Table of Contents` near the top (after the intro callout)

### 5) Notion math safety

Notion markdown import is unreliable for inline math.

- Prefer block equations with `$$` on separate lines and blank lines around them.
- Avoid `$...$` and `\(...\)` inline math (allowed but flagged by the linter for review).

---

## Concept lesson templates

### Template A — `page_type: concept` (default)

Required H2 sections (in this order):
1. `Table of Contents` *(required if >3 H2 sections)*
2. `Learning Objectives` *(required)*
3. `Key Concepts` *(required)*
4. `Worked Example` *(required)*
5. `Practice Problems` *(required)*
6. `Common Mistakes to Avoid` *(recommended)*
7. `Key Takeaways` *(required)*
8. `Navigation` *(required, last)*

### Template B — `page_type: drill` (explicit practice-first page)

Use this for “workbook-style” pages whose primary goal is practice and pattern recognition.

Required H2 sections:
1. `Table of Contents` *(required if >3 H2 sections)*
2. `Learning Objectives` *(required)*
3. `Practice Problems` *(required; may contain a large “Problem Set”)*
4. `Key Takeaways` *(required)*
5. `Navigation` *(required, last)*

Recommended additions (optional):
- A short “How to approach” note at the top of `Practice Problems`
- A compact checklist of common decision rules


