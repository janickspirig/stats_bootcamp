---
title: "Quiz 2"
notion_id: "86d6e1ca-e688-42f4-995b-bd3841ef8b29"
notion_url: "https://www.notion.so/Quiz-2-86d6e1cae68842f4995bbd3841ef8b29"
exported_at: "2025-12-14T01:06:11.630877+00:00"
---

# Quiz 2

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

