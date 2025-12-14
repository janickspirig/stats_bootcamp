---
title: "Quiz 1"
notion_id: "b87e848d-dd26-4359-862b-2ad1180ca472"
notion_url: "https://www.notion.so/Quiz-1-b87e848ddd264359862b2ad1180ca472"
exported_at: "2025-12-13T23:22:45.593245+00:00"
---

# Quiz 1

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
