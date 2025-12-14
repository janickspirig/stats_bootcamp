---
title: "I can conduct chi-square tests"
category: "Statistics Bootcamp"
module: 13
order: 1
---

# I can conduct chi-square tests

> 📚 **Overview:** Test goodness-of-fit and independence for categorical data.

Testing relationships between categorical variables.

---

## Learning Objectives

After completing this section, you will be able to:
- Conduct chi-square test of independence
- Calculate expected frequencies
- Interpret results

---

## Intuition (what this test is doing)

The χ² test compares what you **actually observed** in a contingency table to what you would **expect to observe** if there were **no relationship** (i.e., if the variables were independent).

You can think of χ² as a single “mismatch score” across all cells:
- If observed counts are close to expected counts, χ² is small (looks like independence).
- If some cells are far away from what independence would predict, χ² becomes large (evidence of association).

---

## When to use / when not to use

- **Use when**: both variables are **categorical** (e.g., gender × product choice) and you want to test if they are related.
- **Do not use when**: your variables are numeric (use t-tests/regression instead).
- **Common exam check**: expected counts should be “not too small” (rule of thumb: **all expected \(E\) ≥ 5**).

---

## Assumptions (say these explicitly)

- **Independent observations** (each person/item counted once)
- **Categorical data in counts** (not percentages)
- **Expected counts sufficiently large** (typically all \(E \ge 5\); otherwise results can be unreliable)

---

## Key Formula

$$
\chi^2 = \sum \frac{(O - E)^2}{E}
$$

Where:
- O = observed frequency
- E = expected frequency

**Expected frequency:**

$$
E_{ij} = \frac{(\text{Row Total}_i)(\text{Column Total}_j)}{n}
$$

**Degrees of freedom:** df = (rows - 1)(columns - 1)

![Chi-square distribution with right-tail rejection region](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/chi_square_distribution_rejection_region.png)

![Pipeline: Observed table → Expected table → (O-E)²/E](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/chi_square_expected_counts_pipeline.png)

---

## Interpretation sentence templates (exam-ready)

Use one of these after your decision:

- **Reject \(H_0\)**: “At α = [..], there is sufficient evidence that **[variable A]** and **[variable B]** are **associated** (not independent).”
- **Do not reject \(H_0\)**: “At α = [..], there is not sufficient evidence of an association between **[A]** and **[B]**.”
- **One-liner reminder**: “Association does not prove causality; it only says the distribution differs across categories.”

---

## Common traps (high-frequency)

> ⚠️ **Trap 1: Mixing up O and E.**
> O is the given table; E is computed from row/column totals.

> ⚠️ **Trap 2: Using percentages instead of counts.**
> The test is defined on counts (frequencies).

> ⚠️ **Trap 3: Forgetting the expected-count rule.**
> If some \(E\) are too small, the χ² approximation can be poor.

> ⚠️ **Trap 4: Incorrect df.**
> df = (r−1)(c−1), not \(rc\) or \(n-1\).

---

## Worked Example

**Problem:**
Test if gender and product preference are independent:

|  | Product A | Product B | Total |
|--|-----------|-----------|-------|
| Male | 30 | 20 | 50 |
| Female | 20 | 30 | 50 |
| **Total** | 50 | 50 | 100 |

**Solution:**

### Step 1: Hypotheses
- H₀: Gender and preference are independent
- H₁: Gender and preference are related

### Step 2: Expected Frequencies

$$
E = \frac{\text{Row Total} \times \text{Column Total}}{n}
$$

All expected = (50 × 50)/100 = 25

### Step 3: Calculate χ²

$$
\chi^2 = \frac{(30-25)^2}{25} + \frac{(20-25)^2}{25} + \frac{(20-25)^2}{25} + \frac{(30-25)^2}{25}
$$

$$
= 1 + 1 + 1 + 1 = 4.0
$$

### Step 4: Decision
df = (2-1)(2-1) = 1
χ²₀.₀₅,₁ = 3.841
4.0 > 3.841 → Reject H₀

### Step 5: Conclusion
Gender and product preference are significantly related.

---

## Practice Problems

### Problem 1

|  | Yes | No | Total |
|--|-----|-----|-------|
| Treatment | 40 | 10 | 50 |
| Control | 30 | 20 | 50 |
| **Total** | 70 | 30 | 100 |

Test for independence at α = 0.05.

<details>
<summary>💡 Show Solution</summary>

**Expected frequencies:**
- E(Treatment, Yes) = (50×70)/100 = 35
- E(Treatment, No) = (50×30)/100 = 15
- E(Control, Yes) = 35
- E(Control, No) = 15

$$
\chi^2 = \frac{(40-35)^2}{35} + \frac{(10-15)^2}{15} + \frac{(30-35)^2}{35} + \frac{(20-15)^2}{15}
$$

$$
= 0.71 + 1.67 + 0.71 + 1.67 = 4.76
$$

df = 1, χ²₀.₀₅,₁ = 3.841
4.76 > 3.841 → Reject H₀

Significant association between treatment and outcome.

</details>

---

## Key Takeaways

- χ² tests categorical relationships
- E = (row total × column total) / n
- df = (r-1)(c-1)
- Check that all E ≥ 5

---

## Navigation

[← Module Index](index.md) | [Next: ANOVA →](anova.md)


