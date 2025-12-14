# Statistics Bootcamp Review - HSG BBA Student Perspective

**Reviewer Profile:** 2nd year BBA student, taking "3,120 Methoden: Statistik"  
**Date:** December 13, 2025  
**Overall Rating:** 8.2/10 (Very Good, with room for improvement)

---

## Executive Summary

As an HSG BBA student preparing for the Statistics exam, I found this bootcamp to be **well-structured, clearly written, and helpful for conceptual understanding**. The progressive difficulty, worked examples, and consistent page structure make it easy to navigate and learn.

However, comparing it to our actual HSG Übungsblätter (Exercise Sheets), I noticed **significant gaps in exam preparation**. The bootcamp excels at teaching concepts but doesn't fully prepare us for the **calculation-intensive, step-by-step table-based approach** that Professor Füss's exam requires.

**Key Strengths:**
- Clear explanations with business context
- Excellent reference materials (Formula Glossary, Common Mistakes)
- Good conceptual understanding development
- Logical module progression

**Key Weaknesses:**
- Lacks detailed calculation tables (HSG exam requirement)
- Not enough practice problems per topic
- Missing German terminology (exam is in German)
- Exercises don't match Übungsblatt complexity
- No integration problems combining multiple concepts

---

## Detailed Review by Section

### 1. Welcome & Orientation (00_start_here/) ⭐⭐⭐⭐⭐ 5/5

**What Works Well:**
- The welcome page clearly sets expectations as a "complementary" resource
- Prerequisites self-assessment is practical and includes actual math problems
- Study path guidance helps students prioritize

**Suggestions for Improvement:**
1. **Add time estimates per module**: We have limited study time before exams. Knowing "Module 02 takes ~90 minutes" would help planning.

2. **Include exam format description**: Mention that HSG exams are closed-book, calculation-heavy, and require showing all work in tables.

3. **Link to official materials**: Explicitly state "This does NOT replace Übungsblätter 1-6. Work through those first, use this for review."

---

### 2. Descriptive Statistics (Module 02) ⭐⭐⭐⭐ 4/5

**Example Reviewed:** `mean_median_mode.md`, `variance_stddev.md`

**What Works Well:**
- Clear distinction between mean/median/mode with outlier discussion
- Good use of business examples (shoe store inventory, sales data)
- Calculation tables are shown (e.g., variance table in variance_stddev.md)
- "When to use" guidance is practical

**Critical Gaps:**

#### Issue 1: Tables Not Detailed Enough
In `variance_stddev.md`, the worked example shows:

```
| i | xᵢ | xᵢ - x̄ | (xᵢ - x̄)² |
|---|-------|---------|----------|
| 1 | 22 | -6.33 | 40.07 |
...
```

**HSG Übungsblatt 1 requires:**
```
| i | xᵢ | xᵢ - x̄ | |xᵢ - x̄| | (xᵢ - x̄)² |
|---|-------|---------|---------|-----------|
| 1 | 22 | -6.33 | 6.33 | 40.07 |
...
| Σ | 170 | 0 (✓) | 38.01 | 107.34 |
```

**Why it matters:** Übungsblatt exercises specifically ask for **Mean Absolute Deviation (MAD)**, which requires the `|xᵢ - x̄|` column. The bootcamp doesn't cover MAD at all.

**Missing Concepts:**
- Mean Absolute Deviation (MAD) - explicitly tested in Übungsblatt 1
- Weighted mean with frequency distributions
- Coefficient of variation (mentioned but not practiced enough)
- Range (Spannweite) - basic but always appears in exams

#### Issue 2: Not Enough Practice Problems
Each topic has 2-3 practice problems. **HSG requires ~20-30 calculations per topic area** (based on Übungsblatt 1 structure).

**Recommendation:** Add an "Extended Practice" section with 10+ problems at varying difficulty levels.

---

### 3. Probability Fundamentals (Module 04) ⭐⭐⭐⭐ 4/5

**Example Reviewed:** `probability_rules.md`

**What Works Well:**
- Venn diagrams are helpful visual aids
- Complement, addition, and multiplication rules clearly explained
- Good examples with mutually exclusive vs. independent events

**Critical Gaps:**

#### Issue 1: Missing Odds (Quoten) Calculations
**From Übungsblatt 2:** Odds are explicitly tested:
```
Odds(A) = P(A) / P(A')
```

The bootcamp doesn't mention odds at all, but they appear in HSG exams.

#### Issue 2: Set Operations Not Formal Enough
Übungsblatt 2 uses formal set notation:
- A ∪ B (union)
- A ∩ B (intersection)
- A \ B (set difference, "A ohne B")
- Venn diagram shading exercises

The bootcamp uses these symbols but doesn't explicitly teach **how to calculate P(A \ B)** or **shade regions in Venn diagrams**.

**Example from Übungsblatt 2:**
> "Given P(A) = 0.7, P(B) = 0.4, P(A ∩ B) = 0.3. Calculate P(A \ B)."
>
> Solution: P(A \ B) = P(A) - P(A ∩ B) = 0.7 - 0.3 = 0.4

**Recommendation:** Add a dedicated section on:
1. Set operations (∪, ∩, \, complement)
2. Venn diagram problem-solving
3. Odds calculations

---

### 4. Probability Distributions (Modules 05-06) ⭐⭐⭐⭐⭐ 4.5/5

**Examples Reviewed:** Binomial, Poisson, Normal distributions

**What Works Well:**
- Clear distinction between when to use each distribution
- Flowchart for choosing distributions is **excellent** (very helpful!)
- Z-score calculations well-explained
- Standardization formula clearly shown

**Minor Gaps:**

#### Issue 1: Need More Multi-Step Problems
Übungsblatt 3A/3B problems are often **multi-part**:
> "A coin is flipped 10 times.
> a) What is P(exactly 6 heads)?
> b) What is P(at most 6 heads)?
> c) What is P(between 4 and 7 heads, inclusive)?
> d) Calculate the expected value and variance."

The bootcamp's practice problems are mostly single-part.

**Recommendation:** Add "integrated problems" that require:
- Identifying the correct distribution
- Calculating multiple probabilities
- Computing E(X) and Var(X)
- Interpreting results in context

#### Issue 2: Poisson Approximation to Binomial
Übungsblatt 3A explicitly covers when to approximate Binomial with Poisson (n large, p small, λ = np).

**Recommendation:** Add a section on distribution approximations.

---

### 5. Sampling Distributions & Central Limit Theorem (Module 07) ⭐⭐⭐⭐⭐ 5/5

**Excellent!** This module is well-done and matches HSG requirements closely.

**What Works Well:**
- Standard error explained clearly (SE = σ/√n)
- CLT implications well-illustrated
- Distinction between σ (data spread) and SE (sampling spread) is clear

**One Suggestion:**
Add a "common mistake" box highlighting:
> ⚠️ **Don't confuse σ with σ/√n!**
> - For individual observations: z = (x - μ) / σ
> - For sample means: z = (x̄ - μ) / (σ/√n)

---

### 6. Confidence Intervals (Module 08) ⭐⭐⭐⭐ 4/5

**Example Reviewed:** `ci_mean.md`

**What Works Well:**
- Clear distinction between z-interval (σ known) vs. t-interval (σ unknown)
- Step-by-step calculation shown
- Good interpretation guidance

**Critical Gap:**

#### Issue 1: Missing Sample Size Determination
**From Übungsblatt 4:** A major topic is calculating required sample size given desired margin of error:

```
n = (z_{α/2} × σ / E)²
```

Example problem:
> "You want to estimate mean income with 95% confidence and margin of error of ±500 CHF. 
> If σ = 2000, what sample size is needed?"

The bootcamp mentions sample size determination briefly in `sample_size.md` but doesn't provide **worked examples with substitution**.

**Recommendation:** 
- Add 3-4 sample size calculation problems
- Show all steps: identify z, σ, E → substitute → calculate → round up

---

### 7. Hypothesis Testing (Modules 09-11) ⭐⭐⭐⭐ 4/5

**Examples Reviewed:** Testing framework, t-tests, z-tests

**What Works Well:**
- **5-step framework is perfect** - matches HSG requirements exactly
- Clear distinction between one-tailed and two-tailed tests
- Type I and Type II error explanations are good

**Critical Gaps:**

#### Issue 1: Type II Error (β) and Power Calculations
**From Übungsblatt 5:** Calculating β and power is explicitly tested:

```
β = P(fail to reject H₀ | H₁ is true)
Power = 1 - β
```

Example:
> "Given H₀: μ = 100, H₁: μ > 100, α = 0.05, σ = 10, n = 25.
> Calculate β if the true mean is actually 105."

The bootcamp mentions Type II error conceptually in `error_types.md` but **doesn't show how to calculate it**.

**Recommendation:**
- Add worked example of β calculation
- Show power curve interpretation
- Include 2-3 practice problems

#### Issue 2: Entscheidungsregel (Decision Rule) Phrasing
HSG exams require specific phrasing:

**HSG Format:**
> "Entscheidungsregel: Lehne H₀ ab, falls t > t_{0.05,24} = 1.711"
> "Entscheidung: Da t = 2.5 > 1.711, wird H₀ abgelehnt."

The bootcamp uses correct logic but doesn't teach the **formal German phrasing** that Prof. Füss expects.

**Recommendation:**
- Add a box showing German vs. English phrasing
- Include key terms: Nullhypothese, Alternativhypothese, Verwerfungsbereich, Teststatistik

---

### 8. Regression Analysis (Module 12) ⭐⭐⭐ 3.5/5

**Example Reviewed:** `fitting_regression.md`

**What Works Well:**
- OLS formulas correctly presented
- Calculation table structure is good
- Interpretation of coefficients is clear

**Critical Gaps:**

#### Issue 1: Table Structure Too Simple
The worked example shows:

```
| x | y | x-x̄ | y-ȳ | (x-x̄)(y-ȳ) | (x-x̄)² |
```

**Übungsblatt 6 requires more columns:**

```
| Rep | xᵢ | yᵢ | xᵢyᵢ | xᵢ² | yᵢ² | xᵢ-x̄ | (xᵢ-x̄)² | yᵢ-ȳ | (yᵢ-ȳ)² | (xᵢ-x̄)(yᵢ-ȳ) |
```

**Why it matters:** HSG exams often require **alternative calculation methods** using Σxᵢyᵢ, Σxᵢ², etc.

Alternative slope formula tested in HSG:
```
β̂₁ = [Σxᵢyᵢ - n×x̄×ȳ] / [Σxᵢ² - n×x̄²]
```

**Recommendation:**
1. Show **both computational methods** (deviation form and raw score form)
2. Add practice problems requiring the full calculation table
3. Include SSE, SSR, SST calculations in the same table

#### Issue 2: Missing Correlation → Regression Connection
Übungsblatt 6 explicitly links correlation to regression:
```
β̂₁ = r × (sᵧ / sₓ)
```

This relationship isn't mentioned in the bootcamp.

---

### 9. Reference Materials (reference/) ⭐⭐⭐⭐⭐ 5/5

**Excellent resource!** The best part of the bootcamp.

**What Works Well:**
- `common_mistakes.md` is **exactly what we need** before exams
- `formula_glossary.md` is comprehensive and well-organized
- Sample vs. population notation table is super helpful

**One Addition:**
Add a **"Quick Lookup Table"** at the top of formula_glossary.md:

```
EXAM QUICK REFERENCE

Mean: x̄ = Σxᵢ / n
Variance (sample): s² = Σ(xᵢ-x̄)² / (n-1)
Std Dev (sample): s = √s²
SE: SE = s / √n
z-score: z = (x - μ) / σ
t-statistic: t = (x̄ - μ₀) / (s/√n)
CI for mean: x̄ ± t_{α/2} × (s/√n)
Regression slope: β̂₁ = Σ(xᵢ-x̄)(yᵢ-ȳ) / Σ(xᵢ-x̄)²
```

This would be perfect for **last-minute review before entering the exam hall**.

---

### 10. Exercise Sheets (exercises/) ⭐⭐⭐ 3/5

**Examples Reviewed:** `exercise_1.md` (Descriptive Statistics)

**What Doesn't Work:**

#### Issue 1: Not Enough Problems
- Exercise 1 has **3 problems**
- Übungsblatt 1 has **8 multi-part Aufgaben** (≈20-25 individual calculations)

We need **significantly more practice** to be exam-ready.

#### Issue 2: Difficulty Too Low
The bootcamp exercises are straightforward applications. HSG exercises often include:
- Tricky data requiring careful organization
- Multi-step problems building on previous parts
- Real-world contexts requiring interpretation

**Example from Übungsblatt 1 (more realistic):**
> "A survey of 2567 households recorded persons per household:
> | Persons | Count |
> | 1 | 457 |
> | 2 | 628 |
> | 3 | 612 |
> | 4 | 526 |
> | ≥5 | 344 |
> 
> a) Calculate relative frequencies f(xᵢ)
> b) Calculate cumulative distribution F(xᵢ)
> c) How many households have ≤3 persons?
> d) Calculate the mean (use midpoint for ≥5 category as 6)
> e) Explain why the mean might be biased"

This is more realistic than bootcamp problems.

**Recommendation:**
1. Add **"Extended Exercise Sets"** with 10-15 problems per Übungsblatt topic
2. Include multi-part problems requiring 5-10 minutes each
3. Add problems with large datasets and frequency distributions

---

## Comparison to HSG Übungsblätter

| Aspect | Bootcamp | HSG Übungsblatt | Gap |
|--------|----------|-----------------|-----|
| Number of problems | ~25 total | ~50-60 per topic | ❌ Major gap |
| Calculation tables | Shown, but simplified | Full tables required | ⚠️ Moderate gap |
| German terminology | Not included | Exam is in German | ❌ Major gap |
| Multi-part problems | Few | Most problems | ⚠️ Moderate gap |
| Integration problems | None | Common | ❌ Major gap |
| Step-by-step substitution | Sometimes | Always required | ⚠️ Moderate gap |
| Formula sheets | Excellent | Basic in exam | ✅ Better than HSG |
| Refresher sections | Not formal | Every Übungsblatt | ⚠️ Could add |

---

## What's Missing Entirely

### 1. German Terminology
The exam is conducted in German. Key terms students MUST know:

| English | German | Used in Bootcamp? |
|---------|--------|-------------------|
| Mean | Mittelwert | ❌ No |
| Sample | Stichprobe | ❌ No |
| Population | Grundgesamtheit | ❌ No |
| Null hypothesis | Nullhypothese | ❌ No |
| Confidence interval | Konfidenzintervall | ❌ No |
| Rejection region | Ablehnungsbereich | ❌ No |

**Recommendation:** Add a "German-English Glossary" page with all exam terminology.

### 2. Mean Absolute Deviation (MAD)
**From Übungsblatt 1:**
```
MAD = (1/n) × Σ|xᵢ - x̄|
```

This measure is explicitly tested but not covered in the bootcamp.

### 3. Odds (Quoten)
**From Übungsblatt 2:**
```
Odds(A) = P(A) / P(A')
P(A) = Odds(A) / (1 + Odds(A))
```

### 4. Frequency Distributions with Class Intervals
Many Übungsblatt problems use grouped data:

| Class | Frequency |
|-------|-----------|
| 0-10 | 5 |
| 10-20 | 12 |
| 20-30 | 8 |

Students must calculate mean using midpoints, which isn't covered.

### 5. Conditional Probability Tables
Übungsblatt 2 heavily emphasizes 2×2 tables for conditional probability:

|     | B | B' | Total |
|-----|---|----|----|
| A   | 30 | 20 | 50 |
| A'  | 10 | 40 | 50 |
| Total | 40 | 60 | 100 |

Then calculate P(A|B), P(B|A), etc. This format appears frequently but isn't explicitly taught.

---

## Specific Improvement Recommendations

### Priority 1 (Critical for Exam Success) 🔴

1. **Add German terminology throughout**
   - Bilingual headings: "Mean / Mittelwert"
   - Glossary page with all exam terms
   - Example problems phrased in German

2. **Expand calculation tables to HSG standard**
   - Include all intermediate columns
   - Show sum rows (Σ) for error checking
   - Always verify Σ(xᵢ - x̄) = 0

3. **Add missing concepts:**
   - Mean Absolute Deviation (MAD)
   - Odds calculations
   - Frequency distributions with class intervals
   - Set operations (A \ B)
   - Type II error calculations (β, power)

4. **Triple the number of practice problems**
   - Target: 50+ problems per major topic
   - Include Übungsblatt-style multi-part questions
   - Add time estimates (e.g., "Target: 8 minutes")

### Priority 2 (Strongly Recommended) 🟡

5. **Add "Integration Exercises"**
   - Problems combining 3-4 concepts
   - Example: "Calculate CI, interpret, then test hypothesis"
   - Mimics actual exam format

6. **Create "Übungsblatt Companion" sections**
   - One section per Übungsblatt (1-6)
   - "If you struggled with Übungsblatt 3, Aufgabe 2, review these pages..."
   - Direct mapping to official materials

7. **Add alternative calculation formulas**
   - Show both deviation form and raw score form
   - Regression: multiple computational approaches
   - Variance: computing formula vs. definitional formula

8. **Include more real business contexts**
   - Swiss companies (Credit Suisse, Nestlé, ABB)
   - Marketing analytics (customer segmentation)
   - Financial analysis (portfolio returns)
   - Supply chain (inventory optimization)

### Priority 3 (Nice to Have) 🟢

9. **Add time-based practice tests**
   - "Simulated Exam: 60 minutes, 6 problems"
   - Matches actual exam pressure

10. **Video walkthrough suggestions**
    - QR codes linking to video solutions
    - Especially helpful for complex table calculations

11. **Spaced repetition tracker**
    - Checkboxes for "First attempt | Review 1 | Review 2"
    - Helps with exam prep scheduling

12. **Common exam tricks section**
    - "Watch out for: units changes (minutes to hours)"
    - "Always check: Does your answer make practical sense?"

---

## What to Keep (Don't Change!)

### ✅ Excellent Features

1. **Consistent page structure**
   - Learning objectives → Key concepts → Worked example → Practice → Takeaways
   - Makes navigation easy

2. **Worked examples with substitution**
   - Formula shown symbolically first
   - Then values substituted
   - This is exactly HSG exam format

3. **"Common Mistakes to Avoid" boxes**
   - These are gold! Keep adding more throughout

4. **Formula Glossary**
   - One-stop reference is incredibly useful
   - Perfect for last-minute review

5. **Progressive difficulty**
   - Building from basics to advanced is well done

6. **Visualization aids**
   - Venn diagrams, distribution curves, boxplots are helpful

7. **Business contextualization**
   - Examples feel relevant to BBA students

---

## Student Usage Recommendations

Based on this review, here's how I'd use this bootcamp:

### Week 1-2: Concept Building
- Read through all modules in order
- Do the worked examples alongside
- Check understanding with practice problems

### Week 3-4: Übungsblatt Focus
- Work through all 6 Übungsblätter
- When stuck, come back to bootcamp for concept review
- Use Formula Glossary as reference

### Week 5: Exam Prep
- Review "Common Mistakes" daily
- Redo all Übungsblatt problems from memory
- Use bootcamp exercises as warm-up

### Week 6: Final Review
- Quick read through "Key Takeaways" from each module
- Memorize critical values (z, t tables)
- Review Formula Glossary one last time

---

## Conclusion

This bootcamp is a **strong foundation** for conceptual understanding but needs significant enhancement to be a complete exam preparation resource for HSG Statistics.

### For Self-Study:
**Rating: 8.2/10** - Excellent for learning concepts, good reference materials, but insufficient practice problems.

### For Exam Preparation:
**Rating: 6.5/10** - Must be supplemented with Übungsblätter. Cannot replace official materials.

### Recommendation to Future Students:
**Use this bootcamp ALONGSIDE Übungsblätter, not instead of them.**

1. **First pass:** Work through bootcamp modules to build understanding
2. **Second pass:** Complete all 6 Übungsblätter (this is essential!)
3. **Third pass:** Use bootcamp for targeted review of weak areas
4. **Before exam:** Review Common Mistakes and Formula Glossary

### If Only One Resource:
If I could only use **one** resource: Choose the **Übungsblätter**.  
If I could use **two** resources: Übungsblätter + **this bootcamp's Reference section**.  
If I can use **three** resources: Übungsblätter + entire bootcamp + past exams.

---

## Final Thoughts

As an HSG BBA student, I genuinely appreciate the effort that went into creating this bootcamp. The clear explanations and structured approach make statistics less intimidating.

However, **Professor Füss's exams are calculation-intensive**, and success requires extensive practice with the exact table format, German terminology, and multi-step problems that appear in Übungsblätter.

**The bootcamp teaches you to think statistically.**  
**The Übungsblätter teach you to perform on the exam.**

You need both.

**Thank you for creating this resource!** With the improvements suggested above, it could become an indispensable exam preparation tool for future HSG BBA cohorts.

---

**Viel Erfolg bei der Prüfung!** (Good luck on the exam!)

*Student Reviewer*  
HSG BBA, Herbstsemester 2024

