---
title: "Quiz 8"
notion_id: "21074ffd-3319-806d-8a53-fc1c8d94b143"
notion_url: "https://www.notion.so/Quiz-8-21074ffd3319806d8a53fc1c8d94b143"
exported_at: "2025-12-13T23:01:02.292328+00:00"
---

# Quiz 8

## Question 1
↪️ [Check here](/73d1ad1d44a740a993f4ba6f9e8f51e4#5c91315536c54105b46f5e7d40675452)
---
## Question 2
↪️ [Check here](/73d1ad1d44a740a993f4ba6f9e8f51e4#b25a1d2587414017a35e6974ec7efb2b)
---
## Question 3
↪️ [Check here](/73d1ad1d44a740a993f4ba6f9e8f51e4#35a174a258e04d368882fd45fb4f721f)
---
## Question 4
Gegeben ist folgender *pd.DataFrame df*. Die Spalte **index** ist definiert als der Index von df.
| index | value0 | value1 |
| --- | --- | --- |
| 0 | 555 | 383 |
| 21 | 926 | 31 |
| 9 | 133 | 63 |
| 25 | 350 | 9 |
| 31 | 456 | 461 |
| 5 | 850 | 497 |
| 11 | 311 | 891 |
| 12 | 580 | 406 |
| 34 | 431 | 321 |
Welcher **Wert** wird von folgendem Code zurückgegeben: *df.loc[25].sum()*
**359**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.sum()](/1867045b058343e1a66b677961515907#6f1bd7bccbe24ecf8bcb37abc05b0550)**
1. **DataFrame Structure**:
- The DataFrame `df` has three columns: `index`, `value0`, and `value1`.
- The `index` column is set as the index of the DataFrame, meaning it is used to label the rows.
```plain text
| index | value0 | value1 |
|-------|--------|--------|
| 0     | 555    | 383    |
| 21    | 926    | 31     |
| 9     | 133    | 63     |
| 25    | 350    | 9      |
| 31    | 456    | 461    |
| 5     | 850    | 497    |
| 11    | 311    | 891    |
| 12    | 580    | 406    |
| 34    | 431    | 321    |
```
1. **Code Explanation**:
- `df.loc[25]`:
- This line accesses the row in the DataFrame where the index is `25`.
- The row with index `25` is:
```plain text
| index | value0 | value1 |
|-------|--------|--------|
| 25    | 350    | 9      |
```
- `.sum()`:
- This method sums up all the values in the selected row.
- For the row with index `25`, the values are `350` and `9`.
- Summing these values:
```plain text
350 + 9 = **359**
```
</details>
---

