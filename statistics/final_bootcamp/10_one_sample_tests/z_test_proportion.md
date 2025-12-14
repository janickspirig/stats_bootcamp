---
title: "I can perform a z-test for proportions"
category: "Statistics Bootcamp"
module: 10
order: 3
---

# I can perform a z-test for proportions

> 📚 **Overview:** Test hypotheses about a population proportion using sample data.

Testing claims about a population proportion.

**Canonical workflow:** Review the 5-step template first: [Testing Framework](../09_hypothesis_testing_basics/testing_framework.md)

---

## Learning Objectives

After completing this section, you will be able to:
- Conduct a one-sample z-test for proportions
- Check conditions for validity
- Interpret results

---

## Checklist

- **When to use:** One-sample proportion test with large n (normal approximation).
- **Conditions (must check):** \(n p_0 \\ge 5\) and \(n(1-p_0) \\ge 5\).
- **What to report:** H₀/H₁, α and tail, \(\\hat{p}\), z value (with substitution), critical value (or p-value), decision, conclusion in context.
- **Common trap:** Standard error uses **p₀** (from H₀), not \(\\hat{p}\).

---

## Key Formula

$$
z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}
$$

**Conditions:**
- np₀ ≥ 5
- n(1-p₀) ≥ 5

---

## Worked Example

**Problem:**
A company claims 80% customer satisfaction. A survey of 200 customers finds 150 satisfied (75%). At α = 0.05, is satisfaction lower than claimed?

**Solution:**

### Step 1: Hypotheses
- H₀: p ≥ 0.80
- H₁: p < 0.80 (left-tailed)

### Step 2: Check Conditions
- np₀ = 200 × 0.80 = 160 ≥ 5 ✓
- n(1-p₀) = 200 × 0.20 = 40 ≥ 5 ✓

### Step 3: Calculate
p̂ = 150/200 = 0.75

$$
z = \frac{0.75 - 0.80}{\sqrt{\frac{0.80 \times 0.20}{200}}} = \frac{-0.05}{\sqrt{0.0008}} = \frac{-0.05}{0.0283} = -1.77
$$

### Step 4: Decision
Critical value: z₀.₀₅ = -1.645
-1.77 < -1.645 → Reject H₀

### Step 5: Conclusion
At α = 0.05, there is sufficient evidence that customer satisfaction is below 80%.

Business interpretation: The company should treat this as a warning signal and investigate drivers of dissatisfaction (product/service issues).

---

## Practice Problems

### Problem 1

A politician claims 55% support. A poll of 400 voters finds 200 support (50%). At α = 0.05, test if support differs from 55%.

<details>
<summary>💡 Show Solution</summary>

**Step 1: Hypotheses**
- H₀: p = 0.55
- H₁: p ≠ 0.55 (two-tailed)

**Step 2: Conditions and significance level**
Conditions: 400 × 0.55 = 220 ≥ 5 and 400 × 0.45 = 180 ≥ 5 ✓
α = 0.05 (two-tailed → α/2 = 0.025 per tail)

**Step 3: Test statistic**

$$
z = \frac{0.50 - 0.55}{\sqrt{\frac{0.55 \times 0.45}{400}}} = \frac{-0.05}{0.0249} = -2.01
$$

**Step 4: Critical value and decision**
Critical value: ±1.96

Decision: |-2.01| > 1.96 → Reject H₀

**Step 5: Conclusion**
At α = 0.05, there is sufficient evidence that support differs from 55%.

Business interpretation: The campaign should update messaging/targeting based on the new estimated support level.

</details>

---

## Common Mistakes to Avoid

![Visual reminder that proportion tests use p0 (not p-hat) in SE](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/proportion_test_uses_p0_in_se.png)

> ⚠️ **Mistake 1:** Using \(\\hat{p}\) in the standard error.
> For hypothesis tests, the standard error uses **p₀** from H₀.

> ⚠️ **Mistake 2:** Skipping the conditions check.
> Always verify \(n p_0 \\ge 5\) and \(n(1-p_0) \\ge 5\) before using the z-test approximation.

> ⚠️ **Mistake 3:** Two-tailed critical values use α/2.
> If α = 0.05 and two-tailed, use 1.96 (not 1.645).

---

## Key Takeaways

- Use z-test for proportions with large samples
- Standard error uses p₀ (hypothesized value), not p̂
- Check np₀ ≥ 5 and n(1-p₀) ≥ 5

---

## Navigation

[← T-Test for Mean](t_test_mean.md) | [Module Index](index.md) | [Next Module: Two-Sample Tests →](../11_two_sample_tests/index.md)


