---
title: "Math operations"
notion_id: "3ab00512-198e-49db-a6a1-02e5ed4eb4be"
notion_url: "https://www.notion.so/Math-operations-3ab00512198e49dba6a102e5ed4eb4be"
exported_at: "2025-12-13T22:48:36.806512+00:00"
---

# Math operations

## Question 1 - Modulo operator
Create a Python function `mod_div` that uses the modulo operator to determine divisibility and prints a custom message for each case. The function should:
1. Take two arguments, an integer `num` and an integer `divisor`.
1. Use the modulo operator to check if `num` is divisible by `divisor`.
1. Print "num is divisible by divisor" if `num` is divisible by `divisor`.
1. Print "num is not divisible by divisor" if `num` is not divisible by `divisor`.
Write the definition of the function and some example calls to the function for values `num = 10` and `divisor = 2`, as well as `num = 10` and `divisor = 3`.
For example, calling the function as mod_div(20, 5) should print “*20 is divisible by 5”.*
<details>
<summary>Solution</summary>

```python
def mod_div(num, divisor):
    if num % divisor == 0:
        print(f"{num} is divisible by {divisor}")
    else:
        print(f"{num} is not divisible by {divisor}")

# Example calls to the function:
mod_div(10, 2)
mod_div(10, 3)
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition (****`def mod_div(num, divisor):`****)**: Define a function named `mod_div` that takes two parameters, `num` and `divisor`.
1. **Modulo Check** (`if num % divisor == 0:`): Use the modulo operator `%` to check if the remainder of `num` divided by `divisor` is zero. This determines if `num` is divisible by `divisor`.
1. **Print Statement for Divisibility** (`print(f"{num} is divisible by {divisor}")`): If the above condition is true, print a message indicating that `num` is divisible by `divisor`.
1. **Else Statement** (`else:`): If the modulo operation does not yield zero, the control goes to the else block.
1. **Print Statement for Non-Divisibility** (`print(f"{num} is not divisible by {divisor}")`): In the else block, print a message indicating that `num` is not divisible by `divisor`.
1. **Example Call 1** (`mod_div(10, 2)`): Call the function with `num = 10` and `divisor = 2`. This should print "10 is divisible by 2".
1. **Example Call 2** (`mod_div(10, 3)`): Call the function with `num = 10` and `divisor = 3`. This should print "10 is not divisible by 3".
</details>
</details>
---
## Question 2 - floor division
Write a Python function named `floor_division_pairs` that takes two lists of integers `list1` and `list2` as parameters. The function should iterate through each pair of elements (one from each list at the same index) and perform a floor division of the elements. Specifically, for each index `i`, compute `list1[i] // list2[i]`, and store the result in a new list called `result`. Finally, return the `result` list.
Ensure the lengths of the two lists are equal. If not, print an error message saying "The lists must have the same length."
For example, if you call the function as follows:
```python
floor_division_pairs([10, 20, 30], [3, 4, 5])
```
The return value should be:
```plain text
[3, 5, 6]
```
<details>
<summary>Solution</summary>

```python
def floor_division_pairs(list1, list2):
    if len(list1) != len(list2):
        print("The lists must have the same length.")
        return None

    result = []
    for i in range(len(list1)):
        result.append(list1[i] // list2[i])

    return result
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def floor_division_pairs(list1, list2):
```
This line defines a function named `floor_division_pairs` which takes two lists `list1` and `list2` as its parameters.
1. **Length Check**:
```python
if len(list1) != len(list2):
```
This line checks if the lengths of `list1` and `list2` are not equal.
1. **Error Message and Return**:
```python
print("The lists must have the same length.")
return None
```
If the lengths are not equal, an error message is printed and the function returns `None`.
1. **Result List Initialization**:
```python
result = []
```
This line initializes an empty list `result` which will store the results of the floor divisions.
1. **For Loop**:
```python
for i in range(len(list1)):
```
This line begins a `for` loop that iterates through the indices of the lists.
1. **Floor Division and Append**:
```python
result.append(list1[i] // list2[i])
```
This line performs the floor division of the elements from `list1` and `list2` at index `i`, then appends the result to the `result` list.
1. **Return Result**:
```python
return result
```
Finally, this line returns the `result` list that contains the floor division results of pairs of elements from the input lists.
</details>
</details>
---


