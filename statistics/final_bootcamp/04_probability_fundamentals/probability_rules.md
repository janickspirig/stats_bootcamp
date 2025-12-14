---
title: "I know the basic rules of probability"
category: "Statistics Bootcamp"
module: 4
order: 1
---

# I know the basic rules of probability

> 📚 **Overview:** Probability rules are the foundation for all statistical inference. Master these essential rules to build a strong foundation.

---

## 📑 Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Key Concepts](#key-concepts)
3. [Worked Example](#worked-example)
4. [Practice Problems](#practice-problems)
5. [Summary of Rules](#summary-of-rules)
6. [Key Takeaways](#key-takeaways)

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate probabilities using the complement rule
- Apply the addition rule for unions
- Apply the multiplication rule for intersections
- Identify mutually exclusive and independent events

---

## Key Concepts

### What is Probability?

**Probability** is a number between 0 and 1 that represents the likelihood of an event.

$$
0 \leq P(A) \leq 1
$$

- P(A) = 0: Event A is impossible
- P(A) = 1: Event A is certain
- P(A) = 0.5: Event A has a 50% chance

---

### Complement Rule

The probability of an event NOT occurring:

$$
P(A') = 1 - P(A)
$$

Or equivalently: P(A) + P(A') = 1

**Example:** If P(rain) = 0.3, then P(no rain) = 1 - 0.3 = 0.7

---

### Odds (Quoten)

Odds translate a probability into a “success vs failure” ratio.

$$
Odds(A) = \frac{P(A)}{P(A')}
$$

**Example:** If P(A) = 0.20, then Odds(A) = 0.20 / 0.80 = 0.25 (read: “1 to 4”).

---

### Addition Rule (OR)

For the probability of A OR B occurring:

**General Form:**

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

**For Mutually Exclusive Events** (cannot occur together):

$$
P(A \cup B) = P(A) + P(B)
$$

<!-- IMAGE_PLACEHOLDER
Type: venn_diagram
Description: Venn diagram showing two overlapping circles A and B. The overlap region is labeled "A ∩ B" (intersection). The formula P(A ∪ B) = P(A) + P(B) - P(A ∩ B) is shown below.
Data: Two overlapping circles
Style: Classic Venn diagram with labeled regions
Filename: addition_rule_venn.png
-->
![Addition rule Venn diagram](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/addition_rule_venn.png)

---

### Set Operations and Set Difference

Some exams explicitly use set notation beyond ∪ and ∩.

- **Set difference:** \(A \\setminus B\) means “A without B” (in A but not in B).

$$
P(A \\setminus B) = P(A) - P(A \\cap B)
$$

**Venn shading tip:** Shade the part of circle A that excludes the overlap region with B.

---

### Multiplication Rule (AND)

For the probability of A AND B occurring:

**General Form:**

$$
P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)
$$

**For Independent Events:**

$$
P(A \cap B) = P(A) \cdot P(B)
$$

---

### Types of Events

| Type | Definition | Example |
|------|------------|---------|
| **Mutually Exclusive** | Cannot happen together | Rolling 1 AND rolling 6 |
| **Independent** | One doesn't affect the other | Coin flip 1 AND coin flip 2 |
| **Dependent** | One affects the other | Card 1 AND card 2 (without replacement) |

> 💡 **Important:** Mutually exclusive events cannot be independent (if A happens, B can't, so A affects B).

---

## Worked Example

**Problem:**
A factory produces items. 70% pass quality inspection. Of those that pass, 90% work correctly. Of those that fail inspection, only 20% work correctly.

a) What is the probability that a randomly selected item works correctly?
b) What is the probability an item either passes inspection OR works correctly?

**Solution:**

### Part a: Probability of Working

Define events:
- P = Pass inspection, P(P) = 0.70
- P' = Fail inspection, P(P') = 0.30
- W = Works correctly

Given:
- P(W|P) = 0.90 (works, given passed)
- P(W|P') = 0.20 (works, given failed)

Use Law of Total Probability:

$$
P(W) = P(W|P) \cdot P(P) + P(W|P') \cdot P(P')
$$

$$
P(W) = 0.90 \times 0.70 + 0.20 \times 0.30 = 0.63 + 0.06 = 0.69
$$

**Answer: 69% of items work correctly.**

### Part b: Pass OR Works

First, find P(Pass AND Works):

$$
P(P \cap W) = P(W|P) \cdot P(P) = 0.90 \times 0.70 = 0.63
$$

Apply addition rule:

$$
P(P \cup W) = P(P) + P(W) - P(P \cap W) = 0.70 + 0.69 - 0.63 = 0.76
$$

**Answer: 76% either pass inspection or work correctly (or both).**

---

## Practice Problems

### Problem 1

A bag contains 5 red balls and 3 blue balls. You draw one ball at random.

a) What is P(red)?
b) What is P(blue)?
c) What is P(not red)?

<details>
<summary>💡 Show Solution</summary>

Total balls = 5 + 3 = 8

**a) P(red)** = 5/8 = 0.625

**b) P(blue)** = 3/8 = 0.375

**c) P(not red)** = 1 - P(red) = 1 - 5/8 = 3/8 = 0.375

Note: P(not red) = P(blue) because there are only two colors.

</details>

---

### Problem 2

You roll two fair dice. Find:
a) P(sum = 7)
b) P(at least one 6)
c) P(both dice show the same number)

<details>
<summary>💡 Show Solution</summary>

Total outcomes = 6 × 6 = 36

**a) P(sum = 7)**
Ways to get 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 ways
$$P(\text{sum}=7) = \frac{6}{36} = \frac{1}{6}$$

**b) P(at least one 6)**
Use complement: P(at least one 6) = 1 - P(no 6's)
P(no 6 on die 1) = 5/6
P(no 6 on die 2) = 5/6
P(no 6's) = (5/6)(5/6) = 25/36
$$P(\text{at least one 6}) = 1 - \frac{25}{36} = \frac{11}{36}$$

**c) P(both same)**
Same: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) = 6 ways
$$P(\text{same}) = \frac{6}{36} = \frac{1}{6}$$

</details>

---

### Problem 3

In a survey, 60% of people like coffee, 40% like tea, and 25% like both.

a) What percentage like coffee OR tea?
b) What percentage like neither?
c) Are liking coffee and tea independent events?

<details>
<summary>💡 Show Solution</summary>

Given: P(C) = 0.60, P(T) = 0.40, P(C ∩ T) = 0.25

**a) P(Coffee OR Tea)**
$$P(C \cup T) = P(C) + P(T) - P(C \cap T)$$
$$P(C \cup T) = 0.60 + 0.40 - 0.25 = 0.75$$

**Answer: 75%**

**b) P(Neither)**
$$P(\text{neither}) = 1 - P(C \cup T) = 1 - 0.75 = 0.25$$

**Answer: 25%**

**c) Independence Check**
If independent: P(C ∩ T) should equal P(C) × P(T)
$$P(C) \times P(T) = 0.60 \times 0.40 = 0.24$$

But P(C ∩ T) = 0.25 ≠ 0.24

**Answer: Not independent** (but very close!)

</details>

---

### Problem 4 (Set difference + odds)

Given: P(A) = 0.70, P(B) = 0.40, P(A ∩ B) = 0.30.

Calculate:
a) P(A \\ B)
b) Odds(A)

<details>
<summary>💡 Show Solution</summary>

**a) Set difference**

$$
P(A \\setminus B) = P(A) - P(A \\cap B) = 0.70 - 0.30 = 0.40
$$

**b) Odds**

P(A') = 1 − 0.70 = 0.30

$$
Odds(A) = \frac{P(A)}{P(A')} = \frac{0.70}{0.30} = 2.33
$$

Interpretation: Odds(A) ≈ 2.33 means A is about 2.33 times as likely as not-A.

</details>

---

## Summary of Rules

| Rule | Formula | When to Use |
|------|---------|-------------|
| Complement | P(A') = 1 - P(A) | "NOT" problems, "at least one" |
| Addition (General) | P(A∪B) = P(A) + P(B) - P(A∩B) | "OR" problems |
| Addition (Mutually Exclusive) | P(A∪B) = P(A) + P(B) | Events can't both happen |
| Multiplication (General) | P(A∩B) = P(A|B)·P(B) | "AND" problems |
| Multiplication (Independent) | P(A∩B) = P(A)·P(B) | Events don't affect each other |
| Set difference | P(A\\B) = P(A) - P(A∩B) | "A but not B" |
| Odds | Odds(A) = P(A)/P(A') | Convert probability into odds |

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Adding probabilities without subtracting overlap.
> P(A or B) = P(A) + P(B) is only valid if mutually exclusive!

> ⚠️ **Mistake 2:** Assuming events are independent without checking.
> Independence must be stated or verified.

> ⚠️ **Mistake 3:** Confusing mutually exclusive with independent.
> These are different concepts!

---

## Key Takeaways

> 🎯 **Remember:**
> - **Complement:** P(not A) = 1 - P(A)
> - **Addition rule:** Subtract intersection to avoid double-counting
> - **Multiplication rule:** Use P(A|B) for dependent events
> - **Mutually exclusive:** Can't happen together, P(A∩B) = 0
> - **Independent:** Don't affect each other, P(A∩B) = P(A)×P(B)

---

## Navigation

[← Module Index](index.md) | [Next: Conditional Probability →](conditional_probability.md)

**Related Reference:** [Formula Glossary](../reference/formula_glossary.md)


