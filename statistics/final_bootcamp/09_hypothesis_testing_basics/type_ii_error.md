---
title: "I can calculate Type II error (β)"
category: "Statistics Bootcamp"
module: 9
order: 5
---

# I can calculate Type II error (β)

> 📚 **Overview:** How to compute **β** (Type II error) in HSG-style hypothesis testing questions.

Type II error happens when we **do not reject \(H_0\)** even though \(H_0\) is false.

---

## Learning Objectives

After completing this section, you will be able to:
- Define β (Type II error) correctly
- Compute β in common one-sample mean tests (σ known)
- Translate β into **power** (\(1-\\beta\))

---

## Core idea (what β is)

- **Type I error (α):** Reject \(H_0\) when \(H_0\) is true (you control this)
- **Type II error (β):** Fail to reject \(H_0\) when \(H_0\) is false (depends on effect size, σ, n, α)

In symbols:

$$
\\beta = P(\\text{do not reject }H_0 \\mid H_1 \\text{ is true})
$$

---

## Step-by-step recipe (σ known, one-sample mean)

We assume:
- \(X\\sim \\mathcal{N}(\\mu,\\sigma^2)\) (or n large so \(\\bar X\) approx normal)
- σ is known
- Test about \(\\mu\) with sample size \(n\)

### 1) Pick the test and the critical value

- Right-tailed: \(H_1: \\mu>\\mu_0\) uses critical \(z_{\\alpha}\)
- Left-tailed: \(H_1: \\mu<\\mu_0\) uses critical \(z_{\\alpha}\) (negative threshold in x̄-space)
- Two-tailed: \(H_1: \\mu\\neq\\mu_0\) uses \(z_{\\alpha/2}\)

### 2) Convert the critical value into a critical threshold for \(\\bar x\)

Standard error:

$$
SE = \\frac{\\sigma}{\\sqrt{n}}
$$

Example (right-tailed):

$$
\\bar x_c = \\mu_0 + z_{\\alpha}\\cdot SE
$$

### 3) Compute β under a specific true mean \(\\mu_1\)

For right-tailed tests, “fail to reject” means \(\\bar X < \\bar x_c\):

$$
\\beta(\\mu_1)=P(\\bar X < \\bar x_c\\mid \\mu=\\mu_1)
= \\Phi\\left(\\frac{\\bar x_c-\\mu_1}{SE}\\right)
$$

---

## Worked Examples (HSG style)

### Example 1 (Right-tailed, σ known)

Test at \(\\alpha=0.05\):

- \(H_0: \\mu=100\\)
- \(H_1: \\mu>100\\)
- σ = 10, n = 25

Compute β if the true mean is \(\\mu_1=105\\).

<details>
<summary>💡 Show Solution</summary>

**Step 1: Critical value**

Right-tailed at α=0.05 → \(z_{0.05}=1.645\\)

**Step 2: Critical threshold for \(\\bar x\)**

SE \(=10/\\sqrt{25}=2\\)

$$
\\bar x_c = 100 + 1.645\\cdot 2 = 103.29
$$

**Step 3: β under \(\\mu_1=105\)**

Fail to reject if \(\\bar X<103.29\\).

$$
\\beta = \\Phi\\left(\\frac{103.29-105}{2}\\right)
=\\Phi(-0.855)\\approx 0.196
$$

**Power:** \(1-\\beta \\approx 0.804\\).

</details>

---

### Example 2 (Left-tailed, σ known)

Test at \(\\alpha=0.01\):

- \(H_0: \\mu=500\\)
- \(H_1: \\mu<500\\)
- σ = 15, n = 36

Compute β if the true mean is \(\\mu_1=495\\).

<details>
<summary>💡 Show Solution</summary>

**Step 1: Critical value**

Left-tailed at α=0.01 → \(z_{0.01}=2.326\\) (left tail critical is \(-2.326\\) in z-space)

**Step 2: Critical threshold for \(\\bar x\)**

SE \(=15/\\sqrt{36}=2.5\\)

For left-tailed tests: reject if \(\\bar x\\) is **too small**.

$$
\\bar x_c = 500 - 2.326\\cdot 2.5 = 500 - 5.815 = 494.185
$$

**Step 3: β under \(\\mu_1=495\)**

Fail to reject if \(\\bar X \\ge 494.185\\).

$$
\\beta = P(\\bar X \\ge 494.185\\mid \\mu=495)
= 1-\\Phi\\left(\\frac{494.185-495}{2.5}\\right)
$$

Compute z:

$$
z = \\frac{-0.815}{2.5} = -0.326
$$

So:

$$
\\beta = 1-\\Phi(-0.326) = \\Phi(0.326) \\approx 0.628
$$

**Power:** \(1-\\beta\\approx 0.372\\).

</details>

---

### Example 3 (Two-tailed, σ known)

Test at \(\\alpha=0.05\):

- \(H_0: \\mu=20\\)
- \(H_1: \\mu\\neq 20\\)
- σ = 4, n = 16

Compute β if the true mean is \(\\mu_1=22\\).

<details>
<summary>💡 Show Solution</summary>

**Step 1: Critical values**

Two-tailed α=0.05 → α/2=0.025 → \(z_{0.025}=1.96\\).

**Step 2: Critical thresholds**

SE \(=4/\\sqrt{16}=1\\)

Lower and upper critical means:

$$
\\bar x_L = 20 - 1.96\\cdot 1 = 18.04,\\qquad
\\bar x_U = 20 + 1.96\\cdot 1 = 21.96
$$

**Step 3: β under \(\\mu_1=22\)**

Fail to reject happens when \(\\bar X\\) falls **inside** \([18.04, 21.96]\\).

$$
\\beta = P(18.04\\le \\bar X\\le 21.96\\mid \\mu=22)
= \\Phi\\left(\\frac{21.96-22}{1}\\right)-\\Phi\\left(\\frac{18.04-22}{1}\\right)
$$

Compute z-scores: \(z_U=-0.04\\), \(z_L=-3.96\\).

So:

$$
\\beta \\approx \\Phi(-0.04)-\\Phi(-3.96) \\approx 0.4840-0.0000 \\approx 0.4840
$$

**Power:** \(1-\\beta\\approx 0.516\\).

</details>

---

## Quick Check

1) If \(\\beta=0.20\\), what is the power?  
2) Name two levers that reduce β.

<details>
<summary>Answers</summary>

1) Power \(=1-\\beta=0.80\\).  \n+2) Increase n, increase α (for fixed n), decrease σ, larger effect size \(|\\mu_1-\\mu_0|\\).

</details>

---

## Navigation

[← Testing Framework](testing_framework.md) | [Module Index](index.md) | [Next: Power Analysis →](power_analysis.md)


