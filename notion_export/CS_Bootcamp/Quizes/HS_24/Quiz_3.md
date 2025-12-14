---
title: "Quiz 3"
notion_id: "17074ffd-3319-80ea-8b8f-e6b0e15ed7ca"
notion_url: "https://www.notion.so/Quiz-3-17074ffd331980ea8b8fe6b0e15ed7ca"
exported_at: "2025-12-13T23:04:28.895732+00:00"
---

# Quiz 3

# Question 1
Given is the following signature of a function:
```python
def blueprint(text="sum", start=0, end=10):
```
Which of the following options calls the function successfully? Mark all correct options!
✅ `blueprint(end=10, text="sum", start=0)`
✅ `blueprint("sum", 3, 9)`
✅ `blueprint("division", 0, 5)`
✅ `blueprint("sum")`
❌ `blueprint(end=10, text="sum", start=0, True)`
❌ None of the above.

<details>
<summary>Explanation</summary>

> 💡 **[Optional parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc)**
The function `blueprint` has a signature with default values for its parameters: `text="sum"`, `start=0`, and `end=10`. This means you can call the function without providing any arguments, and it will use these default values. However, you can also provide arguments to override these defaults.
Let's look at each option:
✅ **Correct, **this call uses keyword arguments to specify values for `end`, `text`, and `start`. The order of keyword arguments doesn't matter as long as they match the parameter names.
✅ **Correct, **this call uses positional arguments. The first argument `"sum"` is for `text`, `3` is for `start`, and `9` is for `end`. This matches the order of parameters in the function signature.
✅ **Correct, **similar to the previous option, this call uses positional arguments. `"division"` is for `text`, `0` is for `start`, and `5` is for `end`.
✅ **Correct, **the** **call provides only the first positional argument `"sum"` for `text`. The other parameters `start` and `end` will use their default values `0` and `10`.
❌ **Incorrect, **because it mixes keyword arguments with a positional argument (`True`) after them. In Python, once you start using keyword arguments, all subsequent arguments must also be keyword arguments. Mixing them in this way is not allowed.
❌ **Incorrect,** because there are indeed correct ways to call the function, as shown in the previous options.
</details>
---
## Question 2
We all know that **tuple** and **string** variables are *immutable*. Please assume a tuple *t1* that contains a **list** object. This **list** contains (among others) a *string* object. Can this specific **list element** be replaced with another *string* object?
✅ True
❌ False

<details>
<summary>Explanation</summary>

> 💡 **[Immutability of tuples](/5b0832dbf9454eb1941b7632e68a9abb#f89004e9cdc3442889aebbf8ba334659)**
The question is about the immutability of tuples and strings, and whether a list inside a tuple can have its elements changed.
1. **Tuples** are immutable:
- This means that once a tuple is created, you cannot change, add, or remove its elements. However, if a tuple contains a mutable object, like a list, the contents of that list can be changed.
1. **Strings** are immutable:
- Once a string is created, you cannot change its characters. You can, however, replace the entire string with a new one.
1. **Lists** are mutable:
- Lists can have their elements changed, added, or removed after they are created.
Now, let's consider the scenario described in the question:
- You have a tuple `t1` that contains a list. This list, in turn, contains a string.
- The question asks if the list element (the string) can be replaced with another string.
The correct answer is ✅ **True** as although the tuple itself is immutable, the list inside it is mutable. This means you can change the elements of the list, including replacing a string with another string. Here's a simple example:
```python
t1 = ([1, 2, 3, "hello"],)  # A tuple containing a list
t1[0][3] = "world"          # Replacing the string "hello" with "world" in the list
```
- In this example, `t1` is a tuple containing one element, which is a list `[1, 2, 3, "hello"]`.
- `t1[0]` accesses the list inside the tuple.
- `t1[0][3]` accesses the fourth element of the list, which is the string `"hello"`.
- We replace `"hello"` with `"world"`, demonstrating that the list element can indeed be replaced.
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

What is the *value* of the variable d after the execution?
- ❌ (3, 7)
- ❌ *list*
- ❌ [3, 7]
- ❌ tuple
- ❌ 8
- ✅ *Something else not listed.*
- ❌ (3, 8)

<details>
<summary>Explanation</summary>

> 💡 **[Nested lists](/5b0832dbf9454eb1941b7632e68a9abb#5d06cfcdb5574513a592b854a821fe3e)**
### Code explanation
Let's go through the code step by step to understand what the value of the variable `d` is after the execution:
1. `a = [1, 2, (3, 4, '2'), 5]`
- This line creates a list `a` with four elements: the integers `1` and `2`, a tuple `(3, 4, '2')`, and the integer `5`.
1. `b = a[1] + a[2][0]`
- `a[1]` accesses the second element of the list `a`, which is `2`.
- `a[2][0]` accesses the first element of the tuple `(3, 4, '2')`, which is `3`.
- The expression `a[1] + a[2][0]` adds these two values: `2 + 3`, resulting in `b = 5`.
1. `c = (b, (a[2][1], b + 2))`
- `b` is `5`, as calculated previously.
- `a[2][1]` accesses the second element of the tuple `(3, 4, '2')`, which is `4`.
- `b + 2` calculates `5 + 2`, resulting in `7`.
- The tuple `c` is created as `(5, (4, 7))`.
1. `d = c[1][1]`
- `c[1]` accesses the second element of the tuple `c`, which is the tuple `(4, 7)`.
- `c[1][1]` accesses the second element of the tuple `(4, 7)`, which is `7`.
- Therefore, `d = 7`.
### Answer Explanations
❌ (3, 7): **Incorrect**, because `d` is not a tuple; it's a single value `7`.
❌ list: **Incorrect,** because `d` is not a list; it's a single integer value.
❌ [3, 7]: **Incorrect,** because `d` is not a list; it's a single integer value.
❌ tuple: **Incorrect,** because `d` is not a tuple; it's a single integer value.
❌ 8: **Incorrect,** because `d` is `7`, not `8`.
✅ Something else not listed.: **Correct**, because the value of `d` is `7`, which is not explicitly listed in the options.
❌ (3, 8):**Incorrect,** because `d` is not a tuple; it's a single integer value.
</details>
---
## Question 4
Look at the following code snippet:
```python
def sum_double_numbers(start, end, step=2):
    r = 0
    for i in range(start, end, step):
        r += i * 2
    return r
```
Mark all correct statements regarding this function definition.
✅ The function **sum_double_numbers** needs at least 2 and can take at most 3 arguments/parameters.
✅ If called syntactically correct, the function **sum_double_numbers** can return the sum of the doubled values of all integers between the given **start** (inclusive) and **end** (exclusive) parameter.
✅ The return value is **0** if the function is called with: **sum_double_numbers(10, 1)**.
❌ The function **sum_double_numbers** can be called by **sum_double_numbers()**, i.e., without explicitly giving any argument, and will be executed without raising an error.
❌ If called syntactically correct, the function **sum_double_numbers** returns the sum from all integers between the given **start** (inclusive) and **end** (exclusive) parameter.
✅ The return value is **6** if the function is called with: **sum_double_numbers(1, 3, 1)**.
✅ The return value is **4** if the function is called with: **sum_double_numbers(0, 4)**.
❌ *The function definition is incorrect. None of the statements are true.*

<details>
<summary>Explanation</summary>

> 💡 **[Range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385), [optional parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc), [augmented assignments](/5b0832dbf9454eb1941b7632e68a9abb#30b886f101854a3ca81b231e9cda05a3)**
### Code Explanation
```python
def sum_double_numbers(start, end, step=2):
    r = 0
    for i in range(start, end, step):
        r += i * 2
    return r
```
- **Function Definition**: The function `sum_double_numbers` is defined to take three parameters: `start`, `end`, and an optional `step` with a default value of 2.
- **Variable Initialization**: `r` is initialized to 0. This variable will store the sum of doubled numbers.
- **Loop**: The `for` loop iterates over a range of numbers starting from `start` to `end` (exclusive), incrementing by `step`.
- **Doubling and Summing**: Inside the loop, each number `i` is doubled (`i * 2`) and added to `r`.
- **Return Statement**: The function returns the accumulated sum `r`.
### Answer Explanations
✅ **Correct**, the function requires at least `start` and `end` parameters. The `step` parameter is optional because it has a default value of 2. Therefore, the function can take 2 or 3 arguments.
✅ **Correct**, the function doubles each integer in the specified range and sums them up, which matches the description.
✅ **Correct**, the range `range(10, 1, 2)` is empty because the start is greater than the end. Therefore, the loop doesn't execute, and `r` remains 0.
❌ **Incorrect**, the function requires at least the `start` and `end` arguments. Calling it without any arguments will raise a `TypeError` because these required arguments are missing.
❌ **Incorrect**, the function returns the sum of the doubled values, not just the sum of the integers themselves.
✅ **Correct**, the range `range(1, 3, 1)` includes the numbers 1 and 2. Doubling these gives 2 and 4, respectively. Their sum is 6.
✅ **Correct**, the range `range(0, 4, 2)` includes the numbers 0 and 2. Doubling these gives 0 and 4, respectively. Their sum is 4.
❌ **Incorrect**, the function definition is correct, and several statements about it are true, as explained above.
</details>
---
## Question 5
Given is the following function:
```python
def get(elements):
	to_return = []
	for element in elements:
		if isinstance(element, int):
		to_return += [element]
	return to_return[::-1]
```
What does the function **get** do? You can assume that the usage is correct!
❌ It returns the last *even* *integer* of the given list **elements**. 
❌ It returns the first *even* *integer* of the given list **elements**. 
✅ It returns the list of *integers* of the given list **elements** in reverse order.
❌ It *always* return the value **0**. 
❌ It returns the list of *integers* of the given list **elements** in their original order. 

<details>
<summary>Explanation</summary>

> 💡 **[For-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [type checking](/5b0832dbf9454eb1941b7632e68a9abb#6f8e8203d09a4c3aafa6f5d78119fe00)**
### Code Explanation
1. `def get(elements):`
- This line defines a function named `get` that takes one parameter, `elements`, which is expected to be a list.
1. `to_return = []`
- This line initializes an empty list called `to_return`. This list will be used to store integers found in the `elements` list.
1. `for element in elements:`
- This line starts a loop that goes through each item in the `elements` list, one by one.
1. `if isinstance(element, int):`
- This line checks if the current `element` is an integer. The `isinstance` function returns `True` if `element` is of type `int`.
1. `to_return += [element]`
- If the `element` is an integer, it is added to the `to_return` list. The `+=` operator is used to append the integer to the list.
1. `return to_return[::-1]`
- This line returns the `to_return` list, but in reverse order. The `[::-1]` slice notation is used to reverse the list.
### Answer Explanations
❌ **Incorrect, **the function does not specifically look for even integers. It collects all integers and returns them in reverse order.
❌ **Incorrect, s**imilar to the previous option, the function does not focus on even integers. It collects all integers.
✅ **Correct,** because the function collects all integers from the `elements` list and returns them in reverse order.
❌ **Incorrect, **because the** **function does not always return 0. It returns a list of integers found in the input list, reversed.
❌ **Incorrect, **because the function returns the list of integers in reverse order, not in their original order.
</details>
---

