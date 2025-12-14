---
title: "Multiple-choice questions"
notion_id: "eb74373d-e499-458c-a0d1-662200f7a02b"
notion_url: "https://www.notion.so/Multiple-choice-questions-eb74373de499458ca0d1662200f7a02b"
exported_at: "2025-12-13T22:54:29.643386+00:00"
---

# Multiple-choice questions

---
📄 **[Programming basics]** (subpage)
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
📄 **[Computing basics]** (subpage)
---
**Decimal to binary**
What is 452 in binary?

<details>
<summary>Solution</summary>

`1 1100 0100`
| Calculation | Resulting binary digit | Aggregated binary digits |
| --- | --- | --- |
| `452 / 2 = 226` | `0` | `0` |
| `226 / 2 = 113` | `0` | `00` |
| `113 - 1 = 112 / 2` | `1` | `100` |
| `56 / 2 = 28` | `0` | `0100` |
| `28 / 2 = 14` | `0` | `0 0100` |
| `14 / 2 = 7` | `0` | `00 0100` |
| `7 - 1 = 6 / 2 = 3` | `1` | `100 0100` |
| `3 - 1 = 2 / 2 = 1` | `1` | `1100 0100` |
| `1 - 1 = 0` | `1` | `1 1100 0100` |
</details>
---
**Binary to decimal**
What is `1101 0011` in decimal? 

<details>
<summary>Solution</summary>

211
We go through the binary number from right to left:
`1` → `1 * 2^0 = `**`1`**
`1` → `1 * 2^1 = `**`2`**
`0` → `0 * 2^2 = `**`0`**
`0` → `0 * 2^3 = `**`0`**
`1` → `1 * 2^4 = `**`16`**
`0` → `0 * 2^5 = `**`0`**
`1` → `1 * 2^6 = `**`64`**
`1` → `1 * 2^7 = `**`128`**
Now we sum up all the numbers:
1 + 2 + 0 + 0 + 16 + 0 + 64 + 128 = <u>**211**</u>
</details>
---
**Logic gates**
Assign the images below to their logic gate and create their truth table.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/35462356-6d1c-4967-ae72-fbd005674a21/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=49951f46294e67ba8de6da7e12552196ac93751b28940b1a04e5986e35c9724f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/86d2f17d-981c-4b80-92cc-e38b737660b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=e5d4e5ddebfe87fdde141067834425b2725353f294b34d80356c33a3c748f533&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f7ffde3-100f-4167-aa32-0cd81d32311c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=644f4f6383d84506165025d86ab44877f3b9f3acda2f6a64b969b5754a36d99f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d7a05b3c-4771-4673-8ac5-89221fdfc57d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=33fa42494740f49bede0e52fe42fc6078bc60d676fe31a378088f55ce8bbcdb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/efdb3faf-eea5-41cd-87d1-6255fbf8cee1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=a6f5a3c3f3d0e760a4c6ab75fdba7595224dd320ab7671eda3ee6860229b8d0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/35462356-6d1c-4967-ae72-fbd005674a21/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZZ62AVI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCfO%2Fl3UOIzDAqzMUbrm%2Fw3G2OFEb%2BAyyH24DVlTilUZQIhAIQCZBuoUyXnSdQ8fMMOspFqWsqlrv2%2BxKSFZI8cTH7YKv8DCCcQABoMNjM3NDIzMTgzODA1IgwHQj7SzdqdHg15XSoq3AMm8UJt1IkH8t8S8A5ODwZ8QVd7pNAhJ3nm%2FMjMCILGGwUaFKZzbuoWcj8YtVksjPDyteMMQb0Kp7F6hlQznoPZuyDnBb3Sr%2BN9KxvUWDjBm28mAgXb4SEWC1tfHXEdMIi5Bm3eYjwuGuvztTDBh2gSVYtdnhDwg2feGfurXAkNhfcCRB%2BpUT5Rn2knkub4nFDyjPKcOTVSUfBXtsp%2Fx09vfO%2FiFA1RpZtKO1ePVcISLoXpDuxonLrzdk7A%2BU%2FHw5CIRWbrZc77ZesEfV3I7IW3ltBDyOSRbE4uvI0UnN282R1R0bV229PEIVVV73UZDLPk73sAvn8zbXSrqkolTW8c8Kafu4R4pF3ifAgdDSrBcHdXMo%2Bz6xOoRzXDUTQaIU3jOXK8xp5KcaN%2FdnXqdLgMhrDorGykmfS%2BmxOih9yDGGiLoRFzCk3%2FA5GvbrbTqjUtmYMQDgYv0zEkmfKG6nNuOh4Kz2DPALmx6qC85%2FfS1MR7ll%2B0IV7NVUY%2BNpwEMqZUQ50kGmZCt7UHv6VL9ZhEP7l7PFDtSpRSA8XeEOIDh9Lma0iqIZzO3u4JoYm88vaRnYnvo4Ep4bM7JFdrgJw%2F%2Bn3utLLeZweM84uVRXXsdZaTqwzTMAV80C19WTDwzffJBjqkAcYK2CivStFjhvN5uA2DA0K%2Fsvmp5egxv44tM32q3lf4rkz2J%2BEPNMQL02xL2L5WKi7L0IIRpe%2FtaWfHAXcQxRf39xHoYMexcWsEota%2Fvy%2BR%2BtFN06SJCksUjowhDdOAC%2FJYcvnmUvU6jzvEQTL4OYI7M%2FH%2FNycvBVNJZ5YMS5btJJJMxu4sMUEhGPQRxSZ9mBmjOL%2BhRENEEJUIMZlbo93vC8MZ&X-Amz-Signature=ec732bfcd689dd0ee0dce48786942e398b1713582604c9f1ed2a382107c7b8d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: NAND
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | True (1) |
| False (0) | True (1) | True (1) |
| True (1) | False (0) | True (1) |
| True (1) | True (1) | False (0) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/86d2f17d-981c-4b80-92cc-e38b737660b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZZ62AVI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCfO%2Fl3UOIzDAqzMUbrm%2Fw3G2OFEb%2BAyyH24DVlTilUZQIhAIQCZBuoUyXnSdQ8fMMOspFqWsqlrv2%2BxKSFZI8cTH7YKv8DCCcQABoMNjM3NDIzMTgzODA1IgwHQj7SzdqdHg15XSoq3AMm8UJt1IkH8t8S8A5ODwZ8QVd7pNAhJ3nm%2FMjMCILGGwUaFKZzbuoWcj8YtVksjPDyteMMQb0Kp7F6hlQznoPZuyDnBb3Sr%2BN9KxvUWDjBm28mAgXb4SEWC1tfHXEdMIi5Bm3eYjwuGuvztTDBh2gSVYtdnhDwg2feGfurXAkNhfcCRB%2BpUT5Rn2knkub4nFDyjPKcOTVSUfBXtsp%2Fx09vfO%2FiFA1RpZtKO1ePVcISLoXpDuxonLrzdk7A%2BU%2FHw5CIRWbrZc77ZesEfV3I7IW3ltBDyOSRbE4uvI0UnN282R1R0bV229PEIVVV73UZDLPk73sAvn8zbXSrqkolTW8c8Kafu4R4pF3ifAgdDSrBcHdXMo%2Bz6xOoRzXDUTQaIU3jOXK8xp5KcaN%2FdnXqdLgMhrDorGykmfS%2BmxOih9yDGGiLoRFzCk3%2FA5GvbrbTqjUtmYMQDgYv0zEkmfKG6nNuOh4Kz2DPALmx6qC85%2FfS1MR7ll%2B0IV7NVUY%2BNpwEMqZUQ50kGmZCt7UHv6VL9ZhEP7l7PFDtSpRSA8XeEOIDh9Lma0iqIZzO3u4JoYm88vaRnYnvo4Ep4bM7JFdrgJw%2F%2Bn3utLLeZweM84uVRXXsdZaTqwzTMAV80C19WTDwzffJBjqkAcYK2CivStFjhvN5uA2DA0K%2Fsvmp5egxv44tM32q3lf4rkz2J%2BEPNMQL02xL2L5WKi7L0IIRpe%2FtaWfHAXcQxRf39xHoYMexcWsEota%2Fvy%2BR%2BtFN06SJCksUjowhDdOAC%2FJYcvnmUvU6jzvEQTL4OYI7M%2FH%2FNycvBVNJZ5YMS5btJJJMxu4sMUEhGPQRxSZ9mBmjOL%2BhRENEEJUIMZlbo93vC8MZ&X-Amz-Signature=869a059774fed444c5d57e0517761e79e08b03bb8ce35629f2c6b095ac39ef39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: OR
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | False (0) |
| False (0) | True (1) | True (1) |
| True (1) | False (0) | True (1) |
| True (1) | True (1) | True (1) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f7ffde3-100f-4167-aa32-0cd81d32311c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZZ62AVI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCfO%2Fl3UOIzDAqzMUbrm%2Fw3G2OFEb%2BAyyH24DVlTilUZQIhAIQCZBuoUyXnSdQ8fMMOspFqWsqlrv2%2BxKSFZI8cTH7YKv8DCCcQABoMNjM3NDIzMTgzODA1IgwHQj7SzdqdHg15XSoq3AMm8UJt1IkH8t8S8A5ODwZ8QVd7pNAhJ3nm%2FMjMCILGGwUaFKZzbuoWcj8YtVksjPDyteMMQb0Kp7F6hlQznoPZuyDnBb3Sr%2BN9KxvUWDjBm28mAgXb4SEWC1tfHXEdMIi5Bm3eYjwuGuvztTDBh2gSVYtdnhDwg2feGfurXAkNhfcCRB%2BpUT5Rn2knkub4nFDyjPKcOTVSUfBXtsp%2Fx09vfO%2FiFA1RpZtKO1ePVcISLoXpDuxonLrzdk7A%2BU%2FHw5CIRWbrZc77ZesEfV3I7IW3ltBDyOSRbE4uvI0UnN282R1R0bV229PEIVVV73UZDLPk73sAvn8zbXSrqkolTW8c8Kafu4R4pF3ifAgdDSrBcHdXMo%2Bz6xOoRzXDUTQaIU3jOXK8xp5KcaN%2FdnXqdLgMhrDorGykmfS%2BmxOih9yDGGiLoRFzCk3%2FA5GvbrbTqjUtmYMQDgYv0zEkmfKG6nNuOh4Kz2DPALmx6qC85%2FfS1MR7ll%2B0IV7NVUY%2BNpwEMqZUQ50kGmZCt7UHv6VL9ZhEP7l7PFDtSpRSA8XeEOIDh9Lma0iqIZzO3u4JoYm88vaRnYnvo4Ep4bM7JFdrgJw%2F%2Bn3utLLeZweM84uVRXXsdZaTqwzTMAV80C19WTDwzffJBjqkAcYK2CivStFjhvN5uA2DA0K%2Fsvmp5egxv44tM32q3lf4rkz2J%2BEPNMQL02xL2L5WKi7L0IIRpe%2FtaWfHAXcQxRf39xHoYMexcWsEota%2Fvy%2BR%2BtFN06SJCksUjowhDdOAC%2FJYcvnmUvU6jzvEQTL4OYI7M%2FH%2FNycvBVNJZ5YMS5btJJJMxu4sMUEhGPQRxSZ9mBmjOL%2BhRENEEJUIMZlbo93vC8MZ&X-Amz-Signature=f692807d98da3d30a51e61135d5b0ca221e38aa0c8756ea1daeb61792abe4566&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: AND
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | False (0) |
| False (0) | True (1) | False (0) |
| True (1) | False (0) | False (0) |
| True (1) | True (1) | True (1) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d7a05b3c-4771-4673-8ac5-89221fdfc57d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZZ62AVI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCfO%2Fl3UOIzDAqzMUbrm%2Fw3G2OFEb%2BAyyH24DVlTilUZQIhAIQCZBuoUyXnSdQ8fMMOspFqWsqlrv2%2BxKSFZI8cTH7YKv8DCCcQABoMNjM3NDIzMTgzODA1IgwHQj7SzdqdHg15XSoq3AMm8UJt1IkH8t8S8A5ODwZ8QVd7pNAhJ3nm%2FMjMCILGGwUaFKZzbuoWcj8YtVksjPDyteMMQb0Kp7F6hlQznoPZuyDnBb3Sr%2BN9KxvUWDjBm28mAgXb4SEWC1tfHXEdMIi5Bm3eYjwuGuvztTDBh2gSVYtdnhDwg2feGfurXAkNhfcCRB%2BpUT5Rn2knkub4nFDyjPKcOTVSUfBXtsp%2Fx09vfO%2FiFA1RpZtKO1ePVcISLoXpDuxonLrzdk7A%2BU%2FHw5CIRWbrZc77ZesEfV3I7IW3ltBDyOSRbE4uvI0UnN282R1R0bV229PEIVVV73UZDLPk73sAvn8zbXSrqkolTW8c8Kafu4R4pF3ifAgdDSrBcHdXMo%2Bz6xOoRzXDUTQaIU3jOXK8xp5KcaN%2FdnXqdLgMhrDorGykmfS%2BmxOih9yDGGiLoRFzCk3%2FA5GvbrbTqjUtmYMQDgYv0zEkmfKG6nNuOh4Kz2DPALmx6qC85%2FfS1MR7ll%2B0IV7NVUY%2BNpwEMqZUQ50kGmZCt7UHv6VL9ZhEP7l7PFDtSpRSA8XeEOIDh9Lma0iqIZzO3u4JoYm88vaRnYnvo4Ep4bM7JFdrgJw%2F%2Bn3utLLeZweM84uVRXXsdZaTqwzTMAV80C19WTDwzffJBjqkAcYK2CivStFjhvN5uA2DA0K%2Fsvmp5egxv44tM32q3lf4rkz2J%2BEPNMQL02xL2L5WKi7L0IIRpe%2FtaWfHAXcQxRf39xHoYMexcWsEota%2Fvy%2BR%2BtFN06SJCksUjowhDdOAC%2FJYcvnmUvU6jzvEQTL4OYI7M%2FH%2FNycvBVNJZ5YMS5btJJJMxu4sMUEhGPQRxSZ9mBmjOL%2BhRENEEJUIMZlbo93vC8MZ&X-Amz-Signature=dab4b1dcba0a5c41c1707d038f6f382da5dff389b3b6972772cc9ba1683e9370&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: NOR
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | True (1) |
| False (0) | True (1) | False (0) |
| True (1) | False (0) | False (0) |
| True (1) | True (1) | False (0) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/efdb3faf-eea5-41cd-87d1-6255fbf8cee1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZZ62AVI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCfO%2Fl3UOIzDAqzMUbrm%2Fw3G2OFEb%2BAyyH24DVlTilUZQIhAIQCZBuoUyXnSdQ8fMMOspFqWsqlrv2%2BxKSFZI8cTH7YKv8DCCcQABoMNjM3NDIzMTgzODA1IgwHQj7SzdqdHg15XSoq3AMm8UJt1IkH8t8S8A5ODwZ8QVd7pNAhJ3nm%2FMjMCILGGwUaFKZzbuoWcj8YtVksjPDyteMMQb0Kp7F6hlQznoPZuyDnBb3Sr%2BN9KxvUWDjBm28mAgXb4SEWC1tfHXEdMIi5Bm3eYjwuGuvztTDBh2gSVYtdnhDwg2feGfurXAkNhfcCRB%2BpUT5Rn2knkub4nFDyjPKcOTVSUfBXtsp%2Fx09vfO%2FiFA1RpZtKO1ePVcISLoXpDuxonLrzdk7A%2BU%2FHw5CIRWbrZc77ZesEfV3I7IW3ltBDyOSRbE4uvI0UnN282R1R0bV229PEIVVV73UZDLPk73sAvn8zbXSrqkolTW8c8Kafu4R4pF3ifAgdDSrBcHdXMo%2Bz6xOoRzXDUTQaIU3jOXK8xp5KcaN%2FdnXqdLgMhrDorGykmfS%2BmxOih9yDGGiLoRFzCk3%2FA5GvbrbTqjUtmYMQDgYv0zEkmfKG6nNuOh4Kz2DPALmx6qC85%2FfS1MR7ll%2B0IV7NVUY%2BNpwEMqZUQ50kGmZCt7UHv6VL9ZhEP7l7PFDtSpRSA8XeEOIDh9Lma0iqIZzO3u4JoYm88vaRnYnvo4Ep4bM7JFdrgJw%2F%2Bn3utLLeZweM84uVRXXsdZaTqwzTMAV80C19WTDwzffJBjqkAcYK2CivStFjhvN5uA2DA0K%2Fsvmp5egxv44tM32q3lf4rkz2J%2BEPNMQL02xL2L5WKi7L0IIRpe%2FtaWfHAXcQxRf39xHoYMexcWsEota%2Fvy%2BR%2BtFN06SJCksUjowhDdOAC%2FJYcvnmUvU6jzvEQTL4OYI7M%2FH%2FNycvBVNJZ5YMS5btJJJMxu4sMUEhGPQRxSZ9mBmjOL%2BhRENEEJUIMZlbo93vC8MZ&X-Amz-Signature=5648b171180477c9839fd6830b3d108efd43c30a01d973d367fecebc4f3bc206&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: XOR
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | False (0) |
| False (0) | True (1) | True (1) |
| True (1) | False (0) | True (1) |
| True (1) | True (1) | False (0) |
</details>
---
**Logic gates**
Which logic gate is represented here?
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d9e5aec0-bc51-48d2-94f2-21491e487e6b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=1fdc105c6d1f3f9645e80b48f2f6eb0c7225acb0dd34ff3919f8e27c27fa398b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- [ ] Q = A AND B
- [ ] Q = A OR B
- [ ] Q = A XOR B
- [ ] Q = A NAND B
- [ ] Q = A NOR B

<details>
<summary>Solution</summary>

Q = A **XOR** B
| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
</details>
---
**Logic gates**
Create and fill out a Truth-table for the logic gate combination below. Your table should have three columns: A, B and Z.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c219addd-4634-4ed7-97e9-9d9433e6027d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=197dffff56025042ccf1f1089d2a20e3060a30d29112c40e997fa06e4512d583&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Solution</summary>

| A | B | Z |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
</details>
---
**Logic gates**
If we put 0 as A and 1 as B into the Full Adder, what will S and C-out be?

<details>
<summary>Solution</summary>

`S = 1`, `C-out = 0`
1 + 0 = 1 → no carry
</details>
---
**Logic gates**
The Half-adder has a Carry-Out but no Carry-In. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Binary addition**
What is `01010101` + `10110101`?

<details>
<summary>Solution</summary>

`100001010`
Write numbers above each other and sum them up
</details>
---
|  |
|  |
|  |
|  |
|  |
**CPU**
What is stored in Register 0 and Register 1 after executing the following program:
`0011011 0001100 1110 0101 1001`

| Command | Explanation |
| --- | --- |
| 00xyyyy | Load number yyyy into R[x] |
| 11xy | Multiply R[x] with R[y] and store result in R[y] |
| 10xy | Add R[x] and R[y] and store result in R[y]  |
| 01xy | Subtract R[y] from R[x] and store result in R[x] |

<details>
<summary>Solution</summary>

| R[0] | R[1] |
| --- | --- |
| 12 | 11 |
| 132 | **132** |
| **121** |  |
</details>
---
**CPU**
What is stored in Register 0 and Register 1 after executing the following program:
`0001101 0010010 0101 1101 1010`

| Command | Explanation |
| --- | --- |
| 00xyyyy | Load number yyyy into R[x] |
| 11**x**y | Multiply R[x] with R[y] and store result in R[y] |
| 10xy | Add R[x] and R[y] and store result in R[y]  |
| 01xy | Subtract R[y] from R[x] and store result in R[x] |

<details>
<summary>Solution</summary>

| R[0] | R[1] |
| --- | --- |
| 13 | 2 |
| 11 | **22** |
| **33** |  |
</details>
---
**CPU**
In which part of the CPU is the the Full-Adder located?
- [ ] Control Unit
- [ ] Registers
- [ ] Arithmetic Logic Unit (ALU)
- [ ] Memory Unit

<details>
<summary>Solution</summary>

Arithmetic Logic Unit (ALU)
All mathematical operations / computation is done in ALU
</details>
---
📄 **[Distributed Systems & Networks]** (subpage)
---
**APIs**
When I want to call an API out of my program code, it is important that I program in the same language as the server is implemented. True or False?

<details>
<summary>Solution</summary>

False
We can send the data to the server in JSON format and the server can also send the response data back in JSON format. Almost all programming languages know how to deal with data in JSON as it is a standardised format. Thus, I can program in Python and the server could be implemented in C#.
</details>
---
**APIs**
The API key which allows authentication and authorisation must be placed in the body of an HTTP request. True or False?

<details>
<summary>Solution</summary>

False
The API key must be placed in the header of the HTTP request.
</details>
---
**APIs**
Web APIs allow a digital entity such as a notebook or a roboter to access a remote server’s resources.

<details>
<summary>Solution</summary>

True
Humans look up the quickest route from A to B over Web browser. My business website does it in the source code by sending a request to the Google API.
</details>
---
**Application layer**
What are the three main things that happen on the Application layer?

<details>
<summary>Solution</summary>

Translation (text into binary)
Compression (Reduction of binary data)
Encryption / Decryption (entered e-banking password is encrypted)
</details>
---
**Transport layer**
Explain why sequence numbers are important.

<details>
<summary>Solution</summary>

A reques coming from the Application layer is split into different TCP segments that are sent to the remote server. Because of packet switching it can occurr that the segment that was sent as third arrives the remote server as the first one. The sequence number allows the remote server to put together the TCP segmetns in the right order again.
</details>
---
**Network layer**
Which of the following things are part of an IP packet?
- [ ] 1) Source MAC address
- [ ] 2) Host MAC address
- [ ] 3) TCP segment
- [ ] 4) HTTP request

<details>
<summary>Solution</summary>

3, 4
TCP segment is in the Payload of the IP packet
HTTP request is in the payload of the TCP segment
MAC address are only added on Data Link layer
</details>
---
**Network layer**
On the Network layer we have multiple different protocols that are used. True or False?

<details>
<summary>Solution</summary>

False
Narrow-waist of networking stack → only IP protocol on Network level
</details>
---
**Network layer**
If my device is not connect to the internet it does not have an IP address. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Ports**
I send an HTTP request from Chrome and Safari, which of the following statements are True?
- [ ] 1) The source port number in both requests is the same.
- [ ] 2) The source port number in both requests is different.
- [ ] 3) The remote port number in both requests is the same
- [ ] 4) The remote port number in both requests is different.

<details>
<summary>Solution</summary>

2, 3
Source port tells my own computer from which application the request is coming from to wire the response back to the right place. The remote server does not care if request was sent by Chrome or Safari, it just cares about the source computer which sent the request.
</details>
---
**TCP vs. UDP**
UDP is less reliable as we don’t know if our request that we sent out over UDP was successfully received by the host. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**UCP**
When we stream a video from Netflix, the User Diagram Protcol (UDP) is used. True or False?

<details>
<summary>Solution</summary>

False
Video streaming uses a bunch of [other protocols](https://www.haivision.com/blog/all/video-encoding-basics-live-video-streaming-protocols/) such as RTMP, RTP or SRT.
</details>
---
**DNS**
When sending a DNS request, the TCP protocol is commonly used. True or False?

<details>
<summary>Solution</summary>

False, DNS goes normally over UDP.
</details>
---
**Data Link layer**
I can manually reset the MAC address of my notebook. True or False?

<details>
<summary>Solution</summary>

False
MAC addreses are burned into a device → permanent physical addressing
</details>
---
**Symmetric encryption**
Choose all correct answers from below:
- [ ] 1) In symmetric encryption, no public keys exist.
- [ ] 2) In symmetric encryption, messages are decrypted with one’s private key.
- [ ] 3) In symmetric encryption, a message is encrypted and decrypted with the same key.
- [ ] 4) In symmetric encryption, both counterparts use only one key.
- [ ] 5) Symmetric encryption can generally be considered as safe and is therefore widely adopted.

<details>
<summary>Solution</summary>

1, 3, 4
</details>
---
**Asymmetric encryption**
Choose all correct answers from below:
- [ ] 1) In asymmetric encryption, public keys are not shared.
- [ ] 2) In asymmetric encryption, private keys are not shared.
- [ ] 3) In asymmetric encryption, the message is encrypted with the public key of the counterpart.
- [ ] 4) In asymmetric encryption, the message is encrypted with the private key of the counterpart.
- [ ] 5) In asymmetric encryption, the private and public key depend mathematically on each other.
- [ ] 6) in asymmetric encryption, a message can only be decrypted with one’s public key.
- [ ] 7) in asymmetric encryption, a message can only be decrypted with one’s private key.

<details>
<summary>Solution</summary>

2, 3, 5, 7
</details>
---
**Diffie-Hellman key exchange**
Choose all correct answers from below:
- [ ] 1) In Diffie-Hellman, messages are decrypted with one’s private key.
- [ ] 2) In Diffie-Hellmann, both counterparts use the same key to encrypt end decrypt messages.
- [ ] 3) Diffie-Hellmann brings together the power of symmetric and asymmetric encryption. 
- [ ] 4) In Diffie-Hellmann, the hacker is not able to decrypt the message as he does not possess one of the public keys.

<details>
<summary>Solution</summary>

2, 3
</details>
---
**HTTP methods**
When I want to change my e-banking password, what kind of request is most likely sent to the e-banking server? 
- [ ] 1) PUT
- [ ] 2) POST
- [ ] 3) GET
- [ ] 4) DELETE

<details>
<summary>Solution</summary>

PUT
My e-banking user exists already. Thus, we modify an existing resource (my e-banking user) on the server, which we can achieve by sending a PUT request.
</details>
---
**HTTP methods**
When I create a new Notion account, what kind of request is most likely sent to the Notion server?
- [ ] 1) PUT
- [ ] 2) POST
- [ ] 3) GET
- [ ] 4) DELETE

<details>
<summary>Solution</summary>

POST
We want to create a new resource on the server (my new Notion account) which we can achieve by sending a POST request to the server.
</details>
---
**HTTP Response codes**
Explain for the response codes below what they mean. 
200 | 201 | 400 | 401 | 404 | 501 | 503

<details>
<summary>Solution</summary>

200 → OK
201 → Created
400 → Bad request
401 → Unauthorised
404 → Not found
501 → Internal server error
503 → Service unavailable
</details>
---
**HTTPS**
When sending an HTTPS request, which of the following things are encrypted?
- [ ] 1) Payload
- [ ] 2) Host IP address
- [ ] 3) HTTP method
- [ ] 4) Host port number
- [ ] 5) Source port number
- [ ] 6) Amount of data transferred

<details>
<summary>Solution</summary>

1, 3
If we would encrypt the other things it would be difficult to send the request to the right destination.
</details>
---
**HTTPS / TLS**
When sending my e-banking login to the bank’s sever, HTTPS makes sure that my password, i.e., the data is encrypted and secured whereas TLS makes sure that the connection to the server is reliable and secure.

<details>
<summary>Solution</summary>

True
HTTPS is responsible for encryption on application level while TLS is encryption on transport / connection level. They play together to ensure that the e-banking login gets transmitted securely to the bank’s server.
</details>
---
**TLS handshake**
We cannot use both at the same time, TLS/SSL and HTTPS. True or False?

<details>
<summary>Solution</summary>

False
We use HTTPS on application level and TLS/SSL on transport level. 
First we establish a reliable connection with the remote server by performing a TLS/SSL handshake. Then we exchange data with the remote server securely over HTTPS.
</details>
---
**TLS handshake**
Explain what the role of the Certificate Authority (CA) is during the TLS/SSL handshake.

<details>
<summary>Solution</summary>

The CS checks if the remote server actually is the person / party which it pretends to be. Because the server could send to us any kind of certificate, also a fake one, so before we send our e-banking password to this server we must check with the CA that this actually is the UBS e-banking server.
</details>
---

📄 **[Databases]** (subpage)
---
**1:m relationship**
Let’s assume we have two data tables: Parents and Children. We know that a parent can have multiple children but a child can only belong to one parent. How can we connect the two tables together? 
- [ ] 1) Insert the Primary Key in the Children table into the Parents table
- [ ] 2) Insert the Primary Key in the Parents table into the Children table
- [ ] 3) Insert the Primary Key in the Children table into the Parents table and the Primary Key in the Parents table into the Children table

<details>
<summary>Solution</summary>

2
A parent can have multiple children. With inserting the Parent Primary Key into the Children table we can associate the same parent with multiple kids.
</details>
---
**m:n relationship**
Let’s assume that we have two tables: Girls and Boys. We want to insert another table called Relationships. This table should store all past and current relationships that existed or exist between the Girls and the Boys. How many Foreign Keys would that table have?
- [ ] 0
- [ ] 1
- [ ] 2

<details>
<summary>Solution</summary>

2
We deal with an m:n relationship between Boys and Girls. One Girl could have had multiple relationships in the past and the same is true for one Boy. Thus, the relationship table is our mapping table. We can store all couples that existed or exist by inserting the Girls Primary Key and the Boys Primary Key in the Relationships table. Thus, the table then has two Foreign Keys.
</details>
---
**JOINs**
Which type of JOIN usually results in the highest number of records in the output table?
- [ ] 1) Inner
- [ ] 2) Left
- [ ] 3) Right
- [ ] 4) Outer

<details>
<summary>Solution</summary>

4
The outer join includes all records from the left table and all records from the right table in the output. Where no data is found, #NaN is inserted. Thus, this type of join results usually in the highest number of records. 
If all records in the left table are associated to a record in the right table and vice-versa, all JOINs would yield the same number of records in the output table.
</details>
---
**SQL queries**
We have this table called Students:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bf7650b6-881f-4352-af87-8479d2a11196/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZVK6DQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDAOx1cPg5xoBoPHVrpRQUR1htCvmx5wyTC5l1g%2FiJIDwIhAITt7xnuqkCSB6iVWFLD%2BGdSmL%2BlaSGhVTjaIClzuflmKv8DCCcQABoMNjM3NDIzMTgzODA1IgysJM9NUFBn%2B5x6iWoq3APo%2BuLGnj%2B8cnBvPktjFLZiWcT45V2sXSRVwXvIP4nrUgT%2FgQBCrUIx%2F1xRodXk%2BPtq7bVm5pWpx40yjOd9d177R4%2FgZlDfeQypfMTAmgyYkuH31tpkXz9lBxLIZIwzgFRRXXbo81IUnK3%2BD72zoUdc7q7uaEepuw%2BG%2B1oiZp5%2F0X6JVJa%2BqSRs8%2FcwReQj703782vnrHjVBo%2BBbRKoAHXEVvuxcanmeJPXWIo%2FabdPA9YDs4Id7mHnxVvZPbsxtwyYDkNvb%2BlvmnWLoCoeY%2Ftox0DFrjWKQwAabHJiEy2xCgIyRHz3W2brzGCfs98XxKAreicG3Jbvn4CU1NPw6hNbTNfRmCA0q%2BcI6%2BT7Aq%2Bm6hw6xPtF5nhDjyKtVMyDFAup83VhzKr21T4HzPT69p63lKze35asbVZwwB%2B0J51ZdUpNGXxBugbUXHIui092cAIyIlf3A7CL3MVVgCVBc3eKFEABfvgM0kYOHp8D8O%2B1wQs0P%2BtjLHHq%2BNjUnpaAZKrGyUlgDckolxmRVswsckP2Ic6tZYvPQ%2Bx8x1OOgrRVPD9RF7wMvHFDD9Rsh04L1O43Cjx4XY2mW6K8RAeFWVSubLbhhGEwLMawO9ihXnQUEdlovFvBOFPaW4cYtjD5zffJBjqkAW%2BgmA5TBsJIAnjRDPje2H9zTj2WvOfq7EaDGbaWf%2BnB0dwyS06FUml6L3IrMhzmxThVy9P6twmyTd01DLgHI6MMV1PMDtf0pL6iqVA%2B5xQI4IX3onNiHcA%2FwzdjDsjqod3FfLx0LaF64fcf5YcTpbYeuDTbPFxvUbcICgO52Gv%2FEccG9K%2FXlfgvuISs%2BhgGIcBWTggZ1lfitO7vNAurV2c%2BFIOY&X-Amz-Signature=78bda5d50c1dab59da130d42a536806df11ee9fde7e5bf9e4267f839e7c54302&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we want to have this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e812d65a-f8b9-4756-9d4e-9c2351985a16/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZVK6DQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDAOx1cPg5xoBoPHVrpRQUR1htCvmx5wyTC5l1g%2FiJIDwIhAITt7xnuqkCSB6iVWFLD%2BGdSmL%2BlaSGhVTjaIClzuflmKv8DCCcQABoMNjM3NDIzMTgzODA1IgysJM9NUFBn%2B5x6iWoq3APo%2BuLGnj%2B8cnBvPktjFLZiWcT45V2sXSRVwXvIP4nrUgT%2FgQBCrUIx%2F1xRodXk%2BPtq7bVm5pWpx40yjOd9d177R4%2FgZlDfeQypfMTAmgyYkuH31tpkXz9lBxLIZIwzgFRRXXbo81IUnK3%2BD72zoUdc7q7uaEepuw%2BG%2B1oiZp5%2F0X6JVJa%2BqSRs8%2FcwReQj703782vnrHjVBo%2BBbRKoAHXEVvuxcanmeJPXWIo%2FabdPA9YDs4Id7mHnxVvZPbsxtwyYDkNvb%2BlvmnWLoCoeY%2Ftox0DFrjWKQwAabHJiEy2xCgIyRHz3W2brzGCfs98XxKAreicG3Jbvn4CU1NPw6hNbTNfRmCA0q%2BcI6%2BT7Aq%2Bm6hw6xPtF5nhDjyKtVMyDFAup83VhzKr21T4HzPT69p63lKze35asbVZwwB%2B0J51ZdUpNGXxBugbUXHIui092cAIyIlf3A7CL3MVVgCVBc3eKFEABfvgM0kYOHp8D8O%2B1wQs0P%2BtjLHHq%2BNjUnpaAZKrGyUlgDckolxmRVswsckP2Ic6tZYvPQ%2Bx8x1OOgrRVPD9RF7wMvHFDD9Rsh04L1O43Cjx4XY2mW6K8RAeFWVSubLbhhGEwLMawO9ihXnQUEdlovFvBOFPaW4cYtjD5zffJBjqkAW%2BgmA5TBsJIAnjRDPje2H9zTj2WvOfq7EaDGbaWf%2BnB0dwyS06FUml6L3IrMhzmxThVy9P6twmyTd01DLgHI6MMV1PMDtf0pL6iqVA%2B5xQI4IX3onNiHcA%2FwzdjDsjqod3FfLx0LaF64fcf5YcTpbYeuDTbPFxvUbcICgO52Gv%2FEccG9K%2FXlfgvuISs%2BhgGIcBWTggZ1lfitO7vNAurV2c%2BFIOY&X-Amz-Signature=5518abc576933e80aaa59a1195149c85c4299f436e51cbe7143771763cee727e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Write a query that does the necessary.

<details>
<summary>Solution</summary>

```sql
SELECT COUNT(*) as 'no_of_students'
FROM students
```
</details>
---
**SQL queries**
We have this table called Students:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bf7650b6-881f-4352-af87-8479d2a11196/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZVK6DQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDAOx1cPg5xoBoPHVrpRQUR1htCvmx5wyTC5l1g%2FiJIDwIhAITt7xnuqkCSB6iVWFLD%2BGdSmL%2BlaSGhVTjaIClzuflmKv8DCCcQABoMNjM3NDIzMTgzODA1IgysJM9NUFBn%2B5x6iWoq3APo%2BuLGnj%2B8cnBvPktjFLZiWcT45V2sXSRVwXvIP4nrUgT%2FgQBCrUIx%2F1xRodXk%2BPtq7bVm5pWpx40yjOd9d177R4%2FgZlDfeQypfMTAmgyYkuH31tpkXz9lBxLIZIwzgFRRXXbo81IUnK3%2BD72zoUdc7q7uaEepuw%2BG%2B1oiZp5%2F0X6JVJa%2BqSRs8%2FcwReQj703782vnrHjVBo%2BBbRKoAHXEVvuxcanmeJPXWIo%2FabdPA9YDs4Id7mHnxVvZPbsxtwyYDkNvb%2BlvmnWLoCoeY%2Ftox0DFrjWKQwAabHJiEy2xCgIyRHz3W2brzGCfs98XxKAreicG3Jbvn4CU1NPw6hNbTNfRmCA0q%2BcI6%2BT7Aq%2Bm6hw6xPtF5nhDjyKtVMyDFAup83VhzKr21T4HzPT69p63lKze35asbVZwwB%2B0J51ZdUpNGXxBugbUXHIui092cAIyIlf3A7CL3MVVgCVBc3eKFEABfvgM0kYOHp8D8O%2B1wQs0P%2BtjLHHq%2BNjUnpaAZKrGyUlgDckolxmRVswsckP2Ic6tZYvPQ%2Bx8x1OOgrRVPD9RF7wMvHFDD9Rsh04L1O43Cjx4XY2mW6K8RAeFWVSubLbhhGEwLMawO9ihXnQUEdlovFvBOFPaW4cYtjD5zffJBjqkAW%2BgmA5TBsJIAnjRDPje2H9zTj2WvOfq7EaDGbaWf%2BnB0dwyS06FUml6L3IrMhzmxThVy9P6twmyTd01DLgHI6MMV1PMDtf0pL6iqVA%2B5xQI4IX3onNiHcA%2FwzdjDsjqod3FfLx0LaF64fcf5YcTpbYeuDTbPFxvUbcICgO52Gv%2FEccG9K%2FXlfgvuISs%2BhgGIcBWTggZ1lfitO7vNAurV2c%2BFIOY&X-Amz-Signature=78bda5d50c1dab59da130d42a536806df11ee9fde7e5bf9e4267f839e7c54302&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we want to have this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/35b45d58-c46d-4039-952f-492de3ea98a3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZVK6DQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDAOx1cPg5xoBoPHVrpRQUR1htCvmx5wyTC5l1g%2FiJIDwIhAITt7xnuqkCSB6iVWFLD%2BGdSmL%2BlaSGhVTjaIClzuflmKv8DCCcQABoMNjM3NDIzMTgzODA1IgysJM9NUFBn%2B5x6iWoq3APo%2BuLGnj%2B8cnBvPktjFLZiWcT45V2sXSRVwXvIP4nrUgT%2FgQBCrUIx%2F1xRodXk%2BPtq7bVm5pWpx40yjOd9d177R4%2FgZlDfeQypfMTAmgyYkuH31tpkXz9lBxLIZIwzgFRRXXbo81IUnK3%2BD72zoUdc7q7uaEepuw%2BG%2B1oiZp5%2F0X6JVJa%2BqSRs8%2FcwReQj703782vnrHjVBo%2BBbRKoAHXEVvuxcanmeJPXWIo%2FabdPA9YDs4Id7mHnxVvZPbsxtwyYDkNvb%2BlvmnWLoCoeY%2Ftox0DFrjWKQwAabHJiEy2xCgIyRHz3W2brzGCfs98XxKAreicG3Jbvn4CU1NPw6hNbTNfRmCA0q%2BcI6%2BT7Aq%2Bm6hw6xPtF5nhDjyKtVMyDFAup83VhzKr21T4HzPT69p63lKze35asbVZwwB%2B0J51ZdUpNGXxBugbUXHIui092cAIyIlf3A7CL3MVVgCVBc3eKFEABfvgM0kYOHp8D8O%2B1wQs0P%2BtjLHHq%2BNjUnpaAZKrGyUlgDckolxmRVswsckP2Ic6tZYvPQ%2Bx8x1OOgrRVPD9RF7wMvHFDD9Rsh04L1O43Cjx4XY2mW6K8RAeFWVSubLbhhGEwLMawO9ihXnQUEdlovFvBOFPaW4cYtjD5zffJBjqkAW%2BgmA5TBsJIAnjRDPje2H9zTj2WvOfq7EaDGbaWf%2BnB0dwyS06FUml6L3IrMhzmxThVy9P6twmyTd01DLgHI6MMV1PMDtf0pL6iqVA%2B5xQI4IX3onNiHcA%2FwzdjDsjqod3FfLx0LaF64fcf5YcTpbYeuDTbPFxvUbcICgO52Gv%2FEccG9K%2FXlfgvuISs%2BhgGIcBWTggZ1lfitO7vNAurV2c%2BFIOY&X-Amz-Signature=142dfb9a4b1980a153272422a12b58e00f56843cbaae32cef6e996065234b0c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Write a query that does the necessary.

<details>
<summary>Solution</summary>

```sql
SELECT date_of_birth, COUNT(*) as 'number of people born'
FROM students
WHERE date_of_birth = '1997-04-23'
```
</details>
---
**SQL queries**
We have this table called Enrolments:
We have this table called Courses:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1706f8e7-a234-40f0-aba2-dbd75215db31/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYYGULGU%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGK6J9EE2FfSzah7dyXKOrn2YOK5pRq7Yj6p89dOiuj2AiBmp1ngve%2Bde5L8%2FPIp%2By6aW%2B8lFBLkj5xapHd%2Fevphmyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMD9nz%2BU5BCW0mM7qVKtwDkYTO3C%2ByZxgGnDvvOAKjFOKJ%2Fn5PC%2BMxiJaPdYbG0pijH%2Bh2Lo3y%2FAobQ99Dkadq%2FQ%2FMjRZI9%2B4XrJBeXvjnsQFcFWWz0TJEMjQ3rdLzBXrSgvyZN2zKDnCL3yhN3IXkBD7xGb4WxBz1mGzzDdXUwk9s4MDSN70BmkccYfvW8qiHUVKGakUwBPDJyf9XsCMbKyoBBF757jOn7kBz4mkA40ZxwlfIDWQghXwjXB2WOLnm3lentggn%2F2i3HKUMqGBVkyCAuBnFHHYbjleEyEBCfFcgUODoSoEAIUrb8FpggWQnDVq468e9MV%2FnphY4XbKuQxExSLLF0CE2NbhvAkbow%2B%2B%2B%2FpQwpZGYOeBd2UspPRmGzkBTz0%2B%2Fan%2Frq9spzSXgq3QTwNxf%2B%2Fy%2B7Ee6P1JxXWkMdyoDRMIdW9wib7BQQHy7TQvkrqIwlfC%2BW3l61Fec1A6DSyx6r6mw74XJIqSOWlZwTUuPtDLmgXT%2FDUXgnEtZe5Vu%2BlcyfDdTlPZ7dXTtZvT2KplrA%2FxMgDiw2TawB6nC1Vzl8q64Y0fEVF9QqKClxYRbTN5RgQ%2BT4mGPCtJ4EgBn5cKp56C6AH6ibV%2FEvGeeQ6DyF4I9mig4YwmoV8YRwfusMx7xK8MRPIww5c33yQY6pgGwiidJw2IrHAmvTH2Y94zAovV02w0se2ruEovWqTKhWToI81i933bu%2B1pxHBp2cgaAx9HzN%2FHHVBVRhxeC1khMH7tbO3M6TwmjBoRqn7RQrdgCDvOgmHrdFnindfa0NZWdqotu6Wm7fVUFbRCXLhmUINYla6jIu%2FgR59D6DsFVFMazulempuOHd9TOf07PEO6bHulTC0JOJmF99Ky0SIIMN3Ktys2d&X-Amz-Signature=7cdaf786885dcaf49159d6a0b2f0515681a0f2d38d3b817712cd1ded30df978b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/655ae48c-f696-4775-9b67-321fc8af6a1f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3VSVU2V%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBW0tgGQE1O2GcTZfd%2FNs%2BDSGzj%2FjD%2FIRKHmJ1b4d%2Fd7AiEA6GdP4DvSCyejSocXNNFzie%2FXPPmIwr23T9TIvV0ckzwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKJBj8u5fzHYfdjAgSrcAwe0%2FWB5NdBxHT3riU45vec%2FSPSRe8VHeXkwGS8YNYWDiSvCvVyRJ8jlNpa7rPmRQ593VCgmoydJ1yRcn%2B%2BKcXHsz2aMstXjBI5BOcant5qcR1lYzLBBYolEUxZCHgBxj0dbjIVnJz2%2BHOgcn45pmawax4zlDlRTxmNhQ2VfOUrwgE%2BAZDpW9rd7IdUu6ZSetsCnVVcT1q4%2BPuA4Dt%2F1Ahv%2Bk5Gg5ZvSztzK4dtDpox1vmTI8yYiP7%2FPCb9nc5ey6Zh%2FSC4cX97Q3hpmsTEJFl9TOfImzMZ9xB0ag9b9SagaVxzOX75tiZBk6LxUYSZh1kSD8YWfsL%2B%2Fn%2B5NnJ%2BTiGOZ%2FLKgkOvnJ6ZSqOrS6%2F9X6blUTbKPULPhbclJX5rntRAExTp4EW2vOo9Gu8CTDCTj8KLvpyI1lO5u47YFLVbxpHAdAlvKiV44vu0IWy4otuMcC9ZQ%2FaHFwHZ1WcxBTWSpZu8pJZ6VZVV9tvv7M44F8C0cG5Dbo4tvK4es4Zb9PceFhtoBUy5xwYOxR1I8QdzqTTRXGCpso7ijmTfPdwFckUKNu347M6Z7jd0ZKqCIixHK%2FhkY9V4oHsemJylyRvQvJ%2BPwt6RRHixS3IoVgcvzgE0eZyAb4ykoM8i%2BMMHO98kGOqUB%2BmS%2BoFEvsCA2Np89RSBvwf6ug7ZYyaoO3CnUlgWIbXfc5tAlp0KLUqxKtJrk7tRUTrCpsk3AqPZC%2B4pnkncvWOyG4sGeBE%2B6RXwID0FCEtxhPtOas1AZZYo2NG4pBYzvBh%2F7XYPNug77BM1hws%2BfdatntU6zhfe5uWCJDIDX8TecjlNGCLF4JyebOtIg30X7FST1qSjKAm3zFvwL1MrT%2BBkbbRGN&X-Amz-Signature=e43b9ef1c751946917872970cf4b43c1766bacc9581e6aab211b3145065bee1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we want to have this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8dcd1760-888e-4e2f-938e-8902a8c020d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZVK6DQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDAOx1cPg5xoBoPHVrpRQUR1htCvmx5wyTC5l1g%2FiJIDwIhAITt7xnuqkCSB6iVWFLD%2BGdSmL%2BlaSGhVTjaIClzuflmKv8DCCcQABoMNjM3NDIzMTgzODA1IgysJM9NUFBn%2B5x6iWoq3APo%2BuLGnj%2B8cnBvPktjFLZiWcT45V2sXSRVwXvIP4nrUgT%2FgQBCrUIx%2F1xRodXk%2BPtq7bVm5pWpx40yjOd9d177R4%2FgZlDfeQypfMTAmgyYkuH31tpkXz9lBxLIZIwzgFRRXXbo81IUnK3%2BD72zoUdc7q7uaEepuw%2BG%2B1oiZp5%2F0X6JVJa%2BqSRs8%2FcwReQj703782vnrHjVBo%2BBbRKoAHXEVvuxcanmeJPXWIo%2FabdPA9YDs4Id7mHnxVvZPbsxtwyYDkNvb%2BlvmnWLoCoeY%2Ftox0DFrjWKQwAabHJiEy2xCgIyRHz3W2brzGCfs98XxKAreicG3Jbvn4CU1NPw6hNbTNfRmCA0q%2BcI6%2BT7Aq%2Bm6hw6xPtF5nhDjyKtVMyDFAup83VhzKr21T4HzPT69p63lKze35asbVZwwB%2B0J51ZdUpNGXxBugbUXHIui092cAIyIlf3A7CL3MVVgCVBc3eKFEABfvgM0kYOHp8D8O%2B1wQs0P%2BtjLHHq%2BNjUnpaAZKrGyUlgDckolxmRVswsckP2Ic6tZYvPQ%2Bx8x1OOgrRVPD9RF7wMvHFDD9Rsh04L1O43Cjx4XY2mW6K8RAeFWVSubLbhhGEwLMawO9ihXnQUEdlovFvBOFPaW4cYtjD5zffJBjqkAW%2BgmA5TBsJIAnjRDPje2H9zTj2WvOfq7EaDGbaWf%2BnB0dwyS06FUml6L3IrMhzmxThVy9P6twmyTd01DLgHI6MMV1PMDtf0pL6iqVA%2B5xQI4IX3onNiHcA%2FwzdjDsjqod3FfLx0LaF64fcf5YcTpbYeuDTbPFxvUbcICgO52Gv%2FEccG9K%2FXlfgvuISs%2BhgGIcBWTggZ1lfitO7vNAurV2c%2BFIOY&X-Amz-Signature=476b29ca16b3f2d04dc46e6f8af1d03505c6effb7e487f78d0f0508f10a0af1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Write a query that does the necessary.

<details>
<summary>Solution</summary>

```sql
SELECT courses.name as 'course name', COUNT(*) as 'number of students'
FROM courses
INNER JOIN
   ENROLLMENTS
        ON courses.id = enrollments.course_id
GROUP BY courses.name
ORDER BY COUNT(*) DESC
```
</details>
---
**SQL queries**
Which of the four queries below produces the following output: 
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/42243842-134c-402b-8764-bc2bac3684d2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZVK6DQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDAOx1cPg5xoBoPHVrpRQUR1htCvmx5wyTC5l1g%2FiJIDwIhAITt7xnuqkCSB6iVWFLD%2BGdSmL%2BlaSGhVTjaIClzuflmKv8DCCcQABoMNjM3NDIzMTgzODA1IgysJM9NUFBn%2B5x6iWoq3APo%2BuLGnj%2B8cnBvPktjFLZiWcT45V2sXSRVwXvIP4nrUgT%2FgQBCrUIx%2F1xRodXk%2BPtq7bVm5pWpx40yjOd9d177R4%2FgZlDfeQypfMTAmgyYkuH31tpkXz9lBxLIZIwzgFRRXXbo81IUnK3%2BD72zoUdc7q7uaEepuw%2BG%2B1oiZp5%2F0X6JVJa%2BqSRs8%2FcwReQj703782vnrHjVBo%2BBbRKoAHXEVvuxcanmeJPXWIo%2FabdPA9YDs4Id7mHnxVvZPbsxtwyYDkNvb%2BlvmnWLoCoeY%2Ftox0DFrjWKQwAabHJiEy2xCgIyRHz3W2brzGCfs98XxKAreicG3Jbvn4CU1NPw6hNbTNfRmCA0q%2BcI6%2BT7Aq%2Bm6hw6xPtF5nhDjyKtVMyDFAup83VhzKr21T4HzPT69p63lKze35asbVZwwB%2B0J51ZdUpNGXxBugbUXHIui092cAIyIlf3A7CL3MVVgCVBc3eKFEABfvgM0kYOHp8D8O%2B1wQs0P%2BtjLHHq%2BNjUnpaAZKrGyUlgDckolxmRVswsckP2Ic6tZYvPQ%2Bx8x1OOgrRVPD9RF7wMvHFDD9Rsh04L1O43Cjx4XY2mW6K8RAeFWVSubLbhhGEwLMawO9ihXnQUEdlovFvBOFPaW4cYtjD5zffJBjqkAW%2BgmA5TBsJIAnjRDPje2H9zTj2WvOfq7EaDGbaWf%2BnB0dwyS06FUml6L3IrMhzmxThVy9P6twmyTd01DLgHI6MMV1PMDtf0pL6iqVA%2B5xQI4IX3onNiHcA%2FwzdjDsjqod3FfLx0LaF64fcf5YcTpbYeuDTbPFxvUbcICgO52Gv%2FEccG9K%2FXlfgvuISs%2BhgGIcBWTggZ1lfitO7vNAurV2c%2BFIOY&X-Amz-Signature=1e0c88390da2877581665eb771168760f3d6ae60aafed80fa568dcdb0908e070&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<u>Query 1</u>
<u>Query 2</u>
```sql
SELECT COUNT(DISTINCT category)
	as 'number of courses'
FROM courses
```

<u>Query 3</u>
```sql
SELECT name
	as 'number of courses'
FROM courses
GROUP BY COUNT(*)
```

<details>
<summary>Solution</summary>

Query 1
</details>
```sql
SELECT COUNT(*)
	as 'number of courses'
FROM courses
```

<u>Query 4</u>
```sql
SELECT DISTINCT COUNT(*)
	as 'number of courses'
FROM courses
```
---
**SQL queries**
Which of the four queries below produces the following output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/afb3d2ea-66c0-4a3c-8b6c-1aed883fd9a7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEZVK6DQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDAOx1cPg5xoBoPHVrpRQUR1htCvmx5wyTC5l1g%2FiJIDwIhAITt7xnuqkCSB6iVWFLD%2BGdSmL%2BlaSGhVTjaIClzuflmKv8DCCcQABoMNjM3NDIzMTgzODA1IgysJM9NUFBn%2B5x6iWoq3APo%2BuLGnj%2B8cnBvPktjFLZiWcT45V2sXSRVwXvIP4nrUgT%2FgQBCrUIx%2F1xRodXk%2BPtq7bVm5pWpx40yjOd9d177R4%2FgZlDfeQypfMTAmgyYkuH31tpkXz9lBxLIZIwzgFRRXXbo81IUnK3%2BD72zoUdc7q7uaEepuw%2BG%2B1oiZp5%2F0X6JVJa%2BqSRs8%2FcwReQj703782vnrHjVBo%2BBbRKoAHXEVvuxcanmeJPXWIo%2FabdPA9YDs4Id7mHnxVvZPbsxtwyYDkNvb%2BlvmnWLoCoeY%2Ftox0DFrjWKQwAabHJiEy2xCgIyRHz3W2brzGCfs98XxKAreicG3Jbvn4CU1NPw6hNbTNfRmCA0q%2BcI6%2BT7Aq%2Bm6hw6xPtF5nhDjyKtVMyDFAup83VhzKr21T4HzPT69p63lKze35asbVZwwB%2B0J51ZdUpNGXxBugbUXHIui092cAIyIlf3A7CL3MVVgCVBc3eKFEABfvgM0kYOHp8D8O%2B1wQs0P%2BtjLHHq%2BNjUnpaAZKrGyUlgDckolxmRVswsckP2Ic6tZYvPQ%2Bx8x1OOgrRVPD9RF7wMvHFDD9Rsh04L1O43Cjx4XY2mW6K8RAeFWVSubLbhhGEwLMawO9ihXnQUEdlovFvBOFPaW4cYtjD5zffJBjqkAW%2BgmA5TBsJIAnjRDPje2H9zTj2WvOfq7EaDGbaWf%2BnB0dwyS06FUml6L3IrMhzmxThVy9P6twmyTd01DLgHI6MMV1PMDtf0pL6iqVA%2B5xQI4IX3onNiHcA%2FwzdjDsjqod3FfLx0LaF64fcf5YcTpbYeuDTbPFxvUbcICgO52Gv%2FEccG9K%2FXlfgvuISs%2BhgGIcBWTggZ1lfitO7vNAurV2c%2BFIOY&X-Amz-Signature=3b472ac6a5420872aa4e03c911436296ab6b3d4d80cfb51cf466f5d729742a42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Remember the relationships between the tables:
- Courses `1:m` Enrolments
- One course can have many enrolments
- One enrolment belongs to one course
- Students `1:m` Enrolments
- One student can have many enrolments
- One enrolment belongs to one student
- Grades `1:1` Enrolments
- One grade belongs to one enrolment
- One enrolment has one grade

<u>Query 1</u>
```sql
SELECT students.first_name, students.last_name, AVG(grades.grade) as 'avg_grade'
FROM courses
INNER JOIN
	enrollments
		ON courses.id = enrollments.course_id
INNER JOIN
	students
		ON students.enrollment_id = enrollments.id
INNER JOIN
	grades
		ON grades.id = enrollments.grade_id
GROUP BY students.id
ORDER BY AVG(grades.grade) DESC
LIMIT 10
```
<u>Query 2</u>
```sql
SELECT students.first_name, students.last_name, AVG(grades.grade) as 'avg_grade'
FROM courses
INNER JOIN
	enrollments
		ON courses.id = enrollments.course_id
INNER JOIN
	students
		ON students.enrollment_id = enrollments.id
INNER JOIN
	grades
		ON grades.enrollment_id = enrollments.id
GROUP BY students.id
ORDER BY AVG(grades.grade) DESC
LIMIT 10
```
<u>Query 3</u>
```sql
SELECT students.first_name, students.last_name, AVG(grades.grade) as 'avg_grade'
FROM courses
INNER JOIN
	enrollments
		ON courses.enrollment_id = enrollments.id
INNER JOIN
	students
		ON students.id = enrollments.student_id
INNER JOIN
	grades
		ON grades.enrollment_id = enrollments.id
GROUP BY students.id
ORDER BY AVG(grades.grade) DESC
LIMIT 10
```
<u>Query 4</u>
```sql
SELECT students.first_name, students.last_name, AVG(grades.grade) as 'avg_grade'
FROM courses
INNER JOIN
	enrollments
		ON courses.id = enrollments.course_id
INNER JOIN
	students
		ON students.id = enrollments.student_id
INNER JOIN
	grades
		ON grades.enrollment_id = enrollments.id
GROUP BY students.id
ORDER BY AVG(grades.grade) DESC
LIMIT 10


```

<details>
<summary>Solution</summary>

Query 4
Based on the information about the relationships between the tables you must think about which table has what Foreign Keys to establish these relationships.
For example, in query 3 we join on `courses.enrollment_id = enrollments_id`
This would imply that one enrolment can have many courses and one course only one enrolment as `enrollment_id` is a Foreign Key in table Courses. However, the opposite is the case: `course_id` is a Foreign Key in Enrollments table (see query 4).
</details>
---
**Relationships between tables**
Look at the three tables below and answer the following questions.
- What type of relationship exists between table Students and Courses?
- What type of relationship exists between table Students and Enrolments?
- What type of relationship exists between table Courses and Enrolments?
- In table Enrolments, which column(s) are Primary Key(s) and which are Foreign Key(s)?
- What was the reason why table Enrolments was created?
<u>Table Students</u>
<u>Table Enrolments</u>
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7860251e-e68c-4a7f-a413-d6ddfd5fd578/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKAUGAPE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBws6P5KsCGOKzjRgYL9lN4G%2B61vY9gumEY4VeutMQoKAiEAv5kGLgpyEFXlW1fSz4fACIQjK%2FnjeCBI1gxwp6siE9Yq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFOIV2cM%2FLp3XXnH6ircA3hQJ%2BpfB9JXwq4CHchrAgUhLLvjgLilzdEaMWi6Ie4HGQm1QpFsFyI1J0AvminyZzZSAOjOzq8Cf7z0jLU0d8%2FIZTTIefNApyqGT23e8ezJZGKKIE5Or9cKj%2BO6SwXC%2FmnRoyw%2Fb%2FoZRvN1HfJ79hheSVmEfLYNHvt9CwErX0th0dnxVsp%2Fae2Gnnd27JwVKW%2FwoWZTRYad2LKpVrhLGFNnmwQxkLSDYQEuT3ekmMMX7FD9pKVlWkpsrg3LqEvZXhUzQzxP6XhAHK1r3lGK5c8WZRd4f8idA9HC2UPhvChgjLqbhuZxlGCpj7G7T77nnwm8MJRGoWnFOt%2F8ol%2BzVqjKE5wid82AFb5Jkwq8WOY3pbRZxw5X%2B3Ln0ZTyPgoGUpS13AKXF3sCfBVHK6NnXg28xUvmOthq0tT8Q3DdSvXTTLWTdWEnARFCX2J1NBAYBdyu%2BrsYW%2BzEUPMvbrw9MjndlGOukk%2BeGovAmMAKWqt5FLAFVbW2fXXuDMd8D1Bx1fWRd6u9P8RfponmXslqYr2cB5MquDiQ2LIv%2FRuviWMXXTg2XUime5cns%2FHt2t1ZsVnNr4AiWi85QBLL9lasXn9cODwb5A7jho7qeOZJcFNeowNPSgNeEC%2FFunVeMLbO98kGOqUBcXF%2Bgacd%2FdS4wUvnH2%2Bq57vAtk5MZxCSYq%2BwihRSYLgPFtqlFP5hPbs%2BN%2FkAeL1zhk1cxDc6zXLlVpXD27fJ5tlC5%2BKvSJzv9MCzoi1KYJDxUOKG2HmBswEwG7aOBrGCBjnqF3u9UZCKQ3UYPiDPbIrcyMIgqsCTWq7oMp%2FtgDH1sGiPFRHzYDrDcvSFBktH9EPMFQ6ElcMzk5kJSr8XKsXTWvSJ&X-Amz-Signature=e03d2f6a3883db55a2077a4edb62c366fc681ba1e86c14ef409addce6f946a44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<u>Table Courses</u>
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cbabca09-d632-450b-9e21-c60709d4161d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKAUGAPE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBws6P5KsCGOKzjRgYL9lN4G%2B61vY9gumEY4VeutMQoKAiEAv5kGLgpyEFXlW1fSz4fACIQjK%2FnjeCBI1gxwp6siE9Yq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFOIV2cM%2FLp3XXnH6ircA3hQJ%2BpfB9JXwq4CHchrAgUhLLvjgLilzdEaMWi6Ie4HGQm1QpFsFyI1J0AvminyZzZSAOjOzq8Cf7z0jLU0d8%2FIZTTIefNApyqGT23e8ezJZGKKIE5Or9cKj%2BO6SwXC%2FmnRoyw%2Fb%2FoZRvN1HfJ79hheSVmEfLYNHvt9CwErX0th0dnxVsp%2Fae2Gnnd27JwVKW%2FwoWZTRYad2LKpVrhLGFNnmwQxkLSDYQEuT3ekmMMX7FD9pKVlWkpsrg3LqEvZXhUzQzxP6XhAHK1r3lGK5c8WZRd4f8idA9HC2UPhvChgjLqbhuZxlGCpj7G7T77nnwm8MJRGoWnFOt%2F8ol%2BzVqjKE5wid82AFb5Jkwq8WOY3pbRZxw5X%2B3Ln0ZTyPgoGUpS13AKXF3sCfBVHK6NnXg28xUvmOthq0tT8Q3DdSvXTTLWTdWEnARFCX2J1NBAYBdyu%2BrsYW%2BzEUPMvbrw9MjndlGOukk%2BeGovAmMAKWqt5FLAFVbW2fXXuDMd8D1Bx1fWRd6u9P8RfponmXslqYr2cB5MquDiQ2LIv%2FRuviWMXXTg2XUime5cns%2FHt2t1ZsVnNr4AiWi85QBLL9lasXn9cODwb5A7jho7qeOZJcFNeowNPSgNeEC%2FFunVeMLbO98kGOqUBcXF%2Bgacd%2FdS4wUvnH2%2Bq57vAtk5MZxCSYq%2BwihRSYLgPFtqlFP5hPbs%2BN%2FkAeL1zhk1cxDc6zXLlVpXD27fJ5tlC5%2BKvSJzv9MCzoi1KYJDxUOKG2HmBswEwG7aOBrGCBjnqF3u9UZCKQ3UYPiDPbIrcyMIgqsCTWq7oMp%2FtgDH1sGiPFRHzYDrDcvSFBktH9EPMFQ6ElcMzk5kJSr8XKsXTWvSJ&X-Amz-Signature=8aad201e0611cfdcffc74eb4057824661d03122cf4a90d626b7ca6b2fb23531d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7e1c0470-ce21-4d6a-a1a7-16214fa6fc4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KFVT3OS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICo4h3y7oeOolT9ouODausuqhu0KPRWbWvB4QY51D5dxAiBiqzHmuihpvPe0XIzSsthnJy4W5WAKBd9oiyEFQYMG2yr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMB7DHhe8qMZJnuWJRKtwDh8g7rVdPdrmlxKy6PgKXTWlofMpsB8HKBSr%2BtVFaPKU%2BbQ0KB%2B5RsKnCIJjv%2FbGjDS%2BK2g95rofwOudBEyu2VncaXH%2FrJIi5FCBqXp2l2qBN3Qub1ZSsq8a3xoHVXtWokJ9UVJw7gOVRu1roZaVhm9kPfiernAUNEhidaqUrFKPdivA9%2Fgu3fhGVTyjQvsRDzV%2F%2Fo%2BX0UKiza8a1OLaK0RZDah50pVvsGwv35uD1xtj%2F2xZ1UYLRj%2BIhOo9splpzMMaBcel%2Bo18u02jvY93nrZiMtnIiHLoo5M8uv5ij9s%2FjmfM12hyvf4yOT0zYVWKRfahcIt9VGf%2FTY4NUbiPxZZZXfSd8yCaGqo8S0Ranbl3JWiDNxDteWuLK%2Fp6MNgb92n%2Fj%2Fba0XmMNW8t4SOlhmQKpOgSiNMBHKpkLxd%2BWmsJceclTiGzsymbnHs9%2BDirxsWJ8%2FdjeQKbxzf%2BvHSB9QNOjM45h8FCX3XvBPw7W6kPxcP0r40N2JnTXVZ8cSRz9%2Bdv%2B6WDcKdj4cXrd8lzuRltqtaMbmWt0GJ%2Ff8Y8QUB4p6APge8rxZpCw967EsTkXDc7JZBx0MS8OhqVc%2BjmDIfNx5owig7MIxrBgfPOJvkSUbY1aCRCxPK0vM%2FMw6c73yQY6pgF1f%2BZxmT0ahkWdslBhqLi7KHnj%2BSdNZy5e0Y%2BGmWFEZjA2oOwLiUbzz98xkGqWYgDzdNEPFpBL5tgPTw0kK0gJpuVslveEb9wIMu%2BazzxmAyLZcH2rJhok3u4EV3jP2ygLl6%2FDLPeoWH54VkETQQskZ4mULdlisgQ6sPrBkFbV17hEZmTCqNEcJ2CPQe6Zdk8Fg4IESbVpDoKiVWGjF0k%2FX8gwolCe&X-Amz-Signature=333909e8fd3126ba927cb782326217be89557998b600c358b714defdd2d2f99f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Solution</summary>

- m:n → One student can visit multiple courses and one course can be visited by multiple students
- 1:m → One enrolment belongs to exactly one student. One student can have many enrolments
- 1:m → One enrolment belongs to exactly one course. One course can have many enrolments.
- Foreign Keys: `student_id` and `course_id`, Primary Key: `id`
- Because there is an m:n relationship between Students and Courses. Therefore it was necessary to create this mapping table Enrolments in between so that the relationship is split up into two 1:m relationships.
</details>
---

📄 **[OOP]** (subpage)
---
**Creating new class instances**
Which of the following class methods is called when a new object is created?
- `__str__()`
- `__repr__()`
- `__init__()`
- `__cons__()`

<details>
<summary>Solution</summary>

`__init__()` is the constructor of a class and is called whenever a new object of this class is instantiated.
</details>
---
**Constructor**
What is wrong with the code below?
```python
class Lecturer():

  def __init__(name, birthday, employee_id, experience, department):

    self._name = name
    self._birthday = birthday
    self._employee_id = employee_id
    self._experience = experience

    self.department = department
```

<details>
<summary>Solution</summary>

The keyword `self` is missing as first parameter in the constructor.
</details>
---
**Constructor**
We have defined the following class Lecturer:
```python
class Lecturer():

  def __init__(self, name, birthday, employee_id, experience, department='ICS-HSG'):

    self._name = name
    self._birthday = birthday
    self._employee_id = employee_id
    self._experience = experience

    self.department = department
```
What is the output of the code snippet below?
```python
marco = Lecturer('Marco Müller', '01.01.1960', '99-3344-55', 5)
marco.department
```

<details>
<summary>Solution</summary>

`'ICS-HSG'`
`department=` is an optional parameter, if no value is provided then ‘ICS-HSG’ is used.
</details>
---
**Private attributes**
What is the general motivation behind declaring class attributes as private?
- [ ] 1) Private attributes are simpler to implement
- [ ] 2) We have better control over who can access and modify attributes that are private
- [ ] 3) It is general Python standard to declare public and private attributes for an class
- [ ] 4) We can make these attributes only accessible to members of the class and not to anyone else (assume it would be technically supported to do so)

<details>
<summary>Solution</summary>

2, 4
Inside the getter and setter methods we can define conditions that specify under conditions that must be met in order to access or modify the attribute.
Member of the class means that on the object itself we can access and modify the attributes (inside the getter and setter methods)
</details>
---
**Private attributes**
When we have defined a private class attribute, e.g., `Student._student_name` then we are not able to access or modify the attribute without a getter and setter methods. True or False?

<details>
<summary>Solution</summary>

False
Although we set the attribute to private, which we see by looking at the naming convention `_<< attribute name>>`, we can still access and modify it without getter and setter methods,* e.g. *`janick.student_name = 'Elia'` would still work → it is all in the responsibility of the developer.
</details>
---
**Getter and setter methods**
We have the following class Student:
```python
class Student():

  def __init__(self, name, birthday, student_id, gpa):
   
		
    self._name = name
    self._birthday = birthday
		self._student_id = student_id

		self.exp_graduation = exp_graduation
		self.gpa = gpa
```
Implement for the private attribute `_birthday` its getter and setter method.

<details>
<summary>Solution</summary>

```python
# getter method
@property
def birthday(self):
   return self._birthday

# setter method
@birthday.setter
def birthday(self, birthday):
  self._birthday = birthday
```
</details>
---
**Special methods**
We have the following class Student:
```python
class Student():

  def __init__(self, name, birthday, student_id, gpa):
   
		
    self._name = name
    self._birthday = birthday
		self._student_id = student_id

		self.exp_graduation = exp_graduation
		self.gpa = gpa

	...
	...

	def __repr__(self):
    return (
	        f'StudentID: {self._student_id}, '
        + f'Name: {self._name}, '
				+ f'Birthday: {self._birthday}'
    )

  def __str__(self):
    return (
          f'StudentID: {self._student_id}, '
        + f'Name: {self._name}'
    )
```
We create a new instance of this class:
```python
janick = Student('Janick Spirig', '25.02.1997', '15-538-085', 7.0)
```
What is the output of the following two commands?
```python
janick
```
```python
print(janick)
```

<details>
<summary>Solution</summary>

```python
StudentID: 15-538-085, Name: Janick Spirig, Birthday: 25.02.1997
```
→ the `__repr__()` method is called
```python
StudentID: 15-538-085, Name: Janick Spirig
```
→ the `__str__()` method is called
</details>
---
**Inheritance**
We have the following class Lecturer:
```python
class Lecturer(Person):

  def __init__(self, name, birthday, employee_id, experience):
		
		### YOUR CODE ###

    self._experience = experience
```
Answer the following questions:
- What is the parent class of Lecturer?
- What line of code do we need to implement at `### YOUR CODE ###`?

<details>
<summary>Solution</summary>

Person is the parent class which can be seen in the class header `class Lecturer(Person)`
We must call the constructor of the parent class to create a Person object, which we can do with the following line of code:
```python
super().__init__(name, birthday, employee_id)
```
</details>
---
**Inheritance**
With which method can we check if a class instance is a child of its parent class?
For example, lets say we create a new lecturer:
```python
marco = Lecturer('Marco Müller', '11.02.1975', '12-9382-12', 5)
```
Which command allows us to check if `marco` is a child of its parent class?

<details>
<summary>Solution</summary>

We can use `isinstance()` method → `isinstance(marco, Person)` → True
</details>
---
**Inheritance**
We have defined the class Person and Student.
```python
class Person:
  def __init__(self, name, birthday, person_id):
    self.name = name
    self.birthday = birthday
    self.person_id = person_id

  def __repr__(self):
    return (
          f'{self.name}, '
        + f'{self.person_id}'
    )

  def __str__(self):
    return (
        f'{self.name}'
    )


class Student(Person):

  def __init__(self, name, birthday, student_id, gpa):
    
    super().__init__(name, birthday, student_id)

    self._gpa = gpa

  @property
  def gpa(self):
    return self._gpa

  @gpa.setter
  def gpa(self, gpa):
    self._gpa = gpa

  def __repr__(self):
    return (f'I am the student {super().__str__()} and my GPA is {self._gpa}!')

  def __str__(self):
    return (f'I am the student {super().__repr__()} and my GPA is {self._gpa}!')
```
Allocate the two code snippets below to an output option.
```python
# CODE 1
marc = Student('Marc Hauser', '11.01.1996', '198-234-532', 5.1)
marc
```
```python
# CODE 2
marc = Student('Marc Hauser', '11.01.1996', '198-234-532', 5.1)
print(marc)
```

**Outputs**
- [ ] 1) I am the student Marc Hauser, 198-234-532 and my GPA is 5.1!
- [ ] 2) I am the student Marc Hauser and my GPA is 5.1!
- [ ] 3) error
- [ ] 4) I am the student and my GPA is 5.1!

<details>
<summary>Solution</summary>

CODE 1 → Output 2
Here the `Student.__repr__()` method is called and then `Person.__str__()` 
CODE 2 → Output 1
Here the `Student.__str__()` method is called and then `Person.__repr__()`

</details>
---
**Accessing private attributes**
What is the output of the code snippet below?
```python
class Student():

  def __init__(self, name, birthday, student_id, entry_year, exp_graduation, gpa):

    # private attributes
    self._name = name
    self._entry_year = entry_year

    # public attributes
    self.exp_graduation = exp_graduation
    self.gpa = gpa
    self.enrolled_courses = []

  @property
  def entry_year(self):
    if len(self._name.split('a')) > 3:
      return self._entry_year
    elif len(self._name) > 7:
      return 2020
    else:
      return 2019

  @entry_year.setter
  def name(self, entry_year):
    self._entry_year = entry_year



annalena = Student('Annalena', '12.02.1996', '123-523-675', 2019, 2022, 5.1)
annalena.entry_year
```

<details>
<summary>Solution</summary>

2020
In the getter method we check whether the student name contains more than three ‘a’. This evaluates to False, in the elif we check whether the student name has more than 7 letters, this evaluates to True as ‘Annalena’ has 8 letters. Thus, 2020 is returned.
</details>
---
**Polymorphism & encapsulation**
Decide for each statement below whether it is True or False.
- [ ] 1) Polymorphism allows us to have a method with the same name for two different child classes and makes sure that the right one is being executed.
- [ ] 2) Polymorphism allows us to group common attributes and methods of two classes on a parent class and inherit these from the parent class.
- [ ] 3) We don’t violate against encapsulation when we add a course to a student from whitin the Course class.
- [ ] 4) Encapsulation describes the idea of binding all methods and data related to a class under this specific class together. 

<details>
<summary>Solution</summary>

True
False → this is inheritance
False → we violate against encapsulation as we manipulate the Student data from outside the class
True
</details>
---
📄 **[Data Science]** (subpage)
---
**Data types**
Define for each item below whether they are Nominal, Ordinal, Interval or Ratio data. 
- Hair colour
- Time
- IQ
- Weight
- Gender
- Job seniority level
- Date
- Weight

<details>
<summary>Solution</summary>

| Hair colour | Nominal |
| --- | --- |
| Time | Interval |
| IQ | Interval |
| Weight | Ratio |
| Gender | Nominal |
| Job seniority level | Ordinal |
| Date | Interval |
| Weight | Ratio |
</details>
---
**Data types**
Define for each statement below whether it is True or False
- [ ] 1) Ordinal data have equal spacing
- [ ] 2) Nominal data can be segmented into categories
- [ ] 3) Ratio data have a true zero
- [ ] 4) Interval data have equal spacing and can be put into a rank order
- [ ] 5) Ordinal data can be segmented into categories, can be put into a rank order but do not have equal spacing

<details>
<summary>Solution</summary>

False → no equal spacing
True
True
True
True

</details>
---
**Numpy**
What is one major advantage of numpy array over conventional lists?
- [ ] 1) In a numpy array we can store even more different kind of data types
- [ ] 2) Numpy arrays are not limited in the number of dimensions they can represent
- [ ] 3) With numpy arrays we can do calculations element-wise over entire arrays

<details>
<summary>Solution</summary>

`C`
</details>
---
**Pandas**
What does the method `.read_csv()` return?
- [ ] 1) DataTable
- [ ] 2) DataFrame
- [ ] 3) DataSeries
- [ ] 4) Numpy Array

<details>
<summary>Solution</summary>

2 → DataFrame
</details>
---
**Pandas**
If the data in a .csv file is not comma separated, we cannot use the `.read_csv()` method. True or False?

<details>
<summary>Solution</summary>

False
We can still use the method, but we must provide a value for the `delimiter=` parameter as this is by default set to comma (`delimiter=','`)
</details>
---
**Pandas**
Which parameter allows us to specify our own column names when using the .read_csv() method?
- [ ] 1) `column_names=`
- [ ] 2) `columns=`
- [ ] 3) `headers=`

<details>
<summary>Solution</summary>

`columns=`
</details>
---
**Pandas**
Which value do we need to assign to the `axis=` parameter if we want to drop a Column or a Row?
- [ ] 1) Column: `axis = 0`, Row: `axis = 0`
- [ ] 2) Column: `axis = 1`, Row: `axis = 0`
- [ ] 3) Column: `axis = 0`, Row: `axis = 1`
- [ ] 4) Column: `axis = 1`, Row: `axis = 1`

<details>
<summary>Solution</summary>

2) Column: `axis = 1`, Row: `axis = 0`
</details>
---
**Pandas**
Which value do we need to assign to the `axis=` parameter if we want to compute the sum for a Column or a Row?
- [ ] 1) Column: `axis = 0`, Row: `axis = 0`
- [ ] 2) Column: `axis = 1`, Row: `axis = 0`
- [ ] 3) Column: `axis = 0`, Row: `axis = 1`
- [ ] 4) Column: `axis = 1`, Row: `axis = 1`

<details>
<summary>Solution</summary>

3) Column: `axis = 0`, Row: `axis = 1`
</details>
---
**Pandas**
How many rows do the functions `.head()` and `.tail()` return?
- [ ] 1) 5
- [ ] 2) 10
- [ ] 3) 15
- [ ] 4) 20

<details>
<summary>Solution</summary>

1
</details>
---
**Pandas**
The `.min()` and `.max()` methods can be applied on an entire DataFrame and on a single column. True or False?

<details>
<summary>Solution</summary>

True
If we apply these methods on the entire DataFrame, e.g., `df.min()`, a Series is returned that contains the minimum value for each column.
</details>
---
**Pandas**
Which information does the `.describe()` method return?
- [ ] 1) Mean value
- [ ] 2) Mode value
- [ ] 3) Variance
- [ ] 4) Median value
- [ ] 5) Number of values
- [ ] 6) First quartile
- [ ] 7) Skewness
- [ ] 8) Second quartile
- [ ] 9) Third quartile
- [ ] 10) Minimum value
- [ ] 11) Maximum value
- [ ] 12) Standard deviation

<details>
<summary>Solution</summary>

1, 2, 4, 5, 6, 8, 9, 10, 11, 12
</details>
---
**Pandas**
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3KRXSO7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD0Q1tJXQpGjS7ulotvHULKo8EPiezfDxF9JEh7qJwq3QIhALcauY7Btr%2BYLumeSLEk2G2jYvrhxAnRPVBR%2FDoo0q%2FOKv8DCCgQABoMNjM3NDIzMTgzODA1IgxRffy9vH%2BYiabQykQq3AN%2FgoYmxZfv8n6RzH0JYLRefd%2FggWFadiExzM4n9J50lBCByIBT5nQTJ6hGmjEpbTxRVD5mDJUDgYrF05%2BDEn%2BJL056AZ3nt%2BxWe4on5I7V%2BB%2BGn3LnCeN%2FBbcPwvMvepFMS3vrrguhO6nf4%2Boec%2BjfOVToYoVNd49ote7HOmBZcOiUPoHejyXeLQ1xH3X6RuuoOEGQQC32w3WSmhu%2FScoAF4WCyzwzzqcoagfD38DFGXC4PkoYQlk%2FT9nKmA0QtMCBkopQoW8qTGEy8LG0XPetrS%2Fyz2elwxYp8uIkTCYghSdwAEBGcwA%2Bpnu5lzSm%2FsjbBB4WsTu5LD%2F490Uqvo1O8Sapw6vJ1APN0W6Y8X5%2B3JQGh74B5mee8XOTl1%2BGqUiaJv1FUaTKShyHaLx8qZTTSZ983t9d7PH0QLEvB1JU6PUYmIs3rGKdayuohB%2BfUBLCp8VdFbj2Fg3Df9IInLxW1qdgL4gX%2FKgvcyRyZWuJdvCpls5HASxpnzztIMm5ePMM9VLFWAlDdjxqxIMTw8GZhyYC0%2Fxndc88ocENHMvqCUX08A%2Btz%2BUM8OiYEKm6b3N9s92FjATBGnVV50AFFkw9PkWqS3YxO13Ie%2BKeQvWwn8Hx%2BIYBoRSY2WkBjDDAz%2FfJBjqkAbZ2v66bS03C6UcFcHVpqqQtxXdiO%2B0oxBFgiMxFvq6HbDhYcAHDFPSP8noeiaHOMFFca%2BuAg0H3yJ5pk%2Bjt4y6vdOMfoIRJHTaxzCQyGPmfZCPzmXnBr4olpDiq40ZoWoD28GLG%2B3uMt1bVCaviHTS8vNe51rtQMgMivOzQvuesPRRt%2F1%2BvPilcVJjwCdzrbBiwqAJJFubWA%2FdhGSMiARt30%2BQ0&X-Amz-Signature=5f4b27ef48ffa47eb0b53d5a7bf0e93c6c752637f7ddd57e5432b31cb4622cc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can we access all rows in `my_df` that have a value for `calories` bigger than 300 and a value for `duration` bigger than 40?

<details>
<summary>Solution</summary>

`df.loc[(df['calories'] > 300) & (df['duration'] > 40)]`
OR
`df[(df['calories'] > 300) & (df['duration'] > 400)]`

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b9273317-ed78-4094-b212-ec015d413af7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZZOTLZF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDaymlBWwDPaYRw28gG6wyffaq%2FAZbokDyvKvXRahs2mwIhAI%2Fzbr5ApeHN2eNhp8Q%2F6ct9NcCA0qEppVaNlRje3JXUKv8DCCcQABoMNjM3NDIzMTgzODA1Igx%2BPXTtYL4gohtUoHwq3AO8lJUxkVm7usURlAVV9VQC5TJdj6TR51tGGZx%2BwQpBRRQOwyQDlNmjTbJyRbpscVqkmkBK8YWwaxFRVSt65%2FDHNdauKRWaJUbSr6aYOlOJnSNxZcQ%2Fci1Nx%2FB1FkQeGt2%2BF%2F2S4Qvl516XIqb9tRm3kxiJZF0B765%2FIxOeTW%2FXLnivcj6KoaJaJTH63HH1AWaZtKtJY%2BOAMZNQMT7uWlKqVCNkszS%2Fg3ZGJrY83HFNBGR7I0WIOmXp0MJn5r7Z1vsr%2Fgl8pQzPuHhZtkaYRebSedfvViLAfgp4SKjKDGl2LCFjkuXrSz17nq8IMp6iO6ebqD5XiK1i6wgSdWKAnUHpXC5gyJNAr2LvQ6kY%2Fh7PTPdrv2gLztou4Uereq8hAnvPNGUXb75a1JtuqVqZqW7byCTzeiffhjUedd6wSf6m5JdockG6fWmNfq8nNKsXySN3kG03%2FCn8NshzcejtqaedLlVkJ5YdtDCV8M4WtquU%2FXy52ml7AncjvJKaFxLwYmZ28NLi0DOSGf2zKeDWBgT8M%2B16s7U%2BEjRXf60wW2qRaSLmwmmb5kVf5G964JqWiH%2F%2BomIJKKxxDEub7gTObMub%2F8wA6h5O6tNfJuxOsO1hAZHozpxmP3P9%2FbcGcDCwzvfJBjqkAcX6OwigDqjBQhpq5ie72UlEPyN08R%2BHi08Z%2FsrdiVcNf7XQFfKu5FCnPJwwWPt%2FoIJFBi6bzLj9b7ivjtc3MMan2xwaftEUlLrZtMe5Q5iJSSGMg2gIg%2BjimfhCBY6GsoROymkuKhu7bTnTJpQqiG1fpkJmEErJNJbNQh%2BbReBzKOmsryWMUyEFr4eusPqxqAicwvfhLyClcuVtr5EE0FkZJLBP&X-Amz-Signature=624cd0ad34285eb500e8ba0956322982d0c68cca0f77bca76834685f418ab93a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
**Pandas**
The `.sort_values()` method is case sensitive which is why the value `'Zurich'` would be placed before the value `'basel'`. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Matplotlib**
A Matplotlib figure can have mutiple Axes. True or False?

<details>
<summary>Solution</summary>

True
In a Figure of subplots for example, each subplot is one separate Axes
</details>
---
**Matplotlib**
When we create a Figure of multiple subplots we create first all the empty subplots and then fill them one after the other with data. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Matplotlib**
Let’s assume we want to visualise the Age, Height and Weight of 10 different people. To do so, we create a Multiple Barchart. Thus, the name of each person is displayed at the x-axis and has three bars in this order (from left to right): Age (blue), Height (red), Weight (green). 
In the image below we see the bar groups of the first two persons:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3888d003-fe6a-493c-8a99-7b5b73692a67/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3KRXSO7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD0Q1tJXQpGjS7ulotvHULKo8EPiezfDxF9JEh7qJwq3QIhALcauY7Btr%2BYLumeSLEk2G2jYvrhxAnRPVBR%2FDoo0q%2FOKv8DCCgQABoMNjM3NDIzMTgzODA1IgxRffy9vH%2BYiabQykQq3AN%2FgoYmxZfv8n6RzH0JYLRefd%2FggWFadiExzM4n9J50lBCByIBT5nQTJ6hGmjEpbTxRVD5mDJUDgYrF05%2BDEn%2BJL056AZ3nt%2BxWe4on5I7V%2BB%2BGn3LnCeN%2FBbcPwvMvepFMS3vrrguhO6nf4%2Boec%2BjfOVToYoVNd49ote7HOmBZcOiUPoHejyXeLQ1xH3X6RuuoOEGQQC32w3WSmhu%2FScoAF4WCyzwzzqcoagfD38DFGXC4PkoYQlk%2FT9nKmA0QtMCBkopQoW8qTGEy8LG0XPetrS%2Fyz2elwxYp8uIkTCYghSdwAEBGcwA%2Bpnu5lzSm%2FsjbBB4WsTu5LD%2F490Uqvo1O8Sapw6vJ1APN0W6Y8X5%2B3JQGh74B5mee8XOTl1%2BGqUiaJv1FUaTKShyHaLx8qZTTSZ983t9d7PH0QLEvB1JU6PUYmIs3rGKdayuohB%2BfUBLCp8VdFbj2Fg3Df9IInLxW1qdgL4gX%2FKgvcyRyZWuJdvCpls5HASxpnzztIMm5ePMM9VLFWAlDdjxqxIMTw8GZhyYC0%2Fxndc88ocENHMvqCUX08A%2Btz%2BUM8OiYEKm6b3N9s92FjATBGnVV50AFFkw9PkWqS3YxO13Ie%2BKeQvWwn8Hx%2BIYBoRSY2WkBjDDAz%2FfJBjqkAbZ2v66bS03C6UcFcHVpqqQtxXdiO%2B0oxBFgiMxFvq6HbDhYcAHDFPSP8noeiaHOMFFca%2BuAg0H3yJ5pk%2Bjt4y6vdOMfoIRJHTaxzCQyGPmfZCPzmXnBr4olpDiq40ZoWoD28GLG%2B3uMt1bVCaviHTS8vNe51rtQMgMivOzQvuesPRRt%2F1%2BvPilcVJjwCdzrbBiwqAJJFubWA%2FdhGSMiARt30%2BQ0&X-Amz-Signature=f38fef8f0e5b41e54f1f61d6059fa2ff77ef906458081d47c800bc77d2e19370&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Each bar has a width of 0.2
What are the x-axis positions of the four points in the image below?

<details>
<summary>Solution</summary>

-0.2, 0.2, 0.8, 1.2 
The middle of the red bar of the first person is at position 0 and has a width of 0.2. Thus, it leans 0.1 to the left and 0.1 to the right. The half of the blue and green bars also leans to the left and right. Thus, their middle must be placed at -0.2 and 0.2 respectively.
Same calculation for the second person, whose red middle bar is placed at position 1.
</details>
---
**Seaborn**
Seaborn is built on top of Matplotlib and its main benefit is its simplicity to use. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Chart interpretation**
Look at the Boxplot shown below:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ef351802-9321-4c8c-804f-9a26069cb8ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3KRXSO7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD0Q1tJXQpGjS7ulotvHULKo8EPiezfDxF9JEh7qJwq3QIhALcauY7Btr%2BYLumeSLEk2G2jYvrhxAnRPVBR%2FDoo0q%2FOKv8DCCgQABoMNjM3NDIzMTgzODA1IgxRffy9vH%2BYiabQykQq3AN%2FgoYmxZfv8n6RzH0JYLRefd%2FggWFadiExzM4n9J50lBCByIBT5nQTJ6hGmjEpbTxRVD5mDJUDgYrF05%2BDEn%2BJL056AZ3nt%2BxWe4on5I7V%2BB%2BGn3LnCeN%2FBbcPwvMvepFMS3vrrguhO6nf4%2Boec%2BjfOVToYoVNd49ote7HOmBZcOiUPoHejyXeLQ1xH3X6RuuoOEGQQC32w3WSmhu%2FScoAF4WCyzwzzqcoagfD38DFGXC4PkoYQlk%2FT9nKmA0QtMCBkopQoW8qTGEy8LG0XPetrS%2Fyz2elwxYp8uIkTCYghSdwAEBGcwA%2Bpnu5lzSm%2FsjbBB4WsTu5LD%2F490Uqvo1O8Sapw6vJ1APN0W6Y8X5%2B3JQGh74B5mee8XOTl1%2BGqUiaJv1FUaTKShyHaLx8qZTTSZ983t9d7PH0QLEvB1JU6PUYmIs3rGKdayuohB%2BfUBLCp8VdFbj2Fg3Df9IInLxW1qdgL4gX%2FKgvcyRyZWuJdvCpls5HASxpnzztIMm5ePMM9VLFWAlDdjxqxIMTw8GZhyYC0%2Fxndc88ocENHMvqCUX08A%2Btz%2BUM8OiYEKm6b3N9s92FjATBGnVV50AFFkw9PkWqS3YxO13Ie%2BKeQvWwn8Hx%2BIYBoRSY2WkBjDDAz%2FfJBjqkAbZ2v66bS03C6UcFcHVpqqQtxXdiO%2B0oxBFgiMxFvq6HbDhYcAHDFPSP8noeiaHOMFFca%2BuAg0H3yJ5pk%2Bjt4y6vdOMfoIRJHTaxzCQyGPmfZCPzmXnBr4olpDiq40ZoWoD28GLG%2B3uMt1bVCaviHTS8vNe51rtQMgMivOzQvuesPRRt%2F1%2BvPilcVJjwCdzrbBiwqAJJFubWA%2FdhGSMiARt30%2BQ0&X-Amz-Signature=871dd6d0614b486e2b43433aec372f173d77b51f8390df0c266d481855198d75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Which education level has:
- the highest median?
- the smallest range?
- most outliers?

<details>
<summary>Solution</summary>

Highest median → unknown
Smallest range → tertiary
Most outliers → secondary
</details>
---
**Chart interpretation**
Look at the Seaborn jointplot shown below.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/984f8797-0e56-4fb4-ad03-41befca8318a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3KRXSO7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD0Q1tJXQpGjS7ulotvHULKo8EPiezfDxF9JEh7qJwq3QIhALcauY7Btr%2BYLumeSLEk2G2jYvrhxAnRPVBR%2FDoo0q%2FOKv8DCCgQABoMNjM3NDIzMTgzODA1IgxRffy9vH%2BYiabQykQq3AN%2FgoYmxZfv8n6RzH0JYLRefd%2FggWFadiExzM4n9J50lBCByIBT5nQTJ6hGmjEpbTxRVD5mDJUDgYrF05%2BDEn%2BJL056AZ3nt%2BxWe4on5I7V%2BB%2BGn3LnCeN%2FBbcPwvMvepFMS3vrrguhO6nf4%2Boec%2BjfOVToYoVNd49ote7HOmBZcOiUPoHejyXeLQ1xH3X6RuuoOEGQQC32w3WSmhu%2FScoAF4WCyzwzzqcoagfD38DFGXC4PkoYQlk%2FT9nKmA0QtMCBkopQoW8qTGEy8LG0XPetrS%2Fyz2elwxYp8uIkTCYghSdwAEBGcwA%2Bpnu5lzSm%2FsjbBB4WsTu5LD%2F490Uqvo1O8Sapw6vJ1APN0W6Y8X5%2B3JQGh74B5mee8XOTl1%2BGqUiaJv1FUaTKShyHaLx8qZTTSZ983t9d7PH0QLEvB1JU6PUYmIs3rGKdayuohB%2BfUBLCp8VdFbj2Fg3Df9IInLxW1qdgL4gX%2FKgvcyRyZWuJdvCpls5HASxpnzztIMm5ePMM9VLFWAlDdjxqxIMTw8GZhyYC0%2Fxndc88ocENHMvqCUX08A%2Btz%2BUM8OiYEKm6b3N9s92FjATBGnVV50AFFkw9PkWqS3YxO13Ie%2BKeQvWwn8Hx%2BIYBoRSY2WkBjDDAz%2FfJBjqkAbZ2v66bS03C6UcFcHVpqqQtxXdiO%2B0oxBFgiMxFvq6HbDhYcAHDFPSP8noeiaHOMFFca%2BuAg0H3yJ5pk%2Bjt4y6vdOMfoIRJHTaxzCQyGPmfZCPzmXnBr4olpDiq40ZoWoD28GLG%2B3uMt1bVCaviHTS8vNe51rtQMgMivOzQvuesPRRt%2F1%2BvPilcVJjwCdzrbBiwqAJJFubWA%2FdhGSMiARt30%2BQ0&X-Amz-Signature=b19c659ced0d0577aad2977426e466e40773ecee44321f8c1d2020d39e11c40d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
For Width and Length, in which range are most of the data points (approximately)?

<details>
<summary>Solution</summary>

We must look at the Histogram on top and to the right.
The highest bar on top of the chart goes from around 2.5 to 5. Thus, for Length most of the values are in this range.
The highest bar on the right goes from around 17.5 to 20. Thus, for Width most of the values are in this range.

</details>
---
**Chart interpretation**
Look at the Scatterplot shown below.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c31ada37-237c-485a-800a-759a40b9f3dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3KRXSO7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD0Q1tJXQpGjS7ulotvHULKo8EPiezfDxF9JEh7qJwq3QIhALcauY7Btr%2BYLumeSLEk2G2jYvrhxAnRPVBR%2FDoo0q%2FOKv8DCCgQABoMNjM3NDIzMTgzODA1IgxRffy9vH%2BYiabQykQq3AN%2FgoYmxZfv8n6RzH0JYLRefd%2FggWFadiExzM4n9J50lBCByIBT5nQTJ6hGmjEpbTxRVD5mDJUDgYrF05%2BDEn%2BJL056AZ3nt%2BxWe4on5I7V%2BB%2BGn3LnCeN%2FBbcPwvMvepFMS3vrrguhO6nf4%2Boec%2BjfOVToYoVNd49ote7HOmBZcOiUPoHejyXeLQ1xH3X6RuuoOEGQQC32w3WSmhu%2FScoAF4WCyzwzzqcoagfD38DFGXC4PkoYQlk%2FT9nKmA0QtMCBkopQoW8qTGEy8LG0XPetrS%2Fyz2elwxYp8uIkTCYghSdwAEBGcwA%2Bpnu5lzSm%2FsjbBB4WsTu5LD%2F490Uqvo1O8Sapw6vJ1APN0W6Y8X5%2B3JQGh74B5mee8XOTl1%2BGqUiaJv1FUaTKShyHaLx8qZTTSZ983t9d7PH0QLEvB1JU6PUYmIs3rGKdayuohB%2BfUBLCp8VdFbj2Fg3Df9IInLxW1qdgL4gX%2FKgvcyRyZWuJdvCpls5HASxpnzztIMm5ePMM9VLFWAlDdjxqxIMTw8GZhyYC0%2Fxndc88ocENHMvqCUX08A%2Btz%2BUM8OiYEKm6b3N9s92FjATBGnVV50AFFkw9PkWqS3YxO13Ie%2BKeQvWwn8Hx%2BIYBoRSY2WkBjDDAz%2FfJBjqkAbZ2v66bS03C6UcFcHVpqqQtxXdiO%2B0oxBFgiMxFvq6HbDhYcAHDFPSP8noeiaHOMFFca%2BuAg0H3yJ5pk%2Bjt4y6vdOMfoIRJHTaxzCQyGPmfZCPzmXnBr4olpDiq40ZoWoD28GLG%2B3uMt1bVCaviHTS8vNe51rtQMgMivOzQvuesPRRt%2F1%2BvPilcVJjwCdzrbBiwqAJJFubWA%2FdhGSMiARt30%2BQ0&X-Amz-Signature=8b669d5a44c5f4755273899faf7a45092c61c8a37b9ec64911dc6cffdd059e67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
A clear Correlation exists between Goals and Assists. True or False?

<details>
<summary>Solution</summary>

False
</details>
---

📄 **[Machine Learning]** (subpage)
---
**Machine Learning**
When I have categorial data we usually deal with a Regression problem and when we have numerical data we usually deal with a Classification problem. True or False?

<details>
<summary>Solution</summary>

False
When we have categorial data we mostly apply classification algorithms as we want to put things into categories and when we have numerical data we want to predict something numeric and thus we can use Regression.
</details>
---
**Machine Learning**
In supervised learning we have labelled data available while in unsupervised learning we don’t have the labels available and thus often apply clustering algorithms to get first insights about data. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**k-Nearest-Neighbour**
We have collected 1521 samples of flowers. Now we receive a new flower that we want to classify. To calculate the euclidean distance it takes 0.02 seconds. To initialize the model it takes another 0.8 seconds. A model initialization is required before the whole classification process of a flower can be started. How many flowers can our model classify in one day?

<details>
<summary>Solution</summary>

2767 flowers
To calculate 1521 distances, the model requires 30.42 seconds (1521 samples * 0.02 seconds). On top of that comes 0.8 seconds for model initialisation. 30.42 + 0.8 = 31.22 seconds to classify one flower
A days has 24 * 60 * 60 = 86’400 seconds.
Thus in one day we can classify 86’400 / 31.22 = 2767.45 flowers → round down → 2767 flowers
</details>
---
**k-nearest-Neighbour**
Look at the code snippet below. What is missing at ############# ?
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/84b596ef-d755-48f5-bda8-bcbbeaae8b51/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K5L7PAS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCBhrVmVEFXqzlyBCe4NSUwbY2qa8gRrPs2FoTfqp2nyQIhALl4dEdmAfSkPzHPUNdkeTLkA%2FtKpa7pyndHe7WqdSYoKv8DCCgQABoMNjM3NDIzMTgzODA1Igw1de5CT5AGHo%2F3aw8q3AOCEKiLbc%2BUe2CfJ1ElucQXeWF%2FA%2B7XYbAC%2BMvNiCchGaBU5IsX9PE82lYQAVS12hA5RiD8C0yTMfWtenb2sDP5ssZ%2FRajn2AIjjtbzYFbVDDR5YORiYnX0QB%2BpPERsCbetfyWR0%2FYMGb5gshK2SEpcffwoRMN9iWL%2B9MP9%2F8aQHhOGIC2gu3WeEHKcgippYZ9GPbTImoBhA4WC7XHGvKybXMAg%2FzwFOJBwYdvHak%2BOOCOsgXKLy%2F54Dlxkr%2FS41BDfaBcSoN5NqR%2F4vJwDOE1rqspIXxhZIjaXBXgUb1tWLYwhTD6ZL2Imu3gy0UWPJ7HArvbGFoIox8LBica0vYzsgdr1EXpnwPfhDQN1OVDJj%2FZ5Amju%2FA5rnxq1YrqL2tUuiM4HHEQ0hYcxzy%2BBvMR9trk5QfGUIPS1KkmQ5tE166hhoUifCOcCIcMf%2FwJafYh1toN4%2FNNGPRfIXLNOCiclsC9l0YS8pu9IK64CUQLvcSD9VD7YWUMgDuIAuFgFyCyl9zTZNPlNjdoMmzA0XZwc6HP9PE3tzhS%2BNC6VFXNate5HWqGTXpiCWpCc5L8yELOxK2%2FO6gHAvCZZaTUkWkXN46jxdWDAZa9JP5DzHwn0o4%2BqdXNt%2BFo5Ck1iFTCXzvfJBjqkAWFL6g9BUBWv31%2BfAD7F4xbaTgLs%2F813IIA9g65OOkC1Uw7qOSLKvbUrq8HryBFp%2Fpd96xm2NgCrztq1%2F5fBtZTx9VDtI%2BjL1jWGxvY2T693WqrGw6g7%2F3%2FAwan0zO7O4Gkf9B51hujVzM3XJiryRq5d1YQpIOCrWHm%2BDBBI%2F7%2B4sEO7R5BuO3ehsMkiDg4jNLvT5612sW6zicU1f3YTnCfEHGSl&X-Amz-Signature=44304ea8f0c4301b9600ba7ee7c4f66681304bf0b4f8aacae8cdeaf661ea06c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Solution</summary>

```python
k_neighbors = [n[1] for n in distances[:k]]
```
We need to select the k closest neighbours in order to perform a majority voting in the next line.

</details>
---
**Macro & Micro Average**
From a model we got the following confusion matrix after having classified  the test dataset which consists of 1000 flowers. 
|  |  | Actual |  |  |
| --- | --- | --- | --- | --- |
|  |  | Setosa | Versicolor | Virginica |
| Predicted | Setosa | 100 | 100 | 50 |
|  | Versicolor | 50 | 200 | 50 |
|  | Virginica | 150 | 250 | 50 |
- What is the Precision of the model for Setosa?
- What is the Recall of the model for Versicolor?
- What is the F1 score of the model for Virginica?
- What is the Precision and Recall of the overall model when following the Macro Average approach?

<details>
<summary>Solution</summary>

40% → 100/(100+100+50)
36% → 200/(100+200+250)
17% → Recall = 33.33%, Precision = 11.11%
Precision = 39.26%, Recall = 34.34%
</details>
---
**Precision vs. Recall**
If you would need to implement a classifier that is able to predict whether a person is infected with a deadly virus or not, on which performance metric would you focus more: Precision or Recall? Why?

<details>
<summary>Solution</summary>

Recall
We would most likely focus more on Recall, as the cost of misclassification is very high; if we don’t capture a person that is infected with the virus then this person could potentially die. If we send a person to the doctor because the classifier predicts an infection, but it turns out that there is no infection, then this isn’t too bad.
</details>
---
**Precision vs. Recall **
If you would need to implement a classifier that is able to detect spam emails based on the email content and move them to the spam folder automatically, on which performance metric would you focus more: Precision or Recall? Why?

<details>
<summary>Solution</summary>

Precision
We would rather focus on Precision because we when we classify an email as spam we want to be really sure that it actually is spam. Because otherwise the chance that from time to time an important email from our boss lands in the spam folder is much higher. Contrarily, if a spam email lands in the regular inbox the consequences are not very drastic. We can simply delete the email manually. 
</details>
---
**F1 score**
What happens to the F1 score if we optimise towards one of the performance metrics, Precision or Recall?
- [ ] 1) F1 score increases
- [ ] 2) F1 score stays the same
- [ ] 3) F1 score decreases

<details>
<summary>Solution</summary>

3
Let’s assume we optimise towards Recall and set the threshold for positive class very low. As a result we classify many samples as positive and capture almost all samples that actually are positive. However, at the same time the numbers of samples classified as positives that are actually negative (False Positive) goes up as well, which drives Precision down. Consequently F1 score goes down as there is now a bigger difference between Recall and Precision (Recall went up, Precision came down).
</details>
---
**TF-IDF**
If a word appears across many documents in the dataset, what happens to its TF-IDF score?
- [ ] 1) TD-IDF goes down
- [ ] 2) TD-IDF stays the same
- [ ] 3) TD-IDF goes up

<details>
<summary>Solution</summary>

1
The document frequency (the number of documents in which the term appears) is in the denominator of the IDF formula. Thus, IDF decreases and TD stays the same. As we multiply TF with IDF, the TF-IDF score goes down.
</details>
---
**TF-IDF**
If a TF-IDF score of a term is higher than its term frequency its expressiveness has decreased through the TF-IDF transformation. True or False?

<details>
<summary>Solution</summary>

False
If TD-IDF is higher than TF before, its expressiveness has increased and thus has in the classification higher ‘saying’ compared to other terms.
</details>
---
**scikit-learn**
What does the scikit-learn function `.fit_transform()` do for us?
- [ ] 1) It trains a classifier
- [ ] 2) It tests a classifier
- [ ] 3) It does data transformation and is usually applied on the training dataset only
- [ ] 4) It does data transformation and is usually applied on the test dataset only
- [ ] 5) It does data transformation and is usually applied on the training and the test dataset

<details>
<summary>Solution</summary>

1, 3
We use it on the training data, otherwise we would ‘learn’ something from the test data and our model would be biased. When we need to do data transformation only we use `.transform()`
</details>
---
**scikit-learn **
When applying TF-IDF, we apply the `.fit_transform()` method on the training and on the test data set. True or False?

<details>
<summary>Solution</summary>

False
On the training data we apply [`.fit_transform()`](/9e4a78074aea481ca4c75e506d4671c7#16f816916fcc43318154a1b6b6ea38ae) which creates a Sparse Matrix and adjusts the weights according to TF-IDF.
On the test data we apply [`.transform()`](/9e4a78074aea481ca4c75e506d4671c7#3c583c11477d480d89e97c4211ae4d7b) which creates a Sparse Matrix only, to prevent bias.
</details>
---
**scikit-learn**
In which order would you apply the following functions in a machine learning use case? Note: Some functions may not exist at all.
- [ ] 1) `classification_report()`
- [ ] 2) `.fit()`
- [ ] 3) `.ResultReport()`
- [ ] 4) `KNeighborsClassifier(k_neighbors)`
- [ ] 5) `.fit_transform()`
- [ ] 6) `.test()`
- [ ] 7) `.transform()`
- [ ] 8) `.predict()`

<details>
<summary>Solution</summary>

1. `KNeighborsClassifier(k_neighbors)` → Create classifier
1. `.fit_transform()` → Transform training data
1. `.transform()` → Transform test data
1. `.fit()` → Train classifier
1. `.predict()` → make predictions on test data
1. `classification_report()` → Evaluate performance

`.test()` and `.ResultReport()` do not exist
</details>
---
**scikit-learn**
Put the following actions in the order in which we usually perform them when we want to implement a general classifier, which for example predicts an Iris flower’s type.
- Choose classifier
- Load data
- Evaluate classifier
- Sanity check
- Test classifier
- Split dataset
- Train classifier

<details>
<summary>Solution</summary>

1️⃣ Load data
2️⃣ Split dataset
3️⃣ Choose classifier
4️⃣ Train classifier
5️⃣ Test classifier
6️⃣ Evaluate classifier
7️⃣ Sanity check
</details>
---
**scikit-learn**
Put the following actions in the order in which we usually perform them when we want to implement a text classifier, which for example predicts whether a movie review is positive or negative.
- Create sparse matrices and apply TF-IDF
- Split dataset
- Train classifier
- Evaluate classifier
- Sanity check
- Test classifier
- Load data
- Choose classifier

<details>
<summary>Solution</summary>

1️⃣ Load data
2️⃣ Split dataset
3️⃣ Create sparse matrices and apply TF-IDF
4️⃣ Choose classifier
5️⃣ Train classifier
6️⃣ Test classifier
7️⃣ Evaluate classifier
8️⃣ Sanity check
</details>
---
**Overfitting** 
When we train a classifier for too long, the risk of overfitting increases and thus our classifier has high Bias and low Variance. True or False?

<details>
<summary>Solution</summary>

False
The risk does indeed increase when we train the classifier for too long. However, when we have an overfitted model, it has low Bias and high Variance as with every test dataset its performance varies significantly as it is highly tailored towards one specific set of training data.
</details>
---
**Underfitting**
Decide for each metric below whether they are low or high when we have an underfitted model. 
- Bias
- Variance
- Train error
- Test error

<details>
<summary>Solution</summary>

High, Low, High, High
We have high test error because we assume that test data is similar to train data and when we have an underfitted model, our model has not learned anything from the training data.
</details>
---
**Overfitting**
Decide for each metric below whether they are low or high when we have an overfitted model. 
- Bias
- Variance
- Train error
- Test error

<details>
<summary>Solution</summary>

Low, High, Low, High
Now we have low training error and high test error because the model is now highly specialised on the training data.
</details>
---
**k-Fold Cross Validation**
Order the actions below into the right sequence, i.e., how they are usually executed when doing k-Fold Cross Validation
- [ ] 1) Think about Hyperparameter tuning
- [ ] 2) Divide data into k-folds
- [ ] 3) Average performance metrics
- [ ] 4) Think about how input data could be improved
- [ ] 5) Run train / test runs

<details>
<summary>Solution</summary>

2, 5, 3, 1 & 4 (simultaneously)

</details>
---
**Hyperparameters**
A Hyperparameter distinguishes itself from a Parameter that it is not provided during the creation of a classifier as they can be learned from the model. True or False?

<details>
<summary>Solution</summary>

False
Hyperparameters must be provided when creating the model. Normal parameters can be learned from the data. Hyperparameters not.
</details>
---
**Hyperparameters**
When the performance of our classifier is not satisfactory, we can consider performing Hyperparameter tuning. True or False? How could we do it?

<details>
<summary>Solution</summary>

True
We coudl again use k-Fold Cross Validation, for each fold we would run separate k-Fold Cross Validation to find the ideal Hyperparameters for this specific fold and in the end we can have a look at all performance metric ↔ Hyperparameter conditions to select the ones that performed best.
</details>
---
---

