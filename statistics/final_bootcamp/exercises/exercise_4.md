---
title: "Exercise 4: Sampling & Estimation"
category: "Statistics Bootcamp"
module: 98
order: 5
---

# Exercise 4: Sampling & Estimation

> 📚 **Overview:** Practice with confidence intervals and sample size determination.

Practice problems for confidence intervals and sample size.

---

## Topics Covered
- Sampling distributions
- Central Limit Theorem
- Confidence intervals for means
- Confidence intervals for proportions
- Sample size determination

---

## Problem 1 (CI for Mean)

Sample: n = 36, x̄ = 50, s = 12
Construct a 95% confidence interval for the population mean.

<details>
<summary>💡 Show Solution</summary>

Since σ is **unknown** (we only have sample s), we use the **t-distribution**.

df = n − 1 = 35, t₀.₀₂₅,₃₅ ≈ 2.030

$$
SE = \frac{s}{\sqrt{n}} = \frac{12}{\sqrt{36}} = 2
$$

$$
ME = 2.030 \times 2 = 4.06
$$

$$
CI = 50 \pm 4.06 = (45.94, 54.06)
$$

</details>

---

## Problem 2 (CI for Proportion)

Poll: n = 500, 280 favor a proposal (56%)
Construct a 95% CI for the true proportion.

<details>
<summary>💡 Show Solution</summary>

$$
\hat{p} = 0.56
$$

$$
SE = \sqrt{\frac{0.56 \times 0.44}{500}} = \sqrt{0.000493} = 0.0222
$$

$$
ME = 1.96 \times 0.0222 = 0.0435
$$

$$
CI = 0.56 \pm 0.0435 = (0.517, 0.604)
$$

**95% CI: 51.7% to 60.4%**

</details>

---

## Problem 3 (Sample Size)

You want to estimate a mean with ME ≤ 2 at 95% confidence.
Preliminary estimate: σ = 10. What n is needed?

<details>
<summary>💡 Show Solution</summary>

$$
n = \left(\frac{z \times \sigma}{E}\right)^2 = \left(\frac{1.96 \times 10}{2}\right)^2 = (9.8)^2 = 96.04
$$

**n = 97 (round up)**

</details>

---

## Problem 4 (Interpret the CI)

You computed a 95% CI for the mean profit per customer as (45.94, 54.06).
Write one correct interpretation sentence.

<details>
<summary>💡 Show Solution</summary>

Correct interpretation: “We are 95% confident that the true population mean profit per customer lies between 45.94 and 54.06 (in the given units).”

</details>

---

## Problem 5 (Margin of error and sample size trade-off)

For a mean CI with σ fixed, how does the margin of error change if you quadruple the sample size?
Answer in one sentence.

<details>
<summary>💡 Show Solution</summary>

Margin of error is proportional to \(1/\\sqrt{n}\), so quadrupling n halves the margin of error.

</details>

---

## Problem 6 (CI for mean, σ known vs unknown)

A sample has n = 25 and x̄ = 80.

a) If σ = 10 is known, write the 95% CI formula (no need to compute).
b) If σ is unknown but s = 10, what distribution do you use and what df?

<details>
<summary>💡 Show Solution</summary>

a) \(\\bar{x} \\pm z_{0.025}\\cdot (\\sigma/\\sqrt{n}) = 80 \\pm 1.96\\cdot (10/5)\)
b) Use **t** with df = n − 1 = 24, and CI is \(80 \\pm t_{0.025,24}\\cdot (s/\\sqrt{n})\).

</details>

---

## Problem 7 (CI for proportion, conservative n)

A poll wants a 95% CI with margin of error at most 2 percentage points (E = 0.02), but p is unknown.
What sample size is required (conservative)?

<details>
<summary>💡 Show Solution</summary>

Use p = 0.5:

$$
n = 0.25\\left(\\frac{1.96}{0.02}\\right)^2 = 0.25\\cdot 98^2 = 0.25\\cdot 9604 = 2401
$$

Answer: n = 2401.

</details>

---

## Problem 8 (Common SE trap)

Which is larger: σ or σ/√n (for n > 1)? Why does this matter for inference?

<details>
<summary>💡 Show Solution</summary>

σ is larger because dividing by √n reduces the value.
It matters because inference about the mean uses the sampling variability of \(\\bar{x}\), which is σ/√n (the standard error).

</details>

---

## Problem 9 (Sampling distribution probability)

Daily demand has population mean μ = 100 units and population standard deviation σ = 20 units.

For samples of size n = 64, compute:

$$
P(\\bar{X} > 105)
$$

<details>
<summary>💡 Show Solution</summary>

SE \(=\\sigma/\\sqrt{n}=20/\\sqrt{64}=20/8=2.5\\).

$$
z = \\frac{105-100}{2.5} = 2
$$

$$
P(\\bar X>105)=P(Z>2)=1-0.9772=0.0228
$$

</details>

---

## Problem 10 (Sample size for 99% CI, σ known)

You want a 99% confidence interval for the mean with margin of error \(E\\le 3\\).

Assume σ = 12 is known. What minimum n is needed?

<details>
<summary>💡 Show Solution</summary>

For 99%: \(z_{0.005}=2.576\\).

$$
n = \\left(\\frac{z\\sigma}{E}\\right)^2
= \\left(\\frac{2.576\\cdot 12}{3}\\right)^2
= (10.304)^2
= 106.18
$$

Round up: **n = 107**.

</details>

---

## Problem 11 (Confidence level trade-off)

You have the same data and sample size, but you compare a 90% CI vs a 99% CI.

Which one is wider? Why? (One sentence.)

<details>
<summary>💡 Show Solution</summary>

The 99% CI is wider because it uses a larger critical value (e.g., 2.576 vs 1.645), increasing the margin of error for the same SE.

</details>

---

## Problem 12 (Correct CI interpretation?)

Which interpretation is correct?

a) “There is a 95% chance the true mean lies in our computed 95% CI.”  
b) “If we repeated this sampling many times, about 95% of the constructed 95% CIs would contain the true mean.”

<details>
<summary>💡 Show Solution</summary>

Correct: **b)**. The confidence level describes the long-run success rate of the procedure, not the probability of the fixed parameter after you computed one interval.

</details>

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Interpreting a 95% CI as “95% of data lie in the interval.”
> CI is about the **parameter**, not individual observations.
> ⚠️ **Mistake 2:** Forgetting to round **sample size up**.
> ⚠️ **Mistake 3:** Using z when σ is unknown (should use t with df = n−1).

---

## Key Takeaways

- CI = estimate ± (critical value) × (standard error)
- Margin of error shrinks like \(1/\\sqrt{n}\)
- For proportions with unknown p, p=0.5 is conservative
- Always interpret in context

---

## Related Modules

- [Module 07: Sampling Distributions](../07_sampling_distributions/index.md)
- [Module 08: Estimation](../08_estimation_confidence_intervals/index.md)

---

## Navigation

[← Exercise 3B](exercise_3b.md) | [Exercises Index](index.md) | [Exercise 5 →](exercise_5.md)


