---
title: "I can calculate and interpret z-scores"
category: "Statistics Bootcamp"
module: 6
order: 2
---

# I can calculate and interpret z-scores

> 📚 **Overview:** Z-scores standardize values so you can compare data across different scales and use standard normal tables.

Z-scores standardize values, allowing comparison across different Normal distributions.

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate z-scores from raw values
- Convert z-scores back to raw values
- Interpret what a z-score means
- Compare values from different distributions

---

## Key Concepts

### The Z-Score Formula

$$z = \frac{x - \mu}{\sigma}$$

Where:
- $x$ = raw value
- $\mu$ = mean
- $\sigma$ = standard deviation
- $z$ = standardized score

---

### Interpretation

A z-score tells you **how many standard deviations** a value is from the mean.

| Z-Score | Interpretation |
|---------|----------------|
| z = 0 | Value equals the mean |
| z = 1 | Value is 1 standard deviation above mean |
| z = -1 | Value is 1 standard deviation below mean |
| z = 2 | Value is 2 standard deviations above mean |
| z = -2.5 | Value is 2.5 standard deviations below mean |

---

### Converting Back to Raw Scores

$$x = \mu + z \cdot \sigma$$

---

## Worked Example

**Problem:**
Exam scores are normally distributed with μ = 72 and σ = 8.

a) What is the z-score for a student who scored 88?
b) What is the z-score for a student who scored 60?
c) What raw score corresponds to z = 1.5?
d) Which is better: scoring 88 on this exam or 125 on an exam with μ = 110, σ = 12?

**Solution:**

### Part a: Z-score for 88

$$z = \frac{88 - 72}{8} = \frac{16}{8} = 2.0$$

**Interpretation:** A score of 88 is 2 standard deviations above the mean.

### Part b: Z-score for 60

$$z = \frac{60 - 72}{8} = \frac{-12}{8} = -1.5$$

**Interpretation:** A score of 60 is 1.5 standard deviations below the mean.

### Part c: Raw score for z = 1.5

$$x = 72 + 1.5 \times 8 = 72 + 12 = 84$$

**Answer:** z = 1.5 corresponds to a score of 84.

### Part d: Comparing scores

**Exam 1:** Score = 88, z = 2.0 (calculated above)

**Exam 2:** Score = 125, z = (125 - 110) / 12 = 15 / 12 = 1.25

**Comparison:** z = 2.0 > z = 1.25

**Answer:** Scoring 88 on the first exam is relatively better, even though 125 > 88 in raw terms. The first score is 2 standard deviations above average vs only 1.25.

---

## Practice Problems

### Problem 1

Heights of adult women are normally distributed with μ = 165 cm and σ = 6 cm.

a) What is the z-score for a woman who is 177 cm tall?
b) What is the z-score for a woman who is 159 cm tall?
c) What height corresponds to z = -2?

<details>
<summary>💡 Show Solution</summary>

**a) Z-score for 177 cm:**
$$z = \frac{177 - 165}{6} = \frac{12}{6} = 2.0$$

**b) Z-score for 159 cm:**
$$z = \frac{159 - 165}{6} = \frac{-6}{6} = -1.0$$

**c) Height for z = -2:**
$$x = 165 + (-2)(6) = 165 - 12 = 153 \text{ cm}$$

</details>

---

### Problem 2

Two students take different math tests:
- Anna: Score = 78, Class mean = 70, SD = 8
- Bob: Score = 85, Class mean = 75, SD = 10

Who performed better relative to their class?

<details>
<summary>💡 Show Solution</summary>

**Anna's z-score:**
$$z_A = \frac{78 - 70}{8} = \frac{8}{8} = 1.0$$

**Bob's z-score:**
$$z_B = \frac{85 - 75}{10} = \frac{10}{10} = 1.0$$

**Answer:** Both performed equally well relative to their classes (both are exactly 1 standard deviation above their class mean).

</details>

---

### Problem 3

Battery life for a smartphone is normally distributed with μ = 10 hours and σ = 1.5 hours.

a) A phone lasts 12.5 hours. What's its z-score?
b) What battery life corresponds to z = -1.5?
c) A phone is in the bottom 2.5% for battery life. Approximately what z-score and battery life does it have?

<details>
<summary>💡 Show Solution</summary>

**a) Z-score for 12.5 hours:**
$$z = \frac{12.5 - 10}{1.5} = \frac{2.5}{1.5} = 1.67$$

**b) Battery life for z = -1.5:**
$$x = 10 + (-1.5)(1.5) = 10 - 2.25 = 7.75 \text{ hours}$$

**c) Bottom 2.5%:**
By Empirical Rule, bottom 2.5% is approximately at z = -2
$$x = 10 + (-2)(1.5) = 10 - 3 = 7 \text{ hours}$$

</details>

---

## Why Z-Scores Matter

1. **Standardization:** Converts any Normal to Standard Normal
2. **Comparison:** Compare values from different distributions
3. **Probability:** Use z-tables to find probabilities
4. **Percentiles:** Identify position in distribution
5. **Outlier detection:** |z| > 2 or 3 suggests unusual values

---

## Z-Score Quick Reference

| Z-Score | Approximate Percentile |
|---------|----------------------|
| -3 | 0.1% |
| -2 | 2.5% |
| -1 | 16% |
| 0 | 50% |
| +1 | 84% |
| +2 | 97.5% |
| +3 | 99.9% |

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Subtracting mean from wrong position.
> It's (x - μ), not (μ - x). Order matters for the sign.

> ⚠️ **Mistake 2:** Using variance instead of standard deviation.
> The formula uses σ (SD), not σ² (variance).

> ⚠️ **Mistake 3:** Forgetting z-scores can be negative.
> Values below the mean have negative z-scores.

---

## Key Takeaways

- **Z-score** = (value - mean) / standard deviation
- Tells you how many SDs from the mean
- Positive z → above mean; Negative z → below mean
- **Essential for comparing** scores from different scales
- **Key bridge** to probability calculations

---

## Navigation

[← Normal Distribution](normal_distribution.md) | [Module Index](index.md) | [Next: Normal Probabilities →](normal_probabilities.md)

**Related Reference:** [Statistical Tables](../reference/statistical_tables.md)


