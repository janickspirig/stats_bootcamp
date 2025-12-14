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

**Where:**
- x̄ = sample mean
- n = sample size
- xᵢ = individual observations

**Arithmetic Mean (Population)**

$$
\mu = \frac{1}{N}\sum_{i=1}^{N} x_i
$$

**Where:**
- μ = population mean
- N = population size

**Weighted Mean**

$$
\bar{x}_w = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}
$$

**Median**
- If n is odd: median = value at position (n+1)/2
- If n is even: median = average of values at positions n/2 and (n/2)+1

---

### Measures of Dispersion

**Range**

$$
R = x_{max} - x_{min}
$$

**Mean Absolute Deviation (MAD)**

$$
MAD = \frac{1}{n}\sum_{i=1}^{n} |x_i - \bar{x}|
$$

-Exam tip: Show a small calculation table with \(x_i\), \(x_i-\\bar{x}\), and \(|x_i-\\bar{x}|\), then sum the absolute deviations.

**Variance (Sample)**

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

**Variance (Sample) — computational shortcut**

$$
s^2 = \frac{1}{n-1}\left(\sum_{i=1}^{n} x_i^2 - \frac{\left(\sum_{i=1}^{n} x_i\right)^2}{n}\right)
$$

-Exam tip: This shortcut is convenient when you already have \(\\sum x_i\) and \(\\sum x_i^2\) from a calculation table.

**Variance (Population)**

$$
\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2
$$

**Standard Deviation (Sample)**

$$
s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}
$$

**Standard Deviation (Population)**

$$
\sigma = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2}
$$

**Coefficient of Variation**

$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

**Interquartile Range (IQR)**

$$
IQR = Q_3 - Q_1
$$

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

**Covariance (Population)**

$$
\sigma_{xy} = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu_x)(y_i - \mu_y)
$$

**Pearson Correlation Coefficient**

$$
r = \frac{s_{xy}}{s_x \cdot s_y} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2 \cdot \sum_{i=1}^{n}(y_i - \bar{y})^2}}
$$

Where: $-1 \leq r \leq 1$

---

## 2. Probability

### Basic Probability Rules

**Complement Rule**

$$
P(A') = 1 - P(A)
$$

**Addition Rule (General)**

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

**Addition Rule (Mutually Exclusive)**

$$
P(A \cup B) = P(A) + P(B)
$$

**Conditional Probability**

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

**Multiplication Rule (General)**

$$
P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)
$$

**Multiplication Rule (Independent Events)**

$$
P(A \cap B) = P(A) \cdot P(B)
$$

**Bayes' Theorem**

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

**Law of Total Probability**

$$
P(B) = \sum_{i=1}^{n} P(B|A_i) \cdot P(A_i)
$$

---

### Counting Rules

**Permutations (Order Matters)**

$$
P(n,r) = \frac{n!}{(n-r)!}
$$

**Combinations (Order Doesn't Matter)**

$$
\binom{n}{r} = C(n,r) = \frac{n!}{r!(n-r)!}
$$

---

## 3. Discrete Distributions

### Expected Value and Variance

**Expected Value**

$$
E(X) = \mu = \sum_{i} x_i \cdot P(X = x_i)
$$

**Variance**

$$
Var(X) = \sigma^2 = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

**Standard Deviation**

$$
\sigma = \sqrt{Var(X)}
$$

---

### Binomial Distribution

$$
X \sim Bin(n, p)
$$

**Probability Mass Function**

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

**Mean**: μ = np

**Variance**: σ² = np(1-p)

---

### Poisson Distribution

$$
X \sim Poi(\lambda)
$$

**Probability Mass Function**

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

**Mean**: μ = λ

**Variance**: σ² = λ

---

### Hypergeometric Distribution

$$
X \sim Hyp(N, K, n)
$$

**Probability Mass Function**

$$
P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}
$$

**Where:**
- N = population size
- K = number of success states in population
- n = number of draws
- k = number of observed successes

**Mean**: μ = n × (K/N)

**Variance**: σ² = n × (K/N) × ((N-K)/N) × ((N-n)/(N-1))

---

## 4. Continuous Distributions

### Normal Distribution

$$
X \sim N(\mu, \sigma^2)
$$

**Probability Density Function**

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

### Standard Normal Distribution

**Z-Score (Standardization)**

$$
z = \frac{x - \mu}{\sigma}
$$

**For sample mean:**

$$
z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}
$$

---

### Exponential Distribution

$$
X \sim Exp(\lambda)
$$

**Probability Density Function**

$$
f(x) = \lambda e^{-\lambda x}, \quad x \geq 0
$$

**Cumulative Distribution Function**

$$
F(x) = 1 - e^{-\lambda x}
$$

**Mean**: μ = 1/λ

**Variance**: σ² = 1/λ²

---

## 5. Sampling and Estimation

### Standard Error

**Standard Error of the Mean (σ known)**

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$

**Standard Error of the Mean (σ unknown)**

$$
SE_{\bar{x}} = \frac{s}{\sqrt{n}}
$$

**Standard Error of Proportion**

$$
SE_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}}
$$

---

### Confidence Intervals

**CI for Mean (σ known)**

$$
\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
$$

**CI for Mean (σ unknown)**

$$
\bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}
$$

**CI for Proportion**

$$
\hat{p} \pm z_{\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

**CI for Difference of Means (Independent Samples)**

$$
(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
$$

**CI for Difference of Proportions (Independent Samples)**

$$
(\hat{p}_1 - \hat{p}_2) \pm z_{\alpha/2} \cdot \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}
$$

---

### Sample Size Determination

**Sample Size for Mean**

$$
n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2
$$

**Sample Size for Proportion**

$$
n = \hat{p}(1-\hat{p})\left(\frac{z_{\alpha/2}}{E}\right)^2
$$

Where $E$ = margin of error

---

## 6. Hypothesis Testing

### Test Statistics

**Z-Test for Mean (σ known)**

$$
z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}
$$

**T-Test for Mean (σ unknown)**

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
$$

**Z-Test for Proportion**

$$
z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}
$$

---

### Two-Sample Tests

**Two-Sample T-Test (Independent, Equal Variances)**

$$
t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
$$

**Pooled Standard Deviation**

$$
s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}
$$

**Paired T-Test**

$$
t = \frac{\bar{d}}{s_d/\sqrt{n}}
$$

Where d̄ = mean of differences, sₐ = standard deviation of differences

**Two-Proportion Z-Test**

$$
z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}
$$

Where p̂ = (x₁ + x₂)/(n₁ + n₂) (pooled proportion)

---

### Two-Sample Tests (Unequal Variances — Welch)

**Welch Two-Sample T-Test (Independent, Unequal Variances)**

$$
t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)_0}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
$$

**Welch–Satterthwaite Degrees of Freedom**

$$
df \approx \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{\left(\frac{s_1^2}{n_1}\right)^2}{n_1-1} + \frac{\left(\frac{s_2^2}{n_2}\right)^2}{n_2-1}}
$$

**F-Test for Variances**

$$
F = \frac{s_1^2}{s_2^2}
$$

(where s₁² > s₂²)

---

## 7. Regression Analysis

### Simple Linear Regression

**Model**

$$
y = \beta_0 + \beta_1 x + \varepsilon
$$

**Slope (OLS Estimator)**

$$
\hat{\beta}_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2} = \frac{s_{xy}}{s_x^2}
$$

**Intercept (OLS Estimator)**

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}
$$

**Predicted Value**

$$
\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i
$$

**Residual**

$$
e_i = y_i - \hat{y}_i
$$

---

### Goodness of Fit

**Total Sum of Squares (SST)**

$$
SST = \sum_{i=1}^{n}(y_i - \bar{y})^2
$$

**Regression Sum of Squares (SSR)**

$$
SSR = \sum_{i=1}^{n}(\hat{y}_i - \bar{y})^2
$$

**Error Sum of Squares (SSE)**

$$
SSE = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \sum_{i=1}^{n}e_i^2
$$

**Relationship**: SST = SSR + SSE

**Coefficient of Determination (R-squared)**

$$
R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}
$$

**Standard Error of Regression**

$$
s_e = \sqrt{\frac{SSE}{n-2}}
$$

**Mean Square Error (MSE)**

$$
MSE = \frac{SSE}{n-2}
$$

**Mean Square Regression (MSR) — Simple Regression**

$$
MSR = \frac{SSR}{1}
$$

**F-Ratio (Overall Model Significance) — Simple Regression**

$$
F = \frac{MSR}{MSE}
$$

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


