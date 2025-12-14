# Student Review: Statistics Bootcamp
**Reviewer Profile:** 2nd Semester BBA Student, HSG  
**Background:** Solid high school math, minimal statistics exposure, preparing for "3,120 Methoden: Statistik" exam  
**Career Goal:** Management consulting  
**Date:** December 2024

---

## Overall Impression: ⭐⭐⭐⭐½ (4.5/5)

This bootcamp is **genuinely helpful** and saves me from drowning in lecture slides. It's structured, exam-focused, and doesn't waste my time with unnecessary theory. That said, there are a few gaps when compared to actual HSG Übungsblätter that I'll detail below.

---

## What Works Really Well ✅

### 1. **The "I can..." / "I know..." Structure is Brilliant**
Coming from someone who has zero stats background, this is a game-changer. Instead of abstract chapter titles like "Inferential Statistics," I see:
- "I can calculate variance and standard deviation"
- "I can compute a confidence interval for the mean"

This tells me **exactly** what I need to be able to do. It's like a checklist for exam prep, which is perfect for someone like me who wants to optimize study time.

**Example:** When I see "I understand the testing framework," I know this is the 5-step template Prof. Füss expects on exams. That's actionable.

---

### 2. **Business Context in Every Example**
The bootcamp uses:
- Sales figures (CHF)
- Customer satisfaction scores
- Marketing campaigns
- Delivery times

As someone aiming for consulting, these examples feel **relevant**. I'm not calculating the average height of penguins (like my cousin's biology stats course)—I'm analyzing business problems. This keeps me engaged.

**Specific win:** Exercise 1, Problem 4 uses household survey data with frequency tables. This mirrors real market research scenarios I'll encounter at BCG or McKinsey.

---

### 3. **The FAQ Page is Gold**
The expandable Q&A format is perfect:
- "When do I use a z-test vs a t-test?" → Answered in 3 lines
- "What's the difference between SD and SE?" → Clear, with formula

I wish my lecture notes were this concise. This is exactly what I need at 2 AM before the exam when I panic about α vs α/2.

**Suggestion:** Add a few more FAQs based on Übungsblatt pitfalls:
- "When do I use Binomial vs Poisson vs Hypergeometric?"
- "How do I know if data is paired or independent?"

---

### 4. **Study Path Options (Plan A/B/C) Respect My Time**
The bootcamp acknowledges that I might have:
- 16+ hours → Full review
- 8-10 hours → Focused review
- 4-6 hours → Last-minute cram

This is **realistic**. I'm taking 6 courses this semester. Having a "smart cram" option that prioritizes Modules 09-11 (hypothesis testing = 30-40% of exam) is strategic.

**Personal use:** I followed Plan B (8-10 hours) starting one week before my mock exam, and it covered ~80% of the content I needed.

---

### 5. **Calculation Tables Match HSG Style**
Exercise 1 (MAD, variance) includes step-by-step calculation tables:
- Columns for \(x_i\), \(x_i - \bar{x}\), \(|x_i - \bar{x}|\)
- Show all intermediate values
- Sum at the bottom

This is **exactly** how Prof. Füss grades. If I don't show the table, I lose 50% of the points even if my final answer is correct. The bootcamp trains me to do this automatically.

---

## What's Missing / Could Be Better ⚠️

### 1. **Not Enough Multi-Part "Aufgaben" (Like Real HSG Exercises)**
HSG Übungsblätter have problems with parts a), b), c), d) that build on each other. The bootcamp has some, but I need **more**.

**Example of what I want to see more of:**
> **Aufgabe:** A bottling company fills bottles with mean μ = 500ml, σ = 15ml, n = 36.
> 
> a) Calculate P(495 < X̄ < 505)  
> b) Construct a 95% CI for the mean  
> c) If the true mean dropped to 490ml, what is the probability we fail to detect it? (Type II error)  
> d) What sample size would reduce this error to 10%?

Parts c) and d) are **advanced integration questions** that I see on actual HSG exams but are underrepresented in the bootcamp.

**Current status:** Exercises 1-6 have good content, but they feel like "warm-up" problems. I need 2-3 **brutal** exercises per module that combine multiple concepts.

---

### 2. **No "Past Exam Style" Section**
The CS Bootcamp (which my roommate uses) has an "Old Exams" page. I'd love:
- 2-3 full exam-length problems (like actual Klausuren)
- Time limits (5-8 minutes per Aufgabe part, as per HSG style)
- "Worked solutions with common mistakes highlighted"

**Why this matters:** Practicing under time pressure is **critical**. I can solve problems given unlimited time, but exams are a sprint. I need to train for speed + accuracy.

---

### 3. **More Emphasis on "When to Use Which Distribution"**
Module 05 has "choosing_distribution.md," which is helpful, but I still mess up:
- Binomial vs Hypergeometric (with/without replacement)
- Poisson approximation conditions (when is np < 5 sufficient?)
- Normal approximation to Binomial (when do I use continuity correction?)

**What I need:** A **decision flowchart** (like the test selection flowchart in `which_test.md`) but for distributions. I want to print it out and stick it on my wall.

**Current gap:** The text explains each distribution well, but the **selection logic** between them needs more prominence.

---

### 4. **German Terminology Glossary is Underutilized**
I take the exam in German. While formulas are universal, I need to know:
- Stichprobe (sample) vs Grundgesamtheit (population)
- Ablehnungsbereich (rejection region)
- Fehler 1. Art / 2. Art (Type I/II errors)

The student profile document mentions these, but the bootcamp itself doesn't have a **German-English term mapping page**.

**Suggested addition:** A simple two-column table in the reference section:
| German Term | English Term |
|-------------|--------------|
| Mittelwert | Mean |
| Standardabweichung | Standard Deviation |
| Signifikanzniveau | Significance Level |
| ... | ... |

This would take 10 minutes to create and would be **super useful** for students switching between German lectures and English bootcamp materials.

---

### 5. **Formula Glossary is Good, But I Want "Formula Cheat Sheets" by Topic**
The formula glossary is comprehensive, but when I'm solving a regression problem, I don't want to scroll through 50 formulas.

**What I'd love:**
- **One-page PDF cheat sheets** per module (like the ones profs allow in exams)
- Example: "Hypothesis Testing Cheat Sheet" with:
  - 5-step framework
  - Test statistic formulas (z, t, proportions)
  - Critical value lookup reminders
  - df formulas

**Current workaround:** I manually created these myself using the bootcamp content. But if they were pre-made, that's 2+ hours I'd save.

---

### 6. **More "Common Mistakes" Examples Embedded in Exercises**
The "Common Mistakes" reference page is excellent, but I'd absorb it better if **wrong answer explanations** were embedded in practice problems.

**Example format I'd love to see:**

<details>
<summary>💡 Show Solution</summary>

**Correct Answer:** t = 2.5

**Common Mistake #1:** Using σ instead of s/√n  
❌ "If you used σ = 15 directly instead of SE = 15/√25 = 3, you'd get t = 0.67 (wrong!)"

**Common Mistake #2:** Forgetting to use α/2 for two-tailed test  
❌ "If you used z = 1.645 instead of z = 1.96, you'd reject H₀ incorrectly."

</details>

This **active learning** approach would drill the mistakes into my head better than reading a separate "mistakes" page.

---

## Specific Module Feedback

### Modules I Loved ❤️

**Module 09: Hypothesis Testing Basics**
- The **reusable 5-step template** is copy-paste gold
- Clear distinction between critical value vs p-value approaches
- Worked examples with business interpretation

**Module 02: Descriptive Statistics**
- Calculation tables are exam-ready
- Weighted mean, MAD, CV—all covered
- Problem 8 (skewness) teaches me **when to use median vs mean**, which is super practical

**Module 08: Confidence Intervals**
- Formula → substitution → interpretation pattern is perfect
- Sample size determination is explained well (this is often tested!)

---

### Modules That Need More Depth

**Module 13: Advanced Topics**
- ANOVA and Chi-square feel rushed
- These are 10-15% of the exam, but the bootcamp treats them as "bonus"
- I'd like at least one **full worked ANOVA problem** with F-table lookup

**Module 07: Sampling Distributions**
- Central Limit Theorem is conceptually explained, but I need more **calculation practice**
- Specifically: "Given population parameters, calculate P(X̄ > k)" problems

---

## Who Is This Bootcamp For?

### ✅ **Perfect for:**
- HSG students taking "Methoden: Statistik" (or equivalent)
- Students with good high school math but **zero stats experience**
- People who want **exam-focused, no-fluff** review
- Self-directed learners who prefer structured paths

### ⚠️ **Not ideal for:**
- Students looking for deep theoretical proofs (this is applied/practical)
- Complete beginners who need video lectures (this is text-based)
- Non-business students (examples are business-heavy)

---

## Comparison to Other Resources

| Resource | Strengths | Weaknesses |
|----------|-----------|------------|
| **This Bootcamp** | Structured, exam-focused, business context | Needs more brutal exercises, German glossary |
| **Lecture Slides** | Official, comprehensive | Dense, hard to extract "what I need to know" |
| **Übungsblätter** | Realistic exam problems | Solutions sometimes skip steps, no concept review |
| **YouTube (StatQuest, etc.)** | Visual, intuitive | Not HSG-specific, wastes time on irrelevant topics |

**My workflow:** Bootcamp for concept learning + Übungsblätter for practice + this bootcamp's FAQ for last-minute review.

---

## Did This Help Me Pass?

**Short answer:** Yes, but I also used Übungsblätter.

**Long answer:** I used Plan B (focused review) one week before my exam. The bootcamp covered:
- Hypothesis testing framework (Module 09) → Saved me hours of lecture slide review
- CI construction (Module 08) → Practiced until I could do it in my sleep
- Test selection flowchart → Helped me avoid picking the wrong test

Where the bootcamp wasn't enough:
- Integration problems (needed Übungsblätter for this)
- Speed training (needed to time myself on past exams)

**Estimated impact:** The bootcamp probably raised my grade by **0.5-1.0 points** (on a 6-point Swiss scale) by giving me a clear study structure and catching gaps I didn't know I had.

---

## Final Verdict

### Strengths 💪
1. Learning-goal driven structure (I know exactly what I need to master)
2. Business-contextualized examples (keeps me engaged)
3. Exam-ready calculation tables and templates
4. Time-efficient study paths (Plan A/B/C)
5. FAQ page for quick lookups

### Gaps to Fill 🔧
1. More multi-part, integration-heavy exercises (like Übungsblatt 4-6)
2. Past exam-style problems with time limits
3. German terminology glossary
4. Distribution selection flowchart
5. One-page formula cheat sheets per topic
6. More ANOVA/Chi-square depth

---

## Recommendations for Future Students

### If you have 2+ weeks before the exam:
1. **Week 1:** Complete Plan A (full review) + make your own notes
2. **Week 2:** Grind through Übungsblätter, use bootcamp FAQ for stuck points
3. **Day before:** Review bootcamp's "Common Mistakes" + formula glossary

### If you have 1 week:
1. **Days 1-3:** Plan B (focused review), Modules 08-11
2. **Days 4-6:** Practice Übungsblätter problems, reference bootcamp as needed
3. **Day 7:** Cram FAQ, common mistakes, test selection flowchart

### If you have 1-2 days (panic mode):
1. Use Plan C + do Exercise 5 (hypothesis testing)
2. Memorize the 5-step framework
3. Print "Common Mistakes" and read it 3 times

---

## Would I Recommend This? 

**Yes, with caveats.**

This bootcamp is a **high-quality supplement**, not a replacement for:
- Attending lectures
- Solving Übungsblätter
- Past exam practice

Think of it as a **GPS for your statistics exam prep**. It won't drive the car for you, but it will:
- Show you the fastest route
- Warn you about common pitfalls
- Keep you from getting lost in unnecessary theory

For an HSG student like me (busy, ambitious, want to ace the exam efficiently), this is **exactly what I need**—just add a German glossary and more brutal exercises, and it'd be perfect.

---

## One Sentence Summary

**"A well-structured, exam-focused bootcamp that covers 80% of what I need to pass HSG statistics—pair it with Übungsblätter for the remaining 20%."**

---

**Rating Breakdown:**
- Content Quality: 5/5
- Exam Relevance: 4/5 (needs more integration problems)
- User Experience: 5/5 (clear structure, easy navigation)
- Completeness: 4/5 (ANOVA/Chi-square need more depth)
- Time Efficiency: 5/5 (Plan A/B/C system is brilliant)

**Overall: 4.5/5 ⭐⭐⭐⭐½**

---

*Reviewed by: Anonymous HSG BBA Student, Cohort 2024*  
*Study Time Invested: ~10 hours (Plan B)*  
*Exam Result: On track for 5.0+ (will update after final exam)*

