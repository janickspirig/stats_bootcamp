---
title: "I can apply the Poisson distribution"
category: "Statistics Bootcamp"
module: 5
order: 2
---

# I can apply the Poisson distribution

> 📚 **Overview:** The Poisson distribution models the number of events occurring in a fixed interval—arrivals, defects, calls, and more.

---

## 📑 Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Key Concepts](#key-concepts)
3. [Worked Example](#worked-example)
4. [Practice Problems](#practice-problems)
5. [Key Takeaways](#key-takeaways)

---

## Learning Objectives

After completing this section, you will be able to:
- Identify when to use the Poisson distribution
- Calculate Poisson probabilities
- Find mean and variance of a Poisson random variable
- Apply Poisson to real-world counting problems

---

## Key Concepts

### When to Use Poisson

Use the Poisson distribution when:

1. **Counting events** in a fixed interval (time, space, volume)
2. Events occur **independently**
3. **Average rate (λ)** is known and constant
4. Two events can't occur at exactly the same instant

**Common applications:**
- Customer arrivals per hour
- Defects per unit of product
- Calls to a call center per minute
- Accidents per month
- Emails received per day

---

### Notation and Formula

$$X \sim Poi(\lambda)$$

**Probability Mass Function:**
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

Where:
- $\lambda$ (lambda) = average rate (mean number of events)
- $k$ = number of events (0, 1, 2, ...)
- $e$ ≈ 2.71828

---

### Mean and Variance

A unique property of the Poisson:

$$\mu = E(X) = \lambda$$
$$\sigma^2 = Var(X) = \lambda$$

The mean equals the variance!

---

## Worked Example

**Problem:**
A call center receives an average of 3 calls per hour. What is the probability of receiving exactly 5 calls in the next hour?

**Solution:**

### Step 1: Verify Poisson Conditions
- ✅ Counting events (calls)
- ✅ Fixed interval (1 hour)
- ✅ Independent (one call doesn't cause another)
- ✅ Known rate (λ = 3)

### Step 2: Identify Parameters
- λ = 3 (calls per hour)
- k = 5 (calls we want)

### Step 3: Apply Formula

$$P(X = 5) = \frac{3^5 \cdot e^{-3}}{5!}$$

### Step 4: Calculate

$$3^5 = 243$$
$$e^{-3} \approx 0.0498$$
$$5! = 120$$

$$P(X = 5) = \frac{243 \times 0.0498}{120} = \frac{12.10}{120} = 0.1008$$

**Answer: 10.08% probability of exactly 5 calls.**

---

## Practice Problems

### Problem 1

A website experiences an average of 2 crashes per month. Calculate:
a) P(no crashes next month)
b) P(exactly 3 crashes next month)
c) P(at least 1 crash next month)

<details>
<summary>💡 Show Solution</summary>

**Given:** λ = 2 crashes per month

**a) P(X = 0):**
$$P(X=0) = \frac{2^0 \cdot e^{-2}}{0!} = \frac{1 \times 0.1353}{1} = 0.1353$$
**Answer: 13.53%**

**b) P(X = 3):**
$$P(X=3) = \frac{2^3 \cdot e^{-2}}{3!} = \frac{8 \times 0.1353}{6} = 0.1804$$
**Answer: 18.04%**

**c) P(X ≥ 1):**
$$P(X \geq 1) = 1 - P(X=0) = 1 - 0.1353 = 0.8647$$
**Answer: 86.47%**

</details>

---

### Problem 2

A rare disease affects 1 in 10,000 people. In a city of 50,000 people, what's the probability that exactly 3 people have the disease?

*Hint: This is a Poisson approximation to Binomial (large n, small p).*

<details>
<summary>💡 Show Solution</summary>

**Poisson approximation:** λ = np = 50,000 × (1/10,000) = 5

**Calculate P(X = 3):**
$$P(X=3) = \frac{5^3 \cdot e^{-5}}{3!} = \frac{125 \times 0.00674}{6} = 0.1404$$

**Answer: 14.04%**

Note: The Binomial calculation would give a very similar answer.

</details>

---

### Problem 3

A manufacturing process produces defects at a rate of 0.5 per square meter. For a 6 square meter sheet:
a) What's the expected number of defects?
b) What's the probability of a perfect sheet (no defects)?
c) What's the probability of at most 2 defects?

<details>
<summary>💡 Show Solution</summary>

**Given:** Rate = 0.5 per m², Area = 6 m²
**λ = 0.5 × 6 = 3** defects expected

**a) Expected defects:**
$$E(X) = \lambda = 3$$

**b) P(X = 0):**
$$P(X=0) = \frac{3^0 \cdot e^{-3}}{0!} = e^{-3} = 0.0498$$
**Answer: 4.98%**

**c) P(X ≤ 2) = P(0) + P(1) + P(2):**
- P(X=0) = 0.0498
- P(X=1) = $\frac{3^1 \cdot e^{-3}}{1!} = 3 \times 0.0498 = 0.1494$
- P(X=2) = $\frac{3^2 \cdot e^{-3}}{2!} = \frac{9 \times 0.0498}{2} = 0.2240$

$$P(X \leq 2) = 0.0498 + 0.1494 + 0.2240 = 0.4232$$
**Answer: 42.32%**

</details>

---

## Changing the Interval

If λ is given for one interval, you can adjust for different intervals:

**Example:** 
- Average of 3 calls per hour
- What about 30 minutes? λ = 3/2 = 1.5
- What about 2 hours? λ = 3 × 2 = 6

**The rate scales linearly with the interval size.**

---

## Poisson vs Binomial

| Feature | Poisson | Binomial |
|---------|---------|----------|
| What we count | Events in interval | Successes in n trials |
| n (trials) | Not defined | Fixed |
| Rate/probability | λ (rate) | p (probability) |
| Use when | Events in continuous interval | Fixed discrete trials |

**Poisson approximates Binomial** when:
- n is large (≥ 100)
- p is small (≤ 0.01)
- Use λ = np

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Using wrong λ for the interval.
> If rate is "per hour" and you want "per 2 hours," multiply λ by 2.

> ⚠️ **Mistake 2:** Forgetting e^(-λ).
> Every Poisson calculation includes this term.

> ⚠️ **Mistake 3:** Using Poisson when trials are fixed.
> Fixed number of trials → Binomial, not Poisson.

---

## Key Takeaways

- **Use Poisson** for counting events in a fixed interval
- **Formula:** $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$
- **Mean = Variance = λ** (unique property)
- λ scales with interval size
- Poisson approximates Binomial for large n, small p

---

## Navigation

[← Binomial](binomial.md) | [Module Index](index.md) | [Next: Hypergeometric →](hypergeometric.md)

**Related Reference:** [Distribution Table](../reference/distribution_table.md)


