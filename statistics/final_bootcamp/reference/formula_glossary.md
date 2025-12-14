---
title: "Formula Glossary"
category: "Statistics Bootcamp"
module: 99
order: 1
---

# Formula Glossary

> 📚 **Quick Reference:** All statistical formulas organized by topic. Use Ctrl+F / Cmd+F to search for specific formulas.

---

## 📑 Table of Contents

1. [Descriptive Statistics](#1-descriptive-statistics)
2. [Probability](#2-probability)
3. [Discrete Distributions](#3-discrete-distributions)
4. [Continuous Distributions](#4-continuous-distributions)
5. [Sampling and Estimation](#5-sampling-and-estimation)
6. [Hypothesis Testing](#6-hypothesis-testing)
7. [Regression Analysis](#7-regression-analysis)
8. [Chi-Square and ANOVA](#8-chi-square-and-anova)
9. [Quick Reference: Critical Values](#quick-reference-common-critical-values)

---

## 1. Descriptive Statistics

### Measures of Central Tendency

**Arithmetic Mean (Sample)**

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

<details>
<summary>Show symbol meanings</summary>

- **$\bar{x}$**: sample mean (average of the sample)
- **$n$**: sample size (number of observations in the sample)
- **$x_i$**: i-th observation in the sample
- **$\sum_{i=1}^{n}$**: sum over all observations from \(i=1\) to \(n\)

</details>

**Arithmetic Mean (Population)**

$$
\mu = \frac{1}{N}\sum_{i=1}^{N} x_i
$$

<details>
<summary>Show symbol meanings</summary>

- **$\mu$**: population mean (average of the population)
- **$N$**: population size (number of units in the population)
- **$x_i$**: i-th value in the population
- **$\sum_{i=1}^{N}$**: sum over all population values from \(i=1\) to \(N\)

</details>

**Weighted Mean**

$$
\bar{x}_w = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\bar{x}_w$**: weighted mean
- **$x_i$**: i-th observation/value
- **$w_i$**: weight for observation \(x_i\) (importance / frequency)
- **$n$**: number of (weighted) observations/categories
- **$\sum_{i=1}^{n}$**: sum over all observations/categories

</details>

**Median**
- If n is odd: median = value at position (n+1)/2
- If n is even: median = average of values at positions n/2 and (n/2)+1

---

### Measures of Dispersion

**Range**

$$
R = x_{max} - x_{min}
$$

<details>
<summary>Show symbol meanings</summary>

- **$R$**: range
- **$x_{max}$**: largest observation/value
- **$x_{min}$**: smallest observation/value

</details>

**Mean Absolute Deviation (MAD)**

$$
MAD = \frac{1}{n}\sum_{i=1}^{n} |x_i - \bar{x}|
$$

-Exam tip: Show a small calculation table with \(x_i\), \(x_i-\\bar{x}\), and \(|x_i-\\bar{x}|\), then sum the absolute deviations.

<details>
<summary>Show symbol meanings</summary>

- **$MAD$**: mean absolute deviation (average absolute distance to the mean)
- **$n$**: sample size
- **$x_i$**: i-th observation in the sample
- **$\bar{x}$**: sample mean
- **$|x_i - \bar{x}|$**: absolute deviation from the mean (always non-negative)
- **$\sum_{i=1}^{n}$**: sum over all observations

</details>

**Variance (Sample)**

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

<details>
<summary>Show symbol meanings</summary>

- **$s^2$**: sample variance
- **$n$**: sample size
- **$n-1$**: degrees of freedom for sample variance
- **$x_i$**: i-th observation in the sample
- **$\bar{x}$**: sample mean
- **$(x_i - \bar{x})^2$**: squared deviation from the mean
- **$\sum_{i=1}^{n}$**: sum over all observations

</details>

**Variance (Sample) — computational shortcut**

$$
s^2 = \frac{1}{n-1}\left(\sum_{i=1}^{n} x_i^2 - \frac{\left(\sum_{i=1}^{n} x_i\right)^2}{n}\right)
$$

-Exam tip: This shortcut is convenient when you already have \(\\sum x_i\) and \(\\sum x_i^2\) from a calculation table.

<details>
<summary>Show symbol meanings</summary>

- **$s^2$**: sample variance
- **$n$**: sample size
- **$\sum_{i=1}^{n} x_i^2$**: sum of squared observations
- **$\left(\sum_{i=1}^{n} x_i\right)^2$**: square of the sum of observations
- **$n-1$**: degrees of freedom

</details>

**Variance (Population)**

$$
\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2
$$

<details>
<summary>Show symbol meanings</summary>

- **$\sigma^2$**: population variance
- **$N$**: population size
- **$x_i$**: i-th value in the population
- **$\mu$**: population mean
- **$(x_i - \mu)^2$**: squared deviation from the population mean
- **$\sum_{i=1}^{N}$**: sum over all population values

</details>

**Standard Deviation (Sample)**

$$
s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}
$$

<details>
<summary>Show symbol meanings</summary>

- **$s$**: sample standard deviation (units of \(x\))
- **$s^2$**: sample variance
- **$n$**: sample size
- **$x_i$**: i-th observation
- **$\bar{x}$**: sample mean
- **$\sqrt{\\cdot}$**: square root (turns variance into standard deviation)
- **$\sum_{i=1}^{n}$**: sum over all observations

</details>

**Standard Deviation (Population)**

$$
\sigma = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\sigma$**: population standard deviation (units of \(x\))
- **$\sigma^2$**: population variance
- **$N$**: population size
- **$x_i$**: i-th value in the population
- **$\mu$**: population mean
- **$\sqrt{\\cdot}$**: square root
- **$\sum_{i=1}^{N}$**: sum over all population values

</details>

**Coefficient of Variation**

$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

<details>
<summary>Show symbol meanings</summary>

- **$CV$**: coefficient of variation (relative variability, in percent)
- **$s$**: sample standard deviation
- **$\bar{x}$**: sample mean
- **$\times 100\\%$**: converts the ratio to a percentage

</details>

**Interquartile Range (IQR)**

$$
IQR = Q_3 - Q_1
$$

<details>
<summary>Show symbol meanings</summary>

- **$IQR$**: interquartile range
- **$Q_1$**: 1st quartile (25th percentile)
- **$Q_3$**: 3rd quartile (75th percentile)

</details>

---

### Measures of Shape

**Skewness (Sample)**

$$
g_1 = \frac{n}{(n-1)(n-2)} \sum_{i=1}^{n} \left(\frac{x_i - \bar{x}}{s}\right)^3
$$

**Kurtosis (Excess)**

$$
g_2 = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum_{i=1}^{n} \left(\frac{x_i - \bar{x}}{s}\right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)}
$$

---

### Covariance and Correlation

**Covariance (Sample)**

$$
s_{xy} = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})
$$

<details>
<summary>Show symbol meanings</summary>

- **$s_{xy}$**: sample covariance between \(X\) and \(Y\)
- **$n$**: sample size (paired observations \((x_i,y_i)\))
- **$x_i$**: i-th observation of variable \(X\)
- **$y_i$**: i-th observation of variable \(Y\)
- **$\bar{x}$**: sample mean of \(X\)
- **$\bar{y}$**: sample mean of \(Y\)
- **$n-1$**: degrees of freedom
- **$\sum_{i=1}^{n}$**: sum over all paired observations

</details>

**Covariance (Population)**

$$
\sigma_{xy} = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu_x)(y_i - \mu_y)
$$

<details>
<summary>Show symbol meanings</summary>

- **$\sigma_{xy}$**: population covariance between \(X\) and \(Y\)
- **$N$**: population size
- **$x_i$**: i-th value of \(X\) in the population
- **$y_i$**: i-th value of \(Y\) in the population
- **$\mu_x$**: population mean of \(X\)
- **$\mu_y$**: population mean of \(Y\)
- **$\sum_{i=1}^{N}$**: sum over all population pairs

</details>

**Pearson Correlation Coefficient**

$$
r = \frac{s_{xy}}{s_x \cdot s_y} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2 \cdot \sum_{i=1}^{n}(y_i - \bar{y})^2}}
$$

Where: $-1 \leq r \leq 1$

<details>
<summary>Show symbol meanings</summary>

- **$r$**: Pearson correlation coefficient (unitless, between \(-1\) and \(1\))
- **$s_{xy}$**: sample covariance between \(X\) and \(Y\)
- **$s_x$**: sample standard deviation of \(X\)
- **$s_y$**: sample standard deviation of \(Y\)
- **$n$**: sample size
- **$x_i, y_i$**: i-th paired observations
- **$\bar{x}, \bar{y}$**: sample means
- **$\sqrt{\\cdot}$**: square root
- **$\sum_{i=1}^{n}$**: sum over observations

</details>

---

## 2. Probability

### Basic Probability Rules

**Complement Rule**

$$
P(A') = 1 - P(A)
$$

<details>
<summary>Show symbol meanings</summary>

- **$P(\\cdot)$**: probability of an event
- **$A$**: event
- **$A'$**: complement of \(A\) (“not \(A\)”)

</details>

**Addition Rule (General)**

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

<details>
<summary>Show symbol meanings</summary>

- **$A, B$**: events
- **$P(\\cdot)$**: probability
- **$A \\cup B$**: union (“\(A\) or \(B\)” or both)
- **$A \\cap B$**: intersection (“\(A\) and \(B\)”)

</details>

**Addition Rule (Mutually Exclusive)**

$$
P(A \cup B) = P(A) + P(B)
$$

<details>
<summary>Show symbol meanings</summary>

- **$A, B$**: events
- **$P(\\cdot)$**: probability
- **$A \\cup B$**: union (“\(A\) or \(B\)”)
- **Mutually exclusive**: \(A \\cap B = \\emptyset\) (cannot happen together)

</details>

**Conditional Probability**

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

<details>
<summary>Show symbol meanings</summary>

- **$P(A\\mid B)$**: probability of \(A\) given \(B\) occurred
- **$A, B$**: events
- **$A \\cap B$**: event “\(A\) and \(B\)” occur together
- **$P(B)$**: probability of \(B\) (must be \(>0\))

</details>

**Multiplication Rule (General)**

$$
P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)
$$

<details>
<summary>Show symbol meanings</summary>

- **$A, B$**: events
- **$A \\cap B$**: intersection (“\(A\) and \(B\)”)
- **$P(A\\mid B)$**: conditional probability of \(A\) given \(B\)
- **$\\cdot$**: multiplication

</details>

**Multiplication Rule (Independent Events)**

$$
P(A \cap B) = P(A) \cdot P(B)
$$

<details>
<summary>Show symbol meanings</summary>

- **$A, B$**: events
- **Independent**: knowing \(A\) happened does not change probability of \(B\)
- **$A \\cap B$**: “\(A\) and \(B\)” together
- **$\\cdot$**: multiplication

</details>

**Bayes' Theorem**

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

<details>
<summary>Show symbol meanings</summary>

- **$P(A\\mid B)$**: “posterior” (updated) probability of \(A\) given \(B\)
- **$P(B\\mid A)$**: likelihood of observing \(B\) when \(A\) is true
- **$P(A)$**: prior probability of \(A\)
- **$P(B)$**: probability of \(B\) (normalizing constant)
- **$A, B$**: events

</details>

**Law of Total Probability**

$$
P(B) = \sum_{i=1}^{n} P(B|A_i) \cdot P(A_i)
$$

<details>
<summary>Show symbol meanings</summary>

- **$P(B)$**: probability of event \(B\)
- **$A_i$**: i-th case/group in a partition of the sample space (mutually exclusive and exhaustive)
- **$P(B\\mid A_i)$**: probability of \(B\) given case \(A_i\)
- **$P(A_i)$**: probability of case \(A_i\)
- **$\sum_{i=1}^{n}$**: sum over all cases \(A_i\)

</details>

---

### Odds (Probability ↔ Odds Conversion)

**Odds (given probability \(p\))**

$$
o = \frac{p}{1-p}
$$

<details>
<summary>Show symbol meanings</summary>

- **$o$**: odds in favor of the event
- **$p$**: probability of the event (must satisfy \(0 < p < 1\))
- **$1-p$**: probability the event does not occur

</details>

**Probability (given odds \(o\))**

$$
p = \frac{o}{1+o}
$$

<details>
<summary>Show symbol meanings</summary>

- **$p$**: probability of the event
- **$o$**: odds
- **$1+o$**: converts odds back to a probability scale

</details>

---

### Counting Rules

**Permutations (Order Matters)**

$$
P(n,r) = \frac{n!}{(n-r)!}
$$

<details>
<summary>Show symbol meanings</summary>

- **$P(n,r)$**: number of permutations (choose \(r\) items from \(n\), order matters)
- **$n$**: total number of items
- **$r$**: number of items chosen
- **$!$**: factorial, e.g. \(n! = n(n-1)\\cdots 2\\cdot 1\)

</details>

**Combinations (Order Doesn't Matter)**

$$
\binom{n}{r} = C(n,r) = \frac{n!}{r!(n-r)!}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\binom{n}{r}$** or **$C(n,r)$**: number of combinations (choose \(r\) from \(n\), order doesn’t matter)
- **$n$**: total number of items
- **$r$**: number of items chosen
- **$!$**: factorial

</details>

---

## 3. Discrete Distributions

### Expected Value and Variance

**Expected Value**

$$
E(X) = \mu = \sum_{i} x_i \cdot P(X = x_i)
$$

<details>
<summary>Show symbol meanings</summary>

- **$E(X)$**: expected value (mean) of random variable \(X\)
- **$\mu$**: mean of the distribution of \(X\)
- **$x_i$**: i-th possible value that \(X\) can take
- **$P(X=x_i)$**: probability that \(X\) equals \(x_i\)
- **$\sum_i$**: sum over all possible values \(x_i\)
- **$\cdot$**: multiplication

</details>

**Variance**

$$
Var(X) = \sigma^2 = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

<details>
<summary>Show symbol meanings</summary>

- **$Var(X)$**: variance of \(X\) (spread)
- **$\sigma^2$**: variance (population/distribution variance)
- **$E[(X-\\mu)^2]$**: expected squared deviation from the mean
- **$E(X^2)$**: expected value of \(X^2\)
- **$[E(X)]^2$**: square of the expected value
- **$\mu$**: mean of \(X\)

</details>

**Standard Deviation**

$$
\sigma = \sqrt{Var(X)}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\sigma$**: standard deviation of the distribution (units of \(X\))
- **$Var(X)$**: variance of \(X\)
- **$\sqrt{\\cdot}$**: square root

</details>

---

### Binomial Distribution

$$
X \sim Bin(n, p)
$$

<details>
<summary>Show symbol meanings</summary>

- **$X$**: random variable (number of successes)
- **$\sim$**: “is distributed as”
- **$Bin(n,p)$**: binomial distribution
- **$n$**: number of independent trials
- **$p$**: probability of success on each trial

</details>

**Probability Mass Function**

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

<details>
<summary>Show symbol meanings</summary>

- **$P(X=k)$**: probability that \(X\) equals \(k\) successes
- **$k$**: number of successes (an integer from \(0\) to \(n\))
- **$\binom{n}{k}$**: number of ways to choose which \(k\) trials are successes
- **$p^k$**: probability contribution of \(k\) successes
- **$(1-p)^{n-k}$**: probability contribution of \(n-k\) failures

</details>

**Mean**: μ = np

**Variance**: σ² = np(1-p)

<details>
<summary>Show symbol meanings</summary>

- **$\mu$**: mean of the binomial distribution (expected number of successes)
- **$\sigma^2$**: variance of the binomial distribution
- **$n$**: number of trials
- **$p$**: probability of success per trial
- **$np$**: expected successes
- **$np(1-p)$**: variance expression

</details>

---

### Poisson Distribution

$$
X \sim Poi(\lambda)
$$

<details>
<summary>Show symbol meanings</summary>

- **$X$**: random variable (count of events in a fixed interval)
- **$Poi(\\lambda)$**: Poisson distribution
- **$\lambda$**: average rate/mean number of events per interval

</details>

**Probability Mass Function**

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

<details>
<summary>Show symbol meanings</summary>

- **$P(X=k)$**: probability of \(k\) events
- **$k$**: event count (0,1,2,...) 
- **$\lambda$**: average rate/mean number of events
- **$e$**: Euler’s number (\(\approx 2.7183\))
- **$k!$**: factorial

</details>

**Mean**: μ = λ

**Variance**: σ² = λ

<details>
<summary>Show symbol meanings</summary>

- **$\mu$**: mean of the Poisson distribution
- **$\sigma^2$**: variance of the Poisson distribution
- **$\lambda$**: rate parameter (equals both mean and variance)

</details>

---

### Hypergeometric Distribution

$$
X \sim Hyp(N, K, n)
$$

<details>
<summary>Show symbol meanings</summary>

- **$X$**: random variable (number of successes in the sample)
- **$Hyp(N,K,n)$**: hypergeometric distribution (sampling *without* replacement)
- **$N$**: population size
- **$K$**: number of “success” items in the population
- **$n$**: sample size (number of draws)

</details>

**Probability Mass Function**

$$
P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$P(X=k)$**: probability of observing \(k\) successes
- **$k$**: number of observed successes in the sample
- **$\binom{K}{k}$**: ways to choose \(k\) successes from the \(K\) success items
- **$\binom{N-K}{n-k}$**: ways to choose the remaining \(n-k\) failures
- **$\binom{N}{n}$**: total ways to choose any sample of size \(n\) from \(N\)
- **$N$**: population size
- **$K$**: number of successes in population
- **$n$**: number of draws (sample size)

</details>

**Mean**: μ = n × (K/N)

**Variance**: σ² = n × (K/N) × ((N-K)/N) × ((N-n)/(N-1))

<details>
<summary>Show symbol meanings</summary>

- **$\mu$**: mean of the hypergeometric distribution
- **$\sigma^2$**: variance of the hypergeometric distribution
- **$n$**: sample size (draws)
- **$K/N$**: population success proportion
- **$(N-n)/(N-1)$**: finite population correction (because no replacement)

</details>

---

## 4. Continuous Distributions

### Normal Distribution

$$
X \sim N(\mu, \sigma^2)
$$

<details>
<summary>Show symbol meanings</summary>

- **$X$**: (continuous) random variable
- **$\sim$**: “is distributed as”
- **$N(\\mu,\\sigma^2)$**: normal distribution with mean \(\mu\) and variance \(\sigma^2\)
- **$\mu$**: mean of the normal distribution (center)
- **$\sigma^2$**: variance of the normal distribution (spread)

</details>

**Probability Density Function**

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

<details>
<summary>Show symbol meanings</summary>

- **$f(x)$**: probability density at value \(x\) (density, not a probability)
- **$x$**: value on the x-axis
- **$\mu$**: mean
- **$\sigma$**: standard deviation (units of \(x\))
- **$\pi$**: pi (\(\approx 3.1416\))
- **$e$**: Euler’s number (\(\approx 2.7183\))

</details>

### Standard Normal Distribution

**Z-Score (Standardization)**

$$
z = \frac{x - \mu}{\sigma}
$$

<details>
<summary>Show symbol meanings</summary>

- **$z$**: z-score (how many standard deviations \(x\) is from \(\mu\))
- **$x$**: observed value
- **$\mu$**: population mean
- **$\sigma$**: population standard deviation

</details>

**For sample mean:**

$$
z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$z$**: z-score / standardized test statistic for a sample mean
- **$\bar{x}$**: sample mean
- **$\mu$**: population mean (hypothesized mean under \(H_0\) in tests)
- **$\sigma$**: population standard deviation (assumed known here)
- **$\sigma/\\sqrt{n}$**: standard error of the mean
- **$n$**: sample size

</details>

---

### Exponential Distribution

$$
X \sim Exp(\lambda)
$$

<details>
<summary>Show symbol meanings</summary>

- **$X$**: continuous random variable (waiting time)
- **$Exp(\\lambda)$**: exponential distribution
- **$\lambda$**: rate parameter (events per unit time)

</details>

**Probability Density Function**

$$
f(x) = \lambda e^{-\lambda x}, \quad x \geq 0
$$

<details>
<summary>Show symbol meanings</summary>

- **$f(x)$**: probability density at \(x\)
- **$x$**: value (waiting time), must satisfy \(x \\ge 0\)
- **$\lambda$**: rate parameter
- **$e^{-\lambda x}$**: exponential decay term

</details>

**Cumulative Distribution Function**

$$
F(x) = 1 - e^{-\lambda x}
$$

<details>
<summary>Show symbol meanings</summary>

- **$F(x)$**: cumulative probability \(P(X \\le x)\)
- **$x$**: value (waiting time), \(x \\ge 0\)
- **$\lambda$**: rate parameter
- **$e$**: Euler’s number

</details>

**Mean**: μ = 1/λ

**Variance**: σ² = 1/λ²

<details>
<summary>Show symbol meanings</summary>

- **$\mu$**: mean of the exponential distribution
- **$\sigma^2$**: variance of the exponential distribution
- **$\lambda$**: rate parameter

</details>

---

## 5. Sampling and Estimation

### Standard Error

**Standard Error of the Mean (σ known)**

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$SE_{\\bar{x}}$**: standard error of the sample mean (spread of \(\bar{x}\) across samples)
- **$\sigma$**: population standard deviation (assumed known)
- **$n$**: sample size
- **$\sqrt{n}$**: square root of \(n\)
- **$\sigma/\\sqrt{n}$**: standard error (units of \(x\))

</details>

**Standard Error of the Mean (σ unknown)**

$$
SE_{\bar{x}} = \frac{s}{\sqrt{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$SE_{\\bar{x}}$**: estimated standard error of \(\bar{x}\)
- **$s$**: sample standard deviation (used as estimate of \(\sigma\))
- **$n$**: sample size

</details>

**Standard Error of Proportion**

$$
SE_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$SE_{\\hat{p}}$**: standard error of a sample proportion
- **$\hat{p}$**: sample proportion estimate (often used in practice)
- **$p$**: true population proportion (used in theory / under \(H_0\))
- **$n$**: sample size

</details>

---

### Confidence Intervals

**CI for Mean (σ known)**

$$
\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\bar{x}$**: sample mean
- **$\pm$**: “plus/minus” (lower and upper bound)
- **$z_{\\alpha/2}$**: critical value from standard normal for two-sided level \(\alpha\)
- **$\alpha$**: significance level (e.g., 0.05 for 95% CI)
- **$\sigma$**: population standard deviation (known)
- **$\sigma/\\sqrt{n}$**: standard error
- **$n$**: sample size

</details>

**CI for Mean (σ unknown)**

$$
\bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\bar{x}$**: sample mean
- **$t_{\\alpha/2, n-1}$**: critical value from t-distribution with \(df=n-1\)
- **$df=n-1$**: degrees of freedom
- **$s$**: sample standard deviation
- **$s/\\sqrt{n}$**: estimated standard error
- **$\alpha$**: significance level

</details>

**CI for Proportion**

$$
\hat{p} \pm z_{\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\hat{p}$**: sample proportion
- **$z_{\\alpha/2}$**: z critical value
- **$n$**: sample size
- **$\hat{p}(1-\\hat{p})$**: estimated variance component for a Bernoulli proportion

</details>

**CI for Difference of Means (Independent Samples)**

$$
(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\bar{x}_1, \\bar{x}_2$**: sample means of groups 1 and 2
- **$s_1, s_2$**: sample standard deviations of groups 1 and 2
- **$n_1, n_2$**: sample sizes of groups 1 and 2
- **$t_{\\alpha/2}$**: t critical value (df depends on method; often Welch)
- **$\sqrt{\\frac{s_1^2}{n_1} + \\frac{s_2^2}{n_2}}$**: standard error of the difference

</details>

**CI for Difference of Proportions (Independent Samples)**

$$
(\hat{p}_1 - \hat{p}_2) \pm z_{\alpha/2} \cdot \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\hat{p}_1, \\hat{p}_2$**: sample proportions in groups 1 and 2
- **$n_1, n_2$**: sample sizes
- **$z_{\\alpha/2}$**: z critical value
- **$\sqrt{\\cdot}$**: standard error of the difference in proportions

</details>

---

### Sample Size Determination

**Sample Size for Mean**

$$
n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2
$$

<details>
<summary>Show symbol meanings</summary>

- **$n$**: required sample size
- **$z_{\\alpha/2}$**: z critical value for confidence level
- **$\sigma$**: population standard deviation (planning value)
- **$E$**: margin of error (maximum tolerated error in \(\bar{x}\))

</details>

**Sample Size for Proportion**

$$
n = \hat{p}(1-\hat{p})\left(\frac{z_{\alpha/2}}{E}\right)^2
$$

Where $E$ = margin of error

<details>
<summary>Show symbol meanings</summary>

- **$n$**: required sample size
- **$\hat{p}$**: planning estimate for the proportion (use 0.5 if unknown for worst case)
- **$z_{\\alpha/2}$**: z critical value
- **$E$**: margin of error

</details>

---

## 6. Hypothesis Testing

### Test Statistics

**Z-Test for Mean (σ known)**

$$
z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$z$**: z test statistic
- **$\bar{x}$**: sample mean
- **$\mu_0$**: hypothesized mean under the null hypothesis \(H_0\)
- **$\sigma$**: population standard deviation (known)
- **$\sigma/\\sqrt{n}$**: standard error of \(\bar{x}\)
- **$n$**: sample size

</details>

**T-Test for Mean (σ unknown)**

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$t$**: t test statistic
- **$\bar{x}$**: sample mean
- **$\mu_0$**: hypothesized mean under \(H_0\)
- **$s$**: sample standard deviation
- **$s/\\sqrt{n}$**: estimated standard error of \(\bar{x}\)
- **$n$**: sample size

</details>

**Z-Test for Proportion**

$$
z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$z$**: z test statistic
- **$\hat{p}$**: sample proportion
- **$p_0$**: hypothesized proportion under \(H_0\)
- **$n$**: sample size
- **$\sqrt{\\frac{p_0(1-p_0)}{n}}$**: standard error under \(H_0\)

</details>

---

### Two-Sample Tests

**Two-Sample T-Test (Independent, Equal Variances)**

$$
t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$t$**: t test statistic
- **$\bar{x}_1, \\bar{x}_2$**: sample means of groups 1 and 2
- **$n_1, n_2$**: sample sizes
- **$s_p$**: pooled standard deviation (assumes equal variances)
- **$\\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}}$**: sample-size factor in the standard error

</details>

**Pooled Standard Deviation**

$$
s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$s_p$**: pooled standard deviation
- **$s_1, s_2$**: sample standard deviations of groups 1 and 2
- **$n_1, n_2$**: sample sizes
- **$n_1+n_2-2$**: degrees of freedom for pooled estimate

</details>

**Paired T-Test**

$$
t = \frac{\bar{d}}{s_d/\sqrt{n}}
$$

Where d̄ = mean of differences, sₐ = standard deviation of differences

<details>
<summary>Show symbol meanings</summary>

- **$t$**: t test statistic
- **$\bar{d}$**: mean of the paired differences \(d_i\)
- **$s_d$**: standard deviation of the differences
- **$n$**: number of pairs
- **$s_d/\\sqrt{n}$**: standard error of \(\bar{d}\)

</details>

**Two-Proportion Z-Test**

$$
z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}
$$

Where p̂ = (x₁ + x₂)/(n₁ + n₂) (pooled proportion)

<details>
<summary>Show symbol meanings</summary>

- **$z$**: z test statistic
- **$\hat{p}_1, \\hat{p}_2$**: sample proportions in groups 1 and 2
- **$n_1, n_2$**: sample sizes
- **$\hat{p}$**: pooled proportion \(\\frac{x_1+x_2}{n_1+n_2}\) (used under \(H_0: p_1=p_2\))
- **$\\sqrt{\\hat{p}(1-\\hat{p})(\\frac{1}{n_1}+\\frac{1}{n_2})}$**: pooled standard error

</details>

---

### Two-Sample Tests (Unequal Variances — Welch)

**Welch Two-Sample T-Test (Independent, Unequal Variances)**

$$
t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)_0}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$t$**: t test statistic (Welch)
- **$\bar{x}_1, \\bar{x}_2$**: sample means
- **$(\\mu_1-\\mu_2)_0$**: hypothesized mean difference under \(H_0\) (often 0)
- **$s_1, s_2$**: sample standard deviations
- **$n_1, n_2$**: sample sizes
- **$\\sqrt{\\frac{s_1^2}{n_1}+\\frac{s_2^2}{n_2}}$**: standard error (unequal variances)

</details>

**Welch–Satterthwaite Degrees of Freedom**

$$
df \approx \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{\left(\frac{s_1^2}{n_1}\right)^2}{n_1-1} + \frac{\left(\frac{s_2^2}{n_2}\right)^2}{n_2-1}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$df$**: approximate degrees of freedom for Welch t-test
- **$\\approx$**: approximately equal (Welch df is not usually an integer)
- **$s_1, s_2$**: sample standard deviations
- **$n_1, n_2$**: sample sizes

</details>

**F-Test for Variances**

$$
F = \frac{s_1^2}{s_2^2}
$$

(where s₁² > s₂²)

<details>
<summary>Show symbol meanings</summary>

- **$F$**: F test statistic
- **$s_1^2, s_2^2$**: sample variances of groups 1 and 2
- Convention: put the larger sample variance in the numerator so \(F \\ge 1\)

</details>

---

## 7. Regression Analysis

### Simple Linear Regression

**Model**

$$
y = \beta_0 + \beta_1 x + \varepsilon
$$

<details>
<summary>Show symbol meanings</summary>

- **$y$**: dependent (response) variable
- **$x$**: independent (explanatory) variable
- **$\beta_0$**: intercept (true parameter)
- **$\beta_1$**: slope (true parameter)
- **$\varepsilon$**: error term (unobserved factors)

</details>

**Slope (OLS Estimator)**

$$
\hat{\beta}_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2} = \frac{s_{xy}}{s_x^2}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\hat{\\beta}_1$**: estimated slope (OLS estimator)
- **$n$**: number of observations
- **$x_i, y_i$**: i-th observed pair
- **$\bar{x}, \\bar{y}$**: sample means
- **$s_{xy}$**: sample covariance between \(X\) and \(Y\)
- **$s_x^2$**: sample variance of \(X\)
- **$\sum_{i=1}^{n}$**: sum over all observations

</details>

**Slope (OLS Estimator) — raw-score form**

$$
\hat{\beta}_1 = \frac{\sum_{i=1}^{n} x_i y_i - n\bar{x}\bar{y}}{\sum_{i=1}^{n} x_i^2 - n\bar{x}^2}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\hat{\\beta}_1$**: estimated slope
- **$\sum x_i y_i$**: sum of products
- **$\sum x_i^2$**: sum of squared \(x\) values
- **$n$**: sample size
- **$\bar{x}, \\bar{y}$**: sample means

</details>

**Slope (OLS Estimator) — correlation form**

$$
\hat{\beta}_1 = r \cdot \frac{s_y}{s_x}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\hat{\\beta}_1$**: estimated slope
- **$r$**: Pearson correlation coefficient between \(X\) and \(Y\)
- **$s_y$**: sample standard deviation of \(Y\)
- **$s_x$**: sample standard deviation of \(X\)
- **$\cdot$**: multiplication

</details>

**Intercept (OLS Estimator)**

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}
$$

<details>
<summary>Show symbol meanings</summary>

- **$\hat{\\beta}_0$**: estimated intercept
- **$\bar{y}$**: sample mean of \(Y\)
- **$\bar{x}$**: sample mean of \(X\)
- **$\hat{\\beta}_1$**: estimated slope

</details>

**Predicted Value**

$$
\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i
$$

<details>
<summary>Show symbol meanings</summary>

- **$\hat{y}_i$**: predicted value for observation \(i\)
- **$x_i$**: observed \(x\) for observation \(i\)
- **$\hat{\\beta}_0, \\hat{\\beta}_1$**: estimated coefficients

</details>

**Residual**

$$
e_i = y_i - \hat{y}_i
$$

<details>
<summary>Show symbol meanings</summary>

- **$e_i$**: residual (prediction error)
- **$y_i$**: observed response
- **$\hat{y}_i$**: predicted response

</details>
---

### Goodness of Fit

**Total Sum of Squares (SST)**

$$
SST = \sum_{i=1}^{n}(y_i - \bar{y})^2
$$

<details>
<summary>Show symbol meanings</summary>

- **$SST$**: total sum of squares (total variability in \(Y\))
- **$y_i$**: observed response
- **$\bar{y}$**: mean of \(Y\)
- **$n$**: sample size
- **$\sum_{i=1}^{n}$**: sum over observations

</details>

**Regression Sum of Squares (SSR)**

$$
SSR = \sum_{i=1}^{n}(\hat{y}_i - \bar{y})^2
$$

<details>
<summary>Show symbol meanings</summary>

- **$SSR$**: regression sum of squares (explained variability)
- **$\hat{y}_i$**: predicted response
- **$\bar{y}$**: mean of \(Y\)
- **$n$**: sample size

</details>

**Error Sum of Squares (SSE)**

$$
SSE = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \sum_{i=1}^{n}e_i^2
$$

<details>
<summary>Show symbol meanings</summary>

- **$SSE$**: sum of squared errors (unexplained variability)
- **$y_i$**: observed response
- **$\hat{y}_i$**: predicted response
- **$e_i$**: residual \(y_i-\\hat{y}_i\)
- **$n$**: sample size

</details>

**Relationship**: SST = SSR + SSE

**Coefficient of Determination (R-squared)**

$$
R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}
$$

<details>
<summary>Show symbol meanings</summary>

- **$R^2$**: proportion of variance in \(Y\) explained by the model
- **$SSR$**: explained sum of squares
- **$SST$**: total sum of squares
- **$SSE$**: error sum of squares

</details>

**Standard Error of Regression**

$$
s_e = \sqrt{\frac{SSE}{n-2}}
$$

<details>
<summary>Show symbol meanings</summary>

- **$s_e$**: standard error of the regression (estimated SD of errors)
- **$SSE$**: sum of squared errors
- **$n-2$**: degrees of freedom (simple regression)
- **$\sqrt{\\cdot}$**: square root

</details>

**Mean Square Error (MSE)**

$$
MSE = \frac{SSE}{n-2}
$$

<details>
<summary>Show symbol meanings</summary>

- **$MSE$**: mean squared error
- **$SSE$**: sum of squared errors
- **$n-2$**: degrees of freedom

</details>

**Mean Square Regression (MSR) — Simple Regression**

$$
MSR = \frac{SSR}{1}
$$

<details>
<summary>Show symbol meanings</summary>

- **$MSR$**: mean square regression
- **$SSR$**: regression sum of squares
- **$1$**: df for regression in simple regression (one slope)

</details>

**F-Ratio (Overall Model Significance) — Simple Regression**

$$
F = \frac{MSR}{MSE}
$$

<details>
<summary>Show symbol meanings</summary>

- **$F$**: F test statistic for overall model significance
- **$MSR$**: mean square regression
- **$MSE$**: mean squared error

</details>
---

### Inference in Regression

**Standard Error of Slope**

$$
SE(\hat{\beta}_1) = \frac{s_e}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2}}
$$

**T-Test for Slope**

$$
t = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)}
$$

**CI for Slope**

$$
\hat{\beta}_1 \pm t_{\alpha/2, n-2} \cdot SE(\hat{\beta}_1)
$$

---

### Variance / Standard Errors of OLS Estimators (Lecture Formulas)

**Unbiased Estimator of Error Variance (Simple Regression)**

$$
\hat{\sigma}^2 = \frac{SSE}{n-2} = \frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}{n-2}
$$

**Variance of Slope Estimator**

$$
Var(\hat{\beta}_1) = \frac{\sigma^2}{\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

**Variance of Intercept Estimator**

$$
Var(\hat{\beta}_0) = \sigma^2\left(\frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^{n}(x_i-\bar{x})^2}\right)
$$

**Covariance of Intercept and Slope Estimators**

$$
Cov(\hat{\beta}_0,\hat{\beta}_1) = -\sigma^2\left(\frac{\bar{x}}{\sum_{i=1}^{n}(x_i-\bar{x})^2}\right)
$$

**In Practice**

- Replace \( \sigma^2 \) with \( \hat{\sigma}^2 \) to get estimated variances, and take square roots to obtain **standard errors**.

---

## 8. Chi-Square and ANOVA

### Chi-Square Test

**Chi-Square Statistic**

$$
\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
$$

Where:
- Oᵢ = observed frequency
- Eᵢ = expected frequency

**Expected Frequency (Independence Test)**

$$
E_{ij} = \frac{(\text{Row Total}_i)(\text{Column Total}_j)}{n}
$$

---

### One-Way ANOVA

**F-Statistic**

$$
F = \frac{MSB}{MSW} = \frac{SSB/(k-1)}{SSW/(n-k)}
$$

**Between-Group Sum of Squares**

$$
SSB = \sum_{j=1}^{k} n_j(\bar{x}_j - \bar{x})^2
$$

**Within-Group Sum of Squares**

$$
SSW = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (x_{ij} - \bar{x}_j)^2
$$

Where:
- $k$ = number of groups
- $n_j$ = sample size of group j
- $\bar{x}_j$ = mean of group j
- $\bar{x}$ = overall mean

---

## Quick Reference: Common Critical Values

| Confidence Level | α | z_{α/2} |
|-----------------|---|---------|
| 90% | 0.10 | 1.645 |
| 95% | 0.05 | 1.960 |
| 99% | 0.01 | 2.576 |

---

## Navigation

[← Back to Reference Index](index.md) | [Distribution Table →](distribution_table.md)


