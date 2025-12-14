---
title: "Quiz 2"
notion_id: "c53d7592-ee2b-4149-be8f-c22250cb9add"
notion_url: "https://www.notion.so/Quiz-2-c53d7592ee2b4149be8fc22250cb9add"
exported_at: "2025-12-13T23:16:08.155276+00:00"
---

# Quiz 2

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

