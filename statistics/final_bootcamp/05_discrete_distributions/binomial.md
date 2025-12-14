---
title: "I can apply the Binomial distribution"
category: "Statistics Bootcamp"
module: 5
order: 1
---

# I can apply the Binomial distribution

> 📚 **Overview:** The Binomial distribution models the number of successes in a fixed number of independent trials—one of the most commonly used discrete distributions.

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
- Identify when to use the Binomial distribution
- Calculate Binomial probabilities
- Find mean and variance of a Binomial random variable
- Solve practical problems using the Binomial distribution

---

## Key Concepts

### When to Use Binomial

Use the Binomial distribution when ALL of these conditions are met:

1. **Fixed number of trials (n)** - You know exactly how many trials
2. **Two outcomes** - Each trial is success or failure
3. **Independent trials** - One trial doesn't affect another
4. **Constant probability (p)** - Same probability of success each trial

> 💡 **Memory aid: BINS** - Binary outcomes, Independent trials, N fixed, Same probability

---

### Notation and Formula

$$
X \sim Bin(n, p)
$$

**Probability Mass Function:**

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

**Where:**
- n = number of trials
- k = number of successes
- p = probability of success
- C(n,k) = combination "n choose k"

---

### Mean and Variance

**Mean (Expected Value):**

$$
\mu = E(X) = np
$$

**Variance:**

$$
\sigma^2 = Var(X) = np(1-p)
$$

**Standard Deviation:**

$$
\sigma = \sqrt{np(1-p)}
$$

---

## Worked Example

**Problem:**
A quality control inspector examines 10 products. Each product has a 15% probability of being defective. What is the probability of finding exactly 2 defective products?

**Solution:**

### Step 1: Verify Binomial Conditions
- ✅ Fixed trials: n = 10
- ✅ Two outcomes: Defective or not
- ✅ Independent: One product's quality doesn't affect another
- ✅ Constant p: 15% for each product

### Step 2: Identify Parameters
- n = 10 (products)
- k = 2 (defectives we want)
- p = 0.15 (probability defective)

### Step 3: Apply Formula

$$
P(X = 2) = \binom{10}{2} (0.15)^2 (0.85)^8
$$

### Step 4: Calculate

$$
\binom{10}{2} = \frac{10!}{2! \cdot 8!} = \frac{10 \times 9}{2} = 45
$$

$$
(0.15)^2 = 0.0225
$$

$$
(0.85)^8 = 0.2725
$$

$$
P(X = 2) = 45 \times 0.0225 \times 0.2725 = 0.2759
$$

**Answer: 27.59% probability of exactly 2 defective products.**

### Bonus: Mean and Standard Deviation

$$
\mu = np = 10 \times 0.15 = 1.5 \text{ defectives (on average)}
$$

$$
\sigma = \sqrt{10 \times 0.15 \times 0.85} = \sqrt{1.275} = 1.13
$$

---

## Practice Problems

### Problem 1

A salesperson makes 8 cold calls. Each call has a 20% probability of resulting in a sale. Calculate:
a) P(exactly 3 sales)
b) P(at least 1 sale)
c) Expected number of sales

<details>
<summary>💡 Show Solution</summary>

**Given:** n = 8, p = 0.20

**a) P(X = 3):**
$$P(X=3) = \binom{8}{3}(0.20)^3(0.80)^5$$
$$= 56 \times 0.008 \times 0.3277 = 0.1468$$
**Answer: 14.68%**

**b) P(at least 1 sale) = P(X ≥ 1):**
Use complement: P(X ≥ 1) = 1 - P(X = 0)
$$P(X=0) = \binom{8}{0}(0.20)^0(0.80)^8 = 1 \times 1 \times 0.1678 = 0.1678$$
$$P(X \geq 1) = 1 - 0.1678 = 0.8322$$
**Answer: 83.22%**

**c) Expected sales:**
$$E(X) = np = 8 \times 0.20 = 1.6 \text{ sales}$$

</details>

---

### Problem 2

In a multiple choice test with 20 questions, each with 5 options, a student guesses randomly on all questions.
a) What's the expected number of correct answers?
b) What's the probability of getting exactly 5 correct?
c) What's the probability of passing (at least 10 correct)?

<details>
<summary>💡 Show Solution</summary>

**Given:** n = 20, p = 1/5 = 0.20

**a) Expected correct:**
$$E(X) = np = 20 \times 0.20 = 4 \text{ correct}$$

**b) P(X = 5):**
$$P(X=5) = \binom{20}{5}(0.20)^5(0.80)^{15}$$
$$= 15,504 \times 0.00032 \times 0.0352 = 0.1746$$
**Answer: 17.46%**

**c) P(X ≥ 10):**
This requires summing P(X=10) + P(X=11) + ... + P(X=20)
Or use complement: P(X ≥ 10) = 1 - P(X ≤ 9)

Using calculator/table: P(X ≥ 10) ≈ 0.0026
**Answer: About 0.26%** (very unlikely to pass by guessing!)

</details>

---

### Problem 3

A manufacturer knows 5% of items are defective. In a batch of 15 items:
a) What's the probability of no defectives?
b) What's the variance of the number of defectives?
c) What's the probability of at most 2 defectives?

<details>
<summary>💡 Show Solution</summary>

**Given:** n = 15, p = 0.05

**a) P(X = 0):**
$$P(X=0) = \binom{15}{0}(0.05)^0(0.95)^{15} = (0.95)^{15} = 0.4633$$
**Answer: 46.33%**

**b) Variance:**
$$\sigma^2 = np(1-p) = 15 \times 0.05 \times 0.95 = 0.7125$$

**c) P(X ≤ 2) = P(X=0) + P(X=1) + P(X=2):**
- P(X=0) = 0.4633 (from above)
- P(X=1) = $\binom{15}{1}(0.05)^1(0.95)^{14} = 15 \times 0.05 \times 0.4877 = 0.3658$
- P(X=2) = $\binom{15}{2}(0.05)^2(0.95)^{13} = 105 \times 0.0025 \times 0.5133 = 0.1348$

$$P(X \leq 2) = 0.4633 + 0.3658 + 0.1348 = 0.9639$$
**Answer: 96.39%**

</details>

---

## Visual Understanding

<!-- IMAGE_PLACEHOLDER
Type: chart
Description: Three bar charts showing Binomial distributions with different parameters: n=10,p=0.5 (symmetric), n=10,p=0.2 (right-skewed), n=10,p=0.8 (left-skewed). Each shows probabilities for k=0 to k=10.
Data: PMF values for each combination
Style: Side-by-side bar charts with means marked
Filename: binomial_shapes.png
-->
![Binomial distribution shapes](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/binomial_shapes.png)

**Key observations:**
- p = 0.5 → Symmetric distribution
- p < 0.5 → Right-skewed
- p > 0.5 → Left-skewed

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Using Binomial when sampling without replacement.
> Binomial requires independence. For sampling without replacement, use Hypergeometric.

> ⚠️ **Mistake 2:** Forgetting (1-p) for failures.
> The formula uses both p^k AND (1-p)^(n-k).

> ⚠️ **Mistake 3:** Confusing "at least" with "exactly."
> P(X ≥ 2) ≠ P(X = 2). Use complement or sum for "at least."

---

## Key Takeaways

> 🎯 **Remember:**
> - **Use Binomial** for fixed n, independent trials, constant p, two outcomes (BINS)
> - **Mean:** μ = np
> - **Variance:** σ² = np(1-p)
> - **"At least one":** Use complement: P(X ≥ 1) = 1 - P(X = 0)
> - If sampling **without replacement**, use Hypergeometric instead

---

## Navigation

[← Module Index](index.md) | [Next: Poisson Distribution →](poisson.md)

**Related Reference:** [Distribution Table](../reference/distribution_table.md) | [Formula Glossary](../reference/formula_glossary.md)


