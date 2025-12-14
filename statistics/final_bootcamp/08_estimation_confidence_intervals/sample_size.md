---
title: "I can determine required sample size"
category: "Statistics Bootcamp"
module: 8
order: 4
---

# I can determine required sample size

> 📚 **Overview:** Calculate required sample size for desired precision—planning before data collection.

Planning studies to achieve desired precision.

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate sample size for estimating a mean
- Calculate sample size for estimating a proportion
- Understand the trade-offs in sample size decisions

---

## Checklist

- **When to use:** You need to plan a study so that your estimate has a target margin of error \(E\) at confidence level \(1-\\alpha\).
- **What to choose:** confidence level → \(z_{\\alpha/2}\), an estimate of σ (for means) or p (for proportions), and the desired \(E\).
- **Rule:** Always **round up** (sample size must be an integer and must meet the precision target).

---

## Key Concepts

### Sample Size for Mean

To achieve margin of error E with confidence level (1-α):

$$
n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2
$$

**Requirements:**
- Need preliminary estimate of σ (from pilot study, literature, or theory)
- Round UP to next integer

---

### Sample Size for Proportion

$$
n = \hat{p}(1-\hat{p})\left(\frac{z_{\alpha/2}}{E}\right)^2
$$

**If p is unknown:** Use p = 0.5 (most conservative):

$$
n = 0.25 \left(\frac{z_{\alpha/2}}{E}\right)^2
$$

---

## Worked Example

**Problem:**
A company wants to estimate average customer satisfaction with:
- 95% confidence
- Margin of error ≤ 0.5 points
- Preliminary estimate: σ ≈ 2.5 points

What sample size is needed?

**Solution:**

### Step 1: Identify Values
- z₀.₀₂₅ = 1.96
- σ = 2.5
- E = 0.5

### Step 2: Apply Formula

$$
n = \left(\frac{1.96 \times 2.5}{0.5}\right)^2 = \left(\frac{4.9}{0.5}\right)^2 = (9.8)^2 = 96.04
$$

### Step 3: Round Up

$$
n = 97
$$

**Answer:** Need at least 97 customers.

Business interpretation: To make a decision based on the survey with ±0.5 accuracy at 95% confidence, the company should budget for at least 97 responses.

---

## Practice Problems

### Problem 1

Estimate mean income with:
- 95% confidence
- Margin of error ≤ CHF 500
- Preliminary σ ≈ CHF 3,000

<details>
<summary>💡 Show Solution</summary>

Step 1: Identify \(z, \\sigma, E\)
$$
n = \left(\frac{1.96 \times 3,000}{500}\right)^2
$$

$$
= \left(\frac{5,880}{500}\right)^2
$$

$$
= (11.76)^2 = 138.3
$$

**Answer:** n = 139 (round up)

Business interpretation: If you sample fewer than 139, your margin of error will exceed CHF 500 at 95% confidence.

</details>

---

### Problem 2

A political poll wants:
- 95% confidence
- Margin of error ≤ 3 percentage points
- No prior estimate of p

<details>
<summary>💡 Show Solution</summary>

Use p = 0.5 (conservative):

$$
n = 0.25 \left(\frac{1.96}{0.03}\right)^2
$$

$$
= 0.25 \times (65.33)^2
$$

$$
= 0.25 \times 4,268
$$

$$
= 1,067
$$

**Answer:** n = 1,067

Business interpretation: To quote a ±3% margin of error at 95% confidence, the poll needs roughly 1,067 respondents.

</details>

---

### Problem 3

Same poll as Problem 2, but with 99% confidence. How does this change n?

<details>
<summary>💡 Show Solution</summary>

$$
n = 0.25 \left(\frac{2.576}{0.03}\right)^2
$$

$$
= 0.25 \times (85.87)^2
$$

$$
= 0.25 \times 7,374
$$

$$
= 1,844
$$

**Answer:** n = 1,844

**Comparison:** Going from 95% to 99% confidence increased required n from 1,067 to 1,844 (73% increase).

</details>

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Rounding down.
> Always round up (otherwise your margin of error target is not guaranteed).

> ⚠️ **Mistake 2:** Using the wrong z-value.
> Use \(z_{\\alpha/2}\) for two-sided confidence intervals (e.g., 95% → 1.96).

> ⚠️ **Mistake 3:** Forgetting the conservative choice for proportions.
> If p is unknown, use p = 0.5 (maximizes \(p(1-p)\)) to avoid under-sampling.

---

## Quick Reference Formulas

| Estimating | Sample Size Formula |
|------------|---------------------|
| Mean | $n = \left(\frac{z \sigma}{E}\right)^2$ |
| Proportion (p known) | $n = p(1-p)\left(\frac{z}{E}\right)^2$ |
| Proportion (p unknown) | $n = 0.25\left(\frac{z}{E}\right)^2$ |

---

## Trade-offs

| Change | Effect on n |
|--------|-------------|
| Higher confidence | ↑ n |
| Smaller margin of error | ↑ n |
| Larger σ | ↑ n |
| Halve E | 4× n |
| 95% → 99% confidence | ~1.7× n |

![Margin of error decreasing as sample size increases](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/ci_width_vs_n.png)

---

## Key Takeaways

- **Sample size formula** ensures desired precision
- **Always round UP** to next integer
- Use p = 0.5 if proportion is unknown
- Higher precision or confidence → larger n
- Halving margin of error quadruples sample size

---

## Navigation

[← CI for Proportion](ci_proportion.md) | [Module Index](index.md) | [Next Module: Hypothesis Testing →](../09_hypothesis_testing_basics/index.md)


