---
title: "Quiz 1"
notion_id: "8ecab16a-ae39-4f71-a44e-8af0374adb18"
notion_url: "https://www.notion.so/Quiz-1-8ecab16aae394f71a44e8af0374adb18"
exported_at: "2025-12-13T23:12:02.477877+00:00"
---

# Quiz 1

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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/70b23ec3-231e-4f47-9662-e005179ddbe6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VCDEXBD%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEIXkmFnes4Py0TgH9inPdZa5SNNFtv71mi4yqHSQKR4AiEArGI0JUVBYC%2F4cxB%2BDzXLETrKf2Vn9AvxbWBE6WtpJSQq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDN33BEO%2BJQO%2BMiOwLSrcA4VNBict3%2FvpAltRkUtt%2FVeuAryQVoy3y65Oirag3bZ%2FUEBJKITwscxIXOIQOeJmD2QfKlZ%2F8wfjtw%2BCwZde%2FXjfC7RXL9W6QzpdUih7Qn5XoedRLhUKZPL%2FWlXYfmSV%2BonjlWTQ19k6V30OfvMvBkOsQDL4zEWW1pqToaGG5ZRs4XcPH7tGFfH37IdsX6YV6ng%2F1SZG0F6aGdk7%2BXqFM%2Bff74kFqM6NpZoKbg7NXlkCF2C3X%2BfMG2uSSVlG2%2FBKKtwcYyuyAYP76QDNbQqy2fLHNLAHtc4CVnuEqOxoGbQU3hm2RQlpf1GhzetKeY1kvFPh3nfsClsahVXRH%2F%2BIVavk37HFSdw3AcAGBhl5UCBE03xD9xTdzdivWgMaxbDI5PPiSP50lOo9BtXd7048APhfHUbZypCr4Hojxlobs8z6sgrh0W83BCxiexHAGhe07n%2FB90P4A1YtVW2vAVdRjrnpfkwDPzFHqFMHBK%2FrJD7YVYtGAWNwwih%2F5qk%2B5cZr3ohtgaOv8yqpzF4YQHsKoz%2FxQxtPBk0ij2zCYdDlEWQmlGXTa4EebqpXKdEE33%2FRcqmq2%2B0akjERiBR42jTGzcUkwpsDrQ8%2FRIbAWiDmLnGFPI8oFcs9Ik%2BqEXSSMODN98kGOqUB0rlV4HdjT%2FKL3FRksPXtHdpLxHYVqpIs%2F7QQI4%2By7IoEfzWx4qgn%2FMstpOA4uV2LlQ0B9nhmoWasWmQ0xQZ4yEJICTyx5PmWTyGDoo90Zq0VXWwCBDFTsxdYaTZLKYNYmJSAmZAh5HcGrOa6JxzeJM43Ga2ei02ARKv33frFpfUi0YP5jdYS20%2BeG0LGSxPzMUDBYdQOW1vuxOgZeaFWZM41TsXr&X-Amz-Signature=e556e2804f0cd5fa7ce7f297be8293f76543a2d0cf4d2df1d2027c7815e0dc90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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



