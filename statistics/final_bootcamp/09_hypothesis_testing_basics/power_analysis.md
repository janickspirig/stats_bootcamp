---
title: "I can do power analysis"
category: "Statistics Bootcamp"
module: 9
order: 6
---

# I can do power analysis

> 📚 **Overview:** Power (\(1-\\beta\)) tells you how likely your test is to detect a real effect.

---

## Learning Objectives

After completing this section, you will be able to:
- Define statistical power
- Compute power for one-sample mean tests (σ known) at a given \(\\mu_1\\)
- Understand how n, α, σ, and effect size affect power

---

## Definitions (exam-ready)

- **Power:** Probability to reject \(H_0\) when \(H_0\) is false.

$$
\\text{Power} = 1-\\beta
$$

Where:

$$
\\beta = P(\\text{do not reject }H_0\\mid \\mu=\\mu_1)
$$

---

## Practical workflow (what you do on paper)

1. Specify the test (left/right/two-tailed) and α
2. Convert critical z (or t) to a critical \(\\bar x\\) threshold
3. Compute β under \(\\mu_1\\) using the sampling distribution of \(\\bar X\\)
4. Power = \(1-\\beta\\)
5. Add one business sentence: is this power “good enough”?

**Rule of thumb:** Many courses target **80% power** (\(\\approx 0.80\\)).

---

## Worked Examples

### Example 1 (Right-tailed, σ known)

Test at α = 0.05:

- \(H_0: \\mu = 100\\)
- \(H_1: \\mu > 100\\)
- σ = 10, n = 25

Compute power if \(\\mu_1 = 105\\).

<details>
<summary>💡 Show Solution</summary>

SE \(=10/\\sqrt{25}=2\\)

Critical value (right-tailed): \(z_{0.05}=1.645\\)

Critical mean threshold:

$$
\\bar x_c = 100 + 1.645\\cdot 2 = 103.29
$$

β at \(\\mu_1=105\\):

$$
\\beta = P(\\bar X < 103.29\\mid \\mu=105)
= \\Phi\\left(\\frac{103.29-105}{2}\\right)
= \\Phi(-0.855)\\approx 0.196
$$

Power \(=1-\\beta\\approx 0.804\\).

Business interpretation: With n=25, you have ~80% chance to detect a true increase to 105 at α=0.05.

</details>

---

### Example 2 (How n changes power)

Same test as Example 1, but compare n=9 vs n=25 vs n=49.

Assume \(\\mu_1=105\\), σ=10, α=0.05 (right-tailed).

<details>
<summary>💡 Show Solution</summary>

Critical z: 1.645.

For each n:

- \(SE=\\sigma/\\sqrt{n}\\)
- \(\\bar x_c = 100 + 1.645\\cdot SE\\)
- \(\\beta = \\Phi((\\bar x_c-105)/SE)\\)

**n = 9**: SE=10/3=3.333

\\(\\bar x_c = 100 + 1.645\\cdot 3.333 = 105.483\\)

\\(\\beta=\\Phi((105.483-105)/3.333)=\\Phi(0.145)=0.558\\)

Power \(\\approx 0.442\\)

**n = 25**: SE=2

\\(\\bar x_c = 103.29\\)

\\(\\beta=\\Phi(-0.855)=0.196\\)

Power \(\\approx 0.804\\)

**n = 49**: SE=10/7=1.429

\\(\\bar x_c = 100 + 1.645\\cdot 1.429 = 102.35\\)

\\(\\beta=\\Phi((102.35-105)/1.429)=\\Phi(-1.855)=0.032\\)

Power \(\\approx 0.968\\)

Conclusion: Increasing n sharply improves power.

</details>

---

## Quick Check

1) If β = 0.35, what is power?  
2) For fixed n and σ, what happens to power if you lower α from 0.05 to 0.01?

<details>
<summary>Answers</summary>

1) Power = 0.65.  
2) Power decreases (harder to reject \(H_0\\) with a stricter α).

</details>

---

## Navigation

[← Type II Error (β)](type_ii_error.md) | [Module Index](index.md) | [Next Module: One-Sample Tests →](../10_one_sample_tests/index.md)

