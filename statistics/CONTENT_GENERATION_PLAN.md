# Statistics Bootcamp Content Generation Plan

## Overview

This plan outlines the creation of **81 markdown files** for the Statistics Bootcamp.
Each file will be saved to `statistics/final_bootcamp/` and can be copy-pasted into Notion.

**Output Directory Structure:**
```
statistics/final_bootcamp/
├── 00_start_here/
│   ├── index.md
│   ├── welcome.md
│   ├── prerequisites.md
│   └── study_path.md
├── 01_foundations/
│   ├── index.md
│   ├── data_types.md
│   └── scales_of_measurement.md
├── 02_descriptive_statistics/
│   ├── index.md
│   ├── mean_median_mode.md
│   ├── variance_stddev.md
│   ├── quartiles_boxplots.md
│   └── skewness_kurtosis.md
├── ... (modules 03-13)
├── reference/
│   ├── formula_glossary.md
│   ├── distribution_table.md
│   ├── which_test.md
│   ├── statistical_tables.md
│   └── common_mistakes.md
└── exercises/
    ├── exercise_1.md
    ├── exercise_2.md
    ├── exercise_3a.md
    ├── exercise_3b.md
    ├── exercise_4.md
    ├── exercise_5.md
    └── exercise_6.md
```

## CRITICAL: Practice Problems Requirement

**EVERY concept page ("I can..."/"I know..." page) MUST include:**

1. **Worked Example** (1-2): Fully solved step-by-step with calculation tables
2. **Practice Problems** (2-3): Original problems created by the agent with:
   - Business-contextualized scenario
   - Specific numerical data
   - Toggle solution with complete step-by-step answer
   
**These practice problems are SEPARATE from the official HSG exercises.**
The agent must CREATE NEW practice problems based on the concepts taught.

Practice Problem Format:
```markdown
## Practice Problems

### Problem 1
A company surveyed 50 customers and found a mean satisfaction score of 7.2 
with a standard deviation of 1.8. Calculate the 95% confidence interval 
for the true population mean.

<details>
<summary>Show Solution</summary>

**Given:** n = 50, x̄ = 7.2, s = 1.8, confidence = 95%

**Step 1: Identify the formula**
$$CI = \bar{x} \pm t_{\alpha/2} \cdot \frac{s}{\sqrt{n}}$$

**Step 2: Find critical value**
df = 50 - 1 = 49, α/2 = 0.025
t₀.₀₂₅,₄₉ ≈ 2.01

**Step 3: Calculate**
$$CI = 7.2 \pm 2.01 \cdot \frac{1.8}{\sqrt{50}} = 7.2 \pm 0.51$$

**Result:** 95% CI = [6.69, 7.71]

**Interpretation:** We are 95% confident that the true mean satisfaction 
score is between 6.69 and 7.71.

</details>

### Problem 2
[Another practice problem...]
```

---

## Image Placeholder Format

Where images are needed but not yet generated, use this format:

```markdown
<!-- IMAGE_PLACEHOLDER
Type: [chart/diagram/table/screenshot]
Description: [Detailed description of what the image should show]
Data: [If applicable, the data points or values to visualize]
Style: [Any specific styling requirements]
Filename: [suggested_filename.png]
-->
![Description](images/suggested_filename.png)
```

---

## Phase 1: Reference Pages (Create First)

These establish formulas and terminology used throughout.

### Task 1.1: Create reference/formula_glossary.md
- **Source:** All lecture notes, concepts.json
- **Content:** All formulas organized by topic
- **Sections:** Descriptive Stats, Probability, Distributions, Hypothesis Testing, Regression
- **Format:** Formula name, KaTeX notation, variable definitions

### Task 1.2: Create reference/distribution_table.md
- **Source:** Lectures 4-5, concepts.json
- **Content:** Summary table of all distributions
- **Columns:** Name, Type, Parameters, PMF/PDF, Mean, Variance, When to Use
- **Distributions:** Binomial, Poisson, Hypergeometric, Normal, t, Chi-square, F, Exponential

### Task 1.3: Create reference/which_test.md
- **Source:** Lectures 8-10
- **Content:** Decision tree for selecting statistical tests
- **Format:** Step-by-step questions leading to correct test
- **IMAGE_NEEDED:** Decision tree flowchart

### Task 1.4: Create reference/statistical_tables.md
- **Source:** Standard statistical tables
- **Content:** z-table, t-table, chi-square table, F-table
- **IMAGE_NEEDED:** 4 statistical distribution tables

### Task 1.5: Create reference/common_mistakes.md
- **Source:** Exercise solutions, lecture notes
- **Content:** Top 10-15 common mistakes students make
- **Format:** Mistake description, why it's wrong, how to avoid

---

## Phase 2: Start Here Section

### Task 2.1: Create 00_start_here/index.md
- **Content:** Welcome to bootcamp, links to all orientation pages

### Task 2.2: Create 00_start_here/welcome.md
- **Content:** What this bootcamp is, how to use it, estimated time
- **Source:** BOOTCAMP_PURPOSE.txt

### Task 2.3: Create 00_start_here/prerequisites.md
- **Content:** Math prerequisites, self-assessment questions
- **Format:** Checklist of skills, quick quiz

### Task 2.4: Create 00_start_here/study_path.md
- **Content:** Recommended order, time estimates per module
- **IMAGE_NEEDED:** Module progression flowchart

---

## Phase 3: Module 01 - Foundations

### Task 3.1: Create 01_foundations/index.md
- **Source:** Lecture 1, Sections I-II
- **Content:** Module overview, learning objectives, topic list

### Task 3.2: Create 01_foundations/data_types.md
- **Title:** "I know the different types of data and their characteristics"
- **Source:** Lecture 1, Section I (slides 5-8)
- **Concepts:** Primary/secondary data, qualitative/quantitative
- **IMAGE_NEEDED:** Data types classification diagram

### Task 3.3: Create 01_foundations/scales_of_measurement.md
- **Title:** "I can identify and distinguish scales of measurement"
- **Source:** Lecture 1, Section II (slides 9-11)
- **Concepts:** Nominal, ordinal, interval, ratio (NOIR)
- **IMAGE_NEEDED:** NOIR scale comparison chart

---

## Phase 4: Module 02 - Descriptive Statistics

### Task 4.1: Create 02_descriptive_statistics/index.md
- **Source:** Lecture 1, Sections III-V
- **Related Exercise:** Exercise 1

### Task 4.2: Create 02_descriptive_statistics/mean_median_mode.md
- **Title:** "I can calculate and interpret the mean, median, and mode"
- **Source:** Lecture 1, Section IV
- **Formulas:** Mean (sample/population), median calculation
- **Worked Example:** Calculate all three for a dataset

### Task 4.3: Create 02_descriptive_statistics/variance_stddev.md
- **Title:** "I can calculate variance and standard deviation"
- **Source:** Lecture 1, Section V
- **Formulas:** Sample variance, population variance, standard deviation
- **Worked Example:** Full calculation table
- **IMAGE_NEEDED:** Variance visualization (data spread)

### Task 4.4: Create 02_descriptive_statistics/quartiles_boxplots.md
- **Title:** "I can interpret quartiles and box plots"
- **Source:** Lecture 1, Section V
- **Concepts:** Q1, Q2, Q3, IQR, outliers
- **IMAGE_NEEDED:** Labeled box plot diagram

### Task 4.5: Create 02_descriptive_statistics/skewness_kurtosis.md
- **Title:** "I can identify skewness and kurtosis"
- **Source:** Lecture 1, Section V
- **IMAGE_NEEDED:** Skewness comparison (left, symmetric, right)
- **IMAGE_NEEDED:** Kurtosis comparison (lepto, meso, platy)

---

## Phase 5: Module 03 - Correlation and Covariance

### Task 5.1: Create 03_correlation_covariance/index.md
- **Source:** Lecture 2

### Task 5.2: Create 03_correlation_covariance/correlation.md
- **Title:** "I can calculate and interpret correlation coefficients"
- **Source:** Lecture 2, Section II
- **Formulas:** Pearson correlation coefficient
- **IMAGE_NEEDED:** Scatter plots showing r = -1, 0, +1

### Task 5.3: Create 03_correlation_covariance/covariance.md
- **Title:** "I can calculate and interpret covariance"
- **Source:** Lecture 2, Section III
- **Formulas:** Covariance formula
- **Worked Example:** Full calculation table

### Task 5.4: Create 03_correlation_covariance/correlation_causation.md
- **Title:** "I understand the difference between correlation and causation"
- **Source:** Lecture 2, Section IV
- **Examples:** Spurious correlations, confounding variables

---

## Phase 6: Module 04 - Probability Fundamentals

### Task 6.1: Create 04_probability_fundamentals/index.md
- **Source:** Lecture 3
- **Related Exercise:** Exercise 2

### Task 6.2: Create 04_probability_fundamentals/basic_concepts.md
- **Title:** "I know the basic terms and concepts of probability"
- **Source:** Lecture 3, Section I
- **Concepts:** Sample space, events, outcomes

### Task 6.3: Create 04_probability_fundamentals/axioms.md
- **Title:** "I can apply the axioms of probability (Kolmogorov)"
- **Source:** Lecture 3, Section III
- **Content:** Three axioms with examples

### Task 6.4: Create 04_probability_fundamentals/conditional_probability.md
- **Title:** "I can calculate conditional probabilities"
- **Source:** Lecture 3, Section VI
- **Formulas:** P(A|B) = P(A∩B)/P(B)
- **Worked Example:** Business scenario

### Task 6.5: Create 04_probability_fundamentals/addition_multiplication.md
- **Title:** "I can use addition and multiplication rules"
- **Source:** Lecture 3, Sections V, VII
- **Formulas:** Addition rule, multiplication rule
- **IMAGE_NEEDED:** Venn diagrams for union/intersection

### Task 6.6: Create 04_probability_fundamentals/tree_diagrams.md
- **Title:** "I can construct and interpret tree diagrams"
- **Source:** Lecture 3, Section VIII
- **IMAGE_NEEDED:** Example tree diagram with probabilities
- **Worked Example:** Multi-stage probability problem

---

## Phase 7: Module 05 - Discrete Distributions

### Task 7.1: Create 05_discrete_distributions/index.md
- **Source:** Lecture 4
- **Related Exercise:** Exercise 3A

### Task 7.2: Create 05_discrete_distributions/random_variables.md
- **Title:** "I understand discrete random variables"
- **Source:** Lecture 4, Section I
- **Concepts:** Definition, probability function, CDF

### Task 7.3: Create 05_discrete_distributions/expected_value_variance.md
- **Title:** "I can calculate expected value and variance"
- **Source:** Lecture 4, Sections IV-V
- **Formulas:** E(X), Var(X), Chebyshev inequality
- **Worked Example:** Full calculation

### Task 7.4: Create 05_discrete_distributions/binomial.md
- **Title:** "I can apply the binomial distribution"
- **Source:** Lecture 4, Section VI
- **Formulas:** Binomial PMF, mean, variance
- **IMAGE_NEEDED:** Binomial distribution plot (different n, p)
- **Worked Example:** Quality control problem

### Task 7.5: Create 05_discrete_distributions/poisson.md
- **Title:** "I can apply the Poisson distribution"
- **Source:** Lecture 4, Section VIII
- **Formulas:** Poisson PMF
- **IMAGE_NEEDED:** Poisson distribution plot (different λ)
- **Worked Example:** Call center arrivals

### Task 7.6: Create 05_discrete_distributions/hypergeometric.md
- **Title:** "I can apply the hypergeometric distribution"
- **Source:** Lecture 4, Section VII
- **Formulas:** Hypergeometric PMF
- **Worked Example:** Sampling without replacement

---

## Phase 8: Module 06 - Continuous Distributions

### Task 8.1: Create 06_continuous_distributions/index.md
- **Source:** Lecture 5
- **Related Exercise:** Exercise 3B

### Task 8.2: Create 06_continuous_distributions/continuous_rv.md
- **Title:** "I understand continuous random variables and density functions"
- **Source:** Lecture 5, Section I
- **Concepts:** PDF, CDF, properties

### Task 8.3: Create 06_continuous_distributions/normal.md
- **Title:** "I can work with the normal distribution"
- **Source:** Lecture 5, Section III
- **Formulas:** Normal PDF
- **IMAGE_NEEDED:** Normal curve with labeled regions (68-95-99.7 rule)
- **Worked Example:** Calculate probability

### Task 8.4: Create 06_continuous_distributions/z_scores.md
- **Title:** "I can standardize using z-scores"
- **Source:** Lecture 5, Section III
- **Formulas:** z = (x - μ) / σ
- **Worked Example:** Convert to z-score, use table

### Task 8.5: Create 06_continuous_distributions/exponential.md
- **Title:** "I can apply the exponential distribution"
- **Source:** Lecture 5, Section V
- **Formulas:** Exponential PDF, CDF, mean
- **IMAGE_NEEDED:** Exponential distribution plot (different λ)

---

## Phase 9: Module 07 - Sampling Distributions

### Task 9.1: Create 07_sampling_distributions/index.md
- **Source:** Lectures 6-7
- **Related Exercise:** Exercise 4

### Task 9.2: Create 07_sampling_distributions/sample_population.md
- **Title:** "I understand sampling and population concepts"
- **Source:** Lecture 7, Section I
- **Concepts:** Parameter vs statistic, sampling methods

### Task 9.3: Create 07_sampling_distributions/sampling_distribution.md
- **Title:** "I know what a sampling distribution is"
- **Source:** Lecture 7, Section II
- **IMAGE_NEEDED:** Sampling distribution visualization

### Task 9.4: Create 07_sampling_distributions/clt.md
- **Title:** "I can apply the Central Limit Theorem"
- **Source:** Lecture 7, Section III
- **IMAGE_NEEDED:** CLT demonstration (sample means converge to normal)
- **Worked Example:** Apply CLT to sample mean

### Task 9.5: Create 07_sampling_distributions/standard_error.md
- **Title:** "I can calculate standard error"
- **Source:** Lecture 7, Section IV
- **Formulas:** SE = σ/√n, SE for proportions

---

## Phase 10: Module 08 - Estimation and Confidence Intervals

### Task 10.1: Create 08_estimation_confidence_intervals/index.md
- **Source:** Lectures 7-8
- **Related Exercise:** Exercise 4

### Task 10.2: Create 08_estimation_confidence_intervals/point_estimates.md
- **Title:** "I understand point estimators and their properties"
- **Source:** Lecture 8, Sections I-II
- **Concepts:** Bias, efficiency, consistency

### Task 10.3: Create 08_estimation_confidence_intervals/ci_means.md
- **Title:** "I can construct confidence intervals for means"
- **Source:** Lecture 8, Section III
- **Formulas:** CI with known σ (z), CI with unknown σ (t)
- **IMAGE_NEEDED:** CI visualization on distribution
- **Worked Example:** Both scenarios

### Task 10.4: Create 08_estimation_confidence_intervals/ci_proportions.md
- **Title:** "I can construct confidence intervals for proportions"
- **Source:** Lecture 8, Section IV
- **Formulas:** CI for proportion
- **Worked Example:** Survey proportion

### Task 10.5: Create 08_estimation_confidence_intervals/sample_size.md
- **Title:** "I can determine appropriate sample sizes"
- **Source:** Lecture 8, Section V
- **Formulas:** Sample size for mean, sample size for proportion

---

## Phase 11: Module 09 - Hypothesis Testing Basics

### Task 11.1: Create 09_hypothesis_testing_basics/index.md
- **Source:** Lecture 9
- **Related Exercise:** Exercise 5

### Task 11.2: Create 09_hypothesis_testing_basics/hypotheses.md
- **Title:** "I can formulate null and alternative hypotheses"
- **Source:** Lecture 9, Section II
- **Examples:** Business scenarios for H₀ and H₁

### Task 11.3: Create 09_hypothesis_testing_basics/errors.md
- **Title:** "I understand Type I and Type II errors"
- **Source:** Lecture 9, Section VII
- **Concepts:** α, β, power
- **IMAGE_NEEDED:** Type I/II error diagram

### Task 11.4: Create 09_hypothesis_testing_basics/procedure.md
- **Title:** "I know the 5-step hypothesis testing procedure"
- **Source:** Lecture 9, Section IV
- **Content:** 5-step procedure with template

### Task 11.5: Create 09_hypothesis_testing_basics/z_test.md
- **Title:** "I can conduct a z-test for means"
- **Source:** Lecture 9, Section V
- **Formulas:** z-test statistic
- **Worked Example:** Complete 5-step test

---

## Phase 12: Module 10 - One-Sample Tests

### Task 12.1: Create 10_one_sample_tests/index.md
- **Source:** Lecture 9
- **Related Exercise:** Exercise 5

### Task 12.2: Create 10_one_sample_tests/t_test_mean.md
- **Title:** "I can conduct a t-test for population means"
- **Source:** Lecture 9, Section V
- **Formulas:** t-test statistic
- **IMAGE_NEEDED:** t-distribution with rejection regions
- **Worked Example:** Complete test with t-table lookup

### Task 12.3: Create 10_one_sample_tests/test_proportion.md
- **Title:** "I can test hypotheses about proportions"
- **Source:** Lecture 9, Section VI
- **Formulas:** z-test for proportion
- **Worked Example:** Marketing conversion rate

### Task 12.4: Create 10_one_sample_tests/p_values.md
- **Title:** "I can calculate and interpret p-values"
- **Source:** Lecture 9
- **IMAGE_NEEDED:** p-value visualization on distribution
- **Examples:** Interpret different p-values

---

## Phase 13: Module 11 - Two-Sample Tests

### Task 13.1: Create 11_two_sample_tests/index.md
- **Source:** Lecture 10
- **Related Exercise:** Exercise 5

### Task 13.2: Create 11_two_sample_tests/independent_means.md
- **Title:** "I can compare means of independent samples"
- **Source:** Lecture 10, Section II
- **Formulas:** Two-sample t-test (pooled and unpooled)
- **Worked Example:** A/B test scenario

### Task 13.3: Create 11_two_sample_tests/paired_t_test.md
- **Title:** "I can compare means of dependent samples (paired t-test)"
- **Source:** Lecture 10, Section III
- **Formulas:** Paired t-test statistic
- **Worked Example:** Before/after study

### Task 13.4: Create 11_two_sample_tests/compare_proportions.md
- **Title:** "I can compare proportions across samples"
- **Source:** Lecture 10, Section V
- **Formulas:** Two-proportion z-test

### Task 13.5: Create 11_two_sample_tests/f_test_variance.md
- **Title:** "I can test for equality of variances"
- **Source:** Lecture 10, Section VII
- **Formulas:** F-test statistic
- **IMAGE_NEEDED:** F-distribution with critical region

---

## Phase 14: Module 12 - Regression Analysis

### Task 14.1: Create 12_regression_analysis/index.md
- **Source:** Lecture 11
- **Related Exercise:** Exercise 6

### Task 14.2: Create 12_regression_analysis/simple_regression.md
- **Title:** "I can fit a simple linear regression model"
- **Source:** Lecture 11, Section III
- **Formulas:** OLS slope, intercept
- **IMAGE_NEEDED:** Scatter plot with regression line
- **Worked Example:** Full calculation

### Task 14.3: Create 12_regression_analysis/interpret_coefficients.md
- **Title:** "I can interpret regression coefficients"
- **Source:** Lecture 11, Section III
- **Examples:** Business interpretation of slope/intercept

### Task 14.4: Create 12_regression_analysis/r_squared.md
- **Title:** "I can evaluate model fit using R-squared"
- **Source:** Lecture 11, Section IV
- **Formulas:** R², SST, SSR, SSE
- **IMAGE_NEEDED:** Decomposition of variance diagram

### Task 14.5: Create 12_regression_analysis/inference_regression.md
- **Title:** "I can conduct hypothesis tests on regression coefficients"
- **Source:** Lecture 11, Section VI
- **Formulas:** t-test for coefficients, confidence intervals

---

## Phase 15: Module 13 - Advanced Topics

### Task 15.1: Create 13_advanced_topics/index.md
- **Source:** Lecture 12
- **Related Exercise:** Exercise 6

### Task 15.2: Create 13_advanced_topics/chi_square_independence.md
- **Title:** "I can conduct chi-square tests for independence"
- **Source:** Lecture 12
- **Formulas:** Chi-square statistic, expected frequencies
- **Worked Example:** Contingency table analysis

### Task 15.3: Create 13_advanced_topics/chi_square_gof.md
- **Title:** "I can conduct chi-square goodness-of-fit tests"
- **Source:** Lecture 12
- **Worked Example:** Test if data follows distribution

### Task 15.4: Create 13_advanced_topics/anova.md
- **Title:** "I can perform one-way ANOVA"
- **Source:** Lecture 12
- **Formulas:** F-statistic, SSB, SSW
- **IMAGE_NEEDED:** ANOVA decomposition diagram
- **Worked Example:** Compare means of 3+ groups

### Task 15.5: Create 13_advanced_topics/dummy_variables.md
- **Title:** "I understand dummy variables and interactions"
- **Source:** Lecture 12, Section V
- **Examples:** Categorical predictors in regression

---

## Phase 16: Exercise Pages

### Task 16.1: Create exercises/exercise_1.md
- **Title:** "Exercise 1: Descriptive Statistics"
- **Source:** Übungsblatt_1 (47 pages)
- **Content:** Problem summaries with solution toggles
- **Related Module:** 02_descriptive_statistics

### Task 16.2: Create exercises/exercise_2.md
- **Title:** "Exercise 2: Probability"
- **Source:** Übungsblatt_2 (75 pages)
- **Related Module:** 04_probability_fundamentals

### Task 16.3: Create exercises/exercise_3a.md
- **Title:** "Exercise 3A: Discrete Distributions"
- **Source:** Übungsblatt_3A (56 pages)
- **Related Module:** 05_discrete_distributions

### Task 16.4: Create exercises/exercise_3b.md
- **Title:** "Exercise 3B: Continuous Distributions"
- **Source:** Übungsblatt_3B (25 pages)
- **Related Module:** 06_continuous_distributions

### Task 16.5: Create exercises/exercise_4.md
- **Title:** "Exercise 4: Sampling & Estimation"
- **Source:** Übungsblatt_4 (56 pages)
- **Related Modules:** 07, 08

### Task 16.6: Create exercises/exercise_5.md
- **Title:** "Exercise 5: Hypothesis Testing"
- **Source:** Übungsblatt_5 (55 pages)
- **Related Modules:** 09, 10, 11

### Task 16.7: Create exercises/exercise_6.md
- **Title:** "Exercise 6: Regression"
- **Source:** Übungsblatt_6 (21 pages)
- **Related Modules:** 12, 13

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Reference Pages | 5 |
| Start Here Pages | 4 |
| Module Index Pages | 13 |
| Content Pages | 52 |
| Exercise Pages | 7 |
| **TOTAL PAGES** | **81** |

| Images Needed | Approximate Count |
|---------------|-------------------|
| Statistical charts/plots | ~25 |
| Diagrams/flowcharts | ~10 |
| Distribution tables | 4 |
| **TOTAL IMAGES** | **~39** |

---

## Execution Order

1. **Phase 1** (Tasks 1.1-1.5): Reference pages - establishes formulas
2. **Phase 2** (Tasks 2.1-2.4): Start Here section
3. **Phases 3-15** (Tasks 3.1-15.5): Content modules in order
4. **Phase 16** (Tasks 16.1-16.7): Exercise pages

---

## Validation After Each Phase

After completing each phase:
- [ ] All pages created in correct folder structure
- [ ] All formulas use valid KaTeX syntax
- [ ] All IMAGE_PLACEHOLDER blocks have detailed descriptions
- [ ] Navigation links point to existing pages
- [ ] No placeholder text (TODO, TBD, Lorem ipsum)

