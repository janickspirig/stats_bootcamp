---
title: "Quiz 3"
notion_id: "9b034204-5546-4204-b6b6-79519a305a5f"
notion_url: "https://www.notion.so/Quiz-3-9b03420455464204b6b679519a305a5f"
exported_at: "2025-12-13T23:11:47.594339+00:00"
---

# Quiz 3

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

