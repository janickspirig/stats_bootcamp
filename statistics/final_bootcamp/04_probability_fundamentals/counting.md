---
title: "I can use counting techniques"
category: "Statistics Bootcamp"
module: 4
order: 4
---

# I can use counting techniques

> 📚 **Overview:** Counting techniques help us calculate probabilities by counting favorable outcomes—permutations, combinations, and factorials.

---

## 📑 Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Key Concepts](#key-concepts)
3. [Worked Example](#worked-example)
4. [Practice Problems](#practice-problems)
5. [Counting in Probability](#counting-in-probability)
6. [Key Takeaways](#key-takeaways)

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate factorials
- Use permutations when order matters
- Use combinations when order doesn't matter
- Apply counting techniques to probability problems

---

## Key Concepts

### Factorials

$$
n! = n \times (n-1) \times (n-2) \times ... \times 2 \times 1
$$

**Special case:** 0! = 1

| n | n! |
|---|-----|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 7 | 5,040 |
| 8 | 40,320 |
| 10 | 3,628,800 |

---

### Permutations (Order Matters)

**Definition:** Number of ways to arrange r items from n items when order matters.

$$
P(n,r) = \frac{n!}{(n-r)!}
$$

**Example:** How many ways can 3 people finish in 1st, 2nd, 3rd from a race of 10?

$$
P(10,3) = \frac{10!}{7!} = 10 \times 9 \times 8 = 720
$$

---

### Combinations (Order Doesn't Matter)

**Definition:** Number of ways to choose r items from n items when order doesn't matter.

$$
C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

**Example:** How many ways can you choose 3 people from a group of 10?

$$
C(10,3) = \frac{10!}{3! \cdot 7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = \frac{720}{6} = 120
$$

---

### When to Use Which?

| Scenario | Order Matters? | Use |
|----------|---------------|-----|
| Arrange 3 books on a shelf | Yes | Permutation |
| Pick a committee of 3 | No | Combination |
| Select 1st, 2nd, 3rd place | Yes | Permutation |
| Choose 5 cards from deck | No | Combination |
| Create a password | Yes | Permutation |
| Select lottery numbers | No | Combination |

> 💡 **Key question:** Does the ORDER of selection matter for the outcome?

---

## Worked Example

**Problem:**
A committee of 4 must be chosen from 6 men and 4 women. How many ways can the committee be formed if it must have exactly 2 men and 2 women?

**Solution:**

### Step 1: Identify What We're Counting
- Choose 2 men from 6 men
- Choose 2 women from 4 women
- Order doesn't matter (it's a committee) → Use combinations

### Step 2: Apply Multiplication Principle

$$\text{Total ways} = C(6,2) \times C(4,2)$$

### Step 3: Calculate Each Combination

$$C(6,2) = \frac{6!}{2! \cdot 4!} = \frac{6 \times 5}{2 \times 1} = 15$$

$$C(4,2) = \frac{4!}{2! \cdot 2!} = \frac{4 \times 3}{2 \times 1} = 6$$

### Step 4: Multiply

$$\text{Total} = 15 \times 6 = 90$$

**Answer:** There are 90 ways to form the committee.

---

## Practice Problems

### Problem 1

A password must be 4 digits (0-9), with no repeated digits. How many possible passwords are there?

<details>
<summary>💡 Show Solution</summary>

Order matters (1234 ≠ 4321), no repetition → Permutation

$$P(10,4) = \frac{10!}{6!} = 10 \times 9 \times 8 \times 7 = 5,040$$

**Answer:** 5,040 possible passwords

Alternative calculation:
- 1st digit: 10 choices
- 2nd digit: 9 choices (one used)
- 3rd digit: 8 choices
- 4th digit: 7 choices
- Total: 10 × 9 × 8 × 7 = 5,040

</details>

---

### Problem 2

From a deck of 52 cards, you draw 5 cards. 
a) How many possible 5-card hands are there?
b) How many hands contain exactly 3 hearts?

<details>
<summary>💡 Show Solution</summary>

**a) Total 5-card hands:**
Order doesn't matter → Combination
$$C(52,5) = \frac{52!}{5! \cdot 47!} = \frac{52 \times 51 \times 50 \times 49 \times 48}{120} = 2,598,960$$

**b) Exactly 3 hearts:**
- Choose 3 hearts from 13 hearts: C(13,3)
- Choose 2 non-hearts from 39 non-hearts: C(39,2)

$$C(13,3) \times C(39,2) = 286 \times 741 = 211,926$$

**Answer:** 211,926 hands with exactly 3 hearts

</details>

---

### Problem 3

A lottery requires selecting 6 numbers from 1-49. What is the probability of winning (matching all 6)?

<details>
<summary>💡 Show Solution</summary>

**Total ways to choose 6 from 49:**
$$C(49,6) = \frac{49!}{6! \cdot 43!} = \frac{49 \times 48 \times 47 \times 46 \times 45 \times 44}{720} = 13,983,816$$

**Favorable outcomes:** 1 (only one winning combination)

**Probability:**
$$P(\text{win}) = \frac{1}{13,983,816} \approx 0.0000000715$$

**Answer:** About 1 in 14 million chance (0.00000715%)

</details>

---

## Counting in Probability

The basic probability formula:
$$P(A) = \frac{\text{Favorable outcomes}}{\text{Total outcomes}}$$

Use counting techniques to find both numerator and denominator.

### Example: Cards

**Problem:** What's the probability of being dealt a flush (5 cards, same suit)?

**Total 5-card hands:** C(52,5) = 2,598,960

**Flush hands:**
- Choose 1 suit: 4 ways
- Choose 5 cards from that suit: C(13,5) = 1,287

Total flushes: 4 × 1,287 = 5,148

**Probability:**
$$P(\text{flush}) = \frac{5,148}{2,598,960} = 0.00198 \approx 0.2\%$$

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Using permutations when combinations are needed.
> Ask: Does order matter? If not, use combinations.

> ⚠️ **Mistake 2:** Forgetting to multiply independent choices.
> When selecting from multiple groups, multiply the counts.

> ⚠️ **Mistake 3:** Calculation errors with factorials.
> Simplify before calculating: $\frac{10!}{8!} = 10 \times 9$, not full factorials.

---

## Quick Reference

| Formula | When to Use |
|---------|-------------|
| $n!$ | Total arrangements of n items |
| $P(n,r) = \frac{n!}{(n-r)!}$ | Order matters, no replacement |
| $C(n,r) = \frac{n!}{r!(n-r)!}$ | Order doesn't matter |
| $n^r$ | Order matters, with replacement |

---

## Key Takeaways

> 🎯 **Remember:**
> - **Permutations:** Order matters, use P(n,r)
> - **Combinations:** Order doesn't matter, use C(n,r)
> - **Multiplication principle:** Multiply independent choices
> - Always simplify factorials before calculating
> - Counting feeds directly into probability calculations

---

## Navigation

[← Bayes' Theorem](bayes_theorem.md) | [Module Index](index.md) | [Next: Expected Value →](expected_value.md)

**Related Reference:** [Formula Glossary](../reference/formula_glossary.md)


