---
title: "Quiz 2"
notion_id: "17074ffd-3319-8034-85bb-f556447352f9"
notion_url: "https://www.notion.so/Quiz-2-17074ffd3319803485bbf556447352f9"
exported_at: "2025-12-13T23:04:42.476716+00:00"
---

# Quiz 2

## Question 1
Given is the following function df:
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
Please mark **all** correct statements.
✅ The function **ds** returns the digit sum of a provided argument, if the argument is a *positive integer*.
✅ The function **ds** does not raise any error, if the provided argument is a *negative float*.
❌ The function **ds** returns the digit sum of a provided argument, if the argument is a *negative integer*.
❌ The function **ds** does never return any value.
✅ The function **ds** does not raise any error, if the provided argument is a *negative integer*.
❌ The function **ds** does not raise any error, if the provided argument is a *string*.
✅ The function **ds** returns the digit sum of a provided argument, if the argument has the value *0*.
❌ The function **ds** does not raise any error, if the provided argument is a *positive float*.

<details>
<summary>Explanation</summary>

> 💡 **[Logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2), [for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb) **
### Code Explanation
1. **Function Definition**:
- `def ds(number):` defines a function named `ds` that takes one parameter, `number`.
1. **Variable Initialization**:
- `digit_sum = 0` initializes a variable `digit_sum` to zero. This will be used to store the sum of the digits of the number.
1. **Conditional Check**:
- `if number >= 0:` checks if the provided `number` is greater than or equal to zero (i.e., non-negative).
- If true, it converts the number to a string and iterates over each character (digit) in the string.
- `digit_sum += int(digit)` converts each character back to an integer and adds it to `digit_sum`.
1. **Handling Negative Numbers**:
- If the number is negative, the function sets `digit_sum` to a string message indicating that negative numbers are not accepted.
1. **Return Statement**:
- `return digit_sum` returns the value of `digit_sum`, which could be the sum of digits or an error message.
### Answer Explanations
✅ **Correct**, if the input is a positive integer, the function calculates and returns the sum of its digits.
✅ **Correct**, the function does not explicitly handle floats, but it will not raise an error. Instead, it will treat the float as a negative number and return the error message.
❌ **Incorrect**, for negative integers, the function returns a string message, not the digit sum.
❌ **Incorrect**, the function always returns a value, either the digit sum or an error message.
✅ **Correct**, the function handles negative integers by returning a string message, not by raising an error.
❌ **Incorrect**, if a string is passed, the function will raise a `TypeError` because the comparison `number >= 0` is not valid between a string and an integer.
✅ **Correct**, if the input is `0`, the function will return `0` as the digit sum, since `0` is a non-negative integer.
❌ **Incorrect**, if a positive float is passed, the function will raise a `ValueError` when trying to convert the decimal point to an integer.
</details>
---
## Question 2
Given is the following code snippet:
```python
x = ''

for y in range(10):
    x = x + str(y)
```
What is the content of the variable **x** after the execution? Please ignore any line breaks.
❌ '45' 
❌ *Nothing because an error occurs.* 
❌ '123456789' 
❌ 45 
❌ 0 
❌ '012345678910' 
✅ '0123456789 

<details>
<summary>Explanation</summary>

> 💡 **[For-loop with range](/5b0832dbf9454eb1941b7632e68a9abb#1b3b7196171f4307856b5bcce1f11583), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb) **
### Code Explanation
1. `x = ''`
- This line initializes a variable `x` as an empty string. This means `x` starts with no characters in it.
1. `for y in range(10):`
- This line starts a loop that will run 10 times. The `range(10)` function generates numbers from 0 to 9 (inclusive).
1. `x = x + str(y)`
- Inside the loop, this line takes the current value of `x`, converts the current number `y` to a string using `str(y)`, and then concatenates it to `x`.
- This means that with each iteration of the loop, the current number `y` is added to the end of the string `x`.
Let's see what happens in each iteration of the loop:
- **First iteration (y = 0):** `x` becomes `'0'`
- **Second iteration (y = 1):** `x` becomes `'01'`
- **Third iteration (y = 2):** `x` becomes `'012'`
- **Fourth iteration (y = 3):** `x` becomes `'0123'`
- **Fifth iteration (y = 4):** `x` becomes `'01234'`
- **Sixth iteration (y = 5):** `x` becomes `'012345'`
- **Seventh iteration (y = 6):** `x` becomes `'0123456'`
- **Eighth iteration (y = 7):** `x` becomes `'01234567'`
- **Ninth iteration (y = 8):** `x` becomes `'012345678'`
- **Tenth iteration (y = 9):** `x` becomes `'0123456789'`
After the loop finishes, `x` contains the string `'0123456789'`.
### Answer Explanation
- ❌ **Incorrect**, because the loop adds all numbers from 0 to 9 to `x`, not just 4 and 5.
- ❌ **incorrect, **because the code runs without any errors.
- ❌ **Incorrect**, because the loop starts from 0, so `x` includes '0' at the beginning.
- ❌ **Incorrect**, because `x` is a string, not an integer, and it contains more than just '45'.
- ❌ **Incorrect, **because `x` accumulates all numbers from 0 to 9, not just '0'.
- ❌ **Incorrect,** because the loop stops at 9, so '10' is not included.
- ✅ **Correct,** because, as explained, the loop adds each number from 0 to 9 to `x`, resulting in this string.
</details>
---
## Question 3
The body/suite of a **for** loop can contain another **for** loop (a loop inside a loop).
❌ False
✅ True 

<details>
<summary>Explanation</summary>

> 💡 **[Nested loops](/5b0832dbf9454eb1941b7632e68a9abb#7cc1c66ebe7a4290927071b49aab1c29)**
Let's break down the concept of loops in programming to understand why the correct answer is **True**.
### Understanding Loops
A **loop** in programming is a way to repeat a block of code multiple times. The **for** loop is a common type of loop that iterates over a sequence (like a list, tuple, or string) and executes a block of code for each element in that sequence.
### Nested Loops
A **nested loop** is a loop inside another loop. This means you can have a **for** loop within the body of another **for** loop. This is useful when you need to perform repeated actions within repeated actions.
### Example of a Nested For Loop
Here's a simple example to illustrate a nested **for** loop:
```python
# Outer loop
for i in range(3):  # This loop will run 3 times
    print("Outer loop iteration:", i)

    # Inner loop
    for j in range(2):  # This loop will run 2 times for each iteration of the outer loop
        print("Inner loop iteration:", j)
```
### Code Explanation
1. **Outer Loop**:
- `for i in range(3):` - This loop will iterate 3 times, with `i` taking values 0, 1, and 2.
- `print("Outer loop iteration:", i)` - This line prints the current iteration of the outer loop.
1. **Inner Loop**:
- `for j in range(2):` - This loop will iterate 2 times for each iteration of the outer loop, with `j` taking values 0 and 1.
- `print(" Inner loop iteration:", j)` - This line prints the current iteration of the inner loop, indented for clarity.
Thus, the statement is correct because a **for** loop can indeed contain another **for** loop inside it. This is a common practice in programming, known as nesting, and is used to 
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
❌ The variable s contains the sum of all *positive integers* between 0 (included) and the entered number (excluded).
✅ The program will successfully terminate, i.e., will not raise an error, if a negative *int* value is entered.
✅ The variable s contains the sum of all *even positive integers* between 1 (excluded) and the entered number (included).
✅ The variable s contains the sum of all *even positive integers* between 0 (included) and the entered number (included).
✅ The program will successfully terminate, i.e., will not raise an error, if a positive *float* value is entered.

<details>
<summary>Explanation</summary>

> 💡 **[For-loop with range](/5b0832dbf9454eb1941b7632e68a9abb#1b3b7196171f4307856b5bcce1f11583), [modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c), [logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)**
### Code Explanation
1. `n = int(float(input("Please enter a positive number: ")))`
- This line prompts the user to enter a number.
- `input()` takes the user's input as a string.
- `float()` converts the input string to a floating-point number.
- `int()` then converts this floating-point number to an integer by truncating the decimal part.
- The result is stored in the variable `n`.
1. `s = 0`
- This line initializes the variable `s` to 0. This variable will be used to store the sum of certain numbers.
1. `for i in range(0, n+1):`
- This line starts a loop that iterates over numbers from 0 to `n` (inclusive).
- `range(0, n+1)` generates numbers starting from 0 up to and including `n`.
1. `if i % 2 == 0:`
- This line checks if the current number `i` is even. The `%` operator gives the remainder of the division of `i` by 2.
- If `i % 2` equals 0, then `i` is even.
1. `s += i`
- If the condition `i % 2 == 0` is true, this line adds the current even number `i` to the sum `s`.
### Answer Explanations
❌ **Incorrect**, the variable `s` only sums even numbers, not all positive integers. Additionally, the range includes the entered number, not excludes it.
✅ **Correct**, if a negative integer is entered, `n` will be negative, and `range(0, n+1)` will result in an empty range. The loop will not execute, and the program will terminate without errors.
✅ **Correct**, the loop starts at 0, but since 0 is not a positive integer, the sum effectively starts from the first even positive integer greater than 0. The loop includes the entered number if it is even.
✅ **Correct**, the loop includes 0 and sums all even numbers up to and including the entered number.
✅ **Correct**, a positive float will be converted to an integer, truncating the decimal part. The program will then execute without errors, as it only requires an integer for the loop.
</details>
---
## Question 5
How many loop iterations does the function call of
**range(7, 12, 3)**
produce if used for a *for* loop?
✅ 2 

<details>
<summary>Explanation</summary>

> 💡 **[Range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385)**
### Understanding `range(start, stop, step)`
The `range()` function in Python generates a sequence of numbers. It takes three arguments:
1. **start**: The starting value of the sequence (inclusive).
1. **stop**: The end value of the sequence (exclusive).
1. **step**: The difference between each number in the sequence.
### Analyzing `range(7, 12, 3)`
- **start = 7**: The sequence starts at 7.
- **stop = 12**: The sequence stops before reaching 12.
- **step = 3**: Each number in the sequence increases by 3 from the previous number.
### Sequence Generation
Let's see what numbers are generated by `range(7, 12, 3)`:
1. **First number**: 7 (start value)
1. **Second number**: 7 + 3 = 10
The next number would be 10 + 3 = 13, but since 13 is greater than the stop value 12, it is not included in the sequence.
### Loop Iterations
When you use this range in a `for` loop, it will iterate over the numbers 7 and 10. Therefore, there are **2 iterations** in total.
### Example Code
Here's how it would look in a `for` loop:
```python
for number in range(7, 12, 3):
    print(number)
```
- **First iteration**: `number` is 7, and it prints 7.
- **Second iteration**: `number` is 10, and it prints 10.
After these two iterations, the loop ends because there are no more numbers in the sequence.
### Conclusion
✅ The `range(7, 12, 3)` produces 2 numbers (7 and 10), resulting in 2 iterations in a `for` loop.
</details>
---

