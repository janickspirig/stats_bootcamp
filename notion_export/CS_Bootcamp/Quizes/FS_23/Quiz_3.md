---
title: "Quiz 3"
notion_id: "dfa7a813-7dff-402f-9bcd-ed5d8a28adda"
notion_url: "https://www.notion.so/Quiz-3-dfa7a8137dff402f9bcded5d8a28adda"
exported_at: "2025-12-14T01:02:22.533851+00:00"
---

# Quiz 3

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

