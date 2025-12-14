---
title: "I can compare variances (F-test)"
category: "Statistics Bootcamp"
module: 11
order: 4
---

# I can compare variances (F-test)

> 📚 **Overview:** Test whether two populations have equal variances—prerequisite for pooled t-tests.

Testing if two populations have equal variances.

**Canonical workflow:** Review the 5-step template first: [Testing Framework](../09_hypothesis_testing_basics/testing_framework.md)

---

## Learning Objectives

After completing this section, you will be able to:
- Conduct an F-test for equality of variances
- Understand when this test is useful
- Interpret results

---

## Checklist

- **When to use:** You need to check (or are asked to test) whether two population variances are equal, often before deciding on pooled vs Welch t-test.
- **Assumptions:** Both populations are approximately Normal (F-test is sensitive to non-normality).
- **What to report:** H₀/H₁, α (usually two-tailed), F value with substitution, df₁/df₂, critical value(s) and decision.
- **Two-tailed exam trick:** With the convention F ≥ 1 (larger variance on top), you typically only look up the **upper** critical value at α/2.

---

## Key Formula

$$
F = \frac{s_1^2}{s_2^2}
$$

**Convention:** Put larger variance in numerator (so F ≥ 1)

**Degrees of freedom:**
- df₁ = n₁ - 1 (numerator)
- df₂ = n₂ - 1 (denominator)

---

## Worked Example

**Problem:**
Compare variability of two production lines:
- Line A: n₁ = 16, s₁ = 12
- Line B: n₂ = 21, s₂ = 8

At α = 0.05, are variances equal?

**Solution:**

### Step 1: Hypotheses
- H₀: σ₁² = σ₂²
- H₁: σ₁² ≠ σ₂²

### Step 2: Significance Level
α = 0.05 (two-tailed → α/2 = 0.025 in the upper tail when using F ≥ 1 convention)

### Step 3: Test Statistic

$$
F = \frac{12^2}{8^2} = \frac{144}{64} = 2.25
$$

df₁ = 15, df₂ = 20

### Step 4: Critical Value and Decision
Upper critical value: F₀.₀₂₅,₁₅,₂₀ ≈ 2.57 (from table)

2.25 < 2.57 → Fail to reject H₀

### Step 5: Conclusion
No significant difference in variances at α = 0.05.

Business interpretation: Variability appears similar across lines, so a pooled-variance t-test assumption may be reasonable (if Normality is plausible).

---

## Practice Problems

### Problem 1

- Sample 1: n = 10, s = 15
- Sample 2: n = 12, s = 9

Test for equal variances at α = 0.10.

<details>
<summary>💡 Show Solution</summary>

**Step 1: Hypotheses**
- H₀: σ₁² = σ₂²
- H₁: σ₁² ≠ σ₂²

**Step 2: Significance level**
α = 0.10 (two-tailed → α/2 = 0.05 in the upper tail when using F ≥ 1)

**Step 3: Test statistic**
$$
F = \frac{15^2}{9^2} = \frac{225}{81} = 2.78
$$

df₁ = 9, df₂ = 11

**Step 4: Critical value and decision**
Upper critical value: F₀.₀₅,₉,₁₁ ≈ 2.90

2.78 < 2.90 → Do not reject H₀

**Step 5: Conclusion**
At α = 0.10, there is insufficient evidence that the variances differ.

Business interpretation: You can proceed assuming equal variances if the next step is a pooled t-test (but consider Normality).

</details>

---

## Why Test Variances?

1. Check assumption for pooled t-test
2. Quality control (consistency)
3. Compare measurement precision

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Forgetting this is usually a two-tailed test.
> Variances “different” means either σ₁² > σ₂² or σ₁² < σ₂².

> ⚠️ **Mistake 2:** Putting the smaller variance in the numerator.
> Use the convention **F ≥ 1** to simplify table lookup.

> ⚠️ **Mistake 3:** Wrong df order in the table.
> df₁ belongs to the numerator; df₂ belongs to the denominator.

> ⚠️ **Mistake 4:** Ignoring non-normality.
> The F-test is sensitive; if data are clearly non-normal, interpret with caution (course-dependent).

---

## Key Takeaways

- F = larger variance / smaller variance
- F ≥ 1 by convention
- Sensitive to non-normality
- Often used to check t-test assumptions

---

## Navigation

[← Two-Proportion Test](two_proportion_test.md) | [Module Index](index.md) | [Next Module: Regression →](../12_regression_analysis/index.md)


