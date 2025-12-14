---
title: "I can apply the Hypergeometric distribution"
category: "Statistics Bootcamp"
module: 5
order: 3
---

# I can apply the Hypergeometric distribution

> 📚 **Overview:** The Hypergeometric distribution models sampling without replacement from a finite population—essential for quality control.

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
- Identify when to use the Hypergeometric distribution
- Calculate Hypergeometric probabilities
- Understand how it differs from Binomial
- Apply it to quality control and sampling problems

---

## Key Concepts

### When to Use Hypergeometric

Use the Hypergeometric distribution when:

1. **Finite population** of size N
2. **Sampling without replacement**
3. Population has K "successes" and N-K "failures"
4. You draw n items and want probability of k successes

> 💡 **Key difference from Binomial:** In Hypergeometric, each draw changes the probability for the next draw (no replacement).

---

### Notation and Formula

$$
X \sim Hyp(N, K, n)
$$

**Probability Mass Function:**

$$
P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}
$$

Where:
- $N$ = population size
- $K$ = number of success items in population
- $n$ = sample size (number drawn)
- $k$ = number of successes in sample

---

### Understanding the Formula

$$
P(X = k) = \frac{\text{(ways to choose k from K)} \times \text{(ways to choose n-k from N-K)}}{\text{(ways to choose n from N)}}
$$

Think of it as: (favorable combinations) / (total combinations)

---

### Mean and Variance

**Mean:**

$$
\mu = E(X) = n \cdot \frac{K}{N}
$$

**Variance:**

$$
\sigma^2 = n \cdot \frac{K}{N} \cdot \frac{N-K}{N} \cdot \frac{N-n}{N-1}
$$

The last term $\frac{N-n}{N-1}$ is the **finite population correction**.

---

## Worked Example

**Problem:**
A box contains 12 items: 4 defective and 8 good. You randomly select 5 items. What is the probability of getting exactly 2 defective items?

**Solution:**

### Step 1: Identify Parameters
- N = 12 (total items)
- K = 4 (defective items)
- n = 5 (items selected)
- k = 2 (defective items we want)

### Step 2: Apply Formula

$$
P(X = 2) = \frac{\binom{4}{2} \binom{8}{3}}{\binom{12}{5}}
$$

### Step 3: Calculate Combinations

$$
\binom{4}{2} = \frac{4!}{2! \cdot 2!} = 6
$$

$$
\binom{8}{3} = \frac{8!}{3! \cdot 5!} = \frac{8 \times 7 \times 6}{6} = 56
$$

$$
\binom{12}{5} = \frac{12!}{5! \cdot 7!} = \frac{12 \times 11 \times 10 \times 9 \times 8}{120} = 792
$$

### Step 4: Calculate Probability

$$
P(X = 2) = \frac{6 \times 56}{792} = \frac{336}{792} = 0.4242
$$

**Answer: 42.42% probability of exactly 2 defective items.**

---

## Practice Problems

### Problem 1

A deck of 52 cards contains 13 hearts. You draw 5 cards without replacement. Calculate:
a) P(exactly 2 hearts)
b) P(no hearts)
c) P(all 5 are hearts)

<details>
<summary>💡 Show Solution</summary>

**Parameters:** N = 52, K = 13 (hearts), n = 5

**a) P(X = 2):**

$$
P(X=2) = \frac{\binom{13}{2}\binom{39}{3}}{\binom{52}{5}}
$$

$$
= \frac{78 \times 9,139}{2,598,960} = \frac{712,842}{2,598,960} = 0.2743
$$

**Answer: 27.43%**

**b) P(X = 0):**

$$
P(X=0) = \frac{\binom{13}{0}\binom{39}{5}}{\binom{52}{5}}
$$

$$
= \frac{1 \times 575,757}{2,598,960} = 0.2215
$$

**Answer: 22.15%**

**c) P(X = 5):**

$$
P(X=5) = \frac{\binom{13}{5}\binom{39}{0}}{\binom{52}{5}}
$$

$$
= \frac{1,287 \times 1}{2,598,960} = 0.000495
$$

**Answer: 0.0495% (about 1 in 2000)**

</details>

---

### Problem 2

A quality inspector selects 10 items from a shipment of 100 items, of which 15 are defective. What's the probability of finding:
a) Exactly 1 defective?
b) At least 1 defective?
c) More than 3 defectives?

<details>
<summary>💡 Show Solution</summary>

**Parameters:** N = 100, K = 15, n = 10

**a) P(X = 1):**

$$
P(X=1) = \frac{\binom{15}{1}\binom{85}{9}}{\binom{100}{10}}
$$

Using a calculator or software: **P(X = 1) ≈ 0.3472 (34.72%)**

**b) P(X ≥ 1) = 1 - P(X = 0):**

$$
P(X=0) = \frac{\binom{15}{0}\binom{85}{10}}{\binom{100}{10}} \approx 0.1847
$$

$$
P(X \geq 1) = 1 - 0.1847 = 0.8153
$$

**Answer: 81.53%**

**c) P(X > 3):**
This is 1 - P(X ≤ 3) = 1 - [P(0) + P(1) + P(2) + P(3)]
Using software: P(X > 3) ≈ 0.0401
**Answer: About 4%**

</details>

---

### Problem 3

A committee of 4 must be selected from a group of 10 people (6 men and 4 women). What's the probability the committee has:
a) Exactly 2 women?
b) All women?
c) At least 1 woman?

<details>
<summary>💡 Show Solution</summary>

**Parameters:** N = 10, K = 4 (women), n = 4 (committee size)

**a) P(exactly 2 women):**

$$
P(X=2) = \frac{\binom{4}{2}\binom{6}{2}}{\binom{10}{4}} = \frac{6 \times 15}{210} = \frac{90}{210} = 0.4286
$$

**Answer: 42.86%**

**b) P(all women):**

$$
P(X=4) = \frac{\binom{4}{4}\binom{6}{0}}{\binom{10}{4}} = \frac{1 \times 1}{210} = 0.00476
$$

**Answer: 0.48%**

**c) P(at least 1 woman):**

$$
P(X \geq 1) = 1 - P(X=0)
$$

$$
P(X=0) = \frac{\binom{4}{0}\binom{6}{4}}{\binom{10}{4}} = \frac{1 \times 15}{210} = 0.0714
$$

$$
P(X \geq 1) = 1 - 0.0714 = 0.9286
$$

**Answer: 92.86%**

</details>

---

## Hypergeometric vs Binomial

| Aspect | Hypergeometric | Binomial |
|--------|----------------|----------|
| Replacement | Without | With (or large population) |
| Probability | Changes each draw | Constant |
| Independence | Draws are dependent | Draws are independent |
| Population | Finite, known | Can be infinite |

**When to approximate Hypergeometric with Binomial:**
If n < 5% of N (sample is small relative to population), Binomial is a good approximation.

Example: Sampling 50 from 10,000 → Use Binomial with p = K/N

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Using Binomial when sampling without replacement from a small population.
> If n > 5% of N, use Hypergeometric.

> ⚠️ **Mistake 2:** Confusing N, K, n, and k.
> N = population, K = successes in population, n = sample size, k = successes we want.

> ⚠️ **Mistake 3:** Forgetting the constraint on k.
> k must be between max(0, n-(N-K)) and min(K, n).

---

## Key Takeaways

- **Use Hypergeometric** for sampling without replacement from finite population
- **Formula involves three combinations:** $\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$
- **Mean** = $n \cdot \frac{K}{N}$ (same as Binomial with p = K/N)
- If sample is small relative to population (<5%), Binomial approximation works
- Draws are NOT independent (each draw affects probabilities)

---

## Navigation

[← Poisson](poisson.md) | [Module Index](index.md) | [Next: Choosing Distribution →](choosing_distribution.md)

**Related Reference:** [Distribution Table](../reference/distribution_table.md)


