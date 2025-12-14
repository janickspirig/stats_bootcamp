---
title: "I can compare two independent means"
category: "Statistics Bootcamp"
module: 11
order: 1
---

# I can compare two independent means

> 📚 **Overview:** Two-sample t-test for comparing means from two independent groups.

Testing if two groups have different population means.

**Canonical workflow:** Review the 5-step template first: [Testing Framework](../09_hypothesis_testing_basics/testing_framework.md)

---

## Learning Objectives

After completing this section, you will be able to:
- Conduct an independent samples t-test
- Calculate pooled standard deviation
- State conclusions comparing two groups

---

## Checklist

- **When to use:** Two independent groups, numeric outcome, and you want to test if μ₁ differs from μ₂.
- **Assumptions:** Independent samples; approximately Normal populations (or sufficiently large samples). For pooled test, assume equal variances.
- **What to report:** H₀/H₁, α and tails (often two-tailed), df, pooled SD (if used), t value, critical value(s) or p-value, decision, conclusion in context.
- **Common trap:** If variances are not equal, use **Welch’s t-test** (course-dependent) instead of pooling.

---

## Key Formulas

**Pooled Standard Deviation:**

$$
s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}
$$

**Test Statistic:**

$$
t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}
$$

**Degrees of freedom:** df = n₁ + n₂ - 2

---

## Worked Example

**Problem:**
Two training methods are compared:
- Method A: n₁ = 15, x̄₁ = 82, s₁ = 8
- Method B: n₂ = 12, x̄₂ = 75, s₂ = 10

At α = 0.05, is there a significant difference?

**Solution:**

### Step 1: Hypotheses
- H₀: μ₁ = μ₂
- H₁: μ₁ ≠ μ₂

### Step 2: Pooled Standard Deviation

$$
s_p = \sqrt{\frac{(15-1)(8)^2 + (12-1)(10)^2}{15 + 12 - 2}}
$$

$$
= \sqrt{\frac{14(64) + 11(100)}{25}} = \sqrt{\frac{896 + 1100}{25}} = \sqrt{79.84} = 8.94
$$

### Step 3: Test Statistic

$$
t = \frac{82 - 75}{8.94\sqrt{\frac{1}{15}+\frac{1}{12}}} = \frac{7}{8.94 \times 0.387} = \frac{7}{3.46} = 2.02
$$

df = 25

### Step 4: Decision
t₀.₀₂₅,₂₅ = 2.060
|2.02| < 2.060 → Fail to reject H₀ (marginally)

### Step 5: Conclusion
At α = 0.05, there is insufficient evidence of a difference between methods (p ≈ 0.054).

Business interpretation: The evidence for Method A being better is weak at α = 0.05; management might run a larger trial before switching methods.

---

## Practice Problems

### Problem 1

Compare two groups:
- Group 1: n₁ = 20, x̄₁ = 45, s₁ = 5
- Group 2: n₂ = 25, x̄₂ = 42, s₂ = 6

Test at α = 0.05.

<details>
<summary>💡 Show Solution</summary>

**Step 1: Hypotheses**
- H₀: μ₁ = μ₂
- H₁: μ₁ ≠ μ₂

**Step 2: Significance level**
α = 0.05 (two-tailed → α/2 = 0.025 per tail)

**Pooled SD:**

$$
s_p = \sqrt{\frac{19(25) + 24(36)}{43}} = \sqrt{\frac{475 + 864}{43}} = \sqrt{31.14} = 5.58
$$

**Test statistic:**

$$
t = \frac{45 - 42}{5.58\sqrt{\frac{1}{20}+\frac{1}{25}}} = \frac{3}{5.58 \times 0.30} = \frac{3}{1.67} = 1.80
$$

df = 43, t₀.₀₂₅,₄₃ ≈ 2.02

|1.80| < 2.02 → Do not reject H₀

**Conclusion:** No significant difference at α = 0.05.

Business interpretation: The observed mean difference could be due to sampling variation; avoid changing policy based on this sample alone.

</details>

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Using a pooled test when variances are clearly unequal.
> If variances differ, use Welch’s t-test (if covered) or justify pooling.

> ⚠️ **Mistake 2:** Forgetting the samples must be independent.
> If measurements are matched/before-after, use a paired t-test instead.

> ⚠️ **Mistake 3:** Wrong degrees of freedom.
> For pooled two-sample t-test: df = n₁ + n₂ − 2.

---

## Key Takeaways

- Use for comparing independent groups
- Pool variances when assuming equal σ
- df = n₁ + n₂ - 2
- Use Welch's t-test if variances unequal

![Decision flowchart for pooled vs Welch t-test](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/pooled_vs_welch_decision.png)

---

## Navigation

[← Module Index](index.md) | [Next: Paired T-Test →](paired_t_test.md)


