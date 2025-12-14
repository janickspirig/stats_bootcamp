# Statistics Bootcamp - Notion Page Tree Structure

> This document describes the hierarchical page structure for implementing the Statistics Bootcamp in Notion. It is designed for self-paced exam preparation with logical progression, easy navigation, and quick reference access.

---

## Design Principles

1. **3-Level Hierarchy**: Root > Module > Topic pages (Notion works best with shallow hierarchies)
2. **Learning-Objective Titles**: Content pages named as "I can..." or "I know..." statements for clear learning goals
3. **Navigation Aids**: Dedicated Reference section at root level for quick formula/test lookup
4. **Progressive Flow**: Modules ordered by dependency; each module builds on previous concepts

---

## Complete Page Tree

```
Statistics Bootcamp (ROOT)
│
├── 00 Start Here
│   ├── Welcome & How to Use This Bootcamp
│   ├── Prerequisites & Self-Assessment
│   └── Suggested Study Path
│
├── 01 Foundations
│   ├── I know the different types of data and their characteristics
│   └── I can identify and distinguish scales of measurement
│
├── 02 Descriptive Statistics [Exercise 1]
│   ├── I can calculate and interpret the mean, median, and mode
│   ├── I can calculate variance and standard deviation
│   ├── I can interpret quartiles and box plots
│   └── I can identify skewness and kurtosis
│
├── 03 Correlation and Covariance
│   ├── I can calculate and interpret correlation coefficients
│   ├── I can calculate and interpret covariance
│   └── I understand the difference between correlation and causation
│
├── 04 Probability Fundamentals [Exercise 2]
│   ├── I know the basic terms and concepts of probability
│   ├── I can apply the axioms of probability (Kolmogorov)
│   ├── I can calculate conditional probabilities
│   ├── I can use addition and multiplication rules
│   └── I can construct and interpret tree diagrams
│
├── 05 Discrete Distributions [Exercise 3A]
│   ├── I understand discrete random variables
│   ├── I can calculate expected value and variance
│   ├── I can apply the binomial distribution
│   ├── I can apply the Poisson distribution
│   └── I can apply the hypergeometric distribution
│
├── 06 Continuous Distributions [Exercise 3B]
│   ├── I understand continuous random variables and density functions
│   ├── I can work with the normal distribution
│   ├── I can standardize using z-scores
│   └── I can apply the exponential distribution
│
├── 07 Sampling Distributions [Exercise 4]
│   ├── I understand sampling and population concepts
│   ├── I know what a sampling distribution is
│   ├── I can apply the Central Limit Theorem
│   └── I can calculate standard error
│
├── 08 Estimation and Confidence Intervals [Exercise 4]
│   ├── I understand point estimators and their properties
│   ├── I can construct confidence intervals for means
│   ├── I can construct confidence intervals for proportions
│   └── I can determine appropriate sample sizes
│
├── 09 Hypothesis Testing Basics [Exercise 5]
│   ├── I can formulate null and alternative hypotheses
│   ├── I understand Type I and Type II errors
│   ├── I know the 5-step hypothesis testing procedure
│   └── I can conduct a z-test for means
│
├── 10 One-Sample Tests [Exercise 5]
│   ├── I can conduct a t-test for population means
│   ├── I can test hypotheses about proportions
│   └── I can calculate and interpret p-values
│
├── 11 Two-Sample Tests [Exercise 5]
│   ├── I can compare means of independent samples
│   ├── I can compare means of dependent samples (paired t-test)
│   ├── I can compare proportions across samples
│   └── I can test for equality of variances
│
├── 12 Regression Analysis [Exercise 6]
│   ├── I can fit a simple linear regression model
│   ├── I can interpret regression coefficients
│   ├── I can evaluate model fit using R-squared
│   └── I can conduct hypothesis tests on regression coefficients
│
├── 13 Advanced Topics [Exercise 6]
│   ├── I can conduct chi-square tests for independence
│   ├── I can conduct chi-square goodness-of-fit tests
│   ├── I can perform one-way ANOVA
│   └── I understand dummy variables and interactions
│
├── Reference
│   ├── Formula Glossary
│   ├── Distribution Summary Table
│   ├── Which Test Should I Use?
│   ├── Statistical Tables (z, t, χ², F)
│   └── Common Pitfalls & Mistakes
│
└── Exercises
    ├── Exercise 1: Descriptive Statistics (47 pages)
    ├── Exercise 2: Probability (75 pages)
    ├── Exercise 3A: Discrete Distributions (56 pages)
    ├── Exercise 3B: Continuous Distributions (25 pages)
    ├── Exercise 4: Sampling & Estimation (56 pages)
    ├── Exercise 5: Hypothesis Testing (55 pages)
    └── Exercise 6: Regression (21 pages)
```

---

## Module Progression (Learning Path)

The bootcamp follows the standard HSG lecture progression:

```
Foundations → Descriptive Stats → Correlation → Probability → Distributions → Inference → Regression
     ↓              ↓                 ↓              ↓             ↓              ↓           ↓
  (L1:I-II)     (L1:III-V)         (L2)          (L3)         (L4-L5)       (L6-L10)    (L11-L12)
```

| Module | Prerequisite Modules | Estimated Time |
|--------|---------------------|----------------|
| 01 Foundations | None | 30 min |
| 02 Descriptive Statistics | 01 | 90 min |
| 03 Correlation & Covariance | 02 | 60 min |
| 04 Probability Fundamentals | 01 | 90 min |
| 05 Discrete Distributions | 04 | 90 min |
| 06 Continuous Distributions | 05 | 90 min |
| 07 Sampling Distributions | 06 | 60 min |
| 08 Estimation & CI | 07 | 90 min |
| 09 Hypothesis Testing Basics | 08 | 90 min |
| 10 One-Sample Tests | 09 | 60 min |
| 11 Two-Sample Tests | 10 | 90 min |
| 12 Regression Analysis | 03, 10 | 90 min |
| 13 Advanced Topics | 10, 12 | 90 min |

**Total estimated time**: ~16 hours

---

## Reference Section Details

The Reference section provides quick-access resources critical for exam preparation:

### Formula Glossary
All formulas organized by topic with:
- Symbolic notation
- Variable definitions
- When to use

### Distribution Summary Table
| Distribution | Type | Parameters | When to Use |
|--------------|------|------------|-------------|
| Binomial | Discrete | n, p | Fixed trials, 2 outcomes |
| Poisson | Discrete | λ | Count in interval |
| Hypergeometric | Discrete | N, K, n | Sampling w/o replacement |
| Normal | Continuous | μ, σ | Natural phenomena, CLT |
| Exponential | Continuous | λ | Time between events |
| t | Continuous | df | Small samples, unknown σ |
| χ² | Continuous | df | Categorical data |
| F | Continuous | df₁, df₂ | Variance comparison, ANOVA |

### Which Test Should I Use?
Decision tree based on:
1. Type of data (categorical vs numerical)
2. Number of samples (1, 2, or more)
3. Sample relationship (independent vs dependent)
4. What you're testing (mean, proportion, variance)

### Statistical Tables
Standard lookup tables for:
- Standard normal (z) distribution
- Student's t distribution
- Chi-square distribution
- F distribution

### Common Pitfalls & Mistakes
Exam-focused warnings about:
- Forgetting to use n-1 for sample variance
- Confusing population vs sample notation
- One-tailed vs two-tailed test errors
- Misinterpreting p-values
- Correlation vs causation confusion

---

## Page Content Structure

Each topic page follows this template:

```markdown
# [Page Title - Learning Objective]

## Learning Objectives
After completing this section, you will be able to:
- Objective 1
- Objective 2

---

## Concept Review
[Theory with formulas in KaTeX]

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

---

## Worked Example
[Full step-by-step solution with calculation tables]

| Step | x_i | x_i - x̄ | (x_i - x̄)² |
|------|-----|---------|------------|
| 1    | 17  | -3.14   | 9.86       |
| ...  | ... | ...     | ...        |
| Σ    |     |         | 98.86      |

---

## Practice Problems

### Problem 1
[Problem statement]

<toggle: Solution>
[Detailed solution]
</toggle>

---

## Key Takeaways
- Summary point 1
- Summary point 2

---

## Navigation
← Previous: [Link] | Module Index | Next: [Link] →
Related Reference: [Formula Glossary]
```

---

## Exercise Mapping

| Exercise | Modules Covered | Pages |
|----------|-----------------|-------|
| Exercise 1 | 02 Descriptive Statistics | 47 |
| Exercise 2 | 04 Probability | 75 |
| Exercise 3A | 05 Discrete Distributions | 56 |
| Exercise 3B | 06 Continuous Distributions | 25 |
| Exercise 4 | 07 Sampling, 08 Estimation | 56 |
| Exercise 5 | 09-11 Hypothesis Testing | 55 |
| Exercise 6 | 12-13 Regression & Advanced | 21 |

**Total**: 7 exercises, 335 pages

---

## Statistics Summary

| Category | Count |
|----------|-------|
| Content Modules | 14 (incl. Start Here) |
| Content Pages | 48 |
| Reference Pages | 5 |
| Exercise Pages | 7 |
| **Total Pages** | **63** |

---

## Files

| File | Purpose |
|------|---------|
| `page_tree.json` | Machine-readable structure for AI agent implementation |
| `page_tree.md` | Human-readable documentation (this file) |

---

## Source References

This page tree is based on:
- `statistics/BOOTCAMP_PURPOSE.txt` - Bootcamp goals and pedagogical principles
- `statistics/extracted/curriculum/bootcamp_structure.json` - Module definitions from lectures
- `statistics/exercises/extracted/index.json` - Exercise sheet information
- `notion_tech_Restrictions.txt` - Notion platform capabilities
- `notion_export/CS_Bootcamp/` - Existing bootcamp page structure patterns

