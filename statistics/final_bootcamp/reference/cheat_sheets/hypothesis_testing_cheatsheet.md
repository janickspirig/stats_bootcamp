---
title: "Hypothesis Testing Cheat Sheet"
category: "Statistics Bootcamp"
module: 99
order: 10
---

# Hypothesis Testing Cheat Sheet

> One-page-style reminders for full marks (framework, critical values, wording).

---

## The 5 steps (write these every time)

1. **Hypotheses**: write \(H_0\) (includes equality) and \(H_1\) (direction).
2. **Significance**: state α and tails (two-tailed → use α/2 for critical values).
3. **Test statistic**: formula → substitution → numeric value.
4. **Decision**: compare to critical value(s) **or** compare p-value to α.
5. **Conclusion**: “At α = …, we (do/do not) reject \(H_0\). Therefore …” + one business sentence.

---

## Choose the right test statistic

- **Mean, σ known**:

$$
z = \frac{\bar x-\mu_0}{\sigma/\sqrt{n}}
$$

- **Mean, σ unknown** (one-sample):

$$
t = \frac{\bar x-\mu_0}{s/\sqrt{n}},\qquad df=n-1
$$

- **One proportion**:

$$
z = \frac{\hat p-p_0}{\sqrt{p_0(1-p_0)/n}}
$$

- **Two proportions** (pooled under \(H_0:p_1=p_2\)):

$$
z = \frac{\hat p_1-\hat p_2}{\sqrt{\hat p(1-\hat p)(1/n_1+1/n_2)}}
$$

---

## Critical values (common)

### Two-tailed (α split across tails)

- 90% CI / α=0.10 → \(z_{0.05}=1.645\)
- 95% CI / α=0.05 → \(z_{0.025}=1.96\)
- 99% CI / α=0.01 → \(z_{0.005}=2.576\)

### One-tailed

- α=0.10 → \(z_{0.10}=1.282\)
- α=0.05 → \(z_{0.05}=1.645\)
- α=0.01 → \(z_{0.01}=2.326\)

---

## Decision region reminders

- **Right-tailed** (\(H_1:>\)): reject if statistic is large positive.
- **Left-tailed** (\(H_1:<\)): reject if statistic is large negative.
- **Two-tailed** (\(H_1:\ne\)): reject if \(|\text{statistic}|\) exceeds the critical value.

---

## Conclusion wording (safe template)

“At α = [value], we **[reject / do not reject]** \(H_0\). Therefore, there **[is / is not]** sufficient evidence to conclude that [plain language \(H_1\)].”

---

## Quick traps

- Two-tailed uses **α/2** for critical values.
- SD vs SE: tests use \(\sigma/\sqrt{n}\) or \(s/\sqrt{n}\), not σ or s.
- “Do not reject \(H_0\)” does **not** mean \(H_0\) is proven true.


