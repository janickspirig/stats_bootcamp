---
title: "I can calculate standard error"
category: "Statistics Bootcamp"
module: 7
order: 3
---

# I can calculate standard error

> 📚 **Overview:** Standard error measures the variability of sample statistics—essential for confidence intervals.

Standard error measures the precision of sample estimates.

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate standard error for means and proportions
- Interpret standard error in context
- Distinguish standard error from standard deviation

---

## Key Concepts

### What is Standard Error?

**Standard Error (SE)** = the standard deviation of a sampling distribution.

It measures **how much sample statistics vary** from sample to sample.

---

### Standard Error Formulas

| Statistic | Standard Error | When σ Known/Unknown |
|-----------|---------------|---------------------|
| Mean (σ known) | $SE = \frac{\sigma}{\sqrt{n}}$ | Population σ known |
| Mean (σ unknown) | $SE = \frac{s}{\sqrt{n}}$ | Estimate with sample s |
| Proportion | $SE = \sqrt{\frac{p(1-p)}{n}}$ | Use $\hat{p}$ if p unknown |

---

### Standard Deviation vs Standard Error

| Concept | SD | SE |
|---------|----|----|
| Measures | Spread of individual observations | Spread of sample statistics |
| Symbol | $\sigma$ or $s$ | $SE$ or $\sigma_{\bar{x}}$ |
| Changes with n | No | Yes (decreases) |
| Use | Describing data | Inference about population |

> 💡 **Key insight:** SE always decreases as n increases; SD does not.

---

## SD vs SE vs σ/√n (common exam trap)

Use this as a strict “which denominator?” cheat sheet:

| What you standardize | Typical formula | Denominator |
|---|---|---|
| Individual observation \(x\) | \(z = \\frac{x-\\mu}{\\sigma}\) | σ |
| Sample mean \(\\bar{x}\) | \(z = \\frac{\\bar{x}-\\mu}{\\sigma/\\sqrt{n}}\) | σ/√n |
| Sample mean when σ unknown | \(t = \\frac{\\bar{x}-\\mu_0}{s/\\sqrt{n}}\) | s/√n |

### Mini-quiz (3 quick checks)

<details>
<summary>💡 Show mini-quiz answers</summary>

1) If the question is about **a sample mean**, you use **σ/√n** (or s/√n), not σ.
2) If you **double n**, SE is multiplied by \(1/\\sqrt{2}\\) (it decreases).
3) If σ is unknown and you plug in s, your test statistic uses **t**, not z.

</details>

---

## Worked Example

**Problem:**
A sample of n = 64 employees has a mean salary of CHF 55,000 with sample standard deviation s = CHF 8,000.

a) Calculate the standard error of the mean.
b) Interpret this value.
c) What would be the SE if n = 256?

**Solution:**

### Part a: Calculate SE

$$
SE = \frac{s}{\sqrt{n}} = \frac{8,000}{\sqrt{64}} = \frac{8,000}{8} = 1,000
$$

**Answer: SE = CHF 1,000**

### Part b: Interpretation
If we took many samples of 64 employees, the sample means would typically vary by about CHF 1,000 from the true population mean.

### Part c: SE with n = 256

$$
SE = \frac{8,000}{\sqrt{256}} = \frac{8,000}{16} = 500
$$

**Observation:** Quadrupling n (64 → 256) halves the SE (1,000 → 500).

---

## Practice Problems

### Problem 1

A political poll of n = 400 voters finds 52% support a candidate (p̂ = 0.52).

a) Calculate the standard error for this proportion.
b) If the sample size were n = 1,600, what would be the SE?

<details>
<summary>💡 Show Solution</summary>

**a) SE for n = 400:**

$$
SE = \sqrt{\frac{0.52 \times 0.48}{400}} = \sqrt{\frac{0.2496}{400}} = \sqrt{0.000624} = 0.025
$$

**Answer: SE = 2.5 percentage points**

**b) SE for n = 1,600:**

$$
SE = \sqrt{\frac{0.52 \times 0.48}{1600}} = \sqrt{0.000156} = 0.0125
$$

**Answer: SE = 1.25 percentage points**

Note: Quadrupling n halves SE.

</details>

---

### Problem 2

Two studies estimate average height:
- Study A: n = 25, s = 10 cm
- Study B: n = 100, s = 10 cm

Which study provides a more precise estimate? By how much?

<details>
<summary>💡 Show Solution</summary>

**Study A:**

$$
SE_A = \frac{10}{\sqrt{25}} = \frac{10}{5} = 2 \text{ cm}
$$

**Study B:**

$$
SE_B = \frac{10}{\sqrt{100}} = \frac{10}{10} = 1 \text{ cm}
$$

**Comparison:**
Study B is more precise. Its SE is half that of Study A.

Study B's estimate is **twice as precise** (or has half the uncertainty).

</details>

---

### Problem 3

You want to estimate the mean with a standard error of at most 5. If σ = 30, what minimum sample size is needed?

<details>
<summary>💡 Show Solution</summary>

**Solve for n:**

$$
SE = \frac{\sigma}{\sqrt{n}} \leq 5
$$

$$
\frac{30}{\sqrt{n}} \leq 5
$$

$$
\sqrt{n} \geq \frac{30}{5} = 6
$$

$$
n \geq 36
$$

**Answer: n = 36 minimum**

</details>

---

## Relationship: SE and Sample Size

$$
SE = \frac{\sigma}{\sqrt{n}}
$$

| To reduce SE by... | You need to... |
|--------------------|----------------|
| Half | 4× the sample size |
| One-third | 9× the sample size |
| One-fourth | 16× the sample size |

**Diminishing returns:** Each additional reduction in SE requires progressively more data.

---

## Key Takeaways

- **SE** = standard deviation of the sampling distribution
- **SE for mean:** σ/√n (or s/√n if σ unknown)
- **SE for proportion:** √[p(1-p)/n]
- SE **decreases** as n increases
- Halving SE requires 4× the sample size

---

## Navigation

[← Central Limit Theorem](central_limit_theorem.md) | [Module Index](index.md) | [Next: Sample Size Effect →](sample_size_effect.md)


