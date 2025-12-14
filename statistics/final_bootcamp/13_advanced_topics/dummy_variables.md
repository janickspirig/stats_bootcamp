---
title: "I understand dummy variables"
category: "Statistics Bootcamp"
module: 13
order: 4
---

# I understand dummy variables

> 📚 **Overview:** Include categorical variables in regression using 0/1 coding.

Including categorical predictors in regression.

---

## Learning Objectives

After completing this section, you will be able to:
- Create dummy variables from categorical data
- Interpret regression coefficients for dummies
- Understand the reference category concept

---

## Key Concepts

**Dummy variable:** Binary (0/1) variable representing category membership.

For k categories, use k-1 dummy variables (one is the reference).

---

## Example

**Gender in regression:**
- D = 1 if Female
- D = 0 if Male (reference)

**Model:**

$$
\hat{y} = \beta_0 + \beta_1 D
$$

**Interpretation:**
- $\beta_0$ = mean Y for Males (D=0)
- $\beta_0 + \beta_1$ = mean Y for Females (D=1)
- $\beta_1$ = difference between Female and Male means

---

## Multiple Categories

For 3 regions (North, South, East):
- D₁ = 1 if South, 0 otherwise
- D₂ = 1 if East, 0 otherwise
- North = reference (D₁=0, D₂=0)

**Model:**

$$
\hat{y} = \beta_0 + \beta_1 D_1 + \beta_2 D_2
$$

**Interpretation:**
- $\beta_0$ = mean for North
- $\beta_1$ = South minus North
- $\beta_2$ = East minus North

---

## Practice Problem

Regression output: $\hat{y} = 50 + 8D$ where D = 1 for Premium customers.

a) What's the predicted Y for Regular customers?
b) What's the predicted Y for Premium customers?
c) Interpret the coefficient 8.

<details>
<summary>💡 Show Solution</summary>

**a) Regular (D=0):** $\hat{y} = 50 + 8(0) = 50$

**b) Premium (D=1):** $\hat{y} = 50 + 8(1) = 58$

**c) Interpretation:** Premium customers have a predicted Y that is 8 units higher than Regular customers.

</details>

---

## Key Takeaways

- Use k-1 dummies for k categories
- Coefficients show difference from reference
- Choose reference category thoughtfully
- Can test if categories differ via t-test on coefficient

---

## Navigation

[← ANOVA](anova.md) | [Module Index](index.md) | [Next: Multiple Regression →](multiple_regression.md)


