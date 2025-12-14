---
title: "I can state hypotheses correctly"
category: "Statistics Bootcamp"
module: 9
order: 2
---

# I can state hypotheses correctly

> 📚 **Overview:** Formulating null and alternative hypotheses—the critical first step in any test.

The foundation of any hypothesis test is properly stated hypotheses.

---

## Learning Objectives

After completing this section, you will be able to:
- Write null and alternative hypotheses
- Identify one-tailed vs two-tailed tests
- Choose the correct hypothesis structure for different scenarios

---

## Key Concepts

### The Two Hypotheses

| Hypothesis | Symbol | Contains | Description |
|------------|--------|----------|-------------|
| Null | H₀ | Equality (=) | Status quo, no effect |
| Alternative | H₁ | Inequality (≠, <, >) | What we want to detect |

---

### Rules for Writing Hypotheses

1. **H₀ always contains =** (either =, ≤, or ≥)
2. **H₁ contains the opposite** (≠, >, or <)
3. **Together they are exhaustive** (cover all possibilities)
4. **H₁ usually contains what you're trying to prove**

---

### Types of Tests

| Test Type | H₀ | H₁ | When to Use |
|-----------|-----|-----|-------------|
| Two-tailed | μ = μ₀ | μ ≠ μ₀ | Detect any difference |
| Right-tailed | μ ≤ μ₀ | μ > μ₀ | Detect increase |
| Left-tailed | μ ≥ μ₀ | μ < μ₀ | Detect decrease |

![Cheatsheet mapping H1 direction to tail shading](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/hypotheses_tail_direction_cheatsheet.png)

---

## Worked Example

**Problem:**
A manufacturer claims batteries last at least 100 hours on average. A consumer group suspects they last less. State the hypotheses.

**Solution:**

**What we want to prove:** Batteries last LESS than 100 hours.

This goes in H₁:
- H₀: μ ≥ 100 (manufacturer's claim)
- H₁: μ < 100 (consumer group's suspicion)

**Test type:** Left-tailed (looking for decrease)

---

## Practice Problems

### Problem 1

State hypotheses for each scenario:

a) Testing if a new drug lowers blood pressure below 120 mmHg
b) Testing if a new website design changes conversion rate (currently 5%)
c) Testing if employee satisfaction differs from the national average of 7.0

<details>
<summary>💡 Show Solution</summary>

**a) Drug lowers blood pressure:**
- H₀: μ ≥ 120
- H₁: μ < 120 (left-tailed)

**b) Website changes conversion rate:**
- H₀: p = 0.05
- H₁: p ≠ 0.05 (two-tailed)

**c) Satisfaction differs from 7.0:**
- H₀: μ = 7.0
- H₁: μ ≠ 7.0 (two-tailed)

</details>

---

### Problem 2

Which hypothesis contains what we want to prove?

<details>
<summary>💡 Show Solution</summary>

**H₁ (the alternative hypothesis)** contains what we're trying to prove.

We "put the burden of proof" on the claim we want to make. We only reject H₀ if there's strong evidence for H₁.

</details>

---

## Key Takeaways

- **H₀ always contains =** (equality or "at least"/"at most")
- **H₁ contains what you want to detect**
- Two-tailed: look for any difference
- One-tailed: look for change in specific direction

---

## Navigation

[← Module Index](index.md) | [Next: Type I and Type II Errors →](error_types.md)


