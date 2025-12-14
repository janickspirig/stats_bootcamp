---
title: "Quiz 3"
notion_id: "7c4ec405-aaa6-4d92-898c-fb002e39b92b"
notion_url: "https://www.notion.so/Quiz-3-7c4ec405aaa64d92898cfb002e39b92b"
exported_at: "2025-12-13T23:22:35.968486+00:00"
---

# Quiz 3

## Question 1
Given is the following function:
```python
def get(elements):
    to_return = []
    for element in elements:
        if isinstance(element, int):
            to_return += [element]
    return to_return[::-1]
```
What does the function get do? You can assume that the usage is correct!
✅ It returns the list of integers of the given list elements in reverse order.
❌ It always return the value 0.
❌ It returns the last even integer of the given list elements.
❌ It returns the first even integer of the given list elements.
❌ It returns the list of integers of the given list elements in their original order.

<details>
<summary>Explanation</summary>

> 💡 **[For-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [type checking](/5b0832dbf9454eb1941b7632e68a9abb#6f8e8203d09a4c3aafa6f5d78119fe00)**
The function `get` takes a list `elements` as an input. It iterates over every element in the list. If the element is an integer (checked using `isinstance(element, int)`), it is added to a new list `to_return`. Finally, the function returns the `to_return` list in reverse order (achieved by `[::-1]`).
<details>
<summary>Example execution</summary>

`get([2, 3, "hello", 4, 4.6, 5])`
| Code | `to_return` | `element` | Comments |
| --- | --- | --- | --- |
| `def get(elements):` | - | - | Function definition |
| `to_return = []` | [] | - | Initialize an empty list for `to_return` |
| `for element in elements:` | [] | - | Loop through each element in the list |
| `if isinstance(element, int):` | [] | 2 | Check if value in `element` is an integer → *True* |
| `to_return += [element]` | [2] | 2 | Add the integer to `to_return` |
| `if isinstance(element, int):` | [2] | 3 | Check if value in `element` is an integer → *True* |
| `to_return += [element]` | [2, 3] | 3 | Add the integer to `to_return` |
| `if isinstance(element, int):` | [2, 3] | 'hello' | Check if value in `element` is an integer → *False* |
| `if isinstance(element, int):` | [2, 3] | 4.6 | Check if value in `element` is an integer → *False* |
| `if isinstance(element, int):` | [2, 3] | 5 | Check if value in `element` is an integer → *True* |
| `to_return += [element]` | [2, 3, 5] | 5 | Add the integer to `to_return` |
| `return to_return[::-1]` | [5, 3, 2] | - | Return the reversed `to_return` list |
</details>

✅ **Correct**, because the function is indeed returning the list of integers of the given list elements in reverse order.
❌ **Incorrect**, the function does not always return the value 0. It returns a list of integers in reverse order.
❌ **Incorrect**, the function does not return the last even integer of the given list elements. It returns all integers in the list, not just the even ones, and in reverse order.
❌ **Incorrect**, the function does not return the first even integer of the given list elements. It returns all integers in the list, not just the even ones, and in reverse order.
❌ **Incorrect**, the function does not return the list of integers of the given list elements in their original order. It returns the list in reverse order.
</details>
---
## Question 2
Look at the following code snippet:
```python
def sum_double_numbers(start, end, step=2):
    r = 0
    for i in range(start, end, step):
        r += i*2
    return r
```
Mark all correct statements regarding this function definition.

❌ The function **sum_double_numbers** can be called by **sum_double_numbers()**, i.e., without explicitly giving any argument, and will be executed without raising an error.
❌ If called syntactically correct, the function **sum_double_numbers** returns the sum from all integers between the given **start** (inclusive) and **end** (exclusive) parameter.
✅ The return value is **0** if the function is called with: **sum_double_numbers(10,1**).
✅ The return value is **4** if the function is called with: **sum_double_numbers(0, 4)**
✅ The function **sum_double_numbers** needs at least 2 and can take at most 3 arguments/parameters.
✅ The return value is **6** if the function is called with: **sum_double_numbers(1, 3, 1)**.
✅ If called syntactically correct, the function **sum_double_numbers** can return the sum of the doubled values of all integers between the given **start** (inclusive) and **end** (exclusive) parameter.
❌ *The function definition is incorrect. None of the statements are true.*

<details>
<summary>Explanation</summary>

> 💡 **[Range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385), [optional parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc), [augmented assignments](/5b0832dbf9454eb1941b7632e68a9abb#30b886f101854a3ca81b231e9cda05a3)**
The function `sum_double_numbers(start, end, step=2)` takes three parameters, where `start` and `end` are mandatory and `step` is optional with a default value of 2. The function will iterate over the range from `start` to `end` (exclusive), incrementing by `step` each time, and will double each number in the range and add it to a running total stored in `r`.
<details>
<summary>Example execution</summary>

`sum_double_numbers(2, 9)`
| Code | `i` | `r` | Comments |
| --- | --- | --- | --- |
| `def sum_double_numbers(start, end, step=2):` | - | - | Function definition |
| `r = 0` | - | 0 | Initialize variable `r` to 0 |
| `for i in range(start, end, step):` | 2 | 0 | Loop through range
[<u>**2**</u>, 4, 6, 8] |
| `r += i*2` | 2 | 4 | Add double of 2 to 0 |
| `for i in range(start, end, step):` | 4 | 4 | Loop through range
[2, <u>**4**</u>, 6, 8] |
| `r += i*2` | 4 | 12 | Add double of 4 to 4 |
| `for i in range(start, end, step):` | 6 | 12 | Loop through range
[2, 4, <u>**6**</u>, 8] |
| `r += i*2` | 6 | 24 | Add double of 6 to 12 |
| `for i in range(start, end, step):` | 8 | 24 | Loop through range
[2, 4, 6, <u>**8**</u>] |
| `r += i*2` | 8 | 40 | Add double of 8 to 24 |
| `return r` | - | 40 | Return the final value of `r` |
</details>
❌ **Incorrect**, the function cannot be called without any arguments because `start` and `end` are mandatory parameters. Calling the function without any arguments will raise a `TypeError`.
❌ **Incorrect**, the function doesn't return the sum of all integers between `start` and `end`. It returns the sum of the doubled values of all integers in the range, incremented by `step`.
✅ **Correct**, if the function is called with `sum_double_numbers(10, 1)`, the return value will be 0 because the `start` value is larger than the `end` value, so the range will be empty and the loop will not execute.
✅ **Correct**, if the function is called with `sum_double_numbers(0, 4)`, the return value will be 4. The range will include 0 and 2 (since the step is 2 by default), and the sum of their doubled values is 4.
✅ **Correct**, the function needs at least 2 and can take at most 3 arguments/parameters.
✅ **Correct**, if the function is called with `sum_double_numbers(1, 3, 1)`, the return value will be 6. The range will include 1 and 2, and the sum of their doubled values is 6.
✅ **Correct**, the function `sum_double_numbers` doesn't return the sum of the doubled values of *all* integers between `start` and `end`. Because with the `step` parameter, some integers between start and end are excluded.
❌ **Incorrect**, the function definition is correct. The function can be called with the correct number of arguments and will not raise any error.

</details>
---
## Question 3
Given the following code snippet:
```python
a = [1, 2, (3, 4, '2'), 5]
b = a[1] + a[2][0]
c = (b, (a[2][1], b + 2))
d = c[1][1]
```
What is the *value* of the variable **d** after the execution?
❌ tuple
❌ (3, 8)
❌ [3, 7]
❌ (3, 7)
❌ 8
✅ Something else not listed.
❌ *list*

<details>
<summary>Explanation</summary>

> 💡 **[Nested lists](/5b0832dbf9454eb1941b7632e68a9abb#5d06cfcdb5574513a592b854a821fe3e)**
Let's break down the code line by line:
1. `a` is a list containing four elements, the third of which is a tuple.
1. `b` is the sum of the second element of `a` (which is `2`) and the first element of the third element of `a` (which is `3`).
So, `b = 2 + 3 = 5`.
<details>
<summary>first term : `a[1]` → `2` </summary>

<details>
<summary>second term: `a[2][0]` → `3`</summary>

1. `a[2]` → `(3, 4, '2')`
1. `(3, 4, '2')[0]` → `3`
</details>
1. `c` is a tuple. The first element is `b` (which is `5`), and the second element is another tuple. The first element of this inner tuple is the second element of the third element of `a` (which is `4`), and the second element of the inner tuple is `b + 2` (which is `5 + 2 = 7`).
So, `c = (5, (4, 7))`.
<details>
<summary>first element: `b` → `5`</summary>


</details>
<details>
<summary>second element: `(4, 7)`</summary>

<details>
<summary>first element: `a[2][1]` → `4`</summary>

1. `a[2]` → `(3, 4, '2')`
1. `(3, 4, '2')[1]` → `4`
</details>
<details>
<summary>second element: `b + 2` → `5 + 2` → `7` </summary>

</details>
1.  `d` is the second element of the second element of `c` (which is `7`).
<details>
<summary>`c[1][1]` → `7` </summary>

1. `c[1]` → `(4, 7)`
1. `(4, 7)[1]` → `7`
</details>
So, the correct answer is: **7**, which is not listed as option.
</details>
---
## Question 4
We all know that *tuple* and *string* variables are *immutable*. Please assume a tuple t1 that contains a *list* object. This *list* contains (among others) a *string* object. Can this specific *list element* be replaced with another string object?
✅ True
❌ False

<details>
<summary>Explanation</summary>

> 💡 **[Immutability of tuples](/5b0832dbf9454eb1941b7632e68a9abb#f89004e9cdc3442889aebbf8ba334659)**
While it's true that tuples and strings are *immutable* in Python, meaning their elements cannot be changed once created, the **elements of a list inside a tuple **can be modified. This is because the list itself is a *mutable* data type.
Here's an example:
```python
t1 = (['apple', 'banana'], 'fruit')
print(t1)  # prints (['apple', 'banana'], 'fruit')

# replace 'apple' with 'grape' in the list inside the tuple
t1[0][0] = 'grape'
print(t1)  # prints (['grape', 'banana'], 'fruit')
```
In this example, the string 'apple' in the list inside the tuple `t1` is replaced with 'grape'. This is possible because the list is *mutable*, <u>even though</u> it's inside an *immutable* tuple. So the statement is **True**.
</details>
---
## Question 5
Given is the following signature of a function:
```python
def blueprint(text="sum", start=0, end=10):
```
Which of the following options calls the function successfully? Mark all correct options!
✅ `blueprint(end=10, text="sum", start=0)`
❌ `blueprint(end=10, text="sum", start=0, True)`
✅ `blueprint("sum", 3, 9)`
✅ `blueprint("division", 0, 5)`
✅ `blueprint("sum")`
❌ *None of the above.*

<details>
<summary>Explanation</summary>

> 💡 **[Optional parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc)**
The function `blueprint` has three parameters `text`, `start`, and `end` with default values "sum", 0, and 10, respectively.
This means that none of the parameters are mandatory and the function can be called without any arguments. However, there are two options to provide arguments:
- **keyword arguments **→ we specify the name of the parameter for which we are providing a value, e.g., `start = 0`, any parameters not explicitly defined in the function call will use their default values
- **positional arguments** → python will the assign the first provided value to the first parameter defined in the function header (`text`), the second value to the second parameter (`start`) etc. in cases where the number of arguments provided is less than the parameters defined in the function header, the remaining parameters will use their default values

✅ **Correct**, because all parameters are provided with matching values (*keyword* arguments):
- `"sum"` will be assigned to `text`
- `0` will be assigned to `start`
- `10` will be assigned to `end`
❌ **Incorrect**, because there is an additional argument `True` which does not match any parameter in the function header. Python does not support providing additional arguments that do not match any parameter in the function header.
✅ **Correct**, because the function can be called with these arguments without any error (*postional* arguments).
- `"sum"` will be assigned to `text`
- `3` will be assigned to `start`
- `9` will be assigned to `end`
✅ **Correct**, because the function can be called with these arguments without any error (*postional* arguments).
- `"division"` will be assigned to `text`
- `0` will be assigned to `start`
- `5` will be assigned to `end`
✅ **Correct**, because even though only one value is provided, it will be assigend to the first parameter in the fucntion header (`text`). The other parameters `start` and `end` will use their default values (*positional* arguments):
- `"sum"` will be assigned to `text`
- `0` will be assigned to `start` (default)
- `10` will be assigned to `end` (default)
❌ **Incorrect**, as there are correct options.
</details>
---

