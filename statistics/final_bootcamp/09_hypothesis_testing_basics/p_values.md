---
title: "I can interpret p-values"
category: "Statistics Bootcamp"
module: 9
order: 4
---

# I can interpret p-values

> 📚 **Overview:** What p-values really mean and don't mean—avoid the common misinterpretations.

Understanding what p-values mean (and don't mean).

---

## Learning Objectives

After completing this section, you will be able to:
- Define p-value correctly
- Interpret p-values in context
- Avoid common misinterpretations

---

## Key Concepts

### Definition

> **P-value:** The probability of observing a test statistic as extreme as (or more extreme than) the one calculated, assuming H₀ is true.

$$\text{p-value} = P(\text{data as extreme or more} \mid H_0 \text{ is true})$$

![P-value as shaded area under the curve for one-tailed and two-tailed tests](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/p_value_shaded_area_one_two_tailed.png)

---

### Decision Rule

| If p-value... | Then... | Interpretation |
|---------------|---------|----------------|
| ≤ α | Reject H₀ | Statistically significant |
| > α | Fail to reject H₀ | Not statistically significant |

---

### What P-Value IS

- Probability of the data (or more extreme), given H₀
- Measure of evidence against H₀
- Smaller p → stronger evidence against H₀

### What P-Value IS NOT

❌ Probability that H₀ is true
❌ Probability that results are due to chance
❌ Size of the effect
❌ Probability of making an error

---

## Worked Example

**Problem:**
A test of H₀: μ = 100 vs H₁: μ ≠ 100 yields p = 0.03.

a) Interpret this p-value.
b) At α = 0.05, what is the decision?
c) At α = 0.01, what is the decision?

**Solution:**

**a) Interpretation:**
If the true mean were 100, there's only a 3% chance of observing a sample mean as far from 100 as we observed.

**b) At α = 0.05:**
p = 0.03 < 0.05 → **Reject H₀**
The result is statistically significant at the 5% level.

**c) At α = 0.01:**
p = 0.03 > 0.01 → **Fail to reject H₀**
The result is not significant at the 1% level.

---

## Practice Problems

### Problem 1

Match each p-value to its interpretation:

| P-value | Evidence against H₀ |
|---------|---------------------|
| 0.45 | A) Very strong |
| 0.08 | B) Moderate |
| 0.03 | C) Little to none |
| 0.001 | D) Some |

<details>
<summary>💡 Show Solution</summary>

- 0.45 → **C) Little to none**
- 0.08 → **D) Some** (marginal)
- 0.03 → **B) Moderate** (significant at 0.05)
- 0.001 → **A) Very strong**

</details>

---

### Problem 2

Which of these is a correct interpretation of p = 0.04?

a) "There's a 4% chance H₀ is true."
b) "There's a 4% chance the results are due to random chance."
c) "If H₀ were true, there's a 4% chance of seeing results this extreme."
d) "The probability of Type I error is 4%."

<details>
<summary>💡 Show Solution</summary>

**Correct: c)**

"If H₀ were true, there's a 4% chance of seeing results this extreme."

**Why others are wrong:**
- a) P-value is not probability H₀ is true
- b) This conflates p-value with probability of H₀
- d) Type I error probability is α, which we set before testing

</details>

---

## Common Misconceptions

| Misconception | Reality |
|---------------|---------|
| "p = 0.05 means 5% chance H₀ is true" | P-value is about data, not hypotheses |
| "p < 0.05 means the effect is large" | Statistical significance ≠ practical significance |
| "p = 0.051 means no effect" | Arbitrary cutoff; evidence is similar to p = 0.049 |
| "p > 0.05 proves H₀ is true" | Absence of evidence ≠ evidence of absence |

---

## Key Takeaways

- **P-value** = P(data as extreme | H₀ true)
- **Smaller p** = stronger evidence against H₀
- If p ≤ α → reject H₀ (significant)
- If p > α → fail to reject H₀ (not significant)
- P-value is NOT the probability H₀ is true

---

## Navigation

[← Error Types](error_types.md) | [Module Index](index.md) | [Next: Testing Framework →](testing_framework.md)


