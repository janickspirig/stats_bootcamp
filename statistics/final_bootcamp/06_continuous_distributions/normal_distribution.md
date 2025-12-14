---
title: "I can work with the Normal distribution"
category: "Statistics Bootcamp"
module: 6
order: 1
---

# I can work with the Normal distribution

> 📚 **Overview:** The Normal (Gaussian) distribution is the most important distribution in statistics—essential for understanding sampling distributions and inference.

---

## 📑 Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Key Concepts](#key-concepts)
3. [Worked Example](#worked-example)
4. [Practice Problems](#practice-problems)
5. [Common Applications](#common-applications)
6. [Key Takeaways](#key-takeaways)

---

## Learning Objectives

After completing this section, you will be able to:
- Recognize Normal distribution properties
- Apply the 68-95-99.7 rule (Empirical Rule)
- Understand when the Normal distribution applies
- Identify mean and standard deviation from a Normal curve

---

## Key Concepts

### The Normal Distribution

$$
X \sim N(\mu, \sigma^2)
$$

**Parameters:**
- μ = mean (center of distribution)
- σ = standard deviation (spread)
- σ² = variance

---

### Properties

1. **Symmetric** around the mean
2. **Bell-shaped** curve
3. **Mean = Median = Mode** (all at center)
4. **Asymptotic** - tails approach but never touch x-axis
5. **Total area under curve = 1**

<!-- IMAGE_PLACEHOLDER
Type: chart
Description: Normal distribution curve with mean μ marked at center. Shows symmetry with identical areas on both sides. Labels showing μ (mean), σ (standard deviation units from mean).
Data: Standard normal with μ=0, σ=1
Style: Clean bell curve with labeled components
Filename: normal_curve.png
-->
![Normal distribution curve](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/normal_curve.png)

---

### The 68-95-99.7 Rule (Empirical Rule)

For a Normal distribution:

| Interval | Percentage of Data |
|----------|-------------------|
| μ ± 1σ | **68%** |
| μ ± 2σ | **95%** |
| μ ± 3σ | **99.7%** |

<!-- IMAGE_PLACEHOLDER
Type: chart
Description: Normal curve with shaded regions showing 68% within ±1σ, 95% within ±2σ, and 99.7% within ±3σ. Percentages labeled in each region.
Data: Standard normal with marked regions
Style: Progressively shaded regions with percentage labels
Filename: empirical_rule.png
-->
![Empirical rule (68-95-99.7)](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/empirical_rule.png)

---

### Standard Normal Distribution

The **Standard Normal** is a special case with μ = 0 and σ = 1:

$$
Z \sim N(0, 1)
$$

We convert any Normal to Standard Normal using z-scores (covered next section).

---

## Worked Example

**Problem:**
IQ scores are normally distributed with μ = 100 and σ = 15.

a) What percentage of people have IQs between 85 and 115?
b) What percentage have IQs above 130?
c) Between what values do the middle 95% of IQs fall?

**Solution:**

### Part a: Between 85 and 115

Notice: 85 = 100 - 15 = μ - 1σ
And: 115 = 100 + 15 = μ + 1σ

By the 68-95-99.7 rule: **68%** of people have IQs between 85 and 115.

### Part b: Above 130

130 = 100 + 30 = μ + 2σ

By the Empirical Rule:
- 95% fall within ±2σ
- 5% fall outside
- Half of 5% (2.5%) are above μ + 2σ

**Answer: About 2.5%** have IQs above 130.

### Part c: Middle 95%

By the Empirical Rule, 95% fall within μ ± 2σ:
- Lower: 100 - 2(15) = 70
- Upper: 100 + 2(15) = 130

**Answer:** 95% of IQs fall between 70 and 130.

---

## Practice Problems

### Problem 1

Adult heights are normally distributed with μ = 170 cm and σ = 10 cm.

a) What percentage of adults are between 160 cm and 180 cm?
b) What percentage are shorter than 150 cm?
c) What height is at the 97.5th percentile?

<details>
<summary>💡 Show Solution</summary>

**a) Between 160 and 180 cm:**
160 = 170 - 10 = μ - 1σ
180 = 170 + 10 = μ + 1σ
By Empirical Rule: **68%**

**b) Shorter than 150 cm:**
150 = 170 - 20 = μ - 2σ
95% are within ±2σ, so 5% are outside
Half (2.5%) are below μ - 2σ
**Answer: 2.5%**

**c) 97.5th percentile:**
The 97.5th percentile is at μ + 2σ (since 2.5% are above)
= 170 + 2(10) = **190 cm**

</details>

---

### Problem 2

A machine fills bottles with a mean of 500 ml and standard deviation of 5 ml (normally distributed). 

a) What percentage of bottles contain between 495 and 505 ml?
b) If 10,000 bottles are filled, approximately how many contain less than 490 ml?

<details>
<summary>💡 Show Solution</summary>

**a) Between 495 and 505 ml:**
495 = 500 - 5 = μ - 1σ
505 = 500 + 5 = μ + 1σ
**Answer: 68%**

**b) Less than 490 ml:**
490 = 500 - 10 = μ - 2σ
2.5% fall below μ - 2σ
0.025 × 10,000 = **250 bottles**

</details>

---

### Problem 3

Exam scores have μ = 75 and σ = 8, normally distributed.

a) Using the Empirical Rule, between what scores do 99.7% of students fall?
b) If the passing grade is 59, approximately what percentage pass?

<details>
<summary>💡 Show Solution</summary>

**a) 99.7% interval:**
μ ± 3σ = 75 ± 3(8) = 75 ± 24
**Answer: Between 51 and 99**

**b) Pass rate (score ≥ 59):**
59 = 75 - 16 = μ - 2σ
Only 2.5% score below μ - 2σ
So 97.5% score at or above 59
**Answer: About 97.5% pass**

</details>

---

## Common Applications

The Normal distribution appears in:

| Application | Example |
|-------------|---------|
| **Physical measurements** | Heights, weights, blood pressure |
| **Test scores** | IQ, SAT, GMAT |
| **Manufacturing** | Product dimensions, fill weights |
| **Finance** | Daily stock returns (approximately) |
| **Sample means** | Central Limit Theorem (next module) |

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Assuming all data is Normal.
> Many real datasets are skewed or have outliers.

> ⚠️ **Mistake 2:** Confusing σ with σ².
> Standard deviation (σ) is in the same units as data; variance (σ²) is in squared units.

> ⚠️ **Mistake 3:** Forgetting the Empirical Rule is approximate.
> For precise calculations, use z-scores and tables.

---

## Key Takeaways

> 🎯 **Remember:**
> - Normal distribution is symmetric, bell-shaped
> - Defined by mean (μ) and standard deviation (σ)
> - **68-95-99.7 Rule:** 68% within ±1σ, 95% within ±2σ, 99.7% within ±3σ
> - Standard Normal has μ = 0, σ = 1
> - Many natural phenomena follow Normal distribution

---

## Navigation

[← Module Index](index.md) | [Next: Z-Scores →](z_scores.md)

**Related Reference:** [Distribution Table](../reference/distribution_table.md) | [Statistical Tables](../reference/statistical_tables.md)


