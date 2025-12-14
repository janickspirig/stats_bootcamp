# Image review (final bootcamp)

Perspective: **HSG BBA student** (beginner in stats, time-efficient, wants exam-relevant clarity, step-by-step cues, and practical interpretation).

## Quick overall notes (applies to many images)

- **Strength**: Most visuals are clean, high-contrast, and focus on one key idea (good for revision).
- **Most important improvement**: Add **one mini numeric example** (1 line) to “concept-only” graphics (e.g., Venn/normal curve) so I can immediately connect picture → calculation.
- **Consistency**: Some figures use **“A and B”** while others use **\(A \cap B\)** / **\(A \cup B\)**; aligning notation would reduce cognitive load.
- **Accessibility**: A few rely heavily on color (red/green). Consider adding **patterns/labels** or colorblind-safe palette.

---

## `addition_rule_venn.png` — Addition Rule of Probability

- **What works**: Very clear overlap; formula is visible and central.
- **What’s unclear**: Uses “A and B” instead of \(A \cap B\); “A or B” vs \(A \cup B\) could be made explicit.
- **Improvements**:
  - Add label: **Union = “A or B”** and **Intersection = “A and B”** (or switch to set notation).
  - Add 1 line example: \(P(A)=0.6, P(B)=0.5, P(A\cap B)=0.2 \Rightarrow P(A\cup B)=0.9\).

## `bayes_tree_example.png` — Bayes’ Theorem: Probability Tree

- **What works**: Excellent step-by-step numeric multiplication on the right; final Bayes fraction is shown.
- **What’s unclear**: The **events are labeled A/B** but the end states are **D / D’**; a short legend would help (e.g., “A=…”, “D=defect”).
- **Improvements**:
  - Replace the “P” node with “Population split” or “Prior” to avoid confusion.
  - Add the missing intermediate: \(P(D)=0.018+0.020=0.038\).
  - If this is for business students: use a business example (defect, churn, fraud flag).

## `binomial_shapes.png` — Binomial Distribution Shapes

- **What works**: Strong intuition: \(p=0.2/0.5/0.8\) shows skew direction; mean line is helpful.
- **What’s unclear**: No reminder that **support is \(k=0,\dots,n\)** and what “success” means.
- **Improvements**:
  - Add subtitle: “\(X=\#\) successes in \(n\) trials”.
  - Add one takeaway: “Skew right when \(p<0.5\), skew left when \(p>0.5\)”.

## `boxplot_comparison.png` — Comparing Distribution Shapes via Box Plots

- **What works**: Linking median position to skewness is very exam-useful.
- **What’s unclear**: Small icons near “Symmetric/Right-skewed” look like missing glyphs.
- **Improvements**:
  - Replace icons with plain text or a simple symbol.
  - Add a quick rule box: “Longer upper whisker → right-skew; longer lower whisker → left-skew”.

## `boxplot_labeled.png` — Anatomy of a Box Plot

- **What works**: Best-in-set for boxplots: clear Q1/Q2/Q3, whiskers, outliers, IQR.
- **What’s unclear**: The “1.5×IQR rule” is referenced but not written as inequalities.
- **Improvements**:
  - Add: **Lower fence = \(Q1-1.5\cdot IQR\)**, **Upper fence = \(Q3+1.5\cdot IQR\)**.
  - Consider adding one micro dataset (5–7 points) and show computed quartiles.

## `causation_explanations.png` — Possible Explanations When X and Y Are Correlated

- **What works**: Clear taxonomy (X→Y, Y→X, confounder, spurious). The warning is prominent.
- **What’s unclear**: Examples are not business-first; also “Exercise → Health” is ambiguous directionally.
- **Improvements**:
  - Swap to business examples:
    - X→Y: “Ad spend → sales”
    - Y→X: “Sales → ad spend (budget increases after success)”
    - Z: “Seasonality”
    - Spurious: “Two trending time series”
  - Add one line: “Correlation is descriptive; causality needs design (RCT, natural experiment, controls).”

## `clt_demonstration.png` — Central Limit Theorem in Action

- **What works**: Great visual progression from skewed population to more normal sample means.
- **What’s unclear**: The labels “n=5 samples” etc. could be misread (it’s **sample size \(n\)**, not “number of samples”).
- **Improvements**:
  - Rename to: “Sample size \(n=5\)” and “Histogram of \(\bar X\) over many repetitions”.
  - Add explicit: “Distribution shown = distribution of sample means \(\bar X\)”.

## `conditional_probability_venn.png` — Conditional Probability \(P(B|A)\)

- **What works**: Very clear “Given A” shading; formula is shown.
- **What’s unclear**: Formula uses “\(P(B|A)=P(B|A)/P(A)\)” which looks like a typo; should be \(P(B|A)=P(A\cap B)/P(A)\).
- **Improvements**:
  - Fix formula text on the image (if possible) to:
    - \(P(B|A)=\dfrac{P(A\cap B)}{P(A)}\)
  - Add a numeric example with a Venn area ratio.

## `correlation_examples.png` — Correlation Coefficient Examples

- **What works**: Covers the full spectrum from \(-1\) to \(+1\); trend lines help.
- **What’s unclear**: It doesn’t explicitly separate **strength** from **sign** (students mix this up).
- **Improvements**:
  - Add a small note: “Sign = direction; \(|r|\) = strength”.
  - Add one “outlier sensitivity” mini-panel or callout (“1 outlier can change r a lot”).

## `covariance_patterns.png` — Covariance Patterns

- **What works**: Simple and intuitive; good separation into positive/negative/zero.
- **What’s unclear**: Covariance magnitude isn’t comparable across units; students should know why correlation is preferred.
- **Improvements**:
  - Add note: “Covariance depends on units; correlation standardizes to \([-1,1]\)”.
  - Add formula snippet: \(\text{Cov}(X,Y)=\frac{1}{n-1}\sum (x_i-\bar x)(y_i-\bar y)\).

## `data_types_tree.png` — Data Types Classification

- **What works**: Clean hierarchy; examples help.
- **What’s unclear**: HSG exams often distinguish **metric vs. categorical** and specifically **“interval vs ratio”**; this tree doesn’t include that layer.
- **Improvements**:
  - Consider adding an alternative view or cross-reference to NOIR (Nominal/Ordinal/Interval/Ratio).
  - Add one “common trap” note: “IDs are nominal even though numeric”.

## `discrete_distribution_flowchart.png` — Choosing the Right Discrete Distribution

- **What works**: The decision logic is exactly what I want before exercises.
- **What’s unclear**: Text/boxes overlap (hypergeometric/binomial area), making it hard to read quickly.
- **Improvements**:
  - Fix layout so **no overlaps**; increase whitespace and font size.
  - Add a 1-line example under each distribution (business-style):
    - Binomial: “10 calls, success=conversion”
    - Hypergeometric: “sample without replacement from a batch”
    - Poisson: “arrivals per hour”

## `empirical_rule.png` — The Empirical Rule (68–95–99.7)

- **What works**: Very clean and memorable; shaded regions make it easy.
- **What’s unclear**: No explicit link to z-scores / “standard deviations from mean”.
- **Improvements**:
  - Add: “Standardize: \(Z=(X-\mu)/\sigma\)”.
  - Add quick exam usage: “Approx \(P(|Z|\le 2)\approx 0.95\)”.

## `kurtosis_types.png` — Types of Kurtosis

- **What works**: Visual comparison is clear.
- **What’s unclear**: Kurtosis is often confusing; “heavy tails” vs “peakedness” needs explicit statement (and many intro courses de-emphasize kurtosis).
- **Improvements**:
  - Add one sentence: “Kurtosis relates more to tails/outliers than peak height.”
  - If not required for the exam, consider marking as “advanced / optional”.

## `module_progression.png` — Statistics Bootcamp: Module Progression

- **What works**: Nice at-a-glance roadmap; the color grouping hints at phases.
- **What’s unclear**: It stops at **09**, while the bootcamp folder goes beyond (up to advanced topics). The time estimates may not match actual workload.
- **Improvements**:
  - Update to include the full set of modules (or label this as “Part 1 / core modules”).
  - Add a legend for colors (Foundations / Probability / Inference / Testing) and ensure it matches the curriculum.

## `noir_scales_comparison.png` — NOIR Scales of Measurement

- **What works**: Great summary; “valid operations” is extremely useful for choosing methods.
- **What’s unclear**: Some symbols are tiny; and “Increasing Mathematical Properties” arrow is good but abstract.
- **Improvements**:
  - Increase size of “valid operations”.
  - Add a “common methods” row (e.g., nominal→chi-square, ratio→t-test/regression) or cross-link to the test-selection chart.

## `normal_curve.png` — The Normal Distribution

- **What works**: Clean; mean marker is clear; symmetry callout helps.
- **What’s unclear**: The x-axis uses “standard deviations from mean” but doesn’t explicitly show \(\mu\pm k\sigma\).
- **Improvements**:
  - Replace tick labels with \(\mu-2\sigma, \mu-\sigma, \mu, \mu+\sigma, \mu+2\sigma\).
  - Add one short note: “Area under curve = 1”.

## `normal_empirical_rule.png` — Empirical Rule (duplicate check)

- **What works**: Same as `empirical_rule.png`.
- **What’s unclear**: Appears **duplicated** (same visual). If both are used, it’s confusing.
- **Improvements**:
  - Keep only one file (or make one a variant that also labels \(\mu\pm\sigma\) etc.).

## `regression_diagnostics.png` — Regression Diagnostic Plots

- **What works**: Very practical; clearly contrasts “good” vs assumption violations; QQ plot inclusion is great.
- **What’s unclear**: For a beginner, it’s not explicit *what to do* when an issue is detected.
- **Improvements**:
  - Add “Typical fix” callouts:
    - Nonlinearity → transform/add polynomial term
    - Heteroscedasticity → robust SE / transform
    - Non-normal residuals → check outliers / transformation
  - Add note: “These diagnostics matter mainly for inference (p-values/CI), less for prediction.”

## `sampling_distribution_means.png` — Sampling Distribution of the Mean

- **What works**: Strong: shows \(\mu\) and \(SE=\sigma/\sqrt{n}\) and overlays theoretical normal.
- **What’s unclear**: The title “n=30, 1,000 samples” is good, but students may confuse “samples” with “observations”.
- **Improvements**:
  - Add: “1,000 repetitions of drawing a sample of size \(n=30\)”.
  - Add a quick pointer to CLT conditions.

## `se_vs_sample_size.png` — Standard Error vs. Sample Size

- **What works**: Very intuitive; diminishing returns callout is perfect for decision-making.
- **What’s unclear**: Might be confused with **standard deviation** (SD) vs **standard error** (SE).
- **Improvements**:
  - Add one line: “SD = spread of data; SE = uncertainty of \(\bar X\)”.
  - Add “If \(n\) quadruples → SE halves” as a bold rule.

## `skewness_types.png` — Types of Skewness

- **What works**: Great for the common exam question “mean vs median in skewed distributions”.
- **What’s unclear**: The axis ranges differ; might distract. Tail arrows are helpful though.
- **Improvements**:
  - Standardize axes or note “shapes not to scale”.
  - Add quick rule: “Tail points to direction of skew.”

## `test_selection_flowchart.png` — Choosing the Right Statistical Test

- **What works**: Very useful decision tree; separation of “comparing groups” vs “relationship”.
- **What’s unclear**: Missing common cases for business stats curricula (e.g., **ANOVA**, **proportion tests**, **chi-square GOF vs independence**, **nonparametric**). Also “σ known?” is uncommon in practice; might confuse.
- **Improvements**:
  - Add branch for **proportions** (z-test for p, two-proportion z-test).
  - Add ANOVA for 3+ group mean comparison.
  - Add a note: “σ known is rare; usually use t-tests.”

## `variance_comparison.png` — Comparing Variance: Same Mean, Different Spreads

- **What works**: Clean and memorable; the “narrow vs wide” message is immediate.
- **What’s unclear**: Variance vs SD: beginners sometimes don’t connect “spread” to \(s\) or \(s^2\).
- **Improvements**:
  - Add labels: “SD = 5” and “SD = 15” (and optionally show \(s^2\)).
  - Add formula snippet: \(s^2=\frac{1}{n-1}\sum (x_i-\bar x)^2\).

## `z_table_interpretation.png` — Reading the Standard Normal (Z) Table

- **What works**: The shaded region explanation is excellent; the example \(P(Z\le 1.5)=0.9332\) is concrete.
- **What’s unclear**: Some courses use “area between 0 and z” tables; students need a warning to avoid table-type confusion.
- **Improvements**:
  - Add note: “This table gives left-tail \(P(Z\le z)\). If your table is different, convert.”
  - Add one more example for right tail and two-sided (e.g., \(P(Z>1.5)=1-0.9332\)).


