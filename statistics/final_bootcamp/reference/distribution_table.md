---
title: "Distribution Summary Table"
category: "Statistics Bootcamp"
module: 99
order: 2
---

# Distribution Summary Table

> 📚 **Overview:** When and how to use each probability distribution—quick reference guide.

A comprehensive reference for when and how to use each probability distribution.

---

## Discrete Distributions

| Distribution | Notation | Parameters | When to Use | Mean | Variance |
|--------------|----------|------------|-------------|------|----------|
| **Binomial** | $X \sim Bin(n,p)$ | n = trials, p = success prob | Fixed n trials, 2 outcomes, independent, constant p | $np$ | $np(1-p)$ |
| **Poisson** | $X \sim Poi(\lambda)$ | λ = rate | Count of events in fixed interval | $\lambda$ | $\lambda$ |
| **Hypergeometric** | $X \sim Hyp(N,K,n)$ | N = pop, K = successes, n = draws | Sampling WITHOUT replacement | $n\frac{K}{N}$ | Complex |

---

## Continuous Distributions

| Distribution | Notation | Parameters | When to Use | Mean | Variance |
|--------------|----------|------------|-------------|------|----------|
| **Normal** | $X \sim N(\mu, \sigma^2)$ | μ = mean, σ² = variance | Natural phenomena, CLT applies | $\mu$ | $\sigma^2$ |
| **Standard Normal** | $Z \sim N(0,1)$ | None (standardized) | Reference for z-scores | 0 | 1 |
| **Exponential** | $X \sim Exp(\lambda)$ | λ = rate | Time between Poisson events | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| **t-distribution** | $t \sim t(df)$ | df = degrees of freedom | Small samples, unknown σ | 0 | $\frac{df}{df-2}$ |
| **Chi-square** | $\chi^2 \sim \chi^2(df)$ | df = degrees of freedom | Variance tests, categorical data | $df$ | $2 \cdot df$ |
| **F-distribution** | $F \sim F(df_1, df_2)$ | df₁, df₂ = degrees of freedom | Comparing variances, ANOVA | Complex | Complex |

---

## Detailed Distribution Cards

### Binomial Distribution

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

**Use When:**
- Fixed number of trials (n)
- Only two possible outcomes (success/failure)
- Trials are independent
- Probability of success (p) is constant

**Examples:**
- Number of defective items in a batch of n products
- Number of customers who purchase out of n visitors
- Number of correct answers on a true/false test

**Conditions to Check:**
- ✅ Independence between trials
- ✅ Same probability for each trial
- ✅ Fixed number of trials

---

### Poisson Distribution

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

**Use When:**
- Counting events in a fixed interval (time, area, volume)
- Events occur independently
- Average rate (λ) is known and constant

**Examples:**
- Number of customer arrivals per hour
- Number of defects per unit length
- Number of emails received per day

**Relationship to Binomial:**
- Poisson approximates Binomial when n is large and p is small (np = λ)

---

### Hypergeometric Distribution

$$
P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}
$$

**Use When:**
- Sampling WITHOUT replacement
- Population size N is known
- Number of success items K in population is known
- Drawing n items without replacement

**Examples:**
- Number of red balls drawn from an urn (without replacement)
- Number of defective items in a sample (small population)
- Number of winning lottery tickets

**Difference from Binomial:**
- Use Hypergeometric when sampling without replacement
- Use Binomial when sampling with replacement (or population is very large)

---

### Normal Distribution

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

**Use When:**
- Data is symmetrically distributed around the mean
- Central Limit Theorem applies (sample means)
- Many natural phenomena

**Key Properties:**
- Symmetric around μ
- 68-95-99.7 Rule (Empirical Rule)
- Total area under curve = 1

**Examples:**
- Heights, weights of populations
- Measurement errors
- Sample means (via CLT)

<!-- IMAGE_PLACEHOLDER
Type: chart
Description: Normal distribution curve showing the 68-95-99.7 rule with shaded regions at ±1σ, ±2σ, and ±3σ from the mean
Data: μ=0, σ=1, shade regions progressively
Style: Blue curve, labeled percentages (68%, 95%, 99.7%)
Filename: normal_empirical_rule.png
-->
![Normal distribution empirical rule](https://raw.githubusercontent.com/janickspirig/stats_bootcamp/main/statistics/final_bootcamp/images/normal_empirical_rule.png)

---

### t-Distribution

**Use When:**
- Estimating population mean with unknown σ
- Sample size is small (n < 30 typically)
- Population is approximately normal

**Key Properties:**
- Similar to normal but with heavier tails
- Approaches normal as df increases
- df = n - 1 for one-sample problems

**Critical Values (Two-tailed, α = 0.05):**
| df | t₀.₀₂₅ |
|----|--------|
| 10 | 2.228 |
| 20 | 2.086 |
| 30 | 2.042 |
| ∞ | 1.960 |

---

### Chi-Square Distribution

**Use When:**
- Testing independence in contingency tables
- Goodness-of-fit tests
- Testing population variance

**Key Properties:**
- Always positive (≥ 0)
- Right-skewed
- Becomes more symmetric as df increases

**Formula:**

$$
\chi^2 = \sum \frac{(O - E)^2}{E}
$$

---

### F-Distribution

**Use When:**
- Comparing two variances
- ANOVA (comparing means of 3+ groups)

**Key Properties:**
- Ratio of two chi-square distributions
- Always positive
- Right-skewed
- Two parameters: df₁ (numerator), df₂ (denominator)

**Formula (Variance Test):**

$$
F = \frac{s_1^2}{s_2^2}
$$

---

### Exponential Distribution

$$
f(x) = \lambda e^{-\lambda x}, \quad x \geq 0
$$

**Use When:**
- Modeling time between events in a Poisson process
- "Waiting time" problems
- Memoryless property required

**Examples:**
- Time between customer arrivals
- Lifetime of electronic components
- Time until next phone call

**Relationship to Poisson:**
- If arrivals follow Poisson(λ), time between arrivals follows Exp(λ)

---

## Decision Flowchart: Which Distribution?

**Question 1: Discrete or Continuous?**

If **Discrete** (counting):
- Fixed trials, yes/no outcomes → **Binomial**
- Events in interval, rate known → **Poisson**
- Sampling without replacement → **Hypergeometric**

If **Continuous** (measurement):
- Large sample or known σ → **Normal**
- Small sample, unknown σ → **t-distribution**
- Time between events → **Exponential**
- Variance testing → **Chi-square**
- Comparing variances → **F-distribution**

---

## Navigation

[← Formula Glossary](formula_glossary.md) | [Back to Reference Index](index.md) | [Which Test? →](which_test.md)


