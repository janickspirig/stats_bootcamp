---
title: "Exercise 6: Regression"
category: "Statistics Bootcamp"
module: 98
order: 7
---

# Exercise 6: Regression

> 📚 **Overview:** Practice fitting and interpreting regression models.

Practice problems for regression analysis.

---

## Topics Covered
- Simple linear regression
- R-squared interpretation
- Testing regression coefficients
- ANOVA

---

## Problem 1 (Linear Regression)

| x | y |
|---|---|
| 1 | 3 |
| 2 | 5 |
| 3 | 7 |
| 4 | 9 |
| 5 | 11 |

Find the regression equation.

<details>
<summary>💡 Show Solution</summary>

x̄ = 3, ȳ = 7

| x | y | x-x̄ | y-ȳ | (x-x̄)(y-ȳ) | (x-x̄)² |
|---|---|------|------|-------------|--------|
| 1 | 3 | -2 | -4 | 8 | 4 |
| 2 | 5 | -1 | -2 | 2 | 1 |
| 3 | 7 | 0 | 0 | 0 | 0 |
| 4 | 9 | 1 | 2 | 2 | 1 |
| 5 | 11 | 2 | 4 | 8 | 4 |
| Σ | | | | 20 | 10 |

$$
\hat{\beta}_1 = \frac{20}{10} = 2
$$

$$
\hat{\beta}_0 = 7 - 2(3) = 1
$$

**Equation: ŷ = 1 + 2x**

</details>

---

## Problem 2 (R-squared)

A regression has SST = 200 and SSE = 40.
a) Calculate R²
b) Interpret the result

<details>
<summary>💡 Show Solution</summary>

**a) R²:**

$$
R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{40}{200} = 0.80
$$

**b) Interpretation:**
80% of the variation in Y is explained by the regression model.

</details>

---

## Problem 3 (Testing Slope)

Regression output: β̂₁ = 3.5, SE(β̂₁) = 1.2, n = 22
Test if slope differs from zero at α = 0.05.

<details>
<summary>💡 Show Solution</summary>

$$
t = \frac{3.5}{1.2} = 2.92
$$

df = 20, t₀.₀₂₅,₂₀ = 2.086

**Decision:** 2.92 > 2.086 → Reject H₀

**Conclusion:** Significant linear relationship exists.

</details>

---

## Problem 4 (Raw-score regression table)

Given data:

| x | y |
|---:|---:|
| 1 | 5 |
| 2 | 7 |
| 3 | 8 |
| 4 | 10 |
| 5 | 12 |

Compute \(\\hat{\\beta}_1\) using the raw-score formula:

$$
\\hat{\\beta}_1 = \\frac{\\sum x_iy_i - n\\bar{x}\\bar{y}}{\\sum x_i^2 - n\\bar{x}^2}
$$

<details>
<summary>💡 Show Solution</summary>

Compute sums:

| xᵢ | yᵢ | xᵢyᵢ | xᵢ² |
|---:|---:|---:|---:|
| 1 | 5 | 5 | 1 |
| 2 | 7 | 14 | 4 |
| 3 | 8 | 24 | 9 |
| 4 | 10 | 40 | 16 |
| 5 | 12 | 60 | 25 |
| **Σ** | **42** | **143** | **55** |

n = 5, \(\\bar{x} = 15/5 = 3\), \(\\bar{y} = 42/5 = 8.4\)

$$
\\hat{\\beta}_1 = \\frac{143 - 5\\cdot 3\\cdot 8.4}{55 - 5\\cdot 3^2} = \\frac{17}{10} = 1.7
$$

</details>

---

## Problem 5 (Correlation → regression slope)

You have r = 0.80, sₓ = 5, sᵧ = 12.
Compute the regression slope \(\\hat{\\beta}_1\).

<details>
<summary>💡 Show Solution</summary>

$$
\\hat{\\beta}_1 = r\\cdot \\frac{s_y}{s_x} = 0.80\\cdot \\frac{12}{5} = 1.92
$$

Interpretation: A +1 increase in x predicts +1.92 in y (units).

</details>

---

## Problem 6 (Predictions and residuals)

Using the regression line \(\\hat{y} = 3.3 + 1.7x\), compute:

a) \(\\hat{y}\) when x = 4
b) The residual if the observed y at x = 4 is 10
c) Interpret the sign of the residual

<details>
<summary>💡 Show Solution</summary>

a) \(\\hat{y} = 3.3 + 1.7(4) = 10.1\)
b) Residual = y − \(\\hat{y}\) = 10 − 10.1 = −0.1
c) Negative residual means the observed value is slightly below the model prediction.

</details>

---

## Problem 7 (SSE, SSR, SST relationship)

If SST = 500 and SSE = 120, compute SSR and R².

<details>
<summary>💡 Show Solution</summary>

SSR = SST − SSE = 500 − 120 = 380
R² = SSR/SST = 380/500 = 0.76

Interpretation: 76% of variation in y is explained by the model.

</details>

---

## Problem 8 (Decision sentence)

A regression slope test results in “Reject H₀: β₁ = 0” at α = 0.05.
Write one business interpretation sentence.

<details>
<summary>💡 Show Solution</summary>

Example: “There is evidence that x is associated with y; changing x is linked to a predictable change in y, so management can use x to forecast y (with caution about causality).”

</details>

---

## Problem 9 (Übungsblatt-style full regression table)

Data (x = advertising spend in 1000 CHF, y = weekly sales in 10k CHF):

| x | y |
|---:|---:|
| 1 | 3 |
| 2 | 4 |
| 3 | 5 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |

Compute \(\\hat{\\beta}_1\\) and \(\\hat{\\beta}_0\\) using a deviation table (include Σ totals).

<details>
<summary>💡 Show Solution</summary>

Means: \(\\bar x=3.5\\), \(\\bar y=5\\).

| x | y | \(x-\\bar x\) | \(y-\\bar y\) | \((x-\\bar x)(y-\\bar y)\) | \((x-\\bar x)^2\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 3 | -2.5 | -2 | 5.0 | 6.25 |
| 2 | 4 | -1.5 | -1 | 1.5 | 2.25 |
| 3 | 5 | -0.5 | 0 | 0.0 | 0.25 |
| 4 | 5 | 0.5 | 0 | 0.0 | 0.25 |
| 5 | 6 | 1.5 | 1 | 1.5 | 2.25 |
| 6 | 7 | 2.5 | 2 | 5.0 | 6.25 |
| **Σ** |  |  |  | **13.0** | **17.5** |

$$
\\hat{\\beta}_1 = \\frac{13}{17.5} = 0.7429
$$

$$
\\hat{\\beta}_0 = \\bar y - \\hat{\\beta}_1\\bar x = 5 - 0.7429\\cdot 3.5 = 2.4
$$

Regression: \(\\hat y = 2.4 + 0.7429x\\).

**Slope interpretation:** For each additional 1000 CHF spent on advertising, weekly sales increase by approximately 0.74 × 10k CHF = **7,430 CHF** on average.

</details>

---

## Problem 10 (Prediction + extrapolation)

Using \(\\hat y = 2.4 + 0.7429x\\), compute:

a) \(\\hat y\\) at x = 7  
b) One sentence: why should you be cautious with this prediction?

<details>
<summary>💡 Show Solution</summary>

a) \(\\hat y = 2.4 + 0.7429\\cdot 7 = 7.6003\\approx 7.60\\).

b) x = 7 is outside the observed range (1–6), so this is **extrapolation**; the linear relationship may not hold beyond the data.

</details>

---

## Problem 11 (Confidence interval for slope)

Regression output gives \(\\hat\\beta_1=0.74\\), \(SE(\\hat\\beta_1)=0.12\\), and n = 30.

Construct a 95% confidence interval for \(\\beta_1\\) (use \(t_{0.025,28}\\approx 2.048\\)).

<details>
<summary>💡 Show Solution</summary>

$$
CI: \\hat\\beta_1 \\pm t\\cdot SE = 0.74 \\pm 2.048\\cdot 0.12 = 0.74 \\pm 0.2458
$$

So:

$$
(0.494,\\ 0.986)
$$

</details>

---

## Problem 12 (Residual check)

If the observed y at x = 2 is y = 4, and the model predicts \(\\hat y=3.8857\\), compute the residual and interpret its sign.

<details>
<summary>💡 Show Solution</summary>

Residual \(e=y-\\hat y = 4-3.8857=0.1143\\).

Positive residual means the observation is **above** the regression line (model under-predicted y).

</details>

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Forgetting that residual = observed − predicted.
> ⚠️ **Mistake 2:** Interpreting R² as a causal effect.
> ⚠️ **Mistake 3:** Confusing SSE/SSR/SST (remember: SST = SSR + SSE).

---

## Key Takeaways

- Use either deviation tables or raw-score tables (both give the same slope)
- R² = 1 − SSE/SST = SSR/SST
- Predictions use \(\\hat{y} = \\hat{\\beta}_0 + \\hat{\\beta}_1 x\)
- Always add a short business interpretation sentence

---

## Related Modules

- [Module 12: Regression Analysis](../12_regression_analysis/index.md)
- [Module 13: Advanced Topics](../13_advanced_topics/index.md)

---

## Navigation

[← Exercise 5](exercise_5.md) | [Exercises Index](index.md)


