---
title: "I understand Type I and Type II errors"
category: "Statistics Bootcamp"
module: 9
order: 3
---

# I understand Type I and Type II errors

> 📚 **Overview:** Two ways hypothesis tests can go wrong—and the tradeoffs between them.

Two types of mistakes we can make in hypothesis testing.

---

## Learning Objectives

After completing this section, you will be able to:
- Define Type I and Type II errors
- Understand the relationship between α, β, and power
- Make trade-offs between error types

---

## Key Concepts

### The Decision Table

|  | H₀ is TRUE | H₀ is FALSE |
|--|------------|-------------|
| **Reject H₀** | Type I Error (α) | Correct ✓ |
| **Fail to reject H₀** | Correct ✓ | Type II Error (β) |

![Type I error (alpha), Type II error (beta), and power shown on overlapping H0 and H1 distributions](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/alpha_beta_power_overlap.png)

---

### Type I Error (α)

**Definition:** Rejecting H₀ when H₀ is actually true.

**Analogy:** Convicting an innocent person (false positive)

**Probability:** α (significance level, typically 0.05)

---

### Type II Error (β)

**Definition:** Failing to reject H₀ when H₀ is actually false.

**Analogy:** Letting a guilty person go free (false negative)

**Probability:** β (depends on sample size, effect size, α)

---

### Power

$$\text{Power} = 1 - \beta$$

**Definition:** Probability of correctly rejecting H₀ when it's false.

**Goal:** High power (typically ≥ 0.80)

---

### Relationships

| To Decrease Type I Error (α) | Effect |
|------------------------------|--------|
| Lower α (e.g., 0.01) | Increases Type II Error (β) |

| To Increase Power (1-β) | Methods |
|-------------------------|---------|
| Increase sample size n | Most common approach |
| Increase α | Trade-off with Type I error |
| Larger effect size | Not usually under our control |

---

## β and Power (calculation example)

In HSG-style exercises, you may be asked to **compute β** (Type II error) and **power** for a specific alternative.

### Example (one-tailed z-test, σ known)

**Setup:**
- H₀: μ = 100
- H₁: μ > 100
- α = 0.05
- σ = 10 (known)
- n = 25
- Consider the case where the true mean is μ = 105

**Step 1: Find the rejection threshold for \(\\bar{x}\)**

For a right-tailed z-test, reject H₀ if \(z \\ge z_{0.05} = 1.645\).

$$
z = \\frac{\\bar{x} - \\mu_0}{\\sigma/\\sqrt{n}}
$$

Solve for the critical sample mean \(\\bar{x}_c\):

$$
\\bar{x}_c = \\mu_0 + z_{0.05}\\cdot \\frac{\\sigma}{\\sqrt{n}}
= 100 + 1.645\\cdot \\frac{10}{5}
= 100 + 3.29
= 103.29
$$

Decision rule: reject H₀ if \(\\bar{x} \\ge 103.29\).

**Step 2: Compute β when the true mean is μ = 105**

Type II error here means: **fail to reject H₀ even though μ = 105**.

$$
\\beta = P(\\bar{x} < 103.29 \\mid \\mu=105)
$$

Standardize using the sampling distribution \(\\bar{x} \\sim N(\\mu, \\sigma/\\sqrt{n})\):

$$
\\beta
= \\Phi\\left(\\frac{103.29 - 105}{10/5}\\right)
= \\Phi\\left(\\frac{-1.71}{2}\\right)
= \\Phi(-0.855)
\\approx 0.196
$$

**Power:**

$$
1-\\beta \\approx 1 - 0.196 = 0.804
$$

Business interpretation: With n = 25, the test has about **80% power** to detect an increase to μ = 105 at α = 0.05.

---

## Worked Example

**Problem:**
A medical test has:
- α = 0.05 (5% false positive rate)
- Power = 0.80 (so β = 0.20)

a) What does α = 0.05 mean in context?
b) What does β = 0.20 mean in context?
c) Which error is more serious: telling a healthy person they're sick, or telling a sick person they're healthy?

**Solution:**

**a) α = 0.05:**
5% of healthy people will be incorrectly diagnosed as having the disease (false positive).

**b) β = 0.20:**
20% of people who actually have the disease will be incorrectly told they're healthy (false negative).

**c) Which is worse:**
It depends on the disease! 
- For a fatal but treatable disease: False negatives are worse (Type II)
- For a condition with harmful treatment: False positives are worse (Type I)

---

## Practice Problems

### Problem 1

A company tests if a new process improves quality. Current defect rate is 5%.
- H₀: p ≥ 0.05 (no improvement)
- H₁: p < 0.05 (improvement)

Describe Type I and Type II errors in context.

<details>
<summary>💡 Show Solution</summary>

**Type I Error:**
Concluding the new process improves quality (reject H₀) when it actually doesn't.
- Consequence: Adopting a process that's no better, wasting resources

**Type II Error:**
Concluding there's no improvement (fail to reject H₀) when the process actually is better.
- Consequence: Missing an opportunity to improve quality

</details>

---

### Problem 2

If we reduce α from 0.05 to 0.01, what happens to β?

<details>
<summary>💡 Show Solution</summary>

**β increases** (Type II error becomes more likely).

Lower α means stricter evidence required to reject H₀.
This makes it harder to detect real effects, increasing β.

To maintain power while lowering α, you need a larger sample size.

</details>

---

## Key Takeaways

- **Type I (α):** False positive, reject true H₀
- **Type II (β):** False negative, fail to reject false H₀
- **Power = 1 - β:** Ability to detect real effects
- Decreasing α increases β (trade-off)
- Increase n to reduce both errors

---

## Navigation

[← Stating Hypotheses](stating_hypotheses.md) | [Module Index](index.md) | [Next: P-Values →](p_values.md)


