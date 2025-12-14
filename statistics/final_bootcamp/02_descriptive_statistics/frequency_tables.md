---
title: "I can build frequency tables (f and F)"
category: "Statistics Bootcamp"
module: 2
order: 5
---

# I can build frequency tables (f and F)

> 📚 **Overview:** How to build **relative frequency** \(f(x_i)\) and **cumulative distribution** \(F(x_i)\) tables (HSG exam style).

---

## Learning Objectives

After completing this section, you will be able to:
- Build a frequency table from counts \(n_i\)
- Compute relative frequencies \(f(x_i)\)
- Compute cumulative frequencies \(F(x_i)\)
- Answer typical exam questions like “How many observations are ≤ k?”

---

## Key definitions (what you write on paper)

Assume you have categories or grouped values \(x_i\) with counts \(n_i\), and total:

$$
n = \\sum_i n_i
$$

### Relative frequency

$$
f(x_i) = \\frac{n_i}{n}
$$

### Cumulative distribution (relative cumulative frequency)

$$
F(x_i) = \\sum_{j\\le i} f(x_j)
$$

### Cumulative count (sometimes requested)

$$
N(x_i) = \\sum_{j\\le i} n_j
$$

---

## Worked Example (Übungsblatt style)

A survey of 2567 households recorded persons per household:

| Persons \(x_i\) | Count \(n_i\) |
|---|---:|
| 1 | 457 |
| 2 | 628 |
| 3 | 612 |
| 4 | 526 |
| ≥ 5 | 344 |

Tasks:
1) Compute \(f(x_i)\) and \(F(x_i)\)  
2) How many households have ≤ 3 persons?

<details>
<summary>💡 Show Solution</summary>

Total:

$$
n = 457+628+612+526+344 = 2567
$$

| Persons \(x_i\) | Count \(n_i\) | \(f(x_i)=n_i/n\) | \(F(x_i)\) | Cum. count \(N(x_i)\) |
|---|---:|---:|---:|---:|
| 1 | 457 | 0.1780 | 0.1780 | 457 |
| 2 | 628 | 0.2446 | 0.4226 | 1085 |
| 3 | 612 | 0.2384 | 0.6610 | 1697 |
| 4 | 526 | 0.2049 | 0.8659 | 2223 |
| ≥ 5 | 344 | 0.1340 | 0.9999 ≈ 1.0000 | 2567 |

Households with ≤ 3 persons:

$$
N(x\\le 3) = 457+628+612 = 1697
$$

(Equivalent using \(F(3)\\): \(0.6610\\cdot 2567\\approx 1697\\).)

</details>

---

## Open-ended classes (≥ 5, ≥ 100, …)

If a class is open-ended (e.g., “≥ 5”), you can still compute \(f(x_i)\) and \(F(x_i)\) exactly.

But if a task asks for a **mean** based on class values, you must **approximate** a representative value (a midpoint or a chosen value), and state that this can bias the result.

---

## Practice Problems

### Problem 1

A bank records the number of credit cards per customer:

| Cards \(x_i\) | Count \(n_i\) |
|---|---:|
| 0 | 40 |
| 1 | 110 |
| 2 | 90 |
| 3 | 60 |

Tasks:
1) Compute \(f(x_i)\) and \(F(x_i)\)  
2) How many customers have **at most 1** card?

<details>
<summary>💡 Show Solution</summary>

\(n=40+110+90+60=300\\).

| \(x_i\) | \(n_i\) | \(f(x_i)\) | \(F(x_i)\) | \(N(x_i)\) |
|---|---:|---:|---:|---:|
| 0 | 40 | 0.1333 | 0.1333 | 40 |
| 1 | 110 | 0.3667 | 0.5000 | 150 |
| 2 | 90 | 0.3000 | 0.8000 | 240 |
| 3 | 60 | 0.2000 | 1.0000 | 300 |

At most 1 card: \(N(x\\le 1)=40+110=150\\).\n+
At most 1 card: \(N(x\\le 1)=40+110=150\\).
</details>

---

## Navigation

[← Variance & Standard Deviation](variance_stddev.md) | [Module Index](index.md) | [Next: Quartiles & Box Plots →](quartiles_boxplots.md)


