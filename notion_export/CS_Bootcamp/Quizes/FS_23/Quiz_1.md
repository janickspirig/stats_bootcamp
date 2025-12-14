---
title: "Quiz 1"
notion_id: "5c9b3668-9828-4822-ae16-ca582348274b"
notion_url: "https://www.notion.so/Quiz-1-5c9b366898284822ae16ca582348274b"
exported_at: "2025-12-14T01:04:40.845563+00:00"
---

# Quiz 1

## Question 1
Welchen Datentyp hat das Ergebnis, wenn ein **int**-Wert durch einen anderen oder den gleichen int-Wert geteilt wird? Gehen Sie davon aus, dass der Teiler (Divisor) niemals 0 ist.
✅  **float**
❌  int
❌  Das hängt von beiden konkreten Werten ab.

<details>
<summary>Explanation</summary>

> 💡 **[Mathematical operations](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a)**
A division in Python always returns a value of datatype float. No matter whether there is any remainder or not.
```python
8 / 4
2.0

type(8 / 4)
<class 'float'>


9 / 5
1.8

type(9 / 5)
<class 'float'>
```
</details>
---
## Question 2
Gegeben ist der Python Modulo-Operator %. Welcher Wert ist nach der Ausführung in z gespeichert?
z = 455,16 % 8

**7,16**

<details>
<summary>Explanation</summary>

> 💡 **[Modulo operator](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c)**
The modulo operator looks for the next number that is dividable without remainder by another number and then returns the difference between those two numbers. 
What is our starting point?
455,16
Is 455,16 dividable by 8 without remainder?
No
What is the next number that is dividable by 8?
448
What is the difference between 455,16 and 448?
455,16 - 448 = **7,16**
</details>
---
## Question 3
Welchen Datentyp (data type) haben die Variablen x, y und z nach der Ausführung des Programms?
```python
x = str(22)
y = int(x)+12.0
z = int(x) / 3
z = int(z)
```

**int** → z
**str** → x
**float** → y

<details>
<summary>Explanation</summary>

> 💡 **[Type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb)**
Check the table below to see what is happening with each variable by executing the code snippet line-by-line.
|  |  | x | y | z |
| --- | --- | --- | --- | --- |
| 1 | `x = str(22)` | “22” |  |  |
| 2 | `y = int(x)+12.0` |  | 24.0 |  |
| 3 | `z = int(x) / 3` |  |  | 7.333333 |
| 4 | `z = int(z)` |  |  | 7 |
One thing to not is that in line 1 the integer 22 is converted to a string and then saved in variable `x`. However, in all subsequent calculations we are doing with `x`, the value is first converted back to an integer using `int()`, before any calculation is made.
Also, we can use `int()` to convert a float into an integer. Python removes the digits after the point, i.e., rounds the decimal to a whole number automatically.
</details>
---
## Question 4
Gegeben ist das folgende Programm zur Berechnung des Volumens einer Pyramide:
```python
b = 3.0
h = 2.0

volume = (1/3) * b ** 2 * h

print("Das Volumen ist", volume)
```

Mark all correct statements regarding this snippet.
✅ Das Programm könnte auch ausgeführt werden, wenn **b** und **h** *int*-Werte enthielten, die in *float*-Werte umwandelbar sind.
❌ Das Programm könnte auch ausgeführt werden, wenn **b** und **h** *str*-Werte enthielten, die in int-Werte umwandelbar sind.
✅ Die Berechnung ist korrekt.
❌ Das Programm stellt sicher, dass **b** und **h** gültige Werte beinhalten.

<details>
<summary>Explanation</summary>

✅ **Correct**, any integer value can be transformed into a float value.
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
✅ **Correct**, python codes implements the [according formula](https://www.omnicalculator.com/math/pyramid-volume)
❌ **Incorrect**, we can assign any values to the two variables `b` and `h`. There is no check that prevents python from executing the calculation with values in the wrong format.
</details>
---
## Question 5
Was passiert bei der Ausführung des folgenden Programms?
```python
x = 5

while x <= 7:
	print("Yellow")
	x = x + 1
	print("Black")
print("Yellow")
```
❌ *Yellow* wird unendlich oft ausgegeben, d.h. dass die **while**-Schleife nie abbricht.
❌ *Yellow* wird 1x weniger als *Black* ausgegeben.
❌ Man kann nicht genau sagen, wie oft *Yellow* ausgegeben wird.
❌ *Black* wird in jeder Iteration der **while**-Schleife ausgegeben, darum kann man nicht sagen, woe oft genau *Black* ausgegeben wird.
✅ *Yellow* wird 4x oder weniger oft ausgegeben.
✅ *Black* wird genau 3x ausgegeben.
❌ *Yellow* wird genau 1x ausgegeben.
❌ Das Programm hat einen *SyntaxError*.
❌ *Yellow* wird niemals ausgegeben.
❌ Die Bedingung der **while**-Schleife wird nie *True*, d.h., ihr Inhalt (suite oder body) wird nie ausgeführt.

<details>
<summary>Explanation</summary>

> 💡 **[While loop](/5b0832dbf9454eb1941b7632e68a9abb#b52a89fc421f4692bdc9c73a764ca650)**
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
In conclusion, **Yellow** is printed four times and **Black** is printed three times. 
</details>
---
## Question 6
Markieren Sie alle Ausgaben, die das folgende Programm erzeugt.
```python
x = 10

if x > 20:
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
❌ a
❌ b
❌ c
✅ d
✅ e
❌ f

<details>
<summary>Explanation</summary>

> 💡 **[Logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)**
❌ **Incorrect**, 10 is not greater than 20. Thus, the if-statement evaluates to False.
❌ **Incorrect**, 10 is not greater than 15. Thus, the first elif-statement evaluates to False.
❌ **Incorrect**, 10 is not greater than 10. Thus, the second elif-statement evaluates to False.
✅ **Correct**, no if- or elif-statement evaluated to True. Thus the else statement is executed.
✅ **Correct**, 10 is smaller than 15. Thus, the if-statement evaluates to True.
❌ **Incorrect**, the if-statement evaluated to True. Thus, the else-statement is not executed.
</details>
---
## Question 7
Was gibt das folgende Programm aus?
```python
a = 'c'
b = 'x'
b = a + c

print(a + a + b+ 'x')
```
❌ ccccx
❌ cccc’x’
❌ x”x”xa
❌ c’c’x’x’c
❌ cxcxcx
✅ Nichts, weil es mit einem Fehler abbricht.

<details>
<summary>Explanation</summary>

If we execute this program we receive a [**NameError**](https://www.freecodecamp.org/news/nameerror-name-plot_cases_simple-is-not-defined-how-to-fix-this-python-error/),** **because variable `c` is not defined. 
```python
NameError: name 'c' is not defined
```
This means that Python does not know variable `c` because we haven’t initialized it anywhere. Python knows only two variables, `a` and `b`, as these variables were initialized int eh first two line of the program.
</details>
---
## Question 8
Welchen Wert haben die Variablen `x` und `z` nach der Ausführung des folgenden Programms?

```sql
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

❌ x = False, z = True
✅ x = True, z = True
❌ x = True, z = True
❌ Keine der anderen Antworten 
❌ x = 21, z = True
❌ x = False, z = False

<details>
<summary>Explanation</summary>

> 💡 **[Logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2) & [chaining boolean statements](/5b0832dbf9454eb1941b7632e68a9abb#b0c4461b3a544cad9e004f546fc637ee)**

`x = `**`42`**
`y = `**`True`**
`z = not y` → `not True` → **`False`**

`if y:` → **`True`**
`x = x / 2` → `42 / 2` → **`21`**
`y = not y` → `not True` → **`False`**
`else:`
*not executed as if-statement evaluated to True*

`if x < 42:` → `21 < 42` → **`True`**
`z = not y` → `not False` → **`True`**
`x = not z` → `not True` → **`False`**
`else: `
*not executed as if-statement evaluated to True*

`x` → **`False`**** **
`z` → **`True`**
</details>
---
## Question 9 
Das Bild zeigt die St.Galler Bahnhofsuhr. Diese stellt die Stunden (1. Zeile), Minuten (2. Zeile) und Sekunden (3. Zeile) kodiert im Binärsystem dar. Wie spät ist es im dargestellten Bild?
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8b2cf829-f347-4765-8bfd-4463f7e381fa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEI3VOEU%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQD7ciqzEs2KfJ4omE%2BhbkvgI9jhjROT%2BKw0NSrAI6US9wIhAKNSDKMR6oGOOm56fKPiTaiQAM4%2Fu2a6fU1dymzf1YsOKv8DCCoQABoMNjM3NDIzMTgzODA1IgxdYZ7DhALhR6TuqHoq3APSZoAfghW8Jh0qAORHOL7VGzD%2BSJT5BFLxBhHBaD9%2BZ5KGo%2B9k5MuMYX%2B%2FYbGculeFbJJJqCNHEjVqQuAtQOFZ11mKbUTtfDJJgDGHWMnz7y2NcXKWqWCAQQcCXKmZkz0vv91PASbMPP2IKs59f4H3wqfujzVFg5BbQX1EERHWl2ujb%2BRhc%2BFcvCIsOCyrx9gLTPiCUXQNDTNyZD2oH8TixKZmVp1JhjpfTDYYmvjhxFGkkTQnIFG9XPCT2z0yn1GlYNGHE5vKJS8vdTNkcsaBf4msDzmb2mamJV1AFQ%2BhTCKk%2FsBi7AZ9EzyMNyCjjH%2FL%2B9AZF9lfITQUX3%2BRCOnoMapZNDRawcaXxxxOnRHsZMKbSkKrC3OT%2FzBhNf9pkVujl%2BIhav18Ujn5b2cZxDNrv6%2BNH2oCKNPZXg%2BhnZY42xV8AtCzu8hZIUmULhG58DZq5QWr9%2FeFNzGRklePKx3Edn1VAJvzMQkfiL7UdGbV9l2K97dBrXyb0kpRTmyrvB1Mm6fn8lRpjxmlwH%2FGi1514D9DiEc8bVgYxflHCGwCI0ZahvHalp3ItqehE9jEtvclE1OFTE9zbSPrR6LPcgF3eq9F3wSJSE2frVxUTrGOUIb2i9sEkEtly1PxHzCllvjJBjqkAeC6tVvdcvbgOEz7tFMN2uLZo1hD0fAk3J1LqsJckggBw0n3d%2FXh4Yc6Uy0oNeaudWnyIl9iW4enNmHlcKlCGnFwROtZrXq4zNIqDoNhS2uczVsAMuNtm1d%2FSxAcccjopWCakkXZymLTgFLHgkZqAAPcfbbwm2o5oaLLoIi4SxdrtzsaT6J06vz0hc13UZ8T0sTsJXH93J4tAtoUocDN8uvxC55%2F&X-Amz-Signature=7291a39df78702e5875c7b84717c75ebd380cfd9c9ed69266978f32fa0fe56c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Die Uhrzeit ist:
**9** Stunden, 
**27** Minuten,
**34** Sekunden

<details>
<summary>Explanation</summary>

> 💡 **[Convert binary into decimal](/2b21ebb6314545d48382bb68713e5145)**
**Hours**
| Position | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- |
| Binary | 0 | 1 | 0 | 0 | 1 |
| Calculation | 0 * 2^4 = 0 | 1 * 2^3 = 8 | 0 * 2^2 = 0 | 0 * 2^1 = 0 | 1 * 2^0 = 1 |
| Decimal | 0 | 8 | 0 | 0 | 1 |
Sum of {8, 1} = **9**
---
**Minutes**
| Position | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 0 | 1 | 1 | 0 | 1 | 1 |
| Calculation | 0 * 2^5 = 0 | 1 * 2^4 = 16 | 1 * 2^3 = 8 | 0 * 2^2 = 0 | 1 * 2^1 = 2 | 1 * 2^0 = 1 |
| Decimal | 0 | 16 | 8 | 0 | 2 | 1 |
Sum of {16, 8, 2, 1} = **27**
---
**Seconds**
| Position | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 1 | 0 | 0 | 0 | 1 | 0 |
| Calculation | 1 * 2^5 = 32 | 0 * 2^4 = 0 | 0 * 2^3 = 0 | 0 * 2^2 = 0 | 1 * 2^1 = 2 | 0 * 2^0 = 0 |
| Decimal | 32 | 0 | 0 | 0 | 2 | 0 |
Sum of {32, 2} = **34**
</details>
---
## Question 10
Kann eine Variable vom Typ int mit dem “-” Operator von einer Variable vom Typ str subtrahiert werden?
❌ Ja.
❌ Es kommt auf den Inhalt der Variablen an.
✅ Nein.

<details>
<summary>Explanation</summary>

We cannot deduct one apple (integer) from an orange (string). If we try to do so, we get a [TypeError](/5b0832dbf9454eb1941b7632e68a9abb):
```python
"5" - 3

TypeError: unsupported operand type(s) for -: 'str' and 'int'
```
</details>
---
