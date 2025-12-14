---
title: "Regression Cheat Sheet"
category: "Statistics Bootcamp"
module: 99
order: 12
---

# Regression Cheat Sheet

> Simple linear regression (OLS): what to compute and what to write.

---

## Model

$$
y = \beta_0 + \beta_1 x + \varepsilon
$$

---

## OLS formulas (deviation form)

$$
\hat{\beta}_1 = \frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sum (x_i-\bar x)^2}
$$

$$
\hat{\beta}_0 = \bar y - \hat{\beta}_1\bar x
$$

---

## OLS formulas (raw-score shortcut)

$$
\hat{\beta}_1 = \frac{\sum x_iy_i - n\bar x\bar y}{\sum x_i^2 - n\bar x^2}
$$

$$
\hat{\beta}_0 = \bar y - \hat{\beta}_1\bar x
$$

---

## Table columns (Übungsblatt-style)

Common deviation-table columns:

- \(x_i\), \(y_i\)
- \(x_i-\bar x\), \(y_i-\bar y\)
- \((x_i-\bar x)(y_i-\bar y)\)
- \((x_i-\bar x)^2\)

Optional (for fit diagnostics):

- \(\hat y_i = \hat\beta_0 + \hat\beta_1 x_i\)
- \(e_i = y_i-\hat y_i\)
- \(e_i^2\)

---

## Residual sums and R²

$$
SST = \sum (y_i-\bar y)^2,\quad SSE = \sum (y_i-\hat y_i)^2,\quad SSR = SST-SSE
$$

$$
R^2 = 1-\frac{SSE}{SST}=\frac{SSR}{SST}
$$

---

## Testing the slope

Hypotheses:

- \(H_0:\beta_1=0\)
- \(H_1:\beta_1\ne 0\) (often two-tailed)

Test statistic:

$$
t = \frac{\hat\beta_1}{SE(\hat\beta_1)},\quad df=n-2
$$

---

## Interpretation templates (safe)

- Slope: “A +1 increase in x is associated with about **+\(\hat\beta_1\)** change in y (units), on average.”
- Intercept: “When x = 0, the predicted y is \(\hat\beta_0\)” (often extrapolation).
- R²: “About \(100\cdot R^2\%\) of the variation in y is explained by the model.”


