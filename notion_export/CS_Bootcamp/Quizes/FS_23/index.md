---
title: "FS 23"
notion_id: "3d5be0b4-41af-48fe-ac6d-072b4d22641a"
notion_url: "https://www.notion.so/FS-23-3d5be0b441af48feac6d072b4d22641a"
exported_at: "2025-12-14T01:00:14.479334+00:00"
---

# FS 23

---
📄 **[Quiz 1]** (subpage)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8b2cf829-f347-4765-8bfd-4463f7e381fa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZWINX7H%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAmQOr9KQiTI6iueifRgj6S%2BCkaO8RsvolppY47NxLbgAiEArVQnVf%2BDqTdbfBxxmgzQkWEe6knBWE3wySdaqpRlRcAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFjAnLjw8dlMKSHk3ircAxPrTUjunqn%2B5bIdmkoctiiUzUb6rlZ0kG9u1Vr6gQnguUsYE8ulHS%2FLmG%2Fj5pcPoL0Ym4jebvg%2FS7Y4J%2BJCX1B3N%2B%2B9GpNjR%2B1LHa8J2dobkSF4X5pQANvJ%2BIX17OCAqeKp3I9B5VUUwj36%2FB5MHKfgX0DozfNLW1OR8AMBiTQ%2FsX76PuNMs4nBHcwAylEOLqNKLqvcjmIrTJifuYEbH0yb90wVMEu%2F%2Fv0TFaK6GXrP%2FGLoUoxRJPr9egZU4q28Grnc6I%2BToTJks0r952VvuIORLVyEsaj%2BkthmulXjviZvLyDlj%2F5Eza6hCqxgY%2Bdm4IQskY0PXIpxofxAXmBo7kbFM4WpQ6wlDIT7jf9M%2BiiXE%2BeRMsXqgvLV7hpCsDLYF3bWPxmpXtO3D64ZcuFeJZfefTqOscEwr4vuZ5p9oxQnDkRz2M%2BOiMX%2ByuoC8H5K2JXOeWy7nqq7zsbgxkhonVFDMjBS6QIlGOm5n%2FrmdNqQmCJKIOQlYnEsrGIzFzwOkOlYRpNWXRrwXYAo2ejh51%2FmaNuY9VPpzKl1SKnRJH3On6fDiUHf1GJaQRhhNvnTvIckOAzU9oZIxpIlM%2ByGIhawlxnjO%2B7nkNUR2OTGNFJt71fqXoBIMZR95kBpMI7O98kGOqUB87pw7sJ8gNgOlnD5SfyXMehPTnSjcyHCGrIKi2aI4bsPylBUaniIJh8cg0UY3MJ46PaVgV8yLhX6KV%2Bx%2FeRIR6Ir6S4wEunxqf9WOMw60J1NcxPKgLjmf5ikcyRp9n0oTFo5dZ49y4L5SUgiQp2dupIR3OtxnuquHN6IBB1xdp1sTo6K8n57SE%2BXyipN4A9bglrXrIq4%2FCoHkE7yIvEduLHQq%2BIe&X-Amz-Signature=b302010db28effcc18e658ffc3929317a7a9851d331c15b88a99812bf48c768e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
📄 **[Quiz 2]** (subpage)
## Question 1
Wie viele Schleifendurchläufe erzeugt der Funktionsaufruf
**range(3, 20, 3)**
wenn dieser in einer for-Schleife verwendet wird?
**6**

<details>
<summary>Explanation</summary>

> 💡 **[Range object](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385) in combination with [for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)**
The question asks how many times the an arbitrary for-loop, for example the one below, is executed if `range(3, 20, 3)` is used.
```sql
for i in range(3, 20, 3):
	print(f'this is loop run {i}')

'This is loop run 1'
'This is loop run 2'
'This is loop run 3'
'This is loop run 4'
'This is loop run 5'
'This is loop run 6'
```
We can see that the string is printed 6 times, thus there are 6 runs in total. To get to this answer we need to understand what `range(3, 20, 3)` does. 
`range(3, 20, 3)` has three arguments:
- `3` → first number to **include** in number range
- `20` → first number to **exclude** in number range
- `3` → step size, i.e., the first number and then only every third number
If we remove the step size we get:
`[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]`
Now with the step size of 3 we take only every third number
`[`**`3`**`, `~~`4, 5`~~`, `**`6`**`, `~~`7, 8`~~`, `**`9`**`, `~~`10, 11`~~`, `**`12`**`, `~~`13, 14`~~`, `**`15`**`, `~~`16, 17`~~`, `**`18`**`, `~~`19`~~`]`
And this gives us the following number range:
`[3, 6, 9, 12, 15, 18]`
And if we insert this in the for loop we get:
```sql
for i in [3, 6, 9, 12, 15, 18]:
	print(f'this is loop run {i}')
```
Variable `i` takes on the first value in the list (3), executes the code inside the loop and then moves on to the next element. Thus, as our list consists of six elements, the loop is executed six times.
</details>
---
## Question 2
Gegeben ist das folgende Programm.
```python
count = 0
while count < 10:
	print(str(count))
	if count >= 9:
		print(count)
	elif count == 9:
		print(count)
		print(count+1)
		count += 1
	else:
		count += 1
		print(count)
```

❌ Aufgrund der String-Verkettung (concatenation) kann nicht genau bestimmt werden, wie viele Zeilenausgegeben werden.
❌ Das Programm gibt insgesamt genau zehn Werte aus.
✅ Zwischen den ausgegebenen Zeilen gibt es keine Leerzeilen.
❌ Unter den vom Programm ausgegebenen Werten gibt es genau neun verschiedene Werte.
❌ Das Programm gibt den Wert 3 genau dreimal aus.
✅ Das Programm gibt den Wert 0 genau einmal aus.
✅ Die genaue Anzahl der ausgegebenen Zeilen kann nicht bestimmt werden.
✅ Das Programm gibt den Wert 2 genau zweimal aus.
✅ Das Programm kann ausgeführt werden.
❌ Das Programm gibt den Wert 1 genau einmal aus.
❌ Das Programm gibt den Wert 9 genau dreimal aus.

<details>
<summary>Explanation</summary>

> 💡 **[while-loop](/5b0832dbf9454eb1941b7632e68a9abb#b52a89fc421f4692bdc9c73a764ca650), [augmented assignment](/5b0832dbf9454eb1941b7632e68a9abb#30b886f101854a3ca81b231e9cda05a3)
Always try to **understand and execute the code first**, before looking at the statements!**
This is an example of an endless while-loop. A while-loop is endless when its condition (in this case `count < 10`) never evaluates to False, and thus Python will keep executing the code inside the loop until there is a memory issue or the user stops the execution.
Check the loop iterations below to understand why it is endless. 
<details>
<summary>1st run → in: `count = 0` | out: `count = 1`</summary>

`while count < 10:` → `0 < 10` → **`True`**
`print(str(count))` → `0`
`if count >= 9:` → `0 >= 9` → **`False`**
`elif count == 9:` → `0 == 9` → **`False`**
`else:`
`count += 1` → `count = 0 + 1` → **`1`**
`print(count)` → **`1`**
</details>
<details>
<summary>2nd run → in: `count = 1` | out: `count = 2`</summary>

`while count < 10:` → `1 < 10` → **`True`**
`print(str(count))` → `1`
`if count >= 9:` → `1 >= 9` → **`False`**
`elif count == 9:` → `1 == 9` → **`False`**
`else:`
`count += 1` → `count = 1 + 1` → **`2`**
`print(count)` → **`2`**
</details>
<details>
<summary>3rd run → in: `count = 2` | out: `count = 3`</summary>

`while count < 10:` → `2 < 10` → **`True`**
`print(str(count))` → `2`
`if count >= 9:` → `2 >= 9` → **`False`**
`elif count == 9:` → `2 == 9` → **`False`**
`else:`
`count += 1` → `count = 2 + 1` → **`3`**
`print(count)` → **`3`**
</details>
<details>
<summary>4th run → in: `count = 3` | out: `count = 4`</summary>

`while count < 10:` → `3 < 10` → **`True`**
`print(str(count))` → **`3`**
`if count >= 9:` → `3 >= 9` → **`False`**
`elif count == 9:` → `3 == 9` → **`False`**
`else:`
`count += 1` → `count = 3 + 1` → **`4`**
`print(count)` → **`4`**
</details>
<details>
<summary>5th run → in: `count = 4` | out: `count = 5`</summary>

`while count < 10:` → `4 < 10` → **`True`**
`print(str(count))` → **`4`**
`if count >= 9:` → `4 >= 9` → **`False`**
`elif count == 9:` → `4 == 9` → **`False`**
`else:`
`count += 1` → `count = 4 + 1` → **`5`**
`print(count)` → **`5`**
</details>
<details>
<summary>6th run → in: `count = 5` | out: `count = 6`</summary>

`while count < 10:` → `5 < 10` → **`True`**
`print(str(count))` → `5`
`if count >= 9:` → `5 >= 9` → **`False`**
`elif count == 9:` → `5 == 9` → **`False`**
`else:`
`count += 1` → `count = 5 + 1` → **`6`**
`print(count)` → **`6`**
</details>
<details>
<summary>7th run → in: `count = 6` | out: `count = 7`</summary>

`while count < 10:` → `6 < 10` → **`True`**
`print(str(count))` → **`6`**
`if count >= 9:` → `6 >= 9` → **`False`**
`elif count == 9:` → `6 == 9` → **`False`**
`else:`
`count += 1` → `count = 6 + 1` → **`7`**
`print(count)` → **`7`**
</details>
<details>
<summary>8th run → in: `count = 7` | out: `count = 8`</summary>

`while count < 10:` → `7 < 10` → **`True`**
`print(str(count))` → `7`
`if count >= 9:` → `7 >= 9` → **`False`**
`elif count == 9:` → `7 == 9` → **`False`**
`else:`
`count += 1` → `count = 7 + 1` → **`8`**
`print(count)` → **`8`**
</details>
<details>
<summary>9th run → in: `count = 8` | out: `count = 9`</summary>

`while count < 10:` → `8 < 10` → **`True`**
`print(str(count))` → `8`
`if count >= 9:` → `8 >= 9` → **`False`**
`elif count == 9:` → `8 == 9` → **`False`**
`else:`
`count += 1` → `count = 8 + 1` → **`9`**
`print(count)` → **`9`**
</details>
<details>
<summary>10th run → in: `count = 9` | out: `count = 9`</summary>

`while count < 10:` → `9 < 10` → **`True`**
`print(str(count))` → **`9`**
`if count >= 9:` → `9 >= 9` → **`True`**
`print(count)` → **`9`**
`elif count == 9:` 
*Ignored because if-statement evaluated to True*
`else:`
*Ignored because if-statement evaluated to True*
</details>
<details>
<summary>11th run → in: `count = 9` | out: `count = 9`</summary>

`while count < 10:` → `9 < 10` → **`True`**
`print(str(count))` → **`9`**
`if count >= 9:` → `9 >= 9` → **`True`**
`print(count)` → **`9`**
`elif count == 9:` 
*Ignored because if-statement evaluated to True*
`else:`
*Ignored because if-statement evaluated to True*
</details>
<details>
<summary>99999th run → in: `count = 9` | out: `count = 9`</summary>

`while count < 10:` → `9 < 10` → **`True`**
`print(str(count))` → **`9`**
`if count >= 9:` → `9 >= 9` → **`True`**
`print(count)` → **`9`**
`elif count == 9:` 
*Ignored because if-statement evaluated to True*
`else:`
*Ignored because if-statement evaluated to True*
</details>
<details>
<summary>… run → in: `count = 9` | out: `count = 9`</summary>

`while count < 10:` → `9 < 10` → **`True`**
`print(str(count))` → **`9`**
`if count >= 9:` → `9 >= 9` → **`True`**
`print(count)` → **`9`**
`elif count == 9:` 
*Ignored because if-statement evaluated to True*
`else:`
*Ignored because if-statement evaluated to True*
</details>

With this in mind we can answer the statements:
❌ **Incorrect**, we cannot determine the number of times the loop is executed because it is endless, not because we convert an integer to a string in line 3.
❌ **Incorrect**, the loop is endless and will thus return more than 10 values (we cannot determine an exact number).
✅ **Correct**, at no place in the code an empty line is printed.
❌ **Incorrect**, there are 10 different values that are printed: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
❌ **Incorrect**, value 3 is printed two times: one time in [3rd run](/86d6e1cae68842f4995bbd3841ef8b29) and one time in [4th run](/86d6e1cae68842f4995bbd3841ef8b29).
✅ **Correct**, value 0 is only printed in [1st run](/86d6e1cae68842f4995bbd3841ef8b29).
✅ **Correct**, it is an endless loop.
✅ **Correct**, value 2 is printed two times: one time in [2nd run](/86d6e1cae68842f4995bbd3841ef8b29) and one time in [3rd run](/86d6e1cae68842f4995bbd3841ef8b29).
✅ **Correct**, the program is syntactically correct and thus executable.
❌ **Incorrect**, value is printed two times: one time in [1st run](/86d6e1cae68842f4995bbd3841ef8b29) and one time in [2nd run](/86d6e1cae68842f4995bbd3841ef8b29).
❌ **Incorrect**, the loop gets stuck with value 9 and keeps  iterating, thus value 9 is printed an infinite number of times.
</details>
---
## Question 3
Die Funktion **digit_sum_square(number)** soll das *Quadrat* der *Digit Sum* ihres einzigen Arguments zurück geben. Die *Digit Sum* ist wie im Assignment die Summe der Ziffern einer Zahl.
Markieren sie alle Funktionsdefinitionen, die diese Anforderung erfüllen.
✅ Code snippet 1
```python
def digit_sum_square(number):
	ds = 0
	for num in str(number):
		ds = ds+int(num)
	return ds ** 2
```
❌ Code snippet 2
```python
def digit_sum_square(number):
	ds = 0
	for num in str(number):
		ds = ds+int(num)
	return (ds ** 2)
```
❌ Code snippet 3
```python
def digit_sum_square(number):
	for num in str(number):
		ds = ds + int(num)
	return (ds ** 2)
```
❌ Code snippet 4
```python
def digit_sum_square(number):
	ds = 0
	for num in range(number):
		ds = ds + num ** 2
	return ds
```
❌ Code snippet 5
```python
def digit_sum_square(number):
	ds = 0
	for num in str(number):
		ds = ds + int(num) ** 2
	return ds
```
❌ Code snippet 6
```python
def digit_sum_square(number):
	ds = 0
	i = 0
	while i < number:
		ds = ds + number
		i += 1
	return ds ** 2
```

<details>
<summary>Explanation</summary>

> 💡 **[functions](/5b0832dbf9454eb1941b7632e68a9abb#d98d10a03b3b4d17a846dfff610e9a5f), [for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [while-loop](/5b0832dbf9454eb1941b7632e68a9abb#b52a89fc421f4692bdc9c73a764ca650), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb), [math calculations](/5b0832dbf9454eb1941b7632e68a9abb#c5ed1b94ab75447ba1228022dbea677f), [augmented assignment](/5b0832dbf9454eb1941b7632e68a9abb#30b886f101854a3ca81b231e9cda05a3)**
the question asks for a code which takes an integer as argument, sums u the individual digits in the integers and then exponentiates this sum to the power of 2.
Let’s assume we give integer `123` as input into each code snippet. The digit sum of `123` is 6 and 6 to the power of 2 is **36**.
Thus, we are looking for the code snippet which returns the **integer** value 36.
<details>
<summary>✅ Code snippet 1 → **`36`**</summary>

`def digit_sum_square(123):` → **`36`**** **
`ds = 0`
`for num in str(123):`
<details>
<summary>1st run → `ds = 1`</summary>

`num = '1'`
`ds = ds + int('1')` → `0 + 1` → **`1`**
</details>
<details>
<summary>2nd run → `ds = 3`</summary>

`num = '2'`
`ds = ds + int('2')` → `1 + 2` → **`3`**
</details>
<details>
<summary>3rd run → `ds = 6`</summary>

`num = '3'`
`ds = ds + int('3')` → `1 + 3` → **`6`**
</details>
`return ds ** 2` → `6 ** 2` → **`36`**
</details>
<details>
<summary>❌ Code snippet 2 → **`(36)`**** **(returns a tuple that contains integer 36)</summary>

`def digit_sum_square(123):` → **`36`**
`ds = 0`
`for num in str(123):`
<details>
<summary>1st run → `ds = 1`</summary>

`num = '1'`
`ds = ds + int('1')` → `0 + 1` → **`1`**
</details>
<details>
<summary>2nd run → `ds = 3`</summary>

`num = '2'`
`ds = ds + int('2')` → `1 + 2` → **`3`**
</details>
<details>
<summary>3rd run → `ds = 6`</summary>

`num = '3'`
`ds = ds + int('3')` → `1 + 3` → **`6`**
</details>
`return (ds ** 2)` → `(6 ** 2)` → **`(36)`**
</details>
<details>
<summary>❌ Code snippet 3 → **`NameError`**</summary>

`def digit_sum_square(123):` → `NameError`
`for num in str(123):`
<details>
<summary>1st run → `NameError`</summary>

`num = '1'`
`ds = ds + int('1')` → `NameError: Name ds is not defined`
</details>
</details>
<details>
<summary>❌ Code snippet 4 → **`612745`**</summary>

`def digit_sum_square(123):` → **`612745`**
`ds = 0`
`for num in range(123):`
<details>
<summary>1st run → `ds = 0`</summary>

`num = 0`
`ds = ds + num ** 2` → `0 + 0` → **`0`**
</details>
<details>
<summary>2nd run → `ds = 1`</summary>

`num = 1`
`ds = ds + num ** 2` → `0 + 1` → **`1`**
</details>
<details>
<summary>3rd run → `ds = 5`</summary>

`num = 2`
`ds = ds + num ** 2` → `1 + 4` → **`5`**
</details>
<details>
<summary>4th run → `ds = 14`</summary>

`num = 3`
`ds = ds + num ** 2` → `5 + 9` → **`14`**
</details>
<details>
<summary>4th run → `ds = 30`</summary>

`num = 4`
`ds = ds + num ** 2` → `14 + 16` → **`30`**
</details>
<details>
<summary>5th run → `ds = 55`</summary>

`num = 5`
`ds = ds + num ** 2` → `30 + 25` → **`55`**
</details>
…
<details>
<summary>123rd run → `ds = 612745`</summary>

`num = 122`
`ds = ds + num ** 2` → `597861 + 14884` → **`612745`**
</details>
`return ds` → **`612745`**
</details>
<details>
<summary>❌ Code snippet 5 → **`14`**</summary>

`def digit_sum_square(123):` → `14`
`ds = 0`
`for num in str(123):`
<details>
<summary>1st run → `ds = 1`</summary>

`num = '1'`
`ds = ds + int('1') ** 2`   → `0 + 1 ** 2` → `0 + 1` → `1`
</details>
<details>
<summary>2nd run → `ds = 5`</summary>

`num = '2'`
`ds = ds + int('2') ** 2`   → `1 + 2 ** 2` → `1 + 4` → `5`
</details>
<details>
<summary>3rd run → `ds = 14`</summary>

`num = '3'`
`ds = ds + int('3') ** 2`   → `5 + 3 ** 2` → `5 + 9` → `14`
</details>
`return ds` → `14`
</details>
<details>
<summary>❌ Code snippet 6 → **`15129`**</summary>

`def digit_sum_square(123):` → `15129`
`ds = 0`
`i = 0`
<details>
<summary>1st run → `ds = 123`, `i = 1`</summary>

`while i < number:` → `0 < 123` → `True`
`ds = ds + number` → `ds = 0 + 123` → `123`
`i += 1` → `i = 0 + 1` → `1`
</details>
<details>
<summary>2nd run → `ds = 246`, `i = 1`</summary>

`while i < number:` → `1 < 123` → `True`
`ds = ds + number` → `ds = 123 + 123` → `246`
`i += 1` → `i = 1 + 1` → `2`
</details>
…
<details>
<summary>122nd run → `ds = 15129`, `i = 123`</summary>

`while i < number:` → `122 < 123` → `True`
`ds = ds + number` → `ds = 15006 + 123` → `15129`
`i += 1` → `i = 122 + 1` → `123`
</details>
<details>
<summary>123rd run → `ds = 15129`, `i = 123`</summary>

`while i < number:` → `123 < 123` → `False`
*Loop-body is not executed because while condition evaluated to False*
</details>
`return ds` → `15129`
</details>
</details>
---
## Question 4
Innerhalb einer Schleife(z.B. for-loop, while-loop) kann eine weitereSchleife ausgeführt werden. Allerdings muss die innere Schleife von der gleichen Art sein, d.h. zum Beispiel, wenn die äussere Schleife ein for-loop ist, muss auch die innere ein for-loop sein.
✅ False
❌ True

<details>
<summary>Explanation</summary>

> 💡 **[Nested loops](/5b0832dbf9454eb1941b7632e68a9abb#7cc1c66ebe7a4290927071b49aab1c29)**
This is False because we can also put a for-loop into a while-loop or a while-loop into a for-loop.
</details>
---
## Question 5
Gegeben in das folgende Programm. Nach dem der/die Benutzer/in einen korrekten Wert eingegeben hat, wurde das Programm, wenn möglich, vollständig ausgeführt.
```python
n = int(input("Geben Sie eine positive ganze Zahl ein: "))
s = 0

for i in range(1, n+1):
	s += i
```

Bitte füllen Sie in den nachfolgenden Aussagen die Lücken ein:
Die Summe der **ersten** **n** natürlichen Zahl ist: **s**
Die Variablen **i** und **n** haben nach der Ausführung den gleichen Wert und den gleichen **Datentyp**.

<details>
<summary>Explanation</summary>

> 💡 **[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [augmented assignment](/5b0832dbf9454eb1941b7632e68a9abb#30b886f101854a3ca81b231e9cda05a3)**
Let’s assume that the user provides the number 3 as an input, thus n = 3. We can now run the program:
`n = 3`
`s = 0`
`for i in range(1, 4):`
<details>
<summary>1st run → `s = 1`</summary>

`i = 1`
`s += i` → `s = 0 + 1` → `1`
</details>
<details>
<summary>2nd run → `s = 2`</summary>

`i = 2`
`s += i` → `s = 1 + 2` → `3`
</details>
<details>
<summary>3rd run → `s = 6`</summary>

`i = 3`
`s += i` → `s = 3 + 3` → `6`
</details>
We can see that after the loop execution `s` has the value **6**. And **6** is the sum of the first `n` (3 in this case) natural numbers (1 + 2 + 3 = 6).
Thus, the first sentence makes sense. Whatever value is provided for `n`, the program will return the sum of the first `n` numbers. 
Also, we can see that after the execution, the value **3** is stored in `i`, which is the same value that is stored in `n` (we provided this input → **3**). And both, `n` and `i` are of type integer. Thus, this statement makes sense as well.
</details>
---

📄 **[Quiz 3]** (subpage)
## Question 1
Gegeben ist die folgende Funktion:
```python
def sum_numbers(start=-1, end=3, step=1):
	return sum(range (start, end, step))
```
Markieren Sie alle korrekten Aussagen zu dieser Funktion.
✅ Der Rückgabewert ist 0 wenn die Funktion mit **sum_numbers(step=2) **aufgerufen wird.
✅ Die Funktion **sum_numbers** kann mit drei Argumenten aufgerufen werden.
❌ Die Funktion **sum_numbers** kann mit *beliebig* *vielen* Argumenten aufgerufen werden.
❌ Der Rückgabewert ist **2** wenn die Funktion mit **sum_numbers(1) **aufgerufen wird.
❌ *Die Funktionsdefinition ist fehlerhaft und erzeugt darum spätestens beim Funktionsaufruf einen Fehler.*
✅ Die Funktion **sum_numbers** kann *ohne Argument*, also als **sum_numbers()**, aufgerufen werden und wird dabei *fehlerfrei* ausgeführt.
❌ Der Rückgabewert ist **6** wenn die Funktion mit **sum_numbers(2, 2, 2)** aufgerufen wird.
✅ Die Funktion **sum_numbers** kann mit *zwei* Argumenten aufgerufen werden.
✅ Der Rückgabewert ist **2** wenn die Funktion mit **sum numbers(2) **aufgerufen wird.
✅ Die Funktion **sum_numbers** kann mit *einem* Argument aufgerufen werden.
❌ Der Rückgabewert ist **3** wenn die Funktion mit **sum_numbers() **aufgerufen wird.
❌ Die Funktion **sum_numbers** gibt immer die Summe aller ganzen Zahlen zwischen den Parameterwerten **start** (inklusive) und **end** (exklusive) zurück.

<details>
<summary>Explanation</summary>

> 💡 **[range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385), [functions with default / optional parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc)**
✅ **Correct**, the following values will be assigned to the parameters:
`start = -1`
`end = 3`
`step = 2`
Thus, the following range object is created
`range(-1, 3, 2)`
If we convert the range object to a list we can look into the range
`list(range(-1, 3, 2)` → `[-1, 1]`
**-1** is the first number to include
**3** is the first number to exclude
**2** is the step-size, thus number **0** and **2** are ignored
`sum([-1, 1])` yields `-1 + 1` which is equal to **0**
✅ **Correct**, in the function headers we have three parameters specified: **start**, **end**, **step**
❌ **Incorrect**, for example we cannot call the function with 4 arguments as this yields an error
`sum_numbers(-1, 3, 2, 4)`
`TypeError: sum_numbers() takes from 0 to 3 positional arguments but 4 were given`
❌ **Incorrect**, result is **3.** If we only provide one number as argument (**1** in this case), then this number is assigned to the first parameter `start` and for `end` and `step` the default values are used
`start = 1`
`end = 3`
`step = 1`
Thus, the following range object is created
`range(1, 3, 1)`
If we convert the range object to a list we can look into the range
`list(range(1, 3, 1)` → `[1, 2]`
**1** is the first number to include
**3** is the first number to exclude
**1** is the step-size, thus no number is ignored, we keep both (**1** and **2**)
`sum([1, 2])` yields `1 + 2` which is equal to **3**
❌ **Incorrect**, from the previous answers we have seen that the function is correctly implemented.
✅ **Correct**, if we don’t provide any argument in the function call, then the default values are assigned to the variables: `start = -1`, `end = 3`, `step = 1`
❌ **Incorrect**, result is **0**. In this case values were provided for all three parameters. Thus, the default values are overwritten:
`start = 2`
`end = 2`
`step = 2`
Thus, the following range object is created
`range(2, 2, 2)`
If we convert the range object to a list we can look into the range
`list(range(2, 2, 2)` → `[]`
**2** is the first number to include
**2** is the first number to exclude
**2** is the step-size
Python returns an empty list because 2 is the first number to include and to exclude. So there is actually nothing to include as there is no natural number between 2 and 2.
`sum([])` yields **0**
✅ **Correct**, if two arguments are provided in the function call, e.g. `sum_numbers(1, 5)`, then the number 1 is assigned to `start` and number 5 to `end`. and for step the default value `1` is used.
✅ **Correct**, if we only provide one number as argument (**2** in this case), then this number is assigned to the first parameter `start` and for `end` and `step` the default values are used
`start = 2`
`end = 3`
`step = 1`
Thus, the following range object is created
`range(2, 3, 1)`
If we convert the range object to a list we can look into the range
`list(range(2, 3, 1)` → `[2]`
**2** is the first number to include
**3** is the first number to exclude
**1** is the step-size, thus no number is ignored, we keep the **2**
`sum([2])` yields **2**
✅ **Correct**, if we provide one argument in the function call, then this value is assigned to the `start` parameter and for the `end` and `step` parameters the default values are used.
❌ **Incorrect**, result is **2. If** we don’t provide any argument in the function call, then the default values are used:
`start = -1`
`end = 3`
`step = 1`
Thus, the following range object is created
`range(-1, 3, 1)`
If we convert the range object to a list we can look into the range
`list(range(-1, 3, 1)` → `[-1, 0, 1, 2]`
**-1** is the first number to include
**3** is the first number to exclude
**1** is the step-size, thus no number is ignored and we keep all of them
`sum([-1, 0, 1, 2])` yields **2**
❌ **Incorrect**, if we provide an argument for `step` that is different than **1, **then some numbers are ‘over-jumped’ and excluded from the range and the result is no longer the sum of *all* numbers between `start` and `end`.
</details>
---
## Question 2
Wir wissen, dass Tupel (*tuple*) unveränderbar (*immutable*) sind. Trotzdem wird das folgende Programm fehlerfrei ausgeführt. Hierbei werden zuerst zwei Tupel *(tpl1, tpl2)* erzeugt und dann wird *tpl2* an *tpl1* angehängt. *tpl1* ist also nach der Ausführung der dritten Zeile länger als nach der ersten Zeile.
```python
tpl1 = (1, 2, 3, 'name', 'vorname')
tpl2 = ('alter',)
tpl1 += tpl2
```
Warum ist es möglich, wenn Tupel unveränderbar (*immutable*) sind?
❌ Man kann nicht genau sagen was passiert; es hängt stark von der Grösse und Belegung des Arbeitsspeichers des ausführenden Rechners ab. Darum ist auch die Ausführung auf Google-Colab unberechenbar.
✅ Das Tuple, auf welches tpl1 nach Zeile 1 verwiesen hat, wurde gar nicht verändert. Stattdessen wurde in Zeile 3 ein neues Tupel-Objekt erzeugt und tpl1 zugewiesen.
❌ Die beiden Tupel sind nicht immutable aber es tritt trotzdem kein Fehler auf. Der Fehler würde erst auftreten, wenn auf tpl1 wieder zugegriffen würde.
❌ Die Aussage ist falsch. Das Programm kann nicht fehlerfrei ausgeführt werden.
❌ Es handelt sich gar nicht um Tupel. tpl1 und tpl2 sind eigentlich Listen und Listen sind veränderbar (mutable).

<details>
<summary>Explanation</summary>

> 💡 **[Tuple](/5b0832dbf9454eb1941b7632e68a9abb#f8cb18a835dd45c1aed5abca3279ba9c)**
❌ **Incorrect**, in computer science everything is based on logic. I.e., there are no random things happening, unless we want do code some random behavior purposely. 🙂
✅ **Correct**, if we print the output of `tpl1` before and after the modification we can re-produce what was happening: 
```sql
tpl1 = (1, 2, 3, 'name', 'vorname')
print(tpl1)

tpl2 = ('alter',)
print(tpl2)

tpl1 += tpl2
print(tpl1)

(1, 2, 3, 'name', 'vorname')
('alter',)
(1, 2, 3, 'name', 'vorname', 'alter')
```
We can see that that the value stored in `tpl1` got updated and not the existing tuple modified. This happened in the last code line:
`tpl1 += tpl2`
This can be written as
`tpl1 = tpl1 + tpl2`
Python executed the right part of the equal sign first:
`tpl1 + tpl2` → creates a new tuple `(1, 2, 3, 'name', 'vorname', 'alter')`
Now Python takes this new tuple and overwrites the tuple `(1, 2, 3, 'name', 'vorname')` that is stored in `tpl1`. 
`tpl1 = (1, 2, 3, 'name', 'vorname', 'alter')`
In conclusion no tuple is modified, but a new one is created and the value in variable `tpl1` is overwritten.
❌ **Incorrect**, tuples are always immutable.
❌ **Incorrect**, the program works just fine.
❌ **Incorrect**, both are tuples. Tuples have round brackets `()`, lists have square brackets `[]`.
</details>
---
## Question 3
Gegeben ist das folgende Programm:
```python
a=(1, 2,[3, 4], 5)
a[2][0] = 4
b = a[0:3]
```
Was ist der Wert der Variable b nach der Ausführung_
✅ (1,2,[4,4])
❌ tuple
❌ (1, 2)
❌ Es tritt ein Fehler auf.
❌ *Kann nicht sicher bestimmt werden.*
❌ E*in anderer, hier nicht aufgeführter Wert.*
❌ 3
❌ list
❌ [3, 4]
❌ (1, 2, 3, 4)

<details>
<summary>Explanation</summary>

> 💡 **[Tuple](/5b0832dbf9454eb1941b7632e68a9abb#f8cb18a835dd45c1aed5abca3279ba9c), [nested lists](/5b0832dbf9454eb1941b7632e68a9abb#8526be0c72d1432c83067d8315535bd0), [slicing](/5b0832dbf9454eb1941b7632e68a9abb#7c55714b07c5452ead0bb88983c7abcc)**
To get to the answer `(1,2,[4,4])`, let’s execute the code line-by-line.
`a = (1, 2,[3, 4], 5)`
`a[2][0] = 4`
`a[2]` → `[3, 4]`
`a[2][0]` → **3** → number **3** is being replaced with **4**
Why can we overwrite the number 3, is it not a tuple?
Yes, `a` is a **tuple**. However the tuple consists of a list. And a list is **mutable**, which means that we can overwrite the elements inside this list. If we were to overwrite the first element in the tuple, `a[0] = 5`, this would result in a [`TypeError`](/dfa7a8137dff402f9bcded5d8a28adda).
`b = a[0:3]` → `(1, 2,[4,4])`
**0** → first index position to include
**3** → first index position to exclude
**{0, 1, 2}** → all index positions to include in slice
`a[0]` → 1
`a[1]` → 2
`a[2]` → [4, 4]
</details>
---
## Question 4
Gegeben ist folgendes Programm. Es wurde ausgeführt:
```python
import random

def fizz(buzz):
	result = []
	
	for i in range(buzz):
		if (i % 3 == 0) and (i % 5 == 0):
			result.append(random.randrange(1,7))
		elif i % 3 == 0:
			result = result[:len(result)-1]
		elif i % 5 == 0:
			continue
		else:
			result.append(i)
		
	return len(result)
```
Markieren Sie **alle** korrekten Aussagen zu diesem Programm. 
❌ Der genaue Rückgabewert von **fizz(0)** kann nicht genau bestimmt werden.
✅ Der Rückgabewert ist **2 **wenn die Funktion fizz mit **fizz(4)** aufgerufen wird.
✅ Der Rückgabewert ist **1** wenn die Funktion fizz mit **fizz(1)** aufgerufen wird.
✅ Der Rückgabewert ist **3** wenn die Funktion fizz mit **fizz(3)** aufgerufen wird.
❌ *Keine der anderen Aussagen ist korrekt.*

<details>
<summary>Explanation</summary>

> 💡 **[functions](/5b0832dbf9454eb1941b7632e68a9abb#d98d10a03b3b4d17a846dfff610e9a5f), [logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2), [modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c), [slicing](/5b0832dbf9454eb1941b7632e68a9abb#5d06cfcdb5574513a592b854a821fe3e), [range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385), [for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [random number](/5b0832dbf9454eb1941b7632e68a9abb#ed2397e7feb14e2c8050fe513be5e34b)**
Let’s go through the code line-by-line to understand what is happening.
❌ **Incorrect**, the return value is **0**
<details>
<summary>`fizz(0)` → **0**</summary>

`buzz = 0`
`result = []`
`for i in range(buzz):` → `range(0)` → `[]`
*for-loop is not executed as **`range(0)`** returns an empty range object*
`return(len(result))` → `len([])` → **0**
</details>
✅ **Correct, **the return value is **2**
<details>
<summary>`fizz(4)` → **2**</summary>

`buzz = 4`
`result = []`
`for i in range(buzz):` → `range(4)` → `[0, 1, 2, 3]`
<details>
<summary>1st run → `len(result)` → **1**</summary>

`i = 0`
`result = []`
`if (0%3 == 0)` `and` `(i%5 == 0):`→ `0 == 0` `and` `0 == 0` → `True` `and` `True`
`result.append(random.randrange(1,7))` → *random number is added to **`result`*
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
`if (1%3 == 0)` `and` `(1%5 == 0):`→ `1 == 0` `and` `1 == 0` → `False` `and` `False`
*not executed as if-statement evaluated to ****False***
`elif 1 % 3 == 0:` → `1 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`elif 1 % 5 == 0:` → `1 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`else:`
`result.append(1)`
</details>
<details>
<summary>3rd run → `len(result)` → **3**</summary>

`i = 2`
`result = [`*`<< rnd num >>, << rnd num >>`*`]`
`if (2%3 == 0)` `and` `(2%5 == 0):`→ `2 == 0` `and` `2 == 0` → `False` `and` `False`
*not executed as if-statement evaluated to ****False***
`elif 2 % 3 == 0:` → `2 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`elif 2 % 5 == 0:` → `2 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`else:`
`result.append(2)`
</details>
<details>
<summary>4th run → `len(result)` → **2**</summary>

`i = 3`
`result = [`*`<< num >>, << num >>`*`, 2]`
`if (3%3 == 0)` `and` `(3%5 == 0):`→ `0 == 0` `and` `3 == 0` → `True` `and` `False`
*not executed as if-statement evaluated to ****False***
`elif 3 % 3 == 0:` → `0 == 0` → `True`
`result = result[:len(result)-1]` → `[`*`<< rnd num >>, << rnd num >>`*`]`
`result[:len([`*`<< rnd num >>, << rnd num >>`*`, 2])-1]`
`result[:3-1]`
`result[:2]` → `[`*`<< rnd num >>, << rnd num >>`*`]`
`elif 2 % 5 == 0:`
*not evaluated as first elif-statement evaluated to ****True***
`else:`
*not evaluated as first elif-statement evaluated to ****True***
</details>
`return(len(result))` → `len([`*`<< rnd num >>`*`, `*`<< rnd num >>`*`])` → **2**
</details>
✅ **Correct, **the return value is **1**
<details>
<summary>`fizz(1)` → **1**</summary>

`buzz = 1`
`result = []`
`for i in range(buzz):` → `range(1)` → `[0]`
<details>
<summary>1st run → `len(result)` → **1**</summary>

`i = 0`
`if (0%3 == 0)` `and` `(i%5 == 0):`→ `0 == 0` `and` `0 == 0` → `True` `and` `True`
`result.append(random.randrange(1,7))` → *random number is added to **`result`*
`elif 0 % 3 == 0:`
*not evaluated as if-statement evaluated to ****True***
`elif i % 5 == 0:`
*not evaluated as if-statement evaluated to ****True***
`else:`
*not evaluated as if-statement evaluated to ****True***
</details>
`return(len(result))` → `len([`*`<< rnd num >>`*`])` → **1**
<!-- Unsupported block type: unsupported -->
</details>
✅ **Correct, **the return value is **3**
<details>
<summary>`fizz(3)` → **3**</summary>

`buzz = 4`
`result = []`
`for i in range(buzz):` → `range(4)` → `[0, 1, 2]`
<details>
<summary>1st run → `len(result)` → **1**</summary>

`i = 0`
`result = []`
`if (0%3 == 0)` `and` `(i%5 == 0):`→ `0 == 0` `and` `0 == 0` → `True` `and` `True`
`result.append(random.randrange(1,7))` → *random number is added to **`result`*
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
`if (1%3 == 0)` `and` `(1%5 == 0):`→ `1 == 0` `and` `1 == 0` → `False` `and` `False`
*not executed as if-statement evaluated to ****False***
`elif 1 % 3 == 0:` → `1 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`elif 1 % 5 == 0:` → `1 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`else:`
`result.append(1)`
</details>
<details>
<summary>3rd run → `len(result)` → **3**</summary>

`i = 2`
`result = [`*`<< rnd num >>, << rnd num >>`*`]`
`if (2%3 == 0)` `and` `(2%5 == 0):`→ `2 == 0` `and` `2 == 0` → `False` `and` `False`
*not executed as if-statement evaluated to ****False***
`elif 2 % 3 == 0:` → `2 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`elif 2 % 5 == 0:` → `2 == 0` → `False`
*not executed as elif-statement evaluated to ****False***
`else:`
`result.append(2)`
</details>
`return(len(result))` → `len([`*`<< rnd num >>`*`, `*`<< rnd num >>`*`, 2])` → **2**
</details>
❌ **Incorrect**, because answers 2 to 4 are correct
</details>
---
## Question 5
Gegeben ist die folgende Funktion:
```python
def get(elements):
	for element in elements:
		if isinstance(element, int):
			return element
```
Was macht die Funktion **get**? Nehmen Sie an, die Funktion wird korrekt aufgerufen mit einem Argument, welches eine Liste mit mindestens einem ganzzahligen Element ist.
❌ Sie gibt immer die letzte ganze Zahl (integer)der Liste elements zurück.
✅ Sie gibt immer die *erste gerade* (even integer) **oder** *erste ungerade* (*odd integer*) Zahl der Liste **elements** zurück.
❌ Sie gibt entweder *True* oder *False* zurück.
❌ Sie gibt immer das *erste* Element der Liste **elements** zurück.
❌ Sie gibt immer die erste *gerade* Zahl (*even integer*) der Liste **elements** zurück.

<details>
<summary>Explanation</summary>

> 💡 **[functions](/5b0832dbf9454eb1941b7632e68a9abb#d98d10a03b3b4d17a846dfff610e9a5f), [for-loop](/dfa7a8137dff402f9bcded5d8a28adda), [check datatype](/5b0832dbf9454eb1941b7632e68a9abb#6f8e8203d09a4c3aafa6f5d78119fe00)**
Looking at the function we can observe that it always returns the first element in list `elements` that is of type **integer. **
❌ **Incorrect, **the function returns the first element not the last one. A for-loop goes through an iterable like a list **from left to right**, i.e., starts with the firs tone and ends with the last one, and not the other way around.
✅ **Correct**, the function returns the first integer. Integer are natural / whole numbers. A natural number can either be odd (e.g. 1) or even (e.g. 2). Thus, the first integer in `elements` that is returned by the function will either be odd or even.
❌ **Incorrect**, the function returns an integer, not a boolean value. This is because `isinstance(element, `**`int`**`)` is used which checks if the current element is of datatype integer. If we were to see `isinstance(element, `**`bool`**`)` then the function would return a boolean value.
❌ **Incorrect**, if the first element is another datatype than integer than it would not be returned. For example, for the list `[False, 'CS', 2]`, the function returns the integer **2** which is only the **third** element in the list.
❌ **Incorrect**, the function just returns the first integer, regardless of this integer being odd or even.
</details>
---

📄 **[Quiz 4]** (subpage)
## Question 1
Stellen wir uns vor, wir hätten eine Funktion **fibonacci(n)** definiert. Diese Funktion nimmt als Parameter eine beliebige ganze (*int*) Zahl (*n*) an und prüft, ob **n = 0** und **n = 1**. Wenn eine der beiden Bedingungen wahr ist, gibt die Funktion den Wert von **n** zurück. Wenn keine der beiden Bedingungen **wahr** ist, gibt die Funktion die Summe **fibonacci(n-2) + fibonacci(n-1) **zurück.

Bitte markieren Sie **alle** wahren Aussagen.
❌ Die Funktion **fibonacci(n)** ist zwar rekursiv aber sie ist hier fehlerhaft definiert, da sie zwei Basisfälle (base cases) hat und ihre Ausführung somit niemals endet.
❌ Der Aufruf **fibonacci(1)** hat das gleiche Ergebnis wie **fibonacci(-1)**.
❌ Der Aufruf **fibonacci(1)** hat das gleiche Ergebnis wie **fibonacci(0)**.
✅ Ist **n** eine *negative* ganze Zahl, so kann die Funktion gar nicht ausgeführt werden, da Fibonacci-Zahlen nur für positive Zahlen definiert sind.
✅ **fibonacci(n)** ist eine rekursive Funktion.

<details>
<summary>Explanation</summary>

> 💡 **[recursive functions](/5b0832dbf9454eb1941b7632e68a9abb#1b1c18524841477bacf6a53bcbc56386), [**fibonacci numbers**](https://www.mathsisfun.com/numbers/fibonacci-sequence.html), [fibonacci function](/5b0832dbf9454eb1941b7632e68a9abb#deadb4d546c746fb988789ae1b7832b5), [logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)**
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
❌ **Incorrect**, the function will stop at one point. Specifically, it will stop by returning **0** (line 3) or **1** (line 5), i.e., as soon as one of the two stop conditions is met. 
❌ **Incorrect**. If `fibonacci(1)` is called, the integer **1** will be returned as the condition of the `elif` statement evaluates to **True**: `n == 1` → `1 == 1` → **True**
If we pass a negative integer to the function, e.g., `fibonacci(-5)`, the two **if**-statements, i.e., the stop conditions, will not evaluate to True as **-5** is not equal to **0**, **1** or **2**.
Thus, the code in the **else** block gets executed, which contains two recursive function calls. So we call ourselves again with `fibonacci(-7)` and `fibonacci(-6)`.
From these two examples we can see that the result will not be the same.
❌ **Incorrect**. `fibonacci(0)` will return **0** while `fibonacci(1)` will return **1.**
✅ **Correct**, there are no negative fibonacci numbers. However, calling the function above with a negative number would technically still work. However as `n` gets smaller and smaller with each recursive function call (`fibonacci(n-2)` and `fibonacci(n-1)`) the stop conditions will never be met and a [**recursion error**](/11e0858bd5f644b884dc550dd3c6c4bb) is raised eventually.
✅ **Correct**, the function `fibonacci()` is called inside the function `fibonacci()` itself. Thus, the function is calling itself and is considered **recursive**.
</details>
---
## Question 2
Wie of wird im folgenden Programm die Funktion **f** aufgerufen?
```python
def f(x):
	return × + 2

list(map(f, filter(lambda x: f(x) % 2 == 0, range(6))))
```
Answer: **9**

<details>
<summary>Explanation</summary>

> 💡 **[modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c), [range object](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385), [map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9), [filter function](/5b0832dbf9454eb1941b7632e68a9abb#1dc0b8cb700741e5a48f5ed4180b2035)**
**Important:** Always read nested functions from the inside to the outside! Start by executing the filter function before looking about the map function.
Check the break-down below to understand what is happening line-by-line. 
<details>
<summary>`list(map(f, filter(lambda x: f(x) % 2 == 0, range(6))))` → `[2, 4, 6]`</summary>

<details>
<summary>`map(f, filter(lambda x: f(x) % 2 == 0, range(6)))` → `map-object`</summary>

<details>
<summary>`filter(lambda x: f(x) % 2 == 0, range(6))` → **f(x)** 6 times executed</summary>

**Input**: `range(6)` → ` range(0, 6)` → `[0, 1, 2, 3, 4, 5]`
<details>
<summary>**Function:** `filter(lambda x: f(x) % 2 == 0, [0, 1, 2, 3, 4, 5]`</summary>

<details>
<summary>**1st run** → True → keep **0 **→ **`[0]`**** → **1 execution of** f(x)**</summary>

`x = 0`
`f(0) % 2 == 0` → `2 % 2 == 0` → `0 == 0` → **True**
</details>
<details>
<summary>**2nd run** → False → discard **1 **→ **`[0]`**** → **1 execution of** f(x)**</summary>

`x = 1`
`f(1) % 2 == 0` → `3 % 2 == 0` → `1 == 0` → **False**
</details>
<details>
<summary>**3rd run** → True → keep **2 **→ **`[0, 2]`**** → **1 execution of** f(x)**</summary>

`x = 2`
`f(2) % 2 == 0` → `4 % 2 == 0` → `0 == 0` → **True**
</details>
<details>
<summary>**4th run** → False → discard **3 **→ **`[0, 2]`**** → **1 execution of** f(x)**</summary>

`x = 3`
`f(3) % 2 == 0` → `5 % 2 == 0` → `1 == 0` → **False**
</details>
<details>
<summary>**5th run** → True → keep **4 **→ **`[0, 2, 4]`**** → **1 execution of** f(x)**</summary>

`x = 4`
`f(4) % 2 == 0` → `6 % 2 == 0` → `0 == 0` → **True**
</details>
<details>
<summary>**6th run** → False → discard **5 **→ **`[0, 2, 4]`**** → **1 execution of** f(x)**</summary>

`x = 5`
`f(5) % 2 == 0` → `7 % 2 == 0` → `1 == 0` → **False**

</details>
</details>
**Output:** `[0, 2, 4]` | `f(x)` # executed: **6** times
</details>
<details>
<summary>`map(f, << filter function >>)` → **f(x)** 3 times executed</summary>

**Input**: `[0, 2, 4]`
<details>
<summary>**Function:** `map(f, [0, 2, 4])`</summary>

<details>
<summary>**1st run** → **`[2, 2, 4]`**** → **1 execution of** f(x)**</summary>

`x = 0`
`f(0)` → **2**
</details>
<details>
<summary>**2nd run** → **`[2, 4, 4]`**** → **1 execution of** f(x)**</summary>

`x = 0`
`f(2)` → **4**
</details>
<details>
<summary>**3th run** → **`[2, 4, 6]`**** → **1 execution of** f(x)**</summary>

`x = 0`
`f(4)` → **6**
</details>
</details>
**Output:** `[2, 4, 6]` | `f(x)` # executed: **3** times
</details>
</details>
</details>
We can see that from the **filter** function the function **f(x)** is called **6** and from the map function **3** times. Thus, in total the function **f(x)** is called **9** times.
</details>
---
## Question 3
Welcher Wert wird nach dem folgendem Aufruf von der list-Funktion zurückgegeben?
```python
list(map(max, ([1], [2], [3], [4], [5], [6])))
```
❌ Die Ausführung wird mit einer Fehlermeldung abgebrochen, da die *map*-Funktion nicht mit einem *Tupel* von *Listen* umgehen kann.
❌ `6`
❌ `<map at 0x20132719d00>`
❌ `[False, False, False, False, False, True]`
❌ `[61]`
✅ `[1,2,3,4,5,6]`
❌ Keine der anderen Antworten ist *wahr*.

<details>
<summary>Explanation</summary>

> 💡 **[map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9), [tuple](/5b0832dbf9454eb1941b7632e68a9abb#f8cb18a835dd45c1aed5abca3279ba9c), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb)**
❌ **Incorrect**. A map function expects an **iterable** as an input. Then, it applies the defined function **on each element** in the iterable. Since a tuple is an iterable, there is no issue here.
❌ **Incorrect**. A map function returns a map object. However, in the code the map object is **converted to a list** using the `list()` method. Thus, the output is a list.
❌ **Incorrect**. The `max()` function (which is used inside the map-function) returns the **highest value** in an iterable and not a boolean value.
❌ **Incorrect**. Since a map-function is applied on each element in an iterable, the function output contains usually the **same number of elements** as the input.
✅ **Correct**. Check below to see what is happening line by line. 
<details>
<summary>`list(map(max, ([1], [2], [3], [4], [5], [6])))` → **`[1,2,3,4,5,6]`**</summary>

<details>
<summary>`map(max, ([1], [2], [3], [4], [5], [6]))` → `<map at 0x20132719d00>`</summary>

**1st run** → `max([1])` → **1**
**2nd run** → `max([2])` → **2**
**3rd run** → `max([3])` → **3**
**4th run** → `max([4])` → **4**
**5th run** → `max([5])` → **5**
**6th run** → `max([6])` → **6**
</details>
</details>
❌ **Incorrect**, because the previous answer is correct.
</details>
---
## Question 4
Gegeben ist die folgende Funktion. Bitte markieren Sie **alle **wahren Aussagen.
```python
def recursive_sum(number):
	number = int(number)
	
	if number < 0:
		raise ValueError (f"recursive_sum requires a non-negative argument but has been called with number={number}")
	elif number == 1 :
		return 1
	else:
		return number + recursive_sum(number - 1)
```
✅ Die Funktion **recursive_sum** kann in Standard-Python mit allen Gleitkommazahlen (float) zwischen 1 und 101 als Argument fehlerfrei ausgeführt werden.
❌ Die Funktion **recursive_sum** kann in Standard-Python mit allen positiven ganzen Zahlen grösser als 0 als Argument ausgeführt werden, ohne dass dabei ein Fehler erzeugt wird.
❌ Die Funktion **recursive_sum** gibt immer die Summe aller *positiven* *ungeraden* Zahlen zurück, die kleiner als oder gleich dem Argument sind.
✅ Die Funktion **recursive_sum** kann in Standard Python fehlerfrei ausgeführt werden, obwohl sie mehrere return Statements enthält.
❌ Wird die Funktion als **recursive_sum(2.1234) **aufgerufen, gibt sie den Wert 2 zurück.
✅ Wird die Funktion als **recursive_sum(4)** aufgerufen, gibt sieden Wert 10 zurück.
❌ Die Funktion **recursive_sum** gibt immer die Summe aller *positiven geraden Zahlen* zurück, die kleiner als oder gleich dem Argument sind.
✅ **recursive_sum** ist eine rekursive (*recursive*) Funktion.
✅ Wird die Funktion als **recursive_sum(1.1234) **aufgerufen, gibt sie den Wert 1 zurück.
❌ Wird die Funktion als **recursive_sum(0)** aufgerufen, wird die Programmausführung mit einem *RecursionError* abgebrochen, da der Basisfall (base case) nie erreicht wird.

<details>
<summary>Explanation</summary>

> 💡 **[recursive functions](/5b0832dbf9454eb1941b7632e68a9abb#1b1c18524841477bacf6a53bcbc56386), [logical statements](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb)**
✅ **Correct**. In the first line of the function we can see that the value stored in `number` is being converted to an integer. So when we call the function with a float value, e.g., `recursive_sum(5.7)`, then this **float will be converted to an integer**: `int(5.7)` → **6**
If there wasn’t a conversion of the float to an integer, the function would terminate with a [recursion error](/11e0858bd5f644b884dc550dd3c6c4bb) as the stop condition (`number == 1`) will never be met (because `number` is a float and is compared with an integer).
❌ **Incorrect**. *I don’t know why this shouldn’t be correct.*
❌ **Incorrect**. The function does not filter out odd numbers. Let’s assume we call the function with `recursive_sum(3)`. Check below what is happening line-by-line.
<details>
<summary>`recursive_sum(3)` → **6**</summary>

`number = 3`
`if number < 0:`
*not executed as 3 is not smaller than 0*
`elif number == 1 :`
*not executed as 3 is not equal to 1*
`else:`
`return 3 +` → **3 + ****3** → **6**
<details>
<summary>`recursive_sum(3 - 1)` → **3**</summary>

`number = 2`
`if number < 0:`
*not executed as 2 is not smaller than 0*
`elif number == 1 :`
*not executed as 2 is not equal to 1*
`else:`
`return 2 +` → **2 + ****1** → **3**
<details>
<summary>`recursive_sum(2 - 1)` → **1**</summary>

`number = 1`
`if number < 0:`
*not executed as 1 is not smaller than 0*
`elif number == 1:`
`return 1`
`else:`
*not executed as elif statement evaluated to True*
</details>
</details>
</details>
If the function was to calculate the sum of odd numbers, it would return **4** (3 + 1) and not **6**.
✅ **Correct**. Multiple return statements do not indicate that something is broken but often indicate that we are dealing with a **recursive function** that is calling itself multiple times.
❌ **Incorrect**. If the function is called with `recursive(2.1234)` it returns **3**. Check below what is happening line-by-line. 
<details>
<summary>`recursive_sum(2.1234)` → **3**</summary>

`number = int(2.1234)` → `2`
`if number < 0:`
*not executed as 2 is not smaller than 0*
`elif number == 1 :`
*not executed as 2 is not equal to 1*
`else:`
`return 2 +` → 2** + ****1** → **3**
<details>
<summary>`recursive_sum(2 - 1)` → **1**</summary>

`number = 1`
`if number < 0:`
*not executed as 2 is not smaller than 0*
`elif number == 1 :`
`return 1` → **1**
`else:`
*not executed as the elif-statement evaluated to True*
</details>
</details>
✅ **Correct**. We can observe from the previous two executions that the function is returning the recursive sum of `number`. Te recursive sum of **4** is **4 + 3 + 2 + 1** which is equal to **10**.
❌ **Incorrect**. The function returns the recursive sum of `number`.
✅ **Correct**. Inside `recursive_sum()`, `recursive_sum()` is called. Thus the function is calling itself and is considered **recursive**.
✅ Correct. **1.1234** is converted to integer **1** with `int(1.1234)` and the recursive sum of **1** is **1**.
❌ **Incorrect**. The function will be terminated with a `ValueError` that is defined inside the if-statement. Check the code below to understand what is happening. 
<details>
<summary>`recursive_sum(0)` → **`ValueError`**</summary>

`number = 0` 
`if number < 0:`
*not executed as 0 is not smaller than 0*
`elif number == 1 :`
*not executed as 0 is not equal to 1*
`else:`
`return 0 +` → **`ValueError`**
<details>
<summary>`recursive_sum(0 - 1)` → **`ValueError`**</summary>

`number = 1`
`if number < 0:` → `-1 < 0` → `True`
**`raise ValueError`**` `
`elif number == 1 :`
*not executed as the if-statement evaluated to True*
`else:`
*not executed as the if-statement evaluated to True*
</details>
</details>
</details>
---
## Question 5
In Aufgabe 3 des letzten Assignments ging es darum, eine Liste (to_sort) mit ganzen Zahlen zu nehmen, jede einzelne dieser Zahlen in einen String umzuwandeln, die einzelnen Ziffern jedes Strings absteigend zu sortieren und das Ergebnis in einer neuen Liste (sorted_list) zu speichern. Das folgende Programm erweitert die Anforderung dahingehend, dass in der neuen Liste (sorted_list) nun auch wieder ganze Zahlen statt deren String-Repräsentation vorhanden sein sollen.
Kurz: Aus der Liste **to_sort = [1, 10, 23, 33, 24, 100, 48279] **soll die Liste **sorted_list** mit dem Wert *[1, 10, 23, 33, 42, 100, 98742]* werden.
```sql
to_sort = [1, 10, 23, 33, 42, 100, 48279]

sorted_list = list(map(lambda d: int("".join(sorted(str(d), reverse=True))), to_sort))
```
Warum funktioniert das Programm **nicht** wie vorgesehen?

❌ Die nun gewünschte Funktionalität kann nicht als Lambda dargestellt werden. Stattdessen hätte, wie im Assignment vorgeschlagen, eine eigene Funktion **sort_numbers_by_digit()** implementiert werden müssen.
❌ Da das **return**-Statement fehlt, wird gar nichts gespeichert.
❌ Die Funktion **sorted()** erwartet ein Iterable als Argument, sie bekommt jedoch einen String-Wert übergeben.
❌ Die Funktion **sorted() **sortiert in der falschen Reihenfolge wegen des Keyword Arguments **reverse=True**.
✅ Die Annahme, das Programm würde nicht das tun, was es soll, ist *nicht zutreffend*. Tatsächlich erfüllt das Programm die oben beschriebenen Anforderungen genau.
❌ Die **Lambda**-Funktion erwartet nur *ein* Argument, bekommt hier jedoch eine ganze Liste von Argumenten.
❌ Die Funktion **sorted()** ist eigentlich eine Listen-Methode (*list method*) und kann darum nur auf *list*-Objekten aufgerufen werden.
❌ Ein *String* kann nicht mit der Funktion **sorted()** sortiert werden, da Strings keine Reihenfolge haben.
❌ Da die Funktion **sorted()** immer eine Liste (*list*) zurück gibt, kann diese nicht in eine ganze Zahl (*int*) konvertiert werden.

<details>
<summary>Explanation</summary>

> 💡 **[map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9), [sorted function](/5b0832dbf9454eb1941b7632e68a9abb#7c022c5cc1a647d58ba1a7e82406c3e6), [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb)**
Instead of going through all the answers which are incorrect, it is important to understand why the function is working as intended. Check the line-by-line execution below.
<details>
<summary>`list(map(lambda d: int("".join(sorted(str(d), reverse=True))), to_sort))
`→ `[1, 10, 23, 22, 42, 100, 98742]`</summary>

<details>
<summary>`map(lambda d: int("".join(sorted(str(d), reverse=True))), to_sort)
`→** ****`map-object`**</summary>

<details>
<summary>1st run → **`1`**</summary>

`d = 1`
`int("".join(sorted(str(1), reverse=True)))` → `int("1")` → `1`
`"".join(sorted(str(1), reverse=True))` → `"".join("1")` → `"1"`
`sorted(str(1), reverse=True)` → `"1"`
`str(1)` → `"1"`
</details>
<details>
<summary>2nd run → **`10`**</summary>

`d = 10`
`int("".join(sorted(str(10), reverse=True)))` → `int("10")` → **`10`**
`"".join(sorted(str(10), reverse=True))` → `"".join("10")` → `"10"`
`sorted(str(10), reverse=True)` → `"10"`
`str(10)` → `"10"`
</details>
<details>
<summary>3rd run → **`23`**</summary>

`d = 23`
`int("".join(sorted(str(23), reverse=True)))` → `int("23")` → **`23`**
`"".join(sorted(str(23), reverse=True))` → `"".join("23")` → `"23"`
`sorted(str(23), reverse=True)` → `"23"`
`str(23)` → `"23"`
</details>
<details>
<summary>4th run → **`33`**</summary>

`d = 33`
`int("".join(sorted(str(33), reverse=True)))` → `int("33")` → **`33`**
`"".join(sorted(str(33), reverse=True))` → `"".join("33")` → `"33"`
`sorted(str(33), reverse=True)` → `"33"`
`str(33)` → `"33"`
</details>
<details>
<summary>5th run → **`42`**</summary>

`d = 42`
`int("".join(sorted(str(42), reverse=True)))` → `int("42")` → **`42`**
`"".join(sorted(str(42), reverse=True))` → `"".join("42")` → `"42"`
`sorted(str(42), reverse=True)` → `"42"`
`str(42)` → `"42"`
</details>
<details>
<summary>6th run → **`100`**</summary>

`d = 100`
`int("".join(sorted(str(100), reverse=True)))` → `int("100")` → **`100`**
`"".join(sorted(str(100), reverse=True))` → `"".join("100")` → `"100"`
`sorted(str(100), reverse=True)` → `"100"`
`str(100)` → `"100"`
</details>
<details>
<summary>7th run → **`98742`**</summary>

`d = 48279`
`int("".join(sorted(str(48279), reverse=True)))` → `int("98742")` → **`98742`**
`"".join(sorted(str(48279), reverse=True))` → `"".join("98742")` → `"98742"`
`sorted(str(48279), reverse=True)` → `"98742"`
`str(48279)` → `"48279"`
</details>
</details>
</details>
</details>
---
## Question 6
Welcher Wert wird nach folgendem Aufruf von der **list**-Funktion zurückgegeben?
`list(map(lambda my_var: 2, (1, 2, 3, 4, 5, 6))`
❌ `[2,4,6,8,10,12]`
❌ Die Ausführung wird mit einer Fehlermeldung abgebrochen, da statt einer Liste ein Tupel asl Argument übergeben würde.
✅ `[2, 2, 2, 2, 2, 2]`
❌ `[1, 2]`
❌ `2`
❌ `[3, 4, 5, 6, 7, 8]`
❌ `[3]`
❌ `[2]`
❌ Keine der anderen Antworten ist wahr.

<details>
<summary>Explanation</summary>

> 💡 **[map function](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)**
This is rather a trick-question and you need to pay attention on reading the commas right. Check the below line-by-line execution to understand what is going on. 
`list(map(lambda my_var: 2, (1, 2, 3, 4, 5, 6))` → `[2, 2, 2, 2, 2, 2]`
`map(lambda my_var: 2, (1, 2, 3, 4, 5, 6)` → `map-object`
1st run → `lambda 1: 2` → `2`
2nd run → `lambda 2: 2` → `2`
3rd run → `lambda 3: 2` → `2`
3rd run → `lambda 4: 2` → `2`
3rd run → `lambda 5: 2` → `2`
3rd run → `lambda 6: 2` → `2`
We can see that no matter what we give as input into the lambda function, it will always return **2**. This is because there is the constant value **2** defined to the right of the double-point `:`  Thus, the lambda function is not doing much.
</details>
---

📄 **[Quiz 5]** (subpage)
## Question 1
Gehen Sie davon aus, dass **management_student** (ein Objekt der Klasse **Superhero** aus dem Assignment) gegeben ist. Was passiert, wenn Sie folgenden Python-Code ausführen?
`print(management_student)`

❌ Nichts passiert, solange die Methode .__*init*()__ kein return statement hat.
❌ Es wird immer die Methode .__*repr*()__ ausgeführt, sofern sie definiert ist.
❌ Python versucht das Objekt darzustellen, zeigt aber nur die Klassenbezeichnung und das erste Attribut.
✅ Es wird immer die Methode .*__str()__* ausgeführt, sofern sie definiert ist.

<details>
<summary>Explanation</summary>

> 💡 **[string representation](/83479909f70b47e491c55c9a6178291a#d6adf9d285e743288d38c01044065158), [object representation](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073), [constructor](/83479909f70b47e491c55c9a6178291a#49c076e6f99740dcb067ca6026d9a60d)**
❌ **Incorrect**. The constructor, i.e., the `__init__()` method is executed when a **new object of a class** (class instance) is created. For example, if we would create a new superhero we can do `Superhero()`, and this calls the `__init__()` method inside the **Superhero** class.
❌ **Incorrect**. The object representation, i.e., the `__repr__()` method is executed when the variable in which the reference address to the object is stored is **outputted on the console**.
For example, if we would simply write `management_student` in a code cell and hit shift+enter, then the `__repr__()` method inside the Superhero class is executed.
❌ **Incorrect**. Python will call the `__str__()` method. If the method it is not implemented in the class, then the **memory reference address** of this object is returned and printed.
✅ **Correct**. Inside the `__str__()` method we can specify what should happen when `print(management_student)` is called.
</details>
---
## Question 2
Die Instanz einer Unterklasse **U **(*sub class*) ist auch immer eine Instanz der Superklasse **S **(*super class*) von welcher **U** erbt.
✅ Wahr
❌ Falsch

<details>
<summary>Explanation</summary>

> 💡 **[class inheritance](/c991314990fa47e19addaf16235213db)**
✅ **Correct**. Inheritance is a `is-a` relationship. This means: ***sub class*** **`is-a`** ***super class*** as it inherits the attributes and methods of the ***super class***.
</details>
---
## Question 3
Markieren Sie **alle** zutreffenden Aussagen.
Methoden, die in Python innerhalb von Klassendefinitionen definiert werden:
✅ sind, zum Beispiel im Fall von Getter-/Setter-Methoden, beim Aufruf durch Client-Code, oft nicht als Methoden erkennbar.
❌ dürfen *nicht* genauso heissen, wie Methoden ihrer *Superklasse*.
✅ können Funktionalität von Methoden der jeweiligen Superklasse wiederverwenden.
✅ können, wie Funktionen auch, *optionale* Argumente besitzen.
❌ müssen, wie auch Funktionen, immer ein **return** Statement haben. Ein **print()** ist nicht ausreichend.
✅ können, wie Funktionen auch, Argumente mit *Default*-Werten definieren.
✅ können, wie Funktionen auch, Argumente an *bestimmten Positionen* (positional arguments) erwarten.
✅ definieren, im Gegensatz zu Funktionen, meist eine Referenz zum aufrufenden Objekt (*self*) als Argument.

<details>
<summary>Explanation</summary>

> 💡 **[getter](/83479909f70b47e491c55c9a6178291a#4d9fcd781fd5450697ba15e0c6989f20) & [setter](/83479909f70b47e491c55c9a6178291a#0fd3908f13ee4acf9601894aeebbcb56) method, [access class attributes](/83479909f70b47e491c55c9a6178291a#72cd5f486f4b455093b47d3a2115ff49), [class inheritance](/c991314990fa47e19addaf16235213db), [optional & required parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc), [polymorphism](/1847b80cf96b485da5725e3cd1b35ca9)**
✅ **Correct**. A setter-method (if implemented) is called when a new value is assigned to an attribute of a class instance. However, a setter-method does not change anything on how the new value is assigned in the client code. This means we can still follow the pattern of:
`<< variable >>.<< attribute_name >> = << new_value >>`
For example, if we want to change the name of the management student we would call:
`management_student.name = "Marco"`
And we don’t know if there is a setter method implemented and being executed inside the class **Superhero**.
❌ **Incorrect**. If a method in the sub class is called the same as in the parent class, then the **method is overwritten** by the sub class. Python always tries to execute the **most specific **method of an object (Polymorphism).
For example, let’s assume that the Superhero class is a sub class of Hero and both classes have a method implemented called `get_hero_level()`.
If we now create a new Superhero `management_student = Superhero()` and call `management_student.get_hero_level()` then Python sees that there are **two** methods with this name: the **one** from **Superhero** class and the **one** from **Hero** class. However, the `Superhero.get_hero_level()` **overwrites** `Hero.get_hero_level()` which is why the `Superhero.get_hero_level()` method gets executed.
✅ **Correct**. A sub class i**nherits all methods and attributes** from its super class. For example, if only the Hero class has a `get_hero_level()` method, then we can still call `management_student.get_hero_level()` as the `Hero.get_hero_level()` method is executed automatically.
✅ **Correct**. Each method can have **required** and/or **optional** arguments. No matter if that method is defined inside a class or outside.
❌ **Incorrect**. A method inside a class is conceptually **nothing different** than a regular function. Thus, a return statement is not a necessity.
For example, inside the `get_hero_level()` we can either do `return self.hero_level` to **give the hero level back** to the client-code or **print the hero level** to the console directly using `print(self.hero_level)`.
✅ **Correct**. We learned already that class methods, just as regular functions, can have **required and optional** parameters. Whenever we have optional parameters we have **default values **defined as well. Because we must Python tell **which value to use** if from the client-code no value for the optional parameter is provided.
✅ **Correct**. Just as with regular functions, there can be positional arguments (usually in combination with optional parameters).
✅ **Correct**. This is why in any class method we need to provide the keyword **`self`** in the function header. For example, inside the `Hero.get_hero_level()` method we need to put the `self` parameter as first argument `def get_hero_level(`**`self`**`):` so that the method can then access the current hero level of the management student by calling `self.hero_level`.
</details>
---
## Question 4
Gegeben ist das folgende Programm. Es wurde fehlerfrei ausgeführt.
```python
class Person:
	def __init__(self, name, year_of_birth):
	# Bitte nenmen Sie for the init Methode an, das die Variablen
	# self._name und self._year_of_birth mit den zugehörigen Argumenten
	# name und year_of_birth korrekt initialisiert wurden

	@property
	def name(self):
		return selt._name
	@property
	def year_of_birth(self):
		return self._year_of_birth
	
	def compute_age (self):
		return 2023 - self.year_of_birth
	
	def __str__(self):
		return f"{self.name} ({self. compute_age()})"
	
	def __repr__(self):
		return "Person('(self.name}', (self.compute_age()})"

class Student(Person):
	def __init__(self, name, year_of_birth, courses):
		# Bitte nehmen Sie for the init_ , Methode an, das die
		# Argumente name und year_of_birth korrekt via super().__init__ (...)
		# weitergegeben wurden und dass self.courses mit dem
		# zugehörigen Argument courses korrekt initialisiert wurde

	@property
	def courses (self):
		return self._courses
	
	@courses.setter
	def courses (self, courses):
		if isinstance(courses, list):
			self._courses = courses
		else:
			raise TypeError('courses need to be provided as list obiects')

	def __str__(self):
		return f"{super().__str__()), courses: (', '.join(self.courses)}"
	
	def __repr__(self):
		return "Student('(self.name}', {self.compute_age ()), (self.courses})"

p = Person('Max', 2001)
s = Student('Lena', 2000, ['Travel at the speed of light', 'Harnessing complexity'])
```
Bitte markieren Sie **alle** korrekten Aussagen zu obigem Programm:
✅ Statement 1
Der Aufruf
`s`
gibt folgenden Wert zurück:
Student ('Lena', 23, ['Travel at the speed of light', 'Harnessing complexity'])
✅ Statement 2
**Student** ist eine Klasse.
❌ Statement 3
Der Aufruf
`s.compute_age()
`führt zu einem Fehler, da für die Klasse Student die Methode **.compute_age() **nicht definiert wurde.
✅ Statement 4
Der Aufruf
`s.courses.append('Bending rooms')`
kann fehlerfrei ausgeführt werden, da **.append()** eine list Methode ist, welche Elemente an Listen anhängt.
✅ Statement 5
**Student** ist eine Unterklasse (*sub class*) von **Person**.
✅ Statement 6
Es wurde eine Instanz von **Student** erstellt.
✅ Statement 7
Es wurden zwei Instanzen von **Person** erstellt.
❌ Statement 8
Der Aufruf
`p.name = 'Michaela'`
kann fehlerfrei ausgeführt werden, da das Attributname einen String erwartet.
❌ Statement 9
**Person** erbt von **Student**.

<details>
<summary>Explanation</summary>

> 💡 **[object representation](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073), [append method](/5b0832dbf9454eb1941b7632e68a9abb#2561c3326d19459292a03dea27a7eda1), [class inheritance](/c991314990fa47e19addaf16235213db), [private attributes](/83479909f70b47e491c55c9a6178291a#612dfd274bbe4cb9bb0de56eabc4538d), [setter method](/83479909f70b47e491c55c9a6178291a#0fd3908f13ee4acf9601894aeebbcb56)**
✅ **Correct**. Check the code execution below to understand what is happening.
<details>
<summary>`s` →  **('Lena', 23, ['Travel at the speed of light', 'Harnessing complexity'])**</summary>

<details>
<summary>`def __repr__(self):`</summary>

`return "Student('(self.name}', {self.compute_age ()), (self.courses})"`
→ **('Lena', 23, ['Travel at the speed of light', 'Harnessing complexity'])**
`self.name` → **“Lena”**
<details>
<summary>`self.compute_age()` → **23** </summary>

<details>
<summary>`return 2023 - self.year_of_birth` → **2023 - 2000** → **23**</summary>

`self.year_of_birth` → **2000**
</details>
</details>
`self.courses` → ['Travel at the speed of light', 'Harnessing complexity']
</details>
</details>
✅ **Correct**. There is `class Student` defined.
❌ **Incorrect**. As seen in the [first answer](/57a6ad838ae7469f9ea3a663c2e29032), the method is implemented correctly and thus does not lead to an error.
✅ **Correct**. As the courses variable stores a list containing all the courses in which the student is enrolled, we can simply **access this list** with `s.courses` and then **append to this list **any element, i.e., course using the `.append()` method.
✅ **Correct**. We can see that **Student** is a sub class of **Person** by looking at the class header: `class Student(Person)`. 
✅ **Correct**. `Student()` was called and thus a new instance of **Student** class got created.
✅ **Correct**. One instance of Person was created by calling `Person()` and another instance by calling `Student()`. As **Student** is a sub-class of **Person** and the constructor of the **Person** class is called inside the **Student** class `super().__init__(name, year_of_birth)`, whenever a **Student** object is created also a **Person** object is created at the same time.
❌ **Incorrect**. From the descriptions inside the code we can see that a name attribute exists only on the **Person** class. And on the **Person** class this attribute is called `_name` and not `name`. Thus, when the value for the `_name` attribute is set with `p.name` an **error is raised**. We could set the value with `p._name`, however this is not best practice as `_name` is a **private** attribute (leading underline `_`). Thus, we should modify its value by using a setter method:
```python
@name.setter
def name(self, name):
	self._name = name
```
How we can modify the name by doing `p.name = "Michaela"`. This calls the setter method defined above and inside the setter method the value of the private attribute `_name` is modified. 
❌ **Incorrect**. It is the other way around: **Student** `is-a` **Person**. **Student** `is-a` subclass of **Person**. **Student** inherits from **Person**.
</details>
---
📄 **[Quiz 6]** (subpage)
## Question 1
In Assignment 6 war Ihr letztes Ziel, die 10 besten Restaurants zu finden. Würde der folgende Code dieses Ziel erreichen?
```python
def find_top10_restaurants_for_trip(origin, destination, departure_date, departure_time,
radius):
	limit=10
	c = find_connection(origin, destination, departure_date, departure_time)
	rests = find_restaurants(c.destination_x, c.destination_y, c.get_unix_arrival_time(), radius)
	return rests [:limit]
```
❌ Ja, das ist perfekt. Sie erhalten die 10 besten Restaurants, weil wir die Liste auf 10 begrenzt haben.
❌ Sie müssen dies zusätzlich tun: `rests sorted = sorted(rests, key=lambda tup: tup[1])` und dann `return rests_sorted[:limit]`
❌ Es gibt keine Möglichkeit, nur die ersten 10 Verbindungen anzufordern.
❌ Sie müssen dies zusätzlich tun: `rests_sorted = sorted(rests, key=lambda tup: tup[2], reverse=True)` und dann `return rests_sorted[:limit]`
❌ Die API berücksichtigt bereits standardmäßig nur die Top-10-Restaurants.
✅ Sie müssen dies zusätzlich tun: `rests_sorted = sorted(rests, key=lambda tup: tup[1], reverse=True)` und dann `return rests_sorted[:limit]`

<details>
<summary>Explanation</summary>

> 💡 **[sorted function](/5b0832dbf9454eb1941b7632e68a9abb#7c022c5cc1a647d58ba1a7e82406c3e6), [access elements in nested lists (or tuples)](/5b0832dbf9454eb1941b7632e68a9abb#8526be0c72d1432c83067d8315535bd0)**
❌ **Incorrect**. The code will return the **10 closest** **restaurants** but not necessarily the 10 best ones (based on rating).
❌ **Incorrect**. The `sorted()` function sorts by default in **ascending** order. Thus the restaurant with the **lowest rating** would appear on top in this case.
❌ **Incorrect**. This was implemented in the assignment, to get the next **x** connections.
❌ **Incorrect**. The API returns **all restaurants that are within the provided radius** of the x and y coordinate location. Therefore it can be that the API returns less or more than 10.
✅ **Correct**. The rating of the restaurant is at **index position 1** of each element in `rests`. Thus, the rating can be accessed by using `tup[1]`. Now as we pass the `reverse=True` parameter to the **sorted** function and the restaurants are sorted in **descending** **order** so the **highest-rated** one is appearing **on top**.
</details>
---
## Question 2
Sie möchten ein Experiment durchführen, beidem Sie einen Webbrowser, z.B. Firefox, öffnen und auf [http://example.org](http://example.org/) gehen. Parallel dazu zeichnen Sie mit Wireshark die Pakete im Netzwerk auf. Welche der folgenden Aussagen sind richtig?
❌ Um die IP-Adresse von [example.org](http://example.org/) zu ermitteln, können Sie ipconfig (oder ifconfig) verwenden.
✅ Der Name ([example.org](http://example.org/)) wird vom DNS auf eine zugehörige IP-Adresse abgebildet. Sie können auch den Befehl nslookup verwenden, um die IP-Adresse von [example.org](http://vonexample.org/) zu finden.
✅ Auf Wireshark sehen Sie eine HTTP-GET-Anfrage, gefolgt von der Antwort des Servers mit HTML-Inhalt.
❌ Die IP-Adresse von [example.org](http://example.org/) wird von der IP-Schicht gefunden, welche die Router im Internet abfragt.

<details>
<summary>Explanation</summary>

> 💡 **[networking stack](/305c770201f94279bfd468d86c733ae6), [DNS](/98fd60d45a0a4426a6f28d2665ba5a43#56e2d7cb60a34ae29ac8a805c79f51d8), [HTTP request methods](/f6bdc16ceadd474d895561e3c6762d42)**
❌ **Incorrect**. `ipconfig` command can be used to **configure the Internet Protocol layer** on your local computer and has nothing to do with domain names. For example, with `ipconfig /release` you can get rid off your IP address and with `ipconfig /renew` you can get a new one. Just **don’t** do `ipconfig /release` during a zoom call, otherwise your counterpart will have some questions. 🙂
✅ **Correct**. The DNS server is responsible for **mapping domain names to IP-addresses** and we can use the `nslookup << domain name >>` command to query the IP address of a domain by using the terminal.
![Using nslookup to query the IP-address of [unisg.ch](http://unisg.ch/) webpage](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c30fd7e9-9c93-41fd-957c-3637c155530b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665P3SQ7FK%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBl0AnFl5z9BKJvvkSzRvTJc6yUmXZfNMbYr4VB3RrAkAiBg2P009dKe7kjlDFJLZpFaW4KSpCbbm8AtkrhcZTfmhir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMz294DDiVOM3oJ5MPKtwDsW8dOF3R0V1mLjA3Jv%2B0iju42zyZwy1cXMFXUort%2BZPZJ7eL5bipKZKTVEW3J5D65gezoICFdckj7n04BCkMUIeeBrZ4SeOs%2Bk%2BNy6k2fUjkiuuZHR5k68gelI%2FOK6hJlV6yxunuA17Ydbv8mlsEmBm8q4cviqELapFsvbnxCrSLsLRwT4R6RO%2FGZOSIkVKlbHColyu64d8uXtCcd%2BD8XowpYQuyKmAycrXRdOKpErwtqzFZai%2F71MaBI71RYiTD%2FQ0f1u9rTMr6%2FMiMfyuMKF4rPntCkiKZZCmTWCif1gFMg1Y12sZD4sGTPan%2F7P5dW%2B2mci6wF6w9Le5UexL2lx9nKS5OyS8Dpry1x6JG%2BQ0fiJRqNt4Mtr%2B6TcuQ%2Bme1m1gxh875L6AmK8MCIqeL2OkPuDLTKmVSTT0CUlnWOsnyI1h6PkIQLD5hf5RccIkPyFJUl%2F9Tlhx0GFByK8%2BN8%2B2F2FD%2Bh6MpB5eqb0jbanTZFrEmneolimVhuHoa%2BRn%2F3eyiNme14NrobeM98ui%2B8eJbvJw%2FYFUFB6QqdRy7jtKtRAoMcpBHvw%2F2dzRQtJxe%2F3eOZeqdK81H%2BZy4oqpepDaVL3QeIrU3ojnmDyhwq2%2FL5vWGrJntYucMj6Mwx873yQY6pgGj14I1EqQMxO3FQfBz8QgNt9eCbLkaA1FJfJK6zFdF9qbFaAH7Y%2FsY7eQs4KI8FkBBCtSpQbpYFUwE5Hp%2FictqGGrVJHsEf%2FfZU7yaY699paDY4ONhlcoqdeDPo2HIoOr2RMIPId4nGz0DqrxeZ3vMGBIVqaYFZW%2FDAABpwh8Fs3hD7hr%2BQ7es6%2FzSyFxfq%2FxzJCMMRF%2BSFDl6OIb5%2BBpNbOxtmrea&X-Amz-Signature=6c18975e3d14ea895f4ff9cefce74e119462599f89a7e31475ff64cd896545af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
✅ **Correct**. When calling [http://example.org](http://example.org/) the **http protocol** is used. As we are requesting a resource from the example.org server (the webpage) our browser is sending an HTTP **GET **request.
❌ **Incorrect**. The address is found using the **DNS protocol** and the DNS protocol is part of the **application** layer.
</details>
---
## Question 3
Gegeben ist der folgende Code, der Teile von Assignment 6 implementiert.
```python
def find_restaurants (x, y, open_at, radius):
	url = 'https: //api.yelp.com/v3/businesses/search'
	restaurants = []
	params= {}
	params['latitude'] = x
	params['longitude'] = y
	params['openat'] = open_at
	params['radius'] = radius
	params['categories'] = "restaurants"
	r = requests.get(url, params=params, headers=headers)
```
Bitte markieren Sie **alle** richtigen Aussagen.
✅ Die Anfrage wird zu einem Autorisierungsfehler (*authorization failure*) führen - Sie müssen den API-Schlüssel (*API key*) angeben!
❌ Die Anfrage wird fehlschlagen, weil der Parameter *'city'* fehlt.
❌ Es gibt kein Problem mit dem Code, er wird funktionieren.
✅ Auf Wireshark würden Sie ein TLS-Paket sehen.

<details>
<summary>Explanation</summary>

> 💡 **[API requests](/b431f30ba0674f04a6c836035b69ea8e), [HTTPS](/923d77685b5c46518f7726145cfce814), [TLS](/923d77685b5c46518f7726145cfce814)**
✅ **Correct**. From the [API documentation](https://docs.developer.yelp.com/reference/v3_business_search) we can see that we must authenticate ourselves by providing an API key.
❌ **Incorrect**. From the [API documentation](https://docs.developer.yelp.com/reference/v3_business_search) we can see that there is actually no parameter city. We must provide **latitude** and **longitude **instead:
![Required parameters latitude and longitude](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fe685723-7f02-4a13-bc3e-b92ec8212ba7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJWI3DZE%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCYot348HNkGC7fhLjSyCh4jr5YrhtP9FBXPwG0KPHb%2BAIgcAdqbrYkwSmWpzuZ0vLq%2FBepnuqR5Lj6N5FVHEaHnvMq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIzxQ0rLKPH8zBfljCrcAxMSiDma6X7g8r6zZSidW9y1cwYqxs6b6me2ymED9FrswPCNIEm1HgW1%2FLxhnrSVsrvMTCY6tsw7CDI8LKndHRhaLsGKVTeU9hFVu9xqqM%2B4hwW%2F9AfG0%2BYReNAvFFUnQzNR02Cm9mL3x1TPEl6EQbCNxFr%2F0Ket7VEjnYBv4UaTU%2BvOAS%2BffbLto68oS9qMrVWMZYKlZ%2ByqdlXSBEqp4EOzWn%2BoMMqWcm64ICXQlVyS%2BF%2BaOaVEp%2BUcH%2By%2F0rztuchIQbHdHQgRxmMj86%2BKFyBrYn8Du%2FcR3szMsdBpyqvo%2BY4J6oFxNrLGXVjsgB3AJQjx5zFluWlzAuBU%2BHxPmaNPDenBPecT6t7Ej0aRLJT%2FAoWJTdoFe3B7AtpPcRuj6PP8W56RWO8NgJv6vPclonpFh5wi%2FttvcyE1tWO4V1CmxF6%2Bti6J%2BNsRRdBFGoN12Fec96VbI1UWSUu95PqYid8rwySlsiqbwe7rerSwjJXaV5p3q06F0DjW938ypVkJMDtbYNvNWKjQCDIyU1e2RWEIMomVjnC6us4Zm35KN4MOOcwXz3qIyaxX%2Fg2%2BqEoEFNJnoP%2BuHNouIdY8CeTgGbeEydhLyxBuNupPulW40QrXKN3cXDlfb%2BgrjQFeMN3O98kGOqUBMFYANPzZqFPA11JqfoInjbMx%2FkEw7QNxGlVZ7nai2mYnnp2fXywZVbQXntKGToeNT2NZSRvKJ9tR0QveOPoStnKVS2APCsvkYzhQc7R%2FXOU5oGYi2Zoz1b8WuaWmwdPc6%2FIdKyW%2FvdcCXIuYk7Wa0rDQiCUw5LtFPx0qgHFn6fSrTOMik6u7Sxh3fzLggLPT9QqGS9L2dfIIG7akyK3U1QaCDWV8&X-Amz-Signature=bd6eb802306518ebb0570d11aa6d7b02d1462c14ee61874f689c395e55315003&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. The API key is missing (see answer 1). 
✅ **Correct**. from the url we can see that the **https** protocol is used (`https://`) and the https protocol uses **TLS** to establish a secure connection on the **transport** layer.
</details>
---
## Question 4
Sie rufen im Webbrowser [https://example.org](https://example.org/) auf, während Sie die Pakete mit Wireshark verfolgen. Was würden Sie sehen?
❌ Der gesamte Netzwerkverkehr wird verschlüsselt, d.h., alle Anwendungs-, TCP- und IP-Pakete werden verschlüsselt, so dass ein Angreifer nicht einmal die Ziel-IP-Adresse kennt.
❌ Sie können sehen, dass eine HTTP-GET-Anfrage gesendet wird, aber die Ziel-IP-Adresse ist verschlüsselt, da wir ein sicheres Transportprotokoll verwenden.
✅ Sie können die IP- undTCP-Pakete sehen, aber die Anwendungsdaten innerhalb des TCP-Pakets sind TLS-verschlüsselt (Sie werden also nicht einmal wissen, ob es sich um HTTP handelt).
❌ Sie sehen, dass es sich um eine HTTP-Anfrage an eine URL handelt, aber das HTTP-Verb (GET) und der Anfrageinhalt sind verschlüsselt.

<details>
<summary>Explanation</summary>

> 💡 **[what ](/923d77685b5c46518f7726145cfce814#f0ce6a93e602411b84715ccf86bad894)[*actually*](/923d77685b5c46518f7726145cfce814#f0ce6a93e602411b84715ccf86bad894)[ is encrypted on each layer](/923d77685b5c46518f7726145cfce814#f0ce6a93e602411b84715ccf86bad894)**
❌ **Incorrect**. If we would encrypt everything we **couldn’t send our request over the internet** to [example.org](http://example.org/). Because the other entities in the network **could not see** to where the request / packet should be routed to. So even if https is used, not everything is encrypted and made invisible to others.
❌ **Incorrect**. The remote **IP address is visible**, even though the request is encrypted and secured. This is necessary so that the request can be routed to the right destination over the internet.
✅ **Correct**. The HTTP request is only relevant on the **application layer**, i.e., for our web browser and the [example.org](http://example.org/) server. However, the network **must not see** the HTTP request in order to know to where the request / packet should be routed to.
❌ **Incorrect**. As the previous answer (type of request (HTTP) not visible) is correct, this statement can’t be correct as well.
</details>
---
## Question 5
Gegeben ist der folgende Code, der Teile von Assignment 6 implementiert.
```python
def find_connection(origin, destination, departure_date, departure_time): 2
	url = 'http://transport.opendata.ch/v1/connections'
	params = {}
	params['from'] = origin
	params['to'] = destination
	params['time'] = departuretime
	r = requests.post(url, params = params) first_conn= r.json()['connections'][0]
	
	× = first_conn['to']['coordinate']['x']
	y = first_conn['to']['coordinate']['y']
	departure = first_conn['from']['departure']
	arrival = first_conn['to']['arrival']
	transport_means = first_conn['products']
```
Bitte markieren Sie **alle** richtigen Aussagen.
❌ Der Code ist in Ordnung. Er wird funktionieren.
❌ Die Anfrage wird zu einem Autorisierungsfehler (*authorization failure*) führen- Sie müssen den API-Schlüssel(*API key*) angeben!
✅ Das Abreisedatum (*departure date*) fehlt in den Anfrageparametern.
✅ Die Zeilen, die x und y aus der Antwort abrufen, sind falsch. Es sollte `first_conn['to'][station]['coordinate']['x']` bzw. `first_conn['to'][station]['coordinate']['y']` lauten.
✅ Die Anfrage wird fehlschlagen, da wir GET und nicht POST verwenden müssen.
❌ [opendata.ch](http://opendata.ch/) kann nur über HTTPS erreicht werden, daher wird die Anfrage fehlschlagen.

<details>
<summary>Explanation</summary>

> 💡 **[extracting data from API response](/b431f30ba0674f04a6c836035b69ea8e#10b666e3faee4c088aeeb9b30ee93a28)**
❌ **Incorrect**. Because statements 3, 4 and 5 are correct.
❌ **Incorrect**. Open data does not require an API key, otherwise it wouldn’t make sense to call themselves **open** data 🙂
✅ **Correct**. If we provide a value for the `time` parameter we must also provide a value for the `date` parameter.
✅ Correct. The example output in the [API documentation](https://transport.opendata.ch/docs.html#connections) shows that all information about the station is stored inside a sub-dictionary `station`:
![Example output from the /connections API](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/87eed5b4-a6db-4a5d-a62f-1bbe7c6cd8f2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIU77UYL%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDidSW%2FuTSTstN%2BW4HcEzAaeU9CSdoCXbP0gkNyzov2TwIgbCJMesrPTFhKpEnsR5ZjQr888Xtgt%2FZxr3hSJXkO3xQq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNt6JqtQDjs%2BmamFjyrcA%2BNytdZE%2FlTKzfGDWnG3hD%2Fg%2BjcJ%2FB3PonHg4FJis6FfRa0vO8WW6Vs5tnNGoNbNCLdLd705Zj3fd%2FOIffNRxv9v%2BLiBuBVcv2eEIw4PvZMyK0TjODI96MrB6xN96TuSfmLgGjUc8fe2FjJsnyABE8wKAylYaSbkigUNoOLcXcunboYxmK7TTNre8Qt1v9oZjb4WE9QxRIsMSRVsEzW9FnMZlktaalkCkLSyYWGKEn57EKGCKeVRJB%2BjqmT2F8tbG2atXEGPFSjkB4o8ZG%2FqUHFF67cEDKxGBQqXaST2jPv6OeHtyxd%2BPn%2F%2FLCcdZbclHPut9VQ6vDGc%2BGox4UbsJz0VQagcx8X4SR05wZ1tQ%2FKLYFIoDG9VSZrT6%2B3I4EcyMNpoujVk74WSfG2hSQ%2FbEawhsZtpPrlwyBWh0xNoJ0ugalj%2BI6J25JWRVmQ2KFzxtOe2nd%2FV7td%2FfYuUZKQzEHIVK1XApVd6iLSlXFUHlRSkwiXjjJnFdKohyQAynMw57a%2BBd7FF64xb418ZEH5z6BgzLHN6ARi0eVOHyv4sVKpo4BziDEU6vMoAkF1v4m%2BZxR29U88nSwW166ShH2GsN6aDHsL9ovoe%2F8FJ84C1qIy8lciMFMA2UMpVwVbyMLTO98kGOqUB3ulb3RuvClJNz9kI8gn7JC9Pb245V8dnKrl1HsJVKupum7XlQaLiABozSexl4ndQMjqPujjEmGr%2FRrBlnG3sGaNKl58t3aoUmiYTud3E%2FcgtdJwHbfY5GlQWd47pQDnK9PceXk4HwijmBL4t7vEO0Ezbu1tCtpL0R28BaCEJ9fXgJgSA5RLs99By4%2FSR0z2%2BrPKX3fSTM5xoj5kFb4OZiHNtZUoz&X-Amz-Signature=88d6c1dfd7f6c7b447590a4c9dd79431bc320f918753f1ae37c20fc8ea3f48f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. In the [API documentation](https://transport.opendata.ch/docs.html#connections)  we can see that the http protocol can be used:
![Example request URL to the /connections API](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2e088418-bd12-4539-a730-3e04a06915e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIU77UYL%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDidSW%2FuTSTstN%2BW4HcEzAaeU9CSdoCXbP0gkNyzov2TwIgbCJMesrPTFhKpEnsR5ZjQr888Xtgt%2FZxr3hSJXkO3xQq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNt6JqtQDjs%2BmamFjyrcA%2BNytdZE%2FlTKzfGDWnG3hD%2Fg%2BjcJ%2FB3PonHg4FJis6FfRa0vO8WW6Vs5tnNGoNbNCLdLd705Zj3fd%2FOIffNRxv9v%2BLiBuBVcv2eEIw4PvZMyK0TjODI96MrB6xN96TuSfmLgGjUc8fe2FjJsnyABE8wKAylYaSbkigUNoOLcXcunboYxmK7TTNre8Qt1v9oZjb4WE9QxRIsMSRVsEzW9FnMZlktaalkCkLSyYWGKEn57EKGCKeVRJB%2BjqmT2F8tbG2atXEGPFSjkB4o8ZG%2FqUHFF67cEDKxGBQqXaST2jPv6OeHtyxd%2BPn%2F%2FLCcdZbclHPut9VQ6vDGc%2BGox4UbsJz0VQagcx8X4SR05wZ1tQ%2FKLYFIoDG9VSZrT6%2B3I4EcyMNpoujVk74WSfG2hSQ%2FbEawhsZtpPrlwyBWh0xNoJ0ugalj%2BI6J25JWRVmQ2KFzxtOe2nd%2FV7td%2FfYuUZKQzEHIVK1XApVd6iLSlXFUHlRSkwiXjjJnFdKohyQAynMw57a%2BBd7FF64xb418ZEH5z6BgzLHN6ARi0eVOHyv4sVKpo4BziDEU6vMoAkF1v4m%2BZxR29U88nSwW166ShH2GsN6aDHsL9ovoe%2F8FJ84C1qIy8lciMFMA2UMpVwVbyMLTO98kGOqUB3ulb3RuvClJNz9kI8gn7JC9Pb245V8dnKrl1HsJVKupum7XlQaLiABozSexl4ndQMjqPujjEmGr%2FRrBlnG3sGaNKl58t3aoUmiYTud3E%2FcgtdJwHbfY5GlQWd47pQDnK9PceXk4HwijmBL4t7vEO0Ezbu1tCtpL0R28BaCEJ9fXgJgSA5RLs99By4%2FSR0z2%2BrPKX3fSTM5xoj5kFb4OZiHNtZUoz&X-Amz-Signature=bcbf57ff33b641ba2ca477c92dce4ba525d8802c80117f7bc8c1a05cada19d34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---

📄 **[Quiz 7]** (subpage)
## Question 1
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
## Question 2
Sie schreiben mit SQL genau **eine** syntaktisch korrekte und zu den Tabellenstrukturen passende **SQL UPDATE** Anfrage inkl. einer **WHERE** Bedingung.
Markieren Sie bitte **alle** korrekten Aussagen.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, können mit genau einer solchen Anfrage alle Tupel (*tuple*) der entsprechenden Tabelle verändert werden.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE **Bedingung, kann mit genau einer solchen Anfragegenau ein Tupel (tuple) der entsprechenden Tabelle verändert werden.
❌ Die **WHERE** Bedingung kann nur im Zusammenhang mit **SELECT** Abfragen genutzt werden, nicht jedoch mit **UPDATE** Anfragen.
❌ Unabhängig vom Tabelleninhalt, wird mit genau einer solchen Anfrage immer genau ein Tupel (tuple) der entsprechenden Tabelle verändert.
❌ Mit Hilfe der **WHERE** Bedingung lassen sich die zu aktualisierenden Tabellenspalten festlegen.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, kann mit genau einer solchen Anfrage auch gar kein Tupel (*tuple*)der entsprechendenTabelle verändert werden.

<details>
<summary>Explanation</summary>

> 💡 **[UPDATE](/9f266597386048dd9a967fd9fd8e4b89#3ebedba97a0549f3b646cef4edebfbc4), [SELECT](/9f266597386048dd9a967fd9fd8e4b89#f1c1f44f49aa4d76944c2d427c07c08f), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb)**
Let’s assume we are dealing with the same data table as in the previous question.
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
✅ **Correct**. It can be that the `WHERE` condition evaluates to **True** for **all records** (students in this case) in the table. Then, **all records** will get updated. 
For example, the following query overwrite the first name of all students to **Marco**, because all students have a last name that begins with a capital **S**. Thus, `WHERE LIKE "S%"` evaluates to **True** for **all** **records**
Query:
```sql
UPDATE
	student
SET
	first_name = "Marco"
WHERE
	last_name LIKE "S%"
```
Output:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | **Marco** | Schaunmesser | 1998-05-30 |
| 53450 | **Marco** | Sa | 1998-07-03 |
| 52819 | **Marco** | Schokoloski | 1999-11-30 |
| 52980 | **Marco** | Schaan | 1998-05-31 |
| 52791 | **Marco** | Schauviatt | 2001-11-11 |
✅ **Correct**. It can also be that the where condition evaluates to **True** for only **one record **in the table. Then, only this record will get updated.
For example, the following query overwrites the last name of Preston to **Braun**. Because there is only one student called Preston, thus `WHERE frist_name = "Preston"` evaluates to **True** for only **one record**.
Query:
```sql
UPDATE
	student
SET
	last_name = "Braun"
WHERE
	first_name = "Preston"
```
Output: 
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | **Braun** | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
❌ **Incorrect**. The first two answers show that a **WHERE** condition can be used in combination with both, **SELECT** and **UPDATE**.
❌ **Incorrect**. The first two answers show that the number of records that get modified depends on the **WHERE** condition. The condition can evaluate to **True** for any number of records. 
❌ **Incorrect**. With the **SET** keyword we define the columns that should be modified, i.e., in which column the new value should be inserted. With the **WHERE** keyword we select the records that should be affected by the update. And the two in combination give us back one or multiple single cells. Then, using **UPDATE**, the update is executed, i.e., the new value is inserted into the one or multiple cells that were selected by **SET** and **WHERE**.
![How UPDATE, SET AND WHERE work in combination](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c9113f15-ab06-407c-a276-4e90fa691d3e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YOMBO3P%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD0FRncX7PDAFmMXYLT0WcR3sVBRJeeJECjrR9LkhSSzgIgc6X8sgaSEk6803dbM80lC4B51wtaeGqT4cHjlvWQ5Wsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKuRBCpaVoRRcwvxYCrcA2TXaViddGDcZrDWYzinx9xlMjk%2Bdt%2FtaL8Vh74JVG5ov5mQfwme8bwngYBA%2BatdLdZd0lR93DhAwTF97ZUB534CyLku2u%2F6hZayLOk1czMKGg7MnuDiiu4wJB2x%2FXUK%2Bn7jMaEAmfjseZpTB1Naz9Q4I3Ki028BuHi5vpMTvNpFzmKZ8F6JTSU9b1AX9pW8HszB5lJ3C3sKuszIUQTZyyyeUdGmkTE6spMw0hzzClnmgkF9pVZiyTnqBYEo%2B7%2B2%2FvNJ8vzm21FJ5NqLZGDo9AR9XuNNVRgN3CxKil1ja6QTWF6%2FBy54by19IIMsUuLVxqG5yuEN08Z9m0oDh3z%2FI4Rri18bBi9KCgwAUR0h67agsomEifSnEdKhjoSkegh6QjHU6%2BGHOZ2uWI7OACwdMFzz8omPTBKwnoALfsqdQO%2FDUkgSQhMhrJjWQo4aMbQ1RmZwMOF7xBtVq7tyIcoA18fnN1BWlgA0a83dAcuMplwQa0YJZVICAE%2F68l8%2FymCYnsU6xUpba7vTpOgunRaKbis7axK5DOOzPFypt3c9D63Xx9EC5%2FFkVnLB0jmWOYrdUgBSDDc5e%2F3nOrnqYAzSSDXQePCsficLfdBUztoZOqSnOYilvyYMOBN1vpGvMITO98kGOqUB5zIeycXLDNdbElC0%2FgAqGoybnygSA5EDXPWNTlws7wJ7%2B06m6k6YZagGkDWt%2Bok3OZ0LHGR3SLf8%2B9Qg8jgr82T2%2B9HnpHNYyztcFDQD0EXK%2BXiasNfBIkD%2FlhsRrq5VOnx9oKF9%2B3kYUdiieI9eMj8XhKaXt8JjgE65BPXCZouA6H%2BJsMhYftaBraHN3iMcvsBFmMoQaXf1S%2FkE%2Fn%2FatmbWpcTB&X-Amz-Signature=0a59d40cd3976b7aebad67bb19a49d4ccfd81bd796b9da6b3952daa0ac3efa0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
✅ **Correct**. Of course it can also be that the **WHERE** condition does **not evaluate to True** for any record in the table. As a result, nothing changes.
For example, the following query aims to overwrite the first name to **Marco** for all students with a last name that starts with a capital **A**. However, as there is no student with a last name that starts with a capital **A**, `WHERE LIKE "A%"` evaluates to **False** for **all** **records** and nothing changes.
Query: 
```sql
UPDATE
	student
SET
	first_name = "Marco"
WHERE
	last_name LIKE "A%"
```
Output:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
</details>
---
## Question 3
Sie haben ein SQL-fähiges relationales Datenbanksystem.
Bitte markieren Sie für diesen Kontext alle korrekten Antworten.
❌ Die Abfrage **SELECT DISTINCT * FROM tabellenname** einer Tabelle **tabellenname** liefert immer weniger Tupel zurück als die Abfrage **SELECT * FROM tabellenname** der gleichen Tabelle.
✅ SQL-Injections helfen nie, SQL-Abfragen performant zuhalten, auch wenn diese in Python implementiert werden, welches ansonsten für seine eher langsame Ausführung bekannt ist.
✅ Die Anzahl, der von einer **SELECT** Abfrage zurückgegebenen Tupel, ist immer unabhängig davon, welche Storage- Engine gemäss ANSI-SPARC-Modell verwendet wird.
❌ In einer Datenbank gibt es die Tabelle **courses**. Der SQL- Befehl **SELECT *FROM courses LIMIT 10 **liefert dann immer genau 10 Tupel zurück.
❌ Die Tabellen **A** und **B** beinhalten jeweils drei Tupel. Dann gibt die SQL-Anfrage **SELECT * FROM A INNER JOIN B** ebenfalls genau drei Tupel zurück.

<details>
<summary>Explanation</summary>

> 💡 **[SELECT DISTINCT](/9f266597386048dd9a967fd9fd8e4b89#add7d3de22c14a809cb3c15bb7685bb4), [SELECT](/9f266597386048dd9a967fd9fd8e4b89#f1c1f44f49aa4d76944c2d427c07c08f), [LIMIT](/9f266597386048dd9a967fd9fd8e4b89#ca64b7e9f8c14563a40cd4d464dc5809), [INNER JOIN](/9f266597386048dd9a967fd9fd8e4b89#f3ac72183aeb4fe7b12ff4cf12928a64)**
Let’s assume we are dealing with the same data table as in the previous questions.
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
❌ **Incorrect**. If every entry in the table that is queried is unique, the two queries will return the exact same result. 
For example, in the data above **every student exists only once**, i.e., there are now duplicates. Thus, the two queries below will return the same number of records (5).
**Query 1**
```sql
SELECT DISTINCT *
FROM student
```

**Output 1**
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
**Query 2**
```sql
SELECT *
FROM student
```


**Output 2**
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
If there were two students with the same last name:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | **Schaunmesser** | 1998-05-30 |
| 53450 | Julio Quinton | **Schaunmesser** | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
Then the following queries would not return the same number of records.
**Query 1**
```sql
SELECT DISTINCT last_name
FROM student
```
**Output 1**
| last_name |
| --- |
| **Schaunmesser** |
| Schokoloski |
| Schaan |
| Schauviatt |

**Query 2**
```sql
SELECT last_name
FROM student
```

**Output 2**
| last_name |
| --- |
| **Schaunmesser** |
| **Schaunmesser** |
| Schokoloski |
| Schaan |
| Schauviatt |
✅ **Correct**. This does not depend on the programming language being used.
✅ **Correct**. Querying data **does not depend on the underlying data structure**. That’s exactly why the structured query language (SQL) is so popular as it can be used for multiple database architectures and technologies (e.g., mySQL, MongoDB, SQL Server, Databricks Lakehouse etc.)
❌ **Incorrect**. In case there are **less than 10 records** stored in the the **courses** table, the query will return all records that are available.
For example, the following query returns less than 10 records.
Query:
```sql
SELECT * FROM student
LIMIT 10
```
Output: 
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
This is because there are only 5 students, thus there is no need to filter out any records with `LIMIT 10` as there are fewer students anyway
❌ **Incorrect**. An **INNER JOIN** returns the **intersection** between two tables, i.e., the records that can be found in both tables.
Let’s assume we have the following table **student**:
| id | first_name | last_name | date_of_birth | course_id |
| --- | --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 | 1 |
| 53450 | Julio Quinton | Sa | 1998-07-03 | 2 |
| 52819 | Van | Schokoloski | 1999-11-30 | 4 |
And the following table **course**: 
| id | course_name | level |
| --- | --- | --- |
| 1 | Computer Science | bachelor |
| 2 | Statistics | bachelor |
| 3 | Finance Advanced | master |
By looking at column `course_id` in the **student** table we can see that Preston is enrolled in the Computer Science course, Julio in the Statistics course and for Van we don’t know as there is **no course with id 4** in the table **course**. Also, we can see that no student is enrolled in the course Finance Advanced.
If we now execute the following query, we will get back the intersection of the two tables. That is Preston and Julio as for both a course could be found in the **course** table.
Query:
```sql
SELECT student.first_name, student.last_name, course.course_name
FROM student
INNER JOIN 
	course
ON
	student.course_id = course.id 
```
Output:
| first_name | last_name | course_name | level |
| --- | --- | --- | --- |
| Preston Omer  | Schaunmesser | Computer Science | bachelor |
| Julio Quinton | Sa | Statistics | bachelor |
As you can see the output has **two** records, while the two tables **student** and **course **both have **three** records.
</details>
---
## Question 4
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

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9a3dd2fc-d3d3-4f80-a3d1-2525d393e718/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675YX5USD%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCLc8v2D9%2Fa6o0Yrx9d3zG3XChOAC7vMm6PlaS3D2%2FSawIgRRUSSpaPn9dzW1dQem4PeUDUUQXvwFe6qEasVpLY5%2Fkq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIzctvwGGn7JkR1UMSrcA6L0Uu9a2EKFRq%2FN5YL3tKpXmHCEHhh5qhpVaT34S0p5tQCEywSeSrZZ2HMfoIUilgDEAukZ2ZdxgSyHZOl%2BGI%2Fal5BRviu0F3lLqWZZYmVCmXnFr7Gu8tTF6uwd%2BYkOZv%2B1gyTZ6l6eNGL211J2Ha0fhs0bduG8lJLyIsIXmo%2FvKEwQmXrLs2%2B8Q%2BhrHngj65LmI%2FHsEf0VmTzNU0cMwJP4ZcGvbQXcQr5n%2BoEV1%2FXbnieyi2zU4pA2hPHRkhyXpCYlDTXp%2BKAxe02PZa5DIURAWOsSRejNqWu8Sb0WiXuMBquNm%2FL6wtgOUYYIA6xGam9AW1ZudguGfqCErrsnnDtJxBASjomkwRGrOLBaCX%2FdxABBnAKC9E7WKSXtbaCnOR6iZDoF4HrhdAMKiAVIRzLE%2FUn2rLqlbwT8a6sQgEjTZZrZDdmXwxA0ElICS8YzpqMEEhQ31VwxmgfzKlnqk7v%2BgJ0moZ7brdF%2B0NNfkXL0IB3e93aNVR%2BOWntYNneiEpxmzquTbxgNALeCnbrkP2iOECA8BIq%2FUPgLd6JxjZxDXsDoguCE4z7egAUEv1iJs2ZFH4KoqvzLJxMl6sd%2B5Hii49BaDtBAGG%2BsoERIKldfiOe76li8g6iXZOW2MPLO98kGOqUBFlmZZh5U%2BrW3wfk2zfj0VGOIiPN5b83u1RbIBgVcy1aQ9rd7Kvw6fgeEHRY9cTJlDXbGreI2LE2rQ86HM74yvzAV605jnuAVbMSgo1%2FXvu7ctD%2FjKhH%2FQyxdSkmrUR%2F7CFRvAJS%2Ff8ynT5pX5oLz1vVh88tYvqXzCG3PcEtRUOTLrQoS%2BolOuWs6t0Z41m6oj0TMUp9Njsp2N33whF4W%2BzuUiMit&X-Amz-Signature=25a35260eebc5f7b1226d0d39b3ce79c13aa8ac103c62ae2bb0b0101d2fcf7e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join **enrollments** with **courses** to know in which course category the grade was achieved.
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bb58391f-28e2-4b87-9dfa-efb93b3c38dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKICREF3%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDBKJBiUC%2BU%2BXWUDdClQQBcj5ToTRkLIHN06J9%2FiIRhIAIhAP%2FZglhVUY7M4EoOG4kfEq5edUIWE2PVZX4CBn6NseWcKv8DCCoQABoMNjM3NDIzMTgzODA1IgxxuC8s7b1luBkLZqUq3ANSAFwfMe%2FmqmsdF5jAMmrGfxP70Kwo4uiLKK%2B96kygnncS60l%2FG51JU%2FiDwCS1E0AreB0PXWiWJYZQ7%2F%2FfMNhG4WsuyOp0DFcnEYRahOzQSdUd7PKVJijeJzMkMoPOe9zNkBEsa2d%2BXvkC6OegUn0fj7mAmFOL8r43t8rcBMsxCwZnKjZT3rFD9p6P4ME9I09%2F7ShRCPxxlg8vw0AGSOOgc3Fk1Cw8c90g6NPv%2BY50YnrdvM05%2FwAeK7KwHPyZRAcqX6wqlawhLlkKIiOYoXsZLCfEM700ODd45Q7R%2FbdS1wxgrC1qZ%2B%2FnM9eD3Z50QGF3wQ0oyE6duxuxVz3MtanN3I%2BIxT95oQ%2Fea7o4vDjmyrDcjh8ZXEvLnNkJnPzVCYDraJUhj4AiCyB2uPRaGftCM24PzmMvRewHfUXQ22%2B1nfcPG7ldJoVbJEOty5BIN%2FaKa5fv2zemy%2FbLnFBltkOJDx6PC4eKLxaSzZNr5c5SGEE%2B8cviar5F9gIenMBBftBfStsoIj8LthQln8q4z9QDCqMS3HBX%2FZ7M96tEocJV0nwFoc%2BvCg%2FFRt3AwcNEqs7LITtHqPvIgKQn3o%2F0JuxTbAqg%2BrcbG35DaxZKr9VTQmRVjuaY6aL%2FtNzYLDCFlvjJBjqkAdRy5UCZbGTExMszD6ehDYAi74GjMdLMJwYnwsgxIQEu3jUWTmIrJDoaRnSfbWfaDmoDz44n6dcccgFHP2bmBiWk2TSI0R2ZseVZEsVMPddnWCZRC5ozQ2%2FHYUlAz56h8KkCNEgFuYrrWuCVmVSscm6RHxl9NPYfHlfhrmWN2d4o6hbwOgTWeAnzCDB9P3lyzL%2BjYG8rs2PC%2FdEooPnB8bYvKzGT&X-Amz-Signature=4a721694237d5f3cdd36cd3acb4d719a175ad87bbf985b775ae95ee54c046e4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/34d7ccd1-9629-46da-ab0a-5e19d5df29c6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V46C2V3N%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIBrKi9g%2Bd5SbdYWWcPcQ4Hzlmeg5tgxQD4xa9xwVvthoAiBfga6w7crHksnC3vzQb4Bhs78zab65xq%2BIjiXY4BuzvSr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMVq%2BG4wHlYphHWP6BKtwDI1j794COqaDQxniN2KNyzGcbbF%2BEQgWP5NgU%2BLB%2FBlDrFen3P3MOEymZL02mmW5E5Ao7A1Q8h6HKwlID8y5qGjxJxFQToEbFLvQ6MuVpMVcVpsrGf5NMFHAGRi97WImdayzAlMqgbO4W7el6fLUs4gb1gCKHyz5hcD9qqu1t0ZldiqRj3kkPtrv0WDy6EU25FV6PwPlzSPbfZUTC%2F1MCkUTAllX3T0%2BKXe4CpsmqKr7w7wP3JpESaF2qXFdlaldLIKmmYF8bQDj2sf4wO8jujcunnlT8FBuS4rJFn1o83VuDYcE4Ayb%2BIK4E%2Bxf0cqoZxRT7q3rqtW38nJvE9bb0KatSO%2BFc5F%2B50zrSlwvYj0CEegTtNO2FZoe2QWzFIzFQgmYdZpEbLm95kColgcPo%2F3TYSH4vG68kB0zEdusd11WdC8sjemegl8b%2FWuQgIPxHMirtnwPZ2pTkJzdQrE3v7m%2F438%2B0%2FCMf%2F%2Bp4uke5xtngqjLZvJ4E9B4YcfZ1pRl%2BJK68ThzVjX%2Fo325PC4UJ75p7Qodw1MmvbDo5e9Tq9QZ4GmZt0mENlmnK%2BbmKud9eFphIygmKEoU8ry60t%2F7Q3J%2BWxn1AuG%2Bmy6L4nFtms1HjHCm3rgxjDw6bkXMwpZb4yQY6pgHHbCrnRRPIz5sxhTUuiAHczCt1aRvGd8x%2F%2Bm30F%2FEuKEuzLI4KPmyPEJhAMB6J%2FrrGg2RDoqjelEwIJnbqzTkjNZk4vW069yTNkrLf6TtTJ54WhWIVknlCQY9Tda30OGZWLhl%2BF3Z1%2FzCoJ09ABxNwNlQ8%2FiAEZ3yySiLf5YxrWw%2FKMtuhli4sRk5X%2FdmpQwIZ%2Bu9GzrDpMCpuJBfmUkZksqhxoNAB&X-Amz-Signature=4ff30a213c7eeae00acb0e19227b20dd513e792c64b949f362fb9e7db02d25f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1966400c-2622-49f8-a0af-a4452434e8b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U35TDITK%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD4LUfPrmzsPYtdt8s1bxKgum1VvIkC6CgaVb8wBo2nEQIgO%2FkYeB%2FHPz7KWjfavf96t%2BGxtozDFZhR8P6SolOOK8wq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBv0G2VKFVLZcvfUrCrcA6Rvt4fUKWUOnrVCyE1zRMkMgSLxFdndQq0dBdtD5jr3cYlzVyE1L%2FfS8TnJFLFXcABbNb0%2FL6AWdUiNQYkgYr9Qelc06LoG7E%2BnqQdUjrz7ZajYU%2BYf%2FuSpjkFK7urpE%2BpoelqfJ5Vvx33lVGI73T4r3zgkWuE2Ukp2sgFngvCWSFNRS7PIYRq5BZOwjbVCm%2FsTEK0LFRTlKJugV3oe%2Fe0SBojQv9wk0oBqkwfqZfesw0YjWK64gk0xqwNJAFJfj5Sea6whXzWHol8Q74VRXhom%2FDYvFXNM9hRNTtkxJsLlpoq5yEvnrmU2PnoGekXb6VM7dxZzEK73FF2tvS056CLDsRbBrhi9M2bG%2FZ6%2BbKLo4I3seeiHd26yNzW7pG7jbAEWgDPDdUABh0d9hwiTdhqfULHwCJYeZGjdWpM6jkzyiWkQi6t8P20CjJjiBA45pdItuQidh7RNo3KQxFh0wq4ivJ6k6YRQpROj3LaN1ZnKCqsb5yUbkj6k%2BiTcQzM5PGIjueCwUa%2B0T0ixeZWE449A9u0UxSKw9JlwRJ8OeKLd%2FCt3ehCZnF8JPpt9YJLPBJEaf8xbnjpOJjxTPQdMZb5IRvEGGif%2BJ25%2BbNYlJW7WngW%2BfRsbMZeWvqH7MLHO98kGOqUBe%2Baz6OM687KrcRW32en7P36TuKqJG4VRS8xuJNQxUiv%2F0QD5FGdip1DBC%2FmIJy1sZKTRccjevwYNOq8BqRlzvG31KVpAT8PpoZd6ygQYyiS%2BnDkFuor04M1j2OCnJwknbTIWsyB5yEAuyJPowGunvkl366wn2Wh7SMXJRDcJC18FfrxsW7vXWfCA%2BuG8T97uS7QHuuPWEUwzdHMTCceqZgafTLAM&X-Amz-Signature=72d3b94efd5fbb5efcd9d6d80ce032ebddf14fd7a0c284eeef9670ebfa809d1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4508adda-64be-46b5-af4e-75e75a13807d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XRZADCR%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCICSAsC6Ha%2F32vegc1rBvC%2F5q%2B%2BfyEMLBNo8QsxHdJwywAiEA9OABSVn0NRHxhQKkxFyIVRZspVgAwLrD31EJwh8HIK8q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDD46N9TK%2F0ivI5fdGyrcA3ddmpNwe1ph40HdpkTEpkDORRKgBstg66oweaGE9phXE0T0rT6Odr%2FAfJNd2djYaeNigdun0Hf027ibOb78hpa02dP8IbpykIV0OLIxDV%2Fqz2Fb27xl%2BKFeqDUeUPkkW4ANsJxrxtxeYSWb3g84urL7S2eSdRZy4RoAXrbQSH8ec0ZTJlUmDHJpvL9CeooZICUF5D1SQYPWHVVXRn4GlZ3TcT6gYrsXB2NC%2Fh0qZdnxL6FtKsXqB%2FTu8NS49byHnbUc5E9o5SgO0FLjLCm%2FVMDPGl2C4PH%2BKdwfPb3T5XgW%2BkzKZMWqHn9geYrCvC3u7Wf0hp%2FhEmqOMRzykPuNPQ7QvYGZywn0zqaGj9J1elLyQIL157avKSf7qxB7cwfRST8gfmmPX2oHDVQ7CPUo58juYxTW9WAYstkFMK4cyzIpu082FGjglkY2yfaobdvmtsD%2BbBoTA3lokBv5bwLBRxNwoPpZqoYQnuH6RDMrwQ5PRJ79vJxqmuz6NCGQQiTXOIIhhEN0EMEE9giwMYb9fZLccxZT93ebY%2FEvQsF4cAWCFiP9uvCeaW0Ln6NTCN0eLIiGr9Ei1OY57O8zO8C9cOwhWoOnpyAclCMMGdW2%2Br66Z846kkse8aUQGEjnMJCW%2BMkGOqUB5nZVWBnZBJlFXc6WPfGH3%2FOuPTYZNjZ71M%2BrPlMYiPDFdrJPbfBVnCjNHGzpLRPNYwnNQjYAn%2FeMKObFBXyKtMqti4FNrIsCG07bgj077mW%2FxtHXFPQrW1TLFTZHCelDR5PQvArrXthU3xTyuakEKh7lwp%2BRRRtYO4QN%2BYg3IY3bczVx1StJhDapGoWKLSZXuMKIkkwd3uZYF%2FLSkV6AcwWgtwxM&X-Amz-Signature=dd960f577fee680f670d455ab054194858e7a5beaf5d3e37b94deadd4533d35c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
---

📄 **[Quiz 8]** (subpage)
# Question 1
Gegeben ist die pd.Series **x** wie folgt:
```python
0 1.0
1 2.0
2 7.0
3 NaN
4 2.0
   ...
72 3.0
73 23.0
74 3.0
75 23.0
76 3.0
Length: 77, dtype: float64
```
Die Auswertung von **x.sum()** ergibt 770.0
Markieren Sie alle Ausdrücke die fehlerfrei ausgeführt werden können UND wahr sind.
✅ Code snippet 1
```python
total=0
counter = 0
for f in x:
	if not np.isnan(f):
		counter =+ 1
		total =+ f
x.mean() == total / counter
```
✅ Code snippet 2
```python
x.mean() == x.sum() / x.count()
```
✅ Code snippet 3
```python
x.mean() == x.iloc[:len(x)].mean()
```
❌ Code snippet 4
```python
x.mean () == x.sum () / len (x)
```
❌ Code snippet 5
```python
x.mean() == x. iloc[1:].mean()
```
✅ Code snippet 6
```python
x.mean() == x.iloc[:].mean()
```

<details>
<summary>Explanation</summary>

> 💡 **[.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5), [.iloc[]](/1867045b058343e1a66b677961515907#659a00c8972e48a992e0dcabacb0cd4f), [.sum()](/1867045b058343e1a66b677961515907#6f1bd7bccbe24ecf8bcb37abc05b0550), [.count()](/1867045b058343e1a66b677961515907#8d4d0ed1fc114482978e4da5f21b429f), [for loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [.isnan()](/ccc5737dc7c64936bced118aca375cf9#2d995d983b82436a8d0af9d54c34d7ed), [len()](/5b0832dbf9454eb1941b7632e68a9abb#e097ab624af04d18b7f69088dff7d5f2)**
For simplicity, let’s assume we are dealing with the following series that is stored in **x**.
```python
0   1.0
1   2.0
2   4.0
3   6.0
4   10.0
Length: 5, dtype: float64
```
✅ **Correct**. Check the line-by-line execution below.
`total = 0`
`counter = 0`
`for f in x:` → `total = 23.0`, `counter = 5`
<details>
<summary>1st run → `total = 1.0`, `counter = 1`</summary>

`f = 1.0`
`if not np.isnan(f):` → `not np.isnan(1.0)` → `not False` → `True`
`counter = counter + 1` → `0 + 1` → `1`
`total = total + 1.0` → `0 + 1.0` → `1.0`
</details>
<details>
<summary>2nd run → `total = 3.0`, `counter = 2`</summary>

`f = 2.0`
`if not np.isnan(f):` → `not np.isnan(2.0)` → `not False` → `True`
`counter = counter + 1` → `1 + 1` → `2`
`total = total + 2.0` → `1.0 + 2.0` → `3.0`
</details>
<details>
<summary>3rd run → `total = 7.0`, `counter = 3`</summary>

`f = 4.0`
`if not np.isnan(f):` → `not np.isnan(4.0)` → `not False` → `True`
`counter = counter + 1` → `2 + 1` → `3`
`total = total + 4.0` → `3.0 + 4.0` → `7.0`
</details>
<details>
<summary>4th run → `total = 13.0`, `counter = 4`</summary>

`f = 6.0`
`if not np.isnan(f):` → `not np.isnan(6.0)` → `not False` → `True`
`counter = counter + 1` → `3 + 1` → `4`
`total = total + 6.0` → `7.0 + 6.0` → `13.0`
</details>
<details>
<summary>5th run → `total = 23.0`, `counter = 5`</summary>

`f = 10.0`
`if not np.isnan(f):` → `not np.isnan(10.0)` → `not False` → `True`
`counter = counter + 1` → `4 + 1` → `5`
`total = total + 10.0` → `13.0 + 10.0` → `23.0`
</details>
`x.mean() == total / counter` → `4.6 == 23.0 / 5` → `4.6 == 4.6` → `True`
✅ **Correct**. 
`x.mean()` returns the mean of the series → **4.6**
`x.sum()` returns the sum of the series → **23**
`x.count()` returns the number of elements in the series → **5**
`4.6 == 23 / 5` → ` 4.6 == 4.6` → **`True`** 
✅ **Correct**.
`x.mean()` returns the mean of the series → **4.6**
`x.iloc[:len(x)]` is equal to `x.iloc[:5]` which returns all elements in the series
`4.6 == x.iloc[:5].mean()` 
→ `4.6 == [1.0, 2.0, 4.0, 6.0, 10.0].mean()`
→ `4.6 == 4.6`
→ **`True`**
✅ **Correct**. (I don’t know why this is marked as incorrect in the solution).
`x.mean()` returns the mean of the series → **4.6**
`x.sum()` returns the sum of the series → **23**
`len(x)` returns the number of elements in the series → **5**
`4.6 == 23 / 5` → ` 4.6 == 4.6` → **`True`** 
❌ **Incorrect**.
`x.mean()` returns the mean of the series → **4.6**
`x.iloc[1:]` selects all elements after the first one in the series (**1.0** is excluded)
`4.6 == x.iloc[1:].mean()`
→ `4.6 == [2.0, 4.0, 6.0, 10.0].mean()`
→ `4.6 == 5.5` 
→ **`False`**
✅ **Correct**.
`x.mean()` returns the mean of the series → **4.6**
`x.iloc[:]` returns all elements in the series
`4.6 == x.iloc[:].mean()`
→ `4.6 == [1.0, 2.0, 4.0, 6.0, 10.0].mean()`
→ `4.6 == 4.6`
→ **`True`**
</details>
---
# Question 2
Gegeben ist eine *pd.Series ***s** deren Werte mit **np.arange(100)** erzeugt wurden und deren zugehörige Indizes im selben Aufruf mit **np.arange(100, 0, -1)** erzeugt wurden.
Was passiert nun, wenn wir folgenden Code ausführen:
**s[100] = 99**
❌ Es wird eine Fehlermeldung erzeugt, da nur die *Indizes* von 0 bis 99 existieren.
✅ Der erste Wert von **s** wird verändert.
❌ Bereits die Erstellung von **s** schlägt fehl, da die Anzahl derIndizes ungleich der Anzahl der Werte ist.
❌ Es wird eine Fehlermeldung erzeugt, da die Indizes nicht mehr eindeutig sind.
❌ Der letze Wert von **s** wird verändert.
Die Series hat nun einen zusätzlichen Wert, d.h. die Länge von **s** wurde um ein Elementerweitert.

<details>
<summary>Explanation</summary>

> 💡 **[.arange()](/ccc5737dc7c64936bced118aca375cf9#82ad4caa17294f6a89ccfeb254bcf289), [value assignment](/5b0832dbf9454eb1941b7632e68a9abb#e5cea5d982c844e28376879cb9c3a696)**
The command `np.arange(100, 0, -1)` creates the following numpy array:
```python
array([100,  99,  98,  97,  96,  95,  94,  93,  92,  91,  90,  89,  88,
        87,  86,  85,  84,  83,  82,  81,  80,  79,  78,  77,  76,  75,
        74,  73,  72,  71,  70,  69,  68,  67,  66,  65,  64,  63,  62,
        61,  60,  59,  58,  57,  56,  55,  54,  53,  52,  51,  50,  49,
        48,  47,  46,  45,  44,  43,  42,  41,  40,  39,  38,  37,  36,
        35,  34,  33,  32,  31,  30,  29,  28,  27,  26,  25,  24,  23,
        22,  21,  20,  19,  18,  17,  16,  15,  14,  13,  12,  11,  10,
         9,   8,   7,   6,   5,   4,   3,   2,   1])
```
We can see that an array in descending order from **100** to **1** is created. This is because we are applying a step size of **-1**. Thus, **100** is the **first** element to be **included** and **0** the **first** element to be **excluded**. 
However, for the index position nothing changes, meaning that the first element (**100**) is at index position **0** and the last one (**1**) at index position **99**.
✅ **Correct**. There is **no** index position 100. Python therefore returns an `IndexError`. I don’t know why this answer is market as incorrect in the solution. 😄
❌ **Incorrect**. An `IndexError` is returned.
❌ **Incorrect**. The `arange()` function takes care of that by creating a new array with the size that is necessary to store all elements between **[100, 1]**.
❌ **Incorrect**. Indizes are always **unique**, meaning that at one specific index position **only one **element can be stored. 
❌ **Incorrect**. An `IndexError` is returned.
❌ **Incorrect**. As we are using value assignment (square brackets `[]`) we are trying to **update an existing element** in the array and not adding a new one.
</details>
---
# Question 3
Gegeben ist folgender *pd.DataFrame* **df**. Die Spalte index ist definiert als der Index von **df**.
| index | value0 | value1 |
| --- | --- | --- |
| 2 | 701 | 411 |
| 21 | 483 | 26 |
| 8 | 897 | 62 |
| 6 | 327 | 8 |
| 29 | 458 | 164 |
| 4 | 34 | 652 |
| 11 | 810 | 961 |
| 14 | 432 | 492 |
| 34 | 422 | 307 |
Welcher Wert wird von folgendem Code zurückgegeben: **df.iloc[6][value1]**
961

<details>
<summary>Explanation</summary>

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#659a00c8972e48a992e0dcabacb0cd4f)**
`df.iloc[6]` returns the row with index position 6 as **Series**. In the DataFrame above, **row 11 **is at index position **6** (remember that the first row has index position **0**).
```python
value0    810
value1    961
Name: 11, dtype: int64
```
By adding `['value1']` we can access the value that is stored under **value1**.
Thus, `df.iloc[6]['value1']` returns **961**.
You can see that in the answer `[value1]` is used without putting the column label into **apostrophes**, thus Python would actually raise a `NameError` as there is **no variable** declared as `value1`. Thus, it is important to give `value1` as **string** into the selector → `'value1'`
</details>
---
# Question 4
In Assignment 8 haben wir aus der Datei movies.csv den pd.DataFrame **DF** geladen. Dieser enthält diverse Informationen über viele Filme. Wir nehmen an, dass er in der Spalte imdb score die Bewertung professioneller Kritiker auf einer Skala von 0 (schlechtester Wert) bis 10 (bester Wert) enthält und in der Spalte movie facebook likes die absolute Anzahl von Likes des Filmpublikums.
Hier wollen wir die Funktionen aus dem Assignment um eine weitere Funktion **top_x_overrated_movies** erweitern. Die Idee ist es herauszufinden, welche Filme von den professionellen Kritikern (im Vergleich zur Bewertung durch das Filmpublikum) besser bewertet (überbewertet, overrated) wurden. Die Funktion soll einige Details zu den Top x (also zum Beispiel den x=5 am meisten) überbewerteten Filmen auflisten. Wir haben diese Funktion wie folgt implementiert:
```python
def top_x_overrated_movies(×=5):
	df = DF.copy()
	
	df = df[df['movie_facebook_likes'] > 0]
	
	df['facebook_audience_score'] = (df['movie_facebook_likes'] / df['movie_facebook_likes'].max(axis=0)) * 10

	df['imdb_fb_ratio'] = df['imdb_score'] / df['facebook_audience_score']

	df = df.sort_values(by="imdb_fb_ratio", ascending=False)
	
	return df.head(x)
```

❌ In Zeile 23 müsste es **tail** (statt *head*) heissen, sonst stimmt die Sortierung nicht.
❌ Es ist nicht klar, mit welchem **DataFrame** wir eigentlich arbeiten, da wir mal df und mal DF nutzen, Python-Variablen aber **case sensitive** sind.
❌ Zeile 14 ist problematisch, da es keine Spalte **imdb_fb_ratio** in df oder DF gibt.
❌ In Zeile 10 sind die Klammern falschgesetzt, denn wir wollen ja die Multiplikation mit 10 in jede Zeile broadcasten.
✅ Dei Aussage ist falsch, denn tatsächlich funktioniert die vervollständigte Funktion wie beschrieben.
❌ Es werden nicht die **Top-x** der überbewerteten Filme zurückgegeben sondern faktisch immer die **Top-5**, da in Zeile 1 *x=5* fixiert wird.
❌ In Zeile 10 müsste es **axis=1**(statt axis=0) heissen, da wir nur eine Spalte selektieren und der *DataFrame* somit zu *pd.Series *wird.

<details>
<summary>Explanation</summary>

> 💡 **[.copy()](/1867045b058343e1a66b677961515907#3ee249c7635744768a6ac56eb7e7f728), [.sort_values()](/1867045b058343e1a66b677961515907#f4a6d6bc54ed4a2e885dd225270c2ccc), [optional parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc)**
To understand better what is happening let’s assume the DataFrame **DF** looks as follows:
![Simplified DataFrame DF](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4290dfdb-615f-4850-a456-ff3e1af2658a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZBK5YT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICu%2B2mUfG3Fmhf9MqwLv1DDKxMPPigEGUKQNe40SEJRNAiEAjbIywDtwoYj6tTT2feS9SqTJO0vvUfsiZp5MKlaWHf8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMQg3VJlAL2kL4hU9ircA790MxGi6t98sWPvamctcZarEJEIf%2FoOcaIsOflmaIfJviTduad7OpqhtyqR8PYioRk%2FBHl18DN5bMNB33SYC14AIqBK4ztT2QhbX6jkiy0vfCczC6VzEXc%2Fm4HBswuGJQQ7rxX37eAGfJpx25Hj9Lj4H3ldK3UYThFK8M8rsKptFE8%2FzyABM63dPXUF23cedGQl7A7gMDJoiWo6JIAJM8iPgXFF1vCiFlWE4ms7SVW%2FchB07Ra3i8hEnkBFL20T3J%2BEB6AKlnOkyFzWXyk5aeLzqo6sQTFn7mf%2Bgm4lftT%2B0O6xBMKepFVmcpyuvIbjW9YUga%2Bd6%2BONKAvXhiEGgaEJ4OwBhxAEDFdL5%2Bq9y1m0SQF3KuZ802LaU%2FhcvVSQ%2Fko3ZNMMdiyTJ3WLob1CynRsaCP46bkvXHBe7qOV5%2B1UxzOD5%2FTxNJkTGH8ojZm120eas5EsIZxnaZwxDd4G9EWsjc0DBbul6m6u%2FRTbQqJsb8loBx99l%2FzyHSAcFWaZ1qC5i%2B1%2B7ayTtcLXkSNNrnIrhPXLwgsNe96g%2BkPsmXWU9wuOpMY0FWvldZCPhe3B%2FflKWt7%2FRr7I0X3srArApI3UG8Ws0Z0V5AhyXjkjByKgPdySof1rQdvIbFOeMLLO98kGOqUByBgfU5v1x36XvN7UHu%2FtcbDZcovY6%2B74E9IcsoGoydaa%2Bajy%2BWyCpmHM5aurVmAvlPNUrVGMG3ulvBDIqjOyNlOGrXObjCivK2OxO5wB3iWWWFRYHFslBGnAoYbbj502zPPM3mDAaKyXBix8%2FlfT1mOAwnyE1fwGmfCDxLXyOAvAYd9Yw9OcXwUSSDOintjLwpc%2BzAny%2BKcv9f%2BCoT5nEhT21E4L&X-Amz-Signature=6f0667cf3907d3a69af0ad015a1d7b0f848f8f3bf6e91b0b0ff68919ec331d21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Let’s call the function `top_x_overrated_movies()` and see what happens line-by-line. Please note that because we are calling the function with no parameter value, the **default value** `x=5` is used.
Inside the function, first a copy of **DF** is created and stored in **df**. so that the original DataFrame **DF** is kept unchanged.
```python
df = DF.copy()
```
![Copied DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4290dfdb-615f-4850-a456-ff3e1af2658a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZBK5YT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICu%2B2mUfG3Fmhf9MqwLv1DDKxMPPigEGUKQNe40SEJRNAiEAjbIywDtwoYj6tTT2feS9SqTJO0vvUfsiZp5MKlaWHf8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMQg3VJlAL2kL4hU9ircA790MxGi6t98sWPvamctcZarEJEIf%2FoOcaIsOflmaIfJviTduad7OpqhtyqR8PYioRk%2FBHl18DN5bMNB33SYC14AIqBK4ztT2QhbX6jkiy0vfCczC6VzEXc%2Fm4HBswuGJQQ7rxX37eAGfJpx25Hj9Lj4H3ldK3UYThFK8M8rsKptFE8%2FzyABM63dPXUF23cedGQl7A7gMDJoiWo6JIAJM8iPgXFF1vCiFlWE4ms7SVW%2FchB07Ra3i8hEnkBFL20T3J%2BEB6AKlnOkyFzWXyk5aeLzqo6sQTFn7mf%2Bgm4lftT%2B0O6xBMKepFVmcpyuvIbjW9YUga%2Bd6%2BONKAvXhiEGgaEJ4OwBhxAEDFdL5%2Bq9y1m0SQF3KuZ802LaU%2FhcvVSQ%2Fko3ZNMMdiyTJ3WLob1CynRsaCP46bkvXHBe7qOV5%2B1UxzOD5%2FTxNJkTGH8ojZm120eas5EsIZxnaZwxDd4G9EWsjc0DBbul6m6u%2FRTbQqJsb8loBx99l%2FzyHSAcFWaZ1qC5i%2B1%2B7ayTtcLXkSNNrnIrhPXLwgsNe96g%2BkPsmXWU9wuOpMY0FWvldZCPhe3B%2FflKWt7%2FRr7I0X3srArApI3UG8Ws0Z0V5AhyXjkjByKgPdySof1rQdvIbFOeMLLO98kGOqUByBgfU5v1x36XvN7UHu%2FtcbDZcovY6%2B74E9IcsoGoydaa%2Bajy%2BWyCpmHM5aurVmAvlPNUrVGMG3ulvBDIqjOyNlOGrXObjCivK2OxO5wB3iWWWFRYHFslBGnAoYbbj502zPPM3mDAaKyXBix8%2FlfT1mOAwnyE1fwGmfCDxLXyOAvAYd9Yw9OcXwUSSDOintjLwpc%2BzAny%2BKcv9f%2BCoT5nEhT21E4L&X-Amz-Signature=6f0667cf3907d3a69af0ad015a1d7b0f848f8f3bf6e91b0b0ff68919ec331d21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Next, from the DataFrame **df** only the records (movies) are selected that have **more than 0 **facebook likes. Thus, the movies *Pirates of the Caribbean At World’s End*, *Star Wars*, *Spiderman 3*, *Superman returns*, *Quantum of Solace* are removed.
```python
df = df[df['movie_facebook_likes'] > 0]
```
![Updated DataFrame df containing only movies with more than 0 facebook likes](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/57961bc0-b6a5-45f4-a3b6-c3abcde37f6c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZBK5YT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICu%2B2mUfG3Fmhf9MqwLv1DDKxMPPigEGUKQNe40SEJRNAiEAjbIywDtwoYj6tTT2feS9SqTJO0vvUfsiZp5MKlaWHf8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMQg3VJlAL2kL4hU9ircA790MxGi6t98sWPvamctcZarEJEIf%2FoOcaIsOflmaIfJviTduad7OpqhtyqR8PYioRk%2FBHl18DN5bMNB33SYC14AIqBK4ztT2QhbX6jkiy0vfCczC6VzEXc%2Fm4HBswuGJQQ7rxX37eAGfJpx25Hj9Lj4H3ldK3UYThFK8M8rsKptFE8%2FzyABM63dPXUF23cedGQl7A7gMDJoiWo6JIAJM8iPgXFF1vCiFlWE4ms7SVW%2FchB07Ra3i8hEnkBFL20T3J%2BEB6AKlnOkyFzWXyk5aeLzqo6sQTFn7mf%2Bgm4lftT%2B0O6xBMKepFVmcpyuvIbjW9YUga%2Bd6%2BONKAvXhiEGgaEJ4OwBhxAEDFdL5%2Bq9y1m0SQF3KuZ802LaU%2FhcvVSQ%2Fko3ZNMMdiyTJ3WLob1CynRsaCP46bkvXHBe7qOV5%2B1UxzOD5%2FTxNJkTGH8ojZm120eas5EsIZxnaZwxDd4G9EWsjc0DBbul6m6u%2FRTbQqJsb8loBx99l%2FzyHSAcFWaZ1qC5i%2B1%2B7ayTtcLXkSNNrnIrhPXLwgsNe96g%2BkPsmXWU9wuOpMY0FWvldZCPhe3B%2FflKWt7%2FRr7I0X3srArApI3UG8Ws0Z0V5AhyXjkjByKgPdySof1rQdvIbFOeMLLO98kGOqUByBgfU5v1x36XvN7UHu%2FtcbDZcovY6%2B74E9IcsoGoydaa%2Bajy%2BWyCpmHM5aurVmAvlPNUrVGMG3ulvBDIqjOyNlOGrXObjCivK2OxO5wB3iWWWFRYHFslBGnAoYbbj502zPPM3mDAaKyXBix8%2FlfT1mOAwnyE1fwGmfCDxLXyOAvAYd9Yw9OcXwUSSDOintjLwpc%2BzAny%2BKcv9f%2BCoT5nEhT21E4L&X-Amz-Signature=45c0f4e03959b97cf9552ee90ab0e8951c78ec8ac5b9287138a0b418c8665e37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Next, a **new column** is added to the DataFrame which contains the number** 10** for the movie with the most facebook likes. The facebook likes for the other movies are then scaled in ratio to that movie.
`df['movie_facebook_likes'].max(axis=0)`
returns the highest value in column `movie_facebook_likes` 
→ `197000` (Batman v Superman)
`.max(axis=`**`0`**`)` → select highest value in column
`.max(axis=`**`1`**`)` → select highest value in row
```python
df['facebook_audience_score'] = (df['movie_facebook_likes'] / df['movie_facebook_likes'].max(axis=0)) * 10
```
![Updated DataFrame df with new column facebook_audience_score](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2a2d2196-7e79-4ca1-a7f4-de6a0924e86b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZBK5YT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICu%2B2mUfG3Fmhf9MqwLv1DDKxMPPigEGUKQNe40SEJRNAiEAjbIywDtwoYj6tTT2feS9SqTJO0vvUfsiZp5MKlaWHf8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMQg3VJlAL2kL4hU9ircA790MxGi6t98sWPvamctcZarEJEIf%2FoOcaIsOflmaIfJviTduad7OpqhtyqR8PYioRk%2FBHl18DN5bMNB33SYC14AIqBK4ztT2QhbX6jkiy0vfCczC6VzEXc%2Fm4HBswuGJQQ7rxX37eAGfJpx25Hj9Lj4H3ldK3UYThFK8M8rsKptFE8%2FzyABM63dPXUF23cedGQl7A7gMDJoiWo6JIAJM8iPgXFF1vCiFlWE4ms7SVW%2FchB07Ra3i8hEnkBFL20T3J%2BEB6AKlnOkyFzWXyk5aeLzqo6sQTFn7mf%2Bgm4lftT%2B0O6xBMKepFVmcpyuvIbjW9YUga%2Bd6%2BONKAvXhiEGgaEJ4OwBhxAEDFdL5%2Bq9y1m0SQF3KuZ802LaU%2FhcvVSQ%2Fko3ZNMMdiyTJ3WLob1CynRsaCP46bkvXHBe7qOV5%2B1UxzOD5%2FTxNJkTGH8ojZm120eas5EsIZxnaZwxDd4G9EWsjc0DBbul6m6u%2FRTbQqJsb8loBx99l%2FzyHSAcFWaZ1qC5i%2B1%2B7ayTtcLXkSNNrnIrhPXLwgsNe96g%2BkPsmXWU9wuOpMY0FWvldZCPhe3B%2FflKWt7%2FRr7I0X3srArApI3UG8Ws0Z0V5AhyXjkjByKgPdySof1rQdvIbFOeMLLO98kGOqUByBgfU5v1x36XvN7UHu%2FtcbDZcovY6%2B74E9IcsoGoydaa%2Bajy%2BWyCpmHM5aurVmAvlPNUrVGMG3ulvBDIqjOyNlOGrXObjCivK2OxO5wB3iWWWFRYHFslBGnAoYbbj502zPPM3mDAaKyXBix8%2FlfT1mOAwnyE1fwGmfCDxLXyOAvAYd9Yw9OcXwUSSDOintjLwpc%2BzAny%2BKcv9f%2BCoT5nEhT21E4L&X-Amz-Signature=f76d6de8400797f148df9ab3d890cb44084f158934457a3043ea2e99dad0867f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Next, another column is added to the DataFrame which stores the **ratio** between the imbd score and the facebook score. The **higher** the value in **imdb_fb_ratio** is, the **more** imdb and the facebook audience disagree.
```python
df['imdb_fb_ratio'] = df['imdb_score'] / df['facebook_audience_score']
```
![Updated DataFrame df with new column imdb_fb_ratio](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3486a0e8-d8aa-44b2-b767-c3fb85bb80dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZBK5YT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICu%2B2mUfG3Fmhf9MqwLv1DDKxMPPigEGUKQNe40SEJRNAiEAjbIywDtwoYj6tTT2feS9SqTJO0vvUfsiZp5MKlaWHf8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMQg3VJlAL2kL4hU9ircA790MxGi6t98sWPvamctcZarEJEIf%2FoOcaIsOflmaIfJviTduad7OpqhtyqR8PYioRk%2FBHl18DN5bMNB33SYC14AIqBK4ztT2QhbX6jkiy0vfCczC6VzEXc%2Fm4HBswuGJQQ7rxX37eAGfJpx25Hj9Lj4H3ldK3UYThFK8M8rsKptFE8%2FzyABM63dPXUF23cedGQl7A7gMDJoiWo6JIAJM8iPgXFF1vCiFlWE4ms7SVW%2FchB07Ra3i8hEnkBFL20T3J%2BEB6AKlnOkyFzWXyk5aeLzqo6sQTFn7mf%2Bgm4lftT%2B0O6xBMKepFVmcpyuvIbjW9YUga%2Bd6%2BONKAvXhiEGgaEJ4OwBhxAEDFdL5%2Bq9y1m0SQF3KuZ802LaU%2FhcvVSQ%2Fko3ZNMMdiyTJ3WLob1CynRsaCP46bkvXHBe7qOV5%2B1UxzOD5%2FTxNJkTGH8ojZm120eas5EsIZxnaZwxDd4G9EWsjc0DBbul6m6u%2FRTbQqJsb8loBx99l%2FzyHSAcFWaZ1qC5i%2B1%2B7ayTtcLXkSNNrnIrhPXLwgsNe96g%2BkPsmXWU9wuOpMY0FWvldZCPhe3B%2FflKWt7%2FRr7I0X3srArApI3UG8Ws0Z0V5AhyXjkjByKgPdySof1rQdvIbFOeMLLO98kGOqUByBgfU5v1x36XvN7UHu%2FtcbDZcovY6%2B74E9IcsoGoydaa%2Bajy%2BWyCpmHM5aurVmAvlPNUrVGMG3ulvBDIqjOyNlOGrXObjCivK2OxO5wB3iWWWFRYHFslBGnAoYbbj502zPPM3mDAaKyXBix8%2FlfT1mOAwnyE1fwGmfCDxLXyOAvAYd9Yw9OcXwUSSDOintjLwpc%2BzAny%2BKcv9f%2BCoT5nEhT21E4L&X-Amz-Signature=e2e1d519a2bb0c3610be46ebecc9362690d53e5cb667c97e46ebd7492ccef202&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
To identify the **top x (5)** movies for which the facebook audience and imdb **disagree**, the values must be sorted in **descending** order:
```python
df = df.sort_values(by="imdb_fb_ratio", ascending=False)
```
![Sorted DataFrame df in descending order based on column imdb_fb_ratio](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c9b50c6c-c2f1-49a7-b632-df0fb399c1ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZBK5YT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICu%2B2mUfG3Fmhf9MqwLv1DDKxMPPigEGUKQNe40SEJRNAiEAjbIywDtwoYj6tTT2feS9SqTJO0vvUfsiZp5MKlaWHf8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMQg3VJlAL2kL4hU9ircA790MxGi6t98sWPvamctcZarEJEIf%2FoOcaIsOflmaIfJviTduad7OpqhtyqR8PYioRk%2FBHl18DN5bMNB33SYC14AIqBK4ztT2QhbX6jkiy0vfCczC6VzEXc%2Fm4HBswuGJQQ7rxX37eAGfJpx25Hj9Lj4H3ldK3UYThFK8M8rsKptFE8%2FzyABM63dPXUF23cedGQl7A7gMDJoiWo6JIAJM8iPgXFF1vCiFlWE4ms7SVW%2FchB07Ra3i8hEnkBFL20T3J%2BEB6AKlnOkyFzWXyk5aeLzqo6sQTFn7mf%2Bgm4lftT%2B0O6xBMKepFVmcpyuvIbjW9YUga%2Bd6%2BONKAvXhiEGgaEJ4OwBhxAEDFdL5%2Bq9y1m0SQF3KuZ802LaU%2FhcvVSQ%2Fko3ZNMMdiyTJ3WLob1CynRsaCP46bkvXHBe7qOV5%2B1UxzOD5%2FTxNJkTGH8ojZm120eas5EsIZxnaZwxDd4G9EWsjc0DBbul6m6u%2FRTbQqJsb8loBx99l%2FzyHSAcFWaZ1qC5i%2B1%2B7ayTtcLXkSNNrnIrhPXLwgsNe96g%2BkPsmXWU9wuOpMY0FWvldZCPhe3B%2FflKWt7%2FRr7I0X3srArApI3UG8Ws0Z0V5AhyXjkjByKgPdySof1rQdvIbFOeMLLO98kGOqUByBgfU5v1x36XvN7UHu%2FtcbDZcovY6%2B74E9IcsoGoydaa%2Bajy%2BWyCpmHM5aurVmAvlPNUrVGMG3ulvBDIqjOyNlOGrXObjCivK2OxO5wB3iWWWFRYHFslBGnAoYbbj502zPPM3mDAaKyXBix8%2FlfT1mOAwnyE1fwGmfCDxLXyOAvAYd9Yw9OcXwUSSDOintjLwpc%2BzAny%2BKcv9f%2BCoT5nEhT21E4L&X-Amz-Signature=7c00eb608fbe43f24559b17c1675a42bf87367bbe916cf95da98df037404a95c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Finally, to return the **top x (5) overrated movies** the** first x (5) rows** in the sorted DataFrame must be selected and then returned to the function caller.
```python
return df.head(5)
```
![Final DataFrame containing the top 5 overrated movies is returned to the function caller](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6bbdbd4b-844c-4521-90b8-51f0369547a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZBK5YT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICu%2B2mUfG3Fmhf9MqwLv1DDKxMPPigEGUKQNe40SEJRNAiEAjbIywDtwoYj6tTT2feS9SqTJO0vvUfsiZp5MKlaWHf8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMQg3VJlAL2kL4hU9ircA790MxGi6t98sWPvamctcZarEJEIf%2FoOcaIsOflmaIfJviTduad7OpqhtyqR8PYioRk%2FBHl18DN5bMNB33SYC14AIqBK4ztT2QhbX6jkiy0vfCczC6VzEXc%2Fm4HBswuGJQQ7rxX37eAGfJpx25Hj9Lj4H3ldK3UYThFK8M8rsKptFE8%2FzyABM63dPXUF23cedGQl7A7gMDJoiWo6JIAJM8iPgXFF1vCiFlWE4ms7SVW%2FchB07Ra3i8hEnkBFL20T3J%2BEB6AKlnOkyFzWXyk5aeLzqo6sQTFn7mf%2Bgm4lftT%2B0O6xBMKepFVmcpyuvIbjW9YUga%2Bd6%2BONKAvXhiEGgaEJ4OwBhxAEDFdL5%2Bq9y1m0SQF3KuZ802LaU%2FhcvVSQ%2Fko3ZNMMdiyTJ3WLob1CynRsaCP46bkvXHBe7qOV5%2B1UxzOD5%2FTxNJkTGH8ojZm120eas5EsIZxnaZwxDd4G9EWsjc0DBbul6m6u%2FRTbQqJsb8loBx99l%2FzyHSAcFWaZ1qC5i%2B1%2B7ayTtcLXkSNNrnIrhPXLwgsNe96g%2BkPsmXWU9wuOpMY0FWvldZCPhe3B%2FflKWt7%2FRr7I0X3srArApI3UG8Ws0Z0V5AhyXjkjByKgPdySof1rQdvIbFOeMLLO98kGOqUByBgfU5v1x36XvN7UHu%2FtcbDZcovY6%2B74E9IcsoGoydaa%2Bajy%2BWyCpmHM5aurVmAvlPNUrVGMG3ulvBDIqjOyNlOGrXObjCivK2OxO5wB3iWWWFRYHFslBGnAoYbbj502zPPM3mDAaKyXBix8%2FlfT1mOAwnyE1fwGmfCDxLXyOAvAYd9Yw9OcXwUSSDOintjLwpc%2BzAny%2BKcv9f%2BCoT5nEhT21E4L&X-Amz-Signature=a335c4ac91ebe625294e295005369914ae373b27184d03f1a95ef0d593c47447&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we can see the code works as intended.
</details>
---
# Question 5
Gegeben ist ein *pd.DataFrame* **df**, sowie der folgende Code:
**x = df.loc[42]**
Markieren Sie alle richtigen Aussagen.
✅ Die Variable **x **kann nach der Ausführung des Codes den Datentyp *pd.Series* haben.
❌ Der Datentyp von **x** kann von der Anzahl Spalten von **df** abhängen.
✅ Die Codeausführung kann mit einem Fehler abbrechen.
❌ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *int* haben.
❌ DieVariable **x** kann nach der Ausführung des Codes den Datentyp *string* haben.
❌ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *float64* haben.
✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *pd.DataFrame* haben.
❌ Der Datentyp von **x** kann vom Inhalt der *NICHT-Index*-Werte von **df** abhängen.
✅ Der Datentyp von **x** kann vom Inhalt der *Index*-Werte (*label*) von **df** abhängen.
✅ Die Auswertung von **x.sum() **kann eine Gleitkommazahl (z.B. 6.2) ergeben.

<details>
<summary>Explanation</summary>

> 💡 **[.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.sum()](/1867045b058343e1a66b677961515907#6f1bd7bccbe24ecf8bcb37abc05b0550)**
✅ **Correct**. If there is only **one row** with index label 42, `df.loc[42]` will return a Series.
For example, if we have the following DataFrame: 
![Example DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2142b4f1-fcb5-4540-b3c8-76840cdbf1a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNJWAC7L%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIDa533Z93PvOBiSaTPv42xIzcWh4brz7pPzJU4aYAVlVAiEAz283I7mlG0dr1wqaSsfjmpPIug4o5WAUCiUAEQEoMJcq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDN48iMPAKG5WnoPtpCrcAwkuzhHGP6tOVhaWP6W%2Fw%2BuDS0DWsvtjaj13iaF7F2mdbgXYGK676hbgRipU5Xrskh25aAYA2Ynmh%2FwnPO5%2FNeGd4UO%2B%2FB4iy1YkCKzh350PhAQHcDBs0xZdj0FSXAFxJaJZXdP5omyxZLpLImpA3LbU5e8OUeyuCLfSvv%2Fxoj6K7YD0XoUDiDlV4Ct7t1NBdwK4AfNafvAP0noY0zDfyf3gZLzjRhHREUeMCVYdwRui8pIyJ6otXLoZdzhiSaVT5iSqr%2Bak6UKCXc%2Fps79ma5sIAu2iMe1sLEHUaXMfD8mctjI453pRF%2BdOOS09SUVwIdKaJfPikaOws4sESdTUS%2BU5oVk96KA%2BUjaeGnSpFGvmoZcMVQK0LlblKuLdQ6VZfJcIuXNOXp8Ef7vHU04N5VAvENENP7so0VZdwQQBWfe3kmPi945rF8JuYcd8bqJNnWMiOHAsK0ZAOB5UoYY42KIbAl6JsiyjEuXD53BD7eHS%2F5PjiRn%2FB9W0xh1TIP4ks%2BA0YyeqCGdYRQ%2FF%2BljGnA%2BHKv7BX%2FbgCGmfefQl8DBmkoZ3aNz3jW02eM1aVb0aDedbDpePYmFu02jIpnm6n1apxrLtjunOC7ESGeGXVonjeW03kQ5%2BUE77x9ExMJ2W%2BMkGOqUBbBnqSfooSKpd224nQwOAx%2BS4UocDOtt90IR%2FLac2JuLowAFT7HGH%2Bjid08R8ed3yYGENXXOhCsEck2dlAUvaPsVzwje1Rpe%2FVj2eDy4pduNa8V9RkZVj%2FY4IBvqQLOA6vG%2B95GqfPGjN%2B9A6Qk%2BWzRpbNzw0qtr3tAc%2BVD%2B5h0d%2BuB5yyQ6QKCM3sVOV4KTrACUng%2FN5%2BP83Cg8tAkQjUZvToe7b&X-Amz-Signature=09cbe327e7a62d3b63f222f6fbea1182f0549887ec59d73fe98e2404d4fb0908&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we do `df.loc[42]`, then the result will be a **Series** as only the first row has the index label **42**.
```python
value1    5
value2    6
Name: 42, dtype: int64
```
❌ **Incorrect**. Does not depend on the number of columns there are. `.loc[]` is a row-wise selector, meaning it selects data from a DataFrame by the **index labels** and not by the column labels.
❌ **Incorrect**. `.loc[]` will always return a Series or a DataFrame.
❌ **Incorrect**. `.loc[]` will always return a Series or a DataFrame.
❌ **Incorrect**. `.loc[]` will always return a Series or a DataFrame.
✅ **Correct**. If there are multiple rows with index label **42**, `df.loc[42]` will return a DataFrame.
For example, if we have the following DataFrame: 
![Example DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/58bb62ce-4582-4538-81dd-f048a0eb0441/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNJWAC7L%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIDa533Z93PvOBiSaTPv42xIzcWh4brz7pPzJU4aYAVlVAiEAz283I7mlG0dr1wqaSsfjmpPIug4o5WAUCiUAEQEoMJcq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDN48iMPAKG5WnoPtpCrcAwkuzhHGP6tOVhaWP6W%2Fw%2BuDS0DWsvtjaj13iaF7F2mdbgXYGK676hbgRipU5Xrskh25aAYA2Ynmh%2FwnPO5%2FNeGd4UO%2B%2FB4iy1YkCKzh350PhAQHcDBs0xZdj0FSXAFxJaJZXdP5omyxZLpLImpA3LbU5e8OUeyuCLfSvv%2Fxoj6K7YD0XoUDiDlV4Ct7t1NBdwK4AfNafvAP0noY0zDfyf3gZLzjRhHREUeMCVYdwRui8pIyJ6otXLoZdzhiSaVT5iSqr%2Bak6UKCXc%2Fps79ma5sIAu2iMe1sLEHUaXMfD8mctjI453pRF%2BdOOS09SUVwIdKaJfPikaOws4sESdTUS%2BU5oVk96KA%2BUjaeGnSpFGvmoZcMVQK0LlblKuLdQ6VZfJcIuXNOXp8Ef7vHU04N5VAvENENP7so0VZdwQQBWfe3kmPi945rF8JuYcd8bqJNnWMiOHAsK0ZAOB5UoYY42KIbAl6JsiyjEuXD53BD7eHS%2F5PjiRn%2FB9W0xh1TIP4ks%2BA0YyeqCGdYRQ%2FF%2BljGnA%2BHKv7BX%2FbgCGmfefQl8DBmkoZ3aNz3jW02eM1aVb0aDedbDpePYmFu02jIpnm6n1apxrLtjunOC7ESGeGXVonjeW03kQ5%2BUE77x9ExMJ2W%2BMkGOqUBbBnqSfooSKpd224nQwOAx%2BS4UocDOtt90IR%2FLac2JuLowAFT7HGH%2Bjid08R8ed3yYGENXXOhCsEck2dlAUvaPsVzwje1Rpe%2FVj2eDy4pduNa8V9RkZVj%2FY4IBvqQLOA6vG%2B95GqfPGjN%2B9A6Qk%2BWzRpbNzw0qtr3tAc%2BVD%2B5h0d%2BuB5yyQ6QKCM3sVOV4KTrACUng%2FN5%2BP83Cg8tAkQjUZvToe7b&X-Amz-Signature=3085fe35a7b4b707f0433f12cb97ae0527bb3184e703365519b98e1253d78453&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we do `df.loc[42]`, then the result will be a **DataFrame** as the first and the third row have the index label **42**.
![Output of `df.loc[42]`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/79b591db-0f3b-41d2-ab52-6b47f480b5ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNJWAC7L%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIDa533Z93PvOBiSaTPv42xIzcWh4brz7pPzJU4aYAVlVAiEAz283I7mlG0dr1wqaSsfjmpPIug4o5WAUCiUAEQEoMJcq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDN48iMPAKG5WnoPtpCrcAwkuzhHGP6tOVhaWP6W%2Fw%2BuDS0DWsvtjaj13iaF7F2mdbgXYGK676hbgRipU5Xrskh25aAYA2Ynmh%2FwnPO5%2FNeGd4UO%2B%2FB4iy1YkCKzh350PhAQHcDBs0xZdj0FSXAFxJaJZXdP5omyxZLpLImpA3LbU5e8OUeyuCLfSvv%2Fxoj6K7YD0XoUDiDlV4Ct7t1NBdwK4AfNafvAP0noY0zDfyf3gZLzjRhHREUeMCVYdwRui8pIyJ6otXLoZdzhiSaVT5iSqr%2Bak6UKCXc%2Fps79ma5sIAu2iMe1sLEHUaXMfD8mctjI453pRF%2BdOOS09SUVwIdKaJfPikaOws4sESdTUS%2BU5oVk96KA%2BUjaeGnSpFGvmoZcMVQK0LlblKuLdQ6VZfJcIuXNOXp8Ef7vHU04N5VAvENENP7so0VZdwQQBWfe3kmPi945rF8JuYcd8bqJNnWMiOHAsK0ZAOB5UoYY42KIbAl6JsiyjEuXD53BD7eHS%2F5PjiRn%2FB9W0xh1TIP4ks%2BA0YyeqCGdYRQ%2FF%2BljGnA%2BHKv7BX%2FbgCGmfefQl8DBmkoZ3aNz3jW02eM1aVb0aDedbDpePYmFu02jIpnm6n1apxrLtjunOC7ESGeGXVonjeW03kQ5%2BUE77x9ExMJ2W%2BMkGOqUBbBnqSfooSKpd224nQwOAx%2BS4UocDOtt90IR%2FLac2JuLowAFT7HGH%2Bjid08R8ed3yYGENXXOhCsEck2dlAUvaPsVzwje1Rpe%2FVj2eDy4pduNa8V9RkZVj%2FY4IBvqQLOA6vG%2B95GqfPGjN%2B9A6Qk%2BWzRpbNzw0qtr3tAc%2BVD%2B5h0d%2BuB5yyQ6QKCM3sVOV4KTrACUng%2FN5%2BP83Cg8tAkQjUZvToe7b&X-Amz-Signature=5948a1426ceae6f0c37b5df208cd1ecea9744a6f59043ca177eb9aeff2157bb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. As `.loc[]` is a row-wise selector, meaning it selects data from a DataFrame by the **index labels**, its output always depends on the values in the index column.
✅ **Correct.** As seen in [statement 1](/6da39bd8ae5b48f89afb46080f1fe947) and [statement 6](/6da39bd8ae5b48f89afb46080f1fe947), based on **how many times** the number **42** appears in the index column the data type of the return value **can vary**.
✅ **Correct**. `x.sum()` sums up the values in each column for the row with the index label **42**, i.e., that were selected by `df.loc[42]`. If the values in the DataFrame are **floats**, then the result of `x.sum()` will be a **float** value as well.
For example, let’s assume we have the following DataFrame:
![Example DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a6a5c483-92c9-40c1-bd03-ac7db58b2b10/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNJWAC7L%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIDa533Z93PvOBiSaTPv42xIzcWh4brz7pPzJU4aYAVlVAiEAz283I7mlG0dr1wqaSsfjmpPIug4o5WAUCiUAEQEoMJcq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDN48iMPAKG5WnoPtpCrcAwkuzhHGP6tOVhaWP6W%2Fw%2BuDS0DWsvtjaj13iaF7F2mdbgXYGK676hbgRipU5Xrskh25aAYA2Ynmh%2FwnPO5%2FNeGd4UO%2B%2FB4iy1YkCKzh350PhAQHcDBs0xZdj0FSXAFxJaJZXdP5omyxZLpLImpA3LbU5e8OUeyuCLfSvv%2Fxoj6K7YD0XoUDiDlV4Ct7t1NBdwK4AfNafvAP0noY0zDfyf3gZLzjRhHREUeMCVYdwRui8pIyJ6otXLoZdzhiSaVT5iSqr%2Bak6UKCXc%2Fps79ma5sIAu2iMe1sLEHUaXMfD8mctjI453pRF%2BdOOS09SUVwIdKaJfPikaOws4sESdTUS%2BU5oVk96KA%2BUjaeGnSpFGvmoZcMVQK0LlblKuLdQ6VZfJcIuXNOXp8Ef7vHU04N5VAvENENP7so0VZdwQQBWfe3kmPi945rF8JuYcd8bqJNnWMiOHAsK0ZAOB5UoYY42KIbAl6JsiyjEuXD53BD7eHS%2F5PjiRn%2FB9W0xh1TIP4ks%2BA0YyeqCGdYRQ%2FF%2BljGnA%2BHKv7BX%2FbgCGmfefQl8DBmkoZ3aNz3jW02eM1aVb0aDedbDpePYmFu02jIpnm6n1apxrLtjunOC7ESGeGXVonjeW03kQ5%2BUE77x9ExMJ2W%2BMkGOqUBbBnqSfooSKpd224nQwOAx%2BS4UocDOtt90IR%2FLac2JuLowAFT7HGH%2Bjid08R8ed3yYGENXXOhCsEck2dlAUvaPsVzwje1Rpe%2FVj2eDy4pduNa8V9RkZVj%2FY4IBvqQLOA6vG%2B95GqfPGjN%2B9A6Qk%2BWzRpbNzw0qtr3tAc%2BVD%2B5h0d%2BuB5yyQ6QKCM3sVOV4KTrACUng%2FN5%2BP83Cg8tAkQjUZvToe7b&X-Amz-Signature=763bc985f50e56e309f5d2a437aa445ea52926fdf9f6351c911ee0d4b4536882&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we execute `x = df.loc[42]`:
```python
value1    5.2
value2    6.7
Name: 42, dtype: float64
```
Finally, we sum up the values by executing `x.sum()`:
**11.9**
We can see that the result is 11.9 → a float
</details>
---

📄 **[Quiz 9]** (subpage)
# Question 1
Gegeben sind zwei pd.DataFrame-Objekte ORDERS und PERSONS.
Die Ausführung folgender Code-Zeile führt zu nachfolgender Ausgabe:
```python
print(ORDERS.columns, PERSONS.columns, sep="\n")
```
Ausgabe:
Index['products, 'purchase-id'], dtype='object')
Index|'name, birthdate, 'purchase-id'], dtype='object')
Sie wollen beide Dataframes so zusammenführen (merge), dass der resultierende Dataframe alle Personen aus **PERSONS** enthält und bei den Personen, die eine Bestellung (order) getätigt haben, ausserdem auch die zugehörigen Informationen des **ORDERS** Dataframes enthält. Bestellungen, die zu keiner Person aus PERSONS zugeordnet werden können, sollen nicht enthalten sein. Bei der Zuordnung der Einträge aus PERSONS und ORDERS fungiert die Spalte purchase-id als Schlüssel.
Bitte vervollständigen Sie dazu den folgenden Code:
pd.merge(PERSONS, **ORDERS**,
how=**’left’**,
left_on=**’purchase_id’**,
right_on=**’purchase_id’,**
)

<details>
<summary>Explanation</summary>

> 💡 **[.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
Let’s assume that the two DataFrame look as follow:
**ORDERS**
![Example DataFrame ORDERS](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/428b68ca-d506-48fe-b030-0891d8209a74/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XASNETOZ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCW2fvJrjmbyCw22ya9LP7BfFG%2FCRJa5xj4PoAP63%2BXxwIhALpLe0ZMPev5TViBWUVKzQ9XIjGvw51sHJVpsgSVwWLeKv8DCCcQABoMNjM3NDIzMTgzODA1Igy2fEvbKQWqDKzJm28q3AM9LFtXRYwy1UBfDdKDTVuM2J6S05J5pTewgwdMJA237g%2FH3yrDIzq8Gl5JgrJ1MP4ZBgZZygd3e%2BlUQVqA%2BbnIBZV0R6WHy1I4RgCWKKzLBkUEhGwdBScL03kCYqccOPFr5ikKpzBUjZ%2B5N25EhmaUdSTaSQ6Wz0rZLaMZLXcC8gX7ooFOxAZ3m4HxiuFmMXlnbYLvZ0XT8G8UXo2A6fDkLBRZiIO6pHKG097tC6DO8pb15M1oykIMHHR0fPjOTO3IrTOHX0Iez%2BE8ZRO%2BqWqBuUEgPAhoMGbsMzS0F8IjWjxk9yx7GPaMYAVNFgw33J227%2FEEJ%2BaMYuDs%2FixltwY4jkBm2pMtFXlcIQjXAol7C8MBx2G2TLgAkWd%2Bk1RalmFtPTGCa3IVyPpGbxmxZuYLd2EjZrJorZrphi1gp8%2F%2Fvok4UxfTCq8RLkncccbX%2Fx7phJj3Du6sXETKex9FK3Nw0NsLm7laBd2%2FVT4NQhwhVTUUITMvpopdICTzyJ35x9gHDUDqgpGbiNQl0zRZz%2FSL3Wj0tm%2Be55q7Ne5dr4dcO7I8RyQ02ZQRL8xZwmmqHHEERvj%2FsiwbaHB6bTL%2FMFjFkNZCV5VzFFzFZ2bk21IUyRQy14b%2Fi3sObizHATDozffJBjqkAclf4eRSHInAosoZn%2BCLYiZqL6zPNJE%2BcivL7ugV3lCJBG73LdcnzWU5vqoSq3VD4Ua7Gv8NoQHQUY6NmJbkS1pIHvW%2BWR6E2FBo%2F0yXlUclij1e8Wi7mNJFKTI1tYL7NMj76qnp%2FHpZ96EsZmq%2BgEjdpL52EUOgPP%2BizSgh6jfJD4YqAokVHpEO90J8tesvdn2TVJNZ2uBNjA4hApzOYvWoV0KW&X-Amz-Signature=73891f30f345652ff84cb8ee28eca095dffbde6b0de463ed0d9dc696b0ded8e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the **ORDERS** DataFrame contains an entry for each purchase that was made. The column **products** contains a list of all the products id’s that were purchased.
**PERSONS**
![Example DataFrame PERSONS](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7775f2c6-d1e4-401c-b175-f0c94da4f9e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XASNETOZ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCW2fvJrjmbyCw22ya9LP7BfFG%2FCRJa5xj4PoAP63%2BXxwIhALpLe0ZMPev5TViBWUVKzQ9XIjGvw51sHJVpsgSVwWLeKv8DCCcQABoMNjM3NDIzMTgzODA1Igy2fEvbKQWqDKzJm28q3AM9LFtXRYwy1UBfDdKDTVuM2J6S05J5pTewgwdMJA237g%2FH3yrDIzq8Gl5JgrJ1MP4ZBgZZygd3e%2BlUQVqA%2BbnIBZV0R6WHy1I4RgCWKKzLBkUEhGwdBScL03kCYqccOPFr5ikKpzBUjZ%2B5N25EhmaUdSTaSQ6Wz0rZLaMZLXcC8gX7ooFOxAZ3m4HxiuFmMXlnbYLvZ0XT8G8UXo2A6fDkLBRZiIO6pHKG097tC6DO8pb15M1oykIMHHR0fPjOTO3IrTOHX0Iez%2BE8ZRO%2BqWqBuUEgPAhoMGbsMzS0F8IjWjxk9yx7GPaMYAVNFgw33J227%2FEEJ%2BaMYuDs%2FixltwY4jkBm2pMtFXlcIQjXAol7C8MBx2G2TLgAkWd%2Bk1RalmFtPTGCa3IVyPpGbxmxZuYLd2EjZrJorZrphi1gp8%2F%2Fvok4UxfTCq8RLkncccbX%2Fx7phJj3Du6sXETKex9FK3Nw0NsLm7laBd2%2FVT4NQhwhVTUUITMvpopdICTzyJ35x9gHDUDqgpGbiNQl0zRZz%2FSL3Wj0tm%2Be55q7Ne5dr4dcO7I8RyQ02ZQRL8xZwmmqHHEERvj%2FsiwbaHB6bTL%2FMFjFkNZCV5VzFFzFZ2bk21IUyRQy14b%2Fi3sObizHATDozffJBjqkAclf4eRSHInAosoZn%2BCLYiZqL6zPNJE%2BcivL7ugV3lCJBG73LdcnzWU5vqoSq3VD4Ua7Gv8NoQHQUY6NmJbkS1pIHvW%2BWR6E2FBo%2F0yXlUclij1e8Wi7mNJFKTI1tYL7NMj76qnp%2FHpZ96EsZmq%2BgEjdpL52EUOgPP%2BizSgh6jfJD4YqAokVHpEO90J8tesvdn2TVJNZ2uBNjA4hApzOYvWoV0KW&X-Amz-Signature=488efbf547146041ad1eef0bd62e89938756f04bfe45938ccb407ae9be76329d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the **PERSONS** DataFrame contains an entry for each registered person. The column purchase-id is a foreign-key from the **ORDERS** table which tells us which purchase a person has made. We can see that everyone except Hans have made a purchase.
Now the questions asks to get the following output by merging the two tables:
![Desired output](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8f70aadf-d2dd-452b-b332-09702065ca4a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XASNETOZ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCW2fvJrjmbyCw22ya9LP7BfFG%2FCRJa5xj4PoAP63%2BXxwIhALpLe0ZMPev5TViBWUVKzQ9XIjGvw51sHJVpsgSVwWLeKv8DCCcQABoMNjM3NDIzMTgzODA1Igy2fEvbKQWqDKzJm28q3AM9LFtXRYwy1UBfDdKDTVuM2J6S05J5pTewgwdMJA237g%2FH3yrDIzq8Gl5JgrJ1MP4ZBgZZygd3e%2BlUQVqA%2BbnIBZV0R6WHy1I4RgCWKKzLBkUEhGwdBScL03kCYqccOPFr5ikKpzBUjZ%2B5N25EhmaUdSTaSQ6Wz0rZLaMZLXcC8gX7ooFOxAZ3m4HxiuFmMXlnbYLvZ0XT8G8UXo2A6fDkLBRZiIO6pHKG097tC6DO8pb15M1oykIMHHR0fPjOTO3IrTOHX0Iez%2BE8ZRO%2BqWqBuUEgPAhoMGbsMzS0F8IjWjxk9yx7GPaMYAVNFgw33J227%2FEEJ%2BaMYuDs%2FixltwY4jkBm2pMtFXlcIQjXAol7C8MBx2G2TLgAkWd%2Bk1RalmFtPTGCa3IVyPpGbxmxZuYLd2EjZrJorZrphi1gp8%2F%2Fvok4UxfTCq8RLkncccbX%2Fx7phJj3Du6sXETKex9FK3Nw0NsLm7laBd2%2FVT4NQhwhVTUUITMvpopdICTzyJ35x9gHDUDqgpGbiNQl0zRZz%2FSL3Wj0tm%2Be55q7Ne5dr4dcO7I8RyQ02ZQRL8xZwmmqHHEERvj%2FsiwbaHB6bTL%2FMFjFkNZCV5VzFFzFZ2bk21IUyRQy14b%2Fi3sObizHATDozffJBjqkAclf4eRSHInAosoZn%2BCLYiZqL6zPNJE%2BcivL7ugV3lCJBG73LdcnzWU5vqoSq3VD4Ua7Gv8NoQHQUY6NmJbkS1pIHvW%2BWR6E2FBo%2F0yXlUclij1e8Wi7mNJFKTI1tYL7NMj76qnp%2FHpZ96EsZmq%2BgEjdpL52EUOgPP%2BizSgh6jfJD4YqAokVHpEO90J8tesvdn2TVJNZ2uBNjA4hApzOYvWoV0KW&X-Amz-Signature=337031369fc7aaefe2894ed910b8763dc9ed880af58163ee4a26d342dd50e951&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that from the table **PERSONS**, all persons should be included in the output, **regardless** if the person has made a purchase already or not. From the table **ORDERS** however, only the orders should be included **that were made by a person** in the **PERSONS** table. As the second order id (**10111**) does **not appear anywhere** in the column purchase-id of the **PERSONS** table, this record should be **excluded**. 
Therefore, a **left** merge is done which selects all persons in the **PERSONS** table and only the matching ones in the **ORDERS** table.
```python
pd.merge(
	PERSONS,
	ORDERS,
	how='left'
	left_on='purchase-id',
	right_on='purchase-id'
)
```
</details>
---
# Question 2
Gegeben ist ein *pd.DataFrame* mit den Spalten **x, y, Anzahl** und sehr vielen Zeilen. Dabei kann es gut vorkommen, dass mehrere Zellen die jeweils gleichen Werte für **x** und **y** aufweisen. Die Spalte Anzahl weist beliebige Zahlenwerte auf.
Sie möchten nun gerne die durchschnittliche Anzahl für alle Kombinationen von x und y herausfinden. Welche Funktion/Methode kann das leisten?
❌ *melt()*
❌ *count()*
✅ *pivot_table()*
❌ *len()*
❌ *merge()*
❌ *keine der anderen genannten*

<details>
<summary>Explanation</summary>

> 💡 **[melt()](/1867045b058343e1a66b677961515907#5e95974d66444f179b205b86fa56a92d), [count()](/1867045b058343e1a66b677961515907#8d4d0ed1fc114482978e4da5f21b429f), [pivot_table()](/1867045b058343e1a66b677961515907#b7e324abb8a749b38b4a2386f6d4dbf7), len(), [merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
Let’s assume the DataFrame looks as follow:
![Example DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/668dc5b1-a998-4f9a-b59c-f1a2d1e0d096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ECHBKQK%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIESxP1PgtlNzoCY%2BZw4UU6gtjehuEdjnd1YkRGNnl09pAiAqWnE5N5FoKxuMV%2B3p1kKidrgUG9LCyFZSInDkMej3FSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMe9TlEi0E04%2Fjxj1OKtwDc4A51SybU6nsgwnYoW2OupSypswhZPDg7%2FbUhOfyyPPa4ilIaGCfvDIk9cdo2PRzmkFfgbY3jAflc%2BQJGdrJSimKsNRqOhatd8%2BPd4z8DCvH5pZPyAqYFrx2Q7LIiazfJGLXW%2BfkPqU3svfP%2FDZYUDZk3kysdjuhIZzXsOMqb5qNkZC3rkPIFMjiXcD5G3%2F%2BQtZnZFS3EcU%2BB5H06B1LojH4GDOTU3yg%2BcZZQLU2sHO68eib%2BlCHeHrXLVsLsKJQ2GEogqdqTqHivGyutZqjDBO7ek%2FDfgqhjHJBFa1PxupvO2WFBYE69INSzJRmAM8e%2BhTnGLeIHOb4wSxmiPUhvQvX4HISyuFZlRc61SEbFgXwOdsP7G%2F6BEJaeTWzlUtU3MBMwDoZwdcovG9JCzLtkju2YSYGG2mnU%2BrG%2FiUdyeDqifKade5lIVS3l0sMvbjeuWpgogtkyrtpKpD7MFsSViImDk8x%2FxtiMXLI8JPnOhSg3aURsqp5gb%2FCvjHJmg3cq97FKoSopzvKwOAn%2FhpeHhd4JPLGRMGWLcT5FjSi5FCAPjrrT62WX4BjurT4lfnUFpNtVpPbpRE4WFV5YuHDEKugC6zuw6tRiqamgnDCeYfGz6hHn8TdxspLqTkw%2FM33yQY6pgHiYUs3J5ZQpKIm6MwU1ond9Ope6NpWUgBD%2Fzo7ZYOmOy%2BBF0s0jJ%2BfWeMfEuRzenAqrfQAi88IMS2%2FjREFAJYb99vGO1Df4DQNLqPwswKn%2F%2BCHSs9R5z5VldTACbUAQEKaGycS99pYaBtSSek9Cw9%2BjZqzBKMALYcjg1N40BqXUBB55iUAByMIfA4DejZfFbYEPyD%2FB1qOWwgVwqiKcMncKiNR6icB&X-Amz-Signature=250a1703ac160f0606ad24db2d64aa8a745c1b8e897c3838db34efa4464e04b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The question is asking now to identify the **unique combinations** for **x** and **y** values and then compute the **average** in column `Anzahl` of these combinations. 
Whenever something ***summarizing*** for data in a DataFrame should be computed (e.g., count how many times a value x appears etc.), the `pivot_table()` function **can** be used.
Using the `pivot_table()` function we can get the desired output
![Desired Output](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2aaab5c7-af83-4dbc-9e8e-d67005019193/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ECHBKQK%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIESxP1PgtlNzoCY%2BZw4UU6gtjehuEdjnd1YkRGNnl09pAiAqWnE5N5FoKxuMV%2B3p1kKidrgUG9LCyFZSInDkMej3FSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMe9TlEi0E04%2Fjxj1OKtwDc4A51SybU6nsgwnYoW2OupSypswhZPDg7%2FbUhOfyyPPa4ilIaGCfvDIk9cdo2PRzmkFfgbY3jAflc%2BQJGdrJSimKsNRqOhatd8%2BPd4z8DCvH5pZPyAqYFrx2Q7LIiazfJGLXW%2BfkPqU3svfP%2FDZYUDZk3kysdjuhIZzXsOMqb5qNkZC3rkPIFMjiXcD5G3%2F%2BQtZnZFS3EcU%2BB5H06B1LojH4GDOTU3yg%2BcZZQLU2sHO68eib%2BlCHeHrXLVsLsKJQ2GEogqdqTqHivGyutZqjDBO7ek%2FDfgqhjHJBFa1PxupvO2WFBYE69INSzJRmAM8e%2BhTnGLeIHOb4wSxmiPUhvQvX4HISyuFZlRc61SEbFgXwOdsP7G%2F6BEJaeTWzlUtU3MBMwDoZwdcovG9JCzLtkju2YSYGG2mnU%2BrG%2FiUdyeDqifKade5lIVS3l0sMvbjeuWpgogtkyrtpKpD7MFsSViImDk8x%2FxtiMXLI8JPnOhSg3aURsqp5gb%2FCvjHJmg3cq97FKoSopzvKwOAn%2FhpeHhd4JPLGRMGWLcT5FjSi5FCAPjrrT62WX4BjurT4lfnUFpNtVpPbpRE4WFV5YuHDEKugC6zuw6tRiqamgnDCeYfGz6hHn8TdxspLqTkw%2FM33yQY6pgHiYUs3J5ZQpKIm6MwU1ond9Ope6NpWUgBD%2Fzo7ZYOmOy%2BBF0s0jJ%2BfWeMfEuRzenAqrfQAi88IMS2%2FjREFAJYb99vGO1Df4DQNLqPwswKn%2F%2BCHSs9R5z5VldTACbUAQEKaGycS99pYaBtSSek9Cw9%2BjZqzBKMALYcjg1N40BqXUBB55iUAByMIfA4DejZfFbYEPyD%2FB1qOWwgVwqiKcMncKiNR6icB&X-Amz-Signature=7ec4e68c6fc88f19e6853627438785b88ebfad54c8cd55e2afcffa10531893bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>*Note*</summary>

I actually didn’t use the `pivot_table()` function here because in my opinion it makes much more sense to do a simple group by:
```python
df.groupby(['x', 'y']).agg(
    {'Anzahl' : 'mean'}
)
```
</details>
</details>
---
# Question 3
Gegeben ist folgender *pd.DataFrame* **df:**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8a98d285-ea0b-43af-860e-020ddd35c49c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z7VZYMZ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCWSUzcBYhjF%2B5Uv3YcaYtv%2BW1x9IcqSLqNLFVTTmsWogIhALg3o6uiETmoKd4i6j%2BwBNjeT%2F1SpKdaMqvnukAxHt1BKv8DCCcQABoMNjM3NDIzMTgzODA1IgxWMzVSYlq3bIkdTF4q3ANi5wIWNWNZcx877feFS%2Bm%2FkFX%2FW67FYaHofHvaJPve4jHvSUAFjr7cP%2Bzrhrehv%2BC%2F6uVJc3wVzvuWnFxCS91xz2gNsTyxrVG0pZuMa7d%2BJn4HhrDj2hxYqA0joyg3C8QURzNCcZt1ssJ9ckqk3sfbHGyQu0rASTbFK3XRRpw%2B6B2WSe3vLiR2zFj6c3HtRp5UeGxwzesMBkpWqTnV4pnykdjbhNXYydG6AznGmYRCFgieyXdwaqPO3fMRofQvfUF9ghU57fRlD9EBBMivRxmyS4O9G2XpCcYCy5AoLllxwukTNV9EaWhc%2Bb7%2FUFmf25T%2BaHPcJERS1z0l6Tp4N5CQUZURtwia88Q%2FgmigS%2BvClqYatCqWRTPXBhzwIAK972AM6gUYASBKzMUmXECCURzDEwkXyqbDhU6TddesMs3DLIwiTRjDj%2F%2FR8LYXJrvHT8QXBe%2FJOu8HE2saUNktyKINl%2B1Hp5txm87fD72CfmF9gaL7uYcP02aRdSfZBl1r1QAyloIL4qfDXt9POvQ6RfsCGMdfOXgHlca8gGQkF2RGQBZiQ5DtkHbwk3SDW2vU8XAbTWW1UPtfTy43ra%2F9cYYQJJ49yO19TMPnfiysNzPZLA11XncXOofAg0ZJvTDXzvfJBjqkASqcwLjwW6e%2FrHtrlrPNBOetd67bRVNPXuKc37vl656ag%2FGgWLrMecEd2VV4ZrqOoV8qc4GORPtdsfybfdUIKw6cSYIFJBWnEg4SDm5%2BsvQCl7lyCc8zgLD71UDsi0NQRo9US3W37587741QM2TzrFspjKx7p40dqBBvuBu44Ao09ZJw%2F7kzKXExuoi6XGcqPMBuw9Vi75Ki9NdcZ6HUCo1kioq2&X-Amz-Signature=5e9877d09e7d7042b6493d0fdaf4e46547fe21768622b7773aab24dfdc92674d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Welche der folgenden Codezeilen gibt das Durchschnittsalter je Geschlecht zurück?
❌ df['Alter'].mean()
❌ dt.groupby('Alter').mean()
❌ df['Geschlecht'].value_counts()
✅ df.groupby('Geschlecht')['Alter'].mean()
❌ df.groupby('Alter')['Geschlecht'].mean()
❌ keine der anderen genannten

<details>
<summary>Explanation</summary>

> 💡 **[groupby()](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15), [value_counts()](/1867045b058343e1a66b677961515907#b585cb62f9dd4878aa31acb88e071f0e), [mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
❌ **Incorrect**. Only the average age across **both genders** is returned.
```python
df['Alter'].mean()
36
```
❌ **Incorrect**. The average age for **each unique age** is returned, which is of course the age itself as there are **not more than one person** with the same age.
```python
dt.groupby('Alter').mean()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/14cd5803-adf1-44ab-99ee-6770a9d73201/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667J46VTED%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDEmIMHYjemsFt32pq7KNEoJLybP5zcPk5OMUD4YGo4LQIhANmuyVbmn5mbTVbBvDekI9Gnt%2BR54nqy2TUA%2F5%2FMT5laKv8DCCcQABoMNjM3NDIzMTgzODA1IgxhN1VME1u3vyCOJKsq3AN9vUOCQWoHDAUKYpZs3YlLFzD6j1LdZHZ2fLg%2Bnu53patCb1fAV9YIftD5Mna5Sfshw58kgsY4GiDH2JJYf7qiJO9DYZmQAJ24SLsDOzcVl79O8HQgD22C7T2a6EIdmol6qEQ15d8IE5BfCadDLuySVFr2L0N56ni0dwYYKLL6LUwmekGbiDIgdExphXUt80reyVoXZpr3ZqBIcuq9pQANvSCKG2iZ4XisZI0iiEktfSTld517UQod1xR2Ao52y4Y8lrUBeieJixgmXtgb%2BlaFV%2BMbMNmVmrv2UXP0WCrJekfQ5hmPphHr3XjZLuKTD7Iu9WPzZOKzIae0JIG%2BpcBZC49cW09MHEI5Maq%2Bb%2BFIeyzGweafmK%2BAGSieflWWeQT8ZDkV2%2FAuTdKlwUAXkke7%2BhhE7z0Mjj5KzDQnqkX5uxS%2FkB4ThveGva%2F20%2Bj5vCy%2B0ezGqJrEaXJi13xHM%2BwXxRuIbgr%2Bp1yxGC8OqBcPFlqll%2B%2FoJz6yWo3SJ7d%2BYC6PVlIN2btP95Kekn%2FZgTibpl9CEPfFk9dI9hLKyhMLyP96O95xNkHKaLjjQgVWKYOks3zI5D3AVqTMy0p10gY2StjTaDX9BmK2T9k00akyjmkbFoSNAV4Bcj2DIzDTzvfJBjqkAVyksSgcJpPfMflcP%2B4sZhNUU7wyQPMWOmFEkRrnCDMp4dgOfSHwF1eLn1AgIGFZ%2FcwpXA6LB3AEhyoy%2BO%2BlhEk5YFpDFCLrCatPOcYgTFVvG6cO1HrKJU1Yk9a8vYOKJ0jcygH5BupqR6CkGYhTILJn8oxXcBZwNorLmKnLj2UDMqDNk8qr2UUAUK6KbeqFFMwbzypPgiKR1BAdjZkbG%2FgaZW0%2F&X-Amz-Signature=9b9a841916d15417984d96a878604fcd0d1ab0c4af225e6d36bd85ea43ff3710&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. A series containing the **number of persons** for both genders is returned.
```python
df['Geschlecht'].value_counts()

m    5
w    5
Name: Geschlecht, dtype: int64
```
✅ **Correct**. A series containing the **average age** for both genders is returned.
```python
df.groupby('Geschlecht')['Alter'].mean()

Geschlecht
m    33.6
w    39.4
Name: Alter, dtype: float64
```
❌ **Incorrect**. A `TypeError` is returned as **gender is a string** and it is not possible to compute an arithmetic mean (average) with text data (strings).
❌ **Incorrect**. [Statement 4](/e1a14712985b4466992e86be0e4cd8bc) is correct.
</details>
---
# Question 4
Gegeben ist eine CSV-Datei mit dem Namen "data.csv', die die folgenden Informationen enthält:
```plain text
Name,Alter,Land
John,25,USA
Emily,38,UK
Karin,33,Switzerland
Michael,35,USA
Sophia,28,Germany
Urs,25,Switzerland
Maximilian,20,Germany
```
Diese Informationen werden in folgendem Programm verwendet, welches das Durchschnittsalter aller Personen aus der Schweiz (Switzerland) berechnen und ausgeben sol:
```python
df = pd.read_csv('data.csv')
CH_data= df[df['Land'] == 'CH']
print("Durchschnittsalter der Personen aus der Schweiz:", df['Alter'].mean())
```
✅ Das Programm kann ausgeführt werden, ohne dass Python einen Fehler wirft.
❌ Das Programm gibt das Durchschnittsalter der Personen aus der Schweiz (Switzerland) korrekt aus.
✅ Das Programm ist in Zeile 2 fehlerhaft.
❌ Das Programm ist in Zeile 1 fehlerhaft.
✅ DasProgramm ist in Zeile 3 fehlerhaft.

<details>
<summary>Explanation</summary>

> 💡 **[read_csv()](/1867045b058343e1a66b677961515907#bb02198699ce440f948c4c281f1957ac), [mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5), [selecting rows based on condition](/1867045b058343e1a66b677961515907#a61901eaa28c4a7da25d80a1223b80f7)**
Let’s go through the code line-by-line to understand what is happening. 
First, the data is read from the csv file.
```python
df = pd.read_csv('data.csv')
```
![DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3482174a-0b14-479d-a944-3953a3e7bc02/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNJNDI26%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCgMUc5JxT9ZffG64xGy1RGypjgVlL0zljXcx5F6XsyoAIgHwsxrD7yEAdUKUA9wE0%2FqaDHwootsvVj7DlCpD7lJPsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDD%2FywJUyuQgESY%2Fm1yrcA1eOWEhrNn1eNw7owg3kTKrtAaxrmjwlRt7r0wLLLPapubwK0yD72BPEfyifH3%2FgmqeE%2BGr909sR35u3%2FvtqNVmXOB1EtAm%2FZZ3SsoYtahPUDmssjd9awnxWOvOPv9MuDvj8vnNNsUPK2HcaV2pWWXaf35t3MFjbTnCqVlfNH4q1fZslOsb3fcf92qymaZ8np1a0IGIvHWqXGnlnACrkFqial21bbgfEzWsoxuiOrZobEJ7381JLPmi3fEs4LedCwoyKDkXuN45HvMkL2FCnygQ4VIlmQ6oQcJhnLqHnmiAAlmQatmSRRn4z%2F0QyiTNzw%2FWEeuA47OC0IrBmonWfDVK9TbTe9TKwMPCo%2F3u0PHtQUkzqH0DhbgySba1TbmmGJt4vcugx8F1BLSyu2%2BBmfkUXq19b3cLJyYI1a%2B2CjOl750tpPJcbJmTXAKVuT9V5n65MWSV%2B1QhOvdMJE8Okdq2y2ovyKsx93rlftv64p7jZwlTJaqF8Z%2FjNKbt8LUK5EqsKVgKOc8TOm4qbFNnD6k%2Bi2%2BbDJoRDKvfLl9U06huKtMHOQEr8F4idTykLXxpSKqMbPe6lwAetlrtCjedd4ZeWF5EYtnNXFWMwpnbXnGkHJBdVq8hLS52AbfpYMP2W%2BMkGOqUBHENlAU05cu%2FB3dBiDThfJNrU25Qwz0RNjVUoh0%2F6SujrPJYb%2FcEUZ12ocY4HcJlWLt2aMkd%2FnEzKc0N5tVyzHuANDSS5COHNFtDYjmH4qMf0IYH1fvlEsswoOAMn820kVKMlxU344hFa1J%2BdJKL9u3IBuWRlJvMObKbv8fPC4kcya6fEoip62fFmxPUWG6K2Z%2FrAXDiH9mTDYA2EvedOLF3omo4e&X-Amz-Signature=d7b3528259326fecf50d0ba1e0449e072ee124e4ce9aa8003f0d652bb41350d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Next, all records are selected that contain the value `'CH'` in column `Land`.
```python
CH_data = df[df['Land'] == 'CH']
```
However, as no record contains the value `'CH'` in column `Land` the DataFrame **CH_data** is **empty**.
![Empty DataFrame CH_data](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f7a4b601-3675-4abc-b01d-3486ce99183e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNJNDI26%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCgMUc5JxT9ZffG64xGy1RGypjgVlL0zljXcx5F6XsyoAIgHwsxrD7yEAdUKUA9wE0%2FqaDHwootsvVj7DlCpD7lJPsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDD%2FywJUyuQgESY%2Fm1yrcA1eOWEhrNn1eNw7owg3kTKrtAaxrmjwlRt7r0wLLLPapubwK0yD72BPEfyifH3%2FgmqeE%2BGr909sR35u3%2FvtqNVmXOB1EtAm%2FZZ3SsoYtahPUDmssjd9awnxWOvOPv9MuDvj8vnNNsUPK2HcaV2pWWXaf35t3MFjbTnCqVlfNH4q1fZslOsb3fcf92qymaZ8np1a0IGIvHWqXGnlnACrkFqial21bbgfEzWsoxuiOrZobEJ7381JLPmi3fEs4LedCwoyKDkXuN45HvMkL2FCnygQ4VIlmQ6oQcJhnLqHnmiAAlmQatmSRRn4z%2F0QyiTNzw%2FWEeuA47OC0IrBmonWfDVK9TbTe9TKwMPCo%2F3u0PHtQUkzqH0DhbgySba1TbmmGJt4vcugx8F1BLSyu2%2BBmfkUXq19b3cLJyYI1a%2B2CjOl750tpPJcbJmTXAKVuT9V5n65MWSV%2B1QhOvdMJE8Okdq2y2ovyKsx93rlftv64p7jZwlTJaqF8Z%2FjNKbt8LUK5EqsKVgKOc8TOm4qbFNnD6k%2Bi2%2BbDJoRDKvfLl9U06huKtMHOQEr8F4idTykLXxpSKqMbPe6lwAetlrtCjedd4ZeWF5EYtnNXFWMwpnbXnGkHJBdVq8hLS52AbfpYMP2W%2BMkGOqUBHENlAU05cu%2FB3dBiDThfJNrU25Qwz0RNjVUoh0%2F6SujrPJYb%2FcEUZ12ocY4HcJlWLt2aMkd%2FnEzKc0N5tVyzHuANDSS5COHNFtDYjmH4qMf0IYH1fvlEsswoOAMn820kVKMlxU344hFa1J%2BdJKL9u3IBuWRlJvMObKbv8fPC4kcya6fEoip62fFmxPUWG6K2Z%2FrAXDiH9mTDYA2EvedOLF3omo4e&X-Amz-Signature=8a2882f761485b9164f8c2662712cc3eeaee26fde701d6709ad27b2c9e8fb793&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now the average value of column `Alter` in DataFrame **df** is calculated.
```python
print("Durchschnittsalter der Personen aus der Schweiz:", df['Alter'].mean())

Durchschnittsalter der Personen aus der Schweiz: 29.142857142857142
```
However, is the average age for persons from Switzerland really **29.14** years?
We can see that **Karin** and **Urs** are from Switzerland. Karin is 33 years and Urs 25 years old. Thus the average age is **exactly** (33 + 25) / 2 = **29** **years**.
Hence, the code has some errors. 
The **first error** is in **line 2** where we are aiming to select only the persons from Switzerland. Instead of using `'CH'` as criteria we should us `'Switzerland'` as the column Land does not contain country abbreviations but rather the **full names** of the countries.
If we update the code in line 2 accordingly, the DataFrame **CH_data** is no longer empty.
```python
CH_data = df[df['Land'] == 'Switzerland']
```
![DataFrame CH_data](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b1e07a43-f2b1-481b-ba63-0c69398aa0da/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNJNDI26%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCgMUc5JxT9ZffG64xGy1RGypjgVlL0zljXcx5F6XsyoAIgHwsxrD7yEAdUKUA9wE0%2FqaDHwootsvVj7DlCpD7lJPsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDD%2FywJUyuQgESY%2Fm1yrcA1eOWEhrNn1eNw7owg3kTKrtAaxrmjwlRt7r0wLLLPapubwK0yD72BPEfyifH3%2FgmqeE%2BGr909sR35u3%2FvtqNVmXOB1EtAm%2FZZ3SsoYtahPUDmssjd9awnxWOvOPv9MuDvj8vnNNsUPK2HcaV2pWWXaf35t3MFjbTnCqVlfNH4q1fZslOsb3fcf92qymaZ8np1a0IGIvHWqXGnlnACrkFqial21bbgfEzWsoxuiOrZobEJ7381JLPmi3fEs4LedCwoyKDkXuN45HvMkL2FCnygQ4VIlmQ6oQcJhnLqHnmiAAlmQatmSRRn4z%2F0QyiTNzw%2FWEeuA47OC0IrBmonWfDVK9TbTe9TKwMPCo%2F3u0PHtQUkzqH0DhbgySba1TbmmGJt4vcugx8F1BLSyu2%2BBmfkUXq19b3cLJyYI1a%2B2CjOl750tpPJcbJmTXAKVuT9V5n65MWSV%2B1QhOvdMJE8Okdq2y2ovyKsx93rlftv64p7jZwlTJaqF8Z%2FjNKbt8LUK5EqsKVgKOc8TOm4qbFNnD6k%2Bi2%2BbDJoRDKvfLl9U06huKtMHOQEr8F4idTykLXxpSKqMbPe6lwAetlrtCjedd4ZeWF5EYtnNXFWMwpnbXnGkHJBdVq8hLS52AbfpYMP2W%2BMkGOqUBHENlAU05cu%2FB3dBiDThfJNrU25Qwz0RNjVUoh0%2F6SujrPJYb%2FcEUZ12ocY4HcJlWLt2aMkd%2FnEzKc0N5tVyzHuANDSS5COHNFtDYjmH4qMf0IYH1fvlEsswoOAMn820kVKMlxU344hFa1J%2BdJKL9u3IBuWRlJvMObKbv8fPC4kcya6fEoip62fFmxPUWG6K2Z%2FrAXDiH9mTDYA2EvedOLF3omo4e&X-Amz-Signature=18f79c3ca9b3833a8aca0a39e2b8c99a5e64787e3a77e19e359440fff94ebc88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we can compute the average age in line three based on this DataFrame. To do so, we must **correct the code**: We must access the column `Alter` in **CH_data** and not in **df**.
```python
print("Durchschnittsalter der Personen aus der Schweiz:", CH_data['Alter'].mean())

Durchschnittsalter der Personen aus der Schweiz: 29.0
```
We can see, by **correcting the errors in line 2 and line 3**, the code works now as intended: it returns the average age of all persons from Karin and Urs, the two Swiss people in DataFrame **df**.
</details>
---
# Question 5
Welche der folgenden Datentypen kann die Abfrage von Inhalten einer *pd.Series* zurückgeben?
✅ str
✅ pd.Series
✅ int
✅ Car
✅ float
✅ pd.DataFrame

<details>
<summary>Explanation</summary>

> 💡 **[Python datatypes](/5b0832dbf9454eb1941b7632e68a9abb#d1c2e1bb9bac46b8afbe6f4f6950edd9), [Pandas datatypes](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
✅ **Correct**. It is possible to store strings in a DataFrame cell / Series.
✅ **Correct**. It is possible to store a Series object in a DataFrame cell / Series. 
✅ **Correct**: It is possible to store integers in a DataFrame cell / Series.
✅ **Correct**. It is possible to store object variables of custom datatypes in a DataFrame cell / Series.
✅ **Correct**. It is possible to store a float in a DataFrame cell / Series.
✅ **Correct**. It is possible to store a variable in a DataFrame cell / Series that contains another DataFrame.
</details>
---
📄 **[Quiz 10]** (subpage)
# Question 1
Wie viele Diagramme (axes) werden von folgendem Ausdruck erzeugt?
**fig, axs = plt.subplots(39, 37)**
1’443

<details>
<summary>Explanation</summary>

> 💡 **[subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d)**
The syntax of the subplot() function is as follow:
`plt.subplots( << n_rows >>, << n_col >>)`
Thus, with the command above a grid with **39 rows** and **37 columns** is generated.
Hence, in the variable `axs` a **nested list** will be stored that contains 39 lists (rows) and each list contains 37 elements (plots per row). In the end there will be 39 * 37 = **1’443 **subplots.
</details>
---
# Question 2
Gegeben sind die folgenden drei Boxplots.
Bitte klicken Sie in der Figure an die Stelle, an welcher der Median der petal length für Virginica dargestellt wird.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/461e7a15-add0-4599-bc2c-ab3062e85d3d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLULATRM%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCICkFmp%2FmV2pw9DhEVmA6Ppjr0Q1bokclQpV%2BAgRwCP%2BbAiBsr7lwVqq9Rm5VK7aegmmmDq%2FvtLo5rnW%2FA%2BYK6MgwaSr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIM13kMHVvRJ6eAG9YvKtwD1IIkf%2BXTUxyIiAU6RgTYGokL2cCZ1A7wc9PoEpoPwdEW6ZDxky94JGj71P%2BlosZOYqLI1FpMYFbzykmwnKG%2BREncDmXXTjDMWhkF%2Fx5ke34aJM82rWusyDqSAOMWX7Tu6RGFzHwlSq8nYnmvUMLTh%2FyybtTpicRxCKJItbhPZgmgnTKXJWiuoHS72c0xaBSuGwVNFyFjoXF24VAzeI%2BZqjZU8mw5Xx652Rl7PPVw%2FJVWsSCD9qZfY3ScrKE%2FYVXe1qE4lGEjxA63vk2O%2BjOdTm4RpfNimhinkY%2BnWIuJP17iFY3%2BDFdZx3Wsr6kCLltmtC6Jm%2BFv9Aw%2B80VUgiJaDOKTprz11kXwf3kFpSltn8VsTtvInmjMQTiDjpa9Mj7O%2F9jXFwwoi%2BXtupiHl0F05zEMmCqRsAlCgCpOwtv76uwWVMeP9KyS%2Bj%2BlkFAcECQzCWulS0yTDuufMVyVFcMbQP9ojKmXhBVhWV5CvOIh7UxEvNxLKeZu0qRzm20deCMGXRmADMc5%2FR8SeAaMaG6tC%2FtesNTz9t2HxkTAX7aET32oPIjVxUlgyO8wxzXwtaSzVrrwDVV34JtWYB4s2%2BBnzfbQZu%2BK1enCxSCXAmCXvBgbHlWmxUVWgHRcKmcwkJb4yQY6pgHTQYgMEAdMcEQW%2Fxmc9vQbtgVcHfK3sXjQQLdravpGmTAh2qFtO6mH0bngp8atQrDkDcxok8ZSH4%2Bli5C4yX5r2GY8vm1IkYCbL8l80XQW%2FB0%2FBovpsneLJy9SILB%2BSqS1LoCb15mQYLzDguDGskY3KG%2FmPfFXU32zfCOVhxXnB86%2BbB6550fMKUSrSdqh%2Fjhezd%2F7IlDgEC5Xh1EW29GQ%2F5M%2BVncs&X-Amz-Signature=7411c530d023004a24ccbc2ea240bce51a6aee7bc7f65830fc33da93727cdc15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

> 💡 **[Boxplot](/6ac6e358ebd649cbab8c4f731dfa5cc8#29b3bf078dde4d20ae32783413578357)**
As the chart below shows, the **horizontal line** in the box represents the Median.
![Elements of a boxlot](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9ca63491-9ce3-4d62-bae0-fdde85c85fec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AXOJZXF%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIFXAjzJalYsIwr%2FmyXl0LIZfQ0pQaeZ6UMRafoQq5MCHAiB%2F1gBCBQ701GNYO61SFiTiRhDJDbCOdVffQ8e%2B5%2FY89Sr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMFYHp2EjKlpVXjaQUKtwDwPCfCN2jfVEGLGw3m0VzI%2Fd%2B2L6qZLjWQgsnqKYGTRorUYMqz%2FQfsf6dRw%2FbQFFFIRCl%2BHke14K%2Bm9q4at%2FFWljc32TbWRT30y5NRUNccKdobW8s%2Fl%2FmZ19IeS9%2FhGHLLLl9OC5opOfHqqGHZW%2FC0y4UHHhgRvU4Tbz2ogIdezFVbSS6avQUKm8GIJzi4yze%2FofC04KzjVZnLvsMUWvcn8NpM7BJ%2Br5ItYnesTVhP%2BZsss9KtT3P5d2NV8eJ5%2FOdfzrCisIz9saFqM789l6FU0uVeDK4UpXrSER%2FjllsOJHNVj%2BsRa98afM9uQAs81PofL11cajEU8BLMFMOe7A%2BFKifYTrpF7B%2Bh2CDawdvBoH4AIvAORc6gkQ0HHRj9ahxM2IgqDEFneyKo8B4jhukJgHJwyzLFaFAhirRnR9WBqEn16Op%2BoX9hoiLpFUYl38ggy4kAqDxAcw9lDOWOVqRtKuZMsQZKKzGmjR0cMb5ctZZtSOjuVCdHrqciIBYBBx6ZaR3RkMxC04TIXggjnJeUEdhK0TMixt12utjKThBAjyPLUqmCESya4LNGlvdlZpL9ZmC96JyvAMhQd%2FOQtHCcaFfm25H7cbO8XGo9qYt%2FSlJk0W%2FLgCauUI4h6Ewz5b4yQY6pgGafsXY94DLZxmPLWrByh8G1VJ6ZzV%2Bz5wN2W8Srs9B398HPJlrDRgGC9o%2BMafLekIb6UeI4LMr1KBKBZpGTuxZqvVy9UZGAzT0aeQQx6bNNyCCuOHW7V1QUgRYx8ujYkFEhAozGSSQl23nzO6v0Am9GuXkLQTdGPJlaLN%2BJGEOgDk%2B3Ii1h1yHnSxAOuAlXzY9Aw7OK3eBm17Dm4sW1bvf1Xuwleci&X-Amz-Signature=4db6b92e5b5537f07551479ff34548f820c6924914e2fba67c184c24ff69a59c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
# Question 3
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
![Subplots with different y-coordinates](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3b16e380-4f6d-4a51-9579-054fc1832c97/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMZT62QI%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC5JYTDmWLjsgKuehsALCQ2FMmN%2Bkbeky2eWbwzS9W%2BDwIhALcvNKjNv4hCFjWo95Ds8sWzV6yhjkfnHKtgjvwwFq2lKv8DCCoQABoMNjM3NDIzMTgzODA1Igw7Yuv7gpf469Yt16Uq3AMzLjIGViT7a6p1V%2FyVXmAZSpG5SRVnpTxZdy4aUE4PjTU1gX96ftK4kFclfPstacjSp8ZA7lCT5sLVsxG1zQb82ryUm8RBzj4IGrekXrgNnP6Fwvm5DT03rW1L6uXrUti%2FMeNWyC4do0PWTiD0TSf9d8H9UejE85RZxsMpdr7gYvR9Drw6xTDFKPNoPnyFeKNzFkLs3nfdqijG3JkaTeaVAa7TP31PPn5Lnb94jNpIUWvjJ3lhmRbjRSanltGgsh13mDCDjQeSK%2B8oo7CEGU%2BV0M%2FOqQ4%2BWmqd6UwaxSzFaGXsPsZYORnMK3BbDZt6SHsqcfupFBtmXjCRfODSelnMDw6XIJtm3QoSVEzXHsT2rL9sfnhj2Qstf7RXGqM%2Bemji35z%2FoU5IKQULrNFTKtTGTpayofe2amAs9dQcGVd4dXLsULN5GZ0jgcU7lrHrqfuV%2BgA9iuuROPnrsSAXA7pE3Kk3OQApUMl%2B%2FipFoN4MAU9Xqx2LJuzxU31%2F0if3h%2BaYsQ6cj3P0E04UpnzenzXb0pwZsKqUxJE4vuPq%2F6oPTKYttWXXr7F6i6rxf0M98Zw1OMVBEKfgxPS%2B3RlLYIJm6iztQIFUtEZESUOltpyzZNwrRg4sHVxIT41qAjCJlvjJBjqkAUFUVYvhohJCwc6kIR18jXLwpJazBbvX7psJMpTft6Yp6z1cAlx5JCpHNKhTXX6J%2FA9eqhDbm4HEkikzDr6Z8z8KbMnjDdYI%2B4IASQr6pIdWV%2BreNMUesD1VkAeoexTj0YzlR9GzZyJcOFCgUD7L%2BupzImzR2KT%2BkhcBHU7jOH1XQUrIquAjV7dpHZReSbCfXXcB08B1LnydLRjYZIMQM2CbjQJy&X-Amz-Signature=38b9f5e20430a8ad4873e242958872727728bf3aa838382f3d800bad6c7e202d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now when we add parameter `sharey=True` to the first command:
```python
fig, axs = plt.subplots(2, 2, sharey=True)
```
The y-axis will be shared across all subplots:
![Subplots with different y-coordinates but shared y-axis](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/223c7937-1818-41eb-9e48-3aee7bd3bebe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMZT62QI%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC5JYTDmWLjsgKuehsALCQ2FMmN%2Bkbeky2eWbwzS9W%2BDwIhALcvNKjNv4hCFjWo95Ds8sWzV6yhjkfnHKtgjvwwFq2lKv8DCCoQABoMNjM3NDIzMTgzODA1Igw7Yuv7gpf469Yt16Uq3AMzLjIGViT7a6p1V%2FyVXmAZSpG5SRVnpTxZdy4aUE4PjTU1gX96ftK4kFclfPstacjSp8ZA7lCT5sLVsxG1zQb82ryUm8RBzj4IGrekXrgNnP6Fwvm5DT03rW1L6uXrUti%2FMeNWyC4do0PWTiD0TSf9d8H9UejE85RZxsMpdr7gYvR9Drw6xTDFKPNoPnyFeKNzFkLs3nfdqijG3JkaTeaVAa7TP31PPn5Lnb94jNpIUWvjJ3lhmRbjRSanltGgsh13mDCDjQeSK%2B8oo7CEGU%2BV0M%2FOqQ4%2BWmqd6UwaxSzFaGXsPsZYORnMK3BbDZt6SHsqcfupFBtmXjCRfODSelnMDw6XIJtm3QoSVEzXHsT2rL9sfnhj2Qstf7RXGqM%2Bemji35z%2FoU5IKQULrNFTKtTGTpayofe2amAs9dQcGVd4dXLsULN5GZ0jgcU7lrHrqfuV%2BgA9iuuROPnrsSAXA7pE3Kk3OQApUMl%2B%2FipFoN4MAU9Xqx2LJuzxU31%2F0if3h%2BaYsQ6cj3P0E04UpnzenzXb0pwZsKqUxJE4vuPq%2F6oPTKYttWXXr7F6i6rxf0M98Zw1OMVBEKfgxPS%2B3RlLYIJm6iztQIFUtEZESUOltpyzZNwrRg4sHVxIT41qAjCJlvjJBjqkAUFUVYvhohJCwc6kIR18jXLwpJazBbvX7psJMpTft6Yp6z1cAlx5JCpHNKhTXX6J%2FA9eqhDbm4HEkikzDr6Z8z8KbMnjDdYI%2B4IASQr6pIdWV%2BreNMUesD1VkAeoexTj0YzlR9GzZyJcOFCgUD7L%2BupzImzR2KT%2BkhcBHU7jOH1XQUrIquAjV7dpHZReSbCfXXcB08B1LnydLRjYZIMQM2CbjQJy&X-Amz-Signature=356c8ed75eaeb2f065c15ca48948e77ef0d8e6e026e1a3ee914b084f1696b102&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. `sharey=True` does **not** make the subplots share the y-coordinates, i.e., the data that is shown. In the example above, each subplot is showing a **different** line.
Also, as we have seen above, it is possible to **share the y-axis** while **not sharing the x-axis**. There is no dependency between the two parameters.
✅ **Correct**. `sharey=True` makes the subplot **share the y-axis**. Therefore, the y-axis is scaled to a range that captures the **max-value** and the **min-value** across **all** subplots.
❌ Incorrect. As seen above, when doing `sharey=False` (or not providing a value for this parameter at all), the y-axis are **not discarded**, but each subplot will have **its own** y-axis.  
</details>
---
# Question 4
In Assignment 10 haben Sie mit dem fruits DataFrame gearbeitet. Die Zeilen-Label haben die Namen der Früchte enthalten, die Spalten-Label haben die Namen der Wochentage enthalten, und die Kombination (z.B. Zeile 1, Spalte 2) hat die Anzahl Verkäufe einer spezifischen Frucht an einem spezifischen Wochentag enthalten.
Sie möchten nun in einem einfachen Liniendiagramm (Lineplot) die durchschnittlichen Verkäufe (Durchschnitt aller Früchte, y-Achse) im Wochenverlauf (über die Wochentage, x-Achse) darstellen. Wie lautet die zugehörige Codezeile?

plt.plot(fruits**.columns**, fruits**.mean()**, ‘m:’, label='Durchschnitt")

<details>
<summary>Explanation</summary>

> 💡 **[plot()](/10c38918e9a84ef79c8040d2fba85e2e#c9af98cf80ba468aa1947825383ef41e), [.columns](/1867045b058343e1a66b677961515907#b56cca6739ca4649ab31ebab1ee61f83), [mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
The **fruits** DataFrame looks as follow:
![DataFrame fruits](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d57f73a4-7024-4ebd-93d2-bca3d6b7d248/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H667MBI%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDgdnY87aQWVfUvx8PT5Sio3arrSrdwLXCtoa%2FJ%2FUdvjAiEAieaAsRZ7o%2FQgrsfvvMDv6OOd84sqPgiGeN3tGx04ZZwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDH5BZIMo78Ntqqyb8CrcA0YuZbMQZAIf2mF%2FgsKt1fjz38xFqLZT%2FrQXysO3siNkX8fcNdJi3T95xPNO3oOE7jjj0T0yYG0T4mMLxQAe%2BcaEFwU2vsG7b2v7pw6nU8qGoJeXihy4yLkmW3r8Lx5LI2H7pN3HitOkHAMgudOUtBYyRyilbRq7rjOpjqm%2B4YoQ7XZr49nOI60JrgwTetS6pzCoFnJ9VbIo2oaBW3QZycW5%2BxGHjtCnz%2Ft0WWWNwQ6bzU9Rqq5aaL2GSfPnzapDWXFgltL69%2BOnN8WIFxAKHqHDIKtdNaF93uKbieZbVHURstxw0N0ZtY1RfqNv1jK1irNkJRS6thQ%2F8HR5dJ4mGne3vH3EL33npYGwOTFmvDQXjEScpaoN4%2FoDXtyHcpgaxVEA1X9NI0uGUQ2tAOERvdNPZnCw2gmHtOepF1JD6EQpTbnGi729LW9%2FZW0kgRyuEnMOkiaOnxUHquq6%2F%2FgRvuFzUVZjcdgPIudh%2Bnw%2BHTBMVWRswdb%2FWSjY7izq7l50zBdjD1B9BiqYoUhwJ99tQfCWwMAexyrsAtD%2FzB7ZMEXY79MHtEfx1oE%2FrGRB85W%2FuMKhRwNoh4Qo%2FPrtAIdWyeR8cape%2BMtxRm637X1%2FAo82SMQvC60Vdf%2FcirGeMI3O98kGOqUBkkMQpMuD0EmIWop%2FJlEFpOpzHgWnHxNpUQMdOmWmG62gskFltd6rPeiDeBHEgFGDGbs24sDk7HSTnbgM9zNfAFStSP68Aoxqn7P1hGai0tgeweYAk%2Bkq%2F5XixdmbondUHcVwg1WlCORvAwOUAW7md2SX%2BzK0bJkRQ0v7iwdUp5s6GqHTbc9W%2BbHSfbZ2G3LVfUYrGBYlIs5yHeL3dxit3zJh5pTl&X-Amz-Signature=1c04147c2bfe97518335005c25491685824182b0e2d1a29bd069631e34bfe4be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And the Lineplot that should be generated looks as follow:
![Lineplot showing average sales per weekday](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/844d157e-d8b9-4553-af0c-192d8b1f77ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H667MBI%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDgdnY87aQWVfUvx8PT5Sio3arrSrdwLXCtoa%2FJ%2FUdvjAiEAieaAsRZ7o%2FQgrsfvvMDv6OOd84sqPgiGeN3tGx04ZZwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDH5BZIMo78Ntqqyb8CrcA0YuZbMQZAIf2mF%2FgsKt1fjz38xFqLZT%2FrQXysO3siNkX8fcNdJi3T95xPNO3oOE7jjj0T0yYG0T4mMLxQAe%2BcaEFwU2vsG7b2v7pw6nU8qGoJeXihy4yLkmW3r8Lx5LI2H7pN3HitOkHAMgudOUtBYyRyilbRq7rjOpjqm%2B4YoQ7XZr49nOI60JrgwTetS6pzCoFnJ9VbIo2oaBW3QZycW5%2BxGHjtCnz%2Ft0WWWNwQ6bzU9Rqq5aaL2GSfPnzapDWXFgltL69%2BOnN8WIFxAKHqHDIKtdNaF93uKbieZbVHURstxw0N0ZtY1RfqNv1jK1irNkJRS6thQ%2F8HR5dJ4mGne3vH3EL33npYGwOTFmvDQXjEScpaoN4%2FoDXtyHcpgaxVEA1X9NI0uGUQ2tAOERvdNPZnCw2gmHtOepF1JD6EQpTbnGi729LW9%2FZW0kgRyuEnMOkiaOnxUHquq6%2F%2FgRvuFzUVZjcdgPIudh%2Bnw%2BHTBMVWRswdb%2FWSjY7izq7l50zBdjD1B9BiqYoUhwJ99tQfCWwMAexyrsAtD%2FzB7ZMEXY79MHtEfx1oE%2FrGRB85W%2FuMKhRwNoh4Qo%2FPrtAIdWyeR8cape%2BMtxRm637X1%2FAo82SMQvC60Vdf%2FcirGeMI3O98kGOqUBkkMQpMuD0EmIWop%2FJlEFpOpzHgWnHxNpUQMdOmWmG62gskFltd6rPeiDeBHEgFGDGbs24sDk7HSTnbgM9zNfAFStSP68Aoxqn7P1hGai0tgeweYAk%2Bkq%2F5XixdmbondUHcVwg1WlCORvAwOUAW7md2SX%2BzK0bJkRQ0v7iwdUp5s6GqHTbc9W%2BbHSfbZ2G3LVfUYrGBYlIs5yHeL3dxit3zJh5pTl&X-Amz-Signature=b90d7f407017ac86c6d1925c89c7531cb52fdce6cb5d02cf6c38859b4b8bf350&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
# Question 5
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
# Question 6
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
![Positions on x-axis of `data_y1`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0e86d183-723f-43e8-8a93-b286b4064a26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXGA4ARZ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCID1SnhtwsEPNt%2Fbqki8I%2Bi16qHAYbovtiMV%2F%2BylUQqpIAiEA9pW2SF9Ybt9dykxY%2FYso6MQRdf4Yq4k88ePrgDmAOmgq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDF60VtmICayg29QtsircA8DbNYqgWRqRyh5uJof6K3Da48TrVCMnURToPLUMevuMgQurIfytzCJdOnQRlfR2AddzyyO7sggsfP5sNIa9oU3%2BNm3Eafg2P8GBNMKui2Bkx9QoM8juZkrjTfwv7W6pIqu7unS2FYKNl8mYO9JwovM%2BL2XEVdvEjjgWBS%2F9G%2FpQzs8Mm3%2BiUGx4kYhsxPCom5XPSuc5qvub%2F8%2BP3qyKe4gqutk1oEhXAexS5eXgLGCFVN4t3js6XBOPklB74fAfZ57XPN4zKo0jcfqwoUMuqmZ0szYQ9DZrM8z%2F5DwveTcRfXAUJ4m2M4VLXgkTKxTSLn9ar8x4qotW3JpVFy0r4hBpIuLWxOOzhKA%2BcPsZShLixeN%2B0ZtqR4cydgSf35XIhWEEFgEvKqrKoBz9UxicUq26yVcBlS8ygsbXZhTIqdBPb39u3tI3oxvJb9uRonJ%2FanGgVatyPLljxyclTi5fjjQPqIMmv5wd9s3ZyMat8tSkt9H4dGixscxB7a%2BQg2ny%2F%2BgwEj8YN20kGhrDH0hT8nwkus1s5ZcykneidHv%2BM%2B2vvL6N5PcacbL5bsa4Hr67qxg3MKwWtb2pNCI2SBxnCMW8k2VnLlQBWRLa88hrf3Z1uWZnf7VG27jtDdczMP3N98kGOqUB76lIJoc3JoQYT4wfD4x8C5WxdqvekE6bZlyYLInzvovw9UKvwH2plwtEOInOHX8Wx%2FBJMhFFcBceqsgHYvNgL1We9wZP5tvBo86AbhGg%2FfjaT23BE17qNrz3kPEsymgjg2bleed7ggkq5rM056EvWXjfG0pjOhH3fODHy9U2w1iDuI4GjFY7n3noHLV6sHUWHEIfM1DQiyUQMdNEXx4%2BJyLZ4Wx1&X-Amz-Signature=2b6fdd630b76f2ef71d5a43672083ee8915c6a0424b4320c549217a1f1192ba0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Output when using `width_1 = 0.6` and `width_2 = 0.6`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0a3532b8-7d9d-4d1d-91aa-479f5c2ed59c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QWOYGST%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDf4v3SLw59yLn7BVjBuNHwYcSPubBxYAQXUE6SXScp6QIhAPQ%2B6Oc52fIGWRPpaXg7Uivfshi9TMUyNW0CMcT2SjUrKv8DCCoQABoMNjM3NDIzMTgzODA1Igy%2BVCSqebUcbgEIq1wq3APtiz%2FsUa3749nrNT5oUx7sU50U2%2BpeypiTOoIVHTKduXI0bs1iyaNxDBUrvB52LAXggixHggyGDAKuWGVlVH5UBts05p78PD%2BUqNwRy%2FKtRHzPlEziES7W%2BrmzsKuDJTPlnKp%2BrBYv0YMl9h3yVdCVF2dJLS7vB4L3kFu%2BB0TjWt2oOPz3%2F1ZUbi1QatzhFt77RZb0shT%2FIQ2rO82QB2QBbkRnyHiAgqnwWcn4zpLlyhEulOFqOaf%2F%2FVVOhSD584JP1erTzUJF5EOiYvnr4wlzi%2BqcW%2FT0LPd%2BoEwAO%2FteUHCqGbUXpdTKKcB2Hu0hUQVBeOD5XlVBERtPWlG3%2FJkeVrSrnNpEu0V1i%2BZUKTMIam0JeYwvy7RXGirz1TFYxqg07djSkVk3Xm2jrQi6OD2XQh6FUrwnXSOXh6mIJiDKeXXYUtoXnyKtAy6TOyS3%2FMIt1Cojfly9a2rgCqFrltxdBRi9Ejml%2FhKUQoAXvq5Fu%2FJb6oPNEdWhki953NoChm9JMrkCv%2FrG5%2BcScTvhxV9hQYTueasaYlIyVUEsBuZcVu%2Fscn0RQ%2B5z9A8244ZmTXTOIUhmeEglen%2B9PlqjfClfmjzKmWQy1wiYTl%2Bq9ih47N13gFhFUt6%2BRGWlizCLlvjJBjqkAZg9cw2r4S%2BWvpmLXCCTMg3QDhZ3yZbzXCQ5e0qKzo%2F%2F7O%2Bg4HgxXFib%2BpnOP%2Bd3XDW4BvknDLszN38KYFpaOk047LhF5SiX0DvVa6yihmEL8JNOruzc5%2BG7ypPj98sAmnaYzEByHfm6I7UyvIlwSy5fBBXDaMveHS6R7QL2e%2FsUVkAo64r2LEtzKnvcBZQxIQ%2FswTDG6uAq%2BJGrOcVdIQ7Q7Asq&X-Amz-Signature=5f98ff9d4fd42c3460be72e0345286de69ea5b5795621d1bb47c54281fa6fbae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Output when using `width_1 = 1.0` and `width_2 = 1.0`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d1f8d14e-3260-4c15-841e-a8f5ad99de5f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MCAMX3N%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIA0c%2F5I0kfn2VIQ9eDEeww5oDH0%2BulSYFb%2BnbxlAWUsnAiAe365A%2FruorCUkiIpRK6vfLK%2Bippe%2BN6f9IaEPHwM65yr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIM9k3K2lwkFLn6CsAUKtwDKPTxN8wN0uw72gwUpsQY8Y4mSuHlBjFseJ%2F%2BbpdcupOyb4T01by0mavs%2FwUWvBlqERzf5cAmrcay0awFuoNYgh%2F2uk2QqgIiao%2B1Rt7FJ3rKz753irHG8FlgfycSpbjkfRyrKh1XIuVb1RoNRmZ2LrDV1QNLOh8mp7q7G8TzYLw%2FfkgBxW05a%2BPzAJ6xh0Ni4R5%2BDa9CE3qEJVvgahiQrKBqyHpCXFtghD2jH43skyXKRBFxIfmpD7pBEPjnBKfHhWJoqDPYmOJuXN8m%2Fv6zF5VEAJ93%2BQkJ7AwymRg7y1rBtWBYdWUdiXGFDQzx1iXSA9SEWa3xzg%2B8GzHs0wSPfaFM4stQ3oWDeFNx0kNxYyjsE1PtXqXN1rj7B6WQf6eoE44MzmXy541juvlOiEtNLmF%2Fgo2olFVv9R8zbaO8%2FrpUqVbuARN2VInz7uQLS71W17V71oDw9%2F2u3NZXeDScG4lzLakAVA%2BrK21L1B7tOX7Mt3GWT1YB2ALydyyotF8Hw81iwUV792cttku2jEXjEs3dfW9yEkafjEi5n%2BP%2BR4p4Q7pvxY5eIl1ChWpha%2FwoqTzHcbvEljqeVXNDTzNYuw2jl7vIJAJAHTTsF0Ap7UcEZ1ssh4iW7sh6t6cwkpb4yQY6pgHu5UpvI5qdxhY%2F%2FQA%2B4n0qoAHs%2B60RbgEUOOq%2BIublhIjp05frYPAtPlDyg5FwJ51kqA4wXTA8Vi7uAH%2Fr33imIGkMqGn6qkrkeeyjptIcz2TtJQvRF2lhxuxexbXA1PKe6ClOTANMU27UL8DDfZ6t%2BCmJLUm2hwMk%2BCPyVRBvrYceWY9hMQLRGCCS6p1AifRRXuHWZW3X%2F%2BXjofY%2FDSRkUU%2BA21oC&X-Amz-Signature=a9ee805f967701a2c9b8de1b039946d960e530c23bb06e0b407ffe61986b75c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Output when using `width_1 = 0.3` and `width_2 = 0.3`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3d9aa130-4908-4a45-8f67-21824f1a2471/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEMD6EBO%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDESs8g7CTbM6JYmeopxMbpuc%2Bj9btcgypAbQatDJGlcgIgKYNv41tCK6K%2B53tuSyHQZqS%2BEvmFKmOl%2Ffv%2BmF2V4rQq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWTc41Hcg21QS%2BHYircA%2F21crCrdmXZcm2UH5OLnP3cqBF8c20Z5G0IL%2FpyQ2M7scmZsxSv5tDytQgfAhxObXN6GeTeYPv32vqkWT6FjQ3ZvW7jnNYSfM%2BYnRJhboSA11cpcPJlGg2VqA%2B2WMUl0sMLm7HweA9ibuM5MB8hJlg%2Ft2%2FnMYIaGvcHw%2Bul1m%2BGy0Fqs9XWr4OBdld%2BDM1ozIHCZ7hEWPxwQWBFNhJSKFIQJH4UMd1VwdTSC7MOQ%2Fo%2FRGkHjOB9yYx6q2GUl9mKXE1EkEJa%2B%2FVC%2BHf1P2UueU2zr5iobFqXkb2oqqW6X3iyjCgrubFXML7azJJaYSIAgXXkQa%2B%2BGfdSAR%2FevolwarQIHMbV1pqmqmhz2TM7x550OyytyZ8rL%2FrI79OdnBJy%2FDaljJUImraAKFBU6lHS5ZGVdyuYURoVHvMat1Ca6QU4KzjICZrLX3VMAjE4BDuNqWy4cqRKTdzi5Xklms5R9Ac92ytPsaqzGNnR7%2BnknvaC%2BVoh5Gl39KdBKQs4X18mp67vXsXY%2BpNAPrR3OEKWXwUcNtK5x9s%2Fo1ksDp%2F4ZSDVRnmH1UsWHPLS4Rp6UAeGeObv85ScHSmfu0W7Cz0Wo%2FhTwgZy3twqdqwxnWC3nIWIYRNiHmLNNpAMSk1HMMDO98kGOqUB1pspnP6JCd3bUbqrdPNAQBZR78eMQ9ImCvAI73LNgy1pj1RyCy%2Bn3zVTSsNDw3%2FgIwwhtqtK7GCbWMnmlwI5lvly0lG3BD3j%2BFxzeO0Nv7LZaZIDkd0Fl55TaKx1CTqQE2H8ilE6SYPIP1VITE%2B5VyNPuMjCW2%2Fayor6RES1k9dqnP3KE3lqspbUEYEosS7T3YhctAoIV2S%2BpxeTPauSYMoebiwi&X-Amz-Signature=7f97370b1dfe0cb9ac2b465695dd6a11c604050e76f5513dc13ec0c194cab2ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Output when using `width_1 = 0.1` and `width_2 = 0.1`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b54fa942-f8ae-42a6-b581-af1c834b2598/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VL5SPXUN%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCfjEoyYC8QduOXXprGYs9ZKVE9vOrKncGkOZ0Fvo%2BfNAIhANajR0Dls7Frrhov5DJx%2FKTTGZJddMM4HirVfkzut2G9Kv8DCCoQABoMNjM3NDIzMTgzODA1IgxgOKKa1NMCPjjn72Yq3APr%2B5HOqtFfRo%2FGIXuxPMKfN0zjK3V9E5WMPWLU2AJzNdF0YftMe2BfWR%2F1RjzWfCnBEAku5PJbi%2FsdkLWELQMgiEdIxBWebIwddikqi%2BmO9ChwjLyiSpByfF9npTu60E8seu5mna%2BcNcTdjDW%2F3VE3n%2Bcd0KieG9jmF1NmWqxlyEqdmBFLev51Z8m8ODHjlv5SiXnYCbWJqcIBDblnNEnTewU3NkaSvGCSOMu1amD00tjfRmFN3U39zrVLO9kDFHPdJWU%2BM%2BEl%2BOXUxsSsc0pNhngmz8BwmWSxQuqX1J3txB7u3WuKR%2BN792uVg2TJGllpGOcjj96Hk6lI9Jos5iK6a4b5BunPLqsI4UMm%2F%2BAzoImgGOn4kPXy1pbctbr13oQ44mvpl5RpdrADORYucQj2xRbz85kUwCaF4X9fOml4FnO7GE68iRUGrI80dcPhDv0mhB%2FsUmaILZqh2kB1VZ0MPwjyX2LUoreGSi9e9xqrN2JmgEN15IQiotiSOw2S5CIax6DTwMOxyGY3xSRxQBVsaBH8z%2FtTsiL3Fd8GYVP%2FrtbRA3nYAKjgGNVCJDFNEPlJSmPCfPwspiwj9RKx2mH2R%2BZbCUbyZyEqW1auA3PC4CyKZBCjGbLxCOnbljCGlvjJBjqkAQAxD02DSmD2laaI9dZUHDyYg5qYcuYpWf2x8zNpvhPUNAZPLnkEAYwvR5yU4bORSlXcvdXbHf4BHm3jVRlUTs2Lv%2BPuTtcihJV1%2FJ0hNDL4y5mZ8DFwkJyDaajx90f4X7re0vGtnwK0VGDEerdBA2GOhJPQTHgc%2FM5jiEFVi2yWcHOlC8uEQkDCiDjAXU1rrcdg%2FdDS%2BgzpLAcu8cmWl598hfaT&X-Amz-Signature=6d63b02ec8e1f95d5ef999ad45a9a33c08e72e518c87fd2395e3e0b616cee2be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Output when using `width_1 = 0.5` and `width_2 = 0.4`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c8e54f56-f26c-446d-947a-35788889e1d6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ARJ3TCP%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDmy2t2grgaWGVwUqUPoOlmOOL5XAkElL3WmobIGuCSsgIhAJCELnqttXImWggTE3dkWroSgieD%2FrIh38ROUsyguh%2FXKv8DCCoQABoMNjM3NDIzMTgzODA1Igw%2BIARUolCFwyn9TFUq3AMuT2gv9ekUSV8eNWZnMB53DvOmXqf8SQ%2FrQYsysCYWBmrRf2klTbZEE1Gfg%2FyUtkpZ8uVrbpiPGqkdxtemp6F7uspjm5pCiMKnGXRJ8KGFG2wjGId7DV897%2FYLDyUGSDQfJyCDbPX0Vw%2BBLhLK%2BFLIveL6dI1008tG3%2BS9WlLvge%2Ft%2BxATKSxd24uVgta9OCKI6lDQ%2B2Gm4wKB2ydpMHkL5iMewwhQBj5M57iLD9fBmpyjABQawynjy63y3Nwxhtg4sQYdmn9UuTBv%2BdVPAqTo0eQSsMEixFhQlKsXGLLDypdNmO4EcH7s7%2Bb6pVj3JbtkuVwQ%2FUt920yn7zQLfHuMiXTWePyks6dCiA1NYgYD8UvKgGwLUmAOy6X0iThkoDtb5zVsBrmSGpJ4QXUf6r6vsp75zYvFmpIaSKuyVe9IbL%2BpAzZWrinRAJ7FHIeWFoR9KfS553K2boYAGHtNml%2F9rLaYdUhGqJUvmgQjBnuVHfMHwhZLOpEAotqlnZSEv4V3CfJ15EoRfVm4zVH3YvMXZ%2FfY9x2dC4SKwB%2FhewyqyF9ciEQcX4zxjrQle5ix1iGbP8NCug0wsPdnne18g2NTbVZ7kSW9jDaIaYhrmtmikB6rHQbbduNYvY83LTCJlvjJBjqkAX%2BJ%2FE9DAefz%2F2gI12mPEqEsnvWFMSstLGzIXKbamnCClOXw0x1pj%2Bxu%2By9w2M1WpauODL5fDYVPvSQXOG%2FRP7aJN1to5qD3QzF%2Bs1ACqqyq644wb4%2BE1GBIQNULxGe82f3zFT049sLM7K8VEpekpGmbA8tEgQx%2BHuZjT2zPQ06s%2BL7%2B%2FPe5VQBIU%2Bhtqk64x7YX5AzGSRcUhz10UJDHx4YD4PF3&X-Amz-Signature=28d1040ca5d6f8367103cfcfa463c587f23d072300cecd41cb4f3ca6bba61616&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![Output when using `width_1 = 0.4` and `width_2 = 1.0`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3a9c70a3-e6e1-4800-b8e8-1bc30573319b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WODTBOEW%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCR5iSQpKcYAt3iFqvpTk0RZbsEMcV6IaRjT8tyOItqBgIgZihqwLXs1zrz1hS59uOjD1QnUVPb9t0nR7EohQyw00oq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDNWzz6N5uHspZ6SYFSrcA1tjg43GOqWvFcc91h8AgBDc8h2Ylhch9c0IgPWkepocvfd7vSDab5zsrzFig6nW00Zsjvf2vBo3T4yTIWRjHpXqA6kWi%2B3xdtrxtMSiSk09qNL4UoP5eKa3cPcW7HK1dKYn8yS6itWHNlr4oU7x7rVkGshi%2F6RrQ6HwdW2VebkmHtMCzszLofTZ%2BQlJK1fRInAzuhK44kHyAw4NNF95BMTr%2FfId7OueJaZ4scxOxlMMyvcDA7U41u3creb1vl9xr%2FvtTWTIPjqa%2FOTbCwqrDF4RXaaRWJ46nay%2FBBO15UTffAzA2QtFrabYIxgGTOTLXvIJxmT7atSYxLCkxP6Vw%2F1gqmFQAbp3QjwYwt68gKV4ifhf7qagfS2hG6bWSXP1n%2BUn%2BAbd83258y5u9z6lJ6nbv9r6O0H4FZEHpAfU8Fnnv9GivB6ZODLFicJ1NeiiYfHlMgOxBxyLJLd9WBS%2BI17xrQSZ3UwKARnj7z8HNNwV%2FtNO771jvfkFFdISfDZdqL6exjytWHd2avmqevz5QtaY2wUkR0v9Vj7HootYZqpzSxuQxMumnfKzP5SonDcbARJPM9sXAhxWjE4Vf9mad9i%2BPKV5GP3xEBLeb7MOjUWsZ2cpakdPg5Jq2gO3ML%2BW%2BMkGOqUBzrmThI5gBckj4alWMFIujdVoQj%2Bk0fTFsacgEeOFcf0Ze4qye6Y%2FzHfVptnR8I0KRJaazDTiXXfTbtSOtX8v0hZpnhVPIkCKmmXh1SPS5u9S%2BXTapxbpvRbuumDk2rTPnprMYNNojjt3WWAvJtkUL86Va%2FEkJgJejL8Wdq4PB%2Fv5eNjkvArlxxHHawM4C57hEAvJaJQweiybAackKrPlnTa4iidG&X-Amz-Signature=07ee97d4b3d6d018ac1ec3a7c5b7a91a8d9f1c3489139fb8f1902bac6efe9662&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
</details>
---

📄 **[Quiz 11]** (subpage)
# Question 1
In je mehr Dokumenten ein Wort vorkommt, umso höher ist die Inverse *Dokumentenfrequenz (idf)*. Wahr oder Falsch?
❌ Wahr
✅ Falsch

<details>
<summary>Explanation</summary>

> 💡 **[tf-idf](/ac27cea2b4b741a7b9ad41c16767e1d5#3380ebe081cf4aa9b9e54fe6714fc829)**
The more a word appears across documents the **less meaningful** it is for assigning a class (e.g. positive or negative) to the document. Thus, the **idf-score** of a word that appears often will be **lower** compared to a word that rarely occurs.
</details>
---
## Question 2
Sie entwickeln ein maschinelles Lernsystem, um den medizinischen Bedarf von Patienten vorherzusagen. Sie haben 100 verschiedene mögliche Behandlungen, die Sie aufgrund von Patienteninformationen zuweisen können. Sie haben festgestellt, dass die Vorhersagegenauigkeit für Patienten mit seltenen Allergien tendenziell geringer ist.
Welche der folgenden Aussagen treffen zu? Markieren Sie alle richtigen Aussagen.
❌ Die seltenen Allergien der Patienten werden besser ignoriert und nicht in das Modell zur Vorhersage einbezogen.
❌ Accuracy wird als einzige Metrik verwendet, um die Leistung des Modells bei der Vorhersage von seltenen Allergien zu bewerten.
✅ Training- und Test-Set sollten disjunkt sein (kein Datenpunkt befindet sich in mehr als einem der zwei Sets).
✅ Sie verwenden eine stratifizierte Aufteilung zwischen dem Training und dem Testset, um die Genauigkeit der Vorhersagen für Patienten mit seltenen Allergien zu verbessern.
❌ Bei dieser Aufgabe handelt es sich um eine Regressionsanalyse.
✅ Bei dieser Aufgabe handelt es sich um eine Klassifikationsaufgabe.

<details>
<summary>Explanation</summary>

> 💡 **[accuracy with imbalanced dataset](/3ca737faa7034fb9b1150be74f7f4430#78718402c90345c3b48288c2366ce503), [train-test split](/ac27cea2b4b741a7b9ad41c16767e1d5#3f214527ee3f4c38bc6e506187a44555), [classification vs. regression](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617)**
❌ **Incorrect**. We should be **very careful** with excluding outliers, i.e., patients with rare allergies. Being able to predict rare allergies was maybe the core motivation for developing a classifier in the first place, so by excluding these patients there is no reason for developing a classifier.
❌ **Incorrect**. The rare allergies will likely be **under-represented** in the test data. Thus, the classes will be **imbalanced**. Whenever we are dealing with an imbalanced dataset Accuracy is likely **not the best metric** to measure model performance.
Let’s assume there are **100 patients** in out rest dataset. **95** patients have a **common** allergy and **5** patients a **rare** allergy. Now, in all cases the model predicts the common allergy and we get an accuracy score of:
$$
\text{Accuracy} = \frac{95}{95 + 5} = 95\%
$$
In this case the accuracy score of 95% indicates that the model is performing very well. However, our model actually has **mis-classified all patients with a rare allergy** and thus performs **very poorly**. Hence, the accuracy score of 95% is **misleading**, which is caused by the **imbalanced** dataset.
✅ **Correct**. If observations are in both, test and training data, our model will be **biased** as it has seen the solution before solving the exam.
✅ **Correct**. It is advisable to split the data between training and test dataset with some degree of **randomness**.
❌ **Incorrect**. This is a **supervised** classification task. We have a **predefined set of classes **(the different allergies) that should be assigned to observations (patients). Regression analysis is used to predict a numerical value such as the remaining days the patients have left to live. 😢
---
</details>
---
# Question 3
Gegeben ist folgender (partieller) Classification Report aus *scikit-learn*.
|  | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
| setosa | 0,85 | 0,92 | 0,76 | 18 |
| versicolor | 0,93 | 0,93 | 0,93 | 14 |
| virginica | 0,89 | 0,85 | 0,87 | 13 |
Einer der F1-Score-Werte in der Tabelle ist falsch. Berechnen Sie den richtigen F1-Score für die entsprechende Zeile. Geben Sie das Ergebnis auf zwei Dezimalstellen korrekt an.
**0,88**

<details>
<summary>Explanation</summary>

> 💡 **[f1-score](/3ca737faa7034fb9b1150be74f7f4430#9aabbb38114445a694155a99c1818adf), [precision](/3ca737faa7034fb9b1150be74f7f4430#8f3e40c59c36482197bc746cf80dbc50), [recall](/3ca737faa7034fb9b1150be74f7f4430#5ef7c9301e424eaf85bdfe87d032c836)**
Check below the calculation for each class in the IRIS dataset.
**Setosa**
$$
\text{f1-score} = \frac{2 * 0.85 * 0.92}{0.85 + 0.92} = 0.88
$$
**Versicolor**
$$
\text{f1-score} = \frac{2 * 0.93 * 0.93}{0.93 + 0.93} = 0.93
$$
**Virginica**
$$
\text{f1-score} = \frac{2 * 0.89 * 0.85}{0.89 + 0.85} = 0.87
$$
We can now see that the f1-score for **Setosa** was not correct. It is **0.88** and not 0.76.
</details>
---
# Question 4
Ordnen Sie folgende Probleme der entsprechenden Kategorie zu. 
Klassifizierung
- Wine-Datensatz
- IRIS-Datensatz
Regression
- Vorhersage des Aktienkurs
- Kreditrisikovorhersage
- Vorhersage der Länge der Blüten für den IRIS-Datensatz

<details>
<summary>Explanation</summary>

> 💡 **[types of machine learning](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617), [datatypes](/8abd5dae91fc4e90b63453e6d4a80952#058e2f9345364edcb90e0a46f4ba6c36), [regression](/3b0dfaa603e642b498b666d147d66714)**
Here we need to ask ourselves what kind of data type we want to predict?
- type of wine → <u>categories</u> → **classification** 
- type of flower → <u>categories</u> → **classification** 
- stock price → <u>numerical value</u> → **regression** 
- risk score → <u>numerical value</u> → **regression**
- length of flower → <u>numerical value</u> → **regression**
</details>
---
# Question 5
Sie haben in der Vorlesung *k-fold Cross-Validation* kennengelernt. Welche der folgenden Aussagen treffen zu? Markieren Sie alle richtigen Aussagen.
✅ Cross-Validation kann helfen Overfitting zu erkennen und zu vermeiden.
✅ Bei der *K-Fold Cross-Validation* wird jeder Fold genau einmal als Testset verwendet.
❌ Jeder Datenpunkt kann mehrmals als Testdatenpunkt in K-Fold Cross-Validation auftreten.
❌ Bei *K-Fold Cross-Validation* wird das Modell nur einmal trainiert und dann auf einem einzigen Testset ausgewertet.

<details>
<summary>Explanation</summary>

> 💡 **[k-Fold Cross-Validation](/ce8b46807fc14f28839eb7b27e773558), [Overfitting](/ce8b46807fc14f28839eb7b27e773558)**
✅ **Correct**. By splitting the training and test data into **multiple folds** and running them through **multiple training and test iterations**, the risk of having similar data in the training data decreases. As a result, the performance metrics (accuracy, precision, recall, f1-score) are more **robust** / **representative**.
✅ **Correct**. Each fold is used once as test dataset. In the other training-test iterations the fold is part of the training data.
❌ **Incorrect**. Observations are not duplicated, i.e., the underlying data is not modified.
❌ **Incorrect**. The model will be trained and testes **k**-times. Each fold becomes the test data in one iteration.
</details>
---

---

