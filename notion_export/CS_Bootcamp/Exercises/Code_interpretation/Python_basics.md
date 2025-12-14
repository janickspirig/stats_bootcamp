---
title: "Python basics"
notion_id: "daac644c-4c59-40c7-82ae-ffbd609065eb"
notion_url: "https://www.notion.so/Python-basics-daac644c4c5940c782aeffbd609065eb"
exported_at: "2025-12-13T22:51:59.390894+00:00"
---

# Python basics

---
I know, some codes are pretty hard. However, if you get these then the exam will feel like a breeze for you 🙂
No matter how hard the code looks, grab a pen and paper and go through it line-by-line. If you have understood all the topics taught in [Python basics](/5b0832dbf9454eb1941b7632e68a9abb), then you should be able to solve these code snippets.
---
[**Datatypes**](/5b0832dbf9454eb1941b7632e68a9abb#d1c2e1bb9bac46b8afbe6f4f6950edd9)
```python
2 + '5'
```
<details>
<summary>Solution</summary>

```python
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
</details>
---
[`.split()`](/5b0832dbf9454eb1941b7632e68a9abb#82c0353b9ca6493e99478917afa8516e)
```python
text = 'Computer Science is awesome'

text.split(" ")[2]
```
<details>
<summary>Solution</summary>

‘is’
</details>
---
[`.isupper()`](/5b0832dbf9454eb1941b7632e68a9abb#9a11b3028c464a978fd538409bbc3bb1) & [`.islower()`](/5b0832dbf9454eb1941b7632e68a9abb#00591cce76ac44d3bdb5458243b12da9)
```python
text1 = 'hello'

text2 = 'GOOD ByE'

text1.islower() and text2.isupper()
```
<details>
<summary>Solution</summary>

False
</details>
---
[Unequal](/5b0832dbf9454eb1941b7632e68a9abb#fa20c3ae27214b2c97c2d7f1c9257f49)
```python
'5' != 5
```
<details>
<summary>Solution</summary>

True
</details>
---
[Boolean](/5b0832dbf9454eb1941b7632e68a9abb#b0c4461b3a544cad9e004f546fc637ee)
```python
a = 2
b = 5
c = 1

(a > 5 and b > c) or a > c
```
<details>
<summary>Solution</summary>

True
</details>
---
[Boolean](/5b0832dbf9454eb1941b7632e68a9abb#b0c4461b3a544cad9e004f546fc637ee)
```python
a = 2
b = 4
c = 8

(a > 5 or not b > c) and not a > c
```
<details>
<summary>Solution</summary>

True
</details>
---
[Division](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a)
```python
type(9/3)
```
<details>
<summary>Solution</summary>

```python
<class 'float'>
```
</details>
---
[**Modulo**](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c)
```python
data = [1,2,5,3,9,6]
summe = 0

for x in data:
  if data.index(x) % 2:
    summe += x
  else:
    summe -= x

print(summe)
```
<details>
<summary>Solution</summary>

`-4`
</details>
---
[**Modulo**](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c)
```python
18 % 14
```
<details>
<summary>Solution</summary>

4
</details>
---
[**logical statement**](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)
```python
a = False
b = not True
c = 7 > 6 and not 0

if a and b:
	print("Hi")
elif b or (c and a):
	print("Bye")
else:
	print(f"Peace? {c}")
```
<details>
<summary>Solution</summary>

`Peace? True`
</details>
---
[**Modulo**](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c)**, **[**while-loop**](/5b0832dbf9454eb1941b7632e68a9abb#b52a89fc421f4692bdc9c73a764ca650)**, **[**logical statement**](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)
```python
y = 0
x = 0

while y < 10: 
	if not y % 2:
    y += 3

  else:
    y += 4
  
  x += 1

print(y)
print(x)
```
<details>
<summary>Solution</summary>

`11`
`3`
</details>
---
[**Floor division**](/5b0832dbf9454eb1941b7632e68a9abb#7a4d967ac86c4e1f9b4c57989df35867)
```python
if 9 // 2 - 3:
	print('Hello')
else:
	print('Bye')
```
<details>
<summary>Solution</summary>

Hello
</details>
---
[List](/5b0832dbf9454eb1941b7632e68a9abb#5d06cfcdb5574513a592b854a821fe3e)
```python
a = [4, 3, (2, 7), 8]
b = a[0] + a[2][1]
c = (b, (a[2][0], b + 3))
d = c[0]

print(d)
```
<details>
<summary>Solution</summary>

11
</details>
---
[**List slicing**](/5b0832dbf9454eb1941b7632e68a9abb#01370999e4334066ba04335de9ae836a)
```python
my_list = [1, 2, 3, 4, 5, 6]
my_list[-5:-3]
```
<details>
<summary>Solution</summary>

`[2, 3]`
</details>
---
[**List slicing**](/5b0832dbf9454eb1941b7632e68a9abb#01370999e4334066ba04335de9ae836a)
```python
my_list= list(range(2, 15))
my_list[-4:-13:-2]
```
<details>
<summary>Solution</summary>

`[11, 9, 7, 5, 3]`
</details>
---
[**List slicing**](/5b0832dbf9454eb1941b7632e68a9abb#01370999e4334066ba04335de9ae836a)
```python
my_list= list(range(2, 15))
my_list[6:12:-2]
```
<details>
<summary>Solution</summary>

`[]`
</details>
---
[**List slicing**](/5b0832dbf9454eb1941b7632e68a9abb#01370999e4334066ba04335de9ae836a)** & **[**range**](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385)
```python
my_list= list(range(2, 15))
my_list[9:14]
```
<details>
<summary>Solution</summary>

`[11, 12, 13, 14]`
</details>
---
[**List slicing**](/5b0832dbf9454eb1941b7632e68a9abb#01370999e4334066ba04335de9ae836a)** & **[**range**](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385)
```python
my_list= list(range(2, 15))
my_list[9:17:2]
```
<details>
<summary>Solution</summary>

`[11, 13]`
</details>
---
[**List slicing**](/5b0832dbf9454eb1941b7632e68a9abb#01370999e4334066ba04335de9ae836a)** & **[**range**](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385)
```python
my_list= list(range(3, 12, 2))
my_list[::-2]
```
<details>
<summary>Solution</summary>

`[11, 7, 3]`
</details>
---
[**Access nested list**](/5b0832dbf9454eb1941b7632e68a9abb#8526be0c72d1432c83067d8315535bd0)
How can we access the String `'first'` in the following list?
```python
biggest_cities = [['Geneva', 'second'], ['Zurich', 'first'], ['Basel', 'third']]
```
<details>
<summary>Solution</summary>

`biggest_cities[1][1]`
`biggest_cities[-2][1]`
</details>
---
[**Access nested list**](/5b0832dbf9454eb1941b7632e68a9abb#8526be0c72d1432c83067d8315535bd0)
How can we access the String `'BS'` in the following list?
```python
biggest_cities = [['Geneva', ['second', 'GE']], ['Zurich', ['first', 'ZH']], ['Basel', ['third', 'BS']]]
```
<details>
<summary>Solution</summary>

`biggest_cities[2][1][1]`
</details>
---
[**List comprehension**](/5b0832dbf9454eb1941b7632e68a9abb#cf5a90b80642480db120fbbe3f4ea4a7)
```python
my_list = ['Janick', 'Melanie', 'Kira', 'Kristoph', 'Max']
[x.upper() for x in my_list if 'K' in x]
```
<details>
<summary>Solution</summary>

```python
['KIRA', 'KRISTOPH']
```
</details>
---
[**List comprehension**](/5b0832dbf9454eb1941b7632e68a9abb#cf5a90b80642480db120fbbe3f4ea4a7)
```python
my_list = ["JAnick", "Sabine", "HsG", "SchwEIz"]
[x.lower() for x in my_list if "S" in x]
```
<details>
<summary>Solution</summary>

`['sabine', 'schweiz']`
</details>
---
[**List comprehension**](/5b0832dbf9454eb1941b7632e68a9abb#cf5a90b80642480db120fbbe3f4ea4a7)
```python
[x / 2 for x in list(range(10,15)) if x % 2]
```
<details>
<summary>Solution</summary>

`[5.5, 6.5]`
</details>
---
[**List comprehension**](/5b0832dbf9454eb1941b7632e68a9abb#cf5a90b80642480db120fbbe3f4ea4a7)
```python
[x.upper() for i, x in enumerate(['a', 'b', 'c', 'd']) if i%2]
```
<details>
<summary>Solution</summary>

`['B', 'D']`
</details>
---
[C](/5b0832dbf9454eb1941b7632e68a9abb#bd2c733f84784eaf923d8f476187add1)[**opy a list**](/5b0832dbf9454eb1941b7632e68a9abb#bd2c733f84784eaf923d8f476187add1)
```python
universities = ['HSG', 'UZH', 'EPFL', 'ETH']
cities = ['St.Gallen', 'Zurich', 'Lausanne', 'Zurich']

universities = cities
cities[-1] = 'Bern'

print(universities == cities)
```
<details>
<summary>Solution</summary>

True
</details>
---
[**Copy a list**](/5b0832dbf9454eb1941b7632e68a9abb#bd2c733f84784eaf923d8f476187add1)
```python
universities = ['HSG', 'UZH', 'EPFL', 'ETH']
cities = ['St.Gallen', 'Zurich', 'Lausanne', 'Zurich']

universities = cities.copy()
cities[-1] = 'Bern'

print(universities == cities)
```
<details>
<summary>Solution</summary>

False
</details>
---
[**Tuple**](/5b0832dbf9454eb1941b7632e68a9abb#f8cb18a835dd45c1aed5abca3279ba9c)
```python
my_name = ('Janick', 'Spirig')
my_name[0] = 'Elia'

my_name
```
<details>
<summary>Solution</summary>

```python
TypeError: 'tuple' object does not support item assignment
```
</details>
---
[Set](/5b0832dbf9454eb1941b7632e68a9abb#f036e38587ac4bac9bda6d09abc39a30)
```python
my_list = [1, 3, 2, 3, 1, 1, 5, 9, 5, 2, 3]

len(set(my_list))
```
<details>
<summary>Solution</summary>

5
</details>
---
[**Dictionary**](/5b0832dbf9454eb1941b7632e68a9abb#c6da8b579a8040a8b7f209a0ac28380f)**, **[**for-loop**](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)**, **[**logical statement**](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)
```python
predictions = [
		'apple', 'apple', 'pear', 'apple',
		'pear', 'berry', 'apple', 'pear',
		'orange', 'apple', 'pear', 'orange',
		'orange', 'apple', 'pear', 'berry'
]

my_dict = {}

for x in predictions:
	if not x in my_dict:
		my_dict[x] = 1
	else:
		my_dict[x] = my_dict[x] + 1

for key, value in my_dict.items():
	print('Fruit: {}, {}'.format(key, value))§
```
<details>
<summary>Solution</summary>

```python
Fruit: apple, 6
Fruit: pear, 5
Fruit: berry, 2
Fruit: orange, 3
```
</details>
---
[Dictionary](/5b0832dbf9454eb1941b7632e68a9abb#a7ac954b45b441c6ba2cc4fbc81d26ad), [lists](/5b0832dbf9454eb1941b7632e68a9abb#5d06cfcdb5574513a592b854a821fe3e), [modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c)
```python
universities = ['HSG', 'UZH', 'EPFL', 'ETH']
cities = ['St.Gallen', 'Zurich', 'Lausanne', 'Zurich']
uni_dict = {}

for i in range(len(universities)):
  if universities.index(universities[i]) % 2:
    uni_dict[universities[i]] = cities[i-1]
  else:
    uni_dict[universities[i]] = cities[i]

uni_dict
```
<details>
<summary>Solution</summary>

```python
{
	'HSG': 'St.Gallen',
	'UZH': 'St.Gallen',
	'EPFL': 'Lausanne',
	'ETH': 'Lausanne'
}
```
</details>
---
[Dictionary](/5b0832dbf9454eb1941b7632e68a9abb#a7ac954b45b441c6ba2cc4fbc81d26ad)
```python
my_friends = {
    "Marco": 3,
    "Alex": 5,
    "Julia" : 6
}

values = [3, 4, 5, 6]

for value in values:
  if value in my_friends.values():
    continue
  else:
    if 'unknown' in my_friends:
      my_friends['unknown'] += value
    else:
      my_friends['unknown'] = value

print(max(my_friends, key=my_friends.get))
```
<details>
<summary>Solution</summary>

`Julia`
</details>
---
[`map()`](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)
```python
list(map(lambda k: k.upper() , ['Hello', 'world']))
```
<details>
<summary>Solution</summary>

`['HELLO', 'WORLD']`
</details>
---
[`map()`](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)
```python
list(map(lambda x: x[0] + x[1] , [('H', 'e'), ('l', 'l'), ('o', 'o')]))
```
<details>
<summary>Solution</summary>

`['He', 'll', 'oo']`
</details>
---
[`map()`](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)
```python
result = list(map(lambda x: x % 4 == 0, [3, 4, 5, 6, 7, 8, 9]))
```
<details>
<summary>Solution</summary>

`[False, True, False, False, False, True, False]`
</details>
---
[`map()`](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)
```python
def f(x):
	return x + 3

result = list(map(f, map(f, range(2, 9))))
print(result)
```
<details>
<summary>Solution</summary>

`[8, 9, 10, 11, 12, 13, 14]`
</details>
---
[`map()`](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)
```python
def transform(x):
  return [i+1 if not i % 2 else i for i in x]

list(map(lambda x: transform(x), [[2, 3], [3, 4], [5, 6]]))
```
<details>
<summary>Solution</summary>

`[[3, 3], [3, 5], [5, 7]]`
</details>
---
[`map()`](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)
```python
def check_grade(grade):
  if grade > 5.0:
    return 'Good'
  else:
    return 'Average'

student_a = [2.0, 4.0, 5.6]
student_b = [5.2, 5.1, 5.0]
student_c = [4.2, 5.9, 3.9]

all_grades = [student_a, student_b, student_c]

all_grades = list(map(lambda x: list(map(check_grade, x)), all_grades))

print(all_grades)
```
<details>
<summary>Solution</summary>

`[['Average', 'Average', 'Good'], ['Good', 'Good', 'Average'], ['Average', 'Good', 'Average']]`
</details>
---
[`filter()`](/5b0832dbf9454eb1941b7632e68a9abb#1dc0b8cb700741e5a48f5ed4180b2035)
```python
list(filter(lambda LONGNAME: len(LONGNAME) % 2 == 0, ['Hello', 'world', 'moon']))
```
<details>
<summary>Solution</summary>

`['moon']`

</details>
---
[`filter()`](/5b0832dbf9454eb1941b7632e68a9abb#1dc0b8cb700741e5a48f5ed4180b2035)
```python
def transform(x):
  if sum(x) != 7:
    return False
  else:
    return True

list(filter(lambda x: transform(x), [[2, 3], [3, 4], [5, 6]]))
```
<details>
<summary>Solution</summary>

`[[3, 4]]`
</details>
---
[`map()`](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9), [`filter()`](/5b0832dbf9454eb1941b7632e68a9abb#1dc0b8cb700741e5a48f5ed4180b2035)
```python
def check_grade(grade):
  if grade > 4.0:
    return True
  else:
    return False

student_a = [2.0, 4.0, 5.6]
student_b = [5.2, 5.1, 5.0]
student_c = [4.2, 5.9, 3.9]

all_grades = [student_a, student_b, student_c]

all_grades = list(map(lambda x: list(filter(lambda y : check_grade(y), x)), all_grades))

print(all_grades)
```
<details>
<summary>Solution</summary>

`[[5.6], [5.2, 5.1, 5.0], [4.2, 5.9]]`
</details>
---
[`reduce()`](/5b0832dbf9454eb1941b7632e68a9abb#9f73cbff0b4f4c93bbb2c23d80eee7d5)
```python
from functools import reduce

reduce(lambda x, y : x**y, [3, 2, 1, 2])
```
<details>
<summary>Solution</summary>

`81`
</details>
---
[`reduce()`](/5b0832dbf9454eb1941b7632e68a9abb#9f73cbff0b4f4c93bbb2c23d80eee7d5), [`map()`](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9)
```python
from functools import reduce

numbers_a = [2, 1, 3, 2]
numbers_b = [3, 2, 2, 2]
numbers_c = [1, 2, 3, 3]

all_numbers = [numbers_a, numbers_b, numbers_c]

result = list(map(lambda x: reduce(lambda y, z: y*z, x), all_numbers))

print(result)
```
<details>
<summary>Solution</summary>

`[12, 24, 18]`

</details>
---
[**Logical statements**](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)
```python
x = 2
z = 7

if z > 4 or x < 1:
  print('Hello')
else:
  print('Bye')
```
<details>
<summary>Solution</summary>

`Hello`
</details>
---
[**Logical statements**](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)
```python
x = 2
z = 7

if z > 4 or x < 1:
  print('Hello')
else:
  print('Bye')
```
<details>
<summary>Solution</summary>

`Hello`
</details>
---
[**Logical statements**](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)
```python
x = 2
z = 7
y = 7

if (z > 4 and not x < 1) and y < x:
  print('Hello')
else:
  print('Bye')
```
<details>
<summary>Solution</summary>

`Bye`
</details>
---
[**Logical statements**](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)
```python
a = 5 % 2
b = False
c = 1

if b and a:
	a = a + 10
elif b or c:
	a = a + 8 - c

if a < 7:
	b = not b
else:
	b = not c

print(a)
print(b)
print(c)
```
<details>
<summary>Solution</summary>

`8`
`False`
`1`
</details>
---
[Boolean algebra](/5b0832dbf9454eb1941b7632e68a9abb#26cc7021a7944be18174da50709dbdd8), [**logical statements**](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)
```python
x = 1
y = (True or False) and 2 < 1
z = (True and False) or not (True or False)

if x and y:
  print("x and y")
elif x and z:
  print("x and z")
elif not (y or z):
  print("y or z")
else:
  print("else")
```
<details>
<summary>Solution</summary>

`y or z`
</details>
---
[Boolean algebra](/5b0832dbf9454eb1941b7632e68a9abb#26cc7021a7944be18174da50709dbdd8), [**logical statements**](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2)
```python
x = 0
y = (True or False) and 2 > 1
z = (True and False) or not (True or False)

if x and y:
  print("x and y")
elif x and z:
  print("x and z")
elif not (y or z):
  print("y or z")
else:
  print("else")
```
<details>
<summary>Solution</summary>

`else`
</details>
---
**Error handling, **[**`//`**](/5b0832dbf9454eb1941b7632e68a9abb#7a4d967ac86c4e1f9b4c57989df35867)** & **[**`**`**](/5b0832dbf9454eb1941b7632e68a9abb#56829fbdf96741858731ed4b8520ab9a)
```python
data_x = [1,2,5,3]
data_y = [3,5,6,2]

sum = 0

for i in range(0, len(data_x)):
  try:
    sum += (data_x[i] // data_y[i-1])
  except IndexError:
    sum += data_x[i] ** 2

print(sum)
```
<details>
<summary>Solution</summary>

`1`
</details>
---
[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [set](/5b0832dbf9454eb1941b7632e68a9abb#f036e38587ac4bac9bda6d09abc39a30)
```python
persons = ['Marco', 'Daniel', 'Sabine', 'Janick', 'Marco', 'Sabine']
counter = 0

for name in set(persons):
  counter += 1

print(counter)
```
<details>
<summary>Solution</summary>

4
</details>
---
[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)
```python
liste = list(range(4,16,1)
counter = 0

for x in liste:
	counter += 1

print(counter)
```
<details>
<summary>Solution</summary>

12
</details>
---
[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)
```python

my_list = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
new_list = []

for x in my_list:
  index_position = my_list.index(x)
  new_list.append(x + index_position)

new_list
```
<details>
<summary>Solution</summary>

`[12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]`
</details>
---
[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)
```python
a = [1, 2, 3]
b = [2, 3]
c = [4, 5, 6, 7]

counter = 0

for i in a:
  for j in b:
    for k in c:
      counter+=1

print(counter)
```
<details>
<summary>Solution</summary>

`24`
</details>
---
[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)
```python
days = ['mo','di','mi','do','fr','sa']
avg_temps = [10,11,12,13,14,15]
avg_temps.reverse()

new_dict = {}
i = 0

for day in days:
  if i < len(avg_temps):
    new_dict[day] = avg_temps[i-3]
  else:
    new_dict[day] = avg_temps[i]
  i += 1
```
<details>
<summary>Solution</summary>

```python
{'mo': 12, 'di': 11, 'mi': 10, 'do': 15, 'fr': 14, 'sa': 13}
```
</details>
---
[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [range](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385)
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []

for x in range(len(my_list)):
  current_element = my_list[x]
  new_list.append(x + current_element)

new_list
```
<details>
<summary>Solution</summary>

`[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]`
</details>
---
[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)
```python
my_string = ''
my_other_string = ''
my_last_string = ''

for x in range(2,20,2):
	if x % 3:
		my_string += str(x)
	elif not x % 2:
		my_other_string += str(x)
	else:
		my_last_string += str(x)

print(my_string)
print(my_other_string)
print(my_last_string)
```
<details>
<summary>Solution</summary>

`248101416`
`61218`
</details>
---
[**while-loop**](/5b0832dbf9454eb1941b7632e68a9abb#b52a89fc421f4692bdc9c73a764ca650)
```python
sum = 0
counter = 0
n = 5

while counter <= 5:
    sum +=counter
    counter += 1

print(sum)
```
<details>
<summary>Solution</summary>

`15`
</details>
---
[**while-loop**](/5b0832dbf9454eb1941b7632e68a9abb#b52a89fc421f4692bdc9c73a764ca650)
```python
i = 0
data = [2,3,1,0,5]
result = 0

while i < data.index(i):
  result += data[1:][0]
  i += 1

print(result)
```
<details>
<summary>Solution</summary>

`6`
</details>
---
[**for-loop**](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)** & **[**while-loop**](/5b0832dbf9454eb1941b7632e68a9abb#b52a89fc421f4692bdc9c73a764ca650)
```python
number = 5
sum = 0

for i in range(1, number):
    while i < 4:
      sum += 2
      i += 1

print(sum)
```
<details>
<summary>Solution</summary>

6
</details>
---
[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede)
```python
my_list = range(2, 8, 2)

result = 0

for i, element in enumerate(my_list):

  if i+1 < len(my_list):
    result += (element + my_list[i+1])
  else:
    result += element

print(result)
```
<details>
<summary>Solution</summary>

22
</details>
---
[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede) & [break](/5b0832dbf9454eb1941b7632e68a9abb#62af9ae3a32b4733b902d98611973817)
```python
my_list = range(8)

j = 0
i = 0

for x in my_list:
  
  if j > x:
    break
  else:
    j += my_list.index(x)
  
  i += 1

print(i)
```
<details>
<summary>Solution</summary>

4
</details>
---
[while-loop](/5b0832dbf9454eb1941b7632e68a9abb#b52a89fc421f4692bdc9c73a764ca650) & [break](/5b0832dbf9454eb1941b7632e68a9abb#62af9ae3a32b4733b902d98611973817)
```python
i = 1
j = 0

result = [] 

while i <= 10:
  j = 6 * i
  result.append(j)

  if i >= 5:
    break

  i = i + 1

result
```
<details>
<summary>Solution</summary>

`[6, 12, 18, 24, 30]`
</details>
---
[**Continue keyword**](/5b0832dbf9454eb1941b7632e68a9abb#fe988d55110a4f1fa1181df33ad90af6)
```python
from datetime import datetime, date
 
all_ages = ["1930-2-25","1995-1-23","1960-1-10", "1985-1-10"]

def calculateAge(birthdays):

    if not isinstance(birthdays, list):    
        birthdays = [birthdays]
        print(birthdays)

    for x in birthdays:
        d1 = datetime.combine(date.today(), datetime.min.time())
        d2 = datetime.strptime(x, "%Y-%m-%d")
        age = int(round(abs(d1-d2).days / 365 - 1, 0))

        if age > 40:
          continue
        else: 
          print("Your age is {}".format(age))

calculateAge(all_ages)
```
<details>
<summary>Solution</summary>

`Your age is 26`
`Your age is 36`
</details>
---
[**Break keyword**](/5b0832dbf9454eb1941b7632e68a9abb#62af9ae3a32b4733b902d98611973817)
```python
sum = 0
counter = 0
n = 30

while counter <= n:
    next_sum = sum + counter

    if next_sum < 30:
      sum = next_sum
    else:
      break

    counter += 1

print(sum)
```
<details>
<summary>Solution</summary>

`28`
</details>
---
[**Check datatype **](/5b0832dbf9454eb1941b7632e68a9abb#6f8e8203d09a4c3aafa6f5d78119fe00)
```python
unclean = [1, 'banana', 3, 5, 'apple', 10]

for element in unclean:
  if not isinstance(element, int):
    unclean.remove(element) 

unclean
```
<details>
<summary>Solution</summary>

`[1, 3, 5, 10]`
</details>
---
[**Nested for-loop**](/5b0832dbf9454eb1941b7632e68a9abb#7cc1c66ebe7a4290927071b49aab1c29)
```python
sum2 = 0

for i in range(4):
    sum = 0

    for j in range(i):
      sum += i + j
    
    sum2 += sum

print(sum2)
```
<details>
<summary>Solution</summary>

18
</details>
---
[**Functions**](/5b0832dbf9454eb1941b7632e68a9abb#d98d10a03b3b4d17a846dfff610e9a5f)
```python
def foo(x):
  x = x**2
  if x == 25:
    x = x / 5
  else:
    x = x * 2

print(foo(5))
```
<details>
<summary>Solution</summary>

`None`
[There is no return statement](/5b0832dbf9454eb1941b7632e68a9abb#67bb23dea99842b996f3dbd9078f2135)
</details>
---
[Functions](/5b0832dbf9454eb1941b7632e68a9abb#d98d10a03b3b4d17a846dfff610e9a5f)
```python
def hello(first_name, last_name, age):
  print(f'Hi {first_name}, {last_name}')
  print('Your age is', age)

hello('Janick', 'Spirig')
```
<details>
<summary>Solution</summary>

```python
TypeError: hello() missing 1 required positional argument: 'age'
```
</details>
---
[Functions](/5b0832dbf9454eb1941b7632e68a9abb#d98d10a03b3b4d17a846dfff610e9a5f)
```python
def hello(first_name, age=25, last_name='unknown'):
  print(f'Hi {first_name}, {last_name}')
  print('Your age is', age)

hello(first_name='Janick', last_name='Spirig')
```
<details>
<summary>Solution</summary>

Hi Janick, Spirig
Your age is 25
</details>
---
[Functions](/5b0832dbf9454eb1941b7632e68a9abb#d98d10a03b3b4d17a846dfff610e9a5f)
```python
def hello(first_name, last_name, age=25):

  print(f'Hi {first_name}, {last_name}')
  print('Your age is', age)

hello('Janick', 22)
```
<details>
<summary>Solution</summary>

Hi Janick, 22
Your age is 25
</details>
---
[**Functions**](/5b0832dbf9454eb1941b7632e68a9abb#d98d10a03b3b4d17a846dfff610e9a5f)
```python
def fizz(buzz):
	result = []
	for i in range(1,7):
		if buzz % 2 == 1:
			buzz -= 2
		elif buzz % 2 == 0:
			buzz += 1
		result.append(buzz)
	return list(reversed(result))

r = fizz(7)
```
<details>
<summary>Solution</summary>

`[-5, -3, -1, 1, 3, 5]`
</details>
---
**Crazy function **🤯
```python
import random

def getNumbers(number1, number2, number3):
  for i in range(len(number1)-1):
    if (number1[i] == 2 and number2[i+1] == 2) or (not number3[i] == 2 and not number3[i] == 3):
      
      num1 = number1[i] 
      num2 = number2[-i]
      
      length = len(number3) 
      
      num3 = number3[list(map(lambda x: random.randrange(0, x), [length]))[0]]
      
      print("{},{},{}".format(num1, num2, num3))
      
		  break
    

getNumbers([2,1,3,4,5],
           [1,2,3,4,5],
           [1,4,3,2,5])
```
<details>
<summary>Solution</summary>

`2,1,2` or`2,1,1` or `2,1,3` or `2,1,4` or `2,1,5` 
</details>
---
[**Recursive function**](/5b0832dbf9454eb1941b7632e68a9abb#1b1c18524841477bacf6a53bcbc56386)
```python
def something(n, a):
	if a == 0:
		return n
	else:
		a = a - 1
		n = n * 2
	return something(n, a)

print(something(2, 10))
```
<details>
<summary>Solution</summary>

`2048`
- something(2, 10) → 2048
- a = 9
- n = 4
- something(4, 9) → 2048
- a = 8
- n = 8
- something(8, 8) → 2048
- a = 7
- n = 16
- something(16, 7) → 2048
- a = 6
- n = 32
- something(32, 6) → 2048
- a = 5
- n = 64
- something(64, 5) → 2048
- a = 4
- n = 128
- something(128, 4) → 2048
- a = 3
- n = 256
- something(256, 3) → 2048
- a = 2
- n = 512
- something(512, 2) → 2048
- a = 1
- n = 1024
- something(1024, 1) → 2048
- a = 0
- n = 2048
- something(2048, 0) → 2048
- if a == 0 → TRUE
- **return n**
</details>
---
[**Recursive function**](/5b0832dbf9454eb1941b7632e68a9abb#1b1c18524841477bacf6a53bcbc56386)
```python
def something_else(a, b):
	if a == 0:
		return b
	else:
		b = b + a
		a = a - 1
	return something_else(a, b)

print(something_else(10, 10))
```
<details>
<summary>Solution</summary>

`65`
</details>
---
[**Recursive function**](/5b0832dbf9454eb1941b7632e68a9abb#1b1c18524841477bacf6a53bcbc56386)
```python
def something_else(a, b):
	if a == 0:
		return b
	else:
		b = b*2 + a
		a = a - 1
	something_else(a, b)

print(something_else(10, 10))
```
<details>
<summary>Solution</summary>

`None`
</details>
---
**`any()`**** function**
```python
first_list = [['Janick'], ['Melanie'], ['Kira'], ['Kristoph'], ['Max']]
second_list = [['Martin'], ['Pascal']]

if not any(name in first_list for name in second_list):
  print('not here')
else:
  print('here')
```
<details>
<summary>Solution</summary>

```python
not here
```
---
</details>
---
**OOP**
```javascript
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __repr__(self):
    return self.sayHi()

  def sayHi(self):
    return f"Hello: {self.first_name}"

class Child(Person):
  def __init__(self, first_name, last_name):
    super().__init__(first_name, last_name)

  def sayHi(self):
    return f"Hello: {self.last_name}"


child_1 = Child("Max", "Meier")
child_1.sayHi()
```
<details>
<summary>Solution</summary>

`'Hello: Meier'`
</details>
---
**OOP**
```javascript
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __repr__(self):
    return self.sayHi()

  def sayHi(self):
    return f"Hello: {self.first_name}"

class Child(Person):
  def __init__(self, first_name, last_name):
    super().__init__(first_name, last_name)

  def __repr__(self):
    return super(Child, self).sayHi()

  def __str__(self):
    return f"{self.sayHi()}, {super(Child, self).__repr__()}"

  def sayHi(self):
    return f"Hello: {self.last_name}"


child_1 = Child("Max", "Meier")
print(child_1)
```
<details>
<summary>Solution</summary>

`'Hello: Meier, Hello: Meier'`
</details>
---
**OOP**
```javascript
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __repr__(self):
    return self.sayHi()

  def sayHi(self):
    return f"Hello: {self.first_name}"

class Child(Person):
  def __init__(self, first_name, last_name):
    super().__init__(first_name, last_name)

  def __repr__(self):
    return super(Child, self).sayHi()

  def __str__(self):
    return f"{self.__repr__()}, good to meet you!"


child_1 = Child("Max", "Meier")
child_1
```
<details>
<summary>Solution</summary>

`'Hello: Max'`
</details>
---
