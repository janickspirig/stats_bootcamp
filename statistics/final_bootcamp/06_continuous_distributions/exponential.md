---
title: "I can apply the Exponential distribution"
category: "Statistics Bootcamp"
module: 6
order: 4
---

# I can apply the Exponential distribution

> 📚 **Overview:** The Exponential distribution models waiting times between events—time until failure, next arrival, etc.

The Exponential distribution models waiting times between events.

---

## Learning Objectives

After completing this section, you will be able to:
- Identify when to use the Exponential distribution
- Calculate probabilities using the Exponential CDF
- Understand the memoryless property
- Connect Exponential and Poisson distributions

---

## Key Concepts

### When to Use Exponential

Use the Exponential distribution for:
- **Time between events** in a Poisson process
- **Waiting time** until the next event
- **Lifetime** of components with constant failure rate

---

### Notation and Formulas

$$X \sim Exp(\lambda)$$

**Probability Density Function (PDF):**
$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

**Cumulative Distribution Function (CDF):**
$$F(x) = P(X \leq x) = 1 - e^{-\lambda x}$$

**Survival Function:**
$$P(X > x) = e^{-\lambda x}$$

---

### Mean and Variance

**Mean (Expected waiting time):**
$$\mu = E(X) = \frac{1}{\lambda}$$

**Variance:**
$$\sigma^2 = Var(X) = \frac{1}{\lambda^2}$$

**Standard Deviation:**
$$\sigma = \frac{1}{\lambda}$$

> 💡 **Note:** Mean = Standard Deviation for Exponential distribution.

---

### Connection to Poisson

If events occur according to a **Poisson process with rate λ**, then:
- **Number of events** in time t follows Poisson(λt)
- **Time between events** follows Exponential(λ)

---

## Worked Example

**Problem:**
Customers arrive at a bank at an average rate of 3 per hour (Poisson process).

a) What is the probability that the next customer arrives within 10 minutes?
b) What is the probability of waiting more than 30 minutes for the next customer?
c) What is the expected waiting time between customers?

**Solution:**

### Setup

λ = 3 customers per hour = 3/60 = 0.05 per minute

### Part a: P(X ≤ 10 minutes)

$$P(X \leq 10) = 1 - e^{-0.05 \times 10} = 1 - e^{-0.5}$$
$$= 1 - 0.6065 = 0.3935$$

**Answer: 39.35%** probability of arrival within 10 minutes.

### Part b: P(X > 30 minutes)

$$P(X > 30) = e^{-0.05 \times 30} = e^{-1.5} = 0.2231$$

**Answer: 22.31%** probability of waiting more than 30 minutes.

### Part c: Expected waiting time

$$E(X) = \frac{1}{\lambda} = \frac{1}{0.05} = 20 \text{ minutes}$$

Or: 1 hour / 3 customers = 20 minutes between customers.

---

## Practice Problems

### Problem 1

Light bulbs have an average lifetime of 1000 hours (exponentially distributed).

a) What's the probability a bulb lasts more than 1200 hours?
b) What's the probability a bulb fails within the first 500 hours?
c) What's the median lifetime (50% of bulbs fail by this time)?

<details>
<summary>💡 Show Solution</summary>

**Setup:** Mean = 1000, so λ = 1/1000 = 0.001 per hour

**a) P(X > 1200):**
$$P(X > 1200) = e^{-0.001 \times 1200} = e^{-1.2} = 0.3012$$
**Answer: 30.12%**

**b) P(X ≤ 500):**
$$P(X \leq 500) = 1 - e^{-0.001 \times 500} = 1 - e^{-0.5} = 1 - 0.6065 = 0.3935$$
**Answer: 39.35%**

**c) Median (solve for P(X ≤ m) = 0.5):**
$$1 - e^{-\lambda m} = 0.5$$
$$e^{-\lambda m} = 0.5$$
$$-\lambda m = \ln(0.5) = -0.693$$
$$m = \frac{0.693}{\lambda} = 0.693 \times 1000 = 693 \text{ hours}$$
**Answer: Median = 693 hours**

</details>

---

### Problem 2

A call center receives calls at a rate of 4 per minute. Find:
a) P(next call within 15 seconds)
b) P(wait at least 30 seconds for next call)
c) Expected time until next call

<details>
<summary>💡 Show Solution</summary>

**Setup:** λ = 4 per minute = 4/60 per second ≈ 0.0667 per second

**a) P(X ≤ 15 seconds):**
$$P(X \leq 15) = 1 - e^{-0.0667 \times 15} = 1 - e^{-1} = 1 - 0.368 = 0.632$$
**Answer: 63.2%**

**b) P(X > 30 seconds):**
$$P(X > 30) = e^{-0.0667 \times 30} = e^{-2} = 0.135$$
**Answer: 13.5%**

**c) Expected time:**
$$E(X) = \frac{1}{4} \text{ minute} = 15 \text{ seconds}$$

</details>

---

### Problem 3

A server processes requests. Time between arrivals is exponential with mean 2 seconds.

a) What is λ?
b) What's the probability of no request in the next 5 seconds?
c) What's the probability of a request within 1 second?

<details>
<summary>💡 Show Solution</summary>

**a) Finding λ:**
Mean = 1/λ = 2, so λ = 0.5 per second

**b) P(X > 5):**
$$P(X > 5) = e^{-0.5 \times 5} = e^{-2.5} = 0.0821$$
**Answer: 8.21%**

**c) P(X ≤ 1):**
$$P(X \leq 1) = 1 - e^{-0.5 \times 1} = 1 - e^{-0.5} = 1 - 0.6065 = 0.3935$$
**Answer: 39.35%**

</details>

---

## The Memoryless Property

The Exponential distribution is **memoryless**:

$$P(X > s + t | X > s) = P(X > t)$$

**Interpretation:** If you've already waited s time units, the probability of waiting t more units is the same as starting fresh.

**Example:** If a light bulb has lasted 500 hours, the probability it lasts another 500 hours is the same as a new bulb lasting 500 hours.

> 💡 **Memoryless property** = the component doesn't "age" or "wear out" (constant failure rate assumption).

---

## Exponential vs Other Distributions

| Feature | Exponential | Normal | Poisson |
|---------|-------------|--------|---------|
| Type | Continuous | Continuous | Discrete |
| Values | x ≥ 0 | All real numbers | 0, 1, 2, ... |
| Shape | Right-skewed | Symmetric | Right-skewed |
| Memoryless | Yes | No | N/A |
| Use | Waiting time | Measurements | Event counts |

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Confusing λ with 1/λ.
> λ is the rate; 1/λ is the mean. Check which is given!

> ⚠️ **Mistake 2:** Using wrong units for λ.
> If λ = 3/hour and you want P(X < 30 minutes), convert carefully.

> ⚠️ **Mistake 3:** Expecting X to be normally distributed.
> Exponential is always right-skewed with mode at 0.

---

## Key Takeaways

- **Exponential** models time between Poisson events
- **CDF:** P(X ≤ x) = 1 - e^(-λx)
- **Mean** = 1/λ, **Variance** = 1/λ²
- **Memoryless:** Past waiting doesn't affect future probability
- Connected to **Poisson** (if events are Poisson, waiting is Exponential)

---

## Navigation

[← Normal Probabilities](normal_probabilities.md) | [Module Index](index.md) | [Next Module: Sampling Distributions →](../07_sampling_distributions/index.md)

**Related Reference:** [Distribution Table](../reference/distribution_table.md)


