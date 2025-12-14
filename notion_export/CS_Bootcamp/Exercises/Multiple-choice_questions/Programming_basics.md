---
title: "Programming basics"
notion_id: "99b7b2f7-8288-4ce9-8c4e-7f4d183ac05c"
notion_url: "https://www.notion.so/Programming-basics-99b7b2f782884ce98c4e7f4d183ac05c"
exported_at: "2025-12-13T22:55:14.407470+00:00"
---

# Programming basics

---
**Lists**
In a list it is possible to store values of different datatypes, i.e., `[True, 0, 'Hello', 5.43]`
is a valid list. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Lists**
In a list it is possible to store values of different datatypes, i.e., `[True, 0, 'Hello', 5.43]` is a valid list. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Lists**
We have defined the following list:
```python
biggest_cities = [['Geneva', 'second'], ['Zurich', 'first'], ['Basel', 'third']]
```
How can the String `'first'` be accessed?
1. `biggest_cities[0][1]`
1. `biggest_cities[1][1]`
1. `biggest_cities[-2][1]`

<details>
<summary>Solution</summary>

`biggest_cities[1][1]`
The list `['Zurich', 'first']` has index position 1 → `biggest_cities[1]`
The element `'first'` has index position 1 as well → `biggest_cities[1]`
**OR**
`biggest_cities[-2][1]`
The list `['Zurich', 'first']` has index position -2 from the back → `biggest_cities[-2]`
The element `'first'` has index position 1 as well → `biggest_cities[1]`
</details>
---
**Strings**
It matters whether strings are enquoted as "some string" or 'some string’. True or False?

<details>
<summary>Solution</summary>

False
</details>
---
**Variables**
Upper or lower case of variable names matter in Python, i.e., age = 5 is not the same as Age = 5. True or False?

<details>
<summary>Solution</summary>

True
Variable names are case-sensitive.
</details>
---
**Boolean**
A boolean variable can only have two values, True or False. Correct?

<details>
<summary>Solution</summary>

Correct
A boolean variable can take on two values only: True or False.
Remember that True is the same as 1 and False the same as 0.
</details>
---
**Dictionaries**
Which of the following statements is wrong about dictionaries?
- Elements in a dictionary are accessed by their key
- Elements in a dictionary are mutable
- Dictionaries can be nested to any depth
- Elements in a dictionary are access by their position

<details>
<summary>Solution</summary>

Let’s assume we have the following dictionary:
```python
city_population = {
	'Zurich' : 400000,
	'Basel' : 170000,
	'Bern' : 133000,
	'St.Gallen' : 75000
}
```
✅ Elements in a dictionary are accessed by their key
```python
city_population['Bern']

133000
```
✅ Elements in a dictionary are mutable
```python
city_population['Zurich'] = 450000

city_population['Zurich']
450000
```
✅ Dictionaries can be nested to any depth
True. We can have multiple nested dictionaries. However, at some point this might get really complex to maintain.
❌ Elements in a dictionary are access by their position
An element (key-value pair) in a dictionary does not have an index position. I.e., we cannot tell Python directly to access the value associated to the first or second key in a dictionary:
```python
city_population[2]

KeyError: 2 # there is no key 2 in the dictionary
```
However, what we can do if we want to access the n-th value in a dictionary is to use the `.keys()` method:
```python
keys = list(city_population.keys())
# ['Zurich', 'Basel', 'Bern', 'St.Gallen']

nth_key = keys[2]
# 'Basel'

city_population[nth_key]
170000
```
We can see that first we retrieve all the keys that exist in the dictionary as a list. Then we extract the second string value in this list and access now the value that is associated to that key.
</details>
---
**Functions**
Functions accept required and optional parameters. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Functions**
The order in which parameters are passed to a function does not matter. True or False?

<details>
<summary>Solution</summary>

False
It matters. Assume we have the following function.
```python
def greeting_person(first_name, last_name):
	print(f'Hi {first_name}, {last_name}')
```
The value we pass as the first parameter will be used as `first_name`. And the second value we pass to the function will be used as `last_name`.
```python
greeting_person('Janick', 'Spirig')

Hi Janick, Spirig
```
If we want that the first value is used for `last_name` and the second for `first_name`, we need to assign the parameter values explicitly: *`<< parameter_name >>`*` = `*`<< value >>`*
```python
greeting_person(last_name='Spirig', first_name='Janick')

Hi Janick, Spirig
```
</details>
---
**Functions**
Lambda functions can be re-used multiple times. True or False?

<details>
<summary>Solution</summary>

Lambda functions are anonymous functions that do not have a name / definition. Thus, we cannot re-use lambda functions. If we want to execute the code inside a function multiple times, we need to define a regular function using the `def` keyword.
</details>
---
**Logical statements**
If there is an if and else statement , one of the two will always be executed. True or False?

<details>
<summary>Solution</summary>

True
If the condition following the if statement evaluates to **True**, the code inside the if statement is executed. 
If the condition following the if statement evaluates to **False**, the code inside the else statement is executed.
</details>
---
**Logical statements**
Let’s assume we have multiple elif statements. If multiple conditions of the elif statements evaluate to True, the code inside all these statements will be executed. True or False?

<details>
<summary>Solution</summary>

False
Only the code of the first elif statement that evaluated to True will be executed.
```python
x = 7
y = 5

if x < y:
  print('Greetings from the if')
elif x > y:
  print('Greetings from the 1st elif')
elif x == 7:
  print('Greetings from the 2nd elif')
else:
  print('Greetings from the else')


'Greetings from the 1st elif'
```
We can see that the conditions of both elif statements are True: `x` is greater than `y` and `x` is equal to 7. However, only the code inside the first elif statement is executed, then Python exits the logical statement.
</details>
---
**Loops**
As soon as Python encounters the break keyword, it exits the loop immediately. True or False? 

<details>
<summary>Solution</summary>

True
The break keyword makes Python exit the loop execution and jump to the first code-line after the loop.
</details>
---
**Loops**
As soon as Python encounters the continue keyword, it jumps out of the loop immediately. True or False? 

<details>
<summary>Solution</summary>

False
As soon as Python encounters the continue keyword, it jumps immediately back to the loop header and processes the next element in the iterable.
</details>
---
