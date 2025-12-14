---
title: "Quiz 3"
notion_id: "74acad64-83e4-45ac-9118-fd9c2ff48f1b"
notion_url: "https://www.notion.so/Quiz-3-74acad6483e445ac9118fd9c2ff48f1b"
exported_at: "2025-12-13T23:18:05.032549+00:00"
---

# Quiz 3

## Question 1
Given the following code snippet:
```python
a = [1, 2, (3, 4), 5]
b = a[1] + a[2][1]
c = (b, (a[2][0], b + 2))
d = c[1]
```
What is the value of the variable **d** after the execution?
✅  `(3, 8)`
❌  `[3, 7]`
❌  `(3, 7)`
❌  Can’t be determined.
❌  Something else not listed.
❌  `8`

<details>
<summary>Explanation</summary>

Here it is important that you understand how we can [access elements in a nested list](/5b0832dbf9454eb1941b7632e68a9abb#8526be0c72d1432c83067d8315535bd0).
The table below shows line-by-line the values of each variable.
| Line | a | b | c | d |
| --- | --- | --- | --- | --- |
| 1 | `[1, 2, (3, 4), 5]` |  |  |  |
| 2 | `[1, 2, (3, 4), 5]` | `a[1]` → 2
`a[2][1]` → 4

2 + 4 = **6** |  |  |
| 3 | `[1, 2, (3, 4), 5]` | 6 | `b` → 6
`a[2][1]` → 3

**`(6, (3, 8))`** |  |
| 4 | `[1, 2, (3, 4), 5]` | 6 | `(6, (3, 8))` | `c[1]` → **`(3, 8)`** |
</details>
---
## Question 2
We all know that *tuple* are *immutable*, so can the following code snippet be run *without an error*?
```python
t = (1, 2)
t += (3, 4)
```
✅  True
❌  False

<details>
<summary>Explanation</summary>

After executing this code the tuple `(1, 2, 3, 4)` is saved in variable `t`. We can see that the integers 3 and 4 were appended to the existing tuple. However, [compared to lists tuples are still immutable](/5b0832dbf9454eb1941b7632e68a9abb#f89004e9cdc3442889aebbf8ba334659). This means we cannot modify an existing element or delete an element, but we can add more elements to a tuple as we have just seen:
✅  Add more elements
```python
t = (1, 2)
t += (3, 4)

print(t)
(1, 2, 3, 4)
```
❌  Delete an element
```python
del t[3] 

TypeError: 'tuple' object doesn't support item deletion
```
❌  Modify an element
```python
t[2] = t[2] + 5

TypeError: 'tuple' object does not support item assignment
```
</details>
---
## Question 3
Given is the following function:
```python
def get(elements):
	to_return = 0
	for value in elements:
		if isinstance(value, int) and value % 2 == 1:
			to_return = value
			break
	return to_return
```
❌  It returns the last *even integer* of the given list **elements**.
❌  It returns the first even integer of the given list **elements**.
✅  It returns the first *odd integer* of the given list **elements**.
❌  It returns the last *odd integer* of the given list **elements**.
❌  It *always* returns the value **0**.

<details>
<summary>Explanation</summary>

Let’s assume:
`elements = [6.5, 4, 5, 3]`
`get(elements)`
- 1st run of for-loop
- `value = 6.5`
- `isinstance(6.5, int) and 6.5 % 2 == 1` → `False`` and ``False` → **`False`**
- `isinstance(6.5, int)` → `False`
- `6.5 % 2 == 1` → `0.5 == 1`→ `False`
- 2nd run of for-loop
- `value = 4`
- `isinstance(4, int) and 4 % 2 == 1` → `True`` and ``False` → **`False`**** **
- `isinstance(4, int)` → `True`
- `4 % 2 == 1` → `0 == 1`→ `False`
- 3rd run of for-loop
- `value = 5`
- `isinstance(5, int) and 5 % 2 == 1` → `True`` and ``True` → **`True`**
- `isinstance(5, int)` → `True`
- `5 % 2 == 1` → `1 == 1`→ `True`
- `to_return = 5`
- `break`
- `return 5`

> ❗ **5 was the first odd integer in `elements`
Remember that the [break statement](/5b0832dbf9454eb1941b7632e68a9abb#4d9ef2de33854aae9818e50cbf61907d) makes Python exit the for-loop immediately and to proceed with the first line after the for-loop**
</details>
---
## Question 4
Look at the following code snippet:
```python
def sum_numbers(start=0, end=10):
	result = 0
	new_end = end + 1
	for i in range(start, new_end):
		result += i
	return result
```
Mark all correct statements regarding this function definition:
❌  The function **sum_numbers** can take at most 1 argument/parameter.
✅  The return value is **1** if the function is called with: **sum_numbers(1,1)**.
✅  The return value is **15** if the function is called with: **sum_numbers(4,6**).
❌  The function **sum_numbers** returns the sum from all integers between the given **start** (inclusive) and **end** (exclusive) parameter.
✅  The function **sum_numbers** can be called by **sum_numbers()**. Meaning, without explicitly giving any parameter.
✅  The function **sum_numbers** returns the sum from all integers between the given **start** (inclusive) and **end **(inclusive) parameter.
❌  The return value is **9** if the function is called with: **sum_numbers(4,6)**
❌  The return value is **0** if the function is called with: **sum_numbers(1,1)**
❌  The function definition is incorrect. None of the statements are true.

<details>
<summary>Explanation </summary>

❌ **Incorrect**, because we see in the function header that it has two parameters: `start` and `end`.
✅ **Correct**, because when we provide 1 and 1 as inputs then we get 1 back. Check below what the function is executing in detail.
<details>
<summary>Step-by-step execution</summary>

`sum_numbers(1, 1)`
`start = 1`, `end = 1`
`result = 0`
`new_end = 1 + 1` → `2`
`for i in range(1, 2)` → `[1]`
- 1st run of for-loop
- `i = 1`
- `result = 0 + 1` → `1`
`return 1`
</details>
✅ **Correct**, because when we provide 4 and 6 as input parameters we get back 15.
<details>
<summary>Step-by-step execution</summary>

`sum_numbers(4, 6)`
`start = 4`, `end = 6`
`result = 0`
`new_end = 6 + 1` → `7`
`for i in range(4, 7)` → `[4, 5, 6]`
- 1st run of for-loop
- `i = 4`
- `result = 0 + 4` → `4`
- 2nd run of for-loop
- `i = 5`
- `result = 4 + 5` → `9`
- 3th run of for-loop
- `i = 6`
- `result = 9 + 6` → `15`
`return 15`
</details>
❌ **Incorrect**, because the function returns the som from all integers between the start and end parameter, inclusive **both**. This is why there is `new_end = end + 1`, so that the integer provided for the parameter `end` is included in the number range as well. So the wrong part in this statement is *end *~~*(exclusive)*~~*. *To become a correct statement this part would have to be replaced with *end (*<u>*inclusive*</u>*).*
✅ **Correct**, because the parameters are optional. We can identify [optional parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc) by the equal sign `=` after the parameter name and the default values. Thos values get assigned to the parameters when no parameter values were provided by the function caller. For example, when we would call the function like `sum_numbers()`, then `0` would be assigned to `start` and `10` to `end`.
✅ **Correct**, because [Statement 4 is incorrect](/74acad6483e445ac9118fd9c2ff48f1b#e8b9ab0a98bd41b9831445b2e614619c).
❌ **Incorrect**, because the return value is 15. Check the explantation [here](/74acad6483e445ac9118fd9c2ff48f1b#0b3cfc5d1a594248a4c881ee38df011c).
❌ **Incorrect**, because the return value is 1. Check the explanation [here](/74acad6483e445ac9118fd9c2ff48f1b#40acacd2c26441eb8c10ed1b9ec324d8).
❌ **Incorrect**, because statement 2, 3, 5 and 6 are correct.
</details>
---
## Question 5
Given is the following code snippet: 
```python
def fizz(buzz):
	result = []
	for i in range(1,4):
		if buzz % 2 == 0:
			buzz -= 2
		elif buzz % 2 == 1:
			buzz += 2
		result.append(buzz)
	return list(reversed(result))

r = fizz(6)
```
What is the value of **r** after the execution?
❌  None
❌  [4, 2, 0] 
✅  [0, 2, 4]
❌  *Can’t be determined.* 
❌  (0, 2, 4)
❌  (4, 2, 0)

<details>
<summary>Explanation</summary>

To determine the right answer, let’s have a look at the step-by-step execution of the function. 
`fizz(6)`
`buzz = 6`
`result = []`
`for i in range(1, 4)` → `[1, 2, 3]`
- 1st run of for-loop
- `i = 1`
- `if 6 % 2 == 0` → `0 == 0` → True
- `buzz = 6 - 2`
- `buzz = 4`
- `result.append(4)`
- `result = [4]`
- 2nd run of for-loop
- `i = 2`
- `if 4 % 2 == 0` → `0 == 0` → True
- `buzz = 4 -2`
- `buzz = 2`
- `result.append(2)`
- `result = [4, 2]`
- 3rd run of for-loop
- `i = 3`
- `if 2 % 2 == 0` → `0 == 0` → True
- `buzz = 2 - 2`
- `buzz = 0`
- `result.append(0)`
- `result = [4, 2, 0]`
`return list(reversed([4, 2, 0]))` → **`[0, 2, 4]`**
`reversed([4, 2, 0])` → `list_reverseiterator object`
`list(list_reverseiterator object)` → `[0, 2, 4]`
We see that eventually the list `[0, 2, 4]` is returned from the function and saved in `r`.
</details>
---
## Question 6
Given is the following signature of a function:
```python
def blueprint(text, start, end=10)
```
Which of the following options calls the function **successfully**? Mark all correct options!
✅  `blueprint("diff", 5)`
❌  `blueprint("sum")`
✅  `blueprint("sum", 3, 9)`
❌  `blueprint()`

<details>
<summary>Explanation</summary>

When we have a look at the function header we see that `text` and `start` are mandatory parameters and `end` is an [optional parameter](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc). This means that in case no value is provided for `end` parameter, i.e., the function caller provides only two parameter values, then the value 10 is assigned to parameter `end`. 
✅ **Correct**, because two values are provided, i.e., for all mandatory parameters:
`text = "diff"`, `start = 5`, `end = 10`
❌ **Incorrect**, because only one value is provided although there are two mandatory parameters. This one value gets assigned to the parameter `text` so a value is missing for `start`:
`text = "sum"`, `start = `**`?`****, **`end = 10`
** **✅ **Correct**, because three values are provided, for the two mandatory ones and also for the optional `end` parameter.
`text = "sum"`, `start = 3`, `end = 9`
❌ **Incorrect**, because no values are provided. Thus, no values can be assigned to `text` and `end`.
`text = ?`, `start = `**`?`****, **`end = 10`
</details>
---
