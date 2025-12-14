---
title: "Exercise 3B: Continuous Distributions"
category: "Statistics Bootcamp"
module: 98
order: 4
---

# Exercise 3B: Continuous Distributions

> 📚 **Overview:** Practice with Normal distribution and z-scores.

Practice problems for Normal and Exponential distributions.

---

## Topics Covered
- Normal distribution
- Z-scores
- Normal probabilities
- Exponential distribution

---

## Problem 1 (Normal)

IQ scores: μ = 100, σ = 15
a) P(IQ > 130)
b) P(85 < IQ < 115)
c) What IQ score is at the 90th percentile?

<details>
<summary>💡 Show Solution</summary>

**a) P(X > 130):**
z = (130 - 100)/15 = 2.0
P(Z > 2.0) = 1 - 0.9772 = **0.0228 (2.28%)**

**b) P(85 < X < 115):**
z₁ = (85 - 100)/15 = -1.0
z₂ = (115 - 100)/15 = 1.0
P(-1 < Z < 1) = 0.8413 - 0.1587 = **0.6826 (68.26%)**

**c) 90th percentile:**
z₀.₉₀ = 1.28
x = 100 + 1.28(15) = **119.2**

</details>

---

## Problem 2 (Normal)

Test scores: μ = 70, σ = 8
What score separates the top 5% from the rest?

<details>
<summary>💡 Show Solution</summary>

z₀.₉₅ = 1.645
x = 70 + 1.645(8) = 70 + 13.16 = **83.16**

Scores above 83.16 are in the top 5%.

</details>

---

## Problem 3 (Exponential)

Time between customer arrivals: mean = 5 minutes.
a) P(next customer within 3 minutes)
b) P(wait more than 10 minutes)

<details>
<summary>💡 Show Solution</summary>

λ = 1/5 = 0.2 per minute

**a) P(X ≤ 3):**

$$
P(X \leq 3) = 1 - e^{-0.2(3)} = 1 - e^{-0.6} = 1 - 0.549 = 0.451
$$

**b) P(X > 10):**

$$
P(X > 10) = e^{-0.2(10)} = e^{-2} = 0.135
$$

</details>

---

## Problem 4 (Z-table lookup mechanics)

Using a standard normal table that gives P(Z ≤ z), find:

a) P(Z ≤ 0.75)
b) P(Z > 1.75)
c) P(Z ≤ -1.23) using symmetry

<details>
<summary>💡 Show Solution</summary>

a) P(Z ≤ 0.75) = 0.7734
b) P(Z > 1.75) = 1 − P(Z ≤ 1.75) = 1 − 0.9599 = 0.0401
c) P(Z ≤ −1.23) = 1 − P(Z ≤ 1.23) = 1 − 0.8907 = 0.1093

</details>

---

## Problem 5 (Reverse lookup)

Find z such that P(Z ≤ z) = 0.95, then interpret it as a percentile.

<details>
<summary>💡 Show Solution</summary>

From the z-table, P(Z ≤ z) = 0.95 corresponds to z ≈ 1.645.
Interpretation: z = 1.645 is the **95th percentile** of the standard normal distribution.

</details>

---

## Problem 6 (Normal, “find x such that…”) 

Delivery times are Normal with μ = 2.0 days and σ = 0.5 days.
Find x such that P(X ≤ x) = 0.90.

<details>
<summary>💡 Show Solution</summary>

Find z for 0.90: z ≈ 1.28.
x = μ + zσ = 2.0 + 1.28(0.5) = 2.64 days.
Business interpretation: 90% of deliveries arrive within about **2.64 days**.

</details>

---

## Problem 7 (Between probability)

Suppose X ~ N(50, 10²).
Compute P(40 < X < 65).

<details>
<summary>💡 Show Solution</summary>

z₁ = (40 − 50)/10 = −1.0 → P(Z ≤ −1.0) = 0.1587
z₂ = (65 − 50)/10 = 1.5 → P(Z ≤ 1.5) = 0.9332
P(40 < X < 65) = 0.9332 − 0.1587 = 0.7745

</details>

---

## Problem 8 (Exponential memoryless check)

Waiting time until the next bus is Exponential with mean 10 minutes.
You have already waited 8 minutes. What is the probability you wait more than 5 additional minutes?

<details>
<summary>💡 Show Solution</summary>

Mean = 10 → λ = 0.1 per minute.
Memoryless property: P(X > 8+5 | X > 8) = P(X > 5) = e^{-0.1·5} = e^{-0.5} = 0.607.

</details>

---

## Problem 9 (Normal, negative z with symmetry)

Suppose \(X\\sim N(200, 30^2)\\). Compute \(P(X<170)\\).

<details>
<summary>💡 Show Solution</summary>

$$
z=\\frac{170-200}{30}=-1
$$

So \(P(X<170)=P(Z<-1)=0.1587\\).

</details>

---

## Problem 10 (Central interval)

Suppose \(X\\sim N(50, 10^2)\\). Find numbers L and U such that:

$$
P(L<X<U)=0.95
$$

<details>
<summary>💡 Show Solution</summary>

Central 95% corresponds to \(z=\\pm 1.96\\).

$$
L=50-1.96\\cdot 10=30.4,\\qquad U=50+1.96\\cdot 10=69.6
$$

</details>

---

## Problem 11 (Reverse lookup: lower tail)

Find z such that \(P(Z\\le z)=0.025\\).

<details>
<summary>💡 Show Solution</summary>

From the z-table, \(P(Z\\le 1.96)=0.975\\). By symmetry:

$$
P(Z\\le -1.96)=0.025
$$

So \(z\\approx -1.96\\).

</details>

---

## Problem 12 (Exponential percentile / quantile)

Waiting time is Exponential with mean 8 minutes.

Find t such that \(P(X\\le t)=0.90\\).

<details>
<summary>💡 Show Solution</summary>

Mean 8 → \(\\lambda=1/8=0.125\\).

For Exponential:

$$
P(X\\le t)=1-e^{-\\lambda t}=0.90
\\Rightarrow e^{-\\lambda t}=0.10
\\Rightarrow t = -\\frac{\\ln(0.10)}{0.125}
$$

$$
t = \\frac{2.3026}{0.125}=18.4208
$$

So \(t\\approx 18.42\\) minutes.

</details>

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Forgetting the table gives LEFT area.
> For “greater than”, use 1 − table value.
> ⚠️ **Mistake 2:** Mishandling negative z.
> Use symmetry: P(Z ≤ −a) = 1 − P(Z ≤ a).
> ⚠️ **Mistake 3:** Mixing up σ and σ² in N(μ, σ²).

---

## Key Takeaways

- Standardize: z = (x − μ)/σ
- Use complement and symmetry for fast table work
- Reverse lookup = percentile cutoffs
- Exponential is memoryless

---

## Related Module

[Module 06: Continuous Distributions](../06_continuous_distributions/index.md)

---

## Navigation

[← Exercise 3A](exercise_3a.md) | [Exercises Index](index.md) | [Exercise 4 →](exercise_4.md)


