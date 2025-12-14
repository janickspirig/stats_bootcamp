---
title: "Exercise 5: Hypothesis Testing"
category: "Statistics Bootcamp"
module: 98
order: 6
---

# Exercise 5: Hypothesis Testing

> 📚 **Overview:** Practice with z-tests, t-tests, and two-sample tests.

Practice problems for one-sample and two-sample tests.

---

## Topics Covered
- Hypothesis testing framework
- One-sample t-tests
- Two-sample t-tests
- Proportion tests

---

## Problem 1 (One-Sample t-test)

A manufacturer claims products weigh 500g.
Sample: n = 25, x̄ = 495, s = 15
Test if products are underweight at α = 0.05.

<details>
<summary>💡 Show Solution</summary>

**Hypotheses:**
- H₀: μ ≥ 500
- H₁: μ < 500

**Test statistic:**

$$
t = \frac{495 - 500}{15/\sqrt{25}} = \frac{-5}{3} = -1.67
$$

df = 24, t₀.₀₅,₂₄ = -1.711

**Decision:** -1.67 > -1.711 → Fail to reject H₀

**Conclusion:** Insufficient evidence of underweight at α = 0.05.

</details>

---

## Problem 2 (Two-Sample t-test)

Group A: n₁ = 12, x̄₁ = 78, s₁ = 8
Group B: n₂ = 15, x̄₂ = 72, s₂ = 10

Test for difference at α = 0.05.

<details>
<summary>💡 Show Solution</summary>

**Pooled SD:**

$$
s_p = \sqrt{\frac{11(64) + 14(100)}{25}} = \sqrt{\frac{704 + 1400}{25}} = 9.16
$$

**Test statistic:**

$$
t = \frac{78 - 72}{9.16\sqrt{\frac{1}{12}+\frac{1}{15}}} = \frac{6}{3.53} = 1.70
$$

df = 25, t₀.₀₂₅,₂₅ = 2.060

**Decision:** 1.70 < 2.060 → Fail to reject H₀

**Conclusion:** No significant difference at α = 0.05.

</details>

---

## Problem 3 (Proportion Test)

Claim: 60% of customers are satisfied.
Sample: 500 customers, 280 satisfied (56%).
Test at α = 0.05.

<details>
<summary>💡 Show Solution</summary>

**Hypotheses:**
- H₀: p = 0.60
- H₁: p ≠ 0.60

**Test statistic:**

$$
z = \frac{0.56 - 0.60}{\sqrt{\frac{0.60 \times 0.40}{500}}} = \frac{-0.04}{0.0219} = -1.83
$$

z₀.₀₂₅ = ±1.96

**Decision:** |-1.83| < 1.96 → Fail to reject H₀

**Conclusion:** Insufficient evidence to reject the 60% claim.

</details>

---

## Problem 4 (One-tailed vs two-tailed)

A service center claims the mean handling time is 12 minutes.
Sample: n = 36, x̄ = 12.8, s = 2.4

Calculate:
a) Test H₀: μ = 12 vs H₁: μ > 12 at α = 0.05
b) Test H₀: μ = 12 vs H₁: μ ≠ 12 at α = 0.05

<details>
<summary>💡 Show Solution</summary>

Use a one-sample t-test (σ unknown), df = 35.

Test statistic:

$$
t = \\frac{12.8 - 12}{2.4/\\sqrt{36}} = \\frac{0.8}{0.4} = 2.00
$$

a) Right-tailed at α = 0.05: critical value \(t_{0.05,35} \\approx 1.690\).

2.00 > 1.690 → **Reject H₀**.

Conclusion: evidence that handling time is **higher than 12**.

Business interpretation: staffing may be insufficient; longer handling time risks higher queue times.

b) Two-tailed at α = 0.05: use α/2 = 0.025 → \(t_{0.025,35} \\approx 2.030\).

|2.00| < 2.030 → **Do not reject H₀**.

Conclusion: insufficient evidence that the mean differs from 12.

Business interpretation: the “difference” depends on the question asked; tail choice must match the claim.

</details>

---

## Problem 5 (Choose z vs t)

For each scenario, choose the correct test statistic (z or t) and explain in one line:

a) n = 49, σ is known from historical records
b) n = 16, σ is unknown

<details>
<summary>💡 Show Solution</summary>

a) **z** (σ known → use \(z = (\\bar{x}-\\mu_0)/(\\sigma/\\sqrt{n})\)).
b) **t** (σ unknown → use \(t = (\\bar{x}-\\mu_0)/(s/\\sqrt{n})\), df = n−1).

</details>

---

## Problem 6 (Two-proportion z-test)

A new checkout design is tested:
- Old: 90 purchases out of 900 visitors
- New: 120 purchases out of 950 visitors

Test at α = 0.05 if conversion differs (two-tailed).

<details>
<summary>💡 Show Solution</summary>

H₀: p₁ = p₂, H₁: p₁ ≠ p₂

\(\\hat{p}_1 = 90/900 = 0.10\), \(\\hat{p}_2 = 120/950 \\approx 0.1263\)

Pooled \(\\hat{p} = (90+120)/(900+950) = 210/1850 \\approx 0.1135\)

$$
z = \\frac{0.10 - 0.1263}{\\sqrt{0.1135(1-0.1135)(1/900+1/950)}}
$$

Compute SE:

\(0.1135(0.8865) \\approx 0.1006\)

\(1/900+1/950 \\approx 0.002164\)

SE \(\\approx \\sqrt{0.1006\\cdot 0.002164} \\approx \\sqrt{0.000217} \\approx 0.0147\)

z \(\\approx -0.0263/0.0147 = -1.79\)

Critical values: ±1.96 → |−1.79| < 1.96 → **Do not reject H₀**.

Business interpretation: evidence is not strong enough at α=0.05 to justify rollout; run a larger test if the lift matters.

</details>

---

## Problem 7 (F-test → pooled or not?)

Two groups (independent samples):
- Group 1: n₁ = 20, s₁ = 12
- Group 2: n₂ = 25, s₂ = 6

a) Compute the F statistic using the convention F ≥ 1
b) If the variances are clearly different, what t-test variant should you prefer (pooled vs Welch)?

<details>
<summary>💡 Show Solution</summary>

a) Larger variance on top:

$$
F = \\frac{12^2}{6^2} = \\frac{144}{36} = 4.00
$$

df₁ = 19, df₂ = 24.

(Critical value lookup is table-dependent; F = 4 is typically quite large.)

b) If variances appear unequal, prefer **Welch’s t-test** (if covered) rather than pooling.

</details>

---

## Problem 8 (β and power calculation)

Test H₀: μ = 100 vs H₁: μ > 100 with α = 0.05.
Assume σ = 10 (known) and n = 25.
Compute β and power if the true mean is μ = 105.

<details>
<summary>💡 Show Solution</summary>

Critical z: \(z_{0.05} = 1.645\)
Critical sample mean threshold:

$$
\\bar{x}_c = 100 + 1.645\\cdot \\frac{10}{\\sqrt{25}} = 100 + 3.29 = 103.29
$$

β = P(fail to reject | μ=105) = P(\\(\\bar{x} < 103.29\\) | μ=105)

SE = σ/√n = 10/5 = 2

$$
\\beta = \\Phi\\left(\\frac{103.29 - 105}{2}\\right) = \\Phi(-0.855) \\approx 0.196
$$

Power = 1 − β ≈ 0.804.
Business interpretation: With n=25, you have ~80% chance to detect a true increase to 105 at α=0.05.

</details>

---

## Problem 9 (Conclusion wording)

Fill in the blanks:
“At α = ___, we ___ reject H₀. Therefore, there ___ sufficient evidence to conclude that ___.”

<details>
<summary>💡 Show Solution</summary>

Example correct wording:
“At α = 0.05, we **do not** reject H₀. Therefore, there **is not** sufficient evidence to conclude that the alternative hypothesis is true.”

</details>

---

## Problem 10 (Critical threshold for \(\\bar{x}\\), σ known)

Test \(H_0: \\mu=100\\) vs \(H_1: \\mu>100\\) at α = 0.05.

Assume σ = 10 is known and n = 25.

Compute the **critical sample mean threshold** \(\\bar{x}_c\\) (the smallest \(\\bar{x}\\) that leads to rejecting \(H_0\\)).

<details>
<summary>💡 Show Solution</summary>

Right-tailed α = 0.05 → \(z_{0.05}=1.645\\).

SE \(=\\sigma/\\sqrt{n}=10/5=2\\).

$$
\\bar{x}_c = 100 + 1.645\\cdot 2 = 103.29
$$

Reject \(H_0\\) if \(\\bar{x} > 103.29\\).

</details>

---

## Problem 11 (β and power, σ known)

Continue Problem 10. Compute β and power if the true mean is \(\\mu_1=105\\).

<details>
<summary>💡 Show Solution</summary>

Fail to reject if \(\\bar{X}<103.29\\).

SE = 2.

$$
\\beta = P(\\bar X < 103.29\\mid \\mu=105)
= \\Phi\\left(\\frac{103.29-105}{2}\\right)
= \\Phi(-0.855)\\approx 0.196
$$

Power \(=1-\\beta\\approx 0.804\\).

</details>

---

## Problem 12 (Two-tailed p-value, z-test)

A process claims μ = 50 with known σ = 8. A sample of n = 64 has \(\\bar{x}=52\\).

Test \(H_0: \\mu=50\\) vs \(H_1: \\mu\\neq 50\\) and compute the p-value (approx).

<details>
<summary>💡 Show Solution</summary>

SE \(=8/\\sqrt{64}=1\\).

$$
z = \\frac{52-50}{1} = 2
$$

Two-tailed p-value:

$$
p = 2\\cdot P(Z\\ge 2) = 2(1-0.9772)=2(0.0228)=0.0456
$$

</details>

---

## Problem 13 (β and power, left-tailed)

Test \(H_0: \\mu=80\\) vs \(H_1: \\mu<80\\) at α = 0.05.

Assume σ = 12 is known and n = 36. Compute β and power if the true mean is \(\\mu_1=75\\).

<details>
<summary>💡 Show Solution</summary>

Left-tailed α = 0.05 → \(z_{0.05}=1.645\\) (critical value is \(-1.645\\) in z-space).

SE \(=12/\\sqrt{36}=2\\).

Critical mean threshold:

$$
\\bar{x}_c = 80 - 1.645\\cdot 2 = 76.71
$$

Reject \(H_0\\) if \(\\bar{x} < 76.71\\). So fail to reject if \(\\bar X\\ge 76.71\\).

$$
\\beta = P(\\bar X\\ge 76.71\\mid \\mu=75)
= 1-\\Phi\\left(\\frac{76.71-75}{2}\\right)
= 1-\\Phi(0.855)
$$

With \(\\Phi(0.855)\\approx 0.803\\):

$$
\\beta\\approx 1-0.803 = 0.197
$$

Power \(\\approx 0.803\\).

</details>

---

## Problem 14 (α vs α/2 check)

Fill in the blanks:

If a test is **two-tailed** with α = 0.05, then each tail has area ___ and the critical z-values are approximately ___ and ___.

<details>
<summary>💡 Show Solution</summary>

Each tail has area \(\\alpha/2 = 0.025\\). Critical z-values: \(-1.96\\) and \(+1.96\\).

</details>

---

## Problem 15 (Full marks template drill)

Write the **five steps** you should show for full credit in a hypothesis test (one line per step).

<details>
<summary>💡 Show Solution</summary>

1) State \(H_0\\) and \(H_1\\) (and parameter).  
2) State α and tail direction (use α/2 if two-tailed).  
3) Write test statistic formula → substitute values → compute statistic.  
4) Find critical value(s) or p-value and show the comparison.  
5) Decision (reject / do not reject) + conclusion in context (+ one business sentence).

</details>

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Using α when you need α/2.
> Two-tailed tests use α/2 for critical values.

> ⚠️ **Mistake 2:** Confusing SD with SE.
> Tests use \(s/\\sqrt{n}\) or \(\\sigma/\\sqrt{n}\), not s or σ directly.

> ⚠️ **Mistake 3:** Wrong test choice (z vs t).
> σ known → z; σ unknown → t (df = n−1).

> 💡 **Note on precision:** Critical values from statistical tables (e.g., t = 2.03) may differ slightly from software (e.g., t = 2.0301). Both are acceptable — use what your exam provides. The conclusion will be the same.

---

## Key Takeaways

- Always follow the **5-step framework** (hypotheses → α → statistic → decision → conclusion)
- Match the tail (and α vs α/2) to H₁
- Show substitution steps for full credit
- Add one business interpretation sentence after the conclusion

---

## Related Modules

- [Module 09: Hypothesis Testing Basics](../09_hypothesis_testing_basics/index.md)
- [Module 10: One-Sample Tests](../10_one_sample_tests/index.md)
- [Module 11: Two-Sample Tests](../11_two_sample_tests/index.md)

---

## Navigation

[← Exercise 4](exercise_4.md) | [Exercises Index](index.md) | [Exercise 6 →](exercise_6.md)


