---
title: "Explanation Exercise 2.3"
notion_id: "9043e089-2502-4608-b74a-930eece54df7"
notion_url: "https://www.notion.so/Explanation-Exercise-2-3-9043e08925024608b74a930eece54df7"
exported_at: "2025-12-14T01:06:31.518140+00:00"
---

# Explanation Exercise 2.3

[https://colab.research.google.com/drive/1SLKZWJMNM1eXkSOVjHZ0wCGLdPnWD66D?usp=sharing](https://colab.research.google.com/drive/1SLKZWJMNM1eXkSOVjHZ0wCGLdPnWD66D?usp=sharing)
<details>
<summary>i) `maximum_value = maximum_or_not(1, 2, 3)` → **D) 3**</summary>

In this case, `value1 = 1`, `value2 = 2`, `value3 = 3`.
The if condition `value1 > max(value2, value3, *value4)` is not satisfied, so we skip it.
Then we go into the for loop, but `value4` is empty, so it does nothing.
Then we check `if len(value4) == 0 and (value2 > value3)`, but `value2` is not greater than `value3`, so we skip it.
Finally, we return `max(maximum_value, value3)`, which is `max(0, 3)`.
Hence, the answer is **D) 3**.
</details>
<details>
<summary>ii) `maximum_value = maximum_or_not(3, 2, 2)` →  **E) 3**</summary>

In this case, `value1 = 3`, `value2 = 2`, `value3 = 2`.
The if condition `value1 > max(value2, value3, *value4)` is satisfied, so we return `value1` which is equal to 3.
</details>
<details>
<summary>iii) `maximum_value = maximum_or_not(1, 2)` → **E) 100**</summary>

In this case, `value1 = 1`, `value2 = 2`, `value3 = 100` (default value). 
The if condition `value1 > max(value2, value3, *value4)` is not satisfied, so we skip it.
Then we go into the for loop, but `value4` is empty, so it does nothing. 
Then we check `if len(value4) == 0 and (value2 > value3)`, but `value2` is not greater than `value3`, so we skip it.
Finally, we return `max(maximum_value, value3)`, which is `max(0, 100)`. 
Hence, the answer is **E) 100**.
</details>
<details>
<summary>iv) `maximum_value = maximum_or_not(1, 1, 1, 1)` → **B) 1**</summary>

In this case, `value1 = 1`, `value2 = 1`, `value3 = 1`, `value4 = [1]`. 
The if condition `value1 > max(value2, value3, *value4)` is not satisfied, so we skip it.
Then we go into the for loop, but none of the conditions inside the loop are satisfied. 
Finally, we return `max(maximum_value, value3)`, which is `max(0, 1)`. 
Hence, the answer is **B) 1**.
</details>
<details>
<summary>v) `maximum_value = maximum_or_not(1, 1, 1, 1, 1, 1, 1, 1, 2, 1)` → **C) 2**</summary>

In this case, `value1 = 1`, `value2 = 1`, `value3 = 1`, `value4 = [1, 1, 1, 1, 2, 1]`. 
The if condition `value1 > max(value2, value3, *value4)` is not satisfied, so we skip it.
Then we go into the for loop, and `maximum_value` gets updated to `2` when `value = 2`.
Finally, we return `max(maximum_value, value3)`, which is `max(2, 1)`. 
Hence, the answer is **C) 2**.
</details>
<details>
<summary>vi) `maximum_value = maximum_or_not(value3=1, value2=1, value1=100)` → **E) 100**</summary>

In this case, `value1 = 100`, `value2 = 1`, `value3 = 1`. 
The if condition `value1 > max(value2, value3, *value4)` is satisfied, so we return `value1`. 
Hence, the answer is **E) 100**.
</details>
<details>
<summary>vii) `maximum_value = maximum_or_not(value3=1, value2=1, value1=100, 300)` → **H) An Error/Exception is raised**</summary>

In this case, the function call is incorrect because positional argument follows keyword argument. Hence, an error is raised. 
</details>
<details>
<summary>viii) `maximum_value = maximum_or_not(300, value3=1, value2=1)` → **G) 300**</summary>

In this case, `value1 = 300`, `value2 = 1`, `value3 = 1`. 
The if condition `value1 > max(value2, value3, *value4)` is satisfied, so we return `value1`. 
Hence, the answer is **G) 300**.
</details>
<details>
<summary>ix) `maximum_value = maximum_or_not(100, value3=1, value2=200, 300)` → **H) An Error/Exception is raised**</summary>

In this case, the function call is incorrect because positional argument follows keyword argument. Hence, an error is raised. 
</details>
