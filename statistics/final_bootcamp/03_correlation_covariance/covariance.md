---
title: "I can calculate and interpret covariance"
category: "Statistics Bootcamp"
module: 3
order: 1
---

# I can calculate and interpret covariance

> 📚 **Overview:** Covariance measures how two variables move together—whether they tend to increase or decrease at the same time.

---

## 📑 Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Key Concepts](#key-concepts)
3. [Worked Example](#worked-example)
4. [Practice Problems](#practice-problems)
5. [Common Mistakes to Avoid](#common-mistakes-to-avoid)
6. [Key Takeaways](#key-takeaways)

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate sample and population covariance
- Interpret the sign of covariance
- Understand the limitations of covariance as a measure
- Build calculation tables for covariance

---

## Key Concepts

### What is Covariance?

**Covariance** measures the direction of the linear relationship between two variables.

- **Positive covariance:** When X increases, Y tends to increase
- **Negative covariance:** When X increases, Y tends to decrease
- **Zero covariance:** No linear relationship

---

### Formulas

**Sample Covariance:**

$$
s_{xy} = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})
$$

**Population Covariance:**

$$
\sigma_{xy} = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu_x)(y_i - \mu_y)
$$

---

### Interpretation

| Covariance | Interpretation |
|------------|----------------|
| sₓᵧ > 0 | Positive relationship (X↑ → Y↑) |
| sₓᵧ < 0 | Negative relationship (X↑ → Y↓) |
| sₓᵧ = 0 | No linear relationship |

> ⚠️ **Limitation:** The magnitude of covariance depends on the units of X and Y. A covariance of 100 doesn't mean "stronger" than 10 unless the variables have the same units and scales.

---

## Worked Example

**Problem:**
A marketing analyst collected data on advertising spend (thousands CHF) and sales (thousands CHF) for 6 months. Calculate the sample covariance.

| Month | Advertising (X) | Sales (Y) |
|-------|-----------------|-----------|
| 1 | 10 | 100 |
| 2 | 15 | 120 |
| 3 | 12 | 110 |
| 4 | 18 | 140 |
| 5 | 20 | 150 |
| 6 | 13 | 115 |

**Solution:**

### Step 1: Calculate Means

$$
\bar{x} = \frac{10+15+12+18+20+13}{6} = \frac{88}{6} = 14.67
$$

$$
\bar{y} = \frac{100+120+110+140+150+115}{6} = \frac{735}{6} = 122.5
$$

### Step 2: Build Calculation Table

| i | $x_i$ | $y_i$ | $x_i - \bar{x}$ | $y_i - \bar{y}$ | $(x_i-\bar{x})(y_i-\bar{y})$ |
|---|-------|-------|-----------------|-----------------|------------------------------|
| 1 | 10 | 100 | -4.67 | -22.5 | 105.08 |
| 2 | 15 | 120 | 0.33 | -2.5 | -0.83 |
| 3 | 12 | 110 | -2.67 | -12.5 | 33.38 |
| 4 | 18 | 140 | 3.33 | 17.5 | 58.28 |
| 5 | 20 | 150 | 5.33 | 27.5 | 146.58 |
| 6 | 13 | 115 | -1.67 | -7.5 | 12.53 |
| **Σ** | 88 | 735 | 0 | 0 | **355.02** |

### Step 3: Calculate Sample Covariance

$$
s_{xy} = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{n-1} = \frac{355.02}{6-1} = \frac{355.02}{5} = 71.00
$$

### Interpretation
The covariance is **positive (71.00)**, indicating that advertising spend and sales tend to move in the same direction. When advertising increases, sales also tend to increase.

---

## Practice Problems

### Problem 1

Calculate the covariance for the following data on study hours (X) and exam scores (Y):

| Student | Hours (X) | Score (Y) |
|---------|-----------|-----------|
| A | 2 | 65 |
| B | 4 | 75 |
| C | 3 | 70 |
| D | 5 | 85 |
| E | 6 | 90 |

<details>
<summary>💡 Show Solution</summary>

**Step 1: Calculate Means**

$$
\bar{x} = \frac{2+4+3+5+6}{5} = \frac{20}{5} = 4
$$

$$
\bar{y} = \frac{65+75+70+85+90}{5} = \frac{385}{5} = 77
$$

**Step 2: Calculation Table**

| X | Y | X - 4 | Y - 77 | Product |
|---|---|-------|--------|---------|
| 2 | 65 | -2 | -12 | 24 |
| 4 | 75 | 0 | -2 | 0 |
| 3 | 70 | -1 | -7 | 7 |
| 5 | 85 | 1 | 8 | 8 |
| 6 | 90 | 2 | 13 | 26 |
| **Σ** | | 0 | 0 | **65** |

**Step 3: Calculate Covariance**

$$
s_{xy} = \frac{65}{5-1} = \frac{65}{4} = 16.25
$$

**Interpretation:** Positive covariance indicates more study hours are associated with higher scores.

</details>

---

### Problem 2

A dataset has covariance sₓᵧ = -45. What does this tell you about the relationship between X and Y?

<details>
<summary>💡 Show Solution</summary>

A **negative covariance (-45)** indicates:
- X and Y move in **opposite directions**
- When X increases, Y tends to decrease
- When X decreases, Y tends to increase

**Examples of negative relationships:**
- Price and quantity demanded
- Time spent on phone and battery percentage
- Age of car and resale value

**Note:** We cannot say how "strong" this relationship is without knowing the units and scales of X and Y.

</details>

---

### Problem 3

Two analysts calculate covariance for similar relationships:
- Analyst A: Advertising (CHF) vs Sales (CHF): Covariance = 50,000
- Analyst B: Advertising (thousands CHF) vs Sales (thousands CHF): Covariance = 50

Is the relationship in A's data 1000 times stronger than in B's data?

<details>
<summary>💡 Show Solution</summary>

**No!** The covariances cannot be directly compared because the units differ.

If Analyst A used CHF and Analyst B used thousands of CHF, the underlying relationship could be identical:
- 1000 CHF × 1000 CHF = 1,000,000 × the units factor
- The covariance in A's data is larger only because of the scale

**This is why we use correlation** — it's standardized and unit-free, allowing fair comparisons across different scales.

</details>

---

## Visual Interpretation

<!-- IMAGE_PLACEHOLDER
Type: scatter
Description: Three scatter plots side by side: (1) Positive covariance - points trending upward from left to right, (2) Negative covariance - points trending downward from left to right, (3) Zero covariance - points scattered randomly with no pattern. Each labeled with its covariance sign.
Data: Generate synthetic data for each pattern
Style: Clean scatter plots with trend annotations
Filename: covariance_patterns.png
-->
![Covariance patterns](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/covariance_patterns.png)

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Comparing covariances across different units.
> Use correlation instead for comparisons.

> ⚠️ **Mistake 2:** Interpreting covariance magnitude as strength.
> The magnitude depends on units; only the sign is universally interpretable.

> ⚠️ **Mistake 3:** Forgetting to divide by (n-1) for sample covariance.
> Same rule as variance: use (n-1) for samples.

---

## Key Takeaways

> 🎯 **Remember:**
> - **Covariance** measures direction of linear relationship
> - **Positive:** Variables move together
> - **Negative:** Variables move opposite
> - **Limitation:** Magnitude depends on units
> - Use **correlation** for standardized comparison

---

## Navigation

[← Module Index](index.md) | [Next: Correlation →](correlation.md)

**Related Reference:** [Formula Glossary](../reference/formula_glossary.md)


