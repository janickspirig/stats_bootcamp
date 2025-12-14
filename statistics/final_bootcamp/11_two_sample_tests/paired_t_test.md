---
title: "I can compare paired samples"
category: "Statistics Bootcamp"
module: 11
order: 2
---

# I can compare paired samples

> 📚 **Overview:** Paired t-test for before/after or matched-pairs designs.

Testing matched or repeated measurements.

**Canonical workflow:** Review the 5-step template first: [Testing Framework](../09_hypothesis_testing_basics/testing_framework.md)

---

## Learning Objectives

After completing this section, you will be able to:
- Identify when to use a paired t-test
- Calculate differences and conduct the test
- Interpret results correctly

---

## Checklist

- **When to use:** Before/after on the same subjects, or matched pairs.
- **Workflow:** Convert to differences \(d_i\), then run a one-sample t-test on the differences.
- **What to report:** H₀/H₁ about μd, α and tail, \(\\bar{d}\), \(s_d\), df = n−1, t value, critical value (or p-value), decision, conclusion in context.
- **Common trap:** Don’t treat paired data as independent samples.

---

## Key Formula

$$
t = \frac{\bar{d}}{s_d/\sqrt{n}}
$$

Where:
- $d_i = x_{1i} - x_{2i}$ (difference for each pair)
- $\bar{d}$ = mean of differences
- $s_d$ = standard deviation of differences
- n = number of pairs
- df = n - 1

---

## When to Use Paired Test

- Before/after measurements on same subjects
- Matched pairs (twins, similar subjects)
- Same subject, two conditions

---

## Worked Example

**Problem:**
Blood pressure is measured before and after treatment for 8 patients:

| Patient | Before | After | Difference |
|---------|--------|-------|------------|
| 1 | 145 | 138 | 7 |
| 2 | 150 | 142 | 8 |
| 3 | 130 | 128 | 2 |
| 4 | 155 | 145 | 10 |
| 5 | 140 | 135 | 5 |
| 6 | 148 | 140 | 8 |
| 7 | 135 | 130 | 5 |
| 8 | 142 | 138 | 4 |

Test if treatment reduces blood pressure at α = 0.05.

**Solution:**

### Step 1: Hypotheses
- H₀: μd ≤ 0 (no reduction)
- H₁: μd > 0 (reduction)

### Step 2: Calculate Statistics
Differences: 7, 8, 2, 10, 5, 8, 5, 4
- $\bar{d}$ = 49/8 = 6.125
- $s_d$ = 2.59 (calculate from differences)

### Step 3: Test Statistic

$$
t = \frac{6.125}{2.59/\sqrt{8}} = \frac{6.125}{0.916} = 6.69
$$

df = 7

### Step 4: Decision
t₀.₀₅,₇ = 1.895
6.69 > 1.895 → Reject H₀

### Step 5: Conclusion
Strong evidence that treatment reduces blood pressure.

Business interpretation: The treatment likely has a real effect; decision-makers can justify adopting it if benefits outweigh costs/side effects.

---

## Practice Problems

### Problem 1

Test scores before and after training:
Before: 70, 65, 80, 75, 72
After: 75, 70, 85, 78, 76

Test for improvement at α = 0.05.

<details>
<summary>💡 Show Solution</summary>

**Step 1: Hypotheses**
- H₀: μd ≤ 0
- H₁: μd > 0

**Step 2: Significance level**
α = 0.05 (right-tailed)

**Differences:** 5, 5, 5, 3, 4
$\bar{d}$ = 22/5 = 4.4
$s_d$ = 0.89

$$
t = \frac{4.4}{0.89/\sqrt{5}} = \frac{4.4}{0.40} = 11.0
$$

df = 4, t₀.₀₅,₄ = 2.132

11.0 > 2.132 → Reject H₀

**Conclusion:** Strong evidence of improvement.

Business interpretation: The training appears effective; scaling the program may be justified.

</details>

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Using an independent t-test on paired data.
> Pairing reduces variability; ignoring it wastes power and can mislead.

> ⚠️ **Mistake 2:** Wrong direction of the difference.
> Define \(d_i\) consistently (e.g., Before − After). The sign must match H₁.

> ⚠️ **Mistake 3:** Forgetting df.
> df = n − 1 where n is the number of pairs (not total observations).

---

## Key Takeaways

- Use for matched or repeated measurements
- Reduces variability by controlling for individual differences
- Focus on differences, not original values
- df = n - 1 (number of pairs minus 1)

---

## Navigation

[← Independent T-Test](independent_t_test.md) | [Module Index](index.md) | [Next: Two-Proportion Test →](two_proportion_test.md)


