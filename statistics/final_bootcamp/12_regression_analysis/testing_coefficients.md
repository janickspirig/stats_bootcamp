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


