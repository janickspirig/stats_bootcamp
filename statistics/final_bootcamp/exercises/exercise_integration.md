---
title: "Integration Exercise: Mixed Exam-Style Problems"
category: "Statistics Bootcamp"
module: 98
order: 8
---

# Integration Exercise: Mixed Exam-Style Problems

> 📚 **Overview:** Longer, multi-part problems that combine multiple topics (Übungsblatt-style).  
> Suggested pacing: **5–8 minutes per sub-part** (a/b/c/…).

---

## Problem 1 (Frequency table → mean/SD → CLT probability)

A service desk records the number of complaints per day:

| Complaints \(x_i\) | Count \(n_i\) |
|---|---:|
| 0 | 10 |
| 1 | 20 |
| 2 | 15 |
| 3 | 5 |

Tasks:
a) Build a table with \(f(x_i)\) and \(F(x_i)\).  
b) Compute the mean number of complaints per day.  
c) Compute the sample variance and sample standard deviation.  
d) Assume the population mean is μ = 1.3 and the population standard deviation is σ = 0.90. For samples of n = 36 days, compute \(P(\\bar{X} > 1.6)\\).

<details>
<summary>💡 Show Solution</summary>

**a) Relative and cumulative frequencies**

Total \(n=50\\).

| \(x_i\) | \(n_i\) | \(f(x_i)=n_i/n\) | \(F(x_i)\) |
|---:|---:|---:|---:|
| 0 | 10 | 0.2000 | 0.2000 |
| 1 | 20 | 0.4000 | 0.6000 |
| 2 | 15 | 0.3000 | 0.9000 |
| 3 | 5 | 0.1000 | 1.0000 |

**b) Mean**

$$
\\bar{x} = \\frac{0\\cdot 10 + 1\\cdot 20 + 2\\cdot 15 + 3\\cdot 5}{50}
= \\frac{65}{50}
= 1.3
$$

**c) Sample variance and SD**

| \(x_i\) | \(n_i\) | \(x_i-\\bar{x}\) | \((x_i-\\bar{x})^2\) | \(n_i(x_i-\\bar{x})^2\) |
|---:|---:|---:|---:|---:|
| 0 | 10 | -1.3 | 1.69 | 16.90 |
| 1 | 20 | -0.3 | 0.09 | 1.80 |
| 2 | 15 | 0.7 | 0.49 | 7.35 |
| 3 | 5 | 1.7 | 2.89 | 14.45 |
| **Σ** | **50** |  |  | **40.50** |

$$
s^2 = \\frac{40.50}{49} = 0.8265,\\qquad s=\\sqrt{0.8265}=0.9091
$$

**d) CLT probability for sample mean**

SE \(=\\sigma/\\sqrt{n}=0.90/\\sqrt{36}=0.90/6=0.15\\).

$$
z = \\frac{1.6-1.3}{0.15} = 2
$$

$$
P(\\bar X>1.6)=P(Z>2)=0.0228
$$

</details>

---

## Problem 2 (Two-proportion test + interpretation)

A website tests a new checkout design:

- Old design: 90 purchases out of 900 visitors  
- New design: 120 purchases out of 950 visitors

Tasks:
a) State \(H_0\\) and \(H_1\\) for a two-tailed test at α = 0.05.  
b) Compute the pooled proportion \(\\hat p\\).  
c) Compute the z statistic and decision (use critical values ±1.96).  
d) Write one business interpretation sentence.

<details>
<summary>💡 Show Solution</summary>

**a) Hypotheses**

- \(H_0: p_1=p_2\\)
- \(H_1: p_1\\ne p_2\\)

**b) Pooled proportion**

$$
\\hat p = \\frac{90+120}{900+950} = \\frac{210}{1850}=0.1135
$$

**c) Test statistic**

$$
\\hat p_1=90/900=0.10,\\qquad \\hat p_2=120/950=0.1263
$$

$$
SE = \\sqrt{\\hat p(1-\\hat p)\\left(\\frac{1}{900}+\\frac{1}{950}\\right)}
$$

Compute:

$$
\\hat p(1-\\hat p)=0.1135\\cdot 0.8865\\approx 0.1006
$$

$$
\\frac{1}{900}+\\frac{1}{950}\\approx 0.002164
$$

$$
SE\\approx \\sqrt{0.1006\\cdot 0.002164}=\\sqrt{0.000217}=0.0147
$$

$$
z = \\frac{0.10-0.1263}{0.0147} = -1.79
$$

Decision: \(|z|=1.79<1.96\\) → **do not reject \(H_0\\)**.

**d) Business interpretation**

At α = 0.05, the evidence is not strong enough to justify rollout; if the lift matters financially, run a larger experiment.

</details>

---

## Problem 3 (Regression table + R²)

Data (x = ad spend, y = sales):

| x | y |
|---:|---:|
| 1 | 3 |
| 2 | 4 |
| 3 | 5 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |

Tasks:
a) Compute \(\\hat\\beta_1\\) and \(\\hat\\beta_0\\).  
b) Compute predictions \(\\hat y\\) and residuals \(e=y-\\hat y\\).  
c) Compute \(SSE=\\sum e^2\\).  
d) Interpret the slope in one business sentence.

<details>
<summary>💡 Show Solution</summary>

From the deviation table method (see Module 12), the regression is:

$$
\\hat y = 2.4 + 0.7429x
$$

Predictions and residuals:

| x | y | \(\\hat y\) | \(e=y-\\hat y\) | \(e^2\) |
|---:|---:|---:|---:|---:|
| 1 | 3 | 3.1429 | -0.1429 | 0.0204 |
| 2 | 4 | 3.8857 | 0.1143 | 0.0131 |
| 3 | 5 | 4.6286 | 0.3714 | 0.1380 |
| 4 | 5 | 5.3714 | -0.3714 | 0.1380 |
| 5 | 6 | 6.1143 | -0.1143 | 0.0131 |
| 6 | 7 | 6.8571 | 0.1429 | 0.0204 |
| **Σ** |  |  |  | **0.3429** |

So \(SSE\\approx 0.3429\\).

Business interpretation (slope): A +1k CHF increase in advertising is associated with about **+0.743** (≈ **+7.43k CHF**) higher weekly sales on average (in this sample).

</details>

---

## Navigation

[Exercises Index](index.md)


