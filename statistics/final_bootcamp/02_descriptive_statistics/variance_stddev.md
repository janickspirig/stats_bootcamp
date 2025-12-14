---
title: "I can calculate variance and standard deviation"
category: "Statistics Bootcamp"
module: 2
order: 2
---

# I can calculate variance and standard deviation

> 📚 **Overview:** Variance and standard deviation measure how spread out data is around the mean. Master these essential measures of dispersion.

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
- Calculate sample and population variance
- Calculate sample and population standard deviation
- Understand why we divide by (n-1) for sample variance
- Interpret these measures in context
- Calculate and use the coefficient of variation

---

## Key Concepts

### Variance

**Variance** measures the average squared deviation from the mean.

**Sample Variance:**

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

**Sample Variance (computational shortcut):**

$$
s^2 = \frac{1}{n-1}\left(\sum_{i=1}^{n} x_i^2 - \frac{\left(\sum_{i=1}^{n} x_i\right)^2}{n}\right)
$$

Use this form when you already have \(\\sum x_i\) and \(\\sum x_i^2\) from a table.

**Population Variance:**

$$
\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2
$$

> 💡 **Why n-1?** This is called Bessel's correction. It makes the sample variance an unbiased estimator of the population variance.

---

### Standard Deviation

**Standard deviation** is the square root of variance, in the same units as the original data.

**Sample Standard Deviation:**

$$
s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}
$$

**Population Standard Deviation:**

$$
\sigma = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2}
$$

---

### Mean Absolute Deviation (MAD)

The **Mean Absolute Deviation (MAD)** measures the average absolute distance from the mean (in the same units as the data).

$$
MAD = \frac{1}{n}\sum_{i=1}^{n} |x_i - \bar{x}|
$$

**When it’s useful:** Compared to variance, MAD is often easier to interpret because it’s not in squared units.

---

### Coefficient of Variation

The **CV** expresses standard deviation as a percentage of the mean, allowing comparison across different scales.

$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

**When to use:**
- Comparing variability of datasets with different units
- Comparing variability of datasets with different means

---

## Worked Example

**Problem:**
Calculate the sample variance and standard deviation for the following customer ages:
22, 25, 27, 30, 31, 35

**Solution:**

### Step 1: Calculate the Mean

$$
\bar{x} = \frac{22 + 25 + 27 + 30 + 31 + 35}{6} = \frac{170}{6} = 28.33
$$

### Step 2: Build a Calculation Table

| i | $x_i$ | $x_i - \bar{x}$ | $|x_i - \bar{x}|$ | $(x_i - \bar{x})^2$ |
|---|-------|-----------------|------------------|---------------------|
| 1 | 22 | 22 - 28.33 = -6.33 | 6.33 | 40.07 |
| 2 | 25 | 25 - 28.33 = -3.33 | 3.33 | 11.09 |
| 3 | 27 | 27 - 28.33 = -1.33 | 1.33 | 1.77 |
| 4 | 30 | 30 - 28.33 = 1.67 | 1.67 | 2.79 |
| 5 | 31 | 31 - 28.33 = 2.67 | 2.67 | 7.13 |
| 6 | 35 | 35 - 28.33 = 6.67 | 6.67 | 44.49 |
| **Σ** | 170 | **0.02** ≈ 0 | **22.00** | **107.34** |

> 💡 **Check:** The sum of deviations should be approximately 0 (rounding error is acceptable).

### Step 2b: Calculate MAD

$$
MAD = \frac{\sum |x_i - \bar{x}|}{n} = \frac{22.00}{6} = 3.67
$$

### Step 3: Calculate Sample Variance

$$
s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1} = \frac{107.34}{6-1} = \frac{107.34}{5} = 21.47
$$

### Step 4: Calculate Sample Standard Deviation

$$
s = \sqrt{21.47} = 4.63 \text{ years}
$$

### Interpretation
The ages deviate from the mean (28.33) by approximately 4.63 years on average.

MAD interpretation: On average, ages are about **3.67 years** away from the mean (using absolute deviations).

---

## Practice Problems

### Problem 1

Calculate the sample variance and standard deviation for these exam scores:
72, 78, 82, 85, 88, 90

<details>
<summary>💡 Show Solution</summary>

**Step 1: Mean**

$$
\bar{x} = \frac{72 + 78 + 82 + 85 + 88 + 90}{6} = \frac{495}{6} = 82.5
$$

**Step 2: Calculation Table**

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|-------|-----------------|---------------------|
| 72 | -10.5 | 110.25 |
| 78 | -4.5 | 20.25 |
| 82 | -0.5 | 0.25 |
| 85 | 2.5 | 6.25 |
| 88 | 5.5 | 30.25 |
| 90 | 7.5 | 56.25 |
| **Σ** | 0 | **223.50** |

**Step 3: Variance**

$$
s^2 = \frac{223.50}{5} = 44.70
$$

**Step 4: Standard Deviation**

$$
s = \sqrt{44.70} = 6.69 \text{ points}
$$

</details>

---

### Problem 2

Two stocks have the following monthly returns:
- Stock A: Mean = 5%, Standard Deviation = 8%
- Stock B: Mean = 12%, Standard Deviation = 15%

Which stock has more relative variability?

<details>
<summary>💡 Show Solution</summary>

Calculate the Coefficient of Variation for each:

**Stock A:**

$$
CV_A = \frac{8\%}{5\%} \times 100\% = 160\%
$$

**Stock B:**

$$
CV_B = \frac{15\%}{12\%} \times 100\% = 125\%
$$

**Answer:** Stock A has higher relative variability (160% vs 125%) even though Stock B has a higher absolute standard deviation.

This means Stock A's returns are more volatile relative to its average return.

</details>

---

### Problem 3

Given the following data: 10, 12, 14, 16, 18

Calculate both the sample variance (using n-1) and the population variance (using n). What's the difference?

<details>
<summary>💡 Show Solution</summary>

**Mean:**

$$
\bar{x} = \frac{10 + 12 + 14 + 16 + 18}{5} = \frac{70}{5} = 14
$$

**Sum of Squared Deviations:**

| $x_i$ | $(x_i - 14)^2$ |
|-------|----------------|
| 10 | 16 |
| 12 | 4 |
| 14 | 0 |
| 16 | 4 |
| 18 | 16 |
| **Σ** | **40** |

**Sample Variance (n-1):**

$$
s^2 = \frac{40}{5-1} = \frac{40}{4} = 10
$$

**Population Variance (n):**

$$
\sigma^2 = \frac{40}{5} = 8
$$

**Difference:** Sample variance (10) is larger than population variance (8). This is because dividing by n-1 corrects for the bias that occurs when estimating population variance from a sample.

</details>

---

## Visualization

<!-- IMAGE_PLACEHOLDER
Type: chart
Description: Two normal distributions overlaid, both centered at mean=50, but one with small standard deviation (narrow, tall curve) and one with large standard deviation (wide, flat curve). Labels showing "Low variance" and "High variance" for each.
Data: Both curves centered at 50, one with σ=5, one with σ=15
Style: Two distinct colors, legend, labeled axes
Filename: variance_comparison.png
-->
![Variance comparison](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/variance_comparison.png)

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Dividing by n instead of (n-1) for sample variance.
> Remember: sample variance uses (n-1) in the denominator!

> ⚠️ **Mistake 2:** Forgetting to square the deviations.
> The sum of $(x_i - \bar{x})$ is always 0; you need $(x_i - \bar{x})^2$.

> ⚠️ **Mistake 3:** Reporting variance when standard deviation is more interpretable.
> Variance is in squared units; standard deviation is in original units.

> ⚠️ **Mistake 4:** Not checking that $\sum(x_i - \bar{x}) \approx 0$.
> This is a great error check for your calculation table.

---

## Key Takeaways

> 🎯 **Remember:**
> - **Variance** = average squared deviation from mean
> - **Standard deviation** = square root of variance (same units as data)
> - Use **n-1** for samples, **n** for populations
> - **CV** allows comparison across different scales
> - Build calculation tables to avoid errors

---

## Quick Check

1) True/False: Standard deviation is in the same units as the original data.
2) Fill in the blank: For a sample variance, the denominator is ___.
3) Which measure is easier to interpret in the original units: variance or MAD?

<details>
<summary>Answers</summary>

1) True.
2) n − 1.
3) MAD (and also standard deviation) are in the original units; variance is in squared units.

</details>

## Quick Reference

| Measure | Sample Formula | Population Formula |
|---------|---------------|-------------------|
| Variance | s² = Σ(xᵢ-x̄)² / (n-1) | σ² = Σ(xᵢ-μ)² / N |
| Std Dev | s = √s² | σ = √σ² |
| CV | CV = (s / x̄) × 100% | - |

---

## Navigation

[← Mean, Median, Mode](mean_median_mode.md) | [Module Index](index.md) | [Next: Quartiles & Box Plots →](quartiles_boxplots.md)

**Related Reference:** [Formula Glossary](../reference/formula_glossary.md)


