---
title: "I can work with odds and odds ratios"
category: "Statistics Bootcamp"
module: 4
order: 6
---

# I can work with odds and odds ratios

> 📚 **Overview:** Convert between probability and odds, and interpret odds ratios (OR).

---

## Learning Objectives

After completing this section, you will be able to:
- Convert probability \(p\\) to odds and back
- Compute an odds ratio (OR) for two groups
- Interpret odds and OR in plain language

---

## Intuition (probability vs odds)

Probability \(p\) answers: “Out of all cases, how often does the event happen?”

Odds answer a slightly different question: “How many **event** cases do we expect **per non-event** case?”

- If \(p=0.50\), odds \(=0.50/0.50=1\): about **1 event per 1 non-event**.
- If \(p=0.10\), odds \(=0.10/0.90=0.111\): about **1 event per 9 non-events**.

An **odds ratio** compares odds between two groups. OR = 2 means the odds are twice as high in group 1 as in group 0.

---

## When to use / when not to use

- **Use when**: comparing event likelihood between two groups using a 2×2 table (e.g., default vs non-default by customer type).
- **Use when**: interpreting coefficients from logistic regression (OR is the natural scale there; advanced context).
- **Do not use when**: you want “probability is X times larger” (that is a **risk ratio**, not an OR).

---

## Definitions

### Odds

If an event has probability \(p\\), then its **odds** are:

$$
\\text{odds} = \\frac{p}{1-p}
$$

To convert odds \(o\\) back to probability:

$$
p = \\frac{o}{1+o}
$$

---

### Odds ratio (OR)

For two groups (1 and 0) with probabilities \(p_1\\) and \(p_0\\):

$$
OR = \\frac{\\frac{p_1}{1-p_1}}{\\frac{p_0}{1-p_0}}
$$

Interpretation:
- OR = 1 → same odds in both groups
- OR > 1 → higher odds in group 1
- OR < 1 → lower odds in group 1

---

## Interpretation sentence templates (exam-ready)

- “The odds of **[event]** are **[OR]×** as high in group 1 as in group 0.”
- “OR = [..] (>1) indicates higher odds in group 1; OR < 1 indicates lower odds.”

---

## Common traps (high-frequency)

> ⚠️ **Trap 1: Interpreting OR as ‘probability doubles’.**
> OR = 2 does *not* mean the probability is 2×. The probability change depends on the baseline rate.

> ⚠️ **Trap 2: Mixing up OR and risk ratio (RR).**
> OR ≈ RR only when the event is rare; otherwise OR can look much larger than RR.

> ⚠️ **Trap 3: Swapping group 0/1.**
> Always state which group is the numerator (OR for group 1 relative to group 0).

---

## Worked Examples

### Example 1 (probability → odds)

If \(P(\\text{Default})=0.08\\), compute the odds of default.

<details>
<summary>💡 Show Solution</summary>

$$
\\text{odds} = \\frac{0.08}{1-0.08} = \\frac{0.08}{0.92} = 0.0870
$$

Interpretation: odds ≈ 0.087 means about 0.087 defaults per 1 non-default (≈ 1 to 11.5).

</details>

---

### Example 2 (odds → probability)

If odds = 0.25, what is the probability?

<details>
<summary>💡 Show Solution</summary>

$$
p = \\frac{0.25}{1+0.25} = \\frac{0.25}{1.25} = 0.20
$$

</details>

---

### Example 3 (odds ratio)

Group 1 has event probability \(p_1=0.20\\), group 0 has event probability \(p_0=0.10\\). Compute OR.

<details>
<summary>💡 Show Solution</summary>

Odds in group 1: \(0.20/0.80=0.25\\)  
Odds in group 0: \(0.10/0.90=0.1111\\)

$$
OR = \\frac{0.25}{0.1111} = 2.25
$$

Interpretation: the odds of the event are about **2.25×** higher in group 1 than in group 0.

</details>

---

## Practice Problems

### Problem 1

Convert probability \(p=0.40\\) to odds.

<details>
<summary>💡 Show Solution</summary>

$$
\\text{odds} = \\frac{0.40}{0.60} = 0.6667
$$

</details>

---

### Problem 2

Group A has odds 0.50 and group B has odds 0.25. Compute OR (A relative to B).

<details>
<summary>💡 Show Solution</summary>

$$
OR = \\frac{0.50}{0.25} = 2
$$

</details>

---

## Navigation

[← Bayes' Theorem](bayes_theorem.md) | [Module Index](index.md) | [Next: Counting →](counting.md)


