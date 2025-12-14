---
title: "Distributions Cheat Sheet"
category: "Statistics Bootcamp"
module: 99
order: 11
---

# Distributions Cheat Sheet

> Quick selection rules + approximation reminders.

---

## Discrete distributions (count data)

### Binomial

Use when:
- Fixed number of trials \(n\)
- Each trial is success/failure
- Constant probability \(p\)
- Trials independent (with replacement / large population)

Key:

$$
X\sim Bin(n,p),\quad E[X]=np,\quad Var(X)=np(1-p)
$$

### Hypergeometric

Use when:
- Sample \(n\) from finite population \(N\)
- “Successes” in population \(K\)
- Without replacement

### Poisson

Use when:
- Counting events in a time/space interval
- Known average rate \( \lambda \)

Key:

$$
X\sim Pois(\lambda),\quad E[X]=\lambda,\quad Var(X)=\lambda
$$

---

## Approximation rules (exam-friendly)

### Binomial \(\rightarrow\) Poisson

Use when \(n\) large, \(p\) small:

- Set \( \lambda = np \)
- Common rule: \(p\le 0.05\) and \(np\le 10\) (stricter: \(np<5\))

### Hypergeometric \(\rightarrow\) Binomial

If \(n/N \le 0.05\), treat draws as “almost independent”:

- Use \(p=K/N\) in \(Bin(n,p)\)

### Binomial \(\rightarrow\) Normal (with continuity correction)

If \(np\ge 5\) and \(n(1-p)\ge 5\):

- \(Y\sim N(np, np(1-p))\)
- Continuity correction:
  - \(P(X\le k)\approx P(Y\le k+0.5)\)
  - \(P(X\ge k)\approx P(Y\ge k-0.5)\)

---

## Continuous distribution (Normal)

If \(X\sim N(\mu,\sigma^2)\):

$$
z = \frac{x-\mu}{\sigma}
$$

For sample means:

$$
\bar X \sim N\left(\mu,\frac{\sigma^2}{n}\right),\quad z=\frac{\bar x-\mu}{\sigma/\sqrt{n}}
$$

---

## Quick keywords

- “per hour / per page / per km”: Poisson
- “fixed n trials with p”: Binomial
- “without replacement from N”: Hypergeometric
- “at least one”: use complement \(1-P(X=0)\)


