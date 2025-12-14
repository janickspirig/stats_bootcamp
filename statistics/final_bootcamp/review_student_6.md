# Statistics Bootcamp Review — An HSG BBA Student's Honest Opinion

**Reviewer Profile:** 1st-year HSG BBA student, currently taking "3,120 Methoden: Statistik"  
**Background:** Swiss Matura graduate, solid high school math, zero prior statistics knowledge  
**Date:** December 2024  
**Study Goal:** Pass the statistics exam with a good grade (ideally 5.0+)

---

## TL;DR — The Verdict

| Aspect | Rating | Quick Take |
|--------|--------|------------|
| **Overall Quality** | ⭐⭐⭐⭐ (7.5/10) | Solid foundation, but incomplete for exam-only prep |
| **Content Accuracy** | ⭐⭐⭐⭐⭐ (9/10) | Formulas are correct, notation is proper |
| **Exam Relevance** | ⭐⭐⭐⭐ (7/10) | Good coverage, but gaps vs. Übungsblätter |
| **Usability** | ⭐⭐⭐⭐⭐ (9/10) | Clean navigation, consistent structure |
| **Practice Problems** | ⭐⭐⭐ (6/10) | Too few — need 3x more for exam readiness |
| **Reference Materials** | ⭐⭐⭐⭐⭐ (9.5/10) | Formula glossary + common mistakes = gold |

**Bottom Line:** This bootcamp is a *great supplement* to lectures and official Übungsblätter. It explains concepts clearly and the worked examples match the HSG format. However, **don't use this as your only resource** — the exercise quantity is insufficient for building exam speed.

---

## 📚 What Is This Bootcamp Actually For?

Let me be clear about what this bootcamp does well:

### ✅ Use This For:
- **Understanding concepts** when the lecture slides confuse you
- **Seeing worked examples** in the exact format HSG expects (formula → substitution → answer)
- **Quick reference** during study sessions (formula glossary is excellent)
- **Identifying your weak spots** using the Learning Goals checklist
- **Last-minute review** of common mistakes before the exam

### ❌ Don't Use This For:
- **Your only practice** — the exercises are too few
- **Replacing the Übungsblätter** — you still need to do those by hand
- **Learning German terminology** — this is fully in English
- **Complete exam preparation** — it's a supplement, not a substitute

---

## 🎯 What I Actually Needed as a BBA Student

Coming into HSG, here's what I knew about statistics: basically nothing. I could calculate an average and that's about it. The student profile is accurate — we have good high school math, but statistics is new territory.

### What This Bootcamp Gets Right

**1. Starts from Zero (Mostly)**

The foundations module doesn't assume prior knowledge. The NOIR mnemonic for scales of measurement? Actually helpful. The data types tree? I can visualize it during the exam.

**2. Calculation Tables Match HSG Format**

This is crucial. The worked examples use the same table structure as our Übungsblätter:

| xᵢ | xᵢ - x̄ | (xᵢ - x̄)² |
|----|--------|-----------|
| 22 | -6.33  | 40.07     |
| ...| ...    | ...       |
| Σ  | ≈0     | 107.34    |

When I first saw this, I thought "okay, they actually understand what we need to do on paper."

**3. Clear When to Use What**

The "Which Test" decision guide saves time. Instead of panicking during the exam wondering "is this a z-test or t-test?", I can mentally run through the decision tree.

**4. Common Mistakes Page is a Lifesaver**

I read `common_mistakes.md` the night before my mock exam. It's like having a TA whisper all the things students get wrong:
- n vs. n-1 for sample variance ✓
- SD vs. SE confusion ✓
- One-tailed vs. two-tailed traps ✓
- Wrong df for different tests ✓

This page alone is worth reviewing multiple times.

---

## ⚠️ Where the Bootcamp Falls Short

### Problem 1: Not Enough Practice Problems

**This is the biggest issue.**

Each exercise file has maybe 3-5 problems. Our Übungsblätter have 7-8 multi-part problems each (that's 20-30 individual calculations). To build exam speed, I need repetition. Lots of it.

| Topic | Bootcamp Problems | What I Actually Need |
|-------|------------------|---------------------|
| Descriptive Stats | ~8 | 25+ |
| Probability | ~5 | 20+ |
| Hypothesis Testing | ~9 | 30+ |
| Regression | ~5 | 20+ |

**My workaround:** I did the bootcamp exercises first to understand the concepts, then hit the official Übungsblätter for volume.

---

### Problem 2: Missing Content That's on the Exam

A few things I encountered on the Übungsblätter that aren't well covered here:

| Missing/Weak Topic | Where I Found It | Impact |
|-------------------|------------------|--------|
| **Mean Absolute Deviation (MAD)** | Übungsblatt 1 | High — it's a core exam topic |
| **Frequency Distribution Tables** | Übungsblatt 1 | High — building f(x) and F(x) tables |
| **Odds Ratio (Quoten)** | Übungsblatt 2 | Medium — probability section |
| **Type II Error (β) Calculations** | Übungsblatt 5 | High — power analysis is tested! |
| **Full Regression Calculation Tables** | Übungsblatt 6 | High — need Σx, Σy, Σxy, Σx² |

The MAD gap surprised me most. It's in Übungsblatt 1, but I couldn't find a dedicated section in the bootcamp initially. *(Edit: I found it mentioned in variance_stddev.md, but it needs more emphasis and practice problems.)*

---

### Problem 3: German Terminology Missing

Our exam and Übungsblätter are in German. Key terms I had to learn separately:

| English | German | Why It Matters |
|---------|--------|----------------|
| Sample | Stichprobe | Read every question |
| Population | Grundgesamtheit | Know the difference! |
| Mean | Mittelwert | Core concept |
| Variance | Varianz | Core concept |
| Standard deviation | Standardabweichung | Core concept |
| Significance level | Signifikanzniveau | Every hypothesis test |
| Reject H₀ | H₀ ablehnen | Must state correctly |
| Confidence interval | Konfidenzintervall | Interpretation matters |

A German-English glossary would save students 30+ minutes of vocab lookup.

---

### Problem 4: Hypothesis Testing Needs Expansion

Module 09 (Hypothesis Testing Basics) is the most important topic for the exam, but the `testing_framework.md` page feels too short. The five-step process is there, but I wanted:

- More one-tailed vs. two-tailed examples
- β (Type II error) and power calculations with worked examples
- Explicit "what to write" templates for full marks
- Decision region diagrams

The current content teaches the concept, but doesn't drill it enough.

---

## 💪 What Works Exceptionally Well

### The Formula Glossary (`formula_glossary.md`)

**Rating: 9.5/10**

This is the page I kept open during all my study sessions. Every formula, organized by topic, with clear notation. I printed this out for my exam prep.

Suggestions:
- Add MAD formula more prominently
- Include computational shortcuts (alternative variance formula)

---

### The Common Mistakes Page (`common_mistakes.md`)

**Rating: 10/10 — No changes needed**

Whoever wrote this understands what students actually struggle with. The checklist at the bottom is perfect for a final review:

- [ ] Used correct notation (sample vs. population)
- [ ] Used n-1 for sample variance
- [ ] Stated both H₀ and H₁ correctly
- [ ] Used correct test (z vs. t, one vs. two-tailed)
- ...

I wish I had found this page in week 1.

---

### The FAQ Page (`faq.md`)

**Rating: 8.5/10**

The expandable format is perfect for quick lookups:
- "When do I use z vs. t?" → Click, got it.
- "What's the difference between SD and SE?" → Explained in 3 lines.
- "How do I read the z-table quickly?" → Practical tips.

This is how study materials should work — answer the question, move on.

---

### The Learning Goals Checklist (`learning_goals.md`)

**Rating: 9/10**

I used this as my exam prep tracker. Each goal links to its explanation page, so I can:
1. Read the goal: "I can calculate variance and standard deviation"
2. Test myself: Can I do this without notes?
3. If no → Click through to the concept page
4. If yes → Check it off

The checklist format matches how my brain works before an exam.

---

## 📊 Module-by-Module Quick Review

| Module | Quality | Key Strength | Main Gap |
|--------|---------|--------------|----------|
| 00 Start Here | ⭐⭐⭐⭐ | Clear structure, good study tips | Add exam-day checklist |
| 01 Foundations | ⭐⭐⭐⭐ | NOIR mnemonic, data types clear | Need more classification drills |
| 02 Descriptive Stats | ⭐⭐⭐⭐ | Good calculation tables | MAD needs own section, frequency tables |
| 03 Correlation | ⭐⭐⭐⭐ | Causation examples excellent | More calculation practice |
| 04 Probability | ⭐⭐⭐⭐ | Bayes tree diagrams helpful | Add odds ratio (Quoten) |
| 05 Discrete Dist. | ⭐⭐⭐⭐ | Choosing distribution guide | More cumulative probability practice |
| 06 Continuous Dist. | ⭐⭐⭐⭐ | Z-table interpretation clear | More reverse lookup exercises |
| 07 Sampling | ⭐⭐⭐ | CLT concept explained | Needs more SE examples |
| 08 Estimation | ⭐⭐⭐⭐ | CI formulas correct | Add sample size determination problems |
| 09 Hypothesis Testing | ⭐⭐⭐ | Framework is correct | **Needs major expansion** — β, power |
| 10 One-Sample Tests | ⭐⭐⭐⭐ | Clear z vs. t guidance | More five-step examples |
| 11 Two-Sample Tests | ⭐⭐⭐⭐ | Pooled variance shown | When to use paired vs. independent |
| 12 Regression | ⭐⭐⭐ | Formulas correct | **Needs expansion** — full tables, residuals |
| 13 Advanced | ⭐⭐⭐ | Concepts introduced | May be lower priority for exam |

---

## 🔧 My Top 5 Recommendations

If I could improve this bootcamp, here's what I'd prioritize:

### 1. Triple the Practice Problems
Every exercise file needs 8-10 multi-part problems, not 3-5. Include more problems with "build the calculation table from raw data" since that's what the exam demands.

### 2. Add a German Glossary
A simple page with 50-60 key terms in German-English would save hours of frustration.

### 3. Expand Hypothesis Testing (Module 09)
- Add β calculation examples
- Add power analysis
- Show more one-tailed vs. two-tailed comparisons
- Include decision region diagrams

### 4. Add Frequency Distribution Content
Building relative frequency f(xᵢ) and cumulative distribution F(xᵢ) tables is heavily tested. Needs dedicated examples.

### 5. Expand Regression (Module 12)
The current content is too brief for how much this topic is worth on the exam. Need complete calculation tables with Σx, Σy, Σxy, Σx², residuals, and interpretation.

---

## 🎓 How I Actually Used This Bootcamp

Here's my study workflow that worked:

### Phase 1: Concept Learning (Weeks 1-4)
1. Attend lecture
2. Same day: Read the corresponding bootcamp module
3. Try the bootcamp practice problems
4. Check against solutions, note what I got wrong

### Phase 2: Practice Drilling (Weeks 5-8)
1. Do official Übungsblätter (full problems, by hand)
2. When stuck: Reference bootcamp concept page
3. Use formula glossary as cheat sheet
4. Track progress with Learning Goals checklist

### Phase 3: Exam Prep (Week 9-10)
1. Review Common Mistakes page
2. Re-do problems I got wrong
3. Time myself on Übungsblatt-style problems
4. Final skim of formula glossary

**Time spent on bootcamp:** ~12 hours total  
**Time on Übungsblätter:** ~25 hours  
**Result:** Felt prepared for the exam format

---

## 📝 Final Thoughts

### What I'd Tell a Fellow HSG Student

> "Download this bootcamp and use it alongside your lectures. The explanations are clearer than some slides, and the worked examples show exactly how to set up calculation tables. The formula glossary and common mistakes pages are essential — print them out.
>
> BUT: don't skip the official Übungsblätter. The bootcamp exercises are too few to build exam speed. Think of this as your concept guide, not your practice arena."

### Would I Recommend This?

**Yes, with caveats.**

- ✅ For understanding concepts → Highly recommended
- ✅ For seeing worked examples → Highly recommended  
- ✅ For quick reference → Essential (formula glossary, common mistakes)
- ⚠️ For practice volume → Supplement with Übungsblätter
- ⚠️ For German terminology → Need additional resources

### What Would Make This a 9/10 Bootcamp

1. **More exercises** — at least 100 additional problems across all topics
2. **German terminology** — integrated throughout or as a dedicated glossary
3. **Expanded hypothesis testing** — β calculations, power analysis, more examples
4. **Complete regression section** — full calculation tables, interpretation focus
5. **Timed practice sets** — simulate exam conditions

---

## Appendix: Quick Reference for Fellow Students

### Best Pages to Bookmark

1. `reference/formula_glossary.md` — All formulas in one place
2. `reference/common_mistakes.md` — Read before every exam
3. `reference/which_test.md` — Decision tree for test selection
4. `faq.md` — Quick answers to common questions
5. `learning_goals.md` — Track your progress

### Exam Day Essentials (from this bootcamp)

- Five-step hypothesis testing template (memorize from Module 09)
- Critical z-values: 90% → 1.645, 95% → 1.96, 99% → 2.576
- n-1 for sample variance (never forget!)
- SE = s/√n (not just s!)
- Always state conclusion in context

### My Personal "Most Useful" Ranking

1. Formula Glossary (used every study session)
2. Common Mistakes (saved points on the exam)
3. FAQ (quick clarifications)
4. Variance/StdDev page (calculation tables)
5. Testing Framework (five-step template)

---

*Review written from the perspective of an HSG BBA student*  
*Based on: HSG_BBA_Student_Profile.txt and personal study experience*

**Final Rating: 7.5/10** — Strong foundation, needs more practice problems and German content

*Good luck with your exam, fellow HSG students! Remember: formula → substitution → calculation → interpretation. Always show your work.* 🍀
