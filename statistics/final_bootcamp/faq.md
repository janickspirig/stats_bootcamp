---
title: "FAQ (Common Questions)"
category: "Statistics Bootcamp"
module: 0
order: 5
---

# FAQ (Common Questions)

Short, exam-oriented answers to the most common questions. Expand what you need, skip the rest.

---

<details>
<summary>When do I use a z-test vs a t-test?</summary>

- Use a **z-test** when the population standard deviation **σ is known** (or the course explicitly tells you to treat it as known).
- Use a **t-test** when **σ is unknown** and you use the sample standard deviation **s** (this is the most common case).

Shortcut: σ known → z; σ unknown → t (df = n − 1).

</details>

<details>
<summary>What does “fail to reject H₀” mean?</summary>

It means: the sample does **not** provide strong enough evidence (at your chosen α) to reject H₀.

Important: it does **not** mean “H₀ is proven true”. It means “not enough evidence against H₀”.

</details>

<details>
<summary>How do I choose one-tailed vs two-tailed?</summary>

- Use **two-tailed** (H₁: “≠”) when you care about deviations in **both** directions.
- Use **one-tailed** (H₁: “>” or “<”) when the question is explicitly directional (e.g., “is it higher?”).

Exam trap: Two-tailed tests use **α/2** for critical values in each tail.

</details>

<details>
<summary>What is the difference between standard deviation (SD) and standard error (SE)?</summary>

- **SD** describes the spread of individual observations in your data.
- **SE** describes the spread (uncertainty) of a **sample statistic** like \(\\bar{x}\) across repeated samples.

Key formula: \(SE(\\bar{x}) = \\sigma/\\sqrt{n}\) (or \(s/\\sqrt{n}\) if σ unknown).

</details>

<details>
<summary>When do I divide by n vs (n−1) for variance?</summary>

- Divide by **n** for **population variance** (you have the entire population).
- Divide by **n−1** for **sample variance** (you estimate population variance from a sample).

Shortcut: sample → n−1, population → n.

</details>

<details>
<summary>How do I read the z-table quickly?</summary>

Most z-tables give **P(Z ≤ z)** (left-tail area).

- For \(P(Z > z)\): use \(1 - P(Z \\le z)\)
- For negative z (if table shows only positives): use symmetry \(P(Z \\le -a) = 1 - P(Z \\le a)\)

</details>

<details>
<summary>What is the difference between confidence interval and hypothesis test?</summary>

- A **confidence interval (CI)** estimates a parameter range (e.g., plausible μ values).
- A **hypothesis test** makes a decision about a specific claim (reject / do not reject H₀).

Connection: for two-sided tests at level α, H₀: μ = μ₀ is rejected if μ₀ lies **outside** the \(100(1-\\alpha)\\%\\) CI.

</details>

<details>
<summary>What is a p-value (in one sentence)?</summary>

The p-value is the probability (assuming H₀ is true) of observing a test statistic at least as extreme as the one you got.

Decision rule: p-value < α → reject H₀.

</details>

<details>
<summary>What are Type I and Type II errors (in plain language)?</summary>

- **Type I error (α):** reject H₀ even though H₀ is true (false positive).
- **Type II error (β):** do not reject H₀ even though H₀ is false (false negative).

Power = \(1-\\beta\): chance to detect a real effect.

</details>

<details>
<summary>How do I decide which distribution to use (Binomial vs Poisson vs Hypergeometric)?</summary>

- **Binomial:** fixed number of trials n, independent, constant success probability p.
- **Poisson:** counts of events per interval; parameter λ; often a good approximation when n is large and p is small (\(\\lambda=np\)).
- **Hypergeometric:** sampling **without replacement** from a finite population (N, K, n).

</details>

<details>
<summary>How do I know if data is paired or independent?</summary>

- **Paired data**: the two measurements “belong together” (same unit measured twice).
  - Examples: before/after for the same customers; same employee under two conditions; matched pairs.
  - Typical approach: compute differences \(d_i\) and run a **paired t-test** on the mean difference.

- **Independent data**: observations in group 1 are from different units than group 2.
  - Examples: two different customer groups; A/B test with separate users; two independent samples.
  - Typical approach: **two-sample t-test** (pooled or Welch, depending on variance assumption).

Quick check: If you can draw lines connecting each observation in group 1 to exactly one in group 2, it’s probably paired.

</details>

<details>
<summary>When should I use continuity correction?</summary>

Continuity correction is used when you approximate a **discrete** distribution (often Binomial) with a **continuous** Normal distribution.

If \(X\\sim Bin(n,p)\\) and you use \(Y\\sim N(np, np(1-p))\\), then:

- \(P(X \\le k) \\approx P(Y \\le k+0.5)\\)
- \(P(X \\ge k) \\approx P(Y \\ge k-0.5)\\)
- \(P(a \\le X \\le b) \\approx P(a-0.5 \\le Y \\le b+0.5)\\)

</details>

<details>
<summary>What is the difference between correlation and causation?</summary>

Correlation measures association (variables move together). Causation means changing x **causes** a change in y.

You can have correlation without causation due to confounding variables, reverse causality, or coincidence.

</details>

<details>
<summary>What does R² tell me (and what does it NOT tell me)?</summary>

R² is the fraction of variation in y explained by the regression model.

It does **not** prove causality, and it does not guarantee good predictions outside the observed data range.

</details>

---

## Where to go next

- Test selection: `reference/which_test.md`
- Hypothesis testing template: `09_hypothesis_testing_basics/testing_framework.md`
- SD vs SE cheat sheet: `07_sampling_distributions/standard_error.md`
- Z-table workflow: `06_continuous_distributions/normal_probabilities.md`


