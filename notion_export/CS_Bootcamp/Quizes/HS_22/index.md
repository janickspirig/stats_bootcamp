---
title: "HS 22"
notion_id: "63b225c3-7436-45ce-ba78-7562a98638b7"
notion_url: "https://www.notion.so/HS-22-63b225c3743645ceba787562a98638b7"
exported_at: "2025-12-13T23:15:52.177759+00:00"
---

# HS 22

---
📄 **[Quiz 2]** (subpage)
## Question 1
Which of the following code snippets computes the *double* of the *digit sum* of the integer in variable **var** and stores the result as an integer?
❌  Code snippet 1
```python
var = 131

ds = 0

for num in str(var):
	ds = ds + num
```
❌  Code snippet 2
```python
var = 131

ds = 0

for num in str(var):
	ds = ds + int(num) ** 2
```
✅  Code snippet 3
```python
var = 131

ds = 0

for num in str(var):
	ds = ds + int(num) * 2
```
❌  Code snippet 4
```python
var = 131

ds = 0

for num in var:
	ds = ds + num * 2
```

<details>
<summary>Explanation</summary>

<details>
<summary>❌  Code snippet 1</summary>

If we run this code we get an error:
`TypeError: unsupported operand type(s) for +: 'int' and 'str’`
This is because in variable `num` we save the current digit of the number as a string, such as `'1'`. And then inside the for-loop we try to add up the integer `ds` which has the value `0` and the string `num`. This is not possible as they are different datatypes.
→ This code is not working properly and thus the answer is wrong.
</details>
<details>
<summary>❌  Code snippet 2</summary>

If we run this code we get the integer `11` as output.
This is because we [exponentiate](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a) (`**`) each digit in the number and then add this result up with the integer stored in `ds`.
1st run: `ds = 0`, `num = 1` → `ds += 1 ** 2` → `ds = 1`
2nd run: `ds = 1`, `num = 3` → `ds += 3 ** 2` → `ds = 10`
3rd run: `ds = 10`, `num = 1` → `ds += 1 ** 2` → **`ds = 11`**
→ 11 is not equal to the double (10) of the digit sum of 131. Therefore, this option is wrong.
</details>
<details>
<summary>✅  Code snippet 3</summary>

In the header of the for-loop we correctly convert the number 131 to a string first because we cannot iterate over integers. Inside the for-loop we then correctly convert the current digit of the number stored in `num` to an integer, double this integer by doing `* 2` and then add the result from this operation to the integer stored in `ds`. After completion of the for-loop the integer 10 is stored in `ds`.
→ The digit sum of 131 is 5 (1 + 3 + 1 = 5). 10 is the double of 5 (5 * 2 = 10).
</details>
<details>
<summary>❌  Code snippet 4</summary>

If we run this code we get an error:
`TypeError: 'int' object is not iterable`
An Integer is not an iterable and therefore we can not use an integer in the header of a for-loop as we cannot iterate over it. If we want to iterate from left to right through an Integer, we need to convert it first to a string using the built-in [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb) method `str()`.
</details>
</details>
---
## Question 2
How many loop iterations does the following function call produce if used in a for-loop?
```python
range(3, 19, 3)
```
6

<details>
<summary>Explanation</summary>

Let’s assume we use this range object in the context of the following example for-loop.
```python
for x in range(3, 19, 3):
	print('Hello')
```
The question asks basically how many times the string `'Hello'` is printed, i.e., the for-loop is executed.
To answer this question we must figure out how many elements in the [range object](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385) includes.
`range(3, 19, 3)`
Which is the first element to include? → 3
Which is the first element to exclude? → 19
This produces the following number range:
`[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]`
But: Do we have a step size? Yes → 3
We only take every third element in the number range above:
`[3, `~~`4`~~`, `~~`5`~~`, 6, `~~`7`~~`, `~~`8`~~`, 9, `~~`10`~~`, `~~`11`~~`, 12, `~~`13`~~`, `~~`14`~~`, 15, `~~`16`~~`, `~~`17`~~`, 18]`
Our updated number range is:
`[3, 6, 9, 12, 15, 18]`
How many elements does this number range include? → 6
</details>
---
## Question 3
Given is the following code snippet:
```python
values = ""

for value in range(255):
	if value % 2  == 1: 
		values = values + str(value)
```
Mark all correct statements regarding this code snippet:
❌  **values** is a *String* containing all even numbers from 1 to 554.
❌  **values** is an *integer* containing the digit sum of the **range** function’s parameter value.
✅  **values** is a *String* containing all uneven numbers from 1 to 253.
❌  **values** is a *String* containing all uneven numbers from 1 to 555.
❌  **values** remains an empty *String* because the **if** statement will never evaluate to *True*.
❌  **values** is a *String* containing all even numbers from 0 to 554.

<details>
<summary>Explanation</summary>

Here we need to understand two things: How [`range()`](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385) and [modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c) `%` work.
If we only submit one parameter to the range function, then this parameter is treated as the first element to exclude and our range starts at 0. Thus, `range(555)` produces a number range containing the numbers from 0 to 554.
If we do `% 2` in an if-statement we can check whether a number is odd or even. For even numbers, `% 2` returns 0 and for uneven numbers, it returns 1. Thus, the code inside the if-statement will be executed for uneven numbers only as `if 1 == 1` evaluates to True.
With this information we can now think about the value stored in variable values. We see that inside the if-statement we simply append the number stored in `value` to the string stored in `values`. Since the if-body is only executed for uneven numbers, `values` will be a String containing the uneven numbers from 1 to 553. 1 is the first uneven number in the number range and 553 the last one. 
</details>
---
## Question 4
Given is the following code snippet:
```python
s = ""

for i in range(15, 24):
	s = s + str(i)
```
What is the content of the variable **s** after the execution?
❌  15161718192021222324
✅  151617181920212223
❌  nothing because an error occurs.
❌  01234567891011121314151617181920212223

<details>
<summary>Explanation</summary>

Again, we simply need to understand how the [`range()`](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385) function works and then this question becomes relatively easy. 
`range(15, 24)` produces the number range `[15, 16, 17, 18, 19, 20, 21, 22, 23]`
With the for-loop we now take each integer out of this number range, convert the integer to a string and append it to the string stored in `s`. 
Thus, in the end we have a string stored in `s` in which the numbers from 1 to 13 are chained together.
</details>
---
## Question 5
Given is the following code snippet:
```python
number = 3

for j in range(number, 8):
	print(j)
```
Mark the one valid statement regarding this code snippet.
❌  The snippet prints the value of j exactly 0 times.
❌  The snippet prints the value of j exactly 4 times.
❌  The snippet prints the value of j exactly 8 times.
✅  The snippet prints the value of j exactly 5 times. 
❌  The loop variable **j** must be called **i** because it’s an integer loop variable, so the execution will be stopped with a *SyntaxError*.

<details>
<summary>Explanation</summary>

`range(3, 8)` will produce a number range containing the elements 3, 4, 5, 6, 7. Thus, the range contains 5 elements in total. Thus, the loop and therefore the value in j will be printed exactly 5 times. 
The last one, option 5, is incorrect. We can give the temporary loop variable whichever name we want. For example, we could also do `for `**`banana`**` in range(number, 8):`
</details>
---
## Question 6
The body/suite of a for-loop can contain another for loop (a loop inside a loop). 
❌  False
✅  True

<details>
<summary>Explanation</summary>

Of course, we can simply put one loop into another one, aka [nested-loops](/5b0832dbf9454eb1941b7632e68a9abb#7cc1c66ebe7a4290927071b49aab1c29).
</details>
---

📄 **[Quiz 3]** (subpage)
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
📄 **[Quiz 4]** (subpage)
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

📄 **[Quiz 5]** (subpage)
## Question 1
What is printed by the following code cell assuming that the **__init__** method of the class **Person** was appropriately implemented according to its comment?
```python
class Person:

	def __init__(self, name, year_of_birth):
		# for the __init__ method, please assume that the variables
		# self._name and self._year_of_birth would be appropriately
		# initialized with the respective arguments

	@property
	def name(self):
		return self._name.upper()

	@property
	def year_of_birth(self):
		return int(self.year_of_birth)

	def __str__(self):
		return f'{self.name} is born in the year {self.year_of_birth}'

print(Person('Max', '2000'))
```
❌ *Nothing will be printed. Instead an error will be raised because ****year_of_birth**** should be an integer value.*
❌ *Nothing will be printed. Instead an error will be raised due to the missing ****setter methods.***
✅ MAX is born in the year 2000
❌ *Nothing will be printed. Instead an error will be raised because ****_year_of_birth**** and ****year_of_birth**** should be integer values.*
❌ Max is born int he year 2000
❌ *Nothing will be printed. Instead an error will be raised because we directly manipulate private attributed (****_name****, etc.) in the ****__init__**** method.*
❌ Person(’May’, ‘2000’)
❌ ’Max’ is born in the year ‘2000’
❌ Nothing will be printed. Instead an error will be raised because _ year_of_birth should be an integer value.

<details>
<summary>Explanation</summary>

❌ **Incorrect**,** **because we are free to store any value in any variable, i.e., it is technically possible to store a string in a variable `age` and the number 1 in a variable `name`. Thus, Python does not check if the value submitted for ***year_of_birth*** is an integer or not. It just stores the value in the variable.
❌ **Incorrect**, because we are not obliged to define setter methods, although we are suing getter methods (`@property`), as these are two different / separate constructs.
✅ **Correct**. Here we must now have a look on what is actually happening inside the code. Again, it is important to read the code from the inside to the outside:
<details>
<summary>`Person(’Max’, ‘2000)` → `x_606102`</summary>

1. The person class is called with the parameter values  ‘Max’ and ‘2000’
1. Python executes the code inside the constructor / `__init__` function
1. ‘Max’ is saved in variable `_name`
1. ‘2000’ is saved in variable `_year_of_birth`
1. Python returns memory address (`x_606102`) of this newly created class instance
</details>
<details>
<summary>`print(x_606102)` → ‘MAX is born int he year 2000’</summary>

1. The object that is stored at the address `x_606102` (Max) is accessed
1. Whenever we call `print()` for an object, Python checks if there is a `__str__` method implemented. If yes, the code inside this same method is executed.
1. Python executes the `def __str__` method
1. The person’s name is accessed with `self.name`
1. As we implemented a getter method `@property name`, the code inside this method is executed which returns the upper case version of the person’s name (’MAX’).
1. The person’s year of birth is accessed with self.year_of_birth
1. Again, we have the getter method `@property year_of_birth`. Inside this method, Python transform the value stored in variable `_year_of_birth` to an integer and returns it.
1. The string containing the upper case name (’MAX’) and the year of birth (2000) is returned
1. Python prints the string ‘MAX is born in the year 2000’ to the console.
</details>
❌ **Incorrect**. See explanation one → we are not bound to a specific data type that we can store in variables. Also, the code produces a valid output as we have seen.
❌ **Incorrect**. Yes, we modify the attributes directly. However, we do it within the class. Because `__init__` method lives inside the class Person, which we can see from the indentation. The whole idea behind getter and setter is to prevent data manipulation from outside the class, but from inside the class is entirely fine.
❌ **Incorrect**, because the name is printed in capitalised letters. 
❌ **Incorrect**, because the data of birth is printed as integer and not as string.
❌ **Incorrect**, because see explanation 1).
</details>
---
## Question 2
Given is the following code snippet:
```python
class Person:
	def __init__(self, name='Max', age=2, year_of_birth=2020):
		self.name = name
		self.year_of_birth = year_of_birth
	
	def age(self, current_year):
		return current_year - self.year_of_birth
```
Please *mark all* of the following code cells that, when executed after the class definition of Person, return an **integer value of 2**.
❌ `p = Person('Max', 2, 2020)`
❌ `Person('Max', 2, 2020).age`
✅ `Person('Max', 3, 2020).age(2022)`
✅ `Person('Max', 2020).age(2022)`
❌ `Person('Max', 2, 2020).age()`
✅ `Person('Max', 2, 2020).age(2022)`

<details>
<summary>Explanation</summary>

❌ **Incorrect**, because `age` is not an attribute of the Person class in the first place. I.e., nowhere inside the constructor a value is assigned to a variable called `age`. However, age is a function and if we want to call this function we must do so by using brackets, `p.age()`.
❌ **Incorrect**, age is still not an attribute but rather a function. And a function we can only call with brackets `<< function_name >>.()`.
✅ **Correct**, because first a new object for Max is created and the value 2020 is stored in the variable `year_of_birth`.
Now, we chain function calls together by immediately calling the `.age()` function for the person Max and submit the value 2022 as parameter.
Inside the function the difference between the value received as parameter (`current_year`) and the person’s `year_of_birth` is calculated: `2022 - 2022`, which yields `2`.
✅ **Correct**, the only difference to the previous example is that we only provide two values to the constructor instead of three. However, from the header of the constructor we can see that all parameters are optional. Thus, if we don’t provide a value for one or more parameters, the default values are used (the ones after the equal `=` sign).
After creating the class instance, the object has following values:
`name = 'Max'` → first value that we provided and the first value is stored in name
`age = 2020` → second value that we provided and the second value is stored in age
`year_of_birth = 2020` → default value was used as we only provided two values
And this creates the same situation as before: We call .age() function in which `2022 - 2020` is calculated and the number `2` is returned.
❌ **Incorrect**, it would yield an error. In the function header we see that we have a mandatory parameter, `current_year`. However, we call the function without a providing any value (`.age()`). Thus, Python is missing this value and throws an error.
✅ **Correct**, it’s basically the same as code snippet three. With the only difference that we provide 2 as value for `age`. However, when calculating the difference between `current_year` and `year_of_birth`, the variable `age` does not matter.
</details>
---
## Question 3
What is the output of the following code snippet?
```python
numbers = [5, 6, 1, 4]
sum(list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers))))
```
Output: **20**

<details>
<summary>Explanation</summary>

We get to the solution by reading the code from the inside to the outside.
<details>
<summary>1) `filter(lambda x: x % 2 == 0, numbers)` → **[6, 4]**</summary>

<details>
<summary>1st run: `x = 5` → **False**** **→** **exclude number 5</summary>

<details>
<summary>`1 == 0` → **False**</summary>

<details>
<summary>`lambda 5: 5 % 2` → **1**</summary>

`5 % 2` → **1**
</details>
</details>
</details>
<details>
<summary>2nd run: `x = 6` → **True** → include number 6</summary>

<details>
<summary>`0 == 0` → **True**</summary>

<details>
<summary>`lambda 6: 6 % 2` → **0**</summary>

`6 % 2` → **0**
</details>
</details>
</details>
<details>
<summary>3rd run: `x = 1` → **False**** **→** **exclude number 1</summary>

<details>
<summary>`1 == 0` → **False**</summary>

<details>
<summary>`lambda 1: 1 % 2` → **1**</summary>

`1 % 2` → **1**
</details>
</details>
</details>
<details>
<summary>4th run: `x = 4` → **True**** **→** **include number 4</summary>

<details>
<summary>`0 == 0` → **True**</summary>

<details>
<summary>`lambda 4: 4 % 2` → **0**</summary>

`4 % 2` → **0**
</details>
</details>
</details>
</details>
<details>
<summary>2) `map(lambda x: x * 2, [6, 4])` → **map([12, 8])**</summary>

<details>
<summary>1st run: `x = 6` → **12**</summary>

<details>
<summary>`lambda 6: 6 * 2` → **12**</summary>

`6 * 2` → **12**
</details>
</details>
<details>
<summary>2nd run: `x = 4` → **8**</summary>

<details>
<summary>`lambda 4: 4 * 2` → **8**</summary>

`4 * 2` → **8**
</details>
</details>
</details>
<details>
<summary>3) `list(map([12, 8])` → **[12, 8]**</summary>

simple conversion from map object to a list
</details>
<details>
<summary>4) `sum([12, 8])` → <u>**20**</u></summary>

`12 + 8 = 20` → <u>**20**</u>
</details>
</details>
---
## Question 4
What is printed by following code cell assuming that **__init__** method of the class **Person** was appropriately implemented according to its comment?
```python
class Person:

	def __init__(self, name, year_of_birth):
		# for the __init__ method, please assume that the variables
		# self._name and self._year_of_birth would be appropriately
		# initialized with the respective arguments

	def __str__(self):
		return f'{self.name} is born in the year {self.year_of_birth}'

class Student(Person):

	def __init__(self, name, year_of_birth, subject_of_study):
		super().__init__(name, year_of_birth)
		self.subject_of_study = subject_of_study

	def __str__(self):
		return f'{super().__str__()} and studies {self.subject_of_study}'

everyone = [Person('Max', 2000), Student('Max', 2000, 'Management')]

for i, e in enumerate(everyone):
	print(f'Person {i}: {everyone[i]}')
```
❌ Person 0: Max is born in the year 2000
     Person 1: Max is born in the year 2000
✅ Person 0: Max is born in the year 2000
     Person 1: Max is born in the year 2000 and studies Management
❌ Person 0: person 0
     Person 1: person 1
❌ Max is born in the year 2000
     Max is born in the year 2000 and studies Management
❌ Max is born in the year 2000
     and studies Management
❌ *Nothing will be printed because an error will be raised.*
❌ Person 0: Max is born in the year 2000
     Person 1: and studies Management
❌ Max is born in the year 2000 and studies Management

<details>
<summary>Explanation</summary>

To identify the correct answer we must understand 1️⃣ how the magic method **__str__()**, 2️⃣ inheritance, Polymorphism specifically, and 3️⃣ keyword **super()** work.
1️⃣ **__str__() **method is called whenever we use **print() **or we access the object inside a string**.** Python then executes the code that is inside the **__str__() **method. In the code above the **__str__() **method is implemented for both classes.
**Person****.__str__() **→ ** **the name of the person is printed and its year of birth
**Student****.__str__() **→  the method** ****Person****.__str__() **is called (which returns a text containing the name and year of birth of the person) and the subject of study is attached to that text
2️⃣ When looking at the class header `class Student(Person)` we see that **Student** is a child of the class **Person**. Thus, whenever we create a student it inherits all attributes (`_name` & `_year_of_birth`) and methods (`__str__()`)** **of the **Person **class. So, for a student object, we can also access the attributes and methods that are implemented by the **Person** class, without creating another person object.
However, we see that Student and Person class both have the **__str__() **method. So, when we have a student object `student_janick` and we call `print(student_janick)`, should the code inside **Person****.__str__() **or **Student****.__str__() **be executed? Due to Polymorphism, Python will execute the code that is *more specific* to this object. As **Person** is a generalisation of a student, **Student** class is more specific to `student_janick` and thus the method **Student****.__str__() **will be executed.
3️⃣ With the keyword **super()** we can access the attributes and methods of the parent class (**Person**) from within the child class (**Student**). In our example, this allows us to access the a person’s name and year of birth form within the class **Student**. Also, it allows us to execute the method **Person****.__str__()**. 
If we look now in the code, this is exactly what is happening inside **Student****.__str__()**. We call the method **Person****.__str__() **using** **`super().__str__()` which returns a text containing the person’s name and year of birth. We take now this string and extend it with the student’s subject of study. This final string is then returned from the **Student****.__str__() **method.
---
After having understood these three concepts, we can now dive into the code.
We see that for Max we create one instance of class **Person** and one instance of class **Student**. We store both class instances in the list `everyone`.
Now we iterate over the list using **enumerate()** function. This function returns the index position of the current object and stores it in `i` as well as the actual class instance object which is stored in `e`. 
<details>
<summary>1st run → Person 0: Max is born in the year 2000</summary>

We have the following values assigned to `i` and `e`.
<details>
<summary>`i = 0`</summary>

Because it is the first run
</details>
<details>
<summary>`e = Person.Max`</summary>

`e._name = 'Max'`
`e._year_of_birth = 2000`
`e.__str__()`
</details>
Now the output string has two parts:
<details>
<summary>‘Person {`i`}’ → returns ‘Person 0’</summary>

Integer 0 is saved in variable `i`
</details>
<details>
<summary>{everyone[`i`]} → returns ‘Max is born in the year 2000’</summary>

- Max is an object of class **Person**
- We access the object, thus **Person****.__str__() **is executed
- This returns** **the string ‘Max is born in the year 2000’
</details>
If we concatenate these two parts together we get:
Person 0: Max is born in the year 2000
</details>
<details>
<summary>2nd run → Person 1: Max is born in the year 2000 and studies Management</summary>

We have the following values assigned to `i` and `e`.
<details>
<summary>`i = 1`</summary>

Because it is the second run
</details>
<details>
<summary>`e = Student.Max`</summary>

`e.subject_of_study = 'Management'` 
`e.Student.__str__()`
`e._name = 'Max'` → inherited from **Person** class
`e._year_of_birth = 2000` → inherited from **Person** class
`e.Person.__str__()` → inherited from **Person** class
</details>
Now the output string has two parts:
<details>
<summary>‘Person {`i`}’ → returns ‘Person 1’</summary>

Integer 0 is saved in variable `i`
</details>
<details>
<summary>{everyone[`i`]} → returns ‘Max is born in the year 2000 and studies Management’</summary>

- Max is an object of class **Student**
- We access the object, thus **Student****.__str__() **is executed
- Inside **Student****.__str__() **we concatenate
- **super().__str__() **
- which calls **Person****.__str__()**
- This returns the string ‘Max is born in the year 2000’ is returned
- and studies **{self.subject_of_study}**
- which accesses the attribute **Student****.subject_of_study**
- This returns the string ‘and studies Management’
</details>
If we concatenate these two parts together we get:
Person 1: Max is born in the year 2000 and studies Management
</details>
</details>
---
## Question 5
One task in the assignment was to implement the *instance method ***.heal(self, other) **of the class **HealingSuperhero**. **HealingSuperhero** inherits from **Superhero**.
Let’s assume there are two instances of Superhero: **danny** and **hulk**, while **danny** is also an instance of HealingSuperhero.
When calling **danny.heal(hulk)**, which one of the following statement is correct?
❌ An error occurs because it is important on which instance the **.heal** method is called. The correct call would have been **hulk.heal(danny)**.
❌ The execution stops with an error message because the instance method **.heal(self, other)** expects two parameters and only one was given. 
❌ It is not guaranteed to work because the **powerlevel** on one or both instances could be 0, which will lead to an error (*DivisionByZero*).
❌ The powerlevel of both instances will be increased according to the implemented rule.
✅ The **powerlevel** of only the instance **hulk** will be increased according to the implemented rule.

<details>
<summary>Explanation</summary>

❌ **Incorrect**. danny is an instance of class **HealingSuperhero**. This class implements  the method **.heal(self, other)**. Thus, the call **danny.heal(hulk)** is correct.
**hulk.heal(danny)** would throw an error because **hulk** is an instance of **Superhero** class only, thus **hulk** has the method **.heal(self, other)** not available.
❌ **Incorrect**. The method expects only one parameter: **other**. **self** is the default parameter which tells Python to execute the method on the object from which the method is being called from.
❌ **Incorrect**. Inside the method **.heal()** we do an addition and no division.
`other.powerlevel += self.powerlevel`
❌ Incorrect. Only the powerlevel of the superhero saved in the other parameter will be increased.
✅ Correct. **hulk** is provided as value for parameter **other**.
</details>
---
## Question 6
Which of the following statements are True in the context of **object orientation**? Please *mark all* True statements. 
✅ A subclass can inherit attributes and methods from its superclass.
❌ Classes are instances of objects
❌ A method in a subclass must both have the same name as a method in the subclass’ superclass. Otherwise it is not clear, which method to execute. 
✅ In Python, classes may inherit from their superclasses over multiple levels of a class hierarchy. 
✅ While private attributes (e.g., *_variablename*) can be directly manipulated in Python by client code, they should not be directly manipulated by client code.
❌ If an object is an instance of a subclass it cannot be an instance of the subclass’ superclass at the same time. 

<details>
<summary>Explanation</summary>

✅ **Correct**. That’s the definition of inheritance 🙂
❌ **Incorrect**. Objects are instances of classes. Multiple instances (and thus multiple objects) of the same class can be created.
❌ **Incorrect**. As we have seen in [Question 4](/1fc79937e6494e4d81b5ad6c98c5da49#4a5cfb1647154934bc2bfd83bf745f48), [Polymorphism](/1fc79937e6494e4d81b5ad6c98c5da49#8e66b9f440dc4520beadca7059fee6cd) takes care of which method to execute when. For example, when a method with the same name exists in the subclass and the superclass, then the more specific method, i.e., the one in the subclass is executed.
✅ Correct. We can have multiple levels in the class hierarchy.
For example: 
               Person
               Student
 Undergrad      Postgrad
✅ **Correct**. Although an attribute is private, it can technically still be accessed and modified from outside the class. For this reason, we create getter and setter methods.
This is also because Python is an interpreted language. In a compiled language like Java, when declaring an attribute as private it is technically not possible to access it from outside the class.
❌ **Incorrect**. An instance of a subclass is automatically an instance of the subclass’ superclass, i.e., whenever an instance of the subclass is created, an instance of the subclass’ superclass is created simultaneously.
</details>
---

📄 **[Quiz 6]** (subpage)
## Question 1
Which additional key-value pair must be added to the request params in Line 8 in the given code example if you only want to receive the first 10 connections?
Look at the he documentation and select the correct statement: 
[https://transport.opendata.ch/docs.html](https://transport.opendata.ch/docs.html)
```python
url = 'http://transport.opendata.ch/v1/connections'

params = {}
params['from'] = origin
params['to'] = destination
params['date'] = departure_date
params['time'] = departure_time

r = requests.get(url, params=params)
```
❌ `params['limit'] = 10`
❌ `params['10'] = 'limit'`
❌ `params['page'] = '10'`
❌* The API already considers only the first 10 connections by default. *
❌* There is no possibility to request the first 10 connections. *
❌ `params['page'] = 10`
✅ `params['limit'] = 10`

<details>
<summary>Explanation</summary>

In the API documentation, we see that the number of connections to be displayed in the result can be specified over the `limit` parameter:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c6e17cac-20fa-47d5-8e77-41b1b793095d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QOOIRNG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDBrWVuGDy%2FMzkT6ifOoAjBSw41o%2F1hm6CI8wUYx6NCVAiEAzMf7ILn%2Fq7v0A3WSSE6laX4v1SfoL%2B9DfiNcI%2BjhPS0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDAkpXYWUEac6zLIrQCrcA1JK5aVOd5N9zGgWNiA8iEpGZF28NZ%2BxDx3esx1lyX5mcwx5R2zTifetVMj0%2F8%2FyppfpVfNSfJnWx4PTOhIM8kDr833xL6%2FCRUmNdjLSGLbc%2Bx49My5stjlClx3Buk57Rim%2F3Zm7Hbsitt81cul5AM9ArhSXILcs35oyOLWPNNN%2Fp5RvqN9jUx0ps%2F9eoKkm7chgwj0j2pFNQeY0NloVZynn92XmkoxEprgzZQ0tqg3sEdCaRqkoz8VC0mOY94EuNd0BdLxKrTaTyk0QylTNk52aUETPw9bcL8ap6ZEt7lRiTuo1D3aZ%2BDK94O4y9%2BhgrWc%2BsV6v3pBumpEkhzIlzfPvMrdVFk8SAiTrlJ7d3aA4Bib6hC4lQy5Am4zTT1y8aoULPj5bqSTvsnXXhj6bYJU1W2B%2BSWCtvfCqYQ9EhTi8BOOm7bwBASBAmrX3xCbvg4Tao%2BH0wLzmgjkDz3O%2Fc%2FnA%2F0BCXfDIhNS8syFFLyFQCjfqTVBMIEVuQ1OBi0Wrr%2F7%2FklNrrIQ1NGd6Wd0oFsJQC2YsOI2%2Bh9YCxgpc2EpvKpXV%2Bfatd8hzI8cxSqO26dF4mj2%2FxzZE%2Bc9uEtq50YDJA77y8i7LABQrrYsvH8vOKtz%2B3f0DvwsBrcnUMITO98kGOqUBiPy1zEWlFt0K%2BxnUMN0gyK878pMJweQmXdO26fXkNMnQDCm1gvkB5LOuJIs213xYtZfJPBDnZKdgERlvMqYi%2FupP%2BbD1PYJwfMf6TH%2BbMBHfEjhNEqjjkKviHvpiLSRTqUtRWBjTSeKPOcnyIRGHMZAb0uob1kLz4Ua7zMe%2BUc5P%2F6G0m06a%2BLkibVl5L%2By9fhQ524z%2BesAGI0XYXwcZYbHHpYEZ&X-Amz-Signature=452609fcb97d23cffa96bbd73b669fe459232dbb8df517cac735de13c2908996&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
## Question 2
If you launch two different Web browsers (e.g. Chrome and Firefox) on two different computers and open [https://unisg.ch](https://unisg.ch/) in both at the same time, which of the following applies?
❌ In any case, both browsers will use the same local port to access the remote server.
✅ In any case, both browsers will use the same remote IP to access the remote server.
✅ In any case, both browsers will use the same remote port to access the remote server.
❌ In any case, both browsers will use the same local IP to access the remote server.

<details>
<summary>Explanation</summary>

❌ **Incorrect**. The two browsers are running on different computers. The local port for https connections can be different for the two computers. 
✅ **Correct**. Both browsers are accessing server of the university over the URL [unisg.ch](http://unisg.ch/). Thus, both browsers are pointing to the same remote server, which is assigned exactly one IP address. 
✅ **Correct**. Both browsers are using the https protocol. Thus, the unisg server receives the requests over the same port (usually 443). If one browser would do an http request and the other one https, then the remote ports would differ (http → 8080, https → 443).
❌ **Incorrect**. The two browsers are running on different computer. IP addresses are device specific and unique. Thus, they differ between the two computers.
</details>
---
## Question 3
Consider the following code that implements parts of Assignment 6 and mark all correct statements.
```python
def find_top10_restaurants_for_trip(origin, destination, departure_date, departure_time, radius):
    limit = 10
    connection = find_connection(origin, destination, departure_date, departure_time)
    restaurants = find_restaurants(
			c.destination_x,
			c.destination_y,
			c.get_unix_arrival_time()
		)
    rests_sorted = sorted(restaurants, key=lambda tup: tup[1], reverse=True)
    
    return rests_sorted[:limit]
```
✅ After line 7, *radius* needs to be added to the function *find_restaurants()* as an additional parameter after *connection.get_unix_arrival_time()*.
❌ In line 3, *radius* needs to be added to the function *find_connection()* as an additional parameter after departure_time.
❌ In Assignment 6, this code generally would not work because the datatypes from [*transport.opendata.ch*](http://transport.opendata.ch/) are not compatible with [*api.yelp.com*](http://api.yelp.com/).
❌ In Assignment 6, this code leads to the issuing of two HTTP POST requests (to [*transport.opendata.ch*](http://transport.opendata.ch/) and [*api.yelp.com*](http://api.yelp.com/) respectively).

<details>
<summary>Explanation</summary>

✅ **Correct**. In the assignment we see that the method find_resturants() requires the parameter radius. 
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6cbc72ed-5f0b-43c1-8dc2-80432c9425f7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UV7AMQX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCR2Kgb10r55KZeKIE0dXIn0ZM9A90k0K347Dc2zqA7bQIhAOgV8mmzfOnHh3D3ICLyaswBhMbVgDMK43BYnsssBaFSKv8DCCcQABoMNjM3NDIzMTgzODA1Igwe2rndaMcpussl1nYq3ANmtAljUjN17jlkk7ptmXL%2FvdygA6%2BeyLDxbN01jSXQUGnZLarJeOme0oL%2Bt3x90RqWFwKPdvEIcFGbmQ%2FFkbJv68yAx36ZflVUFw5Oy4uQ%2Bjyi%2FDbpriUGECf8pMQKjqUtSdTGlaiFfosVfXVOv5PWRptI%2BbBGJAPnLgyd%2F29zs47KVp9XWab2TsNbZEP7Ue%2BxPoqWm%2FsMYB8ScghYHvnAe%2BVuw1EeBvJYFEyFBCRF3uISDTmg1ym5GyM1s1HocxISYv5nwyhI1r5fRGa6KKynT%2F1sfaCG77PgGCeF8G2q4uDFrM7Z3sEDI9RNzMsXqrBz93P2zCyBI9v9rFRmw8IztOJCfEXHP8Su587x8ra1RdHdkB5NGFDsBBOSIMXYS7PYPAhg6sQZ3Xt4CKFKnEh7H9WrxpdFEjpdc2BPBcXLaFRr9KoFJKHnmVdAeGgl5KzD3iFNMa0HIYf3u1XY03Osu%2FDBBm5aIjRsA3RYvCRKoTKNUXDP0UVwzZ%2B25vEMfDyfQciJ8FIdiXUTO0My1RYZQ%2Fh6SldSVZnlLPR8Z9R%2BfQyft%2BlbE6%2BPoa45NJKlJLR5jKfM2gibw%2B7ePDaQ5BXNJYE7qnNlUsbxUq43YJAt%2Fh7WkCR%2BrYEdqZ8doTDlzffJBjqkASVEDpRb3SlMI6kaXRtOaJ3KbWJWkZS8XpSOurlSX5XE3GR8m4wPJQ%2BoJSFtRq4R9GlbjgEz0Be4VznxNZAxgVQSQ%2F8OhAjnU458NComrxHjPYPvi9MAuq4Zv14P8w2vQpvM%2Bp7Hbcqkdsyge%2Fe7ZHTtqYi5RlymSX1KSQqPc99m%2F%2F81p%2FWbTygmGOIwgV1RBw5%2B7h3fjbC2oOlrXgrm%2FYJIb0DW&X-Amz-Signature=a76c0d2f0269ed7637446167e1638f61ff8bd0ca4fa5f1dac89684446b0c269d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
This is because the [Yelp API tells us](https://docs.developer.yelp.com/reference/v3_business_search) that this parameter  must be provided to look for businesses around a specific location. 
❌ **Incorrect**. Radius has nothing to do with public transport connections. 🙂
❌ **Incorrect**. The datatypes are compatible. Both API expect and return JSON objects. And we already learned [how to work with JSON objects](/5b0832dbf9454eb1941b7632e68a9abb#2248b4b3bfb444e89a15bbeb58513b6e) in Python.
This is exactly the power of JSON. We don’t know whether the Yelp API and Open Transport API are implemented with he same technologies. However, because they both adhere to JSON standard, we can use the output data from Open Transport API as input data for our request at the Yelp API.
❌ **Incorrect**. As we are retrieving data from both API’s we are issuing GET requests. We would use POST requests if we would want to create a new resource on one or both of the servers. For example a new train connection or a new restaurant that recently has opened.

</details>
---
## Question 4
Consider the following code that implements part of Assignment 6. Assume that “abcd” is a valid API key. 
Your colleague asks you for feedback on this code.
What do you tell them?
```python
api_key = 'abcd'
url= 'https://api.elp.com/v3/businesses/search'

headers = {'Authorisation': 'Bearer ' + api_key}

restaurants = {}

params = {}
params['latitude'] = x
params['longitude'] = y
params['opening_times'] = opening_times
params['radius'] = radius
params['categories'] = "restaurants"

r = requests.post(params=params, url, headers=headers)
```
❌ You need to use a PUT request in line 15.
✅ You need to use a GET request in line 15.
❌ The variable radius in line 12 needs to be cast to float. Otherwise an error will occur.
❌ The code works perfectly.
✅ The parameters in line 15 are in the wrong order, they need to be orders like this: 
`r = requests.get(url, params=params, headers=headers)`
❌ The parameters in line 15 are in the wrong order, they need to be ordered like this:
`r = requests.get(params=params, headers=headers, url)`

<details>
<summary>Explanation</summary>

❌ **Incorrect**. We are retrieving data from the server. Thus, we need to use GET request.
✅ **Correct**. We are retrieving (getting) data from the server.
❌ **Incorrect**. Because statement 5 is correct, which means there is an error in the code.
✅ **Correct**. According to the [requests library documentation](https://requests.readthedocs.io/en/latest/api/#requests.get), the url must be the first parameter.
❌ **Incorrect**. The url must be submitted as the first parameter.
</details>
---
## Question 5
When working on Assignment 6, which packets did you see in Wireshark when interacting with [https://unisg.ch](https://unisg.ch/) ?
✅ TCP packets with TLS-encrypted content.
❌ UDP packets with TLS-encrypted content.
❌ TCP packets and HTTP packets.
❌ HTTP packets with TLS-encrypted content.

<details>
<summary>Explanation</summary>

✅ **Correct**. Because we are using **HTTPS** on the **application** layer, **TLS** is used on the **transport** layer to establish an encrypted and secure connection between the client and the unisg server.
❌ **Incorrect**. UDP connections are not encrypted with TLS. TLS is used to make TCP connections secure. → [Difference between UDP and TCP](/305c770201f94279bfd468d86c733ae6#0dea562007ff4bcb8e4f0fd74d244a86).
❌ **Incorrect**. As we are using the secure **HTTP****S** in the url, we cannot see any **HTTP** packets.
❌ **Incorrect**. TLS is used in combination with HTTPS. Both protocols enable encryption. HTTPS on the application level and TLS on the transport level.

</details>
---

📄 **[Quiz 7]** (subpage)
## Question 1
Please assume that the table **persons** exists, with a non-null column **grade** that has correct numerical values and a column **course** that contains one course name in each tuple as a String.
Fill in the missing keywords to compute and return the *mean value* of **grades** for the ten best graded courses in the table **persons**.
```sql
**SELECT** course, **AVG(grade)**
FROM **persons**
**GROUP BY** course
ORDER BY **AVG(grade)** **DESC**
**LIMIT** 10
```

<details>
<summary>Explanation</summary>

Whenever you need to answer a SQL question it is important to first make sure you understand the data structure. In this database there is only one table, with at least two columns:
| ID | name | course | grade |
| --- | --- | --- | --- |
| 1 | Max Müller | Micro II | 3.9 |
| 2 | Marie Meier | Statistics | 5.1 |
| 3 | Alex Muster | Micro II | 4.0 |
| 4 | Lea Kälin | FCS | 5.4 |
| 5 | Marco Bühler | FCS | 4.3 |
| 6 | Anna Friedrich | Statistics | 4.9 |
From the example data above, we see that each record / row in the table represents a student’s grade for a specific course. 
Now the question asks us to select the top 10 courses by average grade. Thus, we want to calculate the average of the values in column grade per course.
Assuming the example data and that we want to select the top 2 courses, the output from our query should look like this:
| course | AVG(grade) |
| --- | --- |
| Statistics | 5.00 |
| FCS | 4.85 |
Now that we are clear on what the output should look like, we can think about the query we have to write. Below, you can see that happens in the query line-by-line.
**Query**
```sql
SELECT course
FROM persons
```

**Output**
| ID | course |
| --- | --- |
| 1 | Micro II |
| 2 | Statistics |
| 3 | Micro II |
| 4 | FCS |
| 5 | FCS |
| 6 | Statistics |
```sql
SELECT course, AVG(grade)
FROM persons
GROUP BY course
```

| course | AVG(grade) |
| --- | --- |
| FCS | 4.85 |
| Micro II | 3.95 |
| Statistics | 5.00 |
```sql
SELECT course, AVG(grade)
FROM persons
GROUP BY course
ORDER BY AVG(grade) DESC
```

| course | AVG(grade) |
| --- | --- |
| Statistics | 5.00 |
| FCS | 4.85 |
| Micro II | 3.95 |
```sql
SELECT course, AVG(grade)
FROM persons
GROUP BY course
ORDER BY AVG(grade) DESC
LIMIT 2 # 10 (in exercise)
```

| course | AVG(grade) |
| --- | --- |
| Statistics | 5.00 |
| FCS | 4.85 |

We see that the key-statement we are using is `GROUP BY`. Whenever we use `GROUP BY`, we are aggregating data rows in a table, i.e., reducing the number of rows. To do so, we have to tell SQL two things:
- **Grouping column **→ Column `x` in the table should be reduced to unique values only. In our example, we wanted to have unique values only in column `course`, thus we used `GROUP BY course`.
- **Aggregation function** → How duplicate values in grouping column `x` should be aggregated / put into each other. In our example, `AVG(grade)` was the aggregation function, which calculated the mean value in column `grade`.
</details>
---
## Question 2
Given is the following table students:
| **id** | **first_name** | **last_name** | **date_of_birth** |
| --- | --- | --- | --- |
| 51759 | Meghan | Peery | 1996-12-26 |
| 53532 | Lashanda | Maglioli | 1999-11-12 |
| 50399 | Jamey | Sobotta | 1999-01-07 |
| 59587 | Julianna | Ravitz | 1998-03-29 |
| 53646 | Sylvester | Sampere | 2000-07-07 |
What is the numerical result of the following query?
```sql
SELECT COUNT(*)
FROM students
WHERE date_of_birth < DATE('1999-04-15')
```
3

<details>
<summary>Explanation</summary>

Here the output should be the numbers of students that were born before the 15th of April 1999. Let’s go through the code step-by-step.
**Query**
```sql
SELECT *
FROM students
```

**Output**
| **id** | **first_name** | **last_name** | **date_of_birth** |
| --- | --- | --- | --- |
| 51759 | Meghan | Peery | 1996-12-26 |
| 53532 | Lashanda | Maglioli | 1999-11-12 |
| 50399 | Jamey | Sobotta | 1999-01-07 |
| 59587 | Julianna | Ravitz | 1998-03-29 |
| 53646 | Sylvester | Sampere | 2000-07-07 |

```sql
SELECT *
FROM students
WHERE date_of_birth < DATE('1999-04-15')
```

```sql
SELECT COUNT(*)
FROM students
WHERE date_of_birth < DATE('1999-04-15')
```
| **id** | **first_name** | **last_name** | **date_of_birth** |
| --- | --- | --- | --- |
| 51759 | Meghan | Peery | 1996-12-26 |
| 50399 | Jamey | Sobotta | 1999-01-07 |
| 59587 | Julianna | Ravitz | 1998-03-29 |
3

</details>
---
## Question 3
In your database, you have at least the following five tables (same as in Assignment 07):
- **students (id, first_name, last_name, date_of_birth)**
- **registrations (id, student_id, immatriculation, exmatriculation)**
- **courses (id, name, category)**
- **enrollments (id, student_id, course_id, semester)**
- **grades (id, enrollment_id, grade)**

Which one of the following queries returns all students that have a grade better than 5 (which numerically is greater than 5) in the course ‘Fundamentals of Space-Time-Travel’?

❌ **Query 1**
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade < 5
	AND
	courses.name = 'Fundamentals of Space-Time-Travel'
GROUP BY
	courses.id
```
✅ **Query 2**
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade > 5
	AND
	courses.name = 'Fundamentals of Space-Time-Travel'
GROUP BY
	students.id
```
❌ **Query 3**
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = grades.id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade > 5
	AND
	courses.name = 'History of Space-Time-Travel'
GROUP BY
	students.id
```
❌ **Query 4**
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN students
	ON students.id = grades.id
INNER JOIN courses
	ON courses.id = grades.id
WHERE
	grades.grade > 5
	AND
	courses.name = 'History of Space-Time-Travel'
GROUP BY
	students.id
```

<details>
<summary>Explanation</summary>

We want the students with a higher grade than 5.0 in the course History of Space-Time-Travel. Thus, we must look into the different code snippets and check where we find the condition:
```sql
grades.grade > 5
AND
courses.name = 'History of Space-Time-Travel'
```
We can find this condition in the **second** and **fourth** code snippet.
When looking at the fourth code-snippet we can see that the first join is not going to work, as there is no direct relation between **students** and **grades** table. This makes sense as one student can be enrolled into multiple courses and thus have multiple grades and a specific grade, e.g., 5.0, can be achieved by many students. This is why there is a table **enrollments **in between.
To validate, that the second query is correct, let’s execute it step by-step.
1. We join enrollments and grades to know all the grades of all the students.
```sql
SELECT *
FROM grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
```

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f8640f82-72d0-485f-ac2d-1c5b0a940cce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJ5Z3WC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFn0B%2F23hnUKKqqmJwuqTRnWnK4aWVY75J8fQlZOQl1bAiAQyeRji8lyPweKfyEslGqoWCkakElxi6jNT7FVLk9UFCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMI%2Bh6qFkXSXbKY%2F8uKtwDcN48%2BT5942Uw%2FJ1nbzQZ1b5B0hl%2BMp6J5Qy1smXZKFUUsx8Pn6Whc9EmsYTLdxLQaz2bYUxNhMBsjQVweNM3YyUD%2FoX2xtLoBa6U0oykYkO4TQOHVsq7qiCi822Wd%2Ft1q%2F%2BvhGeZ9NyB1vjYVxEn3bR2Gi%2FhcGD%2FjBKNHAXBOgSLwAek4LdYc4Y5uIkQz1m4lKwoCaaONPp4QcMXLhSH3hE7o9G3ps587tNNjlOxBf6wXdLBYUDqfCxfjLJmxC1fCXuHzy9E%2FapddqYctAziaIKlxRwr0NhXEW2fVfwexkG7SQjhcdSs247PQHID%2BczLiTI%2Frh2kuIS9dMl3vSnAI90lna74O36K8c01aIMHVgGFsGj2GzusiPWDK4j5AHxmsJfnRfmHVUv5jSkX%2B%2BOkmkDjt8s9R9g0GXA8pip8FKj2iotvLb5hy4SHAvI4d4E4SPv5BJEvVwoRHe4ahhPpXYPI8uJA0D6WQKCPW3IhEHjjSOsnPCpYcYro2xu9FeFgOMJRMVooKfHqQCrRiJBE6BqGHYzXz1XtHvoR%2F1hXIaTVcT1Z%2BYuVQgmWnlchUcS5hW%2FIOH5LLGEO6CefxPvvRxfmKUHYbRoys%2Bjt7KvEnzWNeKudlIPxTaxA6KowmM73yQY6pgHMQf7SVsKM%2F%2F9cWcMKj4WAodloK45QHpFIh4ROQvpCJ%2F836gUUaVSXRHQoutjYbHpQbqBkRKDTHWJpQ1j7B9ZQX6kBnJkrYC1z0rbtEQqABg%2BD88FBtTFhnFGJfkoN8hJ4vDAuyYMjP03K2Z4mQ7wyTpNldhGMLFbis14OfDQflP%2BdH068lHi8blq0FLyBNRdMSzSY%2B2myGaL3gR3AGoybyUzFsL6H&X-Amz-Signature=19f77d8687916151fbbb5a27e36089c96f3825f60fc5bafeb2b3718602eb8163&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join courses with enrollments to know which student has achieved which grade.
```sql
SELECT *
FROM grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fcd7ff2b-aa13-486f-b950-463a2c9048b6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C52WUIZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBzWsPbK27owZV6v3OFk8MMe8TrwcAI391zfK71A3shJAiA6K8SKuf1XgWbtFVe4pBLzQLvPJzETc3DqbpOgM0%2FIzCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMFX%2Bb5SICGDC5fszrKtwDDPgZImJHjDCFvuxkuT6Bkg2fumgbIcKI3P4Rop%2BwEjZEKEgACSb2PMluFrN2RKYP6obkRkyfvhYdcarUXiIFw2QhkfUoue16HZ1gIdKEofngfeHdpzPGQEjtUvWLf6SZhAhWHw4O%2FM15qwtKLpwH2Kqm4kfrF8V7PPpRwKSTiAC0knc7vVk51iBvxObpFhBLlFiEUyYmOHazPIKRXZiiyMBvTI51wfweHRa2XZUp6CzIPcLO7y9VXKStPguwHmfPGxcGBWNzi3YsVFWX7ND4dJcN6znih%2BCKPWXazFLghSPtztL1n8Frd2MECk8dg0tl6WeFZdzYaK0mq0kshI0q28%2BTMqqB2iiETRUpOkCMbR%2BwLTrGK1joysY47CvxIiRQkzKSL6oDRVHTJCOJ3NV%2Bl%2Ba%2F4loPtdVk7UAL0OQ%2B8UT7K0%2BDdpenBMX9XjYcOWPUhbtvhdOhzxwlGUUj1GNaQlsNRue9WLSVan1bkUzjwguJh6F6MFHJkzvWja%2BBUG%2BzmzSLYMIxhrS7LyrtDrhbw3jTpodAy6U58nwBHWOD49rztrOhKzdHHHDXEwEeBnDEwozr8ZgujTxKzFX5eSpPA1aAZTaXJK%2B0XYH%2BCdhW6CeVudWdaj0Rqrzx4Lowq873yQY6pgGO9G2UoHyZUZZomKKYcDxipwbcsqsbqYvFFy4mutOOpvSLdWyImmTp57x16PQgsdNMA2aoAyJGjrV7ih5zkXM5EjjWk%2F4HOqF9g0A4lphC%2BwtvUFXrFYIZWyl0Ypq4e5M%2FtyV%2BwHvK%2Fo3fkaxghWM8YJLu62slHDDfNasAoS7vr%2Be%2FxhVc6IzUe%2BTo28xbFQsa8bq66tXaRRDRXfxGsNcSIu6zk9KE&X-Amz-Signature=2902d352eb8b476c5f51a9f4c30dbc3e1e2b36681249008a95dce35520b60c2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join the courses table to see in which course the grade was achieved.
```sql
SELECT *
FROM grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8ab9b52d-3764-4ef5-9bec-045d82960315/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDM4FOH2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDKSrGqdgMEgk9jwjel8ta8HgC0U5X0qkZi2krkUn0WeQIhAOzHPXONRINEg2vtnffEQol%2BOG0mf9trihSp2sNsw5uCKv8DCCcQABoMNjM3NDIzMTgzODA1IgwNH%2FILfDNIsu3y0bYq3AMbg5%2FDRovtlyJUYg9KgqGEc7lTuai75bHDd3Tswqx3Ad0ZF97Xc%2F5cmUyMPzzv%2Foi%2FzJpNtc75T3cnzM%2FB2j9HB2VaVE4ys8ZvY86u8Qblq8OZVY0myjo8SuCNcq7MWn9CMmcZEk%2FnLnH5xn9UfvuI2k278Sj77r1f2cvm8KCCjc0T7EIeVO7w4wh%2BPFzVO1fqo2NzUwY%2FBN7VyXjZeVruzEio%2BSb8kI5B0WJvtT71CFDSBEd8YAk295270v1cswKWvuiSdbqRFVNnAcUO80lZNIxAE35titWjaj7NXbhsNKoy%2B7w5inxdX8ryhHDpESYVV%2BKswfqTnsEZhps9xweJpgtGOsOWgCYg4fDlC7AKWeQYa0JF%2BlR6AOCUh0DLRuTjxgFYF21cdv%2BDz5oBTGJpDTr9ai5PHM27adQCnyuilk82uhSEgm3uzkwhI7H9uQ4DHEkZVsyxbTYlXxpI82U5hnhN8Tr%2BUbuDP%2FOLZCEaWP%2F3IOTVK850VpQhspwSkoeHEh8ROsOS3CTfrwWJcK8HZ2TAknzG9XGjM62SvP67wVNc7kI%2BqWuLljG1nKKoHX90Vobb%2BUDduJVCZr85eQDG0cCWPxqkhUCtBaAGwx%2FvhU4VEmDZwfo%2B6Q06xjDozffJBjqkAWUe4y3MlocpaMI8NnbKQoc%2F37ts3Rq%2Fu4SzeNIp1n6Yj34kyACeu4MwIbPr4HOm9ArtvlxMGTJBvWup1%2FXFDOHgFVIVchjX7%2FuKKOK0Ti975aUeK%2BQgueJT4mzVZp88fWOYewl%2Fx%2BFJCVr64bInIK3qHCQnIhOaS%2FsghfjeCigo3BBEXbzPp2TZRyStm65WGnVgTYydp8irBqKubyZslRNqub80&X-Amz-Signature=ca7046f07a2947496592ee58018e31fffd327b09dcfb713baa248a2dd0aceca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We can now start filtering our data table and select only the records that have a grade higher than 5.0 in the course 'History of Space-Time-Travel'.
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade > 5
	AND
	courses.name = 'Fundamentals of Space-Time-Travel'
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/236210d3-f5a0-47d4-abe4-d2c76f246867/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCU5LBJ6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIDcd9Y8SGKg%2FP8Hpvoq9LsWDiqwJpjt1hCRHwSy4VjbgAiA9fYZwR7TM5Vrd%2FoT1pWOB67P2za5IEAYYuxjyX8sqwir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMaScWxnV5mUWMUybGKtwDH3mrHoSBthmq%2BCd8OID1qqkijL4BqTMWSkRgsANEnLN2UmWJpOsYLa4FA3VksHMysI%2BRzjGKR9S6rR8VBxYROVTY4y5zttC4Pwqz2GU96q4iiiStoA%2FiUbidPDxM%2Bk0D4UgWCoZEKwy0IizC9%2FIBMgZVJ8xT%2B0jyJZGtqAaZT1SZDZTimItXq3E9q%2F7fNSu2DmF0EX%2BczbqiAudcjLGpXU614EGVSU0XBGk7XCqb2mreHNraoFexz8bzngXA8yPuGycoSvj9tlSfm%2BogITW2hejBpebtw6%2FC8m7b4XMlsUwJrVo0YEfRU6ch0xQcamqZsLUDZWxiKYTCa0u5HZbuBC8fhzSUAJ1R3zu7Pb%2FgGyFs5lZknyGn4NZbl2JLx30jv%2FzkJ1jBTvE7kzsR54rwKOh8p%2BeqxfqtjjmlCtzlRoCDLySUsq16SMTaOInPkimKbJbQ0tETjs7xMexhNUnCXRz0DA4G%2FWzUs4fAPUAR1nmmMFoSDYtMENg7OxSVlTZC61Tc%2BxM6UHUkQtNUxnjICqB1l7LwPCQdyXxUqNIAg%2FSTvzHNIQp82TI3TbFaBah8AGJp5SeUvJlt8%2FrJg6rS26o3Lx4ufEuswE45DRNV9XFxhA5ygL9oeDfkLYAw0873yQY6pgGcFkPFdqR3pB6adPlCakkLENfj1sGhG9Ey3uSr4gh8xBNXYV3H7sAe2C9BAHf2GXZpPrZUR%2FDIAb7B83BG%2BDoqC7wCVIRKA5tiJ87eoroJOMrq%2BkgyGxBJxR9qQkrKTMhJRtDDgC5ts4XyYrQ7k24GlgRFyeTH8pIDib03q%2FiYoQKwGL5aLLTQgldN43NXk8EqxorC%2BUcxKiUj48%2FQrPwc1Cg53OB4&X-Amz-Signature=e5010cef2bc94f8e540cb026cd51c318c03269a33373bd370d49616d36b352c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We can now group the records by student and select the relevant columns only.
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade > 5
	AND
	courses.name = 'Fundamentals of Space-Time-Travel'
GROUP BY
	students.id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b033da62-45a0-473a-b625-896edcb536f3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMOGW2FN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDiHo8cO4IEAJQFHOnQTC8NiJ7p%2B7foQ3dGcY6F73hPbgIgPol2pEfgfBN60FkSxW9R4WrQ36qUw7bWrelTWF5z6BIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNXzDj0DToPnxffqqircA1wUHnaqvDLDVH8KHg1gsnAiS2Z9oXzGdmGhcc%2F5wIjs6VZ0b%2F5QPJkVqB47AI3GcWO0t2Z91gi%2F7oNpHjNUdpv1dh6TW7xtxuq5kZuZkckJe37QEt%2BOuG35xAT0tWh1j9PR036Rt5jn4XS5%2B0dZtw58n0%2BhWz94sr%2BBQGhzwAmJVMDJmqbSWNhxbQr%2FnUCWncTlAWOD2OCNsSnoi4VI%2BfCQfacj%2BwY14NDnpNd6zS7Uj5peE0oMDD3ONo2XKIpOoW6TlYVJtCo0e2sqvPxkaXQePvX%2BfKIQDwGg5aFtgxBVjPEBE7KjIZQgO6Ukfm8MPGYHAVvtJ5XGnKXFDq5mNP1656bKaM%2Bb%2F1lX7T%2FVQ%2FbXsSfAEO2AlbUXzpGBRIzrb9XHKg13oMNct4w%2FuAUECo3KtJOw%2FbTlTfy5mWVMM4GeTKEyi5%2FKPmwuvMTBAh9WGQZ0nVKdNVD%2BtI2maH8Fg7ncU9WFzSk7pC%2BPSpSn5SKMeaLycWIdjhf0zRGRW6seV2xRiiCS2iSzDuwpOhlr%2B9DLGq%2FrRbcYndti8Orye7bRNbp46RfdA8V47DO6K0JNduXRkqmznYGclhP2iYQRfyAV6RNn9ybnYUdKyPEsZWv9Pk6nkrAe0ndzlDRLMMTO98kGOqUBI4CMYwIefXCPwxbadt27LwF5nVUz9kx5EpHRpd0Dp4WzfOKsUfgczyv8hS2%2FGH4FwJZF1M%2FjnmAWpyjq7DQ%2BeaNcsKr8DM1nZk8nzdkAowDE1U02Cu5jgiV6dAf74QOHhzPCpx%2FL0XPsGLUECAXhv4WTu09nmm4r1fmeM3Y5Rp2KpiXFQehAJuDT2sQk8UJ2qQjxs5DTESACanIj8UF2de%2FYEqNG&X-Amz-Signature=e2f2dbee63b950a643cf63eeb1d4a87feef673d7d7193c05c7a575becf1e76b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
## Question 4
What happens if there is <u>no</u> **WHERE** statement in an **UPDATE** query?
❌ There is no restriction, so no entry in the chosen table will be overwritten.
✅ There is no restriction, so all entries in the chosen table will be overwritten.
❌ A syntax error will appear because updating entries in a table id done with the **INSERT** query.
❌ A syntax error will appear because an **UPDATE** query requires a **WHERE** statement.

<details>
<summary>Explanation</summary>

❌ **Incorrect**, because the second statement is correct.
✅ **Correct.** [Check this](https://stackoverflow.com/questions/12163047/update-query-without-where-clause).
❌ **Incorrect.** We use `INSERT` to add a new record to a data table
❌ **Incorrect**. It is** **not mandatory to define `WHERE` statement.
</details>
---
## Question 5
Given the following table students:
| **id** | **first_name** | **last_name** | **date_of_birth** |
| --- | --- | --- | --- |
| 51759 | Preston Omer | Haumesser | 1998-05-30 |
| 53532 | Julio Quinton | Shain | 1998-07-03 |
| 50399 | Van | Sokoloski | 1999-11-30 |
| 59587 | Lyman Richie Tracey | Elgin | 1998-05-31 |
| 53646 | Dale | Oviatt | 2001-11-11 |
Which query will return the entire tuple *Van Sokoloski*?
```sql
**SELECT** *
**FROM** students
**WHERE **id = **52819**
```

<details>
<summary>Explanation</summary>

Here we can simply select the student Van Sokoloski over its ID. So SQL looks into the column **id** and returns the row / tuple that contains **52819 **as value of that column.
</details>
---
📄 **[Quiz 8 ]** (subpage)
## Question 1
Given is a *pd.DataFrame* **df** with a fixed and default index, several rows and the four columns **a**, **b**, **c** and **d** in that exact oder. 
Which of the following statements will always return a *pd.Series* that contains the full column **a** of **df**?
✅ `df.a`
❌ `df.iloc[:, 'a']`
❌ `df.loc[:, ['a']]`
✅ `df.loc[0:, 'a']`
❌ `df.iloc['a']`
✅ `df.['a']`
❌ `df.iloc[:, ['a']]`
❌ `df.T.loc['Name']`
✅ `df.T.iloc[0]`
❌ `df.loc['a']`

<details>
<summary>Explanation</summary>

Let’ assume that DataFrame **df** looks like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ee0d79a9-f5d5-403e-94ef-83b6082ccc01/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTPIU3LX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCJtR%2BuuVE%2Bv6A9Q%2FySAIaNTaRlLPnOakVZHEa4Z3nhtgIhAK6T4RwrLDrAryWdXrs1UwP2Sbk6meg%2F4tKUYV5D%2BbCrKv8DCCcQABoMNjM3NDIzMTgzODA1IgwjD8DxkfURm9d%2FJrAq3AMMQO1oXwyMDTL2aqSuO04cgyOmhhrrIMhK9cgNLbhSyedqR9eYYrZdCcti647S16DR4tva%2FhyHP6qyiBQhWs4lC1%2FJZlhmbr1EGhmtyiyStXB4kL91xAqx4%2FldAdi%2FFDhMRLpRaP%2BX0U7iF3Gnt0jvvLDo2IV43Yr8CIM1V183p%2Fu%2FBjN%2FFAlwv5Bu3xNT5dwQ07kuldfMZG6hTP0HDI8lu5FJ5EYOFqerp65cnXBUnw50fRjOizgndIBQ0ketL5F%2F2kB2zY98ldrosMIKG2EXtrdKh%2FMhgd58ClemeKva3yKj9JLjWmVk46QiLa3HcLOXiP50DmsTViG9wHQ6OQKczRuwzpq2%2FnujY6IUaOmrjtgeH9lmixMrLdtcpAAJC0XwWclReo4Gpe8VdW2kI6bBfNppGxKkrAoXuXg5MqgzTk1f9bKvQiE%2F5klOEODRil0U8t78lAh5ua96jlvAndhQrlOAwjx5J8Speh16JkHaP7pW2SkK0iSAucJNFSePqFqu0%2FTS3m6UvYGea1dS86GQReuJKeaFpWjCOpOiuRjngklsI6R%2FoQmtU%2BcJt2GpjJGG7vIuqGX80d2iV1q%2Bs59QeE%2Fm1CaUdYyD%2FKMl3YDQSx0Qcn0U1XygQctPxjDAzvfJBjqkAWr3yg9vTn%2FyIq%2F9vGqkmHSsvcLhjErvAr7kB%2FzPFngX6im%2FuEWERh7hidu2UBXCvIvsr00UdbAo7gABCK5pZFxmePOwQmmvSQ%2Bq5zjZ86kGSUeZbffbAJ%2BO7R9DUzYp56exbv%2FnniHHdcFNh0so1arCjQnu9TAy8ZmIY6d9%2BNmsU2ozogy5iV3%2FTk8PYFFEnSIvydZh89ZaS3W%2BjdoQIoXUkxWJ&X-Amz-Signature=86aadc89eb35b2fc3de77cce43407686f40b812c9f009057e8b1864b5518c78e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Below you can find an overview of each statement’s return value.
✅ `df.a` → pd.Series
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b1f61fb3-eb02-46d0-a103-be82889c5473/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYGCY7SU%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDuZwZs8eJO7gk%2FxzHKlyGiewH%2BlyjAryGXa88DB5jZjwIgMsE8Bne0lvOv8TM8umhIKa79Z5qd3t1e8LNS7hCFIaYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLc192g34hEii0URVCrcA78QznXDsqeP%2F8p5WnP58mxNJPkZAeHoOkm9HNyfEr7hL8HzG1DIq7gvB%2FfhwnquT%2BaD%2F7yY2IrlI5agXRFZeBA0m8pOzO4kFVvpymOFluGhVDc%2FR3lRXgPsRUK1wwGY%2FqidUfX5mbX0vDV7MhZyOIl3rB%2FU8c3hHiibwYyi9yFENufpEb5bVdR3PaKNfoHCqy3F4jMElmrV5gDe2iaKCj1dBPpfNTSx%2BGjScpaWx2Q6cN%2FAxaS9OgpLk%2FSog7B%2BDZouwTxNO4%2FPCSdIn3I1mTcACNHmN5Kpavjei19Dd8FSQrykmu9lyD6cvO65jTwO5QW%2BOwbaTUky42%2Bk8%2Fz3PYkm%2B18cVZ5WgBmxTt9z7OQejtVORmqSdmF3F55q1oX%2BEBoYZrOetVLSctmYdNIF5vrLBYuod45eMscb2MBG3TZn5jit5ic0qL7ulW2NU2REPg3csLHdRu9GovR9h8HhUNJVizrYuc0FqnFnVwFAVLUljLZeQ016q8fo37ca2OY9ZlUCwD%2FS495TjejL4Puvh8PNT%2FQQXComB9003XW3yLruSIra%2Bs%2BCbl6t9fOFfGakShiaFhNMkL11BhIVXvDxmlhQ2jVRTnMU9vikPIioh5iut5KgPwbLSG2vahTkMPnN98kGOqUBS5St3Ha1eYRnABM2Jqhj%2B%2F4gsXCYEa6VJj3GCd84%2Ffc3PQGyWgAMNzEUUSRwiyXyrtq4vzgnvT2mhMPs7bAtlKMZHi9ijewP02vyZVJ8cIeoHpBmm1Yiwlyy63alG5FDskZ5ZbrNUQ18KUp8meklZmj2Sb4pknpqyZnMBsw0e1YsrD%2FbeKKv%2FPuMYE%2BUYe85P%2BslP%2BZOP7JVs8RmqLfPzqyUfbFu&X-Amz-Signature=260e97bd997ce8116b38ecbc8e59109755cc7e9934e48c12c2289a569e214690&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ `df.iloc[:, 'a']` → error message
ValueError, `.iloc[]` can only be used with index positions and not column labels
❌ `df.loc[:, ['a']]` → pd.DataFrame
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cf0d4d18-5a8b-4532-b215-6f0e381c8819/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSL74APY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIApCJyE3nuU9ZEIU%2F5fLiAciv%2BlC3rjZ9n6W77RR8e9zAiBG%2FBBFVV%2F8ap6wtInc2CkoWITxKPgsAzV7AIzj5gdsrir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM10FxGma9fFlH2VdeKtwDXXHFV3rbHmRq0GVJ2Y%2BNLNh%2FVQ%2FPjsp%2FBZfxDwXq%2F6wd6m3FKzXZkQAiN6%2FVorkhwP5qIntaWPbR7MOG5TkgfdYsBv%2F%2B6WNPwWjFz3Xr5oPa7ic0qwVL5AKHIUSiYrTsGQhNsNgpyNkhpsJ0E5k6%2FljUrEwzvSVqjTafbPc%2FRBPskssbpoIsU7omiwXwR7FIxouDcFRsfMDbZE1YVcVUlReygVRPESt1CP6gQN%2BA3m7ugz3UUBT1GD5v4TQCSBqluJxVBngf2hnrTI%2BAbLdSQmhhSxp1rzlFbnNQFqJOkr4e2sJedMM1T%2F6ky6spr%2B%2FcJ2KNlWdjXdzS7y8ib768rMm1aNeWAZvAkaTTEunHiU%2FuoydbcAfeaALrPE7yZV7U7jKp3w9sbrldPbIIsw7gzjxa2xYuaFpz1ezS8ctvOF5vlMC2rprFDMT8aNAqcxyV6c8nKnPWKtoZBtQdcXJC7QIR%2FgykIST2FHUy9vDgEXEBe17ouoXOJUyTBL%2B4UXNk%2F9pKxMcUsYmvWvkMJhEdaT7eu5lhCLLCKWsLjfu1sjzdVxRKbRje7OtFXK%2FwR6f%2FJPpdrNEvxJ1SOYasT9csPanbpt2xRrj1S03ylLrMOgW2gNec0cevlQpZB7owxs73yQY6pgFlRMvWlBydtsnpb9jU2jZMBwRFup6gFoevKH40NxyMr7xYwRS0GnWhMgzSaJjQMUvaSQFiSSl%2F%2FQ97iWxcZ8ChuDqK5SsdwPZf2j%2B%2F35%2BIYzwt5EudPG4JE78XuVsoQ9HEKBP6j3XrnvQqhAHhAcVBrBR77veSRibAAKMktI4OcPon9Jo3p0U6JYDCwot%2FwbNcqIMA9puPlq7qtrsUpONNStzJQ6g8&X-Amz-Signature=b7cc40b72ad919348e7fd825e2169d6e7fe2be99c3628af69ce7a18d2475ac0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
✅ `df.loc[0:, 'a']` → pd.Series
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2aefc3c8-f861-4e01-89c6-d60a50a40838/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RTDDZBO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDH681Jjg3yZRDE0a93vP5aJJvhJ6lCo0N9E0PHhRER5AiEAv84e6kkEre7BI8tvjeL%2FFeWmb4syJMMweYePbHYnfTAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDEjXrK402CL4d5PBYSrcA6TzuXtCSATv88dEwGQ1NKuUqtl4eb36jY9O7zi9d4dQ1IqK8BkPnim7csANRIv%2FtsM0uDFo1tjLUuKc1emuIQwT%2BKWf0%2BhF%2BVVcuF8fURAW5vGEQ9n%2FSTWVEkGUtKM7XzW4S72I23AZCj5xlg9otu2Ci4RIK1XawUpr%2BK5JAzJYqeDNknP8qhPaM80QzVsUjHfWYvFNP%2B129ibvKcsseya1rei%2BwW1xv%2FQ3K5GSl3bTzVlLLr1vUsFbK1Zt86oVVaQIO%2B566mKsKcDQow%2BbkLY8B0%2FwY3DQerOo5362goSuSxdCzBKji%2FNbag3cF0ZT0aGATLgeVYjs7O8JJO7mxTIDF0aaGmc1rAJfhJtxOQ1rh4CUD1SttWYwktWTcybdbvDk2PtJ9GiMeXrBBzowHR4vdRyFhzbMiOjtWo1sJkO8UvLuNoxlLH2vv%2BbLjhH5gcyX%2FzXZ5gFyozxHr2mo8Sxp15OY173n1KxzE779P%2FR867O5FPPJsrfrIM%2FhMVAnZK2o22tYsLBX6IJTPUKorz0mwl2TUxuzQ6wo2uu%2FwyCXXTYSsN3fNTtKOR79MoPhSsP1fcDRkDDw3MBNNePTLSr%2FqvTOr%2Bg40mNCug0FuCv0Vq%2FCh%2FuROPglETrrMIPO98kGOqUB80yh1KZy%2BmVUCD0Pzten9cwusf77lKKC2%2B8kO1TlHWs76FMsP5Ny9c2dB3QoTBbakzLjBMPVuCvwnAhi2ql1erckXfn17BkLvBGbnLT9lpXCgxiyrwB16XqbA4xBgc9P6ZyM9YP7llJpwRwhgfVBQiYcyZzyxN%2BINOvlDztRhG4BZTVUIc5Ob2W5W70sGhcube6UgFXQ9pM1Dm0VqKP4ZmJeHYH3&X-Amz-Signature=c02d1b13067263c1a42c0b9947e35978cf4852a7c2b48b69c9687290500f7968&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ `df.iloc['a']` → error message
TypeError, `.iloc[]` can only be used with index positions and not column labels 
✅ `df.['a']` → pd.Series
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a315c7b8-e11d-438b-aa95-6df4c0da5b50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LG7LVS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIARfq00%2Fcaa2611TOOpnemuHgv21Rj3gbQkUA9BubfygAiEAkDKsAjjVKsMy1ZCl1uEOSrXGXXzHGjfjT%2BIeG1bJwT0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMjQRkOy6vQVdo10GyrcA0WOTI8o9TsLJVCA9YKcON9xWOooyjxvTJeBbWoozc9jcN0Y%2BRPjAZ3%2FztSsLp%2BFfYyGrKM0EUX07uaDOkVfxQje18Dx524bmADre%2BX10K45UAGPcL5bFs0fA49C8%2FnEmPhndatebC6v710IYWF6JFa5Fvi3v8zLiy3WvyNSHpvERO72fpMrDmz0fpnmDb2V1MYl2Jh4JQc1zCHpgqtMBUXME8%2BMiUVopJS9uzbijVKEPL4CiUCPr5xKAen0WHiTK9MUDYKhVkU8eTTIUeHtFwdcUzC2xYkfhXrIEBfLJD%2FPr367bjtxdZyqlq3tDb%2Fge2MyUjIyJ0Xdn5eNUzRxEmqDBDU3oVCTG4K7AuXHJsqGvkDlXIv2XLubPUk7tnshuBggGpQNruMdC9XcUyajz66t7K509sKdmxReT%2Fj3UDXqMuvlfZifngGql3oLOJbJAJnt5u%2FTQKd6HljhfZ1tcHuicbngnAb8eNnPtwBDh3B1VoAy%2Bxug00cxwBjHIocAU9SaKwKbtJAIpGg7WgYCkuGwmTrTy9NgCWRnUgGOi4w2oZR4JvlhsG%2BkdklyCApqxADpLephPn7JTQ6PGJs6zAMd1DyyDzKQ0zKYur23d6%2FNn7UoVYFE5vJkP6nMMOHN98kGOqUB%2FkxmLf1jL0vCWd0LvQGj%2BiHPdGsYmT%2BHwRfm3yJ0uc7iEmudRmxKTnZfW%2BB8bP6PEOXUslcjmirN84JVFUXqorIs93pYedm9R25%2FQC8gupcSYuEsOkcb%2FXYgh8hhcq4vGPYr6eqY6NrdS7Z7WgnjHXQ2fZJuYbROW56vBqh7OJbfYSHfy8%2B2JVQEotvc%2BtkWm8yDtRHlOB%2FSnnNXa4s3RzeVfxIx&X-Amz-Signature=9dc961e818153cb1b3927d93052c499bedbc38647b67b32556edf464928a7ef5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ `df.iloc[:, ['a']]` → error message
IndexError, `.iloc[]` can only be used with index positions and not column labels
❌ `df.T.loc['Name']` → error message
KeyError, there is no column called **‘Name’** in the DaaFrame
✅ `df.T.iloc[0]` → pd.Series
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a315c7b8-e11d-438b-aa95-6df4c0da5b50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW6RFBLX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCx0ailllrEgLhCd4DluzD%2B122M%2FwOLZcDXMYEqEAufwQIhANCtv%2BxncEkK%2BRBXdu%2FyklFgbRFbelp0Tj8VGQU6fn8wKv8DCCcQABoMNjM3NDIzMTgzODA1IgynvQTLvn4FWjnFrWMq3AMoNY0NdMJ70dU0Aaq%2BbaRPsYnveiqQpY9Dcr4W%2BUggIW3te4sjbFydFbGiiTloa9NfvHUvUXbac5pgdk0RMKESmFAx2n5zK72kMbuVhWs55vyX9hlX6UuccM6Kk48NhppFZqQMRpIocWypN%2BsADl5W2BP93LVu0vqoDuqHt67mKipa6zu9iRnXrYdA0sAwSsJz845oSDMdgO96ZY19VTwR7GDgaVqySLEZkxJT7XkMRbpKJP09O%2FLpbd2kfMASzqTa7y4m%2BgBegOKGsE12Bw4JoByIMBRVkyBQrX5a7vqUMzq0GHiJXs71XtLZLewY53ca5XoJ%2Bhnla52jrYiUByjlZDSnhjqusGeE4YTnCTNizCOi6z8ejL51341Z83zsBvDJiucO5P2f7iE%2B%2BeMCKmLyfAFqUJmcP3oKeFIA1kMlryyu5c9BxD4HWfbfa%2F6u2MjdYWBmGnq6jOW4TkCjttYGNFl8j5h8SOQiVWq9kBVpOMihuU1%2F8As6BFLHWIsLLyIibi2FSy9mMVVzn7BTeq59Pgjhw%2B0bk93wJ62Q%2B1WsucQAkU9qq0fk7Ldsj1aLnh%2FBfOHyB6%2BNavs%2BCDAGsjjxIsBh8K4Y%2FKGBmNC7KQHYmU6kDWGosU6UEy2gHjD8zffJBjqkAb2%2FYwu559L54S9%2FUclmQdndH87hD3M4uBO9rMt%2BP9KeB2o0Gwdgv%2Fe5fMllI5E4Cz6gyQo5xk%2B4%2BcKQFx4AYrsUUMzYVU3NPmVQKQMaMLGjBeJp%2F4BPr6T9e6wKxe7FrBhlw4mOkj4vp72kbPRVLIsFrKaA5m%2FW0qoPWcqxUtA5Knr2k84cLrqbCWGhk9X8KgxBvy8drFfTOgBF%2BsKAMsEi0JvE&X-Amz-Signature=3f1bf7794ef0831b9a58b4b7a4d42c3951188c1887f2c4761f308d9c69a7b42e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ `df.loc['a']` → error message
KeyError, there is no row in the DataFrame with value **‘a’** as index label
</details>
---
## Question 2
Given is the following code snippet from Assignment 8. 
The function should compute the ratio of gross/budget for each movie and return a DataFrame with that information. Why is it not working as intended?
```python
def gross_per_budget():
	df = DF.copy()
	df = df[['director_name', 'movie_title', 'gross', 'budget', 'duration']]
	df['gross/budget'] = df['gross'] / df['budget']
	df = df.sort_values(by='movie_title', ascending=False)
	return df
```

❌ The original DF is modified in the current code. Line 2 needs to be changed to
```python
df = DF
```
✅ The resulting DataFrame also contains the column `duration` which is not included in the above mentioned criteria and therefore should be removed in line 3.
✅ In line 5, the dataframe needs to be sorted by the column “gross/budget”
```python
df = df.sort_values(by='gross/budget', ascending=False)
```
❌ After line 3, empty values (NaN) need to be removed like this:
```python
df = df.dropna(axis="columns")
```
❌ There is nothing wrong with this code. It works perfectly!
✅ After line 3, empty values (NaN) need to be removed like this:
```python
df = df.dropna(axis="index")
```

<details>
<summary>Explanation</summary>

❌ **Incorrect**, because the original DataFrame `DF` is not modified, rather a copy of it is created by suing the `.copy()` method. This new DataFrame is then saved in variable `df`.
✅ **Correct**, the criteria mentions that only the columns `direct_name`, `movie_title`, `gross`, `budget` and `gross/budget` should be included.
✅ **Correct**, the criteria mentions that it should be sorted based on column `gross/budget` and in descending order, this is why the parameter `ascending=` must be set to `False`.
❌ **Incorrect**, this code would drop remove any column from the DataFrame that contains at least one NaN value.
`axis='columns'` → drops columns that have at least one NaN value
`axis='index'` → drops rows that have at least one NaN value
Let’s assume there is one movie with no director name. Then the column `direct_name` would be deleted entirely and we loose this information for all the movies.
❌ **Incorrect**.
✅ **Correct**, we want to remove any rows that have some missing values. Which we can achieve through `axis='index'`.
</details>
---
## Question 3
Given is the DataFrame DF from Assignment 8. 
Which of the following code snippets returns a list of genres for the movie at the given integer position ***position***?
Remember that the ***genres*** for a movie are saved in the column genres, and are in a format like in the following example: “Action|Adventure|Fantasy”.
✅ **Code 1**
```python
def get_genres(position):
	genres = DF.iloc[position]['genres']
	if pd.isna(genres):
		return []
	else:
		return genres.split("|")
```
**❌ Code 2**
```python
def get_genres(position):
	genres = DF.iloc[position]
	if pd.isna(genres):
		return []
	else:
		return genres.split(" | ")
```
**❌ Code 3**
```python
def get_genres(position):
	genres = DF[position]['genres']
	if pd.isna(genres):
		return []
	else:
		return genres.split("|")
```
**❌ Code 4**
```python
def get_genres(position):
	genres = DF.iloc[position]['genres']
	if pd.isna(genres):
		return []
	else:
		return genres
```

<details>
<summary>Explanation</summary>

✅ **Correct**. With `.iloc[]` we select the movie at the index position ***position***. By chaining the selector with `DF.iloc[position]['genres']` we select the value inside column `genres`. This value is a string. Thus we must split the string by delimiter `|` which returns a list containing all genres, or an empty list if the movie does not have any genres.
❌ **Incorrect**. Here we only select the entire row of the movie at position ***position***, but not the column `genre` only. Thus, the `genres` variable does not exist and Python will throw an error when trying to access it.
❌ **Incorrect**. Here we don’t use `.iloc[]` to select a the specific movie. Therefore, Python will try to select the column with label ***position***. This results in an error as no column with a numerical label exists in the DataFrame.
❌ **Incorrect**. We don’t split the value in `genres`. Remember that the genres are saved as strings in the DataFrame and delimited by a straight bar `|`. Thus, if we don’t split this string, the function will not return a list.
</details>
---
## Question 4
Given is a pd.DataFrame as **df**.
Which datatype(s) can end up in variable **x** after the following statement:
**x = df.iloc[42]**
Assume, that the queried entry exists, meaning that **x** is not empty. 
❌ **x** can be of datatype *pd.Series* and *pd.DataFrame*. 
✅ **x** will have exclusively the datatype *pd.Series*.
❌ None of the other options. 
❌ **x** will have exclusively the datatype pd.DataFrame.

<details>
<summary>Explanation</summary>

`df.iloc[42]` selects the row in the DataFrame which has index position 42. Thus it will select the 43th row in the DataFrame.
Whenever a **single** row or column is returned by a selector, then the return value is a **Series**.
Whenever **multiple** rows or columns are returned by a selector, then the return value is a **DataFrame**. 
</details>
---
## Question 5
It cannot be that for a *pd.DataFrame* **df**, the result **df.loc[x]** and **df.iloc[x]** are equal even if the value of **x** is the same in both cases.
❌ True
✅ False

<details>
<summary>Explanation</summary>

The result can be equal. To do so the index position must be the same as the index label. Let’s assume the following DataFrame `df`:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/77f0afdf-245b-4050-ba01-3fb30b8f7e8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UV7AMQX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCR2Kgb10r55KZeKIE0dXIn0ZM9A90k0K347Dc2zqA7bQIhAOgV8mmzfOnHh3D3ICLyaswBhMbVgDMK43BYnsssBaFSKv8DCCcQABoMNjM3NDIzMTgzODA1Igwe2rndaMcpussl1nYq3ANmtAljUjN17jlkk7ptmXL%2FvdygA6%2BeyLDxbN01jSXQUGnZLarJeOme0oL%2Bt3x90RqWFwKPdvEIcFGbmQ%2FFkbJv68yAx36ZflVUFw5Oy4uQ%2Bjyi%2FDbpriUGECf8pMQKjqUtSdTGlaiFfosVfXVOv5PWRptI%2BbBGJAPnLgyd%2F29zs47KVp9XWab2TsNbZEP7Ue%2BxPoqWm%2FsMYB8ScghYHvnAe%2BVuw1EeBvJYFEyFBCRF3uISDTmg1ym5GyM1s1HocxISYv5nwyhI1r5fRGa6KKynT%2F1sfaCG77PgGCeF8G2q4uDFrM7Z3sEDI9RNzMsXqrBz93P2zCyBI9v9rFRmw8IztOJCfEXHP8Su587x8ra1RdHdkB5NGFDsBBOSIMXYS7PYPAhg6sQZ3Xt4CKFKnEh7H9WrxpdFEjpdc2BPBcXLaFRr9KoFJKHnmVdAeGgl5KzD3iFNMa0HIYf3u1XY03Osu%2FDBBm5aIjRsA3RYvCRKoTKNUXDP0UVwzZ%2B25vEMfDyfQciJ8FIdiXUTO0My1RYZQ%2Fh6SldSVZnlLPR8Z9R%2BfQyft%2BlbE6%2BPoa45NJKlJLR5jKfM2gibw%2B7ePDaQ5BXNJYE7qnNlUsbxUq43YJAt%2Fh7WkCR%2BrYEdqZ8doTDlzffJBjqkASVEDpRb3SlMI6kaXRtOaJ3KbWJWkZS8XpSOurlSX5XE3GR8m4wPJQ%2BoJSFtRq4R9GlbjgEz0Be4VznxNZAxgVQSQ%2F8OhAjnU458NComrxHjPYPvi9MAuq4Zv14P8w2vQpvM%2Bp7Hbcqkdsyge%2Fe7ZHTtqYi5RlymSX1KSQqPc99m%2F%2F81p%2FWbTygmGOIwgV1RBw5%2B7h3fjbC2oOlrXgrm%2FYJIb0DW&X-Amz-Signature=f1ae70f2b2817cadd8f10158b5c21b3fea6f3f7ccb16eae9919c601b5ac18083&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that in the index column we have stored integer numbers from 0 to 4. The first row has the label 0, the second row the label 1 etc.
If we want to access now a specific row, e.g., the first one, then we can either use `.loc[0]` or `.iloc[0]`. The result will be the same. 
```python
df.loc[0]

a     1
b     5
c     6
d    10
Name: 0, dtype: int64

df.iloc[0]

a     1
b     5
c     6
d    10
Name: 0, dtype: int64
```
And of course, we can store the number 0 in a variable `x` and provide `x` as parameter to the two selectors:
```python
x = 0

df.loc[x]

a     1
b     5
c     6
d    10
Name: 0, dtype: int64

df.iloc[x]

a     1
b     5
c     6
d    10
Name: 0, dtype: int64
```
</details>
---
## Question 6
We have the following *pd.DataFrame* **df**. The column **index** is defined as the index of **df**.
| index | value1 | value2 |
| --- | --- | --- |
| 2 | aa | z |
| 22 | b | y |
| 10 | c | x |
| 24 | d | w |
| 30 | e | v |
| 7 | f | u |
| 13 | g | t |
| 15 | h | s |
| 33 | i | r |
Which index does the command return: `df.iloc[6]`

<details>
<summary>Explanation</summary>

`df.iloc[6]` returns the row at position 6 in the DataFrame. 
The first row has position 0. Thus, the seventh row has position 6. 
The following row is at position 6:
| index | value1 | value2 |
| --- | --- | --- |
| 2 | a | z |
| 22 | b | y |
| 10 | c | x |
| 24 | d | w |
| 30 | e | v |
| 7 | f | u |
| **13** | **g** | **t** |
| 15 | h | s |
| 33 | i | r |
This row has the integer value **13** as index label.
</details>
---
## Question 7
Given is the following *pd.Series* as variable **s**:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e86f9897-778d-4350-9e4c-1f744594578d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW73GWVX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDPcH%2FJhC4VPO6Z4QXDwLIod%2FWfTwyawKPOnbeawcbB3AiEAiOrKogFrobvA6gEqHlC91gTpVz%2BN2lrI5vt1S6k7K8Iq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDAOcyvSfqgDjhSqkOCrcAxmcUcL6pKAWWIkk6TOARvi4MdjfZ9XyzLh1eiMbd2eTOz6%2BGUFrBQkBoedFrN1UidUGxqtiFJc02BLcPkO%2Fn8%2B%2BNOQV7j8yhbhtofEqOZ2WGJYvR42JfZ06KUEXBhBtOH1Hn63ZzGmQpd0goBP6AcqJL02%2FJusSc%2B7tB16OD3ukRdNjktk%2BwoBpnmPMBRXlKfOb2cWppykUU5HclEVryyNSZJ0wPWZM2ZXeK3foKWlrUzdTVSptIK%2BOvMsvC1Nb6e%2BLJ1rj8ZJ7l433AdAXITbKr%2FrcIECFoIrlF%2Btcq9hUKen0ftagNtBKttHkznHyoAuOb8owNnh7t%2Br5efvHeGfc%2BynObfWBPeMfFN1zcpwVELnnVigtL%2BV7jW0UcPzxmm%2FiIXM9q%2FFDWx5%2FA9TXvfNRtgKnW1fDV4GvGV22DGapwr17eGlQoVpOKLfnrZcBRC6v2Y3z1Rfe%2Bnul3emt46M05Q7q1mz1f3TqmsJyZR6vkXECz83dbTRW6rQFA2pTUdvTgMsJbkjuqveFqxld2HGafct6KGJFIzH9qTn6uGAI5Ap4epYB68pEYUr7rd9E%2BQObOehfzb%2FZqRPnB3S1wtMnolRmK32sT8Ea851KNkpaTLD8mE%2FO6GOkUANbMOnN98kGOqUBTN1hDg2kXR%2FZR7M11nv21MzYMdXTur8Bwtdid898zYzjuE4yGaTkaLBddR0XbD9beZ3pJXcNQD6Av1qzVw3QndlgXw8qJlvKKLBgk4qMdxU%2B1UkywUu06Pj87DePFT2pWXqCZHIy3ppzfcDbewsoSVHTKe444nIws513uqQkgXzy686opMxQTaMR5vAo8zahZi1jaxre5dmpSI6amRVmABrBJVxa&X-Amz-Signature=e85bffe4b72bf42d9eea209aeeb4ce0d62f5480166264c58733bab313d8831e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
What is the result of the statement
**s.mean()**
6.6

<details>
<summary>Explanation</summary>

The `.mean()` function ignores empty values (NaN). Thus, Python does the following calculation:
7.0 + 6.0 + 5.0 + 6.0 + 9.0 = 33
33 / 5 = <u>**6.6**</u>
</details>
---
## Question 8
Given is a *pd.DataFrame* **df** with 100 rows and a continuous index starting from 0 to 99.
What happens if we add a new row with an index that already exists? 
✅ The new row is added, non-unique indices are no problem. 
❌ Similar to SQL/Databased, the index is a *primary key*, so the new row can’t be added and it will fail with an error. 
❌ Adding to the end will result in an automatic matching index: Here, the added row will have the index 100. 
❌ Pandas recognizes that you add the same index twice and will automatically create a *MultiIndex*, hence use the next column additionally as an index.

<details>
<summary>Explanation</summary>

Here, you just have to remember that Pandas allows us to insert rows that have the same index value. 😄 
In SQL, this is <u>**not**</u> possible. I.e., each index value must be unique.
</details>
---

📄 **[Quiz 9]** (subpage)
## Question 1
You have the two *pd.DataFrame* objects **persons** and **addresses** with the following columns:
```python
print(addresses.columns)
>>> ["zip", "city", "street", "number"]

print(persons.columns)
>>> ["name", "address_id"]
```
The indices of both DataFrames are continuous non-duplicate integers starting from 0. The column **address_id** in **persons** is supposed to be *foreign key* for the **index** of the **addresses** DataFrame.
There are some persons that do not have an address, so the value of the **address_id** for these entries will be *np.nan/NaN/pd.NA*. 
Additionally, an entry in the addresses DataFrame could be referred to by none, one, or multiple persons.
Which of the following statements returns a *pd.DataFrame* with <u>all</u> columns of both DataFrames **persons** and **addresses** with the following restriction:
The resulting DataFrame must contain all entires form the DataFrames persons and addresses.
❌ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`
❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`
✅ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`

<details>
<summary>Explanation</summary>

Lets’s visualise the two data tables first and plug in some example data:
**Persons **(left data table)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7496c730-cb41-4f7f-af50-44c35591eec8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626E2BDIR%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBItfjvJSr6pfze38FIveSkYOCbTqPo5imlsIzDoat6bAiEAxAWLNBTgi%2BJ1Q9u3Ig60fW6BKGOkBYjSBr6BGjOlvEIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDB%2BhzPbxmtXP22KTTircA4PEKhyOKCO%2FWRvFUHal59m28YAEI4yobWsEgwlSMq2YZIDDI52UNP%2BXLjGOr%2Buy42MRvFf0ViilR0l9pfPkZz7vVID6BD%2BJFMFYud9M%2BMgI1eLMzqVNgmCashBAj%2BnzsjPtjlBJ%2FMmPIt6zIH93kKPD%2BxUvc%2BPOhPykMvBSoCMf9v349ht%2FTNDSeVrgOmSuxg2OyXHQHMCf1qJdcCKEbvBtL3E8iVzuxOb5u7S9wzpkm5Y%2Bi7yzy7p9sZDPd6Mv6Fmb%2B%2FK%2B4NshZ8iBF2oRqLsZoSez9tAOEoX7fyvlpHSKCckPPqJhddHbPy6Af5i18SPIJlasDW6ver0HTJ5%2F09JmQeQ5hin%2FD9kuqX2K1CWrvLbqhHlsAKuC47SMSoABcmwo8iL81jKEFG8Xb8lx49lh4mDGn2jjcu%2BLO4rIqjgEIEpiAqyymOeGFvgZs6w2rqWda20OkUHLX8iUhY%2BwxmjwQOFy%2BIwid6YrpRzfi9VMARB0n7oowwwVhCuFoqRqkPoVpO5V22IFy19xLpdYEwdnG87001NflGr%2FMQpVkSYeizLpSZWzDByT4GPx23VBuC2WF97bbGjM4kV1LmzV%2BiO%2FvdA1dwhYk2qTKQj5L%2FDaW5%2FiQ%2FXbzwUIoNq9MOLN98kGOqUB6iI7JLSo4sh3vi7JnQ%2B7ZQJIzjiK%2Fm1FrPIQCnaYDcPZyM%2Fr16ZTfvOHshfgrAV%2FW9nX7IndvpPZukhpYZDE35VymMZdoSLY3nFcATMRRhQ9P91THsvy%2FARdjoQcoqx8mY2XphJUL5qnchjjbJ2iHKyrXqOQmDNqjbpRRTgRbX9AdMfWWMagmV4B%2FWFH7pV9rKyICzTObLuUti6OJb5RzoxDbuSw&X-Amz-Signature=6141d2ff438e2f324cdde78d915ead0df2cfe44fd942f69810ae43936b3a5fbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**Addresses **(right data table)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/096ac0e8-1fd5-4af6-bd55-5f2706b0e926/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLYLYHQ7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDKryZxFiXy4DzNlnsq0XFIoXULyNS%2B2Mgy1AVicJN7jQIhANgoV2xXY1lY4%2B3b5k5zoateZAxu95tzsOLzUOj7hDfeKv8DCCgQABoMNjM3NDIzMTgzODA1Igw%2FQrqrWKDxXhmGpQAq3ANwTtfLJoyQq1Zk368XeFFpNgk%2BdCLdwJyBYtGgwaJlfKpYlZ%2BO5Aykmq0ZVxhRyZeIbyMpgjauZ2QFv0LlOk9E16MsoXY7ocKDi5e%2F1kYlJQeYTGO2xCDNvWM7qxxiVpHls1dNPJDHbtnDKPqGDH1ZpHlYVHQLxwpn6fvIzrgNnuv%2B3HBahb4xZmaRS5t%2BSBK6vaNxxz9g4RHnO6h6J2H9yPtn2lGC3A5uzppQmJwPOzUPPvtgLgt5Bomw43vFw9XlGmM0k%2BXrgG9xyr8JA53XQaZtXixI90tlRpf2wBDCMuRjvV8UUkWiz0UkqWGKRx30O78Mc4MC4Lyauhw%2BCa2PsdCdEgLs6ANbZk8s5kNl01tr4ibsQW1jlArZxGF0nuL3yTYi0fw7JqYvg7ZBvsSBWOVd%2FAVJdBiAMwkLM%2F4aeTs7SY84V%2BU7KBExSEIqFVT8EQWnMg10SDR1jDY5nvIfk7agX9VshWSP0Pw2uimjcj2Ik7RWSwaM3fbS4s4m28315vX9hrMc9VXnKW0u91xeo%2F2Ls6UAK26X79UZabf2wxftLRmhhJzftAFyv%2BGmGhNAWZ0n2XtINi90WO0U6ki1F%2BHwallMGYTu%2BG1SFadprFZMk3q8KJotl%2FSBITCOzvfJBjqkAT6aUwQggFocCl0zm2mxkq6xWLM38KdeCOBVMtgx1jHyeAQDxM7IbLSdL42VHN3Okd8%2BaOpjEgfuufqaRgL9rxDTEEJPuwG40J891nEhYjEYobKH92vorCk6%2B5JVk7e0heWizIk3cVc008p945WPSCZNBUxmcPPg%2FpcRbA%2BoYemLcx6VjWtWFRyPIp4dRxhzZaSHGwTYU7eEtmlD3dIYBbU3GwO2&X-Amz-Signature=b8ca32db46f12d1509f0570efcfdec56b781b66cfcebac9f7047f372a29a8f4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

By following the foreign key `address_id` in the **Persons** table, we see that Marco and Melanie both live in the same building.
We also see that Friedrich doesn’t have an address and that the third entry in the **Adressess** table is not used by any person.
Now we want to merge the two DataFrames together, without losing any data. This means that the output table should contain all three addresses and all four persons. 
We must define the following parameters to perform this merge:
| Parameter | Value | Explanation |
| --- | --- | --- |
| `how` | `outer` | We want to keep all records from both tables, regardless if an address is used by a person or a person is assigned to an address. |
| `left_on` | `addresses_id` | This column contains the matching value in the left data table. I.e., here we tell Python which person belongs to which address. |
| `right_index` | `True` | The values in `address_id` can be found in the index column in the **Addresses** table. So whenever there is a matching value between `address_id` and the index column in **Addresses**, Python should connect the records. |
This corresponds to the sixth statement in the answer options.
If you are still unsure, check the output per statement below to understand in detail what is happening.
<details>
<summary>❌ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/91295b4a-a196-48b3-a33e-68bbace9fc32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGD3AUXE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDNGd7TpJdyYweAAagFjmJU%2FtKPDW67mK80dKhRCB478gIgBdElUq17mnzc4ppM366nFoOh2%2BcwkC1wQuZUP6BGubsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOPoDyV8iygmj%2Fp9CSrcA6EIBbzP4TftdJAwsCq2tCreHd%2B1S7ZUBrsZqxFPVVYLs%2BpBiViQjXoOozxHFWzxIVhSE4hBocsZ0J0YLU0eUe6wpGVftZyThBi9Wn%2BpKGVwOQ8J%2F3UvmJcajTqoUsjsRed5NDNaUXBb70d9m0sJkI3sjmYm4X%2FU9eBPIrqMedIxAM6QB%2Foo%2FNyVl4j1iytkrlcr%2FVSAx6NZxegRx4Tzpj70gy5TOefQWozwpjouH4cAOJe69adj4sl6Vr0CkL3vvuO%2BtlSQG4%2BG5%2BtcScIxp%2F28%2B3MC4Dv2mZvOs34ZICBpHFKNiEawgH2z9VgXEIptqocUVhtPYsVmcbIzlrTAVGXYMtNjHnOspiguYAftl7tSY0JVMCG7whnmI0XCRqhuF249BcfD%2BCEUq%2FhB5TEAlJs69JMzEVtmq6fmQal9IG10ytTsupE%2BZVjsM4XxCmpFyv4QVtqkNVQN1o61qedtbS3VfXSf4a02nYF69kXDx3Kwgg%2F7nMq3lxrr6VlAA6gnoRDviAi6wYHtIS3QogfBj6UdBjvBvBIWAhkqPC8p87KAJiz7Qbub3Iw7zAF3vasqulZqbnH9JMQD9KwT1GmggXMQvSjHvtPoasbW5ZPQSY1oXYjsRAnTZ%2BwcgAdRMPzN98kGOqUBjn9UoJM%2FOU%2FMqJ%2F5nHiwCYvamGxSBtEf7qU2z%2FZDBUO5fsFkIoyZiCEUsuO3rQuiHBKumi4jfoUN9QTWqyCeiwjYjgq5kyW%2BNGVLqeMFCBNPelX%2F%2B1ilH8TyRCef%2FWT4KeUJ7G0cg7bNX%2FQ84pfBHrWBqghpbcOOqvpaKC4Jow3kspXl%2F8O3XR6bsy4KR26jECNUi%2FFzyzw18grEozh6oP4V3LDd&X-Amz-Signature=c3f7667779a019901b08da9af95d5c3ba8eb064a63237fc5bb402d7d58504142&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ where values are missing, NaN is inserted
→ only persons that are assigned to an address are included
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ead1aaf6-c414-42fa-bb00-b88bb8c18882/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZWUS5PR%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDdcFItJTrjZmjonoGyDeY6HjF6VqhtCa%2FZBceYm5GiewIgAMe5srVQYEzONmivcRC9z1rAzTasM4o4SPkP3Nh%2Bx1gq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOcaqnAzb2wWJJAw7yrcA2yfWvCddUUyKGjICsQG5akwKvNIMIlT5WGUOFYpMZEm%2F713FgxkATur%2FlZRPuSiXUzynfLJBg5C71wqsSOsbwVtbZffumg5C6u3d7SRofHIJmGTy16GVeA4%2BXq9pugUc5Cwl7U9T8Qu17%2FfybyPEpTo5DN2fU7%2FxqtLA1tQsS5uanO%2FEB0vuLur9%2BXpqnSP1cX2gHwH5UEG7Pgw9%2Fc5P8Uh%2B2Cxg%2FsNN37V705tK16QFvK1TEh7UE%2Bhd0WG7MJ7ZOcU4uOLHEqY4zxNSReHVL3igY5cZOlnQ1exw1590MFaNkySrtpurF0ng9fEHe4RwcX6MqulqdyfKQb055ONcKAhPlWRlJMBZXO26kYjd1aheJNIvJ7WJoRwLD8nBWfIPhA64SFo1SL3g9Ir%2BkgATSXcYKCj9VkeLXrxtmTa5ScP%2B8Ugk5la%2FNglOOSVB9Hs3QvDVztVQkTz%2FHBP0D9DbUigxcC0%2ByAoqn0RQ14fCpLj7AM58N9dmTbPrcXw2o6Qp%2BLiBUhFzmgmIv%2B2pwBPgviNgu5MtLf8dDUYXbNXTqmV0XbANrerTJyKTB5YZxSfckxhairRxCHIbxD3EGp5TELjo8sI2B%2Bg674K4kIT%2BBIKiu4%2B9I4zPGwllCKdMMXO98kGOqUBxbOPGyczJi%2FGjK0kRWSzrH5JomOSa11wBGRWBMr%2FTILhydYiGzO60QdZ4hnyLU%2FW8IuTkBx3rzUZ47njKVbrCQRz5J%2B9N5VD3zx5YU7%2FTgZaV40T6mXozJoxYUaj052TwjoOVXOHZo4OxJQ6UwiHp1rZdIqMj6lBY%2Fsm2m7jKlV3kz27xo8wHj3xpRb9Dbv7%2BkuomGn4ZkOqUUmpBtfjsgLDaqGw&X-Amz-Signature=47fa21e80315f017f9c1171f9109b86a5cc2f93db1a16bce3a4e250eac712610&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ only persons that are assigned to an address are included
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/87be0349-c455-4f07-ad7c-9be7413cb92f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEYNPRNP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC4%2FHAvphJ0jN2vWHXUarjKowjv8iEEn73RugbUkVHWJQIhANa5wTTXSl8rXIwqz2ZJW1e6eXgvgDj1IydOS1Oz1DCoKv8DCCcQABoMNjM3NDIzMTgzODA1Igz7L6J4FNdJ%2F%2FDbyJ8q3AMCtomGukCOySr2EJDEs4I1ClKGSTjghG6dnTmJTQYLudwUdBXiZt7l3ZrXqhIibYUsE4HSyXmuX9ZvOsO8jrjZ1NOJunNaHtrcfwxs8gj%2BJkY%2FpODOBAJ%2B5oETmI09HnyOZMAMxOuuSMznUy%2BOa1%2FoiuMN8nDj6OWiWrzZC0SZlqadyXP7Icx%2FvqVe3zIIC7jMHZGqWgflDLW7hfKQZPDS3FqtZ%2BOqcQ%2Byir71R%2B%2BUvHztxzfWPH7wRRk4KCdReks%2BrKCLjieilzgy9yzE2%2FDyHdOfCQBKVlevdcY50Lvgc8qpXCQb%2BBhtttb8yIfaN3b6ZNxtCtqyLT6lQ2SASHbL6XiX46o4Hrgk83pJY9mUkMwW%2BjyjA3MWphS0MUTB75RMNNKuyqmeMGWbDY%2FpTIpLJohz82HcsyF7oU8S8BEDOWdrDdwGYk%2FWq%2FZuBb60TR6l7h%2FvHtopIswb5OfeeBWt9JrmIuXXDeCs8TPoeEo%2F3gtpi1wyw1%2B6CPFoYIuBxuy9v9%2FJUN5xgQosB0m6we95S0EfbwKTI4YXzAZNaB2OhBLYSuirmOKLds%2Bheu4rzvVlLQ5jE%2FWu5nj8TuP9NSc8o3WIbKf2Aj770CA2CKjbYn7DaluL%2B9NuCCf5yjCxzvfJBjqkARz0yeL1fX56tMxvuNSYsftWr1qkHtdMW8fiVFSil%2FE%2Bvv3Xr1qvzTXEltlG2LrcnY6fyNGsZPlLxZQ8OJU3%2FUYSu9zYT9B5EloQOLf%2FlrULOlEt7ITGN4uo01LVq7mwv%2Fj2MLnVUp6mSi%2FkSFO0fmH27JBRKETZtgf%2BCBES8YLMw0rJUxEZ2D5y%2BRosu3F0E6HxAk0M1QiNashAbSxqogys8j4S&X-Amz-Signature=0c1c9d52df94c176ae0b62e89bb342415bb04b235f746d63cde1ae39e0455479&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`</summary>

**KeyError: **'address_id'
→ There is no column `address_id` in the **addresses** table
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9f0a6977-7c62-42fc-bc16-72859d19254a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QHMAU66%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCQ2a%2F9COQsUu33d8O3Kv5OUiGL4cYea1JrFyW3ktZIMQIgfdr24ByhjnWiPEZraxLOHI%2Be9%2BRBPye9sETHFH8pdaEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLImifOvRDPEXstT1ircAzWK%2BfkW4y%2B4x4qvBJwdKkBegLlvEvmUsnO21Ks%2FRXw9%2FroE2NcajcxRIzs4FZ%2FCptSafDr%2B1y7DuS3LlLS5dz3tdn%2FZf6VryM3U3OglI8x6DRJp5OdfOikzFHGBd%2B5zeKR9WdenRC0sLJSlpc%2BCWuR7mldq0Ye2P8rTe6%2FJmMz4jq5%2FeJm7t%2F4CZT2KvRTtQ3I8MsM738y%2F29ocmyEMD7sv3rk%2FGmUeUE7Ltn%2BO3ljyT9rye81vLOH8UZqvheJ8z5dOg2LzrE%2BegJZckFLGsZwke5eh4IpuQbQ06u3ys9IFu7LE5aLIv%2F6XqJBrfG5oyJP2Kx1GOqtLn61zDQijxxhQbkSSRBHR4olNuh4xqdLC59HtK%2BK25atD%2BvP2wTZVWOOK0yRe%2F48NNMAvAyMHT%2FKB866V65wiabdG8JbOLRcQgo9xRLnGGqs%2FOZgy%2Bh%2FvpUT7HmBJpRQICtvftB07Xd9YWd5lhOifRhKhQAHOWfZAjWvfsixRRPa6Z8fWILbidsPXXsZQ5aGMB2m%2FRviituF6LYq3qZUthnqpeEM9f7Nhm6zlINCFuQ2nMBnFWnllcCxyHwcyWZoKDA%2FK44OrJq4sBvMEtINp3lEBdkfHKCIBkRJAaeBcjzMJyXdsMNbO98kGOqUBXUljx8CklsYtr%2FWHOvP0Tf2DT88r%2FW2DyLX9n9h0m6VWxQqzA5%2F%2Bi4P%2FCebjnCPIVGZ9owrfeU7LHx15T4yW%2BUphahgpE91I8Tcr2efITYuO9K%2BfNjPw%2FW5FJo0j3x0J2Tr3lmedlVmGF9cvo5L8tSPjiUV%2FZUL7%2BFj3v1RgcOrgvnQiNe7Zfj06Rtps6jz%2Fy7DQf%2BAJ5RubA6jBrPyPdaI7SRpJ&X-Amz-Signature=6ef668a58e316a2dcacd4e62acf3b54c66ee0cf50564884e020c485857f34b98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>✅ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bd8f2a5a-01bb-48bf-9f2b-40d2d8b90f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZDVIV6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCnAMtgc%2F6nvwXQXJee%2F9xJXLXCXz2TIZ1LcbeFUEI3kwIgAP0whHl%2FphxxvUoCE8HYHw86pnudMgs5nK94%2F68y8eMq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHGhNAO39Jc0hEKT9yrcA1%2BTF0j6TO9%2FzXBjBLqY%2Bpt%2B81Szx2jdG0XyVps3WkbX33VQfsqqm1sXBaImXvxmVB%2FDLDlbvaubBd8g7rbbApxS8eeAMwIM%2FNhxoq0eKF3nvYC0JNCDm8etnJcOh4AsAyuZIfIJCHyp6ZakQ8vs%2Fz6MFnHnKIhcQXAUVC%2F79He5LpYZfSK7Dj4550eq1SLog%2FJ3qjJAR9rNxTJXN17Or03sMy8U%2FhE8MKTgXOaZHy9wR7zlLGA8Wx847X2MNnb20K2L9mrvWhSGP1qDVUqRYC2fZEbddnU%2FyzoT7cYmBj962M2HI8q5xT%2F08zPSsrk0NSqtT0YugwFLQWWK4thF9eV0r%2FF6PyKSVNclEoUdu%2FKnwnGEpgZuDOTRoPEmjD9LT7%2Fpmhy6FEhG4C8PhtQsxeUb26Aa0uJR0ZOJH4T9Xv5ml8s5PQjrevtTgOTdCQwC8NU8PHzmNumyQ%2F03YYzGZiKQJSGMc6T2rSC1Ybvl4wnO1w6S4m3oVhZiopfYZkiuCJnCHw5KPasGCpwHk774vlzzzB6ZyniNwXqTZfr1nemMGw%2BmGp0RGCGE3SK1R%2FPvZAHHl2f8%2FaK6V3AJWlifoowreLwigSI5lt9aDlpSST8k9Wpe3cmUQWbt1JEzMM7O98kGOqUBhbMB3ONBw8kF8JAFpiOGrXeqZFb1hLlgijp7x8NacVSdqLkgGbN0PvTtY1%2Fr1spmMDOjnhlgH2oGulQEHKlDclOW178QwPLvQE7HdXuv2FDe4%2Bi%2FJVd5u8zB6z9OkEjE98hskLYLcSfD7CzIToR3aok2rMfq9CcBiLYCVFIiqLn%2By0OtJujbSWMBCiupm7n%2FOiMwy8PoFooykjSbItbHdq0fb7rR&X-Amz-Signature=88ab15d0a0f17d2a9d0e0bf7c07ec4e1025fc25dcfd7a50d575b27baa187ed28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/79add2f1-05d4-4b12-bf06-902e4b32c1d5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJYMOZKC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDlLiIx0QCijrmXzAFqIN88fwz%2FjgQK0%2Fd4zsx67CjUawIhAJWWUfyVRiatRnUEazPGpKqHhgRxLFpPk%2FEvBCJiuqF1Kv8DCCcQABoMNjM3NDIzMTgzODA1Igw5QIuNihQ0n4hpaIwq3APZgh0vkhYbfVMzJdJaGw1ItjRuJVnU4I4hnU9qu71EbbjI5xZNsUIf%2FQAWzKp2cDo4DkxhiRrH2uYFw5sFtwJKeZrMrU8TP5WT%2B0th2WsBXKQHDh5jLdweERbiHt%2BSm7l6GVebkaA6QNrGbiVQvg%2Bir19u%2BlNsBjyy6uJxX3J02818GXFPIlszn7eFtMF2cqSi9qPvF31C9389pAU%2BPbAWb8heStzccgohUPvy8Tt4j9g4UdZhhpuEls6M1eyHjR2Yxc%2Fflycgr9TyiXKg%2FVCvLK%2BaCxO%2B54kqJE5MMVcaxmwUd3jJsc5U4946QCd0PPDT3TvWqRtjcSjq3xaJCxgp4r9b85ROZvqofArcJn4AJvQY%2Fr2HhSxEc6sSwFjCULI1c4%2FghzK8da2J%2Bu9ucaXADrsRqXP%2BK1JNAQHoO4KsJ5lXMyMpb0fX3vDAyi2eJ%2FrzE2km3n0DU5NVIk4MbxinWn9VeZeKC3Hk42jIrzJJXVsghbej8qDTbWjlBZ61Pw0f9rfblzpsk1xP4ghScjI%2F06Nd9jjaHE0xrqHpbxk5aOAZAAc%2FZypiijgFBz9ud%2B1fqQw7MvbROo7XEk9u%2Byc%2BfjQHKBKFZhqqmnDgQFJzHy1EF6nOQRfOJWXWWDCWzvfJBjqkAUMEB3iyYkiwFtTfC8Tn5HQ5aRNif%2BIuicWX4CnzTQcmQ2Wy%2Fkrw%2BhIdLeS8qDAVRSRGlGk2HjV62VhOqHMVgpMdF55iR9q1j%2Bq%2BssYyi7zxtvbhbqelezgFUmJo6n9RBTNasRHVyv1l7Ks9gSnbL2H33n8dkcWu0iHMyyEDj2PR8F1CKlZr4Wq6ed%2FMe%2B8RPnP9R%2F7CwvAvK2zlgmOlTC9tCPhE&X-Amz-Signature=6d6c123a1d61586961434b7357e6c942a27e612802a421d1a4f6a5093fa27fb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d82929e6-299f-486f-824a-b346718e0dbe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN636AOX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAED2KaaenvBadMTIqsoWmcVQ0IPUp7pQyhLFMTSwABqAiEAsh0ikG%2Faws9uaRGLB%2BkDhckUkEfAxWU7Rs1XldJ017sq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGCRGMYfUfH33qtGrCrcA4IKTJJBRcgLBGkADdHhcMDO0DamFUKvF8pjP2upKsrjUka1jg8F9JCzkEOk51Uw5KA70ZTLR681iRigHk%2B8ZBgWiU04pn3r3Ro4iScKIHFHUH8yGCnvwC3z5lY9kIwf29pO4ah2C7%2B0ASDDkKXNzrS3JQfKPVaEBAQXDlW4DREpz7svGuyYM2o8ZCn81KHB3eAEaIFtfHwOgKbtXLMP5cZxSVk%2FpmOESBlAGjxe%2FOqlTGdbBj%2FIjkZnV3sp4Hx%2BBqhmzfEbgfuHO14JJDqN3BeU3zjT2GTcV3dCGdJO8z67V5oC3jCcLnhaY7VVVah%2By1zEhXlIxl651pM3W8xrLVCMEZ56iT4BsMB%2F7Ie3hXSO6wSRDAyVKK0bi0FmXUsHS%2Ff8rbOTJitvO4da3S8HdlioPGwbf8aXbBbkIFKwNVnEUszKz6vzkJkdB5rXnoMhLi7WEIa%2BHlBnO1rHTvMvXB7mkBaDVijsxZHhC%2BDv3IElTvk2M961%2BziX5kuwsXFRffIh1ncy19%2FD4x7n8VZ1rqIGuPvOqk46DUYiZPVMq0lvWL97kUWcl7fQmKjBXIEIOStK9a1wMTGBb4BJuhuRlKzW8uNRGXTYK0p13T5dtr8%2BsMKRNpAwRXNmAMDOMIHO98kGOqUBFpKqSFSudKmzsKLtbfMOnA7AOeh6MKS%2Fu2O%2F8KuTOEGQb8EhAvd4vgAHNvJS9H84c9oZNDEVewkT8T2jrtIWQujUjqzA9zMjZKDalBJkz%2BsgjaA0Oa3uUqhlB9pQ%2Fs9dxHYGozv8VKm27LmrmU81NX11VvL6yOrwkJHcqbvywJodHTOptMLI2SJKkORwGvjWTVc7gJHgvozCBlYEjJ7peiOeqK6t&X-Amz-Signature=068419ad35341fe5a6fd26c37a021ad374c1bae9e828e7de365b8d0fe59c3559&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ only persons that are assigned to an address are included
</details>
</details>
---
## Question 2
As a nice housemate that you are, you prepared Christmas presents for your family. 
You have measured the height, width, and length of the packages and saved the information in a *pd.DataFrame* **df**. Additionally, for each present, you recorded the name of the recipient in the column recipient which you set as the index for **df**.
How can you aggregate the minimal height, width, and length <u>per recipient</u>?
The result should look something like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/daf59472-35da-4221-aecb-ad0307bc494c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UV7AMQX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCR2Kgb10r55KZeKIE0dXIn0ZM9A90k0K347Dc2zqA7bQIhAOgV8mmzfOnHh3D3ICLyaswBhMbVgDMK43BYnsssBaFSKv8DCCcQABoMNjM3NDIzMTgzODA1Igwe2rndaMcpussl1nYq3ANmtAljUjN17jlkk7ptmXL%2FvdygA6%2BeyLDxbN01jSXQUGnZLarJeOme0oL%2Bt3x90RqWFwKPdvEIcFGbmQ%2FFkbJv68yAx36ZflVUFw5Oy4uQ%2Bjyi%2FDbpriUGECf8pMQKjqUtSdTGlaiFfosVfXVOv5PWRptI%2BbBGJAPnLgyd%2F29zs47KVp9XWab2TsNbZEP7Ue%2BxPoqWm%2FsMYB8ScghYHvnAe%2BVuw1EeBvJYFEyFBCRF3uISDTmg1ym5GyM1s1HocxISYv5nwyhI1r5fRGa6KKynT%2F1sfaCG77PgGCeF8G2q4uDFrM7Z3sEDI9RNzMsXqrBz93P2zCyBI9v9rFRmw8IztOJCfEXHP8Su587x8ra1RdHdkB5NGFDsBBOSIMXYS7PYPAhg6sQZ3Xt4CKFKnEh7H9WrxpdFEjpdc2BPBcXLaFRr9KoFJKHnmVdAeGgl5KzD3iFNMa0HIYf3u1XY03Osu%2FDBBm5aIjRsA3RYvCRKoTKNUXDP0UVwzZ%2B25vEMfDyfQciJ8FIdiXUTO0My1RYZQ%2Fh6SldSVZnlLPR8Z9R%2BfQyft%2BlbE6%2BPoa45NJKlJLR5jKfM2gibw%2B7ePDaQ5BXNJYE7qnNlUsbxUq43YJAt%2Fh7WkCR%2BrYEdqZ8doTDlzffJBjqkASVEDpRb3SlMI6kaXRtOaJ3KbWJWkZS8XpSOurlSX5XE3GR8m4wPJQ%2BoJSFtRq4R9GlbjgEz0Be4VznxNZAxgVQSQ%2F8OhAjnU458NComrxHjPYPvi9MAuq4Zv14P8w2vQpvM%2Bp7Hbcqkdsyge%2Fe7ZHTtqYi5RlymSX1KSQqPc99m%2F%2F81p%2FWbTygmGOIwgV1RBw5%2B7h3fjbC2oOlrXgrm%2FYJIb0DW&X-Amz-Signature=040ed6609e1ccf93bbaf5b82e7b3e79c8fe888bf62b1a7c34f10cdcfea2d7598&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Mark <u>all</u> statements that result in the variable **agg** contain the *pd.DataFrame* as above. The *recipient* must be the index.
❌ `agg = df.index.min()`
❌ `agg = df.min('index')`
✅ `agg = df.groupby('recipient').agg('min')`
❌ None of the statement will create the wanted DataFrame.
✅ `agg = df.groupby('recipient').min()`
❌ `agg = df.agg('min', axis=1).groupby('recipient')`
✅ `agg = df.groupby('recipient').agg(np.min)`

<details>
<summary>Explanation</summary>

The DataFrame df contains a list of all presents that are gifted. However, there can be more than one present per person (recipient). Therefore, we want to find out the smallest present per recipient in terms of height, width and length.
To solve this question, you must understand how the .groupby() and .agg() functions work. As we can clearly see from this example, there are usually multiple ways that lead to the same output.
❌ **Incorrect**, because it selects the smallest value in the index column, which is the recipient that comes first in the alphabet (Bri).
❌ **Incorrect**, because it selects the smallest value in the index column, which is the recipient that comes first in the alphabet (Bri).
✅ **Correct**, it groups the presents by the values in the index column and then selects the smallest value in each column per recipient.
❌ **Incorrect**.
✅ **Correct**, it groups the presents by the values in the index column and then selects the smallest value in each column per recipient.
❌ **Incorrect**, because it selects the smallest absolute value in each column before the grouping per recipient is done. So the grouping is only done when there are some recipients left out already.
✅ **Correct**, it groups the presents by the values in the index column and then selects the smallest value in each column per recipient.
</details>
---
## Question 3
Which of the following data types *can* a query on a *pd.DataFrame *return?
✅ Panda Series
✅ String
✅ Panda DataFrame
✅ a 64 bit float

<details>
<summary>Explanation</summary>

Let’s take the **Addresses** DataFrame as an example.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7795a55f-ad9a-4b4b-bb55-e1f6fd9dbbd4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SK2MMD7S%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAiZ%2BsGP3gknwn70zWvN4m3ZuQlnuqKlDGDhGWsir2E1AiAmjZnY17bOuyLQiLPvDFkWs2I7zyhrxUapNGLBKmdzECr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMG09TJnNf5%2F4ZgaQJKtwDnSGbWzTznlPWiJFJ6Yi%2BkhgFsq1I6OR8L5GaRRK3yC7MNze78RbhINCCyQCJfgXBqAzT41HedL4%2BeN%2BpbmSq5I1l2tiMOxTyvJQSJ%2FY560A%2Fb9z1m3fXMPz9HyYcREiszXJyMMSQM5ff3E7A%2F5lzgHXnfYsy4ZOOr9mA4MSM%2Fr1SypEf%2Fk%2Fm5T5%2BH%2BBC31wtbyWw8fzGB3%2FmbhEpkHc%2F148b8obZhPy7SfPkI5CQVp%2FpC1ESaOaViBkpmUkUZHzmien%2FKgBQxsjscWTKE5MfLZxbDjT7qKmP7Mx5KODhsxSDLKYcgk3avgwO5tMiwxlyCOM0vvsseiNG0PP0oXMAOsxniw6GYxrhwmJmIY28VhgVm%2Bj0HLGZxRGIysFpg1JosDUyMhsg4Hx3rH0ABFhXJPSoXqN2XQjL7PbnOuV2OZk0MOUFdftFAcKXg3%2FAAKBJVJ%2Fr%2Fg2Bv3riADJSP1yB0syFWiyy1yW9YV9sTadX5PDrJ28D7HGZCNyaTQBoXdVocdXXf%2FAfrNeL%2Bfg0PaUhAnKsVswNYwlg%2F3vZDD7ObrgevqjqSlqXDawJwkgCoWJLgEpvLY5GZhOPSkdpBw6516v4h8hK%2BmWua%2BsJk611fVmTc98lQjgWtn%2BYQOQwgc73yQY6pgHBrP5mv2%2BTlf%2BYKFvH5vmFXdtee6kSD9Lr042GMlBwdK7EuR4J%2FpXnFy%2Fn5FbiXF%2Fc4yX7nkRoVsmcXMx6opOIzWywODsIjIVKXEkRwplG5bCh6vsUlAcnrvPaHNmUOfFUXoF7Ce3t4IZKhJuxPWzkfGlaS29ahYhlcZ%2BSXloWOQliHtFgA0Bq03GiCDLBHtsiR5tVif%2Bgok2mUKqT3L4vuazWY7iG&X-Amz-Signature=f12504ed24950b49e2411e8211e14831ac8b0324121bd6fbcf7296e7226b654d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
For each answer option you can find below an example that queries the according data type from the DataFrame. 
<details>
<summary>✅ Panda Series</summary>

```python
addresses['zip']

0    8001
1    9000
2    3000
Name: zip, dtype: int64

type(addresses['zip'])
pandas.core.series.Series
```
→ whenever we access a single column or a single row, a Series is returned
</details>
<details>
<summary>✅ String</summary>

```python
addresses.iloc[1,1]

'Bärengraben'

type(addresses['zip'])
str
```
→ in the column `city` we have string values stored, so when we access the value of a single cell, a String is returned
</details>
<details>
<summary>✅ Panda DataFrame</summary>

```python
addresses.iloc[1:3,2:4]

type(addresses.iloc[1:3,2:4])
pandas.core.frame.DataFrame
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/74745340-74e3-415c-b85a-171ec7a2ebcf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E7SJINT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDWnwaVLP%2BMKjsGJevrcNbG2nODOetHJtp1Sw3xAFzKcQIhAKtkT6HRc3PaKTdTzpkDpHdw%2FFIoDV9yLQzBKMikLVsMKv8DCCcQABoMNjM3NDIzMTgzODA1IgwmUVKUdvVHO5f5lzsq3AN9LkYwj9HXZ31HXMRTBMR1T7N0zRu23YnIUqZlNk38gbuCpmKLGnDBJPreKAw%2BMnlXzeTBmmhI6EWtYJl9%2Bt%2BrozGsCXXPzLREaRU1e6W3hErE%2FU%2BilkPH60vLa2wIYZGARUK%2BsyOU%2BIqCGwXdswnb2Vax58weyf%2Bl9mSFN7FZbU%2BFa%2FCBtD8agDGr78WR5p%2FQ9r4qm3YmL%2FNqeMGRmPSFvcPabWYDxEUS0k%2B2s0PJjmcsVFyFvhSbOBT4kWR5aXujt9N0NTefRsVvvdEIlAtPjlF3y%2FRW%2BYkV%2Fl67yXRaIQKU9Il%2FoYTAyC3U5xMEP6WPhL3YxY6vMXyySctei3BvItG9ixqF9OupF5%2BdG6C5jfBasANpzWjdDMJovJSCgB7mRZ0cRdLoAi84bdy6pLcmbxAYrvytKN5XQ9hytpvYt7mSDuHHnx7xT%2B2whXMt%2Bk%2B4BC%2FpTEs4%2B51sregI9A5PED4VOljyfvwPh5iVnpA1hQaEAwXxLWiD6LTuK1Ge%2FWWISLFvwK8nT3AvDp7KduJ%2BBGe5LcDo8611A%2FM6iAVc7HuJEl2qrSKwYQaW36f%2FDAY4yy4d7mcy9b%2BHe3q8rdxh6kJJxfPK7nFoN98lStX016Zv05EiYOOO6Y2TZzCzzvfJBjqkAaW%2BqpYQBoyqjFDcleaQQ9synVSLcik%2B0IvcBLnHiSR3H6mkQ6JJmiJ9LUSU3%2BD1Hfwj5ubucwuOVKzlMxj%2B6%2FTgEaRm9aiUsLn8GxFzgkna5rBEzYTV5du9cl%2BID0zJz1PG7tSU5hEbFifMEMRncsiG5qcWCx2kvvilQMqc%2F2K39pUjJuMTK2GrklJQTtDiYX3Wr2g2pGZhlsZWQta%2BqDm31x1P&X-Amz-Signature=6a42f564b2c968bbf5c968a313ca07d3973f3efbb65e9067ba71aab99fcff08a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ whenever we access multiple rows or/and multiple columns a Data Frame is returned
</details>
<details>
<summary>✅ a 64 bit float</summary>

```python
addresses['rooms'][0]
2.5

type(addresses['rooms'][0])
numpy.float64
```
→ in the column `rooms` we have float values stored, so when we access the value of a single cell, a Float is returned
</details>
</details>
---
## Question 4
In Assignment 9 you implemented the function *study_overview()*, which works on the DataFrame STUDIES. It should give an overview of where which combinations of *courses* and *regions* exist.
Now look at the following implementation of the function:
```python
def study_overview():
	return STUDIES.merge(index='bachelor/master', columns='course', values='region')
```
Mark all the correct statements!
✅ The function pivot() must be used instead of merge().
✅ *index* and *values* are set incorrectly, correct would be *index=’region’* and *values=’bachelor/master’*
❌ The function reshape() must be used instead of merge()
✅ The function cannot be executed successfully.
❌ *columns* and *values* are set incorrectly, correct would be *columns=’region’* and *values=’course’*. 
❌ None of the above functions can be executed on the DataFrame.

<details>
<summary>Explanation</summary>

If you did the assignment, then you know that this is about a pivot and not about a merge. Thus, we must use the `pivot()` function.
Before pivoting the `STUDIES` DataFrame looks as follows: 
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6ccf22e9-5b8a-4115-825d-54ea726f78d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZWINX7H%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAmQOr9KQiTI6iueifRgj6S%2BCkaO8RsvolppY47NxLbgAiEArVQnVf%2BDqTdbfBxxmgzQkWEe6knBWE3wySdaqpRlRcAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFjAnLjw8dlMKSHk3ircAxPrTUjunqn%2B5bIdmkoctiiUzUb6rlZ0kG9u1Vr6gQnguUsYE8ulHS%2FLmG%2Fj5pcPoL0Ym4jebvg%2FS7Y4J%2BJCX1B3N%2B%2B9GpNjR%2B1LHa8J2dobkSF4X5pQANvJ%2BIX17OCAqeKp3I9B5VUUwj36%2FB5MHKfgX0DozfNLW1OR8AMBiTQ%2FsX76PuNMs4nBHcwAylEOLqNKLqvcjmIrTJifuYEbH0yb90wVMEu%2F%2Fv0TFaK6GXrP%2FGLoUoxRJPr9egZU4q28Grnc6I%2BToTJks0r952VvuIORLVyEsaj%2BkthmulXjviZvLyDlj%2F5Eza6hCqxgY%2Bdm4IQskY0PXIpxofxAXmBo7kbFM4WpQ6wlDIT7jf9M%2BiiXE%2BeRMsXqgvLV7hpCsDLYF3bWPxmpXtO3D64ZcuFeJZfefTqOscEwr4vuZ5p9oxQnDkRz2M%2BOiMX%2ByuoC8H5K2JXOeWy7nqq7zsbgxkhonVFDMjBS6QIlGOm5n%2FrmdNqQmCJKIOQlYnEsrGIzFzwOkOlYRpNWXRrwXYAo2ejh51%2FmaNuY9VPpzKl1SKnRJH3On6fDiUHf1GJaQRhhNvnTvIckOAzU9oZIxpIlM%2ByGIhawlxnjO%2B7nkNUR2OTGNFJt71fqXoBIMZR95kBpMI7O98kGOqUB87pw7sJ8gNgOlnD5SfyXMehPTnSjcyHCGrIKi2aI4bsPylBUaniIJh8cg0UY3MJ46PaVgV8yLhX6KV%2Bx%2FeRIR6Ir6S4wEunxqf9WOMw60J1NcxPKgLjmf5ikcyRp9n0oTFo5dZ49y4L5SUgiQp2dupIR3OtxnuquHN6IBB1xdp1sTo6K8n57SE%2BXyipN4A9bglrXrIq4%2FCoHkE7yIvEduLHQq%2BIe&X-Amz-Signature=d8131179e0034cdfa21b9fc79d7a43d3d7a76f99ed4408d5dd36e93afba7527f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we want to pivot this DataFrame, so that it gives us an overview about which course exist in which region and on which level the course is offered in this region.
In other words, we want to produce this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7021005c-d1d2-4384-a661-26c1cf321e5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZWINX7H%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAmQOr9KQiTI6iueifRgj6S%2BCkaO8RsvolppY47NxLbgAiEArVQnVf%2BDqTdbfBxxmgzQkWEe6knBWE3wySdaqpRlRcAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFjAnLjw8dlMKSHk3ircAxPrTUjunqn%2B5bIdmkoctiiUzUb6rlZ0kG9u1Vr6gQnguUsYE8ulHS%2FLmG%2Fj5pcPoL0Ym4jebvg%2FS7Y4J%2BJCX1B3N%2B%2B9GpNjR%2B1LHa8J2dobkSF4X5pQANvJ%2BIX17OCAqeKp3I9B5VUUwj36%2FB5MHKfgX0DozfNLW1OR8AMBiTQ%2FsX76PuNMs4nBHcwAylEOLqNKLqvcjmIrTJifuYEbH0yb90wVMEu%2F%2Fv0TFaK6GXrP%2FGLoUoxRJPr9egZU4q28Grnc6I%2BToTJks0r952VvuIORLVyEsaj%2BkthmulXjviZvLyDlj%2F5Eza6hCqxgY%2Bdm4IQskY0PXIpxofxAXmBo7kbFM4WpQ6wlDIT7jf9M%2BiiXE%2BeRMsXqgvLV7hpCsDLYF3bWPxmpXtO3D64ZcuFeJZfefTqOscEwr4vuZ5p9oxQnDkRz2M%2BOiMX%2ByuoC8H5K2JXOeWy7nqq7zsbgxkhonVFDMjBS6QIlGOm5n%2FrmdNqQmCJKIOQlYnEsrGIzFzwOkOlYRpNWXRrwXYAo2ejh51%2FmaNuY9VPpzKl1SKnRJH3On6fDiUHf1GJaQRhhNvnTvIckOAzU9oZIxpIlM%2ByGIhawlxnjO%2B7nkNUR2OTGNFJt71fqXoBIMZR95kBpMI7O98kGOqUB87pw7sJ8gNgOlnD5SfyXMehPTnSjcyHCGrIKi2aI4bsPylBUaniIJh8cg0UY3MJ46PaVgV8yLhX6KV%2Bx%2FeRIR6Ir6S4wEunxqf9WOMw60J1NcxPKgLjmf5ikcyRp9n0oTFo5dZ49y4L5SUgiQp2dupIR3OtxnuquHN6IBB1xdp1sTo6K8n57SE%2BXyipN4A9bglrXrIq4%2FCoHkE7yIvEduLHQq%2BIe&X-Amz-Signature=1624a14e5860076f73eaf5519424ce9233aa68a25958c33ac638e9ad4bab30ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
If we look at the structure of the pivot table we see that we must specify three parameters: `index`, `columns` and `values`.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ce3fbd7a-7ed0-4aca-813b-7b876b8a9341/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZWINX7H%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAmQOr9KQiTI6iueifRgj6S%2BCkaO8RsvolppY47NxLbgAiEArVQnVf%2BDqTdbfBxxmgzQkWEe6knBWE3wySdaqpRlRcAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFjAnLjw8dlMKSHk3ircAxPrTUjunqn%2B5bIdmkoctiiUzUb6rlZ0kG9u1Vr6gQnguUsYE8ulHS%2FLmG%2Fj5pcPoL0Ym4jebvg%2FS7Y4J%2BJCX1B3N%2B%2B9GpNjR%2B1LHa8J2dobkSF4X5pQANvJ%2BIX17OCAqeKp3I9B5VUUwj36%2FB5MHKfgX0DozfNLW1OR8AMBiTQ%2FsX76PuNMs4nBHcwAylEOLqNKLqvcjmIrTJifuYEbH0yb90wVMEu%2F%2Fv0TFaK6GXrP%2FGLoUoxRJPr9egZU4q28Grnc6I%2BToTJks0r952VvuIORLVyEsaj%2BkthmulXjviZvLyDlj%2F5Eza6hCqxgY%2Bdm4IQskY0PXIpxofxAXmBo7kbFM4WpQ6wlDIT7jf9M%2BiiXE%2BeRMsXqgvLV7hpCsDLYF3bWPxmpXtO3D64ZcuFeJZfefTqOscEwr4vuZ5p9oxQnDkRz2M%2BOiMX%2ByuoC8H5K2JXOeWy7nqq7zsbgxkhonVFDMjBS6QIlGOm5n%2FrmdNqQmCJKIOQlYnEsrGIzFzwOkOlYRpNWXRrwXYAo2ejh51%2FmaNuY9VPpzKl1SKnRJH3On6fDiUHf1GJaQRhhNvnTvIckOAzU9oZIxpIlM%2ByGIhawlxnjO%2B7nkNUR2OTGNFJt71fqXoBIMZR95kBpMI7O98kGOqUB87pw7sJ8gNgOlnD5SfyXMehPTnSjcyHCGrIKi2aI4bsPylBUaniIJh8cg0UY3MJ46PaVgV8yLhX6KV%2Bx%2FeRIR6Ir6S4wEunxqf9WOMw60J1NcxPKgLjmf5ikcyRp9n0oTFo5dZ49y4L5SUgiQp2dupIR3OtxnuquHN6IBB1xdp1sTo6K8n57SE%2BXyipN4A9bglrXrIq4%2FCoHkE7yIvEduLHQq%2BIe&X-Amz-Signature=a95072fbbc9871d745df056d5290032e80f98bd2d3fde4fb6a970b61c738ca59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Thus, we need to specify the parameters as follow:
- `index = region`
- `columns = course`
- `values = bachelor/master`
And the correct function call becomes:
`STUDIES.pivot(index='region', columns='course', values='bachelor/master')`
</details>
---
## Question 5
In Assignment 09, there was the pd.DataFrame **ORDERS** with the column products that encoded the items and their count as a JSON encoded string. 
As a first step, you fixed the error of the **json** module and overwrote the column products now with a dictionary in the correct format. 
Which of the following statement returns a pd.Series with the same index as df and the minimal number of distinct products as values for each purchase?
❌ `df['products'].apply(lambda r: max(r.keys())`
❌ `df['products'].apply(lambda r: r.values().min())`
❌ `df['products'].apply(lambda r: min(r.keys())`
❌ `df['products'].apply(lambda r: r.values()).min()`
❌ `df['products'].apply(lambda r: min(r)`
❌ None of the given choices will produce a *pd.Series*.
✅ None of the given choices will produce the wanted result, even though it produces a *pd.Series*.

<details>
<summary>Explanation</summary>

The **ORDERS** DataFrame looks like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d484d0cd-76dc-4a7e-bdcc-97483546438f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQTPKTV6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIHH%2BiLkiBnDCAB3fTvsM%2B2myI0of2OusFXEKRPIXs%2FOuAiEAzCXcqi22SZR7Q2oamZX%2BjJOFOtyaXjuyICK2lrGv9QEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBneUFN5sV6ZHHKN%2FSrcA6Zj2luPKfnAfU2Ban%2FgZ9cwHJvUnOzM8tCfvE3Q08B26h0b2RLtoqmmydGiQWavGrKLTscxehqwRU88%2BPKqETvmqB%2B4zU0n3HpChNvWSKOPe1TdLKkQd3KG07wGjIQB8ttc%2FI7TQvEpnMy9Bx92IFcZGEaEczDA632QpE66Np%2FpkGAZDSU4rpXRU0w%2BLCShTS2HNGmy6BaBGJ9AIm2TLIGi6G5Cqtn9KwsnWVCnP5FbNyRGb5pZRfnGo1hd4XlAaeAnVjzXxvr5KT4z7ckmr6Ts5Ys1vu%2Bm3raU2ZcjPdmlujzfCVfYUrkIIUFUImGSwItT1S21LI3cHYo4FjqzXzzmHVkobZVKHHA8UGRr43r91LbBCjCXCyiVdAoTeV5f%2Fykl%2Fwz2QNubJVaISVdF66wOoc56PCMoBT%2Bk5qq5VMp0Sc%2F6HLUYPMWXrwk2IuVioobl4UfMW8J%2BNWegouqzMBLnzSNIX2Vylk5%2Bo6f%2FqDHh%2B%2Fe3B07m2xwd3uHpBthHrzHlutmPQ6BWosSkjOgEo2J%2Bmzt%2F6sEub05VqoKEX%2B42La%2BLY%2Fp9QitRN8QDx3%2BJsamcw5jgX1GJ38fOY8mEMd09FyNNtgME71frUHyFoWo1y5sGtiwh69VHPUUrMM%2FO98kGOqUBBl0YQD8Yp9ZN1geGrLg%2FZ40Aai%2B01w3NBopLCJArnO6nduk9eOJ6hR3pGA%2BhuOa9u5YNNCGgDlieuKaGNwf3fD7nTzz%2BpX%2BQHauc%2BwwB4PxJpMX3xgM2MimjwZa6F%2B8B9QMPcyZEaRlKA2CTSS%2BLT8egq7jLE4qHThXtB7YFRL4EOzF8nJNlQoJZ6SEZGzY5u0EmHzMf7PDt8EK330wnn0qUZST0&X-Amz-Signature=9aa2585dbc6ad0ef2e6b90b50d094a5219150586477b7c18e1bc61e35e2f2c3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that in the column `products` there is a dictionary that contains all the products and the according quantity that were purchased.
Now we want to count how many different products were purchased in each purchase. 
Let’s look at the second value in `products` (index 1):
```python
products = {'chair': 2, 'apple': 1, 'car': 1, 'smartphone': 2, 'drill': 1, 'mask': 1}
```
We can see that in this purchase 6 products were bought and 8 items in total.
So if we want to know the minimal number of different products that were bought, we need to extract the the number of keys in the dictionary, what we can achieve with the `keys()` method:
```python
products.keys()

dict_keys(['chair', 'apple', 'car', 'smartphone', 'drill', 'mask'])
```
Now this gives us back a list containing all the keys. To count now the number of keys there are, we can simply use the len() method. 
```python
len(products.keys())

6
```
However, none of the answer options contains this code. Thus, no answer is correct.
</details>
---
## Question 6
You have the two *pd.DataFrame* objects **persons** and **addresses** with the following columns:
```python
print(addresses.columns)
>>> ["zip", "city", "street", "number"]

print(persons.columns)
>>> ["name", "address_id"]
```
The indices of both DataFrames are continuous non-duplicate integers starting from 0. The column **address_id** in **persons** is supposed to be *foreign key* for the **index** of the **addresses** DataFrame.
There are some persons that do not have an address, so the value of the **address_id** for these entries will be *np.nan/NaN/pd.NA*. 
Additionally, an entry in the addresses DataFrame could be referred to by none, one, or multiple persons.
Which of the following statements returns a *pd.DataFrame* with <u>all</u> columns of both DataFrames **persons** and **addresses** with the following restriction:
The resulting DataFrame must contain all entires form the DataFrames **addresses** and their referenced person, if one exists. If no person is referenced for an address, the corresponding values for this row should be set to np.nan/NaN/pd.NA.
If a person is not referenced by an address, the person should not be included in the result.
✅ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`
❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`

<details>
<summary>Explanation</summary>

Lets’s visualise the two data tables first and plug in some example data:
**Persons **(left data table)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7496c730-cb41-4f7f-af50-44c35591eec8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663E5ITIWR%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAdoN2LZDg13G8f7k6y%2Fa%2FXINuYWmdaNjW01qs0LA%2FWfAiEAolkAC5NRylRfLPSExTzlL0SISus50Zt8Hr%2BU00yxcW0q%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJ%2BOtMqc%2Bdo4Msd%2B0CrcA9z9Ta1tTXjC%2BGf%2FO%2FMOSvVsLNFcHu%2FSyZ5N8XmzAD0IJfGKheiQlmuvFZBlyI70ZNsycldlz3%2FXAdKqmN34c9NjDmjHKAgIOTfhKZiDvHyIRVLUx7Dbo8OUfYdXksVsYBYz0F2J8Pq%2B2so%2B2HIl9wCeLceBAhWI5qHtj8MT286c8PU6TxANSoDx3vh4IToMWnbqNREMT1ld%2BGKg8VbbyUy1JgutORtSz4cYN0B5cVW2%2FQLLHJCUG2wwVfGBCyHvXkMa%2BFhFz2MkMwayMT1hukYRMaj5VBmXUcJ77t7B7Hcde4ryYt3GHE0ylD5IQ5%2FGqWSSRYtRqSyVJfmfJw%2F8frYUqJLXJn0f3WJnA7LQ9JvDDURrj7HEPK9EmrA7GKLvwUMyShfL91Pw7Qz7m6Z5OIhT%2BpZHE9vTpurdwa2zH4ofYFuEiQqBExDhhT6w5Ne5%2BBSx4KkFmUpaMIaMKRH%2Fgji7Q7ELU3vvc9mNq2wJB%2FsK0mGVm3SQd8wrbjCH6%2FeCMldsYft2nVw5m4kNK7VqwrXUdYmkCOk711YNF%2BEs6AsH3Zk9vBVqHNcChkjcHcnb9ZO0K%2BRfeb4m%2BeXMRNpMZtZSbJrP3sVNQkZBzOlZBKovil5om8cpTz%2BRBpurMMrP98kGOqUBAiZukr2JBwRGJqQKMMMV9uQspyXSslJcZtGARIMiCnQL29cgec7td%2B%2BC4W%2FzyinE6ThukyNSS75wJaL0qlckVGAx4YHruUUi6zt1jqvDdeb2CPyqf1jFJkiL0v9eQY5WS2cytwvSuC4h%2Fv2J%2FyD8%2F3Hda%2FX6N%2FZcwMMENx7D8kAo2ymsdp4WhWITESF6l2OTX9mZ0qIkrpuB6GCopYSY9F3W957m&X-Amz-Signature=df32386f6724a51aa29b5b5b24eebb1e2253afc6e473a7ca3f7d3c8057fe573b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**Addresses **(right data table)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/096ac0e8-1fd5-4af6-bd55-5f2706b0e926/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N4FIADZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICKfhMgTyJR4rtiGWURz3TYaV7Gs%2FO%2F4i5CemlniJzLOAiBsQH8o%2BT4nT44AmP3VXF3ptZGIcveCB7BkpPYU3PbYayr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMZdpfXix3mLQp9ZGNKtwDVwoLwKidOqvJXqVn7XbjNp7zipum9EYR3nje95ecI2ciXBx7UpgeQ2DWZRXSf6uEicDt7roAvDPaTz6x8nT0g7lkwk2dosOG4koH6VvU5FUwemnegmb9NHOmxU8m89p2Um7Vme1AVCHzBFVxGqwH0rpneha10kLfaULMtwLkDqIpxRFjz7ZFtd9kB9mF9i%2B9DD%2F9029RlOfrEqwXFrxkFIVFdjelL1sNmlF1MSeQjRxVbVzMzWxD6SYVTZX%2Bma2jtIvtk6CglGWFw0blJRNuCTPuzIRE6Rl1k4E%2FTxYYTVCHX%2BKDanKnowwLkp90bGrSqBjray38KS7aZGnEE8KzL%2F00V7wEHUHB5%2BBj4vmBDLqVlwJxyNQS8yNCaI%2Fav1dQRqPUqkePRfF4fWuGfkSPIFH6GbN%2FAuj3kbZP28%2BLrOI3tly57%2FcCbMV0CDHJka%2Fc8doIMg5je8b1fk6H5j8RygdHKqhhICQoSHJWmuXlTMlk6c5XsZlF4ALsrty4bFNhF%2BnrZLkuxoyMWimEnN56cAQVaVm%2F9FaV%2BX2zNS%2FvXvbzxOs5xRsgSxt9zImQ8EsqQx%2FQq32vSjbj7znoESFsbX%2B0I%2BK9j22oO5ujdp%2F4PnlPaEZ6wO8YkOdXE2Iwtc73yQY6pgG0e0Dk6qellL0S4BBKPG2LK%2BfYEOxjKxq6SoTRPkBKTValVM%2FylJi22aChciSUYak8TTrj%2FFDRLuedSBHKz%2BfJlxLZ4z2WDrrqHTqHxEgJX%2B26%2FHZXmlG7hkzISIuO2BygpylIAR4vMwfNPdqnPlrbsOQun%2FEUC5T8jsRx1GVJaAj5JDgk9cVOB0hqcvFDgifAy6LCby2%2BMzLkhuAnVYRAkq%2FrdEtU&X-Amz-Signature=39827f3add69ae91b8a9fea54d0f11a301b9bf06db936b50e90c0bb901e95dd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

By following the foreign key `address_id` in the **Persons** table, we see that Marco and Melanie both live in the same building.
We also see that Friedrich doesn’t have an address and that the third entry in the **Addresses** table is not used by any person.
Now we want to merge the two DataFrames together, without losing data from the right data table, **Addresses**. This means that the output table should contain all three addresses but only the persons who are assigned to an address: Marco, Anna, Melanie. Friedrich should not be included. 
We must define the following parameters to perform this merge:
| Parameter | Value | Explanation |
| --- | --- | --- |
| `how` | `right` | We want to keep all records from the right table, regardless if an address is used by a person or not. From the left table, we want to include only matching values, i.e., persons that are assigned to an address. |
| `left_on` | `addresses_id` | This column contains the matching value in the left data table. I.e., here we tell Python which person belongs to which address. |
| `right_index` | `True` | The values in `address_id` can be found in the index column in the **Addresses** table. So whenever there is a matching value between `address_id` and the index column in **Addresses**, Python should include the person in the result. |
This corresponds to the first statement in the answer options.
If you are still unsure, check the output per statement below to understand in detail what is happening.
<details>
<summary>✅ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/91295b4a-a196-48b3-a33e-68bbace9fc32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFCKXLWX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCQXMtcnO4ZiXjzElf9lmekBcDRV80d%2FmDmX0X%2FvlnqhgIgWlXDCB8mX4bt0WWto86q3%2FqjATRPY3%2BAdlt7VLWmmfsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNdEI2QkBAKCir%2Bn%2FyrcA3uvqKkvLMFGPN7lbH2NzmKqycn6NPEQS0hIQWDSMsSZsqkvtVNqfnGhnmp855zg6mqh5ATv3BkMwXUNUsys9HkxXVohBem5HSI7wksAKVFNynqawof8o2D9g3ZVRe%2BzGGXQGb4uki9ZdYtb38GhBdNZyaZrSx5K1K8mGFODeoCR31k1wjxJNn8UV3XVhthi6RD%2BaD0tcwj4BrPtjj4QD74HxGqoBBCLPty%2BH2Dgd6FKjtmZp6XDAobnVnOm7qOxtc%2Fx8IYIVksoq1qo6XQWGi0F4%2B4w2vwAl9IF4tEPMQq%2FtOhN47ONc6kPyEPLSvO0Ldw980a3FQJ8zX4D89hUCgeepS9G9qKEEckmbvW7hl3IAESgCFaXtGKvv5vaDrnssomF3S7404zU77Xnjqk7%2FFObv8YOrxovRaEwb0ZycvzstCLcpSJDcsbNU%2BlCBS175U8p%2Bds6cs4ScrSNeADGaTzszLRmld3dsERL5yaVmMFdPUB6W%2FEBLWA9PhE1ZeXrY10nH0whOHjADwojzCCGega0ZPZCvCQt6fG9i5IWIoUwo1wvj7xdrQiWc1lsnlVLL2OZWaqtBAdxA8PL4F%2B3FlDaBmM1n7YQgEslarZF0kyK7V1ys7zpcuB85LmAMP3N98kGOqUBtpvK%2FzWZstipi6HRYdNT2D3uUhzfeKVDnOTlCMW5VMtaQbtibqeg9z5NdVJTzMowDSwJ8e%2FVIkVNWLXO5zZySMJw7vO0NmLYhA42lLTt%2BV1WU6J1CILVGtsAgRqf5SqwNOVERC74m%2FMMwJ3zW7XGlC%2B5X8wMkt2VwdMVRBkh7kVwC9J30%2BLLruVD19g4X67%2BPnR5XMVjruVf1luzGld9%2FZOFUaY4&X-Amz-Signature=fdc6140bdd135bd900af1270c615e06437a834a6b0d5a9c299904861b5f8f247&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ only persons that are assigned to an address are included
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ead1aaf6-c414-42fa-bb00-b88bb8c18882/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCBNLHPG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDdElMge%2FiGaudoo2wDtPI7xKLSsKDaKzDMJX%2BpODVJWgIhAKzc%2BjkuBv2aHFZOyOxdHJiam%2Bd%2BGEtLzBaQKJQsOBKTKv8DCCcQABoMNjM3NDIzMTgzODA1IgysjLWiT2Zbu6%2FohHMq3AM%2FRzLdi26PxTtt2ZOvJcYdWnye0ADVVdMP%2BR1q3IfVhVAl5C5v%2BJBk5lD2oCJMIpezloqeASD0BWeN%2FTS2yBX4wxco2UzSTXAgqdSDknSh%2BjGGx0kOxdZ0dxD3TJNrk8Bj0D0Br%2BhFvKHAXNh7PtKOVyDCpm1n3SA6fA7B%2BHm4JSnTku8j7svfmgSWWpxlSwfvEprcM8Qwc5rjiTrxi7M22bMYzu4ocMJpgFiQlkLvQd8AecD43gtH2q2jsJK3XX7ySvkRULHh%2B7366D7MpQbCcBtmK12VneZKby8OIlwI6QHMpZFC2idvzP89qyJlDTJX5ryYelRo5kIPEe1jYYRZIeruDP4vp9Y24WS0vvloFcFhKNbu22LAUwUSQfc%2FeeUD%2BJEuip0B9tF6Quf5qFIzirbuF1FRvNc8uOBWdAyfERP035OeiRLTDc8NNww7ugnUbWkBaQ2mcwhxjJ5pjaDbsLM7twAJtcMrMdE%2BYOIW6Ez9OyyqK%2B1CFUOpwTkFCmFm%2BArAw466LKw85E1%2FAtmpD4WB38y7RmJvxMqNEb1S8MimbI9Zt13yWZylOLxMN9p2Z3WfkDkkCYJerPD72f%2FApcf3neSPKxcea%2FCdxJ43OoQ1ytI%2F0yCBjV8o1TD6zffJBjqkAYHD4UUkyjGbzXyuCr2KYp1%2B%2BdAL9DIyF3Z5ZcGtp3NlOpsbbcRDc4mT27BAY7OZR9AoeiC2%2F3KMHwCYDpQ4CD9WjI2zp5LtlqGcs3rJSVApThdLr1XypjRbCGoXqJM9A2nwf0pgh9gNhTkL4bOlD%2Bn72PiyoURPoelicosniqbEfStfxNZsA57P%2F9nJwBXciIbS%2BnYAD79O7pLrCXp4BJpjP4LN&X-Amz-Signature=4761a85bbc8002aa1adab66b077e513315474e4374165865f0998142cb2c9974&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ only persons that are assigned to an address are included
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/87be0349-c455-4f07-ad7c-9be7413cb92f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=3dcc5565e25a820d67c308a1a996a893a9fe9ff90a4e7d267cc70c57cc6dcb72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`</summary>

**KeyError: **'address_id'
→ There is no column `address_id` in the **addresses** table
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9f0a6977-7c62-42fc-bc16-72859d19254a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BFPEVGV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDjQDfkfPn5nuJBqro9RmVNAQk2Py5K6VeTsEw74bRFxAiEAtPeu1hEuNwvau8eS2a2uiM1GbTTi7i8XmZKYAEkC80kq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDK46%2FjwQGPFHqPPb8SrcA%2BB423cIe97XOckUhdGtznoUuPvc8Ggb2M8vlVjxMZ4G4T%2B0pq%2BmRS8DMAErDGMaiHGhDFBExQQDDK66FSQFPPfpODEsyx1hhWyHu%2FqOQQc2MljFgFyhELGYf7varc%2F0b1F4MVx0TdZ7LF3NB0t3ABH%2BEtEmcxHt3ee91QN74Y553XGlgf8dyL69ezkTc5MHEJQtNkzh6In%2B%2Bt3AnVeV1mZd%2BGrMS1s1xYdTipO7F9ro5%2FiJQs6cnzg77tOmCT1KnBZk1xLISdqS9xk%2Blij6Ef5sml%2BX%2ByLAkK8b0huufIG1iduJY8po6SLOVHuZ1qC8WpL4tGNEc0HRUAldNhWDSN3bZFDGdtXekrcRVB9HvZ8dSaCFgaid4IXTnL2o0KBqYcP6JHhw%2BFDJBPJnQ%2Bj3J8IZSBDnLYR%2Bi3KRZASrowD3thXVfsKOabN2UFbXyQmU2%2BBuuT4jR1pWEKPYi%2BtS%2BmZyvXdiRdaZ1xjcZIQZ6mSWpMiucPTVu0udTZhD5%2B%2BupeSXMItoUNvXuFP%2B8ZNArnrvHHmJNlTw6XeMT5oM3Q7GzR8mp4Kx9O%2FwchAmUFpxzmwc4reuGEetQQAcLR2CZcjBxUFTPvbfKUjukk%2B80Pn1sLPsZ60CnHjWDyDNMIPO98kGOqUBJWU%2BosSlnStwC4VojK2Q7KGcMxGS5Q91HT98jNGsMi2jg3zt8cfjBXUSKfuiI2EQZhLk9MRctnZyr0bE3351E5KJ7V9fU8iKpUadle2uVJnvAl7KIqQzGfP5U3Wcs9xw00aHwE6wHpyC0KD%2FHOICV1N7pw6tkPGRQoVMDdzzPv63n7bVmm7TF6bykc8FUrZstuUvKwCT%2FmmC%2BTSGSX6TPi%2FChMIB&X-Amz-Signature=3ded29ceb47efcb6ad17b39c3739359bf05a2adfc842823f9c65cbe5da47081b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bd8f2a5a-01bb-48bf-9f2b-40d2d8b90f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653KMPGQB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGAbRwcVDoK6dsUWaTfNji0ijhxrBvpMg%2FVSswPWBQaQAiBUlVNgKF6JP9qylwZZ7yxGrvQcawiQOGRhluJnTuoqdCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM93Ya4E0VxcnMSuPWKtwDPgVvsj%2B93sheerKQULCGuLPa%2Fd425qrNMUJ8RUkIOq%2B5llPGNyvgVtwZpJUiW6OAwfGTVNq72ILNmBNeUX%2FQTbEjqojLYXxlj1RIyxnyDa8zdtWLItntkkG6vO7N6USztJgI4r4HNiwViI%2FnRZ6wKiX2biYfiV6REPVkZOogttPzUdyG0VBoPgbwvpTLx04QFXSyyzSUMyEWslcxXqx0kzspi9u%2Bb%2F3fqqC3F2KLn%2BmqlSXjQXQxCjMaCwgvbxfI85ApkyInn6ishjUdT22ljk%2BXBdaB2MPk8ChBV2yGw%2BAtKtRDTEwysV1xNPoWp1frOofqVfHrVKraQaQL4mpa0fmu1iZEt6PPQrgXexgwnjWHnmbaEC98V7chOsrEYpKnpEvs8WDiqDVdGaicAEiR8Ng9mi52ZBVt%2BByXNsHzhU9DnDVm0aaJF1DiV6CKrOzPiKlIHyaIdYB%2FZCU26mhN6%2Fmz2oUZL2kRBaKIMGMzLWbsqbmiXuiz2Z0A%2B24rhWt6t7LYyfC8kFj0mMserby%2FJnLH1o07b11w32Jal3nk7rsPL9D1KJewWG0pPGprzLW5e2XdMpXM%2FjLjY502Irsg1qKYkA7npy%2BAflyYqYxriwIPNFrjWaQMzFyqX0Mwtc73yQY6pgH7MALFUXg8KE61PxK0UKXp46GaQxPCvOiMgmDna3JsVKlgf06mHkvaOQZ2VIH1%2Bxykh9D79HXZdYrx1T89bZsKEyjbk0lovJpKovJSLxM5f5radnVbCFNFze9hG26y3CvWkW%2F%2BrM570%2FXYLd4%2FDmwU7ye7J9K3XOjtZ%2FBAkioWTaIJ3xTpHrajyu9Kxs%2FK5F6KcNJd6uzdn7E3RGn8LQtTV3oM07kr&X-Amz-Signature=315daac460026cd4d7e75d9365db272826da150af2be046284ebe93fc737aa1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/79add2f1-05d4-4b12-bf06-902e4b32c1d5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JLQCPYG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICkiqXAJfxHRJX3cPbt3ryTUYRRv83qf%2FY2sZSDgt1EeAiEA8kWp5Wq4zlvew409Wm8%2Fzi%2F4f8Kzgs8N2uBLuELqSeIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBpWDt%2FpST36%2BdUkaircA7XMDIlSx9tWsrZAPq9frd3yvwphIuGE5uGgcilhu0N8iKuaWHUxFVwPUaGlZawGgATxqwY8YLWkMDKXOY4a3pXODf9%2BqmgY5Ol9cNHR9C0ND6LiH3Glhw2opejVZ9Y9rdxSTTXwg%2B%2FMrJxEWnxct4TkU%2BX1SIwb19cYalB2i6BJiF%2FaoZNa%2FJexDiMCJwwsX30ES28SjYBdqOVs7K8AFs1xkRKBsqfsTUI6IMiwP0q0eno9zeJiUaXrEjxLC0C6Dw97SkXWLR5jS15tLe2XtDMSVwlEZI8oB2Gg60xuZsvy5dzmwL%2BCd4n3sm5XR5G4n76wEChT4VRx4FxZhH%2FfskaTM2I6a1o%2FyuH2BGRwfM6OplJEXp2RcXd2yfLahKOrvQdGcberSTcb%2F2PibEtR3brwVjB%2Ff85SOOmmgaL0ldIxXv%2BcXIADu3BLLCvEqpIu6Z4MnxKvXYD4D7JnlXLx4%2BVDTHIabGhCHQI%2BlPASfHGJlidz4jr2%2Fc8a4Khkot1yv4GWZbccKfJYZirJRp%2FaRvAt2%2F82Ptgm7kp0c6BEIAksrUMRUabVaAS8rVDfe%2FInvoT33q%2BYk%2Buss5MLi6fX6sewMlK7Sk1VvBNrse2zQB%2FXwRCrLQ6Bi4HFwCCaMMXO98kGOqUBoPKhwii5%2FY4WHYoP2uuCUq1RRMemUh8KCDiTsfR8p6vuh7QfX4KlbAPwVkndbvIolvIaet768oJoJkBckd3CHbq1uE2KRHk18l7Urxmwhas6SuQoSdMA%2BPcVpY%2F17cXsjQ0Q6m2xwTtmh5fmDQwrcGB5EWq8xr3J8pjg%2BF9iSbWO1UDGXcncLb9rnSKNxGxHlqIuhLgw9vy1imzI4TXRQvN0pldG&X-Amz-Signature=f8a94999f948329def6178c93677641b70cb0fbf087839c95d3970f444a94019&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d82929e6-299f-486f-824a-b346718e0dbe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJZ2TMX2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFrykteqCqf2tyzUMqkQnKsL3x27tQIap9qzR%2FAhuv1yAiAy85Kl2dAkG%2BP1H%2F%2FdQZ5iyZeIOzvLyJXz%2BJ6a0TWzWCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm9Z%2BxmDniqTNK5UCKtwDUVeOBGgw4sBkKp0AX%2F%2BK0ZIqSOaIlVs1WrcEdX%2B1%2BLcl1Ozavw2U6YXBzDrhzG0djuVR5H9LNdc6IZe5dmVz3Tx%2B1BeBSYmg0ykfMQdlZW3UVYFZlGI4rrGbj8nHTZBUwHyhSBpCSWpJG8a44SVGyVLsCRI7FTbcZT1TZ96gb3h46W30Du7PMGK64Q4cYZwpQ8P%2BOrVFKPC3F6VUlaAH0iVI%2BOpKn%2BriQkPZDpDtG1Hy2cb2DgvUF1LCbNiR9RSn99CY2NeYXwQ%2By949Cj5VQwqzC5%2FfpIYhaYF437cDPAhbF2dr7fbG7amhr4mzmI3mSCxA%2F7tYDfHiufCyOHew46Kge7EkJxG%2BKO7KYtyvhimdxV3%2FfBce6SxKjmNszyD1agAfFS%2Fo%2BRyd34bo2Ex5PP9ekHaLfBv%2F6z%2FAf3q%2BrNed6GqwebtpBpszOygEm10IL1pWE5ewiUDQqdDsa%2FkP9gSTFQ0kJrohYzIQT5UNvOaCxIyZOgO4K2oYLvgZREzdMSFZ%2B8oXoOFu%2B%2F7RQ5xJTPu8gCGGXFQjyVmQqlIQLGm5z1B4kJDWz9BUSkwM3%2FZi01%2F1GJptP8jpAD9TUhulVSAI54vV6uKv5E4cam7FJv%2FiKlq4fGkPv21FRMYwtM73yQY6pgEeI0MNI09DmqD5WfmFGJOqfFr9x447kC%2FcefM5U5gouAEqZ5I%2BHInXVMFLjGYLGyTxaKf1IiwT08yl0QVwnOGHbycy5ETBysskHz0XyNn0iSIoFyOzf3CWtVcGPNcTL9SZa3o%2Bv%2BjcmVaj4cUagq4eGLMdVcJ9YUW0i5DBb8S8vhhWHpYzT6keahd%2BkzuRZztDyit6oDJwuivfAP6HQKpkJLJSMChe&X-Amz-Signature=fbc4bc1f9414d2baaef8c772a0354f29fe7ed69526e57b296387c57f17719a83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ only persons that are assigned to an address are included
</details>
</details>
---

📄 **[Quiz 10]** (subpage)
## Question 1
How many *axes* are created with the statement:
```python
fig, axes = plt.subplots(7, 8)
```
56

<details>
<summary>Explanation</summary>

The subplots function takes two parameters as inputs: (1) No. of rows, (2) No. of columns.
In this code snippet we create a plot with 7 rows and 8 columns. Thus, the plot will in total contain 7 * 8 = **56** subplots that can be filled with data.
</details>
---
## Question 2
We want to create the following line plot with the values from following *pd.DataFrame* **df**.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ba7cae60-975c-45ea-9d4d-d5740d079a09/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=7c1198e99be9c9e3dfc06a42097bf53a33c39f14e45f7d2d6750a62b86357da2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The *pd.DataFrame* **df** looks like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8855b98d-ce33-4262-99e5-5ab81fcf48a2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=1c7629c605381d7951161ef99a571a732514b58eaf8bd9f1efd15b64812a1429&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can you get the x-values and y-values for the **blue** line?
x-values: `df.columns`
y-values: `df.loc['Banana']`

<details>
<summary>Explanation</summary>

**x-values**
The x-values are the ones that are displayed on the horizontal axis, i.e., the weekdays. We see that in the DataFrame **df**, the weekdays are the column names. With `.columns` attribute we can select the column names of a DataFrame.
**y-values**
The y-values are the ones that determine how the blue line flows (if it goes up or down). Each line represents a fruit. The blue line represents the fruit Banana. We can see that each fruit has a row in the DataFrame. Thus, we want to select the Banana row which we can do by using `df.loc['banana']` or `df.iloc[1]` (Banana is the second row in the DataFrame).
</details>
---
## Question 3
Given is the following code:
```python
fig, ax = plt.subplots(figsize=(8, 6))

width = 0.3

xticklabels = fruits.columns
xticks = np.arange(0, len(xticklabels))

ax.bar(xticks - width, fruits.loc['Cherry'], width = width, color='green', label='Cherry')
ax.bar(xticks, fruits.loc['Banana'], width=width, colot='blue', label='Banana')
ax.bar(xticks + width, fruits.loc['Apple'], width=width, color='red', label='Apple')

ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

ax.legend()

plt.show()
```
Which figure does the code produce?
**❌ Figure 1**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/695a6b05-f2f8-40a9-bf6a-a39a44b06cb5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=f9337971fe994627f2deadae554c4efd56e3fcdb26b97e7bb7160a1a1b8272aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 2**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/28f2f2fb-1f68-4c7b-bcd1-b8a02271a5b7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=0e83d53992e90cf001a26d6ddca0dca1a4b09f00ac739f19c6024c7097a15d45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**✅ Figure 3**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/671fec9e-0d8b-481a-8e6d-5e86347f6490/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=0cf4a9a08b2230418be8795d1629ae686a9d65524869c8f0051d904966accd6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 4**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3d5de852-f8cf-4ece-88eb-e79c917123e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=2441a3c871ef9627997b5be70add8003790dc70505843aa9eed81c68ddb70b20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

Here the trick is to know how the bars are positioned. We can figure this out by looking at the following lines in the code:
```python
ax.bar(xticks **- width**, fruits.loc['Cherry'], width = width, color='green', label='Cherry')
ax.bar(xticks, fruits.loc['Banana'], width=width, colot='blue', label='Banana')
ax.bar(xticks **+ width**, fruits.loc['Apple'], width=width, color='red', label='Apple')
```
The first parameter of the .bar() method are the x-positions of the bars.
We can see that:
- for the **Cherry** fruit, we deduct the width (-0.3) from `xticks`. Thus, the Cherry bars are positioned to the left. 
- for the **Banana** fruit, we don’t deduct or add any value from `xticks`. Thus, the Banana bars are positioned in the middle. 
- for the **Apple** fruit, we add the width (+0.3) to `xticks`. Thus, the Apple bars are positioned to the right. 
In the third plot, **Cherry** is on the left, **Banana** in the middle and **Apple** on the right. 
</details>
---
## Question 4
Given are the following three boxplots.
In the image, select the region where 50% of the *sepal width* observations for *Versicolor* are visualized.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/74518876-1b87-44f7-b914-783cb42a8308/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=366ac9510eda879c6aeab5e800b8883861a38d88d9393c34d4754227e6120553&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

The structure of a box-plot is as follow:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fd06423b-c4cf-4779-842a-ac6488fdb79f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RORUTW6P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDs6MCIz6cR31Z7BWX%2FZZWmXAZiHEA68woYcfwqyhPaFwIhAMxHDKMB3AB4NDMC34atJg9UkZGovyKE92SLri4AcXf4Kv8DCCgQABoMNjM3NDIzMTgzODA1Igz8F1RLXaKHfOG4lNIq3ANOzAwtEE0NBvADEw2AihCKyBO%2BDHG5hGSHbFvCXPvwxHKO7j07sZZkUGvWtvQd%2B4E%2BlR1I3GppH1AcPORq4rhlA%2F8OPNR%2FeVDVEuMpeeH0fK9%2BkdBkEjvrruazL%2FuXvEHWFkBnuw7uU6WmqXQZabmNcTOgLZBVJmwon%2BNWvtR%2FvZBpNdOYT5lYccZqBlBMrgf4Ly6HpwoizAv9n%2BJa9Lq%2Ff2V%2BU05odTh5vyjoySfHzky7Yfxz%2FYXbSs%2BOrPBSXb0hUyhpboYOlCDagQKbuyHf4RCUdmrNCZ%2F97XfmBS6vX2jdIAkX%2BAfr92DemG5n56bw3wec3TJgC5xm7q%2Fh%2FnTIgdiDclsXk1nLK5HteTSHJTImUBKAlCEe1WWhMLyU%2B0bx96tCcpHdMzXfZakFBvfNCvGWHz1C0DTtZCBceA5b0xc9Cc4gHFcfUT5r5xfWlYFMsosNIFy%2FXD93JCHlOOYU3EZKSAtDJM4zmsSrIJs5LYq3Qmqebc88HJQgfPLoEOUb0T2km1iQdyB%2FuVXCzodApxTAkS5rY7NnPI3JBi63LGApXPX0yp4xOlonI%2BzbZ3MedolPQid9TF2t3nQQKkRhtM0aX4d8BdV%2BE%2FDLYMRlxOVIP8Up4ES3bZmKnDDTzvfJBjqkAfPuvTzRv0iPveTY3R2Gm%2BmRJ6yL2pig3eSDjn4YZVMsNuLWJpb7ZZzi%2F9C4uHfG%2Bal%2B2pfcuug1wRQ1fctjtAeOCDOtjoeIdt4mtsI7NGYTucpw39SOcU%2BEtY2dm1hlFcrtrH6KWp6Q71r7bZ0WElSxrndsflVN4vJUs38BPQSM8GjkUYqRGsvWvY6Z4ZO1JhxqjzZYLAdKhQjHCL6HGdsA9GPY&X-Amz-Signature=2c4166d96cf7fb60c7d01a291f3ffde9e3ee8f5bf9806d854362c6b3b6e664ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Each quartile represents 25% of the data, thus the box in the middle represents 50% of the data.
</details>
---
## Question 5
We want to produce this plot:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5363df47-9e70-4389-9327-e859bf892a00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=55d808127a60da717c574347a7635a5ee8b01ed27dce1416f66de3d850cf4bce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Which keyword argument is required to create this plot?
`fig, axes = plt.subplots(3, 1, `**`sharex=True`**`)`

<details>
<summary>Explanation</summary>

With `sharex=True`, the x-ticks are shared amongst the subplots. Thus, the name of the weekdays are only displayed ones. 
The y-ticks, however, are not shared and are displayed in each subplot separately.
</details>
---
## Question 6
We have the following *pd.DataFrame ***df** of fruit sales. The code below was used to create the given figure.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5ecb8592-f208-42fa-ba9a-7e451775c803/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=921dfe9c4b975df9d473c599a99ff20b9ca91daf9b2095457cadf9d8e22ed24a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
fig, ax = plt.subplots(figsize=(8,6))

ax.bar(df.columns, df.max(), color='green')
ax.bar(df.columns, df.loc['Banana'], color='blue')
ax.bar(df.columns, df.min(), color='red')

plt.show()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/873e4980-985f-43d3-87ee-044ba976e19a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ4UJD4V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCZD%2BVOyVCI1iazozvNdFIRb%2B84wXkE%2Fem9Puu8yY3WqAIgQ3SNOoCBy%2BUwA3hP8Is9bH0MoV4zlqSxL5FIrxvSJmcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLpYscfitQoo9%2B8iCCrcA9H4sU8OdJoqEbtVYGWujJqML5oRYbn1FNTonnhOdSJIOoYQLRaEVlDW9R0W4PJLP1B3pnkL29UFK7M4h7wh3nTNj7d%2BoQX3zjTEtSRtuaq%2FryrPz28ffxGQTqd6LiLgShUq8HG4MohzCCoE2eTNlvCAnbQmmKywWE9oUfj3DmDJRx3MUdYJkC6RkCquT0lfM8%2FjUGPkkIocaSa9ebmzvkPrdjE3Km6uxy7%2BJI1yuNOcNU6k8wbSqbGW2EJWFQ49RzCTLSQ4wbruMnjKZhqoFYURoV%2BL%2BiVefMy4eFwSRNEL2a7tg9aZW5fyHZvo3EzURXPxjnJJy%2BhddaQMDK5kfiDcq1OE%2F2ypGhqtAEmeAXy1LbpAUHFEPtOiq0Lkbm%2FXjO0G3ujKHcFLTVUuFm2%2FCkBruz74aMBbWILeHso5Jui2Ks4%2FF%2FPqkYSV4J3aNWAzXzuQV0yd%2FL%2BqloSyMCyeqlRsCYynJzSRiuObYE%2BDKLCJ3PGjm%2BT6GrbHLRYe3QwwcG%2FQh92uN1y5Ph5RKWx0T57mPhNAiGBEZa0psvYwXUnVfV6IDoBrAq%2BJaXQOZmJ9mzmGbeOL3RNSAmHcGMAeixhOB3eawBP3xGZrPMe7DfbmGRFY229pzZrKGjlBMPHN98kGOqUBdoSe7W1A90XVNYx3WEMnyu6%2BAXAvVg%2FhllADPxhemx%2BCDJg7lpSvlt8WBknY7wIm2bhJOE2jP2MCuRnJLcnvfZIsdTgU2ruodHC2cEDZL5AJPJUxEKfkoIoIiExqLIX20GeErUkLl9RZNjisruzM6Q46bb0TO29C3zYt0%2FIyMuCIjsUCm8%2F8BD8mdgVD1MOiFaxgkBgE5j3eNuK8z6iLQHn%2BW7kv&X-Amz-Signature=1ee7d581c96177531e6929113ae9989874a2722a72c617630e4d59d07cb509d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Mark <u>all</u> the statement that are true.
✅ From the plot, it is impossible to know how many bananas were sold on Friday. 
❌ Relative to the other fruits on the same day, most bananas were sold on Wednesday. 
❌ On Thursday, Friday, and Saturday, the sales for bananas were 0. 
❌ Friday is the day with fewest sales in total.
✅ Bananas were the most sold fruit on Tuesday because the blue bar is the largest there. 
✅ Sunday is the day with the fewest sales in total.
❌ This is a stacked bar plot. 

<details>
<summary>Explanation</summary>

✅ **Correct**, because the green and the red bar are overlapping the blue bar, thus we can not infer from the plot how many bananas were sold on that day.
❌ **Incorrect**, most bananas were sold on Tuesday. 
❌ **Incorrect**, the sales was not zero, the bars are simply not visible in the plot as they are overlapped by the other bars.
❌ **Incorrect**, Sunday is the day with the lowest sales.
✅ **Correct**, the blue bars represent the sales of bananas.
✅ **Correct**, don’t get irritated by the heights of the bars, as they are not stacked on each other but rather just overlapping.
❌ **Incorrect**, it is a simple multiple bar plot. The bars are just overlapping each other, which is why it appears like a stacked bar chart. If we want to create a stacked bar chart we would need to define the `bottom=` parameter.
</details>
---
📄 **[Quiz 11]** (subpage)
## Question 1
Which of the following statements regarding k-Nearest Neighbors are true and which are false?
❌ kNN only works if our data is 2-dimensional
✅ In the case of binary classification it is a good idea to use an uneven (odd) number of k
✅ kNN is deterministic, if the nearest neighbor can be identified unambiguously for every sample
❌ In kNN the absolute distance of every of the k nearest neighbors (for k>1) must not be considered for the prediction.
❌ kNN ia an unsupervised classification algorithm.
❌ We can’t use 1 (one a sour value for k).

<details>
<summary>Explanation</summary>

❌ **Incorrect**, we can also use kNN when there are more than two dimensions in the data (e.g. Wine dataset).
✅ **Correct**, because then we can guarantee that there is always a majority class that wins and that we don’t end up with a tie in the majority voting.
✅ **Correct.**
❌ **Incorrect**, to select the k nearest neighbors we first compute the distances to all known observations. Thus, we must consider all datapoints.
❌ **Incorrect**, it is a supervised classification algorithm as we have to provide the class labels of the training data, otherwise no prediction is possible. 
❌ **Incorrect**, we can use any value we want for k (k>0), however, using k=1 does not make a lot of sense as there can be an outlier next to the unknown observation and then the class of this outlier would be assigned.
</details>
---
## Question 2
You are given the following confusion matrix. The meaning of the rows and columns is the same as in the confusion matrix that can be created with scikit-learn. 
For which of the three classes does the predictor perform best? Click on the corresponding image of the class.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f03fe3a2-dff9-4dbb-a4ee-502ad31480aa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMI7JWWQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDsSkEAeCueHG4Y9B5vzNDNpQa5mMBqj6ege3IaOch6vAiEAo1C6uAE2h2P5aWtGzI0Xnz%2FUh9qxqkaR5Qd357HZaicq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDG92UlBd2Png5BVhCircA6GZ6XET44Tr0O8gr1Xszz1GPIzkukN%2BNq3ivqkB5XjJDBx1ZC9Cipu6Z2mfsO6n03V0BX1eoaS5PzRjL%2F4%2B1ABKAKUqlg1qbhY6gKYpBYre4Da6eKr1kwUxIlMVulwmvxv7kT%2BzjqAvP1ljjaL%2BeQkoastOPjPN1PkJgz5vaxLXAGfcT8%2FM54vS0vk9TetGQqVpNVKt%2BL2aZEEyByG2JFOW6fa9K%2BzuCKVo%2B05usXDW4p7sxmDc%2FNWGcTPDpW9yrJdMJhh3QI5gDpayen7KMaFPMzZmkRDBDkYh5zZsBeXpQxM7sFfrmPi1Fc0g1DGJF6o%2BUTeZy54qDrcRPQ1wX9lYV0WA0KvXeAlxzWSe2PfdIWu7npbVF1OM4WQXCf9aa2XFzWL5oVHm9mhmB4AGRLvkCo8tYlDYUH0%2B0YdgcpULgO3UPAKYvkh0WIFxB%2FoIXH0rEad8p4us6uYECwUlLM%2BJUigZdVMw3yarYKCbIX3vh0GD1XxDR1S5PSgCqQIOoFkXHSxwPwurSK3GgXZhE261KGQQLXrECpIUGY84OvWuwv%2BJk3Y%2FE3h%2B7EDrbwQ5N60iOdHR4XehJhNkIpymj4gu4aF9P%2FSjcuYX1V6sshbxG0LY2Xp1hdPFPKCvMMHO98kGOqUB5GEuMcEjmkIx%2Fd8SxisXUbeVN7sbEcGOrEWsTiUdm2PoxQmargCH7tZq%2B5nmNcqjw0hxKn5c43xorUiofNzGGot%2B3kdCeIiJy7DoDrbNOXVDjU7xTMnCFMb8e6re6RsqiplERgUa1FkauZYRnVnJYepRyY5ctFc3LU7Y%2BStI%2FYMvRPJO4hsbPuRz5pP8EHGOAt1OlD%2F6QI0ZzrOeTxCjm9OqEm9O&X-Amz-Signature=9c13c4d093ba90e02bedd7ac91348fa760f4ed15da9f7c7db2bd3dcb02942682&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

The structure of the scikit-learn confusion matrix is as follow:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b2996f9d-91d3-41fa-84bd-f3c4f27c6cc8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=06865d937e03283c0532ca65b80553dd2b3d4002e953081a7388cbd51ce1b596&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the predicted labels are on the x-axis and the actual labels on the y-axis.
So we can interpret the confusion matrix in the exercise as follow: (we assume that accuracy is the metric we foucus on)
- **Animal 1:** Out of 30 animals, the classifier has identified 10 (33%).
- **Animal 2:** Out of 33 animals, the classifier has identified 30 (90%).
- **Animal 3:** Out of 28 animals, the classifier has identified 15 (53%).
</details>
---
## Question 3
The confusion matrix of arbitrary size of the results of the evaluation of a classifier has only 0s in the diagonals. There is at least one sample for each class, but the classes are unbalanced (there is not the same number of samples in every class). 
Which of the following statements is correct? 
❌ The situation can never happen.
✅ The classifier was **always** wrong.
❌ The classifier was **always** right.
❌ Every class was predicted at least once (regardless of whether or not that prediction was correct). 

<details>
<summary>Explanation</summary>

A confusion matrix described like this would look as follow. Let’s assume in the test dataset there are 50 observation.
|  | True | False |
| --- | --- | --- |
| True | 0 | 30 |
| False | 20 | 0 |
We can see that the classifier did not predict the True or the False label for one time correctly. 
The classifier classified all the True’s as False’s and all the False’s as True’s and was thus always wrong.
</details>
---
## Question 4
Which of the following statements about the IRIS dataset is correct?
❌ It is a dataset for binary classification.
❌ It is about classification of flower colours. 
✅ It has three classes. 
❌ It can not be used to train a kNN classifier.

<details>
<summary>Explanation</summary>

❌ **Incorrect**, it has three classes and is thus not binary.
❌ **Incorrect**, it is about the classification of the type of flower.
✅ **Correct**
❌ **Incorrect**, we can use multi-class datasets with kNN. And the data is also two dimensional (sepal and petal length).
</details>
---
## Question 5
You have written code that trains and evaluates a scikit-learn model. You run the code multiple times but notice that the evaluation results are different each time. Which of the following answers are possible explanations for this? Check all that apply.
❌ The **classification_report** function is not deterministic. 
✅ You have changed some or all of the parameters of the model between runs. 
✅ The **train_test_split** method shuffles the data.
❌ The model is overfitted. 

<details>
<summary>Explanation</summary>

❌ **Incorrect**, as it is deterministic (it does what it should and produces the output that we expect).
✅ **Correct**, often we change the parameters of a model based on the result it achieved, we call this hyperparemeter tuning. 
✅ **Correct**, the data is shuffled according to the train / test ratio to prevent unwanted bias from happening.
❌ **Incorrect**, if the model would be overfitted then we would get consistently the same bad performance on the test dataset.
</details>
---
## Question 6
Which of the following statements are **True**?
❌ Unsupervised learning is preferable over supervised learning because we don’t need to label the training data. 
✅ When training a classifier, the data quality of the training data is important, because the classifier does not learn how to deal with wrong data. 
❌ In a supervised learning approach, using all of our labeled data for training a classifier is preferable, because we then can assume that the classifier ha s a good accuracy for classifying additional samples.
✅ Before making a train-test-split it may be a good idea, depending on the data set, to shuffle the samples in the dataset to reduce potential bias of the predictor.

<details>
<summary>Explanation</summary>

❌ **Incorrect**. It always depends on the use-case for which we are building a model. Sometimes we have labeled data available other times not, etc.
✅ **Correct**. If we put garbage into the model it will give us garbage back. 😄
❌ **Incorrect**. We never use all the data for training. Otherwise we couldn’t check the performance of our model as the model knows already all the data from the training process and is therefore heavily biased. 
✅ **Correct**. Yes, shuffling is often a good idea to prevent that, for example, all outliers are in the training set and not a single one in the test set which results in very high bias.
</details>
---

---

