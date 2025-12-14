---
title: "I can identify skewness and kurtosis"
category: "Statistics Bootcamp"
module: 2
order: 4
---

# I can identify skewness and kurtosis

> 📚 **Overview:** Skewness and kurtosis describe the shape of a distribution beyond its center and spread. Learn to recognize and interpret these important characteristics.

---

## 📑 Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Key Concepts](#key-concepts)
3. [Worked Example](#worked-example)
4. [Practice Problems](#practice-problems)
5. [Visual Recognition Guide](#visual-recognition-guide)
6. [Common Mistakes to Avoid](#common-mistakes-to-avoid)
7. [Key Takeaways](#key-takeaways)

---

## Learning Objectives

After completing this section, you will be able to:
- Identify left-skewed, right-skewed, and symmetric distributions
- Understand the relationship between mean and median in skewed data
- Interpret kurtosis (leptokurtic, mesokurtic, platykurtic)
- Recognize shape characteristics from data and graphs

---

## Key Concepts

### Skewness

**Skewness** measures the asymmetry of a distribution.

<!-- IMAGE_PLACEHOLDER
Type: chart
Description: Three distribution curves side by side showing: Left-skewed (negative skew) with tail to the left, Symmetric (zero skew) as a normal bell curve, Right-skewed (positive skew) with tail to the right. Each labeled with mean/median relationship.
Data: Three curves with annotations showing tail direction
Style: Three distinct curves, labeled with skewness values and mean/median positions
Filename: skewness_types.png
-->
![Types of skewness](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/skewness_types.png)

| Type | Skewness Value | Tail Direction | Mean vs Median |
|------|----------------|----------------|----------------|
| Left-skewed (Negative) | < 0 | Tail to left | Mean < Median |
| Symmetric | ≈ 0 | No tail | Mean ≈ Median |
| Right-skewed (Positive) | > 0 | Tail to right | Mean > Median |

---

### Interpreting Skewness Values

| Skewness Value | Interpretation |
|----------------|----------------|
| -1 to -0.5 | Moderately left-skewed |
| -0.5 to 0.5 | Approximately symmetric |
| 0.5 to 1 | Moderately right-skewed |
| < -1 or > 1 | Highly skewed |

---

### Examples of Skewness

**Right-skewed (Positive):**
- Income distribution (most earn moderate, few earn very high)
- House prices
- Wait times
- Age at retirement

**Left-skewed (Negative):**
- Age at death in developed countries
- Easy exam scores (most score high)
- Failure time of well-designed products

**Symmetric:**
- Heights of adults
- IQ scores
- Measurement errors

---

### Kurtosis

**Kurtosis** measures the "tailedness" of a distribution—how heavy or light the tails are compared to a normal distribution.

<!-- IMAGE_PLACEHOLDER
Type: chart
Description: Three distribution curves overlaid showing: Leptokurtic (high kurtosis, peaked with heavy tails), Mesokurtic (normal kurtosis, standard bell curve), Platykurtic (low kurtosis, flat with light tails). All centered at the same point.
Data: Three curves with different tail weights
Style: Overlaid curves with legend, annotations for peak and tail characteristics
Filename: kurtosis_types.png
-->
![Types of kurtosis](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/kurtosis_types.png)

| Type | Excess Kurtosis | Shape |
|------|-----------------|-------|
| Leptokurtic | > 0 | Peaked, heavy tails, more outliers |
| Mesokurtic | ≈ 0 | Normal distribution shape |
| Platykurtic | < 0 | Flat, light tails, fewer outliers |

> 💡 **Note:** "Excess kurtosis" compares to the normal distribution (which has kurtosis = 3, so excess kurtosis = 0).

---

### Relationship Between Mean and Median

The relationship between mean and median indicates skewness:

- If **Mean > Median** → Right-skewed (positive)
- If **Mean < Median** → Left-skewed (negative)
- If **Mean ≈ Median** → Symmetric

---

## Worked Example

**Problem:**
A company recorded employee salaries (in thousands CHF):
45, 48, 52, 55, 58, 62, 65, 68, 72, 75, 78, 82, 150

Describe the shape of this distribution.

**Solution:**

### Step 1: Calculate Mean

$$
\bar{x} = \frac{45+48+52+55+58+62+65+68+72+75+78+82+150}{13} = \frac{930}{13} = 71.54
$$

### Step 2: Calculate Median

n = 13 (odd), median = 7th value

Sorted: 45, 48, 52, 55, 58, 62, **65**, 68, 72, 75, 78, 82, 150

**Median = 65**

### Step 3: Compare Mean and Median
- Mean (71.54) > Median (65)
- Difference: 71.54 - 65 = 6.54

### Step 4: Interpretation

**Shape:** Right-skewed (positive skewness)

**Evidence:**
- Mean > Median (pulled up by the outlier)
- The high salary (150) creates a right tail
- Most employees earn between 45-82k, but one earns 150k

**Implication:** The median (65k) better represents the "typical" salary than the mean (71.54k).

---

## Practice Problems

### Problem 1

For each scenario, predict whether the distribution would be left-skewed, right-skewed, or symmetric:

a) Scores on a very difficult exam
b) Heights of adult women
c) Time to complete a simple task (minimum time exists)
d) Age at first marriage in a developed country

<details>
<summary>💡 Show Solution</summary>

| Scenario | Predicted Shape | Reasoning |
|----------|-----------------|-----------|
| a) Very difficult exam | **Right-skewed** | Most score low, few score high |
| b) Heights of women | **Symmetric** | Natural biological variation |
| c) Time to complete task | **Right-skewed** | Minimum time exists, some take very long |
| d) Age at first marriage | **Right-skewed** | Minimum age (18+), some marry much later |

</details>

---

### Problem 2

A dataset has:
- Mean = 42
- Median = 45
- Mode = 48

What does this tell you about the distribution's shape?

<details>
<summary>💡 Show Solution</summary>

**Analysis:**
- Mean (42) < Median (45) < Mode (48)
- Mean is pulled to the left

**Conclusion:** The distribution is **left-skewed (negatively skewed)**.

The tail extends to the left, pulling the mean below the median. The mode (most frequent value) is the highest, indicating the peak is on the right side of the distribution.

</details>

---

### Problem 3

Two distributions have the following characteristics:

| Distribution | Mean | Median | Std Dev |
|--------------|------|--------|---------|
| A | 50 | 50 | 10 |
| B | 50 | 50 | 10 |

But A is leptokurtic and B is platykurtic. How would they differ?

<details>
<summary>💡 Show Solution</summary>

Even with the same mean, median, and standard deviation:

**Distribution A (Leptokurtic):**
- More peaked in the center
- Heavier tails (more extreme values)
- More likely to produce outliers
- Values more concentrated near mean AND in tails

**Distribution B (Platykurtic):**
- Flatter in the center
- Lighter tails (fewer extreme values)
- Less likely to produce outliers
- Values more evenly spread throughout

**Practical difference:**
If these represent investment returns, A would have more days with extreme gains or losses, while B would have more "average" days.

</details>

---

## Visual Recognition Guide

### Identifying Skewness from Histograms

| What You See | Skewness |
|--------------|----------|
| Peak on left, tail on right | Right-skewed (positive) |
| Peak on right, tail on left | Left-skewed (negative) |
| Mirror image, peak in center | Symmetric |

### Identifying Skewness from Box Plots

| What You See | Skewness |
|--------------|----------|
| Longer right whisker, median closer to Q1 | Right-skewed |
| Longer left whisker, median closer to Q3 | Left-skewed |
| Equal whiskers, median in center of box | Symmetric |

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Confusing skewness direction with tail direction.
> Right-skewed means the tail extends to the RIGHT, not that the peak is on the right.

> ⚠️ **Mistake 2:** Thinking kurtosis measures "peakedness" only.
> Kurtosis is more about tail heaviness than peak height.

> ⚠️ **Mistake 3:** Using mean for skewed data without acknowledging skewness.
> Always report median alongside mean for skewed distributions.

---

## Key Takeaways

> 🎯 **Remember:**
> - **Skewness** measures asymmetry (left, symmetric, right)
> - **Right-skewed:** Mean > Median, tail to right
> - **Left-skewed:** Mean < Median, tail to left
> - **Kurtosis** measures tail heaviness, not just peak height
> - For skewed data, median is often more representative than mean
> - Compare mean and median to quickly assess skewness

---

## Quick Reference

| Measure | Positive (+) | Zero (0) | Negative (-) |
|---------|--------------|----------|--------------|
| Skewness | Right tail | Symmetric | Left tail |
| Excess Kurtosis | Heavy tails | Normal tails | Light tails |

---

## Navigation

[← Quartiles & Box Plots](quartiles_boxplots.md) | [Module Index](index.md) | [Next Module: Correlation →](../03_correlation_covariance/index.md)

**Related Reference:** [Formula Glossary](../reference/formula_glossary.md)


