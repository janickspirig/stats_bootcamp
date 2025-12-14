---
title: "Common Mistakes to Avoid"
category: "Statistics Bootcamp"
module: 99
order: 5
---

# Common Mistakes to Avoid

> 📚 **Overview:** Top errors students make on exams—and how to prevent them.

A guide to the most frequent errors students make in statistics exams and how to avoid them.

---

## 1. Sample vs. Population Notation

> ⚠️ **Mistake:** Using the wrong symbol for sample vs. population parameters.

### Correct Notation

| Parameter | Population | Sample |
|-----------|------------|--------|
| Mean | $\mu$ | $\bar{x}$ |
| Standard Deviation | $\sigma$ | $s$ |
| Variance | $\sigma^2$ | $s^2$ |
| Size | $N$ | $n$ |
| Proportion | $p$ | $\hat{p}$ |
| Correlation | $\rho$ | $r$ |

### How to Remember
- Greek letters = Population (μ, σ, ρ)
- Latin letters = Sample (x̄, s, r)

---

## 2. Dividing by n vs. n-1

> ⚠️ **Mistake:** Using n instead of (n-1) for sample variance/standard deviation.

### The Rule
- **Population variance:** Divide by N
- **Sample variance:** Divide by (n-1)

### Why n-1?
This is called "Bessel's correction." It corrects for bias when estimating population variance from a sample.

### Formulas

**WRONG (for samples):**
$$s^2 = \frac{\sum(x_i - \bar{x})^2}{n}$$

**CORRECT (for samples):**
$$s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1}$$

---

## 3. Confusing Standard Deviation and Standard Error

> ⚠️ **Mistake:** Using standard deviation when standard error is needed (or vice versa).

### The Difference

| Measure | What It Describes | Formula |
|---------|-------------------|---------|
| **Standard Deviation (s)** | Spread of individual data points | $s = \sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}}$ |
| **Standard Error (SE)** | Spread of sample means | $SE = \frac{s}{\sqrt{n}}$ |

### When to Use Each
- **SD:** Describing variability in your data
- **SE:** Constructing confidence intervals, hypothesis tests

---

## 4. One-Tailed vs. Two-Tailed Tests

> ⚠️ **Mistake:** Using the wrong type of test or wrong critical value.

### How to Decide

| Hypothesis | Test Type | Critical Value |
|------------|-----------|----------------|
| H₁: μ ≠ μ₀ | Two-tailed | z_{α/2} or t_{α/2} |
| H₁: μ > μ₀ | One-tailed (right) | z_α or t_α |
| H₁: μ < μ₀ | One-tailed (left) | -z_α or -t_α |

### Example
For α = 0.05:
- Two-tailed: z = ±1.96
- One-tailed: z = 1.645 (or -1.645)

---

## 5. Misinterpreting P-Values

> ⚠️ **Mistake:** Saying "There is a 5% chance the null hypothesis is true."

### What P-Value Actually Means
The p-value is the probability of observing data as extreme (or more extreme) than what we got, **assuming H₀ is true**.

### Correct Interpretation
- ✅ "If H₀ were true, there's a 5% chance of seeing results this extreme."
- ❌ "There's a 5% probability that H₀ is true."

### Decision Rule
- If p-value < α → Reject H₀
- If p-value ≥ α → Fail to reject H₀

---

## 6. Confusing Confidence Level and Confidence Interval

> ⚠️ **Mistake:** Saying "There's a 95% probability that μ is in this interval."

### Correct Interpretation
- ✅ "We are 95% confident that the true population mean lies within this interval."
- ✅ "If we repeated this sampling process many times, 95% of the resulting intervals would contain the true mean."
- ❌ "There is a 95% probability that μ is between 10 and 15."

### Why It Matters
The true parameter μ is fixed (not random). The interval is what varies from sample to sample.

---

## 7. Correlation vs. Causation

> ⚠️ **Mistake:** Concluding that X causes Y because they are correlated.

### Remember
**Correlation does NOT imply causation!**

### Possible Explanations for Correlation
1. X causes Y
2. Y causes X
3. A third variable Z causes both
4. Pure coincidence

### To Establish Causation You Need
- Controlled experiments
- Random assignment
- Elimination of confounding variables

---

## 8. Wrong Degrees of Freedom

> ⚠️ **Mistake:** Using incorrect degrees of freedom for t-tests.

### Common df Values

| Test | Degrees of Freedom |
|------|-------------------|
| One-sample t-test | df = n - 1 |
| Two-sample t-test (pooled) | df = n₁ + n₂ - 2 |
| Paired t-test | df = n - 1 (n = number of pairs) |
| Chi-square (independence) | df = (r-1)(c-1) |
| Chi-square (goodness-of-fit) | df = k - 1 |
| Regression (t-test for slope) | df = n - 2 |

---

## 9. Forgetting to State Hypotheses Correctly

> ⚠️ **Mistake:** Writing H₀ with ≠ or H₁ with =

### Rules
- **H₀ (Null):** Always contains = (equality)
- **H₁ (Alternative):** Contains ≠, <, or >

### Correct Examples
- ✅ H₀: μ = 100, H₁: μ ≠ 100
- ✅ H₀: p = 0.5, H₁: p > 0.5
- ❌ H₀: μ ≠ 100 (WRONG!)
- ❌ H₁: μ = 100 (WRONG!)

---

## 10. Rounding Errors

> ⚠️ **Mistake:** Rounding too early in calculations.

### Best Practice
1. Keep at least 4 decimal places during intermediate calculations
2. Only round the final answer to 2-3 decimal places
3. Never round the values you look up from tables

### Example

**WRONG:**
- z = 1.234, round to 1.23
- Use 1.23 in next calculation → accumulated error

**CORRECT:**
- Keep z = 1.234 for all calculations
- Round only the final answer

---

## 11. Using Z When You Should Use T

> ⚠️ **Mistake:** Using z-test when σ is unknown.

### When to Use Each

| Condition | Use |
|-----------|-----|
| σ is known | Z-test |
| σ is unknown, n ≥ 30 | t-test (or z as approximation) |
| σ is unknown, n < 30 | t-test (must use!) |

### Rule of Thumb
**When in doubt, use t.** The t-distribution approaches z as n increases anyway.

---

## 12. Forgetting Assumptions

> ⚠️ **Mistake:** Applying tests without checking if assumptions are met.

### Common Assumptions to Check

**For t-tests:**
- [ ] Random sample
- [ ] Independence of observations
- [ ] Normal distribution (or n ≥ 30)
- [ ] For two-sample: equal variances (if using pooled)

**For Chi-square:**
- [ ] Expected frequencies ≥ 5
- [ ] Random sample
- [ ] Independence

**For Regression:**
- [ ] Linear relationship
- [ ] Independence of errors
- [ ] Constant variance (homoscedasticity)
- [ ] Normally distributed errors

---

## 13. Misreading Tables

> ⚠️ **Mistake:** Looking up the wrong row/column in statistical tables.

### Tips for Table Reading
1. **Z-table:** First digit in row, second digit in column
2. **T-table:** df in row, α in column
3. **Chi-square:** df in row, α in column
4. **F-table:** df₁ in column, df₂ in row

### Double-Check
Always verify your lookup makes sense:
- Critical values should be positive
- Larger df → smaller t critical value
- Larger confidence → larger critical value

---

## 14. Calculation Table Errors

> ⚠️ **Mistake:** Making arithmetic errors in calculation tables.

### Checklist for Calculation Tables

| Check | How |
|-------|-----|
| Row sum | Add all individual values |
| Column check | Σ(xᵢ - x̄) should equal 0 (or very close) |
| Variance positive | (xᵢ - x̄)² should always be positive |
| Mean is reasonable | Should be between min and max |

### Example Table

| i | xᵢ | xᵢ - x̄ | (xᵢ - x̄)² |
|---|-----|---------|-----------|
| 1 | 10 | -5 | 25 |
| 2 | 15 | 0 | 0 |
| 3 | 20 | 5 | 25 |
| Σ | 45 | **0** ✓ | 50 |

x̄ = 45/3 = 15 ✓

---

## 15. Type I vs. Type II Error Confusion

> ⚠️ **Mistake:** Mixing up the two types of errors.

### Memory Aid

| Error | What Happened | Analogy |
|-------|---------------|---------|
| **Type I (α)** | Rejected H₀ when H₀ is TRUE | False alarm (convicted innocent person) |
| **Type II (β)** | Failed to reject H₀ when H₀ is FALSE | Missed detection (guilty person goes free) |

### Relationship
- Decreasing α → Increases β
- Increasing sample size → Decreases both errors
- Power = 1 - β

---

## Quick Checklist Before Submitting

- [ ] Used correct notation (sample vs. population)
- [ ] Used n-1 for sample variance
- [ ] Stated both H₀ and H₁ correctly
- [ ] Used correct test (z vs. t, one vs. two-tailed)
- [ ] Checked degrees of freedom
- [ ] Looked up correct critical value
- [ ] Showed all calculation steps
- [ ] Stated conclusion in context
- [ ] Didn't round until final answer

---

## Navigation

[← Statistical Tables](statistical_tables.md) | [Back to Reference Index](index.md)


