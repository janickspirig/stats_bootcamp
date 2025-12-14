---
title: "Quiz 4"
notion_id: "11e0858b-d5f6-44b8-84dc-550dd3c6c4bb"
notion_url: "https://www.notion.so/Quiz-4-11e0858bd5f644b884dc550dd3c6c4bb"
exported_at: "2025-12-14T01:01:17.806119+00:00"
---

# Quiz 4

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

