---
title: "I can test regression coefficients"
category: "Statistics Bootcamp"
module: 12
order: 3
---

# I can test regression coefficients

> 📚 **Overview:** Hypothesis tests and confidence intervals for regression slopes.

Hypothesis tests for slope significance.

---

## Learning Objectives

After completing this section, you will be able to:
- Test if slope is significantly different from zero
- Construct confidence intervals for slope
- Interpret results

---

## Intuition (what you are actually testing)

In simple regression, the slope \(\\beta_1\) is the **average change in \(Y\)** for a **+1 change in \(X\)** (in the population).

This hypothesis test answers a specific question:

> “Do we have enough evidence (from this sample) that the true population slope is **not zero**?”

If you reject \(H_0: \\beta_1 = 0\), you are saying: “A linear association is likely present.” You are **not** automatically saying: “Changing \(X\) will cause \(Y\) to change.”

---

## When to use / when not to use

- **Use when**: you have a simple linear regression model and want to test whether the slope differs from 0.
- **Use when**: you need an exam-style conclusion about “significant relationship” between \(X\) and \(Y\).
- **Do not use when**: the relationship is clearly non-linear (the “slope” test can be misleading without appropriate terms/transformations).

---

## Practical vs statistical significance

- **Statistically significant** means “unlikely under \(H_0\)” (p-value small / test statistic extreme).
- **Practically significant** means “large enough to matter for a decision” (business impact).

A tiny slope can be statistically significant with large \(n\), but irrelevant in practice.

---

## Interpretation sentence templates (exam-ready)

- **Reject \(H_0\)**: “At α = [..], there is sufficient evidence that the slope differs from 0; \(X\) is statistically significantly associated with \(Y\) in a linear model.”
- **Do not reject \(H_0\)**: “At α = [..], there is not sufficient evidence that the slope differs from 0; we cannot conclude a linear association from this sample.”
- **Confidence interval**: “A [95%] CI for \(\\beta_1\) is [..]. If the interval includes 0, the slope is not significant at α = 0.05.”

---

## Common traps (high-frequency)

> ⚠️ **Trap 1: Writing causal conclusions.**
> Use “associated with” unless the design supports causality.

> ⚠️ **Trap 2: Forgetting units.**
> The slope is “units of \(Y\) per +1 unit of \(X\)”.

> ⚠️ **Trap 3: Wrong degrees of freedom.**
> For simple regression slope tests: df = \(n-2\).

> ⚠️ **Trap 4: Confusing ‘significant’ with ‘important’.**
> Always consider the size of \(\\hat\\beta_1\), not only the p-value.

---

## Key Formula

**Test Statistic:**

$$
t = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)}
$$

**Standard Error of Slope:**

$$
SE(\hat{\beta}_1) = \frac{s_e}{\sqrt{\sum(x_i-\bar{x})^2}}
$$

Where $s_e = \sqrt{\frac{SSE}{n-2}}$ (standard error of regression)

**Degrees of freedom:** df = n - 2

---

## Hypotheses

| Test | H₀ | H₁ |
|------|-----|-----|
| Is there a relationship? | β₁ = 0 | β₁ ≠ 0 |
| Is relationship positive? | β₁ ≤ 0 | β₁ > 0 |
| Is relationship negative? | β₁ ≥ 0 | β₁ < 0 |

---

## Worked Example

**Problem:**
From previous example: $\hat{\beta}_1$ = 1.7, SSE = 0.30, $\sum(x-\bar{x})^2$ = 10, n = 5

Test if the slope is significantly different from zero at α = 0.05.

**Solution:**

### Step 1: Hypotheses
- H₀: β₁ = 0
- H₁: β₁ ≠ 0

### Step 2: Calculate Standard Error

$$
s_e = \sqrt{\frac{0.30}{5-2}} = \sqrt{0.10} = 0.316
$$

$$
SE(\hat{\beta}_1) = \frac{0.316}{\sqrt{10}} = \frac{0.316}{3.16} = 0.10
$$

### Step 3: Test Statistic

$$
t = \frac{1.7}{0.10} = 17.0
$$

df = 3

### Step 4: Decision
t₀.₀₂₅,₃ = 3.182
|17.0| > 3.182 → Reject H₀

### Step 5: Conclusion
Strong evidence of a significant relationship between X and Y.

---

## Practice Problems

### Problem 1

Regression output shows:
- β̂₁ = 2.5
- SE(β̂₁) = 0.8
- n = 20

Test if slope differs from zero at α = 0.05.

<details>
<summary>💡 Show Solution</summary>

$$
t = \frac{2.5}{0.8} = 3.125
$$

df = 18, t₀.₀₂₅,₁₈ = 2.101

|3.125| > 2.101 → Reject H₀

Significant relationship exists.

</details>

---

## Confidence Interval for Slope

$$
\hat{\beta}_1 \pm t_{\alpha/2, n-2} \cdot SE(\hat{\beta}_1)
$$

If CI doesn't include 0, slope is significant.

---

## Key Takeaways

- Test β₁ = 0 to check if relationship exists
- t = slope / SE(slope)
- df = n - 2 for simple regression
- CI for slope provides range of plausible values

---

## Navigation

[← R-Squared](r_squared.md) | [Module Index](index.md) | [Next: Assumptions →](regression_assumptions.md)


