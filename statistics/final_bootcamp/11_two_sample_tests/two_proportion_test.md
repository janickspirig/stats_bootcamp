---
title: "I can compare two proportions"
category: "Statistics Bootcamp"
module: 11
order: 3
---

# I can compare two proportions

> 📚 **Overview:** Test whether two population proportions are different.

Testing if two population proportions differ.

**Canonical workflow:** Review the 5-step template first: [Testing Framework](../09_hypothesis_testing_basics/testing_framework.md)

---

## Learning Objectives

After completing this section, you will be able to:
- Conduct a two-proportion z-test
- Calculate pooled proportion
- Interpret results

---

## Checklist

- **When to use:** Two independent groups, binary outcome, and you want to test if p₁ differs from p₂.
- **Conditions:** Each group should have at least ~5 successes and ~5 failures (rule of thumb).
- **What to report:** H₀/H₁, α and tail (often two-tailed → α/2), pooled proportion \(\\hat{p}\), z value (with substitution), critical value(s) or p-value, decision, conclusion in context.
- **Common trap:** For tests, use the **pooled** proportion in the standard error (because H₀ assumes p₁ = p₂).

---

## Key Formulas

**Pooled Proportion:**

$$
\hat{p} = \frac{x_1 + x_2}{n_1 + n_2}
$$

**Test Statistic:**

$$
z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}}
$$

---

## Worked Example

**Problem:**
- Website A: 500 visitors, 45 purchases (9%)
- Website B: 600 visitors, 72 purchases (12%)

At α = 0.05, is there a significant difference?

**Solution:**

### Step 1: Hypotheses
- H₀: p₁ = p₂
- H₁: p₁ ≠ p₂

### Step 2: Pooled Proportion

$$
\hat{p} = \frac{45 + 72}{500 + 600} = \frac{117}{1100} = 0.1064
$$

### Step 3: Test Statistic

$$
z = \frac{0.09 - 0.12}{\sqrt{0.1064 \times 0.8936 \times (\frac{1}{500}+\frac{1}{600})}}
$$

$$
= \frac{-0.03}{\sqrt{0.0951 \times 0.00367}} = \frac{-0.03}{0.0187} = -1.60
$$

### Step 4: Decision
z₀.₀₂₅ = ±1.96
|-1.60| < 1.96 → Fail to reject H₀

### Step 5: Conclusion
No significant difference in conversion rates.

Business interpretation: Don’t roll out Website B based on this sample alone; run a larger A/B test if the lift is important.

---

## Practice Problems

### Problem 1

- Treatment: 80/200 success (40%)
- Control: 60/200 success (30%)

Test for difference at α = 0.05.

<details>
<summary>💡 Show Solution</summary>

**Step 1: Hypotheses**
- H₀: p₁ = p₂
- H₁: p₁ ≠ p₂

**Step 2: Significance level**
α = 0.05 (two-tailed → α/2 = 0.025 per tail)

**Pooled proportion:**

$$
\hat{p} = \frac{80 + 60}{400} = 0.35
$$

**Test statistic:**

$$
z = \frac{0.40 - 0.30}{\sqrt{0.35 \times 0.65 \times (\frac{1}{200}+\frac{1}{200})}}
$$

$$
= \frac{0.10}{\sqrt{0.2275 \times 0.01}} = \frac{0.10}{0.0477} = 2.10
$$

z₀.₀₂₅ = ±1.96
|2.10| > 1.96 → Reject H₀

**Conclusion:** Significant difference in success rates.

Business interpretation: The treatment likely improves outcomes; consider rollout if the uplift is profitable.

</details>

---

## Common Mistakes to Avoid

![Visual showing pooled proportion used in SE under H0](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/two_proportion_pooled_se_visual.png)

> ⚠️ **Mistake 1:** Using unpooled SE in a hypothesis test.
> Tests use the pooled \(\\hat{p}\) under H₀.

> ⚠️ **Mistake 2:** Forgetting to check success/failure counts.
> If counts are too small, the Normal approximation may not be valid.

> ⚠️ **Mistake 3:** Missing α/2 in two-tailed tests.
> Two-tailed at α = 0.05 uses 1.96 (not 1.645).

---

## Key Takeaways

- Use pooled proportion under H₀
- Standard z-test (not t)
- Check conditions: both groups have ≥5 successes and failures

---

## Navigation

[← Paired T-Test](paired_t_test.md) | [Module Index](index.md) | [Next: F-Test →](f_test_variance.md)


