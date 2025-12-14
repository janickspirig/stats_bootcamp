---
title: "I understand point vs interval estimation"
category: "Statistics Bootcamp"
module: 8
order: 1
---

# I understand point vs interval estimation

> 📚 **Overview:** Point estimates give single values; interval estimates provide ranges with confidence levels.

Two approaches to estimating population parameters.

---

## Learning Objectives

After completing this section, you will be able to:
- Define point estimate and interval estimate
- Understand desirable properties of estimators
- Interpret confidence level correctly

---

## Key Concepts

### Point Estimate

A **point estimate** is a single value used to estimate a population parameter.

| Parameter | Point Estimator |
|-----------|-----------------|
| Population mean μ | Sample mean $\bar{x}$ |
| Population proportion p | Sample proportion $\hat{p}$ |
| Population variance σ² | Sample variance s² |
| Population SD σ | Sample SD s |

**Limitation:** No indication of precision or uncertainty.

---

### Interval Estimate

An **interval estimate** provides a range of plausible values for the parameter.

$$\text{Point Estimate} \pm \text{Margin of Error}$$

**Confidence Interval (CI):** An interval estimate associated with a confidence level.

---

### Confidence Level

The **confidence level** (e.g., 95%) means:
- If we took many samples and built a CI from each
- 95% of those intervals would contain the true parameter

> ⚠️ **NOT:** "There's a 95% probability that μ is in this interval."

The true parameter is fixed; the interval is what varies from sample to sample.

![Many confidence intervals from repeated samples showing 95% coverage](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/ci_repeated_samples_coverage.png)

---

### Components of a Confidence Interval

$$\text{CI} = \text{Point Estimate} \pm (\text{Critical Value}) \times (\text{Standard Error})$$

| Component | Symbol | Description |
|-----------|--------|-------------|
| Point Estimate | $\bar{x}$, $\hat{p}$ | Center of interval |
| Critical Value | $z_{\alpha/2}$, $t_{\alpha/2}$ | From z or t table |
| Standard Error | SE | Spread of sampling dist |
| Margin of Error | ME | Half-width of interval |

---

## Common Critical Values (z)

| Confidence Level | α | α/2 | z_{α/2} |
|-----------------|---|-----|---------|
| 90% | 0.10 | 0.05 | 1.645 |
| 95% | 0.05 | 0.025 | 1.960 |
| 99% | 0.01 | 0.005 | 2.576 |

---

## Worked Example

**Problem:**
A sample of 100 customers has mean satisfaction score 7.2 with s = 1.5.

Give both a point estimate and describe how a 95% confidence interval would be constructed.

**Solution:**

**Point Estimate:**
$\bar{x} = 7.2$

This is our best single guess for μ.

**Interval Estimate (setup):**
$$CI = \bar{x} \pm t_{0.025, 99} \cdot \frac{s}{\sqrt{n}}$$

Components:
- Point estimate: 7.2
- Critical value: t₀.₀₂₅,₉₉ ≈ 1.984
- SE = 1.5/√100 = 0.15
- ME = 1.984 × 0.15 = 0.30

$$CI = 7.2 \pm 0.30 = (6.90, 7.50)$$

**Interpretation:** We are 95% confident that the true mean satisfaction score is between 6.90 and 7.50.

---

## Practice Problems

### Problem 1

A poll of 400 voters finds 55% support a candidate.

a) What is the point estimate of population support?
b) Is the point estimate likely to be exactly correct?

<details>
<summary>💡 Show Solution</summary>

**a) Point estimate:**
$\hat{p} = 0.55$ or 55%

**b) Exactly correct?**
No, it's extremely unlikely that exactly 55.0000...% of the population supports the candidate. The point estimate is our best guess, but the true value could be anywhere nearby (which is why we use confidence intervals).

</details>

---

### Problem 2

A 95% CI for average salary is (CHF 58,000, CHF 62,000).

Which interpretations are correct?
a) "There's a 95% probability μ is between 58,000 and 62,000."
b) "95% of employees earn between 58,000 and 62,000."
c) "If we repeated the sampling many times, 95% of the resulting CIs would contain μ."
d) "We are 95% confident that the true mean salary is between 58,000 and 62,000."

<details>
<summary>💡 Show Solution</summary>

**Correct:** c) and d)

**Incorrect:**
- a) The true μ is fixed, not random. We can't assign probability to fixed values.
- b) This describes individual salaries, not the mean. A CI for the mean says nothing about individual variation.

</details>

---

## Key Takeaways

- **Point estimate:** Single best guess (no uncertainty measure)
- **Interval estimate:** Range with associated confidence level
- **Confidence level:** Long-run success rate of the method
- CI = Point Estimate ± Margin of Error
- Larger confidence level → wider interval

---

## Navigation

[← Module Index](index.md) | [Next: CI for Mean →](ci_mean.md)


