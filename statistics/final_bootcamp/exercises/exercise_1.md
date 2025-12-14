---
title: "Exercise 1: Descriptive Statistics"
category: "Statistics Bootcamp"
module: 98
order: 1
---

# Exercise 1: Descriptive Statistics

> 📚 **Overview:** Practice calculating mean, variance, quartiles, and more.

Practice problems covering data types, central tendency, and dispersion.

---

## Topics Covered
- Data types and scales of measurement
- Mean, median, mode
- Variance, standard deviation
- Quartiles and box plots

---

## Problem 1

A company recorded the following sales figures (in thousands CHF) for 8 months:
45, 52, 48, 55, 60, 42, 58, 50

Calculate:
a) The mean
b) The median
c) The sample variance
d) The sample standard deviation

<details>
<summary>💡 Show Solution</summary>

**a) Mean:**

$$
\bar{x} = \frac{45+52+48+55+60+42+58+50}{8} = \frac{410}{8} = 51.25
$$

**b) Median:**
Sorted: 42, 45, 48, 50, 52, 55, 58, 60
Median = (50 + 52)/2 = 51

**c) Sample Variance:**

| x | x - 51.25 | (x - 51.25)² |
|---|-----------|--------------|
| 45 | -6.25 | 39.0625 |
| 52 | 0.75 | 0.5625 |
| 48 | -3.25 | 10.5625 |
| 55 | 3.75 | 14.0625 |
| 60 | 8.75 | 76.5625 |
| 42 | -9.25 | 85.5625 |
| 58 | 6.75 | 45.5625 |
| 50 | -1.25 | 1.5625 |
| Σ | | 273.50 |

$$
s^2 = \frac{273.50}{7} = 39.07
$$

**d) Standard Deviation:**

$$
s = \sqrt{39.07} = 6.25
$$

</details>

---

## Problem 2

Classify each variable:
a) Employee satisfaction rating (Very dissatisfied to Very satisfied)
b) Annual revenue in CHF
c) Product category (Electronics, Clothing, Food)
d) Temperature in Celsius

<details>
<summary>💡 Show Solution</summary>

| Variable | Qual/Quant | Scale |
|----------|------------|-------|
| a) Satisfaction | Qualitative | Ordinal |
| b) Revenue | Quantitative | Ratio |
| c) Category | Qualitative | Nominal |
| d) Temperature (°C) | Quantitative | Interval |

</details>

---

## Problem 3

Calculate the coefficient of variation for:
- Dataset A: Mean = 50, SD = 10
- Dataset B: Mean = 200, SD = 30

Which dataset has more relative variability?

<details>
<summary>💡 Show Solution</summary>

**CV = (SD / Mean) × 100%**

CV_A = (10/50) × 100% = 20%
CV_B = (30/200) × 100% = 15%

**Dataset A has more relative variability (20% vs 15%)**

</details>

---

## Problem 4 (Frequency Table — Übungsblatt style)

A survey of 2567 households recorded persons per household:

| Persons per household | Count |
|---|---:|
| 1 | 457 |
| 2 | 628 |
| 3 | 612 |
| 4 | 526 |
| ≥ 5 | 344 |

Calculate:
a) Relative frequencies \(f(x_i)\)
b) Cumulative distribution \(F(x_i)\)
c) How many households have ≤ 3 persons?
d) The mean number of persons per household (use midpoint 6 for the “≥ 5” category)
e) One sentence: why might the mean be biased here?

<details>
<summary>💡 Show Solution</summary>

**a)–b) Relative and cumulative frequencies**

Total \(n = 2567\).

| Persons | Count | \(f(x_i)=\\frac{\\text{count}}{n}\) | \(F(x_i)\) |
|---|---:|---:|---:|
| 1 | 457 | 0.178 | 0.178 |
| 2 | 628 | 0.245 | 0.423 |
| 3 | 612 | 0.238 | 0.661 |
| 4 | 526 | 0.205 | 0.866 |
| ≥ 5 | 344 | 0.134 | 1.000 |

**c) Households with ≤ 3 persons**

\(457 + 628 + 612 = 1697\) households (equivalently \(0.661 \\times 2567 \\approx 1697\)).

**d) Mean (with midpoint 6 for ≥5)**

Let \(x\) be persons per household and approximate the last category by 6.

$$
\\bar{x} = \\frac{1\\cdot 457 + 2\\cdot 628 + 3\\cdot 612 + 4\\cdot 526 + 6\\cdot 344}{2567}
$$

Compute the numerator:
- \(1\\cdot457 = 457\)
- \(2\\cdot628 = 1256\)
- \(3\\cdot612 = 1836\)
- \(4\\cdot526 = 2104\)
- \(6\\cdot344 = 2064\)

Sum = \(457 + 1256 + 1836 + 2104 + 2064 = 7717\)

$$
\\bar{x} = \\frac{7717}{2567} = 3.01
$$

**Answer:** Mean ≈ **3.01 persons** per household.

**e) Bias explanation (one sentence)**

The “≥5” category is open-ended; using a midpoint (6) may under- or over-estimate the true average if many households have much more than 6 persons.

</details>

---

## Problem 5 (MAD)

For the dataset: 22, 25, 27, 30, 31, 35

Calculate:
a) The mean \(\\bar{x}\)
b) The MAD \(= \\frac{1}{n}\\sum |x_i-\\bar{x}|\)

<details>
<summary>💡 Show Solution</summary>

**a) Mean**

$$
\\bar{x} = \\frac{170}{6} = 28.33
$$

**b) MAD**

Absolute deviations: 6.33, 3.33, 1.33, 1.67, 2.67, 6.67

$$
MAD = \\frac{6.33+3.33+1.33+1.67+2.67+6.67}{6} = \\frac{22.00}{6} = 3.67
$$

**Business interpretation:** Typical customer age differs from the mean by about **3.7 years**.

</details>

---

## Problem 6 (Weighted Mean)

A retailer sells three product lines with different unit margins:

| Product | Units sold | Margin per unit (CHF) |
|---|---:|---:|
| A | 120 | 8 |
| B | 60 | 15 |
| C | 20 | 40 |

Calculate the **weighted mean margin** per unit sold.

<details>
<summary>💡 Show Solution</summary>

Total units = 120 + 60 + 20 = 200

Total margin = \(120\\cdot 8 + 60\\cdot 15 + 20\\cdot 40 = 960 + 900 + 800 = 2660\)

$$
\\bar{x}_w = \\frac{2660}{200} = 13.30
$$

**Answer:** Weighted mean margin = **CHF 13.30** per unit.

Business interpretation: This is the average margin you actually earn per unit after accounting for the sales mix.

</details>

---

## Problem 7 (Box Plot / Outliers)

Monthly delivery times (days): 1, 2, 2, 2, 3, 3, 3, 4, 6, 12

Calculate:
a) Q1, median, Q3
b) IQR
c) Lower/upper fences (1.5×IQR)
d) Which values are outliers?

<details>
<summary>💡 Show Solution</summary>

Sorted data: 1, 2, 2, 2, 3, 3, 3, 4, 6, 12 (n=10)

Median = average of 5th and 6th values = (3 + 3)/2 = 3

Lower half: 1, 2, 2, 2, 3 → Q1 = 2  
Upper half: 3, 3, 4, 6, 12 → Q3 = 4

IQR = Q3 − Q1 = 4 − 2 = 2

Lower fence = 2 − 1.5×2 = -1  
Upper fence = 4 + 1.5×2 = 7

Outliers: values > 7 → **12** is an outlier.

Business interpretation: One extreme delay (12 days) likely reflects an exceptional incident and should be investigated separately.

</details>

---

## Problem 8 (Skewness: mean vs median)

A store’s daily sales (CHF) over 9 days are:
1200, 1300, 1250, 1400, 1350, 1280, 1320, 1270, 6000

Without fully computing all shape measures:
a) Is the distribution likely left-skewed, symmetric, or right-skewed?
b) Which is more representative here: mean or median?

<details>
<summary>💡 Show Solution</summary>

a) **Right-skewed** because of one very large outlier (6000).
b) **Median** is more representative because it is robust to outliers; the mean will be pulled upward by the 6000 day.

Business interpretation: Use the median for “typical day” planning (staffing/inventory), and treat extreme days separately.

</details>

---

## Problem 9 (Sample vs population variance)

For the dataset: 4, 6, 8, 10

Calculate:
a) The **population** variance \(\\sigma^2\\)  
b) The **sample** variance \(s^2\\)  
c) One sentence: why is \(s^2\\) typically larger?

<details>
<summary>💡 Show Solution</summary>

Mean:

$$
\\bar{x} = \\frac{4+6+8+10}{4} = 7
$$

Deviations: -3, -1, 1, 3 → squared: 9, 1, 1, 9 → sum = 20.

a) Population variance:

$$
\\sigma^2 = \\frac{20}{4} = 5
$$

b) Sample variance:

$$
s^2 = \\frac{20}{3} = 6.6667
$$

c) Because dividing by \(n-1\\) (instead of n) corrects the downward bias in estimating the population variance from a sample.

</details>

---

## Problem 10 (Mean and variance from a frequency table)

A company records the number of customer complaints per day:

| Complaints \(x_i\) | Count \(n_i\) |
|---|---:|
| 0 | 10 |
| 1 | 20 |
| 2 | 15 |
| 3 | 5 |

Compute:
a) The mean \(\\bar{x}\\)  
b) The sample variance \(s^2\\) (show a calculation table)

<details>
<summary>💡 Show Solution</summary>

Total \(n=50\\).

Mean:

$$
\\bar{x} = \\frac{0\\cdot 10 + 1\\cdot 20 + 2\\cdot 15 + 3\\cdot 5}{50}
= \\frac{65}{50}
= 1.3
$$

Variance table:

| \(x_i\) | \(n_i\) | \(x_i-\\bar{x}\) | \((x_i-\\bar{x})^2\) | \(n_i(x_i-\\bar{x})^2\) |
|---:|---:|---:|---:|---:|
| 0 | 10 | -1.3 | 1.69 | 16.90 |
| 1 | 20 | -0.3 | 0.09 | 1.80 |
| 2 | 15 | 0.7 | 0.49 | 7.35 |
| 3 | 5 | 1.7 | 2.89 | 14.45 |
| **Σ** | **50** |  |  | **40.50** |

Sample variance:

$$
s^2 = \\frac{40.50}{49} = 0.8265
$$

</details>

---

## Problem 11 (MAD with table — Übungsblatt style)

For the dataset: 17, 18, 19, 19, 21, 22, 25

Compute:
a) The mean \(\\bar{x}\\)  
b) The MAD \(= \\frac{1}{n}\\sum |x_i-\\bar{x}|\\) using a table

<details>
<summary>💡 Show Solution</summary>

Mean:

$$
\\bar{x} = \\frac{17+18+19+19+21+22+25}{7} = \\frac{141}{7} = 20.1429
$$

| \(x_i\) | \(x_i-\\bar{x}\) | \(|x_i-\\bar{x}|\) |
|---:|---:|---:|
| 17 | -3.1429 | 3.1429 |
| 18 | -2.1429 | 2.1429 |
| 19 | -1.1429 | 1.1429 |
| 19 | -1.1429 | 1.1429 |
| 21 | 0.8571 | 0.8571 |
| 22 | 1.8571 | 1.8571 |
| 25 | 4.8571 | 4.8571 |
| **Σ** |  | **15.1429** |

$$
MAD = \\frac{15.1429}{7} = 2.1633
$$

</details>

---

## Problem 12 (Interpretation drill)

You computed for a dataset:
- Mean = 50
- Standard deviation = 10
- MAD = 8

Write **one** business interpretation sentence for each measure.

<details>
<summary>💡 Show Solution</summary>

- Mean: “On average, the outcome is about 50 (units).”
- SD: “Typical observations deviate from the mean by about 10 (units).”
- MAD: “On average, observations differ from the mean by about 8 (units) in absolute terms.”

</details>

## Related Module

[Module 02: Descriptive Statistics](../02_descriptive_statistics/index.md)

---

## Navigation

[← Exercises Index](index.md) | [Exercise 2 →](exercise_2.md)


