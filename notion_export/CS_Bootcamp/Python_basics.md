---
title: "Python basics"
notion_id: "5b0832db-f945-4eb1-941b-7632e68a9abb"
notion_url: "https://www.notion.so/Python-basics-5b0832dbf9454eb1941b7632e68a9abb"
exported_at: "2025-12-13T22:32:29.154585+00:00"
---

# Python basics

# Datatypes
---
## **Overview**
---
Datatypes allow us to represent different information. When writing a text such as an essay we store information using letters and numbers. Python provides us various datatypes that allow us to store information from the real world in a computer program. Below you find an overview of the most important datatypes that you should be familiar with:
| Datatype | Description | Example | [Conversion method](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb) |
| --- | --- | --- | --- |
| [**String**](/5b0832dbf9454eb1941b7632e68a9abb#e38f24dd40804149b005946e21d51444) | A sequence of letters | `"Janick"` | `str()` |
| [**Integer**](/5b0832dbf9454eb1941b7632e68a9abb#c1d975398d44483ea2868588b5f50a63) | Whole numbers | `12` | `int()` |
| [**Float**](/5b0832dbf9454eb1941b7632e68a9abb#2e73116cedce42a3897b56f378b550f1) | Decimal numbers | `12.34` | `float()` |
| [**Boolean**](/5b0832dbf9454eb1941b7632e68a9abb#26cc7021a7944be18174da50709dbdd8) | Binary values, True or False | `True` | `bool()` |
| [**List**](/5b0832dbf9454eb1941b7632e68a9abb#5d06cfcdb5574513a592b854a821fe3e) | A collection of elements that can be of different datatypes. | `[’Janick’, 12, 12.34]` | `list()` |
| [**Tuple**](/5b0832dbf9454eb1941b7632e68a9abb#f8cb18a835dd45c1aed5abca3279ba9c) | A collection of elements that is immutable. | `('Janick', 'Janick')` | `tuple()` |
| [**Set**](/5b0832dbf9454eb1941b7632e68a9abb#f036e38587ac4bac9bda6d09abc39a30) | A collection of elements that does not contain any duplicates. | `{'Janick'}` | `set()` |
| [**Range**](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385) | A sequence of numbers from a specific start to end point with an optional step. | `range(0, 10)` | `range()` |
| [**Dictionary**](/5b0832dbf9454eb1941b7632e68a9abb#a7ac954b45b441c6ba2cc4fbc81d26ad) | An unordered collection in which keys are mapped to values. | `{
    'name' : 'Janick Spirig',
    'degree' : 'M.A.'
}` | `dict()` |
| [**JSON**](/5b0832dbf9454eb1941b7632e68a9abb#f5be024255f24935ae141727b88d80a5) | A data structure to represent objects as a formatted string. | `'{
   'name' : 'Marco',
   'birthday' : '11.02.1998',
   'degree' : 'B.A.',
   'place' : 'Zurich'
}'` | `json.loads()
 json.dumps()` |
---
## String
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5ae4faae-0975-4d6c-b80c-4bfa4b227414/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666INECNHA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICOpzFNHDSjz8rZ%2FSJtV5hrlzKwGjlgt8X9w7OitvHqZAiEA2re2PQFYYhgZBlFcfffEld12f6YneCx%2BExfD6KcFbLwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGECo%2Fs2FQcxOWp3ayrcA5%2Fn9GFwySlt0HAu8abkbrBheaf23dP3FZ2qebJ2IH03ssbqOH7zhx5xrUeibUZxnuXbZm5rYwxzKiPcV3IGTiQqLFzO28o9Yx4d9xXGdMzTaYvVCKJT152Py6PLY83Jc8ue7ZD1Ly6m5gB6GF3qFBbkhqm04J8VRWwraro%2BNDwX56DvpsX7S6JwEPk3aOE1wbvb0O1NY1ld1JKxTDeaKD0WgWymF9eu6SjL1KcQu9IdvAC0wXMuuNny5u7wzLiAQYED80Bd2T7hot2UpYJvX%2BFCH0T8xIhJNxAyzJZ9vEyIkXA2ErPrKf6RbpDYvGOUzRP0csELRkUyYqgyR3oqL5WoavBOtNhztq9Wm0PZzqFGG7fl3ad1reXvzUP03xloBrAhdMGc1vjav9VmkJWSVPkQRkfLHMkWRirbm83vIRmJqlbho9DqMMXpxsVxm2t%2FHpEOPA0QwkpPTD6xcGAglBhnswpEl5YAEbqMcEVeYT1RmgScXF2P5R5YVfB9j%2FPQj6C91FsIgYfC6FCQx9aFDJmoGx2WZA8u5GAHcdtaI1tjiRw2tsvE7OTL3srJRYClaqDhwuWTEA2km6F5kSxwsSmrXlbNYIJOi6KCx6c0CGuGZlth3eaJEZtjLE8MMN%2FO98kGOqUBCZ0qkaJzZPI2WMo9aZowVZ1kSvaq6OAscH1VS8uonXoOHCwKoc0yXTD33vp%2Bn5UHam%2BEx0Q9fK8OVPsO2IP1ic7Ja%2BoFi2WfKAlsLZPSOIq2nj7%2BezMdtAbZPktC1kIN0TS%2FWlnfl238%2FigYHYomxcfVpSaqsxr64gdzNlen5KKBcaMLJIwzzuEnnfP96058G8H%2B43bgEDTitLlIBYqASHX7RkLK&X-Amz-Signature=e1c0a2970ad56ce51124fb6f1189c4a235349e0cf895a6c9fea9c4603246abf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Definition**
A string is a sequence of letters. We can recognise a string by its quotation marks at the beginning and at the end of the text. Thereby it does not matter whether we use double  or single quotation marks. This means that
`my_name = "janick"`
is the same as 
`my_name = 'janick'`
### Methods
---
[**`.split()`**](https://www.programiz.com/python-programming/methods/string/split)
This method allows us to split a string by a specific character. The method gives back a list with all elements that the string has been divided into.
```python
my_fruit = "Rhabarber"

splitted_string = my_fruit.split("b")

type(splitted_string)
<class 'list'>

splitted_string
['Rha', 'ar', 'er']
```
---
[**`.strip()`**](https://www.programiz.com/python-programming/methods/string/strip)
This method allows us to remove unnecessary whitespaces to the left and right of a string. If we don’t provide any input to the function, then spaces are removed by default.
```python
my_fruit = "    Rhabarber   "

my_fruit.strip()
'Rhabarber'
```
If we provide a specific character, Python looks out for this character and removes it accordingly.
```python
my_fruit = ".Rhabarber.."

my_fruit.strip('.')
'Rhabarber'
```
---
[**`.upper()`**](https://www.programiz.com/python-programming/methods/string/upper)
This method allows us to capitalise all characters in a text.
```python
my_fruit = "RhAbArber"
my_fruit.upper()
'RHABARBER'
```
---
[**`.lower()`**](https://www.programiz.com/python-programming/methods/string/lower)
This method allows us to put all characters in a text into small letters. 
```python
my_fruit = "RhAbArber"
my_fruit.lower()
'rhabarber'
```
---
[**`.isupper()`**](https://www.programiz.com/python-programming/methods/string/isupper)
This method allows us to check if all characters in a text are capitalised or not. It returns True or False.
```python
my_fruit = "RhAbArber"
my_fruit.isupper()
False

my_fruit = "RHABARBER"
my_fruit.isupper()
True
```
---
[**`.islower()`**](https://www.w3schools.com/python/ref_string_islower.asp)
This method allows us to check if all characters in a text are in small letters or not. It returns True or False.
```python
my_fruit = "RhAbArber"
my_fruit.islower()
False

my_fruit = "rhabarber"
my_fruit.islower()
True
```
---
[**`.replace()`**](https://www.w3schools.com/python/ref_string_replace.asp)
This method allows us to replace characters in a string with some other characters.
```python
my_fruit = "Rhabarber"

my_fruit.replace("a", "i")
'Rhibirber'
```
---
[**`.join()`**](https://www.programiz.com/python-programming/methods/string/join)** & **[**`sorted()`**](https://www.programiz.com/python-programming/methods/built-in/sorted)
Using these two methods in combination allows us to sort the characters in a string. By default the characters are sorted in ascending order. In order to sort a string in descending order, the parameter `reverse` must be set to `True`.
```python
first_name = "janick"
last_name = "spirig"

"".join(sorted(first_name))
'acijkn'


"".join(sorted(last_name, reverse=True))
'srpiig'
```
---
[**`.format()`**](https://www.w3schools.com/python/ref_string_format.asp)
This method allows us to insert values that are saved in variables into a string. To do so, inside the string we must define where the value should be inserted using `{}`. 
```python
name = 'Janick'

print('Hello {}'.format(name))
Hello Janick
```
If there are multiple values to be inserted, multiple inputs can be provided to the `.format()`. The first value is then inserted at the first `{}` and the second value at the second `{}` etc.
```python
firstname = 'Janick'
lastname = 'Spirig'

print('Hello {}, {}'.format(firstname, lastname))
Hello Janick, Spirig
```
Alternatively we can also define a [format-string](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/) by writing `f` in front of the string. Then we can write the variables into the curly brackets `{}` directly.
```python
firstname = 'Janick'
lastname = 'Spirig'

print(f'Hello {firstname}, {lastname}')
Hello Janick, Spirig
```
There are many additional [formatting options](https://cheatography.com/brianallan/cheat-sheets/python-f-strings-number-formatting/) that can be used in combination with `f`
---

---
## Integer
---
**Definition**
Integers are regular / whole numbers such as `1` `2` `3` `4` `5` etc.
We can do any kind of [math calculation](/5b0832dbf9454eb1941b7632e68a9abb#c5ed1b94ab75447ba1228022dbea677f) with Integers.
---
## Float
---
**Definition**
Floats are decimal numbers such as `1.34` `5.3834` etc.
We can do any kind of [math calculation](/5b0832dbf9454eb1941b7632e68a9abb#c5ed1b94ab75447ba1228022dbea677f) with floats.
---
## Boolean
---
**Definition**
A boolean variable can only have two two possible values: `True` or `False`. Therefore, a boolean is also called a <u>*binary*</u> variable. Booleans are very useful as they allow to formulate expressions to check conditions.
> 💡 **`True` can also be written as `1` and `False` as `0`.**
### Comparing values
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c167acc1-0f7a-4728-b4de-1ec22372a1de/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GZZOO4P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFXc9PDc7rGki%2FarKh40CNLVwKMpCXND2cLu6YW80d5tAiEA%2FqiI2zNlzIuShb%2BIET4ydqjDFGXOJZjbs%2Ffb1GYUmtsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDPZRf3f6EZQP3nIwlSrcA6aZP1TPwc6lw4D2F1aTOcfGbFWye2xijFVBdcudivrjtxEFJPRCaR5CJIW0aJogFCrMa5XW0JVSjZtn6bYiRn7P2F7hFTshWiGEzZp4DYNXs4ZZuffQeyOsSGBtXQd%2FZP8hgenwa%2F%2FIQpCRSOVscSfUZivIy1LDei4RrQu9IzLmYzijyhLT2glbwBEAs%2BuD84BzdhgHCk3NHSuySxEIu6zcB6dtyoAa1iV47EWYb4UURoXuxDtP2aqbg%2FoeiNpf1Kt5tpw3xYN21kPZdSLb%2Fvo8P9x6ul2FW493K5gq%2BTKTw%2Ba4GPO7%2Fdo6mZAdqBNPKTWSJ00L5fbUhMF%2BbEel4np0vnGSLp6cFhK6cf5tN%2F6UdQHBke61fZ6J9Q8FeZ9vy%2FeSaqRYAIpd2MpyCOY5BL5x9k%2FFniStd7U6d3Y8Ky5MlFNMeWCLqJl96m%2BwNdhAQmjFoADFmC9%2Ba4ldAv5BUBFwUCLP7cjowTL5McdPHb9TJ1LHKbjISgqA8ic54LbcBuXWMUO6wwNjr3il6aUHYokU3efP5CWCvH1QDSYnj2DxY1qEILWIP78f%2BOM6Xv6goALN3ffmf4GKhIM5mAq0T8oJh4105g3L60GD8BGMIkYJERX68Wexqn35G4Z2MOTN98kGOqUBkLEIh8axZff5t2iwlHJjUmX4FQZxtHJbnjA0CGaL8ErDHNrPY5nd%2Fkpy%2FVdm%2FzfkPmUH4QO6hoxGN2r1HhJQQT3CCthQWL2xlhooJRpI%2FWMpf1rZP4e2%2Fq6T65o%2FnhE8Y%2FXbwzq1zTmE1an23sitvaLc9jejJzmznbrA3JBC1R62waok9OBAx3QzNlPlYe3CmiMsltmqjYyH11T%2FVLGANLLgnQfj&X-Amz-Signature=bf1ca17cc6ca09aebbfba594b9f84b637c32dd6ad3ff8eebec7beba7bc8250f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**equal → ****`==`****  **
If we want to check if two values / variables are equal we can use `==`. It is important to note, that this operator not only checks if the two values are content-wise the same but also if they are of the same datatype. 
```python
a = 5
b = 5
c = '5'

a == b
True # 5 and 5 are equal

a == c
False # 5 and '5' are not equal
```
If you can see from the code-snippet above, we have three variables initialised. If we check if `a` and `b` are equal, we receive `True`, meaning that they are equal. However, if we check if `a` and `c` are equal, we receive `False`, meaning that they are unequal.
Of course all the variables have stored the number 5. However, in variable `a` and `c` we have stored the number as an *integer* and in variable `c` as a *string*. This is why the second comparison yields `False`, because variable `a` is an *integer* and variable `c` a *string*, meaning that the two variables store the same content but are of different datatypes.
---
**unequal → ****`!=`**** **
This comparison is just the opposite of the previous one, `==`. Thus, `!=` checks if two values / variables are unequal. If they are unequal we get `True` and if they are equal we get `False`.
```python
a = 5
b = 5
c = '5'

a != b
False # 5 and 5 are not unequal

a != c
True # 5 and '5' are unequal
```
You can see now that if we replace `==` for `!=` we get the exact opposite results.
First, it checks if `a` and `b` are unequal. As they are equal (in both variables we have stored the integer 5) we get `False`, meaning that `a` and `b` are not unequal. 
Second, it checks if `a` and `c` are unequal. As they are unequal (in variable `a` we have stored the integer 5 and in variable `c` the string 5) we get `True`, meaning that `a` and `c` are unequal.
---
**smaller than → ****`<`****    greater than → ****`>`**** **
These operators we likely know already from math in elementary school. They just check if the value on the left is smaller (`<`), or greater respectively (`>`) than the value on the right. 
```python
a = 6
b = 4

a > b
True # 6 is greater than 4

a < b
False # 6 is not smaller than 4

a = 6
b = 6

a > b
False # 6 is not greater than 6

a < b
False # 6 is not smaller than 6
```
From the code-snippet above we see that the first comparison checks if `a` is greater than `b`. Because 6 is greater than 4 we get `True`.
In the second comparison we check if `a` is smaller than `b`. Because 6 is not smaller than 4 we get `False`.
If we set the value of variable `b` to 6 as well, we get two times False, because none of the two values is greater or smaller because they are equal.
---
**smaller equal →****`<=`****     greater equal → ****`>=`**
These comparisons are very similar to the previous two. With the only difference that they evaluate to `True` if the two values are equal.
```python
a = 6
b = 4

a >= b
True # 6 is greater than 4

a <= b
False # 6 not smaller or equal than 4

a = 6
b = 6

a >= b
True # 6 is equal to 6

a <= b
True # 6 is equal to 6
```
From the code-snippet above we see that the first two statements still evaluate to `True`. However, if we check the last two statements we see that they evaluate to `True` as well.
In the third statement it is checked if `a` is greater than or equal to `b`. Because in both variables we have stored the integer 6, this statement evaluates to `True` as the two values are equal.
In the fourth statement it is checked if `a` is smaller than or equal to `b`. Because integer 6 and integer 6 is equal, this statement evaluates to `True` as well.
---
**Comparisons with **[**numpy**](/ccc5737dc7c64936bced118aca375cf9)** arrays**
All of the comparison operators discussed so far, we can also apply on numpy arrays. Here it is important to note, that the comparison is done element-wise and a numpy array is returned that contains the result (either True or False) of each element-wise comparison.
```python
import numpy as np

a = np.array([2, 5, 4, 6])
b = np.array([2, 3, 4, 7])

a == b
array([ True, False,  True, False])

a != b
array([ False, True,  False, True])
```
From the code-snippet above we see that we have created two numpy arrays that contain 4 integer values each.
If we now check if the two arrays are equal using `==`, we get:
- `True` (2 and 2 are equal)
- `False` (5 and 3 are not equal)
- `True` (4 and 4 are equal)
- `False` (6 and 7 are not equal).
If we check if the two arrays are unequal using `!=`, we get the opposite results:
- `False` (2 and 2 are not unequal)
- `True` (5 and 3 are unequal)
- `False` (4 and 4 are not unequal)
- `True` (6 and 7 are unequal).
---
### **Chaining boolean statements**
---
Now as we have understood how each comparison operator works, we can start thinking about how to chain them together. We can wrap multiple comparison statements into a bigger one using the boolean operators `and` + `or`.
<details>
<summary>Disclaimer</summary>

The examples discussed are rather simple ones. However, we can easily make more complex ones in which we combine more than two boolean comparisons with the keywords `and` `or` `not`. However, if you got the basics right then you’re all set to even crack the most complex boolean statements.
---
</details>
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1577edea-b626-4b7f-b95f-6b12179fd0cf/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O3T4A5G%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDWx0LjBpv6LAJf3IbXIwgk3tYB3ubZIPr54FQ9LTvosAiEA2WSRwhQWfd5k7U5ZDCPI6ilNRLPEP46uuganufWK%2B2wq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFJIyK0h9oBVeDbg7CrcAzdQ70cbWzyojJVpUYQM7KDVg6SgmYh6QvG%2F9u05s1m0horjtMDB1JPTu2LMcRGuzRV2Swo6%2BuCxhtILKMPk3ptrAaJWfQCcr31nvda1OdoXrM0tYINPngsjSUoaSpjg0qrppQTL%2FTKYcyAwWP0LnzQl%2Bdu3XuzerAtc4XlD90yGiRhgr1ssO6cZyX9H4bmIg9LxiHZ5tbZ31%2FCbMi5bBrG4PWvfrjCiidsAWIVj8NsufGkjfqPHflWz8OiA1M2DqdZsbSDycRKLKzRrcvVIP9WsqXfam1MnvpZlbGmQ%2BFJMOw6oGJ6I4GHvhQmbFdYO9pFgGmn8d1Pb5esN5zNG9Xm5FdQyh2bxxxAzsCnpmKXHBILCd2h%2F%2FFqqZQHhdAYajo5alnY7%2F2e579Sp1owMNcCo0%2F2Eplhnt%2BXQRO5T9HZG0%2FPRIyAlJHYTwWa9PNJcqo0xOwPxtidiPtrdcmVILFbS50dw8Xa2%2FDJTw6fMlAY8nUIBZTkmo7sJ8ImTkDHNI1Bkf4Jpy5Ulug4Sbf%2Bhd2J30ijAsKXtloJKwwmFO4pCk8ADmpjC3%2F3TE9FcN3zKy%2B9g1dLG3RyF0Lq0kNNFIkicsabatdEnhgER2hPnMFy6h2pO%2Fv1mbF6s1nJsMIzO98kGOqUBdclr9K%2FZez%2FayIqqpOBLvJd2nxq5mfRi6bqTnIYKNo%2BWicOrGGr0vkU3FivjgDU2S09bc1x17Sf94tRmc%2BICK9yz9oBX837u6kgQ4DRp5IpqeT3%2BxXa%2BdD9q3hM%2BeS0lWMc8ALlnGAosXhwREuomFpM7biLH8VroJ1BF34Jb71hA8tiCcItewoi%2BdZzHGs1%2BSbeUfkgETOHo%2Fl3mYZ1hjq%2B6zhRU&X-Amz-Signature=de06adeb3e3b07a1d1faaa76ea0237d7170a3447a405c15cb75656c5412a8ab3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**`and`**** operator simple**
The `and` operator works as follow:
|  | Input 1 | Input 2 | Result |
| --- | --- | --- | --- |
| 1 | `True` | `False` | `False` |
| 2 | `False` | `True` | `False` |
| 3 | `False` | `False` | `False` |
| 4 | `True` | `True` | `True` |
As we can see from the table above a boolean statement that connects two inputs with an `and` only evaluates to `True` if both inputs are `True`, otherwise it evaluates to `False`. Thus, both inputs must necessarily be `True`. Let’s consider an example:
```python
a = 5
b = '5'

a == b and a != b
False
```
|  |
|  |
|  |
|  |
|  |
We can see from the code snippet above that the boolean statement evaluates to `False`. 
To understand why, let’s look at the first input (the boolean comparison to the left of the `and` keyword). We see that we check if `a` and `b` are equal. This is not the case as in `a` we have stored the integer 5 and in `b` the string 5. Thus, input 1 is `False`:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False | ? | ? |
|  |
|  |
Now let’s have a closer look at input 2 (the boolean comparison to the right of the `and` keyword). Here we check now whether `a` and `b` are unequal. This is the case as integer 5 is not the same as string 5. Thus, input 2 is `True`:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False | True | ? |
Now what is the result of the overall statement? We can check to which entry in the [reference table](/5b0832dbf9454eb1941b7632e68a9abb#736fb47f961941e9abf2a7f39e6812b4) our [intermediary table](/5b0832dbf9454eb1941b7632e68a9abb#d32c6ec4ea4a4938b1a1e0d6d88640c5) above belongs to. We see that Input 1 equal to `False` and Input 2 equal to `True`, corresponds to the second line in the reference table. The column Result in the reference table tells us that in this case the result of the overall statement is `False`
|  | Input 1 | Input 2 | Result |
| --- | --- | --- | --- |
| 2 | `True` | `False` | `False` |
If we think about the comparison that we have done again, it is quite logical that the result is False. Because we are checking if `a` and `b` are equal and unequal at the same time. And of course, if they are equal than they cannot be unequal.
---
**`and`**** operator **[**numpy**](/ccc5737dc7c64936bced118aca375cf9)** arrays**
|  |
|  |
|  |
|  |
We can also use the and keyword on numpy arrays with the `np.logical_and()` method. This method takes two arrays as input and goes through the two arrays element-wise and executes for each pair of values the and operation: `x1 and y1` `x2 and y2` `x3 and y3` etc.
```python
import numpy as np
x = np.array([1, 1, 0, 0])
y = np.array([0, 1, 1, 0])

np.logical_and(x, y)
array([False,  True, False, False])
```
We can see that we get a numpy array as result that contains four values:
1. `1 and 0` → `True and False` → **`False`**** **(case 1 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#1c87eaabfe004c4f9a5f7efaebdbc36e))
1. `1 and 1` → `True and True` → **`True`**** **(case 4 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#1c87eaabfe004c4f9a5f7efaebdbc36e))
1. `0 and 1` → `False and True` → **`False`**** **(case 2 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#1c87eaabfe004c4f9a5f7efaebdbc36e))
1. `0 and 0` → `False and False` →**`False`**** **(case 3 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#1c87eaabfe004c4f9a5f7efaebdbc36e)) 
---
**`or`**** operator simple**
The `or` operator works as follow:
|  | Input 1 | Input 2 | Result |
| --- | --- | --- | --- |
| 1 | `True` | `False` | `True` |
| 2 | `False` | `True` | `True` |
| 3 | `False` | `False` | `False` |
| 4 | `True` | `True` | `True` |
From the table above we see that when we connect boolean statements with the `or` keyword, at least one of the two inputs must be equal to `True` in order for the overall statement to evaluate to `True`. Thus, only one of the inputs must be True necessarily. Let’s consider the same example as before:
|  |
|  |
|  |
|  |
|  |
```python
a = 5
b = '5'

a == b or a != b
True
```
Again, the first comparison (to the left of the `or` keyword) evaluates to `False` and the second comparison (to the right of the `or` keyword) evaluates to `True`. Thus, we get:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| `False` | `True` | ? |
To determine the result of the overall statement we can again look into the [reference table](/5b0832dbf9454eb1941b7632e68a9abb#a18d68521412461d95fd8dffb4abfa46). When input 1 is `False` and input 2 is `True` this corresponds to case 2 and thus the result is `True`
|  | Input 1 | Input 2 | Result |
| --- | --- | --- | --- |
| 2 | `False` | `True` | `True` |
If we think about the comparison that we have done again, it is quite logical that the result is True. Because we are checking if `a` and `b` are equal or unequal. And of course, no matter what value we store in `a` and `b` they are always either equal or unequal as the two cases are mutually exclusive.
---
**`or`**** operator **[**numpy**](/ccc5737dc7c64936bced118aca375cf9)** arrays**
|  |
|  |
|  |
|  |
Also in case of the `or` keyword there is the `np.logical_or()` method that we can run on numpy arrays.
```python
import numpy as np
x = np.array([0, 1, 0, 1])
y = np.array([0, 1, 1, 0])

np.logical_or(x, y)
array([False,  True, True, True])
```
As numpy does the or operation pair-wise the resulting array contains four elements again:
1. `0 or 0` → `False or False` → **`False`**** **(case 3 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#5c281ded337046a8a696e7415e346b27))
1. `1 or 1` → `True or True` → **`True`**** **(case 4 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#5c281ded337046a8a696e7415e346b27))** **
1. `0 or 1` → `False or True` → **`True`**** **(case 2 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#5c281ded337046a8a696e7415e346b27))
1. `1 or 0` → `True or False` → **`True`**** **(case 1 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#5c281ded337046a8a696e7415e346b27))
---
**`not`**** keyword simple**
The `not` keyword reverts the result of any boolean expression.
If we place a `not` in front of `True`, then this becomes `False` and if we place it in front of `False`, then this becomes `True`. 
If we place the `not` keyword in front of the `and` keyword it becomes an `or` and if we we place it in front of the `or` keyword it becomes an `and`. 
> 💡 **In the case of `not and` we need to look into the `or` [reference table](/5b0832dbf9454eb1941b7632e68a9abb#5c281ded337046a8a696e7415e346b27).
In the case of `not or` we need to look into the `and` [reference table](/5b0832dbf9454eb1941b7632e68a9abb#1c87eaabfe004c4f9a5f7efaebdbc36e).**
Let’s look at the examples from before again.
```python
a = 5
b = '5'

a == b not and a != b
True
```
From the code snippet above we see that there is now `not` in front of the `and` keyword. As `not and` is equal to `or`, Python checks basically `a == b or a != b`, which yields `True` as `a` is unequal `b` (→ case 2 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#a18d68521412461d95fd8dffb4abfa46)).

```python
a = 5
b = '5'

a == b or not a != b
False
```
In this code snippet we see that the `not` is not placed before the `and` keyword anymore, but in front of the second boolean expression.
In this case, the `not` keyword essentially reverts the result of `a != b` 
`a != b` → `True` → `not True` → `False`
As `a` is unequal `b`, the first boolean expression `a == b` yields `False` as well.
Thus, in the end Python checks `False or False`, which yields `False` (→ case 3 in [reference table](/5b0832dbf9454eb1941b7632e68a9abb#a18d68521412461d95fd8dffb4abfa46)).
---
**`not`**** keyword **[**numpy**](/ccc5737dc7c64936bced118aca375cf9)** arrays**
In numpy we also have a `not` keyword which reverts the boolean values in an array element-wise. Specifically, we can use the `np.logical_not()` method to achieve this.
```python
import numpy as np

x = np.array([1, 1, 0, 1])

np.logical_not(x)
array([False, False, True, False])
```
As we can see, the code-snippet above reverts the values stored in `x`. This means that `1` (True) becomes `False` in the result and `0` (False) becomes `True`.
---
---
## List
---
**Definition**
Lists are very useful as they allow us to store multiple elements as a collection, i.e., in one single variable. So be it to store multiple names of students, ages of persons or a multitude of fruit names, lists allow us to achieve that.
We can recognise a list by its square brackets at the beginning `[` and at the end `]`:
`my_fruits = ["Rhabarber", "Apple", "Pear", "Orange"]` 
Lists are also powerful because they allow to store elements of different datatypes in the same list. Thus, we can store two strings, two integers, two floats and one boolean in the same list:
`my_list = ["Janick", "Spirig", 2, 4, 8.45, 9.32, False]`
This `my_list` and `my_fruits` are simple examples of one dimensional lists, but we can also have multi-dimensional lists, so-called nested lists. Let’s say we have two students and we want to store the name, age and GPA of each student:
`my_students = [["Janick Spirig", 25, 5.12], ["Melanie Huber", 22, 4.87]]`
From the brackets `[]` we can infer that the list `my_students` contains two sub-lists which represent the two students and contain three elements: name, age and GPA.
### Access & overwrite elements
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d72717d8-22ee-4014-9d9a-fb15985660ba/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647ZUQKON%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCFRtVDa8HMS5yswP0K1JKU9s9VUd%2FauanLDPSGr99OwAIgAWpICCErQND829OaRk4fyDHtXLiPLyEPLC7%2BtyvkVOAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDEz%2BEoyvG0JKU8NhtSrcAxVUbDkpv3VqHr8xMw%2FMPGuM%2FD3HXGSCaKC4X3nPOHAPxpefxbvxCe6hCbcEas0elAEegX81QYPV56ULtMHCIwCugv7TjzTKElLT36T13LRdSjPRVHqdHN7%2BTPlRjHmu%2B7crF9gPR5A8DnYW77Ao6t4O6XZERV690INGkJI6TZISBUcA4BWjUILTUojJsLCfMEpHXfDSDPQK5Tx2KHqtz9JDmMHCnSBiq2NE79%2FudZXKI2EUikvT0H6xPlqTwzYvXHqpP9adS%2FLEtFN7gEzsLLY8qv6peOGbIPspxsb0Fcxa3RvYgn5Irb3qX1vuxkVJhESFdhWQA%2F0rfZouJRl%2FRCvYg3ihw2UBT%2BdGXFn1SGxSecSfx44%2Bd0LglKA%2BlplAQS6taYVF671dfCEUiPe6Afw1o0SI7DIuuCPrNAjUc%2FbPaWVxQOWzQnVSG9pjy8%2BewBQdcENVMccg9LWeW4NgpZGqBRARwjIMSuJvdzCZq01J2EtvnAZxXwClXv%2Bm3gLMkXy5WXjl70icjtLBntTwXNupEs5wBhDdChwljVzImQ6GKv9PIQ6IUl7RvM8urLObQPOunH%2FsEWnIKL%2B9mfnKHGbL7%2Fwliz37hpjh8UU%2FGWIXSzGr3s0LnW5ad9JRMLXO98kGOqUBWGzaEzbdtUXYa7qa2aR8N10XvNgNVPBp%2BPfmdqbKO5jTfRqyn7tOmxlNFu0Kp1AeLK0Z90%2FLz%2BZDtr6WcUHQ8mDPt3zJiaKu0hHevjGzw2%2BMqbCckQTVNq%2BxQrOYzOsIQmSXoKwEGYyXxVjRSBlsq%2BRm0Co%2F9XZ6hqg5B%2B5nQMzvbrzndigmeDWUEnCsbdzQTloYXhjLD7bNMr%2BYyKefQLtSvunp&X-Amz-Signature=3175428f41c7890e36b2d5414ec81cd047784a23209742607154de9999d7319d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Index positions**
Before thinking about accessing and modifying values in a list, it is important to understand that each element is placed at a specific position, which we call index position. Thereby, each element has a position when looking at the list from the front, i.e., from left to right and one when looking at the list from the back, i.e., from right to left. If we consider the list [`my_list`](/5b0832dbf9454eb1941b7632e68a9abb#bd97468896274d51a88e66d08fc628bf) the index positions of the elements are as follow:
![Forward-looking and backward-looking positions of the elements in `my_list`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6ced3812-d7c4-4029-9292-23360bb1744f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647ZUQKON%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCFRtVDa8HMS5yswP0K1JKU9s9VUd%2FauanLDPSGr99OwAIgAWpICCErQND829OaRk4fyDHtXLiPLyEPLC7%2BtyvkVOAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDEz%2BEoyvG0JKU8NhtSrcAxVUbDkpv3VqHr8xMw%2FMPGuM%2FD3HXGSCaKC4X3nPOHAPxpefxbvxCe6hCbcEas0elAEegX81QYPV56ULtMHCIwCugv7TjzTKElLT36T13LRdSjPRVHqdHN7%2BTPlRjHmu%2B7crF9gPR5A8DnYW77Ao6t4O6XZERV690INGkJI6TZISBUcA4BWjUILTUojJsLCfMEpHXfDSDPQK5Tx2KHqtz9JDmMHCnSBiq2NE79%2FudZXKI2EUikvT0H6xPlqTwzYvXHqpP9adS%2FLEtFN7gEzsLLY8qv6peOGbIPspxsb0Fcxa3RvYgn5Irb3qX1vuxkVJhESFdhWQA%2F0rfZouJRl%2FRCvYg3ihw2UBT%2BdGXFn1SGxSecSfx44%2Bd0LglKA%2BlplAQS6taYVF671dfCEUiPe6Afw1o0SI7DIuuCPrNAjUc%2FbPaWVxQOWzQnVSG9pjy8%2BewBQdcENVMccg9LWeW4NgpZGqBRARwjIMSuJvdzCZq01J2EtvnAZxXwClXv%2Bm3gLMkXy5WXjl70icjtLBntTwXNupEs5wBhDdChwljVzImQ6GKv9PIQ6IUl7RvM8urLObQPOunH%2FsEWnIKL%2B9mfnKHGbL7%2Fwliz37hpjh8UU%2FGWIXSzGr3s0LnW5ad9JRMLXO98kGOqUBWGzaEzbdtUXYa7qa2aR8N10XvNgNVPBp%2BPfmdqbKO5jTfRqyn7tOmxlNFu0Kp1AeLK0Z90%2FLz%2BZDtr6WcUHQ8mDPt3zJiaKu0hHevjGzw2%2BMqbCckQTVNq%2BxQrOYzOsIQmSXoKwEGYyXxVjRSBlsq%2BRm0Co%2F9XZ6hqg5B%2B5nQMzvbrzndigmeDWUEnCsbdzQTloYXhjLD7bNMr%2BYyKefQLtSvunp&X-Amz-Signature=7dd42149191d36448bfadc843092f52b217910c21fc4cc8c65495af839a02b97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
> 💡 **The first element in a list always has index position 0. The last element in a list always has index position -1.**
---
**Access elements in normal list**
Let’s assume we want to access the value `9.32` in the list [`my_list`](/5b0832dbf9454eb1941b7632e68a9abb#bd97468896274d51a88e66d08fc628bf). We first must figure out the index position of `9.32`. The first element in a list always has index position 0. Thus, as `9.32` is the 6th element in the list its index position is 5.
```python
my_list[5]
9.32
```
In this example we counted from the beginning of the list. However, we can also count from the back of the list. As we know already, when we count from the back the last element has position -1, the second last one -2 the third last one -3 etc.
So if we want to access the value 9.32 from the back of the list we can do so by providing the value -2 in the brackets as it is the second last element in [`my_list`](/5b0832dbf9454eb1941b7632e68a9abb#bd97468896274d51a88e66d08fc628bf).
```python
my_list[-2]
9.32
```
---
**Overwrite elements in normal list**
Now if we want to overwrite the value `False` in [`my_list`](/5b0832dbf9454eb1941b7632e68a9abb) with `True` we must again figure out the value’s index position. `False` is the 7th element in the list and thus has index position 6. 
```python
my_list[6] = True

print(my_list)
["Janick", "Spirig", 2, 4, 8.45, 9.32, True]
```
As the value `False` is the last element in the list we can alternatively also access and overwrite it when counting from the back. 
```python
my_list[-1] = True

print(my_list)
["Janick", "Spirig", 2, 4, 8.45, 9.32, True]
```
---
**Access element in nested list**
Let’s assume we want to access the GPA of the student Melanie, i.e., the second student, in the list [`my_students`](/5b0832dbf9454eb1941b7632e68a9abb#e3c19f2a15a84127a05dd028ea60ebc9).
To do so we must figure out two things:
- Index position of the student Melanie in list `my_students`?
- Melanie is represented by the second list
- Second element has index position 1
- We can access this list by calling `my_students[1]`
```python
my_students[1]
["Melanie Huber", 22, 4.87]
```
- Index position of GPA within the list `my_students[1]`?
- GPA is the third element in the list
- Third element has index position 2
- We can access the GPA by calling `my_students[1][2]`
```python
my_students[1][2]
4.87
```
As we can see, when we want to access an element in a nested list we start from the most-outer list and then dive deeper into the sublist by chaining the square brackets selectors together.
---
**Overwrite element in nested list**
Similarly if want to overwrite an element in a nested list we can again chain the square bracket selectors together and update the value using the `=` sign.
Let’s assume we want to change the age of the student Janick to 24. We first must figure out the position of the entire list that represents the student Janick (`[0]`) and then the index position of the age within this list (`[1]`). By chaining the two selectors together we can then update the value accordingly.
```python
my_students[0][1] = 24

print(my_students[0])
["Janick Spirig", 24, 5.12]
```
---
### Methods
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b982215b-921f-4d4d-960e-4c038a6c2537/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q36LMLW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGkNbMeUBz%2B1u%2BMwfiBAb4durP%2FAefrmWRc8ftVTZbgXAiBqi6odWH30qoxtRPJYhrpzJ6Nj9r9NDbpV2lcIgLvm0Cr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMJik1UzDV6oMxTPodKtwD055t8nOIQ%2BKLkwx1LbOifXVmlVa6gDBKK%2BGjgqb8%2BrSKz0V5lUJaK21Cb%2BEVcxX6qOuLzZ%2BaR2lCuB%2Fqfw2VUcfmSfiu5LGypqIm9xVRwxEFzzGWB1cQc1RTP2fFJT%2FBl237xHeqwZ2jPj7bATTejOSwVWfafQOyFNXHHXxOT%2F22sr019wAC%2BNWg2Ym6UYiCBB9D3qAPFiXz2JViAcuXiaC5uPxQfv2mOfSxpWSmswXCw1OrsiMN5Y4HhuGbPFqchxCwweeZQI4qsiCNOIE8CTwxT9RvV2ij9bQMuNozQnrE%2FxuYiPx8FlEXqDe%2BXIouokSJjBPfh%2FBwPIwvaL1NrMKr5k%2FIQ455oMExLNYa%2FPltmoa5IWnBWqLAa5C1rOr9%2FSBrmcer4Z81qbuRic4wiqcJq%2Fa1kNYpx7EJ18zQJxiSDApa76dzYgZMBIhC%2FFlXXbZ5AvE%2FrHfplb5k3PSG1rtDFipgRGBrtOtTGliKgb%2BXWd04TQPzzGaSzpYHAn3SNOSuHOMX%2BfdSq361nnSCuc3U2LoyTI6RaZ%2Bs7ec2RpkCZb0p9of4lB8gjhrHsEeg20sD%2BCrZVeED5YtEz7Fsf29bgX2%2BDvO%2BovQT5fnJx%2Be5R22ox4yVdMHBBR4w1M73yQY6pgHED%2BBxuWvHQp%2F2Xce8b9YGMHMQXdM6W3nLRxHk%2F6Tvmce0q36Le21fIrTeDimEhFCLffAzPvKt2WDDlHZ%2B%2BzM50QsWfbXDLWo4OGcxdL%2BbDwau1xdLHhcoelndOkaM4WyEd%2BS71Pwv3F6eP1naWLW6jiRJyjnpFnYrsEFFDq5JY8iK3EDtLMkdyUD9duazKKnze%2B2tlvw%2Bhx34VtsXGMb2%2FbTl%2FNim&X-Amz-Signature=db01477ebd43140f4ecf9e791ee81de6ecbd42ce06b3b02f1f241f0fb044fca5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
[**`len()`**](https://www.programiz.com/python-programming/methods/built-in/len)
This method allows us to check how many elements there are in a list. 
```python
my_fruits = ['Rhabarber', 'Orange', 'Banana']

len(my_fruits)
3
```
---
[**`.append()`**](https://www.programiz.com/python-programming/methods/list/append)
This method allows us to add a new element to the end of an existing list.
```python
my_fruits = ['Rhabarber', 'Orange']

my_fruits.append('Kiwi')

my_fruits
['Rhabarber', 'Orange', 'Kiwi']
```
We can also provide a list as a parameter which is then appended as a separate list, thus the initial list becomes nested.
```python
more_fruits = ['Apple', 'Pear']

my_fruits.append(more_fruits)

my_fruits
['Rhabarber', 'Orange', 'Kiwi', ['Apple', 'Pear']]
```
---
[**`.extend()`**](https://www.programiz.com/python-programming/methods/list/extend)
This method allows us to merge two list together. Each element is taken out of the second list and added to the first list separately. Compared to `.append()`, this has the advantage that the second list is not added as a nested list.
```python
my_fruits = ['Rhabarber', 'Orange']
more_fruits = ['Apple', 'Pear']

my_fruits.extend(more_fruits)

my_fruits
['Rhabarber', 'Orange', 'Kiwi', 'Apple', 'Pear']
```
---
[**`.index(<< some list element >>)`**](https://www.programiz.com/python-programming/methods/list/index)
This method allows us to retrieve the index position of a specific list element. Remember that the first element has always position 0!
```python
my_fruits = ['Rhabarber', 'Orange', 'Kiwi', 'Apple', 'Pear']
my_fruits.index('Orange')
1
```
If we try to retrieve the index position for an element that is not part of the list, a `ValueError` is thrown.
```python
my_fruits.index('Lettuce')
ValueError: 'Lettuce' is not in list
```
---
[**`.insert(<< index position >>, << new element >>)`**](https://www.programiz.com/python-programming/methods/list/insert)
This method allows us to insert a new element into a list at a specific index position. Thus, all other elements after the new one are moved one index position to the right. 
```python
my_fruits = ['Rhabarber', 'Orange', 'Kiwi']

my_fruits.insert(0, 'Apple')
my_fruits.index('Apple')
0

my_fruits.index('Orange')
2
```
---
[**`.reverse()`**](https://www.programiz.com/python-programming/methods/list/reverse)
This method allows us to reverse an entire list. Thus, the last element is now the first and the first is now the last. 
```python
my_fruits = ['Rhabarber', 'Orange', 'Kiwi']

my_fruits.reverse()

my_fruits
['Kiwi', 'Orange', 'Rhabarber']
```
---
[`reversed()`](https://realpython.com/python-reverse-list/#creating-reversed-lists)
This method allows us to reverse an entire list. Thus, the last element is now the first and the first is now the last. 
```python
my_fruits = ['Rhabarber', 'Orange', 'Kiwi']

reversed(my_fruits)

['Kiwi', 'Orange', 'Rhabarber']
```
---
[**`.sort()`**](https://www.programiz.com/python-programming/methods/list/sort)
This method allows us to sort and update the list in place, i.e., the original list is changed. By default if we don’t provide any parameter, the list is sorted in ascending order.
```python
my_fruits = ['Kiwi', 'Orange', 'Apple']

my_fruits.sort()
['Apple', 'Kiwi', 'Orange']
```
By setting parameter `reverse` to `True` we can achieve that the list is sorted in descending order.
```python
my_fruits = ['Kiwi', 'Orange', 'Apple']

my_fruits.sort(reverse=True)
['Orange', 'Kiwi', 'Apple']
```
By defining the `key` parameter with a `lambda` function we can achieve that a nested list is ordered based on a specific element of its sublists.
```python
my_fruits = [['Kiwi', 'Orange'], ['Apple', 'Pear']]

my_fruits.sort(key=lambda x : x[0])
[['Apple', 'Pear'], ['Kiwi', 'Orange']]
```
---
[**`sorted(<< some_list >>)`**](https://www.programiz.com/python-programming/methods/built-in/sorted)
This method is very similar to `.sort()`, with the main difference that it returns a new sorted list, without changing the original list. It also has the optional `key` and `reverse` parameters.
```python
my_fruits = ['Kiwi', 'Orange', 'Apple']

my_fruits_new = sorted(my_fruits)

print(my_fruits_new)
['Apple', 'Kiwi', 'Orange']

print(my_fruits)
['Kiwi', 'Orange', 'Apple']
```
If the list should be sorted in descending order, the `reverse` parameter needs to be set to `True`. 
```python
my_fruits = ['Kiwi', 'Orange', 'Apple']

my_fruits_new = sorted(my_fruits, reverse=True)

print(my_fruits_new)
['Orange', 'Kiwi', 'Apple']

print(my_fruits)
['Kiwi', 'Orange', 'Apple']
```
---
[**`<< fill_value >>.join( << some_list >> )`**](https://www.programiz.com/python-programming/methods/string/join)
This method allows us to join all elements in a list together into a single string. Thereby, the `<< fill_value >>` is inserted between the single elements in the list.
```python
names = ['Janick', 'Marco', 'Hanna']

", ".join(names)
'Janick, Marco, Hanna'
```
If we provide empty quotations as fill value, then the elements are simply concatenated together.
```python
names = ['Janick', 'Marco', 'Hanna']

"".join(names)
'JanickMarcoHanna'
```
---
[**`.copy()`**](https://www.programiz.com/python-programming/methods/list/copy)
This method allows us to copy an existing list, so that we have two lists with the same values.
```python
my_fruits = ['Kiwi', 'Orange', 'Apple']

my_fruits_copy = my_fruits.copy()

my_fruits
['Kiwi', 'Orange', 'Apple']

my_fruits_copy
['Kiwi', 'Orange', 'Apple']
```
Be aware that these are now two different lists, thus when we make any change to one of them it will not affect the other one.
```python
my_fruits[1] = 'Pear'

my_fruits
['Kiwi', 'Pear', 'Apple']

my_fruits_copy
['Kiwi', 'Orange', 'Apple']
```
---
[**`any(<< condition >> for x in << some list >>)`**](https://www.programiz.com/python-programming/methods/built-in/any)
This method allows us to check if at least one element in a list is `True`.
```python
my_list = [True, False, True]

any(my_list)
True
```
```python
my_list = [0, False, False]

any(my_list)
False
```
We can also use the `any()` function to check for any kind of condition. The function will return `True` if at least one element in the list meets the condition specified.
```python
my_list = [5, 6, 4]

any(i > 4 for i in my_list)
True
```
```python
my_list = [5, 6, 4]

any(i < 4 for i in my_list)
False
```
---
[**`all(<< condition >> for x in << some list >>)`**](https://www.programiz.com/python-programming/methods/built-in/all)
This function allows us to check if all elements in a list are `True`.
```python
my_list = [True, False, True]

all(my_list)
False
```
```python
my_list = [1, True, True]

all(my_list)
True
```
We can also use the `all()` function to check for any kind of condition. The function will return `True` if all elements in the list meet the condition specified.
```python
my_list = [5, 6, 4]

all(i > 4 for i in my_list)
False
```
```python
my_list = [5, 6, 4]

any(i > 3 for i in my_list)
True
```
---
[**`.clear()`**](https://www.programiz.com/python-programming/methods/list/clear)
This method allows us to delete all elements in a list.
```python
my_fruits = ['Kiwi', 'Orange', 'Apple']

my_fruits.clear()

my_fruits
[]
```
---
[**`del[<< index position >>]`**](https://www.programiz.com/python-programming/del)
This method allows us to delete an element at a specific index position. So when we don’t know what element is at index position 1 but we want to remove it anyway, we can use `del[]`.
```python
my_fruits = ['Kiwi', 'Orange', 'Apple']

del my_fruits[0]

my_fruits
['Orange', 'Apple']
```
---
[**`.remove(<< some list element>>)`**](https://www.programiz.com/python-programming/methods/list/remove)
This method allows us to delete a specific element from a list. Compared to the `del[]` method, it looks for the specific element and does not go by the index position. So when we know that ‘Apple’ is part of our list, but don’t know at which index position it stands, we can use the `.remove()`.
```python
my_fruits = ['Kiwi', 'Orange', 'Apple']

my_fruits.remove('Apple')

my_fruits
['Kiwi', 'Orange']
```
---
### Slicing
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/84de2ef1-1bf1-43bf-8b67-ef3865b3b6c9/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DQSFJVO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCTkg3Q6djR8%2FwEWnxHs1qKo9q0WAjHRwI%2ByxxxLb%2BdtwIgCIrZAF0KY08PSVKerEnQ0XTW35zHP9ULbgFCCeu0SRQq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDFzHajtxZL0TxehVhyrcA6oU0%2FNl%2F3Iu4zfGM5lh0MkD7rQqarKufYwcVgcX7B2c40GLGFWnj2OjGz6vkPqDocFWSTn3lYp%2BSuW1ETrBO%2B%2B0qq%2FHBAGDaA8CmcRs9YYPK3NH8aEgU7hMZsctpX426uX8m6OL4RKkf0ChF1gubo8R7oe%2BN4lmgvaTRT4xeU2dndF1ofiazXXkGKu1FKprB6DQ3IITZkigwMbdu0ZfYVIinY7wep5aeGlB6t%2FKxIx4RnoNHV8BTJfrxpXd1VgrBotqMPFjLXgv1lRl1c3MGbNEOg9l06U2cF85L0TKediw6RUO0lj8JYwGKmg7BkM9RsHd7nrSWqZ04gcEBxL9hml3v4IMYdMcvZ0Z0R45WvsIBIZXlwIKjeGy4%2B2N1yXx4N3N3WB98ZIl%2BTTPEX57ZRYYRapS1Dv0KpjZKDY0hnBoTGbCFylCzzcS8YHiA7jvoPjWK6q6u6ztmY25WQtZdu3A05GPli5oFEzmCng7uL2voAWFaIz2ij1ahMh6kslv3WNQKmO9Pj8LKrZMbDW2aFAUSJanXCSLd%2Fp3pjQ8jaIuFQGEf%2BYFuMNEm7CUSpnOx1fQSJK%2F5369orgF4Odf37IaRXxFollGacesTy6UU6bVN6P5neW%2BYJo%2B%2BMxRMN%2FO98kGOqUBpGZSqH6wpUX%2FrZIQKZOtUgCSrRn4ReDCePpPePlTk0WWDVAGvN%2BLLSkyTdE9peEKM9OXhlp6nlVvyhtBbFZH4Y9%2BREF0ppZvP%2BtoYk9X5sG6LQYBDP1OWIpu2c1qbtbgyhIMa5jy5vUeXvyUG5CBfmQmVUmuoOzz8eknjw8Xa1m5xCkJj7xzvhYFhneHFB%2FNn8Lfmxpsbeuz941j0doGyjxnIKkh&X-Amz-Signature=c16b2444ecba405497fc567a9efec22a842812911db29b2508a2cd2458f77da8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Syntax**
One powerful type of operation that we can do with lists is slicing as it allows us to extract a sub-set of element of a given list.
The general slicing syntax is the following:
`[<< first index included >>, << first index excluded >>, << step size >>]`
The step size is optional. It is important to note that we slice by index positions and not by element. To make this more clear, you find below some examples of the most important slicing operations that you should be aware of.
Let’s first create a new list called `my_list`
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
---
**Normal slicing**
Let’s extract the elements `3` `4` & `5` from [`my_list`](/5b0832dbf9454eb1941b7632e68a9abb).
```python
my_list[2:5]
[3, 4, 5]
```
Why `[2:`?
Number `3` is the first element in the list that should be included and stands at index position 2 (remember that we start counting index positions at 0)
Why `:5]`?
Number `5` is the last number that should be included and stands at index position 4. Remember that we need to tell Python the index position of the first element that should be excluded and not the index position of the last element that should be included.
---
**Normal slicing with one parameter**
Let’s extract the first five elements, i.e., the numbers `1` `2` `3` `4` & `5` from `my_list`.
```python
my_list[:5]
[1, 2, 3, 4, 5]
```
Basically we have here almost the same command as in the example before. However, this time we only provide one parameter inside the brackets `[:5]` and don’t write anything to the left of the double point `:`, which tells Python that we want to include all elements from the beginning on.
Similarly, if we want to extract the third and all following elements we can simply provide a parameter to the left of the double point `[2:]` but no parameter to the right of the double point `:`
```python
my_list[2:]
[3, 4, 5, 6, 7, 8, 9]
```
---
**Normal slicing with step size**
Let’s extract every second element from the list between the second and sixth element in the list.
```python
my_list[2:7:2]
[3, 5, 7]
```
The first part of the slicing operation `[2:7` looks already quite familiar. However, within this result-list we want to extract now every second element only. This is why we add an additional parameter step-size `:2]` to the slicing operation and we get `my_list[2:7:2]`. This operation essentially tells Python that it should return the first element defined (index position 2) and then every second element until index position 7 has been reached. 
The step size can be of any length, for example we can also include every third element only, which consequently returns even less elements in the result set.
```python
my_list[2:7:3]
[3, 6]
```
---
**Negative slicing**
We can also do negative slicing, which basically means that we slide the list from the back (remember [index positions](/5b0832dbf9454eb1941b7632e68a9abb#5229e788b0d74c0d81a5a46a8e74880b)). To do so, we simply add minus signs `-` in front of the integers in the slicing selector. Syntax-wise nothing changes, we only must keep in mind that we count now elements from the back, meaning we start at `-1` and not at `-0`.
Let’s assume we want to extract the 5th last until the 3rd last element.
```python
my_list[-5:-2]
[5, 6, 7]
```
Why `[-5:`?
The 5th last element is the first one that should be included.
Number `3` is the first element in the list that should be included and stands at index position 2 (remember that we start counting index positions at 0)
Why `:-2]`?
The 3rd last element is the last one that should be included. Thus, the first element to be excluded is the second last one.
Thus, with the selector `my_list[-5:-2]` Python counts backwards five elements and marks this one (5) as the first to include. Then it counts backwards two elements and marks this one (8) as the first one to exclude.
> 💡 **Compared to normal slicing we do negative slicing by counting the elements and not the index position. So we start at the end of the list, i.e., at the last element and say this is element one and then just count backwards.**
---
**Negative slicing with step size**
Just as with normal slicing, we can also include an additional step-size parameter in the slicing selector. Let’s say we want to extract every second element between the 7th last and the 2nd last element. 
```python
my_list[-7:-1]
[3, 4, 5, 6, 7, 8]
```
From the code snippet above we see that Python again counts backwards seven elements and marks this one (3) as the first element to include and then counts backwards one element (9) and marks this one as the first one to exclude. 
Now we can insert the step `:2` and Python will exclude every second element, i.e., the elements `4` `6` & `8`.
```python
my_list[-7:-1:2]
[3, 5, 7]
```
It is important to note that although we have negative slicing, the step-size does not have a minus but is a positive integer. If we would do step-size `-2` Python would return an empty list.
```python
my_list[-7:-1:-2]
[]
```
---
**Slicing with step size -1**
Something very cool we can do with slicing is including a step-size `:-1` which reverts the elements in the result list that the slicing selector returned.
Let’s say we want to extract all elements from the list but in reversed order, meaning that the last element (9) should appear now as the first one and the first element (1) as the last one.
```python
my_list[::-1]
my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
```
We see that with the first `:` we select all elements from the list and with the second `:` we tell Python that step-size `-1` should be applied. This step-size reverts the slicing result, i.e., the entire list. 
Another example: Let’s extract the fifth (5) element and all following elements but in reversed order.
```python
my_list[4::-1]
[5, 4, 3, 2, 1]
```
We see that first Python simply does normal slicing by selecting the element at index position 4, i.e., the 5th element (5) and all following elements and then reverses their order as we have provided step-size `-1`.
---
> 💡 ****Remember:****
- Slicing goes over index positions
- When writing a double-point `:` all elements before or after are included
- When applying negative slicing, we start counting from the back, thus the first parameter must be bigger than the second one, i.e., `[-2:-5]` is not a valid slice
- With the optional step-size parameter `n` we can over-jump elements in the slicing result by including the first element and then only every `n`-th element
- We can reverse a list with step-size `:-1` otherwise, step size must be positive
---
### Copying a list
---
**Background**
One special case that we must be aware of is when we want to copy a list. More specifically, we must know the difference between assigning an existing list to a new variable using value assignment `=` and actually copying a list using `.copy()`.
> 💡 **When using `.copy()` a new list is created. When using value assignment `=` we store the reference address of an existing list in a new variable, making both variables pointing to the same list.**
---
**Copying with ****`.copy()`**
Let’s assume we have a list that contains data about a student: 
`student_melanie = ["Melanie Huber", 22, 4.87]`
Now we want to copy this list and save the new list in a new variable. As we know already we can achieve that by using the `.copy()` method. 
```python
student_melanie_new = student_melanie.copy()

print(student_melanie_new)
["Melanie Huber", 22, 4.87]
```
Now the good thing is that when we update any value in the new list `student_melanie_new`, the original list `student_melanie` won’t be modified as they are separate lists.
```python
student_melanie_new[2] = 5.4

print(student_melanie_new)
["Melanie Huber", 22, 5.4]

print(student_melanie)
["Melanie Huber", 22, 4.87]
```
---
**Copying using assignment ****`=`**
Let’s assume we have again some data about the student Melanie.
`student_melanie = ["Melanie Huber", 22, 4.87]`
Also we have data about the best performing student.
`best_student = ["Marco Meier", 25, 5.12]`
Now Melanie has achieved a new GPA of 5.2 and thus we update her GPA.
```python
student_melanie[2] = 5.2
```
Since Melanie’s GPA of `5.2` is now higher than Marco’s GPA of `5.12` we must also update the value in `best_student`.
To do so, we can overwrite the value stored in `best_student` by assigning (not copying!) this variable to the same list that is stored in `student_melanie`.
```python
best_student = melanie_student

print(best_student)
["Melanie Huber", 22, 5.2]
```
As we can see from the code snippet above, this time we did not use the `.copy()` method but just a regular assignment operation `=` as this brings the benefit that when we update the `student_melanie` variable, the variable `best_student` is automatically updated as well.
So let’s say we want to update the age of Melanie now to 23. We do so and check the values stored in both variables.
```python
student_melanie[1] = 23

print(student_melanie)
["Melanie Huber", 23, 5.2]

print(best_student)
["Melanie Huber", 23, 5.2]
```
As we can see from the code-snippet above, we just updated one of the two variables and the other one got updated as well, automatically. Thus, when we do an assignment operation using `=` we actually don’t create a copy of a list, we instead cause that both variables are pointing to the same list.
---
### List comprehensions
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e521b634-ecb8-4704-931e-58581b0f140c/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GGK64HG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGS2MzIoX09NGbiXmyseO%2B8iv92Uq5om%2B7Jz%2BfDGxIYIAiEAtbUZ2%2BQpoUgf7YEMMCHKNmBvjr%2Br3moIhHZQ0S7%2F8kkq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFzF%2BTOqZrpc75m0jSrcA%2FHwtSUFxpG4H55n5Yls3%2BjSbIGPtFWRXlusa3%2B896t5fCZChXPXgJGxFRzR4Yyoe0XxEYVIV9LXj539z%2FkGr0oXpoG009trUuurK7wgBoyKCyZh3JBryjP%2FshHUXKCrg7BXxEmT74SIEk0EiiwWNv4IE6J9pfypVAT4xJOTqtVe9EZyVYkP5GlKVRUKl%2BgxNNCvLzlFXRoRDxRo7m9L2GyoXgICmHiexqKWwEJgHfpZ93uRdky1ZDAcWQQf6T9VZ1qlkTi37QfK2MN9VVPcFqigPL2PdWxUC9vGVgr%2BNmAP3nzzwZ%2FOZzibwuSbY01yU1S6UbXMJb0LdNE2BCr3mtNmB%2FUvCaHtwZtB4KTnvcnli4b%2BWOk9sKzRkyhdbMsh4eCsiXjXnXTI7KSneK7SJ%2FxNi4sWhDGo6RfDKcF1Qf6WsahMGjW%2Bg4usJGKOvzCE62WmQ6jViTaJs%2F%2F50XiN4SIuJsG7UveBnBgMhaFz9hfQPs3f3PWDixoyzystenhFH2MQm8Ox3LkWXTzvJpTWmENZAmSCZ5BTmWI57zyV3Z%2FqUtkHRUG6%2BYDkBNzi8V0GymjMNpCdEC4Sq2u%2Bp4mYcDOXl%2Bjdn4c3Vtgc9Ip6U%2FDD8MaQflJH918lERvJMPLN98kGOqUBI3M0%2B%2BLaTuHFjDjhGUq0P%2BwiyQzzaVxviWpznNoMqwhMoNorlwSMGlsuEbchlhlzMyPP8D5IK2fcf%2B4XovFWgwCaO9Q2I6wJ80U6SwNYf8ktpuyZUf3Pmqv1IHASKwu24nrlX3Oy1FCktgk0dbkW6ku1mZZ9jGgW7AJ0QYbI6ZIs%2Fm2d0pNJS8z4%2FRFG%2FN37dAmIah%2Bmw%2B%2FJsqN1vLM52gOzwWDY&X-Amz-Signature=cfe99acbbeb8d9615640f52c2f032bf737003e8e864484c5cf29b77717e27095&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**General**
Often we have to modify all the elements in a list. With a for-loop it is very easy to iterate through a list and modify one element after the other. However, a for-loop requires at least two lines of code and high computational resources. To simplify the usage of for-loops in combination with lists, we can use list comprehensions.
The general list comprehension syntax is as follow:
`[ << operation >> for x in << some iterable >> if << condition >> ]`
As we can see, a list comprehension can combine a for-loop and an if-else statement in one single line. The brackets at the left (`[`) and right (`]`) indicate that the list comprehensions return a new list. As we will see, the `if << condition >>` part is optional.
---
**List comprehension with for-loop**
Let’s assume we have two lists containing different names and we want to check if some names are equal. It can now be that the same name is stored as `'Anna'` in one list and as `'anna'` in the other list.
```python
names1 = ['anna', 'FriTZ', 'LaRa', 'MartiN']
names2 = ['Anna', 'bEnjamim', 'laRA', 'martin']
```
If we now check `'Anna' == 'anna'` the result is `False` because boolean comparisons are case-sensitive. Therefore, we must transform the names in both list to either lower or upper case only. We could do this with a for-loop wrapped into a function so we can use the for-loop twice for both lists.
```python
def to_upper(my_list):
	my_list_new = []
	
	for x in my_list:
		my_list_new.append(x.upper())
	
	return my_list_new
```
We can now call the function `to_upper` for both lists in order to convert the names to upper-case only.
```python
to_upper(names1)
['ANNA', 'FRITZ', 'LARA', 'MARTIN']

to_upper(names2)
['ANNA', 'BENJAMIM', 'LARA', 'MARTIN']
```
From this example we can see that we need many lines of code to achieve what we want: A new function and two function calls.
Using list comprehensions we can simplify this operation a lot by getting rid of the `to_upper` function.
```python
[x.upper() for x in names1]
['ANNA', 'FRITZ', 'LARA', 'MARTIN']

[x.upper() for x in names2]
['ANNA', 'BENJAMIM', 'LARA', 'MARTIN']
```
<details>
<summary>*Disclaimer*</summary>

We can see that we need a lot less lines of code. However, we also see that we have some redundancy here as we use the `.upper()` function twice in the same context. However, this is a very small redundancy and to write functions for everything  does not make a lot of sense. Thus, the saving of code lines outweighs this redundancy in this scenario.
</details>
The list comprehensions in the code snippet above work as follow:
1. `for x in names1` → the current name is stored in variable `x`
1. `x.upper()` → the name stored in variable `x` is transformed to upper letters
1. Step 1 and 2 are repeated until Python arrived at the end of the list
1. New list containing all names in upper-case letters is returned
> 💡 **When we read a list comprehension we start in the middle at the `for` keyword. Then we go to the right (`x in names1`) and only then we look at the left of the `for` keyword (`x.upper()`). Respecting this order is crucial as otherwise confusion can arise.**
The image below shows how the first option, function `to_upper`, and the second option, list comprehension, relate to each other.
![How for-loop and list comprehension relate to each other](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/86961609-5af3-477a-abf7-fe34334ae1ea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GGK64HG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGS2MzIoX09NGbiXmyseO%2B8iv92Uq5om%2B7Jz%2BfDGxIYIAiEAtbUZ2%2BQpoUgf7YEMMCHKNmBvjr%2Br3moIhHZQ0S7%2F8kkq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFzF%2BTOqZrpc75m0jSrcA%2FHwtSUFxpG4H55n5Yls3%2BjSbIGPtFWRXlusa3%2B896t5fCZChXPXgJGxFRzR4Yyoe0XxEYVIV9LXj539z%2FkGr0oXpoG009trUuurK7wgBoyKCyZh3JBryjP%2FshHUXKCrg7BXxEmT74SIEk0EiiwWNv4IE6J9pfypVAT4xJOTqtVe9EZyVYkP5GlKVRUKl%2BgxNNCvLzlFXRoRDxRo7m9L2GyoXgICmHiexqKWwEJgHfpZ93uRdky1ZDAcWQQf6T9VZ1qlkTi37QfK2MN9VVPcFqigPL2PdWxUC9vGVgr%2BNmAP3nzzwZ%2FOZzibwuSbY01yU1S6UbXMJb0LdNE2BCr3mtNmB%2FUvCaHtwZtB4KTnvcnli4b%2BWOk9sKzRkyhdbMsh4eCsiXjXnXTI7KSneK7SJ%2FxNi4sWhDGo6RfDKcF1Qf6WsahMGjW%2Bg4usJGKOvzCE62WmQ6jViTaJs%2F%2F50XiN4SIuJsG7UveBnBgMhaFz9hfQPs3f3PWDixoyzystenhFH2MQm8Ox3LkWXTzvJpTWmENZAmSCZ5BTmWI57zyV3Z%2FqUtkHRUG6%2BYDkBNzi8V0GymjMNpCdEC4Sq2u%2Bp4mYcDOXl%2Bjdn4c3Vtgc9Ip6U%2FDD8MaQflJH918lERvJMPLN98kGOqUBI3M0%2B%2BLaTuHFjDjhGUq0P%2BwiyQzzaVxviWpznNoMqwhMoNorlwSMGlsuEbchlhlzMyPP8D5IK2fcf%2B4XovFWgwCaO9Q2I6wJ80U6SwNYf8ktpuyZUf3Pmqv1IHASKwu24nrlX3Oy1FCktgk0dbkW6ku1mZZ9jGgW7AJ0QYbI6ZIs%2Fm2d0pNJS8z4%2FRFG%2FN37dAmIah%2Bmw%2B%2FJsqN1vLM52gOzwWDY&X-Amz-Signature=99b338d21e3f0f0f22712bd977fb1c4faac330588ab91157e8a213f57b313da3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**List comprehension with for-loop and if condition**
We can extend the list comprehension by adding a condition to it. The condition causes that the operation will be executed only for those elements for which the condition evaluated to `True`. 
Let’s assume we have a list that contains strings and integers
```python
my_list = [1, 'banana', 3, 5, 'apple', 10]
```
Based on `my_list` we want to create a new list `my_new_list` that contains only the integers of `my_list`. We could again use a regular for-loop to achieve this:
```python
for element in my_list:
	
	my_new_list = []

	if isinstance(element, int):
		my_new_list.append(element)

my_new_list
[1, 3, 5, 10]
```
Or we can use a much simpler list comprehension to achieve the same.
```python
my_new_list = [x for x in my_list if isinstance(x, int)]

my_new_list
[1, 3, 5, 10]
```
We can see that we have now an `if` keyword in the list comprehension. With this new element, Python executes this list comprehension as follow:
1. `for x in my_list` → the current value is stored in variable `x`
1. `if isinstance(x, int)` → it is checked if the value is an integer
1. `x` → if element is an integer it is put into the result list
1. Step 1 to 3 are repeated until Python arrived at the end of the list
1. New list containing integers only is returned
Again we see the importance of correct interpretation. The condition is checked before the operation. So we first read middle to right and only then we look at what is there to the left of the `for` keyword.
---
**List comprehension with for-loop and if-else condition**
Let’s assume that for the non-integers (strings) we want to insert the value `'invalid'` in `my_new_list`. We can extend the list comprehension as follow:
```python
my_new_list = [x if isinstance(x, int) else 'invalid' for x in my_list]

my_new_list
[1, 'invalid', 3, 5, 'invalid', 10]
```
We can see that the if-statement has moved now to the front of the `for` keyword and contains now also an else-statement. Whenever we use an `if` and an `else` we need to put the condition after the operation and before the `for` keyword.
Python however still executes the code in the same order as before:
1. `for x in my_list` → the current value is stored in variable `x`
1. `if isinstance(x, int)` → it is checked if the value is an integer
1. `x` → if element is an integer it is put into the result list
1. `else 'invalid'` → if element is not an integer, the value ‘invalid’ is put into the result list 
1. Step 1 to 4 are repeated until Python arrived at the end of the list
1. New list containing integers and string `'invalid'` is returned
> 💡 **When the condition contains only an `if` statement we write it after the for keyword. When the condition contains an `if` **AND** an `else` statement we write it between the operation and the `for` keyword.**
---

---
## Tuple
---
**Definition**
Similarly as a [list](/5b0832dbf9454eb1941b7632e68a9abb#5d06cfcdb5574513a592b854a821fe3e), a tuple is also a collection of different objects such as 
`my_fruits = ('Rhabarber', 'Apple', 'Pear', 'Orange')` 
We can also store different types of objects in the same tuple such as 
`my_arbitrary_tuple = ('Rhabarber', True, 500, 200.45)` 
> 💡 ****Tuple vs. List****
Compared to a list, a tuple is annotated with curvy brackets `()` and is **immutable**.
This means we cannot update any value in the tuple after we have created it.
```python
my_fruits = ('Rhabarber', 'Apple', 'Pear', 'Orange')
my_fruits[2] = 'Kiwi'

TypeError: 'tuple' object does not support item assignment
```
### Access elements
---
Same as lists → [check here](/5b0832dbf9454eb1941b7632e68a9abb#430375c9e3ea4d7d92dab7f5283a1e7e).
```python
my_fruits = ('Rhabarber', 'Apple', 'Pear', 'Orange')

my_fruits[2]
'Pear'
```
```python
students = (('Janick', 25), ('Marco', 24))

students[0][1]
25
```
---
### Methods
---
Below you find an overview which of the lists methods can also be applied on tuples. 
| Method | Can be applied on tuple |
| --- | --- |
| [`len()`](/5b0832dbf9454eb1941b7632e68a9abb#e097ab624af04d18b7f69088dff7d5f2) | Yes |
| [`.append()`](/5b0832dbf9454eb1941b7632e68a9abb#2561c3326d19459292a03dea27a7eda1) | No |
| [`.extend()`](/5b0832dbf9454eb1941b7632e68a9abb#95a1b8efeda643fd9f8728ef92e82203) | No |
| [`.index()`](/5b0832dbf9454eb1941b7632e68a9abb#dcd2ede9020740e587b8eb9931622a11) | Yes |
| [`.insert()`](/5b0832dbf9454eb1941b7632e68a9abb#05aecd6477dd4f66bb8472a2305614b7) | No |
| [`.reverse()`](/5b0832dbf9454eb1941b7632e68a9abb#5423b380520445efa0ddb552b4d7cead) | No |
| [`.sort()`](/5b0832dbf9454eb1941b7632e68a9abb#2c743eec0b2546119e1e79f642f00e25) | No |
| [`sorted()`](/5b0832dbf9454eb1941b7632e68a9abb#7c022c5cc1a647d58ba1a7e82406c3e6) | Yes |
| [`.copy()`](/5b0832dbf9454eb1941b7632e68a9abb#df643776070043b79ff8b852ba3def62) | No |
| [`any()`](/5b0832dbf9454eb1941b7632e68a9abb#dc93a29fa5194f55836401522ec3b104) | Yes |
| [`all()`](/5b0832dbf9454eb1941b7632e68a9abb#fc9a71849e2e45b3b0a102f0502ea8de) | Yes |
| [`.clear()`](/5b0832dbf9454eb1941b7632e68a9abb#ce556531b7364fd79a71ef9d0b12f598) | No |
| [`del[]`](/5b0832dbf9454eb1941b7632e68a9abb#89fdb4db529c4947a5514d47bf18abe4) | No |
| [`.remove()`](/5b0832dbf9454eb1941b7632e68a9abb#7bc0fda22b674fe1a1fa1abce52eff07) | No |
---
### Slicing
---
Same as lists → [check here](/5b0832dbf9454eb1941b7632e68a9abb#01370999e4334066ba04335de9ae836a).
```python
students = (('Janick', 25), ('Marco', 24), ('Melanie', 26))

students[1:3]
(('Marco', 24), ('Melanie', 26))
```
```python
students = (('Janick', 25), ('Marco', 24), ('Melanie', 26))

students[::2]
(('Janick', 25), ('Melanie', 26))
```
```python
students = (('Janick', 25), ('Marco', 24), ('Melanie', 26))

students[::-1]
(('Melanie', 26), ('Marco', 24), ('Janick', 25))
```
etc.
---
## Set
---
**Definition**
A set is a collection of unique objects, this means that in a set the same value cannot appear twice. We can create a set by using curly brackets `{}`.
`my_set = {1, 2, 3, 4, 5}`
### Common operations
---
We can use the `set()` method, this is often used to remove duplicate values from an iterable like a list.
```python
my_list = [1, 1, 2, 3, 3, 4, 5, 5]

set(my_list)
{1, 2, 3, 4, 5}
```
Often we can use a set to determine how many unique elements there are in an iterable such as a list or tuple. To do so, we convert the iterable to a set using `set()` and then count the elements using the [`len()`](/5b0832dbf9454eb1941b7632e68a9abb#e097ab624af04d18b7f69088dff7d5f2) method. 
```python
my_list = [1, 1, 2, 3, 3, 4, 5, 5]

len(set(my_list))
5
```
Note that a set object is an unordered collection. Thus, we cannot access an element over an index position as we do it with lists.
```python
my_set = {1, 2, 3, 4, 5}

my_set[2]
TypeError: 'set' object is not subscriptable
```
---
### Methods
---
[**`.add()`**](https://www.programiz.com/python-programming/methods/set/add)
This method allows us to add a new element to a set.
```python
my_set = {1, 2, 3, 4, 5}

my_set.add(6)

my_set
{1, 2, 3, 4, 5, 6}
```
If we try to add an element that already exists in the set, no element is added as duplicates are not allowed.
```python
my_set = {1, 2, 3, 4, 5}

my_set.add(5)

my_set
{1, 2, 3, 4, 5}
```
---
[**`.union()`**](https://www.programiz.com/python-programming/methods/set/union)
This method allows us to combine two sets together by creating a new set that includes all unique values from both sets. Note that duplicates are filtered out automatically.
```python
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {1, 2, 4, 7, 8} 

my_set_1.union(my_set_2)
{1, 2, 3, 4, 5, 7, 8}
```
---
[**`.intersection()`**](https://www.programiz.com/python-programming/methods/set/intersection)
This method allows us to retrieve all elements that two sets have in common.
```python
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {1, 2, 4, 7, 8} 

my_set_1.intersection(my_set_2)
{1, 2, 4}
```
---
[**`.symmetric_difference()`**](https://www.programiz.com/python-programming/methods/set/symmetric_difference)
This method allows us to retrieve all elements that are either in set 1 or 2 but not in both.
```python
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {1, 2, 4, 7, 8}

my_set_1.symmetric_difference(my_set_2)
{3, 5, 7, 8}
```
---

---
## Range
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/14e2f00c-fbe3-47cb-816d-016f39be48ae/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y626XCDN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIHAHiX4SCPdbYGv6Fi4wSRjXgWlY0hW9LUEEeVtAdByIAiEAu5Y83gy7ACwho80YRu5%2Bje8%2BYYfqfDyHYTvmb5ZS6%2BYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBoNMTM352eHzNeaWyrcA6IUh0PCiWJW6PcRZiTDOW2NOaijhtu4ad2izrKt7fwTIxFoSteMr%2Bj%2F3fvpNgT8iiQMCOWsTnmoaYi0Dhg7fZf3w2B%2F%2FmrHjPKBKeoUSob5EHdXNAN1LzlDD8YBcRNTFsNLqQtBwvIar7qf3p71jMKnI4YuZ3mZEZLZqDF4Y6qx2NqoNRRAwJVDClkdJ9KGtr8QcxKtcz9%2FVvd7vvxDpGwcn5FtTAt2Q5TmnJ0SB%2FAjoZ%2BLDFHJfyDKBaotIsLTVMupHPE3jRqZ6FEDgf4hVP7p7brQklRWcKuS%2FZG%2BYlUyECL74iCaEv0okv9hADZp3LBTUDhBX0KfZhKd2PGhUURuneQXBEcu5yRq44dpFQ2vwjBXt%2FiUbApEyqXOysDtOT7yW5jDDoossYLVVqLYQESzWupUHA0CSwlkMhOAg%2FHLDePN3%2B1FUMK2Rm2iDxHdQC7G78qjt9XtpuaihBBjyEODVyxbXgPHDGJZFHzscaR%2BmruTs70ebHav0piRYriAqkzyOoUCJGEYl%2FLOps114nom9egqmUsTt46cb9RRceQRw2QSshynxpQdZTiS1L31VIQHNBlSQBTcu%2F2Q%2BikQLmOPLXUmUUnc4jdIaFIgXE9gk8d%2BqpJj07GcgqufMLbO98kGOqUB5uQpPXquxLgV%2BjbI3qHnql80cyU%2FAYylAVeWc93BHOnVO4EDGE9NeaApMaEf8ojYI71Y76QnmO4XasIDV3x4MtdGFPFQm2AIY6omBlH6SV2FvkFJf%2Fedcxjci5pgXBsuXw2tKNiE7GvsRh8UWN%2Fxj3lhhbtEfz7msHtxrx%2FTg3Ssh7%2BESfbfILBYNteboPR1YGB3E6908DsnsUoAEHQldhTXuKnM&X-Amz-Signature=c9810c18d214c25cf1b14a4af10d035b8f7a8f21ffe80238d4e65d30150f4842&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Definition**
A range object is an immutable sequence of numbers and we can create a new range object using the built-in `range()` method:
`range(<< first num included >>, << first num excluded >>, << step size >>)`
The  `<< step size >>` and `<< first num included >>` are optional.
### Common operations
---
**Checking what’s inside**
When printing the range object, the output is not very useful as it des not display the entire number range. Thus, we don’t know which numbers are included and which numbers are not.
```python
my_range = range(1,5)

my_range
range(1, 5)
```
Therefore, we usually convert the range to a list before we print it to the console.
```python
my_range = range(1,5)

list(my_range)
[1, 2, 3, 4]
```
From the code snippet above we see that 1 is the first number that was included and 5 the first number that was excluded from the number range.
---
**Create range with one or three parameters**
When we only provide one parameter / number to the `range()` function, then this parameter is treated as the first number to be excluded and the range starts from 0.
```python
my_range = range(6)

list(my_range)
[0, 1, 2, 3, 4, 5]
```
We can also make use of step size as we know it already from list.
```python
my_range = range(1,5,2)

list(my_range)
[1, 3]
```
---
**Using a range in combination with a for-loop**
Let’s assume we want to process every element in a list inside the for loop. We can do it with a simple for-loop:
```python
my_list = ['a', 'b', 'c']

for x in my_list:
	print(x)

a
b
c
```
But what if we also want to do something with the index position of the elements. In this case we can make use of `range()` and `len()` function. By nesting these two functions together, we receive a range object that includes every index position of the list.
```python
my_list = ['a', 'b', 'c']

for i in range(len(my_list)) :
	print(my_list[i])

a
b
c
```
From the code snippet above we can see that by nesting `range()` and `len()` together we can iterate over a list as well. The main difference to the previous code snippet is that now an integer is saved the temporary variable `i` and not a list element as we have seen it before with the variable `x`.
Python executes the code step-by-step as follow:
- `len(my_list)` → `len(['a', 'b', 'c'])` → `3`
- `range(3)` → `range(0, 3)` → range with numbers `0` `1` and `2`
- First run
- `i = 0`
- `print(my_list[0])` → `'a'`
- Second run
- `i = 1`
- `print(my_list[1])` → `'b'`
- Third run
- `i = 2`
- `print(my_list[2])` → `'c'`

> 👉🏻 **For a more detailed explanation how `for` and `range()` are used in combination with each other [check here](/5b0832dbf9454eb1941b7632e68a9abb).**
---
## Dictionary
---
**Definition**
Dictionaries allow us to store information in the form of key-value pairs. We can detect a dictionary by its curly brackets `{}` and the double-points `:` inside that separate keys from values.
### Common operations
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5a846a70-a4eb-41a2-a7f7-3c0e9d5cc42a/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDTF3UH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDw3QPxKTjoFn60WUxLDakb8jtIjoZ4KcpuV0G%2BL08bygIhAPJD87i1a0TJIJ2i4gx3LZU0swkuRNHpDynMhNJmzWtlKv8DCCcQABoMNjM3NDIzMTgzODA1IgyE%2BIyRc4FnDE3g8Nwq3AMWHBUWlKg2Tdj4FuumYT9tUphNn1rE7muJpNPEh4%2Bvs5aT6SpNL1rS5SOHOQGSXKD5b4q%2Bwun7KoueYYgDkatjK2KEOFCqvfooJJDObO8MuwHRLe82QXn5tJV%2FMhlLG1g4SOwL1okC9W6g0RPETms67%2BAkpyyAU%2FDb9YT3prvv%2F%2F%2BITluWU8fB%2BKPQQieyFUHpcl3ypg2bEb5JF1pCEUrVpnpyQ20U184KDMs%2FsSKbA1bRGbcmrHcwxBVBnh1rg%2BvYjwXB8qoBsRiTCAmWGp%2BCT6i1YIqUgf38GZ%2FXVO1BetJpxazCOpwNl04dFG4B5IETyzB%2F%2FkhjAbptmlgGyWFcGaCPo61rMuqXRx%2BR7XjwX0PsylYkuWiJx9iDBvVrXZPEg02qdrINZwE%2BDGSPkxVHv4Yp%2FhjnA2CgudAEpTbRzuUrtafXYYo8vDpj%2Fu%2F6JnuGTkCkdPHSxqmjMOFqbmDvrvUSgSFAc58hyMzMweOJwcN0f8vLxmlwrLv7LIBBPNO5PAslth1tQA0u%2B%2Bbj5aqQdc7nXaFStSASdE9QwSbSWtR0hRPmLRBmlHM5HFKMSpMviG8eVjUMYYcVa8%2Fa04seLQ8MoPaYsUBC%2BokcODGDiBEBmT9MJOIP2HsjYTC1zvfJBjqkAcobvgEPDsUDywK93rjTh6IeyeJxuLApRcidUwjw0Q0X%2BXKTApqqDEGF4xwoeADqWLvl5bHlRZnTv%2FVnVjepu9YP7JnnYCURlHcE1lyf%2BdFeNiWEIa%2FWNm2IgobhAAmp5MHCIadGf89gwPeWO%2FYxTQ9jNOWyX4gdjVdNgcbsysfsojft3NxdeQs8A8F2gKDL%2FGQ6hLZgFKsrTsTilwwG%2Frm3ba2d&X-Amz-Signature=d83c5ee4bd54f24bbd552e933dabffd073429b37f61d87f4a4de3fc8acc4b1cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Creating a dictionary**
Let’s assume we know the names and ages of four students. To store this information we could simply create two lists, one called `student_names` that contains all names and another one called `student_ages` that respective ages.
```python
student_names = ['Janick', 'Marco', 'Melanie', 'Barbara']
student_ages = [25, 27, 19, 22]
```
With this approach we have all the information stored, however, in a very cumbersome way. Let’s think about a scenario in which we want to find out the age of the student Melanie. To do so, we need to remember that Melanie is the third student in the `student_names` list and that the `student_ages` list is ordered in the same way. If we don’t know at which position Melanie stands or that both lists are ordered in the same way it would be difficult to find out Melanie’s age. 
To mitigate this issue we can create a dictionary in which we use the student names as keys and the ages as corresponding values.
```python
person_age = {
	'Janick' : 25,
	'Marco' : 27,
	'Melanie' : 19,
	'Barabara' : 22
}
```
We see that creating a dictionary is quite simple, we just use curly brackets `{}`, define a `key` followed by a double-point `:`, its corresponding `value` and a final comma `,` to separate the different entries from each other. Thus, each entry in the dictionary, i.e., student / age combination is called a key-value pair.
---
**Accessing a value**
If we now want to access the age of Melanie we can use a similar approach as with lists, namely the square brackets `[]`. We call the variable in which we have stored our dictionary, `person_age`, and provide the respective key, i.e., a student name inside the brackets. 
```python
person_age['Melanie']
19
```
---
**Modifying a value**
Modifying a value is very similar: We just provide the key inside the brackets whose value we want to modify and provide the new value after the equal `=` sign. So let’s assume we want to update the age of Marco to 31. 
```python
person_age['Marco'] = 31

person_age['Marco']
31
```
---
**Deleting a key-value pair**
If we want to delete an entire key-value pair from a dictionary we can use the `del()` method. As a parameter we just need to provide the key of the key-value pair that we want to remove from the dictionary. Let’s assume we want to remove the entry `'Janick' : 25` from the dictionary. 
```python
del(person_age['Janick'])

person_age['Janick']
KeyError: 'Janick'
```
---
**Nesting dictionaries**
We also have the possibility to put one dictionary into another one and thus create a so-called nested dictionary. 
Let’s assume we want to store for each student their grades that they achieved in each subject: Math, Arts and Sports. Again, for each student we have three subjects (keys) and three grades (values). Thus, we can create a nested dictionary that looks as follow. 
```python
grades = {
	'Janick' : {
			'Math' : 4.3,
			'Arts' : 5.1,
			'Sports' : 5.6
		},
	'Marco' : {
			'Math' : 4.7,
			'Arts' : 4.3,
			'Sports' : 5.3
		},
	'Melanie' : {
			'Math' : 5.1,
			'Arts' : 4.6,
			'Sports' : 5.7
		},
	'Barbara' : {
			'Math' : 5.0,
			'Arts' : 3.9,
			'Sports' : 4.3
		}
}
```
We see that on the first level, we have a dictionary called `grades`, which has four entries / keys (the student names). Each key has a dictionary assigned that contains three entries: the subject names as keys and the corresponding grades as values. Because the parent dictionary `grades` contains four child dictionaries, we have a nested dictionary.
---
**Accessing a value in a nested dictionary**
If we want to access a specific value in a nested dictionary we have to guide our way through it. This means we have to start at the top by selecting the variable in which the dictionary is stored, then use the first bracket selector `[]` and provide a key to dive into the first dictionary, then the next bracket selector `[]` with key to dive into the second dictionary etc.
Let’s assume we want to access the grade of Melanie in the subject math (5.1). We can achieve this as follow.
```python
grades['Melanie']['Math']

5.1
```
We can see that we basically just chain the two selectors together. The first part of the selector `grades['Melanie']` gives us all grades for this student back
```python
'Melanie' : {
			'Math' : 5.1,
			'Arts' : 4.6,
			'Sports' : 5.7
		}
```
Within this dictionary we can select now key `'Math'` which yields us Melanie’s Math grade. To do so, we just appended `['Math']` to the existing selector which then becomes `grades['Melanie']['Math']`.
---
### Methods
---
[**`.items()`**](https://www.programiz.com/python-programming/methods/dictionary/items)
This method allows us to retrieve all key-value pairs in the dictionary. The method will return a list that contains all key-value pairs as separate tuples.
```python
person_age = {
	'janick' : 26,
	'marco' : 27,
	'melanie' : 19
}

person_age.items()
[('janick', 26), ('marco', 27), ('melanie', 19)] # -> list of tuples
```
---
[**`.keys()`**](https://www.programiz.com/python-programming/methods/dictionary/keys)
This method allows us to retrieve all keys in the dictionary. The method will return a list containing all keys.
```python
person_age = {
	'janick' : 26,
	'marco' : 27,
	'melanie' : 19
}

person_age.keys()
['janick', 'marco', 'melanie']
```
---
[**`.values()`**](https://www.programiz.com/python-programming/methods/dictionary/values)
This method allows us to retrieve all values in the dictionary. The method will return a list containing all values.
```python
person_age = {
	'janick' : 26,
	'marco' : 27,
	'melanie' : 19
}

person_age.values()
[26, 27, 19]
```
---
[**`.get(<< some dict key >>)`**](https://www.programiz.com/python-programming/methods/dictionary/get)
This method allows us to retrieve the value of a specific key. To achieve this we could also use a [bracket selector](/5b0832dbf9454eb1941b7632e68a9abb).
```python
person_age = {
	'janick' : 26,
	'marco' : 27,
	'melanie' : 19
}

person_age.get('marco')
26

# alternative solution
person_age['marco']
```
---
### Iterate through
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cb636ca7-6a88-40a5-a3e6-8be1748a262f/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVAC7MGC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDX%2Bw1X4g4nmROSQSXwGlpbCmbNLgnxcIlXR2ugN%2FqgFgIhAMhhImePsaiqw%2F%2FAchPPWvQLgWcE%2FhgFVs3o8DomMfhHKv8DCCcQABoMNjM3NDIzMTgzODA1Igygt%2BEiSEBRqqafFrkq3AN%2FeMr74gJgfGVW%2B%2B2BCwtGrHeDUM%2B9uezV0BFz0SuhDpJDGzEYZ2eBrSU7XyA6paRTRVNRkv3YE7kF5sZcAkCqU0O%2Bq%2FhZnpTip7geLItqEfnvNRx9iWSVOQWVZ4EoEaVIeTYFYJ4hJx1Gct8%2FxRcsv%2FE5g9IsNJlpiyI%2F8LFo2aRSNW8I5XpJRmvDUI6xPptquR155xrs%2BFFBT3ojv2ek0MzOstrpPeGP6CRKXF6IT1YyDV4Jk6W0nV3cvGDAQ5vC2bQ1bAiMkYhIS9Y7zInet9SXFD2rNXW26N72qsPdkyWIu%2BBIswix7H8M%2Fu2T8lC5gxayQ0B2GIyAoN2lO5fNOAZGQZHKFHmo3GhcHzx1M7nSECQ9OXcFn5gRlj3Sa%2FZuFSt4pUSfH1b1BftW2%2FlGQ0G6menyH1ds6GXrh1pAse%2FmXLNLcsp4YgUaGuxb5HcxpWc9YYUg%2FOUVUdQ8lSNoVzMbi8mWvDmpZvSUJ%2F0G45SOnor50b4DU9HuLB%2ByAiU8GpPnhMmARc01qNo%2FKlbiHTLqz%2Ff3gV1y2krxIgeY1r5GR0gsfVJTT9R2ivi3n5vl5ATaFcvZO4Lco3Mw332tn8A%2Bc0dBlm0BBwTi2yjEHesob5SKOFFOhfGCazCqzvfJBjqkAc2VGXkuRkXIGvtwHq876uhRa8CSVV%2B7rUl%2FSCdTXZJP9OTEwGQW4Ec2EGdj9%2B0zZbU1uLcXxhLu5ofxl1UdrN4k6JErYgj8Wuv%2FKs7j4n6x5vAqQzb1oR7UpwD1NmCArUTxhwJIDaVfAMfHTzxzJ0PxubfJIfWwjCubUQBTSWbk8dwpguetNqrz8RfdKooWAcFuRsNzOCFYsgx4Kx5jLYutSS8V&X-Amz-Signature=3766bae5449f65206b3a786bbd9761ad934f87d2ae5a25ac3312c82bcdb1de78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Motivation**
If we want to apply an operation to each key-value pair in a dictionary it is often required to iterate through the dictionary. This means we select each key-value pair one after the other in the dictionary, do some computation with it and may update the key-value pair. To do this, there are multiple possibilities that are explained below.
---
**Simple for-loop**
With this approach, Python goes through the dictionary and saves the key of the current key-value pair in the temporary loop-variable. We then use this variable to access the value. 
```python
person_age = { 'janick' : 26, 'marco' : 27, 'melanie' : 19 }

for key in person_age:
	print(f'{key}, {person_age[key]}')

janick, 26
marco, 27
melanie, 19
```
---
**For-loop with ****`.items()`**
With this approach, we need to define two temporary variables in the loop-header as the key and value of the current entry are stored in separate variables. Compared to the [first approach](/5b0832dbf9454eb1941b7632e68a9abb#4dfe7b9ebc8f449f910ae680cf8053be) with only one temporary variable, this brings the advantage that we don’t have to extract the value from the dictionary inside the loop-body as it is already stored in a temporary variable.
```python
person_age = {
	'Janick' : 25,
	'Marco' : 27,
	'Melanie' : 19,
	'Barabara' : 22
}

person_age.items()
[('Janick', 26), ('Marco', 27), ('Melanie', 19), ('Barbara', 22)]

for key, value in person_age.items():
	print(key)
	print(value)
	print('---')

### OUTPUT ###
Janick
25
---
Marco
27
---
Melanie
19
---
Barabara
22
---
```
From the code-snippet above we see first that when we apply the [`.items()`](/5b0832dbf9454eb1941b7632e68a9abb) method on the dictionary we get a list of tuples, where each tuple represents a key-value pair in the dictionary. Thus, to iterate over this list we can use now a for-loop by declaring two temporary variables `key` and `value` in which the key and the value of the current entry are being stored.
---
**Iterate over keys with ****`.keys()`**
If we only want to iterate over the key’s of a dictionary, we can make use of the [`.keys()`](/5b0832dbf9454eb1941b7632e68a9abb) method, which gives us back a list with all the keys in the dictionary. To iterate now through this list we can again use a for-loop.
```python
person_age = {
	'Janick' : 25,
	'Marco' : 27,
	'Melanie' : 19,
	'Barbara' : 22
}

person_age.keys()
['Janick', 'Marco', 'Melanie', 'Barbara']

for key in person_age.keys():
	print(key)
	print('---')

### OUTPUT ###
Janick
---
Marco
---
Melanie
---
Barbara
---
```
From the code-snippet above we see that the `.keys()` method first returns a list that contains four strings, i.e., all the keys in the dictionary (student names). As we know already we can iterate through a list using a simple for-loop, which returns us each key, i.e., student name, one after the other. As we can note, this approach is very [similar to the first one](/5b0832dbf9454eb1941b7632e68a9abb#4dfe7b9ebc8f449f910ae680cf8053be).
---
**Iterate over values with ****`.values()`**
Similar to the `.keys()` method, we can use the [`.values()`](/5b0832dbf9454eb1941b7632e68a9abb) method to do something with the values in a dictionary only.
```python
person_age = {
	'Janick' : 25,
	'Marco' : 27,
	'Melanie' : 19,
	'Barbara' : 22
}

person_age.values()
[25, 27, 19, 22] # list of integers

for value in person_age.values():
	print(value)
	print('---')

### OUTPUT ###
25
---
27
---
19
---
22
---
```
We can see that the `.values()` method itself returns a list that contains all values. We can use again a simple for-loop to iterate over this list and we get one value at a time.
---

---
## JSON
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ddddf0e3-e8b8-47b0-9e0c-2db6d492b7cd/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TPKRRGQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFB6yQ9%2FOL%2FKcA7m99nmQPZxsifuacYNQ87OzhMEoGIWAiEAwWfjTTJKRwC3kEytzzpcrcOWjaQE3ey68G1uAk4l984q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDAUFUcDOWMDrbdLc1yrcA%2FoxizovX2IYvemtzFrd3%2F%2FnIe2%2FBQIHsYzuZnqzFQ3GsiUe9b439ljtF%2F7IPNrPlPfsySpvjXim5UdIvHKtPPYfH8EEKhTdHHEp5oExur8ZLHj315gygT0g5EoN0UZRj76CozMhudcZbgjVJpNgwr945PYjSTt2MDXEtba4QJS2qqZ5SH5ox3cehkeI5l0S18DQTPtZdPzH7iSdHwaZpUHGMtcURtTj2iCcrLtEMH0LBu2VsEmVNS5ibMwAi8q%2FFasnSxkOe%2FSIv682w4lGo%2FpaYXPM8Z6ecYqwTWb8V49IIkcUxaRFRmKGKB3n4%2FfdIn8BIGqJ0NHRstwRC9exfgkgKECtm02oGrxsVHB2RJS28uv9%2FlJVJaLb7WP0Hkm6vW4%2Bzh4IHdT7MqmUfS1w8WK9PNzTdmWVSj8qhKeTAq1eSvjI7kKiuiHuI8QC1kmLTRL0q6w%2FjFmeEA4oK8cYHuD01yIe%2BfoagOeq0QJe0aoqEnjGldo0gKYxb%2BKJzh3x7aEBR3gijnVUd%2BrjaBBzckhv30Qe7lZB29T2GaGUckwTkQ%2B2bBNL1QTTuFk13DJM%2FHLsz%2Bb8WV%2B2uh5VDyjvuTWzI8Awk53vshPO4hAY9SY2%2F5E%2FVAy%2BLpQI8tCOMOLN98kGOqUBQy2TAwIuuVQf6Cxpcfbk%2BAP1VbaxIYl%2BYKzltaO%2F8sRfgERkrKvZybPCVgYJttws5xlICIxb%2BGd%2Bx3zniyq9%2FhHhqfuzoHEG1iESSF40rIqS0ke0jCIkN8GwrVM2nfbBOsYeIoAG%2FhjalzKwSWrgCXcLvk3qDAsGanXlgf38u%2FRZOG6%2BvaJvlLIa4Z7UsRC4afBODfgVIbx0B4Pv0xFikT5MQggF&X-Amz-Signature=8a363774f95c8b174b51f5333b5ed142496155a948ad1e02e17f4465c60d1d07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Definition**
JSON objects are strings that are used to represent objects in a structured format, that is known by the majority of programming languages and systems thus [facilitating data exchange](/d9dea9bec31b42b6aa208d00223b3fb5) between systems. A JSON object is of datatype **String** and its content is of datatype **Dictionary**. That’s why it makes more sense to name JSON objects simply JSON strings as they do not represent a separate datatype.
### Common operations
There are two main operations that we do with a JSON string.
- Converting a class object or a dictionary into a JSON string
- Creating a dictionary or a class object from a JSON string
> 💡 **When acting as the sender of data we convert things into JSON.
When acting as the receiver of data we create data from JSON objects.**
---
**Converting something into a JSON object using ****`.dumps()`**
Usually we don’t create JSON objects from scratch. The use case is often the following: We have a class object or a dictionary in Python that we want to send to a system running on another computer. Thus, we must convert this class object or dictionary to a JSON string, which we can do with the help of the [**JSON library**](https://docs.python.org/3/library/json.html). This process, converting something into a JSON object is called **dumping**.
Let’s assume we have the following dictionary that contains student data.
```python
student_marco = {
	'name' : 'Marco',
	'birthday' : '11.02.1998',
	'degree' : 'B.A.',
	'place' : 'Zurich'
}
```
We can now convert this dictionary to a JSON string using the `json.dumps() `method.
```python
import json

json_marco = json.dumps(student_marco)
```
We see that we must simply import the library and provide the dictionary as input and we have our beautifully formatted JSON string:
```python
print(json_marco)

'{
	"name": "Marco",
	"birthday": "11.02.1998",
	"degree": "B.A.",
	"place": "Zurich"
}'
```
This looks quite similar to the initial dictionary. However, the important difference is that `student_marco` is a dictionary and `json_marco` a string in a structured format. 
```python
type(student_marco)
dict

type(json_marco)
str
```
As `json_marco` is a string containing the same data as `student_marco` we can put now this string into the body of an HTTP request and send it to another system over an API. And because it is a string and almost all programming languages know what a string is, the target system won’t have any problems interpreting the data.
---
**Creating data from a JSON string using ****`.loads()`**
Let’s assume we are now the target system that receives the data about the student Marco, i.e., the json string `json_marco`. How can we now extract the name of the student (`'Marco'`) from this string? It would be much easier to convert it to a dictionary first, right? So how can we convert this string into a dictionary? We can use the `json.loads()` method.
```python
import json

data_marco = json.loads(json_marco)

type(data_marco)
dict
```
As we see, `data_marco` is now a dictionary again and we can access the value associated to the key `name` using the already known [bracket selector](/5b0832dbf9454eb1941b7632e68a9abb#d49c5db522dc4e0faae7a5c23178d161).
```python
data_marco['name']
'Marco'
```
---

---
## Type conversion  
---
**Motivation**
When dealing with datatypes conversion methods (check column Conversion method in [overview table](/5b0832dbf9454eb1941b7632e68a9abb#3684ce5c0e674ca5987a33acfe90011e)) are really useful as they allow us to convert data stored in a variable into another datatype. Of course, the data must be accepted by the target datatype (Valid conversion) otherwise the conversion fails (Invalid conversion).
---
**Valid conversion**
Let’s assume we have a variable `a = "15"`, which is a string and we want to convert this to an integer. To do so, we can simply use the `int()` conversion method.
```python
a = "15"
new_a = int(a)

type(new_a)
<class 'int'>

type(a)
<class 'str'>
```
We can see in the code snippet above that the conversion was successful. We used the `type()` method to check the datatype of the two variables.
---
**Invalid conversion**
However, when we want to convert `name = "Janick"` into an integer, i.e., into a number, this would of course fail because the data `"Janick"` is text and not a number. Therefore, it is important to make sure that before converting data into another type, that the data is compatible with the target datatype.
```python
name = "Janick"

int(name)
ValueError: invalid literal for int() with base 10: 'janick'
```
---

---
# Math calculations
---
## **Overview**
As you may already know, programming is extremely useful when it comes to calculating numbers quickly. In Python (and basically any other programming language) we can perform several types of math calculations:
| Operand | What | Example |
| --- | --- | --- |
| `+` | Addition | `5 + 2 = 7` |
| `-` | Subtraction | `9 - 3 = 6` |
| `/` | Division | `8 / 4 = 2` |
| `*` | Multiplication | `5 * 5 = 25` |
| `**` | Exponentiation | `3 ** 3 = 9` |
| `%` | Modulo | `9 % 5 = 4` |
| `//` | Floor division | `9 // 5 = 1` |
How the first five operands work is quite obvious, we learned this in primary school. So let’s have a closer look at the last two operands below.
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fe58f083-6826-437f-b3ab-f5d872052e06/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B2ZVO3A%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDDlSLaeI3LFuo5f3ixPvGPUmpp5rQmdGUrAJWr%2FisQMQIhAOnkMsFzSYhKYgTINRtITPE5wyQV33KHp68RGk4mkn4uKv8DCCcQABoMNjM3NDIzMTgzODA1Igx%2Fy84IiBmDl6lUMwQq3AOEdM6rFXE0iKT4XxB%2BBpNtQqmsOAcD%2BtOC4AbO7yYgcZwHT2X0IszMcWsWFIKP3UtpSI2ZDVmIqP46LGDwSbUzBeUeEXbeA14EHeqVPJh52eP7dgnqSCtM2gpg6c5a5e647BMJ%2BSo562l8dlJfM9U9kzICuaOUs8lIS70lO2eHTR8Hg1feJKnLW9j8bgV%2FPHjFXxh6ao%2BRGP8e5e3kPYMpOx3PYJJxWeBW%2BAZQfSpll%2BNsTFpyec8SsE28eHmYbTMdEGGbyRqgzHxesN9mltLEJ2hRErbYbSHtHNbySrHaObTp%2FgyOaz3saWIX7qUSHqpxNAhPbJUf%2F6mL7UTmf03tR7N2VxrbFdITJwfYBNPXEugG9Iq6qDPkGgbfWoT3kX0k9F8VMTav%2BZNQunY%2BCOGjweUyLFg%2BqsCZjykbhnxbpOiGW5mIvRyXJ5F%2BkApU1D1cNdHaJ7txLc%2Fmy8A8oLyfO03cfPW31tdl1g7%2BO8UXMEy0safY%2BiYjHDlQtbJfhynQMqWq%2FfpTA0tZBgFZNl73PWZfBKZjimqsZtJUy38uz5dqrwcDO38KRCc4xaFC%2BiEOygllRtBeZ360sMJLg0Z0N1kUsDhk%2FUzhejOR8OBEoyhPCZGLB2IpMewpnDDuzffJBjqkAW5QGXk3Q0CeYQY4uuDPJ22wrs12jovNGfWDVUWNch7P7y2kJ60YBjqjT6r4MZqcfPVlSXlD8v%2BElIL3TZVyaSEILyQkZYY7e1uR4AfWCoFEPkYYmdNW2%2BznNiQm%2FgDkJ%2B4KRpmTF1frJ%2BkRgewdccDYBdNJAkonWQYjMlnT9eu1Ga9I%2FHUNxpV4uYEXVzcXPIhxl%2FiqNoAgeLERH66Ir2OfWG8q&X-Amz-Signature=2ceb2571cec8c55cefd8aa47109df0405a6d591847ed1097f631c18fe08ebe0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## `%` modulo
---
**General**
The modulo operand divides a number `x` by `y` and returns the remainder produced by this division. In other words, modulo returns the difference between `x` and the next number that is dividable by `y`.
In short, the following happens if we do `x % y`:
- Is `x` dividable by `y` without remainder?
- <u>Yes</u>
- Return 0
- <u>No</u>
- Look for next number dividable by `y` without remainder
- Calculate `z`, the difference between `x` and the next number dividable by `y` without remainder
- Return `z`
---
Let’s assume `x = 5` and `y = 2` and apply modulo. 
```python
result = 5 % 2

print(result)
1
```
Let’s apply the schema that we learned before:
- Is `5` dividable by `2` without remainder?
- <u>~~Yes~~</u>
- <u>**No**</u>
- Look for next number dividable by `2` without remainder → **`4`**
- Calculate the difference between `5` and `4`** **→ **`1`**
- Return `1`
---
Let’s assume `x = 12` and `y = 6` and apply modulo. 
```python
result = 12 % 6

print(result)
0
```
- Is `12` dividable by `6` without remainder?
- <u>**Yes**</u>
- Return 0
- <u>~~No~~</u>
---
Let’s assume `x = 135` and `y = 13` and apply modulo. 
```python
result = 135 % 13

print(result)
5
```
- Is `135` dividable by `13` without remainder?
- <u>~~Yes~~</u>
- <u>**No**</u>
- Look for next number dividable by `13` without remainder → **`130`**
- Calculate the difference between `135` and `130`** **→ **`5`**
- Return `5`
---
**Using Modulo to check for odd or even number**
One cool use case of modulo is to use it in combination with a [logical statement](/5b0832dbf9454eb1941b7632e68a9abb#c5add58cfa894385ac4ad0010c5f64f2) to check whether a number is odd or even.
As we know from school, all even numbers are dividable by 2 without rest. If a number is dividable by another number without rest, modulo returns 0.
Thus, when we do `<<any even number>> % 2` we get **0** which is equal to **False**. 
Also we know that an odd not number is not dividable by 2. Thus, When we divide an odd number by 2 we always get a rest of 1. Thus, when we do `<<some odd number>> % 2` we get **1** which is equal to **True**. 
With this two modulo operations we can now define a conditional statement block which checks whether a number is even or odd. We have two options to do so.
<u>First option</u>
```python
if <<some number>> % 2: 
	# number is odd
else:
	# number is even
```
From the code snippet above we see that the code in the if-body is executed when the number is odd and the else body when the number is even.
This is because for odd numbers, `<<some number>> % 2` returns `1` which is equal to `True`.
<u>Second option</u> 
```python
if not <<some number>> % 2: 
	# number is even
else:
	# number is odd
```
From the code snippet above we see that when we add the `not` keyword, the whole thing gets inverted, meaning that the if-body is now executed when the number is even and the else-body when the number is odd.
> 💡 **It is important that we don’t learn these two constructs by heart bur rather put our focus on understanding what 0 and 1 signify and how the modulo operator works.**
---
## `//` floor division
---
**General**
Contrary to [modulo](/5b0832dbf9454eb1941b7632e68a9abb#f032049731b043d198898f95c31fce8c), the floor division does not only look for the next number dividable by `y` but also executes the division and returns its result. In short, the following happens if we do `x // y`:
- Is `x` dividable by `y` without remainder?
- <u>Yes</u>
- Divide `x` by `y` 
- Return result
- <u>No</u>
- Look for next number dividable by `y` without remainder
- Divide that number by `y`
- Return result
---
Let’s assume `x = 5` and `y = 2` and let’s apply floor division.
```python
result = 5 // 2

print(result)
2
```
Let’s apply the schema that we learned before:
- Is `5` dividable by `2` without remainder?
- <u>~~Yes~~</u>
- <u>**No**</u>
- Look for next number dividable by `2` without remainder → **`4`**
- Divide **`4`** by **`2`**
- Return result → `4 / 2 = `**`2`**
---
Let’s assume `x = 12` and `y = 6` and let’s apply floor division.
```python
result = 12 // 6

print(result)
2
```
- Is `12` dividable by `6` without remainder?
- <u>**Yes**</u>
- Divide `12` by `6`
- Return result → `12 / 6 = `**`2`**
- <u>~~No~~</u>
---
Let’s assume `x = 135` and `y = 13` and let’s apply floor division. 
```python
result = 135 // 13

print(result)
10
```
- Is `135` dividable by `13` without remainder?
- <u>~~Yes~~</u>
- <u>**No**</u>
- Look for next number dividable by `13` without remainder → **`130`**
- Divide `130` by `13`
- Return result → `130 / 13 = `**`10`**
---

---
# Logical statements
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6ba0389e-53be-4a79-8dd2-7cdfc6147d1f/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGXT6UHQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDfiLsWU3jaPlY0e72ZgdEp2lXY%2FeGjrIKL%2BJXFF%2BgYCwIhAJnNLqy7a7IcAVB2mlNOLylWmflet2BU8TvLKlxrRwegKv8DCCcQABoMNjM3NDIzMTgzODA1IgwS2%2BUxXNWhMx80J1Iq3AMWpmAo9XqjmOOYIGhgr8iwx0VvzNJ10hRCkNUVAyFJ0GqJgh7tUusKSbgeM7IsqGN1VyN1Y6EC6bP7oYLFraXK08jTZiuHDrbsmMZt16v73qmF%2BL6HayjISbb39Qmy7aFbw4al3tTVs7qoD3TKoPYUNtIUhMPwl7cRzHBKADK3GYkLcHE9V9ANQ80rk1MDLEA%2BQY7MdTP%2BVNblPUV4VDDh4rKFO36HZJyw%2FmTaQQGmwv0Vb%2FSElsdoSES2mw1b6koSu4bXEDJiMZjA8XQ8ldloYzfTfvXk0qZceqlE7ppnvHEy0uCYRdmlOFaISfUN13xvXN19BUkwCy%2B6a9cI%2Bc9%2FMcqMqPAqyJIoONTR2fHd8QgVlrOupcStiRezwNwgraX%2Fif1LEJIYNru6OejE2d0ThCRx1fa0mpLGESTEOo2VPD6QPueDkoNQrhHX1mBkMqYdc5vdtySsRGqvfDoQXMTfXb9CuMPjKvf6eLFpHIfw81Z0ksxfdNTAos3rvsY3m4VeUSW4qwHsBNBEU8xDqpS91p63sm%2FoNaydss2dCjD%2F%2F1t2WJD%2B%2Buv4%2FXa%2FIhQ4bex697wQRw3lbVTM%2BkOMr6WbhV1evS3IUB8%2BpsVie98iuUXq2qdeZv8ykG1ovzCEzvfJBjqkAel4dPKhPXVK60bpUUxZK3hfZoM495Y%2FcFiHNkPLbChbJJcx9m%2FlqxKKhA07AktsuO08BeZ3GlUDByePCEawkdTD64hKkealxw1LYU1Ce5cdHPlCF2eoHZFjyutDOFu5BCryNQODkV5z98tKT85JlQUKE38QP0o5s2X%2FxUSpvMt9AMBsuf%2BNHAHJfWruvjt0dkAnOjhSb6Lwb4r%2F0edb6ld0%2BqP5&X-Amz-Signature=50e4b1679999f667584b851d80e5914610425a9b8a2eb0bb1b41c264151533e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## **Motivation**
Logical statements allows us to steer the execution of our program code. This means we can define conditions under which certain things should be executed. For example, in the case of an online banking program, in the role of the bank we first need to check if the account holder has enough funds before we execute her transaction - otherwise we would be bankrupt very soon. Logical statements allow us to represent such conditions so the funds are transferred only if the client has enough money in the bank account.
---
## **if statement**
---
**General**
The `if` statement is pretty straightforward. It executes all code inside the statement only if the defined condition is met. It is important that the defined condition must be a boolean expression, i.e., evaluate to either True (1) or False (0). Let’s do an example. 
```python
x = 22
y = 45
z = 34

if x > y or z > x:
	print('Greetings from inside the if!')

# output
'Greetings from inside the if!'
```
From the code-snippet above we see that the string / greeting message is printed, i.e., the code inside the `if` statement is executed.
This is because the condition `x < y or z > x` evaluates to `True`. (→ [reference table](/5b0832dbf9454eb1941b7632e68a9abb#a18d68521412461d95fd8dffb4abfa46))
`x > y` → `22 > 45` → `False`
`z > x` → `34 > 22` → `True`
`False or True` → **`True`**

If we change the value of `z` to 21, the condition will yield `False`. (→ [reference table](/5b0832dbf9454eb1941b7632e68a9abb#a18d68521412461d95fd8dffb4abfa46))
`x < y` → `22 > 45` → `False`
`z > x` → `21 > 22` → `False`
`False or False` → **`False`**
```python
x = 22
y = 45
z = 21

if x > y or z > x:
	print('Greetings from inside the if!')

# no output
```
---
## **else statement**
---
**General**
What should Python do if the condition of the `if` statement does not yield `True`? Can we define alternative lines of code that should be executed instead? Yes, we can do that inside the `else` statement. So whenever the condition of the `if` statement does not yield `True`, Python looks for an associated `else` statement and executes this code. Thus, after the `else` keyword we don’t need to provide any condition. Let’s extend the example from before accordingly.
```python
x = 22
y = 45
z = 21

if x < y and z > x:
	print('Greetings from inside the if!')
else:
	print('Greetings from inside the else!')

# output
'Greetings from inside the else!'
```
We see now that although the condition after the `if` still evaluates to `False`, we have an output now as the code inside the `else` statement is executed.
---
## **elif statement**
---
**General**
In the previous examples, we have two different code blocks that can be executed, depending on whether the condition in the `if` statement evaluates to `True` or not.
However, sometimes this is not sufficient. Let’s assume we want to do multiple checks and only if all multiple checks have failed, then we want the `else` statement to be executed. `elif` allow us to add an arbitrary number of conditions. As we can see in the image below, each condition is checked until one yields `True`, then the code inside this `if` or `elif` statement is executed. If all boolean expressions associated to the `if` and `elif` statements evaluated to `False`, only then the code inside the `else` statement is executed.
![How `if`, `elif` and `else` work together](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5921e339-2dd5-43fb-ad1e-fc8a02622595/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI24FNZO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIDOl55OGoPilPNDqMoYx60Mb5aWCwHJZh3qIHEz4owchAiAKreFAowsgquUKwx6DWXdoy2td5WpDr93RtLPksONFzSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMgYWW3dMHOTBwVGZ3KtwDJ3najy%2FNQl7tQWLmJ5Ah85wtiubFaTCMEDioI2vL62zZ%2FtwYU0TTw%2FVdAbweLfFLPZNUdW1XEiVX8HbABnBSXZgAke%2F954w7yGjcxUyzX7TKLsOJr6CmTu8Tk%2BUu7MxJYYgsMZi9l9l%2BwBTccrp7NzqRM6EhIXr2GaO8%2BJ7Q360KFzCdB3Tp539fqoIumNXqVTvzIx2eQtORLEy074AMOAeQrrH4YvYf8h75UlLvW1VHiUy8w50IqZKOVmP5nxL%2BIK3seMp2vI%2B5IW4UrH14BwJNx%2BzpC7ugpwBoq6s6Gr9hUvHu2iBW%2FPd8rovHPESP%2BJxwuLFBJl1spt7R5NVqE77EdTIWK5nUybwhXC0AYpeRdMI9bSLXk8nCMjeBYaax18MUmuwV44Dty5i89aHcAeFtLqGRPjioNgsdiNTMBM9JnQ9V2E8P3%2BNqdnGaT3E0oLr6unGqNxYj4mx2Jl8LZsKjwf9g7tNlru%2BZlEAGZv5l2XjspQHMzLzU0CVQKXBSQHQ90MFZ70sR0XhaJ9kjjXQWQlz4OsMKfRlVUo3dL6M16o8DpkPOSDw8D7BSV9DJJJo3LGgnarBMfhDxNARBkWVnZurR2fJi7aLZObqV0SQLO%2FuBnkX18ulC3BkwxM73yQY6pgGRfI%2FPzWc47OoOqyPyLRx7vxUv0P0M68EDggxFOLwpjEu6C4ES67HWCjy60U8x4EKdR36N80e6QpgDnT0EGg2RG%2FUZT9q1g%2BGk19nHrM9FiCaVC%2FZl7yekW1YQF92peN6zXixe18kSsqC4Vrbqnmi94w1EdEONnTcxt2JT8n2ofZiNG84sfvK9jmL04JJnv%2FgBr9OVPYbvWTfz2KiGH8eVMtwbZnmC&X-Amz-Signature=7654bba051b75d80998510a03c9e0e5ca910ded1a1e1d8556c2b66c07fcf9ac0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
x = 22
y = 19
z = 19

if x < y or z > x:
	print('Greetings from inside the if!')
elif x == y:
	print('Greetings from the first elif!')
elif y <= x and y == z:
	print('Greetings from the second elif!')
else:
	print('Greetings from inside the else!')

# output
'Greetings from the second elif!'
```
As we can see in the code snippet above, we receive a greeting message from the second `elif` statement.
This is because of two reasons:
1. The condition of the `if` statement and the first `elif` statement evaluates to `False`. Thus, Python reaches the second `elif` statement and checks its condition
1. The condition of the second `elif` statement evaluates to `True`. (→ [reference table](/5b0832dbf9454eb1941b7632e68a9abb#736fb47f961941e9abf2a7f39e6812b4))
`y <= x` → `19 <= 22` → `True`
`y == z` → `19 > 19` → `True`
`True and True` → **`True`**

> 💡 **Remember that the `else` statement is only executed if the `if` statement did not evaluate to `True` and all the `elif` statements did not evaluate to `True` either. As soon as the `if` or one of the `elif` statements evaluated to `True`, Python ignores the `else` statement.**
---

---
# Functions
## Motivation
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0bb2f0a7-db6f-457c-9e29-9fa4d20a1a7a/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BCVGMTK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDVa9TZ3%2BFeRcvJ5IsJ%2B7uN8%2FG4xMBx%2FNEEYRF3ClY8hwIgNx4mwljyUmNIxiIyJy6KX6XC7qIzdhKNuDjYnOs4BXsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNVT7lUX8kZb%2FKMSqSrcA6%2BEEartnxAYesUUiFT8Bvy5pgji%2F4GX9BUyGTCgZO6IBGeEy0KUHMD6JXBlsBEEvxvBPdJNC4YLNBITTMGYY%2BkCe%2BRUqvjmz%2FZFTg8WLY3Dqxuvru6f0F6Tp3aGj4nGQ7bY6oi3BNXJD%2BPds9GI2fCtXzIpLFNhmr60tELtjQYdn1E5TQqjxfpQY8vlRFZfCEMi04hDGG2i7FRw4%2B28NEP%2BfklFqmzqq8y5Gof6nj37x%2B4YNW50yc%2Bi89cnB4pU1KP%2FSlETAdIL1%2F71Qvef6W7akDU8Xf3iJtCsvXC9PZl%2B6hOKLTBzYtq36%2BlZSottDyiKRdDguBCEAcrgwqqBqChsQJ47WtVlFgPTL%2BzmyFZRukooZ3LISUINptpbEDum0YdyyATpnBq1UY3vrGuhyiYlN5iP42jjPANXgyQJVZczZvRiUJpKgOYpsbIWDjdRop89FKIHpDKEDqnmKm8mAXLwLN5c4a%2FsJO4bwhceLAMeaIxoT%2BzoKRmcZMJ1O5gFw9mrl5sIuEKlQmqW7r8Qn53vee670H1eyEzj8QbjI%2B3EsI0YQKk2WmMrQDD%2B0PLOXz2r%2FaGbHoa1UfMe4FBP%2FAjXfaI1IQKBUtktxgU%2FGJ5h93m4cJweZBi3eAEIMObN98kGOqUBkwO14hgsLLisjGNkQrhcAPHxncaoy7EUS4Cn9mzYf9ELSECo1ItghsNFARxRGXmaaE9RcqzqO0FcuSkdWCHY6ibdKTN2KO9vZyErlBY%2BYm5fCigE7JKivF6m%2FDTUHkYmgTIEuaXZuQKPcja9yYACMCZKeJMv9YipdUPiltixWCU%2Fknn6R9OBszNTUllahgw%2BaCKMNBa%2BVBnYkMa3g8J8g%2BCq5JV6&X-Amz-Signature=5e30e713867237d3014544aab88759864ae9037a4db03de4366c911a13e9bf51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Why we use functions**
The motivation for functions is similar as for [loops](/5b0832dbf9454eb1941b7632e68a9abb#a0ed22190a314589a93842ccc98136c7): Write a piece of code one single time and then re-use it again and again. Functions are the perfect tool to achieve that, we can implement a certain operation one time and then execute this operation (potentially) from anywhere in our program code and whenever we want.
Let’s assume that we have implemented a student registration system. Whenever a new student signs up at University we want to calculate the student’s age in years and store it in the database. For this scenario it makes sense to implement a function, because:
- We have an operation that is the same for all students (calculate the age in years)
- We are going to use this operation multiple times (whenever a new students signs up)
Functions at their core are very similar to this [kitchen machine](https://www.galaxus.ch/de/s2/product/zyliss-trommelreibe-set-kuechenreibe-5940319?gclid=CjwKCAjwmJeYBhAwEiwAXlg0AUwD6JZuBow-yknxLXaKJDXHl6rW8XmE3sMjwdurCRBPsNU1gmL2sRoCQPgQAvD_BwE&gclsrc=aw.ds):
![Function - kitchen machine analogy](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2402d405-b841-4526-95bc-1296ac572513/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BCVGMTK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDVa9TZ3%2BFeRcvJ5IsJ%2B7uN8%2FG4xMBx%2FNEEYRF3ClY8hwIgNx4mwljyUmNIxiIyJy6KX6XC7qIzdhKNuDjYnOs4BXsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNVT7lUX8kZb%2FKMSqSrcA6%2BEEartnxAYesUUiFT8Bvy5pgji%2F4GX9BUyGTCgZO6IBGeEy0KUHMD6JXBlsBEEvxvBPdJNC4YLNBITTMGYY%2BkCe%2BRUqvjmz%2FZFTg8WLY3Dqxuvru6f0F6Tp3aGj4nGQ7bY6oi3BNXJD%2BPds9GI2fCtXzIpLFNhmr60tELtjQYdn1E5TQqjxfpQY8vlRFZfCEMi04hDGG2i7FRw4%2B28NEP%2BfklFqmzqq8y5Gof6nj37x%2B4YNW50yc%2Bi89cnB4pU1KP%2FSlETAdIL1%2F71Qvef6W7akDU8Xf3iJtCsvXC9PZl%2B6hOKLTBzYtq36%2BlZSottDyiKRdDguBCEAcrgwqqBqChsQJ47WtVlFgPTL%2BzmyFZRukooZ3LISUINptpbEDum0YdyyATpnBq1UY3vrGuhyiYlN5iP42jjPANXgyQJVZczZvRiUJpKgOYpsbIWDjdRop89FKIHpDKEDqnmKm8mAXLwLN5c4a%2FsJO4bwhceLAMeaIxoT%2BzoKRmcZMJ1O5gFw9mrl5sIuEKlQmqW7r8Qn53vee670H1eyEzj8QbjI%2B3EsI0YQKk2WmMrQDD%2B0PLOXz2r%2FaGbHoa1UfMe4FBP%2FAjXfaI1IQKBUtktxgU%2FGJ5h93m4cJweZBi3eAEIMObN98kGOqUBkwO14hgsLLisjGNkQrhcAPHxncaoy7EUS4Cn9mzYf9ELSECo1ItghsNFARxRGXmaaE9RcqzqO0FcuSkdWCHY6ibdKTN2KO9vZyErlBY%2BYm5fCigE7JKivF6m%2FDTUHkYmgTIEuaXZuQKPcja9yYACMCZKeJMv9YipdUPiltixWCU%2Fknn6R9OBszNTUllahgw%2BaCKMNBa%2BVBnYkMa3g8J8g%2BCq5JV6&X-Amz-Signature=76c41d1685d023b9a25128530f21eef9fc94a4478fbf926924e83266b4529106&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We throw something into the function (**Input** → student birthday),
the function processes this input (**Operation** → calculate age in days)
and returns the thing coming out of this operation (**Output** → age in years).
So a function always consists of three elements: 1️⃣ **Input** 2️⃣ **Operation** 3️⃣ **Output**
---
**Structure of a function**
Let’s look at how a function to calculate the age in years of a student could look like:
```python
def calculate_age(birthday):

	date_today = datetime.combine(date.today(), datetime.min.time())
  bithday = datetime.strptime(birthday, "%Y-%m-%d")
		
	student_age = int(round(abs(date_today - birthday).days / 365 - 1, 0))

  return student_age
```
Let’s first look at the structure of this function which consists of:
<details>
<summary>**Header**</summary>

The **Header** is `def calculate_age(birthday):`
- `def` tells Python that a function header is coming
- `calculate_age` is the function’s name, by calling this name we can execute the function form anywhere
- `(birthday)` is the **Input** we give to the function, like the vegetable we put into the kitchen machine. We can have n number of inputs, however, in this scenario we only have one.
</details>
<details>
<summary>**Body**</summary>

The **Body** is the code inside the function, i.e., the **Operation**. In our scenario the function-body consists of the three code lines that calculate the age of the student.
```python
date_today = datetime.combine(date.today(), datetime.min.time())
bithday = datetime.strptime(birthday, "%Y-%m-%d")
student_age = int(round(abs(date_today - birthday).days / 365 - 1, 0))
```
</details>
<details>
<summary>**Return statement**</summary>

The **return statement** defines the **Output** of the function, i.e., what goes back to the function-caller. We can detect the return statement by the **`return`** keyword. Thus, the return statement in our function is **`return`**` student_age` which gives back the student’s age to the function-caller.
</details>

> 💡 **The function header defines the function’s name and **Input**, the function body implements the **Operation** and the return statement gives back the function’s **Output** to the caller.**
---
**Call and execute a function **
Now after having defined our function, how can we call and execute it?
As already mentioned, we need to call a function by its name just as you call your friend by his or her name as well. 
The name of our function is `calculate_age`.
However, we can not execute the function by writing `calculate_age()`, because in the function header we define that we must provide `birthday` as input. More precisely, `birthday` must be a string that contains a value that can be converted to a date.
Considering the function name and the required input we can call and thus execute the function as follow:
```python
student_age = calculate_age("1997-2-25")

student_age
25
```
From the code above we see that the function call worked perfectly fine. Our function calculated the age of the student and gave us back the age in years (25).
---
## Special cases
---
**Function without return statement**
A function does not have to give back an output necessarily. The scenario can also occur in which we want throw something over the garden shed that we no longer need, without expecting anything in return. To account for this scenario, we can simply remove the [return statement](/5b0832dbf9454eb1941b7632e68a9abb#d1ec78fe5ded4db6913e692e46f5f082).
Let’s assume we extend our function def `calculate_age` so that it prints the student’s age to the console from **within** the function and thus the return statement becomes obsolete and we can remove it.
```python
from datetime import datetime, date

def calculate_age(date1):

  date1 = datetime.strptime(date1, "%Y-%m-%d").date()
  student_age = int(round(abs(date.today() - date1).days / 365 - 1, 0))
  
  print('Your age is {}'.format(student_age))
```
We can call the function just as we did before. However, now we don’t need to save the output of the function in a variable and print it to the console as this is done inside the function already.
```python
calculate_age("1997-2-25")

25
```
But does the function `calculate_age` not return anything? Let’s check by saving the output of the function in a new variable `output` anyway.
```python
output = calculate_age("1997-2-25")

output
None
```
We can see that in variable `output` the value `None` is saved. Thus, although there is no `return` keyword defined in the function it still returns a value, namely `None`.
> 💡 **A function **always** returns **something**. Either the value defined after the `return` keyword (return statement) or the value `None` in case no return statement is present in the function body.**
---
**Function with optional parameters**
One important concept related to functions are required and optional parameters.
If a parameter is required we must pass a value when calling the function necessarily. Otherwise, an error (TypeError) will be thrown. In the previous example, birthday is a required parameter. Thus, if we call the `calculate_age` function without passing a value for this parameter we receive an error. 
```python
calculate_age()

TypeError: calculate_age() missing 1 required positional argument: 'birthday'
```
Optional parameters are, well, optional. The idea is that we either can or cannot provide a value for optional parameters and the function would still work either way. Let’s assume we want to extend the `calculate_age` function so that it can do two things:
1. Calculate an age when a date of birth (one date) was provided
1. Calculate the age difference in years when two date of births (two dates) were provided
The function as it is currently implemented covers already the first point. So we need to extend it so it covers the second requirement as well. 
```python
from datetime import datetime, date

def calculate_age(date1, date2=date.today()):

  date1 = datetime.strptime(date1, "%Y-%m-%d").date()

  if date2 != date.today():
    date2 = datetime.strptime(date2, "%Y-%m-%d").date()
    age_difference = round((date2 - date1).days / 365, 2)
    print('The age difference is {} years'.format(age_difference))
  else:
    student_age = int(round(abs(date2 - date1).days / 365 - 1, 0))
    print('Your age is {}'.format(student_age))
```
The extended function seems a bit complicated, but we are actually not interested what is happening inside the function, but rather in the function header. Let’s compare the new header with the previous one:
- **Before:** `def calculate_age(birthday):`
- **Now:** `def calculate_age(birthday1, `**`birthday2=date.date.today()`**`):`
We see that we have added an additional parameter `date2`. Thus, we have now one required parameter `date1` and one optional parameter `date2`.
So when we only provide one value as argument, then the current age is calculated, just as before. When we provide two values as arguments, then the difference between the two dates is calculated and returned.
This is possible thanks to the optional parameter. And here is how it works:
When we provide only one value, Python stores this value in variable `date1` and stores the value `date.today()` (today’s date) in the variable `date2` autonomously. Now, Python can calculate the current age, i.e., the difference between today’s date and the birthday. 
As soon as we provide two values, the first one is still stored in `date1` and the second one in `date2`. Thus, the code after the `=` sign, `date.today()`, is ignored and Python can calculate the difference between the birthday stored in `date2` and the birthday stored in `date1`.
So let’s check if it is working as expected, meaning that we can call the function with one as well as two parameters / birthdays.
```python
# calling with one argument
calculate_age('1997-02-25')
'Your age is 25'

# calling with two arguments
calculate_age('1997-02-25', '2001-05-07')
'The age difference is 4.2 years'
```
As we can see in the above code snippet, our function is working just fine. This is exactly the beauty of optional parameters: They give us flexibility and also the power to do two different things within the same function.
> 💡 **Optional parameters can be identified by the `=` sign in the function header after the variable name. If no value is provided for optional parameters, Python assigns a default value to these parameters by executing the code that follows the `=` sign.**
> 💡 **Only if a parameter is optional we don’t have to necessarily provide a value when calling the function. If a parameter is not optional, i.e., required, and no value is provided then the function will fail and an error is thrown.**
---
**Positional and keyword arguments**
**Positional Arguments** are the ones that need to be passed to functions in correct positional order.
For every position there is a defined argument. The order matters, hence the name Positional Arguments.
```python
def function(arg1, arg2):
    return arg1 + arg2

# Example of call with positional arguments:
function(3, 2) # Output: 5
```
In the example above, `3` is positionally mapped to `arg1` and `2` is mapped to `arg2`.
**Keyword arguments** are arguments that are identified by the parameter name when they are passed to the function.
This means that the order does not matter as long as we specify the keyword arguments.
```python
def function(arg1, arg2):
    return arg1 + arg2

# Example of call with keyword arguments:
function(arg2=2, arg1=3)  # Output: 5
```
In this case, it does not matter in which order `arg1` and `arg2` were given. As long as we specify their names, Python is able to match the values `3` and `2` to `arg1` and `arg2` respectively.
Python allows function calls that use <u>**both**</u> positional and keyword arguments. In such cases, positional arguments need to come <u>**before**</u> keyword arguments.
```python
def function(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

# Example of combined call:
function(3, arg3=1, arg2=2)  # Output: 6
```
In this case, the positional argument `3` is mapping to `arg1`, whereas `arg2` and `arg3` are keyword arguments.
Do note that the positional arguments <u>**must always precede**</u> the keyword arguments in the function call. If this order is changed, Python raises a syntax error.
```python
function(arg3=1, 3, arg2=2) 
```
The code above will throw an error as the positional argument `3` follows the keyword argument `arg3=1`
---
**Recursive functions**
We can not only call functions from outside but also from within the very same function. In this case the function calls itself. Whenever we have such a case, a function calling itself, we call this a **recursive** function.
There are two very typical school-book scenarios that are specially suitable for using recursive functions:
<details>
<summary>[**Factorial of product**](https://corporatefinanceinstitute.com/resources/knowledge/other/factorial/)</summary>

The factorial notation for a given number `n` is `n!`. Let’s assume that we have `n=5` and thus `5!`.  The factorial of product is now calculated as follow:
5 * 4 * 3 * 2 * 1 = 120
We can see that we follow a specific rule here. We take the number `n`, decrease it by 1, multiply again, decrease it by 1, multiply again, …, until the number is equal to 1 - then we stop. So `n=1` is our stop condition.
The stop condition is very important in the context of recursive functions. If we don’t have a stop condition, then the function will run forever until the execution memory crushed down eventually.
We can implement the calculation of the Factorial of a product (`n!`) with the function below:
```python
x = factorial(5)

def factorial(n)
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)
```
We can see that in the body of the if statement we have our stop condition defined. and inside the else statement we have a recursive function call, because we call ourselves → we are already inside the `def factorial(n)` function and we call the `def factorial(n)` function again.
Check the video and the image below to learn how the function calculates `5!` step-by-step.
![Step-by-step overview about what is happening inside the `def factorial(n)` function](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/aa704f3c-732f-4541-86bf-cbd87ca029fa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZFOU6MA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGutGdv%2BxftcsurOvK6tRx5SmB42jhYOKjcESSd%2BuKMDAiBc%2Fwfv3N4mowLxhq%2B4PKVm%2FK9CNHcSPkz1G%2B7yQyuDNCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMTI9XLYrpXYwRhNZuKtwDxIM2w8mWRrLSU%2FOCP3aPHG6wKFMOLBUk0njrg48ACC9HlYqcpA407UdS95gIqb32Ol%2Fe2Q6xw4E2kRPaWJ3eE7jFj5gAtE%2BhoTxopp3MPIvxFhYOKHpt8cQfaOad17UVj%2BGSQ2GD7JmSd3bj%2FZGbWT4bNQBez5e5L%2FyO%2FpJE%2FVjUTm8UgZxp%2BAGzay7J%2BbThcdk1pr2niFak8E3PNCcxH62vpkBaMzD6beUHMDRxPccQxxORfdqaCP0Z3ba7WbMBp1mvqgbtzpT%2BQ%2BLr%2FCnlle6rntATdq%2FMss%2FkbeByLq1K%2BWEst4TAxxj%2BhC7otLh%2FxlR0kTDgPVN3ieJPZQ637igW9mQspwNNoJtbYDcaVYK08NUR4eqP6k%2FlBO%2BG8Bvwi6Xl%2FlTrX45%2FIOYR2BfDDowy%2B7yPsnajCoW32cixRyRXjcGuPZLAaQwoqzafptHa4ePzkCbRGMmU0Mm6VdYVyCAgP0r%2F%2BET24IbbkYyNgPp77G4faeDYoEOvd8WY%2BTDQyGTG2wYqlWfrOcXDZvcwaTi4Gi1gN9XlrLur69QVEnOv%2FxEmRmVzvldoyNMT%2BJCDf5SaTvB098sKsxWSGcWcqCshJM5VIoDBGKprQOS7DIdQrokZtFPguGjrO88wgs73yQY6pgHXf0k%2FCs5yZICdbXhHQWn4mStaLbPLz0%2Bmpg4Rx7zSu8N%2B74do8Cz5DyzkoZnU3odB%2FJ4MhV5M0LiX%2B2z8WQsW8tTbhpLdhNjX6oZGyRzqM0PRcx0V2fqT%2BqS89hRYVMbpdXkgWev0GxqPV%2Bo3IV%2BhMmPKg%2Fwo0v4kWXZnzdzfhzWoeuDKPCGbQU4Nd%2FciO%2F6%2FGFfjyVWxbH8iEo0NPAHWkY92U7w4&X-Amz-Signature=cc4fd7cda6409e420b45b0f12093164f60ce962f7f6ef79bb3496a728b1c6747&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6815e7bd-e61e-493d-b75b-b9e04ed31ca9/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMYGCQNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGtR7TwsrwmQnVMxnAWcwIlOF4Nxsf95TL1kdyi%2Brj4zAiBtSxNMc7LSyNrS1rHf9MzPgdIIhK4cQJb647e7wa%2FCNyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMUyvRXdlY2Vp9hKGDKtwDkFux3DpA9FAC4VekrL8OQZtv0MEI7ygyqdxcKNXW65CL5m7dTtrwF9JqN3c63KEoTPLy%2FKdlPWArglDUA%2F0XODdbdbg6o4ewGy9bMzSiufo9CdRKq3fQSvGHs5iDJaTEZ0u5r3MVGyG3e3G86n8doTGuwdN5%2FuX7xE%2B4EFv483HbbjTOYg%2FwugwCalJYoje9CRRrTBeOOZIjaWHwEwwbq8k6h9DLgu3xQCQQKUV7EKh4Nlb%2FMM0U%2FAMtB19Wt0R8yRON15NLIOwFABm%2B57Ya8TXcllL3XA%2BW6%2FCBR%2BmKUZuOAvrGfft8D9sEc3WIMnU38sFioH%2F9Qk2dhx4pRqSWRKZUJfLmII99MfLdYQKb1wG8ccMyJmyiPtw%2F1cTLWrnx4nBS5htdlDpdkxVY4Hg6cQRFUoE5l4EVxY4Q78%2F0%2BoJVKI3B0Aom3cee4llIRJQ5Wk7Y%2Bus4nJI%2B5QUDhDDoQ4iTcazC8GO92jpQxOGxPCME04qQTFqNvkojqApry4Yid1ZOMiUuhUrnKOdLn5IslaQNoVQqQVihUGag9fMog%2B944ZrSlBfVUaO0M2n3KDCRk3mUvyleVFxkDxdfzCqLWOpPuzVEZ6XnNT2z%2BtRNiVdB6SUv%2FEI7dsAqQmcwx873yQY6pgFE8BtHz%2BwdteKIfOGjhG6LEQO27QkWso7QTOeEOAkNqkAJK7wVa3baJSCOlsLfrQf74%2FTodTPxsmqVqkZiJ9%2FOo0nryn581nWTUO0QZHcwPsmvIay8TU5D90uWyjW36Y4IYrJE6CwfSKtRHpLs01o3Foa2GS%2FLL8v5dBokDK%2F28eqyW3vIS9MMQADua2e0QRLYBzVoESTcXicdc3%2BUU%2FQW12By5Bz7&X-Amz-Signature=e0d68ec63230af45478a4d6216f2f66459b2608c777f58c0ff8440485176c1fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
<details>
<summary>[**Fibonacci sequence**](https://www.cuemath.com/algebra/fibonacci-numbers/)</summary>

The Fibonacci sequence contains numbers that can be calculated as the sum of the previous two numbers. The first ten Fibonacci numbers can be depicted from the table below.
| F0 | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 |
It is a very famous scenario to implement a recursive function to figure out the n-th Fibonacci number. For example, if we forgot what was the 10th Fibonacci number, we could simply execute `fibonacci(9)` and the function would return the value 34.
Below is a recursive function that is able to do that.
```python
def fibonacci(n):
   
    if n < 0:
        print("Incorrect input")
 
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
```
We can see that this function again has some stop conditions. In the case that n is negative, equal to 0, 1 or 2 no more recursive function call is done. These stop conditions are important as we would otherwise end up in an endless loop of recursive function calls until the execution memory is full.
In the last line of the function a recursive function call happens, in fact even two of them. The image and video below explain step-by-step how this function figures out the value of the n-th fibonacci number.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ffb68260-2781-46b4-b981-2d78c62603cc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSU5I4TK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCHJ7TsnqBLsMhtkzEXuR2LFRz8%2BnUb3X0DxqLEO%2FuunAIhAPWthtpAP12Wd2%2FSaqi4T7N25rAZ3WHLuTXIUy%2FF5IK9Kv8DCCcQABoMNjM3NDIzMTgzODA1IgwrsllGd4NgIRicMSoq3AN8%2Fk1HR4ibvazj0V1b5P2l15KwvAhuJHOwbHjR2BqgmkQw0wbRO9puM9J8T0884Z%2B0dm7quAB1rB00MmxgLt6MyDpmJnNrI761zezXpuKj6UJrkk20SkszfxxAcQJfH%2FDSXHQSZ6sLCO6fz8U414cN6bSqmiP60Y4vzWTo9C9Rtw5%2FZtMRjAGpmU1GNNlveYtA6nJNJNwhzoXbIgRLwLyxtuUr2g7CFEi5JX9l%2FIGf3lDopKBMsOWl%2BU9OT6G7bWHKfeaFGMwfmcHvbx36TUM8U64NX0QRBr0QX0Ey0fpJRzkiLMIG43VgRT613ofS7XvCHyTuot0Fi1byPxIV39NkV7R2yhcP%2FmhCMcacIti%2BERFNQfR92%2BKWgVEGOAlejM4OrMvU%2Bft7R1PrjYodqb5HO0UMnFMIkI4i90b%2FK3Oxa7bMV%2FR2YUlOGUH1bQmbTOxIQ1CpZK0JAfcTPpotfNe1oNWffOEAFj4h2EOAWkV0Pr6Ttu0ymXonBcTWwu1BYwlY7q2A11x7PpB11ndOG4n5z1MGIirlBCpiffy4pEv0rhIz4ZXhh4q7Du%2B5GoR%2F7QgVTxlKkw3r5VKWPEyAroTz%2F%2F6FJbXyaA7bOeu1epurCAX%2F00Jfdb1tCQLxOjDCzvfJBjqkAZ6Z94LggzmC3ioF%2Bm3rT37%2F%2FkaU7OuOqN5QZRl%2F1Frzo797%2FquqtAxfAmWtdqAUB9jdFhirLCLwX5AKB%2FStGFVcmHBxw1j8pgJYNRxP6jBfziQYhgrcLw31Zfn9rvgkewtg0%2B2udDAQ968RteqUiaxGJwZESkZFlLc01ADIOmL7xDaD76o%2FwEJiO%2FriemmKb3JQtLj2zV4viuKY5kflaTNM%2FGAO&X-Amz-Signature=aff74f721b75a5980bcbc5edb9c65c925effbe570265e0e0d35c5a4e2eb6add9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/518d0318-9660-4fdb-8e6e-fa068f19aded/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G2SXPBS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEF%2BV5fgQsx1HdCcotH067SPU25qSI7hu5%2Bsidko%2BWW3AiEA%2Bo9Hn4nz0MKvV0m7TENMXxdyg9hg7V6G9XXhClPqG%2BIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBEmpOmS8onl9l2KoircAxgRrrA9Kpif83iunk%2B6mztI15gKMNGth2txWjYxxS6a5AQuuFcOgVQaQEJ2NkEEb%2BnkXF3f0tyOW0mP2UubVxOrRzrx5S1lqSV6CdWWp09VoQA3qNDHzZREBJ10OvSfx8qdOi%2BuXqe6zockDR2RGKfO9rOGiWz%2FfmO4omXT%2Bk42%2FY2zULCMsnZRPt0c8rU11p%2Fk8oa2zoyrjUi6f76srW1RXNod5gm%2F%2FUSUMRD6dJN1vKlKcvHnyFMSYUYyjlpzSL1Z6Lw3uTC7ezVU3rXke41IDzj%2FqFRFQISYDWSJBjZg0h2Xi9rGoni5TapJ3Xaap625bhAHmbI7yfDefFuc3Kl8vMFlL4a2VrCq8ZZc9b6gYVrEDTyAGt9e2INhMoWaJVvEdZTkOSMPL4BWh2n48gC1yYBU166yR6g80s1PXQHPADMtF9qfStxgv0aBXcSm%2BW1gndor5rXh1TbWa2RazWleXLdWjUUPdoTouek2yDwNuRUehSSPzQvpB94L9ouD41atoFM7jDmYu83q5uSay9BQ%2B%2BB%2BDvf0GETO9N8dLofzFUkBaWTfMkAUrabIR6oKZB8Ku2NCtPI84YXBIQkQKgX%2FVa3WftDycfZeMEQAGez69p5i8%2FcrbpwK7wvTMLDO98kGOqUBD2Niaz4eSs93DFFmxh5DJPq7lGCnfCXVnFzu4C0v%2FIblJGmSL3wj7eKD7aVnmgWOEvReDL%2FtSdXCjPBS9dbulmYjy0NmiPsjI%2BSdnICtVnl77%2F2Vnzcl2xJzsRdsJsJYjqSWouuYIaTxUljOpYKm%2F%2FrF0GdOl7lIXtKmw9eTMCpaT08%2BJwBnxluqNjVSzbzXgehgXTTHLkrD2ykGXtmnR0iY5bqC&X-Amz-Signature=66d992a747e0e3e67ccaeddebda47af542388647f6699098990bce6c9a7ee916&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
## Lambda functions
---
**Motivation**
In some cases, we only need to execute a function once. For example, if we want to remove all rows from a [Pandas DataFrame](/1867045b058343e1a66b677961515907) that contain invalid data, then we only do this once. Once a row has been deleted it can not be deleted again. However, we don’t want to write the code that checks for invalid values and removes the row multiple times, i.e., for each row separately. Thus, we need something between no function (because we want to execute the code only one time) and regular function (we want to execute the same piece of code for each row). And this is where so-called anonymous / lambda functions come in to play.
Very often lambda functions are used in combination with a `map()` `reduce()` `filter()` or [`pd.apply()`](/d40ced96935848ad8368835ece679a23) function. The first three are explained below in greater detail.
| Function | What |
| --- | --- |
| `map()` | Modifies all elements in an iterable by executing the specified function for each element. |
| `filter()` | Filters the elements in an iterable by excluding those for which the function evaluates to False. |
| `reduce()` | Shrinks an iterable down to one element by taking all elements together according to the specified function. |
### `m`**`ap()`**
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/02baae58-b884-4abe-b0bd-4fd2374eb9bc/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WZRUUT5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJFMEMCIFrfVfgKjHxq%2FoSa6kpV%2BS6bMfpYZlvVuILRO%2BqE2WEvAh9gJHwoOnxe6PbhgO1KlIye69%2FQkIdGHPFIdeXRzzuoKv8DCCcQABoMNjM3NDIzMTgzODA1IgwrK4xrYAi11Vch5Ecq3APhwEaFmdPlCJD5NvKEkkJBC%2FDyS%2F3DlD0TWI%2FvM7MYd8PUicHhxzGk8VqE8w7n2L9TYtNJahveHAtV04ag1FeQTdzIpi%2FY1GYu8CdJtakhQYrT0wU%2FUwugHDPsaQVGRz9igyh5hjZbSbMM%2FavqWPvYQZlzvV%2B57glykVuM43il0H%2FX87Zz75vEQqZrhThiEZSQQzR0vzA9YSME4DpgqOUI7Y2agJHtOYwgp4qLMOCrGFyg%2FPCVr1C3pVt47n0vlYSCc4cX%2BlxZGfUCV28YunstkSGDYcC0dHI3Ghv38ls27UeSFFvV7jDOkMP8FXMVGOzP9jRiP6MtKkH%2BTHVQCrayU3ufIIb3pV%2F%2Fx%2FtCYDk89VvisTUZzURGVoRFp5evElkPFOC%2FIfC0kozuhqsRf5fa7vzUADjQsp023urusCZjXiEYjg1AdmmHwHUEntfOmVz6Pu4behWsqFxdooJ6Wm%2FDkiFOe1TvQuD3t0db8hfTHqvUH%2F1J%2BIJdwtaI2BzzX4XPyLUjYtEFgxaTXQQh3K%2FP5PyJFIDyGQsJigMg46kq3pT8pnu5V9D6relDz5ektVdyD9fnHwlYYFOEk8Maru3bAS0p2d8aot1zCFiI5RImfyJxAdk5%2FKlFYH2pkzDpzffJBjqnAbjOBMaQHWdfAJobiRrVw9PLco3Ja1GXn6Up7lm%2BjTPrnkYH1oTX3uIH700mv8NExwjdXHae2HgO%2B9z7CQ72wy1kRqDUM75nl868Tkmos0D7FHKxT2zfVw0VuxG%2BQ4kFv5O1TbkSMM8CQo5LNiqFUtS0RofI%2FcoWRCk91PmUCQ6V%2BIxpTH%2FQ98rLoONEZWdoQ96TvHA6vRng4h9%2BDkQKhRuezsyILLw5&X-Amz-Signature=692e8c6632b33be4ac9bd5b1189a5c191da9b10c1a0ddb3e11cf6bb2dc3ced5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Syntax**
The map function takes a function and an iterable as input, runs each element in the iterable through the function, and returns a map object containing the updated iterable.
`map( << some function >> , << some iterable >> )`
As we already know, iterable is an umbrella term for the datatypes list, tuple, dictionary, etc., → things that we can iterate through. 
So every time we want to modify all elements in an iterable in the same way, we can use the map function.
---
**Using map in combination with regular function**
Let’s assume that we have a list called `my_list` that contains the numbers from 0 to 6 and we want to raise each number to the power of two. We can do this using a regular function:
```python
def exponentiate(some_list):
  some_new_list = []
  
  for x in some_list:
    some_new_list.append(x**2)
    
  return some_new_list
  
exponentiate([0,1,2,3,4,5])
[0, 1, 4, 9, 16, 25]
```
As we can see this works perfectly fine. However, we need many lines of code with this implementation and it is a bit cumbersome as we need to write an extra function for this, although we only want to do this transformation once. 
We can simplify this function by using it in combination with a map function. As we can see in the image below, we must provide the function `exponentiate` and the iterable `my_list` as parameters to the map function.
![Using map in combination with a regular function.](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1ccb8893-0ad9-4f20-869d-f036bf43931d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WZRUUT5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJFMEMCIFrfVfgKjHxq%2FoSa6kpV%2BS6bMfpYZlvVuILRO%2BqE2WEvAh9gJHwoOnxe6PbhgO1KlIye69%2FQkIdGHPFIdeXRzzuoKv8DCCcQABoMNjM3NDIzMTgzODA1IgwrK4xrYAi11Vch5Ecq3APhwEaFmdPlCJD5NvKEkkJBC%2FDyS%2F3DlD0TWI%2FvM7MYd8PUicHhxzGk8VqE8w7n2L9TYtNJahveHAtV04ag1FeQTdzIpi%2FY1GYu8CdJtakhQYrT0wU%2FUwugHDPsaQVGRz9igyh5hjZbSbMM%2FavqWPvYQZlzvV%2B57glykVuM43il0H%2FX87Zz75vEQqZrhThiEZSQQzR0vzA9YSME4DpgqOUI7Y2agJHtOYwgp4qLMOCrGFyg%2FPCVr1C3pVt47n0vlYSCc4cX%2BlxZGfUCV28YunstkSGDYcC0dHI3Ghv38ls27UeSFFvV7jDOkMP8FXMVGOzP9jRiP6MtKkH%2BTHVQCrayU3ufIIb3pV%2F%2Fx%2FtCYDk89VvisTUZzURGVoRFp5evElkPFOC%2FIfC0kozuhqsRf5fa7vzUADjQsp023urusCZjXiEYjg1AdmmHwHUEntfOmVz6Pu4behWsqFxdooJ6Wm%2FDkiFOe1TvQuD3t0db8hfTHqvUH%2F1J%2BIJdwtaI2BzzX4XPyLUjYtEFgxaTXQQh3K%2FP5PyJFIDyGQsJigMg46kq3pT8pnu5V9D6relDz5ektVdyD9fnHwlYYFOEk8Maru3bAS0p2d8aot1zCFiI5RImfyJxAdk5%2FKlFYH2pkzDpzffJBjqnAbjOBMaQHWdfAJobiRrVw9PLco3Ja1GXn6Up7lm%2BjTPrnkYH1oTX3uIH700mv8NExwjdXHae2HgO%2B9z7CQ72wy1kRqDUM75nl868Tkmos0D7FHKxT2zfVw0VuxG%2BQ4kFv5O1TbkSMM8CQo5LNiqFUtS0RofI%2FcoWRCk91PmUCQ6V%2BIxpTH%2FQ98rLoONEZWdoQ96TvHA6vRng4h9%2BDkQKhRuezsyILLw5&X-Amz-Signature=348a4f1ae4c3e9f36ca2c148c1f05399a4f539018f1bac78177403de1e213f60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Because we are using `map()` now, we can simplify our function heavily and our code becomes:
```python
def exponentiate(x):
  return x**2

my_list = [0,1,2,3,4,5]

map(exponentiate, my_list)
<map at 0x7f138a1e8b90>
```
As we can see, our function `exponentiate` is a lot simpler now. It only takes one integer as an input and raises it to the power of two and returns the result. With the map function we achieve that the function `exponentiate` is applied / mapped to each element / number inside `my_list`. 
However, we also see that we get a map object as output now and with this we can’t do much. Thus, we need to convert this output to a list. 
```python
def exponentiate(x):
  return x**2

my_list = [0,1,2,3,4,5]

my_list_new = list(map(exponentiate, my_list))

my_list_new
[0, 1, 4, 9, 16, 25]
```
We can see now that we simply used `list()` method to convert the map object to a list and we see now that everything worked perfectly fine as all numbers has been raised to the power of 2.
> 💡 **The `map()` function returns a map object. Thus, we must wrap the `map() `function into the `list()` method to convert the map object to a readable list.**
---
**Using map in combination with lambda function**
Let’s assume we have the same list containing the number from 0 to 5 and we want to do the same operation on these numbers (raise to the power of 2), but without using the `exponentiate` function. We can replace the function with a lambda function.
![Using map in combination with a lambda function](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/632a6be9-e864-44f7-a5df-5ae71e9e4184/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WZRUUT5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJFMEMCIFrfVfgKjHxq%2FoSa6kpV%2BS6bMfpYZlvVuILRO%2BqE2WEvAh9gJHwoOnxe6PbhgO1KlIye69%2FQkIdGHPFIdeXRzzuoKv8DCCcQABoMNjM3NDIzMTgzODA1IgwrK4xrYAi11Vch5Ecq3APhwEaFmdPlCJD5NvKEkkJBC%2FDyS%2F3DlD0TWI%2FvM7MYd8PUicHhxzGk8VqE8w7n2L9TYtNJahveHAtV04ag1FeQTdzIpi%2FY1GYu8CdJtakhQYrT0wU%2FUwugHDPsaQVGRz9igyh5hjZbSbMM%2FavqWPvYQZlzvV%2B57glykVuM43il0H%2FX87Zz75vEQqZrhThiEZSQQzR0vzA9YSME4DpgqOUI7Y2agJHtOYwgp4qLMOCrGFyg%2FPCVr1C3pVt47n0vlYSCc4cX%2BlxZGfUCV28YunstkSGDYcC0dHI3Ghv38ls27UeSFFvV7jDOkMP8FXMVGOzP9jRiP6MtKkH%2BTHVQCrayU3ufIIb3pV%2F%2Fx%2FtCYDk89VvisTUZzURGVoRFp5evElkPFOC%2FIfC0kozuhqsRf5fa7vzUADjQsp023urusCZjXiEYjg1AdmmHwHUEntfOmVz6Pu4behWsqFxdooJ6Wm%2FDkiFOe1TvQuD3t0db8hfTHqvUH%2F1J%2BIJdwtaI2BzzX4XPyLUjYtEFgxaTXQQh3K%2FP5PyJFIDyGQsJigMg46kq3pT8pnu5V9D6relDz5ektVdyD9fnHwlYYFOEk8Maru3bAS0p2d8aot1zCFiI5RImfyJxAdk5%2FKlFYH2pkzDpzffJBjqnAbjOBMaQHWdfAJobiRrVw9PLco3Ja1GXn6Up7lm%2BjTPrnkYH1oTX3uIH700mv8NExwjdXHae2HgO%2B9z7CQ72wy1kRqDUM75nl868Tkmos0D7FHKxT2zfVw0VuxG%2BQ4kFv5O1TbkSMM8CQo5LNiqFUtS0RofI%2FcoWRCk91PmUCQ6V%2BIxpTH%2FQ98rLoONEZWdoQ96TvHA6vRng4h9%2BDkQKhRuezsyILLw5&X-Amz-Signature=18f75a261b48d1ff0728e2c0c62e242a53913ec1e8e58d46a2f70b749d1dc70e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we can we, now write a lambda function where we previously called the exponentiate function. the lambda function can be interpreted as follow:
`lambda << input >> : << operation >>`
In this example the input is the variable `x` and the operation `x**2`. The map function takes each number in `my_list` one after the other and stores it in variable `x`, then the lambda function takes over and returns `x**2`. It is then the map function again which takes this results and updates the according element in `my_list`. This is how the two functions work together.
Our code becomes a very simple one-liner now.
```python
my_list = [0,1,2,3,4,5]

my_list_new = list(map(lambda x : x ** 2, my_list))

my_list_new
[0, 1, 4, 9, 16, 25]
```
The cool thing is that we have the benefits of a function (executing the operation `x**2` multiple times but only writing it once) without creating an actual function. This is the reason why lambda function are called anonymous functions as they don’t have a name and cannot be re-used.
> 💡 **In a lambda function, to the left of the double point `:` we must declare its input and to the right of the double point `:` what it should do with this input.**
---
### `filter()`
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a00ffe1c-795c-4188-bae3-d1549288213b/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXRYQ6FX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFoLLmnHoW5vFU8YARk1jt1PtIbD3zl8i%2BZypD3e7nnSAiB5jHy%2BsRIqRkKfrPv7dFPJsOmmjekQjTgWHOBApvcJOyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMkHd%2F8nDZjZD30yyOKtwDRA3YUoTXpxE2ppCjLjQx9ofu1N1xcDwqtUD0KDdBQ1jqcEUibi%2BHw8Bo0OaSHI9WPEh4dfB7WdpZAcPRLfyvNXIB1yv9oITZORB6zXW3ArjJdm9pu%2Bp3qBqfeTRcMgONqfXnsJmzB46h%2F7H%2FkCMGWNwwICh0sFToanMatKBimEuYiiAWFpcVb69I1Sh4c1cljNWuX0unSt1SuiP55jQjDDPeLpixPIUjMJjBiM4OX6Es85zsQ9qkS4pdoS3cv6KnnzAjr56VQxi7t%2FVHC7OYYx2o6Os7UfJbooDuy5DWVkwCVurtc7iF3wueCxD53TANzlxVy0mrHxN%2BcOt0KDaf1pCgsjGslEFLApd4GSTh6FKf6vmx7YHORSf%2BMPFlBQkxfPvM7cYwUztK708x8Me5rn0MV5vMnyj1ZCrr7IojCtLGCTEJhY1grL6nqR2V6no1CCB4PmtixmG9yfAFyhOkYcuOwp%2BrWLDe49YslFVONjIYqDSfSY01J28hSQYFKla%2BOALCMV2ZxiTkQdy2NzsoAZ1QXNvE8JXbmw0fIEvN40lfj39lTs68xm3dIAoDA7%2BWZI%2B48NejKIIRcAkeh5J6rzD%2Fm7JhSH4AuHqzzB99jHGyAI8mfIIkFcIyLpkwj873yQY6pgGxSHCmVjRTTAZavO86C66eRCsWQnGvJOj1EvmZ8l%2F3B9E6swnBUVGm%2BIGUuTUc10CFX1oQ%2F275EKeGwEWYyms%2FUA%2B4inFXMaWsF94MUPkK%2FtHbVc%2FHowSxFr3CKBNcaCy0qvRtpsOGgbdXKe3tRUAzzRTh%2FwvJB2Za8ZJr%2Fj2OTRDwZj7p7Scho1LpBkCn57XIr6WxfUjOKbGd3KVq0%2FCGumDtlDoJ&X-Amz-Signature=9979f91520bc8d1be21e275866dcaeeaf0864249dae499c8d2a5263e442b45e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Syntax**
The filter function takes also a function and an iterable as inputs. The important difference to map is that the function must be a boolean function and thus return either True or False. This is because the filter function runs each element in the iterable through the function, and returns a list containing only the elements for which the function evaluated to True. The other elements are removed.
`filter( << some boolean function >> , << some iterable >> )`
So every time we want to remove some elements from an iterable based on a condition, we can use the filter function.
---
**Using filter in combination with regular function**
Let’s assume we have a list that contains the numbers from 0 to 5. We now want to remove the even numbers from the list so that the new list contains odd numbers only. We can use a regular function:
```python
def filter_odd(some_list):
	some_new_list = []
  
  for x in some_list:
    if x % 2:
      some_new_list.append(x)
    
  return some_new_list
  
my_list = [0,1,2,3,4,5]

filter_odd(my_list)
[1, 3, 5]
```
We can again simplify this function by using it in combination with the `filter` function. 
![Using filter in combination with a regular function](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/689c366e-7ac8-4444-910e-b373fc7e7cce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXRYQ6FX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFoLLmnHoW5vFU8YARk1jt1PtIbD3zl8i%2BZypD3e7nnSAiB5jHy%2BsRIqRkKfrPv7dFPJsOmmjekQjTgWHOBApvcJOyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMkHd%2F8nDZjZD30yyOKtwDRA3YUoTXpxE2ppCjLjQx9ofu1N1xcDwqtUD0KDdBQ1jqcEUibi%2BHw8Bo0OaSHI9WPEh4dfB7WdpZAcPRLfyvNXIB1yv9oITZORB6zXW3ArjJdm9pu%2Bp3qBqfeTRcMgONqfXnsJmzB46h%2F7H%2FkCMGWNwwICh0sFToanMatKBimEuYiiAWFpcVb69I1Sh4c1cljNWuX0unSt1SuiP55jQjDDPeLpixPIUjMJjBiM4OX6Es85zsQ9qkS4pdoS3cv6KnnzAjr56VQxi7t%2FVHC7OYYx2o6Os7UfJbooDuy5DWVkwCVurtc7iF3wueCxD53TANzlxVy0mrHxN%2BcOt0KDaf1pCgsjGslEFLApd4GSTh6FKf6vmx7YHORSf%2BMPFlBQkxfPvM7cYwUztK708x8Me5rn0MV5vMnyj1ZCrr7IojCtLGCTEJhY1grL6nqR2V6no1CCB4PmtixmG9yfAFyhOkYcuOwp%2BrWLDe49YslFVONjIYqDSfSY01J28hSQYFKla%2BOALCMV2ZxiTkQdy2NzsoAZ1QXNvE8JXbmw0fIEvN40lfj39lTs68xm3dIAoDA7%2BWZI%2B48NejKIIRcAkeh5J6rzD%2Fm7JhSH4AuHqzzB99jHGyAI8mfIIkFcIyLpkwj873yQY6pgGxSHCmVjRTTAZavO86C66eRCsWQnGvJOj1EvmZ8l%2F3B9E6swnBUVGm%2BIGUuTUc10CFX1oQ%2F275EKeGwEWYyms%2FUA%2B4inFXMaWsF94MUPkK%2FtHbVc%2FHowSxFr3CKBNcaCy0qvRtpsOGgbdXKe3tRUAzzRTh%2FwvJB2Za8ZJr%2Fj2OTRDwZj7p7Scho1LpBkCn57XIr6WxfUjOKbGd3KVq0%2FCGumDtlDoJ&X-Amz-Signature=606ac8cb64f7cd7b66f92f9476e92bc69fe71fd6fd2c6367650e2c9c65a44873&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Because we are using `filter()` now, we can simplify our function heavily and our code becomes:
```python
def filter_odd(x):
  return x % 2

my_list = [0,1,2,3,4,5]

my_list_new = filter(filter_odd, my_list)

my_list_new
[1, 3, 5]
```
As we can see now, our function filter_odd is a lot simpler now. It takes an integer as input and applies `x % 2` which [returns 1 / True for odd numbers and 0 / False for even numbers](/5b0832dbf9454eb1941b7632e68a9abb#dd67587d7a0845029106834d0c83ddeb). With the filter function we achieve that elements for which the function returned 0 / False (even numbers) are removed from the list.
> 💡 **The `filter()` function returns the same datatype as the input data. Thus, **we don’t **have to wrap the `filter()` function into the `list()` or other method as we do with the [`map()`](/5b0832dbf9454eb1941b7632e68a9abb) function.**
---
**Using filter in combination with lambda function**
Let’s assume we have the same list containing the numbers from 0 to 5 and we want to do the same operation on these numbers (remove even numbers), but without using the `filter_odd` function. We can again replace the function with a lambda function.
![Using filter in combination with a lambda function](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/291cce1d-6f80-475c-8886-4862219e21a3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXRYQ6FX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFoLLmnHoW5vFU8YARk1jt1PtIbD3zl8i%2BZypD3e7nnSAiB5jHy%2BsRIqRkKfrPv7dFPJsOmmjekQjTgWHOBApvcJOyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMkHd%2F8nDZjZD30yyOKtwDRA3YUoTXpxE2ppCjLjQx9ofu1N1xcDwqtUD0KDdBQ1jqcEUibi%2BHw8Bo0OaSHI9WPEh4dfB7WdpZAcPRLfyvNXIB1yv9oITZORB6zXW3ArjJdm9pu%2Bp3qBqfeTRcMgONqfXnsJmzB46h%2F7H%2FkCMGWNwwICh0sFToanMatKBimEuYiiAWFpcVb69I1Sh4c1cljNWuX0unSt1SuiP55jQjDDPeLpixPIUjMJjBiM4OX6Es85zsQ9qkS4pdoS3cv6KnnzAjr56VQxi7t%2FVHC7OYYx2o6Os7UfJbooDuy5DWVkwCVurtc7iF3wueCxD53TANzlxVy0mrHxN%2BcOt0KDaf1pCgsjGslEFLApd4GSTh6FKf6vmx7YHORSf%2BMPFlBQkxfPvM7cYwUztK708x8Me5rn0MV5vMnyj1ZCrr7IojCtLGCTEJhY1grL6nqR2V6no1CCB4PmtixmG9yfAFyhOkYcuOwp%2BrWLDe49YslFVONjIYqDSfSY01J28hSQYFKla%2BOALCMV2ZxiTkQdy2NzsoAZ1QXNvE8JXbmw0fIEvN40lfj39lTs68xm3dIAoDA7%2BWZI%2B48NejKIIRcAkeh5J6rzD%2Fm7JhSH4AuHqzzB99jHGyAI8mfIIkFcIyLpkwj873yQY6pgGxSHCmVjRTTAZavO86C66eRCsWQnGvJOj1EvmZ8l%2F3B9E6swnBUVGm%2BIGUuTUc10CFX1oQ%2F275EKeGwEWYyms%2FUA%2B4inFXMaWsF94MUPkK%2FtHbVc%2FHowSxFr3CKBNcaCy0qvRtpsOGgbdXKe3tRUAzzRTh%2FwvJB2Za8ZJr%2Fj2OTRDwZj7p7Scho1LpBkCn57XIr6WxfUjOKbGd3KVq0%2FCGumDtlDoJ&X-Amz-Signature=f16436c7b462b0e0d39a09dd4cc66c09b5fa8d6d9dad917a33c98fc6737e0efc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The lambda function replaces again the regular function. The input is the variable `x` and the operation `x % 2`. The filter function takes each number in `my_list` one after the other and stores it in variable `x`, then the lambda function takes over and returns `x % 2`. It is then the filter function again which removes those elements from `my_list` for which the lambda function returned False. This is how the two functions work together.
Our code becomes a very simple (potential) one-liner now.
```python
my_list = [0,1,2,3,4,5]

my_list_new = filter(lambda x : x % 2, my_list)

my_list_new
[1, 3, 5]
```
---
### `reduce()`
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7ea09015-3572-4b57-9da0-4ad109a2286c/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMU4YEW5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDmZwT7BMypEtmJvlptzEbq0RlXU%2Fu8arexrvBWlQ1EwAIgGihUCxOI%2BvqhGAERISooLPnpBdoZwJcgPNmkOlz2fx8q%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDHo2VTNC8bSEIGDPhCrcAwe1I%2FDjFlySkAShVWbMPixe2VhZgQ5zONITXiaI6i9PJLb6FB%2BVkQvQ8lfChVc5411%2BfcnDkOnidbIHHrl3tTbJfSKLpJ0JOVMsl%2Fk2XCBuli3mZPDOJ6TM%2BshLjSuZfhuV6QHZbrR9iRE%2F1wk13mW6Cr9AdFndyHc0kyTkAOXbsusg6IAJ4EyJNwVoBA%2F07t2UW4Gi53Q1jVqpaqCgYs9DPwQ8suNlSair%2BBT5WySKd94BhVuLF4D0gH0RLA6GePHdPD82YIn0tgTEc3EMLgzs2i1wMNIgCTHA4RZ4u2eSy4u71WY7U%2BVpp%2FleRnsdHocmc6YwP%2B2vUUwRO286gbTMMHajFWRvSDtzeMp0e1JWw3Zlmu9Tv9VTKpdOZteMZotrZ2lWVvSrvvYpm9cjULFEu5ZW%2BbYY%2BsEKnoT6We4pOLGMNJEqAKlNNOst88wMlAexMMLUfeFaEAks%2BEInm1BLoUMjsFHeK4%2FBoqp4meymrlUS9J%2B%2BlbiBFs8qZfVvIU8lBPYExqxTC2U%2BM0VZQGpUStpGFvgbk1XvM4a%2BlJNMh3p7XJ%2FBhOdKfhCVNNenCVnlpkzUx6eO2q09SNneVKmkYwJzbqEYrc%2Fro%2B3l%2BuMgCl9rB1ODCfmQaK8qMMLO98kGOqUB0c%2FLARoaKD2N40O4%2F5XP0xg9RcHX1k8bCjklWmyMU5g1tTLcf%2FsqnVmQWG1O5%2Fj5SrbYtb9MhoE9PmdJ2Z%2Ffyccm5AVZzJ87TTMJzoPLed9sa6IKj6uVgBtSBZ87LIY0X9R%2F1Re8jVodE3E63zAmV65IM0tfJysUTm%2BG1%2FGZiNRjBsHbKAYsVehL4DnOure3sWushXFQ%2FjvI6vGVsLHFkxhqHOoR&X-Amz-Signature=a1265dcb50897b5e71136511e1dfe1acd669be8533fd34dd5183cbe6f6e15bb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Syntax**
The reduce function takes also a function and an iterable as inputs. The important difference to [map](/5b0832dbf9454eb1941b7632e68a9abb#8af99f42017f448ea198c32307b14bc9) and [filter](/5b0832dbf9454eb1941b7632e68a9abb#1dc0b8cb700741e5a48f5ed4180b2035) is that it merges the elements in the iterable together so that only one value is returned eventually. How this merge happens must be defined within the provided function.
`reduce( << some function >> , << some iterable >> )`
So every time we want to shrink down multiple elements stored in an iterable such as a list to one single value like an integer or string, we can use the reduce function.
> 💡 **The reduce function is not built-in. This means that before we can use it we have to import it from a package: `from functools import reduce`**
---
**Using reduce in combination with regular function**
Let’s assume we have a list that contains the numbers from 0 to 5. We now want to add all numbers up so that we get an integer value as the sum of all the elements. We can again use a regular function:
```python
def add_up(some_list):
	summe = 0
  
  for x in some_list:
    summe += x
    
  return summe
  
my_list = [0,1,2,3,4,5]

add_up(my_list)
15
```
We can again simplify this function by using it in combination with the reduce  function. 
![Using reduce in combination with a regular function](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d8b5b2a8-341a-415a-aed2-652e6dc187c5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMU4YEW5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDmZwT7BMypEtmJvlptzEbq0RlXU%2Fu8arexrvBWlQ1EwAIgGihUCxOI%2BvqhGAERISooLPnpBdoZwJcgPNmkOlz2fx8q%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDHo2VTNC8bSEIGDPhCrcAwe1I%2FDjFlySkAShVWbMPixe2VhZgQ5zONITXiaI6i9PJLb6FB%2BVkQvQ8lfChVc5411%2BfcnDkOnidbIHHrl3tTbJfSKLpJ0JOVMsl%2Fk2XCBuli3mZPDOJ6TM%2BshLjSuZfhuV6QHZbrR9iRE%2F1wk13mW6Cr9AdFndyHc0kyTkAOXbsusg6IAJ4EyJNwVoBA%2F07t2UW4Gi53Q1jVqpaqCgYs9DPwQ8suNlSair%2BBT5WySKd94BhVuLF4D0gH0RLA6GePHdPD82YIn0tgTEc3EMLgzs2i1wMNIgCTHA4RZ4u2eSy4u71WY7U%2BVpp%2FleRnsdHocmc6YwP%2B2vUUwRO286gbTMMHajFWRvSDtzeMp0e1JWw3Zlmu9Tv9VTKpdOZteMZotrZ2lWVvSrvvYpm9cjULFEu5ZW%2BbYY%2BsEKnoT6We4pOLGMNJEqAKlNNOst88wMlAexMMLUfeFaEAks%2BEInm1BLoUMjsFHeK4%2FBoqp4meymrlUS9J%2B%2BlbiBFs8qZfVvIU8lBPYExqxTC2U%2BM0VZQGpUStpGFvgbk1XvM4a%2BlJNMh3p7XJ%2FBhOdKfhCVNNenCVnlpkzUx6eO2q09SNneVKmkYwJzbqEYrc%2Fro%2B3l%2BuMgCl9rB1ODCfmQaK8qMMLO98kGOqUB0c%2FLARoaKD2N40O4%2F5XP0xg9RcHX1k8bCjklWmyMU5g1tTLcf%2FsqnVmQWG1O5%2Fj5SrbYtb9MhoE9PmdJ2Z%2Ffyccm5AVZzJ87TTMJzoPLed9sa6IKj6uVgBtSBZ87LIY0X9R%2F1Re8jVodE3E63zAmV65IM0tfJysUTm%2BG1%2FGZiNRjBsHbKAYsVehL4DnOure3sWushXFQ%2FjvI6vGVsLHFkxhqHOoR&X-Amz-Signature=d306bd874c41b3f8e4d210bb7c1774b908da3a77c16e2d8ba1658ec07742e3d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Because we are using `reduce()` now, we can simplify our function and our code becomes:
```python
from functools import reduce

def add_up(x, y):
  return x + y

my_list = [0,1,2,3,4,5]

sum_integer = reduce(add_up, my_list)

sum_integer
15
```
As we can see now, the `add_up` function takes now two parameters. Variable `x` represents the intermediary sum and variable `y` the next number to be added. Thus the values of `x` and `y` run-by-run are as follow:
| # run | `x` | `y` |
| --- | --- | --- |
| 1 | 0 | 1 |
| 2 | 1 | 2 |
| 3 | 3 | 3 |
| 4 | 6 | 4 |
| 5 | 10 | 5 |
> 💡 **The function inside filter must have at least two parameters as input. One represents the intermediary result and the other one the *next element to be merged* into the intermediary result.**
---
**Using reduce in combination with lambda function**
Let’s assume we have the same list containing the number from 0 to 5 and we want to do the same operation on these numbers (calculate their sum), but without using the `add_up` function. We can again replace the function with a lambda function.
![Using reduce in combination with a lambda function](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d3b28cc9-733c-4e79-a4cc-85b0ff0d864a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMU4YEW5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDmZwT7BMypEtmJvlptzEbq0RlXU%2Fu8arexrvBWlQ1EwAIgGihUCxOI%2BvqhGAERISooLPnpBdoZwJcgPNmkOlz2fx8q%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDHo2VTNC8bSEIGDPhCrcAwe1I%2FDjFlySkAShVWbMPixe2VhZgQ5zONITXiaI6i9PJLb6FB%2BVkQvQ8lfChVc5411%2BfcnDkOnidbIHHrl3tTbJfSKLpJ0JOVMsl%2Fk2XCBuli3mZPDOJ6TM%2BshLjSuZfhuV6QHZbrR9iRE%2F1wk13mW6Cr9AdFndyHc0kyTkAOXbsusg6IAJ4EyJNwVoBA%2F07t2UW4Gi53Q1jVqpaqCgYs9DPwQ8suNlSair%2BBT5WySKd94BhVuLF4D0gH0RLA6GePHdPD82YIn0tgTEc3EMLgzs2i1wMNIgCTHA4RZ4u2eSy4u71WY7U%2BVpp%2FleRnsdHocmc6YwP%2B2vUUwRO286gbTMMHajFWRvSDtzeMp0e1JWw3Zlmu9Tv9VTKpdOZteMZotrZ2lWVvSrvvYpm9cjULFEu5ZW%2BbYY%2BsEKnoT6We4pOLGMNJEqAKlNNOst88wMlAexMMLUfeFaEAks%2BEInm1BLoUMjsFHeK4%2FBoqp4meymrlUS9J%2B%2BlbiBFs8qZfVvIU8lBPYExqxTC2U%2BM0VZQGpUStpGFvgbk1XvM4a%2BlJNMh3p7XJ%2FBhOdKfhCVNNenCVnlpkzUx6eO2q09SNneVKmkYwJzbqEYrc%2Fro%2B3l%2BuMgCl9rB1ODCfmQaK8qMMLO98kGOqUB0c%2FLARoaKD2N40O4%2F5XP0xg9RcHX1k8bCjklWmyMU5g1tTLcf%2FsqnVmQWG1O5%2Fj5SrbYtb9MhoE9PmdJ2Z%2Ffyccm5AVZzJ87TTMJzoPLed9sa6IKj6uVgBtSBZ87LIY0X9R%2F1Re8jVodE3E63zAmV65IM0tfJysUTm%2BG1%2FGZiNRjBsHbKAYsVehL4DnOure3sWushXFQ%2FjvI6vGVsLHFkxhqHOoR&X-Amz-Signature=1ffb28d9f945aeb98dce2ee63bae0d4b186a424c85da6f851425f96fd96a19c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The lambda function replaces again the regular function. The inputs are the variable `x` (intermediary result) and `y` (next number to be added). The reduce function takes the first two numbers and stores them in variable `x` and `y`. Then the variables are passed to the lambda function and returns `x+y`. It is the reduce function again which stores this return value in `x` and takes the next number in `my_list` and stores it in `y` and the whole process is repeated until the last number in the list has been processed. This is how the two reduce and lambda work together.
Our code becomes a very simple (potential) two-liner now.
```python
from functools import reduce

my_list = [0,1,2,3,4,5]

sum_integer = reduce(lambda x, y : x + y, my_list)

sum_integer
15
```
---

---

---
# Loops
---
## Motivation
---
**Why we use loops**
Often we want to execute a certain piece of code for each element in an iterable. Let’s consider a situation in which we want to send an email to all students (Marco, Melanie and Hans) that are in the university system.
One option to do so, is to write the lines of code to send an email once and then copy-paste them for each student / email we want to send.
```python
subject = 'Marco: Information for upcoming semester'
greeting = 'Hi Marco!'

email = mail.create_email(subject, greeting)
mail.send_email(marco, email)

subject = 'Melanie: Information for upcoming semester'
greeting = 'Hi Melanie!'

email = mail.create_email(subject, greeting)
mail.send_email(melanie, email)

subject = 'Hans: Information for upcoming semester'
greeting = 'Hi Hans!'

email = mail.create_email(subject, greeting)
mail.send_email(hans, email)
```
Another option is to write the code that sends an email once and wrap it into a function. So we get rid off the copy-pasting but still have to define the subject and greeting statically and also end up with multiple function calls, i.e., for each student one function call.
```python
def send_email(recipient, subject, greeting):

	email = mail.create_email(subject, greeting)

	mail.send_email(recipient, email)

subject = 'Marco: Information for upcoming semester'
greeting = 'Hi Marco!'
send_email(marco, subject, greeting)

subject = 'Melanie: Information for upcoming semester'
greeting = 'Hi Melanie!'
send_email(melanie, subject, greeting)

subject = 'Hans: Information for upcoming semester'
greeting = 'Hi Hans!'
send_email(hans, subject, greeting)
```
A final option is to write the code that sends the email once and then iterate over this code for each student and create the subject and greeting dynamically.
```python
students = [marco, melanie, hans]

for student in students:

	subject = '{}: Information for upcoming semester'.format(student.name)
	greeting = 'Hi {}!'.format(student.name)

	email = mail.create_email(subject, greeting)
	mail.send_email(student, email)
```
The last option is the best for several reasons. 
Firstly, when some email parameters like the text of the subject or the greeting message change afterwards we only have to do this modification at one place in the code. If we would opt for the first two options, we would have to do this modification for each student and thus at multiple places in the code. This would be very cumbersome.
Secondly, this way it is easier to keep an overview of our code and thus maintain it efficiently as there are a lot less lines of codes compared to the first two options.
Thirdly, less lines of code is also better as our program then needs less disk space on the server or notebook it is running.
As we can see, this final option we can implement by suing a loop. Generally, we distinguish between two types of loops which are explained in greater detail below:
- **for**-loop → executes a piece of code for each element in an iterable
- **while**-loop → executes a piece of code as long as a condition is met
It is also possible to combine the two loops together. For example, we can easily put one (or multiple) for-loops into a while loop and the other way around.
---
## **for-loop**
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/09f0f1e4-169e-416e-9264-1cb750307a0f/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E7SJINT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDWnwaVLP%2BMKjsGJevrcNbG2nODOetHJtp1Sw3xAFzKcQIhAKtkT6HRc3PaKTdTzpkDpHdw%2FFIoDV9yLQzBKMikLVsMKv8DCCcQABoMNjM3NDIzMTgzODA1IgwmUVKUdvVHO5f5lzsq3AN9LkYwj9HXZ31HXMRTBMR1T7N0zRu23YnIUqZlNk38gbuCpmKLGnDBJPreKAw%2BMnlXzeTBmmhI6EWtYJl9%2Bt%2BrozGsCXXPzLREaRU1e6W3hErE%2FU%2BilkPH60vLa2wIYZGARUK%2BsyOU%2BIqCGwXdswnb2Vax58weyf%2Bl9mSFN7FZbU%2BFa%2FCBtD8agDGr78WR5p%2FQ9r4qm3YmL%2FNqeMGRmPSFvcPabWYDxEUS0k%2B2s0PJjmcsVFyFvhSbOBT4kWR5aXujt9N0NTefRsVvvdEIlAtPjlF3y%2FRW%2BYkV%2Fl67yXRaIQKU9Il%2FoYTAyC3U5xMEP6WPhL3YxY6vMXyySctei3BvItG9ixqF9OupF5%2BdG6C5jfBasANpzWjdDMJovJSCgB7mRZ0cRdLoAi84bdy6pLcmbxAYrvytKN5XQ9hytpvYt7mSDuHHnx7xT%2B2whXMt%2Bk%2B4BC%2FpTEs4%2B51sregI9A5PED4VOljyfvwPh5iVnpA1hQaEAwXxLWiD6LTuK1Ge%2FWWISLFvwK8nT3AvDp7KduJ%2BBGe5LcDo8611A%2FM6iAVc7HuJEl2qrSKwYQaW36f%2FDAY4yy4d7mcy9b%2BHe3q8rdxh6kJJxfPK7nFoN98lStX016Zv05EiYOOO6Y2TZzCzzvfJBjqkAaW%2BqpYQBoyqjFDcleaQQ9synVSLcik%2B0IvcBLnHiSR3H6mkQ6JJmiJ9LUSU3%2BD1Hfwj5ubucwuOVKzlMxj%2B6%2FTgEaRm9aiUsLn8GxFzgkna5rBEzYTV5du9cl%2BID0zJz1PG7tSU5hEbFifMEMRncsiG5qcWCx2kvvilQMqc%2F2K39pUjJuMTK2GrklJQTtDiYX3Wr2g2pGZhlsZWQta%2BqDm31x1P&X-Amz-Signature=4301f53d29fe040a99d185a244b70f2acadcf83a1662530b1a1ff117ee1d55a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Definition**
A for-loop allows us to execute a piece of code until we have reached the end of an iterable. Each time after having executed the code inside the loop, Python jumps to the next value in the iterable, saves this value in a temporary variable and executes the code inside the loop again. This process is repeated until Python has reached the last element in the iterable. The functioning of a for-loop is visualised below.
![Functioning of a for-loop](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bdd8c217-9f01-441a-93cd-be9c3ef3b34e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E7SJINT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDWnwaVLP%2BMKjsGJevrcNbG2nODOetHJtp1Sw3xAFzKcQIhAKtkT6HRc3PaKTdTzpkDpHdw%2FFIoDV9yLQzBKMikLVsMKv8DCCcQABoMNjM3NDIzMTgzODA1IgwmUVKUdvVHO5f5lzsq3AN9LkYwj9HXZ31HXMRTBMR1T7N0zRu23YnIUqZlNk38gbuCpmKLGnDBJPreKAw%2BMnlXzeTBmmhI6EWtYJl9%2Bt%2BrozGsCXXPzLREaRU1e6W3hErE%2FU%2BilkPH60vLa2wIYZGARUK%2BsyOU%2BIqCGwXdswnb2Vax58weyf%2Bl9mSFN7FZbU%2BFa%2FCBtD8agDGr78WR5p%2FQ9r4qm3YmL%2FNqeMGRmPSFvcPabWYDxEUS0k%2B2s0PJjmcsVFyFvhSbOBT4kWR5aXujt9N0NTefRsVvvdEIlAtPjlF3y%2FRW%2BYkV%2Fl67yXRaIQKU9Il%2FoYTAyC3U5xMEP6WPhL3YxY6vMXyySctei3BvItG9ixqF9OupF5%2BdG6C5jfBasANpzWjdDMJovJSCgB7mRZ0cRdLoAi84bdy6pLcmbxAYrvytKN5XQ9hytpvYt7mSDuHHnx7xT%2B2whXMt%2Bk%2B4BC%2FpTEs4%2B51sregI9A5PED4VOljyfvwPh5iVnpA1hQaEAwXxLWiD6LTuK1Ge%2FWWISLFvwK8nT3AvDp7KduJ%2BBGe5LcDo8611A%2FM6iAVc7HuJEl2qrSKwYQaW36f%2FDAY4yy4d7mcy9b%2BHe3q8rdxh6kJJxfPK7nFoN98lStX016Zv05EiYOOO6Y2TZzCzzvfJBjqkAaW%2BqpYQBoyqjFDcleaQQ9synVSLcik%2B0IvcBLnHiSR3H6mkQ6JJmiJ9LUSU3%2BD1Hfwj5ubucwuOVKzlMxj%2B6%2FTgEaRm9aiUsLn8GxFzgkna5rBEzYTV5du9cl%2BID0zJz1PG7tSU5hEbFifMEMRncsiG5qcWCx2kvvilQMqc%2F2K39pUjJuMTK2GrklJQTtDiYX3Wr2g2pGZhlsZWQta%2BqDm31x1P&X-Amz-Signature=6d009075c42bc94b9c7cce771270b1a0d309151f3fece52f603a5346be893d23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
A for loop can be very useful in the following scenarios:
- to modify each element in an iterable like a list, tuple, dictionary etc.
- to execute a piece of code a specific number of times
---
**Syntax**
The syntax of a for-loop is as follow:
**`for`**` << temporary variable >> `**`in`**` << iterable >>:`
`<< code to be executed >>`
---
**Simple for-loop**
Let’s assume we have a list with names and we want to change all the names to capital letters and save the capitalised names in a new list. We can achieve this easily using a for-loop.
```python
names = ['Felix', 'Marta', 'Melanie', 'Mike', 'Frieda', 'Jack']
new_names = []

for x in names:
    new_name = x.upper()
    new_names.append(new_name)

print(new_names)
['FELIX', 'MARTA', 'MELANIE', 'MIKE', 'FRIEDA', 'JACK']
```
From the code snippet above we see that Python iterates over the list `names`. Thereby the current name in the list is saved in the temporary variable `x`. Python then enters the loop body where it capitalises the name and adds it to the list `new_names`. In the end the code inside the loop is executed exactly six times as there are six elements in the list `names`. Check below to understand what is happening step-by-step.
<details>
<summary>1st run of loop</summary>

`x = 'Felix'`
`new_name = 'FELIX'`
`new_names = ['FELIX']`
</details>
<details>
<summary>2nd run of loop</summary>

`x = 'Marta'`
`new_name = 'MARTA'`
`new_names = ['FELIX', 'MARTA']`
</details>
<details>
<summary>3rd run of loop</summary>

`x = 'Melanie'`
`new_name = 'MELANIE'`
`new_names = ['FELIX', 'MARTA', 'MELANIE']`
</details>
<details>
<summary>4th run of loop</summary>

`x = 'Mike'`
`new_name = 'MIKE'`
`new_names = ['FELIX', 'MARTA', 'MELANIE', 'MIKE']`
</details>
<details>
<summary>5th run of loop</summary>

`x = 'Frieda'`
`new_name = 'FRIEDA'`
`new_names = ['FELIX', 'MARTA', 'MELANIE', 'MIKE', 'FRIEDA']`
</details>
<details>
<summary>6th run of loop</summary>

`x = 'Jack'`
`new_name = 'JACK'`
`new_names = ['FELIX', 'MARTA', 'MELANIE', 'MIKE', 'FRIEDA', 'JACK']`
</details>
---
**Simple for-loop using ****`range()`**
*→ check the video *[*here*](/5b0832dbf9454eb1941b7632e68a9abb#dfda5617531d4acb8ca7e70267f9f7e0)
Let’s assume that we have as many friends as there are elements in the list `names` (6) and we want to greet each of them. In the greeting message we want to include the number of the current friend. For example, Felix is friend 1, Marts friend 2, Melanie friend 3 etc. We can achieve this using the following code:
```python
names = ['Felix', 'Marta', 'Melanie', 'Mike', 'Frieda', 'Jack']

for x in range(len(names)):

  friend_number = x + 1
  friend_name = names[x]

  print('Hi {}, my friend number {}!'.format(friend_name, friend_number))

# output
Hi Felix, my friend number 1!
Hi Marta, my friend number 2!
Hi Melanie, my friend number 3!
Hi Mike, my friend number 4!
Hi Frieda, my friend number 5!
Hi Jack, my friend number 6!
```
We can see that in the loop header we use `range(len(names))`, why? 
We want to execute the code inside the loop a specific number of times, i.e., as many elements as there are in the list names. There are six elements in the list. We get this information using `len(names)` which outputs the integer `6`. 
However, we can not say `for x in 6` as 6 is an integer and not an iterable and thus not subscribtable. So how can we generate an iterable that contains six numbers?
Using the [`range()`](/5b0832dbf9454eb1941b7632e68a9abb) method. `range(6)` generates a number range including the number 0, 1, 2, 3, 4 and 5. Thus, the code inside the loop will be executed exactly six times. 
We do `friend_number = x + 1` as the first number in our range object is 0. However, there is no thing such as friend 0. This is why we need to increase `x` by 1 to get the friend number. 
This constellation of combining the `len()` method with the `range()` method is encountered very often as it allows us to execute the loop as specific number of times, without hard-coding anything. This means that the loop would still work even when an element, i.e., a friend is removed or added to the list `names` afterwards.
---
**Simple Nested for-loop**
We can also nest for-loops into each other. Let’s assume we want to create a deck of playing cards. We already have the suits and ranks of the playing cards stored in different lists and we want to create now the deck of all possible playing cards, i.e., all combinations between suits and ranks. We can achieve this with the following code.
```python
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = [1, 2, 3, 4]

card_deck = []

for suit in suits: # outer loop
	for rank in ranks: # inner loop
		card = [suit, rank]
		card_deck.append(card)

print(card_deck)
[['Spades', 1], ['Spades', 2], ['Spades', 3], ['Spades', 4], ['Hearts', 1], ['Hearts', 2], ['Hearts', 3], ['Hearts', 4], ['Diamonds', 1], ['Diamonds', 2], ['Diamonds', 3], ['Diamonds', 4], ['Clubs', 1], ['Clubs', 2], ['Clubs', 3], ['Clubs', 4]]
```
We see now that we have now a second loop in the code which is placed inside the first one. Whenever we have a loop in another loop we call this a nested loop.
With this nested loop we achieve that the first elements in `suits` (`'Spades'`) is saved in the temporary variable `suit` and then we iterate through the entire `ranks` list. Thereby, we create each combination between `'Spades'` and all the rank numbers. Once the last combination was created (`['Spades', 4]`), Python moves on to the second element in `suits` (`'Hearts'`) and iterates over the ranks list again. Using this approach we make sure that we create for each suit four rank cards.
In total we iterate:
- 1 time over the list `suits`
- 4 times over the list `ranks` (for each suit once)

Check below to see what is happening step-by-step.
<details>
<summary>1st run of outer loop</summary>

`suit = 'Spades'`
<details>
<summary>1st run of inner loop</summary>

`rank = 1`
`card = ['Spades', 1]`
</details>
<details>
<summary>2nd run of inner loop</summary>

`rank = 2`
`card = ['Spades', 2]`
</details>
<details>
<summary>3th run of inner loop</summary>

`rank = 3`
`card = ['Spades', 3]`
</details>
<details>
<summary>4th run of inner loop</summary>

`rank = 4`
`card = ['Spades', 4]`
</details>
</details>
<details>
<summary>2nd run of outer loop</summary>

`suit = 'Hearts'`
<details>
<summary>1st run of inner loop</summary>

`rank = 1`
`card = ['Hearts', 1]`
</details>
<details>
<summary>2nd run of inner loop</summary>

`rank = 2`
`card = ['Hearts', 2]`
</details>
<details>
<summary>3rd run of inner loop</summary>

`rank = 3`
`card = ['Hearts', 3]`
</details>
<details>
<summary>4th run of inner loop</summary>

`rank = 4`
`card = ['Hearts', 4]`
</details>
</details>
<details>
<summary>3rd run of outer loop</summary>

`suit = 'Diamonds'`
*1st inner run*
`rank = 1`
`card = ['Diamonds', 1]`
*2nd inner run*
`rank = 2`
`card = ['Diamonds', 2]`
*3rd inner run*
`rank = 3`
`card = ['Diamonds', 3]`
*4th inner run*
`rank = 4`
`card = ['Diamonds', 4]`
</details>
<details>
<summary>4th run of outer loop</summary>

`suit = 'Clubs'`
*1st inner run*
`rank = 1`
`card = ['Clubs', 1]`
*2nd inner run*
`rank = 2`
`card = ['Clubs', 2]`
*3rd inner run*
`rank = 3`
`card = ['Clubs', 3]`
*4th inner run*
`rank = 4`
`card = ['Clubs', 4]`
</details>
---
**Complex Nested for-loop**
We can even create a nested for loop with three levels. Let’s assume that a playing card, apart from a suit and rank also has a colour (black or red). So we need to create all the cards in black and red colour.  To do so, we can wrap the existing two for loops into an additional one.
```python
colours = ['black', 'red']
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = [1, 2, 3, 4]

card_deck = []

for colour in colours: # outer loop
  for suit in suits: # 1st inner loop
    for rank in ranks: # 2nd inner loop
      card = [colour, suit, rank]
      card_deck.append(card)

print(card_deck)
[['black', 'Spades', 1], ['black', 'Spades', 2], ['black', 'Spades', 3], ['black', 'Spades', 4], ['black', 'Hearts', 1], ['black', 'Hearts', 2], ['black', 'Hearts', 3], ['black', 'Hearts', 4], ['black', 'Spades', 1], ['black', 'Spades', 2], ['black', 'Spades', 3], ['black', 'Spades', 4], ['black', 'Suits', 1], ['black', 'Suits', 2], ['black', 'Suits', 3], ['black', 'Suits', 4], ['red', 'Spades', 1], ['red', 'Spades', 2], ['red', 'Spades', 3], ['red', 'Spades', 4], ['red', 'Hearts', 1], ['red', 'Hearts', 2], ['red', 'Hearts', 3], ['red', 'Hearts', 4], ['red', 'Spades', 1], ['red', 'Spades', 2], ['red', 'Spades', 3], ['red', 'Spades', 4], ['red', 'Suits', 1], ['red', 'Suits', 2], ['red', 'Suits', 3], ['red', 'Suits', 4]]
```
We see now that we have two inner loops. But it still it works in the same way as before.
The first element in `colours` (`'black'`) is saved in variable `colour`. Now the first element in `suits` (`'Spades'`) is saved in variable `suit`. Now we iterate over the ranks list. This means we take the first element in `ranks` (`1`) save it in variable `rank`, then the second element in `ranks` (`2`), then the third (`3`), etc., until we have reached the end of the `ranks` list. Only then we proceed with the second element in `suits` (`'Heartes'`) and save it in variable `suit` and iterate over `ranks` again. As soon as we have reached the last element in the `suits` list, we proceed and take the second element in `colours`, (`'red'`) and save it in variable `colour`, iterate over the `ranks` list four times (for each value in `suits`) and over the `suits` list one time.
In total we iterate:
- 1 time over the list `colours`
- 2 times over the list `suits` (for each colour once)
- 8 times over the list `ranks` (for each suit once)

Check below to see what is happening step-by-step. 
<details>
<summary>1st run of outer loop</summary>

`colour = 'black'`
<details>
<summary>1st run of 1st inner loop</summary>

`suit = 'Spades'`
<details>
<summary>1st run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Spades'`
`rank = 1`
`card = ['black', 'Spades', 1]`
</details>
<details>
<summary>2nd run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Spades'`
`rank = 2`
`card = ['black', 'Spades', 2]`
</details>
<details>
<summary>3rd run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Spades'`
`rank = 3`
`card = ['black', 'Spades', 3]`
</details>
<details>
<summary>4th run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Spades'`
`rank = 4`
`card = ['black', 'Spades', 4]`
</details>
</details>
<details>
<summary>2nd run of 1st inner loop</summary>

`suit = 'Hearts'`
<details>
<summary>1st run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Hearts'`
`rank = 1`
`card = ['black', 'Hearts', 1]`
</details>
<details>
<summary>2nd run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Hearts'`
`rank = 2`
`card = ['black', 'Hearts', 2]`
</details>
<details>
<summary>3rd run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Hearts'`
`rank = 3`
`card = ['black', 'Hearts', 3]`
</details>
<details>
<summary>4th run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Hearts'`
`rank = 4`
`card = ['black', 'Hearts', 4]`
</details>
</details>
<details>
<summary>3rd run of 1st inner loop</summary>

`suit = 'Diamonds'`
<details>
<summary>1st run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Diamonds'`
`rank = 1`
`card = ['black', 'Diamonds', 1]`
</details>
<details>
<summary>2nd run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Diamonds'`
`rank = 2`
`card = ['black', 'Diamonds', 2]`
</details>
<details>
<summary>3rd run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Diamonds'`
`rank = 3`
`card = ['black', 'Diamonds', 3]`
</details>
<details>
<summary>4th run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Diamonds'`
`rank = 4`
`card = ['black', 'Diamonds', 4]`
</details>
</details>
<details>
<summary>4th run of 1st inner loop</summary>

`suit = 'Clubs'`
<details>
<summary>1st run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Clubs'`
`rank = 1`
`card = ['black', 'Clubs', 1]`
</details>
<details>
<summary>2nd run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Clubs'`
`rank = 2`
`card = ['black', 'Clubs', 2]`
</details>
<details>
<summary>3rd run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Clubs'`
`rank = 3`
`card = ['black', 'Clubs', 3]`
</details>
<details>
<summary>4th run of 2nd inner loop</summary>

`colour = 'black'`
`suit = 'Clubs'`
`rank = 4`
`card = ['black', 'Clubs', 4]`
</details>
</details>
</details>
<details>
<summary>2nd run of outer loop</summary>

`colour = 'red'`
<details>
<summary>1st run of 1st inner loop</summary>

`suit = 'Spades'`
<details>
<summary>1st run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Spades'`
`rank = 1`
`card = ['red', 'Spades', 1]`
</details>
<details>
<summary>2nd run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Spades'`
`rank = 2`
`card = ['red', 'Spades', 2]`
</details>
<details>
<summary>3rd run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Spades'`
`rank = 3`
`card = ['red', 'Spades', 3]`
</details>
<details>
<summary>4th run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Spades'`
`rank = 4`
`card = ['red', 'Spades', 4]`
</details>
</details>
<details>
<summary>2nd run of 1st inner loop</summary>

`suit = 'Hearts'`
<details>
<summary>1st run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Hearts'`
`rank = 1`
`card = ['red', 'Hearts', 1]`
</details>
<details>
<summary>2nd run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Hearts'`
`rank = 2`
`card = ['red', 'Hearts', 2]`
</details>
<details>
<summary>3rd run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Hearts'`
`rank = 3`
`card = ['red', 'Hearts', 3]`
</details>
<details>
<summary>4th run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Hearts'`
`rank = 4`
`card = ['red', 'Hearts', 4]`
</details>
</details>
<details>
<summary>3rd run of 1st inner loop</summary>

`suit = 'Diamonds'`
<details>
<summary>1st run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Diamonds'`
`rank = 1`
`card = ['red', 'Diamonds', 1]`
</details>
<details>
<summary>2nd run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Diamonds'`
`rank = 2`
`card = ['red', 'Diamonds', 2]`
</details>
<details>
<summary>3rd run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Diamonds'`
`rank = 3`
`card = ['red', 'Diamonds', 3]`
</details>
<details>
<summary>4th run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Diamonds'`
`rank = 4`
`card = ['red', 'Diamonds', 4]`
</details>
</details>
<details>
<summary>4th run of 1st inner loop</summary>

`suit = 'Clubs'`
<details>
<summary>1st run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Clubs'`
`rank = 1`
`card = ['red', 'Clubs', 1]`
</details>
<details>
<summary>2nd run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Clubs'`
`rank = 2`
`card = ['red', 'Clubs', 2]`
</details>
<details>
<summary>3rd run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Clubs'`
`rank = 3`
`card = ['red', 'Clubs', 3]`
</details>
<details>
<summary>4th run of 2nd inner loop</summary>

`colour = 'red'`
`suit = 'Clubs'`
`rank = 4`
`card = ['red', 'Clubs', 4]`
</details>
</details>
</details>
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/28ec8301-6f5d-4601-964e-6de9c1250572/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E7SJINT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDWnwaVLP%2BMKjsGJevrcNbG2nODOetHJtp1Sw3xAFzKcQIhAKtkT6HRc3PaKTdTzpkDpHdw%2FFIoDV9yLQzBKMikLVsMKv8DCCcQABoMNjM3NDIzMTgzODA1IgwmUVKUdvVHO5f5lzsq3AN9LkYwj9HXZ31HXMRTBMR1T7N0zRu23YnIUqZlNk38gbuCpmKLGnDBJPreKAw%2BMnlXzeTBmmhI6EWtYJl9%2Bt%2BrozGsCXXPzLREaRU1e6W3hErE%2FU%2BilkPH60vLa2wIYZGARUK%2BsyOU%2BIqCGwXdswnb2Vax58weyf%2Bl9mSFN7FZbU%2BFa%2FCBtD8agDGr78WR5p%2FQ9r4qm3YmL%2FNqeMGRmPSFvcPabWYDxEUS0k%2B2s0PJjmcsVFyFvhSbOBT4kWR5aXujt9N0NTefRsVvvdEIlAtPjlF3y%2FRW%2BYkV%2Fl67yXRaIQKU9Il%2FoYTAyC3U5xMEP6WPhL3YxY6vMXyySctei3BvItG9ixqF9OupF5%2BdG6C5jfBasANpzWjdDMJovJSCgB7mRZ0cRdLoAi84bdy6pLcmbxAYrvytKN5XQ9hytpvYt7mSDuHHnx7xT%2B2whXMt%2Bk%2B4BC%2FpTEs4%2B51sregI9A5PED4VOljyfvwPh5iVnpA1hQaEAwXxLWiD6LTuK1Ge%2FWWISLFvwK8nT3AvDp7KduJ%2BBGe5LcDo8611A%2FM6iAVc7HuJEl2qrSKwYQaW36f%2FDAY4yy4d7mcy9b%2BHe3q8rdxh6kJJxfPK7nFoN98lStX016Zv05EiYOOO6Y2TZzCzzvfJBjqkAaW%2BqpYQBoyqjFDcleaQQ9synVSLcik%2B0IvcBLnHiSR3H6mkQ6JJmiJ9LUSU3%2BD1Hfwj5ubucwuOVKzlMxj%2B6%2FTgEaRm9aiUsLn8GxFzgkna5rBEzYTV5du9cl%2BID0zJz1PG7tSU5hEbFifMEMRncsiG5qcWCx2kvvilQMqc%2F2K39pUjJuMTK2GrklJQTtDiYX3Wr2g2pGZhlsZWQta%2BqDm31x1P&X-Amz-Signature=b3b6aedcb4e9ec5a3ed29c886d5a619097981bb4b7617d0453ff4ad06e8ec826&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**for-loop with enumerate**
We can combine the **enumerate** function with a for-loop. When iterating with enumerate we get both at the same time: the element in the list as well as its index position. To do so, we define an additional variable, e.g., `i`, in the loop header where the index position is stored.
For example, we can add `enumerate()` to the loop before to get the index position and value of each element in the list `names`.
```python
names = ['Felix', 'Marta', 'Melanie', 'Mike', 'Frieda', 'Jack']
new_names = []

for **i**, name in **enumerate**(names):
    print(f"Index position: {i}"
		print(f"Name {name}"


## Output
Index position: 0
Name: Felix

Index position: 1
Name: Marta

Index position: 2
Name: Melanie

Index position: 3
Name: Mike

Index position: 4
Name: Frieda

Index position: 5
Name: Jack
```
---
## **while-loop**
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d02c0d3c-286a-435c-aba5-3dc61b93d88f/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBFZMB37%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDy5o5BoCfsUh1C8OOmges3cwH0iXDFcVOGC03iMRV6rAIhANyKNwev0o1OoLVx1B%2FvUjz0JHUBpmuJETcP2NbIKVuwKv8DCCcQABoMNjM3NDIzMTgzODA1IgyJ0TH6g9otj%2Ba7XdMq3AMXXzMrB7JnhTFIVVYSyJM%2F8OsVjzqD%2FvPQEqj%2FlYAM6x8FppDNbtsxIwQI%2FYQoAKxtdihR7ZfIhNt7%2FBH2eUvDoe9n8QpsVT4lviiNKUBovWArzsoZpitzHLu5gsAEyy9l37eObwdQ6qJyh01L7KGw2S%2BEucS662fpG71DQDzJc5KhjsUJnD0ZnO1cwYygdI6jZVZfxEv9UZpV5LOmjQkF%2FeC7tnGh2gPSdUid0twc0dLLcmziGOtm07wANUg6uIemi5Fm1giuaWjEFq%2FD9npLeNrmi6Zi2AFBBCTp1pa0UwGcFZ%2F3wJdq7js6hvymonwPV%2BOAC6rk%2FtipLAvLohC8EzuCOHtU2mtaes8eNrUEE2DdWTV8Y%2FoXQ1Gop%2F3aip0b8In3QEGkWUdOJcP7XGxii6PYj48SVmUApDGiH8%2BUIC5mLMjNlfLEZGrBBxMeMpxNFuKh71zosvDz6HFWZCj0LUcW0gHW%2F9lIJm8fsDdIxvkHudyC1PtxTTgIyQ5wPI9P5n%2BFMYJ%2B8f2VHXmFQqJ6bEYkRd%2B%2Fp%2FCIwgLWpjY60hPHei62xdt5sFDoXOz47MNrtS3Sqs1vf%2BlFuP9Nq9ANRzRGpU0xzROi6svFkTg3IlsNoAD4hw1hA7XujjDQzvfJBjqkARxSpzlw0wV8n2cOVdaGqvL8%2BEhd0X1aL3odic8j4x5hx%2Bvtqw4MQjpDaEW0UR1wB%2BPxRyDxtaEXsLicAqMMJTJJ1FintSGeP7DBPcJeOgqZf%2FTstuVdSDThocajyadqV0zJc7GUXNt9KMgnY072mycGAuOB3r9L%2FPasQpfWs0sHk1oHDkXJh8S3VcDiXxOMVyz0JBIIfnIwM3RamEreMNvUiymZ&X-Amz-Signature=6a229edaf713aea08ac41238986afe2404ebe6b3cbd888f87e4d4565c301ecbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Definition**
A while-loop allows us to execute a piece of code as long as a boolean expression evaluates to True. Each time after having executed the code inside the loop, Python checks if the condition still evaluates to True. If yes, the code inside the loop is executed again. If no, Python terminates the execution of the loop and moves on to the first line of code after the loop. This process is visualised in the figure below.
![Functioning of while-loop](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e18e4063-94b6-4047-bab4-0ea4b06775b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBFZMB37%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDy5o5BoCfsUh1C8OOmges3cwH0iXDFcVOGC03iMRV6rAIhANyKNwev0o1OoLVx1B%2FvUjz0JHUBpmuJETcP2NbIKVuwKv8DCCcQABoMNjM3NDIzMTgzODA1IgyJ0TH6g9otj%2Ba7XdMq3AMXXzMrB7JnhTFIVVYSyJM%2F8OsVjzqD%2FvPQEqj%2FlYAM6x8FppDNbtsxIwQI%2FYQoAKxtdihR7ZfIhNt7%2FBH2eUvDoe9n8QpsVT4lviiNKUBovWArzsoZpitzHLu5gsAEyy9l37eObwdQ6qJyh01L7KGw2S%2BEucS662fpG71DQDzJc5KhjsUJnD0ZnO1cwYygdI6jZVZfxEv9UZpV5LOmjQkF%2FeC7tnGh2gPSdUid0twc0dLLcmziGOtm07wANUg6uIemi5Fm1giuaWjEFq%2FD9npLeNrmi6Zi2AFBBCTp1pa0UwGcFZ%2F3wJdq7js6hvymonwPV%2BOAC6rk%2FtipLAvLohC8EzuCOHtU2mtaes8eNrUEE2DdWTV8Y%2FoXQ1Gop%2F3aip0b8In3QEGkWUdOJcP7XGxii6PYj48SVmUApDGiH8%2BUIC5mLMjNlfLEZGrBBxMeMpxNFuKh71zosvDz6HFWZCj0LUcW0gHW%2F9lIJm8fsDdIxvkHudyC1PtxTTgIyQ5wPI9P5n%2BFMYJ%2B8f2VHXmFQqJ6bEYkRd%2B%2Fp%2FCIwgLWpjY60hPHei62xdt5sFDoXOz47MNrtS3Sqs1vf%2BlFuP9Nq9ANRzRGpU0xzROi6svFkTg3IlsNoAD4hw1hA7XujjDQzvfJBjqkARxSpzlw0wV8n2cOVdaGqvL8%2BEhd0X1aL3odic8j4x5hx%2Bvtqw4MQjpDaEW0UR1wB%2BPxRyDxtaEXsLicAqMMJTJJ1FintSGeP7DBPcJeOgqZf%2FTstuVdSDThocajyadqV0zJc7GUXNt9KMgnY072mycGAuOB3r9L%2FPasQpfWs0sHk1oHDkXJh8S3VcDiXxOMVyz0JBIIfnIwM3RamEreMNvUiymZ&X-Amz-Signature=e46b4232c56a37244c0f2ec77d2591215cd28fb9b209e52b9ffe9f8b56d0185c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
It is very important that we make sure that the expression will evaluate to False at some point, as otherwise the loop execution will continue forever and our computer likely shuts down! Thus, inside the body of the loop we need to implement a mechanism that modifies the variables that are tested in the expression in a way so they will make the expression evaluate to False at some point. 
---
**Syntax**
The syntax of a while-loop is as follow:
**`while`**` << boolean expression >>:`
`<< code to be executed >>`
---
**Simple while-loop**
The code snippet below shows a simple example of a while-loop.
```python
counter = 0

while counter < 6:

	print('Counter is equal to {}'.format(counter))
	
	counter += 1

print('We are here')

# output
'Counter is equal to 0'
'Counter is equal to 1'
'Counter is equal to 2'
'Counter is equal to 3'
'Counter is equal to 4'
'Counter is equal to 5'
'We are here'
```
In the example above we see that in the expression we check if the integer `counter` is smaller than 6. If this expression evaluates to True, Python enters the loop and prints the current value of `counter` and increases `counter` by 1 and checks the expression again. As a result, we print the current value of `counter` six times, until `counter` is equal to 6 which makes the expression evaluate to False.
If we wouldn’t increase `counter` by 1, i.e., if the line `counter += 1` would be missing, this loop would run forever until the program crashes due to lacking execution memory. This is why it is important that inside the loop we modify the variables that are tested so that the expression evaluates to False at one point. 
<details>
<summary>*Disclaimer*</summary>

Of course, we could also check an external condition in the expression like if it is sunny or not, at one point it will get cloudy again which would cause the expression evaluate to False and thus exiting the while loop as well.
</details>
As soon as the expression evaluates to False, Python exits the while-loop and jumps to the first line of code after the loop (see indentations), which is `print('We are here')`.
---
**More complicated while-loop**
We can also do more complicated things within the loop body. Actually, we are free to do whatever we want. Remember: Only important thing is that the expression evaluates to False at some point.
```python
summe = 0
counter = 0

while counter <= 5:

    summe += counter
    
    if summe % 2:
      counter += 1
    else:
      counter += 2

print(summe)
```
We see that the expression checks whether counter is less or equal to 5. If that’s the case we go into the loop and execute the code. Otherwise we jump to the first code-line after the loop which is `print(summe)`.
Check the list below, to understand how Python is executing this loop step-by-step. If you don’t remember what is happening when we do `summe % 2`, then [check here](/5b0832dbf9454eb1941b7632e68a9abb#dd67587d7a0845029106834d0c83ddeb).
---
**1st run**
`counter = 0`
`counter <= 5` → `0 <= 5` → `True`
`summe = 0` `counter = 0` → `0 + 0 = 0` → `summe = ``0`
`if ``0`` % 2` → `0` → `False`
`counter += 2` → `counter = 2`
---
**2nd** **run**
`counter = 2`
`counter <= 5` → `2 <= 5` → `True`
`summe = 0` `counter = 2` → `0 + 2 = 2` → `summe = ``2`
`if ``2`` % 2` → `0` → `False`
`counter += 2` → `counter = 4`
---
**3rd** **run**
`counter = 4`
`counter <= 5` → `4 <= 5` → `True`
`summe = 2` `counter = 4` →`0 + 2 = 2` → `summe = ``6`
`if ``6`` % 2` → `0` → `False`
`counter += 2` → `counter = 6`
---
**4th run**
`counter = 6`
`counter <= 5` → `6 <= 5` → `False`
`print(summe)` → `6`
---
We see that in the fourth run, the expression does not evaluate to True anymore as 6 is not smaller or equal than 5. Thus, the loop execution is stopped and Python jumps to the first line after the loop, where the value stored in variable `summe` (6) is printed to the console.
---
## `break` keyword
---
**Definition**
We already learned that as soon as a condition is met, Python exits the for- or while-loop. In the case of a for-loop this condition is reaching the end of an iterable like a list. In the case of a while-loop the condition is a boolean expression evaluating to False. 
However, there is also another option to exit a loop, which is the `break` keyword. Whenever Python encounters this keyword, it exits the loop immediately. Thus, we must extend the flow diagrams of the for- and while-loop accordingly.
![Functioning of while-loop with `break` keyword](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/60eab8f4-da5e-4899-8969-517decb22d53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6MZBAWI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCUxe2m%2BumGGMLbYkz3iOs9toFht%2BQJCE9%2BSHisAcbe2AIgZ6Vd5QqlqyCDisnzSARuMqz3q%2Bx7dPagl%2BVGY6qZvuYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNIGQcA2iA%2FvSHFoAyrcAx2T8kHbvIyr9TZj7UVaCqhjmd6C8d7bwXcW%2Booqs1oqkv3K5FCtQikjjRbOyPyC5IuplgEn8RWSjkWawBvNKTqVnxQI9fO2ZVvzUZZVqdMxSBbNxLdulDEf2tKhVyufBUJ8PCNpLoy%2FShfDERTQJiRgwbrnzIBqqA8SVlJqHbQ0jPWAKqMNooASDQvQ9PLumJqQGLrT1Nw%2F2aQSVPVfk8WHRH77M26AIvjCJvuExDCsuihNXoKOg9sbSNFDOgdMaxfpW26bM4icN8HDSLvQ598s2bgr2ivY6pBxsaQKdaw7kdNZw2TNPnyp1A6n%2BoNVxWoE77FnZ3WEvoHJKexP%2BTzYU9DW2BMxmz%2F6ZFNFFBfLSwMJeD1vQvRmeq0MWI6Zons1XAwpUO6vJF4TJ0BaHzK4v1%2F3zBqpFnwwN%2FoLxEzAZ0h7fXW25EAVOSYt%2BexDAUbW4NK1lEnV%2Fc%2BoTsj7sXf4QrXdHWLOvunmzUwwrl%2BtvImzz4Pj4b%2FQULIr0cllqfFUF%2BX9ctYF84tFhqH0A%2FyaF%2BI7mEttRGQwzGNYmhom4URnJQfcBu%2BF6jnl7Fleuo1ZcIIcs5b8QvPT92HB1F5KjcOhSN4YMg%2BzH7pZfHcwfMz3zZzSfzR%2FrK3bML7O98kGOqUB7zJRTZMOTXgBVP5K4zE2zAPK8WNu1i7nnDauSTh1cngTHPbng%2Fjo9ReyX9d%2Bx94YbiwkvDImeLiiaGKz6WfQcY1ZLiP88RHm%2FiEg8hfVtfL%2Frnuy3smxs2lyfeLosw1eI57tFx2b6PXnAwDpoS9x588DmWAonaI0PqHoWwNMzEMawPn%2BaktjdR94O6%2FYmi%2Fyf780xcWmDU%2Fh2eUofYB66XeEEWXk&X-Amz-Signature=60bb3ecdc025baaf73dac386953fa3c6e8c72be1402a353c824604f303204205&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Functioning of for-loop with `break` keyword](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5729f772-359e-4e20-a33d-32e4579c445a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ3KTIPH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCnfjeqBf1nDzHH%2Fb%2FM5sXq9jS3V0IcFPo67F0fX6nwbAIhAPOAMy04qsbcScDV8UktE39YtwBGxxNBeZBQfT2MQlFmKv8DCCcQABoMNjM3NDIzMTgzODA1IgyPOmBzryqdH7dV47Uq3ANsCPEeu4zX8I7yskfG%2Fy1coTUwZOZlhHuojM%2FrIzXvYqsZ3UEWZoYN2u0XXpkgWvD8kjhuXf1maI3ZEi7kAlLQpqrpkTa6Gp%2BjiQsDhbPMrj5gysg6v9otT4TRJOD%2BcffSo92POHfERGy04HhDrLCIE5BTJ%2B78wDW6pJokyS90BHvbsyWC6q4zpZEeJLs67Xns6J9jDjMdXJlDwiAxkylOGlgnYnDbH%2BtZcFcLuQuTSlUBxs4XHvzv1eojL%2BhhuuYizt5uq%2BcTrpkxWthSL1QMlEexq9cdxjgVaPmn9oBGd3RtMVJtqfOBgcupQJ4t9GX7940%2Fdb8b0W%2FOLTyVmoTKVosI7Bg6uqy8x%2BmDK6oNP%2Bidd3CXOvwQTRbAXzmUYRJVqPO1s3Hd3pNtoz2cfmw0Sp0Hl6d1Gal8PpwaZxkPysvf5GpY55mxOacE14Wqfrk47F2%2FFC%2Ba0xsYk67Sj%2BQfswY6vT4tl7BCHsc0UrijO7PR%2BOSsBb%2FEYkwzUC7vuFcZCCafzohBnbKKW9hkhHvfNTj14q9ziBFzjIF3h6fVpymuLWP2dnH0EPlTgeYv%2BJEBv9vezErng7lXUsK1cCHJaMFQrof8lQ3mu4qZSHmvsDMVmN2Z895g99k%2FITDAzvfJBjqkASZhvo2UcfSAtGZtXwaEH%2FV264kxTEDPoBCIJXd8%2FrIfYebE1gLL18pl5tdJbna6ajsO0u%2Fzw7GPdqRgYyq6bEZnM1XzMhoNROw7pz8wS1J0dA96L%2FkuqkGq8UHHRGS3hZLK%2BwOX8GKq2tv91A9IM0w6Q2lq1HeWS5UyxeH4LHp%2FK%2BIYPuqb6xW02%2F4%2BqOU1B%2Bp2BXe5HDLrb9zMjGy%2FSM8j4r3r&X-Amz-Signature=00f5b9a5b93f1e732ea14392b8068f07e2971b09afd852c5c81469983ef92f8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**While-loop with ****`break`**** **
Let’s assume we wrote a simple calculator that asks a user for two numbers and divides the two numbers. The user can do this calculation as many times as she wants, so the user decides when to stop.
```python
while True:

  number1 = int(input('Provide first number: '))
  number2 = int(input('Provide second number: '))

  result = number1 / number2

  print(result)

  answer = input('Another calculation? (yes/no) ')

  if answer == 'no':
    break

print('Bye!')
```
![Output when executing the calculator](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2fb80900-f728-4b04-82ea-5d0f1d6765f4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C52WUIZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBzWsPbK27owZV6v3OFk8MMe8TrwcAI391zfK71A3shJAiA6K8SKuf1XgWbtFVe4pBLzQLvPJzETc3DqbpOgM0%2FIzCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMFX%2Bb5SICGDC5fszrKtwDDPgZImJHjDCFvuxkuT6Bkg2fumgbIcKI3P4Rop%2BwEjZEKEgACSb2PMluFrN2RKYP6obkRkyfvhYdcarUXiIFw2QhkfUoue16HZ1gIdKEofngfeHdpzPGQEjtUvWLf6SZhAhWHw4O%2FM15qwtKLpwH2Kqm4kfrF8V7PPpRwKSTiAC0knc7vVk51iBvxObpFhBLlFiEUyYmOHazPIKRXZiiyMBvTI51wfweHRa2XZUp6CzIPcLO7y9VXKStPguwHmfPGxcGBWNzi3YsVFWX7ND4dJcN6znih%2BCKPWXazFLghSPtztL1n8Frd2MECk8dg0tl6WeFZdzYaK0mq0kshI0q28%2BTMqqB2iiETRUpOkCMbR%2BwLTrGK1joysY47CvxIiRQkzKSL6oDRVHTJCOJ3NV%2Bl%2Ba%2F4loPtdVk7UAL0OQ%2B8UT7K0%2BDdpenBMX9XjYcOWPUhbtvhdOhzxwlGUUj1GNaQlsNRue9WLSVan1bkUzjwguJh6F6MFHJkzvWja%2BBUG%2BzmzSLYMIxhrS7LyrtDrhbw3jTpodAy6U58nwBHWOD49rztrOhKzdHHHDXEwEeBnDEwozr8ZgujTxKzFX5eSpPA1aAZTaXJK%2B0XYH%2BCdhW6CeVudWdaj0Rqrzx4Lowq873yQY6pgGO9G2UoHyZUZZomKKYcDxipwbcsqsbqYvFFy4mutOOpvSLdWyImmTp57x16PQgsdNMA2aoAyJGjrV7ih5zkXM5EjjWk%2F4HOqF9g0A4lphC%2BwtvUFXrFYIZWyl0Ypq4e5M%2FtyV%2BwHvK%2Fo3fkaxghWM8YJLu62slHDDfNasAoS7vr%2Be%2FxhVc6IzUe%2BTo28xbFQsa8bq66tXaRRDRXfxGsNcSIu6zk9KE&X-Amz-Signature=d3a59c70ad1565ac6b07d47d2d05c676d595afdf565e714ddca9839fdd253aea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In the code snippet above we see that the [`input()`](/5b0832dbf9454eb1941b7632e68a9abb) function is used to ask the user for the two numbers that should be divided.
After dividing the numbers and printing the result, the user is asked if she wants to do another calculation. Then the program checks if the user replied with `'no'`. If this is the case Python breaks and exits the loop, because the user is done, and jumps to the bye message after the loop.
One noticeable difference to the loops seen before is the expression in the loop header that is checked. Now we simply say `while True`. This causes Python to execute the loop indefinitely until we reach the `break` statement. In this scenario this is fine, because it was our intention to give the user the choice & power to decide when to stop the program.
We could implement the same program without the break, just as we did before:
```python
answer = 'yes'

while answer == 'yes':
  number1 = int(input('Provide first number: '))
  number2 = int(input('Provide second number: '))

  result = number1 / number2

  print(result)

  answer = input('Another calculation? (yes/no) ')

print('Bye!')
```
![Output when executing the calculator](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2fb80900-f728-4b04-82ea-5d0f1d6765f4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C52WUIZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBzWsPbK27owZV6v3OFk8MMe8TrwcAI391zfK71A3shJAiA6K8SKuf1XgWbtFVe4pBLzQLvPJzETc3DqbpOgM0%2FIzCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMFX%2Bb5SICGDC5fszrKtwDDPgZImJHjDCFvuxkuT6Bkg2fumgbIcKI3P4Rop%2BwEjZEKEgACSb2PMluFrN2RKYP6obkRkyfvhYdcarUXiIFw2QhkfUoue16HZ1gIdKEofngfeHdpzPGQEjtUvWLf6SZhAhWHw4O%2FM15qwtKLpwH2Kqm4kfrF8V7PPpRwKSTiAC0knc7vVk51iBvxObpFhBLlFiEUyYmOHazPIKRXZiiyMBvTI51wfweHRa2XZUp6CzIPcLO7y9VXKStPguwHmfPGxcGBWNzi3YsVFWX7ND4dJcN6znih%2BCKPWXazFLghSPtztL1n8Frd2MECk8dg0tl6WeFZdzYaK0mq0kshI0q28%2BTMqqB2iiETRUpOkCMbR%2BwLTrGK1joysY47CvxIiRQkzKSL6oDRVHTJCOJ3NV%2Bl%2Ba%2F4loPtdVk7UAL0OQ%2B8UT7K0%2BDdpenBMX9XjYcOWPUhbtvhdOhzxwlGUUj1GNaQlsNRue9WLSVan1bkUzjwguJh6F6MFHJkzvWja%2BBUG%2BzmzSLYMIxhrS7LyrtDrhbw3jTpodAy6U58nwBHWOD49rztrOhKzdHHHDXEwEeBnDEwozr8ZgujTxKzFX5eSpPA1aAZTaXJK%2B0XYH%2BCdhW6CeVudWdaj0Rqrzx4Lowq873yQY6pgGO9G2UoHyZUZZomKKYcDxipwbcsqsbqYvFFy4mutOOpvSLdWyImmTp57x16PQgsdNMA2aoAyJGjrV7ih5zkXM5EjjWk%2F4HOqF9g0A4lphC%2BwtvUFXrFYIZWyl0Ypq4e5M%2FtyV%2BwHvK%2Fo3fkaxghWM8YJLu62slHDDfNasAoS7vr%2Be%2FxhVc6IzUe%2BTo28xbFQsa8bq66tXaRRDRXfxGsNcSIu6zk9KE&X-Amz-Signature=d3a59c70ad1565ac6b07d47d2d05c676d595afdf565e714ddca9839fdd253aea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see now that the `break` keyword is gone again. Instead we just set the variable `answer` initially to `'yes'` and check in the expression after each execution if `answer` is still `'yes'`. If not, the loop is exited and the bye message printed.
As we see there are always multiple options to implement things. The `break` keyword is a very handy tool that gives us even more flexibility.
---
**For-loop with ****`break`**** **
We can also use `break` in a for-loop. Let’s assume that we want to implement a function which takes two inputs:
1.  a list of integers `x`
1. an integer `y` as the target sum
The function `sum_up()` now sums up the numbers in the list `x` and returns how many numbers it needed to reach the target sum `y`.
```python
def sum_up(x, y):	
	
	summe = 0
	num_needed = 0
	
	for number in x:

		summe += number
		num_needed += 1

		if summe >= y:
			break
	
	return num_needed
```
From the code above we see that we initially set the intermediary sum `summe` and the counter `num_needed` to `0`. We now iterate over the numbers in list `x` and add each number to the intermediary sum `summe` and increase the counter `num_needed` by `1`. We now check if the intermediary sum is already equal or greater than the target sum `y`. If yes we break the for-loop as we don’t need to add up more numbers regardless if there are more items in the list. This makes Python jump to the first code-line after the for-loop where the counter `num_needed` is returned. 
Check the examples below:
```python
sum_up([1, 2, 3, 4, 5, 6, 7, 8], 10)
4 # -> 1 + 2 + 3 + 4 = 10 -> 4 numbers needed

sum_up([1, 2, 3, 4, 5, 6, 7, 8], 25)
7 # -> 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 -> 7 numbers needed
```
One motivation for using the `break` keyword in this context are computational resources. We always aim for writing efficient code that consumes as less computational resources as possible. If we would keep iterating over the list `numbers`, although we reached our goal (the target sum `y`) already, we would waste computational resources. This is why it makes sense to use the `break` keyword in this context.
<details>
<summary>*Disclaimer*</summary>

We could also return the counter directly from within the for-loop, this would make Python exit the for-loop as soon as the target sum y has been reached, as well. Again, most of the time there are multiple options to implement things.
```python
def sum_up(x, y):	
	 
	summe = 0
	num_needed = 0
	
	for number in x:

		summe += number
		num_needed += 1

		if summe >= y:
			return num_needed
```
</details>
---
## `continue` keyword
---
**Definition**
Another special keyword that we can use inside loops is `continue`. Whenever Python encounters this keyword, it jumps directly back to the condition, i.e., the loop-header, and thus ignores the code-lines that follow below the `continue` statement for the current run. Again we must extend the flow diagrams of the for- and while-loop accordingly.
![Functioning of while-loop with `continue` keyword](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8a79d6a3-ff3b-44a3-9f7a-91104f4a11ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3KEHMO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDqVqkpSXBov99kn7jEuhaJ24Ml0ZQm7waqU%2FEEFrGUVgIhAPDo7TfAKPr04EdVRgNoC8hohDdMd0zG6mWQXBwy2HhyKv8DCCgQABoMNjM3NDIzMTgzODA1IgyaGlHC6cBHCatKze8q3AP84XD67NXCV11BRhM2nX%2FmeyxMmUCCYqSXINpm6ZMxRbe9HvPWzXasV0AlqGJ2ghajrj4lAXmFBBueu3x9ZR569lOfLR%2Brs59RHR5iILtwSiAgwxqbgCmEygBUV7Ns4xA539AT6lhlgT29kf6WfDyro%2FuZWhW8Pt4L6G%2B79qTW8I30HkxV10ROoYAfk0Au9I9K2rhDmC0XJ2lox6cPSNjdKZpM6DulYIZ4WtEmNjsisR9FIW5x3yjuy3nCvZlweVrj%2B4p7HFjCODhGEKKbBG1NyhRGfuOGt5eV5Ib7Q0GVYDnLhKHUnVKVnOKQ2DweQhJBJHbxtzATds12JETWv4kNuE50ioBBX6uTZ2ijajPq8FHxq8Wsdzevuf6sN7a%2Fp0MuBQLv4vdVOpPwRv%2Fi8tMkHRMovDbvc0DGOAFf%2Bvan9h92k6K6cKZdJu2%2FVUAe5JqUui3kIDRa8Vdo6qAOb1mJK88YCj2jbBb1yf2%2Btz6Y0Jh6DNE%2F5i5cGvWzby5rdA0M2fjzww%2FynEH1vrcaJA1vHBAi87SaOXb4W5qvDtn18ls9Leb2UEnNJCVsl20hnUghdRcMEgM%2BouV6Y2lHhIYWjurqa7AhK4riR12xxUdC7DE95crYYtbSPHvgBTC0zvfJBjqkAd3YQvmNtdVTEEQehME6c4uze9xtKbaZHY7c9LgsyGB1YJkw9y9EVVk9ur7qQwwoT24LDOq4ZzE53Er6xwMEfRiwsSkC57hio3egYy2X8pyIISgUZDZFIIkR3rnZotYkkpgWm4U5M7pRA%2FnvYUF1EYloEjLnFweBWp2B16MDa%2F263RsiNnUZv%2FEMoupLOIx0ghva8JXLiW1eI0qT6Kw%2FdHk6BPXV&X-Amz-Signature=91c230e7020f4fda83bfa0fef9710363d305c2680d39dce2e7d27fe9419be8c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Functioning of for-loop with `continue` keyword](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/70ab097f-0101-4d4c-9fd0-76062f994e0d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5OQ225T%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIASQQqDXiXM93SPZywnnX%2FpjWGutesERTiXYWCfoUecYAiAxtWHjd2PTCmEbsJRyMyGqcp655yBvbVE8CmUf7Bkbvir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMAKDZ%2FQueqJ6jxzpnKtwD9mmpnlCZVYpLe0woPZPdsQunTljAZEflZIVbVYAMvtgIkub5byzAdH%2BDI%2B4rJohpjDt4D3y5PH1e7weL%2BStt4maz5MuwNbTr5Orlbz%2BH72i9sYXBbIUb9tmiiTQU3x3eULXl8KmeZjDus8E32ZObO%2FSTAsNwVBE05fiRIuSxAKOnOINUR59876Y4ziscsiWWNxIF%2BZQTRJ3xx05eD0kTN63KSlac9xzX78Y67AA3JisoI7vtZfLbwn3hAvhlsSvKjEIhHlNTv4u%2B6B%2B19zfP5alb0XtX8hhwDh4gFN%2BbgGzWcfDi4qmL0mFJbFmb%2BsezwdRJpZGlQPoj9GBO5hHN2XzXezQgSKe4Cu5%2FKbFg1Cma%2ByYjLjFNjYwkGwM%2BHu0i9qp4tfddMbrayKZFB1plRmuKHbc077CZWWMmXAJMReFKHF2NB8SIcsUq7AEqsZ9xmof9rZ%2B5vjOUJDq0aVXDG9wMMGCAiipgGW4p0o%2FTVlzox%2FaCCJCw0Qkh3%2B9OSModZavvsM3VCIbebTlXZJEQNgBWNk0q3XlYXdjh1a6xIhBEPag8gJ8aqYQt4BtHQUy6D2qhdZ1oJmn%2Fi0vvWWxvGaUFVfVspWStwFNjB%2FL3IgUycXybPzkKeMFxe8Ywjs73yQY6pgH%2BwX9DPupePbwBcYnTIlsaBokmW5K8M13l2e4oV9YjDyjUpzloBh8ZirvPAY1m2sZN6a%2BhkVxDIMwxjeYMvQJt%2F82XmWoTq7cPV1ZWoaKxzHjvk1HX%2FQlvLYWo5SH3XAR64sUjC1eWVoRx42MOvaG6QR%2BdOtMe25NIj2pqMPPl0BzOXJq9vcBtW6eaLqa1VDIECU1Y8dnwKlXMjC3AgL386hvAhf2M&X-Amz-Signature=7da2b386a6b104b7ce154ade6432f01abe18d7258d4904364d52720f150b034d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**While-loop with ****`continue`**** **
Let’s assume that with the calculator we implemented before it sometimes happens that a user enters a text instead of a number. Thus, before we do the division we must first check if the user entered two integers. If not, the user shall be asked again to enter two numbers. To cover this requirement, we can extend the code as follow.
```python
while True:

  number1 = input('Provide first number: ')
  number2 = input('Provide second number: ')
  
  try:
    number1 = int(number1)
    number2 = int(number2)
  except ValueError:
    print('Invalid input! Please provide two Integers!')
    continue

  result = number1 / number2

  print(result)

  answer = input('Another calculation? (yes/no) ')

  if answer == 'no':
    break

print('Bye!')
```
![Output when executing the calculator](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ec49aeed-3e6b-429e-828f-90f66471dcde/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXHRUY4K%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGRMZ1HDIudwG8HkKhuz5C9pqGCUZdu0JVz0pgZXDqSEAiBKD0QlIV2f%2F33pes4exi%2Fg9eMPZvtIamXWUNRa8YhVNCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM7WzFrAF7kGRdHuHfKtwDRMwGBTULnqcLj6QRJdSKuj1sECtTsiZJqoKVgbfQfHLDLBiOWhN4F%2FIchAFSJsl4Y23kf00Dy%2B60yPhIJXN5fs74VTPhN2NqFl4eGSZnMWxzU6KTeb0Hp%2FRNqc6aIQCUcXfFJFbK0X23uZOIvthj8IyCE5WdJLk%2FnqQRK3qSmCLdwArGo9QhqjswDVNXNPiPyH6%2FQNtazyaCvNm4Ir%2BTZtprIBKihgiHPVpb%2Bl1SYAkeyVh3B19DK%2B5ynqJBmhsblZBzjQfy5FCARu3ls61pRxnFTEwUOtkmF9B7t%2B%2FYme5fmVbpIaG6aypO7c8NKeHUDKxZ1Avd7jFR%2BB7YHuHWlaWhNcbUJrnbOo42c7E%2F4KiT8E2JPK2ZyuXRpeeba6Z%2FPEOANfuYxr7LB%2Fo4%2FzD43jIwda2EUAK0BR%2BI4Cm4nOTLVLbaNnSLuEf2WP7eCRaCM46GSrsMwH3daaSPgZVaBW4nHPWEwOjSqeghzD0vf9hTrdSvJJST8Bol%2BOUVV3bWI2%2BIqNfKur6LtXbumzuRapxZt5Mfidnl392QYs%2BhJKS681nPsMRwC5gx4WZoa%2FL8vMi3haDaICcX7Hd15q04gbX98xZ3UvCWsxXeBiNxHzHnEsE4aPFq9hC83gUwvs73yQY6pgGsdctG0Xhgt8nXxnYPZLN%2F0yQHlPbvTxM5lh%2FkXYPiCZA2CbBKWDvJvupZt3lZMLHPPNRIcvK9FUGN%2BPXnhiUaAtlEogpZklSsHEal%2BI%2FcKYZ4KMfE2ZHINxujwrYhV3vxiSGoczDuc2Vj6UfY7u8d3yGYXsdsENWoetPXV7FFeHvyGGnecvmgOnyH22uOkChUlVTDacUof39KOz9bhdRcQ108noTq&X-Amz-Signature=b6bc2e92c804764f0d3b071c17ac37e46683db6695ab443c543e20533d9d1ff2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see now that we have added a `try` / `except` statement to the calculator. 
Inside the `try` block we convert the two inputs to integers. If this is not possible, e.g., because the user entered a text (string) instead of a number (integer), the code inside the `except` block is executed. Inside this `except` block the calculator tells the user that she must enter two numbers and executes the `continue` keyword, which causes Python to jump back to the beginning of the loop, i.e., to its header `while True:`. 
As a result, the user is asked again and again until she enters two integers as input, only then the `try` block doesn’t fail and Python executes the calculation `number1` / `number2`
---
**For-loop with ****`continue`**** **
We can also use `continue` in a for-loop. Let’s assume that we want to modify the function `sum_up()` so that it does not consider any numbers that are dividable by 3. To cover this requirement, we can adjust the function as follow.
```python
def sum_up(x, y):	
  
  summe = 0
  num_needed = 0
  
  for number in x:
    
    if not number % 3:
      continue
    else:
      summe += number
      num_needed += 1
    
    if summe >= y:
      break
  
  return num_needed
```
We see that we inserted an `if` statement that checks `not number % 3`. If a number is dividable by 3 [`number % 3`](/5b0832dbf9454eb1941b7632e68a9abb) will return `0` and [`not 0`](/5b0832dbf9454eb1941b7632e68a9abb) is equal to `1` which is the same as `True`.
Thus, when a number is dividable by 3 the code inside the `if` is executed. There we only have `continue`, which makes Python jump back to the loop header `for number in x:` and proceed with the next number without updating the variable `summe` and `num_needed`, thus numbers dividable by 3 are ignored. 
If a number is not dividable by 3, the code inside the `else` is executed which updates `summe` and `num_needed` just as we had it before. 
Check the example below: 
```python
sum_up([10, 12, 30, 35, 36, 41], 40)
2 # -> 10 + 35 = 45 -> 2 numbers needed, 12 and 30 are ignored

sum_up([1, 2, 3, 4, 5, 6, 7, 8], 25)
6 # -> 1 + 2 + 4 + 5 + 7 + 8 = 27 -> 6 numbers needed, 3 and 6 are ignored
```
---

---
# Other
## Random numbers
---
**Definition**
In some cases it is useful to generate a random number. Let’s assume we want to implement a head-tail game in Python. To incorporate the randomness factor we thus need Python to generate a random number between 0 and 1. This we can achieve using the [**random**](https://docs.python.org/3/library/random.html) package.
---
[**`.random()`**](https://www.w3schools.com/python/ref_random_random.asp)
This function allows us to generate a random float (decimal) number between 0 and 1.
→ 0 included & 1 excluded
```python
import random

random.random()
0.0023548592797417722

random.random()
0.05659020831692718

random.random()
0.7559122325053506
```
---
[**`.randint(<< start >>, << stop >>)`**](https://www.w3schools.com/python/ref_random_randint.asp)
This function allows us to generate a random integer in the specified number range:
`<< start >> ≤ random_number ≤ << stop >>`
```python
import random

random.randint(5, 10)
6

rando.randint(2, 25)
22

random.randint(33, 35)
33
```
---
[**`.randrange(<< start >>, << stop >>, << step >>)`**](https://www.w3schools.com/python/ref_random_randrange.asp)
This function allows us to select a random number from a specified [number range](/5b0832dbf9454eb1941b7632e68a9abb).
The [important difference](https://stackoverflow.com/questions/3540431/what-is-the-difference-between-random-randint-and-randrange) to [`.randint()`](/5b0832dbf9454eb1941b7632e68a9abb) is that:
The last number `<< stop >>` will never be selected:
```python
import random

random.randrange(0, 1)
0

random.randrange(0, 1)
0

random.randrange(0, 1)
0
```
We can run `.randrange()` with one parameter only:
```python
import random

random.randrange(10)
2

random.randrange(10)
5

random.randrange(10)
7
```
We can specify an optional step
```python
import random

random.randrange(2, 9, 2)
6

random.randrange(2, 9, 2)
8

random.randrange(2, 9, 2)
2
```
---
## Augmented assignments
---
**Definition**
As we learned already when we want to assign a value to a variable we can use the assignment operator `=`. So when we want to save the integer 5 in a variable a we can do:
```python
a = 5
```
Also we have different [math operators](/5b0832dbf9454eb1941b7632e68a9abb#c5ed1b94ab75447ba1228022dbea677f) like `+` `//` `%` that we are already familiar with.
Augmented assignments combine the assignment operator with a math operator by reducing the code needed to update an arithmetic value and thus making the life for coders easier. 
Let’s assume we want to increase the number stored in `a` by 8. We have two options to do so: Value assignment and Augmented assignment. 
**Value assignment**
```python
# addition
a = a + 8

print(a)
13
```
**Augmented assignment**
```python
# addition
a += 8

print(a)
13
```
From the two code snippets we see that both options work fine, but the augmented assignment is a bit simpler as we need to write the variable `a` only once.
So whenever we want to take out a value from a variable, make some math operation with this value and save this result in the same variable again, i.e., updating the variable, we have the option to use augmented assignment.
Check the examples below for all the other math operators.
**Value assignment**
```python
# subtraction
a = a - 2

# division
a = a / 5

# multiplication
a = a * 5

# exponentiation
a = a ** 2

# modulo
a = a % 5

# floor division
a = a // 2
```
**Augmented assignment**
```python
# subtraction
a -= 2

# division
a /= 5

# multiplication
a *= 5

# exponentiation
a **= 2

# modulo
a %= 5

# floor division
a //= 2
```
---
## Check datatype
---
**Definition**
Sometimes we need to check in our code, whether certain data is a specific type. For example, if we ask the user to provide us a text input, then we need to check if the user really provided a tex input and not a number or other values.
---
[`isinstance(<< some data >>, << target data type >>)`](https://www.programiz.com/python-programming/methods/built-in/isinstance)
This method allows us to check if data is of a specific type. It returns `True` if that’s the case and `False` if that’s not the case.
```python
my_name = 'Janick Spirig'

isinstance(my_name, str)
True

isinstance(my_name, int)
False
```
---
## Find highest number
---
**Definition**
Sometimes we want to compare two numbers and return the higher one. For example, if we are comparing the grades of two students and we want to get the higher of the two grades, we can user the max() function.
---
[`max(<< number 1 >>, << number 2 >>)`](https://www.programiz.com/python-programming/methods/built-in/max)
This method allows us to compare two numbers and retrieve the higher one.
```python
grade_max = 5.3
grade_marco = 4.8

highest_grade = max(grade_max, grade_marco)

print(highest_grade)
5.3
```
---
[`max(<< some iterable >>)`](https://www.programiz.com/python-programming/methods/built-in/max)
The method also allows us to retrieve the highest number or letter in an iterbale.
```python
grades = [5.1, 4.3, 5.6, 2.6, 4.5]

highest_grade = max(grades)

print(grades)
5.6
```
```python
names = ['Marco', 'Hans', 'Robert', 'Melanie', 'Roxanna']

last_name_in_alphabet = max(names)

print(names)
'Roxanna'
```
---
## Find lowest number
---
**Definition**
Just as with the `max()` function there is also a `min()` function that does the exact opposite: Retrieves the lowest element.
---
[`min(<< number 1 >>, << number 2 >>)`](https://www.programiz.com/python-programming/methods/built-in/min)
This method allows us to compare two numbers and retrieve the lower one.
```python
grade_max = 5.3
grade_marco = 4.8

highest_grade = min(grade_max, grade_marco)

print(highest_grade)
4.8
```
---
[`min(<< some iterable >>)`](https://www.programiz.com/python-programming/methods/built-in/min)
The method also allows us to retrieve the lowest number or letter in an iterbale.
```python
grades = [5.1, 4.3, 5.6, 2.6, 4.5]

highest_grade = min(grades)

print(grades)
2.6
```
```python
names = ['Marco', 'Hans', 'Robert', 'Melanie', 'Roxanna']

last_name_in_alphabet = min(names)

print(names)
'Hans'
```
---
## max() and min() in combination with lambda
---
We can also pass a lambda function to the `key` argument in `max()` or `min()` to define the metric upon which to find the maximum or minimum. The `key` function is called for each item of the iterable to decide the order of the items.
Example 1: Find the longest and shortest strings in a list
```python
words = ["apple", "banana", "cherry", "dates"]

longest_word = max(words, key=lambda word: len(word))
shortest_word = min(words, key=lambda word: len(word))

print("Longest word: ", longest_word)  # Outputs: banana
print("Shortest word: ", shortest_word) # Outputs: apple
```
Example 2: Find the dictionary with maximum and minimum values for a specific key
```python
data = [
	{'item': 'book', 'price': 12},
	{'item': 'pen', 'price': 5}, 
	{'item': 'notebook', 'price': 7}
]

most_expensive = max(data, key=lambda x:x['price'])
least_expensive = min(data, key=lambda x:x['price'])

print("Most expensive item: ", most_expensive) 
# Outputs: {'item': 'book', 'price': 12}

print("Least expensive item: ", least_expensive)
# Outputs: {'item': 'pen', 'price': 5}
```
---

