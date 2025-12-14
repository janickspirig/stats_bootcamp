---
title: "I can calculate expected value and variance"
category: "Statistics Bootcamp"
module: 4
order: 5
---

# I can calculate expected value and variance

> 📚 **Overview:** Expected value and variance describe the center and spread of probability distributions—essential for decision-making under uncertainty.

---

## 📑 Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Key Concepts](#key-concepts)
3. [Worked Example](#worked-example)
4. [Practice Problems](#practice-problems)
5. [Business Application: Decision Making](#business-application-decision-making)
6. [Key Takeaways](#key-takeaways)

---

## Learning Objectives

After completing this section, you will be able to:
- Calculate expected value (mean) of a discrete random variable
- Calculate variance and standard deviation
- Apply expected value rules for linear combinations
- Solve business decision problems using expected value

---

## Key Concepts

### Expected Value (Mean)

The **expected value** is the long-run average of a random variable.

$$
E(X) = \mu = \sum_{i} x_i \cdot P(X = x_i)
$$

**Interpretation:** If we repeated this process many times, the average outcome would approach E(X).

---

### Variance and Standard Deviation

**Variance:**

$$
Var(X) = \sigma^2 = E[(X - \mu)^2] = E(X^2) - [E(X)]^2
$$

**Standard Deviation:**

$$
\sigma = \sqrt{Var(X)}
$$

---

### Rules for Expected Value

| Rule | Formula |
|------|---------|
| Constant | E(c) = c |
| Multiplication by constant | E(cX) = c·E(X) |
| Addition | E(X + Y) = E(X) + E(Y) |
| Linear combination | E(aX + b) = a·E(X) + b |

---

### Rules for Variance

| Rule | Formula |
|------|---------|
| Constant | Var(c) = 0 |
| Multiplication by constant | Var(cX) = c²·Var(X) |
| Sum (independent) | Var(X + Y) = Var(X) + Var(Y) |
| Linear transformation | Var(aX + b) = a²·Var(X) |

> 💡 **Note:** Adding a constant doesn't change variance, but multiplying does (by the square of the constant).

---

## Worked Example

**Problem:**
A game costs CHF 5 to play. You roll a die:
- If you roll 6: win CHF 20
- If you roll 4 or 5: win CHF 10
- Otherwise: win nothing

Calculate the expected value and decide if you should play.

**Solution:**

### Step 1: Define the Random Variable

Let X = Net winnings (payout minus cost)

| Outcome | Payout | Cost | Net (X) | P(X) |
|---------|--------|------|---------|------|
| Roll 6 | 20 | 5 | 15 | 1/6 |
| Roll 4 or 5 | 10 | 5 | 5 | 2/6 |
| Roll 1, 2, 3 | 0 | 5 | -5 | 3/6 |

### Step 2: Calculate Expected Value

$$E(X) = 15 \times \frac{1}{6} + 5 \times \frac{2}{6} + (-5) \times \frac{3}{6}$$

$$E(X) = \frac{15}{6} + \frac{10}{6} - \frac{15}{6} = \frac{10}{6} = 1.67$$

### Step 3: Interpretation

**E(X) = CHF 1.67** per game

On average, you win CHF 1.67 per game. Over many games, you expect to profit.

**Decision:** Yes, you should play (positive expected value).

---

### Step 4: Calculate Variance (for completeness)

First, calculate E(X²):
$$E(X^2) = 15^2 \times \frac{1}{6} + 5^2 \times \frac{2}{6} + (-5)^2 \times \frac{3}{6}$$
$$E(X^2) = \frac{225}{6} + \frac{50}{6} + \frac{75}{6} = \frac{350}{6} = 58.33$$

Then:
$$Var(X) = E(X^2) - [E(X)]^2 = 58.33 - (1.67)^2 = 58.33 - 2.79 = 55.54$$

$$\sigma = \sqrt{55.54} = 7.45$$

**Interpretation:** Results vary by about CHF 7.45 from the mean of CHF 1.67.

---

## Practice Problems

### Problem 1

A company sells extended warranties. Data shows:
- 80% of customers never claim (cost to company: CHF 0)
- 15% claim small repairs (cost: CHF 100)
- 5% claim major repairs (cost: CHF 500)

The warranty sells for CHF 50. What's the expected profit per warranty?

<details>
<summary>💡 Show Solution</summary>

**Define X = Profit = Revenue - Cost**

| Scenario | Revenue | Cost | Profit | P(X) |
|----------|---------|------|--------|------|
| No claim | 50 | 0 | 50 | 0.80 |
| Small repair | 50 | 100 | -50 | 0.15 |
| Major repair | 50 | 500 | -450 | 0.05 |

**Calculate E(X):**
$$E(X) = 50 \times 0.80 + (-50) \times 0.15 + (-450) \times 0.05$$
$$E(X) = 40 - 7.5 - 22.5 = 10$$

**Answer:** Expected profit is CHF 10 per warranty sold.

</details>

---

### Problem 2

Let X be a random variable with E(X) = 10 and Var(X) = 4.

Calculate E(Y) and Var(Y) for Y = 3X + 5.

<details>
<summary>💡 Show Solution</summary>

**For E(Y):**
Using E(aX + b) = a·E(X) + b
$$E(Y) = 3 \times E(X) + 5 = 3 \times 10 + 5 = 35$$

**For Var(Y):**
Using Var(aX + b) = a²·Var(X)
$$Var(Y) = 3^2 \times Var(X) = 9 \times 4 = 36$$

**Standard deviation:**
$$\sigma_Y = \sqrt{36} = 6$$

**Answer:** E(Y) = 35, Var(Y) = 36, σ_Y = 6

</details>

---

### Problem 3

The number of customers X entering a store per hour has:
- P(X=0) = 0.10
- P(X=1) = 0.20
- P(X=2) = 0.30
- P(X=3) = 0.25
- P(X=4) = 0.15

Find E(X) and Var(X).

<details>
<summary>💡 Show Solution</summary>

**Calculate E(X):**
$$E(X) = 0(0.10) + 1(0.20) + 2(0.30) + 3(0.25) + 4(0.15)$$
$$E(X) = 0 + 0.20 + 0.60 + 0.75 + 0.60 = 2.15$$

**Calculate E(X²):**
$$E(X^2) = 0^2(0.10) + 1^2(0.20) + 2^2(0.30) + 3^2(0.25) + 4^2(0.15)$$
$$E(X^2) = 0 + 0.20 + 1.20 + 2.25 + 2.40 = 6.05$$

**Calculate Var(X):**
$$Var(X) = E(X^2) - [E(X)]^2 = 6.05 - (2.15)^2 = 6.05 - 4.62 = 1.43$$

**Standard deviation:**
$$\sigma = \sqrt{1.43} = 1.20$$

**Answer:** E(X) = 2.15 customers/hour, σ = 1.20

</details>

---

## Business Application: Decision Making

### Expected Value Criterion

When choosing between alternatives, select the one with the highest expected value (for profits) or lowest expected value (for costs).

**Example:** Two investment options

| Option | Outcome | Probability | Value |
|--------|---------|-------------|-------|
| A | Gain | 0.6 | +10,000 |
| A | Loss | 0.4 | -5,000 |
| B | Gain | 0.3 | +30,000 |
| B | Loss | 0.7 | -8,000 |

E(A) = 0.6(10,000) + 0.4(-5,000) = 6,000 - 2,000 = **4,000**
E(B) = 0.3(30,000) + 0.7(-8,000) = 9,000 - 5,600 = **3,400**

**Decision:** Choose A (higher expected value)

> ⚠️ **Note:** Expected value ignores risk! Option B has higher variance. Risk-averse decision makers might still prefer A even more strongly.

---

## Common Mistakes to Avoid

> ⚠️ **Mistake 1:** Forgetting that Var(X+a) = Var(X).
> Constants don't affect variance—only multipliers do.

> ⚠️ **Mistake 2:** Using Var(aX) = a·Var(X) instead of a²·Var(X).
> The constant is SQUARED for variance.

> ⚠️ **Mistake 3:** Adding variances of dependent variables.
> Var(X+Y) = Var(X) + Var(Y) only works if X and Y are independent.

---

## Key Takeaways

> 🎯 **Remember:**
> - **Expected value** = long-run average = Σxᵢ × P(xᵢ)
> - **Variance** measures spread = E(X²) - [E(X)]²
> - Constants shift E(X) but don't change Var(X)
> - Multipliers scale E(X) linearly but Var(X) by the square
> - Expected value is key for decision-making under uncertainty

---

## Navigation

[← Counting](counting.md) | [Module Index](index.md) | [Next Module: Discrete Distributions →](../05_discrete_distributions/index.md)

**Related Reference:** [Formula Glossary](../reference/formula_glossary.md)


