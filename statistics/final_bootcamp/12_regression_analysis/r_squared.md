---
title: "I can interpret R-squared"
category: "Statistics Bootcamp"
module: 12
order: 2
---

# I can interpret R-squared

> 📚 **Overview:** Measure how well your regression model explains the variation in Y.

The coefficient of determination.

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate and interpret R²
- Understand the relationship between r and R²
- Know limitations of R²

---

## Key Formulas

**Sum of Squares:**
- **SST** (Total) = $\sum(y_i - \bar{y})^2$
- **SSR** (Regression) = $\sum(\hat{y}_i - \bar{y})^2$
- **SSE** (Error) = $\sum(y_i - \hat{y}_i)^2$

**Relationship:** SST = SSR + SSE

**R-squared:**

$$
R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}
$$

---

## Interpretation

R² = proportion of variance in Y explained by X

| R² | Interpretation |
|-----|----------------|
| 0 | X explains nothing |
| 0.3 | X explains 30% of Y's variance |
| 0.7 | X explains 70% of Y's variance |
| 1 | X explains everything (perfect fit) |

---

## Relationship to Correlation

For simple linear regression:

$$
R^2 = r^2
$$

If r = 0.8, then R² = 0.64

---

## Worked Example

**Problem:**
From previous example: $\hat{y} = 3.3 + 1.7x$

Calculate R² and interpret.

| x | y | ŷ | y-ȳ | ŷ-ȳ | y-ŷ |
|---|---|---|-----|-----|-----|
| 1 | 5 | 5.0 | -3.4 | -3.4 | 0 |
| 2 | 7 | 6.7 | -1.4 | -1.7 | 0.3 |
| 3 | 8 | 8.4 | -0.4 | 0 | -0.4 |
| 4 | 10 | 10.1 | 1.6 | 1.7 | -0.1 |
| 5 | 12 | 11.8 | 3.6 | 3.4 | 0.2 |

SST = (-3.4)² + (-1.4)² + (-0.4)² + 1.6² + 3.6² = 28.8
SSR = (-3.4)² + (-1.7)² + 0² + 1.7² + 3.4² = 28.9 ≈ 28.9
SSE = 0² + 0.3² + 0.4² + 0.1² + 0.2² = 0.30

$$
R^2 = 1 - \frac{0.30}{28.8} = 1 - 0.01 = 0.99
$$

**Interpretation:** 99% of the variance in sales is explained by advertising.

---

## Practice Problems

### Problem 1

A regression has SST = 100 and SSE = 25. Find R².

<details>
<summary>💡 Show Solution</summary>

$$
R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{25}{100} = 0.75
$$

**Interpretation:** 75% of variance is explained by the model.

</details>

---

### Problem 2

If r = -0.6, what is R²? What does the negative r mean?

<details>
<summary>💡 Show Solution</summary>

R² = (-0.6)² = 0.36 = 36%

The negative r indicates a **negative relationship** (as X increases, Y decreases). R² is always positive - it only indicates strength, not direction.

</details>

---

## Limitations of R²

- Higher R² doesn't mean better model
- R² always increases when adding variables
- Doesn't indicate causation
- Doesn't indicate correct model specification

---

## Key Takeaways

- R² = proportion of variance explained
- R² = r² for simple linear regression
- Range: 0 to 1
- Higher isn't always better

---

## Navigation

[← Fitting Regression](fitting_regression.md) | [Module Index](index.md) | [Next: Testing Coefficients →](testing_coefficients.md)


