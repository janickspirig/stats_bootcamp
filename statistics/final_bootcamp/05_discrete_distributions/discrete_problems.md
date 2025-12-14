---
title: "I can work with discrete distribution problems"
category: "Statistics Bootcamp"
module: 5
order: 5
---

# I can work with discrete distribution problems

> 📚 **Overview:** Comprehensive practice combining all discrete distributions—identify, calculate, and interpret.

---

## 📑 Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Problem Set](#problem-set)
3. [Key Takeaways](#key-takeaways)

---

## Learning Objectives

After completing this section, you will be able to:
- Solve complete problems requiring distribution identification
- Calculate probabilities, means, and variances
- Interpret results in context

---

## Problem Set

### Problem 1: Quality Control

A factory produces computer chips. The defect rate is 2%. A quality inspector tests 100 chips.

a) What distribution should be used?
b) What's the expected number of defective chips?
c) What's the probability of finding exactly 3 defective chips?
d) What's the probability of finding more than 5 defective chips?

<details>
<summary>💡 Show Complete Solution</summary>

**a) Distribution:**
- Fixed trials: n = 100
- Two outcomes: defective or not
- Constant p = 0.02
→ **BINOMIAL** (or Poisson approximation since n is large, p is small)

**b) Expected value:**
$$E(X) = np = 100 \times 0.02 = 2$$

**c) P(X = 3):**
Using Poisson approximation (λ = 2):
$$P(X=3) = \frac{2^3 e^{-2}}{3!} = \frac{8 \times 0.1353}{6} = 0.1804$$

Using exact Binomial:
$$P(X=3) = \binom{100}{3}(0.02)^3(0.98)^{97} = 0.1823$$

**Answer: About 18%**

**d) P(X > 5):**
Using Poisson (λ = 2):
$$P(X > 5) = 1 - P(X \leq 5)$$
$$= 1 - [P(0) + P(1) + P(2) + P(3) + P(4) + P(5)]$$
$$= 1 - [0.1353 + 0.2707 + 0.2707 + 0.1804 + 0.0902 + 0.0361]$$
$$= 1 - 0.9834 = 0.0166$$

**Answer: About 1.7%**

</details>

---

### Problem 2: Customer Service

A call center receives an average of 4 calls per 10 minutes during peak hours.

a) What distribution should be used?
b) What's the probability of receiving exactly 6 calls in the next 10 minutes?
c) What's the probability of receiving no calls in a 5-minute window?
d) What's the probability of receiving at least 10 calls in a 20-minute window?

<details>
<summary>💡 Show Complete Solution</summary>

**a) Distribution:** POISSON (events in time interval)

**b) P(X = 6) with λ = 4:**
$$P(X=6) = \frac{4^6 e^{-4}}{6!} = \frac{4096 \times 0.0183}{720} = 0.1042$$
**Answer: 10.42%**

**c) P(X = 0) in 5 minutes:**
λ for 5 minutes = 4 × (5/10) = 2
$$P(X=0) = e^{-2} = 0.1353$$
**Answer: 13.53%**

**d) P(X ≥ 10) in 20 minutes:**
λ for 20 minutes = 4 × 2 = 8
$$P(X \geq 10) = 1 - P(X \leq 9)$$

Cumulative Poisson (λ=8):
P(X ≤ 9) ≈ 0.7166
$$P(X \geq 10) = 1 - 0.7166 = 0.2834$$
**Answer: About 28%**

</details>

---

### Problem 3: Lottery Committee

A company has 15 employees: 9 engineers and 6 managers. A committee of 5 is selected randomly.

a) What distribution should be used?
b) What's the probability the committee has exactly 3 engineers?
c) What's the expected number of engineers on the committee?
d) What's the probability of at least one manager on the committee?

<details>
<summary>💡 Show Complete Solution</summary>

**a) Distribution:** HYPERGEOMETRIC (sampling without replacement from finite population)

**b) P(exactly 3 engineers):**
N = 15, K = 9 (engineers), n = 5, k = 3
$$P(X=3) = \frac{\binom{9}{3}\binom{6}{2}}{\binom{15}{5}}$$
$$= \frac{84 \times 15}{3003} = \frac{1260}{3003} = 0.4196$$
**Answer: 42%**

**c) Expected engineers:**
$$E(X) = n \cdot \frac{K}{N} = 5 \times \frac{9}{15} = 3$$
**Answer: 3 engineers expected**

**d) P(at least 1 manager):**
This is 1 - P(0 managers) = 1 - P(5 engineers)
$$P(X=5) = \frac{\binom{9}{5}\binom{6}{0}}{\binom{15}{5}} = \frac{126 \times 1}{3003} = 0.0420$$
$$P(\text{at least 1 manager}) = 1 - 0.0420 = 0.9580$$
**Answer: 95.8%**

</details>

---

### Problem 4: Medical Screening

A disease affects 5% of a population. A screening test is administered to 20 randomly selected people.

a) What's the probability that exactly 2 people have the disease?
b) What's the probability that at least one person has the disease?
c) How many people would you expect to have the disease?

<details>
<summary>💡 Show Complete Solution</summary>

**Distribution:** BINOMIAL (n = 20, p = 0.05)

**a) P(X = 2):**
$$P(X=2) = \binom{20}{2}(0.05)^2(0.95)^{18}$$
$$= 190 \times 0.0025 \times 0.3972 = 0.1887$$
**Answer: 18.87%**

**b) P(X ≥ 1):**
$$P(X \geq 1) = 1 - P(X=0)$$
$$P(X=0) = (0.95)^{20} = 0.3585$$
$$P(X \geq 1) = 1 - 0.3585 = 0.6415$$
**Answer: 64.15%**

**c) Expected value:**
$$E(X) = np = 20 \times 0.05 = 1$$
**Answer: 1 person expected**

</details>

---

### Problem 5: Website Errors

A website experiences server errors at an average rate of 3 per day. The IT team wants to understand the error patterns.

a) What's the probability of a "perfect day" (no errors)?
b) What's the probability of experiencing more errors than average on a given day?
c) In a 7-day week, what's the expected total number of errors?
d) What's the variance of errors per day?

<details>
<summary>💡 Show Complete Solution</summary>

**Distribution:** POISSON (λ = 3 per day)

**a) P(X = 0):**
$$P(X=0) = e^{-3} = 0.0498$$
**Answer: About 5% chance of a perfect day**

**b) P(X > 3):**
$$P(X > 3) = 1 - P(X \leq 3)$$
$$= 1 - [P(0) + P(1) + P(2) + P(3)]$$
$$= 1 - [0.0498 + 0.1494 + 0.2240 + 0.2240]$$
$$= 1 - 0.6472 = 0.3528$$
**Answer: About 35%**

**c) Expected in 7 days:**
$$E(\text{weekly}) = 7 \times 3 = 21 \text{ errors}$$

**d) Variance per day:**
For Poisson: Var(X) = λ = 3
**Answer: Variance = 3, Standard deviation = √3 ≈ 1.73**

</details>

---

## Summary: Key Problem-Solving Steps

1. **Identify the distribution** by looking for keywords
2. **List the parameters** (n, p, λ, N, K)
3. **Apply the correct formula**
4. **Check reasonableness** of your answer
5. **Interpret in context**

---

## Quick Formula Reference

| Distribution | P(X = k) | Mean | Variance |
|--------------|----------|------|----------|
| Binomial | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| Poisson | $\frac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ |
| Hypergeometric | $\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$ | $n\frac{K}{N}$ | Complex |

---

## Navigation

[← Choosing Distribution](choosing_distribution.md) | [Module Index](index.md) | [Next Module: Continuous Distributions →](../06_continuous_distributions/index.md)

**Related Reference:** [Distribution Table](../reference/distribution_table.md) | [Formula Glossary](../reference/formula_glossary.md)


