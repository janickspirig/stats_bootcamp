---
title: "I can interpret quartiles and box plots"
category: "Statistics Bootcamp"
module: 2
order: 3
---

# I can interpret quartiles and box plots

> 📚 **Overview:** Quartiles divide data into four equal parts, providing a robust way to describe data distribution and identify outliers.

---

## 📑 Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Key Concepts](#key-concepts)
3. [Worked Example](#worked-example)
4. [Practice Problems](#practice-problems)
5. [Interpreting Box Plots](#interpreting-box-plots)
6. [Common Mistakes to Avoid](#common-mistakes-to-avoid)
7. [Key Takeaways](#key-takeaways)

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate quartiles (Q1, Q2, Q3) for a dataset
- Calculate the interquartile range (IQR)
- Identify outliers using the IQR method
- Interpret and construct box plots
- Understand the five-number summary

---

## Key Concepts

### Quartiles

**Quartiles** divide ordered data into four equal parts.

| Quartile | Symbol | Meaning |
|----------|--------|---------|
| First Quartile | Q1 | 25th percentile (25% of data below) |
| Second Quartile | Q2 | 50th percentile = Median |
| Third Quartile | Q3 | 75th percentile (75% of data below) |

---

### Interquartile Range (IQR)

The **IQR** measures the spread of the middle 50% of data.

$$
IQR = Q3 - Q1
$$

**Properties:**
- Robust to outliers (unlike range)
- Measures variability of the central portion
- Used to identify outliers

---

### Outlier Detection

A data point is a potential **outlier** if it falls outside the "fences":

- **Lower fence:** Q1 - 1.5 × IQR
- **Upper fence:** Q3 + 1.5 × IQR

Any value below the lower fence or above the upper fence is flagged as an outlier.

---

### Five-Number Summary

The **five-number summary** provides a complete picture of data distribution:

1. Minimum
2. Q1 (First Quartile)
3. Q2 (Median)
4. Q3 (Third Quartile)
5. Maximum

---

### Box Plot (Box-and-Whisker Plot)

A **box plot** visualizes the five-number summary:

<!-- IMAGE_PLACEHOLDER
Type: diagram
Description: Labeled box plot showing all components: the box spanning Q1 to Q3, a line inside the box at the median (Q2), whiskers extending to min and max (or to fences), and individual points for outliers. Labels point to each component.
Data: Example with Q1=25, Q2=35, Q3=45, min=10, max=60, one outlier at 75
Style: Clean, labeled diagram with annotations
Filename: boxplot_labeled.png
-->
![Labeled box plot](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/boxplot_labeled.png)

**Components:**
- **Box:** Spans from Q1 to Q3 (contains middle 50%)
- **Line in box:** Median (Q2)
- **Whiskers:** Extend to min/max (or to fences)
- **Points:** Outliers beyond the fences

---

## Worked Example

**Problem:**
Calculate the five-number summary and IQR for this dataset, then identify any outliers:
12, 15, 18, 22, 25, 28, 30, 32, 35, 38, 72

**Solution:**

### Step 1: Order the Data (already ordered)
12, 15, 18, 22, 25, 28, 30, 32, 35, 38, 72

n = 11 values

### Step 2: Find the Median (Q2)
Middle position = (11+1)/2 = 6th value
**Q2 = 28**

### Step 3: Find Q1
Q1 is the median of the lower half: 12, 15, 18, 22, 25
Middle of 5 values = 3rd value
**Q1 = 18**

### Step 4: Find Q3
Q3 is the median of the upper half: 30, 32, 35, 38, 72
Middle of 5 values = 3rd value
**Q3 = 35**

### Step 5: Calculate IQR

$$
IQR = Q3 - Q1 = 35 - 18 = 17
$$

### Step 6: Calculate Fences
- Lower fence = 18 - 1.5 × 17 = 18 - 25.5 = **-7.5**
- Upper fence = 35 + 1.5 × 17 = 35 + 25.5 = **60.5**

### Step 7: Identify Outliers
Check each value against fences:
- Values below -7.5: None
- Values above 60.5: **72 is an outlier**

### Five-Number Summary

| Statistic | Value |
|-----------|-------|
| Minimum | 12 |
| Q1 | 18 |
| Median (Q2) | 28 |
| Q3 | 35 |
| Maximum | 72 |
| **IQR** | **17** |

**Outlier:** 72 (above upper fence of 60.5)

---

## Practice Problems

### Problem 1

Calculate Q1, Q2, Q3, and IQR for this dataset:
5, 8, 12, 15, 18, 22, 25, 28

<details>
<summary>💡 Show Solution</summary>

Data is already sorted, n = 8 (even)

**Median (Q2):**
Average of 4th and 5th values = (15 + 18) / 2 = **16.5**

**Q1 (median of lower half: 5, 8, 12, 15):**
Average of 2nd and 3rd = (8 + 12) / 2 = **10**

**Q3 (median of upper half: 18, 22, 25, 28):**
Average of 2nd and 3rd = (22 + 25) / 2 = **23.5**

**IQR:**

$$
IQR = 23.5 - 10 = 13.5
$$

</details>

---

### Problem 2

Given Q1 = 45, Q3 = 75, identify which of these values are outliers:
20, 30, 50, 80, 100, 125

<details>
<summary>💡 Show Solution</summary>

**Step 1: Calculate IQR**

$$
IQR = 75 - 45 = 30
$$

**Step 2: Calculate Fences**
- Lower fence = 45 - 1.5 × 30 = 45 - 45 = 0
- Upper fence = 75 + 1.5 × 30 = 75 + 45 = 120

**Step 3: Check Each Value**

| Value | Below 0? | Above 120? | Outlier? |
|-------|----------|------------|----------|
| 20 | No | No | No |
| 30 | No | No | No |
| 50 | No | No | No |
| 80 | No | No | No |
| 100 | No | No | No |
| 125 | No | **Yes** | **Yes** |

**Answer:** Only 125 is an outlier.

</details>

---

### Problem 3

Two datasets have the following box plot statistics:

Dataset A: Min=10, Q1=25, Median=35, Q3=45, Max=60
Dataset B: Min=20, Q1=30, Median=35, Q3=40, Max=50

Which dataset has more variability? Explain using IQR.

<details>
<summary>💡 Show Solution</summary>

**IQR for Dataset A:**

$$
IQR_A = 45 - 25 = 20
$$

**IQR for Dataset B:**

$$
IQR_B = 40 - 30 = 10
$$

**Answer:** Dataset A has more variability:
- Dataset A: IQR = 20, Range = 50
- Dataset B: IQR = 10, Range = 30

Dataset A is more spread out in both the middle 50% and overall.

</details>

---

## Interpreting Box Plots

### Comparing Distributions

<!-- IMAGE_PLACEHOLDER
Type: chart
Description: Side-by-side box plots for three groups (A, B, C) showing: Group A is left-skewed, Group B is symmetric, Group C is right-skewed. Different medians and spreads visible.
Data: Three box plots with different shapes
Style: Labeled with group names, clear comparison
Filename: boxplot_comparison.png
-->
![Box plot comparison](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/boxplot_comparison.png)

**What to look for:**
- **Position:** Higher/lower median indicates different centers
- **Box width:** Wider box = more variability (larger IQR)
- **Whisker length:** Unequal whiskers suggest skewness
- **Outliers:** Points outside whiskers indicate unusual values

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Including the median when calculating Q1 and Q3.
> For odd n, the median is NOT included in either half.

> ⚠️ **Mistake 2:** Forgetting to sort the data first.
> Quartiles are based on ordered data!

> ⚠️ **Mistake 3:** Using the wrong multiplier for outliers.
> The standard multiplier is 1.5 × IQR, not 1 or 2.

> ⚠️ **Mistake 4:** Confusing IQR with range.
> Range = Max - Min; IQR = Q3 - Q1

---

## Key Takeaways

> 🎯 **Remember:**
> - **Quartiles** divide data into four equal parts
> - **Q2 = Median** (50th percentile)
> - **IQR = Q3 - Q1** measures spread of middle 50%
> - **Outliers** are beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR
> - **Box plots** visualize the five-number summary
> - Quartiles and IQR are robust to outliers

---

## Quick Reference

| Measure | Definition |
|---------|------------|
| Q1 | 25th percentile |
| Q2 (Median) | 50th percentile |
| Q3 | 75th percentile |
| IQR | Q3 - Q1 |
| Lower Fence | Q1 - 1.5 × IQR |
| Upper Fence | Q3 + 1.5 × IQR |

---

## Navigation

[← Variance & Std Dev](variance_stddev.md) | [Module Index](index.md) | [Next: Skewness & Kurtosis →](skewness_kurtosis.md)

**Related Reference:** [Formula Glossary](../reference/formula_glossary.md)


