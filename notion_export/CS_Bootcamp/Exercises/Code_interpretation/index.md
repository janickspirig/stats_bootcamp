---
title: "Code interpretation"
notion_id: "d90204f9-dca0-40f8-a1ae-dd2b8a914390"
notion_url: "https://www.notion.so/Code-interpretation-d90204f9dca040f8a1aedd2b8a914390"
exported_at: "2025-12-13T22:51:00.233251+00:00"
---

# Code interpretation

---
📄 **[Python basics]** (subpage)
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
📄 **[Numpy]** (subpage)
---
Filtering
```python
import numpy as np

my_array = np.array([4, 2, 5, 6])
my_array[my_array >= 4] ** 2
```
<details>
<summary>Solution</summary>

`array([16, 25, 36])`
</details>
---
Broadcasting
```python
import numpy as np

my_array = np.array([4, 2, 5, 6])
my_array[my_array >= 4] ** 2
```
<details>
<summary>Solution</summary>

`array([16, 25, 36])`
</details>
---
[`.shape`](/ccc5737dc7c64936bced118aca375cf9#3332a8d6e6f040dcb5d7a9aa86174b6b)
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array.shape
```
<details>
<summary>Solution</summary>

`(4, 3)`
</details>
---
[**`.full()`**](/ccc5737dc7c64936bced118aca375cf9#8a83f4b13478461f88b3eaa6fd43315e)
```python
import numpy as np

np.full([3, 2], 'Hello')
```
<details>
<summary>Solution</summary>

```python
array(
	[	
		['Hello', 'Hello'], 
		['Hello', 'Hello'],
		['Hello', 'Hello']
	]
)
```
</details>
---
[**`.reshape()`**](/ccc5737dc7c64936bced118aca375cf9#b266475fda3a493383e07eece2ec3510)
```python
import numpy as np

my_array = np.full([3, 2], 2)
my_array = np.reshape(my_array, (2,3))
my_array * 4
```
<details>
<summary>Solution</summary>

```python
array(
	[	
		[8, 8, 8], 
		[8, 8, 8]
	]
)
```
</details>
---
[**`.ndim`**](/ccc5737dc7c64936bced118aca375cf9#3e82f815ed7741db9931a437f7c2d5ce)
```python
import numpy as np

my_array = np.array([[[0, 1, 2, 3, 4]]])
my_array.ndim
```
<details>
<summary>Solution</summary>

`3`
</details>
---
[**`.mean()`**](/ccc5737dc7c64936bced118aca375cf9#64a39ed9c00c4e64a2f0e20e33cd0d8a)
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
np.mean(my_array[3, :])
```
<details>
<summary>Solution</summary>

`6.0`
</details>
---
Accessing
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array[1:3, 1:][0][1]
```
<details>
<summary>Solution</summary>

`8`
</details>
---
Filtering
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array2 = np.array([True, False, False, True])
my_array[:, 1][my_array2]
```
<details>
<summary>Solution</summary>

`array([2, 2])`
</details>
---
Accessing
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array[1:3, 1:][0][1]
```
<details>
<summary>Solution</summary>

`8`
</details>
---
Filtering
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array2 = np.array([True, False, False, True])
my_array[:, 1][my_array2]
```
<details>
<summary>Solution</summary>

`array([2, 2])`
</details>
---

📄 **[Pandas]** (subpage)
---
**`.shape`**
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/69f344d2-31be-4540-b0e9-e491aef4f09d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=ca528662a5dac7254a5dc2074c2b96a20201c11811404abe3a55a8a8f2e2f355&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.shape
```
<details>
<summary>Solution</summary>

`(20, 3)`

</details>
---
[**`.head()`**](/1867045b058343e1a66b677961515907#bc578af731b541f1959e282a7689fb05)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/69f344d2-31be-4540-b0e9-e491aef4f09d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=ca528662a5dac7254a5dc2074c2b96a20201c11811404abe3a55a8a8f2e2f355&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.head(8)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c8e6dccb-6837-4b57-9313-fc83b502831b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F4TFRUH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCVQnyMh6UqenyjvBud1DknI88KpwST1IXJhKuNcFHxWgIgIwVrnQP2Dg5WcV37XmpZCjUx4JYbusC%2FOjnhozjvfZcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDB9Exe0tfj5lAbovSCrcA%2FeqLYESWbA2XXuVG9FxFSZciATV5b%2Fu%2B5U8sWd3yN%2BiZX44IQ9NcMB17yxPaYEmLk0Gw6N0LkvR1KfWpJphV%2FA3orVpXEzNKo9Sj12RSj%2F6m08bWc0fx3z%2FmBroDzGhNdU1YFYImcyKSrb%2B%2B6wsDEdHDdNq%2BjJKSZyKwQ7gek0%2FmJJ0jap6T7lAZzXgFE01D4s%2FgbodgyPt5eNFrsjjSOd1OPt7Yc3pRUUSBmhxSrhom%2Bb%2BxLnYd7DYDx3igMdO1z%2FRfT7ADcHXLsqSv7Tvv0l8WkU5dRotKy2%2BYnwH29VlqHCoMup9NGabv%2BiLimUnjsnlN%2FiVvBuVj%2FbeVaP0ZpDJluzjZaPHGhuAQnwsWWy6GF7sEcwE2gTWv34nUVUgCzTKT85BWmnRGAtS1uWIiuTi98BbIP6vQcM%2BtQzoJLbQdpps7WD%2BZe1qUjA1AarUH%2FvIJjK%2BmwQAA8Nszhx%2BV0OvG7fBqXDHBhIpdFz5DxstoOh5DskZmjp114F5w63xSHDzeLdN6%2Fhn5Atfv9HaE5pImxzRol%2Bign3g9glr9KVLkTKmNzOZLeoBo189R88oxf3rkgjVGhhH%2Fff4bYJ3ukl6AqEyBSNC6qzmnnuQd%2BShKEN7LaT99tDM7Tx4MPHN98kGOqUBTPvOa8%2FQfDOik%2BLId9PBMY9vPI1NttIaCyDyavASXWSq6oh2LjRUqKdCDKdeLQECWXpc30vOcEoZ8GXEXpKh56j0GAAD%2FLFLZammYwVmM6cY%2ByN6LpWfGfCkT%2FxLYPG1GvopGGs19bbxQmRi5kcqh1arwRM4WIYtimnucMSUr0wLnf8J9OxozNnxMZtOszffUtcccMgXKhbaRi44DjZyoYTxNfn6&X-Amz-Signature=be70ba895f315f5adc3fa33bccd87196c773b4ce70dad6268e9040905741aef0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.tail()`**](/1867045b058343e1a66b677961515907#c202944531cd4fa68d141eaaf404c2ab)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/58177663-5588-4a8e-96cf-76e8d0fcdd71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=1b01bc907b421a13e5569cebf53b83c967ce5e6dc81915c902764114d21f2f6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df.tail(7).head(2)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/317202e0-51e9-423a-b950-5cb85785cf66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662P7K3HFZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEDl4cBdYblCIarpVg0V456g1aeiCUgHLPakx6C9pmQKAiEAqVDyBPw88RmUjY967UMpay8KGrvWXFVsyJET01eU6o0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIhAZSYmiT481IdMuyrcA6mGEqZKzt6oBakaFAMsHSxJyErd9XufxHDyVEMfs4ZlEt5jTeWnaXVOwoMJ0qm7Xf6VCXGxsI%2FZexMDs7qmlC7lwsbqCxcQqeXJks2e6bhsApRcs90eujjG%2BY5%2FpNds0ySKy5E8kTgNw6YFdkxp5IBuNtqVrKMpSkZwZ8RNFugiBOfQIQG9rsf%2BH96ptgjshxXqFeMSz3V64JExUPPT3iQ0i9wAzMjz%2BydTRnfEzn7L4Of8JC0Jo6ya%2Brq9dcDJ0NRso0TBReMUzl9yVCeWQoUpUuWTSHblyNyGRYpJBCs4q%2F6QcDamS2qLWuOqcUbjbaax8Nr7ESKBBZR%2BVb8IuK%2BdGM9FmdsKxKbbN9znpqYu69PB53hW6%2B3BrMYaKqEVf3L0C9km7lw%2BEpra8A96UAg7GmBmtLmeqo%2FdfzIlMymdUvFc7sU4g6sjiJkdcpNwJ18bMn6GTi%2B4gCUlFMqlYbbi0E29gmni3kiDwUCWtiQJVMgu98Mpi5oSpX%2FyQ6c%2FNMJ4w0Au0rJNGolMUpEySUnb%2F%2BCPMOLN3MLHCSfV%2F9kXSWSFWlVQgAt1wWXI0bZ%2BzUBD6JEvjMeesn1v2PmUQge69US0bppIrzumMvzeJaGUGLH8S8%2Bgmv8LAemuMLXO98kGOqUBHwo7aLGOJ81ycCAt9VxNB7BCWPIscpwFWrgGNLWlC8xayfyPDgYrQxYdDLBumv%2BQ0pRySwnJC00b3Ok5StJxWiJU%2B3tAs8JiwTzUhhkTobu6mx%2BfFvSSMNwOPn2F5Yq00BABI2shhD9kE1VIyxRTWHH84gBYG1xIWEhGF%2FNS3jZ8gAmhrFTJ5pta3IiPK61%2FQYc9QfMET%2BNc%2Buego9yR7y4ioiFb&X-Amz-Signature=02779091291310b7279ae4d4c39fb23764adde2c5a56e80db2759df3df2a8ad1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**Boolean selection**](/1867045b058343e1a66b677961515907#a61901eaa28c4a7da25d80a1223b80f7)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/568f9210-51d8-40dd-ac00-5dbc8b3072c8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=11eac1daa1dbc7a3b4123d971c30c4418f0a5889591ebdc75ec9ded17225631e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df[df['A'] > 40]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e4c0ab8e-7b3a-4786-a8c4-a5556c7faa7b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLXYB6V2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCyYCD1HUK2tgv43viwd4p8MM0gtbqgVuVMFj9UTrTPqQIhALpaztl1QTzkB1vt2%2FfiMsLLJ309eif%2BBmfjCIpEnGg8Kv8DCCcQABoMNjM3NDIzMTgzODA1Igx%2BaE76L3WAazQiFX0q3ANX0Bh9g1bHF3P10v1Hz3t3sKM%2FRyc43kXkEkE3t6oU7Pj9vLzdXKog9lbAXXny1N8Y793pgrnbLToAPxL8bkjmJOxJufYFq%2BTO08EdrJ6Vj%2B2LrW0whDKpHHE2SyazUbfGZSNrI%2F0JldGPi3dqezXuEP9i4iz%2F5wexNds%2B6dfxDh%2Fe%2FTrTGYqAAycSmI52%2B2mS2%2FNb%2FoV3R1aHhzrpNfgz4dNmQU9NqZTJnNMa2iorpG3OTKhLyrIiu%2F3nt23MvZWijO4oQVk6aYYcDvvF5wxvHbXAVm%2Fhv6Tnv8sbfDFMtrM8db99R5luGNQW8m4K7IDWfrmhnVKLNyPyjtpqXQ3uHeM54T9FY9HQjJ0JskMo2sC6Vm0y1CRkYqAoZO0jZMi27eRAhU220Bsj4svT8H9ZDS3Ag6SQpNZOyI%2F%2FE6Fk2jqDkygoOr5fOy2TonJayKoWmHs5N8qwHk0c21QisZqy7R1wD%2F%2BG0G6SjCbtv7K1CCchj%2BfQayyxREMUTLDwVLS5o6ZzML48KI0FCEBeUDgvVS%2BTIPf4NdI79PSFrl6NyUuVl%2FXKkx2orBxyCnVNqtKLyPt5LgiNStfzGM7UXxtikQUlPw2dKKbZZwPUJRj6jcUjhOjYYeorN1w2RjDgzffJBjqkAfUzYyhUayH2GsRDpc4B8%2F873or37BJYX5KoN8%2FgkIoYZj1PQe7JuiI4eNlWCo41Z7HbnTIgCgym2y9ZQ0awUyil%2B8jN8vER7cvXfMCKp9L9IkkFtLp7mXk13DY6E%2BUgCyQwd1fZXvEusK4eYSGqqs2NCdmHrGjdYM1LirBirHfYfzzPjHJzV0vnYodeXbzCVmR9s2zK%2BFm09l58xmFpJBRHAxXe&X-Amz-Signature=59e1d1aaa698935476e141dcfb2c2ef084a5a4b6d369bae35a898ff47afcaa3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df[df['G'] <= 46]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2c37fe90-809c-4f49-98c0-b29a0766191d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA7HL5LV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCCGa7CRE4bQ1hjKMzfYfNsnE8coCKC2inhdMq756Xh6gIgdC%2BoOhwjiAX%2BNmDhBkvKy7x6e2qSSBdnKRG0nguZo%2B0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDN5R2FZWM%2By0GhJN0SrcA33%2FQwB7reQmcXAAXlzUsx3H%2BS81Xur%2BT7Js9xd%2Byieq09kYZunip8EkdFf%2Be4UtwlDKmlDpSlE4pfILRzuypvnnkERb6XWpaQP98zAgaxcX5NbkDVgcpG2rL0qy8%2BkvoimAXRCmL6ojao9BNQe1G3drpTCBlLs8HcdSPWaIZSgg6wMOdq9pVDe98nHVzFT9dwCKEbZgY4YmTZkvIe7v6fM8mfsC5n%2BHtYpk9TLPvltbGSp1iBCaNJrbExt9Gv8PvmMvIQyNeDtSHEe8t4F16RPJzF9X%2FazpbX80n9u%2FazCP%2Bm1Ae06%2BJ9PVMGEfHzVGpKgPjCGUR%2BamBDDWM7HFpm%2BjCDGU1bwECP06sn6MhTomrZ0vrv92Gx1CEkmGnvXk1%2B0g5HrzlkqWi%2BK%2Bm2uMZZ17wfrQBQ3bgrxCoPiCy694hz2T%2F0w5P6iFXy%2B6u99lYE7iHI8tnpvCAXQwbSJzqdeTIc38MN%2BGyC20Iht42uuBR7Eb1T%2FKRCW1JfThoJ%2FtwFX9VteRFfR00XxJZ9h2HSNkcgsEvr59vN51yTGpTRwviS%2BNzvLNvENAicmZ6CLsPmUL2%2FaXn3%2BDfc0zi0VJLTaPFUqeJScqZhtZiVrCSBbmuJ2YBCd3wG0%2FVLESMLTO98kGOqUBNjvKIaa%2FGLZ%2BpI7lG%2Fge%2B9TUYYODLxM%2BYGgXK6KWHeDCVvJdYW8uRHfR6Fz1%2BSYzwKU6H%2BjuxYq94UoTQTYFNXj%2BF5UpdTc4c4nb4FpGsYosSWHtzp%2FVUpTvCKHQurEyfnO4b%2FbGzzZRpFjIrcPuNWMKgqxGi4qmQC9UKFEikVpdd2sE7wml69rxXfo%2F5kMqhPEehI4lrdyqpRhXMvkLRzcXzrsm&X-Amz-Signature=8b0bb5bc849d2326644a1f1589d9d8b280d54f0985daa9b51f8426cfe8a79154&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df[(df['A'] > 20) & (df['B'] < 71)]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7b8369da-79c1-461b-8ce3-3814a7151ba5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRDN5S6A%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDz9xjH0ung1j8JC%2BcmABybb831LgKOC4GwVxkfZ32WBgIhAJPKs3dqbC%2FbtqR5OKb6hrc%2FLq1iZrvFAEtONEoyzlsTKv8DCCcQABoMNjM3NDIzMTgzODA1IgxVHZBgKbJSsxqL1GIq3ANp53bWmUtrw7Jm1HHU9ZDlW9vfvFR%2FiEF%2Baj7WurL24UqZagRxNiVjzGkA8ABKYB8WbV0dBRqvTk6EPLt%2Bgynv7fI797aZyquPyuvQrtVETIRbkDs1yTmdIuTYEMNcdsJa5W7NGhNi%2Baf6uCFw4dw5bY47W64OUl46tsX6cYsQfil73KnTe3sB%2FAXXqY3%2FisBQQxLFeP8j4EXS3Y64kxC1MOc8%2FAW1Bf%2FhIbzyAvdLY0sKrcbpeF7IzgWwz3h5NQnAzQCjntT3YY8UgDg6sYjEjsk6ONR%2Bkpx%2B7Fd%2FawZRrGtsZ8jFofhqobhwRpSTwJabECOAEqzrjdJ8JlMqBK%2F3nJl4nl%2BtFm4cJhJ77Dj5S4yyGx8IoJDq3VnbUCsb72465cxp5QkpPepxo7K3GUbPGZZUnyQHoR6GQDvkbrsiSULt5Z2XkfDWWek0MMS6DA%2B8otCy%2BCGveMidf4H%2Bmx9%2F%2FXrSbBFkm%2FpDOJNliQCbWkRtFV5YCqoenNsocs2Vyva%2B9DZVdi8zEeHOT5KVbaR3%2F25aiocwUsvxq5hGn0homOboWSscTTrkGJL02FqVDUwxaSxR%2B6sXeX5NnyROPqVXoLcvQtDBcvoNohuYjP4eah2vtQSEH22hkELNITDTzvfJBjqkAe8qLXIxLUv5EaLTIHtTQMYCN8s0g7iHC%2BZvjEED3ApvsRuDkX2b22VLt8%2F3WYi59V3cRUkUsC6%2FLBS1bqtg3BMIXzn%2BDdPX8sakLaBAUZG93qmQ3IatoaY11iWyjIFtLJaMTZzveQr%2FM1aIu2YmCnu4Let4RjFOuEKaUdTiYHycFfOiqquWUZNJ2Zfl2GxwU5ZhHF0SSASrOMyjNBeVrUaUFD86&X-Amz-Signature=c0c215a03d9c769892de9fe474fce9676403aa49ef1feb8ec12f64e968975df9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df[(df['D'] > 70) | (df['I'] < 30)]['H']
```
<details>
<summary>Solution</summary>

```python
0     7
1    17
2    27
7    77
8    87
Name: H, dtype: int64
```
</details>

---
[**`.sort_values()`**](/1867045b058343e1a66b677961515907#f4a6d6bc54ed4a2e885dd225270c2ccc)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4277a967-82e0-488d-b603-3986cfcf9b9b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=97cc3c057212acf4a662a74593ca85eb3857bee563e5f2ebb6c560da23b8f9d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df.sort_values('H')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f755b7d-739f-4a7c-9463-34ccb3a7d251/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTNDF53O%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDdFpBy87%2FYcKddf6%2FlBuFMOi5cgBFSnQ3qLBRoga6IoAIhANW%2Bd0NoK%2FuIHZDWU%2BoTcZZ5M%2FIFvm8xHb8s6%2B7fFf%2FPKv8DCCcQABoMNjM3NDIzMTgzODA1Igwctns%2FOgE1rqcsbukq3ANpbml5Bq%2ByjkDQijiiOwoi9In1BhunKYyJnURU0cJz5uAqa1gUPe0iFPBVaTUyWjs02ESsd9u4%2FZmGbuS9FcYa%2FJXGOXo6%2FDUpJBfkZl9kVWKRzVsoNNvEHZ7pFzN47oF7SieRxWdhx9CdN2cdt0tqzuIxg9QosRO%2Fh1M02u4foBPkZy9mNkxR47PJA44%2Fba44dfmRHm%2Fv1YYnZ6bRNkucmrVNElCQYjbFuIkNJpL15uLON3kFVk0nELEYWGdDQlsSEQKsIdQ%2FcCwo%2FlJKz9qlKIrvhwYZczK3JZcWHjta0mPWvQv7InWrt3E7uThTXj%2FjduDtyuU0NgUKgZyHVYtSe4VsY57c%2FmTCGbpCRgqK5prwwJ9dSAgZL9r2ZwX4sPrTPmftFp2N30Ty%2FlPAEujy1S89uiq6U3d4IuceYs5RQGZVJSmZPkTIygj3HfhdHdmRKVCt%2BUhpLkJix0YwSqHmQwRoIz2IZ3qt9VSCMRGkdqFi92U%2BYgmjS3WhR0LIbBAhLLOdKCgL2OVNeWLyveyWyZxGi0T5aXatck1%2BrblTSer7MsrcOdPkNgBbpf13V%2BQjWGDa%2FTvz4OyufTLqP9g%2BICSup5whKPC%2FDnEeLNn6c%2FXr11j2qx15BRNojTDGzvfJBjqkAV4z3kvla7Xi4QiDhRITQdw%2BQzh2MXR0snXJ9CffIZW9%2FvcmhOZEIot2SdNt9IKxEIq1kCiJShIrK3KSeDGZv%2BPokEdNB6haJuTEsU%2F58tlyEpit9FDbXvXNn44K6uOF4hbGQx0TtlY4S4ZHjrYxCzbdaNqRf%2FnkeOjhBTlLSTEWml8OmIPQyEBY3%2F5jtD4vonfNUqavN5G0jhKj503bfRn7cBnO&X-Amz-Signature=f3444933334a1433c9e9636e943d53fc9bac77fad89fb0d1af0ba28fcb6c1ea6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df.sort_values('H', ascending=False)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/86143afc-dd47-49cb-8cd5-1e40b4d4183c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTNI6D4K%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBF3uWV3maGp3m9MhKb6G18lpWAtbqkzvrc%2BqtlGuel0AiB8NFW7A65orktoQmMTvIEeaf%2Fh7YZQYrjWQKoRslx8mCr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMCKtRoOTcpet7OWiYKtwDXBpDxnbZpKkqHTV7tYK4Xf0veqWAiswp7oZGGSuV4JdavjvxN1ABbbcNpAmj9vgBXWd2Z5QsKYQ0bhqk0WOVETBFFTDTBqgyUTIvanT%2F3n2E3KzZMd6NM0zI1wP%2F40KG9kJg2Z9IJkn0gwgrWIfjT7w7VIhKlj5PHStR2Z%2BcsmEDOgkovw4whYKKn70yaKEncMqUUrsIHM%2B6GniAigAFtRr%2BjJzAWrB9%2FGHIargGEkp6y0T9wPzTTCg%2BMuCjPNn6jhfO2zooKNv4QF%2FFXbZlaQTHSVtnBA%2FHnTpXzIVGVT2CnX9aZaxGPwbt4FSH3Ba2lBIsTg6QKW2vdu3jIBIaNVFS5OLG%2FZcmXBS4Pzwyq4SWtS3kFrmwZbNbq2lGcDZg5CBf%2FZDCZQ1fDOx6RU8vwlTAXVh%2F70fKLGz7BLEFe3B%2B8ZHCXznF1HQzdOEqIcaTdRHfwrv1J91auail9t6R4rfwHd0yntKnzmW%2F1HRE%2BfYsZz3TLByV4BPpewTm6njaTLGxaU%2B5%2FSFG%2BLx4gl2AMW3rOuEd7wIVeaNJGen9b88eP2fKVlF1qn5FdlMKg9dQvPoCaZX0Kdo1awnXZGnGxSwoCGE3h4tSoO3XXpatpMkSfb3VnnJOFx9r%2Bxswxc73yQY6pgGAkAfN18ptrh2C4G%2F1GnHt%2BrCUa6MgGCWelm8Cg7Ll2akLJztBEtkS2wDRMvHPpeBCWRH0VkkJRVQGfDav0cYU1R%2B%2FHIt6goIiry1XyfhzOzwOVe2f1zcR3HbVERlv7%2F4XZJxLpqR2oLRI9JjGjB%2FT8L9aw1Tx1oX6PV5zbiw4rFY0Kje%2FZceKJyZ8ljj%2FA%2F5vQwpeiE8wpOmzPJ8C3nYfchPozinL&X-Amz-Signature=8d7a51bcf02ed4c2ba66795e217d730b020a9cf7df729cde904d5c23124ff2b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.count()`**](/1867045b058343e1a66b677961515907#8d4d0ed1fc114482978e4da5f21b429f)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/de99cf2a-01de-4394-b9b8-778a479f0f75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=a75ab6561a296ca31cbe187d72b034e1df5861178e2839b9e55b5ce837bda31c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df['Games started'].count()
```
<details>
<summary>Solution</summary>

11
The number of non-`NaN` values in the column `Games started`.
</details>
---
[**`.value_counts()`**](/1867045b058343e1a66b677961515907#b585cb62f9dd4878aa31acb88e071f0e)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2e0c7fec-4523-4dcd-9352-242c0eac4417/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=583ed9d241f22ef0464e0f17078c1af67e85f3b310e85d072e6c951bc027647c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df.iloc[:9, 6].value_counts()
```
<details>
<summary>Solution</summary>

```python
2     2
7     2
5     1
3     1
1     1
10    1
6     1
Name: Assists, dtype: int64
```
</details>
---
**`[]`**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e11b194d-b83f-46be-9096-b1cfe4b86b49/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=cd299bea9e7bd73d29d862b90975d9e7ad4a4561ae59e5e63c2d8466c09a6af5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
type(players_df[['Team']])
```
<details>
<summary>Solution</summary>

`pandas.core.frame.DataFrame`
</details>
---
[**`.unique()`**](/1867045b058343e1a66b677961515907#74cb3dd5af264206a7e4ccc9b07d9a7a)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c914f3b0-79e4-4110-8acd-eb157e678223/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=9f1ab81da892fca050b696eb9208f7ba5ccc1bba0f2b187e5b01f422d353495d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df[:-7]['Team'].unique()
```
<details>
<summary>Solution</summary>

```python
array(['Leicester City', 'Southampton', 'Arsenal', 'Manchester City',
       'Liverpool', 'Tottenham Hotspur', 'Wolverhampton Wanderers'],
      dtype=object)
```
</details>
---
`.nunique()`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f644f684-aabe-4980-a9f8-1245e19ad969/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=c150d9c41c962c46e65fd9fbcd5c05861222a5cc85f4e785753dbb7d1efba777&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df[players_df['Team'] == 'Arsenal']['Team'].nunique()
```
<details>
<summary>Solution</summary>

1
</details>
---
[**`.idxmax()`**](/1867045b058343e1a66b677961515907#ba3eaff47c7b4959a30a15a24dcb4584)** & **[**`.idxmin()`**](/1867045b058343e1a66b677961515907#345599162e1b4b188fd36eaeb3627352)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/96785e84-d4de-4def-a74b-e9ace013302b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=f2baac534bfb09ecfd2cc890f05830c09a089e553f9e321722f3185fe8bfa74e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df['Minutes played'].idxmin()
```
<details>
<summary>Solution</summary>

7
</details>
```python
players_df['Minutes played'].idxmax()
```
<details>
<summary>Solution</summary>

8
</details>
---
[**`.to_frame()`**](/1867045b058343e1a66b677961515907#b585cb62f9dd4878aa31acb88e071f0e)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/aa9c033d-d4bb-4f1f-abf2-3075bc0a809c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=8ee7ba038ba93703f2a14237e0d3185c17d7b1fdaa6a1f6cbc13a2643fb2492a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df.tail(8)['Player'].to_frame()
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a391e12a-fd80-4f67-8ebb-03018c94dbd0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KSTHFOB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB%2FUWEvUn8UqAu7sUB4MHmbT1QI%2BGrjlE%2Fx6xz%2FgriTQAiEA8dPIi67htIXWW5bYt7r6jC00sGeDhBGo8BBF%2FRlBz9Iq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDPxqXbQyCaEKryLZLircA4k1qRZRBYsw0jfwH6N17%2BxHS0mszCusVDok1YisOWr49cGNrnb2coGFXpW5qHDUaiWlc9BHB85PbKTonH1edzI%2B%2BeTLQzAOghWRXlKt4K9LFDWXiZOQwUb7wvomqzUJ0TeT8Pjj2j3gVacI5%2Brxj4WMqilz%2BEoKQgibSrTrCMNZLCQCc2BaW9euuS5prrjBoehpWsZRVwhgpNA4qdcufYUfuIY0dLxS18QODfuprbn1HATVP1ejZsY3akMsPhodztkTDzCiTZWNlJot4rPdmx6%2FM%2Bujmx4oXHK%2FzoC6RpndRAIUAHEl3%2FBDRhyMRiF1hTRY7Rx%2BUE%2FJiWMkxgmfjmifN8AEZ4y69Z3Ibth5XVtFNC2GhocdR4TqHN6M94O21JD2ak6Jdymmepk3xqnBzfpnOU6%2B3uZV2kBS58yS4FvYVFhMcK%2B5nafbA9PvYx%2FjvLI%2F5k1llFW%2Buzzh84SGXQbkg5%2FTy3OmyxEqGDhsTOpDQSH2quBXIMY6PyqLtZpSyJt4rcYtTMcFh3BRsyHL7NzZ%2FkNYbsLTQ1PP5cl5IePzT7ZFqQjln4bGey7zvcA5WOERKbPWuyQdzgLBifpf%2BESFJv%2BcmtIkevAF4hVo9qVEaQ779JZ%2BDMJCggGdMMXO98kGOqUBm4tO2tiXHGgky1Wgr%2BYratrI9kb7wWgF3j6bD1kGmAIqXzeyg4nYGKKCQH3bT6D1Y2ihmSwolrB%2FcV2J7J8eAI%2Fm8n5YjKIXbcmaB5PjGbrib1yYGR8JOhwwuYVKJ25RBoSvSHw6TRuU6VN1KbVsgdBnDVrh4Pl2iEncVhFKGw0Z0y0LZl1wVNuMedZS1jwABs0DluavyWQHKNCkkhpXdqo2U1p9&X-Amz-Signature=ef4ecf2b2f694415e19d8199be1ca41af466657b73a3b3061b354c1fc43a6661&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.groupby()`**](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15)** **&** **[**`.get_group()`**](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b9981f61-90ab-4be5-971d-7e1c69d16d5e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=dbfce768a11fe02b530c2590102608d0049a5d7824596203e330f63909f55238&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df_grouped = players_df.groupby('Team')

df_grouped.get_group('Machenster City')[['Player', 'Goals']]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/03c98ae9-19a5-4d41-81ce-9ca5a314adf6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PDCZO33%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD1E92GnmtzXMfCnMfAPb8UpuDpzkRm2iMqF1IZyCyWawIgSmWvMiR8fE0H8759fVNxVBRAcUkqmwLUiNzD6CY0N1Yq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLzwIJp4rmxmsoEqoSrcA2RgG1ErdTY32qmnQrku8Wt%2BfasEkqF8SEZVALjnhFx%2FCo3j4TbCjUpYmxXnCZWrdbDTmsLC0EK7%2FC9az3udVuG7aAeSA98eyU15IseWG12aHBt1vjhBqlUrGeqCTdTCx7q2WHZmOMD1Zuk0LGDYIW9USMfpI3NgrpPGUomjGhqflNaV64MsqMCroMBSs1y5Rbs5ZrR6UjS9CcQhxKLaletzN6uoIiih08obH2jbWKjtMG710bXFGAh4xD3YdWivcgWs0puxMCqxq4P4gQjLOB16bmgyBEVndgSTKKtZjVDAze0HEW00VZ9Jjkft5%2FWo6sT0sZ16fz%2BrAvKUspso7%2FnPcSb7WnKmpYa8wZ592O4tgi%2BiejDdn%2BmzJR1uO6FCHdZaMNdc%2FxvgOl4f8lpdTAJGGtAFkifhXjPL0VcuDTXpZhB802%2BJHj6j2gWgTbZDKJ9DcuH9Zw3gVEODEuj9mIYJPrxq9F9gCqBsVFKMMammorEkjr3qRWqukBByaMSaCzp3UvvpnHGXF9RcRRNJdwxtzHAVLCaLP4LNdCugqVt0SzDRhaAD0tOKMZSDwpzkXbrl9ohKd75jirJTKmGlnbnF8YYyBa%2BEB%2FNivowOX6R9eKVmqSYXeuObG80wMMbO98kGOqUB4MllWWVMBtdkoqM5meKWn%2BGU3sOc%2B4L3bGGYQh8EbJlMGMoxpRwQcsz%2B%2BPv4u0XPvWEE%2F4D1DJz2TCxN2N85FaBhiAbyUsnU1mW6wozMfVfy1s5624Th4DC2EcT0Y8oP%2B10z5F0zcxEgKe1Ng1I0WwNHAclqHc3QzcGWSaXV%2F%2BBiQ6N%2FVWcJQ0HG9KXVZNUJRJqJCeKOxwvn4hAHgsZLm8WGimYH&X-Amz-Signature=50ec4005d11c5d24e6610fc234c009db34f4b0aa1a745ce9f550b9a1355691b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.iat[]`**](/1867045b058343e1a66b677961515907#54779c5ca3f3440087c94c34ca5b5328)** **&** **[**`.at[]`**](/1867045b058343e1a66b677961515907#c21adec24a86474fbc660584f480a8f9)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c6def28f-c507-4696-8f3d-b3d2cb8fd425/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=1b54b8bb64be2198ee6c51d4ba3013ba3ec1bf08e21c9c1962e2e8af5cd139d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df.iat[3, 5] = np.NaN
players_df.at[2, 'Team'] = np.NaN

palyers_df
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0cd01bb4-2251-4287-b96f-5f3a7768e5fe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y7LSEIL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEraWS4OYoz%2FcPTTgUDRX9133gPv0UiTV9MdluYyV9S3AiEA4WprcMBgliDTLw8dL2IMn6FaoiAd9gNCUIzhgvvpHb8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGA0L2xXDJdF5j3nRircAwmhVNgkxrdQkh1wg1eTDG4gg7gldllqe1RWvMT0O2tjFoT%2FjzEfB8K0fkgduPfkkVR5m4rLHtIPA3dCP7EtAWrwISIQdKNGNEBkSixTFgFYlbfFcq4IIz1FXUKWgD2ZX5j2adOZB4Zeved5llHZJ1xV2mM8DTVKrWzuIJ0vsouGIXv2xePyZjaLQj26ehswo0tiOrpk9M8o8t94AnLns7xc%2F2XEbFCejxhQrxYWsdLWz74CmNS3gOwcxmN5HP%2FOIMUfDMv83jxExXglY%2FxeJNyndH3m%2BFCFZTvBpfwmwccaWufBTwbT%2B3DnqQuialt2th7jalIzofihLXc4rSJSKEYfGqkdW0RhqRQJ%2BwNDs9Jfvg1apXzsDwxbh%2BJbzt6MXpaB3Zm7XZ5Dd9o30upFVTs9Sk%2BMQnMI474NZB%2BHzHiZmPYg28rYEBXuvWSMSHtUemfUmdgBhPpwuB6mvkoBF7PovSAGlbN2b%2ByZi1%2BvSIobXbhji%2Bh1JxmDl7rkIwBot1rLFlPRAK7K99dAbo1mnM4ULljFtWb77cnysjfhy7BGd7uS8GO2zva5bVKLm%2FwwJspfXf5B8kJIEK6yyU7L9pegSMQ2TZ%2BSdLS16T2wNBomtGDeF2nsi6ORev9uMOfO98kGOqUB%2Fi%2BnGsOB7jrQ1oNPugJ2aG3JSCBG%2BGqls3gxr1c3Myqb5cTZasiPwlWEbmHZ38CYRUCATen3XiST84rk0QhjGVXllBfT9kWMh8qodwifsahRdYNfRuKpq6rTXoO61msqlYGur4Jytucalljgj0vgyE4WJcIrKAEejPXfVG4M%2BF7HM%2BusRRBMSrEFvGajlZpvrQFlNN4FhD3pWwBIm2P3%2FCH7M6Wt&X-Amz-Signature=d465a819fd9853d43d651fdec836b808fdff9fabb6d452e4b8e97b773feb38a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.apply()`**](/1867045b058343e1a66b677961515907#9e6d1643dc24411181facc1dd3265ffd)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fc4e68b2-6e69-48fc-8b2b-7a2dd9bb5ad8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=988903f41dd72694ee8125be93856b08b75a2a221f837b0684631d62d28ac407&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df['Goals'] = players_df['Assists'].apply(lambda x: x ** 2)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b64c0a7a-487b-4898-82f8-ac5ec8adac14/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWB2QF5B%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCIBzRzM14GupGJqeEOCCfrMxnGrjIaqxfZAlA%2Fkm2o8wIgbKM6ilzIm6EDHl%2F3WPyrI0ot%2F7sbK3ldlN3UZqEgGswq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLxbkFB%2FrklqydC44yrcA2J1eUvU03ePQXtngnupMMfqSfE1mLQDhjudGjv%2FZP9e2TnemOAD2diPN2kopnSorlPIJ9H%2FitE5%2F5m2bAvC12DlNCKES1epoNjX1gEs98N%2FO2vfHcj7N0KmJjbZP6KrnzmlCna9AD71HQqPlj1ZxaVV4zVy1Dmm8Rz9RvJ74EDPco7eA7WI8O7c5L8h4jaz90jikc37yZchyCBN5uPqt0eTOwjHEXr9OO1SUx0%2BH2BzMJVh6xBQqPU0fA8oY2GyojZ7JMPDAuAirMaexglOaVhAcOXqtLOjxcmtG1CyCxVROU4RYkjMsi5mo2f0oMZiwDvK%2FU6h9Wr5zMigNrrZhGUq4xZW5Z3bKSjGYc78BOEkhZh3NRCOSZxGYMKSQGuYdgmhnlpYDqdQZ1fhPbXF24kZfbwkPWiNED9PN27EU5SofXSzHXIHRQjqdw8yUqzlGW9MCINwsvec87T98nSkWsLJITAhta8uHBUVmy1sOmsdDDyyvlCJdLlhmI0Xu%2B6xRrxsjRaUEvIDrnk5HVYKAB7bTel2JnV5Yf980A5dzyOFQZA1KcPx2JOZKEr07L5JsSU6mwZy7t9GxGGW1P7bBdPKEBVrLpnOTPSsG%2BHRmirgiwPnCc3OwulDo3TFMIXO98kGOqUBYJrRKMfVCgb%2B3zusY16dq7s0zhvekxLWaj9TDA5Ccx9BjAeWiC1qhLJ3XHIVCN4s6eQ0Z6Ov2sIpMUnt0ExuxJ2KR38UrP9pKKnk6KGjP3khc40QXzn3xRVh9Ld2lqJluQ28m3KOnRYVFrl0MfT9PzNpDAo7J2sRx6z%2FT6lEX2I%2Fa%2BRvuaHsAzxNXJHoE8qJb7Qt3X4vfBTPndk4oBUUWye%2FXl%2Bo&X-Amz-Signature=d8735f77aa199e7df576564fa5c0b6e5501757ecd79d569a5149281e4d66d648&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
players_df['Games started'].apply(lambda x: x // 3)
```
<details>
<summary>Solution</summary>

```python
Rank
1     11
2     10
3     11
4     10
5     11
6     10
7      9
8     12
9     10
10    10
Name: Games started, dtype: int64
```
</details>
---
[**`.isna()`**](/1867045b058343e1a66b677961515907#228f2dfad24349f9a7156edde17dc6b3)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/15255d09-bd19-4260-b8fb-c9b0046af1d1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=4f25b92f027323e1d3dfdb14e8f6b52572d92465e9fff8ea87b4073bfb411955&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df.loc[2:6, 'Team'].isna()
```
<details>
<summary>Solution</summary>

```python
Rank
2     True
3    False
4    False
5    False
6    False
Name: Team, dtype: bool
```
</details>
---
[**`.mean()`**](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ca2c8f13-c055-4e00-9df9-3ec299dd87ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IQM42DW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA0b8eIT7kj6kTCGP7Kv4gmo0egwDjwVynqPBEr6BJl3AiAHaxPYIRU7MfdjHkBy3K3Eq4xokUKGJmMW%2BLa4GpOgNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMm65zmqZbcvvk%2Bs28KtwDP92MBK2aEV%2But1fEBqfFVrEA3UkCwBqsOQvN0qUKZSlYR2894IYLkSHFoLznuoq5vhQvAxPDu8eooQI00rA9fTjgNm%2Bz5tL8IEOLYkMqML7UZ6khloLQOLt6Y55L6l6NIVjaDtumzZ4Evyz%2FvCIhDgJk0551UOKCWB81bDGsguttKSrIRZq1XyAery5cCDbIsU0W1WOg0DEzss%2B9U12kTl84eu1Y3S2veAxa5Lj%2BdsqN5ZNOuZeDF0Idx80bO6ggAc2jSlzm9tEw4bdsuwlsA5%2B4btLVIx9r%2BKMYzkD%2F7H0lPhuUP1fJMSJJyAuOrePBvqkbzgELu%2BERlYqvXogXWhdirkCeCTtdNsazQbxm8rP2B2mCiSADIsJQ74i8oNXddaKePwhH0Azmt4clxRssUBIuUxTdn98%2BZDFHqOSJ4BU65EWcw5Skf9P%2FAUKgyo9cr6UfE%2BH15a1tJX3aQDTDfTjXjiKfjhEha8uKLLPPlF4PeUy1E%2BZ3mb1DbB2GeghHVVuIlrjNa8NWKHOh0psHa9wo66I%2BPge2yiGmIU3IoZ4OjiDIb8nnNNM30hXvNOHdZ1HLonG1tvYX8sr4JLmSnFmWrcjtCAH0p8aDAojPxZ1UQKBZCHu4rWhTkmEw5s33yQY6pgGOY4ShBJ2yBd21dUuTW6Ek82%2BC1LHW4wRI9FUKwBI0xQ2v3vJ9%2BKLNWo%2FQ063Olz67xXxIN3vliMbVoDKmGQtytH%2FUYtyUgPGTwhcgQftK7RZ3rsn280OPKN3rWO292P9NoKVqTnOsV7D%2Fh8y6%2BEXuhMs%2BYRtlSV5inm3mOo%2Bs%2BXq%2FxF9tbdK29zPLuKWpkMKH4cuMaFqQDHQhqaRGOswIVmIZL2BR&X-Amz-Signature=e03e4900ca2365bcdb81b16e60f1a018c70228aa81b7604851d6b151930b9d24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df['Value'].mean()
```
<details>
<summary>Solution</summary>

16.11111111111
</details>
---
[**`.get_dummies()`**](/1867045b058343e1a66b677961515907#76a2d8cfe9e242e4a106c2954f3f8cf7)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/61c79be2-5796-42fb-8606-cbf8744fcb7d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=c364b2df76c5543939da75b7387dc605c09a130d23bb3deb42e6d54ca469eafb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
pd.get_dummies(players_df['Team'])
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e9c3802e-1d27-4cfd-9272-4e99b68b1e6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCU5LBJ6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIDcd9Y8SGKg%2FP8Hpvoq9LsWDiqwJpjt1hCRHwSy4VjbgAiA9fYZwR7TM5Vrd%2FoT1pWOB67P2za5IEAYYuxjyX8sqwir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMaScWxnV5mUWMUybGKtwDH3mrHoSBthmq%2BCd8OID1qqkijL4BqTMWSkRgsANEnLN2UmWJpOsYLa4FA3VksHMysI%2BRzjGKR9S6rR8VBxYROVTY4y5zttC4Pwqz2GU96q4iiiStoA%2FiUbidPDxM%2Bk0D4UgWCoZEKwy0IizC9%2FIBMgZVJ8xT%2B0jyJZGtqAaZT1SZDZTimItXq3E9q%2F7fNSu2DmF0EX%2BczbqiAudcjLGpXU614EGVSU0XBGk7XCqb2mreHNraoFexz8bzngXA8yPuGycoSvj9tlSfm%2BogITW2hejBpebtw6%2FC8m7b4XMlsUwJrVo0YEfRU6ch0xQcamqZsLUDZWxiKYTCa0u5HZbuBC8fhzSUAJ1R3zu7Pb%2FgGyFs5lZknyGn4NZbl2JLx30jv%2FzkJ1jBTvE7kzsR54rwKOh8p%2BeqxfqtjjmlCtzlRoCDLySUsq16SMTaOInPkimKbJbQ0tETjs7xMexhNUnCXRz0DA4G%2FWzUs4fAPUAR1nmmMFoSDYtMENg7OxSVlTZC61Tc%2BxM6UHUkQtNUxnjICqB1l7LwPCQdyXxUqNIAg%2FSTvzHNIQp82TI3TbFaBah8AGJp5SeUvJlt8%2FrJg6rS26o3Lx4ufEuswE45DRNV9XFxhA5ygL9oeDfkLYAw0873yQY6pgGcFkPFdqR3pB6adPlCakkLENfj1sGhG9Ey3uSr4gh8xBNXYV3H7sAe2C9BAHf2GXZpPrZUR%2FDIAb7B83BG%2BDoqC7wCVIRKA5tiJ87eoroJOMrq%2BkgyGxBJxR9qQkrKTMhJRtDDgC5ts4XyYrQ7k24GlgRFyeTH8pIDib03q%2FiYoQKwGL5aLLTQgldN43NXk8EqxorC%2BUcxKiUj48%2FQrPwc1Cg53OB4&X-Amz-Signature=be791fc3ef5ca93d85c4671aac2c0c75bedc38a4830d7543c3f68656def24728&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
`.mode()`
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ca2c8f13-c055-4e00-9df9-3ec299dd87ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=7593afc44b3dda472318877342fe02fe09fe222c76e41898612ae59be4c7aed6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df['Value'].mode()
```
<details>
<summary>Solution</summary>

5

</details>
---
`.median()`
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ca2c8f13-c055-4e00-9df9-3ec299dd87ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=7593afc44b3dda472318877342fe02fe09fe222c76e41898612ae59be4c7aed6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df['Value'].median()
```
<details>
<summary>Solution</summary>

10
</details>
---
[**`.drop()`**](/1867045b058343e1a66b677961515907#e2a0a082029042d0a6f9e7892fa68a92)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ecfe5584-1ef8-41dc-b214-722261d1e43c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=4e848e590b03ece711d478b0d89b073413acc4080272e3287661e7fe7f3f88d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df.drop('F', axis=1, inplace=True)

df
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/51237813-dd6f-4c19-aa36-b1ddc9b8c1cb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJUSA5MK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDboVR7jVMxnxsB8KzDKzoUL%2B%2BYYldfLvjd9NRXCRkY7wIgHa%2FKs2lCGvSAidOB0lG2HWTX1%2FNK0yIrULinE1UbcHkq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDGZ2AYEZcgfTXv5dryrcA728f15OynAb3zEko9%2Bfs7IlBJ5m3mrxBcmS5Vmmkybje%2BLvBWIqKzCACU%2FSbk7uZQaTLFRAqlDt4NJknqfgqRmYwYfAWJvjVIPmHK79GP4ULG3tpocwyBiijsOVRBoDT7w63u6boa886KvehPnOEmi8GOjyoxVxYAdbt5AozTMnKgJJIYxf%2BS8%2BqUsSj47Rg2LPYMYSTdtcS1VGxDOiQ%2Bkr1ABs2cJMP8CAnex9GkVq9iUXVnJagJQL2cnI8WRJQF8PJCtu5mzBzOWbHdmT9PalvuIahGt9gUCalnIao5uOuhuDr%2B4E97n4%2FbL2Mx6w2eIHUV1MxREH28iDzun2Jst6zF70bjeKBbyRdbbZgbEPd8ClHf0zFMmTGSBdbPXjnpKvFGj%2FoAiby4Ay3YFTnM6FBOhYuNthceTpIhdqhdnqT3UzIASUpAEtZoOHRcQ42zl5YRXP85gmGp9EKTECCos6cjcHp7EvizhADQA0HnEAO2In%2F0HRdvZVj7k8lEr9kNECtmFvJM2s4veriMHi84gm7IpM0fitiLnKEWMFw0Xv7VzbK9oI%2BOAx3MAmgb5%2BDluJnSbxXWH3%2Fd9BG%2BY%2BU5eRzz1KCoWhFZYzZlbFV5XAMER%2BnNkiWPUD69KBMJrP98kGOqUB3QbwtWxIXabNYGFlfKjjlS2yulQKAK2ETaIq%2Fx6wYEc%2FpGw%2BT9adHyaZoJidP2NY%2FXUgCvRy9oFLTU0K2OO%2Fu%2FGtZ2iTE6rmA3Wc2j9pI77wH7Cf10h97whD1WuAS4B9GhSLmTJCxWcp1SCOHeRWY%2FB0Cs6vxRxHJWtasKf5xAw9cbb88m30JbVG%2BWYcxV9%2FoM7hzkAoNaOIa4nvL57l10fT1rL8&X-Amz-Signature=aba0a06d425cbb0e24f20b8c43c3728b4cd5744a0c98b04226c83fb69d9795d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df.drop(df.columns[5], axis=1, inplace=True)

df
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8004f3ba-d7c6-4c31-8bd9-ea17dd3e23a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645GQB6ZO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCWEvxbvp25QuucFr1E0KpqN0hfDHZPrO6CbMcksor7ZQIhAPZoO6Hb1TkgZk1HUp4SOxaqUG%2B0pkiP835ntXAYNryHKv8DCCcQABoMNjM3NDIzMTgzODA1IgzF0O%2F8hqZ5YRvRJtcq3ANl%2BFfK3ODLJ%2FiW6RhPTAH4eyVU%2FmJopoUH7DUPHEl0nOTBMPSH6cnJW0wIlz5QTeasBNLRHKrARfmY8aL2RQ3foGPwlfwYypuhQlVkRAqfB1Nm%2Bbpg2r47LwwqsLwqa1q5RVgoZzXU1pP2Gzjsy%2FUNs590Vxkk5sZIMslXGd5klBBPVl4JlNwIAt49XN%2FLxP7tLQi%2BETOmtfpk70cJWPto5%2FrPZ4TRB42AbCtGJx18P1e7meimodl%2Fj3jLcWhrKSEuHGkp%2BksEtRb1ayx1APNs5Jrv1dPl%2BaMAqto7i8N0CkcA93gidvu3rCPNaTnNO%2Fo1KTLnuRVsEqD5AD%2BmDSaPsy0RDmFRDJx98dXT3UuptW0Gy0UKfOaDLlnN%2BfM0l09yMf8tYJ7pD3oPuCG7p1NkR6ubQ%2FiY9KwKYmwmIFgLBmDy5ox6QSSFMQ54z4VP7mzycSH58RqS1e3olcO4dEvcjmoJwFLGfSIjdctfDtMm1qWYANNVRKLFvxtUbAiMekjc%2BP74f%2BdIeXL%2FZzOuQwpF4Nn%2Fxw1t3s2yYp2laLvgRp79wHR69LybiSfkE0dliLi2mEWEe5tfa%2FQS2LHTjde4%2BECdhx6qtO8go%2B83afsXt%2F5WuMEpzgnkWXa5izDSzvfJBjqkAbij0NQUONrq5C%2BFr23sUeBa17AYfnHM6sauNAzKNNQj2fF1WgPw5Ia%2FxR3M%2FEavrwnXQYGhRRVFR%2FjiyRF%2F4tGtS5Wyt%2BxyT5sRCFowEmlvqpypiHZpHRGoXyDesqNeQlrAEytlE74n6LaVkso3ZbGxZQwQ1qUxzVYwsAB4Xvc694GTGKn9SrKvrfN5csfmiq8RAHXFI2Yp8L0LT2D9Ufet%2FWMB&X-Amz-Signature=1fb241e07b6b516746499dc93b103e3b5c02f64f32b29f428dc6f3b6bfc3840e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df.drop(6, axis=0)

df
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/03ed3693-8267-4c3d-a7f4-63f2a23f50c4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RAXFWFB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICkONtuhx8oHj8vTX9Gbz9CBjIV7y6WpraX2MPT8jOTrAiBZT5mkgB4QcF4nhkDNNJEu0If9JPQTfx06B43SWtf31Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMoS8Q1COabrzwxqloKtwD9IM6Z35Vj%2FMl89eCo8McVoMe2r%2BEWcQ%2Bmo7pLdic5kqXePGqemhHLcP9PuzMYEl5Jhbi8lhvh69i0XXCLf2aHesobcPcwPFRVyL%2FvL7b0g0YzyXIKZDTlYGscqR1k7fnmf1Me9Ur5SPDqtoGO5nkffb%2BBlgqQ3Ndc1WnOnRfiExgcoG903SqMZpUTpCPMY5T0JF5UpsVyrFmUNtA%2BRVn2i5%2Ft30S%2B%2FBW3piNhLYZ3nsyu7Kd1%2BgIzV6p3E9El2speWDF3UW5onz5dgqxB0osle1UpV40ZKdUb%2BrEpK%2Btdrfwmuy8oXjBLXvAxo8x%2Fk92d0l8MwbzV9EjwSeGljkktFjAIjxoR8mrJ4FCqwQo7mY7qlrfUIieivqSauMhjwZJnrK1LJg%2BenzQlXxq8kmwmT%2BSNKw4MfmHwkDXnVU1htR%2F%2BFe1Zc1s%2FXPtO7mrogrW0mYceKOZ4yglP%2FxoIYn8Tue8HUckvBmS95WXYUiq4TbD%2FNSvhyg9Qpbd9vw4YGpA6nZdTzFsn3db7Ul1srsJcLaNcCLpF6QAlu8TrxC9RG88dTV%2FG9jyHjNBzwbqqAdJVjdy9PrT9p2SM7KgtG4pVXFMfyGXmEGqVP2ga3gwQNZjeL7XKQa4jA19S9cw6M73yQY6pgGtrDKqSwrdYKEXWUx4uFxvuIKhSE2fDOwPk0bEIpADdkuukAGTkhiVJloAsYncc%2BKY6oJxMmIdGyTSwSUecrlk21Sea7mkoxBewFKR%2Fb%2FJ3dxATN%2BGZ07gw5Uo2jRBRNkbSzF2bgaKQaTT02mUlzOS%2F0TI9dj6e%2FEsFoe0ri0vpRUDgnz%2BJ8lUTdLnjvB4aCDoUP1B%2FJr5M4x7PUdD7up7lkVdLdco&X-Amz-Signature=86675716eb3570030e2f048a3ebc5c12c55b0d50230877f8596eb1b3040c1f6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[`.dropna()`](/1867045b058343e1a66b677961515907#3cd5de4bcda14709a032d08303eaa85a)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f722e558-7e32-4369-9d54-1a196ec02f31/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=168a895303278dcf58784ec885557df0450e4bbeef7eef43e4823ecb5caad985&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
new_df.dropna(axis=0, how='all')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/84d981ca-a81f-4f92-b15d-902263a87a8d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVDG2QGM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHjUx86RrRy4ZYKkJTTD2tCZ2mmNDAvwuYgTxiPQCSpPAiB4a0U7VGHzaSDGxbjLWWoz0OF05IWVtuq8vmC7AomdhCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMGrKdIFiVL9%2BY58XlKtwDGqukHliX1vgKwV%2FEwkz7oICgTZZyJUq6EIOeeK6ha%2F1bVGm5toE%2FzSGwkB%2BEDUc1cbsP6QlTu4AFETNivD2AfrbUTKBO2yc78rTYqccrBeNNTlE0Uqver4OGbg5OKzo32N3KiAEXImjBo5MGJFZIOTORvi78ZqsaewE85hamPk2MpGIM00WOw1rvAtHSm1nyQN%2BUxeTcEm5gBxMm6HhXpIedLHGN3uARkmCpw6r%2F75T9Az2Im0d3jxIMAf37QjYVDp31Vedp5%2BvCKwL9n6%2BEVnd470qvV1iKW0t0568%2BYg2pEe0GRSlmNtuys6OQn9OnfDHQmk1u36YGxPCUybpMa68%2FYnB3BJXloYjjZny8xba%2FKAAOB8eQVG9xIAwOSCMAhw2m6hy5mBzA7qV4%2FV%2FHQqRLNoS1CNyofS2eVa04R6%2BbRGj36VhogQHMnShTB1PZW2DxoLOZukXB9XVxoyATLrLJs%2FtmAj%2Fg5Ivt4kXWGteOSZNXCYErusDJbv74rh1WLK4OmiAze5l%2Bb1vpavttkp1mdwrM7kNRy8LY0M5PNORKwVzkj5JmH6Dk2xuCDkwJePR1RnhWjhb53rbn2D4yopgoiq%2F72IzQAItJ0v9gEiR7ym5sT4xqzDxonx8w5c33yQY6pgFX%2BIkCiLAYC1%2B6ket0hU7ZflE%2BfOqEMEC42LY%2BYVVAR6Xu7TaTfIlrbr6QgpO%2FwpaZ7VutwCnOhOzoG4ocVTadTlekloRJVGkM%2BMw%2BFymSTzGVqwUtepOza4wh7knpt84Lulpd%2BwgJSlqDNGiH%2BXmTImUYu%2BNgMgRFfzfIDFEGlqN5W0HIzm%2BFz0y34AyTdchIfbxjGoUkAVJVTnr9uvzfEanYyVIp&X-Amz-Signature=4e064e67d9f062f4a66e40295b6d5cb470b9ce9a7a674eb2e5abc174856f9b52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
new_df.dropna(axis=1, how='all')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4ee04007-1d28-4468-8b11-0a2f47859c4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QOOIRNG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDBrWVuGDy%2FMzkT6ifOoAjBSw41o%2F1hm6CI8wUYx6NCVAiEAzMf7ILn%2Fq7v0A3WSSE6laX4v1SfoL%2B9DfiNcI%2BjhPS0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDAkpXYWUEac6zLIrQCrcA1JK5aVOd5N9zGgWNiA8iEpGZF28NZ%2BxDx3esx1lyX5mcwx5R2zTifetVMj0%2F8%2FyppfpVfNSfJnWx4PTOhIM8kDr833xL6%2FCRUmNdjLSGLbc%2Bx49My5stjlClx3Buk57Rim%2F3Zm7Hbsitt81cul5AM9ArhSXILcs35oyOLWPNNN%2Fp5RvqN9jUx0ps%2F9eoKkm7chgwj0j2pFNQeY0NloVZynn92XmkoxEprgzZQ0tqg3sEdCaRqkoz8VC0mOY94EuNd0BdLxKrTaTyk0QylTNk52aUETPw9bcL8ap6ZEt7lRiTuo1D3aZ%2BDK94O4y9%2BhgrWc%2BsV6v3pBumpEkhzIlzfPvMrdVFk8SAiTrlJ7d3aA4Bib6hC4lQy5Am4zTT1y8aoULPj5bqSTvsnXXhj6bYJU1W2B%2BSWCtvfCqYQ9EhTi8BOOm7bwBASBAmrX3xCbvg4Tao%2BH0wLzmgjkDz3O%2Fc%2FnA%2F0BCXfDIhNS8syFFLyFQCjfqTVBMIEVuQ1OBi0Wrr%2F7%2FklNrrIQ1NGd6Wd0oFsJQC2YsOI2%2Bh9YCxgpc2EpvKpXV%2Bfatd8hzI8cxSqO26dF4mj2%2FxzZE%2Bc9uEtq50YDJA77y8i7LABQrrYsvH8vOKtz%2B3f0DvwsBrcnUMITO98kGOqUBiPy1zEWlFt0K%2BxnUMN0gyK878pMJweQmXdO26fXkNMnQDCm1gvkB5LOuJIs213xYtZfJPBDnZKdgERlvMqYi%2FupP%2BbD1PYJwfMf6TH%2BbMBHfEjhNEqjjkKviHvpiLSRTqUtRWBjTSeKPOcnyIRGHMZAb0uob1kLz4Ua7zMe%2BUc5P%2F6G0m06a%2BLkibVl5L%2By9fhQ524z%2BesAGI0XYXwcZYbHHpYEZ&X-Amz-Signature=3117d74d6ae7c7d67a4c40c45a0be050514bd5ac61d5953057331f18e314515a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[`.dropna()`](/1867045b058343e1a66b677961515907#3cd5de4bcda14709a032d08303eaa85a)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0f04189f-6088-40c0-82f1-9e49e958a4ea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=6cb719d976cb802422231375d6d27ae2477a0057e6b918fbdaa21a56541ac420&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
new_df.dropna(axis=0, how='any')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/36dc593c-1f12-434f-928a-ed45539d53d1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBLW3C4E%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBxDxVKQr38BtFfbp4TtGkha9vQEgPAtutOrNiDoeu4HAiB7ydC5kSUp3bkU6e9k7H81NOXaz8ZBoM5vNpNzD0GZ4ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMibSqxClg3oJr4VspKtwDMS5vXrhGYyjrZd8LZLTmioplLNQIt%2FMK9G0J0JTc5E9DGIl8G50sTitbTPW3ISjAj%2BGtyaZP7zJaGsAa3Wr8RgCfeIsMSeu%2FxuGSvBHkNPH%2FxeLfBriy2nJXpZlHjsn1vkZN4H35XpVFWuw6yzF3oFFowM2PbA%2B9OeqbsGTHcvuU4%2Fadk%2FicSOsNCi9LwEzbynWqe%2FPrILdwADTeIcwv4mVOiogPWPqxxLtdJbKVqtGlwPuK8xCO6ysI%2F7U4IjMrcbMbfiLCVz%2BOLqAu42qsNmYa8iQ3BhYjdNkeqC6nv7r%2FWVeKQLuO%2Bb6ugt4M7TZJGGsAerFhoRvEJWkzNqf2XCS11udtxZuOI57yJneYZEJG6CgnnOWOJAdmxu9CUiPmVAcwEZQgKfgJQuSjkYtTNXUoXasSw1govnRyVDqiaknWOvmLhgV0RUel1WTKTO58TUc9Gxa4W8spNH%2FVEOROhLEVhZTaWMaZ9WwUeO2tIUtay7Hx7YiW78viIMOwgwl62UML2FQrDRabpg4FjmZ51THw8iMFwo16v2%2BmbE5q0KjULHObiQmRAa1a%2BsiVc%2BhVih4Dhusps2eFiOqItehTVKRiEqYkcfGd%2BeKFEQiFHReMs2xNkdDj%2FUaD544wtc73yQY6pgEmn8Y8bKilnhwMUu8MsksrspemeBo6SvDBIoHKBMjFRf3kZbLIpwhoFQDEoJPOB84kOG2HtMiiVBvzXQ1P9R0XJqMozx8sRrbR52gZW6QgKB%2Fko0nV6c9NQUJKSAq6xbxWKzzM23GHoGliDugMC%2FDKRVyeKEBA6TAa27hLInhK5OBX1JtA2R6cIlj0%2FiBvv77KGSjUhMyTzRvzF4ySZ0MYxMkpw0Im&X-Amz-Signature=208b72c56e5a3a344aafdd6b85234e5fe3836116ace1c787acbd81c9036a4d92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
```python
new_df.dropna(axis=1, how='any')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a965a9b9-1e49-42ba-a2bc-943cdf573bad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNGL2EVQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFwwgSOSyr%2B2TLoYprijdY8MtQKEz9Ca8kp9Vth5ciTGAiAjctegf6LRWtNVmqSudZXHwzXUxU0hS%2Bg%2BHqE3FtL6Myr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMmH2crvsoQMzkqqKUKtwDJUV1lwdv8CKPCLD%2F8NBDQTO7OGJr7Dr8622ZyaM5tEqpMYv2EqZxHpEb4JIaKs%2BZzsNV35kcbrdO%2F%2FCsolxrAduui62azpsfGwE0GTIW5fwhsXZ%2BKSvsWDAyB2SFEQEtfo7SMQlE%2FBkwyX0ayWIzudXnaRxXW6GtLwC6cKG6DyFgCXVth52x6y%2Fuas9n7BuzRwn6L636Q7GDbms0NctrnP0yqOGoZ%2FBWFhvRtS%2F2dZ9rhOqkCppfHqTQLkyN%2F%2BzjR8HN5t08sdY14Di1pmnNaAZ8%2F7Gafj6PxOM0r%2FbNp2LffPrFMk3UbzA0HFMMAakvHOwv5Hobwi%2Boo5thD9a2jaDvRIfHTtt%2F6AclwEXbqRAUpwlSsa7nEsns%2FcNTdS3b6u0sJrxk1AfAwg72hMFIwFl2PeR%2B9NS9U5yri1hA5qAeQzYSPY9eDziRzg4WtqLc1T4xQerq64cbLIUc8vpq47do8AbFLKyI2064zyd2fB2FCTvO9%2BBe62J2Epqm41gfchB4bsV0hXStzLU9JGuQm30lUOxbUUBdAwG9zOfKuN5Q%2Bik5mvVlbWeZEhNX%2FWfT2TfUPrd0RAlts0RauUfeFGD53da1eRRDlnivbia%2ByOMs21J9obEtcSx6P08w8c33yQY6pgEkcAN8r2%2BI26F%2BEyhysxtk9CYcb07qThImUam4tS3FU%2FpzVYDv8Cb8WT147yrEoaTkiZ25dR5ECYQj8STXGH%2FrgeIx0ayQoI3xu32W3CvgxzgdY7HDEXJIbIYZOopPM97T38llJg4Ki0gVhGuuH1M0YdTyFHm74ccX%2FDPhDlbdHptUuGHTaB9OH8bUpYHIW2%2BkqPmb9ggZOX37kSTH%2BtTl8slDsGGZ&X-Amz-Signature=a6e139297f688e51d95920df1cc2301f84161ff3d96e60468d9864fbfc122700&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.loc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7) [**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=cedc5e08e64787d648fbda83df2fa84f85b24331582b6309076a81ca8a3df79c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can column `calories` be accessed?
1. `my_df.loc[:, 'calories']`
1. `my_df.iloc[:, ['calories']]`
1. `my_df.calories`
1. `my_df['calories']`
1. `my_df.iloc[:, 'calories']`
1. `my_df[calories]`

<details>
<summary>Solution</summary>

`1` `3` `4`
</details>
---
[**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=cedc5e08e64787d648fbda83df2fa84f85b24331582b6309076a81ca8a3df79c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can we access the values in column `duration` for the 2nd, 3th and 4th row using `.iloc[]`?

<details>
<summary>Solution</summary>

`my_df.iloc[1:4, 1]`
</details>
---
[**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=a0d8d2ad96a4b3f1403c3d8ea41af0c8d9c7cc539983161b893b94bb77f7cabd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
type(my_df.iloc[3])
```
<details>
<summary>Solution</summary>

`pandas.core.series.Series`
</details>
---
[**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=a0d8d2ad96a4b3f1403c3d8ea41af0c8d9c7cc539983161b893b94bb77f7cabd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.iloc[3]
```
<details>
<summary>Solution</summary>

```python
A    30
B    31
C    32
D    33
E    34
F    35
G    36
H    37
I    38
J    39
Name: 4, dtype: int64
```
</details>
---
[**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=a0d8d2ad96a4b3f1403c3d8ea41af0c8d9c7cc539983161b893b94bb77f7cabd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
type(my_df.iloc[2:5, 3:6])
```
<details>
<summary>Solution</summary>

`pandas.core.frame.DataFrame`
</details>
---
[**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=a0d8d2ad96a4b3f1403c3d8ea41af0c8d9c7cc539983161b893b94bb77f7cabd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.iloc[2:5, 3:6]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/71fb880c-fa91-4cf5-bd8f-ef84d991d57a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQFU2RZW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDWf2qI5dZOMO2MFVmOcHcaogBeo6Ue6Mb4mtameQVNkQIgUkMR6XTTKT2pamNZ90hVKTsV1UcszPc4VFwcALTDOHQq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBg%2F4s7tPcFj0lGYoSrcA%2BBuX4GfI98Bg4y833%2FndEcf2GC3P8NzyjICTTIy0s3u%2Bzlf91pKUzSWC2IHIzoFCojdqvmkvAkAykhSpHAhsvoIhDx%2FHD8113320YRPtXRLiFSdZIX8XndymzMOd2rUo9F2PUADGsPLnqtZO3jYzhv5WYKMPaPtF5z%2FjFGzaPZ%2BlggX9H66ei4NQsDFNZnDA8WwSLGZJvyh8IlIuPeB93fQJbLnoJdg%2Bg4706BAen9GvQ4QWxiFDld7O0T8Oikjz%2Bm7DmJfUA%2BvwePEDt%2F%2FrynVEfMcthKhBO%2BXnnTSBHE4TeqmQZF0z6207B0ZYJgxaXhkSBEsHXON7T%2F8%2BL%2FDe6rvw%2FQ7Hq4nnMnDJHGyBwXzH3vQ9uQO%2F%2Fc8bpqnv5jtdudE8QpEnrTGYgrd8WTMRpt91fyaDoWETBi8hcP2uZwubwShVKRHYoJMR6Xj9GVkx1qaFwUyGoassqJny9U%2B8T2CrSMfcDlNsHSViCjZ%2B1vj6epY1ghq46ArwUy4BuGFflzLXoYvHMrTdyiNIuwt3rN82ShFizPVOGwUPOPeMHy%2BTCAmaj1B1pbxpLkn4ontKXfxmZ81ssZdaSFyFFELoopBp08%2B6HJpcDBdDzUKrBQIqRRm146mXmunuF%2FYMIPO98kGOqUBzxmMTV1it6%2Bu8TGdvrOPqSpQVGzvuMGwU%2F2I567Goi%2FIqS1xYw35IAxJdFh8OcY1fYf73f1orD%2BaMS8RAhSwDAAgsaAFYNb2MhDMQM1uGbDopeD0IvbL6EcqOxm041aDrQPlFQt0FvzvGHdj%2B0O%2Fa%2B3I7RlLH6%2FZRG4rXX679mwIhSUC0mlkYrN1zLvHpLlQIJggs%2FDV4cp68K5PYcx0y661Q68N&X-Amz-Signature=08f447169db729662c340d4d91ee0867f246bd3b39f61c37dbe173025780ac46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.loc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=a0d8d2ad96a4b3f1403c3d8ea41af0c8d9c7cc539983161b893b94bb77f7cabd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df.loc[2:5, ['A', 'J']]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0aec0518-7834-48b9-a0f5-08d85640fbef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO4UACHS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBdoKkpqpdwxc%2BIzF5yNLg%2F2pw2wXIqSyogX9o20L1f4AiEArWJFiovqXPgaWmX5uC5V3oWSQL%2Fw%2B8s71I8msPvavggq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDP5IZY92AN3eGYAlRyrcA9mffsV6NARiUFfKqwBEMhUEAXucXw%2BKWywTLhcyw%2FAkLeCWwJQbDyqE6EUimQk%2B7ycOecrySAUGA6FnzBogjChcBA8jHKQvtCM%2FjtfzG3KIhExIRKeb3FOBwD%2FX7575izOGqFF93IL%2F3rouK17outJaCcBLNFlzVqd1WHBhQ8okxDdiv4gq6scApVeoM9R%2B8m%2FbVCGjQ7A%2FzuADym%2FrVXJfwv3tS%2BKUruk1tMR%2BwkYpUwmVFnECR9wx5Ax6zr3fn1Y8RMga72B7yQsnM5rZb5NB1O3flADlsVz50sjljXA1pp9%2BZAe%2B1gnkCIGetAPJ6S6SQ55vV%2FVQTeX0m0qOI3989pEuCB%2B6oem%2BnUqgbRhHgcBtwBTuFb7XJJtZdYKVta6PV0tvbcy7iQvi3%2FWLB5V0bj%2FsWzDm7Z7bY3tJWiNpNJ31co9%2Fiwx5GXFWuJkMPyvZky2lofDnOxZNcTFdVCzr1xQzGX69cXiSM6fydDw1FMMM6dsIwJ4iWIITYfqE0Qn5Q7GGbb2FGAlaV9bPvXnuqZxUPca8Tdpio4SNqLIef9v3h%2FThN1PavLbMZwyDGJGVJqRd530l8bRMq6857HP1PievGOOlRulZyPgKrsZhRSDkNtEpxcNvw%2BHHMNPO98kGOqUBgXwJKRiB7FhhpA6NTqgQIQ28B1kahoRWBbu0NH1yzlRKN28WnNcPUy8xmdZskPRKn6yiC7dfw3qqm9fypWBqeYYGxfLqiLCxbTY0buezRopUbkOcCJ5zS1P3BlJ0R8kmLLUDhNWdEwQD8veJrPBnAz9tjvXtHp0p3h%2Bm3ZfHufU%2Bx1Aa0uRoHl5yEJzv3%2FPzfJjULVivsty%2BeGjrB%2Bflr0m%2BZ%2BY6&X-Amz-Signature=1c385cc0cfa38b5768ba7bff642600265a546ca5debbe0bd0343220cd5ac4c17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.loc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=a0d8d2ad96a4b3f1403c3d8ea41af0c8d9c7cc539983161b893b94bb77f7cabd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.loc[2:5, 3:6]
```
<details>
<summary>Solution</summary>

`TypeError: cannot do slice indexing on Index with these indexers [3] of type int`
</details>
---
[**`.mean()`**](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=cedc5e08e64787d648fbda83df2fa84f85b24331582b6309076a81ca8a3df79c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.mean(axis=0)[0]
```
<details>
<summary>Solution</summary>

`298.0`
</details>
---
[**`.mean()`**](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=cedc5e08e64787d648fbda83df2fa84f85b24331582b6309076a81ca8a3df79c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.mean(axis=1)[3]
```
<details>
<summary>Solution</summary>

`130.0`
</details>
---
[**`.apply()`**](/1867045b058343e1a66b677961515907#9e6d1643dc24411181facc1dd3265ffd)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BJRQWRC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEmJl6koMnKgXwlVaJtSUzp97B3iVRpwnZWC3zYGBeJxAiEAwC4HRNTt4A7ksb5l%2Fz5i3XqLSzspQW9p8V9TS0fpkakq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHKhJ5eNA%2FmebY7SMyrcA6CRcU1vqmYfsgJmEQMwzkTRMODMdp8Qru9azZM6%2B7DtAB00zT6GgmXE0tgYHgQeeoVAvgaZ%2FExmJmUSEZaa5zMC1Txj2WV2OYPZ9jd7ltDUfqzf5HEIs35uRFfXADIy291Hu7cYvIrzEZlB59ZkQ6KW4FEuNfmxkJAJ06LlZLIgYmMwu5jydCfF508btYcqypRWPfjaEjWT34wbJnTWxd%2B9lXLU0oWEdqEjorNhVe584Z73BstFGDjtwCqB9L90fDEbGCZpcSpRgV14i%2FAtJXManBtbXJ8oz7FqO2jX6nsKMd%2F9a7wjb12%2BK82kHVK%2Br6t0cQDmdoZYjG8h1WuzWAcJ1WpWRQt1lF%2BflUkhGYmxeaacobxFNc64LltZjXBksD3UtmyEjEmtkB3jcs9EOVJye9VJRZR1Sd8KYOdUYOmS2QmyGVa5G8Qi7GVtK3L8w32I2o5U6vb8DCxUk2wbC%2F7lvvYt16xLDIKXVgp4w%2F6mnSLCN89fv5jb%2FCPStV3hurzPaJIfDVwS5WjLHp25%2FtSCwkqEOelkDRhcVrwjqwmDpZoK9ocjpcCbBZVvSmmdeZ%2BqUTzTGUkguNC8xIMIrBPtBHul1cwLIRXrSDllmNCXlo1Y8fqYpO%2BdRrdmMPPN98kGOqUBpansn7BCZp5%2B6uJ0qze9eA0b9Zw0f1CuWcBsaPUxE86P52PALDmPeqQQbfRi5%2FnsxcbfHFdw9n9ZIYcDZEXp%2B9r2MRiyrWEKdGmuHKwgeSHa0r4LeuOZiNSALS9sLxG8CrJswoVFwGLBAP2Iiz9o1EdEr12hUswHunIw0Ofb40199R%2FVux9LFmxIOV%2BozLYtX85ePSQRpfVOz%2BF%2FltI7mCGiRiaY&X-Amz-Signature=cedc5e08e64787d648fbda83df2fa84f85b24331582b6309076a81ca8a3df79c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df2 = my_df.apply(lambda x : x*2, axis = 0)
df2.iloc[2, 0]
```
<details>
<summary>Solution</summary>

`780`
</details>
---
[**`.apply()`**](/1867045b058343e1a66b677961515907#9e6d1643dc24411181facc1dd3265ffd)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZ2SXIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCe4SNFSNulWe7QS1phkMFYbngZKPildE3L8EA1vkNv5QIgXkiO%2FeWum17VM8IbjEJIHct7CFJ1SToIX7PnU3eyC0Mq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ2CSgoXGIYyhpfO9SrcAzz%2Bb27KBmlbC4AORmzvFUD8iSzskQNs1LKQCzhpPTKx6o34Gb8XVZzCEwgi0QfzKN0UOJSUGuXGykWVB95tc47R4oZhZT43n7Q6ovxUKZ949hjfh0clfiAx8njL78n%2BpETcMqZslOZkgkFVwiVLBGJETg86GeLCihw5Q57rKDbgBZz7Iu8BOcQ6NneNKFfX4Z56U8DH%2F5rc8iacHmbm4JZYjSiovgHjNF3gzo8OPjPr5LhW4aimBM%2FZ0u%2BJYM138oJagHLNA7PXD8LYeNvu9C7GIJvK2BHi5Og3PHuu0rInn1cYeItgul2B8XBjSIfG14lB6t1tU7MpEa%2FODMwkVPZzcuG8mTDK1htNS0%2BYAh1ttJSd6k1ewS78YLgIKDDSle4rQr39QWyZwg4KR3IlClgvs1b99tUzYf%2FBNLiiGU2aUv1%2FcI8TiHsZbMd23tcxFPl5BljH6lkypcqTtbJPNJ5TttqhCrzEy1o55BXqCCaPtwbfJbFMy8IyaikO4%2B%2B9u3cOQuoLEtaCnMXXkrtoEwWkXs1GF5tbp%2BaOiSj3099lRSSqMnYKM6U%2BfTdWX0ulg4uJPDucmSO5SEnH71AtrH%2BGt9C7EF2RvHdrEBcLkOw%2BBjNISStUkaN89uYXMKHO98kGOqUBgViu5S9QMhNNb4bBP3XMU%2BK85I2S%2BAPCDKCGtDJwuDS42ncjIuon%2BFf4XkMxcOw8qtF0LvHt5J4Gsfgz031gZZC%2F0VTYS7gspToTiw5WOjuuvr3azt0yjb5mfmreuyVyoSyqT7GM99sA6T57Jq6Ef0Vy%2Fp9kdrmaNWIVRcVaQ6wxPy31Pu3dbz6g2KljyjnCtlYnkBmdsL3cpuC%2FG7N%2FRXtfBhsE&X-Amz-Signature=16388fb33864c7bcbde1b4143a13d06779ba9fa850c73628730cfa9db946a467&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df['K']= df['J'].apply(lambda x : x % 7)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0c813279-3e2b-4df3-9411-93753cfb528f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RTDDZBO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDH681Jjg3yZRDE0a93vP5aJJvhJ6lCo0N9E0PHhRER5AiEAv84e6kkEre7BI8tvjeL%2FFeWmb4syJMMweYePbHYnfTAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDEjXrK402CL4d5PBYSrcA6TzuXtCSATv88dEwGQ1NKuUqtl4eb36jY9O7zi9d4dQ1IqK8BkPnim7csANRIv%2FtsM0uDFo1tjLUuKc1emuIQwT%2BKWf0%2BhF%2BVVcuF8fURAW5vGEQ9n%2FSTWVEkGUtKM7XzW4S72I23AZCj5xlg9otu2Ci4RIK1XawUpr%2BK5JAzJYqeDNknP8qhPaM80QzVsUjHfWYvFNP%2B129ibvKcsseya1rei%2BwW1xv%2FQ3K5GSl3bTzVlLLr1vUsFbK1Zt86oVVaQIO%2B566mKsKcDQow%2BbkLY8B0%2FwY3DQerOo5362goSuSxdCzBKji%2FNbag3cF0ZT0aGATLgeVYjs7O8JJO7mxTIDF0aaGmc1rAJfhJtxOQ1rh4CUD1SttWYwktWTcybdbvDk2PtJ9GiMeXrBBzowHR4vdRyFhzbMiOjtWo1sJkO8UvLuNoxlLH2vv%2BbLjhH5gcyX%2FzXZ5gFyozxHr2mo8Sxp15OY173n1KxzE779P%2FR867O5FPPJsrfrIM%2FhMVAnZK2o22tYsLBX6IJTPUKorz0mwl2TUxuzQ6wo2uu%2FwyCXXTYSsN3fNTtKOR79MoPhSsP1fcDRkDDw3MBNNePTLSr%2FqvTOr%2Bg40mNCug0FuCv0Vq%2FCh%2FuROPglETrrMIPO98kGOqUB80yh1KZy%2BmVUCD0Pzten9cwusf77lKKC2%2B8kO1TlHWs76FMsP5Ny9c2dB3QoTBbakzLjBMPVuCvwnAhi2ql1erckXfn17BkLvBGbnLT9lpXCgxiyrwB16XqbA4xBgc9P6ZyM9YP7llJpwRwhgfVBQiYcyZzyxN%2BINOvlDztRhG4BZTVUIc5Ob2W5W70sGhcube6UgFXQ9pM1Dm0VqKP4ZmJeHYH3&X-Amz-Signature=883234cc07a1a6d851f193434a4ab67ced1e39928a13c84f5655b30e4a75edac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.unique()`**](/1867045b058343e1a66b677961515907#74cb3dd5af264206a7e4ccc9b07d9a7a)** **& `.nunique()`
![players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2ba26b62-6de1-47c6-8d67-724d44c6f4bd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZ2SXIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCe4SNFSNulWe7QS1phkMFYbngZKPildE3L8EA1vkNv5QIgXkiO%2FeWum17VM8IbjEJIHct7CFJ1SToIX7PnU3eyC0Mq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ2CSgoXGIYyhpfO9SrcAzz%2Bb27KBmlbC4AORmzvFUD8iSzskQNs1LKQCzhpPTKx6o34Gb8XVZzCEwgi0QfzKN0UOJSUGuXGykWVB95tc47R4oZhZT43n7Q6ovxUKZ949hjfh0clfiAx8njL78n%2BpETcMqZslOZkgkFVwiVLBGJETg86GeLCihw5Q57rKDbgBZz7Iu8BOcQ6NneNKFfX4Z56U8DH%2F5rc8iacHmbm4JZYjSiovgHjNF3gzo8OPjPr5LhW4aimBM%2FZ0u%2BJYM138oJagHLNA7PXD8LYeNvu9C7GIJvK2BHi5Og3PHuu0rInn1cYeItgul2B8XBjSIfG14lB6t1tU7MpEa%2FODMwkVPZzcuG8mTDK1htNS0%2BYAh1ttJSd6k1ewS78YLgIKDDSle4rQr39QWyZwg4KR3IlClgvs1b99tUzYf%2FBNLiiGU2aUv1%2FcI8TiHsZbMd23tcxFPl5BljH6lkypcqTtbJPNJ5TttqhCrzEy1o55BXqCCaPtwbfJbFMy8IyaikO4%2B%2B9u3cOQuoLEtaCnMXXkrtoEwWkXs1GF5tbp%2BaOiSj3099lRSSqMnYKM6U%2BfTdWX0ulg4uJPDucmSO5SEnH71AtrH%2BGt9C7EF2RvHdrEBcLkOw%2BBjNISStUkaN89uYXMKHO98kGOqUBgViu5S9QMhNNb4bBP3XMU%2BK85I2S%2BAPCDKCGtDJwuDS42ncjIuon%2BFf4XkMxcOw8qtF0LvHt5J4Gsfgz031gZZC%2F0VTYS7gspToTiw5WOjuuvr3azt0yjb5mfmreuyVyoSyqT7GM99sA6T57Jq6Ef0Vy%2Fp9kdrmaNWIVRcVaQ6wxPy31Pu3dbz6g2KljyjnCtlYnkBmdsL3cpuC%2FG7N%2FRXtfBhsE&X-Amz-Signature=20e784b796350d1862a3f496171d99725e355549ffa9966d626d13c2444c18da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df.unique()
```
<details>
<summary>Solution</summary>

`AttributeError: 'DataFrame' object has no attribute 'unique’`
</details>
```python
players_df['Team'].unique()
```
<details>
<summary>Solution</summary>

`array(['Leicester City', 'Southampton', 'Arsenal', 'Manchester City',
'Liverpool', nan, 'Wolverhampton Wanderers', 'Manchester United'],
dtype=object)`
</details>
```python
players_df['Team'].nunique()
```
<details>
<summary>Solution</summary>

7
</details>
---
[**`.pivot()`**](/1867045b058343e1a66b677961515907#b7e324abb8a749b38b4a2386f6d4dbf7)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6b01f9a6-c80f-467d-a6a2-790e9fb34459/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZ2SXIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCe4SNFSNulWe7QS1phkMFYbngZKPildE3L8EA1vkNv5QIgXkiO%2FeWum17VM8IbjEJIHct7CFJ1SToIX7PnU3eyC0Mq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ2CSgoXGIYyhpfO9SrcAzz%2Bb27KBmlbC4AORmzvFUD8iSzskQNs1LKQCzhpPTKx6o34Gb8XVZzCEwgi0QfzKN0UOJSUGuXGykWVB95tc47R4oZhZT43n7Q6ovxUKZ949hjfh0clfiAx8njL78n%2BpETcMqZslOZkgkFVwiVLBGJETg86GeLCihw5Q57rKDbgBZz7Iu8BOcQ6NneNKFfX4Z56U8DH%2F5rc8iacHmbm4JZYjSiovgHjNF3gzo8OPjPr5LhW4aimBM%2FZ0u%2BJYM138oJagHLNA7PXD8LYeNvu9C7GIJvK2BHi5Og3PHuu0rInn1cYeItgul2B8XBjSIfG14lB6t1tU7MpEa%2FODMwkVPZzcuG8mTDK1htNS0%2BYAh1ttJSd6k1ewS78YLgIKDDSle4rQr39QWyZwg4KR3IlClgvs1b99tUzYf%2FBNLiiGU2aUv1%2FcI8TiHsZbMd23tcxFPl5BljH6lkypcqTtbJPNJ5TttqhCrzEy1o55BXqCCaPtwbfJbFMy8IyaikO4%2B%2B9u3cOQuoLEtaCnMXXkrtoEwWkXs1GF5tbp%2BaOiSj3099lRSSqMnYKM6U%2BfTdWX0ulg4uJPDucmSO5SEnH71AtrH%2BGt9C7EF2RvHdrEBcLkOw%2BBjNISStUkaN89uYXMKHO98kGOqUBgViu5S9QMhNNb4bBP3XMU%2BK85I2S%2BAPCDKCGtDJwuDS42ncjIuon%2BFf4XkMxcOw8qtF0LvHt5J4Gsfgz031gZZC%2F0VTYS7gspToTiw5WOjuuvr3azt0yjb5mfmreuyVyoSyqT7GM99sA6T57Jq6Ef0Vy%2Fp9kdrmaNWIVRcVaQ6wxPy31Pu3dbz6g2KljyjnCtlYnkBmdsL3cpuC%2FG7N%2FRXtfBhsE&X-Amz-Signature=6f0e675ca50b7bc8ef068e9ad9c15b67e29ddbdc347868e23dc551424de28128&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df.pivot('Team' ,'Goals' , 'Player')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ab2ba056-0bb1-42b1-8a42-8fe72f98b327/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCU5LBJ6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIDcd9Y8SGKg%2FP8Hpvoq9LsWDiqwJpjt1hCRHwSy4VjbgAiA9fYZwR7TM5Vrd%2FoT1pWOB67P2za5IEAYYuxjyX8sqwir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMaScWxnV5mUWMUybGKtwDH3mrHoSBthmq%2BCd8OID1qqkijL4BqTMWSkRgsANEnLN2UmWJpOsYLa4FA3VksHMysI%2BRzjGKR9S6rR8VBxYROVTY4y5zttC4Pwqz2GU96q4iiiStoA%2FiUbidPDxM%2Bk0D4UgWCoZEKwy0IizC9%2FIBMgZVJ8xT%2B0jyJZGtqAaZT1SZDZTimItXq3E9q%2F7fNSu2DmF0EX%2BczbqiAudcjLGpXU614EGVSU0XBGk7XCqb2mreHNraoFexz8bzngXA8yPuGycoSvj9tlSfm%2BogITW2hejBpebtw6%2FC8m7b4XMlsUwJrVo0YEfRU6ch0xQcamqZsLUDZWxiKYTCa0u5HZbuBC8fhzSUAJ1R3zu7Pb%2FgGyFs5lZknyGn4NZbl2JLx30jv%2FzkJ1jBTvE7kzsR54rwKOh8p%2BeqxfqtjjmlCtzlRoCDLySUsq16SMTaOInPkimKbJbQ0tETjs7xMexhNUnCXRz0DA4G%2FWzUs4fAPUAR1nmmMFoSDYtMENg7OxSVlTZC61Tc%2BxM6UHUkQtNUxnjICqB1l7LwPCQdyXxUqNIAg%2FSTvzHNIQp82TI3TbFaBah8AGJp5SeUvJlt8%2FrJg6rS26o3Lx4ufEuswE45DRNV9XFxhA5ygL9oeDfkLYAw0873yQY6pgGcFkPFdqR3pB6adPlCakkLENfj1sGhG9Ey3uSr4gh8xBNXYV3H7sAe2C9BAHf2GXZpPrZUR%2FDIAb7B83BG%2BDoqC7wCVIRKA5tiJ87eoroJOMrq%2BkgyGxBJxR9qQkrKTMhJRtDDgC5ts4XyYrQ7k24GlgRFyeTH8pIDib03q%2FiYoQKwGL5aLLTQgldN43NXk8EqxorC%2BUcxKiUj48%2FQrPwc1Cg53OB4&X-Amz-Signature=94e56ac554cfcd5be0ac9bb3124a5c3a92112569271a9f20943ed8a2ecf6c7bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
```python
players_df.pivot('Goals', 'Team', 'Shots on goal')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5c172887-8c06-4769-b64c-4c4ffdc81431/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOKK2MTP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIDcW1qr%2Bf7e%2F6MRNGC47t%2BI9%2B0DcYaqU2EyxLZyvRb87AiAnier9diqvoxctZ6wed3iYlzz%2Fi0Ws5Wn7qgcF87uufyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMkltHB7X7RdzlKairKtwDnx20pvTHyhfAHQgCuSde9sMDnwUhMaeytMe5CWfwH%2BuE3zozzUv8fZEbR%2FZ2ITjCvpxMjcK3eahnJ6kg78PVUpKvzEoxN8JDrEEdWnhRG9FS7hZ2x%2Bz3sF0%2FUQzas28msz7ZQ68SdFi39KyaJ6r3n21VK0FTDSWL9ge3RfFNUgZoNjTeQv6d1enMKDuz%2BP%2Bn%2FtzNQ3YdUWJ5Cgq0Do0eVVeKwtL25XrsuvgMen52RLAJdZs%2FzWlJ%2FQdNDeu5VGxCclgD8Obs0wZitdNXWT7LNwLmE8d9vBw4fTVJJ0QEYTFFqAtRXIthzWfNNTrd8IZ%2FRhqFAiXxQpSwl3CxRmiCvZXRwSJc2f8Spy1FxB6XHeBnHEHjdGKPMOUFlXAmYFlCwzBWCWYGXxZsIhk2NBFIifecTcnJGP99EyeLea3jf3AQXnayzHcBuR0LRYTk57W8nOH137s%2Fd%2FUwXD9CxvXqBwvAu8LNTLOv8g1Hzz3HJlumq4LUHUTVdto03EsELEOrwPTITg%2BK%2Bz5dg51eRLbPALTzaSaU2EAdcZ%2FZCATIc5hnZLKY1mevUiXrjetGwAEn3hWxbAwcrJb1ME36NdBW%2FwW%2B2zjB1VifQ3Du3Wh9dnU33ZWaldLbMNl8ZaMwx873yQY6pgEvqSmYMVNPNmp4W3dk5bLbNYw5FsBm6On8UdxqTleYzeMTsi%2BxNuZGYuB4A9prfPcWMNC8Cj1ce0kA7AtEsCv6hRfKDn%2FglfjnF7dBTNBFVmnh%2Fqhj0Fd05Fi9eJR%2FVT4mEAFIDoSS3ZMAHAwx7%2B%2BIVHiG5Pa59eKafjfnfDDIXSLReNyo3ehPK0q%2FmzOD9M4Dq1ICAIyXVnx3MjzlQPTXS2kIRgwP&X-Amz-Signature=03949d56d4a763f406cc1a12b05bea0cd7399789ccddc36f8508b9497db00b83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.T`**](/1867045b058343e1a66b677961515907#b65f0a7a58214e66ba42846c09b6dbdd)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e2a0d44b-4888-4885-95e6-69a9b9a8e624/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZ2SXIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCe4SNFSNulWe7QS1phkMFYbngZKPildE3L8EA1vkNv5QIgXkiO%2FeWum17VM8IbjEJIHct7CFJ1SToIX7PnU3eyC0Mq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ2CSgoXGIYyhpfO9SrcAzz%2Bb27KBmlbC4AORmzvFUD8iSzskQNs1LKQCzhpPTKx6o34Gb8XVZzCEwgi0QfzKN0UOJSUGuXGykWVB95tc47R4oZhZT43n7Q6ovxUKZ949hjfh0clfiAx8njL78n%2BpETcMqZslOZkgkFVwiVLBGJETg86GeLCihw5Q57rKDbgBZz7Iu8BOcQ6NneNKFfX4Z56U8DH%2F5rc8iacHmbm4JZYjSiovgHjNF3gzo8OPjPr5LhW4aimBM%2FZ0u%2BJYM138oJagHLNA7PXD8LYeNvu9C7GIJvK2BHi5Og3PHuu0rInn1cYeItgul2B8XBjSIfG14lB6t1tU7MpEa%2FODMwkVPZzcuG8mTDK1htNS0%2BYAh1ttJSd6k1ewS78YLgIKDDSle4rQr39QWyZwg4KR3IlClgvs1b99tUzYf%2FBNLiiGU2aUv1%2FcI8TiHsZbMd23tcxFPl5BljH6lkypcqTtbJPNJ5TttqhCrzEy1o55BXqCCaPtwbfJbFMy8IyaikO4%2B%2B9u3cOQuoLEtaCnMXXkrtoEwWkXs1GF5tbp%2BaOiSj3099lRSSqMnYKM6U%2BfTdWX0ulg4uJPDucmSO5SEnH71AtrH%2BGt9C7EF2RvHdrEBcLkOw%2BBjNISStUkaN89uYXMKHO98kGOqUBgViu5S9QMhNNb4bBP3XMU%2BK85I2S%2BAPCDKCGtDJwuDS42ncjIuon%2BFf4XkMxcOw8qtF0LvHt5J4Gsfgz031gZZC%2F0VTYS7gspToTiw5WOjuuvr3azt0yjb5mfmreuyVyoSyqT7GM99sA6T57Jq6Ef0Vy%2Fp9kdrmaNWIVRcVaQ6wxPy31Pu3dbz6g2KljyjnCtlYnkBmdsL3cpuC%2FG7N%2FRXtfBhsE&X-Amz-Signature=b7fe4ab1a1c0987ff542509d843b0246ea1fc0c3d33cc3e8edd05d5be4639ea7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d9242361-8805-4665-949c-9386b8c6ce62/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GA2MXSU%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCID9rRghxvPU2O4hCsm7x%2FjunQ3RALzxiAuOnj%2Bt1YICmAiAN1ZPZH4RE2VxfwrfTD1T8OooP1CNn%2FF2d4BYI8VFwrir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMkK9QS%2F71gxVtSSilKtwDG%2BWvkTp2BKePYMnIIw38YeJTb7FDXbjt41SD2t99ZfmGAA0a%2FElITH93k3UE7AphxYvo9QhdPGI5jzc%2BUKm9b9bfITfYXW3IEQ6aKNZ4EL8YUvolhiD%2F18h0kCrjqq3FOdz1wtTYTb51BRhRBHZjUqzm1cgFFnr3Zm33lqBlpNn%2Bspnqp1twYWatRJ5PnJjXzeEkFIMCok3BAMBlEhBI9N5HY81hCr7djNkHYWb%2FJQFsBgCgzXcSEuVviWCn9ZP0TwjuKdXWBvQobEWqd1k3zs2q%2FiSq6AyDijIWTHWzWA%2FZvOUmcanDs6%2FP%2FZTPwOE71u%2F8kLST9MIrLKQ6gJg%2BxQc1zvt%2Bf6w9ocPdaDLrJJykaH0CADnD%2BSSW7KxEoiTOjCwgbEF0gkTtyG7RgarjxNfAVR%2BrKJBoojPIZjms13oFnAh95ZkfibEoK9Pp3VkUXHFnTd%2F%2FV8v5GXmNQVCSrjd8N2T0Z8EU3bl0dL9ncEyDy9EWxF%2FbEG6AgikM3DQH5ONiKfm6dCv5kMGc%2BUb4H3%2BO7D3FsC0FSDRE6a839uBB77nMtZ1Ar3Lq8Do1bwqUSepO%2BLe2iqp%2F1AaWaVekBQW4IoAToyUtOPRfY8iQfpNDZEO5T5g%2Br%2FIC%2Br4w7s33yQY6pgHGzeA1a%2FJO%2BsracSAlAMZg9ta2tAm9%2BwsTvA%2B4lQmgN3JMWN0L%2Fc7FIrftfIPAWPc%2BRq7Yk4IbWh8QouPzn0kaTrxjxsYsHZ0nDm8fwYMxtghaRoludEmuF1ZXrHJzEr%2Fk7b0O4wt%2BvUZAy5E5%2FuInBojcsDpBa3FwGc4QnraaKvKuv6OkXOpgmV%2FO9g80bfdRR8Mtdpteyhjc7sXHmNFU44L8xSO%2F&X-Amz-Signature=978ec651fd68a0349777a4b2303962c43bcbfc2b5f50db95e3d171229e2e55ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.melt()`**](/1867045b058343e1a66b677961515907#5e95974d66444f179b205b86fa56a92d)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f5c49bcc-7d18-46b2-81c0-dd9d73d5ce8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZ2SXIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCe4SNFSNulWe7QS1phkMFYbngZKPildE3L8EA1vkNv5QIgXkiO%2FeWum17VM8IbjEJIHct7CFJ1SToIX7PnU3eyC0Mq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ2CSgoXGIYyhpfO9SrcAzz%2Bb27KBmlbC4AORmzvFUD8iSzskQNs1LKQCzhpPTKx6o34Gb8XVZzCEwgi0QfzKN0UOJSUGuXGykWVB95tc47R4oZhZT43n7Q6ovxUKZ949hjfh0clfiAx8njL78n%2BpETcMqZslOZkgkFVwiVLBGJETg86GeLCihw5Q57rKDbgBZz7Iu8BOcQ6NneNKFfX4Z56U8DH%2F5rc8iacHmbm4JZYjSiovgHjNF3gzo8OPjPr5LhW4aimBM%2FZ0u%2BJYM138oJagHLNA7PXD8LYeNvu9C7GIJvK2BHi5Og3PHuu0rInn1cYeItgul2B8XBjSIfG14lB6t1tU7MpEa%2FODMwkVPZzcuG8mTDK1htNS0%2BYAh1ttJSd6k1ewS78YLgIKDDSle4rQr39QWyZwg4KR3IlClgvs1b99tUzYf%2FBNLiiGU2aUv1%2FcI8TiHsZbMd23tcxFPl5BljH6lkypcqTtbJPNJ5TttqhCrzEy1o55BXqCCaPtwbfJbFMy8IyaikO4%2B%2B9u3cOQuoLEtaCnMXXkrtoEwWkXs1GF5tbp%2BaOiSj3099lRSSqMnYKM6U%2BfTdWX0ulg4uJPDucmSO5SEnH71AtrH%2BGt9C7EF2RvHdrEBcLkOw%2BBjNISStUkaN89uYXMKHO98kGOqUBgViu5S9QMhNNb4bBP3XMU%2BK85I2S%2BAPCDKCGtDJwuDS42ncjIuon%2BFf4XkMxcOw8qtF0LvHt5J4Gsfgz031gZZC%2F0VTYS7gspToTiw5WOjuuvr3azt0yjb5mfmreuyVyoSyqT7GM99sA6T57Jq6Ef0Vy%2Fp9kdrmaNWIVRcVaQ6wxPy31Pu3dbz6g2KljyjnCtlYnkBmdsL3cpuC%2FG7N%2FRXtfBhsE&X-Amz-Signature=7ad1641603df5c25aab501e58cc15c4a0b88c1903a277d11480d05d4eb401269&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df[['Team', 'Player', 'Goals']].melt()
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/16d89d26-291f-489a-9140-050a0e525669/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SNCPV7H%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDKjtYTAD7BrzO502GaEau7TNERmmZYJitYCSzHLWTY%2BwIgSIGEC2sAfcoBMNpitdTRBbi0%2BrY7xZlwcZvTiwGmTfsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDL8oC0pP5oyvOzM1ZircAw0lzNQFJ%2BGnIM3dP9epf%2FZrpP0%2BqGe0WbvMeFxDEi8tL8rE2Y6SO8m7%2BPKUBkU2Aik%2F2a5sdwS1ot0M7I6ktW1XVJuUXXg%2FSBFDGOAxGtKUleSPiMZJm8mq5sVzlpi0wwnb1Fk8ApL2wylM7rzTsKR%2Fo9%2BVCAjfqYEvLK0FFk5odzdDkygM5%2Bp94jTKjYGKbG64Ppfcmb%2BBrDLMU4c9Y%2BWJAQfrAJL%2F%2F4d%2BQ7simQBpz3vL39mI0RhV5EC6pEeJPJH%2F5vBUN6Ic9kMu4lX%2FL15BpF2vhVzGbSPsog2LdjD%2F%2BPL8TTnkU%2FU%2FMUZuNcVarGQ1%2B%2B0UuNGOm8WNxtkoXDWUCxoXTltF5k53U%2FK%2F6UXAlYAm5mX5YRhCP2wbttH%2Fal9Tx0Vdf%2BVpcXqFbaw7rQQLiLSqWWnfdH4c2kIiew5MNAHmjPi44vBdlIQhZojq3mREwKkxRdNG%2Fsq0XnlxJG9%2BOBTrUg7AbBZPpq0sI9dRlwjgwEl3znQgVxRrqUJHQjh6LKcj1hx0enbRbLAxdaWNNnv3KW4FrIB28qxRnTTQSZnLjoG7Rgk2fEJCnHxOUikGFW%2BrN7%2FMg1i0ewPCELYZEhGNqC6uTDacnh8bJ9V%2FloKqELeLiX8cwpRfMJbO98kGOqUBxH4TElCRaMF7PauCRrMDYYPsR7s%2FKdj9l9DRDEWCcnZSIAXN3VA8G5W4uLeGYmnkt43qrGIM%2BIp1FrtvCHHxfQRpyhNSwmAgnidz4etGc%2FTrA7gJiI5KFFWDmmYaudJSOhjP1ATydG5cBI%2Bp9BS7J%2F472BP66IoRY0knw%2FyNSnYy7xt%2FjPjfb5rHrCVLYBqI2vU9mrUK9eaiNsGPjJPRT3IyPO1B&X-Amz-Signature=cfe90700dd1d01999900e1a5a4713ac827aee5dfe3464778e371678d7411c346&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.agg()`**](/1867045b058343e1a66b677961515907#1c8f902fb8774ff7ab8c9bd1d9f76684)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a931d954-19f8-4897-83cc-e80d61b447cb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZ2SXIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCe4SNFSNulWe7QS1phkMFYbngZKPildE3L8EA1vkNv5QIgXkiO%2FeWum17VM8IbjEJIHct7CFJ1SToIX7PnU3eyC0Mq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ2CSgoXGIYyhpfO9SrcAzz%2Bb27KBmlbC4AORmzvFUD8iSzskQNs1LKQCzhpPTKx6o34Gb8XVZzCEwgi0QfzKN0UOJSUGuXGykWVB95tc47R4oZhZT43n7Q6ovxUKZ949hjfh0clfiAx8njL78n%2BpETcMqZslOZkgkFVwiVLBGJETg86GeLCihw5Q57rKDbgBZz7Iu8BOcQ6NneNKFfX4Z56U8DH%2F5rc8iacHmbm4JZYjSiovgHjNF3gzo8OPjPr5LhW4aimBM%2FZ0u%2BJYM138oJagHLNA7PXD8LYeNvu9C7GIJvK2BHi5Og3PHuu0rInn1cYeItgul2B8XBjSIfG14lB6t1tU7MpEa%2FODMwkVPZzcuG8mTDK1htNS0%2BYAh1ttJSd6k1ewS78YLgIKDDSle4rQr39QWyZwg4KR3IlClgvs1b99tUzYf%2FBNLiiGU2aUv1%2FcI8TiHsZbMd23tcxFPl5BljH6lkypcqTtbJPNJ5TttqhCrzEy1o55BXqCCaPtwbfJbFMy8IyaikO4%2B%2B9u3cOQuoLEtaCnMXXkrtoEwWkXs1GF5tbp%2BaOiSj3099lRSSqMnYKM6U%2BfTdWX0ulg4uJPDucmSO5SEnH71AtrH%2BGt9C7EF2RvHdrEBcLkOw%2BBjNISStUkaN89uYXMKHO98kGOqUBgViu5S9QMhNNb4bBP3XMU%2BK85I2S%2BAPCDKCGtDJwuDS42ncjIuon%2BFf4XkMxcOw8qtF0LvHt5J4Gsfgz031gZZC%2F0VTYS7gspToTiw5WOjuuvr3azt0yjb5mfmreuyVyoSyqT7GM99sA6T57Jq6Ef0Vy%2Fp9kdrmaNWIVRcVaQ6wxPy31Pu3dbz6g2KljyjnCtlYnkBmdsL3cpuC%2FG7N%2FRXtfBhsE&X-Amz-Signature=9db1e533c7b06a30ef0ba8ce2405f2326c711a10dc45d3cee2848e76e8df8bd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
agg_data = df.agg(
	        {
	            'A': 'sum', 
	            'B': 'median',
	            'K' : 'mean',
	        }
	   )

agg_data
```
<details>
<summary>Solution</summary>

```python
A    100.0
B     21.0
C     22.0
dtype: float64
```
</details>
---
[**`.agg()`**](/1867045b058343e1a66b677961515907#1c8f902fb8774ff7ab8c9bd1d9f76684)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c0482cd9-974a-43e1-ba7b-8c751b6789e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZ2SXIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCe4SNFSNulWe7QS1phkMFYbngZKPildE3L8EA1vkNv5QIgXkiO%2FeWum17VM8IbjEJIHct7CFJ1SToIX7PnU3eyC0Mq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ2CSgoXGIYyhpfO9SrcAzz%2Bb27KBmlbC4AORmzvFUD8iSzskQNs1LKQCzhpPTKx6o34Gb8XVZzCEwgi0QfzKN0UOJSUGuXGykWVB95tc47R4oZhZT43n7Q6ovxUKZ949hjfh0clfiAx8njL78n%2BpETcMqZslOZkgkFVwiVLBGJETg86GeLCihw5Q57rKDbgBZz7Iu8BOcQ6NneNKFfX4Z56U8DH%2F5rc8iacHmbm4JZYjSiovgHjNF3gzo8OPjPr5LhW4aimBM%2FZ0u%2BJYM138oJagHLNA7PXD8LYeNvu9C7GIJvK2BHi5Og3PHuu0rInn1cYeItgul2B8XBjSIfG14lB6t1tU7MpEa%2FODMwkVPZzcuG8mTDK1htNS0%2BYAh1ttJSd6k1ewS78YLgIKDDSle4rQr39QWyZwg4KR3IlClgvs1b99tUzYf%2FBNLiiGU2aUv1%2FcI8TiHsZbMd23tcxFPl5BljH6lkypcqTtbJPNJ5TttqhCrzEy1o55BXqCCaPtwbfJbFMy8IyaikO4%2B%2B9u3cOQuoLEtaCnMXXkrtoEwWkXs1GF5tbp%2BaOiSj3099lRSSqMnYKM6U%2BfTdWX0ulg4uJPDucmSO5SEnH71AtrH%2BGt9C7EF2RvHdrEBcLkOw%2BBjNISStUkaN89uYXMKHO98kGOqUBgViu5S9QMhNNb4bBP3XMU%2BK85I2S%2BAPCDKCGtDJwuDS42ncjIuon%2BFf4XkMxcOw8qtF0LvHt5J4Gsfgz031gZZC%2F0VTYS7gspToTiw5WOjuuvr3azt0yjb5mfmreuyVyoSyqT7GM99sA6T57Jq6Ef0Vy%2Fp9kdrmaNWIVRcVaQ6wxPy31Pu3dbz6g2KljyjnCtlYnkBmdsL3cpuC%2FG7N%2FRXtfBhsE&X-Amz-Signature=aba319d3b5077aeac0b59d57238a0f2209c70dd7295e7b21805ef787599a5b88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
agg_data = players_df.agg(
	        {
	            'Games played' : 'mean', 
	            'Games started' : 'sum',
	            'Minutes played' : 'median',
	        }
	   )

agg_data
```
<details>
<summary>Solution</summary>

```python
Games played        34.1
Games started      323.0
Minutes played    2782.5

dtype: float64
```
</details>
---
[**`.where()`**](/1867045b058343e1a66b677961515907#e162c2c05c46477798bdef0578b2a1c6)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a09b158c-b1c1-45e2-a752-8890edc85f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZ2SXIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCe4SNFSNulWe7QS1phkMFYbngZKPildE3L8EA1vkNv5QIgXkiO%2FeWum17VM8IbjEJIHct7CFJ1SToIX7PnU3eyC0Mq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ2CSgoXGIYyhpfO9SrcAzz%2Bb27KBmlbC4AORmzvFUD8iSzskQNs1LKQCzhpPTKx6o34Gb8XVZzCEwgi0QfzKN0UOJSUGuXGykWVB95tc47R4oZhZT43n7Q6ovxUKZ949hjfh0clfiAx8njL78n%2BpETcMqZslOZkgkFVwiVLBGJETg86GeLCihw5Q57rKDbgBZz7Iu8BOcQ6NneNKFfX4Z56U8DH%2F5rc8iacHmbm4JZYjSiovgHjNF3gzo8OPjPr5LhW4aimBM%2FZ0u%2BJYM138oJagHLNA7PXD8LYeNvu9C7GIJvK2BHi5Og3PHuu0rInn1cYeItgul2B8XBjSIfG14lB6t1tU7MpEa%2FODMwkVPZzcuG8mTDK1htNS0%2BYAh1ttJSd6k1ewS78YLgIKDDSle4rQr39QWyZwg4KR3IlClgvs1b99tUzYf%2FBNLiiGU2aUv1%2FcI8TiHsZbMd23tcxFPl5BljH6lkypcqTtbJPNJ5TttqhCrzEy1o55BXqCCaPtwbfJbFMy8IyaikO4%2B%2B9u3cOQuoLEtaCnMXXkrtoEwWkXs1GF5tbp%2BaOiSj3099lRSSqMnYKM6U%2BfTdWX0ulg4uJPDucmSO5SEnH71AtrH%2BGt9C7EF2RvHdrEBcLkOw%2BBjNISStUkaN89uYXMKHO98kGOqUBgViu5S9QMhNNb4bBP3XMU%2BK85I2S%2BAPCDKCGtDJwuDS42ncjIuon%2BFf4XkMxcOw8qtF0LvHt5J4Gsfgz031gZZC%2F0VTYS7gspToTiw5WOjuuvr3azt0yjb5mfmreuyVyoSyqT7GM99sA6T57Jq6Ef0Vy%2Fp9kdrmaNWIVRcVaQ6wxPy31Pu3dbz6g2KljyjnCtlYnkBmdsL3cpuC%2FG7N%2FRXtfBhsE&X-Amz-Signature=e5a9e21ead287c3afd8a7e5a3ebde49b26970e9cd25c85098e3aa556a89ddec6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
np.where(df % 2, 0, 1)
```
<details>
<summary>Solution</summary>

```python
array([[1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]])
```
</details>
---
[**`.where()`**](/1867045b058343e1a66b677961515907#e162c2c05c46477798bdef0578b2a1c6)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/52e3e193-b95c-41d4-9068-e65439fb4bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKZ2SXIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCe4SNFSNulWe7QS1phkMFYbngZKPildE3L8EA1vkNv5QIgXkiO%2FeWum17VM8IbjEJIHct7CFJ1SToIX7PnU3eyC0Mq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ2CSgoXGIYyhpfO9SrcAzz%2Bb27KBmlbC4AORmzvFUD8iSzskQNs1LKQCzhpPTKx6o34Gb8XVZzCEwgi0QfzKN0UOJSUGuXGykWVB95tc47R4oZhZT43n7Q6ovxUKZ949hjfh0clfiAx8njL78n%2BpETcMqZslOZkgkFVwiVLBGJETg86GeLCihw5Q57rKDbgBZz7Iu8BOcQ6NneNKFfX4Z56U8DH%2F5rc8iacHmbm4JZYjSiovgHjNF3gzo8OPjPr5LhW4aimBM%2FZ0u%2BJYM138oJagHLNA7PXD8LYeNvu9C7GIJvK2BHi5Og3PHuu0rInn1cYeItgul2B8XBjSIfG14lB6t1tU7MpEa%2FODMwkVPZzcuG8mTDK1htNS0%2BYAh1ttJSd6k1ewS78YLgIKDDSle4rQr39QWyZwg4KR3IlClgvs1b99tUzYf%2FBNLiiGU2aUv1%2FcI8TiHsZbMd23tcxFPl5BljH6lkypcqTtbJPNJ5TttqhCrzEy1o55BXqCCaPtwbfJbFMy8IyaikO4%2B%2B9u3cOQuoLEtaCnMXXkrtoEwWkXs1GF5tbp%2BaOiSj3099lRSSqMnYKM6U%2BfTdWX0ulg4uJPDucmSO5SEnH71AtrH%2BGt9C7EF2RvHdrEBcLkOw%2BBjNISStUkaN89uYXMKHO98kGOqUBgViu5S9QMhNNb4bBP3XMU%2BK85I2S%2BAPCDKCGtDJwuDS42ncjIuon%2BFf4XkMxcOw8qtF0LvHt5J4Gsfgz031gZZC%2F0VTYS7gspToTiw5WOjuuvr3azt0yjb5mfmreuyVyoSyqT7GM99sA6T57Jq6Ef0Vy%2Fp9kdrmaNWIVRcVaQ6wxPy31Pu3dbz6g2KljyjnCtlYnkBmdsL3cpuC%2FG7N%2FRXtfBhsE&X-Amz-Signature=31eb78f1a828dc5c50664bf6e4ed33a2878543eead9ec2b2768aad1e81d9f78b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
np.where(df // 3, 10, 20)
```
<details>
<summary>Solution</summary>

```python
array([[10, 10, 10, 10, 10],
       [10, 10, 10, 10, 10],
       [10, 10, 10, 10, 10],
       [20, 20, 20, 10, 10],
       [10, 10, 10, 10, 10]])
```
</details>
---
[**`.merge()`**](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)
`df_1`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5d7fd861-b3a8-4b56-9abc-1a5bf807d1d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VSBQKBL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFNLG3PwDnzmS%2B4GLj8N5jOg7v7NOi81uP4PvKEZ%2FxtSAiEAucl6%2BjRkSa2lnrEgvMXodbKT4pTdNXyGxsgF87srwHEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFZEau%2FPL93xp72%2FhSrcA%2BVkpbvsyGwUd8f82b50D7bHjhGAnOAKFs2XtWMykNFpX8iUaB5dCOw41o55h%2FBWljYqO1tWSOaGE3yCoyQCguywJ8xaerotwjJ7im4LE0QW5wftYaBbPqe7VMnrYHZBg6%2BEvMo%2Bi4X%2Fo9XiGZgacQA%2F2ioArbvWwP%2Fn9cCL%2BgDBIxFn%2BlA7pdiPQSin5%2Bs2gytk2K0PN2mrraoi%2F1fia9NyU3zgdqu%2BKTw%2BoZbqjaDKt1wJllTNyHAlYSgALAn5ER7hd6sG01ixBJHNfqFG0AIB0l1E%2F%2B63fCr%2BBMmIzfg7qH%2F%2BQbWH%2BQYzVdq3tTZXSkM0tlDhBjJhwr%2BTlrej6NUdWGhFKGblo%2B7%2FSCry31%2BGSElLPRaUPevSQLdsmXSI5aKxNwmNoG%2FCCmmGt1UQ0fWsSwsp4sF%2BGogQ0IBtPz3Cm9iwqC15XHUNHDxHUaQ4R9MKOBGAedPrcNvk6ClXlYDWSFGWN7ZB4f9uMfKDIeCLW%2F5W5KsmZ%2BXLoA2RkZ0bpfXYG1mGXB70zeZbNuW9ftZXajO1b6wD0EgkQZgv5Ir2z%2BifQydWBtSHuvEr1NSR0Z3aJXFy8lRS%2BWp89KJLZagvgRjuhev9PU92i2arSiEmyBTVcelUpKVlqv9YMOfN98kGOqUBtjwY6Vg99W7fHOdVnZVimxQf23maHGjia4u09CeN%2FxOWECneLKBrWf1YsU1RwL6mJS1ZIyCp5zlCKXpiQKyHo5ZpAiJZiV9SLqRXU1T%2BGNzcyAFxtsUZYbYrI8U1jBqrxNpAy1ojMhbBt9cnSPLdYKt7G6eK5Z7z0fDG687KZQfy1SpChZ14RiG8Q7cajVlEORsCcodU3GmLRtambwW0XosZE0rN&X-Amz-Signature=8ef6da8d3157c84129ab3514f4f49756fd730a95fd1d81455ed99af82f84e6c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`df_2`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d2043413-8efb-4768-9882-12b859ece727/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBLW3C4E%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBxDxVKQr38BtFfbp4TtGkha9vQEgPAtutOrNiDoeu4HAiB7ydC5kSUp3bkU6e9k7H81NOXaz8ZBoM5vNpNzD0GZ4ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMibSqxClg3oJr4VspKtwDMS5vXrhGYyjrZd8LZLTmioplLNQIt%2FMK9G0J0JTc5E9DGIl8G50sTitbTPW3ISjAj%2BGtyaZP7zJaGsAa3Wr8RgCfeIsMSeu%2FxuGSvBHkNPH%2FxeLfBriy2nJXpZlHjsn1vkZN4H35XpVFWuw6yzF3oFFowM2PbA%2B9OeqbsGTHcvuU4%2Fadk%2FicSOsNCi9LwEzbynWqe%2FPrILdwADTeIcwv4mVOiogPWPqxxLtdJbKVqtGlwPuK8xCO6ysI%2F7U4IjMrcbMbfiLCVz%2BOLqAu42qsNmYa8iQ3BhYjdNkeqC6nv7r%2FWVeKQLuO%2Bb6ugt4M7TZJGGsAerFhoRvEJWkzNqf2XCS11udtxZuOI57yJneYZEJG6CgnnOWOJAdmxu9CUiPmVAcwEZQgKfgJQuSjkYtTNXUoXasSw1govnRyVDqiaknWOvmLhgV0RUel1WTKTO58TUc9Gxa4W8spNH%2FVEOROhLEVhZTaWMaZ9WwUeO2tIUtay7Hx7YiW78viIMOwgwl62UML2FQrDRabpg4FjmZ51THw8iMFwo16v2%2BmbE5q0KjULHObiQmRAa1a%2BsiVc%2BhVih4Dhusps2eFiOqItehTVKRiEqYkcfGd%2BeKFEQiFHReMs2xNkdDj%2FUaD544wtc73yQY6pgEmn8Y8bKilnhwMUu8MsksrspemeBo6SvDBIoHKBMjFRf3kZbLIpwhoFQDEoJPOB84kOG2HtMiiVBvzXQ1P9R0XJqMozx8sRrbR52gZW6QgKB%2Fko0nV6c9NQUJKSAq6xbxWKzzM23GHoGliDugMC%2FDKRVyeKEBA6TAa27hLInhK5OBX1JtA2R6cIlj0%2FiBvv77KGSjUhMyTzRvzF4ySZ0MYxMkpw0Im&X-Amz-Signature=aea7fbeae1136baf4fb81163b9a9f4fd03827a9bcbaaa7ba6d369d5bec9326db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
pd.merge(df_1, df_2, how='inner', left_index=True, right_index=True)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d262f978-a18e-4296-a813-c33347c27d56/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5HUOMUF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCqVuANrJlMVl%2FtdPGRI0lUPlFvhrjp6ZeKqMgS9C%2BsSAIhAJfQx2eGnyinOu003kuFMLiuKPvFapgyMCeivdmGNxXoKv8DCCcQABoMNjM3NDIzMTgzODA1IgwMvCrBfxuxW7%2FUutkq3AOykh6drb0vgSQ3lTXD1gZbdJfzbv2yg5Owb%2FaEMY9PrNoHtzQOTAX%2FYsI58jiEFJsxcpbUe7ZGIfA%2FeNqYT7KoW49a%2FpcrkLYoVOss83w%2BrDaIxyofwdZ3pd8EHbu6xxvgTW4QCNkWt0Dr72DtGA1ITXv%2FisFbW4M3E%2FTCRxY0kf5TlGtwG%2FM%2FEeQc1V0KH2el%2FmSGBTxLkzhnZfgO%2FvhV8lkBDGTOGVB2PKsFDCB%2FVR7M%2FnGOsi5UrzDO1mT2OmFnbHvFHentyayHJ2RpcIUIAFYRiCowQZsw7URojl1qvf75r8dCpmx41i3cYEDVppFwyjlrsiooge69tHSM5RWHwMSBfH%2BYosq22Po5ksVGgexr2agyZcvLohy%2FyhkqmK9hamiaL5wHabngVonxXL9ZNtNzydWfw0oqLCbF81eBb7cyvpY5SPyETjO974fXN5m%2BGX4fO8PtH5YS5u%2Bid8wQtTTQSwY2C2Ynslm642rK7h5N%2BBgy%2Fbti7G5XEbXOBhNyb9q3eD%2B4blwQqkkJf15BFwJlzMW6RvQg8OWKJfNKqBc9xboUrHbMoT%2Bb9%2Fy%2FKkx1Mzmiz9qgGjsCTA1JA7TJJZi5buCqC27rDSk9O7m%2Bp16c5sAgaK3ZAs2KpzDgzvfJBjqkAQwHQPzdJqEPdsaB8UtouMqYcu99zcRPCevvZsiMxz7KejfphNLT0MVkQV2iuVFpp0QkCVpytncHlgk%2B%2FpdbFa0fMiT8HmwNOBhUweQ8Z6Lo9pp3n3SImeNPaaV4HCsNT%2F4H7q7I27uEog5fE5rAk4RCnvALwl%2BJjrJ56XeuTs0%2F9sbvvxzsGj3PlBYw42wpaaJ%2FwyedBV9loZiMxjUyhO%2B2ku1t&X-Amz-Signature=0a4e4de3b0e03f23e7eef193cd6a1171ab3914d684f0625a1a6b3096fa1d92db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
pd.merge(df_1, df_2, how='left', left_index=True, right_index=True)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6cc540cc-de55-4b1d-877f-c5c27aecff43/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ULBCNE4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDmSxN9lx6JL26JilDoanwBPFdb67XL9xlxaugJO1amqQIhAMU438nnxYLo7%2BWv3diYgm%2BaUsYsLtRKQrc6cA48PMqrKv8DCCcQABoMNjM3NDIzMTgzODA1IgwbiESqA3Q1wFV0Xmkq3APmChltjs7gmjN7fvAsZ3L30bB8jXSoRCbkwGKsJAdiQjQk9llw86T7PI6UPRInappHCkBj6O4FEEokUXmR4YXeic9jQiMOcxOsW2jqAnGprVOHSgI9NG5BzGCujlhmOgsznZHu1Xo6mBzA83jOwHooq07ISbfckydEGyPkVDzRbqR250ugoE2nn046wYRztVvLqG0jpAIz96n0vJA3LhSuD8TMYAVp94rWT9AKRKcO5%2FU1HfqxzoaHv7UJUP7LNdBxtBti8Sksx9%2B%2BxjpPLSSzIsEGIXQxmbyvYa6MXahPoN8JU4XaS1q8vkxgENNU5vmYcBkzaPDYpPfA3I23OQ%2FbHCnGA%2BfOChshE8bBCPFdajJGALU4Cfyg%2BEvGbF3SJnuUMdQJhDTCgq%2FQGA9EJZHom6QWHTNTHfwOcwMiYxzKEMdfq5xL8bHAL4EnqOdu3LWByC3vJMhHNnMIPcV675zq2PBUy83FyZsnADBBNUCe4XLbR0WmfQ7s7Uno2hBCmY9IM%2F2GrkCG2NmGzMcB6fQShS8H6riXgrZdHLyflsUlikSlHQBtw%2FXGf53WIkcfplO88Zv84yOTclXcVc52X8z7n1QefIcvefbRUIHASFOt16arJ%2BkCew%2FrhYrbPzCDzvfJBjqkAYFXlyeBdLNKUzCTewhJbAFnNhsIkHlyrUMfnFYG8RzwdHkv%2Fxwi8J555kZgPB8%2B5Q8DRZIgxXr78grMVZNYiH6pRzIyHTkkOOgCKeJKwnhktWCNcOC9a1yWoGi6XDEek1hKKhQEsusQQwv6StHK9DCwbN0zH3dGg6YqPZSaW%2BZp7pOD0yVUsY3GMtzCgjRznTcUXfzCisoWAX0COWNibecc8vPm&X-Amz-Signature=0be7881e809e1f645c3c484da347bb314f255598140c556bceed564e38602fb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
pd.merge(df_1, df_2, how='outer', left_index=True, right_index=True)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4ae29da2-7977-439d-ab2d-7205c92b2709/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLG7QSDV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCq0iLiptDH%2BqJnfckw74tZbQzmYqkHAZUZrmN%2FiCcl9wIhAOgkYOxJqcKK5e8ICQbq0QSiN34Vn3tMiDaKSNGlUX39Kv8DCCcQABoMNjM3NDIzMTgzODA1IgwabEm%2Bu0pMq6Qi2FIq3ANsBLcOuA9IS4TpI9H2zZ2vPm7Y7jfQb4dv9H3rgLVl39GVp7pwTH2GGn7ZmoEJUfroh5FKdqqLWtZoB24l4sSl6eQXf05OoWlR%2BELrz3OOQf4FO6wGrmWJ8bQPqS6zXV6Q5wYcb%2F9%2FI1ffsLII%2BuJzg%2FIcn%2FhQtKMNmXKS2yDLLgloPBdFP51VdpBERTRFZtNOEC5HEc2Iuv%2B0mphUq1rAQe3H13S2iEx0zil%2B%2BSZ168SdqVZLZGEUyqEcuqCZERAk2Ci%2FHvVB27ZOu5DhBkUSApqCFOPaXmOcA5YcnL99ct2QI3ESMhRiLs3mowLI%2F0dfJTHoBsRtnxJfh%2FClz3VaDudRYKwCXWHydzTbI6hNY9veLWvLjSkFNKlpsvEqwe1YYtS0n72fFrD7%2B%2BdNJfsY1Jyh060HTz5y71nNJtxCt9Akc5FH0uvrmx3wNA2%2BwLk68g6y%2Fc3PY396B%2FVuLsfE9CCTqYuZTSczyIYRrjWR1R%2BzR7XMQMVD12WGYdCN4JxrZMEN5ryq9UiIayj051bSOP0RFAOBLVqhT%2FVgVWghOIa3J%2FFJfkKlC4Fi3v8HWzY25fICQf4UpmLVuEuDIy%2BHj5eStrzn0bwK80KpZ7vrsr9XurRE6DKPGRb7%2BTCFzvfJBjqkARHRxn53rjX8RTfjkGnyJGyCq6jhERQolzzRyiaTbYIzJbk%2F9RueL0%2BOQi5gFEXXQ4JeDo9Bj8sDQVZuKAKGOYw0c9Bg0Y09%2BMDsxOho6ILn9X1gHZApc%2FJaGsYR98pXChHXLm0Jw%2BA47A%2F%2FWA0sZRE%2FQQRSrfSvuAvcb66i7tmXOqwFCzZOB8ihVPCQT2MXe88JJ9bMxIdJ8TdC%2BYJXO1iCyMPW&X-Amz-Signature=ff7fd143930d6c92c88f652433c51ee16dd8f6999ae4e66daceddba1d406d82a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
pd.merge(df_1, df_2, how='right', left_index=True, right_index=True)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e6aeec1c-4904-4224-b35e-a2a08d34d259/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGXT6UHQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDfiLsWU3jaPlY0e72ZgdEp2lXY%2FeGjrIKL%2BJXFF%2BgYCwIhAJnNLqy7a7IcAVB2mlNOLylWmflet2BU8TvLKlxrRwegKv8DCCcQABoMNjM3NDIzMTgzODA1IgwS2%2BUxXNWhMx80J1Iq3AMWpmAo9XqjmOOYIGhgr8iwx0VvzNJ10hRCkNUVAyFJ0GqJgh7tUusKSbgeM7IsqGN1VyN1Y6EC6bP7oYLFraXK08jTZiuHDrbsmMZt16v73qmF%2BL6HayjISbb39Qmy7aFbw4al3tTVs7qoD3TKoPYUNtIUhMPwl7cRzHBKADK3GYkLcHE9V9ANQ80rk1MDLEA%2BQY7MdTP%2BVNblPUV4VDDh4rKFO36HZJyw%2FmTaQQGmwv0Vb%2FSElsdoSES2mw1b6koSu4bXEDJiMZjA8XQ8ldloYzfTfvXk0qZceqlE7ppnvHEy0uCYRdmlOFaISfUN13xvXN19BUkwCy%2B6a9cI%2Bc9%2FMcqMqPAqyJIoONTR2fHd8QgVlrOupcStiRezwNwgraX%2Fif1LEJIYNru6OejE2d0ThCRx1fa0mpLGESTEOo2VPD6QPueDkoNQrhHX1mBkMqYdc5vdtySsRGqvfDoQXMTfXb9CuMPjKvf6eLFpHIfw81Z0ksxfdNTAos3rvsY3m4VeUSW4qwHsBNBEU8xDqpS91p63sm%2FoNaydss2dCjD%2F%2F1t2WJD%2B%2Buv4%2FXa%2FIhQ4bex697wQRw3lbVTM%2BkOMr6WbhV1evS3IUB8%2BpsVie98iuUXq2qdeZv8ykG1ovzCEzvfJBjqkAel4dPKhPXVK60bpUUxZK3hfZoM495Y%2FcFiHNkPLbChbJJcx9m%2FlqxKKhA07AktsuO08BeZ3GlUDByePCEawkdTD64hKkealxw1LYU1Ce5cdHPlCF2eoHZFjyutDOFu5BCryNQODkV5z98tKT85JlQUKE38QP0o5s2X%2FxUSpvMt9AMBsuf%2BNHAHJfWruvjt0dkAnOjhSb6Lwb4r%2F0edb6ld0%2BqP5&X-Amz-Signature=34106c494330d5e837d1d250cb3da81d2a256a3352737a71b14084151423afbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---

---
