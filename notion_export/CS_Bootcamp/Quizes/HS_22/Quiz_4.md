---
title: "Quiz 4"
notion_id: "452c8d85-b777-41ec-b961-7162afe25a1a"
notion_url: "https://www.notion.so/Quiz-4-452c8d85b77741ecb9617162afe25a1a"
exported_at: "2025-12-13T23:19:06.665966+00:00"
---

# Quiz 4

## Question 1
Which *value* does the variable **result** contain after the execution of the given statement?
```python
result = list(map(lambda x: x % 3 == 0, [0, 1, 2, 3, 4, 5, 6]))
```
❌  `<map at 0x20132719d00>`
❌  `[True, False, True, False, True, False, True]`
❌  `[0, 1, 2, 0, 1, 2, 0]`
✅  `[True, False, False, True, False, False, True]`
❌  `[0, 1, 0, 0, 1, 1, 0]`

<details>
<summary>Explanation</summary>

We see that we have some nested code here, i.e., `map()` is placed inside the `list()` function. In such scenarios it is important to read the code from the inside to the outside. Thus, we only look at the `map()` function first
As we know, [map applies a function to each element in an iterable](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9). In this code the function is `lambda x: x % 3 == 0` and the iterable is `[0, 1, 2, 3, 4, 5, 6]`.
Map makes Python take out each integer of the list, throw it into the map function and save the return value. Thus, the lambda function is executed executed 7 times.
<details>
<summary>1st run with input 0 → returns True</summary>

`x = 0`
`0 % 3 == 0` → `0 == 0` → True
`0 % 3` → `0`
</details>
<details>
<summary>2nd run with input 1 → returns False</summary>

`x = 1`
`1 % 3 == 0` → `1 == 0` → False
`1 % 3` → `1`
</details>
<details>
<summary>3rd run with input 2 → returns False</summary>

`x = 2`
`2 % 3 == 0` → `2 == 0` → False
`2 % 3` → `2`
</details>
<details>
<summary>4th run with input 3 → returns True</summary>

`x = 3`
`3 % 3 == 0` → `0 == 0` → True
`3 % 3` → `0`
</details>
<details>
<summary>5th run with input 4 → returns False</summary>

`x = 4`
`4 % 3 == 0` → `1 == 0` → False
`4 % 3` → `1`
</details>
<details>
<summary>6th run with input 5 → returns False</summary>

`x = 5`
`5 % 3 == 0` → `2 == 0` → False
`5 % 3` → `2`
</details>
<details>
<summary>7th run with input 6 → returns True</summary>

`x = 6`
`6 % 3 == 0` → `0 == 0` → True
`6 % 3` → `0`
</details>
As we see, from the map function we get back a map object that contains multiple boolean values. However, in order to look what is inside the map object, we need to convert it to a list, which is why `map()` is wrapped into the `list()` method. Eventually, we get following output which is the equivalent to option 4 in the question above.
`[True, False, False, True, False, False, True]`
</details>
---
## Question 2
In the following code snippet, how often is the function **f** called?
```python
def f(x):
	return x + 2

result = list(map(f, map(f, range(7, 16))))
```
18

<details>
<summary>Explanation</summary>

We have here some nested code again. Thus, we must read from the inside to the outside and we start at the code that gets executed first, which is the [range function](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385).
<details>
<summary>`range(7, 16)` → `[7, 8, 9, 10, 11, 12, 13, 14, 15]`</summary>

7 is the first number to be *included*
16 is the first number to be *excluded*
There is no step parameter, which means that all numbers from 7 to 15 will be included.
</details>
<details>
<summary>`map(f, [7, 8, 9, 10, 11, 12, 13, 14, 15])` → `map(9, 10, 11, 12, 13, 14, 15, 16, 17)`</summary>

<details>
<summary>1st call with `f(7)` → `9`</summary>

`x = 7`
`return 7 + 2` → `9`
</details>
<details>
<summary>2nd call with `f(8)` → `10`</summary>

`x = 8`
`return 8 + 2` → `10`
</details>
<details>
<summary>3rd call with `f(9)` → `11`</summary>

`x = 9`
`return 9 + 2` → `11`
</details>
<details>
<summary>4th call with `f(10)` → `12`</summary>

`x = 10`
`return 10 + 2` → `12`
</details>
<details>
<summary>5th call with `f(11)` → `13`</summary>

`x = 11`
`return 11 + 2` → `13`
</details>
<details>
<summary>6th call with `f(12)` → `14`</summary>

`x = 12`
`return 12 + 2` → 14
</details>
<details>
<summary>7th call with `f(13)` → `15`</summary>

`x = 13`
`return 13 + 2` → `15`
</details>
<details>
<summary>8th call with `f(14)` → `16`</summary>

`x = 14`
`return 14 + 2` → `16`
</details>
<details>
<summary>9th call with `f(15)` → `17`</summary>

`x = 15`
`return 15 + 2` → `17`
</details>
</details>
<details>
<summary>`map(f, [9, 10, 11, 12, 13, 14, 15, 16, 17])` → `map(11, 12, 13, 14, 15, 16, 17, 18, 19)`</summary>

<details>
<summary>1st call with `f(9)` → `11`</summary>

`x = 9`
`return 9 + 2` → `11`
</details>
<details>
<summary>2nd call with `f(10)` → `12`</summary>

`x = 10`
`return 10 + 2` → `12`
</details>
<details>
<summary>3rd call with `f(11)` → `13`</summary>

`x = 11`
`return 11 + 2` → `13`
</details>
<details>
<summary>4th call with `f(12)` → `14`</summary>

`x = 12`
`return 12 + 2` → `14`
</details>
<details>
<summary>5th call with `f(13)` → `15`</summary>

`x = 13`
`return 13 + 2` → `15`
</details>
<details>
<summary>6th call with `f(14)` → `16`</summary>

`x = 14`
`return 14 + 2` → `16`
</details>
<details>
<summary>7th call with `f(15)` → `17`</summary>

`x = 15`
`return 15 + 2` → `17`
</details>
<details>
<summary>8th call with `f(16)` → `18`</summary>

`x = 16`
`return 16 + 2` → `18`
</details>
<details>
<summary>9th call with `f(17)` → `19`</summary>

`x = 17`
`return 17 + 2` → `19`
</details>
</details>
<details>
<summary>`list(map(9, 10, 11, 12, 13, 14, 15, 16, 17))` → `[11, 12, 13, 14, 15, 16, 17, 18, 19]`</summary>

To look into the map function, we need to convert it to a list.
</details>
The question asks for the number of times the function `f` was called. We can see that each, the first and the second [map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9) called the function `f` 9 times. Thus, the function `f` was called 18 times in total.
</details>
---
## Question 3
Given is the recursive function **fibonacci(n)** that produces the **n**th Fibonacci number.
Assume it is implemented correctly in standard python and that it checks for the two stop conditions with **n == 0** and **n == 1**. 
In this case, what would happen if we call this function with a **negative integer value as the only argument**.
❌  There are no negative Fibonacci numbers, so it will return the value 0.
❌  The base case is never met, so the code execution will never stop. 
❌  It computes the nth Fibonacci number. 
✅  Eventually an error will be raised.
❌  the function notices the bas input and will complain to the user that a negative number is not allowed.

<details>
<summary>Explanation</summary>

The [fibonacci function](/5b0832dbf9454eb1941b7632e68a9abb#deadb4d546c746fb988789ae1b7832b5) mentioned in the question looks like this:
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
```
If we now call this function with a negative number like `fibonacci(-5)` then the first two if-statements, i.e., the stop conditions will not evaluate to True as -5 is not equal to 0, 1 or 2. Thus, the code in the else block gets executed, which contains two recursive function calls. So we call ourselves again with `fibonacci(-7)` and `fibonacci(-6)`.
We see that parameter `n` got even smaller now and thus never equal 0, 1 or 2. Therefore, no stop condition will ever be met which makes Python call the `fibonacci()` function again and again until an error is thrown as at one point the execution memory will be full.
</details>
---
## Question 4
Given is the following proposed function definition from Task 3 in the Assignment:
```python
def sort_numbers_by_digit(number):
	return "".join(sorted(str(number), reverse=False))
```
The task was to convert the integer **number** to a string and sort this string by character in descending order.
Why does the function not work as intended?
❌  The assumption is incorrect and the function actually does the correct thing.
❌  A *string* cannot be sorted with the function **sorted()** because strings don’t have an order.
❌  The function does not return a *string* since **sorted()** always returns a *list*.
❌  The function **sorted()** requires an *iterable* as an argument. However, we provide a *string* instead.
✅  The function **sorted()** sorts in ascending order because of the keyword argument **reverse=False**.
❌  The function **sort_numbers_by_digit()** only sorts the first character and ignores the remaining ones.

<details>
<summary>Explanation</summary>

**Statement 1** is incorrect because statement 5 is correct.
**Statement 2** is incorrect because the characters in a strings have an alphabetical order (A-Z). Thus, we can sort strings using [`sorted()`](/5b0832dbf9454eb1941b7632e68a9abb#6fbfa2a3d10a494b9747cf8f03d00ce4)[ in combination with ](/5b0832dbf9454eb1941b7632e68a9abb#6fbfa2a3d10a494b9747cf8f03d00ce4)[`.join()`](/5b0832dbf9454eb1941b7632e68a9abb#6fbfa2a3d10a494b9747cf8f03d00ce4).
**Statement 3** is incorrect as `.join()` is used in front of `sorted()` which makes the function return a string. To understand this better, let’s assume we call the function as follow:
`sort_numbers_by_digit(8295)`
`number = 8295`
`return "".join(sorted(str(number), reverse=False))` → `'2589'`
`str(8295)` → `'8295'`
`sorted('8295', reverse=False)` → `['2', '5', '8', '9']`
`"".join(['2', '5', '8', '9'])` → `'2589'`
`return '2589'` → `'2589'`
**Statement 4** is incorrect because we can [provide an iterable as input](/5b0832dbf9454eb1941b7632e68a9abb#7c022c5cc1a647d58ba1a7e82406c3e6) to the sorted function but it is not required as we can also provide a string. When we provide strings however, [a list will be returned](/452c8d85b77741ecb9617162afe25a1a#4ec3ce0706074225a77718228000c054) that contains the characters of the string as single elements in sorted order.
**Statement 5** is correct because the `sorted()` function sorts by default in ascending order. If it should sort in descending order the parameter `reverse` must be set to `True`.
**Statement 6** is incorrect as all characters in the string are included in the sorting.
</details>
---
## Question 5
Which value does the variable **result** contain after the execution of the given statement?
```python
result = list(map(str, [235, 283, 291]))
```
✅  `["235", "283", "291"]`
❌  `"235283291"`
❌  `[2, 3, 5, 2, 8, 3, 2, 9, 1]`
❌  *An Error occurs.*

<details>
<summary>Explanation</summary>

Here it is again very important to read the code from the inside to the outside and of course understand how the map function works.
`list(map(str, [235, 283, 291]))` → `['235', '283', '291']`
<details>
<summary>`map(str, [235, 283, 291])` → `map('235', '283', '291')`</summary>

1st call with `str(235)` → `'235'`
2nd call with `str(283)` → `'283'`
3rd call with `str(291)` → `'291'`
</details>
</details>
---
## Question 6
Look at this code snippet and check **all** *true* statement.
```python
def f(x):
	if x <= 1 :
		return 1
	else:
		return x + f(x - 2)
```
✅  The function **f** is *recursive*.
❌  The result of **f(7)** is 15.
❌  The function **f** is *not recursive*.
✅  The result of **f(7)** is 16.
❌  The function will *never* end.

<details>
<summary>Explanation</summary>

**Statement 1** is correct because in line 5 we call the function again from within the function by doing `f(x -2)`.
**Statement 2** is incorrect because statement 4 is correct.
**Statement 3** is incorrect because statement 1 is correct.
**Statement 4** is correct because the result of `f(7)` is **16**.
<details>
<summary>`f(7)` → **16**</summary>

`x = 7`
`return 7 + ``f(5)` → 7 + **9** → **16**
<details>
<summary>`f(5)` → **9**</summary>

`x = 5`
`return 5 + ``f(3)` → 5 + **4** → **9**
<details>
<summary>`f(3)` → **4**</summary>

`x = 3`
`return 3 + ``f(1)` → 3 + **1** → **4**
<details>
<summary>`f(1)` → **1**</summary>

`return 1`
</details>
</details>
</details>
</details>
**Statement 5** is incorrect because statement 4 is correct which shows that this recursive function is working fine as there is a stop condition in line two and three: `if x <= 1`
</details>
---
## Question 7
Given is the following function **get_double_string(item)** and the *list* **results**, which is a list made of lists.
```python
def get_double_string(item):
	if isinstance(item, str):
		return str(float(item) * 2 )
	else:
		return str(item * 2) 
```
```python
results = [[11.3, 24.0, '31.0'], [42.1, '15.9', 6.0], [82.7, 14.3, '27.1']]
```
Now, you want to convert this list of lists of float and string values using the given function to get doubled input number for each value as a string. Which of the following code statements achieves this result? The resulting list **doubled** should look like this afterwards:
```python
print(doubled)
>>> ['22.6', '48.0', '62.0', '84.2', '31.8', '12.0', '165.4', '28.6', '54.2']
```
✅  Code snippet 1
```python
doubled = []
for r in results:
	doubled += list(map(get_double_string, r))
```
❌  Code snippet 2
```python
doubled = list(map(get_double_string, results))
```
❌  Code snippet 3
```python
doubled = list(map(lambda r: list(map(get_double_string, r)), results))
```
❌  Code snippet 4
```python
doubled = get_double_string(results)
```
❌  *None of the available statements produce the given list ****doubled****.*

<details>
<summary>Explanation</summary>

First of all, it is important to understand what the function `get_double_string()` is essentially doing. This function takes an input `item`, which can either be of type string or integer. If `item` is a string, then the function converts this string to a float value, doubles the float value, converts the result back to a string and returns it.
`get_double_string('5.3')` → `'10.6'`
`item = '5.3'`
`if isinstance('5.3', str):` → True
`return str(float('5.3') * 2)` → `'10.6'`
`str(float('5.3') * 2)` → `'10.6'`
`float('5.3') * 2` → `10.6`
If `item` is not a string, e.g., an integer or a float, then item is doubled, converted to a string and returned as well.
`get_double_string(4.8)` → `'9.6'`
`item = 4.8`
`if isinstance(48', str):` → False
`else:`
`return str(4.8 * 2)` → `'10.6'`
As we can see in the original list we have stored strings as well as floats. So this function fulfils our purpose of doubling a float or string value and return the result as a string. So what we need to do is to iterate over the `results` list which returns us each sublist. And then iterate through this sublist again to take out each elements (integer or string) and throw it into the `get_double_string()` function.
We can achieve this with code snippet 1:
`doubled = []`
for r in results:
<details>
<summary>1st run → `doubled = ['22.6', '48.0', '62.0']`</summary>

`r = [11.3, 24.0, '31.0']`
`doubled += list(map(get_double_string, [11.3, 24.0, '31.0'])`
`map(get_double_string, [11.3, 24.0, '31.0']`
<details>
<summary>1st call with `get_double_string(11.3)` → `'22.6'`</summary>

`item = 11.3`
`if isinstance(11.3, str):` → False
`else:`
`return str(11.3 * 2)` → `'22.6'`
</details>
<details>
<summary>2nd call with `get_double_string(24.0)` → `'48.0'`</summary>

`item = 24.0`
`if isinstance(24.0, str):` → False
`else:`
`return str(24.0 * 2)` → `'48.0'`
</details>
<details>
<summary>3rd call with `get_double_string('31.0')` → `'62.0'`</summary>

`item = '31.0'`
`if isinstance('31.0', str):` → True
`return str(float('31.0') * 2)` → `'62.0'`
</details>
</details>
<details>
<summary>2nd run → `doubled = ['22.6', '48.0', '62.0', '84.2', '31.8', '12.0']`</summary>

`r = [42.1, '15.9', 6.0]`
`doubled += list(map(get_double_string, [42.1, '15.9', 6.0])`
`map(get_double_string, [42.1, '15.9', 6.0]`
<details>
<summary>1st call with `get_double_string(42.1)` → `'84.2'`</summary>

`item = 11.3`
`if isinstance(42.1, str):` → False
`else:`
`return str(42.1 * 2)` → `'84.2'`
</details>
<details>
<summary>2nd call with `get_double_string('15.9')` → `'31.8'`</summary>

`item = '15.9'`
`if isinstance('15.9', str):` → True
`return str(float('15.9') * 2)` → `'31.8'`
</details>
<details>
<summary>3rd call with `get_double_string(6.0)` → `'12.0'`</summary>

`item = 6.0`
`if isinstance(6.0, str):` → False
`else:`
`return str(6.0 * 2)` → `'12.0'`
</details>
</details>
<details>
<summary>3rd run → `doubled = ['22.6', '48.0', '62.0', '84.2', '31.8', '12.0', '165.4', '28.6', '54.2']`</summary>

`r = [82.7, 14.3, '27.1']`
`doubled += list(map(get_double_string, [82.7, 14.3, '27.1'])`
`map(get_double_string, [82.7, 14.3, '27.1']`
<details>
<summary>1st call with `get_double_string(82.7)` → `'165.4'`</summary>

`item = 82.7`
`if isinstance(42.1, str):` → False
`else:`
`return str(82.7 * 2)` → `'165.4'`
</details>
<details>
<summary>2nd call with `get_double_string(14.3)` → `'28.6'`</summary>

`item = 14.3`
`if isinstance(14.3, str):` → False
`else:`
`return str(14.3 * 2)` → `'28.6'`
</details>
<details>
<summary>3rd call with `get_double_string('27.1')` → `'54.2'`</summary>

`item = '27.1'`
`if isinstance('27.1', str):` → True
`return str(float('27.1') * 2)` → `'54.2'`
</details>
</details>
</details>
---

