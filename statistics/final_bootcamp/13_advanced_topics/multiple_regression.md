---
title: "I understand multiple regression"
category: "Statistics Bootcamp"
module: 13
order: 3
---

# I understand multiple regression

> 📚 **Overview:** Extend regression to multiple predictors—controlling for confounders.

Regression with multiple predictors.

---

## Learning Objectives

After completing this section, you will be able to:
- Understand multiple regression model
- Interpret coefficients as partial effects
- Know about adjusted R²

---

## The Model

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_k x_k + \varepsilon
$$

Each $\beta_j$ represents the effect of $x_j$ **holding other variables constant**.

---

## Interpretation

**Example:**

$$
\hat{y} = 10 + 2x_1 + 5x_2
$$

- $\beta_1 = 2$: For each unit increase in x₁, y increases by 2, **holding x₂ constant**
- $\beta_2 = 5$: For each unit increase in x₂, y increases by 5, **holding x₁ constant**
- $\beta_0 = 10$: Predicted y when x₁ = x₂ = 0

---

## Adjusted R²

Standard R² always increases with more variables. **Adjusted R²** penalizes for complexity:

$$
R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}
$$

Use adjusted R² to compare models with different numbers of predictors.

---

## Practice Problem

Model: $\hat{\text{Sales}} = 100 + 3(\text{Ads}) + 2(\text{Price}) - 5(\text{Competitor})$

Interpret each coefficient.

<details>
<summary>💡 Show Solution</summary>

- **Intercept (100):** Predicted sales when all predictors are zero
- **Ads (3):** Each unit increase in advertising increases sales by 3, holding price and competitor constant
- **Price (2):** Each unit increase in price increases sales by 2 (counterintuitive - may indicate luxury good)
- **Competitor (-5):** Each unit of competitor activity decreases sales by 5

</details>

---

## Key Takeaways

- Multiple regression controls for confounders
- Coefficients are **partial effects**
- Use adjusted R² for model comparison
- More variables ≠ better model

---

## Navigation

[← Dummy Variables](dummy_variables.md) | [Module Index](index.md) | [Exercises →](../exercises/index.md)


