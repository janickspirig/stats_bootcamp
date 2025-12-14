---
title: "Quiz 4"
notion_id: "be03ce9e-a9c1-4f6f-a62a-f002654e4657"
notion_url: "https://www.notion.so/Quiz-4-be03ce9ea9c14f6fa62af002654e4657"
exported_at: "2025-12-13T23:22:02.377478+00:00"
---

# Quiz 4

## Question 1
Look at this code snippet and check all true statements.
```python
def f(x):
    if x == 1:
        return 1
    elif x < 1:
        return -1
    else:
        return x * f(x - 2)
```
❌ For a specific positive value y with (y < 100), one cannot say exactly whether **f(y)** returns a positive or a negative value.
✅ The result of **f(3)** is 3.
❌ f will raise an error with certain arguments, just because it contains more than one return statement.
❌ If f is called with an integer number (int) between 0 and 100 (inclusive) as an argument, the execution of f may never end.
✅ The result of **f(4)** is -8.
❌ f can be executed in standard Python with all positive integer numbers (int) representable in Python as arguments without raising an error.
✅ f can be executed in standard Python with all negative floating point numbers (float) representable in Python as arguments without raising an error.
✅ f is recursive.

<details>
<summary>Explanation</summary>

> 💡 **[Recursive functions](/5b0832dbf9454eb1941b7632e68a9abb#1b1c18524841477bacf6a53bcbc56386)**
❌ **Incorrect**, 🤯 very misleading formulation here… as we can see from statement 2 and 4, for a positive argument `x`, the function can return a positive value *or* a negative value.
✅ **Correct**, the result of `f(3)` is indeed **3**. Check the step-by-step explanation below.
<details>
<summary>`f(3)` → **3**</summary>

`x = 3`
`if x == 1:`
*not executed as 3 is not equal 1*
`elif x < 1:`
*not executed as 3 is not smaller than 1*
`else:`
`return x * f(3 - 2)` → **3 * ****1** → **3**
<details>
<summary>`f(3 - 2)` → **1**</summary>

`number = 1`
`if x == 1:`
`return 1`
`elif x < 1:`
*not checked as if statement evaluated to True*
`else:`
*not executed as if statement evaluated to True*
</details>
</details>
❌ **Incorrect**, having multiple return statements in a function does not cause an error in Python. The function will terminate as soon as it hits a return statement and return the corresponding value, or call itself another time (recursion).
❌ **Incorrect**, for all integer numbers between 0 and 100, the function will always terminate. This is because the recursive call in the else clause always reduces the argument by 2, so eventually it will reach 1 or less than 1 and the recursion will stop.
✅ **Correct**, the result of `f(4)` is **-8**. Check the step-by-step explanation below.
<details>
<summary>`f(4)` → **-8**</summary>

`x = 4`
`if x == 1:`
*not executed as 4 is not equal 1*
`elif x < 1:`
*not executed as 4 is not smaller than 1*
`else:`
`return 4 * f(4 - 2)` → **4 * ****-2** → **-8**
<details>
<summary>`f(4 - 2)` → **-2**</summary>

`x = 2`
`if x == 1:`
*not executed as 2 is not equal 1*
`elif x < 1:`
*not executed as 2 is not smaller than 1*
`else:`
`return 2 * f(2 - 2)` → 2** * ****-1** → **-2**
<details>
<summary>`f(2 - 2)` → **-1**</summary>

`x = 0`
`if x == 1:`
*not executed as 0 is not equal 1*
`elif x < 1:`
`return -1`
`else:`
*not executed as second if condition evaluated to True*

</details>
</details>
</details>
❌ **Incorrect**, for certain positive integers, the function will result in a `RecursionError`. This is because Python has a maximum recursion limit, so if the argument (integer number) is too large, it will exceed this limit before reaching 1 or less than 1 and cause a `RecursionError`.
✅ **Correct**, the function can be executed with all negative floating point numbers without raising an error. This is because for all negative numbers, the function will return -1  immediately (floating point numbers are smaller than 1) without going into recursion.
✅ **Correct**, the function is indeed recursive as it calls itself in the else clause.
</details>
---
## Question 2
Given is the following proposed function definition from Task 3 in the Assignment:
```python
def sort_numbers_by_digit(number):
    return "".join(sorted(str(number)))[::-1])
```
The task was to convert the integer number to a string and sort this string by character in descending order.
Why does the function not work as intended?
❌ The function does not return a string since sorted() always returns a list.
❌ A string cannot be sorted with the function sorted() because strings are immutable.
❌ The function sorted() requires an iterable as an argument. However, we provide a string instead.
❌ The function sort_numbers_by_digit() only sorts the first character and ignores the remaining ones.
❌ The function sorted() sorts in ascending order, thus it requires the keyword argument reverse=True.
✅ The assumption is incorrect and the function actually does the correct thing.

<details>
<summary>Explanation</summary>

> 💡 **[.join(), .sorted()](/5b0832dbf9454eb1941b7632e68a9abb#6fbfa2a3d10a494b9747cf8f03d00ce4)**
❌ **Incorrect**, because although `sorted()` does indeed return a list, the function is using `"".join()` to convert the list back into a string by concetanating all elements in the list.
❌ **Incorrect**, because `sorted()` can take a string as an argument and return a list of sorted characters. The immutability of strings doesn't prevent them from being sorted.
<details>
<summary>Example</summary>

```python
# Example demonstrating the use of sorted() with a string in Python

# Define a string
my_string = "python"

# Use sorted() to sort the characters alphabetically
sorted_string = sorted(my_string)

# Display the original and sorted strings
print("Original String:", my_string)
print("Sorted String  :", ''.join(sorted_string))

# Output
Original String: python
Sorted String  : hnopty
```
</details>
❌** Incorrect**, this statement is incorrect because a string is an iterable in Python.
<details>
<summary>Example</summary>

We can iterate through the characters of a string using a for-loop. Thus, a string is considered an *iterable*.
```python
# Example demonstrating that a string is an iterable in Python

my_string = "Hello, Python!"

# Iterate over the characters in the string using a for loop
for char in my_string:
    print(char)

# Output:
# H
# e
# l
# l
# o
# ,
#  
# P
# y
# t
# h
# o
# n
# !
```
</details>
❌ **Incorrect**, because `sorted()` sorts all characters in the string, not just the first one.
❌ **Incorrect**, because although `sorted()` does sort in ascending order by default, the function uses slicing `[::-1]` to reverse the sorted string, effectively sorting it in descending order.
✅ **Correct**, the function does convert the integer to a string, sorts the characters in descending order, and returns the sorted string. Check the example below.
<details>
<summary>`sort_numbers_by_digit(7462)`</summary>

`number = 7462`
<details>
<summary>`return "".join(sorted(str(number)))[::-1])` → `'7642'` </summary>

<details>
<summary>`"".join(sorted(str(number)))[::-1])` → `'7642'`</summary>

<details>
<summary>`sorted(str(number)))[::-1]` → `['7', '6', '4', '2']`</summary>

<details>
<summary>`sorted(str(number))` → `['2', '4', '6', '7']`</summary>

`str(number)` → `'7462'`
</details>
</details>
</details>
</details>
*→ **`'7642'`** is a string sorted in descending order*


</details>
</details>
---
## Question 3
Which value does the list() function return after the execution of the given statement?
```python
list(map(lambda x: x == 2, [0, 1, 2, 3, 4, 5, 6]))
```
✅ [False, False, True, False, False, False]
❌ `2`
❌ `[0, 0, 2, 0, 0, 0]`
❌ `[2]`
❌ `[True, False, True, False, True, False, True]`
❌ `[0, 1, 2, 0, 1, 2, 0]`
❌  `<map at 0x20132719d00>`

<details>
<summary>Explanation</summary>

> 💡 **[Map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)**
✅ **Correct**:
Let's break down the statement:
1. `map(lambda x: x == 2, [0, 1, 2, 3, 4, 5, 6])`
This applies the `lambda` function to every element in the list.
The `lambda` function checks if an element is equal to 2. If it is, it returns `True`, else it returns `False`.
So, for the given list, it returns `False` for 0, 1, 3, 4, 5, 6 and `True` for 2.
1. `list(map(lambda x: x == 2, [0, 1, 2, 3, 4, 5, 6]))`:
This converts the map object returned by the `map()` function into a list.
Therefore, the returned list is `[False, False, True, False, False, False, False]` as only the *third* element in the list (2) is equal to 2, and *all other elements* are not equal to 2.
❌ **Incorrect**, the `map()` function does not return a single value, it returns a map object which is converted to a list in this case.
❌ **Incorrect**, this would be the result if the `lambda` function was returning the input value when it equals 2 and 0 otherwise.
❌ **Incorrect**, this would be the result if the `lambda` function was returning the input value when it equals 2 and discarding all other values.
❌ **Incorrect**, this would be the result if the `lambda` function was checking if the input value is even.
❌ **Incorrect**, this would be the result if the `lambda` function was returning the input value modulo 3.
❌ **Incorrect**, this would be the result if the `list()` function was not used to convert the map object to a list.
</details>
---
## Question 4
In the following code snippet, how often is the function **f** called? Please assume that f is a function that returns the **doubled** value of its only argument.
```python
list(map(f, map(f, range(7, 13))))
```
Enter your value as a positive integer.
If you think an error appears, then please type -1 ("negative one").
**12**

<details>
<summary>Explanation</summary>

> 💡 **[Range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385), [map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)**
The `map()` function applies a given function to each item of an iterable (such as list, tuple etc.) and returns a list of the results.
In the code snippet there are two `map()` functions.
The inner `map(f, range(7, 13))` applies the function `f` to each item in the range from 7 to 12 (inclusive), which results in **6 calls** to the function `f`.
The outer `map(f, ...)` then applies the function `f` to each item in the result of the inner `map()`, which is again **6** **items**. So, this results in another 6 calls to the function `f`.
Therefore, the function `f` is called 6 + 6 = 12 times in total.
</details>
---
## Question 5
Which value does the variable **result** contain after the execution of the given statement?
Please assume that **f** is a function that returns **True** for *even integers* and **False** for *odd integers* as its only argument.
```python
result = list(map(f, [235, 283, 291]))
```
❌ [ ]
❌ We cannot say what happens, because f rather needs to be a lambda function.
❌ "35391"
❌ [2, 2, 8, 2]
✅ [False, False, False]
❌ False

<details>
<summary>Explanation</summary>

> 💡 **[Map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)**
The correct answer is `[False, False, False]`.
Here's why:
The `map()` function in Python applies the function `f` to each element of the list `[235, 283, 291]`.
Given that `f` is a function that returns `True` for even *integers* and `False` for *odd* integers, when it is applied to the list `[235, 283, 291]`, it will return `False` for each element. Therefore, `result` will be a list containing `[False, False, False]`.
</details>
---
## Question 6
Please look at the following code and assume that every **XXX** is replaced by the same function that takes one argument and returns ***True*** if the argument has been an even integer and ***False*** if the argument has been an *odd integer*. Further assume, that every **yyy** is replaced by the same syntactically correct list of arguments of the correct type.
```python
list(map(lambda x: x ** 2, filter(XXX, range(yyy)))) == [item**2 for item in range(yyy) if XXX(item)]
```
What is the resulting value of this line of code?
❌ 4
✅ True
❌ False
❌ *An error occurs.*

<details>
<summary>Explanation</summary>

> 💡 **[Map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9), [filter function](/5b0832dbf9454eb1941b7632e68a9abb#1dc0b8cb700741e5a48f5ed4180b2035), [list comprehension](/5b0832dbf9454eb1941b7632e68a9abb#cf5a90b80642480db120fbbe3f4ea4a7), [range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385)**
First we need to understand what the code snippet is doing.
The code shows two different ways to square even numbers in a range.
One using the `map` and `filter` functions:
```python
list(map(lambda x: x ** 2, filter(XXX, range(yyy))))
```
and the other using a list comprehension:
```python
[item**2 for item in range(yyy) if XXX(item)]
```
Then it is checked whether the two approaches produce the same result , using `==`. If they do, the statement will be `True`. If they don't, the statement will be `False`.
`XXX` is a function that returns `True` if the input `item` is an even number and `False` if it's an odd number. The `yyy` is a list of arguments.
Now, lets assume the value 5 for `yyyy` and make an example:
First approach:
<details>
<summary>`list(map(lambda x: x ** 2, filter(XXX, range(5)))` → `[0, 4, 16]`</summary>

<details>
<summary>`map(lambda x: x ** 2, [0, 2, 4])` →`<map object>`</summary>

`filter(XXX, [0, 1, 2, 3, 4])` → `[0, 2, 4]`
</details>
</details>
Second approach:
<details>
<summary>`[item**2 for item in range(5) if XXX(item)]` → `[0, 4, 16]`</summary>

1st run: `XXX(0)` → `True` → keep item `0` and square → `0`
2nd run: `XXX(1)` → `False` → discard item `1`
3rd run: `XXX(2)` → `True` → keep item `2` and square → `4`
4th run run: `XXX(3)` → `False` → discard item `3`
5th run run: `XXX(4)` → `True` → keep item `4` and square → `16`
</details>
We can now see that the both statements produce the same result.
Therefore, the overall statement `[0, 4, 16] == [0, 4, 16]` will return `True`.
Now lets’a have a look at the statements:
❌ **Incorrect**, the statement is a comparison and will return a boolean value (`True` or `False`), not an integer.
✅ **Correct**, if both methods are implemented correctly and the same list of arguments is used for both.
❌ **Incorrect**, if there is a mistake in the implementation of one of the methods or if different lists of arguments are used.
❌ **Incorrect**, no error should occur if the `XXX` function and `yyy` arguments are implemented correctly.
</details>
---
