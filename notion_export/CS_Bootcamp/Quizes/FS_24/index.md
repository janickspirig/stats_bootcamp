---
title: "FS 24"
notion_id: "066ac518-2d47-4b6e-80f8-44e313943439"
notion_url: "https://www.notion.so/FS-24-066ac5182d474b6e80f844e313943439"
exported_at: "2025-12-13T23:08:32.639890+00:00"
---

# FS 24

---
📄 **[Quiz 1]** (subpage)
## Question 1
Welchen Datentyp (data type) haben die Variablen x, y, und z nach der Ausführung des Programms?
```python
x = str(22)
y = int(x) + 12.0
z = int(x) / 3
z = int(z)
```
Ordnen Sie die Variablen den jeweiligen Datentyp zu (drag and drop).
- `x`: `str`
- `y`: `float`
- `z`: `int`

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb)**
Let’s break down the code line-by-line:
- `x = str(22)`
The number `22` is converted to a string using the `str()` function, so the data type of `x` is a string (`str`).
- `y = int(x) + 12.0
`The string `x` is converted to an integer using the `int()` function, and then added to the float `12.0`. Since an integer plus a float results in a float, the data type of `y` is a float (`float`).
- `z = int(x) / 3`
The string `x` is converted to an integer, which is then divided by the integer `3`. In Python, division always results in a **float**, even if the numbers being divided are both integers.
- `z = int(z)`
Finally, the float `z` is converted back to an integer using the `int()` function. This results in the decimal part of the number being dropped. Therefore, the data type of `z` is an integer (`int`).
<details>
<summary>*Details line-by-line*</summary>

|  |  | x | y | z |
| --- | --- | --- | --- | --- |
| 1 | `x = str(22)` | “22” |  |  |
| 2 | `y = int(x)+12.0` |  | 24.0 |  |
| 3 | `z = int(x) / 3` |  |  | 7.333333 |
| 4 | `z = int(z)` |  |  | 7 |
</details>
</details>
---
## Question 2
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
	x = not z
else:
	z = not z
	x = x
```

✅ x = False, z = True
❌ x = 21, z = False
❌ x = True, z = True
❌ x = 21, z = True
❌ *Keine der anderen Antworten.*
❌ x = True, z = False
❌ x = 84, z = False
❌ x = False, z = False

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)**
Let's break down the code:
- Line 1: `x = 42` assigns the value **42** to the variable `x`
- Line 2: `y = True` assigns the value **True** to the variable `y`
- Line 3: `z = not y` assigns the opposite of `y` (which is **True**) to `z`, so `z` becomes **False**
- Line 5: Since `y` is **True**, the code inside the `if` block is executed (Line 6-7)
- Line 6: `x` is divided by 2, becoming **21**
- Line 7: `y` is changed to the opposite of its current value (**True**), becoming **False**
- Line 11: Since `x` (**21**) is less than 42, the code inside the `if` block is executed
- Line 12: `z` is changed to the opposite of `y` (which is **False**), so `z` becomes **True**
- Line 13: `x` is changed to the opposite of `z` (which is **True**), so `x` becomes **False**
So, after the execution of the code, `x` is **False** and `z` is **True**.
</details>
---
## Question 3
Welchen Datentyp hat das Ergebnis, wenn ein int-Wert durch einen anderen oder den gleichen int-Wert geteilt wird? Gehen Sie davon aus, dass der Teiler (Divisor) niemals 0 ist.
❌ Das hängt von beiden konkreten Werten ab.
❌ **int**
✅ **float**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Mathematical operations](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a)**
In Python, division of integers results in a **float** value, even if the divisor evenly divides the dividend. For example, `4 / 2` will yield `2.0`, not `2`.
</details>
---
## Question 4
Was gibt das folgende Programm aus?
```python
a = 'c'
b = 'x'
b = a + c
print(a + a + b + 'x')
```
❌ *ccccx*
❌ *x''x'a*
❌ *c'c'x'c*
❌ *cccc'x'*
❌ cxcxcx
✅ Nichts, weil es mit einem Fehler abbricht.

<details>
<summary>Explanation</summary>

The program initializes two variables, `a` and `b`, with the strings `'c'` and `'x'` respectively. Then, it attempts to assign to `b` the result of concatenating `a` and `c`. However, `c` is not defined in this context, so the program will raise a `NameError` and terminate before it can reach the `print` statement.
Here is the explanation for each option:
- **`ccccx`** - This would be the output if `c` were defined as `'c'` before the third line. However, since `c` is not defined, the program will raise a `NameError`.
- **`x''x'a`** - This would be the output if `c` were defined as `''` (an empty string) before the third line. Again, since `c` is not defined, the program will raise a `NameError`.
- **`c'c'x'c`** - This output does not match the format of the `print` statement, even if `c` were defined.
- **`cccc'x'`** - This would be the output if `c` were defined as `'c'` before the third line and if the `print` statement were `print(a + a + b + "'x'")`. However, since `c` is not defined, the program will raise a `NameError`.
- **`ccccxcx`** - This would be the output if `c` were defined as `'c'` before the third line and if the `print` statement were `print(a + a + b + 'x' + c + 'x')`. However, since `c` is not defined, the program will raise a `NameError`.
- **`Nothing, because it breaks with an error`** - This is the correct answer. Since `c` is not defined, the program raises a `NameError` when it tries to execute `b = a + c`.
</details>
---
## Question 5
Markieren Sie alle Ausgaben, die das folgende Programm erzeugt.
```python
x = 10

if x >= 20:
	print('a')
elif x > 15:
	print('b')
elif x > 10:
	print('c')
else:
	print('d')
if x < 11:
	print('e')
else:
	print('f')
```
❌ a
❌ b
❌ c
✅ d
✅ e
❌ f

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)**
The code snippet is a series of conditional statements. Here's what's happening:
- `x = 10` assigns the value 10 to the variable `x`.
- The `if` statement checks if `x` is greater than or equal to 20. If true, it would print 'a'. But since `x` is 10, this condition is not met, thus the code inside the if-statement is not executed.
- The `elif` (else if) statement checks if `x` is greater than 15. Again, this condition is not met, so the code inside the elif-statement is not executed.
- The next `elif` checks if `x` is greater than 10. This condition is also not met. 
- The `else` statement is executed because none of the above conditions (if- and elif-statements) are met. **It prints 'd'.**
- Inside the `else` block, there's an `if` statement that checks if `x` is less than 11. Since `x` is 10, this condition is met and '**e' is printed.**
- The `else` statement within the `else` block would only be executed if `x` was not less than 11, but this is not the case here.
So, the printed outputs are 'd' and 'e'.
</details>
---
## Question 6
Gegeben ist der Python *Modulo-Operator %*. Welcher Wert ist nach der Ausführung in z gespeichert?

z = 418,36 % 6

**4,36**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c)**
The Modulo operator **`%`** in Python returns the remainder of a division. In this case, `418.36 % 6` means "what is the remainder when 418.36 is divided by 6?"

The division of 418.36 by 16 is 69.726 with a remainder of 4.36. So, when we use the Modulo operator, it ignores the quotient (69.726 in this case) and returns only the remainder (4.36).
Therefore, `z = 418.36 % 6` will give `z = 4.36`.
</details>
---
## Question 7
Was passiert bei der Ausführung des folgenden Programms? Markieren Sie alle korrekten Aussagen!
```python
x = 5

while x <= 7:
	print("Yellow")
	x = x + 1
	print("Black")
print("Yellow")
```
✅ *Yellow* wird 1x mehr als Black ausgegeben.
❌ *Yellow* wird unendlich oft ausgegeben, d.h. dass die **while**-Schleife nie abbricht.
✅ *Yellow* wird 4x oder weniger oft ausgegeben.
❌ *Black* wird in jeder Iteration der **while**-Schleife ausgegeben, darum kann man nicht sagen, wie oft genau Black ausgegeben wird.
❌ *Yellow* wird niemals ausgegeben.
❌ Man kann nicht genau sagen, wie oft *Yellow* ausgegeben wird.
❌ *Yellow* wird genau 1x ausgegeben.
❌ Das Programm hat einen SyntaxError.
✅ *Black* wird genau 3x ausgegeben.
❌ Die Bedingung der **while**-Schleife wird nie True, d.h. ihr Inhalt (suite oder body) wird nie ausgeführt.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[While loop](/5b0832dbf9454eb1941b7632e68a9abb#b52a89fc421f4692bdc9c73a764ca650)**
Check below to follow the loop execution loop-by-loop.
<details>
<summary>1st iteration → `x = 6`</summary>

`x = 5`
`while 5 <= 7` → **True**
`print("Yellow")` → **“Yellow”**
`x = 5 + 1` → **6**
`print("Black")` → **“Black”**
</details>
<details>
<summary>2nd iteration → `x = 7`</summary>

`x = 6`
`while 6 <= 7` → **True**
`print("Yellow")` → **“Yellow”**
`x = 6 + 1` → **7**
</details>
<details>
<summary>3rd iteration → `x = 8`</summary>

`x = 7`
`while 7 <= 7` → **True**
`print("Yellow")` → **“Yellow”**
`x = 7 + 1` → **8**
</details>
<details>
<summary>4th iteration</summary>

`x = 8`
`while 8 <= 7` → **False**
</details>
`print("Yellow")` → **“Yellow”**
We can see that in the first three iterations of the while loop the condition of `x <= 7` is met and thus Python jumps into the body of the while loop and prints **Yellow** and **Black**.
This happens exactly three times. After the third iteration  `x` is equal to 8 and thus greater than 7. As a result, Python skips the while loop and jumps to the first line after the loop where **Yellow** is printed again. 
In conclusion, **Yellow** is printed four times and **Black** is printed three times. Thus, **Yellow** is printed one more time than **Black**.
</details>
---
## Question 8
Das Bild zeigt die St. Galler Bahnhofsuhr. Diese stellt die Stunden (1. Zeile), Minuten (2. Zeile) und Sekunden (3. Zeile) kodiert im Binärsystem dar. Wie spät ist es im dargestellten Bild?
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/70b23ec3-231e-4f47-9662-e005179ddbe6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHC2JSEI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD6pyLNtW62JxrB62WXVIk%2F7cNN6MNjrPUrsa%2BMZou4rQIgKpZK%2Bqvss3kgXkJmUMvHsGrkyk9w%2FOKQ32DG8yza9foq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDO7ZftvRgo5Yx4zuaircAxFqAO8aT3pHtx93Z3PVhS6DXZzHBHF0tCcOKhgXOtRkqQl6CkUNz5puVdRMpYsrQ5ZJcBc9TKa%2B3RtNo%2BoOu3VNy2%2F9ZkgHhtY%2BEvYm%2F8o2RgblweBO%2Fs8mAcWwFlV%2F%2B5t%2BQyU6e8Llxa2%2BP2MMvXPo0%2Fc%2FLZ8SvkXl0MjX4lkgv8CYlDqLXYCDQWyFsuKzMO6DNQQG3LKsqdlWHP%2B%2BTmSOLQb%2BF63JTBIUTH3bSGdi5GArbeytPFFgVBSPpbFRgDQPXLgyAVYG%2B649g5wQ2%2FuFl4ymnChC86agWT0BbYgJssnj9gQuWmXXBt%2BqoO4Nq6JXdzhHnN%2FxJrQKpRtkTqV7IbUbYH98Ey4UjQlWYyHeJBo9NBTcpjI2hqsch1ZRBRC%2BHVSD4aEtiPGbGP6T2s8R7MTvAKnMGRv8oAJ4cSDrW1oa11yT4ILCmYReuBkcoGR%2Fc4fM5fVxv%2FDUpM8trD8LQCrWgBTtqXuGkYZtMzNQpgwJOzoNtsmlIpJOQ8JlaHbHnlljxB%2BnZ6CSSjZEgnT4lsxu%2FkdxgSPbRkJ%2Fl1l%2BAjyEx5oQ58GijHD%2BwzHSMg32Pc4qrvcwREyvaSthZWfjiPxTrnuCABD4PIG4vnkYk8tChmSmefKjcOZiMNbO98kGOqUBg%2FwwWyMV%2BErU3Y1XSefmrwEpKkbk3Wtr4cEbd1A8lguoMcZDrEW5D8i0DrIk0%2FlzCvQbXJRZLvO3X1gGBsbvyP75KkzBZLWyluSQbZp%2FRFtBs5GR1ohl5mTbZA0EW2Vt1rpAu473cEdXEitP%2BuDGA%2BoOm6vMSmnFqq63lhoQxIRiWrHnSbmUbcWAfhV%2BYaEqaiF5l2wR76Xp1wx8NcDmmyMljJEt&X-Amz-Signature=ee06a57c4d3b6ce33a63d715f150c334cba1f1d98f7d78195bc25a5a4fb51afa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Die Uhrzeit ist:
- ✅ 9 Stunden,
- ✅ 27 Minuten,
- ✅ 34 Sekunden

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Convert binary into decimal](/2b21ebb6314545d48382bb68713e5145)**
The image in question depicts the St. Gallen train station clock, which uses binary coding to display hours, minutes, and seconds. In this case, each row on the clock represents a different unit of time in binary form.
To understand the correct answers, we need to know how to read binary numbers:
- **First row (Hours):** The binary number is `1001`. To convert it to decimal (the number system we use daily), you start from the right, with each digit representing a power of 2. So the calculation is:
- `1*2^3 = 8`
- `0*2^2 = 0`
- `0*2^1 = 0`
- `1*2^0 = 1`
- **Total hours:** 8 + 0 + 0 + 1 = **9 hours**
- **Second row (Minutes):** The binary number is `011011`. The same conversion process results in: 
- `0*2^5 = 0`
- `1*2^4 = 16`
- `1*2^3 = 8`
- `0*2^2 = 0`
- `1*2^1 = 2 `
- `1*2^0 = 1`
- **Total hours:** 0 + 16 + 8 + 0 + 2 + 1 = **27 minutes**
- **Third row (Seconds):** The binary number is `100010`. Converting this to decimal gives:
- `1*2^5 = 32`
- `0*2^4 = 0`
- `0*2^3 = 0 `
- `0*2^2 = 0`
- `1*2^1 = 2`
- `0*2^0 = 0`
- **Total seconds:** 32 + 0 + 0 + 0 + 2 + 0 = **34 seconds**
Therefore, the correct answers are:
- ✅ **9 Hours**: The binary number `1001` equals 9 in decimal.
- ✅ **27 Minutes**: The binary number `011011` equals 27 in decimal.
- ✅ **34 Seconds**: The binary number `100010` equals 34 in decimal.
<details>
<summary>Details about calculation</summary>

**Hours**
| Position | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| Binary | 0 | 1 | 1 | 0 | 1 |
| Calculation | 0 * 2^4 = 0 | 1 * 2^3 = 8 | 1 * 2^2 = 4 | 0 * 2^1 = 0 | 1 * 2^0 = 1 |
| Decimal | 0 | 8 | 4 | 0 | 1 |
Sum of {8, 1} = **9**
---
**Minutes**
| Position | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 0 | 1 | 1 | 0 | 1 | 1 |
| Calculation | 0 * 2^5 = 0 | 1 * 2^4 = 16 | 1 * 2^3 = 8 | 0 * 2^2 = 0 | 1 * 2^1 = 2 | 1 * 2^0 = 1 |
| Decimal | 0 | 0 | 0 | 0 | 2 | 0 |
Sum of {16, 8, 2, 1} = **27**
---
**Seconds**
| Position | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 1 | 0 | 0 | 0 | 1 | 1 |
| Calculation | 1 * 2^5 = 32 | 0 * 2^4 = 0 | 0 * 2^3 = 0 | 0 * 2^2 = 0 | 1 * 2^1 = 2 | 0 * 2^0 = 0 |
| Decimal | 32 | 0 | 0 | 0 | 2 | 0 |
Sum of {32, 2} = **34**
</details>
</details>
---
## Question 9
Kann eine Variable vom Typ int mit dem “-” Operator von einer Variable vom Typ str subtrahiert werden?
❌ Es kommt auf den Inhalt der Variablen an.
✅ Nein.
❌ Ja.

<details>
<summary>Explanation</summary>

We cannot deduct one apple (integer) from an orange (string). If we try to do so, we get a [TypeError](/5b0832dbf9454eb1941b7632e68a9abb):
```python
"5" - 3

TypeError: unsupported operand type(s) for -: 'str' and 'int'
```
</details>
---
## Question 10
Gegeben ist das folgende Programm zur Berechnung des Volumens einer Pyramide:
```python
b = 3.0
h = 2.0

volume = (1/3) * b ** 2 * h

print("Das Volumen ist", volume)
```

Mark all correct statements regarding this snippet.
❌ Das Programm stellt sicher, dass **b** und **h** gültige Werte beinhalten.
❌ Das Programm könnte auch ausgeführt werden, wenn **b** und **h** *str*-Werte enthielten, die in int-Werte umwandelbar sind.
✅ Das Programm könnte auch ausgeführt werden, wenn **b** und **h** *int*-Werte enthielten, die in *float*-Werte umwandelbar sind.
✅ Die Berechnung ist korrekt.

<details>
<summary>Explanation</summary>

❌ **Incorrect**, we can assign any values to the two variables `b` and `h`. There is no check that prevents python from executing the calculation with values in the wrong format.
❌ **Incorrect**, not any string value can be transformed into an integer value. The prerequisite is that the value inside the string is actually a number. For example, the following works:
```python
my_string = "5"
my_integer = int(my_string)

print(my_integer)
5
```
However, it is not possible cannot transform a string containing letters to an integer - we get an error:
```python
my_string = "Hans"
my_integer = int(my_string)

ValueError: invalid literal for int() with base 10: 'Hans'
```
✅ **Correct**, any integer value can be transformed into a float value.
✅ **Correct**, python codes implements the [according formula](https://www.omnicalculator.com/math/pyramid-volume).
</details>
---



📄 **[Quiz 2]** (subpage)
## Question 1
Gegeben ist das folgende Programm:
```python
text = input("Geben Sie den auszugebenden Text ein: ")
frequenz = int(float(input("Geben Sie an, wie oft der Text ausgegeben werden soll: ")))

for i in range(1, frequenz+1):
	print(i, ': ', text, sep='')
```

Markieren Sie alle zutreffenden Aussagen.
✅ Wenn das Programm fehlerfrei ausgeführt werden kann und die in der **zweiten** *input()*-Funktion eingegebene Zahl eine positive ganze Zahl (*int*) ist, dann hängt die Anzahl der ausgegebenen Zeilen von der in der **zweiten** *input()*-Funktion eingegebenen Zahl ab.
✅ Wenn das Programm fehlerfrei ausgeführt werden kann, dann hängt die Anzahl der Aufrufe der *print()*-Funktion **nicht** von der Länge des eingegebenen Texts in der ersten *input()*-Funktion ab.
✅ Wird in der **zweiten** *input()*-Funktion ein beliebiger String, welcher nicht nur aus Ziffern besteht, eingegeben, dann bricht das Programm mit einer Fehlermeldung ab.
❌ Wird in der **zweiten** *input()*-Funktion eine **negative** ganze Zahl (*int*) eingegeben, dann bricht das Programm mit einer Fehlermeldung ab.
❌ Wird in der **ersten** *input()*-Funktion eine beliebige Zahl statt einem String eingegeben, dann bricht das Programm mit einer Fehlermeldung ab.
❌ Es gibt keine Eingabewerte, mit denen das Programm fehlerfrei ausgeführt werden kann.
❌ Wird in der **zweiten** *input()*-Funktion eine Gleitkommazahl (float) eingegeben, dann bricht das Programm mit einer Fehlermeldung ab.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb), [range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385)**
✅ **Correct**, the number of lines output does indeed depend on the number entered in the second input() function. If the user enters 5, the text will be printed 5 times, thus creating 5 lines of output.
✅ **Correct,** the number of times the print() function is called depends on the number entered in the second input() function (frequency), not the length of the text entered in the first input() function.
✅ **Correct,** the second input() function expects a number (which is then converted to an integer). If a string that cannot be converted to a number is entered, the program will indeed break off with an error message.
❌ **Incorrect,** the program will not break if a negative integer is entered. However, since the range() function cannot create a range with a negative number, the loop will not be executed and no text will be printed.
❌ **Incorrect,** the input() function in Python always returns a string. If a number is entered, it will be treated as a string and the program will not break.
❌ **Incorrect,** the program can be executed without errors if a string is entered in the first input() function and a positive integer is entered in the second input() function.
❌ **Incorrect,** the program will not break if a float is entered. The float will be converted to an integer using the int() function. For example, if the user enters 5.7, it will be converted to 5 and the text will be printed 5 times.
</details>
---
## Question 2
Gegeben ist folgendes Programm:
```python
number = input('Bitte geben Sie eine positive ganze Zahl ein: ')
digit_sum = ''

for n in number:
	digit_sum += n
```
Bewerten Sie die folgende Aussage:
Wenn der/die Benutzer/in eine positive ganze Zahl gemäß Aufforderung eingibt, dann erhält digit_sum die Quersumme (*digit_sum*) dieser Eingabe.
Hinweis: Die *digit sum* ist, wie im Assignment, definiert als die Summe aller Ziffernwerte einer natürlichen Zahl.
✅ Falsch (*False*)
❌ Wahr (*True*)
❌ Bei der Programmausführung tritt trotz korrekter Eingabe ein Fehler auf.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [augmented assignments](/5b0832dbf9454eb1941b7632e68a9abb#30b886f101854a3ca81b231e9cda05a3)**
The given program asks the user to input a positive integer. It then iterates over each digit in the number and adds it to the `digit_sum` variable. However, the problem here is that the `digit_sum` variable is a string, and the `+=` operation is concatenating the digits as strings, not adding them as numbers.
Here's what's happening in each line of the code:
1. `number = input('Bitte geben Sie eine positive ganze Zahl ein: ')`
This line asks the user to input a positive integer. The input is stored as a string in the `number` variable.
1. `digit_sum = ''
`This line initializes an empty string `digit_sum`.
1. `for n in number:
`This line starts a loop that iterates over each character (digit) in the `number` string.
1. `digit_sum += n
`This line adds the current digit to the `digit_sum` string. However, since `digit_sum` is a string, the `+=` operation concatenates the digit to the end of the string, rather than adding it as a number.
So, if the user inputs `123`, the program will output `digit_sum` as `'123'`, not `6` (which is the sum of the digits 1, 2, and 3). Therefore, the statement is incorrect. The program does not calculate the digit sum of the input number.
</details>
---
## Question 3
Gegeben ist das folgende Programm:
```python
result = ''

for i in range(1, 8, 2):
    if i % 2 == 0:
        result += str(i)
    elif i == 3:
        result += '3'
    else:
        result += str(i + 1)

result = int(result)
```
Welchen Wert hat result nach der Ausführung des Programms? Geben Sie das Ergebnis ohne etwaige Anführungszeichen oder Nachkommastellen an. Wenn Sie der Meinung sind, dass das Programm mit einem Fehler abbricht, dann geben Sie den Wert -1 ein.

**2368**
<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb), [augmented assignments](/5b0832dbf9454eb1941b7632e68a9abb#30b886f101854a3ca81b231e9cda05a3), [range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385), [for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)**
To understand what is happening in the code, let’s go through it line-by-line.
`result = ''`
`for i in range(1, 8, 1): → [1, 2, 3, 4, 5, 6, 7, 8]`
<details>
<summary>1st iteration → `result = '2'`</summary>

`i = 1`
`if 1 % 2 == 0:` → `1 == 0` → `False`
`elif i == 3:` → `1 == 3` → `False`
`else:`
`result += str(1+1)` → `result=''+'2'` → `'2'`
</details>
<details>
<summary>2nd iteration → `result = '23'`</summary>

`i = 3`
`if 3 % 2 == 0:` → `3 == 0` → `False`
`elif 3 == 3:` → `3 == 3` → `True`
`result += '3'` → `result='2'+'3'` → `'23'`
`else:`
*→ not executed as **`elif`** evaluated to True*
</details>
<details>
<summary>3rd iteration → `result = '236'`</summary>

`i = 5`
`if 5 % 2 == 0:` → `5 == 0` → `False`
`elif 5 == 3:` → `5 == 3` → `False`
`else:`
`result += str(5+1)` → `result='23'+'6'` → `'236'`
</details>
<details>
<summary>4th iteration → `result = '2368'`</summary>

`i = 7`
`if 7 % 2 == 0:` → `7 == 0` → `False`
`elif 7 == 3:` → `7 == 3` → `False`
`else:`
`result += str(7+1)` → `result='236'+'8'` → `'2368'`
</details>
</details>
---
## Question 4
Bitte markieren Sie alle zutreffenden Aussagen:
✅ Eine `for`-Schleife kann über eine beliebige Zeichenkette (String) iterieren.
✅ Der Codeblock der oben genannten `for`-Schleife wird für jedes Element in der Zeichenkette genau einmal ausgeführt.
❌ Im Gegensatz zu for-Schleifen kann man bei `while`-Schleifen vor ihrer Ausführung immer genau sagen, wie oft ihr Codeblock ausgeführt wird.
❌ Der Codeblock jeder `for`-Schleife wird so oft ausgeführt, wie die zu definierende Bedingung wahr (*True*) ist und nicht durch den Code im Codeblock falsch (*False*) wird.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[loops](/5b0832dbf9454eb1941b7632e68a9abb#a0ed22190a314589a93842ccc98136c7)**
✅ **Correct**, in Python, a for-loop can iterate over any iterable object, including strings. Each iteration of the loop corresponds to a character in the string. For example:
```python
for character in "Hello":
    print(character)
```
This code will print each character in the string "Hello" on a new line.
✅ **Correct**, in a for-loop, the code block is executed once for each element in the iterable. In the case of a string, this means the code block is executed once for each character.
❌ **Incorrect**, the number of times a while-loop is executed depends on its condition. If the condition remains true, the loop will continue to execute. It's not always possible to know in advance how many times this will be.
❌ **Incorrect**, this statement describes a while-loop, not a for-loop. A for-loop executes for each item in an iterable, not based on a condition. A while-loop, on the other hand, continues to execute as long as its condition is true.
</details>
---
## Question 5
Wie viele Schleifendurchläufe erzeugt der Funktionsaufruf
**range(2, 23, 6)**
wenn dieser in einer for-Schleife verwendet wird?
**4**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Range object](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385) in combination with [for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)**
The question asks how many times the an arbitrary for-loop, for example the one below, is executed if `range(2, 23, 6)` is used.
```sql
for i in range(2, 23, 6):
	print(f'this is loop run {i}')

'This is loop run 1'
'This is loop run 2'
'This is loop run 3'
'This is loop run 4'
```
We can see that the string is printed 4 times, thus there are 4 runs in total. To get to this answer we need to understand what `range(2, 23, 6)` does. 
`range(2, 23, 6)` has three arguments:
- `2` → first number to **include** in number range
- `23` → first number to **exclude** in number range
- `6` → step size, i.e., the first number and then only every sixth number
If we remove the step size we get:
`[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]`
Now with the step size of 3 we take only every third number
`[`**`2`**`, `~~`3, 4, 5, 6, 7,`~~` `**`8`**`, `~~`9, 10, 11, 12, 13,`~~` `**`14`**`, `~~`15, 16, 17, 18, 19,`~~` `**`20`**`, `~~`21, 22`~~`]`
And this gives us the following number range:
`[2, 8, 14, 20]`
And if we insert this in the for loop we get:
```sql
for i in [2, 8, 14, 20]:
	print(f'this is loop run {i}')
```
Variable `i` takes on the first value in the list (2), executes the code inside the loop and then moves on to the next element. Thus, as our list consists of four elements, the loop is executed four times.
</details>
---

📄 **[Quiz 3]** (subpage)
# Question 1
Gegeben ist die folgende Funktionsdefinition:
```python
def calculate_range_sum(operation='sum', start=0, stop=4, step=1):

    if operation == 'sum':
        return sum(range(start, stop, step))

    elif operation == 'square':
        range_sum = 0
        for i in range(start, stop, step):
            range_sum += i ** 2
        return range_sum

    elif operation == 'square_root':
        range_sum = 0
        for i in range(start, stop, step):
            range_sum += i ** (1/2)
        return range_sum

    elif not isinstance(operation, str):
        raise TypeError(f'Argument operation needs to be of type String, ')

    else:
        raise ValueError(f'Operation {operation} is not known.')
```
Markieren Sie alle korrekten Aussagen zu dieser Funktion.
1. ✅ Die Funktion **calculate_range_sum** kann ohne Argument, also als **calculate_range_sum()**, aufgerufen werden und wird dabei fehlerfrei ausgeführt.
1. ✅ Der Rückgabewert ist **14** wenn die Funktion mit **calculate_range_sum('square')** aufgerufen wird.
1. ✅ Die Funktion **calculate_range_sum** kann erfolgreich mit zwei Argumenten aufgerufen und ausgeführt werden.
1. ✅ Der Rückgabewert ist **2** wenn die Funktion mit **calculate_range_sum(step=2)** aufgerufen wird.
1. ❌ Die Funktionsdefinition ist fehlerhaft und erzeugt darum spätestens beim Funktionsaufruf einen Fehler.
1. ✅ Die Funktion **calculate_range_sum** kann erfolgreich mit einem Argument aufgerufen und ausgeführt werden.
1. ❌ Die Funktion calculate_range_sum gibt immer die Summe aller ganzen Zahlen zwischen den Parameterwerten start (*inklusive*) und stop (*inklusive*) zurück.
1. ✅ Die Funktion **calculate_range_sum** kann erfolgreich mit vier Argumenten aufgerufen und ausgeführt werden.
1. ❌ Der Rückgabewert ist **2** wenn die Funktion mit **calculate_range_sum(2, 2, 2)** aufgerufen wird.
1. ❌ Die Funktion **calculate_range_sum** kann erfolgreich mit beliebig vielen Argumenten aufgerufen und ausgeführt werden.
1. ❌ Die Funktion **calculate_range_sum** gibt immer die Summe aller ganzen Zahlen zwischen den Parameterwerten **start** (inklusive) und **stop** (exklusive) zurück.
1. ✅ Der Rückgabewert ist **6** wenn die Fuktion mit **calculate_range_sum()** aufgerufen wird.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Default parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc), [logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2), [range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385), [augmented assignments](/5b0832dbf9454eb1941b7632e68a9abb#30b886f101854a3ca81b231e9cda05a3), [math operations](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a)**
1. ✅ **Correct**, the function can be called without any arguments. This is because there are default values specified for all arguments (`operation`, `start`, `end`, `step`) in the function header. So when for one, multiple or all parameters no value(s) are provided, the default value(s) will be assigned.
1. ✅ **Correct**, the return value is indeed 14 when the function is called with `calculate_range_sum('square')`. This is because the function calculates the sum of the squares of the numbers in the range from `start` to `stop` with a `step` of 1. In this case, the numbers are 0, 1, 2, and 3. Their squares are 0, 1, 4, and 9, respectively, and their sum is 14.
1. ✅ **Correct**, the function can be successfully called with two arguments. The first argument will be assigned to `operation`, and the second one to `start`. The other parameters, `stop` and `step`, will take their default values of 4 and 1, respectively.
1. ✅ **Correct**, the return value is indeed 2 when the function is called with `calculate_range_sum(step=2)`. This is because the function calculates the sum of the numbers in the range from `start` to `stop` with a `step` of 2. In this case, the numbers are 0 and 2, and their sum is 2.
1. ❌ **Incorrect**, the function definition is not faulty and does not produce an error when called. It checks the type and value of `operation` and raises an error if it's not a string or if it's a string that doesn't match any of the expected values ('sum', 'square', or 'square_root').
1. ✅ **Correct**, the function can be successfully called with one argument. The argument will be assigned to `operation`, and the other parameters, `start`, `stop`, and `step`, will take their default values.
1. ❌ **Incorrect**, the function does not always return the sum of all integers between `start` (inclusive) and `stop` (inclusive). The `stop` value is actually exclusive, and the function can also return the sum of the squares or square roots of the numbers, depending on the `operation`.
1. ✅ **Correct**, the function can be successfully called with four arguments. The arguments will be assigned to `operation`, `start`, `stop`, and `step`, in that order.
1. ❌ **Incorrect**, when calling the function with `calculate_range_sum(2, 2, 2)`,the following parameter values will be assigned:
1. `operation = 2`
1. `start = 2`
1. `stop = 2`
As an integer is stored in `operation`, if-statement `elif not isinstance(operation, str):` will result to True and thus the message *'Argument operation needs to be of type String *is returned.
1. ❌ **Incorrect**, the function can be successfully called with any number of arguments. In this case the function’s default arguments will be used.
1. ❌ **Incorrect**, the function’s return value is different for each `operation`.
1. ✅ **Correct**, when the function is called with no arguments, the default values will be used. Thus, operation sum is executed, which calculate the sum of the numbers `[0, 1, 2, 3]` which yields **6**.
</details>
---
## Question 2
Gegeben ist folgendes Programm. Es wurde ausgeführt:
```python
import random

def fizz(buzz):
	result = []
	
	for i in range(buzz-1):
		if (i % 2 == 0):
			result += [random.randrange(1,100)]
		elif i % 3 == 0:
			result = result[:len(result)-1]
		elif i % 5 == 0:
			break
		else:
			result += [i]
		
	return len(result)
```
Markieren Sie **alle** korrekten Aussagen zu diesem Programm. 
✅ Der Rückgabewert ist **3** wenn die Funktion fizz mit **fizz(4)** aufgerufen wird.
✅ Der Rückgabewert ist **2 **wenn die Funktion fizz mit **fizz(5)** aufgerufen wird.
❌ Der Rückgabewert ist **1** wenn die Funktion fizz mit **fizz(1)** aufgerufen wird.
❌ Wenn **fizz()** mit einem gradzahligen Argument aufgerufen wird, dann kann der Rückgabewert nicht genau bestimmt werden.
❌ Da aufgrund des **break** Statements das **return** Statement in der letzten Zeile nicht erreicht wird, gibt die Function **fizz()** *None* zurück.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[functions](/5b0832dbf9454eb1941b7632e68a9abb#d98d10a03b3b4d17a846dfff610e9a5f), [logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2), [modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c), [slicing](/5b0832dbf9454eb1941b7632e68a9abb#5d06cfcdb5574513a592b854a821fe3e), [range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385), [for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [random number](/5b0832dbf9454eb1941b7632e68a9abb#ed2397e7feb14e2c8050fe513be5e34b)**
Let’s go through the code line-by-line to understand what is happening.
✅ **Correct, **the return value is **3**
<details>
<summary>`fizz(4)` → **3**</summary>

`buzz = 4`
`result = []`
`for i in range(buzz-1):` → `range(4-1)` → `[0, 1, 2]`
<details>
<summary>1st run → `len(result)` → **1**</summary>

`i = 0`
`result = []`
`if (0%2 == 0):`→ `0 == 0`→ `True`
`result += [random.randrange(1,100)]` → *random number is added to **`result`*
`elif 0 % 3 == 0:`
*not evaluated as if-statement evaluated to ****True***
`elif i % 5 == 0:`
*not evaluated as if-statement evaluated to ****True***
`else:`
*not evaluated as if-statement evaluated to ****True***
</details>
<details>
<summary>2nd run → `len(result)` → **2**</summary>

`i = 1`
`result = [`*`<< rnd num >>`*`]`
`if (1%2 == 0):`→ `1 == 0` → `False`
*not executed as if-statement evaluated to ****False***
`elif 1 % 3 == 0:` → `1 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`elif 1 % 5 == 0:` → `1 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`else:`
`result += [1]`
</details>
<details>
<summary>3rd run → `len(result)` → **3**</summary>

`i = 2`
`result = [`*`<< rnd num >>, `*`1]`
`if (2%2 == 0):`→ `0 == 0` → `True`
`result += [random.randrange(1,100)]` → *random number is added to **`result`*
`elif 0 % 3 == 0:`
*not evaluated as if-statement evaluated to ****True***
`elif i % 5 == 0:`
*not evaluated as if-statement evaluated to ****True***
`else:`
*not evaluated as if-statement evaluated to ****True***
</details>
`return(len(result))` → `len([`*`<< rnd num >>`*`, 1, `*`<< rnd num >>`*`])` → **3**
</details>
✅ **Correct, **the return value is **2**
<details>
<summary>`fizz(5)` → **2**</summary>

`buzz = 5`
`result = []`
`for i in range(buzz-1):` → `range(5-1)` → `[0, 1, 2, 3]`
<details>
<summary>1st run → `len(result)` → **1**</summary>

`i = 0`
`result = []`
`if (0%2 == 0):`→ `0 == 0`→ `True`
`result += [random.randrange(1,100)]` → *random number is added to **`result`*
`elif 0 % 3 == 0:`
*not evaluated as if-statement evaluated to ****True***
`elif i % 5 == 0:`
*not evaluated as if-statement evaluated to ****True***
`else:`
*not evaluated as if-statement evaluated to ****True***
</details>
<details>
<summary>2nd run → `len(result)` → **2**</summary>

`i = 1`
`result = [`*`<< rnd num >>`*`]`
`if (1%2 == 0):`→ `1 == 0` → `False`
*not executed as if-statement evaluated to ****False***
`elif 1 % 3 == 0:` → `1 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`elif 1 % 5 == 0:` → `1 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`else:`
`result += [1]`
</details>
<details>
<summary>3rd run → `len(result)` → **3**</summary>

`i = 2`
`result = [`*`<< rnd num >>, `*`1]`
`if (2%2 == 0):`→ `0 == 0` → `True`
`result += [random.randrange(1,100)]` → *random number is added to **`result`*
`elif 0 % 3 == 0:`
*not evaluated as if-statement evaluated to ****True***
`elif i % 5 == 0:`
*not evaluated as if-statement evaluated to ****True***
`else:`
*not evaluated as if-statement evaluated to ****True***
</details>
<details>
<summary>4th run → `len(result)` → **2**</summary>

`i = 3`
`result = [`*`<< rnd num >>, `*`1, `*`<< rnd num >>`*`]`
`if (3%2 == 0):`→ `1 == 0` → `False`
*not executed as if-statement evaluated to ****False***
`elif 3 % 3 == 0:` → `0 == 0` → `False`
`result = result[:len([`*`<< rnd num >>, `*`1, `*`<< rnd num >>`*`])-1]`
→ `result = result[:2]` → `[`*`<< rnd num >>, `*`1]`
`elif i % 5 == 0:`
*not evaluated as if-statement evaluated to ****True***
`else:`
*not evaluated as if-statement evaluated to ****True***
</details>
`return(len(result))` → `len([`*`<< rnd num >>`*`, 1])` → **2**
</details>
❌ **Incorrect**, the return value is **0**
<details>
<summary>`fizz(1)` → **0**</summary>

`buzz = 1`
`result = []`
`for i in range(1-1):` → `range(0)` → `[]`
*for-loop is not executed as **`range(0)`** returns an empty range object*
`return(len(result))` → `len([])` → **0**
</details>
❌ Incorrect, as we have seen from he first answer, the function works with even numbers.
❌ Incorrect, the break statement does not cause a function return, but causes Python to jump out of the for-loop and continue at the first line after the for-loop, which in this case is the line `return len(result)`. So as we can see this line does not return `None`.
</details>
---
## Question 3
Gegeben ist die folgende Funktion:
```python
def get(elmnts):
    for e in elmnts[::-1]:
        if not isinstance(e, int) and not isinstance(e, str):
            continue
        return str(e)
```
Was macht die Funktion **get**? Nehmen Sie an, die Funktion wird korrekt aufgerufen mit einem Argument, welches ein Tupel (*tuple*) mit mindestens einem ganzzahligen Element ist.
❌ Sie gibt immer das *erste* Element des Tupels **elmnts** zurück.
✅ Sie gibt immer einen Wert vom Typ String (*str*) zurück.
❌ Sie gibt immer die letzte *negative* ganze Zahl (*integer*) des Tupels **elmnts** zurück.
❌ Sie gibt immer die erste *gerade* Zahl (*even* *integer*) des Tupels **elmnts** zurück.
❌ Sie gibt immer '2.718281828459045' zurück.
❌ Sie gibt immer den ersten *String* (str) des Tupels **elmnts** zurück.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[List slicing](/5b0832dbf9454eb1941b7632e68a9abb#01370999e4334066ba04335de9ae836a),[ type checking](/5b0832dbf9454eb1941b7632e68a9abb#6f8e8203d09a4c3aafa6f5d78119fe00), [continue](/5b0832dbf9454eb1941b7632e68a9abb#fe988d55110a4f1fa1181df33ad90af6), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb)**
❌ **Incorrect**, the function does not always return the first element of the tuple. It returns the first integer or string it finds when iterating in reverse order.
✅ **Correct**, the function converts the first integer or string it finds to a string and returns it. Therefore, it always returns a value of type `str`.
❌ **Incorrect**, the function does not specifically look for negative integers. It returns the first integer or string it finds in reverse order.
❌ **Incorrect**, the function does not specifically look for even integers. It returns the first integer or string it finds in reverse order.
❌ **Incorrect**, the function does not return this specific value. It returns the first integer or string it finds in reverse order.
❌ **Incorrect**, the function returns the first integer or string it finds in reverse order, not necessarily the first string.
</details>
---
## Question 4
Gegeben ist das folgende Programm:
```python
a = (1, 2, 3, [4, '1234'], 5)
b = int(a[3][1][1][:])
```
Was ist der *Wert* der Variable **b** nach der Ausführung? Wenn Sie der Meinung sind, dass bei der Ausführung ein Fehler auftritt, geben Sie *-1* ein.
**2**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Tuple](/5b0832dbf9454eb1941b7632e68a9abb#f8cb18a835dd45c1aed5abca3279ba9c), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb)**
Let's break down the given code step by step to understand why the value of the variable `b` is `2`.
1. `a = (1, 2, 3, [4, '1234'], 5)`
Here, `a` is a tuple containing five elements:
- The first element is the integer `1`.
- The second element is the integer `2`.
- The third element is the integer `3`.
- The fourth element is a list `[4, '1234']`.
- The fifth element is the integer `5`.
1. `b = int(a[3][1][1][:])`
- `a[3]` accesses the fourth element of the tuple `a`, which is the list `[4, '1234']`.
- `a[3][1]` accesses the second element of that list, which is the string `'1234'`.
- `a[3][1][1]` accesses the second character of the string `'1234'`, which is `'2'`.
- `a[3][1][1][:]` is essentially the same as `a[3][1][1]`, so it still refers to the character `'2'`.
- `int(a[3][1][1][:])` converts the character `'2'` to the integer `2`.
Therefore, the value of `b` after the execution of the code is `2`.
</details>
---
## Question 5
Wir wissen, dass Tupel (*tuple*) unveränderbar (*immutable*) sind. Trotzdem wird das folgende Programm ausgeführt. Hierbei wird zuerst ein Tupel (*t*) erzeugt und dann wird der darin enthaltene erste String von *Mayer* nach *Maier* korrigiert.
```python
t = [1, 2, 3, 'Mayer', 'Joe']
t[3][2] = 'i'
```
Warum ist das möglich, wenn Tupel unveränderbar (*immutable*) sind?
❌ Man kann nicht genau sagen was passiert; es hängt stark von der Grösse und Belegung des Arbeitsspeichers des ausführenden Rechners ab, vor allem dann, wenn, wie im vorliegenden Quellcode, der Garbage Collector noch nicht gestartet wurde.
❌ Es handelt sich gar nicht um ein Tupel. *t* ist eigentlich eine Liste und Listen sind veränderbar (*mutable*). Darum läuft das Programm fehlerfrei.
❌ Das Tupel ist nicht *immutable* aber es tritt trotzdem kein Fehler auf, da ja nicht das Tupel sondern der String geändert wird.
✅ Die Aussage ist falsch. Das Programm kann *nicht* fehlerfrei ausgeführt werden.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Nested lists](/5b0832dbf9454eb1941b7632e68a9abb#8526be0c72d1432c83067d8315535bd0)**
Let's break down the provided code and the answer options to understand why the correct answer is marked as it is.
1. `t = [1, 2, 3, 'Mayer', 'Joe']`
- This line creates a list `t` containing five elements: three integers and two strings.
- Lists in Python are mutable, meaning their elements can be changed after the list is created.
1. `t[3][2] = 'i'`
- `t[3]` accesses the fourth element of the list `t`, which is the string `'Mayer'`.
- `t[3][2]` attempts to access the third character of the string `'Mayer'`, which is `'y'`.
- The code then tries to change this character to `'i'`.
✅ Correct, strings in Python are immutable, meaning once a string is created, its characters cannot be changed. Attempting to change a character in a string directly, as in `t[3][2] = 'i'`, will result in a `TypeError`.
❌ **Incorrect**, the behavior of immutability in Python does not depend on memory size or garbage collection. It is a fundamental property of the data types.
❌ **Incorrect**, as we can see from the square brackets `[]` the element stored in variable `t` is a list and not a tuple. However, as we are trying to change a character of a string that is stored inside the list, the code still throws and error .
❌ **Incorrect**, the issue is not with a tuple but with the immutability of the string. Strings cannot be changed in place, which is why the code will raise an error.
</details>
---

📄 **[Quiz 4]** (subpage)
## Question 1
Geben Sie das folgende Programm. Es wurde fehlerfrei ausgeführt.
```python
class Car:
    def __init__(self, brand, year_of_production):
        # Bitte nehmen Sie für die __init__ Methode an, dass die
        # Variablen self._brand und self._year_of_production mit den
        # zugehörigen Argumenten korrekt initialisiert wurden

    @property
    def brand(self):
        # Bitte gehen Sie davon aus, dass diese Methode den Wert
        # von self._brand zurückgibt
    def year_of_production(self):
        # Bitte gehen Sie davon aus, dass diese Methode den Wert
        # von self._year_of_production zurückgibt

    def compute_age(self):
        return 2024 - self._year_of_production

    def __str__(self):
        return f"This is a {self.brand} of age {self.compute_age()}"

    def __repr__(self):
        return f"Car({self.brand}, {self.year_of_production})"

class ElectricCar(Car):
    def __init__(self, brand, year_of_production, battery_capacity):
        # Bitte nehmen Sie für die __init__ Methode an, dass die
        # Argumente brand und year_of_production korrekt via super().__init__(...)
        # weitergegeben wurden und self.battery_capacity mit dem
        # zugehörigen Argument korrekt initialisiert wurde

    @property
    def battery_capacity(self):
        return self._battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        if not (isinstance(battery_capacity, float) or isinstance(battery_capacity, int)):
            raise TypeError('battery capacity needs to be a number (float or int)')
        elif battery_capacity < 0:
            raise ValueError('battery capacity needs to be a positive number')
        else:
            self._battery_capacity = battery_capacity

    def __str__(self):
        return f"{super().__str__()} and a remaining battery capacity of {self.battery_capacity} kWh"

    def __repr__(self):
        return f"ElectricCar({self.brand}, {self.year_of_production}, {self.battery_capacity})"

c = Car('Porsche', 1984)
e = ElectricCar('Porsche', 2022, 108)

```
Bitte markieren Sie alle korrekten Aussagen zu obigem Programm.
1. ✅ Der Aufruf *e.__str__()* kann fehlerfrei ausgeführt werden.
1. ✅ **c** ist eine Instanz von **Car**.
1. ✅ **e** ist eine Instanz von **Car**.
1. ✅ **ElectricCar** erbt von **Car**.
1. ✅ Der Aufruf *print(e)* kann fehlerfrei ausgeführt werden.
1. ✅ Der Aufruf *e._battery_capacity = 'insufficient'* kann fehlerfrei ausgeführt werden.
1. ❌ Der Aufruf *e.battery_capacity = 'insufficient' *kann fehlerfrei ausgeführt werden.
1. ✅ Der Aufruf *e* kann fehlerfrei ausgeführt werden.
1. ❌ **c** ist eine Instanz von **ElectricCar**.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Class inheritance](/c991314990fa47e19addaf16235213db), [repr ](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073)method, [str method](/83479909f70b47e491c55c9a6178291a#d6adf9d285e743288d38c01044065158), [getter](/83479909f70b47e491c55c9a6178291a#4d9fcd781fd5450697ba15e0c6989f20) & [setter](/83479909f70b47e491c55c9a6178291a#0fd3908f13ee4acf9601894aeebbcb56) method, [access class attributes](/83479909f70b47e491c55c9a6178291a#72cd5f486f4b455093b47d3a2115ff49)**
Let's break down the provided code and the answer options to understand why the correct answers are marked as they are.
### Code Explanation
1. **Class Definition: Car**
```python
class Car:
    def __init__(self, brand, year_of_production):
        self._brand = brand
        self._year_of_production = year_of_production

```
- This defines a class `Car` with an initializer method `__init__` that sets the brand and year of production.
```python
    @property
    def brand(self):
        return self._brand
```
- This defines a property `brand` that returns the value of `_brand`.
```python
    def year_of_production(self):
        return self._year_of_production
```
- This method returns the value of `_year_of_production`.
```python
    def compute_age(self):
        return 2024 - self._year_of_production
```
- This method calculates the age of the car by subtracting the year of production from 2024.
```python
    def __str__(self):
        return f"This is a {self.brand} of age {self.compute_age()}"
```
- This method returns a string representation of the car.
```python
    def __repr__(self):
        return f"Car({self.brand}, {self.year_of_production})"
```
- This method returns a more detailed string representation of the car.
1. **Class Definition: ElectricCar**
```python
class ElectricCar(Car):
    def __init__(self, brand, year_of_production, battery_capacity):
        super().__init__(brand, year_of_production)
        self.battery_capacity = battery_capacity
```
- This defines a class `ElectricCar` that inherits from `Car`. It initializes the brand and year of production using `super().__init__` and sets the battery capacity.
```python
    @property
    def battery_capacity(self):
        return self._battery_capacity
```
- This defines a property `battery_capacity` that returns the value of `_battery_capacity`.
```python
    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        if not (isinstance(battery_capacity, float) or isinstance(battery_capacity, int)):
            raise TypeError('battery capacity needs to be a number (float or int)')
        elif battery_capacity < 0:
            raise ValueError('battery capacity needs to be a positive number')
        else:
            self._battery_capacity = battery_capacity
```
- This defines a setter for `battery_capacity` that checks if the value is a positive number and raises errors if not.
```python
    def __str__(self):
        return f"{super().__str__()} and a remaining battery capacity of {self.battery_capacity} kWh"
```
- This method returns a string representation of the electric car, including the battery capacity.
```python
    def __repr__(self):
        return f"ElectricCar({self.brand}, {self.year_of_production}, {self.battery_capacity})"
```
- This method returns a more detailed string representation of the electric car.
1. **Creating Instances**
```python
c = Car('Porsche', 1984)
e = ElectricCar('Porsche', 2022, 108)
```
- These lines create instances of `Car` and `ElectricCar`.
### Answer Explanations
1. ✅ **Correct**, the `__str__` method is defined in both `Car` and `ElectricCar`, and it will return a string representation of the electric car without errors.
1. ✅ **Correct**, `c` is created as an instance of `Car`.
1. ❌ **Correct**, `e` is an instance of `ElectricCar`, which is a subclass of `Car`.
1. ✅ **Correct, **`ElectricCar` is defined as inheriting from `Car`.
1. ✅ **Correct**, the `print` function calls the `__str__` method, which is defined and will execute without errors.
1. ✅ **Correct**, directly setting the `_battery_capacity` attribute bypasses the setter method, so no error is raised.
1. ❌ **Incorrect**, the setter method for `battery_capacity` checks the type and will raise a `TypeError` because 'insufficient' is not a number.
1. ✅ **Correct**, simply referencing `e` will call the `__repr__` method, which is defined and will execute without errors.
1. ❌ **Incorrect**, `c` is an instance of `Car`, not `ElectricCar`.
</details>
---
## Question 2
Gehen Sie davon aus, dass **bbwl_student** (eine Instanz der Klasse **HealingSuperhero** aus dem Assignment) gegeben ist. Was passiert, wenn Sie folgenden Python-Code ausführen?
```python
str(bbwl_student)
```

❌ Python versucht das Objekt darzustellen. Da die Klasse **HealingSuperhero** aber weder eine *__str__* noch eine *__repr__* Methode implementiert, wird nur ein Wert ähnlich dem folgenden zurückgegeben:
```python
<__main__.HealingSuperhero object at Ox1130e3ed0>
```
❌ Keine der anderen Antworten trifft zu.
✅ Es wird eine der implementierten *str()* Methoden ausgeführt.
❌ Es wird die *repr()* Methode ausgeführt.
❌ Nichts passiert, da die implementierte *__str__* Methode zwar ein *return* Statement hat aber die *print()* Funktion nicht aufruft.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 ** [repr ](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073)method, [str](/83479909f70b47e491c55c9a6178291a#d6adf9d285e743288d38c01044065158) method**
❌ **Incorrect,** this would be true if the class `HealingSuperhero` did not implement either the `__str__` or `__repr__` methods. In such a case, Python would fall back to the default representation of the object, which looks like `<__main__.HealingSuperhero object at Ox1130e3ed0>`. However, the correct answer indicates that a `__str__` method is implemented.
❌ **Incorrect,** this is a catch-all option that is not applicable since one of the other answers is correct.
✅ **Correct,** if the class `HealingSuperhero` has an implemented `__str__` method, Python will use this method to convert the object to a string. The `__str__` method is specifically designed to return a "nice" string representation of the object.
```python
class HealingSuperhero:
    def __str__(self):
        return "HealingSuperhero instance"

bbwl_student = HealingSuperhero()
print(str(bbwl_student))  # Output: HealingSuperhero instance
```
- Here, the `__str__` method is defined in the `HealingSuperhero` class.
- When `str(bbwl_student)` is called, it invokes the `__str__` method and returns the string `"HealingSuperhero instance"`.
❌ **Incorrect, t**he `__repr__` method is used to provide an "official" string representation of an object, which can be useful for debugging. If both `__str__` and `__repr__` are implemented, `str()` will use `__str__`. Since the correct answer indicates that `__str__` is implemented, `__repr__` will not be used in this case.
❌ **Incorrect, t**his statement is misleading. The `str()` function does not require the `print()` function to work. The `str()` function will call the `__str__` method and return its result as a string. The `print()` function is only needed if you want to display the string on the screen.
</details>
---
## Question 3
Gegeben ist folgendes Programm
```python
class Car():
    def __init__(self, brand, model, milage, condition):
        self._brand = brand
        self._model = model
        self.milage = milage
        self.condition = condition

    # Bitte gehen Sie in Ihrer Antwort davon aus, dass hier korrekte und hilfreiche
    # Getter-Methoden brand() und model() implementiert sind

    def __str__(self):
        return f"""
        Das Fahrzeug ist das Modell {self.model} der Marke {self.brand},
        hat einen Kilometerstand von {self.milage} km und ist in
        {"gutem" if self.condition > 50 else "schlechtem"} Zustand
        """

print(Car('Porsche', '964', 150000, 41))
```

Bitte markieren Sie alle zutreffenden Aussagen.
✅ Werden passende Getter- und Setter-Methoden für *milage* und *condition* implementiert, kann das Programm ohne zusätzliche Änderungen fehlerfrei ausgeführt werden.
❌ Das Programm kann ohne die Implementierung der Setter-Methoden für *milage* und *condition* nicht fehlerfrei ausgeführt werden, da die **init** Methode diese Setter-Methoden implizit voraussetzt.
❌ Der Aufruf der *print()* Funktion funktioniert so nicht, da keine Referenz zu dem auszugebenden Objekt vorhanden ist.
❌ Das Programm erzeugt eine Ausgabe, die sehr ähnlich zu folgender ist:
```plain text
Das Fahrzeug ist das Modell 964 der Marke Porsche,
hat einen Kilometerstand von 150000 km und ist in
gutem Zustand

Eventuelle Variationen dieser Ausgabe sind auf die konkrete Implementierung der Getter-Methoden *brand()* und *model()* zurückzuführen.
```
✅ Das Programm kann fehlerfrei ausgeführt werden.
❌ Keine der anderen Aussagen trifft zu.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 ** [repr ](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073)method, [str](/83479909f70b47e491c55c9a6178291a#d6adf9d285e743288d38c01044065158) method**
Let's break down the provided code and the answer options to understand why the correct answers are marked as they are.
### Code Explanation
1. **Class Definition and Initialization**
```python
class Car():
    def __init__(self, brand, model, milage, condition):
        self._brand = brand
        self._model = model
        self.milage = milage
        self.condition = condition
```
- This defines a class named `Car`.
- The `__init__` method is a special method called a constructor. It initializes the object's attributes when a new instance of the class is created.
- `self._brand` and `self._model` are prefixed with an underscore, which is a convention to indicate that these attributes are intended to be private.
- `self.milage` and `self.condition` are public attributes.
1. **String Representation Method**
```python
def __str__(self):
    return f"""
    Das Fahrzeug ist das Modell {self.model} der Marke {self.brand},
    hat einen Kilometerstand von {self.milage} km und ist in
    {"gutem" if self.condition > 50 else "schlechtem"} Zustand
    """
```
- The `__str__` method is another special method that defines how the object is represented as a string.
- It uses an f-string to format the output, including the model, brand, milage, and condition of the car.
- The condition is evaluated to be "gutem" (good) if `self.condition` is greater than 50, otherwise "schlechtem" (bad).
1. **Creating an Instance and Printing**
```python
print(Car('Porsche', '964', 150000, 41))
```
- This line creates an instance of the `Car` class with the specified attributes and prints it.
- The `print` function calls the `__str__` method of the `Car` instance to get its string representation.
### Answer Explanations
✅ **Correct,** because the program can already run without errors. Implementing getter and setter methods for `milage` and `condition` would not affect the current functionality.
❌ **Incorrect,** because the `__init__` method directly assigns values to `milage` and `condition` without requiring setter methods. The program runs fine without them.
❌ **Incorrect, **because the `print` function is given a reference to a `Car` object. The `__str__` method of the `Car` class provides the string representation needed for printing.
❌ **Incorrect,** because the provided `__str__` method references `self.brand` and `self.model`, but these attributes are not directly accessible. They should be accessed through the getter methods (e.g., `self.brand()` and `self.model()`). Without the correct getter methods, the program will raise an `AttributeError`.
✅ **Correct,** because the program can run without errors, assuming the correct getter methods for `brand` and `model` are implemented.
❌ **Incorrect, **incorrect because some of the other statements are indeed correct.
</details>
---
## Question 4
Markieren Sie **alle** zutreffenden Aussagen.
Methoden, die in Python innerhalb von Klassendefinitionen definiert werden:
❌ können auch ohne Referenz zum aufrufenden Objekt *(self)* ausgeführt werden.
❌ können nicht ohne Argumente in den runden Klammern aufgerufen werden, z.B. *objekt_name.methoden_name()*, da immer die Referenz auf *self* notwendig ist.
✅ können, wenn sie genauso heissen wie Methoden ihrer *Superklasse***, ***polymorph* aufgerufen werden.
✅ können *Default-Werte* als Argumente besitzen.
✅ können Argumente an *bestimmten Positionen* (*positional arguments*) erwarten.
❌ sind, auch wenn Sie einen Property-Decorator (*@property*) haben, beim Aufruf durch Client-Code immer als Methoden erkennbar.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Class inheritance](/c991314990fa47e19addaf16235213db), [polymorphism](/1847b80cf96b485da5725e3cd1b35ca9)**
❌ **Incorrect**, in Python, methods defined within a class typically require a reference to the instance of the class, which is usually named `self`. This allows the method to access attributes and other methods of the instance. Without `self`, the method wouldn't know which instance's data to operate on.
If `self` is omitted, the method cannot be called on an instance of the class.
```python
class MyClass:
    def my_method(self):
        print("Hello, World!")

obj = MyClass()
obj.my_method()  # This works because my_method takes self as an argument.
```
❌ **Incorrect**, because when you call a method on an object, you do not need to explicitly pass `self`. Python automatically passes the instance as the first argument.
```python
obj.my_method()  # You don't need to pass self explicitly.
```
✅ **Correct**, Polymorphism allows methods in a subclass to have the same name as methods in a superclass. When you call such a method on an instance of the subclass, the subclass's method is executed.
This demonstrates polymorphism, where the method in the subclass overrides the method in the superclass.
```python
class SuperClass:
    def my_method(self):
        print("SuperClass method")

class SubClass(SuperClass):
    def my_method(self):
        print("SubClass method")

obj = SubClass()
obj.my_method()  # This will print "SubClass method"
```
✅ **Correct**, methods in Python can have default values for their parameters. This means that if no argument is provided for that parameter, the default value is used.
Here, `x` has a default value of 10.
```python
class MyClass:
    def my_method(self, x=10):
        print(x)

obj = MyClass()
obj.my_method()  # This will print 10
obj.my_method(20)  # This will print 20
```
✅ Correct, methods can expect positional arguments, which are arguments that need to be provided in a specific order.
In this example, `x` and `y` are positional arguments.
```python
class MyClass:
    def my_method(self, x, y):
        print(x, y)

obj = MyClass()
obj.my_method(1, 2)  # This will print 1 2
```
❌ **Incorrect**, the `@property` decorator in Python allows you to define methods that can be accessed like attributes. This means that when you use a property, it doesn't look like a method call.
```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

obj = MyClass(10)
print(obj.value)  # This will print 10, and it looks like accessing an attribute, not calling a method.
```
</details>
---
## Question 5
In Python ist die Instanz einer Unterklasse U (*sub class*), welche von der Superklasse S (*super class*) erbt, auch immer eine Instanz von *object*.
❌ Die Frage kann mit den gemachten Angaben nicht eindeutig beantwortet werden.
✅ Wahr
❌ Falsch

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Class inheritance](/c991314990fa47e19addaf16235213db)**
### Example Code
Before explaining the answer options, let's look at a simple example to illustrate inheritance:
```python
class S:
    pass

class U(S):
    pass

u_instance = U()
print(isinstance(u_instance, U))      # True
print(isinstance(u_instance, S))      # True
print(isinstance(u_instance, object)) # True
```
- `class S:` defines a superclass `S`.
- `class U(S):` defines a subclass `U` that inherits from `S`.
- `u_instance = U()` creates an instance of the subclass `U`.
- `print(isinstance(u_instance, U))` checks if `u_instance` is an instance of `U`, which is `True`.
- `print(isinstance(u_instance, S))` checks if `u_instance` is an instance of `S`, which is also `True` because `U` inherits from `S`.
- `print(isinstance(u_instance, object))` checks if `u_instance` is an instance of `object`, which is `True` because all classes in Python inherit from `object`.
### Answer Options
❌ **Incorrect,** because the question can be answered with the given information. In Python, all classes inherit from `object`, so an instance of any subclass will also be an instance of `object`.
✅ Correct, as shown in the example, an instance of a subclass is always an instance of `object` because all classes in Python inherit from `object`.
❌ **Incorrect**, because it contradicts the fundamental inheritance structure in Python. Every class, whether it's a subclass or not, is derived from `object`.
</details>
---

📄 **[Quiz 5]** (subpage)
## Question 1
Sie rufen im Webbrowser [**http://example.org**](http://example.org/) auf, während Sie die Pakete mit Wireshark verfolgen. Was würden Sie sehen?
❌ Sie sehen, dass es sich um eine HTTP-Anfrage an eine URL handelt, aber das HTTP-Verb (GET) und der Anfrageinhalt sind verschlüsselt.
✅ Sie können die IP- und TCP-Pakete sehen, wie auch die Anwendungsdaten innerhalb des TCP-Pakets.
❌ Sie können sehen, dass eine HTTP-GET-Anfrage gesendet wird, aber die Ziel-IP-Adresse ist verschlüsselt, da wir ein sicheres Transportprotokoll verwenden.
❌ Der gesamte Netzwerkverkehr wird verschlüsselt, d.h., alle Anwendungs-, TCP- und IP-Pakete werden verschlüsselt, so dass ein Angreifer lediglich die Ziel-IP-Adresse kennt.
❌ Keine der anderen Antworten ist korrekt.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Networking stack](/305c770201f94279bfd468d86c733ae6), [HTTP request methods](/f6bdc16ceadd474d895561e3c6762d42)**
When you visit [**http://example.org**](http://example.org/) in your web browser, you are making an HTTP request. HTTP is a protocol used for transmitting web pages over the internet. Here’s what happens and what you would see in Wireshark:
- HTTP is not encrypted. This means that the data being sent and received can be read by anyone who intercepts the traffic.
- When you visit a website using HTTP, the request and response data are sent in plain text.
❌ **Incorrect**, HTTP traffic is not encrypted. If it were HTTPS (HTTP Secure), then the data would be encrypted, but the question specifies HTTP.
✅ **Correct,** since HTTP is not encrypted, you can see the IP and TCP packets, as well as the actual data being transmitted (the application data) within the TCP packets. This includes the HTTP GET request and any other data being sent.
❌ **Incorrect,** the target IP address is not encrypted in HTTP traffic. Secure transport protocols like HTTPS would encrypt the data, but not the IP address.
❌ **Incorrect,** this describes HTTPS, not HTTP. In HTTP, none of the traffic is encrypted.
❌ **Incorrect,** one of the other answers is correct, specifically the one stating that you can see the IP and TCP packets and the application data within the TCP packets.
</details>
---
## Question 2
Sie möchten ein Experiment durchführen, bei dem Sie einen Webbrowser, z.B. Firefox, öffnen und auf [https://example.org](https://example.org/) gehen. Parallel dazu zeichnen Sie mit Wireshark die Pakete im Netzwerk auf. Welche der folgenden Aussagen sind richtig?
Wählen Sie *alle* richtigen Aussagen aus.
✅ Der Name ([example.org](http://example.org/)) wird vom DNS auf eine zugehörige IP-Adresse abgebildet. Dabei spielt es keine Rolle, ob Sie **http** oder **https** verwenden.
❌ Um die IP-Adresse von [example.org](http://example.org/) zu ermitteln, werden die Router entlang der Route zu [example.org](http://example.org/) abgefragt.
✅ Auf Wireshark können Sie den HTML-Inhalt der Antwort des Servers **nicht** sehen.
❌ Abhängig davon, ob Ihr Computer via Kabel (Ethernet) oder kabellos (WIFI) mit dem Internet verbunden ist, benötigen Sie zuerst eine DNS-Abfrage (oder eben nicht), um [https://example.org](https://example.org/) zu erreichen.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Networking stack](/305c770201f94279bfd468d86c733ae6), [DNS](/98fd60d45a0a4426a6f28d2665ba5a43#56e2d7cb60a34ae29ac8a805c79f51d8), [HTTP request methods](/f6bdc16ceadd474d895561e3c6762d42)**
✅ **Correct**, DNS (Domain Name System) is like the phonebook of the internet. It translates human-readable domain names (like [example.org](http://example.org/)) into IP addresses that computers use to identify each other on the network. This process is the same whether you are using HTTP or HTTPS. The protocol (HTTP or HTTPS) does not affect the DNS resolution process.
❌ **Incorrect**, DNS resolution does not involve querying routers along the route to the destination. Instead, it involves querying DNS servers. When you type a domain name into your browser, your computer contacts a DNS server (often provided by your ISP or a public DNS service like Google DNS) to resolve the domain name to an IP address. Routers are involved in routing the packets to the destination once the IP address is known, but they do not play a role in the DNS resolution process.
✅ **Correct**, HTTPS encrypts the data between your browser and the server, so tools like Wireshark cannot see the actual content of the data being transmitted. You can see the encrypted packets, but not the decrypted HTML content. If you were using HTTP (which is not encrypted), you would be able to see the HTML content in Wireshark.
❌ **Incorrect**, regardless of whether your computer is connected via Ethernet or WiFi, a DNS query is required to resolve the domain name to an IP address. The method of connection (wired or wireless) does not affect the necessity of a DNS query.
</details>
---
## Question 3
Gegeben ist der folgende Code, der Teile von Assignment 6 implementiert. Sie wollen alle gerade offenen Restaurants in einem gegebenen Radius finden.
```python
def find_restaurants(x, y, open_at, radius):
	url = '<https://api.yelp.com/v3/businesses/search>'
	restaurants = []
	params = {}
	params['latitude'] = x
	params['longitude'] = y
	params['open_at'] = open_at
	params['radius'] = radius
	params['categories'] = "restaurants"
	r = requests.get(url, params=params)
```

Bitte markieren Sie **alle** richtigen Aussagen.
❌ In Zeile 10 muss ein *PUT* request genutzt werden, um die Parameter zu setzen.
✅ Statt *open_at* sollte besser der Parameter *open_now* verwendet werden, um sicher zu jeder Zeit die aktuell geöffneten Restaurants zu finden.
❌ Es gibt kein Problem mit dem Code, er wird funktionieren.
✅ Die Anfrage wird zu einem Autorisierungsfehler (*authorization failure*) führen - Sie müssen den API-Schlüssel (*API key*) angeben!

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[API requests](/b431f30ba0674f04a6c836035b69ea8e), [HTTPS](/923d77685b5c46518f7726145cfce814), [TLS](/923d77685b5c46518f7726145cfce814)**
### Code Explanation
```python
def find_restaurants(x, y, open_at, radius):
    url = '<https://api.yelp.com/v3/businesses/search>'
    restaurants = []
    params = {}
    params['latitude'] = x
    params['longitude'] = y
    params['open_at'] = open_at
    params['radius'] = radius
    params['categories'] = "restaurants"
    r = requests.get(url, params=params)
```
1. **Function Definition**:
- `def find_restaurants(x, y, open_at, radius):` defines a function named `find_restaurants` that takes four parameters: `x` (latitude), `y` (longitude), `open_at` (time), and `radius` (search radius).
1. **URL and Parameters**:
- `url = '<https://api.yelp.com/v3/businesses/search'`> sets the URL for the Yelp API endpoint to search for businesses.
- `params = {}` initializes an empty dictionary to store the parameters for the API request.
- The next lines add key-value pairs to the `params` dictionary for latitude, longitude, open_at, radius, and categories.
1. **API Request**:
- `r = requests.get(url, params=params)` sends a GET request to the Yelp API with the specified parameters.
### Answer Explanations
❌ **Incorrect,** a PUT request is used to update resources on a server. In this case, we are retrieving data, so a GET request is appropriate.
✅ **Correct,** the `open_now` parameter is used to find businesses that are currently open at the time of the request. This is more straightforward than using `open_at`, which requires specifying a specific time.
❌ **Incorrect,** the code will not work as intended because it lacks an API key, which is required for authorization when making requests to the Yelp API.
✅ **Correct,** the Yelp API requires an API key for authorization. Without including the API key in the request headers, the request will fail with an authorization error.
### Corrected Code Example
Here is an example of how you might include the API key in the request:
```python
import requests

def find_restaurants(x, y, open_now, radius, api_key):
    url = '<https://api.yelp.com/v3/businesses/search>'
    headers = {
        'Authorization': f'Bearer {api_key}',
    }
    params = {
        'latitude': x,
        'longitude': y,
        'open_now': open_now,
        'radius': radius,
        'categories': "restaurants"
    }
    r = requests.get(url, headers=headers, params=params)
    return r.json()

# Example usage:
# api_key = 'your_api_key_here'
# print(find_restaurants(37.7749, -122.4194, True, 1000, api_key))
```
In this corrected code:
- `headers` is a dictionary that includes the API key for authorization.
- The `requests.get` function now includes the `headers` parameter to pass the API key along with the request.
</details>
---
## Question 4
Sie öffnen einen Browser auf Ihrem PC und rufen die Seite [https://www.unisg.ch](https://www.unisg.ch/) auf. Gehen Sie davon aus, dass Sie nur über Ihr Heimnetzwerk mit dem Internet verbunden sind.
Was ist die richtige Reihenfolge der ausgeführten Schritte?
✅ **Der Browser formuliert eine HTTP-GET-Anfrage, ermittelt die IP-Adresse des Servers über DNS, verpackt das HTTP in ein TCP-Segment (mit dem https-Standardport 443), verpackt dieses Paket in ein IP-Paket mit den richtigen Adressinformationen und schickt es auf das Trägermedium (natürlich ordnungsgemäss verpackt für dieses Trägermedium).**
❌ Der Browser formuliert eine HTTP-POST-Anfrage, erhält die IP-Adresse des Servers über UDP, verpackt das HTTP in ein DNS-Segment (am https-Standardport 80), verpackt dieses Paket in ein IP-Paket mit den richtigen Adressinformationen und schickt es auf das Trägermedium (natürlich ordnungsgemäss verpackt für dieses Trägermedium).
❌ Der Browser formuliert eine HTTP-POST-Anfrage, ermittelt die IP-Adresse des Servers über DNS, verpackt das HTTP in ein TCP-Segment (mit dem https-Standardport 443), verpackt dieses Paket in ein IP-Paket mit den richtigen Adressinformationen und schickt es auf das Trägermedium (natürlich ordnungsgemäss verpackt für dieses Trägermedium).
❌ Der Browser formuliert eine HTTP-GET-Anfrage, ermittelt die IP-Adresse des Servers über DNS, verpackt das HTTP in ein UDP-Segment (mit dem https-Standardport 440), verpackt dieses Paket in ein TCP-Segment mit den richtigen Adressinformationen und schickt es auf das Trägermedium (natürlich ordnungsgemäss verpackt für dieses Trägermedium).

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Networking stack](/305c770201f94279bfd468d86c733ae6)**
Let's break down the correct answer and why the other options are incorrect.
### Correct Answer Explanation
**✅ Statement 1 **
1. ***…HTTP-GET-Anfrage…***
- When you open a webpage, the browser typically sends an HTTP GET request to retrieve the content of the page.
- Example: `GET / HTTP/1.1`
1. ***…ermittelt die IP-Adresse des Servers über DNS...***
- DNS (Domain Name System) translates the human-readable domain name (e.g., [www.unisg.ch](http://www.unisg.ch/)) into an IP address that computers can use to identify each other on the network.
- Example: `www.unisg.ch` might be translated to `192.0.2.1`.
1. ***…verpackt das HTTP in ein TCP-Segment…***
- HTTP requests are sent over TCP (Transmission Control Protocol), which ensures reliable delivery of data.
- The standard port for HTTPS (secure HTTP) is 443.
1. ***…verpackt dieses Paket in ein IP-Paket…***
- The TCP segment is then encapsulated in an IP packet, which includes the source and destination IP addresses.
1. ***…schickt es auf das Trägermedium…***
- Finally, the IP packet is sent over the physical network medium (e.g., Ethernet, Wi-Fi) to reach the destination server.
### Incorrect Answers Explanation
**❌ Statement 2**
- **HTTP-POST-Anfrage**: Incorrect because a POST request is typically used to send data to the server, not to retrieve a webpage.
- **UDP for DNS**: DNS queries can use UDP, but the rest of the statement is incorrect.
- **DNS-Segment**: There is no such thing as a DNS segment for HTTP data.
- **Port 80**: Port 80 is used for HTTP, not HTTPS.
**❌ Statement 3**
- **HTTP-POST-Anfrage**: Incorrect because a GET request is typically used to retrieve a webpage, not a POST request.
**❌ Statement 4**
- **UDP-Segment**: HTTP data is not sent over UDP; it is sent over TCP.
- **Port 440**: The standard port for HTTPS is 443, not 440.
- **TCP-Segment**: The statement is confusing because it mentions both UDP and TCP, which is incorrect for HTTP data transmission.
</details>
---
## Question 5
Geben ist der folgende Code, der Teile von Assignment 6 implementiert.
```python
def find_connection(origin, destination, departure_date, departure_time):
    url = '<http://transport.opendata.ch/v1/connections>'
    params = {}
    params['from'] = origin
    params['to'] = destination
    params['time'] = departure_time

    r = requests.get(url, params = params)
    first_conn- r.json()['connections'][0]
    x = first_conn['to']['coordinate']['x']
    y = first_conn['to']['coordinate']['y']
    departure = first_conn['from']['departure']
    arrival = first_conn['to']['arrival']
    transport_means = first_conn['products']
```
Bitte markieren Sie **alle** richtigen Aussagen.
✅ Die Zeilen, die x und y aus der Antwort abrufen, sind falsch. Es sollte first_conn['to']['station']['coordinate']['x'] bzw. first_conn['to']['station']['coordinate']['y'] lauten.
❌ Die Anfrage wird zu einem Autorisierungsfehler (*authorization failure*) führen - Sie müssen den API-Schlüssel (*API key*) angeben!
❌ Die Anfrage wird fehlschlagen, da wir POST und nicht GET verwenden müssen.
✅ **Der Code wird so nicht korrekt funktionieren.**
❌ [*opendata.ch*](http://opendata.ch/) kann nur über HTTPS erreicht werden, daher wird die Anfrage fehlschlagen.
✅ **Das Abreisedatum (*****departure date*****) fehlt in den Anfrageparametern.**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Transport Open Data API](https://transport.opendata.ch/docs.html), [requests library](/b431f30ba0674f04a6c836035b69ea8e)**
Let's break down the provided code and the answer options to understand why the correct answers are marked as they are.
### Code Explanation
1. **Function Definition:**
```python
def find_connection(origin, destination, departure_date, departure_time):
```
- This line defines a function named `find_connection` that takes four parameters: `origin`, `destination`, `departure_date`, and `departure_time`.
1. **URL and Parameters:**
```python
url = '<http://transport.opendata.ch/v1/connections>'
params = {}
params['from'] = origin
params['to'] = destination
params['time'] = departure_time
```
- `url` is the endpoint for the API.
- `params` is a dictionary that will hold the parameters for the API request.
- The parameters `from`, `to`, and `time` are set using the function's arguments.
1. **API Request:**
```python
r = requests.get(url, params=params)
```
- This line sends a GET request to the specified URL with the given parameters.
1. **Extracting Data:**
```python
first_conn = r.json()['connections'][0]
x = first_conn['to']['coordinate']['x']
y = first_conn['to']['coordinate']['y']
departure = first_conn['from']['departure']
arrival = first_conn['to']['arrival']
transport_means = first_conn['products']
```
- `r.json()` converts the response to a JSON object.
- `first_conn` extracts the first connection from the JSON response.
- The subsequent lines extract specific details from `first_conn`.
### Answer Explanations
✅ **Correct,** the lines that retrieve `x` and `y` coordinates are incorrect. They should be:
```python
x = first_conn['to']['station']['coordinate']['x']
y = first_conn['to']['station']['coordinate']['y']
```
- The correct path to the coordinates includes the `station` key.
❌ **Incorrect, **the request will not lead to an authorization failure because the API endpoint does not require an API key for this specific request.
❌ **Incorrect, **the request will not fail because of using GET instead of POST. The API documentation specifies that GET is the correct method for retrieving connections.
✅ **Correct, **the code will not work correctly as it stands. There are issues with the path to the coordinates and the missing departure date in the parameters.
❌ **Incorrect,** the endpoint `http://transport.opendata.ch/v1/connections` can be accessed over HTTP, not just HTTPS. Therefore, the request will not fail due to this reason.
✅ **Correct,** the departure date is missing in the request parameters. It should be included like this:
```python
params['date'] = departure_date
```
</details>
---

📄 **[Quiz 6]** (subpage)
## Question 1 
Gegeben ist folgender *pd.DataFrame df*. Die Spalte **index** ist definiert als der Index von df.
| index | value0 | value1 |
| --- | --- | --- |
| 2 | 947 | 363 |
| 22 | 926 | 30 |
| 10 | 403 | 66 |
| 25 | 581 | 10 |
| 31 | 714 | 513 |
| 5 | 897 | 604 |
| 13 | 118 | 827 |
| 14 | 56 | 514 |
| 33 | 154 | 82 |
Welcher **Wert** wird von folgendem Code zurückgegeben: *df.loc[25].sum()*
**591**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.sum()](/1867045b058343e1a66b677961515907#6f1bd7bccbe24ecf8bcb37abc05b0550)**
1. **DataFrame Structure**:
- The DataFrame `df` has three columns: `index`, `value0`, and `value1`.
- The `index` column is set as the index of the DataFrame, meaning it is used to label the rows.
```plain text
| index | value0 | value1 |
|-------|--------|--------|
| 2     | 947    | 363    |
| 22    | 926    | 30     |
| 10    | 403    | 66     |
| 25    | 581    | 10     |
| 31    | 714    | 513    |
| 5     | 897    | 604    |
| 13    | 118    | 827    |
| 14    | 56     | 514    |
| 33    | 154    | 82     |
```
1. **Code Explanation**:
- `df.loc[25]`:
- This line accesses the row in the DataFrame where the index is `25`.
- The row with index `25` is:
```plain text
| index | value0 | value1 |
|-------|--------|--------|
| 25    | 581    | 10     |
```
- `.sum()`:
- This method sums up all the values in the selected row.
- For the row with index `25`, the values are `581` and `10`.
- Summing these values:
```plain text
581 + 10 = **591**
```
</details>
---
## Question 2
In Assigment 8 haben wir aus der Datei *movies.csv* den pd.DataFrame **DF** geladen. Dieser enthält diverse Informationen über viele Filme. Wir nehmen an, dass er in der Spalte color die Information enthält, ob es sich um einen Farbfilm oder einen schwarz/weiss-Film handelt. In der Spalte *movie_facebook_likes* gibt es die absolute Anzahl von Likes des Filmplakiums für jeden Film und in der Spalte budget das Invest in einen Film in US-Dollar.
Hier wollen wir die Funktionen aus dem Assigment um eine weitere Funktion **black_and_white_or_color()** erweitern. Die Idee ist es herauszufinden, welche Filme (Gruppiert nach Werten von *color*) das bessere Invest sind - gemessen in Facebook-Likes pro Million US-Dollar Budget. Die Funktion soll einige Details zur Analyse auflisten und den vorteilhaftesten Wert für *color* zurückgeben.
Wir haben diese Funktion wie folgt implementiert:
```python
1  def black_and_white_or_color():
2      df = DF.copy()
3
4      # wir wollen keine Filme ohne Likes, da es das Ergebnis verzerren könnte
5      df = df[df['movie_facebook_likes'] > 0]
6
7      # hier bilden wir das Verhältnis zwischen den Facebook-Likes und
8      # dem Budget eines Films in Millionen Dollar
9      df['likes_per_million_budget'] = (df['movie_facebook_likes'] / df['budget']) * 1_000_000
10
11     # dann brauchen wir noch zwei Hilfsvariablen
12     colors = df['color'].unique().dropna()
13     color_rating = pd.Series()
14
15     # hier iterieren wir über alle gültigen Werte von 'colors'
16     # und geben das durchschnittliche Verhältnis 'likes_per_million_budget'
17     # für 'color' aus bzw. speichern diese in unserer Hilfsvariable
18     # color_rating. Wir nutzen zudem die .strip()-Methode
19     # um Datenuntypische Abstände zu beheben (Leerzeichen am Anfang oder Ende)
20     # der Werte in df['color'] bzw. 'colors'.
21     for color in colors:
22         print(f"""{color.strip(' ')} movies we get an average number of like.                                             per million dollar of
23     budget of {df[df['color'] == color]['likes_per_million_budget'].mean().round(0)}\\n""")
24         color_rating[color.strip(' ')] = df[df['color'] == color]['likes_per_million_budget'].mean().round(0)
25
26     # und ein Fazit:
27     print(f'Thus, {color_rating.idxmax().strip(' ')} movies may be a better invest')
28
29     return color_rating.idxmax().strip(' ')
```

Die Frage ist nun, warum funktioniert die Funktion nicht wie gewünscht?
1. ❌ In Zeile 21 darf die Target-Variable nicht *color* heissen, da es diesen Variablennamen schon in *df* bzw *DF* gibt.
1. ❌ In Zeile 12 braucht es ein axis Keyword-Argument, um die richtige Dimension zu wählen.
1. ❌ Zeile 23: Man kann einen DataFrame so nicht runden (round(0)).
1. ✅ Die Aussage ist falsch, denn tatsächlich funktioniert die vervollständigte Funktion wie beschrieben.
1. ❌ Die Aussage ist falsch, denn tatsächlich funktioniert die vervollständigte Funktion wie beschrieben.
1. ❌ In den Zeilen 22 und 23 sind die Anführungszeichen durcheinander geraten und es sind auch zu viele.
1. ❌ In Zeile 9 sind die Klammern falsch gesetzt, d.h. die Python-Syntax ist falsch.
1. ❌ Es ist nicht klar, mit welchem DataFrame wir eigentlich arbeiten, da wir mal df und mal DF nutzen, Python-Variablen aber case sensitive sind.
1. ❌ Es besteht ein anderes als die vorgenannten Probleme mit dem Code.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.copy()](/1867045b058343e1a66b677961515907#3ee249c7635744768a6ac56eb7e7f728), [.strip()](/5b0832dbf9454eb1941b7632e68a9abb#979e1c6634f843ffb1b7c6b31d78c060), [.round()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html), [.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
Let's break down the provided code and the answer options to understand why the correct answer is marked as it is.
### Code Explanation
1. **Function Definition and DataFrame Copy**
```python
def black_and_white_or_color():
    df = DF.copy()
```
- This defines a function named `black_and_white_or_color`.
- It creates a copy of the DataFrame `DF` and assigns it to `df`.
1. **Filtering Out Movies Without Likes**
```python
df = df[df['movie_facebook_likes'] > 0]
```
- This line filters out rows where the `movie_facebook_likes` column has a value of 0 or less.
1. **Calculating Likes Per Million Dollar Budget**
```python
df['likes_per_million_budget'] = (df['movie_facebook_likes'] / df['budget']) * 1_000_000
```
- This calculates the number of Facebook likes per million dollars of budget for each movie and stores it in a new column `likes_per_million_budget`.
1. **Unique Colors and Helper Variables**
```python
colors = df['color'].unique().dropna()
color_rating = pd.Series()
```
- `colors` stores unique values from the `color` column, excluding any `NaN` values.
- `color_rating` is an empty Pandas Series that will store the average likes per million budget for each color.
1. **Iterating Over Colors and Calculating Averages**
```python
for color in colors:
    print(f"""{color.strip(' ')} movies we get an average number of likes per million dollar of
budget of {df[df['color'] == color]['likes_per_million_budget'].mean().round(0)}\\n""")
    color_rating[color.strip(' ')] = df[df['color'] == color]['likes_per_million_budget'].mean().round(0)
```
- This loop iterates over each unique color.
- It prints the average likes per million budget for movies of that color.
- It also stores this average in the `color_rating` Series.
1. **Finding and Printing the Best Investment**
```python
print(f'Thus, {color_rating.idxmax().strip(' ')} movies may be a better invest')
return color_rating.idxmax().strip(' ')
```
- This prints which color of movies has the highest average likes per million budget.
- It returns the color with the highest average.
### Answer Options
1. ❌ **Incorrect, t**he variable `color` in the loop does not conflict with the column name `color` in the DataFrame.
1. ❌ **Incorrect, **the `unique()` method does not require an `axis` argument.
1. ❌ Inc**orrect, **the `round(0)` method is being applied on a single value (the mean of likes per million budget) which does not cause any issue.
1. ✅ **Correct,** the function works as described.
1. ❌ **Incorrect, **repeated incorrect statement.
1. ❌ **Incorrect, **the quotation marks are correctly used for the f-string.
1. ❌ **Incorrect, **the parentheses in line 9 are correctly placed.
1. ❌ **Incorrect,** the code consistently uses `df` after copying `DF`.
1. ❌ **Incorrect,** because the code works.
</details>
---
## Question 3
Gegeben ist ein *pd.DataFrame* **df**. Dieser hat neben einem Index eine Spalte **value0** und eine Spalte **value1**. Die beiden Spalten enthalten ganzzahlige (integer) Werte, jedoch fehlen auch einige Werte (NaN).
Bitte schreiben Sie Python-Code, welcher den Durchschnittswert (mean) der Werte in Spalte **value1** zurückgibt. Bei der Berechnung sollen nur die Werte von **value1** berücksichtigt werden, welche grösser als **10** sind. Schreiben Sie unter Verwendung der *mean()*-Methode aus Pandas nur eine Codezeile und verwenden Sie keine anderen zusätzlichen Libraries als Pandas. Sie können davon ausgehen, dass Pandas als *pd* importiert wurde.

**df.loc[df['value1']>10,'value1'].mean()**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
1. **Understanding the Task:**
- We need to calculate the mean of the values in the column `value1` of a DataFrame `df`.
- Only consider values in `value1` that are greater than 10.
- Use the `mean()` method from Pandas.
1. **Correct Code Analysis:**
- `df.loc[df['value1'] > 10, 'value1'].mean()`
- `df['value1'] > 10` creates a boolean Series where each element is `True` if the corresponding element in `value1` is greater than 10, and `False` otherwise.
- `df.loc[df['value1'] > 10, 'value1']` uses `.loc` to filter the DataFrame `df` to include only rows where `value1` is greater than 10, and then selects the `value1` column.
- `.mean()` calculates the mean of the filtered `value1` values.
</details>
---
## Question 4
Gegeben ist ein pd.*DataFrame* **df**, welcher mindestens eine Spalte mit dem eindeutigen Spaltennamen **spalte_1** hat, sowie der folgende Code:
**x = df['spalte_1'].iloc[42]**

Markieren Sie **alle** richtigen Aussagen.
1. ❌ Der Datentyp von **x** kann von der der Anzahl Spalten von **df** abhängen.
1. ✅ Die Codeausführung kann mit einem Fehler abbrechen.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *str* haben.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *int* haben.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *float64* haben.
1. ✅ Der Datentyp von **x** kann vom Inhalt der *NICHT-Index-Werte* von **df** abhängen.
1. ✅ Die Auswertung von **x.sum()** kann eine Gleitkommazahl (z.B. 7.2) ergeben.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *pd.DataFrame* haben.
1. ❌ Der Datentyp von **x** kann vom Inhalt der *Zeilen-Label* von **df** abhängen.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *pd.Series* haben.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.iloc[]](/1867045b058343e1a66b677961515907#659a00c8972e48a992e0dcabacb0cd4f), [pandas data types](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
### Code Explanation
```python
x = df['spalte_1'].iloc[42]
```
1. `df['spalte_1']`
- This part of the code selects the column named `'spalte_1'` from the DataFrame `df`.
- The result is a `pd.Series` object containing all the values from the column `'spalte_1'`.
1. `.iloc[42]`
- The `.iloc` method is used for integer-location based indexing.
- `iloc[42]` selects the 43rd element (since indexing starts at 0) from the `pd.Series` obtained in the previous step.
### Answer Explanations
1. ❌ Incorrect, the datatype of `x` depends on the value in the 43rd row of the column `'spalte_1'`, not on the number of columns in `df`.
1. ✅ Correct, if the DataFrame `df` has fewer than 43 rows, trying to access `iloc[42]` will result in an `IndexError`.
1. ✅ **Correct, i**f the value in the 43rd row of the column `'spalte_1'` is a string, then `x` will be of type `str`.
1. ✅ **Correct, **if the value in the 43rd row of the column `'spalte_1'` is an integer, then `x` will be of type `int`.
1. ✅ **Correct, **if the value in the 43rd row of the column `'spalte_1'` is a float, then `x` will be of type `float64`.
1. ✅ **Correct,** the datatype of `x` depends on the value in the 43rd row of the column `'spalte_1'`, which is a non-index value.
1. ✅ **Correct, **if `x` is a numeric type (like `int` or `float`), calling `x.sum()` will return the value itself, which can be a floating-point number.
1. ❌ **Incorrect, **`x` is a single value from a `pd.Series`, so it cannot be a `pd.DataFrame`.
1. ❌ **Incorrect, **the datatype of `x` depends on the value in the 43rd row of the column `'spalte_1'`, not on the row labels.
1. ❌ **Incorrect, **`x` is a single value from a `pd.Series`, so it cannot be a `pd.Series` itself.
</details>
---

📄 **[Quiz 7]** (subpage)
## Question 1
Gegeben ist der IRIS-Datensatz aus Assignment 9. Die Daten sind im DataFrame IRIS wie im Assignment geladen.

Ihr Ziel ist es, für jede Variable (*feature*) mit Verhältnisskala (*ratio scale*) der einzelnen Beobachtungen und gruppiert nach Untergattungen (*species*) jeweils den Minimal-, Maximal- und Durchschnittswert auszugeben. Die gewünschte Ausgabe soll also ähnlich der folgenden Darstellung sein:
```plain text
   variable 1
             min       max        mean

species A       4.3         5.8       5.006
species B       4.9         7.0       5.936
species C       4.9         7.9       6.588
```

```plain text
   variable 2
             min        max       mean

species A        2.3        4.4       3.418
species B        2.0        3.4       2.770
species C        2.2        3.8       2.974

                           variable n
                ...
```
Dazu haben Sie den nachfolgenden Code geschrieben. Dieser funktioniert allerdings überhaupt nicht wie gewünscht. Wo befindet sich der eine Fehler? Bitte geben Sie die Zeilennummer als ganze Zahl an.
```python
1    for col in IRIS.columns:
2        if col == 'species':
3            print(
4                IRIS.groupby('species').agg(
5                    {
6                        col:
7                        [
8                            'min',
9                            'max',
10                           'mean'
11                       ]
12                   }
13               ),
14               '\\n'
15           )
```

**2**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [if-statement](/5b0832dbf9454eb1941b7632e68a9abb#244a89d427db41da893178dcdf8d51d8), [.groupby()](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15), [.agg()](/1867045b058343e1a66b677961515907#1c8f902fb8774ff7ab8c9bd1d9f76684)**
Let's break down the provided code and the answer options to understand why the correct answer is marked as it is.
### Code Explanation
1. `for col in IRIS.columns:`
- This line starts a loop that iterates over each column name in the DataFrame `IRIS`.
1. `if col == 'species':`
- This line checks if the current column name is `'species'`.
1. `print(`
- This line starts a `print` statement to output the results.
1. `IRIS.groupby('species').agg(`
- This line groups the DataFrame `IRIS` by the `'species'` column and applies aggregation functions.
1. `{`
- This line starts a dictionary to specify the aggregation functions.
1. `col:`
- This line uses the current column name as the key in the dictionary.
1. `[`
- This line starts a list of aggregation functions.
1. `'min',`
- This line specifies the `min` function.
1. `'max',`
- This line specifies the `max` function.
1. `'mean'`
- This line specifies the `mean` function.
1. `]`
- This line closes the list of aggregation functions.
1. `}`
- This line closes the dictionary.
1. `),`
- This line closes the `agg` function and the `groupby` function.
1. `'\\n'`
- This line adds a newline character for formatting.
1. `)`
- This line closes the `print` statement.
### Identifying the Error
The code is intended to print the minimum, maximum, and mean values for each feature, grouped by species. However, the code only prints the results when the column name is `'species'`, which is not what we want. We want to skip the `'species'` column and process the other columns instead.
### Correct Answer
✅ **2**
The error is in line 2: `if col == 'species':`. This line should be changed to `if col != 'species':` to skip the `'species'` column and process the other columns.
### Corrected Code
Here is the corrected code:
```python
1    for col in IRIS.columns:
2        if col != 'species':  # Change this line to skip the 'species' column
3            print(
4                IRIS.groupby('species').agg(
5                    {
6                        col:
7                        [
8                            'min',
9                            'max',
10                           'mean'
11                       ]
12                   }
13               ),
14               '\\n'
15           )
```
Now, the code will correctly print the minimum, maximum, and mean values for each feature, grouped by species, excluding the `'species'` column itself.
</details>
---
## Question 2
**Gegeben sind zwei pd.DataFrame-Objekte ORDERS und PERSONS. Die Ausführung folgender Code-Zeile führt zu nachfolgender Ausgabe:**
```python
print(ORDERS.columns, ORDERS.index, PERSONS.columns, PERSONS.index, sep='\\n')
```
**Ausgabe:**
```python
Index(['products'], dtype='object')
Index([2, 3, 7, 8, 10, 13, 14, 15, 16,
...
99983, 99984, 99985, 99989, 99991, 99993, 99994, 99998, 99999],
dtype='int64', name='purchase-id', length=69703)
Index(['name',  'birthdate'], dtype='object')
Index([0, 1, 0, 3, 5, 8, 9, 10, 15, 16,
...
99979, 99980, 99981, 99984, 99987, 99991, 99992, 99995, 99997, 99998],
dtype='int64', name='purchase-id', length=59805)
```
Sie wollen beide Dataframes so zusammenführen (*merge*), dass der resultierende Dataframe alle Personen aus **PERSONS** enthält und bei den Personen, die eine Bestellung (*order*) getätigt haben, ausserdem auch die zugehörigen Informationen des **ORDERS** Dataframes enthält. Bestellungen, die zu keiner Person aus **PERSONS** zugeordnet werden können, sollen nicht enthalten sein. Bei der Zuordnung der Einträge aus **PERSONS** und **ORDERS** fungiert purchase-id als Schlüssel.
Bitte ersetzen Sie die im Programm mit AAA - EEE markierten Stellen so, dass die gewünschte Funktionalität erreicht wird.
```python
pd.merge(
    AAA,
    ORDERS,
    BBB_index=CCC,
    right_DDD=True,
    how=EEE
)
```
| AAA | ✅ PERSONS |
| --- | --- |
| BBB | ✅ left |
| CCC | ✅ True |
| DDD | ✅ index |
| EEE | ✅ 'left' |

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
Let's break down the provided code and the answer options to understand why the correct answer is marked as it is.
### Understanding the Code and Output
1. **Code to Print DataFrame Attributes:**
```python
print(ORDERS.columns, ORDERS.index, PERSONS.columns, PERSONS.index, sep='\\n')
```
- This code prints the column names and index values of the `ORDERS` and `PERSONS` DataFrames.
- `sep='\\n'` ensures that each attribute is printed on a new line.
1. **Output Explanation:**
```python
Index(['products'], dtype='object')
Index([2, 3, 7, 8, 10, 13, 14, 15, 16,
...
99983, 99984, 99985, 99989, 99991, 99993, 99994, 99998, 99999],
dtype='int64', name='purchase-id', length=69703)
Index(['name', 'birthdate'], dtype='object')
Index([0, 1, 0, 3, 5, 8, 9, 10, 15, 16,
...
99979, 99980, 99981, 99984, 99987, 99991, 99992, 99995, 99997, 99998],
dtype='int64', name='purchase-id', length=59805)
```
- `ORDERS` DataFrame has one column named `'products'` and an index named `'purchase-id'` with 69703 entries.
- `PERSONS` DataFrame has two columns named `'name'` and `'birthdate'` and an index named `'purchase-id'` with 59805 entries.
### Merging DataFrames
To merge the DataFrames as described, we need to:
- Include all rows from `PERSONS`.
- Include matching rows from `ORDERS` based on the `purchase-id`.
- Exclude rows from `ORDERS` that do not have a corresponding `purchase-id` in `PERSONS`.
### Correct Answer Breakdown
1. **AAA: ****`PERSONS`**
- We start with the `PERSONS` DataFrame because we want to include all persons.
- ✅ **Correct**: `PERSONS`
1. **BBB: ****`left`**
- We perform a left join to include all rows from the left DataFrame (`PERSONS`) and only matching rows from the right DataFrame (`ORDERS`).
1. **CCC: ****`True`**
- We specify that the join should be done on the index of the left DataFrame (`PERSONS`).
1. **DDD: ****`index`**
- We specify that the join should be done on the index of the right DataFrame (`ORDERS`).
1. **EEE: ****`'left'`**
- We specify the type of join as a left join to include all rows from `PERSONS`.
### Final Code
```python
pd.merge(
    PERSONS,  # AAA
    ORDERS,  # ORDERS DataFrame
    left_index=True,  # BBB_index=CCC
    right_index=True,  # right_DDD=True
    how='left'  # EEE
)
```
### Explanation of the Correct Answer
- **AAA: ****`PERSONS`**: We start with the `PERSONS` DataFrame because we want to include all persons.
- **BBB: ****`left`**: We perform a left join to include all rows from the left DataFrame (`PERSONS`) and only matching rows from the right DataFrame (`ORDERS`).
- **CCC: ****`True`**: We specify that the join should be done on the index of the left DataFrame (`PERSONS`).
- **DDD: ****`index`**: We specify that the join should be done on the index of the right DataFrame (`ORDERS`).
- **EEE: ****`'left'`**: We specify the type of join as a left join to include all rows from `PERSONS`.
By using these parameters, we ensure that all persons from the `PERSONS` DataFrame are included in the result, along with their corresponding orders from the `ORDERS` DataFrame, if any.
</details>
---
## Question 3
Gegeben ist folgende *txt-Datei*, sie liegt in einem Unterverzeichnis *data*:
### Daten.txt
```plain text
Name,Alter,Land
John,25,USA
Emily,30,UK
Karin,33,Switzerland
Michael,35,USA
Sophia,28,Germany
Urs,25,Switzerland
Maximilian,20,Germany
```
Diese Informationen werden in folgendem Programm verwendet, welches das Durchschnittsalter aller Personen aus den USA berechnen und ausgeben soll:
```python
print(f"""
Durchschnittsalter der Personen aus den USA:
{
    pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']['Alter'].mean()
}
""")
```
Bitte markieren Sie **alle korrekten** Aussagen:
✅ Das Programm kann ausgeführt werden, ohne dass Python einen Fehler wirft.
❌ Die `read_csv`-Funktion braucht weitere Parameter, um mit den gegebenen Daten das richtige Ergebnis zu erzeugen.
❌ Das Programm müsste statt der aktuellen Lösung in Zeile 4 zuerst die Spalte Alter selektieren, statt gleich den Wert USA zuzuweisen.
❌ Die `read_csv`-Funktion benötigt eine csv-Datei. Die hier genutzte txt-Datei ist dafür ungeeignet.
✅ Das Programm gibt das Durchschnittsalter der Personen aus den USA korrekt aus.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.read_csv()](/1867045b058343e1a66b677961515907#bb02198699ce440f948c4c281f1957ac), [.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
Let's break down the provided code and the answer options to understand why the correct answers are marked as they are.
### Provided Code Explanation
```python
print(f"""
Durchschnittsalter der Personen aus den USA:
{
    pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']['Alter'].mean()
}
""")
```
1. **`pd.read_csv('data/Daten.txt')`**:
- This function reads the file `Daten.txt` located in the `data` directory and loads it into a DataFrame.
- The file is in CSV format (Comma-Separated Values), which `read_csv` can handle even if the file extension is `.txt`.
1. **`pd.read_csv('data/Daten.txt')['Land'] == 'USA'`**:
- This part filters the DataFrame to include only the rows where the 'Land' column has the value 'USA'.
1. **`pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']`**:
- This applies the filter to the DataFrame, resulting in a new DataFrame containing only the rows where 'Land' is 'USA'.
1. **`pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']['Alter']`**:
- This selects the 'Alter' column from the filtered DataFrame.
1. **`pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']['Alter'].mean()`**:
- This calculates the mean (average) of the 'Alter' column for the filtered rows.
1. **`print(f"""\\nDurchschnittsalter der Personen aus den USA:\\n{ ... }\\n""")`**:
- This prints the average age of people from the USA using an f-string for formatting.
### Answer Explanations
✅ **Correct,** the code uses valid syntax and functions from the `pandas` library, so it will run without errors as long as the `pandas` library is installed and the file path is correct.
❌ **Incorrect, **the `read_csv` function works correctly with the default parameters for this file format. No additional parameters are needed.
❌ **Incorrect, t**he current approach is correct. It first filters the rows by 'Land' and then selects the 'Alter' column, which is the correct sequence to get the average age of people from the USA.
❌ **Incorrect, **the `read_csv` function can read files with any extension as long as the content is in CSV format. The `.txt` extension does not make the file unsuitable.
✅ **Correct, **the code correctly filters the DataFrame and calculates the mean of the 'Alter' column for rows where 'Land' is 'USA', so it will output the correct average age.
</details>
---
## Question 4
Sie haben erfolgreich aus einer relationalen Datenbank Kundendaten (*customers*) in einen DataFrame *df* geladen. Der folgende Code gibt die nachfolgenden Werte zurück:
```python
df = pd.read_sql('SELECT * FROM customers', DB)
df.tail()
```
| CustomerId | FirstName | LastName | Company | Address | City | State | Country | PostalCode | Phone | Fax | Email | SupportRepId |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 54 | 55 | Mark | Taylor | None | 421 Bourke Street | Sidney | NSW | Australia | 2010 | +61 (02) 9332 3633 | None | [mark.taylor@yahoo.au](mailto:mark.taylor@yahoo.au) |
| 55 | 56 | Diego | Gutiérrez | None | 307 Macacha Güemes | Buenos Aires | None | Argentina | 1106 | +54 (0)11 4311 4333 | None | [diego.gutierrez@yahoo.ar](mailto:diego.gutierrez@yahoo.ar) |
| 56 | 57 | Luis | Rojas | None | Calle Lira, 198 | Santiago | None | Chile | None | +56 (0)2 635 4444 | None | [luisrojas@yahoo.cl](mailto:luisrojas@yahoo.cl) |
| 57 | 58 | Manoj | Pareek | None | 12,Community Centre | Delhi | None | India | 110017 | +91 0124 38983988 | None | [manoj.pareek@rediff.com](mailto:manoj.pareek@rediff.com) |
| 58 | 59 | Puja | Srivastava | None | 3,Raj Bhavan Road | Bangalore | None | India | 560001 | +91 080 22289999 | None | [puja_srivastava@yahoo.in](mailto:puja_srivastava@yahoo.in) |
Für das Jubiläumsfest der Firma wollen Sie nun den/die erste/n Kunden/in aus jedem Land (*Country*) ausfindig machen. Dabei gehen Sie davon aus, dass diese Person die niedrigste Kundennummer (*CustomerId*) für das jeweilige Land hat.
Schreiben Sie Python-Code welcher eine *pandas.Series* zurückgibt, welche die Ländernamen als Label und die entsprechende Kundennummer als Werte enthält.
Schreiben Sie den Code in einer Zeile und halten Sie den Code minimal, d.h. verzichten Sie auf unnötige Sortierungen, etc. Wo notwendig verwenden Sie ausschließlich* Single Quotes* ( ' ' ), anstatt *Double* ( " " ) oder *Triple Quotes* ( """ """ ).
Auch wenn die Ausgabe es nahelegen scheint, können Sie nicht davon ausgehen, dass die Kundennummern in *df* in irgendeiner Weise sortiert sind.
Tip: Die groupby()-Methode wird hier hilfreich sein.

**Code:**
```python
df.groupby('Country')['CustomerId'].min()
```

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.groupby()](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15), [.min()](/1867045b058343e1a66b677961515907#dbdb31a72fac4ce0bc52e49458a2bf93)**
### Code Explanation
```python
df.groupby('Country')['CustomerId'].min()
```
1. **`df.groupby('Country')`**:
- This part of the code groups the DataFrame `df` by the 'Country' column. Grouping means that all rows with the same country name are put together.
1. **`['CustomerId']`**:
- After grouping by 'Country', this part selects the 'CustomerId' column from each group. So now, we are focusing only on the customer IDs within each country group.
1. **`.min()`**:
- This function calculates the minimum value of the 'CustomerId' column for each country group. Since we want the first customer (the one with the lowest customer ID) from each country, this function is perfect for our needs.
### Example DataFrame and Output
Given the example DataFrame:
| CustomerId | FirstName | LastName | Country |
| --- | --- | --- | --- |
| 54 | Mark | Taylor | Australia |
| 55 | Diego | Gutiérrez | Argentina |
| 56 | Luis | Rojas | Chile |
| 57 | Manoj | Pareek | India |
| 58 | Puja | Srivastava | India |
The output of the code would be a pandas Series like this:
```plain text
Country
Argentina    55
Australia    54
Chile        56
India        57
Name: CustomerId, dtype: int64
```
This Series shows the lowest 'CustomerId' for each country, which is exactly what we need for the company's anniversary event.
</details>
---

📄 **[Quiz 8]** (subpage)
## Question 1
Sie sind im Darknet auf alle Noten der letzten FCS-Kurse gestossen. Darin ist detailliert aufgeschlüsselt, wie engagiert sich die jeweiligen Studierenden vorbereitet haben. Es ist die Anwesenheit in den Vorlesungen und Übungen aufgezeichnet, (anwesend/nicht anwesend), die Verweildauer auf *Canvas*, sowie die jeweiligen Quizresultate, und natürlich die erreichte Note (1.0 bis 6.0, in 0.25-Schritten).
Sie möchten nun Ihre Note durch ein KNN-Modell vorhersagen lassen.
Markieren Sie **alle korrekten Aussagen**:
✅ Zur Validierung Ihres Ansatzes sollten Sie scikit-learns train_test_split-Funktion benutzen, um den Datensatz in zwei Teile zu teilen.
❌ Die Aufgabe ist ein *unsupervised Clustering*.
✅ Da der Datensatz mehrere tausend Einträge beinhaltet und damit als *gross* gilt, ist KNN nicht besonders gut als Modell geeignet.
❌ Das Training eines KNN-Modells ist nicht möglich, da die Features mehr als zwei Dimensionen (Anwesenheit, Verweildauer, Ergebnis Quiz 1, Ergebnis Quiz 2, ...) besitzen.
✅ Die Aufgabe ist eine Klassifikation.
❌ Die Aufgabe ist eine Regression.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[train_test_split()](/9e4a78074aea481ca4c75e506d4671c7#4929175cb8d34b8f97fbaca1a2271458), [supervised vs. unsupervised learning](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617), [KNN algorithm](/4e55bc27409940e98f9a060821d07644)**
Let's break down the provided statements and understand why the correct answers are marked as they are.
✅ **Correct, **when working with machine learning models, it's important to validate your approach to ensure it performs well on unseen data. The `train_test_split` function from the `scikit-learn` library is commonly used to split the dataset into a training set and a testing set. This helps in evaluating the model's performance.
❌ **Incorrect,** unsupervised clustering is used when you want to group data points into clusters without predefined labels. In this case, you have labeled data (grades), and you want to predict these labels based on features like attendance and quiz results. This is a supervised learning task, not unsupervised clustering.
✅ **Correct,** K-Nearest Neighbors (KNN) can be computationally expensive, especially with large datasets. This is because KNN requires calculating the distance between the query point and all points in the dataset to find the nearest neighbors. With thousands of entries, this can become very slow and resource-intensive.
❌ **Incorrect,** KNN can handle datasets with multiple dimensions (features). The number of dimensions does not prevent the training of a KNN model. In fact, KNN can work with any number of features, although the computational cost increases with the number of dimensions.
✅ **Correct,** the task is to predict the grade, which falls into discrete categories (e.g., 1.0, 1.25, 1.5, etc.). This makes it a classification problem because you are predicting a categorical outcome based on the input features.
❌ **Incorrect,** Regression is used when the target variable is continuous. In this case, the grades are discrete and fall into specific categories, making it a classification problem rather than a regression problem.
</details>
---
## Question 2
Sie haben in der Vorlesung *k-fold Cross-Validation* kennengelernt. Welche der folgenden Aussagen treffen zu?
Markieren Sie alle richtigen Aussagen.
❌ Jeder Datenpunkt kann mehrmals als Testdatenpunkt in der gesamten *K-Fold Cross-Validation* auftreten.
❌ Bei *K-Fold Cross-Validation* wird ein Modell erstellt, das iterativ auf den jeweiligen Folds trainiert wird.
✅ Bei der *K-Fold Cross-Validation* wird jeder Fold genau einmal als Testset verwendet.
❌ Bei *K-Fold Cross-Validation* wird das Modell nur einmal trainiert und dann auf einem einzigen Testset ausgewertet.
✅ *Cross-Validation* hilft Overfitting zu erkennen und zu vermeiden.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[k-fold Cross-Validation](/ce8b46807fc14f28839eb7b27e773558#bb510ed5d50e4570bd1cdc371c4d549c)**
### What is k-fold Cross-Validation?
K-fold Cross-Validation is a technique used in machine learning to evaluate the performance of a model. It involves splitting the dataset into `k` equally sized folds (subsets). The model is trained `k` times, each time using a different fold as the test set and the remaining `k-1` folds as the training set. This process helps in getting a more reliable estimate of the model's performance.
### Explanation of the Answer Options
❌ **Incorrect, i**n k-fold Cross-Validation, each data point is used exactly once as a test data point. This ensures that every data point is tested for its predictive power, but it does not appear more than once in the test set.
❌ **Incorrect,** while it is true that a model is trained iteratively on different folds, the statement is misleading because it suggests that a single model is iteratively updated. In reality, separate models are trained from scratch on each fold. Therefore, this statement is not entirely accurate.
✅ **Correct,** this is a fundamental property of k-fold Cross-Validation. Each fold is used exactly once as the test set, ensuring that every data point is tested once.
❌ **Incorrect,** this statement describes a simple train-test split, not k-fold Cross-Validation. In k-fold Cross-Validation, the model is trained `k` times, each time on a different training set and evaluated on a different test set.
✅ **Correct,** Cross-Validation, including k-fold Cross-Validation, helps in detecting and preventing overfitting. By evaluating the model on multiple test sets, it ensures that the model's performance is consistent and not just tailored to a specific subset of the data.
</details>
---
## Question 3
Ordnen Sie folgende Probleme der entsprechenden Kategorie zu.
**Klassifikation**
- Vorhersage von Aktienkurs (Steigend/Sinkend)
- IRIS-Datensatz

**Regression**
- Vorhersage von Aktienwerten
- Kreditrisikovorhersage (0-100%)
- Vorhersage der Länge der Blüten für den IRIS-Datensatz

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Classification vs. regression](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617)**
### Klassifikation (Classification)
Classification problems involve predicting a category or class label from a set of possible categories. Here are the examples given:
- **Vorhersage von Aktienkurs (Steigend/Sinkend)** 
This problem involves predicting whether a stock price will go up (steigend) or down (sinkend). There are only two possible outcomes, making it a binary classification problem.
- **IRIS-Datensatz** 
The IRIS dataset is a famous dataset in machine learning used for classification. It involves predicting the species of an iris flower (Setosa, Versicolor, or Virginica) based on features like petal length, petal width, etc. This is a multi-class classification problem.
### Regression
Regression problems involve predicting a continuous value. Here are the examples given:
- **Vorhersage von Aktienwerten
**This problem involves predicting the actual value of a stock price, which is a continuous number. Therefore, it is a regression problem.
- **Kreditrisikovorhersage (0-100%)
**This problem involves predicting the credit risk as a percentage between 0 and 100. Since the output is a continuous value, it is a regression problem.
- **Vorhersage der Länge der Blüten für den IRIS-Datensatz
**This problem involves predicting the length of the petals or sepals of iris flowers, which are continuous values. Therefore, it is a regression problem.
</details>
---
## Question 4
Markieren Sie alle wahren Aussagen bezüglich *Supervised Machine Learning* ("überwachtes maschinelles Lernen").
❌ Eine Regression ist kein *Supervised Machine Learning* ("überwachtes Lernverfahren"), da es keine diskreten Klassen, sondern stetige ("continuous") Zielwerte hat.
✅ Für ein glaubwürdiges Modell, das in einem *Supervised Machine Learning*-Ansatz trainiert werden soll, muss zwingend mindestens ein Train/Test-Split des Datensatzes durchgeführt werden.
❌ *Supervised Learning* hat die Bezeichnung daher, dass nach jedem Trainingsbeispiel eine menschliche Interaktion nötig ist.
❌ Die Erkennung von statistischen Ausreissern ("outlier") wird üblicherweise *supervised* ausgeführt.
✅ Wenn ein Datensatz neben den Features auch jedem Eintrag eine Klasse zugeordnet, kann darauf ein *supervised Machine Learning* Modell trainiert werden.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Supervised machine learning](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617)**
❌ **Incorrect,** Regression is indeed a type of Supervised Machine Learning. In supervised learning, the model is trained on labeled data, which means each training example is paired with an output label. Regression deals with continuous target values (like predicting house prices), while classification deals with discrete classes (like identifying if an email is spam or not). Both are forms of supervised learning.
✅ **Correct, **in supervised learning, it is essential to split the dataset into at least two parts: a training set and a test set. The training set is used to train the model, and the test set is used to evaluate its performance. This helps ensure that the model generalizes well to new, unseen data and is not just memorizing the training data.
❌ **Incorrect,** the term "supervised" in supervised learning does not imply that human interaction is needed after each training example. Instead, it means that the learning algorithm is provided with input-output pairs (labeled data) during training. The "supervision" comes from these labels, not from human intervention during the learning process.
❌ **Incorrect, **outlier detection is typically an unsupervised learning task. It involves identifying data points that deviate significantly from the rest of the dataset. Since outliers are not usually labeled in the data, unsupervised methods are often used to detect them.
✅ **Correct**, because supervised learning requires labeled data. If each entry in the dataset has associated features (input variables) and a class label (output variable), then a supervised learning model can be trained on this data. The model learns to map the features to the corresponding class labels.
</details>
---

📄 **[Quiz 9]** (subpage)
# Question 1
In einer Datenbank haben Sie mindestens die folgenden Tabellen (wie in Assignment 07):
- **students (id, first_name, last name, date _of_birth)**
- **registrations(id, student id, immatriculation, exmatriculation) **
- **courses (id, name, category)**
- **enrollments (id, student id, course_id, semester)**
- **grades (id, enrollment id, grade)**
Welche der folgenden Abfragen (queries) gibt die durchschnittliche Note (average grade) für eine/n Studierende/n pro Kurskategorie aus, von welcher/m Sie nur den Vor- (first name) und Nachnamen (last name) kennen?
❌ Query 1
```sql
SELECT category, AVG(grade) as average_grade
FROM grades
INNER JOIN enrollments ON enrollments.id = grades.enrollment_id
INNER JOIN courses ON courses.id = enrollments.course_id
WHERE students.first_name = ?
AND students.last_name = ?
GROUP BY grade
```
❌ Query 2
```sql
SELECT category, AVG(grade)
FROM grades g
INNER JOIN enrollments e ON e.id = g.enrollment_id
INNER JOIN courses c ON c.id = e.course id
INNER JOIN students s ON s.id = e.student_id
WHERE s.first_name = ?
AND s.last_name = ?
GROUP BY category
```
❌ Query 3
```sql
SELECT category, AVG(grade)
FROM grades
GROUP BY category
WHERE students.first_name = ?
AND students.last_name = ?
```
❌ Query 4
```sql
SELECT category, AVG(grade)
FROM grades
INNER JOIN enrollments ON enrollments.id = grades.enrollment_id
INNER JOIN courses ON courses.id = enrollments.course_id
INNER JOIN students ON students.id = enrollments.student_id
WHERE students.first_name = ?
AND students.last_name
GROUP BY students.id
```
✅ Query 5
```sql
SELECT category, AVG(grade)
FROM grades g
INNER JOIN enrollments e ON e.id = g.enrollment_id
INNER JOIN courses c ON c.id = e.course_id
INNER JOIN students s ON s.id= e.student_id
WHERE s.first_name = ? 
AND s.last_name = ?
GROUP BY category
```
❌ Das ist in einer einzigen Abfrage nicht möglich.
❌  Die Verteilung von Primär- (primary keys) und Fremdschlüsseln (foreign keys) ist in den gegebenen Tabellen auf keinen Fall ausreichend, um die gewünschten Ergebnisse zu erzielen.

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#f1c1f44f49aa4d76944c2d427c07c08f), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb), [AVG](/9f266597386048dd9a967fd9fd8e4b89#ca64b7e9f8c14563a40cd4d464dc5809), [GROUP BY](/9f266597386048dd9a967fd9fd8e4b89#01c3d00f4a9e49c483728e10edd3deba), [INNER JOIN](/9f266597386048dd9a967fd9fd8e4b89#f3ac72183aeb4fe7b12ff4cf12928a64)**
The question asks to write a query that computes the average grade of a specific student per course category. As we are looking for a value per course category, we expect **each course category to have one record** in the output table. Thus, we must look into the different code snippets and check where we find the following **GROUP BY** statement:
```sql
GROUP BY category
```
We can find this **GROUP BY** statement in the **fifth** code snippet.
To validate, that the fifth query is correct, let’s execute it step by-step.
1. We join **enrollments** and **grades** to know all the grades of all the students.
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
```

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9a3dd2fc-d3d3-4f80-a3d1-2525d393e718/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLTI7NM3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD04NmRtr7%2FwaEKPSyuVLYZKPNXzsEJS6tbcZfxZmcITQIhAPfVfcqw4h7iDX67zC46o7FydoA9MctF4EiSlL%2BAN%2FSZKv8DCCcQABoMNjM3NDIzMTgzODA1IgwDcIckQI6jWg%2BdYCoq3AM1blfa0ScL7JbkHq0tkeQhARYRs25SZI9kGALEOqq1fgv7XBngoK7jEtpPA7rS7%2FeH3CCXvFwQ3fnewBVe94FO0rGlO%2FCRlsXsT2f4LK3iJ6rFXVHdLLGA3vB%2BmU2uPUF0KwBBnoz%2FPnBVJizJ64Fm1%2FwBwLE%2BLcnDkEjkI%2Fv59MOKzW2FNEZY68HZ3lzuJiwFYCz%2F2K2GMZKtYZUnOrlldYq4u%2FeHYVF04KadYgA9DbIfAskp4MevuHRgBUwVr0G%2BiH2vsbgqshVKulzBnAXuuGtoJ9LEEdGjveBJGwioS15XsREvAjQRhV%2FC0OA3e0Yx8vJdivKQIshdvKJwdER5N05LgqL%2FzwqN%2BvPK0uiH%2BSrqOJowXGvdcUnnppmeGgIl%2B2SCksb7L%2Bq23Ck4Oxy0YUF0KrwpKSZSEHeg%2ByTEgrhb2jHyVFXauSu9rvlp%2B0cY%2FjpCI2Tr9%2BgDN4uCTpSMa38BjfoTwNM65QAGnx4Eftex9MtpR7BhhK1qzxU%2BUMNZ3d%2FWTO1P%2B0%2FxOiJASXOxNhLQ5FAYECuGI6lapfWd%2FesgmmcStbm9yq3e3Gz8lt%2Fl5Yzqey%2BsXugpquj1AT0TO2yzVvNnLkdlhuvbJtNBUWbWLnI1bW%2BDoImBHjDfzffJBjqkASd3lBzZapBvTZxzHFPcmlnZbnmKJdvOd8xR6G1qmZ6%2B2vdHTY3DeYaYj3MblEugvdbTT73Rj0S8HrO4ZUqb5TLvujnvIwfrfWQSC2FvHxn2PYlIznMZw%2Frhh9ywFJesNDWbTPeeJL78WeltDcXm4rym30yRbRmYu49vwrMYZNTIihcNfxr09Y3dw13SbjyJmNRALfMF9O%2FUa6Ey2nyajpHSwDVS&X-Amz-Signature=6576ed3b605bf806e49165bf0e9d23ba7d34c59aafa43358c4fcffa0d9ab2992&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join **enrollments** with **courses** to know in which course category the grade was achieved.
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bb58391f-28e2-4b87-9dfa-efb93b3c38dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RH6XMHOT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAWSCeLiQpgxToE9pc1RTk9k9a6BLVbddNcZvr9byMOKAiEAjmGSKGZGmY3RU0ldprrBR48UERZqPaqrUjy5EEp8VMQq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKZvEhiPzUpFjI30BircA9u6OgmvgtKy2VxRzVWmSELMLMvZsnp%2B6DH0Buw%2FTjpSR8S1YDoY8d0txDPB5HqkiAdSPjQd1cV3h4vsCFVmWGDx3rPPmmgX6x0MG36Zo54RCsDREj2RhrA9VKW4gYYiWwIW%2B4yqqlrTKA6Tf1TZk4r83KqO%2B12zy6SsGpmOmvH7s1bRR%2Fmgd%2BkSnaBbm5OBMMshSknEm3tE7q3LSgvjBHYZuq1h4D2IlezEntn50GBTYMV%2FEivWvuGgTR%2BY7qNDajN5wpyiGlM6PB%2FkL3RsAtfdfjcWj0rFPDf2BoremCSKV6hMevJN3skp%2BmY8yttf7yMoNl9xSm3XyTRK39983rRu8Oc1XKA435LdezIWk%2FZO4mLJN2rbE5i6HqdQaWQBEP53IuisEmjQFeHCaXgsa1J%2BhrDileUTW2983SAA%2Fwf0egvKiixlbMgrPCup2p7Afp%2BPpAYh7xxnrf38xahIUUWB2qTjGRysyyOaRMpOV3cyMgbHHGN5mX8XY9rHRwUjUi2CIFYoemDaa6nJIuICn5pXigX7oNYpJ%2FPmDtZssarfZprRYcYpo9uXVXsV9nmP9hUvZ0U2v2tBEMdt8JfGYwBVeFnVlri7V5GmPCigK1KgNWxM51VipPbJYtxuMOPN98kGOqUBwNBr1el2etHnz4W0c%2FkSIV%2BkSpM0I5uMzvTApoHHTkUqHWUXRdWLL%2FwjxQb%2FCkNKWOkSZVx2ZojjEjOxAcXEkXmWb8GDeCJ7VI7BJbUbPVIspRP2DA5p0JSYINd2wAxLk80bWo4x%2FL%2BAr3v1sKYsmiX52VeM3yzclkvFVUVS9qoHCooc1gq%2BgHH7Ew%2FinFILPd10VcCPC4fOc7cNFwYncuFdP5iC&X-Amz-Signature=7f751bcd707b3d57e4c2b53fdda86e0e3a792c9085e80eb47dfbdb5c45182f9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join **enrollments** with **students** to get the first and last names of the students.
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
INNER JOIN students s
	ON s.id = e.student_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/34d7ccd1-9629-46da-ab0a-5e19d5df29c6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647O357AG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQC7%2FHt%2Fo1KgmvR56I1bwgWvVl0dkrZaSWpaH8wckuYRZQIgb6qPdSJ8qFhD%2FSL9eerKeSqsEwyvqXCfmwFSFfBA2kwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIMon28aw%2FexuXEzbyrcA1XL3or1UBnXJH3DadJwVDGE4PfuduBLsTHqUE69Q8TT9NV31HFM1QfTK9cl0l9ENcCcIgLuGibGamUkcEV9QUrQ8PQywg3tzv3eL9IYWTqTUNF8es8eIXk%2BinXHMsvjuTmqnKlMaheLLwOX22KmBOmFZ4a7egEcSO4Es5FKoAllTlFYHq9qDHBV7iXdh4siIh2H17amnoHH0Ec3%2BNpylqzp7LvcW4yA5tha2hhocYn09C249yvILwffxJM7AQJQ6V1dFLXx%2BeO95YuItnTIvUE22J%2FS9m6kIVKP9PP%2Bu6Svb1Zi7M2sP%2FPMBAuwy15Yl023CO0j467J0ut9%2BLhFNqXj8VClpJ47fKentADp%2F920SDWOpvXlVpK1NOCT0hu4UmrHM2i4VMaoZeuwjJ7bhUTVoQA3hWs8se%2FnQExYz%2FfFNEP1txzVhbJvZaclulkq7vG2CY2mPxZ9oPg7b3j0lUTGoAoOHWj4dMyeFZ9Cs1ChQ9LE7iJ2%2Fs4aWkxd7ho9DpomaBv%2FZYYb52aQbEguorFEFrOj5RrRpYl15%2BjbGCbJYrGQI1MhWrmxwbFDxi8YM323QMAG95mAePWCO746Ap%2FbVg0P2%2FsBEoGC1JbP1%2BoFVkz7BG4lTS%2FP3MAQMPnN98kGOqUBnK8%2BxFt7r61oiYVCE3YTvvk8wPArehjqlGIsegGwAoONnDAcW0UX3u6%2BWhFdxdg2FW37WdxixDUP8B69DRlf6sB%2FG0vhMN6XRyDiHwDrKB3WYoenS5M%2Fkj45CuhJuBsnjWshUfr9TquQkBqf9c0FZEB639w3K1Hb81GO1A47aqFVE0C3dcdseXjr8uhdEQCWReYcsaXz66hoc8%2FsoWXZ%2BVvD6ROe&X-Amz-Signature=0abb11bf228ded22b75fc2f34386d879b3f9572b1ee5eb6ca497f81092133288&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. As we have all the data in one table we can select now **one specific student** (Alanna Elrick in this case).
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
INNER JOIN students s
	ON s.id = e.student_id
WHERE
	s.first_name = "Alanna"
AND
	s.last_name = "Elrick"
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1966400c-2622-49f8-a0af-a4452434e8b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VTIFFVR%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDMS9JVGjQvQHAweKKbXNGqY1rRfdVQqlgKjw6FWPyW4wIgQlQ3I8gP65jikCtU8rYaehFD2qk8vaf4JgCPKoJ0prQq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFJ2nTjZwQjgqh%2FMjircA%2BzQ7j5GRupC%2F2GIQIksLxR6%2FDh7zMLsI70gf%2Bf%2Bp4ORQZIl9ABhlMNCe4pg4zL05%2FwZ1peqwefBQZ38ejmxaDtlpY%2F1%2BP9p6tsl9XPRULi7W2lP97fGGfU6enxWxrhDF8GR03NZ%2BxVY8f3OHEkRPZKfoNXGqQfGpQUbGqXNuTYjUB%2FYkKJG94Y%2B%2Ft0K3Y%2BS7aubZnFeEpImO%2FH64ngfrfVB4P7qSUx6ZuriieSJowDiag829zehKMvf6P5QQnhgMFfj8lCONdcNxkStHMv82Pw1WTycw1xMCOrlHptqK1HIT9PiC6HavoUTS2daFnIbivp0mnfIoG4rq1DNaQc9EmtFqdDNiVNfnRnilaPxrEb85pw0yXUuo%2Fg594wq2oX%2Ft%2F%2Bb%2FUaXXYGyaDN2si2m2ImTMGGAVdeawRO3T74jxlGT%2BHMcG9hCeKXE1u3EWBIkxFKQo9p4kdPEuhdcS1nrdBP%2F0XalMUNfmZ5oAI1MuVlOs0nZnv7Ew9U%2FlYzE%2FHZThZVMZX%2BEhtT8b%2BT78P982A6%2FzuqfdaN5gD1Z7sOVbAyFVuBd14iEtIaHmui3mb2tH4alszEP5T7wnL%2F1JoVcX1a4NN%2Bd3BIzUMxT%2FGj9aSulMVxASD4t6gTdc0yrMIPO98kGOqUBMlAcYK1jO1XNbHAr23jdHDouTTP3w0plDIRH%2BxdAmU2VRhyvz%2Fbr5SpbaW2JgHwSuQOaZLYb5Oy8NZiLdUAIaUE0cGbd8Oty0at8UnD%2BaLX2temrrexB6feuCxD%2B30I9mDKy8OCJRB7PVmZ0A2qWleBxQyMAAXuHS8I2oXqUtjjlInctaMWNTDEJJjSQFs4IhOc5ilAIvwhaYL4HOe9JZvGKcXM1&X-Amz-Signature=5109d4821d568cd21177fec2a57e40343d1f5c5042ccba9969aa2e4d42eb4eb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. As we have now all the grades and course categories of Alanna Elrick together, we can now **group by course category**, compute the average and select the relevant columns.
```sql
SELECT category, AVG(grade)
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
INNER JOIN students s
	ON s.id= e.student_id
WHERE
	s.first_name = "Alanna"
AND
	s.last_name = "Elrick"
GROUP BY category
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4508adda-64be-46b5-af4e-75e75a13807d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677ZJS5MB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAh%2FQ40q2zp4jiI0OEQcR5DAh9kB93hlf%2Bq4V3%2BQqH07AiEAtf%2BeR52rnyP5GX1PeiUhnl%2FzZ7%2BJqKsbI8mA2tkw1%2FAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFOxvCOnXaKQk9KduCrcA8CIPjkvaT5iZetEfiI%2FfiCOjjQ2CY%2FrpgK%2FBVoV8dHx7cpZbClPUXo121A7mKFpBZXzyMl1KtkHAPo3RS8Hc86CNaEXn8AYwRYQJjd9FagPaZcL3vq2BBM8ET66L%2F3rpHxtUoHfcA2LyO1TFxk1qs756ngQy5yJLolJBix%2FV88%2Fs8u5fi1EkuLzbvbf3RaEOZ6fFOubMIlVv29aFalTOkxHIJVTTrD8I%2Ff2w%2Bvpc4umhhT6gHEQ5b1Qh3uFRgNgTnm3ehkRd9C8qi7p6ipq7KPgFIdsytMwBBJrbWEgJnyIZ%2B%2BC5t2GVZckK8BlFjKEU%2FvjO%2FwMQYjpnYRX31dS%2B8j52vMNTkSGxsXnqPCzL6QK%2F67Kl6mDgsfDDnmIh5THTld63VJu%2BmUw87fSuys0BbisSFLVST4fUGuExUoYp9bbgsro%2FqLou9a8BpD4%2BjmeFWqDBZFmSK6FKlMc8rqGO03LGzLi%2FYIzRV7QoOOM6r1GwDKzEaJ2qxS0jcKcsVx6iOU52x6s9mSCco5c%2F0zxiXJZM%2BXBOUUVMEPnBYIOxFCr0Qbuxol1C98zGhHpsHf7BLWRb2BUoHvhh%2BwahDRNQdbigkuz7Qsizla8XTD9cNoyZIdSOic4hPKuUDJIMOfN98kGOqUB9IhFgrJy1ycvAsTVNiD%2FAp9uNx55eN0cTV9KdU1bY0K2suR6AzcN0ur0h84eDx%2FiN1N1r2JfTJdluiF4xGHN1%2BRcHPpGkbM1zD%2Fxia3Wvqhf3a6BB8hLTXCJDUI%2B22z%2Fq0Bh%2FEZAjJ0TgL%2BvmdXAYaFrNxJAc4QfxeLcNLdn7FW3AMP6XsB8BB44Ed6vJ0fbXUeqJFl%2FLtsYVJwCra1AWl%2BPwc41&X-Amz-Signature=ac4771d62515a77f44c20e2b07f02be36ded27d4ce26463aef55b96d87a30b54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
---
## Question 2
Sie schreiben mit SQL genau **eine** syntaktisch korrekte und zu den Tabellenstrukturen passende SQL **UPDATE** Anfrage inkl. einer **WHERE** Bedingung.
Markieren Sie bitte **alle** korrekten Aussagen.
❌ Mit Hilfe der **WHERE** Bedingung lassen sich die zu aktualisierenden Tabellenspalten festlegen.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, kann mit genau einer solchen Anfrage auch gar kein Tupel (tuple) der entsprechenden Tabelle verändert werden.
❌ Die **WHERE** Bedingung kann nur im Zusammenhang mit **SELECT** Abfragen genutzt werden, nicht jedoch mit **UPDATE** Anfragen.
❌ Unabhängig vom Tabelleninhalt, wird mit genau einer solchen Anfrage immer genau ein Tupel (tuple) der entsprechenden Tabelle verändert.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, kann mit genau einer solchen Anfrage genau ein Tupel (tuple) der entsprechenden Tabelle verändert werden.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, können mit genau einer solchen Anfrage alle Tupel (tuple) der entsprechenden Tabelle verändert werden.

<details>
<summary>Explanation</summary>

Let's break down the provided SQL-related statements and understand why the correct answers are marked as they are.
❌ **Incorrect**, the `WHERE` clause in SQL is used to specify which rows (tuples) should be updated, not which columns (tabellenspalten). The columns to be updated are specified directly in the `UPDATE` statement.
- Example:
```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;

```
- Here, `column1` and `column2` are the columns being updated, and `condition` specifies which rows to update.
✅ **Correct**, if the `WHERE` condition does not match any rows in the table, then no rows will be updated.
- Example:
```sql
UPDATE employees
SET salary = 5000
WHERE employee_id = 9999;

```
- If there is no employee with `employee_id = 9999`, then no rows will be updated.
❌ **Incorrect**, the `WHERE` clause can be used with `UPDATE`, `DELETE`, and `SELECT` statements in SQL to specify conditions.
- Example:
```sql
UPDATE employees
SET salary = 5000
WHERE employee_id = 1;

```
- This updates the salary of the employee with `employee_id = 1`.
❌ **Incorrect**, the number of rows updated depends on the `WHERE` condition. It could update zero, one, or multiple rows.
- Example:
```sql
UPDATE employees
SET salary = 5000
WHERE department = 'Sales';

```
- This could update multiple rows if there are multiple employees in the 'Sales' department.
✅ **Correct**, if the `WHERE` condition matches exactly one row, then exactly one row will be updated.
- Example:
```sql
UPDATE employees
SET salary = 5000
WHERE employee_id = 1;

```
- If there is exactly one employee with `employee_id = 1`, then only that row will be updated.
❌ **Correct**, while it's possible to update all rows in a table, it depends on the `WHERE` condition. If the `WHERE` condition is omitted or matches all rows, then all rows will be updated.
- Example:
```sql
UPDATE employees
SET salary = 5000;

```
- This updates the salary for all employees because there is no `WHERE` condition.
</details>
---
## Question 3
Gegeben ist die folgende Tabelle **students**:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
Welche SQL-Abfrage liefert alle der gezeigten Tupel (tuple) der Tabelle, nicht jedoch potentiell weitere vorhandene Tupel, bei denen der last name nicht mit 'S' beginnt?
**SELECT** * **FROM** students **WHERE** last_name LIKE **‘S%’**

<details>
<summary>Explanation</summary>

> 💡 **[regular expressions](https://dataschool.com/how-to-teach-people-sql/how-regex-works-in-sql/), [SELECT](/9f266597386048dd9a967fd9fd8e4b89#f1c1f44f49aa4d76944c2d427c07c08f), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb)**
The question asks to write a query which retrieves all students with a last name that begins with letter **S**. 
As you can see from the table, all students have a last name that begins with letter **S**. Thus, the entire table as it is is returned, i.e., the `WHERE` condition does not filter out anything. 
Therefore, let’s assume we have the following data with some students that don’t have a last name beginning with letter **S**.
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | **Braun** | 1998-05-30 |
| 53450 | Julio Quinton | **Meier** | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | **Richard** | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
We can see that Preston, Julio and Lyman have last names that do not begin with **S**.
Thus, our expected output from the query should be the following:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
To figure out how the query gets to this table, let’s break it down into pieces:
```sql
SELECT * FROM student
```
returns all columns and records in the student table:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Braun | 1998-05-30 |
| 53450 | Julio Quinton | Meier | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Richard | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
To select Van and Dale only, we can extend the query now with a **WHERE** condition:
```sql
SELECT *
FROM
	student
WHERE
	last_name LIKE "S%**"**
```
returns all students with a last_name beginning with S:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
The **WHERE** condition goes into the column `last_name` and checks for each record / student if the condition `LIKE "S%"`** **applies. 
The condition `LIKE "S%"`** **checks if the last name matches the pattern**  **`"S%"`**.**
Pattern `"S%"`** **means that the string, i.e., last name of a student, must start with a capital **S**.
</details>
---
📄 **[Quiz 10]** (subpage)
## Question 1
Gegeben sind die folgenden drei Boxplots.
Bitte klicken Sie in der Figure an die Stelle, an welcher der Median der petal length für Virginica dargestellt wird.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/461e7a15-add0-4599-bc2c-ab3062e85d3d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z7VZYMZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCWSUzcBYhjF%2B5Uv3YcaYtv%2BW1x9IcqSLqNLFVTTmsWogIhALg3o6uiETmoKd4i6j%2BwBNjeT%2F1SpKdaMqvnukAxHt1BKv8DCCcQABoMNjM3NDIzMTgzODA1IgxWMzVSYlq3bIkdTF4q3ANi5wIWNWNZcx877feFS%2Bm%2FkFX%2FW67FYaHofHvaJPve4jHvSUAFjr7cP%2Bzrhrehv%2BC%2F6uVJc3wVzvuWnFxCS91xz2gNsTyxrVG0pZuMa7d%2BJn4HhrDj2hxYqA0joyg3C8QURzNCcZt1ssJ9ckqk3sfbHGyQu0rASTbFK3XRRpw%2B6B2WSe3vLiR2zFj6c3HtRp5UeGxwzesMBkpWqTnV4pnykdjbhNXYydG6AznGmYRCFgieyXdwaqPO3fMRofQvfUF9ghU57fRlD9EBBMivRxmyS4O9G2XpCcYCy5AoLllxwukTNV9EaWhc%2Bb7%2FUFmf25T%2BaHPcJERS1z0l6Tp4N5CQUZURtwia88Q%2FgmigS%2BvClqYatCqWRTPXBhzwIAK972AM6gUYASBKzMUmXECCURzDEwkXyqbDhU6TddesMs3DLIwiTRjDj%2F%2FR8LYXJrvHT8QXBe%2FJOu8HE2saUNktyKINl%2B1Hp5txm87fD72CfmF9gaL7uYcP02aRdSfZBl1r1QAyloIL4qfDXt9POvQ6RfsCGMdfOXgHlca8gGQkF2RGQBZiQ5DtkHbwk3SDW2vU8XAbTWW1UPtfTy43ra%2F9cYYQJJ49yO19TMPnfiysNzPZLA11XncXOofAg0ZJvTDXzvfJBjqkASqcwLjwW6e%2FrHtrlrPNBOetd67bRVNPXuKc37vl656ag%2FGgWLrMecEd2VV4ZrqOoV8qc4GORPtdsfybfdUIKw6cSYIFJBWnEg4SDm5%2BsvQCl7lyCc8zgLD71UDsi0NQRo9US3W37587741QM2TzrFspjKx7p40dqBBvuBu44Ao09ZJw%2F7kzKXExuoi6XGcqPMBuw9Vi75Ki9NdcZ6HUCo1kioq2&X-Amz-Signature=ae91580b879ef79255e01157c137a082f0e2cde262b21d873c303f96300ef789&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

> 💡 **[Boxplot](/6ac6e358ebd649cbab8c4f731dfa5cc8#29b3bf078dde4d20ae32783413578357)**
As the chart below shows, the **horizontal line** in the box represents the Median.
![Elements of a boxlot](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9ca63491-9ce3-4d62-bae0-fdde85c85fec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GRQNQUX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFRJLv5Kz3dJp8BlmExZl%2B2MJXbcVLDzLHBhrKY7nxNeAiEAyaRVbyHeS1BJ6zx2hZEjneubEnk3RL%2F9cT0MKGdbCtwq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDHH7zw5ncjOFZ8WIACrcAy6Yc7fo0ONhbzIVkqaCllDfdFshpT442ynfvoTpFsGLwpv5OFaIlfpTIoKm%2Fx7ORO1N8oA3%2BHoNNFzayJnxgW40LP%2BgdiCcCDQB53txFHgLNYIzXEC0kGVFWpNaaKSgYY%2FtD59QuE9T94Rl145e%2FaRjSRBxBeR3XJ7tyT5tqTuZlFrl%2F69t0%2FYWUMlltH1KY03yZzyO2cYI3UjryH9z8LejTmVnSGxLk85nOmkgIK373o4a2PrNUU4OUxfKVSkVs2YHiQm%2BoR2ABFSMeV71AGO32D5vxnwy1O0dNEsrM7ibLvqvOZqWRmlAH99KYI5ZdmHWhSjrBhbTWpZAoRwoU43EyfoByXhICW8ohj9fbFkoAO6udGE9XWIZMxjrtX9fmJBiSA1U43GM%2F%2BfPJZgZ1q1aQZMT87PstD8GlCapWwnX2z0sOFsk%2FYYvZzo%2B%2FAwcisYrAnzULCfJAZZwT5f8ckb8KYeuIx6uW2Lsd%2FZW5Oi%2Bdszj7sKniqiJrqs%2BwQWp4jElwbUgVnjeljb5xT3aLsA1c3VvWIN%2BvDMAFC0td7cLUf5HNmnsvE%2FKkg34zMrMhrhGYE1Le9g73MANaHgXn1d9B5mFo8lgHth3TahIIj0M%2FaADAsFQa%2FHJVeUMMMXO98kGOqUBv03Zahp0vGWMP9FZ6ZAqYAi%2FT6aHmO79Z9e%2BLB8rVud0EjRHB%2BrcCMZ9jnCjXK5ae5NC07xxfeCXgsfOfUiihScdeoD%2BHugsBT%2FlKa3XZRpJ4R9mF9tAIB3N%2FXT%2BFKKlY8O7RtmgjI00pyAh4nsBB9pvgGKdAvACaMqmxP%2BLpjo9aaeDP9VKXJbX%2BtA6xQtgoXuyCTZs1jrGI4Fr0NAu1iZhhPdZ&X-Amz-Signature=48aaade22351b5f5e9df228755c87b2683873bfbf43a9f61331f9352ae420332&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
## Question 2
In Assignment 10 haben Sie mit dem fruits DataFrame gearbeitet. Die Zeilen-Label haben die Namen der Früchte enthalten, die Spalten-Label haben die Namen der Wochentage enthalten, und die Kombination (z.B. Zeile 1, Spalte 2) hat die Anzahl Verkäufe einer spezifischen Frucht an einem spezifischen Wochentag enthalten.
Sie möchten nun in einem einfachen Liniendiagramm (Lineplot) die durchschnittlichen Verkäufe (Durchschnitt aller Früchte, y-Achse) im Wochenverlauf (über die Wochentage, x-Achse) darstellen. Wie lautet die zugehörige Codezeile?

plt.plot(fruits**.columns**, fruits**.mean()**, ‘m:’, label='Durchschnitt")

<details>
<summary>Explanation</summary>

> 💡 **[plot()](/10c38918e9a84ef79c8040d2fba85e2e#c9af98cf80ba468aa1947825383ef41e), [.columns](/1867045b058343e1a66b677961515907#b56cca6739ca4649ab31ebab1ee61f83), [mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
The **fruits** DataFrame looks as follow:
![DataFrame fruits](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d57f73a4-7024-4ebd-93d2-bca3d6b7d248/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSZTJCEW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGhNIR0RKK4ZNqn2tg3T3s8bt3TfmfO8%2F2VtvcZUGhfYAiB2cAI5es3yKJXNtykdc7CedyWr0zjv2ffXR1WAxCmshyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM6WFA0b34DZzZoqolKtwDewDQ93yCodEuUGOdBGjcubMGmts9ljbJt0RkB0Nasd6i5Gh9z0U2KY92%2FVTcYPSKDbgKF%2F2HlGxbnRV3lqnbJBYDBKcPlGhRHHByu3eV2wGHCH0QzFKvL%2Fs6%2FU%2Ba%2BxQ707A9enwVBwyUOs7gs9L9n0xYyhcoEiNNKgE2Bo0PfqCgjDV92qEG9XLJ%2FfxiRfkwQD7ai5KukZavQhLLa8p2rK1jM8qgkab7fBmevXXxlYPQJqOk5n8qLKurCvXQvBhKZpS4wUiSETKE6SxQLRJBZX1zbTv5RDkV4l%2FBykX6hLCM4FwmJ3Wo0wNNZoQlw%2BnRYyZA30ouCd2jVqaPUlhDa7RsjRvr4PpYY%2FPwwyWpm%2FbX1T8Sys0N1c4o2iL4IkYtqH6A3Xu286qLM08aIVjIbT9mu9L3BRp1QyP39krxrxbtyfRTE6PJ0ckOP5Yi5m%2B2WOWSqFdH7%2FzZXBOAOCZ6ZSCdKBuv6KX99Ct5wn%2B0CJwGRzfB6ZdqvVKZtXPL7wGcYYSmDQ3UUnSmNtJ8K8TgRFdNzpcGgBek3nrmKr%2BQ1o70fGoW2tBG4CwN8Z23TcAJKH2AF7jWD46c01jxJwJdGFLg1qhWtVtLx6umuiOzllgVlpAxLqSqRYhO%2BNcw7833yQY6pgEsx2SMs1iRMBt5aQdp0WgQudBnV1%2Fl%2BeCrpCaEjEsn5hR4FeaDW17hTzAxTEJEO%2BYbZYl7KBTmHuUn8s8lzCQJf363h0Smr2swkw1eBkgsi72v06nPz9fJ2p5WxJasO9qBSRvQPAh%2B%2FAUuGbFFRY3IKSaAHo%2FN0RjgiDFaBHeVJs7fVHUDv1zA9Tfj4Y5kWQgXrHlOTIF0GN3GEYd2QfVIaniPs%2Ftf&X-Amz-Signature=afcb6f870f4f19d8f0bb902761fa22b9ac29cf6b29551b0e81ffc5884ffa48f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And the Lineplot that should be generated looks as follow:
![Lineplot showing average sales per weekday](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/844d157e-d8b9-4553-af0c-192d8b1f77ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSZTJCEW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGhNIR0RKK4ZNqn2tg3T3s8bt3TfmfO8%2F2VtvcZUGhfYAiB2cAI5es3yKJXNtykdc7CedyWr0zjv2ffXR1WAxCmshyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM6WFA0b34DZzZoqolKtwDewDQ93yCodEuUGOdBGjcubMGmts9ljbJt0RkB0Nasd6i5Gh9z0U2KY92%2FVTcYPSKDbgKF%2F2HlGxbnRV3lqnbJBYDBKcPlGhRHHByu3eV2wGHCH0QzFKvL%2Fs6%2FU%2Ba%2BxQ707A9enwVBwyUOs7gs9L9n0xYyhcoEiNNKgE2Bo0PfqCgjDV92qEG9XLJ%2FfxiRfkwQD7ai5KukZavQhLLa8p2rK1jM8qgkab7fBmevXXxlYPQJqOk5n8qLKurCvXQvBhKZpS4wUiSETKE6SxQLRJBZX1zbTv5RDkV4l%2FBykX6hLCM4FwmJ3Wo0wNNZoQlw%2BnRYyZA30ouCd2jVqaPUlhDa7RsjRvr4PpYY%2FPwwyWpm%2FbX1T8Sys0N1c4o2iL4IkYtqH6A3Xu286qLM08aIVjIbT9mu9L3BRp1QyP39krxrxbtyfRTE6PJ0ckOP5Yi5m%2B2WOWSqFdH7%2FzZXBOAOCZ6ZSCdKBuv6KX99Ct5wn%2B0CJwGRzfB6ZdqvVKZtXPL7wGcYYSmDQ3UUnSmNtJ8K8TgRFdNzpcGgBek3nrmKr%2BQ1o70fGoW2tBG4CwN8Z23TcAJKH2AF7jWD46c01jxJwJdGFLg1qhWtVtLx6umuiOzllgVlpAxLqSqRYhO%2BNcw7833yQY6pgEsx2SMs1iRMBt5aQdp0WgQudBnV1%2Fl%2BeCrpCaEjEsn5hR4FeaDW17hTzAxTEJEO%2BYbZYl7KBTmHuUn8s8lzCQJf363h0Smr2swkw1eBkgsi72v06nPz9fJ2p5WxJasO9qBSRvQPAh%2B%2FAUuGbFFRY3IKSaAHo%2FN0RjgiDFaBHeVJs7fVHUDv1zA9Tfj4Y5kWQgXrHlOTIF0GN3GEYd2QfVIaniPs%2Ftf&X-Amz-Signature=32cfbfefa632577dbe130280b1f077806151a0102e7b3e6bbaeb2b5c7c6c647e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the Lineplot show the average sales per weekday. 
How do we get to this plot? 
We know that the syntax of the **plot()** function looks as follow:
`<< axes >>.plot(<< x_data >>, << y_data >>, << format_string >>, << label >>)`
Thus, we always must ask ourselves which data do we want to show on the:
- **x-axis**
- weekdays
- where are the weekdays stored?
- in the columns of the DataFrame **fruits**
- How can we access the column names?
- `fruits.columns`
```python
Index(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
       'Sunday'],
dtype='object')
```
- **y-axis**
- average sales per weekday
- where are the sales per weekday stored?
- each column in the DataFrame **fruits** represents a weekday
- how can we compute the average per column?
- `fruits.mean()`
```python
Monday       12.000000
Tuesday       8.666667
Wednesday     7.000000
Thursday     13.333333
Friday       24.333333
Saturday     63.000000
Sunday       37.000000
dtype: float64
```

Therefore, `fruits.columns` is used as **first** parameter and `fruits.mean()` as **second** parameter.
The **third** parameter `'m:'` is a format string that tells Matplotlib **how to format** the line. It has the following syntax:
`[color][marker][line]`
Thus, in this example above, `m` is the color and stands for **magenta**. `:` is the line and stands for **dotted line** style. The marker is skipped. As a result, a **dotted magenta** line is shown in the plot. 
Finally, the **fourth** parameter `label` gives the dotted magenta line a **name** which is **shown in the legend** in the top-left of the plot.
</details>
---
## Question 3
Das Argument **sharey** beim Aufruf von z.B. **plt.subplots()** bedeutet, dass
❌ wenn es **True** gesetzt wird, nur einmal die y-Koordinaten übergeben werden müssen, da sich die Diagramme (*axes*) der subplots diese Koordinaten teilen.
❌ der hier zugewiesene Wert in allen Diagrammen (axes) der subplots dargestellt wird. Damit das aber funktioniert, braucht es auch noch ein **sharex**-Argument, sonst wäre der zugehörige x-Wert immer 0.
✅ wenn es **True** gesetzt wird, die y-Achsen (*axis*) der Diagramme (*axes*) der *subplots* gleich skaliert werden.
❌ wenn es **False** gesetzt wird, die y-Achsen (*axis*) der Diagramme (*axes*) der *subplots* weggelassen werden. Das ist bei qualitativen Vergleichen der Kurvenverläufe in den *subplots* nützlich.

<details>
<summary>Explanation</summary>

> 💡 **[subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d)**
❌ **Incorrect**. The y-coordinates must be given for each subplot. Otherwise Python does not know what to plot (e.g., how to draw the line or how high to make the bar). Also, `sharey` does **not** make the subplots **share the y-coordinates** but makes sure that the **y-axis** across the different subplots is **shared**.
For example, we can have multiple line charts in subplots and each subplot has **its own y-coordinates** (the plotted lines are different):
```python
fig, axs = plt.subplots(2, 2)

axs[0][0].plot([2, 4, 5, 7])
axs[0][1].plot([10, 6, 3, 4])
axs[1][1].plot([3, 8, 1, 7])
axs[1][0].plot([12, 5, 4, 6])
```
Thus, the **scale of the y-axis is different** for each subplot (e.g. top left goes from 2 to 7 and bottom left from 4 to 12):
![Subplots with different y-coordinates](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3b16e380-4f6d-4a51-9579-054fc1832c97/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOBB65IL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHaUCIL%2Bd3mXM64C2AffWCIViXauqvlW0tv%2BISAqnFOCAiBUFhHRZjDh56JKdhCbF2MXAnu7NXmeelnVmejz5HoIyCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMzLT%2FmEHx6ObfwXKyKtwD4nc1oi9KF2P9j7CQUESUGlB2Iy%2FMFALnR8iG9TmF4akHy5mIDxPJ5ziKipxtpNQHoOdqcS23%2BX%2Bz%2BQkDEjkGYgmuZE%2BFnJBIxkWb2XNyJZ1pMjPaI105X4uYF1rEM3devKpjn1FT7S36uUH1dC14SULlXMjgdCgI8N8vI42USpyeVXgcpZVpMm%2F1j8OW8xIBqxHEoMubonoGtqptf%2Bgp8BpUdMfgA8db40I2NfE%2FZJdHsTFqzbxXsZ2kc4mJnK424mJHNl5JFAXdXrHaesPbOemZoI98uYzLCRBtG6ZgkaxjuCxJQYSbsy%2FnjvKNLxQCEuoFzYlMxlWAvpvQ0KuwycdJbcxJ2HBLrOLoCp0MEnFYYAyc2VCXjNmwqqON8amFCbePsWq9XRh9OB80kv4U3mcdH5D5kluwJYmeyIH0q5R71U7zJA0%2F9tDsy5NTgVl0oeC4oy3M%2Bqteghxb2Z47k1cB2i9XwgN0NjYwpnF0gkiZA00uPevq8svaZtZP9CaxTF%2BL5SHYjPMO9RcueuyuvCgH7FTOPjIejDsPskF2BrvIlhRVxiO7KhkAw4UTFaR8Hn%2B1I5YLkWfS%2BAySbDWo5HEvHhKZEoLLj84lxFDEmJm4nLTf87c9mMZzh6ww4833yQY6pgG%2FyCY0p%2F5aIH3mD4%2F%2BxWoQNZbxTqqccQtm%2BhIXbEeR3A0crDoydy%2BcXGhsywkgMdKmv3KQgC3PAw12KFgo5bcsAkfe%2FlhSjTtU%2BaDx3%2FhG8YElwNdP1hmzxhxznxtMKtVNl2HJW5uqDR4EPVFfp1f7kM3EhA5Y6zp9GggKsbThgjTikhoOb6kb580QifW7Q64Lbb0IN64xAUnyF4Z%2BQJeDhk%2FQ6JAC&X-Amz-Signature=55efe88686c5867bdc0417a29691d9553ec5458213cacfeb63c1bae8717d44ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now when we add parameter `sharey=True` to the first command:
```python
fig, axs = plt.subplots(2, 2, sharey=True)
```
The y-axis will be shared across all subplots:
![Subplots with different y-coordinates but shared y-axis](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/223c7937-1818-41eb-9e48-3aee7bd3bebe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOBB65IL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHaUCIL%2Bd3mXM64C2AffWCIViXauqvlW0tv%2BISAqnFOCAiBUFhHRZjDh56JKdhCbF2MXAnu7NXmeelnVmejz5HoIyCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMzLT%2FmEHx6ObfwXKyKtwD4nc1oi9KF2P9j7CQUESUGlB2Iy%2FMFALnR8iG9TmF4akHy5mIDxPJ5ziKipxtpNQHoOdqcS23%2BX%2Bz%2BQkDEjkGYgmuZE%2BFnJBIxkWb2XNyJZ1pMjPaI105X4uYF1rEM3devKpjn1FT7S36uUH1dC14SULlXMjgdCgI8N8vI42USpyeVXgcpZVpMm%2F1j8OW8xIBqxHEoMubonoGtqptf%2Bgp8BpUdMfgA8db40I2NfE%2FZJdHsTFqzbxXsZ2kc4mJnK424mJHNl5JFAXdXrHaesPbOemZoI98uYzLCRBtG6ZgkaxjuCxJQYSbsy%2FnjvKNLxQCEuoFzYlMxlWAvpvQ0KuwycdJbcxJ2HBLrOLoCp0MEnFYYAyc2VCXjNmwqqON8amFCbePsWq9XRh9OB80kv4U3mcdH5D5kluwJYmeyIH0q5R71U7zJA0%2F9tDsy5NTgVl0oeC4oy3M%2Bqteghxb2Z47k1cB2i9XwgN0NjYwpnF0gkiZA00uPevq8svaZtZP9CaxTF%2BL5SHYjPMO9RcueuyuvCgH7FTOPjIejDsPskF2BrvIlhRVxiO7KhkAw4UTFaR8Hn%2B1I5YLkWfS%2BAySbDWo5HEvHhKZEoLLj84lxFDEmJm4nLTf87c9mMZzh6ww4833yQY6pgG%2FyCY0p%2F5aIH3mD4%2F%2BxWoQNZbxTqqccQtm%2BhIXbEeR3A0crDoydy%2BcXGhsywkgMdKmv3KQgC3PAw12KFgo5bcsAkfe%2FlhSjTtU%2BaDx3%2FhG8YElwNdP1hmzxhxznxtMKtVNl2HJW5uqDR4EPVFfp1f7kM3EhA5Y6zp9GggKsbThgjTikhoOb6kb580QifW7Q64Lbb0IN64xAUnyF4Z%2BQJeDhk%2FQ6JAC&X-Amz-Signature=34e1687c43341f42217636764afa188af76b2e43f5b29c222e07819804f1383f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. `sharey=True` does **not** make the subplots share the y-coordinates, i.e., the data that is shown. In the example above, each subplot is showing a **different** line.
Also, as we have seen above, it is possible to **share the y-axis** while **not sharing the x-axis**. There is no dependency between the two parameters.
✅ **Correct**. `sharey=True` makes the subplot **share the y-axis**. Therefore, the y-axis is scaled to a range that captures the **max-value** and the **min-value** across **all** subplots.
❌ Incorrect. As seen above, when doing `sharey=False` (or not providing a value for this parameter at all), the y-axis are **not discarded**, but each subplot will have **its own** y-axis.  
</details>
---
## Question 4
Der nachfolgende Python-Code soll ein Balkendiagramm mit folgenden Anforderungen erzeugen:
- Es soll Balkenpaare aus je einem blauen und einem roten Balkendargestellt werden.
- Die beiden Balken eines Balkenpaars sollen ohne Zwischenraum direkt nebeneinander dargestellt werden.
- Ein Balken darf einen anderen Balken nicht überdecken- auch nicht teilweise.
Um das zu erreichen, müssten noch die Breiten der Balken definiert werden. Welche Werte für **width_1** und **width_2** sind hierfür zulässig?
```python
data_y1 = # Bitte nehmen Sie an, dass hier eine Liste mit int-Werten definiert wird
data_y2 = # Bitte nehmen Sie an, dsas hier enie Liste mit int-Werten definiert wird
					# die Listen data_y1 und data_y2 erfüllen folgende Bedingung:
					# len(data_y1) == len(data_y2)

# Hier müssen noch die Balkenbreiten (width_1, width_2) definiert werden:

data_x1 = range(len(data_y1))
data_x2 = [x + width_1/2 + width_2/2 for x in data_x1]

plt.bar(data_x1, data_y1, width=width_1, color='blue')
plt.bar(data_x2, data_y2, width=width_2, color='red')
plt.show ()
```
Markieren Sie **alle** richtigen Antworten.
❌ Option 1
`width_1 = 0.6`
`width_2 = 0.6`
❌ Option 2
`width_1 = 1`
`width_2 = 1`
✅ Option 3
`width_1 = 0.3`
`width_2 = 0.3`
✅ Option 4
`width_1 = 0.1`
`width_2 = 0.1`
✅ Option 5
`width_1 = 0.5`
`width_2 = 0.4`
❌ Option 6
`width_1 = 0.1`
`width_2 = 1`

<details>
<summary>Explanation</summary>

> 💡 **[multiple barchart](/10c38918e9a84ef79c8040d2fba85e2e#4a56b6e5ec454ce4bda78bcd8133eb4b)**
Let’s assume that `data_y1` and `data_y2` contain both 5 numbers. Thus in total 10 bars should be displayed in the figure eventually. 
We know that the list `[0, 1, 2, 3, 4]` is stored in `data_x1`.
Thus, the bars from `data_y1` will be inserted at following positions.
![Positions on x-axis of `data_y1`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0e86d183-723f-43e8-8a93-b286b4064a26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BFPEVGV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDjQDfkfPn5nuJBqro9RmVNAQk2Py5K6VeTsEw74bRFxAiEAtPeu1hEuNwvau8eS2a2uiM1GbTTi7i8XmZKYAEkC80kq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDK46%2FjwQGPFHqPPb8SrcA%2BB423cIe97XOckUhdGtznoUuPvc8Ggb2M8vlVjxMZ4G4T%2B0pq%2BmRS8DMAErDGMaiHGhDFBExQQDDK66FSQFPPfpODEsyx1hhWyHu%2FqOQQc2MljFgFyhELGYf7varc%2F0b1F4MVx0TdZ7LF3NB0t3ABH%2BEtEmcxHt3ee91QN74Y553XGlgf8dyL69ezkTc5MHEJQtNkzh6In%2B%2Bt3AnVeV1mZd%2BGrMS1s1xYdTipO7F9ro5%2FiJQs6cnzg77tOmCT1KnBZk1xLISdqS9xk%2Blij6Ef5sml%2BX%2ByLAkK8b0huufIG1iduJY8po6SLOVHuZ1qC8WpL4tGNEc0HRUAldNhWDSN3bZFDGdtXekrcRVB9HvZ8dSaCFgaid4IXTnL2o0KBqYcP6JHhw%2BFDJBPJnQ%2Bj3J8IZSBDnLYR%2Bi3KRZASrowD3thXVfsKOabN2UFbXyQmU2%2BBuuT4jR1pWEKPYi%2BtS%2BmZyvXdiRdaZ1xjcZIQZ6mSWpMiucPTVu0udTZhD5%2B%2BupeSXMItoUNvXuFP%2B8ZNArnrvHHmJNlTw6XeMT5oM3Q7GzR8mp4Kx9O%2FwchAmUFpxzmwc4reuGEetQQAcLR2CZcjBxUFTPvbfKUjukk%2B80Pn1sLPsZ60CnHjWDyDNMIPO98kGOqUBJWU%2BosSlnStwC4VojK2Q7KGcMxGS5Q91HT98jNGsMi2jg3zt8cfjBXUSKfuiI2EQZhLk9MRctnZyr0bE3351E5KJ7V9fU8iKpUadle2uVJnvAl7KIqQzGfP5U3Wcs9xw00aHwE6wHpyC0KD%2FHOICV1N7pw6tkPGRQoVMDdzzPv63n7bVmm7TF6bykc8FUrZstuUvKwCT%2FmmC%2BTSGSX6TPi%2FChMIB&X-Amz-Signature=550ea90bd7907aeb4d0e5d90dc6ca8943070b3490f6563f2566ca35a6f149649&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The question is now how to choose the correct values for `width_1` and `width_2` so that the following two conditions are met:
1. **not overlap** of the next bar group (where to position the bars?) 
We know that the positions of the x-axis are calculated as **x + width_1/2 + width_2/2**
Considering only position **x1** (0) and position **x2** (1) we must find values for **width_1** and **width_2** that meet following condition:
$$
0 + width_1/2   + width_2/2 + width_2/2 <= 1 - width_1/2
$$
From where is the last term width_2/2 coming from?
0 + width_1/2   + width_2/2  is the `position` where the bar of `data_y2` will be placed. However, this bar itself also **has a width**, i.e., will **go to the right** to some extent. And for this fact the last term width_2/2  is accounting for. 
1. **no empty spac**e between two bars (how wide to make the bars?)
This means that the **second bar should begin where the first bar terminates**. We know that the first bar will have a width of width_1. And we know that the second bar begins at position 0 + width_1/2   + width_2/2.  Thus, we can formulate the following condition:
$$
0 + width_1/2 = 0 + width_1/2   + width_2/2 - width_2/2
$$
We have here width_1/2  as the **position on the x-axis** of a bar always represents the **middle of the bar**. Then half of the width goes to the left and half of the width to the right.
<u>*Note:*</u> If you have a closer look at the second condition, you will note that it will **always** be True. We can simply **remove** + width_2/2 - width_2/2  as this **cancels out** to 0. However, this is only in this exercise the case. It could be that the x positions of `data_y2` are **different** in another exercise and then we would need to update the formula.
Equipped with this knowledge we can now go through each possible answer and check if the conditions are met.
<details>
<summary>❌ **Incorrect**. The bars will overlap.</summary>

❌ <u>Condition 1</u> → the bars will overlap
0 + 0.6/2   + 0.6/2 + 0.6/2 <= 1 - 0.6/2
0.9 <= 0.7
False
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.6/2 = 0 + 0.6/2 + 0.6/2 - 0.6/2
0.3 = 0.3
True
![Output when using `width_1 = 0.6` and `width_2 = 0.6`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0a3532b8-7d9d-4d1d-91aa-479f5c2ed59c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBEP4DMP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCDm%2FTfVrYSZ%2F4LHllohDceCjKEiwAdoDKySeL6v0HUjwIgHtGiMWNW1e59OZkdNuJI9P%2FvGZQ8kJ8Vu73bztek6GIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDeWUreaQjMTFHZl2CrcA7oTwe1LM%2F9VNRHn33qSQ8T1gNOp2%2Bat6FskJiHxPY9GapR8MTFk1edGItdweus8JkBZlTQKW5ZP0vey42%2FlMLuXKMY991jKNx3wgyVyKNDrkRbGPPm6T9SQt4lgzBsPolYp333z83cIu%2BKtXzqyu3D1dEbU4CzSYKGvmouJTpuhz2fssuBRSYOJ7cxImfWB%2FOIg7xliuW1cBrRvFf5leQbL7SuR6YCDsQscwMyWGV0vPESmPg9Q1e9OYuZnqMiqgZvxebevWfwwB%2Bol9rz%2Bjr9Uqbg6PH6cZjVeVv5evRfAhaLwTUxUKGK0BZo%2BOizk5pCP3zBBkQLf%2Fe56MqYw6nOp%2Fo6lLb6ITdl7hht8X4zs7ZdK9ytrouuO0O4zXEkr4zvCUaJqJgSig7P1F633e6N2sh7GZ8nTZUxJy9AxZjLFe%2FRYBWsOe0dQFP2OiOoiEeD1Ad6A%2B%2FfL23DiEl38b5jyy97eXovH8zaY%2FJ1QSgMOJwWCxm7BND8OusFwBq4cQfND0bBRWJUA%2FviQhnAfjjC43c6r7sSpBwaZul5nNjDWpeiuVbNY%2FZYMpfqFrymASnj50Iw2LpaBiR9BKODYgscaGgRJ2ASCSDu7gWSRamW1FMrD9QA0Np%2BalYzQMPrN98kGOqUB2367gJsPDbxg2bwOIO1F%2FOEQBvEfilWKIoyPL1%2F%2FnY18lekWurfQdtbLHyfMEWXb03nK6aIIeq134irJV8xcNE7EYT00rblcUkmg2dPkb7wkvsb6Es4qafVAa3%2B6T3a5jtIkdqgVnVsLg6BvoP6PnGL2E%2FkskYm0x1gWUb13fp6JESca6mtwBmXJU8bvhABrH2ITdym%2BediEWhp5x3ZWYaSAA1ZN&X-Amz-Signature=a2ef0f7ef4c12f785068c8dd5cf8b53340adcda2def0e55abc468a8728bf4f3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
<details>
<summary>❌ **Incorrect**. The bars will overlap.</summary>

❌ <u>Condition 1</u> → the bars will overlap
0 + 1.0/2   + 1.0/2 + 1.0/2 <= 1 - 1.0/2
1.5 <= 0.5
False
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 1.0/2 = 0 + 1.0/2 + 1.0/2 - 1.0/2
0.5 = 0.5
True
![Output when using `width_1 = 1.0` and `width_2 = 1.0`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d1f8d14e-3260-4c15-841e-a8f5ad99de5f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675RFOHGW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCOxvfadQpV0oGta6NfvgcpsrxdS0OtOyPoXE1hlTYAGAIhAMRbv6ydlR6gSxdlCOcMFZGZs0mbDAQF3q3anRDHFBsPKv8DCCcQABoMNjM3NDIzMTgzODA1IgzzW%2BMhwpzKVCXwvLcq3AOZBccwOK2VnTtsyStvSj7aIpcEVZSJnk%2FAtqb%2FyQba0Fz7iv2RFLsyTdyBm%2BNqZS8y4Y%2BMCluO5o4JOs3y7310gRFz8iMWYujp1eHgCF8HenvWCCMEaHXlBwoZW7Xvi4LyLPvZRVKy%2FO5Xsm1mIXbnYSvut2W6p887iyiXLSJLNcK5SMkhKYvZ7Kn3adR%2BK9VPL%2BFSp8%2BsQ5zr0pep5l2Nc8L4BU4zzxx3q0%2FzxxcJ1%2BrjsD3n0a%2BIjAXijVylealf9PmMoYjEnOJ4WS2YwWYvozCF79C0WZ%2Bz%2B5J4P3p9yvE4no8Oh%2BH4PJSvRz6pI59cTrDgdId34eupFka3HeXnHcXIbzpnpcRaX8X1SPs%2F2lEM%2FP74%2FRW3ZXRzYOyAX1%2B4ZhkvlHxcuJx1aKSgtgYjkfXq1OirZTtAWunnFPRyP59IZ5zjBgeDDscWy0m7Xe1sGfp2E3leKCJynLx48PM%2BJXfDdn8RvzKdXi%2BJCJj6HzsTMiknb3rY5uImQ%2B7V6G5F3nMa3ZPo%2FPl1gkcq0kv4frmzTTrDOXU2rGhJRIiUQ9%2B95mP58KDR5NOYVm%2Bo0%2BxBoJt3mN%2BKRdEpRBFSw1PUnV99fAAFPw7ChhGLtB1j4d8W6w1Mey1I1T3WWTDizffJBjqkAbiFPXQGb6dnhlrmtxFnX2ldZhg6KHkWEgAUNhdgu6w%2B7P793u%2BZnZsUWDOKF203RIGQuSoHUrLBwNF7RoO9dB%2FyVgE3sSfB0JsFJP7sZRCSrOahbPbj5vJfq2DubbwNL7aODsNzgbymhsopf6dgqRoznknsBwPbddiQhqDTqpVkC7uwhB4YKvsZ5rNA5V2VRFkTx7fHnZouVjiJR%2FDLiUcjAqcI&X-Amz-Signature=dd3be426de22941c8e2600a2a4617abf65679a2896134497265f43635841efb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
<details>
<summary>✅ **Correct**. Both conditions are met.</summary>

✅ <u>Condition 1</u> → the bars will not overlap
0 + 0.3/2   + 0.3/2 + 0.3/2 <= 1 - 0.3/2
0.45 <= 0.85
True
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.3/2 = 0 + 0.3/2 + 0.3/2 - 0.3/2
0.15 = 0.15
True
![Output when using `width_1 = 0.3` and `width_2 = 0.3`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3d9aa130-4908-4a45-8f67-21824f1a2471/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSGWJAWB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCtos1IDaJWiVUQzSN0IBi1xeoZGs2Whk%2Bs%2FGXUrYUPyQIhAJ6rS4obozHa%2B16DCGWsqcXNnATZlkKNY45k%2FYDUhJgyKv8DCCcQABoMNjM3NDIzMTgzODA1IgyQoEA49%2FctBYa%2FMVIq3AOStOLYovgX9u00Vd76laeEPB%2F%2FUIZ%2B%2FNcj9t8jJNEedW9u%2Fd9dMdxAZsZ4SdtbeF2pKA%2BfnyrkpIEENONpTUwTJTzPLStA2ONmTjO0kkLfAdjel6adX4JhWbafgO5pcZxvdpF13fPFwg6AFNFJdwa7egNMffzksHgXYXUZz4sdQ5b69mk5mBuyftL2d2ubFQOVB6y%2BCLtkDRbBsMz3SKXBhG1h%2B3WQCMmNTnff4d2KTkFlYbXDkd9WY7bpXgSIm8jMMP9Dz6B0%2FO3gxmMTmcH8zACvrcz%2FblpwkZlMD9zFtiX8ZMG1wTlSzPsOjpo2YXZ1s5%2FvgBolKjcFhaI0P6jutkgNMKtCz85BXYU4cUgqy6nJoD%2FnqDgLC5FGq01VdHx%2B%2BmAjgWMzYGPc0R1Zc130EiGaeHOTcgZloHL0levTU6coEyvBApVDtBAFkmMi%2FCEhtdjWnDMqC8z5O0rZtuEoRdjq8Sg2%2FpO7%2FKHxOghM4OK5dFbA9%2FzmNzzMsxd3oTstm6LRnc3Hu0zWe6o966R0ucSFdfqOD4yW7RQDnO29zDUwqYaPy1AUwPHepASeYIxABxCEYULU3J2n1GjQpkcozQtDXNGFbcmuOMB54UFXOiORe73EaYfafY%2B%2BNTDBzvfJBjqkAQknoSKeCejPL9s21B0yOx8rgH6OCYuCcVkp740%2B8mZpvw5o097Hm0e%2ByJ16sF2mNKuDCMc93dJdPcTcgSlOT7gMn%2BGmTbdymGtuO79cFPcxDu6wi4JIrwgVLXwgxoc%2FbXkP1ZDsNpnRBnoVlaPK%2Fp7uEw6r3euyGNWy5IXs%2FuTrdQSAahgL70RacklmDmTtN46ELkZJxCcNTPfbqOEICVa0KSDx&X-Amz-Signature=b51ed8567daa16687f5066fa4d4f324c1a5a85199e8c3347a04524946879cfde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
<details>
<summary>✅ **Correct**. Both conditions are met.</summary>

✅ <u>Condition 1</u> → the bars will not overlap
0 + 0.1/2   + 0.1/2 + 0.1/2 <= 1 - 0.1/2
 0.15 <= 0.95
True
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.1/2 = 0 + 0.1/2 + 0.1/2 - 0.1/2
0.05 = 0.05
True
![Output when using `width_1 = 0.1` and `width_2 = 0.1`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b54fa942-f8ae-42a6-b581-af1c834b2598/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W3QC76M%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIHvm9%2FSsWpoCkeuqbEmhtRDZRFEm5F1ddqS01UmkLGkzAiEA866sk2bOtLpT7y0je9JmVYmnHjLNqwE%2FMY7yFb3SODUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDH%2B4Ay9Wh3szwILEFircA00R458xUj67A8oLSn%2B%2BLPgJWt0%2FHfc%2FAwvyi%2BAWTRWNrSqq2xzOrSSVmEUb1LObGetF6TnTbjH0fEZPTJDFsFejsOq4QbPxvPsWcmDuwaKzV0wtOPt0Umws3YFlfWxfs%2FKlvKEk2BoxCaRHSvvVAspgh7I8NDLrU5bAQBK5ZvuLvPEYOZfiBEgvUwwdlhk6PwnL3drMwr5qUJQpT7A7b4UclX7AJex6LnCQ9LBleQPBfuR6F9RrWutFZwpqkCP%2FIbZpyf%2Bivdk%2BFN0%2FlDv2LyiQFCyuAbO7eZOpXSNtRGG%2Bsfzhfy%2Fi5gxyicT2yiflDeD5xudN%2Fv6UwpX2EBb3yM3a57z%2ByPEgTMyAqG7NsZfks6oAW7veZVxtIxIWv46kc0yegdPgYqO3%2FcjAPjYBJrhkLeXJnZuFwDs8oa6H1M9g02Wg2DStNGCDed3GjaVu1gbrLMd0yTERmRUJoTy4IdzNtlbuWDniberIx05xqHOuDJSQ%2BWM8uJLlptaS%2BGeqQym0HJvivQv%2FrZnc2BcRzaak2R21KUINLDaL9o5%2F%2BexSjB4Bkfq1JaiCPMukg2YitJGBjitztIN%2BBe4uOSbFb5DkpRQdUWF4RKIhym4Df1ulOUXcSzL7jxIc428ZMPnN98kGOqUBnH%2BWv2uqhKRW4qZg9MHDVqORDv0ASpMz8JKCGKNv2FXEyFuLDQj0yJjawr4dG%2F0O0q8mLD7fGIT2JK89jbMKN5bWOt8AyauOys7oucW3q4tarO6eJd%2BhbhA7dPzzIKin%2BoHlkx0RoWhOVNj4lzwInGXTrxmwUVm7PFmg5GMfXD%2FuZqbg5JNDyj5Q16KgNOBYsv4bBPF4%2BmRFqfKyvxhegobYAi5u&X-Amz-Signature=3a529aea26a0d27a737651f7cc7da95cd57caf3209b270d70311a89b7714bf81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
<details>
<summary>✅ **Correct**. Both conditions are met.</summary>

✅ <u>Condition 1</u> → the bars will not overlap
0 + 0.5/2   + 0.4/2 + 0.4/2 <= 1 - 0.5/2
 0.65 <= 0.75
True
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.5/2 = 0 + 0.5/2 + 0.4/2 - 0.4/2
0.5 = 0.5
True
![Output when using `width_1 = 0.5` and `width_2 = 0.4`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c8e54f56-f26c-446d-947a-35788889e1d6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GRQNQUX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230826Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFRJLv5Kz3dJp8BlmExZl%2B2MJXbcVLDzLHBhrKY7nxNeAiEAyaRVbyHeS1BJ6zx2hZEjneubEnk3RL%2F9cT0MKGdbCtwq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDHH7zw5ncjOFZ8WIACrcAy6Yc7fo0ONhbzIVkqaCllDfdFshpT442ynfvoTpFsGLwpv5OFaIlfpTIoKm%2Fx7ORO1N8oA3%2BHoNNFzayJnxgW40LP%2BgdiCcCDQB53txFHgLNYIzXEC0kGVFWpNaaKSgYY%2FtD59QuE9T94Rl145e%2FaRjSRBxBeR3XJ7tyT5tqTuZlFrl%2F69t0%2FYWUMlltH1KY03yZzyO2cYI3UjryH9z8LejTmVnSGxLk85nOmkgIK373o4a2PrNUU4OUxfKVSkVs2YHiQm%2BoR2ABFSMeV71AGO32D5vxnwy1O0dNEsrM7ibLvqvOZqWRmlAH99KYI5ZdmHWhSjrBhbTWpZAoRwoU43EyfoByXhICW8ohj9fbFkoAO6udGE9XWIZMxjrtX9fmJBiSA1U43GM%2F%2BfPJZgZ1q1aQZMT87PstD8GlCapWwnX2z0sOFsk%2FYYvZzo%2B%2FAwcisYrAnzULCfJAZZwT5f8ckb8KYeuIx6uW2Lsd%2FZW5Oi%2Bdszj7sKniqiJrqs%2BwQWp4jElwbUgVnjeljb5xT3aLsA1c3VvWIN%2BvDMAFC0td7cLUf5HNmnsvE%2FKkg34zMrMhrhGYE1Le9g73MANaHgXn1d9B5mFo8lgHth3TahIIj0M%2FaADAsFQa%2FHJVeUMMMXO98kGOqUBv03Zahp0vGWMP9FZ6ZAqYAi%2FT6aHmO79Z9e%2BLB8rVud0EjRHB%2BrcCMZ9jnCjXK5ae5NC07xxfeCXgsfOfUiihScdeoD%2BHugsBT%2FlKa3XZRpJ4R9mF9tAIB3N%2FXT%2BFKKlY8O7RtmgjI00pyAh4nsBB9pvgGKdAvACaMqmxP%2BLpjo9aaeDP9VKXJbX%2BtA6xQtgoXuyCTZs1jrGI4Fr0NAu1iZhhPdZ&X-Amz-Signature=0c821a44f9088bf60664d810f85afb442dcb3bba9f63102da660e041bafb66e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
<details>
<summary>❌ **Incorrect**. The bars will overlap</summary>

❌ <u>Condition 1</u> → the bars will overlap
0 + 0.4/2   + 1.0/2 + 1.0/2 <= 1 - 0.4/2
1.3 <= 0.8
False
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.4/2 = 0 + 0.4/2 + 1.0/2 - 1.0/2
0.2 = 0.2
True
![Output when using `width_1 = 0.4` and `width_2 = 1.0`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3a9c70a3-e6e1-4800-b8e8-1bc30573319b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLMUVWNV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDfsYA7IbBncXiwdnpWU7EHcdpqjUrqS0PE2OVmwWG2zAIhAI2c3bDQ%2FGq%2Fra6R5sx50TKUhxCBQYDHjTA6evWh3eIrKv8DCCcQABoMNjM3NDIzMTgzODA1IgxSkEOdNhhyqbQSibEq3APrpU9l%2BvS4h4RBrA2V3z4f9FqfaGKxiHI5yKhi4PwwqA8AlsNWwjhu%2BxkaAr0pvg4CaphE07yXmKO2IZ4qF69Bfe%2BnZ1LG1SPnZcjMYiy3soPdA8FYrxBUQfixsLhNvTdx4wZKsXC5HFK7L7herpL4on9Ug0w1%2FD%2FHtYf3H9rfZ4egRCA7xecTKLiL4rer92KOndn2x0yfexqcPNQDuYBnnC%2B%2BsYPstKFGDfzeJzjku1RTAoIJUr80wZrG6qm2UifRg45GqkuCQsTAw9xFSM6cBC5x7BJY%2FYvPpNrPX70g0sT2a%2BbEXiOFpK%2FWHkX8UQzGSfjrAPzvqh6KzhIQzJ7nC8m4ahYe0FazouG14sdNMhLcWxGdJ%2BBrMVTF1azXS7SYy87fSp3Yw3ntcPjFFcH813F7n8hmXO45aKLkDe8P4LeayL%2Bit7bmXijKNkWMGy3LmuNX%2B50rnhhm8KU15JM5%2FvrF5RFWZ8XvYbGqxkFI1D7NxmNLSuHOSzix%2BikJhTW9v7QQzRSr4RFn5D3aAh0i6EALPgMHubVxJQgHMEzNXgVU2UPFr422AIFfiP22uiX2Xb8fYS2rUg724bi6f1L17sr0Amnm0cBcqUrg84eNebR5cAaCq%2B%2F1EUH%2BcTDHzvfJBjqkAdm%2FaT4WneS7KfMVrepKyuzB5ME3%2BKzp8jQ9edebEiyU%2B0%2BzPo0YLJOAmrHTXmf5XMMOx%2FrbbqRfqPs3WJ55%2F8ZI7YRllGsIMvojpjrqAR2o4uPfohrlhzVBNkCeSMSLGWcoMXIB%2B3MVk%2B3nXc9Abi3ls7ArtCZ0CYXHFcJJG3KwQOr%2BcSU2QWCJXnodJYFDECLY%2F2h4cHsMVrlJIwJ%2FanY8uTQu&X-Amz-Signature=daa89b19a0c257fc1de636b5e203eb33aac55ed103e9139ded47219418dd6eae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
</details>
---
## Question 5
Ordnen Sie die Funktionsaufrufe den Diagrammtypen zu:
| Diagrammtyp | Funktionsaufruf |
| --- | --- |
| Boxplot | sns.boxplot() |
| Streudiagramm/Scatterplot | plt.scatter() |
| Streudiagramm/Scatterplot mit Regressionsfunktion | sns.regplot() |
| Liniendiagramm/Lineplot | plt.plot() |
| Horizontales Balkendiagramm | plt.barh() |

<details>
<summary>Explanation</summary>

> 💡 **[boxplot()](/6ac6e358ebd649cbab8c4f731dfa5cc8#bd387c5aad634663b85b90e663417f85), [scatter()](/10c38918e9a84ef79c8040d2fba85e2e#8a2779f2348c459db050ee81519ebe28), [regplot()](/6ac6e358ebd649cbab8c4f731dfa5cc8#2cc0db7a99fb4b648afc870d00e8059d), [plot()](/10c38918e9a84ef79c8040d2fba85e2e#c9af98cf80ba468aa1947825383ef41e), [barh()](/10c38918e9a84ef79c8040d2fba85e2e#93afc91e1e5e4f1e93355554eb690c49)**
There is not much to explain here. Just remember which function call creates which plot. Also note, that for Boxplot and Regplot the [seaborn](/6ac6e358ebd649cbab8c4f731dfa5cc8) library is used and for the other ones the plain [Matplotlib](/10c38918e9a84ef79c8040d2fba85e2e) library.
</details>
---
## Question 6
Wie viele Diagramme (axes) werden von folgendem Ausdruck erzeugt?
**fig, axs = plt.subplots(28, 32)**
896

<details>
<summary>Explanation</summary>

> 💡 **[subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d)**
The syntax of the subplot() function is as follow:
`plt.subplots( << n_rows >>, << n_col >>)`
Thus, with the command above a grid with 28** rows** and **32 columns** is generated.
Hence, in the variable `axs` a **nested list** will be stored that contains 28 lists (rows) and each list contains 32 elements (plots per row). In the end there will be 28 * 32 = 896** **subplots.
</details>
---

---

