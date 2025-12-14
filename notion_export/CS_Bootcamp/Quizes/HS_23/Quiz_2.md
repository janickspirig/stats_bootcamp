---
title: "Quiz 2"
notion_id: "03fec2c1-9bb9-4d4d-8f7a-a6f60e57cf05"
notion_url: "https://www.notion.so/Quiz-2-03fec2c19bb94d4d8f7aa6f60e57cf05"
exported_at: "2025-12-13T23:21:29.806756+00:00"
---

# Quiz 2

## Question 1
Given is the following function ds:
```python
def ds(number):
    digit_sum = 0

    if number >= 0:
        for digit in str(number):
            digit_sum += int(digit)
    else:
        digit_sum = 'You provided a negative number. This function requires positive integers.'

    return digit_sum
```
Please mark all correct statements.
❌ The function **ds** returns the digit sum of a provided argument, if the provided argument is a *negative integer*.
❌ The function **ds** does not raise any error, if the provided argument is a *string*.
✅ The function **ds** does not raise any error, if the provided argument is a *negative integer*.
✅ The function **ds** does not raise any error, if the provided argument is a *negative float*.
✅ The function **ds** returns the digit sum of a provided argument, if the argument has the value *0*.
❌ The function **ds** does never return any value.
✅ The function **ds** returns the digit sum of a provided argument, if the argument is a *positive integer*.
❌ The function **ds** does not raise any error, if the provided argument is a *positive float*.

<details>
<summary>Explanation</summary>

> 💡 **[Logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2), [for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb) **
❌ **Incorrect**, because the function `ds` does not return the digit sum if the provided argument is a negative integer. Instead, it returns a message stating that the function requires positive integers.
❌ **Incorrect**, because the function `ds` will raise a `ValueError` if the provided argument is a string. This is because the function attempts to convert each character of the string into an integer, which is not possible if the string contains non-numeric characters.
✅ **Correct**, because the function `ds` does not raise any error if the provided argument is a negative integer. It simply returns a message stating that the function requires positive integers.
✅ **Correct**, because the function `ds` does not raise a `ValueError` if the provided argument is a negative float. It simply returns a message stating that the function requires positive integers.
✅ **Correct**, because the function `ds` will return `0` if the provided argument is `0`. This is because the digit sum of `0` is `0`.
❌ **Incorrect**, because the function `ds` always returns a value. It either returns the digit sum of the provided argument (if it's a non-negative integer), or a message stating that the function requires positive integers (if it's a negative integer).
✅ **Correct**, because the function `ds` will return the digit sum of the provided argument if the argument is a positive integer.
❌ **Incorrect**, because the function `ds` will raise a `ValueError` if the provided argument is a positive float. This is because the function attempts to convert each character of the string representation of the float into an integer, which is not possible for the decimal point.
</details>
---
## Question 2
How many loop iterations does the function call of
**range(6, 13, 2)**
produce if used for a for loop?
**4**

<details>
<summary>Explanation</summary>

> 💡 **[Range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385)**
The `range()` function in Python is used to generate a sequence of numbers over time. You can decide where that sequence of numbers will begin and end as well as how big the difference will be between one number and the next. `range()` takes three arguments:
1. **start**: Starting number where the sequence of numbers will start (including this number).
1. **stop**: Generate numbers up to (exlucing) this number.
1. **step**: Difference between each number in the sequence.
In the function call `range(6, 13, 2)`,
- `6` is the start number
- `13` is the stop number
- `2` is the step
This will generate a sequence of numbers starting from 6 up to but not including 13, with a step of 2. So, the sequence of numbers will be `6, 8, 10, 12`.
If you use this in a for loop, it will iterate 4 times, once for each number in the sequence. That's why the correct answer is 4. Here is how it would look in a for loop:
```python
for i in range(6, 13, 2):
    print(i)
```
This will output:
```plain text
6
8
10
12
```
So, you can see it iterates 4 times.
</details>
---
## Question 3
The body/suite of a for loop can contain another for loop (a loop inside a loop).
❌ False
✅ True

<details>
<summary>Explanation</summary>

> 💡 **[Nested loops](/5b0832dbf9454eb1941b7632e68a9abb#7cc1c66ebe7a4290927071b49aab1c29)**
✅ **True**. This is called a nested loop, where you can have a `for` loop inside another `for` loop. This is often used for iterating over multi-dimensional data structures like lists of lists, matrices etc. Here's an example:
```python
for i in range(3): # outer loop
    for j in range(3): # inner loop
        print(i, j)
```
In this example, for each iteration of the outer loop, the inner loop runs completely.
So for `i = 0`, `j` will take values 0, 1, 2 in separate iterations.
Then for `i = 1`, `j` will again take values 0, 1, 2 and so on.
This will result in 9 (3 * 3) print statements in total.
</details>
---
## Question 4
Given is the following program. After the user has entered a value, the program has been executed completely - if possible, i.e., if no error has been raised.
```python
n = int(float(input("Please enter a positive number: ")))
s = 0

for i in range(0, n+1):
    if i % 2 == 0:
        s += i
```
Please mark all correct answers.
❌ The variable **s** contains the sum of all *positive* integers between 0 (included) and the entered number (excluded).
✅ The program will successfully terminate, i.e., will not raise an error, if a negative *int* value is entered.
✅ The variable s contains the sum of all *even* positive *integers* between 0 (included) and the entered number (included).
✅ The program will successfully terminate, i.e., will not raise an error, if a positive *float* value is entered.
✅ The variable **s** contains the sum of all *even* *positive* *integers* between 1 (excluded) and the entered number (included).

<details>
<summary>Explanation</summary>

> 💡 **[For-loop with range](/5b0832dbf9454eb1941b7632e68a9abb#1b3b7196171f4307856b5bcce1f11583), [modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c), [logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)**
❌ **Incorrect**, because the variable `s` contains the sum of all even positive integers between 0 (included) and the entered number (included), not all positive integers. The condition `if i % 2 == 0:` checks if the number is even before adding it to `s`.
✅ **Correct**, because the program will successfully terminate if a negative int value is entered. The `range(0, n+1)` will simply create an empty sequence if `n` is negative, and the loop will not be executed at all.
✅ **Correct**, because the variable `s` indeed contains the sum of all even positive integers between 0 (included) and the entered number (included). This is because the loop goes from 0 to `n` (inclusive) and only adds `i` to `s` if `i` is even.
✅ **Correct**, because the program will successfully terminate if a positive float value is entered. The `float(input(...))` will convert the input to a float, and the `int(...)` will then convert this float to an integer.
✅ **Correct**, because the variable `s` contains the sum of all even positive integers between 0 (included) and the entered number (included), not starting from 1 (excluded). The loop starts from 0, not 1.
</details>
---
## Question 5
Given is the following code snippet:
```python
x = ''
for y in range(10):
    x = x + str(y)
```
What is the content of the variable x after the execution? Please ignore any line breaks.
❌ 0
✅ '0123456789'
❌ *Nothing because an error occurs.*
❌ 45
❌ '45'
❌ '123456789'
❌ '012345678910'

<details>
<summary>Explanation</summary>

> 💡 **[For-loop with range](/5b0832dbf9454eb1941b7632e68a9abb#1b3b7196171f4307856b5bcce1f11583), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb) **
❌ **Incorrect**, This would be the case if the loop only ran once, but it runs 10 times.
✅ **Correct**, let's see why:
The code is a simple for loop that iterates over a range of 10 numbers (from 0 to 9). For each iteration, it converts the current number `y` to a string using the `str()` function and then appends it to the string `x`.
Here's how it works step by step:
1. In the first iteration, `y` is 0.
After converting it to a string and appending it to `x`, `x` becomes '0'.
1. In the second iteration, `y` is 1.
After converting it to a string and appending it to `x`, `x` becomes '01'.
1. This process continues until `y` is 9, at which point `x` becomes '0123456789'.
<details>
<summary>Breakdown per loop-run</summary>

| Run | Value of `y` | Value of `x` |
| --- | --- | --- |
| 1 | 0 | '0' |
| 2 | 1 | '01' |
| 3 | 2 | '012' |
| 4 | 3 | '0123' |
| 5 | 4 | '01234' |
| 6 | 5 | '012345' |
| 7 | 6 | '0123456' |
| 8 | 7 | '01234567' |
| 9 | 8 | '012345678' |
| 10 | 9 | '0123456789' |
</details>
❌ **Incorrect**, there is no error in the code.
❌ **Incorrect**, the code doesn't add the numbers, it appends them as strings.
❌ **Incorrect**, the range starts from 0, not 1.
❌ **Incorrect**, the range ends at 9, not 10.
</details>
---

