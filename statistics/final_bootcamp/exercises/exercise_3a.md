---
title: "Exercise 3A: Discrete Distributions"
category: "Statistics Bootcamp"
module: 98
order: 3
---

# Exercise 3A: Discrete Distributions

> 📚 **Overview:** Practice with Binomial, Poisson, and Hypergeometric distributions.

Practice problems for Binomial, Poisson, and Hypergeometric distributions.

---

## Topics Covered
- Binomial distribution
- Poisson distribution
- Hypergeometric distribution
- Choosing the right distribution

---

## Problem 1 (Binomial)

A quality inspector tests 15 items. The defect rate is 10%.
a) What's the probability of exactly 2 defects?
b) What's the probability of at most 1 defect?
c) What's the expected number of defects?

<details>
<summary>💡 Show Solution</summary>

X ~ Bin(15, 0.10)

**a) P(X = 2):**

$$
P(X=2) = \binom{15}{2}(0.10)^2(0.90)^{13} = 105 \times 0.01 \times 0.254 = 0.267
$$

**b) P(X ≤ 1) = P(X=0) + P(X=1):**

$$
P(X=0) = (0.90)^{15} = 0.206
$$

$$
P(X=1) = 15(0.10)(0.90)^{14} = 0.343
$$

$$
P(X \leq 1) = 0.206 + 0.343 = 0.549
$$

**c) E(X) = np = 15 × 0.10 = 1.5 defects**

</details>

---

## Problem 2 (Poisson)

A website receives 4 inquiries per hour on average.
a) P(exactly 6 inquiries next hour)
b) P(no inquiries in 30 minutes)

<details>
<summary>💡 Show Solution</summary>

**a) P(X = 6) with λ = 4:**

$$
P(X=6) = \frac{4^6 e^{-4}}{6!} = \frac{4096 \times 0.0183}{720} = 0.104
$$

**b) P(X = 0) for 30 min (λ = 2):**

$$
P(X=0) = e^{-2} = 0.135
$$

</details>

---

## Problem 3 (Hypergeometric)

A box has 20 items: 5 defective, 15 good. You select 6 items.
P(exactly 2 defective)?

<details>
<summary>💡 Show Solution</summary>

$$
P(X=2) = \frac{\binom{5}{2}\binom{15}{4}}{\binom{20}{6}} = \frac{10 \times 1365}{38760} = 0.352
$$

</details>

---

## Problem 4 (Integrated Binomial — multi-part)

A coin is flipped 10 times.
Assume P(Head) = 0.5 and flips are independent.

Calculate:
a) P(exactly 6 heads)
b) P(at most 6 heads)
c) P(between 4 and 7 heads inclusive)
d) E(X) and Var(X)

<details>
<summary>💡 Show Solution</summary>

Let X = number of heads, X ~ Bin(10, 0.5).

a) \(P(X=6) = \\binom{10}{6}(0.5)^{10} = 210/1024 = 0.2051\)

b) \(P(X\\le 6) = 1 - P(X\\ge 7) = 1 - [P(7)+P(8)+P(9)+P(10)]\)

Numerically: P(7)=120/1024, P(8)=45/1024, P(9)=10/1024, P(10)=1/1024 → sum=176/1024=0.1719

So P(X≤6)=1−0.1719=0.8281

c) P(4≤X≤7)=P(X≤7)−P(X≤3)

P(X≤7)=1−P(X≥8)=1−(45+10+1)/1024=1−56/1024=0.9453

P(X≤3)=(1+10+45+120)/1024=176/1024=0.1719

So P(4≤X≤7)=0.9453−0.1719=0.7734
d) E(X)=np=5, Var(X)=np(1−p)=10·0.5·0.5=2.5

Business interpretation: You expect 5 heads on average; the typical spread is \(\\sqrt{2.5}\\approx 1.58\) heads.

</details>

---

## Problem 5 (Choose the right distribution)

For each scenario, choose Binomial / Poisson / Hypergeometric and explain in one line:

a) Counting customers arriving per minute (average 3/min)
b) Drawing 4 cards from a deck without replacement and counting aces
c) Counting defective items in a batch when defect probability is constant per item and items are independent

<details>
<summary>💡 Show Solution</summary>

a) **Poisson** (events per interval)
b) **Hypergeometric** (sampling without replacement)
c) **Binomial** (fixed n trials, independent, constant p)

</details>

---

## Problem 6 (Poisson approximation to Binomial)

An email provider estimates that 0.2% of emails are phishing. You check n = 500 emails.
Use a Poisson approximation to estimate P(at least 1 phishing email).

<details>
<summary>💡 Show Solution</summary>

Binomial with n large, p small → Poisson approximation with \(\\lambda = np = 500\\cdot 0.002 = 1\).

P(X ≥ 1) = 1 − P(X = 0) = 1 − \(e^{-1}\\) = 1 − 0.3679 = 0.6321.

Business interpretation: With 500 emails, it’s quite likely (~63%) you see at least one phishing email.

</details>

---

## Problem 7 (Hypergeometric vs Binomial intuition)

A warehouse has 40 boxes, 8 of which are damaged.
You inspect 5 boxes without replacement.

a) What distribution is appropriate?
b) Compute P(exactly 1 damaged) using that distribution.

<details>
<summary>💡 Show Solution</summary>

a) **Hypergeometric**: N=40, K=8, n=5.

b) Compute:

$$
P(X=1) = \frac{\binom{8}{1}\binom{32}{4}}{\binom{40}{5}} = \frac{8 \times 35960}{658008} = \frac{287680}{658008} = 0.437
$$

**Answer: P(exactly 1 damaged) ≈ 0.437 (43.7%)**

</details>

---

## Problem 8 (Common exam complement)

In a Binomial setting with n = 20 and p = 0.05, compute P(at least one success).

<details>
<summary>💡 Show Solution</summary>

Use complement:

$$
P(X \\ge 1) = 1 - P(X=0) = 1 - (1-p)^{n} = 1 - 0.95^{20}
$$

Numerically: 0.95^{20} ≈ 0.3585 → P(X ≥ 1) ≈ 0.6415.

</details>

---

## Problem 9 (Normal approximation to Binomial + continuity correction)

Let \(X\\sim Bin(n=100, p=0.60)\\).

Approximate \(P(X\\ge 65)\\) using a Normal approximation **with continuity correction**.

<details>
<summary>💡 Show Solution</summary>

Mean \(\\mu=np=60\\). Variance \(np(1-p)=100\\cdot 0.6\\cdot 0.4=24\\). SD \(=\\sqrt{24}=4.899\\).

Continuity correction:

$$
P(X\\ge 65) \\approx P(Y>64.5)
$$

where \(Y\\sim N(60,24)\\).

$$
z = \\frac{64.5-60}{4.899} = 0.918
$$

$$
P(Y>64.5)=1-\\Phi(0.918)\\approx 1-0.8208 = 0.1792
$$

</details>

---

## Problem 10 (Binomial approximation to Hypergeometric)

A company has N = 1000 invoices, K = 40 contain an error. You randomly sample n = 10 invoices **without replacement**.

Approximate the probability of finding **no** errors.

<details>
<summary>💡 Show Solution</summary>

Exact model is Hypergeometric, but \(n/N=10/1000=1%\\) is small, so Binomial approximation is reasonable:

$$
X\\approx Bin(n=10, p=K/N=0.04)
$$

$$
P(X=0)=(1-p)^{n}=0.96^{10}=0.6648
$$

</details>

---

## Problem 11 (Poisson approximation: many trials, small p)

A call center makes n = 100 sales calls. Each call has a success probability p = 0.02. Approximate:

a) \(P(X=0)\\)  
b) \(P(X=1)\\)  
c) \(P(X\\ge 2)\\)

<details>
<summary>💡 Show Solution</summary>

Binomial with n large, p small → Poisson approximation with \(\\lambda=np=2\\).

a) \(P(X=0)=e^{-2}=0.1353\\)

b) \(P(X=1)=2e^{-2}=0.2707\\)

c) \(P(X\\ge 2)=1-P(0)-P(1)=1-0.1353-0.2707=0.5940\\)

</details>

---

## Problem 12 (Poisson rate scaling)

Accidents occur at a rate of 0.3 per day on a road segment. What is the probability of **at least 2** accidents in the next 7 days?

<details>
<summary>💡 Show Solution</summary>

Poisson with \(\\lambda = 0.3\\cdot 7 = 2.1\\).

Use complement:

$$
P(X\\ge 2)=1-P(0)-P(1)=1-e^{-2.1}-2.1e^{-2.1}=1-e^{-2.1}(1+2.1)
$$

Compute \(e^{-2.1}\\approx 0.1225\\):

$$
P(X\\ge 2)\\approx 1-0.1225\\cdot 3.1 = 1-0.3798 = 0.6202
$$

</details>

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Forgetting “without replacement” → Hypergeometric.
> ⚠️ **Mistake 2:** For “at least one” → use complement.
> ⚠️ **Mistake 3:** Using Poisson when n is small or p is not small (approximation conditions fail).

---

## Key Takeaways

- Binomial: fixed n, independent trials, constant p
- Poisson: events per interval (λ)
- Hypergeometric: sampling without replacement
- Multi-part problems often reuse the same distribution once identified

---

## Related Module

[Module 05: Discrete Distributions](../05_discrete_distributions/index.md)

---

## Navigation

[← Exercise 2](exercise_2.md) | [Exercises Index](index.md) | [Exercise 3B →](exercise_3b.md)


