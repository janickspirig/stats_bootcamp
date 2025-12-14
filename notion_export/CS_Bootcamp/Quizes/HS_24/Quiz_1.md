---
title: "Quiz 1"
notion_id: "17074ffd-3319-8080-ac5f-c2835324b65a"
notion_url: "https://www.notion.so/Quiz-1-17074ffd33198080ac5fc2835324b65a"
exported_at: "2025-12-13T23:03:22.149476+00:00"
---

# Quiz 1

## Question 1
Can you *add* a variable using the + operator of type **int** to a variable of type **float**?
- [ ] Yes.
- [ ] Depends on content of the variables.
- [ ] No.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Mathematical operations](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a)**
✅ **Correct**, in most programming languages, including Python, you can add an integer to a float using the `+` operator. The result will be a float. This is because when you combine an integer and a float, the integer is automatically converted to a float to ensure the operation can be performed without losing precision.
**Example:**
```python
int_var = 5      # This is an integer
float_var = 3.2  # This is a float
result = int_var + float_var  # Adding an int to a float

print(result)  # Output will be 8.2, which is a float
```
- In this example, `int_var` is an integer with a value of 5, and `float_var` is a float with a value of 3.2. When you add them together, the result is 8.2, which is a float.
❌ **Incorrect**, the ability to add an `int` to a `float` does not depend on the specific values of the variables. As long as one is an integer and the other is a float, they can be added together, and the result will be a float.
❌ **Incorrect**, you can indeed add an integer to a float. The operation is straightforward and supported by most programming languages, including Python. The result will be a float, as explained above.
</details>
---
## Question 2
The following can be seen on the famous St. Gallen binary clock:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cba5432c-7dc8-4922-afae-f422d4655e2f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIJLSWLF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCH4GO%2B2xCAMF%2BX9Vhf6xLKC%2FdmKpPCOrerQ0CsZVsQ2AIgRca2I1CrQZdQE8HMmg92EEeKsOJm6L1m7PiyXn883Hwq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDHQqTaa69arvb6k0USrcA9iuBdZRjb83YxpFAPbn96eHvYo2QV5Ae2NdgPsv7QoTjMwF4qIgo5bnGOWFmg88DIeaaFio9Rx%2FKw%2BgZ6aqQZeQBB7HHHKWwDK2BVnLALwDBFwE8TGqCjCw2pxkMY6jlOC4tlAszOKR%2FNsFZjWJYjCOix2k1ew%2B%2F9mOCt4t7uVL0M4WRrojQeyE4D3epsSpOpYck3Zl9nB26wfhEN%2B56IBVtnYEkjgW5LSnf01dKolD30ADtlnLXAHi%2BrbSVUEQP6b9pFD3JKzK%2BqVfeeyGEBYE5IgHg4ggqdnEGC5DCRQKe6L2qvrvuQ2HHilbsANmJRdkNmFeIF3dGjKpl1mlVtppBmlvID6UG1%2B9jt0PhSLa6RtzxsHgXwHJUByRYwLqmaAg0WnJcl9YtGLTArS5jVUMkqcCmaiMyB063wnWhCxry%2FqMQjI5US1alNGSP7Ja1DCnH7DLGPOjMrEbo%2F1bnDoyqF5DUhN5EQJ8aYZDZpXhrK7eb6stybWI1VYyVBQ1%2FIVjlXXsLuRKxuny6ak07bYRSZnhyMQigNsxYQMjN%2B%2BykIInm1icrJfDeMyaCYBFMK%2BtHBbxc4rFxxmMFjawI%2FKQuc14zykl11Jw2cDas%2BiCrFCeL28EDYgyO%2BVXML3O98kGOqUBbkouy6ERfRUYsVVI6zesL47Niq51z7oc5jzPs1YEdstoY%2FgYVMvuDuLw3cxeQT3OyTwT6q%2F9LiJkbAjNz08D%2FLgp4X1t4UZZNjGOa6%2FTMwWPu2MMJPKtUEgw4omLBqJku6XBh6KSMHy4ssX0uVQHAsV6ZodaNGDOFnMbgnTGiRrAUG7yQYfVjZ1Om8sctwaxgWdBsHeM39obdMXKVNtd4dEmb%2Fa7&X-Amz-Signature=de654d3a7b0215d0b7c09eac68ce02fdfda8e50b8ecf35f60874df85725f25a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
What time is it there (in hours:minutes:seconds)?
- [ ] 08:10:59
- [ ] 08:12:59
- [ ] 05:06:14
- [ ] 05:06:45

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Convert binary into decimal](/2b21ebb6314545d48382bb68713e5145)**
The image in question depicts the St. Gallen train station clock, which uses binary coding to display hours, minutes, and seconds. In this case, each row on the clock represents a different unit of time in binary form.
To understand the correct answer, we need to know how to read binary numbers:
- **First row (Hours):** The binary number is `00101`. To convert it to decimal (the number system we use daily), you start from the right, with each digit representing a power of 2. So the calculation is:
- `0*2^4 = 0`
- `0*2^3 = 0`
- `1*2^2 = 4`
- `0*2^1 = 0`
- `1*2^0 = 1`
- **Total hours:** 0 + 0 + 4 + 0 + 1 = **5 hours**
- **Second row (Minutes):** The binary number is `000110`. The same conversion process results in: 
- `0*2^5 = 0`
- `0*2^4 = 0`
- `0*2^3 = 0`
- `1*2^2 = 4`
- `1*2^1 = 2`
- `0*2^0 = 0`
- **Total hours:** 0 + 0 + 0 + 4 + 2 + 0 = **6 minutes**
- **Third row (Seconds):** The binary number is `101101`. Converting this to decimal gives:
- `1*2^5 = 32`
- `0*2^4 = 0`
- `1*2^3 = 8`
- `1*2^2 = 4`
- `0*2^1 = 0`
- `1*2^0 = 1`
- **Total seconds:** 32 + 0 + 8 + 4 + 0 + 1 = **45 seconds**
Therefore, the correct answers are:
- ✅ **5 Hours**: The binary number `00101` equals 5 in decimal.
- ✅ **6 Minutes**: The binary number `000110` equals 6 in decimal.
- ✅ **45 Seconds**: The binary number `101101` equals 45 in decimal.
</details>
---
## Question 3
Given is a simple CPU with two 3-bit registers and the following instructions:
**CPU**
| **Instruction** | **Explanation** |
| --- | --- |
| **00nnnx** | **Insert.** The 3-bit binary number *nnn<sub>2</sub>* is inserted into register *x*. |
| **01xy** | **Copy.** The content of register *x* is copied into register *y*. |
| **10xy** | **Add.** The result of *R\[x\] + R\[y\]* is stored in register *y*. |
| **11x** | **Clear.** The content of register *x* is set to 000. |
Please write a program using the available instructions. The program should **insert** the value 2 (in the decimal system) into register 0, **copy** the value to register 1, then **add** the registers and store the result into register 0, and finally **clear** register 1.
For easier readability you may use one blank between each instruction (e.g., 110 1011 0110). Alternatively, you may use no blanks at all. Do NOT insert spaces within instructions.
The program is:
```markdown
000100 0101 1010 111, 000100010110101111, 000100 0101 1010 111
```

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[CPU execution](/e6a0f693f77345a09aa025bc0e86e23b)**
Let's go through the correct program step by step:
1. **000100** - **Insert 2 into register 0**:
- `00` indicates an insert operation.
- `010` is the binary representation of the decimal number 2.
- `0` specifies register 0.
- This instruction inserts the value 2 into register 0.
1. **0101** - **Copy register 0 to register 1**:
- `01` indicates a copy operation.
- `0` specifies the source register (register 0).
- `1` specifies the destination register (register 1).
- This instruction copies the value from register 0 to register 1.
1. **1010** - **Add register 0 and register 1, store in register 0**:
- `10` indicates an add operation.
- `0` specifies the first register (register 0).
- `1` specifies the second register (register 1) and also the destination register.
- This instruction adds the values in register 0 and register 1, and stores the result in register 0.
1. **111** - **Clear register 1**:
- `11` indicates a clear operation.
- `1` specifies register 1.
- This instruction sets the content of register 1 to `000`.
</details>
---
## Question 4
Given is the arithmetic Modulo operator % from Python. What is the result of the following computation stored in the variable z?
```python
z = 37 % 9
```
- [ ] 1

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c)**
1. **Understanding the Modulo Operator ****`%`****:**
- The modulo operator `%` in Python is used to find the remainder of the division of one number by another.
- For example, if you have `a % b`, it means you divide `a` by `b` and take the remainder of that division.
1. **The Code: ****`z = 37 % 9`****:**
- Here, we are calculating `37 % 9`.
- This means we divide 37 by 9 and find the remainder.
- When you divide 37 by 9, the quotient is 4 (because 9 times 4 is 36) and the remainder is 1 (because 37 minus 36 is 1).
1. **Result:**
- Therefore, the result of `37 % 9` is 1, which is stored in the variable `z`.
✅ **Correct**, the result of the computation `37 % 9` is indeed 1, as it represents the remainder of the division.
</details>
---
## Question 5
Given is the following snippet to compute the volume of a pyramid:
```python
b = 3.0
h = 2.0
volume = (1/3) * b ** 2 * h

print("The volume is", volume)
```
Mark all correct statements regarding this snippet.
- [ ] The computation makes sure that the values of *b* and *h* are valid.
- [ ] The computation is correct.
- [ ] Generally, the computation would also work if we put in a string instead of a float for the variables *b* and *h*.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Mathematical operations](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a)**
❌ **Incorrect**, the code does not include any checks to ensure that the values of `b` and `h` are valid. It simply assigns the values `3.0` and `2.0` to `b` and `h`, respectively. If you wanted to ensure the values are valid (e.g., positive numbers), you would need to add additional checks in the code.
✅ Correct, the formula used in the code correctly calculates the volume of a pyramid. The formula
$$
 \frac{1}{3} \times \text{base area} \times \text{height} 
$$
is correctly implemented as `(1/3) * b ** 2 * h`
❌ Incorrect, if you try to use a string instead of a float for `b` or `h`, the code will raise an error. This is because mathematical operations like exponentiation (`*`) and multiplication () cannot be performed on strings. For example, if `b` were a string like `"3.0"`, the operation `b ** 2` would result in a `TypeError`.
</details>
---
## Question 6
Can you add (+) a variable of type *string* to a variable of type *float*?
 Yes but the resulting data type can’t be inferred.
- [ ] Yes, and the result is of type *float*.
- [ ] No.
- [ ] It depends on the content of the *string* variable.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Mathematical operations](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a)**
In programming, different data types have specific rules about how they can interact with each other. Let's look at the options:
1. **Can you add (+) a variable of type *****string***** to a variable of type *****float*****?**
- **✅ No.**
- This is the correct answer because in most programming languages, including Python, you cannot directly add a string to a float. These are two different data types, and the addition operation is not defined between them. A string represents text, while a float represents a number with decimal points. Trying to add them together would result in a type error because the computer doesn't know how to combine text with a number in this context.
1. **Yes but the resulting data type can’t be inferred. ❌**
- This is incorrect because the operation itself is not allowed, so there is no resulting data type to infer. The program would throw an error before any result is produced.
1. **Yes, and the result is of type *****float*****. ❌**
- This is incorrect because adding a string to a float is not a valid operation. Therefore, you cannot get a result of type float. The operation would result in an error.
1. **It depends on the content of the *****string***** variable. ❌**
- This is incorrect because the content of the string does not change the fact that you cannot directly add a string to a float. Even if the string contains numeric characters, it is still treated as text. You would need to convert the string to a float first before performing the addition.
To perform an operation like this, you would need to convert the string to a float if it contains a numeric value. Here's an example in Python:
```python
string_value = "3.5"  # This is a string
float_value = 2.0     # This is a float

# Convert the string to a float before adding
result = float(float_value) + float(string_value)
print(result)  # Output: 5.5

```
- In this example, `string_value` is a string that looks like a number. We convert it to a float using `float(string_value)` before adding it to `float_value`. This way, both operands are of the same type (float), and the addition is valid.
</details>
---
## Question 7
Which values do the variables y and z have *after* the execution of the following script?
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
- [ ] y = True, z = False
- [ ] y = False, z = False
- [ ] y = False, z = True
- [ ] y = True, z = True
- [ ] None of the above.

<details>
<summary>Explanation </summary>

> 🧑‍🏫 **[Logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)**
Let's go through the script step by step to understand the final values of the variables `y` and `z`.
1. **Initial Assignments:**
- `x = 42`: The variable `x` is assigned the value `42`.
- `y = True`: The variable `y` is assigned the boolean value `True`.
- `z = not y`: The variable `z` is assigned the value `not y`, which is `not True`, resulting in `False`.
1. **First Conditional Block (****`if y:`****):**
- Since `y` is `True`, the code inside the `if` block is executed:
- `x = x / 2`: This divides `x` by `2`, so `x` becomes `21.0`.
- `y = not y`: This changes `y` to `not True`, which is `False`.
1. **Second Conditional Block (****`if x < 42:`****):**
- Now, `x` is `21.0`, which is less than `42`, so the code inside this `if` block is executed:
- `z = not y`: Since `y` is `False`, `not y` is `True`, so `z` becomes `True`.
Now, let's evaluate the answer options based on the final values of `y` and `z`:
- ❌ **y = True, z = False**: This is incorrect because `y` is `False` and `z` is `True`.
- ❌ **y = False, z = False**: This is incorrect because `z` is `True`.
- ✅ **y = False, z = True**: This is correct because after executing the script, `y` is `False` and `z` is `True`.
- ❌ **y = True, z = True**: This is incorrect because `y` is `False`.
- ❌ **None of the above**: This is incorrect because the correct answer is provided in the options.
</details>
---
## Question 8
Which *data type* do the variables *x*, *y*, and *z* contain?
```python
x = "22"
y = int(x) + 2
z = int(x) / 3
```
Drag and drop the variables to their respective data type category.
**int**
✅ y
**float**
✅ z
**str**
✅ x

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb)**
Let's break down the code and understand why each variable is categorized under its respective data type.
1. `x = "22"`
- This line assigns the string `"22"` to the variable `x`.
- In Python, anything enclosed in quotes (single or double) is considered a string, which is a sequence of characters.
- Therefore, `x` is of type `str` (string). ✅
1. `y = int(x) + 2`
- Here, the function `int(x)` is used to convert the string `"22"` into an integer `22`.
- After conversion, the integer `22` is added to `2`, resulting in `24`.
- Since the result of this operation is an integer, `y` is of type `int` (integer). ✅
1. `z = int(x) / 3`
- Similar to the previous line, `int(x)` converts the string `"22"` into the integer `22`.
- This integer is then divided by `3`.
- In Python, the division operator `/` **always** results in a float, even if the division is exact.
- Therefore, `z` is of type `float` (floating-point number). ✅
To summarize:
- `x` is a string (`str`) because it holds the value `"22"` in quotes.
- `y` is an integer (`int`) because it results from adding two integers.
- `z` is a float (`float`) because division in Python results in a floating-point number.
</details>
---

