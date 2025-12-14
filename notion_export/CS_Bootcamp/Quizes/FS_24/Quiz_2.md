---
title: "Quiz 2"
notion_id: "9d8c7f02-7230-4583-92ab-077bde0558cd"
notion_url: "https://www.notion.so/Quiz-2-9d8c7f027230458392ab077bde0558cd"
exported_at: "2025-12-13T23:08:51.907917+00:00"
---

# Quiz 2

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

