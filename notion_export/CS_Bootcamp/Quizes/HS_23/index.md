---
title: "HS 23"
notion_id: "3017a608-91f4-4bcd-830c-16a656ee3ae1"
notion_url: "https://www.notion.so/HS-23-3017a60891f44bcd830c16a656ee3ae1"
exported_at: "2025-12-13T23:21:05.011458+00:00"
---

# HS 23

---
📄 **[Quiz 1]** (subpage)
## Question 1
Can you add (+) a variable of type **string** to a variable of type **float**?
❌ Yes but the resulting data type can't be inferred.
❌ It depends on the content of the **string** variable.
✅ No.
❌ Yes, and the result is of type **float**.

<details>
<summary>Explanation</summary>

> 💡 **[Type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb)**
In Python, you cannot add a variable of type string to a variable of type float. This is because they are different data types, and Python does not implicitly convert one type to another.
 Here is an example:
```python
str_var = "Hello"
float_var = 1.5
result = str_var + float_var  # This will raise a TypeError
```
This will raise a `TypeError: can only concatenate str (not "float") to str`.

Let's take a look at the options:

❌ **Incorrect**, because Python doesn't allow adding a string to a float without explicit conversion.
❌ **Incorrect**, because regardless of the content of the string, it cannot be added to a float.
 ✅ **Correct**, because Python doesn't allow adding a string to a float without explicit conversion.
❌ **Incorrect**, because Python doesn't allow adding a string to a float without explicit conversion. Even if the string contains a number, Python treats it as a string, not a number.
</details>
---
<!-- Unsupported block type: unsupported -->
## Question 2
Given is the arithmetic Modulo operator **%** from Python. What is the result of the following computation stored in the variable z?

z = 35 % 10

**5**

<details>
<summary>Explanation</summary>

> 💡 **[Modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c)**
The Modulo operator **`%`** in Python returns the remainder of a division. In this case, `35 % 10` means "what is the remainder when 35 is divided by 10?"

The division of 35 by 10 is 3 with a remainder of 5. So, when we use the Modulo operator, it ignores the quotient (3 in this case) and returns only the remainder.
Therefore, `z = 35 % 10` will give `z = 5`.
</details>
---
## Question 3
Given is a simple CPU with two 3-bit registers and the following instructions:

CPU
| Instruction  | Explanation |
| --- | --- |
| 00nnn | **Insert**. The 3-bit binary number nnnb is inserted into register x. |
| 01xy  | **Copy**. The content of register x is copied into register y. |
| 10xy | **Add**. The result of R[x] + R[y] is stored in register y. |
| 11x Clear. | **The** content of register x is set to 000. |
Please write a program using the available instructions. The program should **insert** the value 2 (in the decimal system) into register 0, **copy** the value to register 1, then **add** the registers and store the result into register 0, and finally **clear** register 1.
For easier readability you may use one blank between each instruction (e.g., 110 1011 0110). Alternatively, you may use no blanks at all (e.g., 11010110110). Do NOT insert spaces within instructions.

The program is:
**00010 0101 1010 111**

<details>
<summary>Explanation</summary>

> 💡 **[CPU instructions](/4e55bc27409940e98f9a060821d07644)**
The correct answer is `000100 0101 1010 111`.
Let's break down why:
1. `00010`: This instruction is **Insert**. The 3-bit binary number `010` (which is 2 in decimal) is inserted into Register 0.
| Register 0 | Register 1 |
| --- | --- |
| `010` |  |
1. `0101`: This instruction is **Copy**. The content (`010`) of register `x` (0 in this case) is copied into Register `y` (1 in this case).
| Register 0 | Register 1 |
| --- | --- |
| `010` |  |
|  | `010` |
1. `1010`: This instruction is **Add**. The result of `R[x]` (0 in this case) `+ R[y]` (1 in this case) is stored in Register `y` (0 in this case).
Adding up `010` and `010` (decimal: 2+2) is equal to `100` (decimal: 4).
| Register 0 | Register 1 |
| --- | --- |
| ~~`010`~~ |  |
|  | `010` |
| `100` |  |
1. `111`: This instruction is **Clear**. The content of register x (1 in this case) is set to `000`. T
| Register 0 | Register 1 |
| --- | --- |
| ~~`010`~~ |  |
|  | ~~`010`~~ |
| `100` |  |
|  | `000` |
</details>
---
## Question 4
Which data type do the variables x, y, and z contain?
```python
x = "22"
y = int(x) + 2
z = int(x) / 3
```
Drag and drop the variables to their respective data type category.

**int**
y

**str**
x

**float**
z

<details>
<summary>Explanation</summary>

> 💡 **[Type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb), [division](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a)**
The data type of a variable in Python is determined by the type of data the variable holds.
Let's look at the variables one by one:
- **`x = "22"`**`
`The variable `x` is assigned a string ("22"). Even though "22" looks like a number, it is enclosed in quotes, which makes it a string. Hence, `x` is of type `str`.
- **`y = int(x) + 2`**`
`Here, the `int(x)` function converts the string `x` into an integer. The result (22) is then added to 2, resulting in another integer (24). Therefore, `y` is of type `int`.
- **`z = int(x) / 3
`**Again, `int(x)` converts the string `x` into an integer (22). However, when this integer is divided by 3, the result is a floating-point number (22/3 = 7.3333...). So, `z` is of type `float`.
</details>
---
## Question 5
Which values do the variables x and z have after the execution of the following script?
```python
x = 42
y = True
z = not y

if y:
	x = x / 2
	y = not y
else:
	x = x * 2

if x < 42:
	z = not y
else:
	z = not z
```

❌ y = False, z = False
❌ y = True, z = False
❌ y = True, z = True
✅ y = False, z = True
❌* None of the above.*

<details>
<summary>Explanation</summary>

> 💡 **[Logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)**
Let's break down the code:
- Line 1: `x = 42` assigns the value **42** to the variable `x`.
- Line 2: `y = True` assigns the value **True** to the variable `y`.
- Line 3: `z = not y` assigns the opposite of `y` (which is **True**) to `z`, so `z` becomes **False**.
- Line 5: Since `y` is **True**, the code inside the `if` block is executed (Line 6-7).
- Line 6: `x` is divided by 2, becoming **21**
- Line 7: `y` is changed to the opposite of its current value (**True**), becoming **False**
- Line 11: Since `x` (**21**) is less than 42, the code inside the `if` block is executed
- Line 12: `z` is changed to the opposite of `y` (which is **False**), so `z` becomes **True**
So, after the execution of the code, `y` is **False** and `z` is **True**.
</details>
---
## Question 6
The following can be seen on the famous St. Gallen binary clock:
[Embed]()
What time is it there (in hours:minutes:seconds)?

❌ 08:10:59
❌ 05:06:14
❌ 08:12:59
✅ 05:06:45

<details>
<summary>Explanation</summary>

> 💡 **[Binary numbers](/2b21ebb6314545d48382bb68713e5145)**
**Hours**
| Position | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| Binary | 0 | 0 | 1 | 0 | 1 |
| Calculation | 0 * 2^4 = 0 | 0 * 2^3 = 8 | 1 * 2^2 = 4 | 0 * 2^1 = 0 | 1 * 2^0 = 1 |
| Decimal | 0 | 0 | 4 | 0 | 1 |
Sum of {4, 1} = **5**
---
**Minutes**
| Position | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 0 | 0 | 0 | 1 | 1 | 0 |
| Calculation | 0 * 2^5 = 0 | 0 * 2^4 = 16 | 0 * 2^3 = 8 | 1 * 2^2 = 4 | 1 * 2^1 = 2 | 0 * 2^0 = 0 |
| Decimal | 0 | 0 | 0 | 4 | 2 | 0 |
Sum of {4, 2} = **6**
---
**Seconds**
| Position | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 1 | 0 | 1 | 1 | 0 | 1 |
| Calculation | 1 * 2^5 = 32 | 0 * 2^4 = 0 | 1 * 2^3 = 0 | 1 * 2^2 = 0 | 0 * 2^1 = 0 | 1 * 2^0 = 1 |
| Decimal | 32 | 0 | 8 | 4 | 0 | 1 |
Sum of {32, 8, 4, 1} = **45**
</details>
---
## Question 7
Given is the following snippet to compute the volume of a pyramid:
```python
b = 3.0
h = 2.0

volume = (1/3) * b ** 2 * h

print("The volume is", volume)
```
Mark all correct statements regarding this snippet.
❌ Generally, the computation would also work if we put in a string instead of a float for the variables **b** and **h**.
✅ The computation is correct.
❌ The computation makes sure that the values of **b** and **h** are valid.

<details>
<summary>Explanation</summary>

> 💡 **[Math calculations](/5b0832dbf9454eb1941b7632e68a9abb#c5ed1b94ab75447ba1228022dbea677f)**
❌ **Incorrect**, because in Python, mathematical operations like multiplication and exponentiation cannot be performed on strings.
If we try to replace the float values of `b` and `h` with strings, we would get a `TypeError`. For example, if `b = "3.0"` and `h = "2.0"`, the line `volume = (1/3) * b ** 2 * h` would cause an error.
✅ **Correct**, the computation is indeed correct. The formula for the volume of a pyramid is `(1/3) * base_area * height`. Here, `base_area` is approximated as `b ** 2` (which assumes a square base), and `height` is `h`. Hence, the calculation in line 4 correctly computes the volume of the pyramid.
❌ **Incorrect**, the computation does not validate the values of `b` and `h`. There are no checks in place to ensure that `b` and `h` are non-negative, which they should be for the physical dimensions of a pyramid. If either `b` or `h` were negative, the computation would still proceed, resulting in a negative volume, which doesn't make sense in the physical world.
</details>
---
## Question 8
Can you add a variable using the + operator of type int to a variable of type float?
✅ Yes.
❌ Depends on the content of the variables.
❌ No.

<details>
<summary>Explanation</summary>

> 💡 **[Data types](/5b0832dbf9454eb1941b7632e68a9abb#3684ce5c0e674ca5987a33acfe90011e)**
✅ **Correct**, in Python, you can add an integer to a float. This is because Python implicitly converts the integer to a float during the addition operation. This is called type coercion.
Here's a simple example:
```python
int_var = 3
float_var = 2.5
sum_var = int_var + float_var
print(sum_var)  # Output: 5.5
```
In this case, the integer **`3`** is converted to a **`3.0`** (a float) before the addition operation. So, **`3.0 + 2.5`** equals **`5.5`**.
❌ **Incorrect**, because in Python, you can add any integer to any float, regardless of their values.
❌ **Incorrect**, because as explained above, Python allows adding integers to floats.
</details>
---
📄 **[Quiz 2]** (subpage)
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

📄 **[Quiz 3]** (subpage)
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

📄 **[Quiz 4]** (subpage)
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
📄 **[Quiz 5]** (subpage)
## Question 1
Please assume that the following program has been executed without any error:
```python
class Vehicle:
    def __init__(self, brand, model, mileage=0, condition=100):
        # Please assume for the __init__ method that the variables
        # self._brand, self._model, self._mileage, self._condition have
        # been correctly initialized with the according arguments

        # please also assume there are getter-methods for brand, model, mileage and
        # condition that just return self._brand, self._model, self._mileage and
        # self._condition

    def drive(self, distance):
        if distance >= 0:
            self._mileage += distance
            self._condition -= self.condition * distance / 10000
            return
        raise ValueError('distance must be a positive number, you have entered', distance)

    def service(self):
        if self._condition + 10 <= 100:
            self._condition += 10
        else:
            self._condition = 100

    def __str__(self):
        return f"{self.brand} {self.model} with {self.mileage} km, a condition of {self.condition}%"

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.mileage}, {self.condition})"

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, mileage=0, condition=100, battery_health=100):
				# Please assume for the __init__ method that the attributes 
				# are also present in the super class are forwarded via super().__init__(...)
				# and that self.battery_health has been initialized with the according argument
		
		# please also assume there is a getter-method for battery_health
		# that just returns self._battery_health

		@battery_health.setter
		def battery_health(self, health_level):
		    if 0 <= health_level <= 100:
		        self._battery_health = health_level
		    else:
		        raise ValueError('health_level must be in the range of 0–100, you have entered', health_level)
		
		def drive(self, distance):
		    if distance >= 0:
		        self._mileage += distance
		        self._condition -= self.condition * distance / 20000
		        return self._mileage
		    else:
		        raise ValueError('distance must be a positive number, you have entered', distance)
		
		def __str__(self):
		    return f"{super().__str__()}, and a battery health level of: {self.battery_health}"
		
		def __repr__(self):
		    return f"ElectricVehicle('{self.brand}', '{self.model}', {self.mileage}, {self.condition}, {self.battery_health})"
		
v = Vehicle('Opel', 'Ascona')
e = ElectricVehicle('Fiat', '500e')
```
Please mark all correct statements regarding this program:
✅ The code *e.drive(2100)* returns 2100.
❌ After executing *v.service()* the code v.condition will return 110.
✅ Trying to execute *e2 = ElectricVehicle(brand='Tesla', model='Model S', mileage=65342, condition=80, battery_health=101)* raises an error.
✅ *e* is an instance of ElectricVehicle.
❌ Trying to execute *e.service()* raises an error.
❌ In the __init__ method of Vehicle we should not initialize *self._model* but rather *self.model*
❌ Vehicles inherits from ElectricVehicle
✅ The code *e = ElectircVehicle(’Fiat’, ‘500e’)* internally calls the __init__ method of Vehicle as well as the __init__ method of ElectricVehicle.

<details>
<summary>Explanation</summary>

> 💡 **[OOP](/83479909f70b47e491c55c9a6178291a), [inheritance](/76bc8240b5c44034a4fde93b7d3158ff)**
✅ **Correct**, `e.drive(2100)` indeed returns 2100. This is because the `drive` method of the `ElectricVehicle` class, which `e` is an instance of, returns `self._mileage` after adding the `distance` to it.
❌ **Incorrect**, `v.service()` will not make `v.condition` return 110. The `service` method of the `Vehicle` class increases the `condition` by 10 only if it's less than 90 (because the condition cannot exceed 100). If it's 100 or more, it just sets it to 100.
✅ **Correct**, trying to execute 
```python
e2 = ElectricVehicle(
		brand='Tesla',
		model='Model S',
		mileage=65342,
		condition=80,
		battery_health=101
)
```
will indeed raise an error. This is because the `battery_health` setter method in the `ElectricVehicle` class raises a `ValueError` if the `health_level` is not between 0–100.
✅ **Correct**, `e` is an instance of `ElectricVehicle`. This is clear from the line `e = ElectricVehicle('Fiat', '500e')`.
❌ **Incorrect**, trying to execute `e.service()` will not raise an error. This method is inherited from the `Vehicle` class and it increases the `condition` by 10 if it's less than 90 and sets it to 100 otherwise.
❌ **Incorrect**, in the `__init__` method of `Vehicle` we should indeed initialize `self._model`. The underscore prefix is a convention in Python indicating that the attribute is intended for internal use (although it can still be accessed directly). The `self.model` would refer to a property or a getter method, not the attribute itself.
❌ **Incorrect**, `Vehicle` does not inherit from `ElectricVehicle`. It's the other way around: `ElectricVehicle` is a subclass of `Vehicle`.
✅ **Correct**, the code `e = ElectricVehicle('Fiat', '500e')` indeed internally calls the `__init__` method of both `Vehicle` and `ElectricVehicle`. This is because `ElectricVehicle` is a subclass of `Vehicle` and its `__init__` method calls `super().__init__(...)` to execute the `__init__` method of the superclass.
</details>
---
## Question 2
One task in the assignment was to implement the *method* **.heal(self, other)** of the class **HealingSuperhero**. HealingSuperhero inherits from **Superhero**.
Let's assume there are two instances of Superhero: **danny** and **hulk**, while **danny** is also an instance of **HealingSuperhero**.
When calling **danny.heal(hulk)**, which one of the following statements is correct?
✅ The **powerlevel** of only the instance **hulk** will be increased, depending on how the *receive_healing()* method is implemented.
❌ The execution stops with an error message because the method **.heal(self, other)** expects two parameters and only one was given.
❌ An error occurs because it is important on which instance the **.heal** method is called. The correct call would have been **hulk.heal(danny)**.
❌ The **powerlevel** of both instances will be increased according to the implemented rule.
❌ The **powerlevel** of **danny** will be increased, depending on how the *receive_healing()* method is implemented.
❌  It is not guaranteed to work because the **powerlevel** on one or both instances could be 0, which will lead to an error (*DivisionByZero*).

<details>
<summary>Explanation</summary>

> 💡 **[Class inheritance](/c991314990fa47e19addaf16235213db)**
Before reviewing the statements let’s look at the relevant code snippet from the assignment:
```python
class HealingSuperhero(Superhero):
		def **init**(self, name, year_of_birth, alias, powerlevel):
				super().**init**(name, year_of_birth, alias, powerlevel)

def heal(self, other):
    other.powerlevel += self.powerlevel
```
We can see that class `HealingSuperhero` inherits from `Superhero` and thus has available all attributes and methods that are defined on the `Superhero` class. 
Also, there is the `.heal()` method which credits the powerlevel of the superhero the method is being called on to the other superhero that is provided as value for the `other` parameter.
For example, we have **hulk** with powerlevel 10 and **danny** with powerlevel 20. 
Now when we call `danny.heal(hulk)`, the new powerlevel of **hulk** will be:
`hulk.powerlevel = hulk.powerlevel + danny.powerlevel`
`hulk.powerlevel = 10 + 20 = 30` 
The powerlevel of **danny** will remain unchanged.
✅ **Correct**, the **powerlevel** of **hulk** will be increased. The second part of the statement, about the *receive_healing()* method is a bit confusing as in the assignment this method was not implemented.
❌ **Incorrect,** because the method `heal(self, other)` does have two parameters and both are provided when calling `danny.heal(hulk)`:
- `self` refers to the instance/superhero on which the method is being called (**danny**)
- `other` refers to the other instance/superhero being passed into the method (**hulk**)
❌ **Incorrect**, because **hulk** is an instance of `Superhero`, not `HealingSuperhero`, therefore **hulk** doesn't have the `.heal()` method. The `.heal()` method can only be called on an instance of `HealingSuperhero`, which **danny** is.
This is because `HealingSuperhero` (child class) inherits from `Superhero` (parent class). Thus, all attrbitues and methods defined on `Superhero` class are inherited and available on `HealingSuperhero` as well.
However, methods and attributes defined on the class `HealingSuperhero` are not available for class `Superhero`.
❌ **Incorrect**, because the `.heal()` method increases the powerlevel of the instance passed as the `other` parameter (**hulk**), not the instance on which the method is being called.
❌ **Incorrect**, the powerlevel of **hulk**, the other superhero, will be increased.
❌ **Incorrect** because there's no division operation happening inside the `.heal()` method.

</details>
---
## Question 3
Which of the following statements are True in the context of **object orientation**? Please mark all True statements:
✅ A subclass can inherit attributes and methods from its superclass.
✅ Objects are instances of classes.
✅ An object that is an instance of a subclass is always also an instance of the subclass' superclass.
❌ Private attributes (e.g., *_variablename*) cannot be directly manipulated in Python by client code. Instead, changing those requires respective setter-methods.
❌ A method in a subclass must not have the same name as a method in the respective superclass. Otherwise it is not clear, which method to execute.
❌ A method, like python functions, always needs to have a return statement. A *print()* is not sufficient.
✅ In Python, classes may inherit from their superclasses over multiple levels of a class hierarchy.

<details>
<summary>Explanation</summary>

> 💡 **[Class inheritance](/c991314990fa47e19addaf16235213db), [private attributes](/83479909f70b47e491c55c9a6178291a)**
✅ **Correct**, a subclass can inherit attributes and methods from its superclass. This is a fundamental aspect of inheritance in object-oriented programming. For example:
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido")
print(fido.name)  # Fido
fido.bark()  # Woof!

```
Here, `Dog` is a subclass of `Animal` and inherits the `name` attribute from it.
✅ **Correct**, objects are instances of classes. An "instance" is a specific object that is created from a particular class. For example, in the code above, `fido` is an instance of the `Dog` class.
✅ **Correct**, an object that is an instance of a subclass is always also an instance of the subclass's superclass. This is due to the inheritance relationship between the subclass and the superclass. In Python, you can use the `isinstance()` function to confirm this:
```python
print(isinstance(fido, Dog))  # True
print(isinstance(fido, Animal))  # True
```
❌ **Incorrect**, private attributes in Python (denoted by a single underscore, e.g., `_variablename`) can be directly manipulated by client code. The underscore is a convention to indicate that the attribute is intended to be private, but Python does not enforce this. So, **although** an attribute has been declared as **private**, it can **still** be accessed **from outside** the class, i.e., by client code.
❌** Incorrect**, a method in a subclass can have the same name as a method in its superclass. This is called method overriding. The subclass's method will be called instead of the superclass's method when the method is invoked on an instance of the subclass, due to [**Polymorphism**](/1847b80cf96b485da5725e3cd1b35ca9).
```python
class Animal:
    def __init__(self, name):
        self.name = name
		def bark(self):
		        print("WUUUUF!")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido")
fido.bark()  # Woof!
```
In the example above we can see that both classes, **Animal** and **Dog** have a method `bark()`. When we call the `bark()` method for **fido**, the one from the **Dog** class is executed.
❌ **Incorrect**, a method, like Python functions, does not always need to have a return statement. If no return statement is present, the function will return `None` by default.
✅ **Correct**, in Python, classes can inherit from their superclasses over multiple levels of a class hierarchy. This is known as multilevel inheritance. For example, you might have a `Mammal` class that inherits from `Animal`, and then a `Dog` class that inherits from `Mammal`. Each level of the hierarchy can add or override attributes and methods.
</details>
---
## Question 4
Please assume that FCS_student1 is an instance of the class Superhero from the Assignment. What is the return value of the following code snippet:
*isinstance(FCS_student1, object)*
❌ An error occurs.
❌ Without further information, the return value cannot be determined.
✅ True
❌ False
<details>
<summary>Explanation</summary>

> 💡 **[Type checking](/5b0832dbf9454eb1941b7632e68a9abb#6f8e8203d09a4c3aafa6f5d78119fe00)**
❌ **Incorrect**, because `isinstance()` is a built-in function in Python that checks if an object is an instance of a specified class or a subclass thereof. It doesn't raise an error in this case.
❌ **Incorrect**, this is incorrect because, as explained earlier, all classes in Python are derived from `object`. Therefore, any instance of any class is also an instance of `object`.
✅ **Correct**. In Python, all classes, including user-defined classes, are derived from the base class `object`. Therefore, an instance of any class in Python is also an instance of the `object` class.
Here, `FCS_student1` is an instance of the `Superhero` class. Since `Superhero` is a class and all classes in Python are derived from `object`, `FCS_student1` is also an instance of `object`. Hence, `isinstance(FCS_student1, object)` returns `True`.
Let's understand this with a simple example:
```python
class Superhero:
    pass

FCS_student1 = Superhero()

print(isinstance(FCS_student1, object))  # Outputs: True
```
In this example, `FCS_student1` is an instance of the `Superhero` class. When we use `isinstance()` to check if `FCS_student1` is an instance of `object`, it returns `True`.
❌ **Incorrect**, because `FCS_student1` is indeed an instance of `object` as explained above.
</details>
---



📄 **[Quiz 6]** (subpage)
## Question 1
Consider the following code that implements part of Assignment 6.
The returned list of restaurants should contain all restaurants in a given radius that are open at the moment.
Assume that "abcd" is a valid API key.
Your colleague asks you for feedback on this code.
What do you tell them?
```python
api_key = 'abcd'
url = '<https://api.yelp.com/v3/businesses/search>'

headers = {'Authorisation': 'Bearer ' + api_key}

restaurants = []

params = {}
params['latitude'] = x
params['longitude'] = y
params['opening_times'] = opening_times
params['radius'] = radius
params['open_now'] = false
params['categories'] = "restaurants"

r = requests.get(url, params=params)
```
❌ The code works perfectly.
❌ The variable *opening_times* in line 11 needs to be cast to a string. Otherwise an error will occurr.
❌ The headers-parameter in line 16 is missing, it must look like this:
`r = requests.get(url, params=params, headers)`
❌ You need to use a **PUT** request in line 16.
❌ The parameter *open_now* needs to be set to *true*.
`params['open_now'] = true`
✅ The headers-parameter in line 16 is missing, it must look like this:
`r = requests.get(url, params=params, headers=headers)`

<details>
<summary>Explanation</summary>

> 💡 **[HTTP methods](/f6bdc16ceadd474d895561e3c6762d42), [HTTP request fields](/305c770201f94279bfd468d86c733ae6#d4dd954760524dca8de4bdfe52cf821d)**
❌ **Incorrect**,** **the code does not work perfectly. There are missing headers in the request.
❌ **Incorrect**, the variable `opening_times` in line 11 doesn't need to be cast to a string as the [Yelp API](https://docs.developer.yelp.com/reference/v3_business_search) doesn't have a parameter for `opening_times` in the first place, so this line of code is unnecessary and incorrect.
❌ **Incorrect**, the headers-parameter is missing in the request, however we can not include the parameter like this as [positional arguments cannot follow keyword arguments](/288f8ada9a05473a8fa7c7a306512db5).
❌ **Incorrect**, we are fetching/requesting resources from the Yelp server, thus we must sue a GET request.
❌ **Incorrect**, open_now parameter expects a boolean to be passed and `false` is a boolean value. So there is no correction needed here.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cf83aa91-009e-4922-b7e6-d11c4db32690/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F3NUSEQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGtFvw9qn8b8bYhL82c9%2F4FaD9L9iv4kFCkE2Pd%2F3GK%2BAiAJXI9Dp8e74MFYlyemVWnaQDUtBz5wKpePOSVnlvIsqSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMTiaWmLz8W2rLqX4HKtwD%2FCjNlhO6bA4J2bNcbiKyw3uaKlNBrsOyfhz5tDpJiBSgeQ5H4x5k%2FyZ0scDdiRQSMhaTxop0guXLXsvC%2Fwh8YwzLInn2dPTdNHt32nnsiYD%2FP3f%2FqWMOS2hjCT%2FTHRDTtriQAp4ymJvJm2oJDScISab9vy2ZZ31A8f%2BrYpdVultJ5IoO84BtRRdVipzsbsTK%2BJ4w7VZG55dDcTlfPqf6A8e8a71%2BE1%2FDSDN0jmvIrBh7VYJ2Hg5NUUi2aHDe4eTz%2BpJSvHkSzhl1YCM0oj%2BoQf6G3NACZPSgi9uQ0dAW%2FlEFhMR8%2FowGAfj87xxsH9P8gX0KejxCtzW88ba%2FmiY1qIoCEXi%2B9LPTR25wtb3qDxm9lk4bLGfMD1QvTIsjJ1xRQ7G%2BqzPyyyQv0nLpAXOXULTKeimujnGY07v3cAaQOZN9tIEWu61%2FFAKoKV3wMVq5KcA1AbF2V4jxPShbctS%2FXjZ8K5qJqwGOLGeHlwW0hlxYHXrsAtmYb%2BsLaNRTe%2ByOo5H2yQTAayzwVTWH92%2F147LAQLGPlJrkVMT9B4Cs6pWon9EEySSwioEb1AF8jXgzHV5DMnN66B52t24tf8O91OmOlk6vZbliUUtFACVilS3hd4%2Bzayp4fACt2vMwjM73yQY6pgGQn8wbRy7WsYaJa1TDdUDLs1HkCXu7b017Z7SW6kvQ0ZJ4qzjhAOBt4RPzvjf8shqYGB6BnEYRcdOKSVu3rxq%2FqUe0pM8z0DdlsVtwWMfWadB59sn%2FR3tA%2BqNIUtgLKoGqIDA3kMiq%2FfgVeswJewFRHXxtwxz4gLijG3QoQncslEjR1rdIjTiny3QOx4ZJZ3l%2FpDr29vWx7UWRM%2Fdf%2BWr0u6NME5ep&X-Amz-Signature=cc506947fdc8199822851b3887ddf561cccf17f6debf8e608d5f7b2f1d7ef5b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
✅ **Correct**, the header includes our API key, thus to have the Yelp server accept and process our request wer must include the headers in the request.
</details>
---
## Question 2
Consider the following code that implements parts of Assignment 6 and mark all correct statements.
```python
def find_top10_restaurants_for_trip(origin, destination, departure_date, departure_time, radius):
    limit = 10
    connection = find_connection(origin,
                                 destination,
                                 departure_date,
                                 departure_time)
    restaurants = find_restaurants(
        connection.destination_x,
        connection.destination_y,
        connection.get_unix_arrival_time(),
        radius
    )
    rests_sorted = sorted(restaurants, key=lambda tup: tup[1], reverse=False)
    return rests_sorted[:limit]
```
❌ In Assignment 6, this code leads to the issuing of two HTTP POST requests (to *transport.opendata.ch* and to *api.yelp.com*, respectively)
✅ In line 13, the parameter *reverse* needs to be set to true, otherwise the function will return the 10 worst rated restaurants instead of the 10 best ones.
❌ In Assignment 6, this code generally would not work because the return datatypes from *transport.opendata.ch* are not compatible with *api.yelp.com.*
✅ In Assignment 6, this code leads to the issuing of two HTTP GET requests (to *transport.opendata.ch* and to *api.yelp.com*, respectively)
❌ In line 3, *radius* needs to be added to the function *find_connection()* as an additional parameter after *departure_time*.

<details>
<summary>Explanation</summary>

> 💡 **[sorted function](/5b0832dbf9454eb1941b7632e68a9abb#7c022c5cc1a647d58ba1a7e82406c3e6), [access elements in nested lists (or tuples)](/5b0832dbf9454eb1941b7632e68a9abb#8526be0c72d1432c83067d8315535bd0)**
❌ **Incorrect**, in the context of this code, we don't see any HTTP POST requests being issued. The functions `find_connection` and `find_restaurants` might be issuing HTTP requests, but we cannot infer the type of request (GET or POST) from the given information.
✅ **Correct**, the `sorted` function in Python sorts in ascending order by default. If we want to sort in descending order (which we would for the top 10 rated restaurants), we need to set `reverse=True`.
❌ **Incorrect**, we cannot infer the compatibility of return datatypes from the given code. The functions `find_connection` and `find_restaurants` are expected to handle any necessary data type conversions.
✅ **Correct**, in both cases we request data from a server. First, we request the next connections and seocnd information about restaurants at the destination. Thus, two GET requests are issued.
❌ **Incorrect**, the `find_connection` function is expected to find a transport connection between `origin` and `destination` at a given `departure_date` and `departure_time`. The `radius` parameter doesn't seem to be relevant for finding a transport connection, it is used for finding restaurants around the destination.
</details>
---
## Question 3
Why is it relevant that packet-switching networks remain agnostic of the concrete medium that is used to transmit signals?
✅ **Economic Efficiency: **Being medium-agnostic allows packet-switching networks to use the most cost-effective transmission technologies available. This could mean opting for copper wires, fiber optics, or wireless technologies depending on the context, such as the required bandwidth, distance, and cost constraints.
❌ **Enhanced Security:** By being agnostic of the transmission medium, packet-switching networks are more secure because hackers cannot tailor their attacks to a specific type of medium. Security hence does not anymore depend on the network protocols that are used.
✅ **Flexibility:** Packet-switching networks that are agnostic of the transmission medium provide flexibility in network design and expansion. As technology evolves or the needs of the network change, different transmission media can be integrated without the need for major changes to the network infrastructure or protocols.
❌ **Increased Speed: **Packet-switching networks that remain agnostic of the transmission medium inherently process data packets faster, regardless of the physical medium used. This is because in this case the network can optimize for specific transmission media, thereby exploiting them best for achieving high transmission speeds.

<details>
<summary>Explanation</summary>

> 💡 **[**Circuit vs. packet switching**](https://www.youtube.com/watch?v=oUN-s6aFMTk)**
✅ **Correct**, being medium-agnostic allows packet-switching networks to use the most cost-effective transmission technologies available. This could mean opting for copper wires, fiber optics, or wireless technologies depending on the context, such as the required bandwidth, distance, and cost constraints.
❌ **Incorrect**, the security of a network does not directly depend on whether it is agnostic to the transmission medium or not. It's more about the security protocols in place, not the type of medium used.
✅ **Correct**, packet-switching networks that are agnostic of the transmission medium provide flexibility in network design and expansion. As technology evolves or the needs of the network change, different transmission media can be integrated without the need for major changes to the network infrastructure or protocols.
❌ **Incorrect**, the speed of data transmission is dependent on the physical medium used and not on whether the network is agnostic to the transmission medium. Different media have different data transmission speeds. For example, fiber optics can transmit data faster than copper wires. Being medium-agnostic does not inherently make a network faster.
</details>
---
## Question 4
Which additional key-value pair must be added to the request **params** in Line 8 in the given code example if you only want to receive ***direct*** connections?
Look at the documentation and select the correct statement: [https://transport.opendata.ch/docs.html](https://transport.opendata.ch/docs.html) 
```python
url = '<http://transport.opendata.ch/v1/connections>'

params = {}
params['from'] = origin
params['to'] = destination
params['date'] = departure_date
params['time'] = departure_time

r = requests.get(url, params=params)
```
❌ `params['true'] = 'direct'`
❌ `params['direct'] = '1'`
❌ `params['connection'] = 'direct'`
❌ *The API already considers only direct connections by default*
✅ *There is no possibility to request only direct connections*
❌ `params['direct'] = 'true'`
❌ `params['direct'] = 1`

<details>
<summary>Explanation</summary>

> 💡 **[**Opendata Transport API documentation**](https://transport.opendata.ch/docs.html)**
❌ **Incorrect**, there's no parameter named 'true' in the API documentation.
❌ **Incorrect**, this parameter does not exist.
❌ `params['connection'] = 'direct'` is incorrect because there's no parameter named 'connection' in the API documentation.
❌ **Incorrect**, by default, the API shows all connections, not just direct 
✅ **Correct**, the API documentation does not state that you can filter for direct connections.
❌ **Incorrect**, the API documentation specifies that the value for the 'direct' parameter should be '1' and not 'true'.
❌ **Incorrect**, because the API documentation specifies that the value for the 'direct' parameter should be a string ('1') and not an integer (1).
</details>
---
## Question 5
How does TCP solve the Two Generals' Problem?
❌ TCP solves the Two Generals' Problem by implementing packet sequencing and acknowledgment of each packet. Each general (sender or receiver) knows for sure that their messages have been received and understood because TCP guarantees delivery of every packet without fail. If a packet is lost, TCP retransmits it until it is confirmed to be received, ensuring both sides are always synchronized.
✅ TCP does not solve the Two Generals' Problem because this problem is fundamentally unsolvable over an unreliable communication system where messages can be lost. However, TCP addresses some of the practical aspects of this problem by using acknowledgments (ACKs), sequence numbers, and timeouts to ensure reliable communication through an unreliable network.
❌ TCP solves the Two Generals' Problem by using its three-way handshake mechanism. This handshake involves the sender initiating the connection (SYN), the receiver acknowledging this request (SYN-ACK), and the sender acknowledging the receiver's acknowledgment (ACK).
❌ TCP does not solve the Two Generals' Problem because it is primarily concerned with speed rather than reliability of message delivery, and thus does not implement acknowledgment or retransmission mechanisms to ensure messages have been received.

<details>
<summary>Explanation</summary>

> 💡 **[TCP](/305c770201f94279bfd468d86c733ae6#d9f0456867ee4c45ac9fc43d26c2f9a2), [**Two Generals’ Problem**](https://www.youtube.com/watch?v=s8Wbt0b8bwY)**
The Two Generals' Problem is a thought experiment in computer science which demonstrates that no amount of message passing alone can guarantee that all participants in a network will agree on some fact. It's a fundamental issue in distributed systems and relates to the difficulty of achieving consensus.
❌ **Incorrect**, while TCP does implement packet sequencing and acknowledgment, it doesn't solve the Two Generals' Problem. The Two Generals' Problem is a consensus problem that cannot be solved if there's a chance that messages can be lost or delayed - conditions that can occur even when using TCP.
✅ **Correct**, The Two Generals' Problem is fundamentally unsolvable in an unreliable communication system, which includes any real-world network. While TCP does use acknowledgments (ACKs), sequence numbers, and timeouts to ensure reliable communication, it cannot guarantee consensus, which is the crux of the Two Generals' Problem.
❌ **Incorrect**, while TCP does use a three-way handshake mechanism to establish a connection, this doesn't solve the Two Generals' Problem. The problem is not about establishing a connection, but about reaching consensus over an unreliable network, which the three-way handshake does not address.
❌ **Incorrect**, TCP is actually designed with reliability as a primary concern, not speed. It does implement acknowledgment and retransmission mechanisms to ensure messages have been received. However, as mentioned before, these mechanisms do not solve the Two Generals' Problem because it's a consensus problem that is unsolvable in an unreliable network.
</details>
---

📄 **[Quiz 7]** (subpage)
## Question 1
Given is the following table **students**:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer | Haumesser | 1998-05-30 |
| 53450 | Julio Quinton | Shain | 1998-07-03 |
| 52819 | Van | Sokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Elgin | 1998-05-31 |
| 52791 | Dale | Oviatt | 2001-11-11 |
Which query will return the entire tuple of *Van Sokoloski*?
Each empty field must contain exactly one word or entry.
`SELECT * FROM students WHERE id = 52819`

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#9f49f1d27402470bb2f991902699a137), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb)**
The table 'students' contains data about students, including their `id`, `first_name`, `last_name`, and `date_of_birth`.
The correct SQL query to return the entire tuple (or row) of Van Sokoloski would be:
```sql
SELECT * FROM students WHERE id = 52819
```
Here's why:
- `SELECT *` is used to select all columns of a row in a table. The asterisk (*) is a wildcard character that represents 'all'.
- `FROM students` specifies the table from which we want to retrieve data, in this case, the 'students' table.
- `WHERE id = 52819` is a condition that selects the row(s) where the 'id' column has the value 52819. Since 'id' values are unique for each student, this condition will return exactly one row, the one of Van Sokoloski.
</details>
---
## Question 2
Given is the following table students:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 51759 | Megan | Peery | 1996-12-26  |
| 53532 | Lashanda | Maglioli | 1999-11-12 |
| 50399 | Jamey | Sobotka | 1999-01-07 |
| 50587 | Julianna | Ravitz | 1998-03-29 |
| 53646 | Sylvester | Sampere | 2000-07-07 |
What is the numerical result of the following query:
```sql
SELECT COUNT(*)
FROM students
WHERE
date_of_birth < DATE('1999-04-15')
```
**3**

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#9f49f1d27402470bb2f991902699a137), [COUNT](/9f266597386048dd9a967fd9fd8e4b89#f7cb9984cd3a437ab2bdf2f38daaddec), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb)**
The SQL query is counting the number of rows in the 'students' table where the `date_of_birth` is less than '1999-04-15'.
In simpler terms, it's counting how many students were born before April 15, 1999.
Let's go through the table:
- Megan Peery was born on 1996-12-26, which is before 1999-04-15. → *include*
- Lashanda Maglioli was born on 1999-11-12, which is after 1999-04-15. → *exclude*
- Jamey Sobotka was born on 1999-01-07, which is before 1999-04-15. → *include*
- Julianna Ravitz was born on 1998-03-29, which is before 1999-04-15. → *include*
- Sylvester Sampere was born on 2000-07-07, which is after 1999-04-15. → *exclude*
So, the students who were born before April 15, 1999, are Megan Peery, Jamey Sobotka, and Julianna Ravitz. That's **3 students.**
</details>
---
## Question 3
In your database, you have at least the following five tables (same as in Assignment 07):
- **students(id, first_name, last_name, date_of_birth)**
- **registrations(id, student_id, matriculation, exmatriculation)**
- **courses(id, name, category_id)**
- **enrollments(id, student_id, course_id, semester)**
- **grades(id, enrollment_id, grade)**
Which one of the following queries returns all students that have a grade better than 5 (which numerically is greater than 5) in the course 'Fundamentals of Space-Time-Travel'?

✅ Code-snippet 1
```sql
SELECT
  students.id, grades.grade, students.first_name, students.last_name
FROM
  grades
INNER JOIN enrollments
  ON enrollments.id = grades.enrollment_id
INNER JOIN students
  ON students.id = enrollments.student_id
INNER JOIN courses
  ON courses.id = enrollments.course_id
WHERE
  grades.grade > 5
  AND
  courses.name = 'Fundamentals of Space-Time-Travel'
GROUP BY
  students.id
```
❌ Code-snippet 2
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
  courses.name = 'Fundamentals of Space-Time Travel'
GROUP BY
	students.id
```
❌ Code-snippet 3
```sql
SELECT
  students.id, grades.grade, students.first_name, students.last_name
FROM
  grades
INNER JOIN enrollments
  ON enrollments.id = grades.enrollment_id
INNER JOIN students
  ON students.id = grades.student_id
INNER JOIN courses
  ON courses.id = enrollments.course_id
WHERE
  grades.grade > 5
  AND
  courses.name = 'History of Space-Time Travel'
GROUP BY
	students.id
```
❌ Code-snippet 4
```sql
SELECT
  students.id, grades.grade, students.first_name, students.last_name
FROM
  grades
INNER JOIN enrollments
  ON enrollments.id = grades.enrollment_id
INNER JOIN students
  ON students.id = enrollments.student_id
INNER JOIN courses
  ON courses.id = enrollments.course_id
WHERE
  grades.grade < 5
  AND
  courses.name = 'Fundamentals of Space-Time Travel'
GROUP BY
	courses.id
```
❌ It is not posisble in one query

<details>
<summary>Explanation</summary>

> ↪️ **Check the [explanation here](/3a3a4b5dac8647878840f77390b282f7#fcc5c6466396409ebabc499c8a893092).**
</details>
---
## Question 4
You have an SQL-compatible relational database system.
Please mark all correct answers for this context.
❌ A database contains the table **courses**. The SQL query **SELECT * FROM courses LIMIT 10** always returns exactly 10 tuples.
✅ The number of tuples returned by a **SELECT** query is *always* independent of which storage engine is used according to the ANSI-SPARC model.
✅ If a database with exactly three tables has *composite primary keys* in each of these tables, then the database does NOT necessarily have to have *foreign keys*.
✅ *SQL injections* never help to keep SQL queries performant, even if they are implemented in Python, which is otherwise known for its rather slow execution.
❌ Tables **A** and **B** each contain three tuples. Then the SQL query **SELECT * FROM A INNER JOIN B** also returns exactly three tuples.
❌ The query **SELECT DISTINCT * FROM tablename** of a table **tablename** always returns fewer tuples than the query **SELECT * FROM tablename** of the same table.

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#9f49f1d27402470bb2f991902699a137), [SELECT DISTINCT](/9f266597386048dd9a967fd9fd8e4b89#add7d3de22c14a809cb3c15bb7685bb4), [INNER JOIN](/9f266597386048dd9a967fd9fd8e4b89#f3ac72183aeb4fe7b12ff4cf12928a64), LIMIT**
❌ **Incorrect**, the SQL query `SELECT * FROM courses LIMIT 10` will return **up to** 10 tuples, not always exactly 10. If the table `courses` contains fewer than 10 tuples/rows, then the query will return all tuples/rows, which would be less than 10.
✅ **Correct**, the ANSI-SPARC model is a theoretical model of data management, and the storage engine doesn't affect the number of tuples returned by a **SELECT** query. The query's result depends on the data in the database, not the way it's stored.
✅ **Correct**, having composite primary keys in a table doesn't necessarily mean that the table will have foreign keys. Composite primary keys and foreign keys serve different purposes. Primary key is used to uniquely identify a record in a table, while foreign key is used to link two tables together.
✅ **Correct**, SQL injections are a security vulnerability, not a performance optimization technique. They occur when untrusted data is inserted into a query without proper validation or escaping, allowing an attacker to manipulate the query and the stored data eventually.
❌ **Incorrect**, 🤯 Unclear? check the [explanation here](/38843c4404ca477c83d9fd80c24f7870#148b03a8dfdc41b496623b69a0c64de2).
❌ **Incorrect**, the `SELECT DISTINCT` query eliminates duplicate rows from the result. If the table doesn't have any duplicate rows, then `SELECT DISTINCT * FROM tablename` will return the same number of tuples as `SELECT * FROM tablename`. 🤯 Still unclear? Check the [explanation here](/38843c4404ca477c83d9fd80c24f7870#6a3170a75ba54ce9a7b1f77d1784ff38).
</details>
---
## Question 5
Please assume that the table **persons** exists, with a non-null column **grade** that has correct numerical values and a column **course** that contains one course name in each tuple as a String.
Fill in the missing keywords to compute and return the *mean value* of **grades** for the ten best graded **courses** in the table **persons**.
```sql
SELECT course, AVG(grade)
FROM persons
GROUP BY course
ORDER BY AVG(grade) DESC
LIMIT 10
```

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#9f49f1d27402470bb2f991902699a137), [GROUP BY](/9f266597386048dd9a967fd9fd8e4b89#01c3d00f4a9e49c483728e10edd3deba), [AVG](/9f266597386048dd9a967fd9fd8e4b89#dc656637e4ae4f128577dd14c9f56303), LIMIT**
The task here is to compute and return the mean value of grades for the ten best graded courses in the table `persons`.
Here is the explanation of each keyword:
- `SELECT`: This keyword is used to select columns from a database tables. In this case, we are selecting `course` column and create a new column `AVG(grade)` that contains the mean grade of each course.
- `AVG(grade)`: This is an aggregate function that returns the average value of a numeric column. Here it is used to calculate the average grade of each course.
- `FROM`: This keyword is used to specify the table from which to retrieve the data. Here, the data is retrieved from the `persons` table.
- `GROUP BY`: This keyword is used in collaboration with the aggregate function `AVG(grade)` to group the result by `course`.
- `ORDER BY`: This keyword is used to sort the result in ascending or descending order. Here, it's used to sort the results by `AVG(grade)` in descending order (`DESC`), so that the course with the higest average grade will appear on top.
- `LIMIT`: This keyword is used to specify the maximum number of records/rows to return. Here, it's used to limit the result to the top 10 courses with the highest average grades.
> 🤯 **Still unclear? Check the[ explanation here](/3a3a4b5dac8647878840f77390b282f7#7a6d3430603d44e4a8e93510b54eb953).**
</details>
---
## Question 6
What happens if there is <u>no</u> **WHERE** statement in an **UPDATE** query?
❌ There is no restriction, so no entry in the chosen table will be overwritten.
❌ A syntax error will appear because updating entries in a table is done with the **INSERT** query.
❌ A syntax error will appear because an **UPDATE** query requires a **WHERE** statement.
✅ There is no restriction, so all entries in the chosen table will be overwritten.

<details>
<summary>Explanation</summary>

> 💡 **[UPDATE](/9f266597386048dd9a967fd9fd8e4b89#3ebedba97a0549f3b646cef4edebfbc4)**
❌ **Incorrect**, because without a **WHERE** clause, the **UPDATE** query will apply to all rows in the table, not none.
❌ **Incorrect**, because the **UPDATE** query is used to update existing data in a table, not the **INSERT** query. **INSERT** is used to add new rows to a table.
❌ **Incorrect**, because while it's good practice to include a **WHERE** clause in an **UPDATE** query to specify which rows should be updated, it's not a syntax requirement. If no **WHERE** clause is included, the **UPDATE** will apply to all rows.
✅ **Correct**, without a WHERE clause, the UPDATE query will apply to all rows in the table.
</details>
---


📄 **[Quiz 8]** (subpage)
## Question 1
Given is the pd.Series x:
```python
0     1.0
1     2.0
2     7.0
3     NaN
4     2.0
...
72    3.0
73    23.0
74    3.0
75    23.0
76    3.0
Length: 77, dtype: float64
```
The evaluation of **x.sum()** returns *770.0*
Please mark **all** statements that can be executed without raising an error **AND** that are True.
❌ x.mean() == x.iloc[1:].mean()
✅ x.mean() == x.sum() / x.count()
✅  Code snippet
```python
total = 0
counter = 0
for f in x:
		if not np.isnan(f):
				counter += 1
				total += f
x.mean() == total / counter
```
✅ x.mean() == x.iloc[:len(x)].mean()
✅ x.mean() == x.iloc[:].mean()
❌ x.mean() == x.sum() / len(x)

<details>
<summary>Explanation</summary>

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.isnan()](/ccc5737dc7c64936bced118aca375cf9#2d995d983b82436a8d0af9d54c34d7ed), [.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
❌ **Incorrect**, because `x.iloc[1:]` means the series starting from index 1 (value **2.0**), i.e., excluding the first element (value **1.0**). The mean of this series will be different from the mean of the whole series.
✅ **Correct**, because the mean is calculated as the sum of all elements divided by the number of all non-NaN elements in the series (`x.count()`).
✅ **Correct**, because this loop calculates the sum of all non-NaN elements and divides it by the number of non-NaN elements, which is again the definition of mean.
✅ **Correct**, because `x.iloc[:len(x)]` is `x.iloc[:77]` which includes all elements up to index position 76 (including), which representes the entire series.
✅ **Correct**, because `x.iloc[:]` also represents the entire series.
❌ **Incorrect**, because `len(x)` gives the total length of the series including NaN values (e.g., index position 3), but the mean is calculated as the sum of all elements divided by the number of non-NaN elements.
</details>
---
## Question 2
We have the following pd.DataFrame df. The column index is defined as the index of df.
| index | value1 | value2 |
| --- | --- | --- |
| 0 | 1 | z |
| 21 | b | y |
| 11 | c | x |
| 24 | d | w |
| 29 | e | v |
| 6 | f | u |
| 9 | g | t |
| 15 | h | s |
| 33 | i | r |
Which **index** does the command return: **df.iloc[6]**
**9**

<details>
<summary>Explanation</summary>

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d)**
The `iloc` function in Pandas is used to select rows by their integer location. It's a zero-based indexing method, meaning that the first row is at position 0, the second row is at position 1, and so on.
In this case, `df.iloc[6]` is asking for the 7th row in the Dataframe (remember, it starts from 0), regardless of the actual index label of that row.
So, the command `df.iloc[6]` will return the row with index **9** as it is the 7th row in the DataFrame.
Here's a breakdown of the DataFrame rows and their integer locations:
- postion 0, 1st row: index = 0, value1 = 'a', value2 = 'z'
- position 1, 2nd row: index = 21, value1 = 'b', value2 = 'y'
- position 2, 3th row: index = 11, value1 = 'c', value2 = 'x'
- position 3, 4th row: index = 24, value1 = 'd', value2 = 'w'
- position 4, 5th row: index = 29, value1 = 'e', value2 = 'v'
- position 5, 6th row: index = 6, value1 = 'f', value2 = 'u'
- **position 6, 7th row: index = 9, value1 = 'g', value2 = 't'** <- Row returned by `df.iloc[6]`
- position 7, 8th row: index = 15, value1 = 'h', value2 = 's'
- position 8, 9th row: index = 33, value1 = 'i', value2 = 'r'
</details>
---
## Question 3
Given is the DataFrame DF from Assignment 8.
Which of the following code snippets returns a ***list*** of genres for the movie at the given integer position ***position***?
Remember that the genres for a movie are saved in the column ***genres***, and are in a format like in the following example: "Action|Adventure|Fantasy".
✅ Code snippet 1
```python
def get_genres(position):
    genres = DF.iloc[position]['genres']
    if pd.isna(genres):
        return []
    else:
        return genres.split("|")
```
❌ Code snippet 2
```python
def get_genres(position):
    genres = DF.genres[position]
    if pd.isna(genres):
        return []
    else:
        return genres.split(" | ")
```
❌ Code snippet 3
```python
def get_genres(position):
    genres = DF[position]['genres']
    if pd.isna(genres):
        return []
    else:
        return genres.split("|")
```
❌ Code snippet 4
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

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.isna()](/1867045b058343e1a66b677961515907#228f2dfad24349f9a7156edde17dc6b3)**
✅ **Correct.** This function uses the `iloc` function to access the row at the given `position` and then fetches the `genres` column. If the genre is not available (NaN), it returns an empty list. Otherwise, it splits the genres string on the **"|"** character and returns the list of genres.
❌ **Incorrect.** This function correctly fetches the `genres` for the given `position` and checks for NaN. However, it tries to split the genres string on **" | "** (note the spaces) instead of **"|"**. This will not correctly split the genres.
❌ **Incorrect.** This function tries to fetch the `genres` by using `position` directly on the DataFrame, which is not correct. It should use either `iloc` or `loc` to access rows by position or index respectively.
❌ Incorrect**.** This function is almost identical to the first one and correctly fetches the `genres`, checks for NaN, but does not split the strings and thus returns the string as-is (e.g. "Action|Adventure|Fantasy") instead of splitting it (e.g. ["Action", "Adventure", "Fantasy"])
> 🤯 **Still unclear? Check also the [explanation here](/b0908e82d8704e3b802a93e78912a002#16b59bc9e99c4a82b529e743aa0725cf).**
</details>
---
## Question 4
Given is a pd.DataFrame df with a fixed and default index, several rows and the four columns a, b, c, and d in that exact order.
Which of the following statements will always return a pd.Series that contains the full column a of df? (There could me more than one.)
`df.T.loc['a']`
`df.iloc['a']`
`df.T.iloc[0]`
`df.loc[:, 'a']`
`df.loc['a']`
`df.iloc[:, ['a']]`
`df['a']`

<details>
<summary>Explanation</summary>

> 💡 **[.T](/1867045b058343e1a66b677961515907#b65f0a7a58214e66ba42846c09b6dbdd),[ .loc[]](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7), [.iloc[]](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)**
✅  **Correct**, because `df.T` transposes the DataFrame, swapping rows and columns. `loc['a']` then selects the 'a' row, which was previously the 'a' column in the original DataFrame.
❌  **Incorrect**, because `iloc` is used for indexing by integer location, not by labels. Therefore, it cannot accept a string argument like 'a'.
✅  **Correct**, because `df.T` transposes the DataFrame, making the first row to be 'a'. `iloc[0]` then selects this first row, which was previously the 'a' column in the original DataFrame.
✅  **Correct**, because `loc` is used for indexing by labels. The colon `:` selects all rows, and 'a' selects the 'a' column.
❌  **Incorrect**, because `loc` is used for indexing by labels, but 'a' is not a row label, it's a column label. This would throw a KeyError if 'a' is not an index in the DataFrame.
❌  **Incorrect**, because `iloc` is used for indexing by integer location, not by labels. Therefore, it cannot accept a string argument like 'a'.
✅  **Correct**, because this is a common way to select a single column from a DataFrame. It returns the 'a' column as a pd.Series.
> 🤯 **Still unclear? Check the [notebook here](https://colab.research.google.com/drive/1jksSqoNvzO-X_2E7ExeRbWjKqufELMNT?usp=sharing).**
</details>
---
## Question 5
Given is the following code snippet from Assignment 8.
The function should compute the ratio of gross/budget for each movie and return a DataFrame with that information. Why is it not working as intended (there may be several reasons)?
Remember that the resulting DataFrame must fulfill all of the following criteria:
- The columns must only be "director_name", "movie_title", "gross", "budget", and finally "gross/budget" (and the index column)
- The value in the column "gross/budget" must be the result of the row-wise division of the column "gross" and "budget".
- There must not be any NaN (empty) values in the resulting dataframe.
- The dataframe must be sorted in descending order by the newly created "gross/budget" column. Do not reset the index.
- The original dataframe (DF) must not be modified.
```python
def gross_per_budget():
	df = DF.copy()
	df = df[['director_name', 'movie_title', 'gross', 'budget', 'duration']]
	df['gross/budget'] = df['gross'] / df['budget']
	df = df.sort_values(by='movie_title', ascending=False)
	return df
```

✅ In line 5, the dataframe needs to be sorted by the column "gross/budget":
```python
df = df.sort_values(by='gross/budget', ascending=False)
```
❌ There is nothing wrong with this code. It works perfectly.
❌ After line 3, empty values (NaN) need to be removed like this:
```python
df = df.dropna(axis="columns")
```
✅ The resulting DataFrame also contains the column 'duration' which is not included in the above mentioned criteria and therefore should be removed in line 3.
❌ The original dataframe F is modified in the current code. Line 2 needs to be changed to
```python
df = DF
```
✅ After line 3, empty values (NaN) need to be removed like this:
```python
df = df.dropna(axis=0)
```

<details>
<summary>Explanation</summary>

✅ **Correct**, the DataFrame should be sorted by the column "gross/budget", not "movie_title". This is because the criteria specifies that the DataFrame must be sorted in descending order by "gross/budget".
❌ **Incorrect**, because there are several issues with the code. For example, it doesn't sort the DataFrame by the correct column, it doesn't remove NaN values, and it includes an unnecessary "duration" column.
❌ **Incorrect**, the `dropna(axis="columns")` function would remove any column that contains at least one NaN value. This is not what we want, because it could remove columns that are required in the result. Instead, we want to remove rows with NaN values, which can be done using `dropna(axis=0)`.
✅ **Correct**, the "duration" column is not required in the final DataFrame, so it should be removed.
❌ **Incorrect**, the original DataFrame (DF) is not modified in the current code. The `copy()` function is used to create a copy of DF, which is then modified. This leaves the original DataFrame unchanged.
✅ **Correct**, the `dropna(axis=0)` function will remove any row that contains at least one NaN value, which is what we want. This will ensure that there are no NaN values in the resulting DataFrame.
</details>
---
## Question 6
Given is a *pd.DataFrame* as **df**.
Which datatype(s) can end up in variable **x** after the following statement:
**x = df.iloc[42]**
Assume, that the queried entry exists, meaning that **x** is not empty.
✅ **x** will have exclusively the datatype *pd.Series*.
❌ None of the other options.
❌ **x** will have exclusively the datatype *pd.DataFrame*.
❌ **x** can be of datatype pd.Series and *pd.DataFrame*.

<details>
<summary>Explanation</summary>

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7), [pandas datatypes](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
The `iloc` function is used in pandas to select rows by their position. If you select a single row using `df.iloc[42]`, the result is a **pd.Series** object, which contains the data of the row. So, `x` will have exclusively the datatype `pd.Series`.
Here is an example:
```python
import pandas as pd

# Create a simple dataframe
df = pd.DataFrame({
   'A': ['foo', 'bar', 'baz'],
   'B': ['qux', 'quux', 'quuz'],
   'C': ['corge', 'grault', 'garply']
})

x = df.iloc[1]
print(type(x))
```
This will output:
```python
<class 'pandas.core.series.Series'>
```
This shows that x is a pd.Series. The other options are incorrect because `df.iloc[42]` will not return a pd.DataFrame and it can't be both pd.Series and pd.DataFrame at the same time.
</details>
---
## Question 7
Given is a *pd.DataFrame* **df** with 100 rows and a continuous index starting from 0 to 99.
What happens if we add a new row with an index that already exists (e.g., 42)?
❌ Adding to the end will result in an automatic matching index: Here, the added row will have the index 100.
❌ Pandas recognizes that you add the same index twice and will automatically create a *MultiIndex*, hence use the next column additionally as an index.
❌ Similar to SQL/Databases, the index is a *primary key*, so the new row can't be added and it will fail with an error.
✅ The new row is added, non-unique indices are no problem.

<details>
<summary>Explanation</summary>

> 💡 **[DataFrames](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
❌ **Incorrect**, because when you add a row with a specific index, pandas will use that index number, not auto-increment the index to 100.
❌ **Incorrect**, because pandas does not automatically convert to a MultiIndex when duplicate indices are added.
❌ **Incorrect**, because unlike SQL/Databases, pandas allows non-unique indices. It doesn't treat index as a primary key.
✅ **Correct**, because in pandas, it's possible to have duplicate indices. If you add a new row with an index that already exists, the new row will be added with the same index. For example:
Let’s assume we have the following DataFrame:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f038a20b-3964-4a36-98d5-34b37f2597a4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3HLYZJA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIEj41g3bPx99Mlg1F0CuI5Vmv7aTGBXhF7Tnl4M9%2BcWTAiAzWShYiMs61xg91KftxA36vJz%2BC8ez9NPIQ28poFSjWSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMvJq5Zf3nFOfszbN4KtwDicBpfoQuRdLq2Egbbt1jBOSLSjxiuoE13Q3E1%2FiOwvb%2FOdChCrwi8rXKh%2B%2BT3AVxY8fJqap2Axf8J0HjFNBvSHZpbOV3NCSGo0nEjtl79m8rfTuBEVHTCZ9bWJ0TPk%2BCLSRjpcw%2BmbWMJAtSHmm%2B%2FvLRyjyPtilDpMAKcOWS41Q2cl3GaxgY9hSGsyJhQ2fqJ3uE46SvKuD1WICTHo7qJ1WDXhcSlRcPoWproQ4uDqzcMGzEsfWfN0SMW3JxcPxqqSFv%2BVeNwg5mpJvfoulOGaKAqmNxw6d4o9vOfw%2Bc8Zq7ltl5VDzWFbPYuryX%2BBM5jtVpe8ofCIPRW0HuZkkqX5nRO2eoSuqXy%2FsBaJ%2FmHgSkYvvyPTGZ4enGQUK%2BW8xYEJOC0TQmTvcyW208iB3YJd%2B3pHW7jiq08Jon6ZADosKAl564Bs2SMy9qbwYgW3BVjjPWSNmLYFimqksjVrkhCrC4NZydnC9JH3hZ23eXdztmLRgX5CzOe62oZEz3JMrV5TV5oitirxxvbw1fVyTqjRqwEIApMzIzdTgsLLTKZI059e%2BOLg147ohaeJLrdEsbzSULw2sqh4MpjJ%2FdEWpEZAgIehUxuoUUkGhte7pQgWVnDB1Hy1GuD3zF3pIw4873yQY6pgGjuQCQsY5KL%2B6t2Ih%2BOiAQnir9QTIaM1rxf1x8mOvwhzc%2BQpuYBkEOwsSV53dlmTBY9HQQWPKJKEPSvfxGKd06MnmWmsyTiD4mU70R0Hk%2FmOAPukkkGdL%2BNL4X8u0AGpck0GzA8cjvx1WbHyWhTQJ1Wabw6NOJg8TVaUY4slzgb7X4CJvS88ThCzgRtmTPmtEdLmoEA4w4oLA9kan%2Bs4sN7AjD%2FQjR&X-Amz-Signature=ce364c5d1728dfdb15c2959264705979bfcb9cf84653c90306833814057f9bbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now if we create a new Series with the index 42 again
```python
new_row = pd.Series({"A": 4}, name=42)
```
And add this new row to the DataFrame:
```python
df = df.append(new_row)
```
We can see that the same index 42 exists now twice in the DataFrame:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/58fb90e3-3ad4-4c32-98ce-b9b7591acf0d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3HLYZJA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIEj41g3bPx99Mlg1F0CuI5Vmv7aTGBXhF7Tnl4M9%2BcWTAiAzWShYiMs61xg91KftxA36vJz%2BC8ez9NPIQ28poFSjWSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMvJq5Zf3nFOfszbN4KtwDicBpfoQuRdLq2Egbbt1jBOSLSjxiuoE13Q3E1%2FiOwvb%2FOdChCrwi8rXKh%2B%2BT3AVxY8fJqap2Axf8J0HjFNBvSHZpbOV3NCSGo0nEjtl79m8rfTuBEVHTCZ9bWJ0TPk%2BCLSRjpcw%2BmbWMJAtSHmm%2B%2FvLRyjyPtilDpMAKcOWS41Q2cl3GaxgY9hSGsyJhQ2fqJ3uE46SvKuD1WICTHo7qJ1WDXhcSlRcPoWproQ4uDqzcMGzEsfWfN0SMW3JxcPxqqSFv%2BVeNwg5mpJvfoulOGaKAqmNxw6d4o9vOfw%2Bc8Zq7ltl5VDzWFbPYuryX%2BBM5jtVpe8ofCIPRW0HuZkkqX5nRO2eoSuqXy%2FsBaJ%2FmHgSkYvvyPTGZ4enGQUK%2BW8xYEJOC0TQmTvcyW208iB3YJd%2B3pHW7jiq08Jon6ZADosKAl564Bs2SMy9qbwYgW3BVjjPWSNmLYFimqksjVrkhCrC4NZydnC9JH3hZ23eXdztmLRgX5CzOe62oZEz3JMrV5TV5oitirxxvbw1fVyTqjRqwEIApMzIzdTgsLLTKZI059e%2BOLg147ohaeJLrdEsbzSULw2sqh4MpjJ%2FdEWpEZAgIehUxuoUUkGhte7pQgWVnDB1Hy1GuD3zF3pIw4873yQY6pgGjuQCQsY5KL%2B6t2Ih%2BOiAQnir9QTIaM1rxf1x8mOvwhzc%2BQpuYBkEOwsSV53dlmTBY9HQQWPKJKEPSvfxGKd06MnmWmsyTiD4mU70R0Hk%2FmOAPukkkGdL%2BNL4X8u0AGpck0GzA8cjvx1WbHyWhTQJ1Wabw6NOJg8TVaUY4slzgb7X4CJvS88ThCzgRtmTPmtEdLmoEA4w4oLA9kan%2Bs4sN7AjD%2FQjR&X-Amz-Signature=c7c2814879f1121e17c80417b52044068d40e2acdc9519c43750d77be217272f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
📄 **[Quiz 9]** (subpage)
## Question 1
Which of the following data types can a query on a pd.DataFrame return?
✅ String
✅ Pandas DataFrame
✅ a 64 bit float
✅ Pandas Series

<details>
<summary>Explanation</summary>

> 💡 **[Pandas datatypes](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
✅ **Correct**, a query on a DataFrame can return a string as it is posisble to store strings inside a DataFrame. Thus, when accessing a single cell in a DataFrame it is posisble to retrieve a string.
✅ **Correct**, a query on a DataFrame can return a new DataFrame that meets the query conditions. For example, if you use the `df[df['column'] > 5]` syntax, it will return a new DataFrame with rows where the value in 'column' is greater than 5.
✅ **Correct**, if your query is designed to return a single value and that value is a float, then yes, it can return a 64-bit float. For example, `df['column'].mean()` would return a 64-bit float if 'column' contains float values.
✅ **Correct**, if your query is designed to return a single column, it will return a Series. For example, `df['column']` would return a Series.
</details>
---
## Question 2
You have the two pd.DataFrame objects persons and addresses with the following columns:
```python
print(addresses.columns)
>>> ["zip", "city", "street", "number"]

print(persons.columns)
>>> ["name", "address_id"]
```
The indices of both DataFrames are continuous non-duplicate integers starting from 0. The column **address_id** in **persons** is supposed to be a *foreign key* for the **index** of the **addresses** DataFrame.
There are some persons that do not have an address, so the value of the **address_id** for these entries will be *np.nan/NaN/pd.NA*.
Additionally, an entry in the **addresses** DataFrame could be referred to by none, one, or multiple persons.
Which of the following statements returns a *pd.DataFrame* with <u>all</u> columns of both DataFrames **persons** and **addresses** with the following restriction:
The resulting DataFrame must contain all entries from the DataFrame **addresses** and their referenced person, if one exists. If no person is referenced for an address, the corresponding values for this row should be set to np.nan/NaN/pd.NA.
If a person is not referenced by an address, the person should not be included in the result.
❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`
❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`
✅ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`

<details>
<summary>Explanation</summary>

> 💡 **[.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
The correct answer is:
✅ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`
Explanation:
The `pd.merge()` function is used to combine two or more dataframes into a single dataframe. The `how` parameter determines the type of merge to be performed. It can be 'left', 'right', 'outer', or 'inner'.
- 'left': use only keys from left frame
- 'right': use only keys from right frame
- 'outer': use union of keys from both frames
- 'inner': use intersection of keys from both frames
In this case, we want to keep all the entries from the `addresses` dataframe and their referenced person, if one exists. If no person is referenced for an address, the corresponding values for this row should be set to np.nan/NaN/pd.NA. This is exactly the behavior of a 'right' merge.
The `left_on` and `right_index` parameters are used to specify the columns or indices on which to merge the dataframes. Here, we are merging on the 'address_id' column from the `persons` dataframe and the index of the `addresses` dataframe.
The other options are incorrect because they either exclude entries from the `addresses` dataframe that are not referenced by a person (inner join), include persons that are not referenced by an address (left join and outer join), or they merge on the wrong columns or indices.
> 🤯 **Sill unclear? Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#5358c79993774a36b6fd71751f8607c6).**
</details>
---
## Question 3
You have the two pd.DataFrame objects persons and addresses with the following columns:
```python
print(addresses.columns)
>>> ["zip", "city", "street", "number"]

print(persons.columns)
>>> ["name", "address_id"]
```
The indices of both DataFrames are continuous non-duplicate integers starting from 0. The column **address_id** in **persons** is supposed to be a *foreign key* for the **index** of the **addresses** DataFrame.
There are some persons that do not have an address, so the value of the **address_id** for these entries will be *np.nan/NaN/pd.NA*.
Additionally, an entry in the **addresses** DataFrame could be referred to by none, one, or multiple persons.
Which of the following statements returns a *pd.DataFrame* with <u>all</u> columns of both DataFrames **persons** and **addresses** with the following restriction:
The resulting DataFrame must contain all entries from the DataFrames **persons** and **addresses.**
❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`
❌ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`
✅ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`

<details>
<summary>Explanation</summary>

> 💡 **[.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
The correct answer is
✅ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`.
Explanation:
In pandas, the `merge` function is used to combine two or more dataframes based on a related column between them. The `how` parameter determines the type of merge to be performed:
- 'left': Use only keys from left frame
- 'right': Use only keys from right frame
- 'outer': Use union of keys from both frames
- 'inner': Use intersection of keys from both frames
The 'outer' merge is the only option that includes all entries from both dataframes, regardless of whether there is a match in the other dataframe. This is why the correct answer is `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`.
The `left_on` and `right_index` parameters specify the columns or indices on which to join the dataframes. In this case, we're joining on the `address_id` column from the **persons** dataframe and the `index` of the **addresses** dataframe. All other options either exclude some entries or incorrectly specify the columns or indices to join on.
> 🤯 **Still unclear? Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#8ec92dddc52c409380bae0890373b33d).**
</details>
---
## Question 4
In Assignment 09, there was the pd.DataFrame **ORDERS** with the column products that encoded the items and their count as a JSON encoded string. 
As a first step, you fixed the error of the **json** module and overwrote the column products now with a dictionary in the correct format. 
Which of the following statement returns a pd.Series with the same index as df and the minimal number of distinct products as values for each purchase?
❌ `df['products'].apply(lambda r: min(r.keys()))`
❌ `df['products'].apply(lambda r: r.values().min())`
❌ `df['products'].apply(lambda r: min(r))`
❌ `df['products'].apply(lambda r: max(r.keys()))`
❌ `df['products'].apply(lambda r: r.values()).min()`
❌ None of the given choices will produce a *pd.Series*.
✅ None of the given choices will produce the wanted result, even though it produces a *pd.Series*.

<details>
<summary>Explanation</summary>

> 💡 **[.apply()](/1867045b058343e1a66b677961515907#9e6d1643dc24411181facc1dd3265ffd)**
> ↪️ **Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#1f6c5f13ae564237afdf9560ace362b5).**
</details>
---
## Question 5
As a nice housemate that you are, you prepared Christmas presents for your family. 
You have measured the height, width, and length of the packages and saved the information in a *pd.DataFrame* **df**. Additionally, for each present, you recorded the name of the recipient in the column recipient which you set as the index for **df**.
How can you aggregate the minimal height, width, and length <u>per recipient</u>?
The result should look something like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/daf59472-35da-4221-aecb-ad0307bc494c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW73GWVX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDPcH%2FJhC4VPO6Z4QXDwLIod%2FWfTwyawKPOnbeawcbB3AiEAiOrKogFrobvA6gEqHlC91gTpVz%2BN2lrI5vt1S6k7K8Iq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDAOcyvSfqgDjhSqkOCrcAxmcUcL6pKAWWIkk6TOARvi4MdjfZ9XyzLh1eiMbd2eTOz6%2BGUFrBQkBoedFrN1UidUGxqtiFJc02BLcPkO%2Fn8%2B%2BNOQV7j8yhbhtofEqOZ2WGJYvR42JfZ06KUEXBhBtOH1Hn63ZzGmQpd0goBP6AcqJL02%2FJusSc%2B7tB16OD3ukRdNjktk%2BwoBpnmPMBRXlKfOb2cWppykUU5HclEVryyNSZJ0wPWZM2ZXeK3foKWlrUzdTVSptIK%2BOvMsvC1Nb6e%2BLJ1rj8ZJ7l433AdAXITbKr%2FrcIECFoIrlF%2Btcq9hUKen0ftagNtBKttHkznHyoAuOb8owNnh7t%2Br5efvHeGfc%2BynObfWBPeMfFN1zcpwVELnnVigtL%2BV7jW0UcPzxmm%2FiIXM9q%2FFDWx5%2FA9TXvfNRtgKnW1fDV4GvGV22DGapwr17eGlQoVpOKLfnrZcBRC6v2Y3z1Rfe%2Bnul3emt46M05Q7q1mz1f3TqmsJyZR6vkXECz83dbTRW6rQFA2pTUdvTgMsJbkjuqveFqxld2HGafct6KGJFIzH9qTn6uGAI5Ap4epYB68pEYUr7rd9E%2BQObOehfzb%2FZqRPnB3S1wtMnolRmK32sT8Ea851KNkpaTLD8mE%2FO6GOkUANbMOnN98kGOqUBTN1hDg2kXR%2FZR7M11nv21MzYMdXTur8Bwtdid898zYzjuE4yGaTkaLBddR0XbD9beZ3pJXcNQD6Av1qzVw3QndlgXw8qJlvKKLBgk4qMdxU%2B1UkywUu06Pj87DePFT2pWXqCZHIy3ppzfcDbewsoSVHTKe444nIws513uqQkgXzy686opMxQTaMR5vAo8zahZi1jaxre5dmpSI6amRVmABrBJVxa&X-Amz-Signature=de7ecc25ef86c9b51d22cf91d98278ec6a9ae0274fc1a453d484663dabe14df3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Mark <u>all</u> statements that result in the variable **agg** contain the *pd.DataFrame* as above. The *recipient* must be the index.
❌ `agg = df.agg("min", axis=1).groupby('recipient')`
❌ `agg = df.index.min()`
❌ `agg = df.min('recipients')`
❌ None of the statements will create the wanted DataFrame.
❌ `agg = df.min('index')`
✅ `agg = df.groupby('recipient').agg('min')`
✅ `agg = df.groupby('recipient').min()`
✅ `agg = df.groupby('recipient').agg(np.min)`

<details>
<summary>Explanation</summary>

> 💡 **[.agg()](/1867045b058343e1a66b677961515907#1c8f902fb8774ff7ab8c9bd1d9f76684), [.groupby()](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15)**
❌ **Incorrect**, because it tries to aggregate before grouping by 'recipient'. Also, `groupby('recipient')` would not work here because after the aggregation, 'recipient' is no longer a column in the DataFrame.
❌ **Incorrect**, because it will return the minimum value of the index, not the minimum values of the height, width, and length for each recipient.
❌ **Incorrect**, because the `min` function does not take a string argument, it should be used without any arguments to return the minimum values for each column.
❌ **Incorrect**, because there are correct statements.
❌ **Incorrect**, because the `min` function does not take a string argument.
✅ **Correct**, because it groups the DataFrame by 'recipient' and then aggregates the minimum values for each group.
✅ **Correct**, because it is the shorthand version of the previous statement. It groups the DataFrame by 'recipient' and then returns the minimum values for each group.
✅** Correct**, because it groups the DataFrame by 'recipient' and then applies the numpy function `np.min` to aggregate the minimum values for each group. It is equivalent to the previous two correct statements.
> 🤯 **Still unclear? Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#400446c4746144e2b55f111129b3b014).**
</details>
---
## Question 6
In Assignment 9 you implemented the function *study_overview()*, which works on the DataFrame STUDIES. It should give an overview of where which combinations of *courses* and *regions* exist.
Now look at the following implementation of the function:
```python
def study_overview():
	return STUDIES.merge(index='bachelor/master', columns='course', values='region')
```
Mark all the correct statements!
❌ *columns* and values are set incorrectly, correct would be *columns='region'* and *values='course'*.
✅ *index* and *values* are set incorrectly, correct would be *index='region'* and *values='bachelor/master'*.
✅ The function pivot() must be used instead of merge().
❌ The function reshape() must be used instead of merge().
✅ The function cannot be executed successfully.
❌ None of the other functions can be executed on the DataFrame.

<details>
<summary>Explanation</summary>

> 💡 **[.pivot()](/1867045b058343e1a66b677961515907#b7e324abb8a749b38b4a2386f6d4dbf7), [.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
> ↪️ **Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#9af05826713b446b9ee59383d2362e05).**
</details>
---

📄 **[Quiz 10]** (subpage)
## Question 1
We have the following *pd.DataFrame ***df** of fruit sales. The code below was used to create the given figure.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5ecb8592-f208-42fa-ba9a-7e451775c803/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=b213ade192e0c6956930823b1e46ee2663bc26fe6bbbe5e9ccc93d199b830719&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
fig, ax = plt.subplots(figsize=(8,6))

ax.bar(df.columns, df.max(), color='green')
ax.bar(df.columns, df.loc['Banana'], color='blue')
ax.bar(df.columns, df.min(), color='red')

plt.show()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/873e4980-985f-43d3-87ee-044ba976e19a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=fb0a0e733d1e1ae1478aba23f82590af3060284946b1733e2ed5304b440c6b1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Mark all the statement that are true.
✅ Sunday is the day with the fewest sales in total.
❌ Relative to the other fruits on the same day, most bananas were sold on Wednesday. 
❌ Friday is the day with fewest sales in total.
❌ This is a stacked bar plot. 
✅ From the plot, it is impossible to know how many bananas were sold on Friday. 
✅ Bananas were the most sold fruit on Tuesday because the blue bar is the largest there. 
❌ On Thursday, Friday, and Saturday, the sales for bananas were 0. 

<details>
<summary>Explanation</summary>

> 💡 **[.subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d), [.bar()](/10c38918e9a84ef79c8040d2fba85e2e#7f417ec8d30647888b638c6e367259e1)**
✅ **Correct**, don’t get irritated by the heights of the bars, as they are not stacked on each other but rather just overlapping.
❌ **Incorrect**, most bananas were sold on Tuesday. 
❌ **Incorrect**, Sunday is the day with the lowest sales.
❌ **Incorrect**, it is a simple multiple bar plot. The bars are just overlapping each other, which is why it appears like a stacked bar chart. If we want to create a stacked bar chart we would need to define the `bottom=` parameter.
✅ **Correct**, because the green and the red bar are overlapping the blue bar, thus we can not infer from the plot how many bananas were sold on that day.
✅ **Correct**, the blue bars represent the sales of bananas.
❌ **Incorrect**, the sales was not zero, the bars are simply not visible in the plot as they are overlapped by the other bars.
</details>
---
## Question 2
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
**✅ Figure 1**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/671fec9e-0d8b-481a-8e6d-5e86347f6490/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=fe9485e3a1c464cf8f06cea9a7e0bac8756037e9914a3ceaab8aacefdec47e72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 2**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/695a6b05-f2f8-40a9-bf6a-a39a44b06cb5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=d29892c275fd0391aa2937a738cb945723b095c650d89297f275e532c7f83a51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 3**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3d5de852-f8cf-4ece-88eb-e79c917123e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=1bb553e7fa663066c2c335036237e9f2a1cb8de4dd6eb486b1c1f2aa1a25be8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 4**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/28f2f2fb-1f68-4c7b-bcd1-b8a02271a5b7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=8565e7e3470140f5ca427372ec147b130564c57f77cbc9e1f4d5bda9fb8669eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

> 💡 **[.bar()](/10c38918e9a84ef79c8040d2fba85e2e#7f417ec8d30647888b638c6e367259e1), [.arange()](/ccc5737dc7c64936bced118aca375cf9#82ad4caa17294f6a89ccfeb254bcf289), [.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.set_xticks()](/10c38918e9a84ef79c8040d2fba85e2e#1a8b5ac6cd6f4f24a77276097215a64f), [.set_xticklabels()](/10c38918e9a84ef79c8040d2fba85e2e#b88bafe085734ba0acc0d42797d954c8)**
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
In Figure 1, **Cherry** is on the left, **Banana** in the middle and **Apple** on the right. 
</details>
---
## Question 3
We want to produce this plot:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5363df47-9e70-4389-9327-e859bf892a00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=643458ce28eb8c0c7c4345f40963fb8f181af38add049e9517302ea1a19a949d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Which keyword argument is required to create this plot?
`fig, axes = plt.subplots(3, 1, `**`sharex=True`**`)`

<details>
<summary>Explanation</summary>

> 💡 **[.subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d)**
With `sharex=True`, the x-ticks are shared amongst the subplots. Thus, the name of the weekdays are only displayed ones. 
The `sharex` argument in `plt.subplots()` is used to control the sharing of properties among x (or y) axes. If `sharex=True`, it means the x-axis will be shared among all subplots, i.e., displayed only once. This is useful when you want all subplots to have the same x-axis, which is the case when you want to distribute the data among weekdays.
</details>
---
## Question 4
How many axes are created with the statement:
```python
fig, axes = plt.subplots(4, 4)
```
**16**

<details>
<summary>Explanation</summary>

> 💡 **[.subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d)**
The statement `fig, axes = plt.subplots(4, 4)` creates 16 axes. This is because the `subplots()` function takes two arguments: the number of rows and the number of columns. In this case, 4 rows and 4 columns are specified, so 4*4 equals 16 subplots or axes in total.
</details>
---
## Question 5
We want to create the following line plot with the values from following *pd.DataFrame* **df**.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ba7cae60-975c-45ea-9d4d-d5740d079a09/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=b867a4cdce48dbb8cbb9cef26a8f5927b1cab7344e2e264a2a0e2f587e58eece&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The *pd.DataFrame* **df** looks like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8855b98d-ce33-4262-99e5-5ab81fcf48a2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=aac77c3b0dffaf749c32ccf67350e9c87cb9b623b52314c1b410437914437924&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can you get the x-values and y-values for the **blue** line?
x-values: `df.columns`
y-values: `df.loc['Banana']`

<details>
<summary>Explanation</summary>

> 💡 **[.columns](/1867045b058343e1a66b677961515907#b56cca6739ca4649ab31ebab1ee61f83), [.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d)**
**x-values**
The x-values are the ones that are displayed on the horizontal axis, i.e., the weekdays. We see that in the DataFrame **df**, the weekdays are the column names. With `.columns` attribute we can select the column names of a DataFrame.
**y-values**
The y-values are the ones that determine how the blue line flows (if it goes up or down). Each line represents a fruit. The blue line represents the fruit Banana. We can see that each fruit has a row in the DataFrame. Thus, we want to select the Banana row which we can do by using `df.loc['banana']` or `df.iloc[1]` (Banana is the second row in the DataFrame).
</details>
---
## Question 6
Given are the following three boxplots.
In the image, select the region where 50% of the *sepal* width observations for *Versicolor* are visualized.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/74518876-1b87-44f7-b914-783cb42a8308/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI6NKAO5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmWI2uv5TeBXS1yaKZTcTHYKptsosaPiFjEG%2B4DqQ67gIhAKVKLTMjPchs7YYrAYVys2xr0F7DQR4aAI03o5ebb97QKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs0T0GPWF9Knszwjkq3AN%2BH3podTT%2FasOGTMaohRXv4apmXKF2ezNu0hXGp9s9y4BSrGiSN1ANAmw%2FWxsYi%2BPrqEZTAC50j8jHNq10kfYUKdTFjPTc5fgQxp0J5WFoUcPSxUjryes%2BAT8lyF%2FvOtYOvz77hrHVw63%2FX%2B3KM3Xeczcng5QnStMldjpS40yUeK91jz1%2F2f96KMPDQBms9rv2RMV0ZfLCAcFlTPEYaBdgKxLRla83blUzJxpb9aC7z4%2FFC%2Fz42BAVdd9W7wnuThEd8IlCrGyvT7xgsc%2FUlWM%2BCu2UIduJXONvAdOUquJJDf7LQZ%2Bb%2F7C43JgODpy7eOGid1RJvt0K%2BZ2gsZWa%2FT5%2FbLpgCS0k0aU8YaIgrSVOkss5AuJimjZ3laOQPll2tkUDiyugStxm2bX8XcJbvwtH1g8zOXd5zZkvYg9y%2BsPZZGFcQu%2Be7DJVOeE5Bm7AGmJTZTNMx7f8VmB518IJjtLV50kUj1pJW7RzagMJTK43hRklwAn4083jhJdB51L%2Ft5aAjeanackdCE6eCqnQ2nGP9KCpuNGdQWhEfrJTZcrWTSyxvSmsovHCvvQjZo%2BWIa42zLDPZcCKi5NQOvcwSmFuTFwzule9sFP7tSQxHA9aNe38%2BOuql8e%2BekFEgzC0zvfJBjqkAVaCl3GKc1E7OBJTC72%2B9RKlXpvL7S98mvStkwOR%2BqDRLEnyTWSzlYZLZUklNH7Y4GI0LeP0%2FHTCpoEBKg4q16F18LvfLUGRZhzGEUEwTEe1QGx6C6wnq8rqbAZk9eOH3MIEpaIIM%2FA7EKv6vYm0snG5GEgeYZyJm4m8Zb%2BE5geJFTlJjUmoUFHPnaCs12wX1p574zAEgzlAOm6V8X5Tsd4jfJXj&X-Amz-Signature=99017fe7dcb5ae7e00d747bf0e3dc4777d44f3afc7088757476babf5629f3fd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

> 💡 **[Boxplot](/10c38918e9a84ef79c8040d2fba85e2e#29e8af14c0a848898738443608b4a50a)**
A boxplot (also known as a whisker plot) displays a summary of the range and statistical distribution of the data. The box itself represents the interquartile range (IQR), which is the range where the middle 50% of your data points lie. This is also known as the 1st quartile (25th percentile) to the 3rd quartile (75th percentile).
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fd06423b-c4cf-4779-842a-ac6488fdb79f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCKVSNP3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD0Q0jlqBBhK%2F4vCsBHZDtPATrYArB0bMPrJKcLkZO1bAIgGRRForfPuCYrm2aTEePbkNafvOFBEKzzY9ChwvXwT9Qq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJvhFXAiaP%2F6%2FpiZQSrcAyYBw%2FNUla%2BC3%2F%2FF2Xnq8q%2Fri%2F9MhRWwONpxh4jYCXg0j0DI4tll2UteK9mj4BwIi6NOOs4FdXJ7A1sICh7cw7%2BLt6%2FAMGrx%2F0DHgFA2p5A6TwpKGHimxx9MFXiBwzQLyLKFjjv2kbRk1%2BWzoKO%2FmheTZ9N1MAj8L3Ra7sFIkfc5P%2F%2FSLAfmPwQuynOhDguYfbEzeR7X%2FOPkXAWWxRXwJYw2vkJSOcsVxHHo03BmXZKfHsIYeVd52BHxXr7clrhCn1BVqTK%2B9wRDG2pAsLpqCaaOHTCy3xbcikBqxicHu899%2BEXy61p2C2ACBxyQzDKTsQouf1RR5b%2FeuOIZ5kp%2F2sjsaql7S7i2IcfchezzJ5a6vcoqDrH74dNRuGdtF9Aos484QnLwcZWKWztIpiW1aEZ09TttJMlujZH2TnMBXeHM2hGcPGBhh0JrVwUAlh2EfcdIUDebiKNth3rkVRrJjuDJG%2FpOjoZbqPykOt9b4%2B7of3y%2F25ClPVBprHj8lyzgK3Fc0%2F%2FKNskSu8LuQV%2Bp4t9OtSSQKRFAkr65K2RjsBNauoEXbiJbNVdgu2RXwGHV9wqUiUwVNT6maauTF0FvENM%2F2%2BsSjOPMjf%2FNjr7ccAvX%2BPM6kr9BAF2kbPvrMODN98kGOqUBcweJuuTYMCjv7xDtSWrUyn6lTvBii53exIdjQv2r7GQd%2BKZcR8pXZF5r%2FrjHg2nGVYV92PpA8sDC9iCJfqfvoI2cKQawy%2FzwaYGQwYtjZeJqWXU00wm28j%2Btv6EctiXeBoxh6mEbNguKExqq9QGB5QZ8eSdleqaScvmoYDgSuYhRx3wGxrz7%2BhW%2FgA5GS3J0P%2F0I9oHq7aj83fslUEMO41TxtiTo&X-Amz-Signature=409b23c9cf4eeb40e156562c215287e74728672718a44097401d52ef411ea1d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Each quartile represents 25% of the data, thus the **box in the middle** represents 50% of the data.
</details>
---

📄 **[Quiz 11]** (subpage)
## Question 1
You have written code that trains and evaluates a **scikit-learn** model. You run the code multiple times but notice that the evaluation results are different each time.
Which of the following answers are possible explanations for this?
Check all that apply.
❌ The **classification_report** function is not deterministic.
❌ All internal parameters of the model are randomly initialized. They always differ.
❌ The model is overfitted.
❌ The model is underfitted.
✅ The **train_test_split** method shuffles the data when not using a random seed.

<details>
<summary>Explanation</summary>

> 💡 **[classification_report](/9e4a78074aea481ca4c75e506d4671c7#edb6797681d048229c93d351b77b476b), [train_test_split](/9e4a78074aea481ca4c75e506d4671c7#4929175cb8d34b8f97fbaca1a2271458)**
❌ **Incorrect**, the `classification_report` function from scikit-learn is deterministic. Given the same input, it will always produce the same output. The function calculates metrics like precision, recall, and F1-score based on the input predictions and true values.
❌ **Incorrect**, while it's true that some machine learning models initialize their parameters randomly, this usually does not lead to significantly different results when training on the same data. However, there are exceptions, such as neural networks, which can end up in different local minima due to random initialization.
❌ **Incorrect**, overfitting refers to a model that has learned the training data too well, to the point where it performs poorly on unseen data. Overfitting would not cause the model to yield different results each time it's run.
❌ **Incorrect**, underfitting refers to a model that has not learned the patterns in the training data well enough, and thus performs poorly on both the training and test data. Like overfitting, underfitting would not cause the model results to vary each time it's run.
✅ **Correct**, the `train_test_split` function from scikit-learn shuffles the dataset before splitting it into training and test sets. If you don't specify a random seed (`random_state` parameter), it will use a different seed each time, resulting in a different split and potentially different results. To get the same results each time, you can set the `random_state` parameter to a fixed number.
</details>
---
## Question 2
You are given the following confusion matrix. The meaning of the rows and columns is the same as in the confusion matrix that can be created with scikit-learn.
For which of the three classes does the predictor perform best? Click on the corresponding image of the class (row image or column image both work).
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f03fe3a2-dff9-4dbb-a4ee-502ad31480aa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BMTFPUH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCWkFhrioeiOwt7tr5G%2F3Fe6AJEnN6t3lqQcWryzQf7RwIhAJ%2BYNzI19l61ZeWaiMFg0e65Ps7HG6UJKnPWm1FnsvhnKv8DCCcQABoMNjM3NDIzMTgzODA1Igzs2d6P2Pt4%2FV8YsZkq3AN8PfzJIt2pHNW2%2FkVfGGUjrrLW3G3gnyQzCKFOewb8NHYTN6%2F4VZ6XQrDueqxYJMHePXNAcPOjyDt4LivfRNkGN83cZyKaeNdPmUqMNlZ9X67ZDLJ65RggaBnY%2BWiXuzbd78P0tc0oTvrEU%2Bz1tkiyMkfLabksMgORGKNReQY%2BLHvjETe2ZwtlkmxhdMRdKUYmsYZAfSdAPwmMjDTWgdW2gnmFZOOnjMSGGGMyvXfghztrxsDrGjp0W5i%2F7iHE0VXNWqiDrDxAX3NP4TIVCB92zLTATUUXZWSKDUAjXgglYnB1Ua3vKa8qruKfniKt2Q6M7AlJDH%2F6nNzez9Zy%2FRDhpf%2F%2BL%2F2uUIMfMdcVozq5%2BWrjyn4IUA24mcbKWnq3N2RcYi6Poe3ya3CSnqHLj6iEJLr1OxoYjkGjvtfrhEBYcIfGXaJr6Jn%2F%2BKHCt7cde2EvfjiVdjTjGwZaksPiH%2F9exBef0uM%2FR5%2B%2B6%2BHILQA0NelwBMR2XCWXfg5gQtcowThIxNJ2Djegn4lPZySfpsNSRwz1bZF75dKN9FBMsWdhvnPeu1S1Shn%2BshC62CbYShCp1ReCnF57eTutRpaSGd6MW2D4Ee5Bh58HMnecuHrmOyyJnReKok0fPG163jC2zvfJBjqkAZQK9FOtz7tmYHpJvaYmE6vIgHBifhiXpKGwlGPxAomhPAKf4%2F6JeJnTGo7zMK74Qw9l02G0AWePSZ%2F5c2%2FG51nfj4tDMlg48IqJcXoIm4NvZGOdw98Gp9Nn3fQvxF7qvjVT9lXw%2BaRjpMSCG1tztKwe1au34WLpus%2BoIngvXYiq2AEPhko4jUGwbvmCVvPoa1Dfy2PS1zv94WZ0lDZU%2BsOqNn18&X-Amz-Signature=0af2925de6d8cee744ad70d8a0bcf3a626afbbe7d5128f777745320f03b6797c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

> 💡 **[Confusion matrix](/3ca737faa7034fb9b1150be74f7f4430#88d2ed1628dd4d95be5744e5cbce0680)**
A confusion matrix is a table layout that allows visualization of the performance of an algorithm. Each **row** of the matrix represents the instances in a **predicted** class while each **column** represents the instances in an **actual** class. Thus, the **predicted** labels are on the **x-axis** and the **actual** labels on the **y-axis**.
The **diagonal** elements represent the number of points for which the predicted label is **equal** to the true label, while **off-diagonal** elements are those that are **mislabeled** by the classifier. The higher the diagonal values of the confusion matrix the better, indicating **many correct predictions**.
So we can interpret the confusion matrix in the exercise as follow (we assume that accuracy is the metric we foucus on):
- **Animal 1:** Out of 30 animals, the classifier has identified 10 (33%).
- **Animal 2:** Out of 33 animals, the classifier has identified 30 (90%). ← highest accuracy
- **Animal 3:** Out of 28 animals, the classifier has identified 15 (53%).
</details>
---
## Question 3
The confusion matrix of arbitrary size |C| × |C| (where *C* is the number of classes) of the results of the evaluation of a classifier has only 0 (zeros) in the diagonals. There is at least one sample for each class, but the classes are unbalanced (there is not the same number of samples in every class).
Which of the following statements is correct?
✅ The classifier was **always** wrong.
❌ This situation can never happen.
❌ Every class was predicted at least once (regardless of whether or not that prediction was correct).
❌ The classifier was **always** right.

<details>
<summary>Explanation</summary>

> 💡 **[Confusion matrix](/3ca737faa7034fb9b1150be74f7f4430#88d2ed1628dd4d95be5744e5cbce0680)**
✅ **Correct**, a confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of data for which the true values are known. In the confusion matrix, the **diagonal** from the top left to the bottom right represents the **correct predictions** made by the classifier, while the **rest** of the matrix represents the **errors**.
If all the diagonal elements are zero, it means that the classifier never predicted the correct class. Thus, the classifier was always wrong.
❌ **Incorrect**, because this situation can happen if the classifier is not trained properly or if it's not suitable for the given data.
❌ **Incorrect**, because every class being predicted at least once doesn't necessarily mean that those predictions were correct. The question states that all diagonal elements are zero, which means no class was predicted correctly.
❌ **Incorrect**, because the classifier was not always right. In fact, it was always wrong as explained above.
</details>
---
## Question 4
Which of the following statements are **True**?
❌ Unsupervised learning is preferable over supervised learning because we don't need to label the training data.
✅ Before making a train-test-split it may be a good idea, depending on the data set, to shuffle the samples in the dataset to reduce potential bias in the classifier.
✅ When training a classifier, the data quality of the training data is important, because the classifier does not learn how to deal with wrong data.
❌ In a supervised learning approach, using all of our labeled data for training a classifier is preferable, because we then can assume that the classifier has a good accuracy for classifying additional samples.

<details>
<summary>Explanations</summary>

> 💡 **[Supervised vs. unsupervised learning](/9b19eda74fac4ffb8e48b36dde3b47a4)**
❌ **Incorrect**, unsupervised learning is not necessarily preferable over supervised learning just because we don't need to label the training data. The choice between supervised and unsupervised learning depends on the specific problem and the available data. For instance, if we have a large amount of labeled data and we want to make predictions, supervised learning would be a better choice.
✅ **Correct**, before making a train-test-split, it's a good practice to shuffle the samples in the dataset. This is because the order of the samples can contain biases or patterns that may influence the performance of the classifier. For example, if the samples are sorted by their labels, the classifier might only learn to predict a single class if all samples of a class are in the training set.
✅ **Correct**, the quality of the training data is indeed important when training a classifier. If the training data contains errors or inconsistencies, the classifier might learn wrong patterns and therefore make incorrect predictions. This is especially true for supervised learning approaches, where the classifier learns from the given labels.
❌ **Incorrect**, using all of our labeled data for training is not necessarily preferable. It's important to hold out a portion of the data (known as a test set) to evaluate the performance of the classifier on unseen data. If we use all our data for training, we might overfit the classifier to the training data, meaning it performs well on the training data but poorly on new, unseen data. This would give us an overly optimistic view of the classifier's performance.
</details>
---
## Question 5
Which of the following statements about the Fruits dataset is correct?
- It has four classes.
- It is a dataset for binary classification.
- It is about the color classification of fruits.
- It can not be used to train a k-Nearest Neighbors classifier.

<details>
<summary>Explanation</summary>

> 💡 **[Fruits dataset](https://www.kaggle.com/datasets/shivmuratgupta/fruit-data)**
✅ **Correct**, it has four classes: Apple, Mandarin, orange and Lemon.
❌ **Incorrect**, because binary classification means that there are only two possible categories or outcomes. However, there are more than two types of fruits in the dataset.
❌ **Incorrect**, it is abotut he classficiation of the *type* of fruit.
❌ **Incorrect**, the kNN algorithm is a type of machine learning algorithm that can be used for both classification and regression tasks. As the Fruits dataset contains labels (and thus we are dealing with supervised machine learning), we can use the kNN algorithm
</details>
---
## Question 6
Which of the following statements regarding k-Nearest Neighbors are true and which are false?
❌ k-Nearest Neighbors only works if the data is 2-dimensional
❌ k-Nearest Neighbors is an unsupervised classification algorithm
❌ We can't use 1 (one) as our value for k
✅ In the case of binary classification it is a good idea to use an uneven (odd) number for k
❌ In k-Nearest Neighbors the absolute distance of every of the k nearest neighbors (for k+1) must not be considered for the prediction
✅ k-Nearest Neighbors is deterministic, if the nearest neighbor can be identified unambiguously for every sample.

<details>
<summary>Explanation</summary>

> 💡 **[kNN algorithm](/4e55bc27409940e98f9a060821d07644)**
❌ **False**,** **k-Nearest Neighbors (k-NN) can work with data of any dimensionality, not just 2-dimensional data. The algorithm calculates the distance between data points in a multi-dimensional space.
❌ **False**, k-NN is a supervised learning algorithm, not unsupervised. It requires labeled data to function properly. It uses these labels to classify new, unseen instances based on their proximity to known instances.
❌ **False**,** **We can indeed use 1 as our value for k. In this case, the algorithm classifies an instance based on its closest neighbor.
✅ **True**,** **using an odd number for k in binary classification can help avoid ties, i.e., situations where an equal number of neighbors belong to each class.
❌ **False**, the distance of each of the k nearest neighbors does matter in some variations of k-NN. For example, in a weighted k-NN, the influence of a neighbor on the classification of a new instance is weighted by the inverse of its distance to the new instance.
✅ **True**, k-NN is deterministic in the sense that, given the same dataset and the same parameters, it will always produce the same classification for a given instance. However, this is assuming that the nearest neighbor can be identified unambiguously for every sample. If two neighbors are at the same distance, the classification might depend on the order of the data in the dataset.
</details>
---

---

