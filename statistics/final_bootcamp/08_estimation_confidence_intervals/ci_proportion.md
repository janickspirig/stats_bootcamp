---
title: "I can construct CI for proportions"
category: "Statistics Bootcamp"
module: 8
order: 3
---

# I can construct CI for proportions

> 📚 **Overview:** Estimate population proportions with confidence—essential for survey analysis.

Confidence intervals for population proportions.

---

## Learning Objectives

After completing this section, you will be able to:
- Construct confidence intervals for proportions
- Check if sample size is large enough
- Interpret proportion CIs correctly

---

## Key Concepts

### Formula

$$
\hat{p} \pm z_{\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

Where:
- $\hat{p}$ = sample proportion = x/n
- x = number of successes
- n = sample size

---

### Conditions for Validity

The normal approximation is valid when:
- $n\hat{p} \geq 5$
- $n(1-\hat{p}) \geq 5$

These ensure enough successes and failures for the sampling distribution to be approximately Normal.

![Normal approximation for sampling distribution of proportion](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/ci_for_proportion_normal_approx.png)

---

## Worked Example

**Problem:**
In a survey of 500 customers, 320 said they would recommend the company. Construct a 95% CI for the proportion of all customers who would recommend.

**Solution:**

### Step 1: Calculate Sample Proportion

$$
\hat{p} = \frac{320}{500} = 0.64
$$

### Step 2: Check Conditions
- n·p̂ = 500 × 0.64 = 320 ≥ 5 ✓
- n·(1-p̂) = 500 × 0.36 = 180 ≥ 5 ✓

### Step 3: Find Critical Value
95% CI: z = 1.96

### Step 4: Calculate Standard Error

$$
SE = \sqrt{\frac{0.64 \times 0.36}{500}} = \sqrt{\frac{0.2304}{500}} = \sqrt{0.000461} = 0.0215
$$

### Step 5: Calculate Margin of Error

$$
ME = 1.96 \times 0.0215 = 0.042
$$

### Step 6: Construct Interval

$$
CI = 0.64 \pm 0.042 = (0.598, 0.682)
$$

**Interpretation:** We are 95% confident that between 59.8% and 68.2% of all customers would recommend the company.

---

## Practice Problems

### Problem 1

A poll of 400 voters finds 52% support a candidate. Construct a 95% CI.

<details>
<summary>💡 Show Solution</summary>

**Given:** n = 400, $\hat{p}$ = 0.52

**Check conditions:**
- 400 × 0.52 = 208 ≥ 5 ✓
- 400 × 0.48 = 192 ≥ 5 ✓

**Calculate:**

$$
SE = \sqrt{\frac{0.52 \times 0.48}{400}} = \sqrt{0.000624} = 0.0250
$$

$$
ME = 1.96 \times 0.0250 = 0.049
$$

$$
CI = 0.52 \pm 0.049 = (0.471, 0.569)
$$

**Answer:** 95% CI is (47.1%, 56.9%)

Note: This interval includes 50%, so we can't conclude the candidate has majority support.

</details>

---

### Problem 2

In a quality sample of 200 items, 8 are defective. Construct a 99% CI for the defect rate.

<details>
<summary>💡 Show Solution</summary>

**Given:** n = 200, x = 8, $\hat{p}$ = 8/200 = 0.04

**Check conditions:**
- 200 × 0.04 = 8 ≥ 5 ✓ (barely)
- 200 × 0.96 = 192 ≥ 5 ✓

**Calculate:**

$$
SE = \sqrt{\frac{0.04 \times 0.96}{200}} = \sqrt{0.000192} = 0.0139
$$

For 99% CI: z = 2.576

$$
ME = 2.576 \times 0.0139 = 0.036
$$

$$
CI = 0.04 \pm 0.036 = (0.004, 0.076)
$$

**Answer:** 99% CI for defect rate is (0.4%, 7.6%)

</details>

---

### Problem 3

A researcher wants a margin of error of at most 3 percentage points for a 95% CI. Using $\hat{p}$ = 0.5 (most conservative), what sample size is needed?

<details>
<summary>💡 Show Solution</summary>

**Formula:**

$$
ME = z \cdot \sqrt{\frac{p(1-p)}{n}}
$$

**Solve for n:**

$$
n = \frac{z^2 \cdot p(1-p)}{ME^2}
$$

$$
n = \frac{(1.96)^2 \times 0.5 \times 0.5}{(0.03)^2}
$$

$$
n = \frac{3.84 \times 0.25}{0.0009} = \frac{0.96}{0.0009} = 1,067
$$

**Answer:** Need at least 1,067 respondents

</details>

---

## Common Critical Values

| Confidence | z |
|------------|---|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |

---

## Key Takeaways

- **Formula:** $\hat{p} \pm z \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
- **Check:** n·p̂ ≥ 5 AND n·(1-p̂) ≥ 5
- Use z (not t) for proportions
- p̂ = 0.5 gives widest interval (most conservative)

---

## Navigation

[← CI for Mean](ci_mean.md) | [Module Index](index.md) | [Next: Sample Size →](sample_size.md)


