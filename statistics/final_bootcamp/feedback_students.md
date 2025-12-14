# Student feedback (merged)

This file merges the 5 student feedback documents into a single view, structured by bootcamp page.

**Sources:**
- Student 1: `statistics/final_bootcamp/review_student_1.md`
- Student 2: `statistics/final_bootcamp/review_student_2.md`
- Student 3: `statistics/review_student_3.md`
- Student 4: `statistics/final_bootcamp/review_student_4.md`
- Student 5: `statistics/final_bootcamp/review_student_5.md`

## Cross-cutting feedback (not page-specific)

### Student 1

#### Statistics Bootcamp Review - HSG BBA Student Perspective

**Reviewer Profile:** 2nd-year HSG BBA student, taking "3,120 Methoden: Statistik"  
**Date:** December 2024  
**Purpose:** Evaluate bootcamp content for exam preparation effectiveness

---

##### Executive Summary

Overall, this bootcamp is a **solid supplementary resource** for exam preparation. The structure is clear, the formulas are correct, and the step-by-step approach matches what we need for the Übungsblätter. However, there are several areas where the content could be significantly improved to better match HSG exam expectations and maximize learning outcomes.

**Overall Rating:** 7/10  
**Potential after improvements:** 9/10

---

##### Table of Contents

1. [General Strengths](#general-strengths)
2. [General Areas for Improvement](#general-areas-for-improvement)
3. [Module-by-Module Review](#module-by-module-review)
4. [Reference Materials Review](#reference-materials-review)
5. [Exercises Review](#exercises-review)
6. [Priority Recommendations](#priority-recommendations)

---

##### General Strengths

###### ✅ What Works Well

1. **Consistent Page Structure**
   - Learning objectives at the start of each page help me know what to focus on
   - The toggle solutions for practice problems let me try before checking
   - Key takeaways summarize the essentials

2. **Calculation Tables**
   - The worked examples use tables exactly like we need for the exam
   - Step-by-step formula → substitution → calculation format matches HSG requirements

3. **Formula Notation**
   - Correct distinction between sample (s, x̄) and population (σ, μ) notation
   - LaTeX formulas render clearly

4. **Navigation**
   - Clear links between modules
   - Easy to jump to related content and references

5. **Common Mistakes Section**
   - The `common_mistakes.md` is extremely valuable - I wish I'd seen this before my first midterm!
   - Type I/II error confusion is exactly what students struggle with

---

##### General Areas for Improvement

###### ⚠️ Critical Issues

###### 1. **INSUFFICIENT PRACTICE PROBLEMS**

**Problem:** Each exercise file has only 2-3 problems. The HSG Übungsblätter have 7-8 multi-part problems (20-30 individual calculations per topic).

**Impact:** Without enough practice, I won't build the speed and accuracy needed for the exam.

**Recommendation:**
- Add at least 5-6 more problems per exercise file
- Include multi-part problems (a, b, c, d) that build on each other
- Add problems with larger datasets requiring full calculation tables

###### 2. **MISSING GERMAN TERMINOLOGY**

**Problem:** The bootcamp is entirely in English, but the actual exam and Übungsblätter are in German.

**Impact:** I might not recognize key terms like:
- "Stichprobe" (sample) vs "Grundgesamtheit" (population)
- "Mittelwert" (mean), "Streuung" (dispersion)
- "Signifikanzniveau" (significance level)

**Recommendation:**
- Add a German-English glossary
- Include German terms in parentheses for key concepts
- Example: "Sample variance (Stichprobenvarianz)"

###### 3. **NOT ENOUGH EMPHASIS ON FIVE-STEP HYPOTHESIS TESTING**

**Problem:** The hypothesis testing framework page (Module 09) is too brief. HSG requires the explicit five-step format:
1. State H₀ and H₁
2. Identify test statistic and distribution
3. Find critical value(s)
4. Calculate test statistic with substitution
5. State decision: "Reject H₀" or "Do not reject H₀"

**Impact:** Students might lose marks for incomplete answers.

**Recommendation:**
- Expand the testing_framework.md significantly
- Show the five-step format explicitly in EVERY hypothesis testing example
- Add a template students can memorize

###### 4. **MISSING CALCULATION SHORTCUTS**

**Problem:** Some formulas have alternative "computational" forms that are faster for exams:

For example, variance can also be calculated as:
$$s^2 = \frac{1}{n-1}\left(\sum x_i^2 - \frac{(\sum x_i)^2}{n}\right)$$

**Recommendation:**
- Add alternative formulas where they exist
- Show when each form is more efficient

---

### Student 2

#### Student Review — HSG BBA Perspective (high-grade oriented)

##### Scope
- Reviewed **82** curriculum markdown files in `statistics/final_bootcamp/`.
- Excluded existing review files (not curriculum):
  - `review_student_1.md`
  - `review_student_4.md`
  - `review_student_5.md`

##### Executive summary (what will most improve grades)
- **More Übungsblatt-style drill density**: many topics have 1–2 examples; HSG exams reward speed + pattern repetition.
- **Standardize procedures**: every test page should use the same 5-step template + identical notation for α/α/2, df, and decision rule.
- **Surface traps**: explicitly label the frequent errors (SE vs SD, p0 vs p-hat, α vs α/2, df, table lookup).
- **Interpretation practice**: add one “so what?” business sentence after every calculation.

### Student 3

#### Statistics Bootcamp Review - HSG BBA Student Perspective

**Reviewer Profile:** 2nd year BBA student, taking "3,120 Methoden: Statistik"  
**Date:** December 13, 2025  
**Overall Rating:** 8.2/10 (Very Good, with room for improvement)

---

##### Executive Summary

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

Unmapped section (Modules 05-06)

**Examples Reviewed:** Binomial, Poisson, Normal distributions

**What Works Well:**
- Clear distinction between when to use each distribution
- Flowchart for choosing distributions is **excellent** (very helpful!)
- Z-score calculations well-explained
- Standardization formula clearly shown

**Minor Gaps:**

###### Issue 1: Need More Multi-Step Problems
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

###### Issue 2: Poisson Approximation to Binomial
Übungsblatt 3A explicitly covers when to approximate Binomial with Poisson (n large, p small, λ = np).

**Recommendation:** Add a section on distribution approximations.

---

Unmapped section (Modules 09-11)

**Examples Reviewed:** Testing framework, t-tests, z-tests

**What Works Well:**
- **5-step framework is perfect** - matches HSG requirements exactly
- Clear distinction between one-tailed and two-tailed tests
- Type I and Type II error explanations are good

**Critical Gaps:**

###### Issue 1: Type II Error (β) and Power Calculations
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

###### Issue 2: Entscheidungsregel (Decision Rule) Phrasing
HSG exams require specific phrasing:

**HSG Format:**
> "Entscheidungsregel: Lehne H₀ ab, falls t > t_{0.05,24} = 1.711"
> "Entscheidung: Da t = 2.5 > 1.711, wird H₀ abgelehnt."

The bootcamp uses correct logic but doesn't teach the **formal German phrasing** that Prof. Füss expects.

**Recommendation:**
- Add a box showing German vs. English phrasing
- Include key terms: Nullhypothese, Alternativhypothese, Verwerfungsbereich, Teststatistik

---

Unmapped section (MAD)

**From Übungsblatt 1:**
```
MAD = (1/n) × Σ|xᵢ - x̄|
```

This measure is explicitly tested but not covered in the bootcamp.

Unmapped section (Quoten)

**From Übungsblatt 2:**
```
Odds(A) = P(A) / P(A')
P(A) = Odds(A) / (1 + Odds(A))
```

###### 4. Frequency Distributions with Class Intervals
Many Übungsblatt problems use grouped data:

| Class | Frequency |
|-------|-----------|
| 0-10 | 5 |
| 10-20 | 12 |
| 20-30 | 8 |

Students must calculate mean using midpoints, which isn't covered.

###### 5. Conditional Probability Tables
Übungsblatt 2 heavily emphasizes 2×2 tables for conditional probability:

|     | B | B' | Total |
|-----|---|----|----|
| A   | 30 | 20 | 50 |
| A'  | 10 | 40 | 50 |
| Total | 40 | 60 | 100 |

Then calculate P(A|B), P(B|A), etc. This format appears frequently but isn't explicitly taught.

---

##### Specific Improvement Recommendations

###### Priority 1 (Critical for Exam Success) 🔴

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

###### Priority 2 (Strongly Recommended) 🟡

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

###### Priority 3 (Nice to Have) 🟢

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

##### What to Keep (Don't Change!)

###### ✅ Excellent Features

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

##### Student Usage Recommendations

Based on this review, here's how I'd use this bootcamp:

###### Week 1-2: Concept Building
- Read through all modules in order
- Do the worked examples alongside
- Check understanding with practice problems

###### Week 3-4: Übungsblatt Focus
- Work through all 6 Übungsblätter
- When stuck, come back to bootcamp for concept review
- Use Formula Glossary as reference

###### Week 5: Exam Prep
- Review "Common Mistakes" daily
- Redo all Übungsblatt problems from memory
- Use bootcamp exercises as warm-up

###### Week 6: Final Review
- Quick read through "Key Takeaways" from each module
- Memorize critical values (z, t tables)
- Review Formula Glossary one last time

---

##### Conclusion

This bootcamp is a **strong foundation** for conceptual understanding but needs significant enhancement to be a complete exam preparation resource for HSG Statistics.

###### For Self-Study:
**Rating: 8.2/10** - Excellent for learning concepts, good reference materials, but insufficient practice problems.

###### For Exam Preparation:
**Rating: 6.5/10** - Must be supplemented with Übungsblätter. Cannot replace official materials.

###### Recommendation to Future Students:
**Use this bootcamp ALONGSIDE Übungsblätter, not instead of them.**

1. **First pass:** Work through bootcamp modules to build understanding
2. **Second pass:** Complete all 6 Übungsblätter (this is essential!)
3. **Third pass:** Use bootcamp for targeted review of weak areas
4. **Before exam:** Review Common Mistakes and Formula Glossary

###### If Only One Resource:
If I could only use **one** resource: Choose the **Übungsblätter**.  
If I could use **two** resources: Übungsblätter + **this bootcamp's Reference section**.  
If I can use **three** resources: Übungsblätter + entire bootcamp + past exams.

---

##### Final Thoughts

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

### Student 4

#### Student Review 4: HSG BBA Perspective
**Reviewer:** Anonymous HSG BBA Student (3rd semester)  
**Date:** December 2025  
**Background:** Statistics course "Methods: Statistics" (3,120) - Herbstsemester 2024

---

##### Executive Summary

As an HSG BBA student preparing for the Methods: Statistics exam, I find this bootcamp to be a solid supplementary resource but it requires significant improvements to achieve optimal learning outcomes and high grades. The content covers the right topics but lacks the business context, calculation precision, and exam-focused structure that HSG students need.

**Overall Rating:** 6.5/10  
**Grade Potential:** Currently supports 4.0-4.5; with improvements could support 5.5-6.0

---

##### 1. Strengths

###### ✅ Clear Structure and Navigation
- Well-organized modules with logical progression
- Good use of learning objectives and time estimates
- Formula glossary is comprehensive and searchable
- Common mistakes section directly addresses frequent exam errors

###### ✅ Technical Accuracy
- Formulas are mathematically correct
- Step-by-step solutions are generally accurate
- Good explanation of n-1 vs n distinction
- Appropriate use of statistical notation

###### ✅ Practice Problems
- Calculation tables follow reasonable format
- Solutions are hidden in toggles (good for self-testing)
- Mix of conceptual and calculation problems

---

##### 2. Major Areas for Improvement

###### 🚨 Lack of Business Relevance
**Current Issue:** Examples are too generic and academic. HSG students need consulting/finance/marketing context.

**Specific Problems:**
- Customer age datasets instead of market research scenarios
- Generic "companies" instead of recognizable Swiss firms (Nestlé, UBS, etc.)
- Missing connection to business decision-making

**HSG Context:** Our program emphasizes practical application for consulting, finance, and management careers.

**Recommendations:**
- Replace generic examples with business cases:
  - Marketing: A/B testing conversion rates for digital campaigns
  - Finance: Risk analysis of investment portfolios
  - Consulting: Customer satisfaction benchmarking for client projects
  - Operations: Quality control in manufacturing processes

###### 🚨 Insufficient HSG Exercise Alignment
**Current Issue:** Bootcamp format doesn't match actual Übungsblatt structure.

**Specific Problems:**
- Missing the multi-part "Aufgabe 1, Aufgabe 2" format
- Calculation tables lack the exact column structure HSG expects
- No emphasis on 4-decimal precision for intermediate calculations
- Missing German terminology integration

**HSG Exercise Style (from actual Übungsblätter):**
```
AUFGABE 1 - DESCRIPTIVE STATISTICS
Given: x = [12, 15, 18, 14, 12, 22, 16, 14, 12, 85]

a) Calculate Range:
   Range = x_max - x_min = 85 - 12 = 73

b) Build calculation table for MAD:
   | xi | xi - x̄ | |xi - x̄| |
   |----|--------|----------|
   | 12 | -21.4  | 21.4     |
   [...]
   Σ |         | 148.2    |
   MAD = Σ|xi-x̄| / n = 148.2 / 10 = 14.82
```

**Recommendations:**
- Restructure exercises to match HSG format exactly
- Include German column headers in tables
- Emphasize 4-decimal precision for intermediates, 2 decimals for final answers
- Add "Refresher" sections like real Übungsblätter

###### 🚨 Weak Business Decision-Making Framework
**Current Issue:** Focus on calculations without connecting to business implications.

**Specific Problems:**
- Missing interpretation sections for business context
- No discussion of "So what?" for managers
- Limited emphasis on statistical vs. practical significance

**HSG Context:** We learn statistics to support business decisions, not just pass exams.

**Recommendations:**
- Add "Business Implications" sections to each worked example
- Include decision-making frameworks:
  ```
  Statistical Result: p = 0.03, reject H₀
  Business Decision: Launch new marketing campaign
  Rationale: Evidence suggests 3% conversion improvement is statistically significant
  Risk Assessment: Consider implementation costs vs. expected ROI
  ```

###### 🚨 Insufficient German Terminology Integration
**Current Issue:** No German terms despite exercises being in German.

**Specific Problems:**
- Missing key terms students encounter in Übungsblätter
- No pronunciation guides for Greek letters
- English-only explanations

**HSG Context:** Lectures and exercises are in German; exams test German terminology.

**Recommendations:**
- Add German glossary with key terms:
  - Mittelwert = Mean, Standardabweichung = Standard Deviation
  - Konfidenzintervall = Confidence Interval, Hypothesentest = Hypothesis Test
- Include German mathematical notation where appropriate
- Add sidebar with German equivalents for key concepts

###### 🚨 Limited Exam Preparation Focus
**Current Issue:** Good content but not exam-optimized.

**Specific Problems:**
- Missing time management tips for calculations
- No "Altklausuren" (past exam) style questions
- Limited emphasis on common HSG trick questions

**HSG Context:** Exams are time-pressured; need to recognize patterns from past exams.

**Recommendations:**
- Add "Exam Strategy" sections
- Include past exam-style questions
- Add timing guidelines: "Spend no more than 5 minutes on Aufgabe 1a"

---

### Student 5

#### Statistics Bootcamp Review - Student Perspective
##### HSG BBA Student Review (Target: High Grade Achievement)

**Reviewer Profile:** HSG BBA student preparing for "3,120 Methoden: Statistik" exam  
**Date:** December 2024  
**Review Focus:** Content quality, exam alignment, learning effectiveness

---

##### Executive Summary

**Overall Assessment:** ⭐⭐⭐⭐ (4/5)

The bootcamp provides solid foundational content with clear explanations and good visual aids. However, **critical gaps exist** compared to actual HSG Übungsblatt format and exam expectations. To achieve top grades, students need more alignment with HSG's specific requirements: detailed calculation tables, German terminology, step-by-step formula substitutions, and emphasis on common exam pitfalls.

**Key Strengths:**
- Clear concept explanations
- Good visual aids
- Business-oriented examples
- Comprehensive topic coverage

**Critical Gaps:**
- Missing German terminology (essential for HSG)
- Exercises don't match HSG calculation table format
- Insufficient step-by-step detail in solutions
- Missing some HSG-specific topics
- Need more emphasis on common exam mistakes

---

##### 1. CONTENT QUALITY & CLARITY

###### ✅ Strengths

**1.1 Concept Explanations**
- Explanations are clear and accessible
- Good use of business examples (salaries, sales, delivery times)
- Visual aids (images) are helpful for understanding
- Progressive difficulty is appropriate

**1.2 Structure**
- Well-organized modules
- Clear learning objectives
- Good navigation between topics
- Reference section is comprehensive

**1.3 Examples**
- Business context is relevant (CHF, Swiss companies)
- Examples are realistic and relatable
- Worked examples show the process

###### ⚠️ Areas Needing Improvement

**1.1 Missing German Terminology**
**CRITICAL ISSUE:** HSG exams use German terminology. Students need to recognize:
- Mittelwert (mean)
- Varianz (variance)
- Standardabweichung (standard deviation)
- Stichprobe (sample)
- Grundgesamtheit (population)
- Konfidenzintervall (confidence interval)
- Hypothesentest (hypothesis test)

**Recommendation:**
- Add a German-English terminology glossary
- Include German terms in parentheses throughout content
- Create flashcards with German terms
- Add German term recognition exercises

**Example Fix Needed:**
```markdown
**Mean (Mittelwert):**
The arithmetic mean (arithmetisches Mittel) is calculated as...
```

**1.2 Formula Presentation**
While formulas are present, they don't always show the **substitution step** that HSG requires.

**Current Format:**
```markdown
$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2$$
```

**HSG Format Required:**
```markdown
**Formula:** $$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

**Substitute values:** $$s^2 = \frac{1}{7-1} \times 107.34 = \frac{107.34}{6} = 17.89$$

**Final answer:** $$s^2 = 17.89$$
```

**Recommendation:** Add explicit "Formula → Substitute → Calculate → Answer" structure to all worked examples.

---

##### 2. EXERCISE FORMAT & ALIGNMENT WITH HSG

###### ❌ Critical Gap: Exercise Format Doesn't Match HSG Übungsblätter

**HSG Requirement:** Exercises must include:
1. **Detailed calculation tables** with all intermediate columns
2. **Step-by-step formula substitutions** showing every number plugged in
3. **Running sums (Σ)** clearly shown
4. **Multi-part problems** that build on each other

###### Current Exercise Format Issues

**Example: Exercise 1, Problem 1**

**Current (Too Brief):**
```markdown
| x | x - 51.25 | (x - 51.25)² |
|---|-----------|--------------|
| 45 | -6.25 | 39.06 |
...
$$s^2 = \frac{273.48}{7} = 39.07$$
```

**HSG Format Required:**
```markdown
**Step 1: Calculate Mean**
$$\bar{x} = \frac{45+52+48+55+60+42+58+50}{8} = \frac{410}{8} = 51.25$$

**Step 2: Build Calculation Table**

| i | $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|---|-------|-----------------|---------------------|
| 1 | 45 | 45 - 51.25 = -6.25 | (-6.25)² = 39.0625 |
| 2 | 52 | 52 - 51.25 = 0.75 | (0.75)² = 0.5625 |
| 3 | 48 | 48 - 51.25 = -3.25 | (-3.25)² = 10.5625 |
| 4 | 55 | 55 - 51.25 = 3.75 | (3.75)² = 14.0625 |
| 5 | 60 | 60 - 51.25 = 8.75 | (8.75)² = 76.5625 |
| 6 | 42 | 42 - 51.25 = -9.25 | (-9.25)² = 85.5625 |
| 7 | 58 | 58 - 51.25 = 6.75 | (6.75)² = 45.5625 |
| 8 | 50 | 50 - 51.25 = -1.25 | (-1.25)² = 1.5625 |
| **Σ** | **410** | **≈ 0** | **273.5000** |

**Step 3: Apply Formula**
$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2 = \frac{1}{8-1} \times 273.50 = \frac{273.50}{7} = 39.07$$

**Step 4: Final Answer**
Sample variance: $s^2 = 39.07$
```

**Recommendation:**
- Restructure ALL exercises to match HSG format exactly
- Show every calculation step explicitly
- Include intermediate value columns in tables
- Add "Check" steps (e.g., verify Σ(xᵢ - x̄) ≈ 0)

###### Missing HSG-Specific Topics

**Topics in Übungsblatt 1 that are missing or insufficient:**

1. **Mittlere Absolute Abweichung (MAD)** - Only briefly mentioned, needs full treatment
   - Formula: MAD = (1/n) Σ|xi - x̄|
   - Calculation table format required
   - Comparison with standard deviation

2. **Gewichtetes arithmetisches Mittel (Weighted Mean)** - Missing
   - Formula: x̄w = Σ(wixi) / Σwi
   - Business application examples needed
   - Calculation table format

3. **Variationskoeffizient (Coefficient of Variation)** - Present but needs more examples
   - More comparison problems
   - Business interpretation emphasis

4. **Häufigkeitsverteilung (Frequency Distribution)** - Needs more detail
   - Building frequency tables from raw data
   - Cumulative frequency calculations
   - Relative frequency interpretation

**Recommendation:** Add dedicated sections for these topics with HSG-style exercises.

---

##### 3. HYPOTHESIS TESTING FORMAT

###### ⚠️ Missing Critical Elements

**HSG Requires 5-Step Format:**

**Current Format (Incomplete):**
```markdown
**Hypotheses:**
- H₀: μ ≥ 500
- H₁: μ < 500

**Test statistic:**
$$t = \frac{495 - 500}{15/\sqrt{25}} = -1.67$$
```

**HSG Format Required:**
```markdown
**Step 1: Hypotheses**
- H₀: μ ≥ 500 (Nullhypothese: Behauptung ist korrekt)
- H₁: μ < 500 (Alternativhypothese: Produkte sind untergewichtig)
- Test: einseitig (one-tailed), links

**Step 2: Signifikanzniveau**
α = 0.05

**Step 3: Teststatistik**
$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} = \frac{495 - 500}{15/\sqrt{25}} = \frac{-5}{15/5} = \frac{-5}{3} = -1.67$$

df = n - 1 = 25 - 1 = 24

**Step 4: Kritischer Wert**
Aus t-Tabelle: t₀.₀₅,₂₄ = -1.711

**Step 5: Entscheidung**
t = -1.67 > -1.711 → H₀ wird nicht abgelehnt (Fail to reject H₀)

**Schlussfolgerung:**
Bei α = 0.05 gibt es keine ausreichenden Beweise, dass die Produkte untergewichtig sind.
```

**Recommendation:**
- Always use 5-step format
- Include German terminology
- Show critical value lookup process
- State decision rule explicitly
- Write conclusion in both languages

---

##### 4. REGRESSION ANALYSIS

###### ✅ Good Coverage, But Needs More Detail

**Current:** Good basic coverage of OLS, R², testing coefficients

**Missing:**
1. **Detailed calculation tables** matching Übungsblatt 6 format
2. **Alternative formula presentations** (HSG sometimes uses different but equivalent formulas)
3. **Interpretation emphasis** (business context)

**Example from Übungsblatt 6 Format Needed:**
```markdown
**Calculation Table:**

| Rep | xi | yi | xiyi | xi² | yi² | xi-x̄ | (xi-x̄)² | yi-ȳ | (yi-ȳ)² | (xi-x̄)(yi-ȳ) |
|-----|----|----|------|-----|-----|-------|---------|------|---------|--------------|
| 1   | 14 | 10 | 140  | 196 | 100 | -2    | 4       | -2.4 | 5.76    | 4.8         |
| 2   | 17 | 9  | 153  | 289 | 81  | 1     | 1       | -3.4 | 11.56   | -3.4        |
| ... |    |    |      |     |     |       |         |      |         |             |
| Σ   | 80 | 62 | 1068 | ... | ... |       | 88      |      | 93.2    | 76          |

**Step-by-step calculation:**
$$\bar{x} = \frac{80}{5} = 16$$
$$\bar{y} = \frac{62}{5} = 12.4$$
...
```

**Recommendation:** Add comprehensive regression calculation examples matching Übungsblatt 6 format.

---

##### 5. COMMON EXAM PITFALLS

###### ⚠️ Not Sufficiently Emphasized

**HSG Tests These Common Mistakes:**

1. **Sample vs. Population Notation**
   - Using s vs. σ incorrectly
   - Dividing by n vs. (n-1) confusion
   - **Current:** Mentioned but not emphasized enough

2. **Standardization Errors**
   - Forgetting √n in standard error
   - Wrong sign in z-score
   - **Current:** Mentioned in "Common Mistakes" but needs more practice

3. **Hypothesis Testing Errors**
   - Confusing H₀ and H₁ direction
   - One-tailed vs. two-tailed (α vs. α/2)
   - **Current:** Needs dedicated "trap questions"

4. **Table Lookup Errors**
   - Wrong degrees of freedom
   - Reading wrong row/column
   - **Current:** Missing - needs practice with actual table lookups

**Recommendation:**
- Add "Trap Question" sections to each module
- Create dedicated "Common Exam Mistakes" practice problems
- Include table lookup exercises with actual t-tables and z-tables
- Add "What's Wrong?" exercises where students identify errors

---

##### 6. BUSINESS CONTEXT & APPLICATIONS

###### ✅ Good, But Could Be Enhanced

**Strengths:**
- Uses CHF (Swiss Francs)
- Business examples (sales, employees, delivery)
- Consulting-style framing

**Enhancement Opportunities:**
- More Swiss/European company examples
- Consulting case study format
- Decision-making emphasis
- More "interpretation in business context" sections

**Example Enhancement:**
```markdown
**Business Interpretation:**
The 95% confidence interval (30.87, 39.13) minutes means:
- We are 95% confident the true mean commute time falls in this range
- **For management:** This suggests commute times are reasonable (under 40 min)
- **For HR:** Consider flexible hours if mean exceeds 35 minutes
- **For operations:** Plan for average 35 minutes with variability
```

---

##### 7. PRACTICE PROBLEM QUANTITY

###### ⚠️ Insufficient for HSG Exam Preparation

**HSG Expectation:** Students solve 50+ problems before exam

**Current:** ~3-4 problems per topic module

**Gap Analysis:**
- Module 02 (Descriptive): 3 problems → Need 8-10
- Module 04 (Probability): 3 problems → Need 8-10
- Module 09 (Hypothesis Testing): 2 problems → Need 10-12
- Module 12 (Regression): 3 problems → Need 8-10

**Recommendation:**
- Add "Additional Practice Problems" sections
- Create "Exam-Style Problems" with full HSG format
- Add "Past Exam Questions" section (if available)
- Include timed practice sets

---

##### 8. REFERENCE MATERIALS

###### ✅ Good, But Missing Critical Elements

**Strengths:**
- Formula glossary is comprehensive
- Distribution tables included
- Quick reference guides

**Missing:**
1. **German-English Terminology Dictionary** (CRITICAL)
2. **HSG-Style Formula Sheet** (as used in actual exams)
3. **Common Critical Values Quick Reference** (needs more detail)
4. **Decision Tree for Test Selection** (present but could be clearer)

**Recommendation:**
- Create comprehensive German-English glossary
- Add "HSG Exam Formula Sheet" matching actual exam format
- Include more critical values (t-table excerpts, z-table excerpts)
- Create visual decision flowchart for test selection

---

##### 9. SPECIFIC MODULE REVIEWS

###### Module 02: Descriptive Statistics

**Strengths:**
- Clear explanations
- Good examples
- Visual aids helpful

**Critical Gaps:**
- Missing MAD (Mittlere Absolute Abweichung) detailed treatment
- Missing weighted mean section
- Frequency distributions need more detail
- Exercises don't show full calculation tables

**Grade Impact:** ⚠️ Medium-High (these topics appear frequently in exams)

###### Module 04: Probability Fundamentals

**Strengths:**
- Clear probability rules
- Good Venn diagram usage
- Conditional probability well explained

**Gaps:**
- Missing German terminology (Wahrscheinlichkeit, Ereignis, etc.)
- Need more set operation problems (A∪B, A∩B, A\B)
- Missing "Quoten" (Odds) calculations
- Need more complex multi-step problems

**Grade Impact:** ⚠️ Medium (probability is foundational)

###### Module 07: Sampling Distributions

**Strengths:**
- CLT well explained
- Good visual demonstration
- Standard error clearly presented

**Gaps:**
- Missing detailed probability interval calculations
- Need more practice with σ/√n calculations
- Missing sample size determination from Übungsblatt 4

**Grade Impact:** ⚠️ Medium (important for later topics)

###### Module 09: Hypothesis Testing

**Strengths:**
- Framework is clear
- Error types explained well

**Critical Gaps:**
- 5-step format not consistently applied
- Missing German terminology
- Need more Type II error (β) calculations
- Missing "Entscheidungsregel" (decision rule) emphasis

**Grade Impact:** ⚠️ HIGH (hypothesis testing is major exam topic)

###### Module 12: Regression Analysis

**Strengths:**
- OLS well explained
- R² interpretation clear

**Gaps:**
- Calculation tables don't match Übungsblatt 6 format
- Missing detailed Σ calculations
- Need more interpretation emphasis
- Missing alternative formula presentations

**Grade Impact:** ⚠️ Medium-High (regression is major topic)

---

##### 10. PRIORITY RECOMMENDATIONS FOR HIGH GRADES

###### 🔴 CRITICAL (Must Fix for Exam Success)

1. **Add German Terminology Throughout**
   - Every key term needs German equivalent
   - Create German-English glossary
   - Add terminology recognition exercises

2. **Restructure All Exercises to Match HSG Format**
   - Detailed calculation tables with all columns
   - Step-by-step formula substitutions
   - Explicit "Formula → Substitute → Calculate → Answer" structure

3. **Enhance Hypothesis Testing Format**
   - Always use 5-step format
   - Include German terminology
   - Show critical value lookup process
   - Explicit decision rules

4. **Add Missing HSG Topics**
   - MAD (Mittlere Absolute Abweichung)
   - Weighted mean (Gewichtetes arithmetisches Mittel)
   - Enhanced frequency distributions
   - Odds (Quoten) calculations

###### 🟡 HIGH PRIORITY (Significantly Improves Grades)

5. **Increase Practice Problem Quantity**
   - 8-10 problems per major topic
   - Add "Exam-Style Problems" sections
   - Include timed practice sets

6. **Emphasize Common Exam Pitfalls**
   - Dedicated "Trap Questions" sections
   - "What's Wrong?" exercises
   - Table lookup practice

7. **Enhance Regression Format**
   - Match Übungsblatt 6 calculation table format
   - Show all Σ calculations explicitly
   - Add business interpretation emphasis

###### 🟢 MEDIUM PRIORITY (Nice to Have)

8. **Add More Business Context**
   - Swiss/European company examples
   - Consulting case study format
   - Decision-making interpretation sections

9. **Create HSG-Style Formula Sheet**
   - Match actual exam formula sheet format
   - Include German terms
   - Quick reference layout

10. **Add Visual Decision Trees**
    - Test selection flowchart
    - Distribution selection guide
    - When to use z vs. t

---

## `index.md` — Statistics Bootcamp

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** worked example, practice, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

## `00_start_here/index.md` — Start Here

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Welcome page | 8/10 | Clear purpose, good study tips |
| Prerequisites | 9/10 | Self-assessment quiz is excellent - caught my algebra gap |
| Study Path | 7/10 | Good time estimates, but "last-minute cram" is optimistic |

**Specific Suggestions:**
- Add: "What to bring to the exam" checklist (calculator, formula sheet, tables)
- Add: "Week before exam" schedule with daily focus areas

---

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 3/3
- **Already strong:** worked example, practice, mistakes, checklist, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 3

**What Works Well:**
- The welcome page clearly sets expectations as a "complementary" resource
- Prerequisites self-assessment is practical and includes actual math problems
- Study path guidance helps students prioritize

**Suggestions for Improvement:**
1. **Add time estimates per module**: We have limited study time before exams. Knowing "Module 02 takes ~90 minutes" would help planning.

2. **Include exam format description**: Mention that HSG exams are closed-book, calculation-heavy, and require showing all work in tables.

3. **Link to official materials**: Explicitly state "This does NOT replace Übungsblätter 1-6. Work through those first, use this for review."

---

## `00_start_here/prerequisites.md` — Prerequisites & Self-Assessment

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `00_start_here/study_path.md` — Suggested Study Path

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 2/3
- **Already strong:** practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `00_start_here/welcome.md` — Welcome to the Statistics Bootcamp

### Student 2

- **Helpfulness:** 5/5 | **HSG-support:** 3/3
- **Already strong:** LOs, worked example, practice, mistakes, checklist, takeaways, tables
- **Improve:**
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `01_foundations/index.md` — Module 01: Foundations

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Data types | 8/10 | Clear primary/secondary distinction |
| Scales (NOIR) | 8/10 | NOIR mnemonic is helpful |
| Practice problems | 6/10 | Need more classification exercises |

**Specific Suggestions:**
- Add: 15-20 quick classification exercises (multiple choice style)
- Add: Discussion of when interval data is treated as ratio (common exam trap)
- Add: Real HSG course examples (e.g., "In the company case study from lecture...")

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 4

**Rating: 7/10**
- Good basic explanations
- Clear calculation examples

**Improvements Needed:**
- Add business context: "Why does a consultant care about mean vs. median?"
- Include more financial examples (stock returns, salary data)
- Emphasize robust statistics for business data (often skewed)

## `01_foundations/data_types.md` — I know the different types of data and their characteristics

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `01_foundations/scales_of_measurement.md` — I can identify and distinguish scales of measurement

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, figures, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `02_descriptive_statistics/index.md` — Module 02: Descriptive Statistics

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Mean, median, mode | 8/10 | Good comparison table, clear when to use each |
| Variance & Std Dev | 7/10 | **Missing: MAD (Mean Absolute Deviation)** - this is in Übungsblatt 1! |
| Quartiles | 7/10 | Good, but box plot interpretation could be deeper |
| Skewness & Kurtosis | 7/10 | Good visuals, but formulas not shown in detail |

**Critical Missing Content:**
1. **Mean Absolute Deviation (MAD)** - Required in Übungsblatt 1
   - Add formula: MAD = (1/n) Σ|xᵢ - x̄|
   - Add worked example with calculation table

2. **Frequency Distribution Tables**
   - HSG heavily tests relative frequency f(xᵢ) and cumulative distribution F(xᵢ)
   - Add section on building frequency tables from raw data

3. **Weighted Mean**
   - Only mentioned briefly in formula glossary
   - Add dedicated section with grouped data example

**Specific Suggestions:**
- Add: Problems with grouped data (frequency tables)
- Add: More box plot interpretation exercises
- Add: Interquartile Range (IQR) calculation examples

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, practice, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 3

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

### Student 4

**Rating: 7/10**
- Good basic explanations
- Clear calculation examples

**Improvements Needed:**
- Add business context: "Why does a consultant care about mean vs. median?"
- Include more financial examples (stock returns, salary data)
- Emphasize robust statistics for business data (often skewed)

## `02_descriptive_statistics/mean_median_mode.md` — I can calculate and interpret the mean, median, and mode

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `02_descriptive_statistics/quartiles_boxplots.md` — I can interpret quartiles and box plots

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `02_descriptive_statistics/skewness_kurtosis.md` — I can identify skewness and kurtosis

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `02_descriptive_statistics/variance_stddev.md` — I can calculate variance and standard deviation

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

### Student 5

- ✅ Good: Calculation table present
- ❌ Fix: Add German terms, show more substitution steps
- ❌ Add: MAD section, weighted mean section

## `03_correlation_covariance/index.md` — Module 03: Correlation & Covariance

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Covariance | 7/10 | Good formula, but needs more calculation practice |
| Correlation | 7/10 | Interpretation is clear |
| Correlation ≠ Causation | 8/10 | Excellent real-world examples |

**Specific Suggestions:**
- Add: Complete calculation table example (like Übungsblatt 6 style)
- Add: More problems computing r from raw data
- Add: Discussion of Spearman rank correlation (if covered in course)

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 4

**Rating: 6/10**
- Technically accurate
- Good visualizations

**Improvements Needed:**
- Add causation vs. correlation business examples
- Include decision trees for probability calculations
- Connect to expected value in business decisions

## `03_correlation_covariance/correlation.md` — I can calculate and interpret correlation

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `03_correlation_covariance/correlation_causation.md` — I understand why correlation does not imply causation

### Student 2

- **Helpfulness:** 5/5 | **HSG-support:** 3/3
- **Already strong:** LOs, worked example, practice, mistakes, checklist, takeaways, figures, tables
- **Improve:**
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `03_correlation_covariance/covariance.md` — I can calculate and interpret covariance

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `04_probability_fundamentals/index.md` — Module 04: Probability Fundamentals

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Basic rules | 8/10 | Clear formulas, good Venn diagrams |
| Conditional probability | 8/10 | Excellent contingency table example |
| Bayes' theorem | 9/10 | Tree diagram method is very helpful |
| Counting | Not reviewed | - |
| Expected value | Not reviewed | - |

**Specific Suggestions:**
- Add: More Venn diagram problems (Übungsblatt 2 style)
- Add: Odds ratio calculations (Quoten) - this is tested!
- Add: Set notation problems (Mengenoperationen)
- Add: More Bayes problems with tree diagrams

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, practice, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 3

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

### Student 4

**Rating: 6/10**
- Technically accurate
- Good visualizations

**Improvements Needed:**
- Add causation vs. correlation business examples
- Include decision trees for probability calculations
- Connect to expected value in business decisions

## `04_probability_fundamentals/bayes_theorem.md` — I can apply Bayes' theorem

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `04_probability_fundamentals/conditional_probability.md` — I can calculate conditional probabilities

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `04_probability_fundamentals/counting.md` — I can use counting techniques

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add a “permutations vs combinations” decision box + 3 drills with one-line reasoning.

## `04_probability_fundamentals/expected_value.md` — I can calculate expected value and variance

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `04_probability_fundamentals/probability_rules.md` — I know the basic rules of probability

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add 2 Venn-diagram drills + one “translate words → set notation” exercise (HSG-style).

## `05_discrete_distributions/index.md` — Module 05: Discrete Distributions

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Binomial | 8/10 | Good BINS mnemonic, clear formula |
| Poisson | Not reviewed | - |
| Hypergeometric | Not reviewed | - |

**Specific Suggestions:**
- Add: More problems computing P(X ≥ k) using complement
- Add: Normal approximation to binomial (when np > 5, n(1-p) > 5)
- Add: "Rule of thumb" for choosing between binomial/hypergeometric

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, practice, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 4

**Rating: 7/10**
- Clear distribution explanations
- Good practical examples

**Improvements Needed:**
- Add business applications: Quality control (normal), customer arrivals (Poisson)
- Include distribution selection flowchart for business scenarios
- Emphasize when to use each distribution in practice

## `05_discrete_distributions/binomial.md` — I can apply the Binomial distribution

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `05_discrete_distributions/choosing_distribution.md` — I can choose the right discrete distribution

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, figures, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add a keyword trigger table (fixed n / rare events / without replacement / arrivals) + 4 quick selection drills.

## `05_discrete_distributions/discrete_problems.md` — I can work with discrete distribution problems

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, practice, takeaways, tables
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `05_discrete_distributions/hypergeometric.md` — I can apply the Hypergeometric distribution

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `05_discrete_distributions/poisson.md` — I can apply the Poisson distribution

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `06_continuous_distributions/index.md` — Module 06: Continuous Distributions

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Normal distribution | 8/10 | 68-95-99.7 rule well explained |
| Z-scores | Not reviewed | - |
| Exponential | Not reviewed | - |

**Specific Suggestions:**
- Add: More z-table lookup practice (forward AND reverse)
- Add: Problems like "find x such that P(X < x) = 0.95"
- Add: Standard normal table reading exercises

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, practice, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 4

**Rating: 7/10**
- Clear distribution explanations
- Good practical examples

**Improvements Needed:**
- Add business applications: Quality control (normal), customer arrivals (Poisson)
- Include distribution selection flowchart for business scenarios
- Emphasize when to use each distribution in practice

## `06_continuous_distributions/exponential.md` — I can apply the Exponential distribution

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `06_continuous_distributions/normal_distribution.md` — I can work with the Normal distribution

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `06_continuous_distributions/normal_probabilities.md` — I can find Normal probabilities

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add a worked example that explicitly shows Z-table row/column lookup + symmetry/complement shortcuts.

## `06_continuous_distributions/z_scores.md` — I can calculate and interpret z-scores

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `07_sampling_distributions/index.md` — Module 07: Sampling Distributions

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| CLT | 7/10 | Concept explained, but needs more worked examples |
| Standard Error | 7/10 | Formula clear, but practice is limited |

**Specific Suggestions:**
- Add: More problems applying σ/√n
- Add: Finite population correction factor (if covered)
- Add: Visual comparison of sampling distributions with different n

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 3

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

### Student 4

**Rating: 6/10**
- Good technical content
- Clear CI explanations

**Improvements Needed:**
- Add business context for sample size decisions
- Include cost-benefit analysis for larger samples
- Connect to market research applications

## `07_sampling_distributions/central_limit_theorem.md` — I can apply the Central Limit Theorem

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, figures, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `07_sampling_distributions/sample_size_effect.md` — I understand the effect of sample size

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, figures, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `07_sampling_distributions/sampling_distributions.md` — I understand sampling distributions

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, figures, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `07_sampling_distributions/standard_error.md` — I can calculate standard error

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add a strict “SD vs SE vs σ/√n” comparison table + a 3-question mini-quiz (very common exam trap).

## `08_estimation_confidence_intervals/index.md` — Module 08: Estimation & Confidence Intervals

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Point vs interval | 7/10 | Conceptually clear |
| CI for mean | 8/10 | Good z vs t guidance |
| CI for proportion | Not reviewed | - |
| Sample size | Not reviewed | - |

**Specific Suggestions:**
- Add: More emphasis on margin of error calculations
- Add: Sample size determination for a given margin of error (HEAVILY TESTED)
- Add: CI interpretation exercises (common exam questions)

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, practice, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 3

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

### Student 4

**Rating: 6/10**
- Good technical content
- Clear CI explanations

**Improvements Needed:**
- Add business context for sample size decisions
- Include cost-benefit analysis for larger samples
- Connect to market research applications

## `08_estimation_confidence_intervals/ci_mean.md` — I can construct CI for the mean

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 2/3
- **Already strong:** LOs, worked example, practice, mistakes, takeaways, tables
- **Improve:**
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `08_estimation_confidence_intervals/ci_proportion.md` — I can construct CI for proportions

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `08_estimation_confidence_intervals/point_vs_interval.md` — I understand point vs interval estimation

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `08_estimation_confidence_intervals/sample_size.md` — I can determine required sample size

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `09_hypothesis_testing_basics/index.md` — Module 09: Hypothesis Testing Basics

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Stating hypotheses | 7/10 | Correct but needs more examples |
| Error types | 7/10 | Type I/II explained, but power discussion is brief |
| P-values | 7/10 | Good interpretation warnings |
| Testing framework | **5/10** | **Too brief - this is the most important module!** |

**Critical Issues:**
1. **testing_framework.md is only 153 lines** - this should be the longest page!
2. Missing: Explicit template for five-step hypothesis test
3. Missing: More one-tailed vs two-tailed examples
4. Missing: β (Type II error) calculations (TESTED in Übungsblatt 5!)

**Specific Suggestions:**
- Expand this module significantly (should be 2-3x current length)
- Add: Power analysis and β calculation examples
- Add: Relationship between α, β, and sample size
- Add: Decision rule diagrams (rejection regions)

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 2/3
- **Already strong:** LOs, practice, checklist, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 4

**Rating: 5/10** (Most Critical for Exam)
- Framework is sound
- Good error type explanations

**Improvements Needed:**
- **URGENT:** Add business decision-making context
- Include power analysis for business implications
- Add examples from consulting case studies
- Emphasize interpretation over just calculations

## `09_hypothesis_testing_basics/error_types.md` — I understand Type I and Type II errors

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `09_hypothesis_testing_basics/p_values.md` — I can interpret p-values

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add 3 interpretation sentences (correct vs incorrect) + one table/picture for p-value area.

## `09_hypothesis_testing_basics/stating_hypotheses.md` — I can state hypotheses correctly

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `09_hypothesis_testing_basics/testing_framework.md` — I understand the testing framework

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, checklist, takeaways
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add a single reusable “5-step test template” that every later test page links back to.

### Student 5

- ✅ Good: Framework explained
- ❌ Fix: Always use 5-step format with German terms
- ❌ Add: More examples with full format
- ❌ Add: Decision rule emphasis

## `10_one_sample_tests/index.md` — Module 10: One-Sample Tests

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Z-test for mean | 7/10 | Correct but needs more practice |
| T-test for mean | 7/10 | Good comparison with z-test |
| Z-test for proportion | Not reviewed | - |

**Specific Suggestions:**
- Add: More complete five-step examples
- Add: Problems where you must decide z vs t
- Add: One-tailed examples (left AND right)

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 4

**Rating: 5/10** (Most Critical for Exam)
- Framework is sound
- Good error type explanations

**Improvements Needed:**
- **URGENT:** Add business decision-making context
- Include power analysis for business implications
- Add examples from consulting case studies
- Emphasize interpretation over just calculations

## `10_one_sample_tests/t_test_mean.md` — I can perform a t-test for the mean

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 0/3
- **Already strong:** LOs, worked example, practice, takeaways
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add an “Assumptions & when t≈z” box + “df and α/2” trap examples.

## `10_one_sample_tests/z_test_mean.md` — I can perform a z-test for the mean

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 0/3
- **Already strong:** LOs, worked example, practice, takeaways
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `10_one_sample_tests/z_test_proportion.md` — I can perform a z-test for proportions

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 0/3
- **Already strong:** LOs, worked example, practice, takeaways
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `11_two_sample_tests/index.md` — Module 11: Two-Sample Tests

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Independent t-test | 7/10 | Pooled variance formula shown |
| Paired t-test | Not reviewed | - |
| F-test | Not reviewed | - |
| Two-proportion | Not reviewed | - |

**Specific Suggestions:**
- Add: More emphasis on when to use paired vs independent
- Add: F-test for comparing variances (pre-test for t-test)
- Add: Examples deciding whether variances are equal

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 4

**Rating: 5/10** (Most Critical for Exam)
- Framework is sound
- Good error type explanations

**Improvements Needed:**
- **URGENT:** Add business decision-making context
- Include power analysis for business implications
- Add examples from consulting case studies
- Emphasize interpretation over just calculations

## `11_two_sample_tests/f_test_variance.md` — I can compare variances (F-test)

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 0/3
- **Already strong:** LOs, worked example, practice, takeaways
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add two-tailed handling via reciprocal (1/F) and make table lookup steps explicit.

## `11_two_sample_tests/independent_t_test.md` — I can compare two independent means

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 0/3
- **Already strong:** LOs, worked example, practice, takeaways
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `11_two_sample_tests/paired_t_test.md` — I can compare paired samples

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `11_two_sample_tests/two_proportion_test.md` — I can compare two proportions

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 0/3
- **Already strong:** LOs, worked example, practice, takeaways
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `12_regression_analysis/index.md` — Module 12: Regression Analysis

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Fitting regression | 6/10 | **Too brief for exam importance!** |
| R-squared | Not reviewed | - |
| Assumptions | Not reviewed | - |
| Testing coefficients | Not reviewed | - |

**Critical Issues:**
1. **fitting_regression.md is only 139 lines** - Übungsblatt 6 is 21 pages on regression!
2. Missing: Complete calculation table (Σx, Σy, Σxy, Σx², etc.)
3. Missing: Predicted values and residuals calculation
4. Missing: Interpretation of coefficients

**Specific Suggestions:**
- Add: Full HSG-style regression calculation table
- Add: Standard error of estimate calculation
- Add: Confidence intervals for regression coefficients
- Add: Residual analysis
- Double the content in this module

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, practice, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 3

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

### Student 4

**Rating: 6/10**
- Good technical explanations
- Clear assumption discussions

**Improvements Needed:**
- Add business regression examples (sales forecasting, pricing)
- Include model interpretation for managers
- Connect to Excel/real tools we actually use

---

## 4. Priority Recommendations for Maximum Grade Impact

### Immediate (High Impact, Low Effort)
1. **Add Business Context Headers**
   ```
   Business Context: A consulting firm needs to determine if a new training program improves employee productivity by more than 5%.
   Statistical Question: Is μ > 5%?
   ```

2. **Include German Terminology**
   Add sidebars: "German: Mittelwert (Mean), Varianz (Variance)"

3. **Add Decision-Making Framework**
   After each test: "Business Decision: [Accept/Reject] the program"

### Medium-term (High Impact, Medium Effort)
1. **Restructure Exercises to HSG Format**
   - Use "Aufgabe 1a), 1b), 1c)" structure
   - Include exact calculation table formats
   - Add German column headers

2. **Add Business Case Studies**
   - Replace generic examples with Swiss company scenarios
   - Include consulting-style interpretations

3. **Include Past Exam Patterns**
   - Add "Common Exam Questions" sections
   - Include trick questions HSG professors use

### Long-term (High Impact, High Effort)
1. **Create Business Decision Trees**
   - Flowcharts for choosing statistical methods
   - Business context for method selection

2. **Add Video/Interactive Elements**
   - Business case walkthroughs
   - Interactive calculation builders

3. **Integrate with Excel/Google Sheets**
   - Practical tools we actually use in business

---

## 5. Expected Grade Impact

**Current Bootcamp:** Supports 4.0-4.5 grade
- Good for basic understanding
- Missing business context and exam precision

**With Recommended Improvements:** Could support 5.5-6.0 grade
- Business-relevant examples improve application questions
- HSG-aligned format improves calculation accuracy
- Decision-making framework improves interpretation questions

**Key Insight:** HSG exams test both technical calculation skills AND business judgment. The bootcamp currently excels at the former but neglects the latter.

---

## 6. Final Recommendations

**For Bootcamp Creators:**
1. Partner with HSG alumni for business examples
2. Analyze actual Übungsblätter more deeply
3. Include German instructors for terminology
4. Focus on business decision-making applications

**For Fellow Students:**
- Use this bootcamp for technical practice
- Supplement with business case studies
- Practice with official Übungsblätter
- Focus on interpretation, not just calculations

**Overall Assessment:** With the recommended improvements, this could become the definitive HSG statistics preparation resource. Currently it's a good technical supplement but needs significant business context enhancement to maximize learning success and exam performance.

---

*This review reflects the perspective of a typical HSG BBA student who wants to excel in statistics while building practical business skills for a consulting/finance career.*

## `12_regression_analysis/fitting_regression.md` — I can fit a linear regression model

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

### Student 5

- ✅ Good: OLS explained
- ❌ Fix: Match Übungsblatt 6 table format
- ❌ Add: More detailed Σ calculations
- ❌ Add: Business interpretation sections

## `12_regression_analysis/r_squared.md` — I can interpret R-squared

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `12_regression_analysis/regression_assumptions.md` — I understand regression assumptions

### Student 2

- **Helpfulness:** 2/5 | **HSG-support:** 1/3
- **Already strong:** LOs, takeaways, figures, tables
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add **2–3 practice problems** (easy/medium/exam-style) with solutions hidden/toggled.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `12_regression_analysis/testing_coefficients.md` — I can test regression coefficients

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `13_advanced_topics/index.md` — Module 13: Advanced Topics

### Student 1

| Aspect | Rating | Comments |
|--------|--------|----------|
| Chi-square | Not reviewed | - |
| ANOVA | Not reviewed | - |
| Multiple regression | Not reviewed | - |
| Dummy variables | Not reviewed | - |

**Note:** These topics may be less weighted on the exam, but verify with syllabus.

---

## Reference Materials Review

### Formula Glossary (formula_glossary.md)

**Rating: 9/10** - Excellent!

**Strengths:**
- Comprehensive coverage
- Well-organized by topic
- Includes quick critical values

**Suggestions:**
- Add: MAD formula (currently missing)
- Add: Alternative computational formulas
- Add: German term equivalents

---

### Common Mistakes (common_mistakes.md)

**Rating: 9/10** - The best page in the bootcamp!

**Strengths:**
- Covers exactly what students get wrong
- Practical and actionable
- The checklist at the end is gold

**Suggestions:**
- Add: More exam-specific tips (time management, partial credit)
- Add: Common calculator errors

---

### Which Test (which_test.md)

**Rating: 8/10** - Very helpful

**Strengths:**
- Clear decision tree structure
- Good scenario examples

**Suggestions:**
- Add: Flowchart visual (placeholder exists but image may be missing)
- Add: Summary table on one page (printable for exam)

---

## Exercises Review

| Exercise | Topics | Problems | Rating | Issue |
|----------|--------|----------|--------|-------|
| Exercise 1 | Descriptive Stats | 3 | 5/10 | Need 5-6 more problems, MAD missing |
| Exercise 2 | Probability | Not reviewed | - | - |
| Exercise 3a/3b | Distributions | Not reviewed | - | - |
| Exercise 4 | Sampling/CI | Not reviewed | - | - |
| Exercise 5 | Hypothesis Testing | 3 | 5/10 | Need 5+ more, no β calculations |
| Exercise 6 | Regression | Not reviewed | - | - |

**Critical Issue:** The exercises are too short. HSG Übungsblätter have 7-8 multi-part problems each. Students need 3-4x more practice problems.

**Recommendation:** Either:
1. Expand each exercise file to 8-10 problems, OR
2. Add "Additional Practice" files with more problems

---

## Priority Recommendations

### 🔴 HIGH PRIORITY (Do First)

1. **Expand hypothesis testing content (Module 09)**
   - Add explicit five-step template
   - Add β (Type II error) calculations
   - Add power analysis examples
   - Triple the practice problems

2. **Add MAD (Mean Absolute Deviation) to Module 02**
   - This is tested in Übungsblatt 1 and currently missing

3. **Expand regression content (Module 12)**
   - Add complete HSG-style calculation table
   - Add more interpretation examples
   - Double the practice problems

4. **Triple the number of practice problems**
   - Each exercise should have 8-10 problems minimum
   - Include multi-part problems (a, b, c, d format)

### 🟡 MEDIUM PRIORITY (Do Second)

5. **Add German terminology glossary**
   - Essential for exam preparation
   - Include at minimum: 50 key terms

6. **Add frequency distribution section (Module 02)**
   - Relative frequency, cumulative frequency
   - Building tables from raw data

7. **Add sample size determination examples (Module 08)**
   - Heavily tested topic
   - Include both for mean and proportion

8. **Add odds ratio (Quoten) calculations (Module 04)**
   - Part of Übungsblatt 2

### 🟢 LOWER PRIORITY (Nice to Have)

9. **Add computational formula alternatives**
   - Faster for exam calculations

10. **Add Z-table reading exercises (Module 06)**
    - Practice forward and reverse lookups

11. **Add printable summary sheets**
    - One-page formula reference
    - One-page test selection guide

12. **Add timed practice sets**
    - Simulate exam conditions
    - Help with time management

---

## Final Assessment

### What I Would Tell a Fellow HSG Student

"This bootcamp is a good starting point for understanding concepts, but **don't rely on it alone for exam prep**. You'll need to:

1. Do ALL the official Übungsblätter (the bootcamp exercises are too few)
2. Learn the German terms separately
3. Practice the five-step hypothesis testing format more
4. Build calculation tables by hand repeatedly until it's automatic

The **formula glossary** and **common mistakes** pages are excellent - print them out! But the practice problems won't give you enough repetition for exam speed."

### What Would Make This a 9/10 Bootcamp

1. Add 50+ more practice problems across all exercises
2. Expand hypothesis testing and regression significantly  
3. Add German terminology throughout
4. Add MAD and frequency distribution content
5. Add β (power) calculations

---

## Appendix: Missing Content Checklist

Content that appears in HSG Übungsblätter but is missing or insufficient in the bootcamp:

- [ ] Mean Absolute Deviation (MAD)
- [ ] Frequency distribution tables (relative & cumulative)
- [ ] Weighted mean with grouped data
- [ ] Odds ratio (Quoten)
- [ ] Set operations with Venn diagrams (Mengenoperationen)
- [ ] Type II error (β) calculations
- [ ] Power of a test (1 - β)
- [ ] Complete regression calculation tables
- [ ] Standard error of regression
- [ ] German statistical terminology

---

*Review completed by: HSG BBA Student (simulated perspective)*  
*Based on: HSG_BBA_Student_Profile.txt and Übungsblätter 1-6 content requirements*

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 0/3
- **Already strong:** LOs, practice
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 4

**Rating: 6/10**
- Good technical explanations
- Clear assumption discussions

**Improvements Needed:**
- Add business regression examples (sales forecasting, pricing)
- Include model interpretation for managers
- Connect to Excel/real tools we actually use

---

## 4. Priority Recommendations for Maximum Grade Impact

### Immediate (High Impact, Low Effort)
1. **Add Business Context Headers**
   ```
   Business Context: A consulting firm needs to determine if a new training program improves employee productivity by more than 5%.
   Statistical Question: Is μ > 5%?
   ```

2. **Include German Terminology**
   Add sidebars: "German: Mittelwert (Mean), Varianz (Variance)"

3. **Add Decision-Making Framework**
   After each test: "Business Decision: [Accept/Reject] the program"

### Medium-term (High Impact, Medium Effort)
1. **Restructure Exercises to HSG Format**
   - Use "Aufgabe 1a), 1b), 1c)" structure
   - Include exact calculation table formats
   - Add German column headers

2. **Add Business Case Studies**
   - Replace generic examples with Swiss company scenarios
   - Include consulting-style interpretations

3. **Include Past Exam Patterns**
   - Add "Common Exam Questions" sections
   - Include trick questions HSG professors use

### Long-term (High Impact, High Effort)
1. **Create Business Decision Trees**
   - Flowcharts for choosing statistical methods
   - Business context for method selection

2. **Add Video/Interactive Elements**
   - Business case walkthroughs
   - Interactive calculation builders

3. **Integrate with Excel/Google Sheets**
   - Practical tools we actually use in business

---

## 5. Expected Grade Impact

**Current Bootcamp:** Supports 4.0-4.5 grade
- Good for basic understanding
- Missing business context and exam precision

**With Recommended Improvements:** Could support 5.5-6.0 grade
- Business-relevant examples improve application questions
- HSG-aligned format improves calculation accuracy
- Decision-making framework improves interpretation questions

**Key Insight:** HSG exams test both technical calculation skills AND business judgment. The bootcamp currently excels at the former but neglects the latter.

---

## 6. Final Recommendations

**For Bootcamp Creators:**
1. Partner with HSG alumni for business examples
2. Analyze actual Übungsblätter more deeply
3. Include German instructors for terminology
4. Focus on business decision-making applications

**For Fellow Students:**
- Use this bootcamp for technical practice
- Supplement with business case studies
- Practice with official Übungsblätter
- Focus on interpretation, not just calculations

**Overall Assessment:** With the recommended improvements, this could become the definitive HSG statistics preparation resource. Currently it's a good technical supplement but needs significant business context enhancement to maximize learning success and exam performance.

---

*This review reflects the perspective of a typical HSG BBA student who wants to excel in statistics while building practical business skills for a consulting/finance career.*

## `13_advanced_topics/anova.md` — I can perform ANOVA

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, takeaways, tables
- **Improve:**
  - Add **2–3 practice problems** (easy/medium/exam-style) with solutions hidden/toggled.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `13_advanced_topics/chi_square.md` — I can conduct chi-square tests

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 1/3
- **Already strong:** LOs, worked example, practice, takeaways, tables
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `13_advanced_topics/dummy_variables.md` — I understand dummy variables

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 0/3
- **Already strong:** LOs, worked example, takeaways
- **Improve:**
  - Add **2–3 practice problems** (easy/medium/exam-style) with solutions hidden/toggled.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
  - Add dummy-variable trap (k categories → k−1 dummies) + reference-category switch drill.

## `13_advanced_topics/multiple_regression.md` — I understand multiple regression

### Student 2

- **Helpfulness:** 4/5 | **HSG-support:** 0/3
- **Already strong:** LOs, worked example, practice, takeaways
- **Improve:**
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `reference/index.md` — Reference

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** mistakes
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 3

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

## `reference/common_mistakes.md` — Common Mistakes to Avoid

### Student 1

**Rating: 9/10** - The best page in the bootcamp!

**Strengths:**
- Covers exactly what students get wrong
- Practical and actionable
- The checklist at the end is gold

**Suggestions:**
- Add: More exam-specific tips (time management, partial credit)
- Add: Common calculator errors

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 3/3
- **Already strong:** worked example, mistakes, checklist, tables
- **Improve:**
  - Add **2–3 practice problems** (easy/medium/exam-style) with solutions hidden/toggled.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `reference/distribution_table.md` — Distribution Summary Table

### Student 2

- **Helpfulness:** 2/5 | **HSG-support:** 1/3
- **Already strong:** figures, tables
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add **2–3 practice problems** (easy/medium/exam-style) with solutions hidden/toggled.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.

## `reference/formula_glossary.md` — Formula Glossary

### Student 1

**Rating: 9/10** - Excellent!

**Strengths:**
- Comprehensive coverage
- Well-organized by topic
- Includes quick critical values

**Suggestions:**
- Add: MAD formula (currently missing)
- Add: Alternative computational formulas
- Add: German term equivalents

---

### Student 2

- **Helpfulness:** 2/5 | **HSG-support:** 1/3
- **Already strong:** tables
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add **2–3 practice problems** (easy/medium/exam-style) with solutions hidden/toggled.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.

### Student 5

- ✅ Good: Comprehensive formulas
- ❌ Add: German terminology column
- ❌ Add: HSG exam formula sheet format
- ❌ Add: Common critical values table

---

## 12. LEARNING EFFECTIVENESS ASSESSMENT

### For Different Learning Styles

**Visual Learners:** ⭐⭐⭐⭐ (4/5)
- Good visual aids
- Could use more diagrams for decision trees

**Auditory Learners:** ⭐⭐⭐ (3/5)
- Text-heavy, could benefit from audio explanations
- Consider adding video links

**Kinesthetic Learners:** ⭐⭐⭐ (3/5)
- Good practice problems
- Need more hands-on calculation practice

**Reading/Writing Learners:** ⭐⭐⭐⭐⭐ (5/5)
- Excellent written explanations
- Well-structured content

### For Exam Preparation

**Conceptual Understanding:** ⭐⭐⭐⭐ (4/5)
- Clear explanations
- Good examples

**Formula Application:** ⭐⭐⭐ (3/5)
- Formulas present but need more substitution practice
- Missing step-by-step emphasis

**Problem-Solving Skills:** ⭐⭐⭐ (3/5)
- Problems present but format doesn't match exam
- Need more quantity

**Exam Readiness:** ⭐⭐⭐ (3/5)
- Good foundation but gaps in format alignment
- Missing German terminology is critical issue

---

## 13. FINAL RECOMMENDATIONS SUMMARY

### To Achieve High Grades (5.5-6.0)

**Must Do:**
1. Add German terminology throughout
2. Restructure exercises to match HSG format
3. Add missing topics (MAD, weighted mean, etc.)
4. Enhance hypothesis testing format
5. Increase practice problem quantity

**Should Do:**
6. Emphasize common exam pitfalls
7. Enhance regression format
8. Add business interpretation sections
9. Create HSG-style formula sheet

**Nice to Have:**
10. More visual decision trees
11. Additional business context examples
12. Timed practice sets

### Estimated Impact on Grade

**Current State:** Would likely achieve **4.5-5.0** (good but not excellent)

**After Critical Fixes:** Could achieve **5.5-6.0** (excellent)

**Key Differentiator:** Format alignment and German terminology are what separate good from excellent grades at HSG.

---

## 14. CONCLUSION

This bootcamp provides a **solid foundation** for statistics learning. The content is clear, well-organized, and covers the necessary topics. However, to achieve **high grades** at HSG, students need:

1. **Format alignment** with actual Übungsblatt structure
2. **German terminology** integration
3. **More detailed calculation steps** matching exam expectations
4. **Additional practice problems** in HSG format
5. **Emphasis on common exam pitfalls**

**Overall:** Good learning resource, but needs refinement to match HSG exam format exactly.

**Recommendation:** Use this bootcamp as a foundation, but supplement with:
- Actual HSG Übungsblätter for format practice
- German terminology flashcards
- Additional calculation table practice
- Past exam questions (if available)

---

**Review Completed By:** HSG BBA Student  
**Target Grade:** 5.5-6.0  
**Confidence Level:** High (based on actual Übungsblatt analysis)

---

## APPENDIX: Quick Reference - What HSG Expects

### Exercise Format Checklist
- [ ] Detailed calculation table with all columns
- [ ] Formula shown symbolically
- [ ] Values substituted explicitly
- [ ] Intermediate calculations shown
- [ ] Final answer clearly stated
- [ ] German terminology used
- [ ] Step numbers labeled (Step 1, Step 2, etc.)

### Hypothesis Test Checklist
- [ ] Step 1: Hypotheses (H₀, H₁) with German terms
- [ ] Step 2: Significance level (α)
- [ ] Step 3: Test statistic with full calculation
- [ ] Step 4: Critical value from table (show lookup)
- [ ] Step 5: Decision and conclusion (in German + English)

### Common Exam Mistakes to Practice
- [ ] Sample vs. population (n vs. n-1)
- [ ] Standard error (σ vs. σ/√n)
- [ ] One-tailed vs. two-tailed (α vs. α/2)
- [ ] Table lookup (correct df, correct α)
- [ ] Hypothesis direction (H₀ vs. H₁)

---

*End of Review*

## `reference/statistical_tables.md` — Statistical Tables

### Student 2

- **Helpfulness:** 2/5 | **HSG-support:** 2/3
- **Already strong:** worked example, mistakes, tables
- **Improve:**
  - Add **2–3 practice problems** (easy/medium/exam-style) with solutions hidden/toggled.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `reference/which_test.md` — Which Statistical Test Should I Use?

### Student 1

**Rating: 8/10** - Very helpful

**Strengths:**
- Clear decision tree structure
- Good scenario examples

**Suggestions:**
- Add: Flowchart visual (placeholder exists but image may be missing)
- Add: Summary table on one page (printable for exam)

---

## Exercises Review

| Exercise | Topics | Problems | Rating | Issue |
|----------|--------|----------|--------|-------|
| Exercise 1 | Descriptive Stats | 3 | 5/10 | Need 5-6 more problems, MAD missing |
| Exercise 2 | Probability | Not reviewed | - | - |
| Exercise 3a/3b | Distributions | Not reviewed | - | - |
| Exercise 4 | Sampling/CI | Not reviewed | - | - |
| Exercise 5 | Hypothesis Testing | 3 | 5/10 | Need 5+ more, no β calculations |
| Exercise 6 | Regression | Not reviewed | - | - |

**Critical Issue:** The exercises are too short. HSG Übungsblätter have 7-8 multi-part problems each. Students need 3-4x more practice problems.

**Recommendation:** Either:
1. Expand each exercise file to 8-10 problems, OR
2. Add "Additional Practice" files with more problems

---

## Priority Recommendations

### 🔴 HIGH PRIORITY (Do First)

1. **Expand hypothesis testing content (Module 09)**
   - Add explicit five-step template
   - Add β (Type II error) calculations
   - Add power analysis examples
   - Triple the practice problems

2. **Add MAD (Mean Absolute Deviation) to Module 02**
   - This is tested in Übungsblatt 1 and currently missing

3. **Expand regression content (Module 12)**
   - Add complete HSG-style calculation table
   - Add more interpretation examples
   - Double the practice problems

4. **Triple the number of practice problems**
   - Each exercise should have 8-10 problems minimum
   - Include multi-part problems (a, b, c, d format)

### 🟡 MEDIUM PRIORITY (Do Second)

5. **Add German terminology glossary**
   - Essential for exam preparation
   - Include at minimum: 50 key terms

6. **Add frequency distribution section (Module 02)**
   - Relative frequency, cumulative frequency
   - Building tables from raw data

7. **Add sample size determination examples (Module 08)**
   - Heavily tested topic
   - Include both for mean and proportion

8. **Add odds ratio (Quoten) calculations (Module 04)**
   - Part of Übungsblatt 2

### 🟢 LOWER PRIORITY (Nice to Have)

9. **Add computational formula alternatives**
   - Faster for exam calculations

10. **Add Z-table reading exercises (Module 06)**
    - Practice forward and reverse lookups

11. **Add printable summary sheets**
    - One-page formula reference
    - One-page test selection guide

12. **Add timed practice sets**
    - Simulate exam conditions
    - Help with time management

---

## Final Assessment

### What I Would Tell a Fellow HSG Student

"This bootcamp is a good starting point for understanding concepts, but **don't rely on it alone for exam prep**. You'll need to:

1. Do ALL the official Übungsblätter (the bootcamp exercises are too few)
2. Learn the German terms separately
3. Practice the five-step hypothesis testing format more
4. Build calculation tables by hand repeatedly until it's automatic

The **formula glossary** and **common mistakes** pages are excellent - print them out! But the practice problems won't give you enough repetition for exam speed."

### What Would Make This a 9/10 Bootcamp

1. Add 50+ more practice problems across all exercises
2. Expand hypothesis testing and regression significantly  
3. Add German terminology throughout
4. Add MAD and frequency distribution content
5. Add β (power) calculations

---

## Appendix: Missing Content Checklist

Content that appears in HSG Übungsblätter but is missing or insufficient in the bootcamp:

- [ ] Mean Absolute Deviation (MAD)
- [ ] Frequency distribution tables (relative & cumulative)
- [ ] Weighted mean with grouped data
- [ ] Odds ratio (Quoten)
- [ ] Set operations with Venn diagrams (Mengenoperationen)
- [ ] Type II error (β) calculations
- [ ] Power of a test (1 - β)
- [ ] Complete regression calculation tables
- [ ] Standard error of regression
- [ ] German statistical terminology

---

*Review completed by: HSG BBA Student (simulated perspective)*  
*Based on: HSG_BBA_Student_Profile.txt and Übungsblätter 1-6 content requirements*

### Student 2

- **Helpfulness:** 2/5 | **HSG-support:** 2/3
- **Already strong:** worked example, checklist, figures, tables
- **Improve:**
  - Add **2–3 practice problems** (easy/medium/exam-style) with solutions hidden/toggled.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `exercises/index.md` — Exercises

### Student 1

| Exercise | Topics | Problems | Rating | Issue |
|----------|--------|----------|--------|-------|
| Exercise 1 | Descriptive Stats | 3 | 5/10 | Need 5-6 more problems, MAD missing |
| Exercise 2 | Probability | Not reviewed | - | - |
| Exercise 3a/3b | Distributions | Not reviewed | - | - |
| Exercise 4 | Sampling/CI | Not reviewed | - | - |
| Exercise 5 | Hypothesis Testing | 3 | 5/10 | Need 5+ more, no β calculations |
| Exercise 6 | Regression | Not reviewed | - | - |

**Critical Issue:** The exercises are too short. HSG Übungsblätter have 7-8 multi-part problems each. Students need 3-4x more practice problems.

**Recommendation:** Either:
1. Expand each exercise file to 8-10 problems, OR
2. Add "Additional Practice" files with more problems

---

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** practice, tables
- **Improve:**
  - Add “**Exam relevance & typical tasks**” (what you must be able to do by hand).
  - Add a “**revision sprint**”: 10-min recap + 3 drills + link to the exercise sheet.
  - Add an explicit “**If you get stuck…**” remediation map (which page to revisit for each common confusion).

### Student 3

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

## `exercises/exercise_1.md` — Exercise 1: Descriptive Statistics

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** practice, tables
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

### Student 5

- ✅ Good: Problems are relevant
- ❌ Fix: Restructure to match HSG format exactly
- ❌ Add: More problems (8-10 total)
- ❌ Add: Frequency distribution problem

## `exercises/exercise_2.md` — Exercise 2: Probability

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 0/3
- **Already strong:** practice
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `exercises/exercise_3a.md` — Exercise 3A: Discrete Distributions

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 0/3
- **Already strong:** practice
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `exercises/exercise_3b.md` — Exercise 3B: Continuous Distributions

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 0/3
- **Already strong:** practice
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `exercises/exercise_4.md` — Exercise 4: Sampling & Estimation

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 0/3
- **Already strong:** practice
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `exercises/exercise_5.md` — Exercise 5: Hypothesis Testing

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 0/3
- **Already strong:** practice
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?

## `exercises/exercise_6.md` — Exercise 6: Regression

### Student 2

- **Helpfulness:** 3/5 | **HSG-support:** 1/3
- **Already strong:** practice, tables
- **Improve:**
  - Add **one fully worked example** in HSG style: formula → substitute → intermediate steps (table if needed) → final answer → interpretation sentence.
  - Add a **Common mistakes** block (3–5 bullets) specific to this topic; cross-link to `reference/common_mistakes.md`.
  - Add a short **Checklist** (“When to use”, “Assumptions”, “What to report”) to reduce exam-time confusion.
  - Add **Key Takeaways** (max 5 bullets) optimized for last-minute revision.
  - Add/strengthen a **business interpretation** line: what decision does this number/test support?
