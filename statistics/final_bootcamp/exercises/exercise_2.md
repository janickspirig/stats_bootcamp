---
title: "Exercise 2: Probability"
category: "Statistics Bootcamp"
module: 98
order: 2
---

# Exercise 2: Probability

> 📚 **Overview:** Practice probability rules, conditional probability, and Bayes' theorem.

Practice problems covering probability rules and Bayes' theorem.

---

## Topics Covered
- Basic probability rules
- Conditional probability
- Bayes' theorem
- Counting techniques

---

## Problem 1

A bag contains 4 red, 3 blue, and 5 green balls. If you draw one ball:
a) P(red)
b) P(not green)
c) P(red or blue)

<details>
<summary>💡 Show Solution</summary>

Total = 12 balls

**a) P(red) = 4/12 = 1/3 = 0.333**

**b) P(not green) = 1 - P(green) = 1 - 5/12 = 7/12 = 0.583**

**c) P(red or blue) = P(red) + P(blue) = 4/12 + 3/12 = 7/12 = 0.583**

</details>

---

## Problem 2

In a company:
- 40% of employees are in Sales
- 70% of Sales employees have met their quota
- 50% of non-Sales employees have met their quota

If an employee has met their quota, what's the probability they are in Sales?

<details>
<summary>💡 Show Solution</summary>

**Given:**
- P(Sales) = 0.40, P(Not Sales) = 0.60
- P(Quota|Sales) = 0.70
- P(Quota|Not Sales) = 0.50

**Find P(Sales|Quota) using Bayes:**

$$
P(\text{Quota}) = 0.70(0.40) + 0.50(0.60) = 0.28 + 0.30 = 0.58
$$

$$
P(\text{Sales}|\text{Quota}) = \frac{0.70 \times 0.40}{0.58} = \frac{0.28}{0.58} = 0.483
$$

**Answer: 48.3%**

</details>

---

## Problem 3

How many ways can you:
a) Arrange 5 books on a shelf
b) Choose 3 people from 10 for a committee

<details>
<summary>💡 Show Solution</summary>

**a) Arrangements (order matters):**

$$
5! = 120
$$

**b) Combinations (order doesn't matter):**

$$
C(10,3) = \frac{10!}{3!7!} = \frac{10 \times 9 \times 8}{6} = 120
$$

</details>

---

## Problem 4 (Set operations)

Given: P(A) = 0.7, P(B) = 0.4, P(A ∩ B) = 0.3.

Calculate:
a) P(A ∪ B)
b) P(A \\ B)
c) P(B \\ A)
d) P(neither A nor B)

<details>
<summary>💡 Show Solution</summary>

a) \(P(A \\cup B) = 0.7 + 0.4 - 0.3 = 0.8\)
b) \(P(A \\setminus B) = P(A) - P(A \\cap B) = 0.7 - 0.3 = 0.4\)
c) \(P(B \\setminus A) = P(B) - P(A \\cap B) = 0.4 - 0.3 = 0.1\)
d) P(neither) = 1 − P(A ∪ B) = 1 − 0.8 = 0.2

</details>

---

## Problem 5 (Odds)

If P(Default) = 0.08 for a loan portfolio, compute the odds of default.

<details>
<summary>💡 Show Solution</summary>

P(Default') = 1 − 0.08 = 0.92
Odds(Default) = 0.08 / 0.92 = 0.0870

Interpretation: odds ≈ 0.087 means about 0.087 “defaults” per 1 “non-default” (roughly 1 to 11.5).

</details>

---

## Problem 6 (Contingency table / conditional probability)

A store records whether a customer bought Product A and whether they used a coupon:

|  | Coupon | No coupon | Total |
|---|---:|---:|---:|
| Bought A | 60 | 40 | 100 |
| Did not buy A | 90 | 110 | 200 |
| Total | 150 | 150 | 300 |

Calculate:
a) P(Bought A)
b) P(Coupon)
c) P(Bought A | Coupon)
d) Are “Bought A” and “Coupon” independent?

<details>
<summary>💡 Show Solution</summary>

a) P(Bought A) = 100/300 = 0.333
b) P(Coupon) = 150/300 = 0.500
c) P(Bought A | Coupon) = 60/150 = 0.400
d) Independence check: P(Bought A) × P(Coupon) = 0.333 × 0.500 = 0.1665, but P(Bought A ∩ Coupon) = 60/300 = 0.200 → not equal ⇒ not independent.

</details>

---

## Problem 7 (Bayes with test accuracy)

A quality test flags defective items:
- Defect rate: P(D) = 0.04
- Sensitivity: P(Flag | D) = 0.90
- False positive rate: P(Flag | D') = 0.08

If an item is flagged, what is P(D | Flag)?

<details>
<summary>💡 Show Solution</summary>

P(Flag) = 0.90·0.04 + 0.08·0.96 = 0.036 + 0.0768 = 0.1128
P(D | Flag) = (0.90·0.04)/0.1128 = 0.036/0.1128 = 0.319

Answer: ~31.9% of flagged items are actually defective.

Business interpretation: Most flags are false positives; consider a second confirmatory test before scrapping items.

</details>

---

## Problem 8 (Counting, multi-part)

A company is selecting a 3-person project team from 8 candidates.

a) How many teams are possible?
b) If the team has roles (Lead, Analyst, Presenter), how many assignments are possible?

<details>
<summary>💡 Show Solution</summary>

a) Teams (order doesn’t matter): C(8,3) = 56
b) Roles (order matters): P(8,3) = 8×7×6 = 336

</details>

---

## Problem 9 (Conditional probabilities from intersections)

Given events A and B with:
- P(A) = 0.30
- P(B) = 0.40
- P(A ∩ B) = 0.15

Compute:
a) P(A | B)  
b) P(B | A)  
c) P(A ∪ B)  
d) P(neither A nor B)

<details>
<summary>💡 Show Solution</summary>

a) \(P(A\\mid B)=\\frac{P(A\\cap B)}{P(B)}=0.15/0.40=0.375\\)

b) \(P(B\\mid A)=\\frac{P(A\\cap B)}{P(A)}=0.15/0.30=0.50\\)

c) \(P(A\\cup B)=P(A)+P(B)-P(A\\cap B)=0.30+0.40-0.15=0.55\\)

d) \(P(\\text{neither})=1-P(A\\cup B)=1-0.55=0.45\\)

</details>

---

## Problem 10 (Bayes with confirmatory test)

A screening process uses **two tests** in sequence. Assume the results of Test 1 and Test 2 are independent **given** the true status.

- Prevalence: P(D) = 0.02
- Test 1: P(+ | D) = 0.95, P(+ | D') = 0.10
- Test 2: P(+ | D) = 0.99, P(+ | D') = 0.02

If both tests are positive, compute \(P(D\\mid ++ )\\).

<details>
<summary>💡 Show Solution</summary>

Given D:

$$
P(++\\mid D)=0.95\\cdot 0.99=0.9405
$$

Given not D:

$$
P(++\\mid D')=0.10\\cdot 0.02=0.002
$$

Total probability of two positives:

$$
P(++) = 0.9405\\cdot 0.02 + 0.002\\cdot 0.98
= 0.01881 + 0.00196
= 0.02077
$$

Bayes:

$$
P(D\\mid ++) = \\frac{0.9405\\cdot 0.02}{0.02077} = \\frac{0.01881}{0.02077} = 0.906
$$

Interpretation: If both tests are positive, there is about a **90.6%** chance the item is truly defective.

</details>

---

## Problem 11 (Odds ↔ probability conversion)

The odds of default are reported as 0.25. Compute the probability of default.

<details>
<summary>💡 Show Solution</summary>

Odds \(o = p/(1-p)\\). Solve for p:

$$
p = \\frac{o}{1+o} = \\frac{0.25}{1.25} = 0.20
$$

Probability of default = **0.20**.

</details>

---

## Problem 12 (Independence check via conditional probability)

Two events A and B satisfy P(A) = 0.60, P(B) = 0.50.

Case 1: P(A | B) = 0.60  
Case 2: P(A | B) = 0.80

For each case, decide whether A and B are independent.

<details>
<summary>💡 Show Solution</summary>

Independence means \(P(A\\mid B)=P(A)\\).

- Case 1: 0.60 = 0.60 → **independent**.
- Case 2: 0.80 ≠ 0.60 → **not independent**.

</details>

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Using P(A)+P(B) for “A or B” when events overlap.
> Only valid if mutually exclusive.
> ⚠️ **Mistake 2:** Confusing independence with mutually exclusive.
> Independent means probabilities multiply; mutually exclusive means intersection is 0.
> ⚠️ **Mistake 3:** Forgetting to compute the denominator in Bayes (total probability).

---

## Key Takeaways

- Translate words → symbols (∪, ∩, \\)
- Bayes requires **P(Flag)** / total probability
- Counting: combinations (choose) vs permutations (arrange)

---

## Related Module

[Module 04: Probability Fundamentals](../04_probability_fundamentals/index.md)

---

## Navigation

[← Exercise 1](exercise_1.md) | [Exercises Index](index.md) | [Exercise 3A →](exercise_3a.md)


