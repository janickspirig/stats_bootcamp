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

## Intuition (why multiple regression exists)

In business, outcomes usually depend on **more than one factor**. Multiple regression lets you estimate the relationship between \(Y\) and one predictor while **controlling for other predictors**.

The key phrase is **“holding other variables constant”**: it means “compare two observations that are the same in all other included predictors, except \(x_j\).”

**Why this matters (confounding):** If advertising spend rises in peak season, then a simple regression of Sales on Ads can mix up “ads effect” with “season effect”. Adding a season variable helps separate these effects.

---

## When to use / when not to use

- **Use when**: you want to explain/predict a numeric outcome using **multiple predictors** (numeric or dummy-coded categorical).
- **Use when**: you expect confounding and want a “controlled” comparison.
- **Do not use when**: the outcome is categorical (use logistic models; not covered here).
- **Do not use when**: the relationship is clearly non-linear and you have no transformation/terms to model it.

---

## Interpretation sentence templates (exam-ready)

For a coefficient on \(x_j\):

- “A one-unit increase in \(x_j\) is associated with an average change of **[β̂ⱼ]** in \(Y\), **holding the other predictors constant**.”
- “The sign of \(\\hat\\beta_j\) is [positive/negative], meaning higher \(x_j\) is associated with [higher/lower] \(Y\) after controlling for the other variables.”

For adjusted R²:

- “Adjusted \(R^2\) increases only if the new predictor improves the model enough to justify the extra complexity.”

---

## Common traps (high-frequency)

> ⚠️ **Trap 1: Forgetting ‘holding others constant’.**
> Multiple regression coefficients are *partial* effects, not simple pairwise relationships.

> ⚠️ **Trap 2: Sign flips.**
> A coefficient can change sign after adding controls (classic confounding).

> ⚠️ **Trap 3: Interpreting the intercept literally.**
> \(\\hat\\beta_0\) is the predicted \(Y\) when all predictors are 0 — often outside the meaningful data range.

> ⚠️ **Trap 4: Multicollinearity.**
> If predictors move together strongly (e.g., Ads and Promo), individual coefficients can become unstable.

> ⚠️ **Trap 5: Causality language.**
> Unless the study design supports it, write “associated with”, not “causes”.

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


