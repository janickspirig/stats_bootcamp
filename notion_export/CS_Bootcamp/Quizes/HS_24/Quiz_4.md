---
title: "Quiz 4"
notion_id: "17074ffd-3319-8017-b171-e2caa4466999"
notion_url: "https://www.notion.so/Quiz-4-17074ffd33198017b171e2caa4466999"
exported_at: "2025-12-13T23:04:16.462772+00:00"
---

# Quiz 4

## Question 1
Which *value* does the variable **result** contain after the execution of the given statement?
Please assume that **f** is a function that returns **True** for even integers and **False** for odd integers as its only argument.
```python
result = list(map(f, [235, 283, 291]))
```
❌ `"35391"`
❌ `False`
❌ `[2, 2, 8, 2]`
✅ `[False, False, False]`
❌ We cannot say what happens, because f rather needs to be a *lambda* function.
❌ `[]`

<details>
<summary>Explanation</summary>

> 💡 **[Map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)**
### Code Explanation
1. **`map(f, [235, 283, 291])`**:
- The `map` function applies the function `f` to each element in the list `[235, 283, 291]`.
- The function `f` is assumed to return `True` for even numbers and `False` for odd numbers.
1. **`list(map(...))`**:
- The `map` function returns an iterator, which is then converted into a list using the `list()` function.
### Answer Explanation
Now, let's apply the function `f` to each number in the list:
- `f(235)` returns `False` because 235 is an odd number.
- `f(283)` returns `False` because 283 is an odd number.
- `f(291)` returns `False` because 291 is an odd number.
Therefore, the `map` function will produce an iterator that yields `[False, False, False]`, and converting this iterator to a list gives us `[False, False, False]`.
</details>
---
## Question 2
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
## Question 3
Given is the following proposed function definition from Task 3 in the Assignment:
```python
def sort_numbers_by_digit(number):
    return "".join(sorted(str(number)))[::-1])
```
The task was to convert the integer **number** to a string and sort this string by character in descending order.
Why does the function **not** work as intended?
❌ A *string* cannot be sorted with the function *sorted()* because strings are immutable.
❌ The function does not return a *string* since *sorted()* always returns a *list*.
✅ The assumption is incorrect and the function actually does the correct thing.
❌ The function *sort_numbers_by_digit()* only sorts the first character and ignores the remaining ones.
❌ The function *sorted()* requires an *iterable* as an argument. However, we provide a *string* instead.
❌ The function *sorted()* sorts in ascending order, thus it requires the keyword argument *reverse=True*.

<details>
<summary>Explanation</summary>

> 💡 **[.join(), .sorted()](/5b0832dbf9454eb1941b7632e68a9abb#6fbfa2a3d10a494b9747cf8f03d00ce4)**
### Code Explanation
1. `str(number)`
- This converts the integer `number` into a string. For example, if `number` is `123`, it becomes `'123'`.
1. `sorted(str(number))`
- The `sorted()` function takes an iterable (like a string) and returns a list of its elements sorted in ascending order. Since strings are iterable, this works perfectly fine. For example, `'123'` becomes `['1', '2', '3']`.
1. `"".join(sorted(str(number)))`
- The `join()` method takes all items in an iterable and joins them into a single string. So, `['1', '2', '3']` becomes `'123'`.
1. `[::-1]`
- This is a slicing operation that reverses the string. So, `'123'` becomes `'321'`.
### Answer Explanations
❌ **Incorrect,** because the `sorted()` function can indeed take a string as input and return a sorted list of its characters. The immutability of strings does not prevent them from being sorted.
❌ **Incorrect,** because while `sorted()` returns a list, the `join()` method is used to convert this list back into a string.
✅ **Correct, **because the function does exactly what is intended: it converts the number to a string, sorts the characters, and reverses the order to get a descending sort.
❌ **Incorrect, **because the `sorted()` function sorts all characters in the string, not just the first one.
❌ **Incorrect,** because a string is indeed an iterable in Python, and `sorted()` can take a string as an argument.
❌ **Incorrect, **because while `sorted()` does sort in ascending order by default, the function reverses the sorted string with `[::-1]`, achieving the desired descending order without needing `reverse=True`.
</details>
---
## Question 4 
Which *value* does the list() function return after the execution of the given statement?
```python
list(map(lambda x: x == 2, [0, 1, 2, 3, 4, 5, 6]))
```
❌ `[2]` 
❌ `[0, 0, 2, 0, 0, 0, 0]` 
❌ `<map at 0x20132719d00>` 
✅ `[False, False, True, False, False, False, False]` 
❌ `[True, False, True, False, True, False, True]` 

<details>
<summary>Explanation</summary>

> 💡 **[Map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)**
Let’s walk through the code from inside to the outside to understand what is happening: 
1. **`[0, 1, 2, 3, 4, 5, 6]`**: This is a list of numbers from 0 to 6.
1. **`lambda x: x == 2`**: This is a lambda function, which is a small anonymous function in Python. It takes one argument `x` and returns `True` if `x` is equal to 2, otherwise it returns `False`.
1. **`map(lambda x: x == 2, [0, 1, 2, 3, 4, 5, 6])`**: The `map` function applies the lambda function to each element of the list `[0, 1, 2, 3, 4, 5, 6]`. It checks each number to see if it is equal to 2.
- For `0`, `1`, `3`, `4`, `5`, and `6`, the lambda function returns `False` because these numbers are not equal to 2.
- For `2`, the lambda function returns `True` because 2 is equal to 2.
1. **`list(...)`**: The `list()` function converts the result of the `map` function into a list. The result of the `map` function is an iterable that contains the results of applying the lambda function to each element of the list.
So, the final result is a list of boolean values indicating whether each number in the original list is equal to 2:
- `[False, False, True, False, False, False, False]`
</details>
---
## Question 5
In the following code snippet, how often is the function f called? Please assume that f is a function that returns the *doubled* value of its only argument.
```python
list(map(f, map(f, range(3, 19))))
```
Enter your value as a positive integer.
If you think an error appears, then please type -1 ("negative one").
✅ 32

<details>
<summary>Explanation</summary>

> 💡 **[Map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9),  [range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385)**
The code uses the `map` function, which applies a given function to all items in an iterable (like a list or range) and returns a map object (which is an iterator).
1. **`range(3, 19)`**:
- This creates a sequence of numbers starting from 3 up to, but not including, 19. So, the numbers are: 3, 4, 5, ..., 18.
- There are 16 numbers in this range.
1. **`map(f, range(3, 19))`**:
- The `map` function applies the function `f` to each number in the range.
- Since there are 16 numbers, `f` is called 16 times in this step.
1. **`map(f, map(f, range(3, 19)))`**:
- The result of the first `map` is another iterable where each element has been doubled by `f`.
- The outer `map` applies the function `f` again to each of these 16 doubled values.
- So, `f` is called another 16 times in this step.
In total, the function `f` is called 16 (from the first map) + 16 (from the second map) = **32 times.**
</details>
---
## Question 6
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
