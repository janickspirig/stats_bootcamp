---
title: "I can fit a linear regression model"
category: "Statistics Bootcamp"
module: 12
order: 1
---

# I can fit a linear regression model

> 📚 **Overview:** Use OLS to find the best-fitting line through your data points.

Using OLS to estimate the regression line.

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate slope and intercept using OLS
- Write the regression equation
- Make predictions using the model

---

## Checklist

- **When to use:** You want to model/predict a numeric outcome \(Y\) using a numeric predictor \(X\) with a linear relationship.
- **What to report (exam style):** the calculation table (with Σ totals), \(\\hat{\\beta}_1, \\hat{\\beta}_0\), the regression equation, and a short business interpretation (what does a +1 in x mean?).
- **Common trap:** Mixing the “deviation” method and “raw-sum” method inconsistently—pick one and show all steps.

---

## The Model

$$
y = \beta_0 + \beta_1 x + \varepsilon
$$

Where:
- $\beta_0$ = intercept (y when x = 0)
- $\beta_1$ = slope (change in y per unit change in x)
- $\varepsilon$ = error term

---

## OLS Formulas

**Slope:**

$$
\hat{\beta}_1 = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2} = \frac{S_{xy}}{S_{xx}}
$$

**Intercept:**

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}
$$

![Scatter plot with fitted OLS line and residual segments](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/ols_fit_and_residuals.png)

---

## Alternative (raw-score) formulas (often faster in tables)

These are equivalent and commonly used when you have sums like \(\\sum x_i\\), \(\\sum y_i\\), \(\\sum x_i^2\\), and \(\\sum x_iy_i\\).

$$
\\hat{\\beta}_1
= \\frac{\\sum x_iy_i - n\\bar{x}\\bar{y}}{\\sum x_i^2 - n\\bar{x}^2}
$$

$$
\\hat{\\beta}_0 = \\bar{y} - \\hat{\\beta}_1\\bar{x}
$$

### Connection to correlation (if you know r)

$$
\\hat{\\beta}_1 = r\\cdot \\frac{s_y}{s_x}
$$

---

## Worked Example

**Problem:**
Fit a regression line to predict sales (Y) from advertising (X):

| X (ads) | Y (sales) |
|---------|-----------|
| 1 | 5 |
| 2 | 7 |
| 3 | 8 |
| 4 | 10 |
| 5 | 12 |

**Solution:**

### Step 1: Calculate Means
$\bar{x}$ = 15/5 = 3
$\bar{y}$ = 42/5 = 8.4

### Step 2: Build Calculation Table

| x | y | x-x̄ | y-ȳ | (x-x̄)(y-ȳ) | (x-x̄)² |
|---|---|------|------|-------------|--------|
| 1 | 5 | -2 | -3.4 | 6.8 | 4 |
| 2 | 7 | -1 | -1.4 | 1.4 | 1 |
| 3 | 8 | 0 | -0.4 | 0 | 0 |
| 4 | 10 | 1 | 1.6 | 1.6 | 1 |
| 5 | 12 | 2 | 3.6 | 7.2 | 4 |
| **Σ** | | | | **17** | **10** |

### Step 2b (Übungsblatt-style): Raw-score table

| Rep | xᵢ | yᵢ | xᵢyᵢ | xᵢ² | yᵢ² |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 5 | 5 | 1 | 25 |
| 2 | 2 | 7 | 14 | 4 | 49 |
| 3 | 3 | 8 | 24 | 9 | 64 |
| 4 | 4 | 10 | 40 | 16 | 100 |
| 5 | 5 | 12 | 60 | 25 | 144 |
| **Σ** | **15** | **42** | **143** | **55** | **382** |

### Step 3: Calculate Slope

$$
\hat{\beta}_1 = \frac{17}{10} = 1.7
$$

Equivalent using the raw-score shortcut:

$$
\\hat{\\beta}_1
= \\frac{\\sum x_iy_i - n\\bar{x}\\bar{y}}{\\sum x_i^2 - n\\bar{x}^2}
= \\frac{143 - 5\\cdot 3\\cdot 8.4}{55 - 5\\cdot 3^2}
= \\frac{17}{10}
= 1.7
$$

### Step 4: Calculate Intercept

$$
\hat{\beta}_0 = 8.4 - 1.7 \times 3 = 8.4 - 5.1 = 3.3
$$

### Regression Equation

$$
\hat{y} = 3.3 + 1.7x
$$

**Interpretation:**
- Each additional ad unit increases sales by 1.7 units
- With no advertising, expected sales is 3.3 units

Business interpretation: If one “ad unit” costs less than the profit from ~1.7 extra sales units, increasing advertising is likely worthwhile (subject to causality/assumptions).

---

## Worked Example (Übungsblatt-style full table + residuals)

**Problem:**
You want to predict weekly sales \(Y\) (in 10k CHF) from advertising spend \(X\) (in 1000 CHF):

| \(x_i\) | \(y_i\) |
|---:|---:|
| 1 | 3 |
| 2 | 4 |
| 3 | 5 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |

Fit the regression line and compute the residuals.

<details>
<summary>💡 Show Solution</summary>

### Step 1: Means

$$
\\bar{x} = \\frac{1+2+3+4+5+6}{6} = \\frac{21}{6} = 3.5
$$

$$
\\bar{y} = \\frac{3+4+5+5+6+7}{6} = \\frac{30}{6} = 5
$$

### Step 2: Deviation table (exam-friendly)

| \(x\) | \(y\) | \(x-\\bar x\) | \(y-\\bar y\) | \((x-\\bar x)(y-\\bar y)\) | \((x-\\bar x)^2\) | \((y-\\bar y)^2\) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3 | -2.5 | -2 | 5.0 | 6.25 | 4 |
| 2 | 4 | -1.5 | -1 | 1.5 | 2.25 | 1 |
| 3 | 5 | -0.5 | 0 | 0.0 | 0.25 | 0 |
| 4 | 5 | 0.5 | 0 | 0.0 | 0.25 | 0 |
| 5 | 6 | 1.5 | 1 | 1.5 | 2.25 | 1 |
| 6 | 7 | 2.5 | 2 | 5.0 | 6.25 | 4 |
| **Σ** |  |  |  | **13.0** | **17.5** | **10.0** |

So:

$$
S_{xy}=\\sum (x_i-\\bar x)(y_i-\\bar y)=13,\\qquad
S_{xx}=\\sum (x_i-\\bar x)^2=17.5
$$

### Step 3: Slope

$$
\\hat{\\beta}_1 = \\frac{S_{xy}}{S_{xx}} = \\frac{13}{17.5} = 0.7429
$$

### Step 4: Intercept

$$
\\hat{\\beta}_0 = \\bar y - \\hat{\\beta}_1\\bar x
= 5 - 0.7429\\cdot 3.5
= 2.4
$$

### Step 5: Regression equation

$$
\\hat y = 2.4 + 0.7429x
$$

### Step 6: Residuals (often useful for R² and model checks)

Residual \(e_i = y_i-\\hat y_i\\).

| \(x\) | \(y\) | \(\\hat y\) | \(e=y-\\hat y\) | \(e^2\) |
|---:|---:|---:|---:|---:|
| 1 | 3 | 3.1429 | -0.1429 | 0.0204 |
| 2 | 4 | 3.8857 | 0.1143 | 0.0131 |
| 3 | 5 | 4.6286 | 0.3714 | 0.1380 |
| 4 | 5 | 5.3714 | -0.3714 | 0.1380 |
| 5 | 6 | 6.1143 | -0.1143 | 0.0131 |
| 6 | 7 | 6.8571 | 0.1429 | 0.0204 |
| **Σ** |  |  |  | **0.3429** |

So \(SSE=\\sum e_i^2\\approx 0.3429\\).

Business interpretation: A +1k CHF increase in advertising is associated with about **+0.743** (≈ **+7.43k CHF**) higher weekly sales on average, in this sample.

</details>

---

## Practice Problems

### Problem 1

| x | y |
|---|---|
| 2 | 10 |
| 4 | 15 |
| 6 | 20 |
| 8 | 25 |

Find the regression equation.

<details>
<summary>💡 Show Solution</summary>

$\bar{x}$ = 5, $\bar{y}$ = 17.5

| x | y | (x-5)(y-17.5) | (x-5)² |
|---|---|---------------|--------|
| 2 | 10 | (-3)(-7.5) = 22.5 | 9 |
| 4 | 15 | (-1)(-2.5) = 2.5 | 1 |
| 6 | 20 | (1)(2.5) = 2.5 | 1 |
| 8 | 25 | (3)(7.5) = 22.5 | 9 |
| Σ | | 50 | 20 |

$\hat{\beta}_1 = 50/20 = 2.5$
$\hat{\beta}_0 = 17.5 - 2.5(5) = 5$

**Equation: ŷ = 5 + 2.5x**

</details>

---

### Problem 2 (Übungsblatt-style: require Σ totals)

The following data relates sales calls \(x\) to closed deals \(y\):

| \(x\) | \(y\) |
|---:|---:|
| 1 | 3 |
| 2 | 4 |
| 3 | 5 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |

Compute \(\\hat\\beta_1\\) and \(\\hat\\beta_0\\) using the **raw-score** table (include Σx, Σy, Σxy, Σx²).

<details>
<summary>💡 Show Solution</summary>

Raw-score table:

| \(x_i\) | \(y_i\) | \(x_i y_i\) | \(x_i^2\) |
|---:|---:|---:|---:|
| 1 | 3 | 3 | 1 |
| 2 | 4 | 8 | 4 |
| 3 | 5 | 15 | 9 |
| 4 | 5 | 20 | 16 |
| 5 | 6 | 30 | 25 |
| 6 | 7 | 42 | 36 |
| **Σ** | **30** | **118** | **91** |

Means: \(\\bar x=21/6=3.5\\), \(\\bar y=30/6=5\\).

$$
\\hat{\\beta}_1
= \\frac{\\sum x_iy_i - n\\bar{x}\\bar{y}}{\\sum x_i^2 - n\\bar{x}^2}
= \\frac{118 - 6\\cdot 3.5\\cdot 5}{91 - 6\\cdot 3.5^2}
= \\frac{13}{17.5}
= 0.7429
$$

$$
\\hat{\\beta}_0 = \\bar y - \\hat{\\beta}_1\\bar x = 5 - 0.7429\\cdot 3.5 = 2.4
$$

Equation: \(\\hat y = 2.4 + 0.7429x\\).

</details>

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Forgetting Σ totals.
> Many exam solutions expect explicit \(\\sum x_i\\), \(\\sum y_i\\), \(\\sum x_i^2\\), and \(\\sum x_iy_i\\) (or the deviation sums).

> ⚠️ **Mistake 2:** Confusing slope and intercept.
> \(\\hat{\\beta}_1\) is the “per +1 in x” effect; \(\\hat{\\beta}_0\) is the predicted y when x = 0 (which may be outside the data range).

> ⚠️ **Mistake 3:** Treating regression as causation automatically.
> A good fit does not prove that changing x will change y (confounding may exist).

---

## Key Takeaways

- OLS minimizes sum of squared residuals
- Slope = covariance / variance of x
- Line always passes through (x̄, ȳ)
- Use equation for predictions

---

## Quick Check

1) Fill in the blank: The slope \(\\hat{\\beta}_1\) represents the change in ___ for a +1 change in ___.
2) True/False: A high R² proves that x causes y.
3) If r = 0, what is \(\\hat{\\beta}_1\) in the formula \(\\hat{\\beta}_1 = r\\cdot (s_y/s_x)\)?

<details>
<summary>Answers</summary>

1) predicted y; x.
2) False.
3) \(\\hat{\\beta}_1 = 0\).

</details>

## Navigation

[← Module Index](index.md) | [Next: R-Squared →](r_squared.md)


