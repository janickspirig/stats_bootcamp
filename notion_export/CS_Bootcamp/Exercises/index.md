---
title: "Exercises"
notion_id: "9c0e1af3-0c7e-407b-82d0-fa17a9e21e16"
notion_url: "https://www.notion.so/Exercises-9c0e1af30c7e407b82d0fa17a9e21e16"
exported_at: "2025-12-13T22:41:21.720588+00:00"
---

# Exercises

---
📄 **[Programming hands-on]** (subpage)
Below you can find some Jupyter Notebooks to practice your coding skills further. I highly recommend to do this as this from my point of view is the most effective strategy to learn programming - by doing it yourself! Just download one of the files and open it in [Google Colab](https://colab.research.google.com/).
### Programming basics
[Programming basics](https://colab.research.google.com/drive/1Al_4lScNus8YkpqcbMGAT9DZznaC6LGM?usp=sharing)
---
### Python basics
[Exercise easy](https://colab.research.google.com/drive/1yHqQPi2l6FQFpl9ocJFAr8_vlYGW82t-?usp=sharing)
[Exercise hard](https://colab.research.google.com/drive/1mFhEJ46nxV7Xcqn1howOtYWS1YtyWXpI?usp=sharing)
[Solution](https://colab.research.google.com/drive/1EmsFKBTozTGGQ-FMRF4AEsdbwvV6hNzM?usp=sharing)
---
### OOP
[Exercise 1](https://drive.google.com/file/d/14XBhKBe2CUwtu1avgXtMi3bEjcXJSEgC/view?usp=sharing)
[Solution 1](https://drive.google.com/file/d/1do9I-Wx2CG03bMgtyNZMjegk6kNnoFNT/view?usp=sharing)
[Exercise 2](https://colab.research.google.com/drive/1VeF_QIv_ZhyHDA9yEBAoGJ-2C40FLwy5?usp=sharing)
[Solution 2](https://colab.research.google.com/drive/1RlcdEILBYZ7Ikm8LtHRIHQ-tv1sfF8Ti?usp=share_link)
---
### Data Science
[Exercise](https://drive.google.com/file/d/1XgHnrFrdhgGv-M2Ora-wDb4B3mO9icRK/view?usp=sharing)
[Solution](https://drive.google.com/file/d/1DbeKIrACuN7jhuWYX6bZwSU3F2QFUf5X/view?usp=sharing)
---
### Data Science & Visualisation
[Exercise](https://drive.google.com/file/d/1mgZnl2bSy3JhO1KRghLUBml6KxQdUgfi/view?usp=sharing)
[Solution](https://drive.google.com/file/d/1s2i-UsXgvUc9MSN2SAuAjCq9RznmzbF6/view?usp=sharing)
[Dataset](https://drive.google.com/file/d/1mAgfDuX9pEe2vbcHUfABFGsBUY_zw1XM/view?usp=sharing)
---

📄 **[Multiple-choice questions]** (subpage)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/35462356-6d1c-4967-ae72-fbd005674a21/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CXXSVKI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICPZz6N%2Brt6%2B2mcVYvndu9R55p2Wn2fELfR0kJarLZW3AiBnU9Xm0N8HWuVXneFBlRcGnVwXKKMhS6e15XJxqaZ8YSr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMj4qiuV6C7aOMkbZOKtwDEHnrEeR7%2Bvk8VwbupVOxXNMegCJhzkkOOy%2B8jxDZexsBpY1MIbeM65IHWUkJatEwGZYVVm2GYqRvxcfCrmlRMhGXysPhv7ts8xr4dO5Vq3H2RmR1rskPT7GvEgs4OwMMXeseVrF1tybnmU9y%2Bu44sdxKmpSCaXjesmOlvIIO3Ge87jkrMNqYs2UGermkT1WtnW3pQ74JHRPVUrTZSW8i6yZzVvynT%2Bcft4paIwOunc%2BR9QYhLba%2FKLin%2BsEZAVDI0a%2BfUBjpZCFSrbMZ1JpRBflz%2F9wFUe22X0n7Wopnj0EwApYrebOq8NZbjSiyop%2BmpC69QwIjQEQWVpd35Eq6xFEmthZzpqeEQiQk%2B0FeeUCek8K3xg5jQxP7cb0SvKDE4Hkd1k1OVy58%2Bfb%2BiKOx8FvjccOmlH3xJi98ty0ScpkrG0DYMmAUTn0mB0WITxsVEHEqQ6qJlD3YdlMrnyOdrsC8k%2B8NvUy9ZEG%2FqZd8ew4DDeMZ9gWg69B9WNGkNB0qWgn9kb2AfrXQTdMRJX1JG8YG0STxiwXeiFq1XPyVZt6THw12GWnAifdzAXRzElsbS%2B1jY%2Fq%2FxJeMbO9df1iwJCScnDFHELpH93iGLJf4P5vQcyIgZI0QxSgzSqQwqs73yQY6pgEkHdwm8lSexgLfLNjmIVEY1CscfltVcM6l8XDtv0JJAIBPX75NQRRgFrv5iYVcLpwKNSRlGV6TpvHcqKyW9%2FmsRU0ZOEcUttFxlRvW9J%2FWRijvn%2FcFspbDt4dZwqHb8CYgawNIUSp38AvvFcQ2glYpj2cNqEhBZqq1NBSqGXHzZVSdpGC1fDHvQM1Q8eDOIKXBRflBsLs2WkFAVrnAP5hm8NQUc5ot&X-Amz-Signature=3a048d55e02de31a41489b43f62965fe5b611e05871b8782b1be8ee0ef652a1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/86d2f17d-981c-4b80-92cc-e38b737660b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CXXSVKI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICPZz6N%2Brt6%2B2mcVYvndu9R55p2Wn2fELfR0kJarLZW3AiBnU9Xm0N8HWuVXneFBlRcGnVwXKKMhS6e15XJxqaZ8YSr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMj4qiuV6C7aOMkbZOKtwDEHnrEeR7%2Bvk8VwbupVOxXNMegCJhzkkOOy%2B8jxDZexsBpY1MIbeM65IHWUkJatEwGZYVVm2GYqRvxcfCrmlRMhGXysPhv7ts8xr4dO5Vq3H2RmR1rskPT7GvEgs4OwMMXeseVrF1tybnmU9y%2Bu44sdxKmpSCaXjesmOlvIIO3Ge87jkrMNqYs2UGermkT1WtnW3pQ74JHRPVUrTZSW8i6yZzVvynT%2Bcft4paIwOunc%2BR9QYhLba%2FKLin%2BsEZAVDI0a%2BfUBjpZCFSrbMZ1JpRBflz%2F9wFUe22X0n7Wopnj0EwApYrebOq8NZbjSiyop%2BmpC69QwIjQEQWVpd35Eq6xFEmthZzpqeEQiQk%2B0FeeUCek8K3xg5jQxP7cb0SvKDE4Hkd1k1OVy58%2Bfb%2BiKOx8FvjccOmlH3xJi98ty0ScpkrG0DYMmAUTn0mB0WITxsVEHEqQ6qJlD3YdlMrnyOdrsC8k%2B8NvUy9ZEG%2FqZd8ew4DDeMZ9gWg69B9WNGkNB0qWgn9kb2AfrXQTdMRJX1JG8YG0STxiwXeiFq1XPyVZt6THw12GWnAifdzAXRzElsbS%2B1jY%2Fq%2FxJeMbO9df1iwJCScnDFHELpH93iGLJf4P5vQcyIgZI0QxSgzSqQwqs73yQY6pgEkHdwm8lSexgLfLNjmIVEY1CscfltVcM6l8XDtv0JJAIBPX75NQRRgFrv5iYVcLpwKNSRlGV6TpvHcqKyW9%2FmsRU0ZOEcUttFxlRvW9J%2FWRijvn%2FcFspbDt4dZwqHb8CYgawNIUSp38AvvFcQ2glYpj2cNqEhBZqq1NBSqGXHzZVSdpGC1fDHvQM1Q8eDOIKXBRflBsLs2WkFAVrnAP5hm8NQUc5ot&X-Amz-Signature=e8deac62f83a9eb96fa39b8db0dcfdb8464129a06f43123d612eca885a5b705c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f7ffde3-100f-4167-aa32-0cd81d32311c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CXXSVKI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICPZz6N%2Brt6%2B2mcVYvndu9R55p2Wn2fELfR0kJarLZW3AiBnU9Xm0N8HWuVXneFBlRcGnVwXKKMhS6e15XJxqaZ8YSr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMj4qiuV6C7aOMkbZOKtwDEHnrEeR7%2Bvk8VwbupVOxXNMegCJhzkkOOy%2B8jxDZexsBpY1MIbeM65IHWUkJatEwGZYVVm2GYqRvxcfCrmlRMhGXysPhv7ts8xr4dO5Vq3H2RmR1rskPT7GvEgs4OwMMXeseVrF1tybnmU9y%2Bu44sdxKmpSCaXjesmOlvIIO3Ge87jkrMNqYs2UGermkT1WtnW3pQ74JHRPVUrTZSW8i6yZzVvynT%2Bcft4paIwOunc%2BR9QYhLba%2FKLin%2BsEZAVDI0a%2BfUBjpZCFSrbMZ1JpRBflz%2F9wFUe22X0n7Wopnj0EwApYrebOq8NZbjSiyop%2BmpC69QwIjQEQWVpd35Eq6xFEmthZzpqeEQiQk%2B0FeeUCek8K3xg5jQxP7cb0SvKDE4Hkd1k1OVy58%2Bfb%2BiKOx8FvjccOmlH3xJi98ty0ScpkrG0DYMmAUTn0mB0WITxsVEHEqQ6qJlD3YdlMrnyOdrsC8k%2B8NvUy9ZEG%2FqZd8ew4DDeMZ9gWg69B9WNGkNB0qWgn9kb2AfrXQTdMRJX1JG8YG0STxiwXeiFq1XPyVZt6THw12GWnAifdzAXRzElsbS%2B1jY%2Fq%2FxJeMbO9df1iwJCScnDFHELpH93iGLJf4P5vQcyIgZI0QxSgzSqQwqs73yQY6pgEkHdwm8lSexgLfLNjmIVEY1CscfltVcM6l8XDtv0JJAIBPX75NQRRgFrv5iYVcLpwKNSRlGV6TpvHcqKyW9%2FmsRU0ZOEcUttFxlRvW9J%2FWRijvn%2FcFspbDt4dZwqHb8CYgawNIUSp38AvvFcQ2glYpj2cNqEhBZqq1NBSqGXHzZVSdpGC1fDHvQM1Q8eDOIKXBRflBsLs2WkFAVrnAP5hm8NQUc5ot&X-Amz-Signature=b83da30e2cca44194679876a9d4a95521a60d15802334b99cbec0da84075cdbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d7a05b3c-4771-4673-8ac5-89221fdfc57d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CXXSVKI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICPZz6N%2Brt6%2B2mcVYvndu9R55p2Wn2fELfR0kJarLZW3AiBnU9Xm0N8HWuVXneFBlRcGnVwXKKMhS6e15XJxqaZ8YSr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMj4qiuV6C7aOMkbZOKtwDEHnrEeR7%2Bvk8VwbupVOxXNMegCJhzkkOOy%2B8jxDZexsBpY1MIbeM65IHWUkJatEwGZYVVm2GYqRvxcfCrmlRMhGXysPhv7ts8xr4dO5Vq3H2RmR1rskPT7GvEgs4OwMMXeseVrF1tybnmU9y%2Bu44sdxKmpSCaXjesmOlvIIO3Ge87jkrMNqYs2UGermkT1WtnW3pQ74JHRPVUrTZSW8i6yZzVvynT%2Bcft4paIwOunc%2BR9QYhLba%2FKLin%2BsEZAVDI0a%2BfUBjpZCFSrbMZ1JpRBflz%2F9wFUe22X0n7Wopnj0EwApYrebOq8NZbjSiyop%2BmpC69QwIjQEQWVpd35Eq6xFEmthZzpqeEQiQk%2B0FeeUCek8K3xg5jQxP7cb0SvKDE4Hkd1k1OVy58%2Bfb%2BiKOx8FvjccOmlH3xJi98ty0ScpkrG0DYMmAUTn0mB0WITxsVEHEqQ6qJlD3YdlMrnyOdrsC8k%2B8NvUy9ZEG%2FqZd8ew4DDeMZ9gWg69B9WNGkNB0qWgn9kb2AfrXQTdMRJX1JG8YG0STxiwXeiFq1XPyVZt6THw12GWnAifdzAXRzElsbS%2B1jY%2Fq%2FxJeMbO9df1iwJCScnDFHELpH93iGLJf4P5vQcyIgZI0QxSgzSqQwqs73yQY6pgEkHdwm8lSexgLfLNjmIVEY1CscfltVcM6l8XDtv0JJAIBPX75NQRRgFrv5iYVcLpwKNSRlGV6TpvHcqKyW9%2FmsRU0ZOEcUttFxlRvW9J%2FWRijvn%2FcFspbDt4dZwqHb8CYgawNIUSp38AvvFcQ2glYpj2cNqEhBZqq1NBSqGXHzZVSdpGC1fDHvQM1Q8eDOIKXBRflBsLs2WkFAVrnAP5hm8NQUc5ot&X-Amz-Signature=aa76145b6a1cf28cd566cecd7050e7c45269d1160fd64553e2f4c59a87658ee7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/efdb3faf-eea5-41cd-87d1-6255fbf8cee1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CXXSVKI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICPZz6N%2Brt6%2B2mcVYvndu9R55p2Wn2fELfR0kJarLZW3AiBnU9Xm0N8HWuVXneFBlRcGnVwXKKMhS6e15XJxqaZ8YSr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMj4qiuV6C7aOMkbZOKtwDEHnrEeR7%2Bvk8VwbupVOxXNMegCJhzkkOOy%2B8jxDZexsBpY1MIbeM65IHWUkJatEwGZYVVm2GYqRvxcfCrmlRMhGXysPhv7ts8xr4dO5Vq3H2RmR1rskPT7GvEgs4OwMMXeseVrF1tybnmU9y%2Bu44sdxKmpSCaXjesmOlvIIO3Ge87jkrMNqYs2UGermkT1WtnW3pQ74JHRPVUrTZSW8i6yZzVvynT%2Bcft4paIwOunc%2BR9QYhLba%2FKLin%2BsEZAVDI0a%2BfUBjpZCFSrbMZ1JpRBflz%2F9wFUe22X0n7Wopnj0EwApYrebOq8NZbjSiyop%2BmpC69QwIjQEQWVpd35Eq6xFEmthZzpqeEQiQk%2B0FeeUCek8K3xg5jQxP7cb0SvKDE4Hkd1k1OVy58%2Bfb%2BiKOx8FvjccOmlH3xJi98ty0ScpkrG0DYMmAUTn0mB0WITxsVEHEqQ6qJlD3YdlMrnyOdrsC8k%2B8NvUy9ZEG%2FqZd8ew4DDeMZ9gWg69B9WNGkNB0qWgn9kb2AfrXQTdMRJX1JG8YG0STxiwXeiFq1XPyVZt6THw12GWnAifdzAXRzElsbS%2B1jY%2Fq%2FxJeMbO9df1iwJCScnDFHELpH93iGLJf4P5vQcyIgZI0QxSgzSqQwqs73yQY6pgEkHdwm8lSexgLfLNjmIVEY1CscfltVcM6l8XDtv0JJAIBPX75NQRRgFrv5iYVcLpwKNSRlGV6TpvHcqKyW9%2FmsRU0ZOEcUttFxlRvW9J%2FWRijvn%2FcFspbDt4dZwqHb8CYgawNIUSp38AvvFcQ2glYpj2cNqEhBZqq1NBSqGXHzZVSdpGC1fDHvQM1Q8eDOIKXBRflBsLs2WkFAVrnAP5hm8NQUc5ot&X-Amz-Signature=9af3aa9de1db94689829147ae892976b8dae0c6e105195ec7a9da7dec1fd0ea5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/35462356-6d1c-4967-ae72-fbd005674a21/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOY6QGLV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICPhtRAFkd%2FSPd1yt1B%2FWvkHFwb6vCINmv8%2FE0Gbx%2BTnAiEA0a78mNM7%2BXQOw7cLU2K%2Fvr6R7VGVa%2F8Gqgahtcubip8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBFDql28DYSIS4gwbyrcA4ab6fG9G%2FxRzbgjTMLP%2FrlY91ul2rgaescAQqiqDdmsE%2F%2Fsm3PBX3bZFYFY3mdc8Xgn6HCijw%2Fu8umasOIPkETGd9R3xD4hXibAb%2FxJpjuAd%2FMJZHeLrLzleo8GY2az2%2FdKSpDuRrTjepMwp3%2FTATotY6crbGvvOhVYfKPBQZb3ahMlQYS8wehPN671oJLFfY9fCJsy12jcxLF3fDf5tvUq4bUe4%2F7M7HjvB1vwRO19WZ9obLFBOI3IUdqHoBiHLBB34lGPqx7VxLbyRhhiG77s76C9D9%2FyvZ2p9yI2lWq%2FF0Wlyd5pSjvOhtlu6qDSTSWSOv84bEBxCnU%2B%2FbukTKnwrmcxYlW%2FIhsiJ0wgcnQkAel4gHDsD8SRY25n3i4olxt953CsH2f5Y0f0%2FICv%2F%2FXrSvU0XKS0uJJ9ZUOdQny8QAZ6HfTOls%2FbaKdVa1LAX2TGqRhTT%2BSuyGoL7oPnihjmzzp51bzB0efZLHjbitFBCxX6G5zoQU8kxjjwMf%2BjmkJhOKA1x44hz0gEHb49f1SAdNGjA8IVAbHtAnItsMe0bZHNaNM3msNtn5deWASi2EWC8qiWZlvS%2BDlOxP8hFFXwSEerrCBdjUr%2FNY2qnCSRr%2FtdbD6PxhklvNmFMP3N98kGOqUBvlzBzbZJAk0QV7b5gtnNsJeK6RrHTs8%2B%2F09dlrynvQi%2BVBrAElaLg8kMp8IrDlpXPuLJEx0dQQtX4ELRONS%2Bs06snIyMJwOqx21s1gj7ClzoUAUwcaWDya2zxqq1VmQinuQrS%2Ba6WBzzmK93WwhtacIWeP0c7tyydDdNtM0NW4pHI08eX3gEnpQH7X7oRNxyNHo2srGlw2Z9g7OBRaWPgPxVShz8&X-Amz-Signature=5c0df4b766a085b8257521a5bc33ae316c41155fad7d97257e6e8e352417610a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: NAND
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | True (1) |
| False (0) | True (1) | True (1) |
| True (1) | False (0) | True (1) |
| True (1) | True (1) | False (0) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/86d2f17d-981c-4b80-92cc-e38b737660b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOY6QGLV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICPhtRAFkd%2FSPd1yt1B%2FWvkHFwb6vCINmv8%2FE0Gbx%2BTnAiEA0a78mNM7%2BXQOw7cLU2K%2Fvr6R7VGVa%2F8Gqgahtcubip8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBFDql28DYSIS4gwbyrcA4ab6fG9G%2FxRzbgjTMLP%2FrlY91ul2rgaescAQqiqDdmsE%2F%2Fsm3PBX3bZFYFY3mdc8Xgn6HCijw%2Fu8umasOIPkETGd9R3xD4hXibAb%2FxJpjuAd%2FMJZHeLrLzleo8GY2az2%2FdKSpDuRrTjepMwp3%2FTATotY6crbGvvOhVYfKPBQZb3ahMlQYS8wehPN671oJLFfY9fCJsy12jcxLF3fDf5tvUq4bUe4%2F7M7HjvB1vwRO19WZ9obLFBOI3IUdqHoBiHLBB34lGPqx7VxLbyRhhiG77s76C9D9%2FyvZ2p9yI2lWq%2FF0Wlyd5pSjvOhtlu6qDSTSWSOv84bEBxCnU%2B%2FbukTKnwrmcxYlW%2FIhsiJ0wgcnQkAel4gHDsD8SRY25n3i4olxt953CsH2f5Y0f0%2FICv%2F%2FXrSvU0XKS0uJJ9ZUOdQny8QAZ6HfTOls%2FbaKdVa1LAX2TGqRhTT%2BSuyGoL7oPnihjmzzp51bzB0efZLHjbitFBCxX6G5zoQU8kxjjwMf%2BjmkJhOKA1x44hz0gEHb49f1SAdNGjA8IVAbHtAnItsMe0bZHNaNM3msNtn5deWASi2EWC8qiWZlvS%2BDlOxP8hFFXwSEerrCBdjUr%2FNY2qnCSRr%2FtdbD6PxhklvNmFMP3N98kGOqUBvlzBzbZJAk0QV7b5gtnNsJeK6RrHTs8%2B%2F09dlrynvQi%2BVBrAElaLg8kMp8IrDlpXPuLJEx0dQQtX4ELRONS%2Bs06snIyMJwOqx21s1gj7ClzoUAUwcaWDya2zxqq1VmQinuQrS%2Ba6WBzzmK93WwhtacIWeP0c7tyydDdNtM0NW4pHI08eX3gEnpQH7X7oRNxyNHo2srGlw2Z9g7OBRaWPgPxVShz8&X-Amz-Signature=bad6107fdceecc9b933e094dd2e70034900fe8b90eb5cd4f235b6dfba9621486&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: OR
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | False (0) |
| False (0) | True (1) | True (1) |
| True (1) | False (0) | True (1) |
| True (1) | True (1) | True (1) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f7ffde3-100f-4167-aa32-0cd81d32311c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOY6QGLV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICPhtRAFkd%2FSPd1yt1B%2FWvkHFwb6vCINmv8%2FE0Gbx%2BTnAiEA0a78mNM7%2BXQOw7cLU2K%2Fvr6R7VGVa%2F8Gqgahtcubip8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBFDql28DYSIS4gwbyrcA4ab6fG9G%2FxRzbgjTMLP%2FrlY91ul2rgaescAQqiqDdmsE%2F%2Fsm3PBX3bZFYFY3mdc8Xgn6HCijw%2Fu8umasOIPkETGd9R3xD4hXibAb%2FxJpjuAd%2FMJZHeLrLzleo8GY2az2%2FdKSpDuRrTjepMwp3%2FTATotY6crbGvvOhVYfKPBQZb3ahMlQYS8wehPN671oJLFfY9fCJsy12jcxLF3fDf5tvUq4bUe4%2F7M7HjvB1vwRO19WZ9obLFBOI3IUdqHoBiHLBB34lGPqx7VxLbyRhhiG77s76C9D9%2FyvZ2p9yI2lWq%2FF0Wlyd5pSjvOhtlu6qDSTSWSOv84bEBxCnU%2B%2FbukTKnwrmcxYlW%2FIhsiJ0wgcnQkAel4gHDsD8SRY25n3i4olxt953CsH2f5Y0f0%2FICv%2F%2FXrSvU0XKS0uJJ9ZUOdQny8QAZ6HfTOls%2FbaKdVa1LAX2TGqRhTT%2BSuyGoL7oPnihjmzzp51bzB0efZLHjbitFBCxX6G5zoQU8kxjjwMf%2BjmkJhOKA1x44hz0gEHb49f1SAdNGjA8IVAbHtAnItsMe0bZHNaNM3msNtn5deWASi2EWC8qiWZlvS%2BDlOxP8hFFXwSEerrCBdjUr%2FNY2qnCSRr%2FtdbD6PxhklvNmFMP3N98kGOqUBvlzBzbZJAk0QV7b5gtnNsJeK6RrHTs8%2B%2F09dlrynvQi%2BVBrAElaLg8kMp8IrDlpXPuLJEx0dQQtX4ELRONS%2Bs06snIyMJwOqx21s1gj7ClzoUAUwcaWDya2zxqq1VmQinuQrS%2Ba6WBzzmK93WwhtacIWeP0c7tyydDdNtM0NW4pHI08eX3gEnpQH7X7oRNxyNHo2srGlw2Z9g7OBRaWPgPxVShz8&X-Amz-Signature=d7bcef42280b6e70ee136ebc4f168862f6f25c7d801417dace299329c7aa5c6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: AND
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | False (0) |
| False (0) | True (1) | False (0) |
| True (1) | False (0) | False (0) |
| True (1) | True (1) | True (1) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d7a05b3c-4771-4673-8ac5-89221fdfc57d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOY6QGLV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICPhtRAFkd%2FSPd1yt1B%2FWvkHFwb6vCINmv8%2FE0Gbx%2BTnAiEA0a78mNM7%2BXQOw7cLU2K%2Fvr6R7VGVa%2F8Gqgahtcubip8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBFDql28DYSIS4gwbyrcA4ab6fG9G%2FxRzbgjTMLP%2FrlY91ul2rgaescAQqiqDdmsE%2F%2Fsm3PBX3bZFYFY3mdc8Xgn6HCijw%2Fu8umasOIPkETGd9R3xD4hXibAb%2FxJpjuAd%2FMJZHeLrLzleo8GY2az2%2FdKSpDuRrTjepMwp3%2FTATotY6crbGvvOhVYfKPBQZb3ahMlQYS8wehPN671oJLFfY9fCJsy12jcxLF3fDf5tvUq4bUe4%2F7M7HjvB1vwRO19WZ9obLFBOI3IUdqHoBiHLBB34lGPqx7VxLbyRhhiG77s76C9D9%2FyvZ2p9yI2lWq%2FF0Wlyd5pSjvOhtlu6qDSTSWSOv84bEBxCnU%2B%2FbukTKnwrmcxYlW%2FIhsiJ0wgcnQkAel4gHDsD8SRY25n3i4olxt953CsH2f5Y0f0%2FICv%2F%2FXrSvU0XKS0uJJ9ZUOdQny8QAZ6HfTOls%2FbaKdVa1LAX2TGqRhTT%2BSuyGoL7oPnihjmzzp51bzB0efZLHjbitFBCxX6G5zoQU8kxjjwMf%2BjmkJhOKA1x44hz0gEHb49f1SAdNGjA8IVAbHtAnItsMe0bZHNaNM3msNtn5deWASi2EWC8qiWZlvS%2BDlOxP8hFFXwSEerrCBdjUr%2FNY2qnCSRr%2FtdbD6PxhklvNmFMP3N98kGOqUBvlzBzbZJAk0QV7b5gtnNsJeK6RrHTs8%2B%2F09dlrynvQi%2BVBrAElaLg8kMp8IrDlpXPuLJEx0dQQtX4ELRONS%2Bs06snIyMJwOqx21s1gj7ClzoUAUwcaWDya2zxqq1VmQinuQrS%2Ba6WBzzmK93WwhtacIWeP0c7tyydDdNtM0NW4pHI08eX3gEnpQH7X7oRNxyNHo2srGlw2Z9g7OBRaWPgPxVShz8&X-Amz-Signature=22d94d41c0ec429481204206faad665db5aaccba043c2abbb0fc83036d75c494&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: NOR
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | True (1) |
| False (0) | True (1) | False (0) |
| True (1) | False (0) | False (0) |
| True (1) | True (1) | False (0) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/efdb3faf-eea5-41cd-87d1-6255fbf8cee1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOY6QGLV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICPhtRAFkd%2FSPd1yt1B%2FWvkHFwb6vCINmv8%2FE0Gbx%2BTnAiEA0a78mNM7%2BXQOw7cLU2K%2Fvr6R7VGVa%2F8Gqgahtcubip8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBFDql28DYSIS4gwbyrcA4ab6fG9G%2FxRzbgjTMLP%2FrlY91ul2rgaescAQqiqDdmsE%2F%2Fsm3PBX3bZFYFY3mdc8Xgn6HCijw%2Fu8umasOIPkETGd9R3xD4hXibAb%2FxJpjuAd%2FMJZHeLrLzleo8GY2az2%2FdKSpDuRrTjepMwp3%2FTATotY6crbGvvOhVYfKPBQZb3ahMlQYS8wehPN671oJLFfY9fCJsy12jcxLF3fDf5tvUq4bUe4%2F7M7HjvB1vwRO19WZ9obLFBOI3IUdqHoBiHLBB34lGPqx7VxLbyRhhiG77s76C9D9%2FyvZ2p9yI2lWq%2FF0Wlyd5pSjvOhtlu6qDSTSWSOv84bEBxCnU%2B%2FbukTKnwrmcxYlW%2FIhsiJ0wgcnQkAel4gHDsD8SRY25n3i4olxt953CsH2f5Y0f0%2FICv%2F%2FXrSvU0XKS0uJJ9ZUOdQny8QAZ6HfTOls%2FbaKdVa1LAX2TGqRhTT%2BSuyGoL7oPnihjmzzp51bzB0efZLHjbitFBCxX6G5zoQU8kxjjwMf%2BjmkJhOKA1x44hz0gEHb49f1SAdNGjA8IVAbHtAnItsMe0bZHNaNM3msNtn5deWASi2EWC8qiWZlvS%2BDlOxP8hFFXwSEerrCBdjUr%2FNY2qnCSRr%2FtdbD6PxhklvNmFMP3N98kGOqUBvlzBzbZJAk0QV7b5gtnNsJeK6RrHTs8%2B%2F09dlrynvQi%2BVBrAElaLg8kMp8IrDlpXPuLJEx0dQQtX4ELRONS%2Bs06snIyMJwOqx21s1gj7ClzoUAUwcaWDya2zxqq1VmQinuQrS%2Ba6WBzzmK93WwhtacIWeP0c7tyydDdNtM0NW4pHI08eX3gEnpQH7X7oRNxyNHo2srGlw2Z9g7OBRaWPgPxVShz8&X-Amz-Signature=c57952a43a9690ac3f1c6b0f89589b2fea31fa719cd24fac99b85d3758d1f8b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d9e5aec0-bc51-48d2-94f2-21491e487e6b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CXXSVKI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICPZz6N%2Brt6%2B2mcVYvndu9R55p2Wn2fELfR0kJarLZW3AiBnU9Xm0N8HWuVXneFBlRcGnVwXKKMhS6e15XJxqaZ8YSr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMj4qiuV6C7aOMkbZOKtwDEHnrEeR7%2Bvk8VwbupVOxXNMegCJhzkkOOy%2B8jxDZexsBpY1MIbeM65IHWUkJatEwGZYVVm2GYqRvxcfCrmlRMhGXysPhv7ts8xr4dO5Vq3H2RmR1rskPT7GvEgs4OwMMXeseVrF1tybnmU9y%2Bu44sdxKmpSCaXjesmOlvIIO3Ge87jkrMNqYs2UGermkT1WtnW3pQ74JHRPVUrTZSW8i6yZzVvynT%2Bcft4paIwOunc%2BR9QYhLba%2FKLin%2BsEZAVDI0a%2BfUBjpZCFSrbMZ1JpRBflz%2F9wFUe22X0n7Wopnj0EwApYrebOq8NZbjSiyop%2BmpC69QwIjQEQWVpd35Eq6xFEmthZzpqeEQiQk%2B0FeeUCek8K3xg5jQxP7cb0SvKDE4Hkd1k1OVy58%2Bfb%2BiKOx8FvjccOmlH3xJi98ty0ScpkrG0DYMmAUTn0mB0WITxsVEHEqQ6qJlD3YdlMrnyOdrsC8k%2B8NvUy9ZEG%2FqZd8ew4DDeMZ9gWg69B9WNGkNB0qWgn9kb2AfrXQTdMRJX1JG8YG0STxiwXeiFq1XPyVZt6THw12GWnAifdzAXRzElsbS%2B1jY%2Fq%2FxJeMbO9df1iwJCScnDFHELpH93iGLJf4P5vQcyIgZI0QxSgzSqQwqs73yQY6pgEkHdwm8lSexgLfLNjmIVEY1CscfltVcM6l8XDtv0JJAIBPX75NQRRgFrv5iYVcLpwKNSRlGV6TpvHcqKyW9%2FmsRU0ZOEcUttFxlRvW9J%2FWRijvn%2FcFspbDt4dZwqHb8CYgawNIUSp38AvvFcQ2glYpj2cNqEhBZqq1NBSqGXHzZVSdpGC1fDHvQM1Q8eDOIKXBRflBsLs2WkFAVrnAP5hm8NQUc5ot&X-Amz-Signature=b072a25607edc58a3c7ccaad8a7d21c3e658e9df67d17f862eb94ea3a154b8a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c219addd-4634-4ed7-97e9-9d9433e6027d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CXXSVKI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICPZz6N%2Brt6%2B2mcVYvndu9R55p2Wn2fELfR0kJarLZW3AiBnU9Xm0N8HWuVXneFBlRcGnVwXKKMhS6e15XJxqaZ8YSr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMj4qiuV6C7aOMkbZOKtwDEHnrEeR7%2Bvk8VwbupVOxXNMegCJhzkkOOy%2B8jxDZexsBpY1MIbeM65IHWUkJatEwGZYVVm2GYqRvxcfCrmlRMhGXysPhv7ts8xr4dO5Vq3H2RmR1rskPT7GvEgs4OwMMXeseVrF1tybnmU9y%2Bu44sdxKmpSCaXjesmOlvIIO3Ge87jkrMNqYs2UGermkT1WtnW3pQ74JHRPVUrTZSW8i6yZzVvynT%2Bcft4paIwOunc%2BR9QYhLba%2FKLin%2BsEZAVDI0a%2BfUBjpZCFSrbMZ1JpRBflz%2F9wFUe22X0n7Wopnj0EwApYrebOq8NZbjSiyop%2BmpC69QwIjQEQWVpd35Eq6xFEmthZzpqeEQiQk%2B0FeeUCek8K3xg5jQxP7cb0SvKDE4Hkd1k1OVy58%2Bfb%2BiKOx8FvjccOmlH3xJi98ty0ScpkrG0DYMmAUTn0mB0WITxsVEHEqQ6qJlD3YdlMrnyOdrsC8k%2B8NvUy9ZEG%2FqZd8ew4DDeMZ9gWg69B9WNGkNB0qWgn9kb2AfrXQTdMRJX1JG8YG0STxiwXeiFq1XPyVZt6THw12GWnAifdzAXRzElsbS%2B1jY%2Fq%2FxJeMbO9df1iwJCScnDFHELpH93iGLJf4P5vQcyIgZI0QxSgzSqQwqs73yQY6pgEkHdwm8lSexgLfLNjmIVEY1CscfltVcM6l8XDtv0JJAIBPX75NQRRgFrv5iYVcLpwKNSRlGV6TpvHcqKyW9%2FmsRU0ZOEcUttFxlRvW9J%2FWRijvn%2FcFspbDt4dZwqHb8CYgawNIUSp38AvvFcQ2glYpj2cNqEhBZqq1NBSqGXHzZVSdpGC1fDHvQM1Q8eDOIKXBRflBsLs2WkFAVrnAP5hm8NQUc5ot&X-Amz-Signature=89cf5fa6d16c184d1cf9bb69dccc2c0d932809e2feb0d43b8089673d804ecfc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bf7650b6-881f-4352-af87-8479d2a11196/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3EO6KBC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDLR%2B0OAI5s%2FhW%2FUxPkMd1knIGBuI6dF7ApTXEESllqPwIgfMDmwH1xWvqrY%2FCqvQ39K9kccyepQC%2FEBkeZ1bHMYkUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKozQNLlpLgfhOddGyrcAyK6kgR6ocM1jTC3E7U43jGf5C%2BxyuvZVMxcUgvBe4%2FnhY%2BzG5vF66X8iDx78KNaKAGkkDAvn00P7WXjNcS7aNIvQuq361QrsDL%2Fk38WHT4lAY1q7mcEH3ynzVZlpbjylK9QrYsfbdh%2BtPwTop0pMSyEaOOe%2BJ2ataMzmEcTeMv1RtM4Y5VFUJ7mf5106fVnGpGnZqcAjyqnBjiQY83kgaCwBEaxdTxwzHK19rHYVTK8C1%2F4dw%2BQnco5EaRTL5N2c9oJvtiIF0nOhqtUhxfp%2B0bv49iwPYhHCMYBwV7e36mdY2Cbo%2FL%2Bl2ww%2Fxg90zdIFfPqnK1upbkQCWVqMByGskIEbE%2FttxqNnBsgCkyWl1udbWEmvTzkLmLBdt%2BSArA5lCTTQay%2BaKjpgW2Bbs%2FFeHDSVrWWx6ljlG%2BliD5Mk7mXFP%2BwzYO8fAx5UcGRC219jJjmca1%2Be9R%2BZoLvy0bRBKrArJotYeKApR5WyTa3%2BbW3jiREJlw4lJlnleZ5XXAqgTyKtvOOVdX7fCF2gHUk7lHxhMKqnGCX5qItfn%2FWom5NtgtADi4gaCVBEVWSK7ci335M9lBMcjHcxl1Jo7M%2BjxA0NvHpy3%2Fi%2FTE%2FJWxw81x1e1u96mJcTM7WxCWzMPLO98kGOqUBhdJVhFj%2FRj3a5TvHOs2Xs%2FqkaI220QcGqHP144fX0Cr25dPI5w5jNOcJSuuteD8Z3gdHNyQBLj2bL7TBduIpSUxC2mioveLoAShLrvViDc7ktu5ypwm59641MKw2%2BjWfEvn77wgpSY4zhtzguWH9pbe1HrZr1ki6%2FtQspK8%2Bm2ZyI391iN4g%2FAZtahVXex3HHRd%2BlJisNOYEnTOXgJ5BXsNq70q9&X-Amz-Signature=2d4322f66825e712c3047fba7b1a0c5e48f2e6dbe66546bb7719627168a9a17d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we want to have this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e812d65a-f8b9-4756-9d4e-9c2351985a16/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3EO6KBC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDLR%2B0OAI5s%2FhW%2FUxPkMd1knIGBuI6dF7ApTXEESllqPwIgfMDmwH1xWvqrY%2FCqvQ39K9kccyepQC%2FEBkeZ1bHMYkUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKozQNLlpLgfhOddGyrcAyK6kgR6ocM1jTC3E7U43jGf5C%2BxyuvZVMxcUgvBe4%2FnhY%2BzG5vF66X8iDx78KNaKAGkkDAvn00P7WXjNcS7aNIvQuq361QrsDL%2Fk38WHT4lAY1q7mcEH3ynzVZlpbjylK9QrYsfbdh%2BtPwTop0pMSyEaOOe%2BJ2ataMzmEcTeMv1RtM4Y5VFUJ7mf5106fVnGpGnZqcAjyqnBjiQY83kgaCwBEaxdTxwzHK19rHYVTK8C1%2F4dw%2BQnco5EaRTL5N2c9oJvtiIF0nOhqtUhxfp%2B0bv49iwPYhHCMYBwV7e36mdY2Cbo%2FL%2Bl2ww%2Fxg90zdIFfPqnK1upbkQCWVqMByGskIEbE%2FttxqNnBsgCkyWl1udbWEmvTzkLmLBdt%2BSArA5lCTTQay%2BaKjpgW2Bbs%2FFeHDSVrWWx6ljlG%2BliD5Mk7mXFP%2BwzYO8fAx5UcGRC219jJjmca1%2Be9R%2BZoLvy0bRBKrArJotYeKApR5WyTa3%2BbW3jiREJlw4lJlnleZ5XXAqgTyKtvOOVdX7fCF2gHUk7lHxhMKqnGCX5qItfn%2FWom5NtgtADi4gaCVBEVWSK7ci335M9lBMcjHcxl1Jo7M%2BjxA0NvHpy3%2Fi%2FTE%2FJWxw81x1e1u96mJcTM7WxCWzMPLO98kGOqUBhdJVhFj%2FRj3a5TvHOs2Xs%2FqkaI220QcGqHP144fX0Cr25dPI5w5jNOcJSuuteD8Z3gdHNyQBLj2bL7TBduIpSUxC2mioveLoAShLrvViDc7ktu5ypwm59641MKw2%2BjWfEvn77wgpSY4zhtzguWH9pbe1HrZr1ki6%2FtQspK8%2Bm2ZyI391iN4g%2FAZtahVXex3HHRd%2BlJisNOYEnTOXgJ5BXsNq70q9&X-Amz-Signature=1d4918fd552817345f3833d046fdcd448c46d390c8ed230ca85aac91c87c9b93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bf7650b6-881f-4352-af87-8479d2a11196/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3EO6KBC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDLR%2B0OAI5s%2FhW%2FUxPkMd1knIGBuI6dF7ApTXEESllqPwIgfMDmwH1xWvqrY%2FCqvQ39K9kccyepQC%2FEBkeZ1bHMYkUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKozQNLlpLgfhOddGyrcAyK6kgR6ocM1jTC3E7U43jGf5C%2BxyuvZVMxcUgvBe4%2FnhY%2BzG5vF66X8iDx78KNaKAGkkDAvn00P7WXjNcS7aNIvQuq361QrsDL%2Fk38WHT4lAY1q7mcEH3ynzVZlpbjylK9QrYsfbdh%2BtPwTop0pMSyEaOOe%2BJ2ataMzmEcTeMv1RtM4Y5VFUJ7mf5106fVnGpGnZqcAjyqnBjiQY83kgaCwBEaxdTxwzHK19rHYVTK8C1%2F4dw%2BQnco5EaRTL5N2c9oJvtiIF0nOhqtUhxfp%2B0bv49iwPYhHCMYBwV7e36mdY2Cbo%2FL%2Bl2ww%2Fxg90zdIFfPqnK1upbkQCWVqMByGskIEbE%2FttxqNnBsgCkyWl1udbWEmvTzkLmLBdt%2BSArA5lCTTQay%2BaKjpgW2Bbs%2FFeHDSVrWWx6ljlG%2BliD5Mk7mXFP%2BwzYO8fAx5UcGRC219jJjmca1%2Be9R%2BZoLvy0bRBKrArJotYeKApR5WyTa3%2BbW3jiREJlw4lJlnleZ5XXAqgTyKtvOOVdX7fCF2gHUk7lHxhMKqnGCX5qItfn%2FWom5NtgtADi4gaCVBEVWSK7ci335M9lBMcjHcxl1Jo7M%2BjxA0NvHpy3%2Fi%2FTE%2FJWxw81x1e1u96mJcTM7WxCWzMPLO98kGOqUBhdJVhFj%2FRj3a5TvHOs2Xs%2FqkaI220QcGqHP144fX0Cr25dPI5w5jNOcJSuuteD8Z3gdHNyQBLj2bL7TBduIpSUxC2mioveLoAShLrvViDc7ktu5ypwm59641MKw2%2BjWfEvn77wgpSY4zhtzguWH9pbe1HrZr1ki6%2FtQspK8%2Bm2ZyI391iN4g%2FAZtahVXex3HHRd%2BlJisNOYEnTOXgJ5BXsNq70q9&X-Amz-Signature=2d4322f66825e712c3047fba7b1a0c5e48f2e6dbe66546bb7719627168a9a17d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we want to have this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/35b45d58-c46d-4039-952f-492de3ea98a3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3EO6KBC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDLR%2B0OAI5s%2FhW%2FUxPkMd1knIGBuI6dF7ApTXEESllqPwIgfMDmwH1xWvqrY%2FCqvQ39K9kccyepQC%2FEBkeZ1bHMYkUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKozQNLlpLgfhOddGyrcAyK6kgR6ocM1jTC3E7U43jGf5C%2BxyuvZVMxcUgvBe4%2FnhY%2BzG5vF66X8iDx78KNaKAGkkDAvn00P7WXjNcS7aNIvQuq361QrsDL%2Fk38WHT4lAY1q7mcEH3ynzVZlpbjylK9QrYsfbdh%2BtPwTop0pMSyEaOOe%2BJ2ataMzmEcTeMv1RtM4Y5VFUJ7mf5106fVnGpGnZqcAjyqnBjiQY83kgaCwBEaxdTxwzHK19rHYVTK8C1%2F4dw%2BQnco5EaRTL5N2c9oJvtiIF0nOhqtUhxfp%2B0bv49iwPYhHCMYBwV7e36mdY2Cbo%2FL%2Bl2ww%2Fxg90zdIFfPqnK1upbkQCWVqMByGskIEbE%2FttxqNnBsgCkyWl1udbWEmvTzkLmLBdt%2BSArA5lCTTQay%2BaKjpgW2Bbs%2FFeHDSVrWWx6ljlG%2BliD5Mk7mXFP%2BwzYO8fAx5UcGRC219jJjmca1%2Be9R%2BZoLvy0bRBKrArJotYeKApR5WyTa3%2BbW3jiREJlw4lJlnleZ5XXAqgTyKtvOOVdX7fCF2gHUk7lHxhMKqnGCX5qItfn%2FWom5NtgtADi4gaCVBEVWSK7ci335M9lBMcjHcxl1Jo7M%2BjxA0NvHpy3%2Fi%2FTE%2FJWxw81x1e1u96mJcTM7WxCWzMPLO98kGOqUBhdJVhFj%2FRj3a5TvHOs2Xs%2FqkaI220QcGqHP144fX0Cr25dPI5w5jNOcJSuuteD8Z3gdHNyQBLj2bL7TBduIpSUxC2mioveLoAShLrvViDc7ktu5ypwm59641MKw2%2BjWfEvn77wgpSY4zhtzguWH9pbe1HrZr1ki6%2FtQspK8%2Bm2ZyI391iN4g%2FAZtahVXex3HHRd%2BlJisNOYEnTOXgJ5BXsNq70q9&X-Amz-Signature=b1042b86e32e0ca442af0049a43ac1cf03164e3fe1aeb44ba4460a9b7f999a0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1706f8e7-a234-40f0-aba2-dbd75215db31/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XE75Y5W4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCrZGvMyoh%2FXpcoXUXnlqPDqQ8d%2FoxvMrUqxaFdKbiRZwIhAIwNDhDMGAs%2BCcCZ%2Bg8qoIwGehFlN9%2BCT8ZRXayurTfSKv8DCCcQABoMNjM3NDIzMTgzODA1IgwE8pLlLfsURygqVEAq3AME984YsfttmAm8eFD5hYKLNY%2FxIUKo4l3wnbqmm3L%2FTQD04%2B%2B53QL4ODItksG163GiOiEMHdneiIHmo0SXrA2AcQkg3YxIKiRp3DRf3uru2h12%2F8%2FnK8AG0rCCC79%2B3Cn1U58soJ0DjzpHFtXyOe2r%2BK5q3fGBYv5IKphdzt5%2BYJBCYmApqhnmU3CaGzl2JTMF1lTjOGeRVROnHvp1AXQca2NYFZqY3ZXGPg8e3StD14RSG2zg4NkzRbkL3UNDkilXauGvBcEs24XQpvoym2SDsZ1gphcnapRZ2pv9ZWPrglRRJMLTCwlVy58jprFa5y5eVy9OGJyesLysE1oXfkkIMys1kRirlqq4ML2zbTCotMNtK47Z%2FryIfegvgmltC4EME1GUVuLRaKrcMTkyywAhav1HHbJAzffLmA6LFXtoe5eZax%2BRX0wNv3bd4X0tcO1GJ%2BsJlC5O4Wbgo2sX9WapAbyaHLbpzy3MTDSGQBrkUZ8q0q1qqrzu8en0jPO1AGN%2FjahW82MMkdul5aV%2Bd75MjPhW5h%2BqbIJ1%2FyacdKQYArWKO6PXiekNBd2BD248Apj4n91G2QWNntagnp2eBv5HYzVohOm%2FPpGy8E8VlqIwT3r68gAwCcGKCnNnUDCIzvfJBjqkAUZOw7dp8djQ7Y9idWMtfwvU1PlaDo2dYApnrF1UkO7ikSTsF9B6ILIi8ac2ps2%2F6LQ2Z38yDqr73vTFO4zePonK3%2F6CAsTk3JMpVRgMlYb4l%2FvEnzbmUGe2er9nCEu8cF7gvrUWb1iKTJpZstb%2F1g5FF24vMJIVA2SXJ5W2ECW5bYRPMf6Jqj9UeHmwjpdDy%2BykzkcNSfaIaOXDupak3p7yXgt6&X-Amz-Signature=c6d6245d340d9eaf592956fa2e3cc63ef635a1c5121133bfeeffe6a1ba8f4e44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/655ae48c-f696-4775-9b67-321fc8af6a1f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTLHF22A%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC43UyREZ5nTasPDnWs88KM91FaqouER49KBwAB60ScBAIhALUAZIXB%2B7dfCcNE9sauNG4YqqVj0fRfYoixn2yJuqdTKv8DCCcQABoMNjM3NDIzMTgzODA1IgxInTdEtq271wykrIMq3AMW48p7rMlcjiNogzEbCA6XOOnip90sAYpm%2FCs7UXeMsCz77PsKK07hZWIlJCbRbxIr%2BZ1hFrxs%2FBZ1FqPCp2b8JMBMyV53NNYAp%2F%2F7JR8X0gKJUZ903vdIDLxozRfm6g93gpFxfitklacz8oO3TMDjkV7dgL4XANRZsK8tU4rlOw7O5an7fSyN4%2BYmIJUnxFZ27t7OUFb2L%2F0%2FDmoTTMMUp0e0nOStL3pYNlTY9eIr3Uw%2B9y6DnNaBnSWNgqqIMkHo7KDhOahar5EimzAzkuPatNRA6qPf5tEc75gegTvpRDEhtbFu2my2yZd20xx%2FPTBGikeJl%2F19%2FgsYQMRKA07%2BOrQCniEapCUlfEnIpJrNcoXdOqL0FW9o2oQKkstTFU1CeJ7GRgPHCXHYpthppbVHdcm9Vs3j1qTCQQ0DKzmpx2JThd07reTiuAiv0QaAajZg1YBvV59pDH5TtbdRtt%2B%2BXF5NtOC4eO1ZCysErQIldlQ1TCM%2FPUbWcOfeMTOSgCqw6Lefbv6fBZTEk3Seg9LPjXC%2Bnp9Boqz4nxEarhZDOm5Sk%2FA7vdSh1P7hHJGmruAe0X8oPdds%2BU%2Fw28liAYVhKc8vEYbbPQorcFRpGBJL%2FkysIUsMZHnIHuIMDjCDzvfJBjqkAX%2FBjp8D9EsRHYnoq2zK4q3%2BWQcC3cAWAuluQ8RHiYB16ycuoviRIJZXGpqmLI8xjlrGCmcUy4hfdMNQJ3Tt3UtXSgu9EyvecXUXqEen0E9Eb0AsO9%2F457rRGr84ZRO0xEgoz%2BVGeCrVxv6lJE6AvwxYfG3imHCY6mimr0Y6aKQ1kHNLRmsEIIPMYvef%2BlAej6eBBHviupf%2BlIttksIeK6ZGezJK&X-Amz-Signature=d1a3ba3455e35ed1de193a9e97dc86aacbeaafe289f1d10b736b24933124e12d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we want to have this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8dcd1760-888e-4e2f-938e-8902a8c020d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3EO6KBC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDLR%2B0OAI5s%2FhW%2FUxPkMd1knIGBuI6dF7ApTXEESllqPwIgfMDmwH1xWvqrY%2FCqvQ39K9kccyepQC%2FEBkeZ1bHMYkUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKozQNLlpLgfhOddGyrcAyK6kgR6ocM1jTC3E7U43jGf5C%2BxyuvZVMxcUgvBe4%2FnhY%2BzG5vF66X8iDx78KNaKAGkkDAvn00P7WXjNcS7aNIvQuq361QrsDL%2Fk38WHT4lAY1q7mcEH3ynzVZlpbjylK9QrYsfbdh%2BtPwTop0pMSyEaOOe%2BJ2ataMzmEcTeMv1RtM4Y5VFUJ7mf5106fVnGpGnZqcAjyqnBjiQY83kgaCwBEaxdTxwzHK19rHYVTK8C1%2F4dw%2BQnco5EaRTL5N2c9oJvtiIF0nOhqtUhxfp%2B0bv49iwPYhHCMYBwV7e36mdY2Cbo%2FL%2Bl2ww%2Fxg90zdIFfPqnK1upbkQCWVqMByGskIEbE%2FttxqNnBsgCkyWl1udbWEmvTzkLmLBdt%2BSArA5lCTTQay%2BaKjpgW2Bbs%2FFeHDSVrWWx6ljlG%2BliD5Mk7mXFP%2BwzYO8fAx5UcGRC219jJjmca1%2Be9R%2BZoLvy0bRBKrArJotYeKApR5WyTa3%2BbW3jiREJlw4lJlnleZ5XXAqgTyKtvOOVdX7fCF2gHUk7lHxhMKqnGCX5qItfn%2FWom5NtgtADi4gaCVBEVWSK7ci335M9lBMcjHcxl1Jo7M%2BjxA0NvHpy3%2Fi%2FTE%2FJWxw81x1e1u96mJcTM7WxCWzMPLO98kGOqUBhdJVhFj%2FRj3a5TvHOs2Xs%2FqkaI220QcGqHP144fX0Cr25dPI5w5jNOcJSuuteD8Z3gdHNyQBLj2bL7TBduIpSUxC2mioveLoAShLrvViDc7ktu5ypwm59641MKw2%2BjWfEvn77wgpSY4zhtzguWH9pbe1HrZr1ki6%2FtQspK8%2Bm2ZyI391iN4g%2FAZtahVXex3HHRd%2BlJisNOYEnTOXgJ5BXsNq70q9&X-Amz-Signature=6d01cf5f40f9bd17025c23de0cc080454199821c9d4c61d16ae1b846e3a8fa92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/42243842-134c-402b-8764-bc2bac3684d2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3EO6KBC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDLR%2B0OAI5s%2FhW%2FUxPkMd1knIGBuI6dF7ApTXEESllqPwIgfMDmwH1xWvqrY%2FCqvQ39K9kccyepQC%2FEBkeZ1bHMYkUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKozQNLlpLgfhOddGyrcAyK6kgR6ocM1jTC3E7U43jGf5C%2BxyuvZVMxcUgvBe4%2FnhY%2BzG5vF66X8iDx78KNaKAGkkDAvn00P7WXjNcS7aNIvQuq361QrsDL%2Fk38WHT4lAY1q7mcEH3ynzVZlpbjylK9QrYsfbdh%2BtPwTop0pMSyEaOOe%2BJ2ataMzmEcTeMv1RtM4Y5VFUJ7mf5106fVnGpGnZqcAjyqnBjiQY83kgaCwBEaxdTxwzHK19rHYVTK8C1%2F4dw%2BQnco5EaRTL5N2c9oJvtiIF0nOhqtUhxfp%2B0bv49iwPYhHCMYBwV7e36mdY2Cbo%2FL%2Bl2ww%2Fxg90zdIFfPqnK1upbkQCWVqMByGskIEbE%2FttxqNnBsgCkyWl1udbWEmvTzkLmLBdt%2BSArA5lCTTQay%2BaKjpgW2Bbs%2FFeHDSVrWWx6ljlG%2BliD5Mk7mXFP%2BwzYO8fAx5UcGRC219jJjmca1%2Be9R%2BZoLvy0bRBKrArJotYeKApR5WyTa3%2BbW3jiREJlw4lJlnleZ5XXAqgTyKtvOOVdX7fCF2gHUk7lHxhMKqnGCX5qItfn%2FWom5NtgtADi4gaCVBEVWSK7ci335M9lBMcjHcxl1Jo7M%2BjxA0NvHpy3%2Fi%2FTE%2FJWxw81x1e1u96mJcTM7WxCWzMPLO98kGOqUBhdJVhFj%2FRj3a5TvHOs2Xs%2FqkaI220QcGqHP144fX0Cr25dPI5w5jNOcJSuuteD8Z3gdHNyQBLj2bL7TBduIpSUxC2mioveLoAShLrvViDc7ktu5ypwm59641MKw2%2BjWfEvn77wgpSY4zhtzguWH9pbe1HrZr1ki6%2FtQspK8%2Bm2ZyI391iN4g%2FAZtahVXex3HHRd%2BlJisNOYEnTOXgJ5BXsNq70q9&X-Amz-Signature=7638f526fd433c503267f2a2d60a24c610d134f0dc318c7044116be9a762f648&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/afb3d2ea-66c0-4a3c-8b6c-1aed883fd9a7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3EO6KBC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDLR%2B0OAI5s%2FhW%2FUxPkMd1knIGBuI6dF7ApTXEESllqPwIgfMDmwH1xWvqrY%2FCqvQ39K9kccyepQC%2FEBkeZ1bHMYkUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKozQNLlpLgfhOddGyrcAyK6kgR6ocM1jTC3E7U43jGf5C%2BxyuvZVMxcUgvBe4%2FnhY%2BzG5vF66X8iDx78KNaKAGkkDAvn00P7WXjNcS7aNIvQuq361QrsDL%2Fk38WHT4lAY1q7mcEH3ynzVZlpbjylK9QrYsfbdh%2BtPwTop0pMSyEaOOe%2BJ2ataMzmEcTeMv1RtM4Y5VFUJ7mf5106fVnGpGnZqcAjyqnBjiQY83kgaCwBEaxdTxwzHK19rHYVTK8C1%2F4dw%2BQnco5EaRTL5N2c9oJvtiIF0nOhqtUhxfp%2B0bv49iwPYhHCMYBwV7e36mdY2Cbo%2FL%2Bl2ww%2Fxg90zdIFfPqnK1upbkQCWVqMByGskIEbE%2FttxqNnBsgCkyWl1udbWEmvTzkLmLBdt%2BSArA5lCTTQay%2BaKjpgW2Bbs%2FFeHDSVrWWx6ljlG%2BliD5Mk7mXFP%2BwzYO8fAx5UcGRC219jJjmca1%2Be9R%2BZoLvy0bRBKrArJotYeKApR5WyTa3%2BbW3jiREJlw4lJlnleZ5XXAqgTyKtvOOVdX7fCF2gHUk7lHxhMKqnGCX5qItfn%2FWom5NtgtADi4gaCVBEVWSK7ci335M9lBMcjHcxl1Jo7M%2BjxA0NvHpy3%2Fi%2FTE%2FJWxw81x1e1u96mJcTM7WxCWzMPLO98kGOqUBhdJVhFj%2FRj3a5TvHOs2Xs%2FqkaI220QcGqHP144fX0Cr25dPI5w5jNOcJSuuteD8Z3gdHNyQBLj2bL7TBduIpSUxC2mioveLoAShLrvViDc7ktu5ypwm59641MKw2%2BjWfEvn77wgpSY4zhtzguWH9pbe1HrZr1ki6%2FtQspK8%2Bm2ZyI391iN4g%2FAZtahVXex3HHRd%2BlJisNOYEnTOXgJ5BXsNq70q9&X-Amz-Signature=332289cbf59ff5f79024dc5f16da2946319326978a28e5e829a18268c0f7c515&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7860251e-e68c-4a7f-a413-d6ddfd5fd578/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSX6ZP77%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDUCgGdZRLu8YQFA1%2FxW5UAdWgSKE4f%2FoFurXOppOqqzwIhAP3WcxogfmfbMxKfElxmhUiBosfcoWQ%2FmjvmVKLojq8pKv8DCCcQABoMNjM3NDIzMTgzODA1IgzgwpFvu39IIFfGJZQq3APCf9THbBLcDXTpMqG2vlGeAeCRbfgXYmmpvZqxHXkZQDZz52iH1QypPCzTA2L8d2OaOwDwR9d1%2Bx7pVVP5YCgQ5%2BZQG9sqeUKL6Hs4dnOWh597GyA18oh0bf8EegfebgT18FOoaD0pbr2%2FFKXXH8yq%2BIckQFp4%2FmtGW4mp4H3dojHPUEaBScvTuM%2F0330VUhyh4ieEaBqhsXXchITx3Z9BoYCAB8vhBlNbwJ72FS3q6p0gSaW9TWBa%2Be5CHx%2BOeL2mmJjrJhRRcj0N7%2BsckxRdBMGCWjC9MrsPHCTD5CvWjFAqzMMOocL8UZdrj5OB%2FBr21Db9V7bSRczud7DBQ7vAvpjkW3UHMzXxZ1gtWRzMhQebaURerhE35XXQhLrQC5qE6N8wB2hbXXAB9P0JttzkGapsEXmO3fwsT7O48c0yDI%2Bp6DtFRvLU4JDMc6UpilNfeJCbTEfAXvXXygXNCXWEC4mzqyS0sCemp%2FM4eAs8WaQWJxou3BxFNidhfeLXwF787CrKUq2SQaGoJ1s5xQtWDf85jB3TeqGtP19lgjYm2bn3yYYQYgAc1yliOHMyXm8BqRGZkaSycmR9HjRkQ9fdfXaBD5%2BTSKIJyzZ9KktQCPwykfheo6oc0OlGyjCyzvfJBjqkAd4%2BVQGV9zQDkor4NOZpd8revnrUsugdHrbBcO2BeAVLWVFlB4nujgEV4tRh662nYRVD1IC3ofSYMotFJp%2Fu6vkViYXpa9EOhQPba3P0GCuxoChKvpaP4SNsdFhpUogJ0NKi8hIvbwVJXwGSSJTep5slsNxg1Lm4hSuVTP1D6sA7BvD4OMnR78WmRZTjavT9IsIo7byErtJ373VLggJsk9eWcJYt&X-Amz-Signature=05b18fa374fe95a7de5e7885d00394b3922cc6e96ae2cc1558b6b45e951267bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<u>Table Courses</u>
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cbabca09-d632-450b-9e21-c60709d4161d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSX6ZP77%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDUCgGdZRLu8YQFA1%2FxW5UAdWgSKE4f%2FoFurXOppOqqzwIhAP3WcxogfmfbMxKfElxmhUiBosfcoWQ%2FmjvmVKLojq8pKv8DCCcQABoMNjM3NDIzMTgzODA1IgzgwpFvu39IIFfGJZQq3APCf9THbBLcDXTpMqG2vlGeAeCRbfgXYmmpvZqxHXkZQDZz52iH1QypPCzTA2L8d2OaOwDwR9d1%2Bx7pVVP5YCgQ5%2BZQG9sqeUKL6Hs4dnOWh597GyA18oh0bf8EegfebgT18FOoaD0pbr2%2FFKXXH8yq%2BIckQFp4%2FmtGW4mp4H3dojHPUEaBScvTuM%2F0330VUhyh4ieEaBqhsXXchITx3Z9BoYCAB8vhBlNbwJ72FS3q6p0gSaW9TWBa%2Be5CHx%2BOeL2mmJjrJhRRcj0N7%2BsckxRdBMGCWjC9MrsPHCTD5CvWjFAqzMMOocL8UZdrj5OB%2FBr21Db9V7bSRczud7DBQ7vAvpjkW3UHMzXxZ1gtWRzMhQebaURerhE35XXQhLrQC5qE6N8wB2hbXXAB9P0JttzkGapsEXmO3fwsT7O48c0yDI%2Bp6DtFRvLU4JDMc6UpilNfeJCbTEfAXvXXygXNCXWEC4mzqyS0sCemp%2FM4eAs8WaQWJxou3BxFNidhfeLXwF787CrKUq2SQaGoJ1s5xQtWDf85jB3TeqGtP19lgjYm2bn3yYYQYgAc1yliOHMyXm8BqRGZkaSycmR9HjRkQ9fdfXaBD5%2BTSKIJyzZ9KktQCPwykfheo6oc0OlGyjCyzvfJBjqkAd4%2BVQGV9zQDkor4NOZpd8revnrUsugdHrbBcO2BeAVLWVFlB4nujgEV4tRh662nYRVD1IC3ofSYMotFJp%2Fu6vkViYXpa9EOhQPba3P0GCuxoChKvpaP4SNsdFhpUogJ0NKi8hIvbwVJXwGSSJTep5slsNxg1Lm4hSuVTP1D6sA7BvD4OMnR78WmRZTjavT9IsIo7byErtJ373VLggJsk9eWcJYt&X-Amz-Signature=e09926baaef133e08500ae848a2e23090fb514fef28c143427158ef286c1d703&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7e1c0470-ce21-4d6a-a1a7-16214fa6fc4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DGHT5HY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQC8Epis%2FaABxY0X0x7%2BuIYSPd6DehSRlVnpf5CEZYUlngIgGSj3FKgIVd9dlbDXk3KG133gLtVkC6jayPtCHfmtGeoq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJbD7SEr96%2FF0zVKaCrcAzXZs1jQDM3CqkpqaQxeaocj9LHnaCpThWsySevOIDhLhr%2FDMXdrvmtZX%2B8xD%2F5qt2Y%2F0DfcWn8rsoGnrqyioadncu7PNWRR5wJkD10OHz56k8HcKnYA9LrGKXL4YgDqbErN63%2FXPFacWkxwTeMKvSvj5A5d%2FWbrMi9ILaClEK%2F%2FOzrd3%2Fd9wqd8kjgFe01jxgBXr1b9obNs8akYuInaTd6nxWR%2BYsu8CLwEGFoRyhM%2BsEqMqjMqfWeiH%2FINBiQHk20SeHRlQq3dQBbJHj%2BoJ4nWBKGvDzP465%2FhnYp4Y%2BilI0sei07C5k86aPxFZcNDEmMqZrKzLvDK2RjMVysPYLxGRXrgid2iIE2C6PgII%2BQEb65dp547oeVUGJBNS8Gprm8NhKBUcVO8RIdYsDjoST7%2FcBhXVGDcFAFl8Tmg7bpvcTug%2FcyOzYs0vsUYzK8vJtYlXDMUWwVHbcAoFVT5Tk2pFC0M2IM0t%2F4uUQ%2Bx9yQfnxpoeeYvPlAIjusihxqILxVuzbl5uPW%2F6bFuVHuixZecWga%2Bs4vXQzYtY6QiwhPsaj4lxjmNRuEVy%2BPuPUTOrVBJ0Jrwm2sUFK4ktwnbNsYXHXyFtj2P6Jj0C4KBimYl9cpvaPaLnzLZb3PUMOTN98kGOqUByiPuXVYICN3GNSd0AqMl0mD14LglmS3NCF6Nz%2BrRCdR%2BxByvpNLTnMSGXjlokca47A2sVev5Eb3Fx8XJiG1W6%2Fphg13%2BQUn2lCS7Zea7oSZkqv1yiqvTwfUnczlTQ7QnqjdS%2BNM5XSCCYOzeeA2T0Gh7GeggMrI%2B6clDKsZgkJMd2cv4f%2F6whIdC%2B2u55o0%2F2nIoXvQn37A6PK3nH9A7XKnPksOd&X-Amz-Signature=308f8e59aeecf54036535c637d3a4c45a429f00c8c1ba3bce437196986196325&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRXXDPZO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD5OjqtETt1nKEJ6Ci7nO5zRtrO5Evmy11IDIFwP2SyxQIgAe35Hwzu8PULnNx13jHvRhxiKBZiPjZnchbUUVpsu28q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMLXQio0golXw3c8rCrcA0QnmddEkxatEgZ0ByyzlphfqrTYEtPodVZ3OUt3IKVgIgfUM9P6E7LqDXNBl9Wd7gw%2BcKMn%2FY5NUWJNVVfJGOmAc5ZRIWu4kl%2BTrEjkyRfTZ5EpCiy9RSSVrTQsyzzNxWPuKB3JMWbpdfgbSICcmU5W%2F9s65jT%2BbZmtCKHDKxfll5SJ5WZoRVa6tjLN9cuH3w4QUl4KX%2F5i%2FFIphxn13NDbAJ4qd3DoMbXmTVcQUQ%2BB589vwZBRikhIDX9w4FNm1vIlvy7NXTR%2BrpYq5o%2FSzrDjnUthx1wqZe7Z42ZQdc%2FLy%2BeqT246JKDkAccgMEcNAnqxrkVtmN5u%2FnlFMW5YoKPiGxxJxOyCIAp1eG%2FK3YZhjrY13%2BLYAq8g2ZskWp%2BhZF65MikoRGU17qEK86b9xpL2Kg5NRPkrYZIGU4zAfs2%2Bx7S5FAX7fbjEhBtoxJflrm3TPvrTiBelvYujuVpSxC0RisdRNMW7ukNyNblt8NFt2xpCHVXZQcJdkGRknOF1Tq81NtRktSZnM%2Fkh6Twz8pjkoQbG7HOA3IcZ%2BWcQpH%2BD4GrtZP80Z5HqEKGIYsGyAjcPVlkUv0ATwONTsJeRU755U2SJB0ZbMoKoACZhWNG4fNaYNzwbUhnAAYbzMMHO98kGOqUBCEj%2FvG1YvF%2BY49uF8vRnqiFTucEHZ0%2FrNU%2FgkGPmpxmH2nCO2JiWnuQ70LGuO0SgKCgUAuq48MDITqU0yjd1E1L1obQ4BJWlnh9WFDJx%2FVeQu82HOmmYAtgck3xRCmtp6HV2J2lFVpQAD%2Fm7GOFq25XEcNnHtyuZmoje3z%2F0xXXMK%2F2lT4n0yuMSoPw8xwQbo%2BLESBwxuUgJ4tHwDc0LeKOzkq04&X-Amz-Signature=d2ad833d0455b220e47323f2348b0eedb2836ca367bc531b621d001cddd8c798&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can we access all rows in `my_df` that have a value for `calories` bigger than 300 and a value for `duration` bigger than 40?

<details>
<summary>Solution</summary>

`df.loc[(df['calories'] > 300) & (df['duration'] > 40)]`
OR
`df[(df['calories'] > 300) & (df['duration'] > 400)]`

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b9273317-ed78-4094-b212-ec015d413af7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y626XCDN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIHAHiX4SCPdbYGv6Fi4wSRjXgWlY0hW9LUEEeVtAdByIAiEAu5Y83gy7ACwho80YRu5%2Bje8%2BYYfqfDyHYTvmb5ZS6%2BYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBoNMTM352eHzNeaWyrcA6IUh0PCiWJW6PcRZiTDOW2NOaijhtu4ad2izrKt7fwTIxFoSteMr%2Bj%2F3fvpNgT8iiQMCOWsTnmoaYi0Dhg7fZf3w2B%2F%2FmrHjPKBKeoUSob5EHdXNAN1LzlDD8YBcRNTFsNLqQtBwvIar7qf3p71jMKnI4YuZ3mZEZLZqDF4Y6qx2NqoNRRAwJVDClkdJ9KGtr8QcxKtcz9%2FVvd7vvxDpGwcn5FtTAt2Q5TmnJ0SB%2FAjoZ%2BLDFHJfyDKBaotIsLTVMupHPE3jRqZ6FEDgf4hVP7p7brQklRWcKuS%2FZG%2BYlUyECL74iCaEv0okv9hADZp3LBTUDhBX0KfZhKd2PGhUURuneQXBEcu5yRq44dpFQ2vwjBXt%2FiUbApEyqXOysDtOT7yW5jDDoossYLVVqLYQESzWupUHA0CSwlkMhOAg%2FHLDePN3%2B1FUMK2Rm2iDxHdQC7G78qjt9XtpuaihBBjyEODVyxbXgPHDGJZFHzscaR%2BmruTs70ebHav0piRYriAqkzyOoUCJGEYl%2FLOps114nom9egqmUsTt46cb9RRceQRw2QSshynxpQdZTiS1L31VIQHNBlSQBTcu%2F2Q%2BikQLmOPLXUmUUnc4jdIaFIgXE9gk8d%2BqpJj07GcgqufMLbO98kGOqUB5uQpPXquxLgV%2BjbI3qHnql80cyU%2FAYylAVeWc93BHOnVO4EDGE9NeaApMaEf8ojYI71Y76QnmO4XasIDV3x4MtdGFPFQm2AIY6omBlH6SV2FvkFJf%2Fedcxjci5pgXBsuXw2tKNiE7GvsRh8UWN%2Fxj3lhhbtEfz7msHtxrx%2FTg3Ssh7%2BESfbfILBYNteboPR1YGB3E6908DsnsUoAEHQldhTXuKnM&X-Amz-Signature=3d0459aff76d5698b1882141e5affbe1fffbabe27d927b37ec537b4b1979b585&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3888d003-fe6a-493c-8a99-7b5b73692a67/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRXXDPZO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD5OjqtETt1nKEJ6Ci7nO5zRtrO5Evmy11IDIFwP2SyxQIgAe35Hwzu8PULnNx13jHvRhxiKBZiPjZnchbUUVpsu28q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMLXQio0golXw3c8rCrcA0QnmddEkxatEgZ0ByyzlphfqrTYEtPodVZ3OUt3IKVgIgfUM9P6E7LqDXNBl9Wd7gw%2BcKMn%2FY5NUWJNVVfJGOmAc5ZRIWu4kl%2BTrEjkyRfTZ5EpCiy9RSSVrTQsyzzNxWPuKB3JMWbpdfgbSICcmU5W%2F9s65jT%2BbZmtCKHDKxfll5SJ5WZoRVa6tjLN9cuH3w4QUl4KX%2F5i%2FFIphxn13NDbAJ4qd3DoMbXmTVcQUQ%2BB589vwZBRikhIDX9w4FNm1vIlvy7NXTR%2BrpYq5o%2FSzrDjnUthx1wqZe7Z42ZQdc%2FLy%2BeqT246JKDkAccgMEcNAnqxrkVtmN5u%2FnlFMW5YoKPiGxxJxOyCIAp1eG%2FK3YZhjrY13%2BLYAq8g2ZskWp%2BhZF65MikoRGU17qEK86b9xpL2Kg5NRPkrYZIGU4zAfs2%2Bx7S5FAX7fbjEhBtoxJflrm3TPvrTiBelvYujuVpSxC0RisdRNMW7ukNyNblt8NFt2xpCHVXZQcJdkGRknOF1Tq81NtRktSZnM%2Fkh6Twz8pjkoQbG7HOA3IcZ%2BWcQpH%2BD4GrtZP80Z5HqEKGIYsGyAjcPVlkUv0ATwONTsJeRU755U2SJB0ZbMoKoACZhWNG4fNaYNzwbUhnAAYbzMMHO98kGOqUBCEj%2FvG1YvF%2BY49uF8vRnqiFTucEHZ0%2FrNU%2FgkGPmpxmH2nCO2JiWnuQ70LGuO0SgKCgUAuq48MDITqU0yjd1E1L1obQ4BJWlnh9WFDJx%2FVeQu82HOmmYAtgck3xRCmtp6HV2J2lFVpQAD%2Fm7GOFq25XEcNnHtyuZmoje3z%2F0xXXMK%2F2lT4n0yuMSoPw8xwQbo%2BLESBwxuUgJ4tHwDc0LeKOzkq04&X-Amz-Signature=22749a57e6719e37976af3dc20761b5b30faa24edc1b335f00b898da93795f84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ef351802-9321-4c8c-804f-9a26069cb8ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRXXDPZO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD5OjqtETt1nKEJ6Ci7nO5zRtrO5Evmy11IDIFwP2SyxQIgAe35Hwzu8PULnNx13jHvRhxiKBZiPjZnchbUUVpsu28q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMLXQio0golXw3c8rCrcA0QnmddEkxatEgZ0ByyzlphfqrTYEtPodVZ3OUt3IKVgIgfUM9P6E7LqDXNBl9Wd7gw%2BcKMn%2FY5NUWJNVVfJGOmAc5ZRIWu4kl%2BTrEjkyRfTZ5EpCiy9RSSVrTQsyzzNxWPuKB3JMWbpdfgbSICcmU5W%2F9s65jT%2BbZmtCKHDKxfll5SJ5WZoRVa6tjLN9cuH3w4QUl4KX%2F5i%2FFIphxn13NDbAJ4qd3DoMbXmTVcQUQ%2BB589vwZBRikhIDX9w4FNm1vIlvy7NXTR%2BrpYq5o%2FSzrDjnUthx1wqZe7Z42ZQdc%2FLy%2BeqT246JKDkAccgMEcNAnqxrkVtmN5u%2FnlFMW5YoKPiGxxJxOyCIAp1eG%2FK3YZhjrY13%2BLYAq8g2ZskWp%2BhZF65MikoRGU17qEK86b9xpL2Kg5NRPkrYZIGU4zAfs2%2Bx7S5FAX7fbjEhBtoxJflrm3TPvrTiBelvYujuVpSxC0RisdRNMW7ukNyNblt8NFt2xpCHVXZQcJdkGRknOF1Tq81NtRktSZnM%2Fkh6Twz8pjkoQbG7HOA3IcZ%2BWcQpH%2BD4GrtZP80Z5HqEKGIYsGyAjcPVlkUv0ATwONTsJeRU755U2SJB0ZbMoKoACZhWNG4fNaYNzwbUhnAAYbzMMHO98kGOqUBCEj%2FvG1YvF%2BY49uF8vRnqiFTucEHZ0%2FrNU%2FgkGPmpxmH2nCO2JiWnuQ70LGuO0SgKCgUAuq48MDITqU0yjd1E1L1obQ4BJWlnh9WFDJx%2FVeQu82HOmmYAtgck3xRCmtp6HV2J2lFVpQAD%2Fm7GOFq25XEcNnHtyuZmoje3z%2F0xXXMK%2F2lT4n0yuMSoPw8xwQbo%2BLESBwxuUgJ4tHwDc0LeKOzkq04&X-Amz-Signature=4252e201ba0b0db72c8943e4a586e72ed3f177488e33009c9a490e4820e6cce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/984f8797-0e56-4fb4-ad03-41befca8318a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRXXDPZO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD5OjqtETt1nKEJ6Ci7nO5zRtrO5Evmy11IDIFwP2SyxQIgAe35Hwzu8PULnNx13jHvRhxiKBZiPjZnchbUUVpsu28q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMLXQio0golXw3c8rCrcA0QnmddEkxatEgZ0ByyzlphfqrTYEtPodVZ3OUt3IKVgIgfUM9P6E7LqDXNBl9Wd7gw%2BcKMn%2FY5NUWJNVVfJGOmAc5ZRIWu4kl%2BTrEjkyRfTZ5EpCiy9RSSVrTQsyzzNxWPuKB3JMWbpdfgbSICcmU5W%2F9s65jT%2BbZmtCKHDKxfll5SJ5WZoRVa6tjLN9cuH3w4QUl4KX%2F5i%2FFIphxn13NDbAJ4qd3DoMbXmTVcQUQ%2BB589vwZBRikhIDX9w4FNm1vIlvy7NXTR%2BrpYq5o%2FSzrDjnUthx1wqZe7Z42ZQdc%2FLy%2BeqT246JKDkAccgMEcNAnqxrkVtmN5u%2FnlFMW5YoKPiGxxJxOyCIAp1eG%2FK3YZhjrY13%2BLYAq8g2ZskWp%2BhZF65MikoRGU17qEK86b9xpL2Kg5NRPkrYZIGU4zAfs2%2Bx7S5FAX7fbjEhBtoxJflrm3TPvrTiBelvYujuVpSxC0RisdRNMW7ukNyNblt8NFt2xpCHVXZQcJdkGRknOF1Tq81NtRktSZnM%2Fkh6Twz8pjkoQbG7HOA3IcZ%2BWcQpH%2BD4GrtZP80Z5HqEKGIYsGyAjcPVlkUv0ATwONTsJeRU755U2SJB0ZbMoKoACZhWNG4fNaYNzwbUhnAAYbzMMHO98kGOqUBCEj%2FvG1YvF%2BY49uF8vRnqiFTucEHZ0%2FrNU%2FgkGPmpxmH2nCO2JiWnuQ70LGuO0SgKCgUAuq48MDITqU0yjd1E1L1obQ4BJWlnh9WFDJx%2FVeQu82HOmmYAtgck3xRCmtp6HV2J2lFVpQAD%2Fm7GOFq25XEcNnHtyuZmoje3z%2F0xXXMK%2F2lT4n0yuMSoPw8xwQbo%2BLESBwxuUgJ4tHwDc0LeKOzkq04&X-Amz-Signature=caaa6dd39934f251ed1f6d2bc675b2b6832d4e53aef8b3dc62122b69e4572044&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c31ada37-237c-485a-800a-759a40b9f3dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRXXDPZO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD5OjqtETt1nKEJ6Ci7nO5zRtrO5Evmy11IDIFwP2SyxQIgAe35Hwzu8PULnNx13jHvRhxiKBZiPjZnchbUUVpsu28q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMLXQio0golXw3c8rCrcA0QnmddEkxatEgZ0ByyzlphfqrTYEtPodVZ3OUt3IKVgIgfUM9P6E7LqDXNBl9Wd7gw%2BcKMn%2FY5NUWJNVVfJGOmAc5ZRIWu4kl%2BTrEjkyRfTZ5EpCiy9RSSVrTQsyzzNxWPuKB3JMWbpdfgbSICcmU5W%2F9s65jT%2BbZmtCKHDKxfll5SJ5WZoRVa6tjLN9cuH3w4QUl4KX%2F5i%2FFIphxn13NDbAJ4qd3DoMbXmTVcQUQ%2BB589vwZBRikhIDX9w4FNm1vIlvy7NXTR%2BrpYq5o%2FSzrDjnUthx1wqZe7Z42ZQdc%2FLy%2BeqT246JKDkAccgMEcNAnqxrkVtmN5u%2FnlFMW5YoKPiGxxJxOyCIAp1eG%2FK3YZhjrY13%2BLYAq8g2ZskWp%2BhZF65MikoRGU17qEK86b9xpL2Kg5NRPkrYZIGU4zAfs2%2Bx7S5FAX7fbjEhBtoxJflrm3TPvrTiBelvYujuVpSxC0RisdRNMW7ukNyNblt8NFt2xpCHVXZQcJdkGRknOF1Tq81NtRktSZnM%2Fkh6Twz8pjkoQbG7HOA3IcZ%2BWcQpH%2BD4GrtZP80Z5HqEKGIYsGyAjcPVlkUv0ATwONTsJeRU755U2SJB0ZbMoKoACZhWNG4fNaYNzwbUhnAAYbzMMHO98kGOqUBCEj%2FvG1YvF%2BY49uF8vRnqiFTucEHZ0%2FrNU%2FgkGPmpxmH2nCO2JiWnuQ70LGuO0SgKCgUAuq48MDITqU0yjd1E1L1obQ4BJWlnh9WFDJx%2FVeQu82HOmmYAtgck3xRCmtp6HV2J2lFVpQAD%2Fm7GOFq25XEcNnHtyuZmoje3z%2F0xXXMK%2F2lT4n0yuMSoPw8xwQbo%2BLESBwxuUgJ4tHwDc0LeKOzkq04&X-Amz-Signature=0299fc9d017be24314f3245e3ade846d9ad1c3af44d21c8c3d150c25a8d309a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/84b596ef-d755-48f5-bda8-bcbbeaae8b51/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEQ4MJLQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCWdk2IY1%2FABrE6Dt6TCMxldxccM%2B88svCYBC6prYpJAwIgEVurhmFV8%2FdLV8M2RzihBqh0scm7Vpjf8w2G86E5t0cq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDN%2Bxzuct0uu0B%2F37zSrcA%2BlsoDieSyRnuc6MdR6F7cKulMT96khVJekMWqfRh9gHl8aMs1Eklgel6HUfZudBUNWfgwVwOfTMyG2sjPcEDVE9M0dOvkiW%2BhKfI%2F8zjDrj4nE1rx9hmsDqjbk9%2BBtpQEoNC6sz0%2B7iY8zqm%2BcG3Uhnq0rRpTOxXSIS9tf3%2FE038888rQl%2BJyKYiJv6CpHS08olSXbNQ6vUQgQYI3%2Fnh5zdm3RnPo5XA22aY6i2pbfjG7ZrIMfEXPV%2F%2FZjEj4XFDpRMYnzcsn1oAXdJ0RSbxPkugoHE5bur7FzsBtH8cmeS2s8y1FicwMspkUluap3kp7fbT0f6Q1RTMbvdaY%2FWSCEVbimhGOX1fKpSGbzhrzwmWkKucjTV5yA34pn9rbzNOfM5E3mwx77QfSgYkEIt8r%2B3IsW6pOMuDCYBbwhkiXPY%2FOaQTozIx9buIgBEV%2BicoEQsJDsPSWqqD8tduq8ClLiNCTW1k7NIZC0wbir5AMMd9FWA6LOVhcf6xEfmwgbvn%2F7DqabHA1cio0hrlxl7iZ2wpp%2FhklfqA1e4WtPVSnoibvYfxlHy3GkvGrdLUL4xWQKgOJbpGc7iPnhtIR25lTISYYgFlGv0Q6OJYYbl2YeP4fkVdXVlT%2B4zG577MM%2FO98kGOqUBNcBkQ3altwqCtO4iCnlSdTiVVybYrxkKcbLLu1tw%2BgRiK2tbVfJlo3wBRMitc7KZKOVfXjBGJMw0MPyezJffzsF0%2BTmOcNl70rqpnvlSywcxdZWMTTOJ6H%2FMUrvBB4mBPgQhHi5QUYG7Z4dAKJHNA99zjEne7s7dzb24N1EPftRg09jPjOplhHRBt8XKy3%2F6a9WV6UM9y%2BMKV0%2F6SCImH43D1Wzs&X-Amz-Signature=aa683fedc7d1cbc1d5a783dccb261b7df6da5774b9602aa0c9e3c7803f1169ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

📄 **[Code interpretation]** (subpage)
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
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/69f344d2-31be-4540-b0e9-e491aef4f09d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=accdf6e06721ff4dfe98ee242ed478acdbcc5c1a6f74997b5710a37477c05ea2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.shape
```
<details>
<summary>Solution</summary>

`(20, 3)`

</details>
---
[**`.head()`**](/1867045b058343e1a66b677961515907#bc578af731b541f1959e282a7689fb05)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/69f344d2-31be-4540-b0e9-e491aef4f09d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=accdf6e06721ff4dfe98ee242ed478acdbcc5c1a6f74997b5710a37477c05ea2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.head(8)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c8e6dccb-6837-4b57-9313-fc83b502831b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REWCSGST%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAbubJWE7y9rCEVyUviWXu%2FI9B7pAt6QKR%2BKhnDtD4b%2BAiBGjmIMJ4XMWu1kHI0Nsehi%2FwrxDjPMrlmziTy4vezWYSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMBWjWZFwBsKpnmHGGKtwDQtP5GwmCzHlLYq%2BxcR78INAgcaTZD%2Ffd0Gdnb96EiMOt6CnYR0cAOiRNU4uPTsxYrBEkw1gi6xC%2FG9xqwD2Xy7Ojkb9mKVmd9DIwH39zYqVYrCuXRi%2BY55T6WTCN%2B%2FW40C%2Biqddeizpu%2FHDazulaqPW%2ByoLXsZqqmh2C27GwU1dHPYKrjc%2F6tVByKQ%2B%2BoHmkk7xZzsDlJjauCiyF7l1%2BEzJhnkr4eU7cevt6jpwePwmYexR07hisyJNG6WBJuwsFE2YqiowVbRwskYm%2F66YLFi51l%2BwJajHn9TAIpUzYb7WdNrjk01GzKmTaOPIEs%2Fn4tbIesyy8Jfo5WWRUpN3nJPcBQc0i%2FgKlIMWDdKao%2Bz4n50zRNf0H5qXUVy7YeEiPS4zp%2BEnbvmUvPoibbCz0u6QPGP3ljB4zInmi0g3FI6DfVmT0u1gDuZdDYlkh6XScSNkCq9ZuJnbVvxp6v3NOBZDZx3d1aeuFeBYn%2FNuLA11Vu3YjeidgCsfbnz4%2BIg1XdUl4SeCC4KSJ8DVcK1RtYEdOt9afoLQjEG3Nq3AVQX6kawhnv1QE67Hz0xqgqWR2zjZYWvhpzDCLMDo3DPs%2BrJC2arRfX%2BrPs3I2d20pHHjPTuz1qgTG9lZrx3kw8c33yQY6pgFUlgbpFFqUWXsndZWiMQxnVe%2FgFnkVkIz2g72OjD2uxecpJyDTpEr0XzRMaaouL%2FteUTCCsM1EkoecKNfc8mQ1yaYKDsEJ6eYIV1hAZhBAp2ZowH8SiQO5%2Bwt0PoB9TulAGxeoDm51NBYJqMpvUnIVaIFGwHzRFy2llAq%2FDdiLSZQI0CZ8S82nzi3i3JHn2usp%2B4mjQGj7C3rgGxS7Bfp6PW%2B5xNR6&X-Amz-Signature=e67671dd26f0135c0984eb292a8176fad6811bdbea7b7a097d7559302200ffbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.tail()`**](/1867045b058343e1a66b677961515907#c202944531cd4fa68d141eaaf404c2ab)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/58177663-5588-4a8e-96cf-76e8d0fcdd71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=933d4f48bf9fca80275b5d67a2cf1b03ed3f1498740fa461a5b41a37b48f3bf6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df.tail(7).head(2)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/317202e0-51e9-423a-b950-5cb85785cf66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYNAQ2E2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCLRTFHEegV%2FJVGxGjO1uCvkplENliJBlKYyaiQ2emJbwIhAJxIhWxwFGfwfrxZNciuYTj6yHyG1eZlmb7QKQopFLZnKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8Xy%2BLODMXjBOOUtIq3AOsBwqary91DR6ZiNyMOmtckvBY3nkizXhF9YsspHjzyDeP5eEVDteH2gQmevRpOIa4S3YptnV0KAJbZPy%2BzuvGb8nAQr7vM3dSQijlTGd6vXqNw%2BiGyOAAsYHwhPpK%2BSjcH3Fndvli%2FFeJPzsAsFN7rXmbq%2BuusX8v1ANb0L5vBaX1te8Eio7QiFg7HZgvC5KQSkgSquw2i%2Fi3FU%2BrUS5SfnV4ukHjw1lnvkpQzi7dtWtD5X1JtqpP6XXjg4cDCE5aMCvGcS6hvkVbgC%2FS4ZxHyXdlbSNif6Y627o6ryFdGZ%2BBl2bF0YttLVwibfv2vX88N2RuCvYKeXFTl6MF2gajNUTCNu%2FvNz2HjYQonW4%2BYALn86YrMZ%2FKIKIv3AgpPh4PdSgrwsfW9yKIppdlPoDt%2FVyJ4fGUoJ3g8ZYfrRTXgZslFZvXt%2Br5EJfNZ3%2F3ZYd%2Bh2gFcyvoPur0w6CvRj4VJKESx6H0tRpEQfgyW2h4XWQFqxmKZcxhCTdXN54lXzjdEVIpa3edi%2FQjqPdILiy2V%2F%2BwPqia4zeL%2Fm6DsU%2BNTeWE54hLcoILHZfYqKgKdb9k%2Fb0iaxaefyU5%2BI13%2BuBgyJ%2Fqr4VvPQTrgbhIxoxDwOEE%2B5ZZbppm0cIVJTCaz%2FfJBjqkAcVHIgLP4legjcR7GdHvN%2FpqvCz2asaqAmLlYCV6th7k9G43AW0kOwfe3O6KYE%2FTFUNbmN06hlaBN%2FS8zC5KKlNqqfazx7Nh7mO3m87E8dqMd9K8yQVjzgXjNRWdg2NxIXXUMbfW2YfAhbLXuCSqzqkDPxBnCv8PpXBApV8vGl53rD%2Bo4J4dAy2Zl62HwoqaVJWmPCKy2dwvTDKcfSD1Ojw89B%2Fo&X-Amz-Signature=af0b7c3fd38d173374b6df8b6cfd619d19f8d88a9ed1c004e760482c6b03aff2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**Boolean selection**](/1867045b058343e1a66b677961515907#a61901eaa28c4a7da25d80a1223b80f7)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/568f9210-51d8-40dd-ac00-5dbc8b3072c8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=8792fdcc234b05156c50a0d0238bdfda86bef5f82b042b4add291c70170dba7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df[df['A'] > 40]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e4c0ab8e-7b3a-4786-a8c4-a5556c7faa7b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZBNIFI6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCqpHJnR513LPnsrUcNdi3HSSaKQdRIKf32qqsOwxD%2BZAIhANNf5PNUHYwtd04PJF8CyKcEzUbTxi3vMy5IalVoLoDqKv8DCCcQABoMNjM3NDIzMTgzODA1Igynv%2FmsaSw1UT37q3Eq3AMVUc2QApGBDDitt%2FADrDWw936RgAwLV2oatztOdlzNqqEYxEAvO06N%2FTlcj9gTatGIvLUsk%2B5YAZOZ3%2FSBVmI6hhD3ZqnCbVczoca60kHqbnmERvyxImtaKswhmERyezkugNsPO4UNe5sAmqBsS4H9C4QhUlzRNFcv64%2B1C8lNR9YC0DVp9tvTxHvMxNQPdxbpYkBE%2Fgufa658RLT5gT0zPL88EO0dibGrcGmzrptV9kuSorkXQmVLz5VZUAw3kct1gfX6gpafVAXwg07QY%2Bpvu3PKjkcqfclwRDoOTYAcg437o2kfvyfjMZ7gKF0jHn3NfQUUv%2FgvDVxsWS%2F%2FDZGO3Re2A42w15bTenVWdikWYW3tm5WTEUmpNnYun3D4%2FvjivQMhkbQC%2FCsvtt21agCcRQCtvBvpvG%2BQw1OywXPlktt58plo8QQ2GjYpsEz%2BqOVXHcy3Y21H1Z1M2NYED8OOfpDJFDB56onYp5trcc%2F%2BGn7PGoG2YAu%2F%2FCHF%2BMMVXxpljh77MouvDXyCgTSU7tmIHdOgDeQRdIHlZP%2BZOxU9N2dmD%2Fgp6UZGBhGB0p4mnSJiVv%2Fg84VjHp3ouncmmhbhkXSlPrHClxvmEkwxfJv9%2F4S5HL5aXCFEgNWKljDlzffJBjqkAQuzsu77qbLsj3Lp5iQkKxqABlJIWNAHLRXxR8ZElMq%2FDxCAYWbJ7oyzVOwIYN9QtzwkXRWYg06z0ANb9HJ%2BgBx430rDeEzXrwLftzDBM%2BlTUzCdHqNc6EwMfkIrS%2FfyTNleiMLma8hYGbF8nHQ6BjSWkA1hT%2B41t2y4fpzElkbC7gwpvZQAiFf7%2BuCFG15mzs7YChZTLlEL2hz%2FZzyT3xuIviFd&X-Amz-Signature=c69f9019fb0cc910c015bf459deebc92e2f72a4c2daee7d06a4848ff49960384&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df[df['G'] <= 46]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2c37fe90-809c-4f49-98c0-b29a0766191d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEVBKPLW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFxRCCQ74gjvJ%2Fvt4IzwwSJmeJr7K%2BsH%2FCelAnvpmw2vAiB9JevGqF%2FNC%2BQ%2FcMw2ZaKVGwPEF0YvcrqGBNp%2FaXrPEyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMAhLD0CmNf%2FcRL90vKtwDR87sQOIWwaxx6hNOlr8ycw8lgM5ozCWC75BFcNqA6e%2BGzIGrbRTDRz%2Bv90IuDhmmJ622fLMqh%2F8cOKfGa09%2FXLKGIFPfgruIFRXfIlr%2BR5p%2BsC5kSEbmEQkW6aG0HU62USCDdzP0M16ySkrLTGjzpA1OadPi8oPGm71%2FjuEFElQEPnKEU%2Bo4JOJg0kwpM6whgXcDRR1UpvHAFPasuRtVXkK3lqlw0n33N5ZYeux6h4jLrWuzSZM5tbkDbe367jUqqqKHGIZjVEPle8dOc2V84kD09QWzuUTq%2Bkw0ZukkkdOK4xro%2BjuXbIYl8T7gHoJOkL6MVlJ02I1LmPCdAvymTiJuTKK6vWk2uMVBwjfeMOnyNNCAxE2deCl0HBtCSvKfy0gQljCAcCUgRLCGOlgomN6a6H4tEVfZ5lpX4bt0fl%2FGqfrbJ84s8Obq4Vm7CzcXjjymHzcMc8k5wgAtOcjGUifoJy4pF2sdXdYhbXwivgDOlwun1WWiheLBK5lN1lQw%2FSLbl%2BCDfLM%2B5lsOEJiaOZHTWT6YFCDfCbP6pGQZLwVFNsbGw32WgoXYIGL5cZbuOlLJIUe7R7G1DkvYLnu%2Fhe00cqNz%2FLdbg6HNwhia9gLvFy7BhCvigV1gIK8w7s33yQY6pgFfWYK0bd25poOQa1%2BaWoJaIKzaLhDH%2FnUvBHElGwivoMgGfdZaaWQn4RZLnWL%2Ba3oA3ti4wAdibb6Xqg6g5O0j1gXN3Z5TK6U8PYYO576H1goTj2Ua%2Fisk0cIk5Td8pRRENcQSzZqzmqr%2FXU7WQ7AM0SE21effRGPlmpvrk5fFAjn846BpVaj32qfeaFFKwYHjFG8LqF9AbiJ0L35moXYsJHRbNrTs&X-Amz-Signature=06c8b0b8f3ff4de9b9ce484d7ca9c42522e16b728b43dbb794cfea37485e39a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df[(df['A'] > 20) & (df['B'] < 71)]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7b8369da-79c1-461b-8ce3-3814a7151ba5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YOBZUD%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGmcN1CQapNiw3EHLUZ0R3KTBFJWFi1LMx9ZNxYKHnXLAiEAnHkHH9SC9et0ZgmZN%2FDzHSZaacGytfus1eonWacJEZAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDFpRpmjFu5XjVvxwxircA155PybcAWCiWV0xoIXqWPSkM8k27sV9IAilddsGtj8Nhe6OXUYGR07XpxR0O8BNxoba6xme7e%2F4%2B2Z0MeXq6vUEN0wIbtgBlVfcoypyQdIOJte2b4J9okOLynWOxZb2r3RU9nrijewE9VMzYFgoNIN6k8%2BrOWwojhMpA49fHD9Q8gnGPp3W1pmrb4XRi%2B4IQBTecjjs%2BUmdb1tB28hClG7rKQMfJk13H5U01fEPhWAvqrxp91VSHNqYQr6XKuPDSQFOpCcbL%2B604uP6nhgpomRaNz72ZBeSPBTGRcrK8m9%2F1p2arSXXpZTmujl%2FsSHERrCNJEsI4YFE9pWjr6Srg2VDBy%2BrxjNrNac2BiLVY%2BHxdbb8a3eBvbGGmqJT2YhTDl%2FzoJuWprYZbYcYQIsGp%2BH%2B5bozSj3dsAndPOvyDKCFtJcKXSNdwPiAv6p74pMaC%2BGXcLFzuDlcX07GdpBf74N3NkNleWfsM%2Fx%2FW%2F8KcisHCTRbq8Fn9WeBo%2BOrmYb8BhqJF18EV%2BKmM58Fyt1s4PwHQXoRAXV%2F8Fny5vHpRTQd%2Blc2rQiu7XU3TJ3obT0i8c5ByDXAj4g4PMc%2B48cjT6idSY%2FOQdhR1eQaiIFrkqas0GOjnOy8ESDORVh0MO7N98kGOqUBY6qpzRJFx%2Fn2SOXjZ92DRmvgNjUv3Ih80zq7AX5iULDYldmH7vlRmfz15ka%2BPsa1xK7qwORx8cXzPij2NMWIlFNn9iBVACGYcCafSust9g%2FBvt0l3gKI415%2BlCCC0ESJqUS3oCWSOwwNTC8MOmTEpn9MI436qgScsHTjHTozaYme0Gq9VOgh3HqfPzBgrvLmJPKCLwzrWes4T%2BTu5qDvYDaCJjl4&X-Amz-Signature=23f5be82d66aa4f492e9d8f076497d05bdbdbbded739a5b5f01c02c3e21e5c46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4277a967-82e0-488d-b603-3986cfcf9b9b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=269cb59e46c78d9498097000917d541a0e098845af80ece96f6321889f6a46db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df.sort_values('H')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f755b7d-739f-4a7c-9463-34ccb3a7d251/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBC5UPMS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDHxfCnixdPazcE8CU%2Bsj5CvdQmoVBzgZ9pUOEMumk5eAIhAJHlAN1oFjiTKoutdc1ykCGRavKjM%2FI1RaLt29rM9Fj4Kv8DCCcQABoMNjM3NDIzMTgzODA1Igzoe7P9oWszDaJG6Koq3APwExgUyp6SGxFe4ZxQA77lyO8M4LqkQZ1mgPLfJ1BOOyiUJeGYBZLfRCi7%2B5%2Fy3DuXC1ISzDlalb%2F1lnTINC1oDfYyV%2FHAu9EBzVYXzvOyCoYYM5jXOhfsVV5s%2BZCdhNl5hUTwTvSF1Qs7eyQp1axlMqJIuqOQEQSY6tMKiDFuW0KvGwrI23fyPlM7bVE%2B0QnGQG18berwkyqjQxIGNmFik4JXSO%2FjPazA1PYAdj8RphyE1Y3ztsNFboW75cgjkPp%2FTyYMx7dkY2LZuWYin%2Bw8QlFyFQYH8DosLVf0rnYap%2Bd8SiUSuMuVWABUPzXkigS8MBqZko2djjXL7uLLhGBKGs4H%2FlY4%2Bf0AxHfnV3TZ9YREMoqjJUjOsG3qEmAgvk0dFkvn7nfMZEUudLZykscnvkIKcKa1zkx9TXB0P6ddkUYBH81CJaL7rHGZwmZ%2BwcDF9VEdJaBuWb4YibW186Jwilk4PphiRHpQu3ihq%2Fzzj6vA9elCyExJnSd5WzsU77V9QRm8e8o1q1h%2F3dedLf4Dr%2F8FkVJdveztji9sTH5dhBV9uXdBJLcEyBqrd1LuBOd9VJWNX%2FxyMJR9%2BuJoB%2FTP5%2FhEeggJVTjZFu1FvSMwLRC5GyOZ5E4KotAy8zCizvfJBjqkAfJEGT8OB%2FSPSf%2BOtxuvEeGjUNg0Wq9MeZMZTwacgYGSwSD2r72tb8lT08lJOAeZjST9yWhkZhtQHVupSVLei9dPEdvqz5g9oAC2xh8MoUVXsuUuN5xJNoomBYIxr%2Fs2oGd0QVKTPq%2F%2BIEd4o7nbBNU92nDxxFvXAyu8da7RFhH9oUIUhZx8a3273%2Fd0M9uNMC6ZgIHgqS5Db2XitxTCLwNj5QC%2B&X-Amz-Signature=e2144d15c39434c739cf386870ec757f74adbd41f39991a35b74dfe8347b37f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df.sort_values('H', ascending=False)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/86143afc-dd47-49cb-8cd5-1e40b4d4183c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFMUDF2H%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAfEMFhM04NhNSgZt0sUpHwdP3MR%2FRuRhlHQcrMhpGUAAiAq7jw3%2FA7Yv0f0smpHsv2Wae1Zb9UW3XDSfGbXuMGlFCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMuOWVenygYQWTSpCkKtwDgrCGKwOY7YL7g%2F750BRO6xApBmOKi4Zjly7RmC%2BmafDbPYQq8mFJnDkDH6Q%2BNajr8Oa22Kg2IH64SGckpxzIruHDrOPTa4pFIp8QUQkYT6G3vrDKtd%2FpRE9PfJenGIwS6yadjowmk7lvzihyAqEeAAxJZknKi6l30eNi6S5Wpl%2BHHtZEdvGOnBQyLAamSH4qMj7afwAOQFglzL%2FRiYfD6Jz539FJRX1sdSsGppMCLe4YL3%2FcLiIh7ZuRPsLONzeaXQnoAw7oCc6MUdgIxrZ135%2BKO0jcqL%2FzQAsfWT9%2FIIpv%2B40xxvxovld50UB11ViNCx6vcKgzCsx0%2FLs3waT%2FrkBXq%2BxgcG2TgfeUFe%2Bja0tKTxhwqALrULTnQbePc5LykdkAMxnkOc2NY1scjsO4xq3GFhPdKOD%2F29EY49XB4x29lcdeFxB4qo4fidHFNkQic%2BwNDXAYl1Mkin6h%2BrtMxamG%2FVbQJCEqD5k8ROHoSovqIKkSnMbOfZtsKJrxZK50gmauI5OhthGAXTnKfrX90L3SRmhZHf20%2BYZdDBWEdY8lRaQ27z279hs6uSqOxgIFgInEALdwLik0Ln9ENegGc3COYI%2BRgzruLubyalX0chB7vMr3qBoXNgbTk0swjc73yQY6pgG4H1TF9xXATvseRZBvBawaKE4mdAH4Nem0hzDBFnAwSjKvw%2Bwwi89egiFNUfUr3ooiJMZMJAeTkWF%2FgBLYngvozCTJdU4zp0rB46V1kbLoaZL2DBx3Tu67k1BkHE%2F2I6I%2BqQ3w8UWNw%2BYPKtiz35IuhLa6yIAOv0mPrpV6f82ok9hVrtIqXNdBO6blgcEDrcixO7l9L70jDYUMfo9ZvMgwtSUy8bl9&X-Amz-Signature=076c185b8eb599a5e49588c217d05340028aeb5ad40e7419baf598d1ef04d7dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.count()`**](/1867045b058343e1a66b677961515907#8d4d0ed1fc114482978e4da5f21b429f)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/de99cf2a-01de-4394-b9b8-778a479f0f75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=c9d3f68a4dfca2c216ae982dd77e0b42011fb07fcebef1adf087415cb39c5e40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2e0c7fec-4523-4dcd-9352-242c0eac4417/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=ef127464236e52972ccf078f0b94e1460ef835fb08f0e96224dbee650b168360&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e11b194d-b83f-46be-9096-b1cfe4b86b49/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=f660c329f9c5a10b01c88b9573f2fd34e4ca2809f0d03aa298b9bee24efdce4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
type(players_df[['Team']])
```
<details>
<summary>Solution</summary>

`pandas.core.frame.DataFrame`
</details>
---
[**`.unique()`**](/1867045b058343e1a66b677961515907#74cb3dd5af264206a7e4ccc9b07d9a7a)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c914f3b0-79e4-4110-8acd-eb157e678223/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=731a91d9a65d0d1a8056becdf870c24484728409095f404f3ba4be2d22a2555a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f644f684-aabe-4980-a9f8-1245e19ad969/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=5637d3ec61e948bf956e0ccf7849de94bdbaf40132056f6677bb8027a4a61c3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df[players_df['Team'] == 'Arsenal']['Team'].nunique()
```
<details>
<summary>Solution</summary>

1
</details>
---
[**`.idxmax()`**](/1867045b058343e1a66b677961515907#ba3eaff47c7b4959a30a15a24dcb4584)** & **[**`.idxmin()`**](/1867045b058343e1a66b677961515907#345599162e1b4b188fd36eaeb3627352)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/96785e84-d4de-4def-a74b-e9ace013302b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=fc07c668ea456893e48b12b6001e9a5c36d6fab92431346bfedbdd22355bc5bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/aa9c033d-d4bb-4f1f-abf2-3075bc0a809c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=349b918b52a82162741d8ecc34eb2ec6c5efc1eec5a41fb1232105eee6994bb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df.tail(8)['Player'].to_frame()
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a391e12a-fd80-4f67-8ebb-03018c94dbd0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXMI426M%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCEDNrBANg7Vc9jOSVwButP93ZAKA%2BSpYZhwXh0yOMXKAIgWv8iT1xbcVachFsJ%2BJ01beTdMpaUaVglBJGkEz6V2kEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDSaIBFRe8yq9OyBvircA9cRxuPuPm7aejmElSlcJFchzYSX%2FbnLGgTQC8Q61Oy7bfzWTCYabrT%2BxIMql1VYF0SeGhq8SGwCoOBb4kFsX9AE2h4MPs0ECUAg70VTlzlkRzdBbIws0%2BENxMcAFRTaX0nH25Ke6Cx57LnvIdq4%2BNOVAl4KQPRvd8lr10Kprnr6z6xGYNxNIB02x9nDfd1ak1YcZ1vfxWIu%2FBdJSMcV5g5QgSJxvMApDMRfqqX9iPjpYBWVlTYZ%2FVgbtpA4R15wsk3bRV50132ySSLeS3DcIksDa%2FHvzjTzwIos9fXu%2FtsDHfWRXcJ1smRqS7CWgIRmaCoHUQv9HBdhXVy3Y1LauMdwD8DMXSUw%2BCrDNtcnR7GCdh4UOEd4ihMY4j0jHSEqMvz4g6i7PAPFoDCq06sEYGqcs5KC8JCxyHWVqLKOlbqGOTM3m17fOrgKUgCAcGVBYOuuX8DrrwDy%2FRQ0%2FAHWVYyeTVcwssc%2BrujAxo3nTAKArKszufszvh1%2BEtOEE4Z3kBHlDSbjCRrZi2iTfleWjDwYx3gg0yFIvIOiXvXSB%2BEYfREAbGRcD7hRLyV1nmFf0pWtTu14aLenGVLj70UUf4yQLAWbl6Oz8ftQICwhfk%2F8eWhy5J3OHd%2FW%2BZKmMPjN98kGOqUBXOZeljBG4pwpBUreif3ly6FlKCLIodWWYIf0NyPjfoeIg45K5GQlcsqZpU9oOf1vYvsPgar9OY557RNsknAv%2BB1%2F0ApOxbW0KkSfE28wrFKPO7kzPcc8rEe1FYfPCgA15Ck49DC08oGFOHmSbB3S1mk%2BPs8IH%2Blq%2BmU6ixhqfdX0eydG4ovw%2BAPSz6mJr9VpEgaMzgYbLkL2wOaCuMuECUO28ilm&X-Amz-Signature=9a544b1b54685806b811a786c1ed904f87f34cd1924ba6e65fcf0f5f5336b53e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.groupby()`**](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15)** **&** **[**`.get_group()`**](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b9981f61-90ab-4be5-971d-7e1c69d16d5e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=fee14618449f4abc5213b2123287fb7bf1e62bf8e935085cdd4e133bdd48ebf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df_grouped = players_df.groupby('Team')

df_grouped.get_group('Machenster City')[['Player', 'Goals']]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/03c98ae9-19a5-4d41-81ce-9ca5a314adf6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IXN5AB4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCKJCgE%2BIkqHMrtE1I%2Bg9FbDL8I%2BVQw3K4e2U39EKGzHwIhANrt8UzFCdvmJmivxUhikL2n5jC0RZI%2BN1yGoxMvyy73Kv8DCCcQABoMNjM3NDIzMTgzODA1IgzmDTGwFQIJzTQ0BKgq3ANBr6T0Ib3guqHv7Q1%2BIAE4B7XwT3kUGze8Rlal%2FQEzdkIjEgduNOLe4WPWvMT6uPVlOcuChu9riUm%2FAOH2stqruEq8%2FKbYOgTSuY1KdyASO35vXpDsHAs81Q3yfFpx6is9s9RvmOAiI8IFjTKATe%2FuAo%2F0mWzGlFRCtKXi%2FIRdXQ0PRC%2FB4xuqssc1qu8rv3e1fA6Qf1EdA5nS43z1duKHs%2BFqrNNon6%2BHLGnRqnpuYyxDZL%2B70JeVPJb19PvJoHDMncSP6ba4KeSP6YCGnjYkC%2BxvMFZzHXAeDPWO49HLKClHjAQxPFiMnVudfDasQCIT54XrQbQKzpGPUXv%2FOnqJIodvpSMidETAS7KC7QLiMBsPHDb8qE0N9m%2B3ccyQy71Pi4wUlCsDWgql8IBYkiCGnYYGHKCO6MYcQ3gXBR5RYdkhCJNtnqvxmuzL0mEhZDskcTJZwF9oc5k3qCeKjRE5LbWyImX4ZJ4Z5lhSlKzJO1DmxJi8dT2LDxck3nzTY0WhJt7K3R7prYM72YDksTa95t1h8v3ntAlzNkUe4a%2FCnHjFn6oc9kiU%2FIhaorTqRrtpUkr9FzU3woxRlOuLEY%2BbxWAOxClc1pqmIcEfkjaqZtVUo%2FlW1p177e2rczC0zvfJBjqkAbGCYdp%2FgkIcm2bOlfwuYhEYOc%2Bmvz5mHlDpwcGbrTJSvdIpv84hJLsvWnOWgZUBU2C%2FneVC2Q8kMgkphOTg0ReiowfJKldn5jbF7i5nleIKCW1RW2AylFsyauM1P3jiTDq2kZY5KPDEeXjbYuUmRMhp6d2cy094FwDhj%2FX8jksRo0xaAicJV7NEmxD%2BAemNTKhXHKWZA0uOM9KJdK5SZjrN%2BnYs&X-Amz-Signature=5e2534cf2b19a86623f5d022833ce611b43ac634d0c77c74e48b4d52c4b7cc90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.iat[]`**](/1867045b058343e1a66b677961515907#54779c5ca3f3440087c94c34ca5b5328)** **&** **[**`.at[]`**](/1867045b058343e1a66b677961515907#c21adec24a86474fbc660584f480a8f9)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c6def28f-c507-4696-8f3d-b3d2cb8fd425/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=5674a8deb9f185a8fcee39aa734d05253b38718a5cc2744116c9ca1c634d370a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df.iat[3, 5] = np.NaN
players_df.at[2, 'Team'] = np.NaN

palyers_df
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0cd01bb4-2251-4287-b96f-5f3a7768e5fe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3KRXSO7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD0Q1tJXQpGjS7ulotvHULKo8EPiezfDxF9JEh7qJwq3QIhALcauY7Btr%2BYLumeSLEk2G2jYvrhxAnRPVBR%2FDoo0q%2FOKv8DCCgQABoMNjM3NDIzMTgzODA1IgxRffy9vH%2BYiabQykQq3AN%2FgoYmxZfv8n6RzH0JYLRefd%2FggWFadiExzM4n9J50lBCByIBT5nQTJ6hGmjEpbTxRVD5mDJUDgYrF05%2BDEn%2BJL056AZ3nt%2BxWe4on5I7V%2BB%2BGn3LnCeN%2FBbcPwvMvepFMS3vrrguhO6nf4%2Boec%2BjfOVToYoVNd49ote7HOmBZcOiUPoHejyXeLQ1xH3X6RuuoOEGQQC32w3WSmhu%2FScoAF4WCyzwzzqcoagfD38DFGXC4PkoYQlk%2FT9nKmA0QtMCBkopQoW8qTGEy8LG0XPetrS%2Fyz2elwxYp8uIkTCYghSdwAEBGcwA%2Bpnu5lzSm%2FsjbBB4WsTu5LD%2F490Uqvo1O8Sapw6vJ1APN0W6Y8X5%2B3JQGh74B5mee8XOTl1%2BGqUiaJv1FUaTKShyHaLx8qZTTSZ983t9d7PH0QLEvB1JU6PUYmIs3rGKdayuohB%2BfUBLCp8VdFbj2Fg3Df9IInLxW1qdgL4gX%2FKgvcyRyZWuJdvCpls5HASxpnzztIMm5ePMM9VLFWAlDdjxqxIMTw8GZhyYC0%2Fxndc88ocENHMvqCUX08A%2Btz%2BUM8OiYEKm6b3N9s92FjATBGnVV50AFFkw9PkWqS3YxO13Ie%2BKeQvWwn8Hx%2BIYBoRSY2WkBjDDAz%2FfJBjqkAbZ2v66bS03C6UcFcHVpqqQtxXdiO%2B0oxBFgiMxFvq6HbDhYcAHDFPSP8noeiaHOMFFca%2BuAg0H3yJ5pk%2Bjt4y6vdOMfoIRJHTaxzCQyGPmfZCPzmXnBr4olpDiq40ZoWoD28GLG%2B3uMt1bVCaviHTS8vNe51rtQMgMivOzQvuesPRRt%2F1%2BvPilcVJjwCdzrbBiwqAJJFubWA%2FdhGSMiARt30%2BQ0&X-Amz-Signature=38fa3baf49cd6e55bbd238b6bb259df8cd0b0b099fc4eff197e9e7f635ee04ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.apply()`**](/1867045b058343e1a66b677961515907#9e6d1643dc24411181facc1dd3265ffd)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fc4e68b2-6e69-48fc-8b2b-7a2dd9bb5ad8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=5fb5b4f1e7dee2176787485f4ec2e9a5e54121888b7a915d424440cac2e5cb3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df['Goals'] = players_df['Assists'].apply(lambda x: x ** 2)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b64c0a7a-487b-4898-82f8-ac5ec8adac14/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O2QTIVA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIFwElG1OzQ%2BZzHGmXc63lkZKAOQPdGfz%2B27ji4DMl86tAiEAw5yzwtH7ziMb2XkXmdC45XWyvi0dhDithOjwerUCmlQq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNpqnYDBR03auN5HESrcA0xbk3fZJo5tD1lSsjKIw0ekJrXfOGHo6axvDSLiBfzLDRG8GX8qyyYHE8F6uUSZv0p8Hf4%2BHgav%2F%2FcCpIE3rabqdDaAlACAc%2BGnAKzcCOlStah5BuT%2FONcNWAeoeMi6PvzTvMuRXYwTKYFfULxS53JI53DL0UaPgYC5e%2BmPuNoheCpWYa6GbEmlESNMtIT98m1xSjEd38jdhTXtdEGBFf8EWd96qvwILRYkZC1qrpFWAG8j8B5hPbhH0mpZdHtT85lgumnR3nCZhGKA%2BRjiDtDSReBfwDR1uA1jGlRKBPO7h1pD1kuCmrD7El86ESBE4PJpMygXlsDYtDgasJbrWWaipAS4ByX%2Bf78stFjR3uXzCh7acVaq1AG8nZO8oYmuOUCMh7Gs5YsOuS0vFUf%2FH2tITkb0L071qoNPpfwloRe8jursxgf2zcDCz%2BYEzYwW16pZBandhAQLnzYk0BYvuBckfP50iuIkmJzijlqjFHbVv2GEb9RX%2Bw%2FK1rng4Aot1vbVyB%2Brmyz9bv0ouTSZ9fyL2dEBejKAUucSNDPawmDAMJS1zUks%2Fcn%2FZXSlchFVk9NqKkc99EUOd3qsj7D2bCre8fdeehCBkxmpZz87QbskNRIOafIfNh1ZECVUMKvO98kGOqUBh7g5APOUCho2vzBDfDnmXWTwAPRQ73fddsUBvuqjxXTf31%2BKQgt9DW28uFdWbImeK311B9%2B8pJfCCS3Ac7FR2mz7ogVofti7sdGfIDmDYcyGbuIqTpRTf6lNSQHZ1zi2nMbuz6GERlNWqnwgHL90QFsLrpDKbCPrCflUXgVizxBBbUvCThhzr8Hqv89pYD7DtTiX206zlfDxsWAcA4pdmgBueR9U&X-Amz-Signature=b3d2605420a639be4c09acfaa68df52aa56eed46d6d1878e58cdfb1c76a16716&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/15255d09-bd19-4260-b8fb-c9b0046af1d1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=bee11974ec666c5247ca27e0140cf58336d98987c5fe8261ab6b79c4aa82a44d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ca2c8f13-c055-4e00-9df9-3ec299dd87ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=51736ff8e7db27596d456b7132174aa3ba6a6a07ea3c38d4ece9b287b3dc2ac5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df['Value'].mean()
```
<details>
<summary>Solution</summary>

16.11111111111
</details>
---
[**`.get_dummies()`**](/1867045b058343e1a66b677961515907#76a2d8cfe9e242e4a106c2954f3f8cf7)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/61c79be2-5796-42fb-8606-cbf8744fcb7d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=3b7002b79bb922e81f7f23f14b1487e44ceed527563d53f66bf047a598e99ed7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
pd.get_dummies(players_df['Team'])
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e9c3802e-1d27-4cfd-9272-4e99b68b1e6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6Q6BGTY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCDMtl31xwn8fpQoVJ4JGgT7UODOntmk2H4MaUl7C%2B00wIgK8RWnmB8YtN8xlwPsAVDdF7RibfG5qO8nhXY0xlVrzsq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDMto1dVHG%2Bfix9pPByrcAwsUPCH7AoOKj%2FhCcQCBgerSAceEwVpy%2FfIB1Q7xvSvMsEkfQaor%2BXCNwsWHTD4LV6rPzTBPc7lIWlwMnZ9xMHdLX6vqa97MENT4LkgPtk7Rp6tyi4ebvHNsfd%2B4psY7CdkPAa6u54On0aw5SaPv784RKCpGs4bo81k9JCLr2czvuEUEUuHZMhkcd916VNfcd%2BfuOfDzJ3wBgYjuiq2kCJrMEVVEgwSKxnaAnSMSPnK2MEVyamfpWZyVvAN3LVmGq32VNAeqg4XXmRaKbzTC2sfqXs2MZvBvI4Bd4O0td5g%2FxUNH76JJ%2FnsRzEd8SV4nAyp7MMEVUv08tNO64THYnOSk2P1ldjga9uRYjkuboO1gqfysEm5Hh788zmBesS%2FMwXmRE1%2BtPgz2XltSM8km8XFtZuzBfXnt3Ki9z4wXFYQlzGIToJnVHpfcyApIhxVhDN%2Bqb8miR1%2Bbm5Oz8sKR61KgWrgCJvCMoGrL%2FdXgJzu8QwTlboPCD7QbL6cXPuc3tjE1RWh5AOYuhPP%2F763PJpNJS3EOW7I%2Fo7IruLI4%2BZmj5bAcy9NghSrr5ndFV%2FvbAhA0wf9aU5r9TA1zj3xfWu7kcDNHouIdoA3Goy0tw270uPXUggQvPpsyJpKQMNDO98kGOqUBhhk8O3GOPYcRMzikU53kUejHv3eRMsTAZyqulbDpIG9shLdrEv6KEAIFq3uHe93uRXE92Tsg91J92o6n%2Fn%2FgEjHOk0JOjqfGOs9ZE6ehUSkfQ2l2VR%2BjgcryYNxUkrD3VPBUFsEKUPMJoYp4USZRTPyjapBkyS%2FGkmdzBemr7TA43aLgMvfgz9XRXpiZNW2JgqCw7a61J%2BKp69gL%2FZ%2BVBvkK5tq5&X-Amz-Signature=8d27321347d1fb42c63bba083b453544e353147187ec18f08681f98860660a7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
`.mode()`
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ca2c8f13-c055-4e00-9df9-3ec299dd87ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=2cedd824d3aeac3ddc20cfc008f110e4552095b676632cf7e0471ff14fda7b7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df['Value'].mode()
```
<details>
<summary>Solution</summary>

5

</details>
---
`.median()`
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ca2c8f13-c055-4e00-9df9-3ec299dd87ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=2cedd824d3aeac3ddc20cfc008f110e4552095b676632cf7e0471ff14fda7b7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df['Value'].median()
```
<details>
<summary>Solution</summary>

10
</details>
---
[**`.drop()`**](/1867045b058343e1a66b677961515907#e2a0a082029042d0a6f9e7892fa68a92)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ecfe5584-1ef8-41dc-b214-722261d1e43c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=fe658d47b0ddd2c8e87eb4c9aae164cd489f252e4fa6695dd83f4255ab50a73e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df.drop('F', axis=1, inplace=True)

df
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/51237813-dd6f-4c19-aa36-b1ddc9b8c1cb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XCXPD6P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGFSjGV7ON6Y8sqy5Or8SbuPZVWL1%2FRI2VQcJgnxLn45AiAU3t4Qr2%2FCJ4MNi5li1zkTC8LCkUUfTEk14K89tXuo%2FSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMP%2FrNqWWm7tdnglvbKtwDYiwe7pD%2BzLxE4wsAPUmys%2BnA2GtgOOVXoTt2VlLiHBSL903D6QcAAtQ%2FTLrUkduzSI4d2wH%2BCNW7EQktJzPF7Jqhr4cWhgyqWaM8qgMy4R%2BJpb28VbFn8APL4NxhW1kkLiQHLXnGoAn%2BXpvfTofOsZSvrSXFSt9DQcoHmBqBmvsjtRca4a2VPZWqrxREUTWQd1Wg6Ucm%2FPGnofH48bbmG9HHTi3OG%2BDTegtfd%2BmmcfQ5bBKRVY7Q1rFHtAU%2BcGjfee%2F26INMlN3iP3KnmrhpBl8z0Ru4YbN1X3acov4B5ZJUo7Ltx1ezGmi3o7PC1aLxuodY2uYkJlPtYMiiK0VJTeeaXmnnu9eA08%2FohflnuzPwN1XgH8RuwFUIDP54IJQUgqO370cdDaG52h2oHMR%2Bv2EcQrGf%2FctC760bJWvFMfnR3rt1S1DSbDE1xtESqflgECEr3cq%2FM74AT91xKK%2BH0dvN64DVi0bt4uinibkyUhUQrExDT3NGmcQsAjwWTitlEQTnoU0WxY9dhdfRKYm0F1CYdqd6lnycI1A9rn4VkdTZ8EGl1h9BoFv5wIhtqfPf5RYTXo6R16MOehnuS9EBo982nh%2BVvS%2FftY0lNlDrae8%2BFt7VarfOQhrHCaAw5873yQY6pgFVYDxcpo0YRAN%2BOvqD4sOlztoiWDfg9IuKyqGoqwyntlFdAiIZXiXTugVYGOehV%2FXuQqIU0pB7kFxMQ%2BEwkHYpwG3d13hwQDnyfIhGInSl9k1bpP6AuNvixEgCxHoDLu2v0idYOGmSP1oSBNZLjuuu5UlLbyObj09TPftp6Gwy6%2BTiqcZ5r%2BfR4t9fckBOM6uZEagMalyHscFS%2BGqU8FTC7wTHfPdj&X-Amz-Signature=1a4735cb5ffa6e7242f61b7b4f24cd8212fb3d114f24102aba554a945036bc66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df.drop(df.columns[5], axis=1, inplace=True)

df
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8004f3ba-d7c6-4c31-8bd9-ea17dd3e23a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U3ZGKPB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCP6STBM2Z2CkUJREy2FPph1%2BOa9RI6quNwgyAsU3QpUAIhAKvF1cXTQ68ViiKgydhxkwrs7MAQee87x5hcj4p3yvIbKv8DCCcQABoMNjM3NDIzMTgzODA1Igx0zTplLselBx8RNzwq3AP7SnU0d9FZrvzmvi6lnNjnKf859GaSbPYzrnEmUofOY9NR89Z6byHJ5EYKzpt6WP%2FVageHhypto%2BPl63Q12KA2CTERJJbf68GdoU6EWrx%2BrdweQSsdjfvFoWWil1u7ZRUm6WlKcH61QbHFVCj8k%2FAG46Ard7B5ocM8CBp%2BX47kBGtbpi%2Br5ALCbXpdCBTZiJCLslBKF%2FzzJFMVw1%2BQEHiI2tHN%2FTxaTByIp05B%2FNEy7XVnRpTsBWMPyd%2BmRWKHNKgEjCLTR4ACJ2xcSLBkWPXxx5RHSd%2BMEErzCnTY8NrN26N9reJBxkm89dThECokufmZyuPIVm3PAeKIPyYNRElgI8atGNvfK9GriMkmBO88rynfdKaIvT5GBCk2s%2FYW1QP2lWGf9NwnuwpkvKBYCZBt14qZxMAyrPUQAQ%2FFCNUu7NLZHpAJ4kZo0oX1M4SDNf7iaAGPoj45O%2BprzqV5Q2okU13MQuxhmJYMkguAPKExv8xmvjksakd1F0aypTfl%2FRbnRKKH%2BYZuNxh%2Fs4Np980m%2FKdAiLU3EolVSQa9Pj7hAQTNoBTcCoAU%2BUrCmq%2B3iM7i%2FOi33XSgR7bVSZXF2Qf9WQG03U0giYUVM%2Fv1s4pivwDZrOp3bUx8n1NInjCCzvfJBjqkAVpKjdDvKYyzBQMoc8TOg9cOx3uqa4IT61vUOokekgJww9CslJ9fJ5%2FPuZuIT7j4Xx1HMfbZKA6%2FKky6Auga2YRs%2BnQ%2BQ68dFj%2BR7d1T4hfwVn%2FMWxSJFnPc6J8%2FP%2BwSXiRU5bHFkKtI6aKHiXzq0WtoTKbgzMLubp%2FaXyAIoqeW6cZ2FPwTEZFxvDot9hCAxQUVNHja8NvI2yDoAQROD8rQoont&X-Amz-Signature=b4918e06d1e3a1a9fa0cbc5326fd76229f4fb3aed0697a52376f9d5ed817b338&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
df.drop(6, axis=0)

df
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/03ed3693-8267-4c3d-a7f4-63f2a23f50c4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654455DHD%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIHA43ncLYdo%2BM%2FYcw7r6EpVXvFEEmYdEoIhjwp9UaS7oAiEAyKrB%2FSAWJE4PmqmLV33ckhPZ4GaOZVsJmPPDG0WGluUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDN5I6BFIKQAo%2BWArWircA2r3bKarB8oOTWaG3zqEEe%2BPLTDvtAmwY0dZF0%2FNYlb7oL59SEyhLmMi2b3q2KpnfWQEJXRA3c7g%2FqLrwE2gtX%2FExHqPac86DmxQWLYFrXFkBefFFJsdcg47iiy6VAjbgILB%2FGw9djdrhmFSylzktGDvqHA4gGMvj4ou2CU4OcHiyrfRHiK0ZrLYML%2BnexsozLwlZfG4L0AD9d5vGiSGSIQD5EIErvypeIUWHJPz9n6YpPUskRZlfycAM9pha4vbucqHz3ksiGGU6q1LrqhJzNnYXPCUsoy3scNUT5biEKT5UXTTK5YKWPMx6vf%2BOVBAsJjkMwwvKiQuhtgz6aJBSPaly%2FvXSkeZJOMS9nLfbyKEXELN9pEYi20VmWpXOCsz7VGhPx3i1Vt646iUO76dn5J6lD3P1hlMAclzr2ngjpdPl%2B%2FcnaBlwSYMvP3v%2BFHT3iNB0iXNG7H9pGilUVJT8e4x03R%2BgRzjGFi2jWrYaEjZXyVSpYOyKvrYc0zkGcuZTOs6uvQrXWWEsZ78tYGp2psxh%2FOtMbLMWShb3T7p8M4GG1wVCALsE%2F%2F35iXM179pr4Flc01u0skTGMz5DgAy%2FIV%2BZznB0t%2BotOTiDH%2FogReH08EzXjSFyzhUQDJxMMLO98kGOqUB7Y3IJCekC1VA7x5ZE2iwtiqhL0IXb80NuzMkd8QkS%2F1qAfSVQNIhVEwN5rlvR2N%2F%2FrCykXfIMMABkjSzKciLZIWxfFmlShbF3wzin%2BWjOYFD%2BPcg2jFrNj8ge%2BXP4PKLXA4Ut1SYKvgkEU0ikgxJdejeP%2BWKEYr3UhirELnEyT%2Fxd%2FvbcPlsElw0HOET34r0trr30m2J9RdAoezXRoaaPwCB03mL&X-Amz-Signature=37fe6204ba2b41fe804854269e238a36f62b02bf2db9a7d51d6c5e63794c5653&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[`.dropna()`](/1867045b058343e1a66b677961515907#3cd5de4bcda14709a032d08303eaa85a)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f722e558-7e32-4369-9d54-1a196ec02f31/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=2f619c82b486ddd39a93f39414154788d6a4c579783d00ed4d9029c5188b1a3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
new_df.dropna(axis=0, how='all')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/84d981ca-a81f-4f92-b15d-902263a87a8d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PS76JIC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCs5jX8q48cOLA3FZMK40GAPFecMxkvikbucvSft%2FZ0XgIgPxUlY2NKhP%2FTJkwpZaH%2BhiD1YkbQSOQVvyYTC1jyc5Eq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBxmFDTuxh4z8USGPircA45vB5ekFNOdiBUVj6ErT0WTy%2FuoMrsvlPSXiH8Q4rtPJzveL%2FH418aHOAJwPw4AYlCYrHZ5Yt0DcySlhiuOj9k5biogwz%2BgA4mptybfYSggTJiGesQjVNmxe9pqsW6BjGeSOlslssIzWMArJgm70VQZxqRrB4vqlZXYUDm5HCAO91g1HUCeGmfxIg73T47SgyfGbOVtOhVNlbFs5uK0DX%2FIASIatFVajNlRxLUxQK%2Fb%2F%2B%2BWbS5NZIXkJ9WmMzadyvZaMpZgCI7wcg%2FWzQTr2AVS8n4nGKGub36NMtGKhzF%2BfpRTu9ANugPLclv6x2YMlJvaNJyG%2B5I5U%2Fmw87qhVI93ZEX8kokdPIJN1EGf8OmHisuJI%2B1DxJJ9SzbuAfMFLrXymLjoaUA%2FVscvhmm5glZSEsrSmxYlzqNvQ268UOF1Q0J5fdTs%2Bc3%2FVBCrNIsjIiJ4l%2FKZVG4dEFo7LE31wnnjlcNEORtvMKgkoexON9%2BoVEUXDUJwzSOakT7ANEjVco8pIXFl7dM30%2BfLLqJJUaGCEfz8pNdyBt3yDT6%2BNq4UuoknmXAOauKYZj%2Fc0%2FUY4ns0ekBtzTt%2FDwhujSraqpm8QO6HUU1VWiL0B0qVzT4MHRMM1RKRlbqKLRTHMKHO98kGOqUBrxDf0v4wvUbeS%2BZWeUX9vXp7%2BoJNxmd4TiQmhHm7BApnxNmYxzqPb7HWhmLYziTlqkVpFYeK2Nga7bwolx%2BQc6CPpbZTlyr3ljHvURbCqc%2FUg%2B3JoT3cjFGJHCyw6hfn42zRZxGC5B6UdWhEUnp5SOBOlqucL8et02p0zfVmtHebWQEmAgkSjK6c4fixB%2FuADijIRPz8e3nXkEzssp%2Ffvcuxin5u&X-Amz-Signature=b94a190f3d05c177b5333dd2d4b4d709409d790b9e0c88eed2c2ebb94b52fe3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
new_df.dropna(axis=1, how='all')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4ee04007-1d28-4468-8b11-0a2f47859c4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VU7T2SSV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD%2FwgqETH5sWiwPhnr7tz88KaAU9C17sEG31AzMGK%2BS9AIhAP8gPSyAwEvMqfcCZL%2BD98Qgq1A7hHMuTMzapJYoT3ftKv8DCCcQABoMNjM3NDIzMTgzODA1IgxRRC32xgVG5R6Fy4Eq3AP1l3laMEh3rgDXqYoMReVQfIdEQ%2BaTZJ%2FBKow6GFPvyGE2Q%2BM9BqwPORb1EYqoSpCavuaMkSYWdV00ZTITP7Dz83nDxKnLQpcCOJmrF1vRvllCMAEkMOM474hQvvvOGx9Be9pyUKsCRibFBZAvd%2BwQ542Z72mf7py%2BMKeX1CZP6lYnSyyA2BibvFL3vCGIOhOa23EIBz%2BydMs8FA3A%2FM%2F5ef2KgZ0aYveE1mNdIFjX1fJmt9OyCPeZG3%2BXqReJ%2Bjdo8Je28jAVxXv%2FGP1%2BrxMD86MsCquy27ZiBi%2B5EDI7d9epcuLApLlV2wfUdcvWilsqucNYQDacm5HXIhYTTy81rcUG%2F5FWeHugbfU%2BsvybRbihnxK6nBckeac%2BQbqGz0%2FUPeKwpIrJjtnD9F5NTGQhCmQe%2FUFBL81ifLH0Hk5ua%2BduoK1shNcW3Kuc9Td%2BpnoFFtn%2BBLoLS4M3WnRi3xNr7MLNvo7UoSlcY%2Fj7ik79gHTYKLCN3e%2FY%2FAVckEMm2%2FTCrrbxrrGNL3M1SYWSuH26jfZTm4eQUqlQYhjrDLY2SWolF3gFYDuhTZzrhkknOiq%2BT8SayPmW3SBwTx8Lt6xHTq2u6YGCmPezK5jVidzLMXdbfWxs2%2FxkIYeogDC1zvfJBjqkAQ%2FEuIHvowPeRUiNHGBvHYL9zgGsLn5P7FkS6oGyOJZjkObU5MaeMzo9%2BLJ2pfXcbOXS3rn7az4z6lA8tNlEufinNEmKhnn1HY5fiNF1grCio8370IplG9Nj3rLjyXgacZOfr3fLbzRA8wPm8fxAYA2TyF9y%2FuT9qQQ5iCPBn264syRjaPwMndPMb2bDYZFBGpOn0gSxlJ1B7OcC7sS63KqqcbKC&X-Amz-Signature=eacef8808501df9445e23d966e311c390cb553ab051318a17250ab7dd0cc772c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[`.dropna()`](/1867045b058343e1a66b677961515907#3cd5de4bcda14709a032d08303eaa85a)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0f04189f-6088-40c0-82f1-9e49e958a4ea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=8d54afa12cde316db0e3c4cdf2d28b132bc5ec711094fbef2cb6a0a7ff97aaf6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
new_df.dropna(axis=0, how='any')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/36dc593c-1f12-434f-928a-ed45539d53d1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ECFGSLG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDKsIvekgzicylvTjatQM7YjXOIbEWljYLOAY8i%2B%2FJ3hQIhAL72KJwi9GwxU95AjEsxoESJnnQP4m8rqE0olMsybLk%2FKv8DCCcQABoMNjM3NDIzMTgzODA1IgxhQD4bFMwXVx%2Fz9zMq3AO2aHLrxpdNT8uqZ6i8tQFDdWSxhHLZpSczuJ%2BNZD7YVn34JMG%2B8RVl%2FSkA01CJpEbb4E8dGY9MwlIZe8nAduCgpD1M%2Fk0ob53%2F6jKZPbr%2FrDS%2FCQG0GB6PV6zUlXomOqyeSW3Lqo3WE4GJgnV%2Fg2IGJrv6CkHkq4O4S0L8%2BiUV4E5JrF%2BlS8ABmsopiSjm8YtikEha2OMU%2Fto3u4bzMSKrgdyZ9pDm7GgJ55WwxT8R4m%2BaJzLxsR%2BUYN5rM6x92BkcVBfrqKkZcaDX3zPs%2Bo%2BCv7LEccgFg5ZzhnIFKaXTClOAt%2B3trF3JzzY6xhVe6kdWrOP6frnLzekpT8JUfJyozHfGS6Q1HcamoEuoz9T3%2F5mBhISQcfKp3za1StlvvJyrcnczn8fsJur9Ifnl7zhLvnxLDErZ3uFmuSFzh9jDg3xowH%2BeBWCU%2Fvu%2Brz6gknf2aj0NMqEluORAHl8n3q8a9KohFG9p%2BwKn8vbzoBwtUxlf21lF8nOFumodacrCBjzymd5BrX%2BmlQL82yZva2Nhq%2BIWxicvvMmprFowiAjzhEPNw7bOeY3uKsWAFxHeRrrISSWMl%2FiK6lySO62PR3T7wla92ODXUdioA4ywgihSgCeRkZxiGqHYY03ezzCMzvfJBjqkAfz88VVic3KnybVtiGVHz4DtSbfpzHE709EPYYTBvWxGhlddSup%2F9jUrUnwsV9pSnrB1E1kZCotcHK1DpJq9fMTPnK9CAlRm6xUiM5unXWmzx%2B7noXlkI%2Ffmhw7jarPVvmglQ7afuUkaW6o0tnRq0LaK3xw4HgxR8uJhTqDeY6pq6s7MCh8uEY6hgt7Ujb3JfDYcy5XvUzTrrxRK0p181pc00Zly&X-Amz-Signature=8e5ccd70f57736e8ce8bcd9a80b78f2a338a8124a767525ebbb077bff3fa14e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
```python
new_df.dropna(axis=1, how='any')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a965a9b9-1e49-42ba-a2bc-943cdf573bad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD3PO6O6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCcOIGcCLsmxsjtHCaKSvwAc8IjLSfDVO3b61MxeRHW9QIhAIMDlDKX53H0t6tgv%2FbK%2FM9Ryp7Co36hHdMP55QgvQSvKv8DCCcQABoMNjM3NDIzMTgzODA1IgwRAA%2Bgtog4RhOVrb0q3APO67P%2FyRJ0N9BSIJ6jeplyKoYcolQIWvx4GjY9uOf6b03Uw23PUl%2FJeWvjoMgvezhRYpiWB4pceOGU1w%2Bocbz8Df4YvZDBRM7664BMIRO0foyNhnTZPwg5zLx6MJypS%2BvmAgBPzTD%2B%2BUzitg9NH%2BVRnjwdR7y%2B35DK7bzGB6R5Sm1Q1ULQLerHmnEX%2BO3oAoavskaCfKztHbP6ub%2F6fo%2B8A9jbJdS80DS7KmJp8LLTvfdmTq3buHAiiz%2BgOb82Xf0TzV4vUm%2Bi0UrtdnT9vNzlaLEL%2F%2FuenNUS0ptXp0lbjpjNlkVVcb8xxn2fR0yZLQiVH5BN5EQgtYHFn184q1ZogrsGTOfldoXvErXs6ge7KoeG%2FNSqwK3RxIUuN41q0NQMQNJf2zR0ITz9HF5vl2xBG0ywCHDRbziK0MusV2MgumHwKll0qi7ItnKG4kxkyRL%2FHrp2MNfMiz2J2dand30AD0gzQjTFuyZwjsAUIVSIAkYHUZ9uq0rIkpPG6i2E1NS%2F6MjPZDlKI1bqNWveA7X6hwgC00E6uxLHx8uqsIYey5DaNZ1XrwCjAQzI1EMHlNYGmzIq8DTYYi2t1kMX0T1fnU%2Ba18xqEWtqYfrbpkseagEbjBrbkwu8nVDC8zDuzffJBjqkAamakdNYpekyEOVblrJcacr5gZBuZkTbAzsam62X2%2FYSSyW11JJc2z2CrdHbdESG7g7Zf5KBDFdvfiOJkEmO%2BU0srKwNLuUajfz5PlJdwRktMGyLS8%2B2UEBzNrw5PQjiRnMVdP3NGDQdgbncQE845iBAHJRWVVI4GEoJK%2BPYty4X8bn1OU6v6IS2l8X%2FO6EXl1gp%2F1W3PC8OG2CnS0o%2BGfQOwxHM&X-Amz-Signature=3f2aeea54ff30b548642485287af7c54964fad62e75143b3ba1fae98618abf12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.loc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7) [**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=f3602b10d61b97e022b5cfabc8f574543b387aa5c1ba9ca6f22e0861c8be35e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=f3602b10d61b97e022b5cfabc8f574543b387aa5c1ba9ca6f22e0861c8be35e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can we access the values in column `duration` for the 2nd, 3th and 4th row using `.iloc[]`?

<details>
<summary>Solution</summary>

`my_df.iloc[1:4, 1]`
</details>
---
[**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=e12dcbc0e8cf7e5b668477614f4e524e9873e26823f5f0f48d3f0a31dba8fe6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
type(my_df.iloc[3])
```
<details>
<summary>Solution</summary>

`pandas.core.series.Series`
</details>
---
[**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=e12dcbc0e8cf7e5b668477614f4e524e9873e26823f5f0f48d3f0a31dba8fe6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=e12dcbc0e8cf7e5b668477614f4e524e9873e26823f5f0f48d3f0a31dba8fe6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
type(my_df.iloc[2:5, 3:6])
```
<details>
<summary>Solution</summary>

`pandas.core.frame.DataFrame`
</details>
---
[**`.iloc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=e12dcbc0e8cf7e5b668477614f4e524e9873e26823f5f0f48d3f0a31dba8fe6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.iloc[2:5, 3:6]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/71fb880c-fa91-4cf5-bd8f-ef84d991d57a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAV5YAJY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDlVbKfbKvtb5Um6tPAXf8pXJ5IrHniblTDwK2iyAJRaQIhAMdFnNeo2lbkGlizoWQcbIvpLaIxiSWqjy9jqwVFzGtRKv8DCCcQABoMNjM3NDIzMTgzODA1Igx8XjOVeXYcVO5wsoQq3AN3WBwFvTyCAhF8izPBYLSBoOgs%2FPg1M4%2B6%2BzC7BkwRlsBd9pVhP07LFwvjbIXpyeiFw1t9GZym48oRoUczEyMVw4YTK7LC50N828hD1wYZv3J9WVenJgJAKRuL%2BeYZsgZd9O0MLPQsROhmCUYZ9ydL7uGgQ4Av08X%2BgfkGHhVdnwgbOCJVB5JPuG7%2FoC%2FEO6xPEgR52GqMQbLe%2Bo%2BDIlPqbA3PIQM%2BbGX792SEUhyDSpqnrlgf5pspJgO7u4Eq0jr%2BTLO1LaeemkeJX9Xuq3uczsD3i4%2B%2FpDBAiL31uProtZ6prD5lUItGeuhO4f7IjKvlJbyUKd73Fb1%2BqM0ZVMPK6%2FRD7XBPbYCl6NYJO0%2F6KE%2BTgbCR7AIuja82UG1HeIQN7LsfPyKQxMlQ0kLk1b2PzcXicAguKcZNmt%2BxfuYqwDAb9AcnMmrjbu%2B3B%2Bz0g2uyeZ7P7JhwN9y8uVl6EbrxbSz6hI2ysZaOwNFVlbOlKZU1Na0gYuJe8fBFt21tQ8hRrJcNSCH89s%2B0%2B4J09mr3x1I0dmZuHXBVD8CKwt%2BWaLwWygNqSMvF7kXYovbSSpDwIzusfIbVCLc5ngBfzNbAPwaJv0FMBOCyJqYeHj5BzyzTAWJqWlZH5LeTUTDyzffJBjqkARdsCtAuuliYc22%2BWn0v5hYn3lIsR%2F91442v86t3OipHWdiXa8wirSEbc7SaesCSOILP8%2BE9wE%2BOIytqHzGaLHqYoCdSA8xChN5DqijFSsmtjvdvZEVLSUcqQXGOtP2OwnwKG4YDy7QhS2SFUw4m3TYOBFbWQQwQkurdxeoPYyDbFigvREx0j7Z0vHdNkgnv2ZEw1zkUyaMGag4er8bI3X%2FqdBuG&X-Amz-Signature=8c4064d946688efdfadcdeabf43483d513d243103a765e1e6020c848483e4ee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.loc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=e12dcbc0e8cf7e5b668477614f4e524e9873e26823f5f0f48d3f0a31dba8fe6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df.loc[2:5, ['A', 'J']]
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0aec0518-7834-48b9-a0f5-08d85640fbef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BNWNQ3Y%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFYrrZXZlUToPMGqgpbr5AHq6RmPzz4RHrCDPa0P69ufAiBadQklobyxBKy79THoeyWJgQqRhY19S7KypT8MczUr7yr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMWWtEhuPvJR4Sei1tKtwDT8aT%2BUuvzLKHd45hs3iCiA8K%2BCHlb3Oku0%2Fv2HSpNKkEK6cdvbL4JmOzZAFVfqGH2y%2BDFszxNSigtlIQ8CFpeyFgq7G9kOcGS32RfeerzKDkoZRiYn7CqAbyk3ZS4fAmhYbOAkrLjvVCv8xuKBftqtFjJHt409l7zyVqGkL1cVGOnSbJ1L8KEAMTVi2Z2cNQ6cGXO%2Bqe0L0JTMDQRsnRDgKAw7XjZBn7Yq0L4YHwRMMrR2%2Bwykgg%2B6OLRJd64PwoYdtsHwLoYpIX48zD0UAR8%2FjpNetJqFt3qLu503X%2BWNQ%2FJ8hlCESAX5SKA5FfY7gzGgCcfDUYzx29fcP4BdnQfxYnj1S9cYUB6Kd3W0pQ2S69qLN%2BgjWQUFw4ihU72IRxt37EbbwXcsw4IFjyjRvt7j1ULHNIEDgtALfRJk5jo8Q9FaSd6xRuKHNvWKTuOWyWkHEwNt9G8nk6BoXxI2ChKvqIvvf2kofL9lqmXCKEvZmljlb6xHbzRFV01khbEvBjlregD5hjl4J1x1GTFWEhpHW79B3fjy5%2BWKXjK1HjggDXEnuNMSSNi0p3iZNBiNpX%2FsiDKFUzyfAvj%2F49FwVxAYC960h6r12HQMPAl9R%2F6d5P3%2FZe%2FFKi%2FiOozswwvs73yQY6pgGgUewvo0aUZxII57vlwkEpORFR38UNKef%2BWXY4vutJRj2ecD9JTm1gwVekHGOvXF53xftsnZTnnNZDcz%2Fy7Qbu2Ana9WQL0anMox8F8M%2Bvv3EScwDRE9orPY7W0pChseZekAeA13CnzRVt55Fz7i2Rk6YnrWTT4L%2BS7DPXh78g0g70LdKS2mX65bNjDmgyonPzCPUCCxKImBGObPWWRNMYRIti6T0u&X-Amz-Signature=6d195527705fc892a772d5eafad638ab82516ed844ea7a97f80fd16cb52d8a95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.loc[]`**](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=e12dcbc0e8cf7e5b668477614f4e524e9873e26823f5f0f48d3f0a31dba8fe6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.loc[2:5, 3:6]
```
<details>
<summary>Solution</summary>

`TypeError: cannot do slice indexing on Index with these indexers [3] of type int`
</details>
---
[**`.mean()`**](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=f3602b10d61b97e022b5cfabc8f574543b387aa5c1ba9ca6f22e0861c8be35e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.mean(axis=0)[0]
```
<details>
<summary>Solution</summary>

`298.0`
</details>
---
[**`.mean()`**](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=f3602b10d61b97e022b5cfabc8f574543b387aa5c1ba9ca6f22e0861c8be35e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
my_df.mean(axis=1)[3]
```
<details>
<summary>Solution</summary>

`130.0`
</details>
---
[**`.apply()`**](/1867045b058343e1a66b677961515907#9e6d1643dc24411181facc1dd3265ffd)
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XITQU7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBcyYkRLHIlbZI9PhoKEtq5r7uiCenuHbped9anlRcfrAiBpWMLMI7w%2B7AOl35flVBCLL%2B5Rp6IRmncqh9BZ%2BG700Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMd3iRMoU6G6AQngNhKtwDSqDx2%2Fw5yVldU9B6d1tZVu3Xl3keNROh5htD%2BdD9uK%2FiWxqip%2Bdcpvt%2FboxdZ0C9%2BzClHAE9T%2FIzhi%2BDlOar%2F0AdpasYdmGwqb2%2FWwK5hVU7dTM6v7lSXn4AFUW%2F2raWuHf1VvL%2FN6DD5oH1nzl1HNRfQcOJVb32FSUriR3zIwq%2FOgjSjl675bMdAKHY0xrBCr9GTXr3YxJYXbXrV7eBgEDZVcKLBmQ6OLosWVl4rZo5k70OldJe8jP24Yhv5O26%2Fb4w3in5hauZYk3t1yiiaZxBwtQKIAsS%2FH2bnXlycG6cP5qYpK0pFuRdxytzNRHEUtX2rrqzyjCwRhr47Wwb%2FhEzGOOEyqluokHNrpzYK7DmD0DAOn9gdDTBLiIgXE0LEr05UF0ClJE%2FTbTHMALF7imJcWP3aELPD46iIgxsFP0IsFNVG2NriNfcYmfuQWH6%2BDvSeVj43pn9p2zvRvY0%2F%2BG9c%2Ff0tHJbXwrMNJmtofVpZIico8uUbW%2FXCD%2Fs1UGH7E%2BLKuwtGdT1MzfbtM9qpAVYuTp5%2BPvdhnqfUN%2FjtR3F2PY2IajNsXsDltTX6l%2BuTACcmv%2BFGVUAloU%2FoLMCkcgGbZEuMyM87VJDbjTTW1j%2Fu%2BwuPOrCs4za6Y4w5873yQY6pgEZ2s46LW8c0oGyCkLfRbp5K%2F4qEKMyCzH3nEL8DH9q%2BTcaYpe4us9WJZcA5BluWtcYhkf1w8zMoxNN4F2nqvEZUl96t4GvOLTsUgSSiB%2Bdep46sM%2Bv4mAgSumQHnelp6XQ2ZydFBm8zDlC99GtRAefvUY%2BC%2FRlrKM%2BNu3HH5nbjVVGGShhfb6Xbb27jv2g6WclHVEn1s4uyO6IVmWEa7do%2FllnYVfs&X-Amz-Signature=f3602b10d61b97e022b5cfabc8f574543b387aa5c1ba9ca6f22e0861c8be35e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64a649ea-d2f9-41a5-97e6-9c2e482f298e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX3OIMW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICvYCnhaVhXXUYXBxWhqPxrapN8tgXsSES4lwZhAM94tAiAeuZpeonktxvEXemumHJsoTOpA%2F7dVs2432hlTBOjy9ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMSJJJ3%2FEc9aNH866mKtwDNZYWCq23TpXKyBqYrTYHY7A0fgsr0PFXkpqJMTotCbTQseGlc0pmFFQ10RIgQoXoTh5GmxbbBfNAm2sqCP173SaXrQRhmqceBxp1FIaX2ZG%2FIwj6zVa4A2nPZN0b4eWespgm3jJ5zhIBIjMlKvHtZd4DoXPBxMgi4c3f03oOiL6RHqqp%2BISyJkG1vFJnBYnVJp9zLL1ZONW6Tm69z5O8oarMkAzw2q%2FVD9Ye86XCSaGOLawao1hKeQcprdBKQyg0s7DPvJGQjAlDTNEWbcIV2fM6e1OkA9riw6saHL%2B1CWVAbOXrKH9kPpaJlxUf2HevIkDE%2Fts3wbDLqUdjhj5au%2F%2FYsTWWV5sQFUUn0JYIB0GjZXOXV96954HndNRk2pUnjH6Bl%2FfKBFfFxgsT7fNfdngnhnbXhIg%2BKPBIXJhK2oQrdNI2Bs1x4zREdU1cq1DJNzVzUHGCmG4NHWxT83vUSD37bpjxfPSmePUeo5Rmtq8PcFaGnVEhGRajxFTME9GyCBJyOMh5F%2BrOIZSRXTtSWE3ndssFTlCwG6UgOh%2FKvh1Qm4Beqbl7fhXMHhW0yldEQiloxYzB4b0AXlNTUfwxU6gBQqm8Vsj%2B4ahRjESQ396RJDo1itchbQhN8aAw7833yQY6pgFtFOHBf8MvcXaKC5iom6%2FK6nZcs7D1SZ3GGfV6JbMjr%2FufzY%2B5vMMjvNMDYXkc8qFap1xzw6%2FwBx13985gE9FH3MPPP3Ro5sbiCL4GfS4GShmVvMgI2yOk3VIvi0u8Z2ypWN3gVQaq7mir0%2FUU9oKfp5fca8YkRQe%2BbT9tawLSBFDEw4Hw%2BDlWD7REb%2FlT6e8pthyStnIKcRp%2B2QOO3GkNacgDCbjR&X-Amz-Signature=36f0392f1d8fb4867d02568a144bc69a099e6b8f187ffed4450059332f4c9656&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
df['K']= df['J'].apply(lambda x : x % 7)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0c813279-3e2b-4df3-9411-93753cfb528f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLTI7NM3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD04NmRtr7%2FwaEKPSyuVLYZKPNXzsEJS6tbcZfxZmcITQIhAPfVfcqw4h7iDX67zC46o7FydoA9MctF4EiSlL%2BAN%2FSZKv8DCCcQABoMNjM3NDIzMTgzODA1IgwDcIckQI6jWg%2BdYCoq3AM1blfa0ScL7JbkHq0tkeQhARYRs25SZI9kGALEOqq1fgv7XBngoK7jEtpPA7rS7%2FeH3CCXvFwQ3fnewBVe94FO0rGlO%2FCRlsXsT2f4LK3iJ6rFXVHdLLGA3vB%2BmU2uPUF0KwBBnoz%2FPnBVJizJ64Fm1%2FwBwLE%2BLcnDkEjkI%2Fv59MOKzW2FNEZY68HZ3lzuJiwFYCz%2F2K2GMZKtYZUnOrlldYq4u%2FeHYVF04KadYgA9DbIfAskp4MevuHRgBUwVr0G%2BiH2vsbgqshVKulzBnAXuuGtoJ9LEEdGjveBJGwioS15XsREvAjQRhV%2FC0OA3e0Yx8vJdivKQIshdvKJwdER5N05LgqL%2FzwqN%2BvPK0uiH%2BSrqOJowXGvdcUnnppmeGgIl%2B2SCksb7L%2Bq23Ck4Oxy0YUF0KrwpKSZSEHeg%2ByTEgrhb2jHyVFXauSu9rvlp%2B0cY%2FjpCI2Tr9%2BgDN4uCTpSMa38BjfoTwNM65QAGnx4Eftex9MtpR7BhhK1qzxU%2BUMNZ3d%2FWTO1P%2B0%2FxOiJASXOxNhLQ5FAYECuGI6lapfWd%2FesgmmcStbm9yq3e3Gz8lt%2Fl5Yzqey%2BsXugpquj1AT0TO2yzVvNnLkdlhuvbJtNBUWbWLnI1bW%2BDoImBHjDfzffJBjqkASd3lBzZapBvTZxzHFPcmlnZbnmKJdvOd8xR6G1qmZ6%2B2vdHTY3DeYaYj3MblEugvdbTT73Rj0S8HrO4ZUqb5TLvujnvIwfrfWQSC2FvHxn2PYlIznMZw%2Frhh9ywFJesNDWbTPeeJL78WeltDcXm4rym30yRbRmYu49vwrMYZNTIihcNfxr09Y3dw13SbjyJmNRALfMF9O%2FUa6Ey2nyajpHSwDVS&X-Amz-Signature=be42e3ba62609c49066bc22e7bc4b62cd819c5d453d17e78d9fc2e66bb53a18e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.unique()`**](/1867045b058343e1a66b677961515907#74cb3dd5af264206a7e4ccc9b07d9a7a)** **& `.nunique()`
![players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2ba26b62-6de1-47c6-8d67-724d44c6f4bd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX3OIMW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICvYCnhaVhXXUYXBxWhqPxrapN8tgXsSES4lwZhAM94tAiAeuZpeonktxvEXemumHJsoTOpA%2F7dVs2432hlTBOjy9ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMSJJJ3%2FEc9aNH866mKtwDNZYWCq23TpXKyBqYrTYHY7A0fgsr0PFXkpqJMTotCbTQseGlc0pmFFQ10RIgQoXoTh5GmxbbBfNAm2sqCP173SaXrQRhmqceBxp1FIaX2ZG%2FIwj6zVa4A2nPZN0b4eWespgm3jJ5zhIBIjMlKvHtZd4DoXPBxMgi4c3f03oOiL6RHqqp%2BISyJkG1vFJnBYnVJp9zLL1ZONW6Tm69z5O8oarMkAzw2q%2FVD9Ye86XCSaGOLawao1hKeQcprdBKQyg0s7DPvJGQjAlDTNEWbcIV2fM6e1OkA9riw6saHL%2B1CWVAbOXrKH9kPpaJlxUf2HevIkDE%2Fts3wbDLqUdjhj5au%2F%2FYsTWWV5sQFUUn0JYIB0GjZXOXV96954HndNRk2pUnjH6Bl%2FfKBFfFxgsT7fNfdngnhnbXhIg%2BKPBIXJhK2oQrdNI2Bs1x4zREdU1cq1DJNzVzUHGCmG4NHWxT83vUSD37bpjxfPSmePUeo5Rmtq8PcFaGnVEhGRajxFTME9GyCBJyOMh5F%2BrOIZSRXTtSWE3ndssFTlCwG6UgOh%2FKvh1Qm4Beqbl7fhXMHhW0yldEQiloxYzB4b0AXlNTUfwxU6gBQqm8Vsj%2B4ahRjESQ396RJDo1itchbQhN8aAw7833yQY6pgFtFOHBf8MvcXaKC5iom6%2FK6nZcs7D1SZ3GGfV6JbMjr%2FufzY%2B5vMMjvNMDYXkc8qFap1xzw6%2FwBx13985gE9FH3MPPP3Ro5sbiCL4GfS4GShmVvMgI2yOk3VIvi0u8Z2ypWN3gVQaq7mir0%2FUU9oKfp5fca8YkRQe%2BbT9tawLSBFDEw4Hw%2BDlWD7REb%2FlT6e8pthyStnIKcRp%2B2QOO3GkNacgDCbjR&X-Amz-Signature=ff17bffa877686f64a23ea311dee6260704d6093cd369833ae3b0d0003478f93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6b01f9a6-c80f-467d-a6a2-790e9fb34459/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX3OIMW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICvYCnhaVhXXUYXBxWhqPxrapN8tgXsSES4lwZhAM94tAiAeuZpeonktxvEXemumHJsoTOpA%2F7dVs2432hlTBOjy9ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMSJJJ3%2FEc9aNH866mKtwDNZYWCq23TpXKyBqYrTYHY7A0fgsr0PFXkpqJMTotCbTQseGlc0pmFFQ10RIgQoXoTh5GmxbbBfNAm2sqCP173SaXrQRhmqceBxp1FIaX2ZG%2FIwj6zVa4A2nPZN0b4eWespgm3jJ5zhIBIjMlKvHtZd4DoXPBxMgi4c3f03oOiL6RHqqp%2BISyJkG1vFJnBYnVJp9zLL1ZONW6Tm69z5O8oarMkAzw2q%2FVD9Ye86XCSaGOLawao1hKeQcprdBKQyg0s7DPvJGQjAlDTNEWbcIV2fM6e1OkA9riw6saHL%2B1CWVAbOXrKH9kPpaJlxUf2HevIkDE%2Fts3wbDLqUdjhj5au%2F%2FYsTWWV5sQFUUn0JYIB0GjZXOXV96954HndNRk2pUnjH6Bl%2FfKBFfFxgsT7fNfdngnhnbXhIg%2BKPBIXJhK2oQrdNI2Bs1x4zREdU1cq1DJNzVzUHGCmG4NHWxT83vUSD37bpjxfPSmePUeo5Rmtq8PcFaGnVEhGRajxFTME9GyCBJyOMh5F%2BrOIZSRXTtSWE3ndssFTlCwG6UgOh%2FKvh1Qm4Beqbl7fhXMHhW0yldEQiloxYzB4b0AXlNTUfwxU6gBQqm8Vsj%2B4ahRjESQ396RJDo1itchbQhN8aAw7833yQY6pgFtFOHBf8MvcXaKC5iom6%2FK6nZcs7D1SZ3GGfV6JbMjr%2FufzY%2B5vMMjvNMDYXkc8qFap1xzw6%2FwBx13985gE9FH3MPPP3Ro5sbiCL4GfS4GShmVvMgI2yOk3VIvi0u8Z2ypWN3gVQaq7mir0%2FUU9oKfp5fca8YkRQe%2BbT9tawLSBFDEw4Hw%2BDlWD7REb%2FlT6e8pthyStnIKcRp%2B2QOO3GkNacgDCbjR&X-Amz-Signature=c356247090d750ab007928ae44845619be1f8ce0c9d5d5e57906cf227a5f6e24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df.pivot('Team' ,'Goals' , 'Player')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ab2ba056-0bb1-42b1-8a42-8fe72f98b327/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJSRWZD5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD65uNCTjSgHINkgwuDR864EOEMgS%2FbImDiscfGmDiGoAIhAM8jj4wn3XtDzflfq%2FPoaD2In5KmvO1QfX68y2%2FZPnS3Kv8DCCcQABoMNjM3NDIzMTgzODA1IgwfGqtTcpcjoIxsM5cq3APTB4wTGx84tOJe3t0j7rXet96ngAzJ54t%2BjFebmRMe0tKYjnjq5tDW21jlar9piyTFjwol%2Be5Ex1AOQlnNlyOYuzY2747qG3ragIEDTAQe02i83ltIPSPC9jMCjwXgfv8xKygfUJE1Ee4FfHuYs0aOpgIIq9qHLRMs%2FYQhMrRkOQyKkR9dZif5trtphAB2sZ0YbGdQejesC5EK3x4CN79MDtoM6Y1SINecTS93IrEBCtn4D7p8pthb4mI9Z26BTzbkJTykUDUh9lj9Q5xKtDXh5nbrmoCfQn%2Fip42hWIFE8Ydb0WTrT9bRyOI%2BzO4yMNvIlXF8LQgKK%2BDCe8tVZ2jgNGb6B2xQwa5vbf4%2Fo2bJHb3jzKipnLMM8yenrWOWPEcGkaPkBsuzXqaU954hRDXD5tkHfzp3nmhVJ1srfMOjr2IqK2SBdnZ63kjRFDX5dglo2MqeDaHUce%2FrXF8I5%2BHU4%2B30jYKqjF2N29nwfyyGLf5xnrBp%2FPJjNEEG%2FZU%2B3T7eJHW5TAntcKwFY3Y2zGg0We7YQ4oqNEs%2Bn0z5z515arlwaz86GzmYYrueRe4EkIBBUkCJS3wgsChOtVb9p6yayOk37iRzEt17%2FUpvvmKcSB53EwJ4%2BXwMMcFLSjCFzvfJBjqkAUWRIybsGp1NR63yUZm4r501Bd%2Fc5GT%2BUjXNZFKuX2Sb9kwXGH2o3f2BOMW23bWdBAp4HDxUeHWffqJ1zcU7GbBBnUI9HVfvty7ufYhyz884oNdEg%2BR62pkAhd9Y0ikrQTk26VfREl29LLtGqbGREblcFAWDIzC1pmYAtRM1mM5SMIzwGdQU%2BakqRXW6k4sB4ql9BdBIBpfXP4wN%2FCdJ8TWjkAlc&X-Amz-Signature=4f11451835794c805eafa9b45bacb67dbd558291fcdb20f149804353a80315e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
```python
players_df.pivot('Goals', 'Team', 'Shots on goal')
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5c172887-8c06-4769-b64c-4c4ffdc81431/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X6IK7C2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBPXXjW6r%2BvyNvIGbhRZvt7HviaiHIqBc%2BXL3BK4KGpsAiBTbVO2I%2BQDoWZtn0xh0eF9QTS%2F%2Bg0HvUBT741Qy3xoOCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMFPWVtTryDEOI0PZqKtwDirepwXvo%2FNdwmJyFQDCdtRzwNT9EU8jyB8EjguDSl%2F1Pgh8dWiuAyl%2BBiXgOwgc%2BhUxx3zuD4EFnp7gcvYIT88NM7S2kvX2HX5PaYGtGlpB4FEZ5kNqh1zwxM7nCjvULMNu2n7o%2Bqs4pNj8uXeh6%2FvxIGsz2OpB%2BhGSQe2MK8u3jNDVgHWlKdFTvcL4tHJDc4Xc7otR3esKa41GLxWmX6RduoEtpNrFk2NuflPWgteXLYnI4sq57LuLReI0Jkj01D5CGot3IYqr1SVLXmS2mps28GA29zjL%2FVoUYWTcEpA80H0KuCWa2VUtDNDnHr77HKKpVYpiYu8277xWWL3f6GJjnoKdLuHoKFYxwN15h%2BhK9V%2FKLygmu%2B9TAVnwQWSbRbL2s7zDx5t3k4w7xPdyerLEruvu3n4tgFob1K05FziI9xtfcY6f3LsfDIBxM3McNfVwhSB6STaxA5Um410seRgIan40nnUy1%2FEErJuaV%2Futqxygdhidtb2yRT7COFoU7sKUccenz9JKWNUgX5cvsEyFbpcn6oCwXTQP%2BM2fG9VJwprHe3SkR67I7Hdl5RXblt4QqTTMuAvIRGgtl%2BWQyoniHNbj%2BPraMFTNYIZ9gzLwRp2kf21WqzLs%2Bd4ow0873yQY6pgHEgJadLWj9uIRaI%2BZIBL4M7F9L2QR6tikw4u3eVAS8MQ0IVHq8qUi7BdtWg5qFvDYKu52GjLoire%2FKfPdNDqz6PMiC%2B4FOLZZYbK2v6KCmwZNs%2FZbI8X8NjF5t2GOrvxYuwvXgzB9K69FV4%2FMaIE0dA2emFhQsj1DsBLA8juS%2BQW1sd1Lee%2FSmCADzEyqEJ0qTyaPFxzVHLwQjd%2ByKN8Bv1Bm%2FUkNU&X-Amz-Signature=2a80b8384ff5c9bd895d19bcbe202109ad02f5a71451d1f33350bb6f045ce94b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.T`**](/1867045b058343e1a66b677961515907#b65f0a7a58214e66ba42846c09b6dbdd)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e2a0d44b-4888-4885-95e6-69a9b9a8e624/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX3OIMW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICvYCnhaVhXXUYXBxWhqPxrapN8tgXsSES4lwZhAM94tAiAeuZpeonktxvEXemumHJsoTOpA%2F7dVs2432hlTBOjy9ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMSJJJ3%2FEc9aNH866mKtwDNZYWCq23TpXKyBqYrTYHY7A0fgsr0PFXkpqJMTotCbTQseGlc0pmFFQ10RIgQoXoTh5GmxbbBfNAm2sqCP173SaXrQRhmqceBxp1FIaX2ZG%2FIwj6zVa4A2nPZN0b4eWespgm3jJ5zhIBIjMlKvHtZd4DoXPBxMgi4c3f03oOiL6RHqqp%2BISyJkG1vFJnBYnVJp9zLL1ZONW6Tm69z5O8oarMkAzw2q%2FVD9Ye86XCSaGOLawao1hKeQcprdBKQyg0s7DPvJGQjAlDTNEWbcIV2fM6e1OkA9riw6saHL%2B1CWVAbOXrKH9kPpaJlxUf2HevIkDE%2Fts3wbDLqUdjhj5au%2F%2FYsTWWV5sQFUUn0JYIB0GjZXOXV96954HndNRk2pUnjH6Bl%2FfKBFfFxgsT7fNfdngnhnbXhIg%2BKPBIXJhK2oQrdNI2Bs1x4zREdU1cq1DJNzVzUHGCmG4NHWxT83vUSD37bpjxfPSmePUeo5Rmtq8PcFaGnVEhGRajxFTME9GyCBJyOMh5F%2BrOIZSRXTtSWE3ndssFTlCwG6UgOh%2FKvh1Qm4Beqbl7fhXMHhW0yldEQiloxYzB4b0AXlNTUfwxU6gBQqm8Vsj%2B4ahRjESQ396RJDo1itchbQhN8aAw7833yQY6pgFtFOHBf8MvcXaKC5iom6%2FK6nZcs7D1SZ3GGfV6JbMjr%2FufzY%2B5vMMjvNMDYXkc8qFap1xzw6%2FwBx13985gE9FH3MPPP3Ro5sbiCL4GfS4GShmVvMgI2yOk3VIvi0u8Z2ypWN3gVQaq7mir0%2FUU9oKfp5fca8YkRQe%2BbT9tawLSBFDEw4Hw%2BDlWD7REb%2FlT6e8pthyStnIKcRp%2B2QOO3GkNacgDCbjR&X-Amz-Signature=f134dbce80b48a359736764efce452e531f254683aaa6b584f49aeef497c56f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d9242361-8805-4665-949c-9386b8c6ce62/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTXSH572%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDr6Rs5B2fhzK%2FBWAfDPTRBi64rHqdmvGfmTTtFbuPvoAIgF8QDNbts3KhOgavWbyYb6oBK6ouQ8B3SgXxZLOyVoh4q%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDPOc9o1H1NH9BRqEhircA1Aqq7WaTxPsWo4toKir8tflOF4p1OwIEm%2BaYR5GotOn%2Fs8xUf3lryu%2BLy2gdWJvXEh6S7bDKiU5IbGn8fu97C%2BUQivXyvBgd8eX74QsoHQhm%2B%2Fqx6hxDNA4LM1H2jJfscHeMP8D9G4Cs6Bf79QGW9ayCY9a95Lq0Z6oviwS%2FMfAaIWje4R56jas4xBFd4wweS4Kbqs4tFiUcrm0%2BwRKPEKDXLrTGuE%2B9kcPqo4zH5ROIrh1h0H30Gl%2FFA8e5i0Esa0OTt5MOoc377mJYGuPx3lAF8GJaoI3f%2BUugBN%2BvU2qGBkkZZuD0DsX2SfWl4wYyCbQNAZ6ITDqZ9lZshai8yjeT8QlkSNo7xA3%2F5HBn8fuS%2FyOQhj8%2Bq%2FtBm8olbCgCRfcTN1avWF4dUBpJ5MMmoYedQIQKuNgEcRvu6NmjOczT3sqHap3DPgOVOonzIfAwGtUBxG7lN2KY%2Bw4eaqfzQGB5qHN0ap47LumC%2BQQYdfniMA%2BoajEc04zwEpPmB%2FgOxUYhW15Q0ftM8eAvrsQjDBVX4%2BczpveeXdDOOJEhooSil8V7gUSHYhxV6GRo1CpVtn4RlS0m7gIrphDTtDbypROAbcwl1ifQm%2BUWbf0muiIxVcV6ZhSfSFb25swMMPO98kGOqUBLi%2B3YTabdgYM1ef%2F2X7oRgfQmXIjSLxj5SCas3NdyBXlhKLSJnSd9%2FEafd%2BEc2JyvqmSASBNNyOaEYiO53XL1XamrsChQbhETdzDgtCgTOJejRx4F3GZ%2FMoII6StPftUTzW4KLzuTeU5eZPBT0fJ7z2fNXj2T13DjAqpAV5j2sRtluNYykJzibEQrxj53dvZ8FjLFGkjUKmFpp2dr8H5HRnsm0X5&X-Amz-Signature=4289ddf0ecfe66fbebcfaa12a1e5ae7cfcae53bc655c3e8e4bd7a54978174137&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.melt()`**](/1867045b058343e1a66b677961515907#5e95974d66444f179b205b86fa56a92d)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f5c49bcc-7d18-46b2-81c0-dd9d73d5ce8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX3OIMW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICvYCnhaVhXXUYXBxWhqPxrapN8tgXsSES4lwZhAM94tAiAeuZpeonktxvEXemumHJsoTOpA%2F7dVs2432hlTBOjy9ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMSJJJ3%2FEc9aNH866mKtwDNZYWCq23TpXKyBqYrTYHY7A0fgsr0PFXkpqJMTotCbTQseGlc0pmFFQ10RIgQoXoTh5GmxbbBfNAm2sqCP173SaXrQRhmqceBxp1FIaX2ZG%2FIwj6zVa4A2nPZN0b4eWespgm3jJ5zhIBIjMlKvHtZd4DoXPBxMgi4c3f03oOiL6RHqqp%2BISyJkG1vFJnBYnVJp9zLL1ZONW6Tm69z5O8oarMkAzw2q%2FVD9Ye86XCSaGOLawao1hKeQcprdBKQyg0s7DPvJGQjAlDTNEWbcIV2fM6e1OkA9riw6saHL%2B1CWVAbOXrKH9kPpaJlxUf2HevIkDE%2Fts3wbDLqUdjhj5au%2F%2FYsTWWV5sQFUUn0JYIB0GjZXOXV96954HndNRk2pUnjH6Bl%2FfKBFfFxgsT7fNfdngnhnbXhIg%2BKPBIXJhK2oQrdNI2Bs1x4zREdU1cq1DJNzVzUHGCmG4NHWxT83vUSD37bpjxfPSmePUeo5Rmtq8PcFaGnVEhGRajxFTME9GyCBJyOMh5F%2BrOIZSRXTtSWE3ndssFTlCwG6UgOh%2FKvh1Qm4Beqbl7fhXMHhW0yldEQiloxYzB4b0AXlNTUfwxU6gBQqm8Vsj%2B4ahRjESQ396RJDo1itchbQhN8aAw7833yQY6pgFtFOHBf8MvcXaKC5iom6%2FK6nZcs7D1SZ3GGfV6JbMjr%2FufzY%2B5vMMjvNMDYXkc8qFap1xzw6%2FwBx13985gE9FH3MPPP3Ro5sbiCL4GfS4GShmVvMgI2yOk3VIvi0u8Z2ypWN3gVQaq7mir0%2FUU9oKfp5fca8YkRQe%2BbT9tawLSBFDEw4Hw%2BDlWD7REb%2FlT6e8pthyStnIKcRp%2B2QOO3GkNacgDCbjR&X-Amz-Signature=b8ef8d7ea10a1c07db9afb5ca86fad7c64a0b375740444ad37090068f6c7d2fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
players_df[['Team', 'Player', 'Goals']].melt()
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/16d89d26-291f-489a-9140-050a0e525669/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCL5ZHVY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDh%2B63PYJ0N1JyD468MJWuWEDIEwBEDIJ2nVql6s0aEgQIhAMt%2FKVwyFjJK7kVQZGjQRbi2ubg%2BslTzZJZvteYihbIrKv8DCCcQABoMNjM3NDIzMTgzODA1IgzTqC3qdsD85pa6P74q3AOpoRV0lHDwiezQ5ZBqPJXJP4f8gk1fagy%2FritPImbSU6NjLpQNH69UvhsxlBvfE5CTfrorSaEAX2iI9WQcP7sj7%2B1uYOxU98u8yvpsBcY8sbEcr%2B2VddfHI%2F0EPlZ2EqhSjpqQDkqQo1AkfWHM9kytrj1c2XrbU9ZIwbW16%2FJDCNuJSwRx4gZ2EN9L%2BYRZn1cZEbELuP4RKV3NzJomxDh7SRcoNhYSYa8qwF857upZADPGqA55t%2FVXINqhgCIjGU02rL0P9Jh%2BXsSL8EaMrhI7vMLJs%2BorJuthdD49jjumuOi%2FyzaGiNck0SyZXDuHc0X2r0gozP%2BnduyEdiXXnSk2igQJNaCjXm%2B25F1%2FET1AnLE2mBv%2FkLl7LggqZj12xtIFLgeAUfkGFxw9qD2k09KGPbyFLrvcmehadJeVVVkaUfv5FQEHVgYj5qojo5axuWu%2B%2BQaFiT3NCOXx%2BolDvOi9%2F5%2FfAJiddD3Vmd4BU%2F4sOC3uBc9%2Fu5CNSGu5KvBc8OWuRaiM1ttDFEf%2BrTb7wESHzhpgIPBwXSypkEpzZ6aRPNFuw1NvoPdTWZtDqqVxJlXxVIgbTBRxZ1svjYLt8w1scjQo3cGcIJKhc3Zv625BLVbY8VUKNThTxlO%2FRjDhzffJBjqkAQ6ILdk0a%2BlZ%2BBy7uhaufd4d9r8IOeGTO3U37XttT22QZZt9vqPNLkBhH8LapedMhLUC4iTqphmoZGFDWzF4JJDj246wGycuJcyW4ZZEf4zzHGVgS%2FGyIEXbnUfca0O687yKmrcuYerRpDZ3sanwMJEcWKIIP53GmF%2F%2FyKUs1PxLFXOl51eEkTD%2B6UsVaP22wMCtJTdLYvjriOOZ8VUJJQLP8ALJ&X-Amz-Signature=2a14d986f43ea5c3610914146183e35dc135eff58a09afa254ff32c673b3f29d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
[**`.agg()`**](/1867045b058343e1a66b677961515907#1c8f902fb8774ff7ab8c9bd1d9f76684)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a931d954-19f8-4897-83cc-e80d61b447cb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX3OIMW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICvYCnhaVhXXUYXBxWhqPxrapN8tgXsSES4lwZhAM94tAiAeuZpeonktxvEXemumHJsoTOpA%2F7dVs2432hlTBOjy9ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMSJJJ3%2FEc9aNH866mKtwDNZYWCq23TpXKyBqYrTYHY7A0fgsr0PFXkpqJMTotCbTQseGlc0pmFFQ10RIgQoXoTh5GmxbbBfNAm2sqCP173SaXrQRhmqceBxp1FIaX2ZG%2FIwj6zVa4A2nPZN0b4eWespgm3jJ5zhIBIjMlKvHtZd4DoXPBxMgi4c3f03oOiL6RHqqp%2BISyJkG1vFJnBYnVJp9zLL1ZONW6Tm69z5O8oarMkAzw2q%2FVD9Ye86XCSaGOLawao1hKeQcprdBKQyg0s7DPvJGQjAlDTNEWbcIV2fM6e1OkA9riw6saHL%2B1CWVAbOXrKH9kPpaJlxUf2HevIkDE%2Fts3wbDLqUdjhj5au%2F%2FYsTWWV5sQFUUn0JYIB0GjZXOXV96954HndNRk2pUnjH6Bl%2FfKBFfFxgsT7fNfdngnhnbXhIg%2BKPBIXJhK2oQrdNI2Bs1x4zREdU1cq1DJNzVzUHGCmG4NHWxT83vUSD37bpjxfPSmePUeo5Rmtq8PcFaGnVEhGRajxFTME9GyCBJyOMh5F%2BrOIZSRXTtSWE3ndssFTlCwG6UgOh%2FKvh1Qm4Beqbl7fhXMHhW0yldEQiloxYzB4b0AXlNTUfwxU6gBQqm8Vsj%2B4ahRjESQ396RJDo1itchbQhN8aAw7833yQY6pgFtFOHBf8MvcXaKC5iom6%2FK6nZcs7D1SZ3GGfV6JbMjr%2FufzY%2B5vMMjvNMDYXkc8qFap1xzw6%2FwBx13985gE9FH3MPPP3Ro5sbiCL4GfS4GShmVvMgI2yOk3VIvi0u8Z2ypWN3gVQaq7mir0%2FUU9oKfp5fca8YkRQe%2BbT9tawLSBFDEw4Hw%2BDlWD7REb%2FlT6e8pthyStnIKcRp%2B2QOO3GkNacgDCbjR&X-Amz-Signature=d5b3f3c1fe871aaafd539283c17a1213699df49fb867c44b0044c20ebb64280d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c0482cd9-974a-43e1-ba7b-8c751b6789e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX3OIMW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICvYCnhaVhXXUYXBxWhqPxrapN8tgXsSES4lwZhAM94tAiAeuZpeonktxvEXemumHJsoTOpA%2F7dVs2432hlTBOjy9ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMSJJJ3%2FEc9aNH866mKtwDNZYWCq23TpXKyBqYrTYHY7A0fgsr0PFXkpqJMTotCbTQseGlc0pmFFQ10RIgQoXoTh5GmxbbBfNAm2sqCP173SaXrQRhmqceBxp1FIaX2ZG%2FIwj6zVa4A2nPZN0b4eWespgm3jJ5zhIBIjMlKvHtZd4DoXPBxMgi4c3f03oOiL6RHqqp%2BISyJkG1vFJnBYnVJp9zLL1ZONW6Tm69z5O8oarMkAzw2q%2FVD9Ye86XCSaGOLawao1hKeQcprdBKQyg0s7DPvJGQjAlDTNEWbcIV2fM6e1OkA9riw6saHL%2B1CWVAbOXrKH9kPpaJlxUf2HevIkDE%2Fts3wbDLqUdjhj5au%2F%2FYsTWWV5sQFUUn0JYIB0GjZXOXV96954HndNRk2pUnjH6Bl%2FfKBFfFxgsT7fNfdngnhnbXhIg%2BKPBIXJhK2oQrdNI2Bs1x4zREdU1cq1DJNzVzUHGCmG4NHWxT83vUSD37bpjxfPSmePUeo5Rmtq8PcFaGnVEhGRajxFTME9GyCBJyOMh5F%2BrOIZSRXTtSWE3ndssFTlCwG6UgOh%2FKvh1Qm4Beqbl7fhXMHhW0yldEQiloxYzB4b0AXlNTUfwxU6gBQqm8Vsj%2B4ahRjESQ396RJDo1itchbQhN8aAw7833yQY6pgFtFOHBf8MvcXaKC5iom6%2FK6nZcs7D1SZ3GGfV6JbMjr%2FufzY%2B5vMMjvNMDYXkc8qFap1xzw6%2FwBx13985gE9FH3MPPP3Ro5sbiCL4GfS4GShmVvMgI2yOk3VIvi0u8Z2ypWN3gVQaq7mir0%2FUU9oKfp5fca8YkRQe%2BbT9tawLSBFDEw4Hw%2BDlWD7REb%2FlT6e8pthyStnIKcRp%2B2QOO3GkNacgDCbjR&X-Amz-Signature=808c4a61b623d52cd14df30c0e153675bddcdcbcb0c83dbab525592bae7baba4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a09b158c-b1c1-45e2-a752-8890edc85f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX3OIMW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICvYCnhaVhXXUYXBxWhqPxrapN8tgXsSES4lwZhAM94tAiAeuZpeonktxvEXemumHJsoTOpA%2F7dVs2432hlTBOjy9ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMSJJJ3%2FEc9aNH866mKtwDNZYWCq23TpXKyBqYrTYHY7A0fgsr0PFXkpqJMTotCbTQseGlc0pmFFQ10RIgQoXoTh5GmxbbBfNAm2sqCP173SaXrQRhmqceBxp1FIaX2ZG%2FIwj6zVa4A2nPZN0b4eWespgm3jJ5zhIBIjMlKvHtZd4DoXPBxMgi4c3f03oOiL6RHqqp%2BISyJkG1vFJnBYnVJp9zLL1ZONW6Tm69z5O8oarMkAzw2q%2FVD9Ye86XCSaGOLawao1hKeQcprdBKQyg0s7DPvJGQjAlDTNEWbcIV2fM6e1OkA9riw6saHL%2B1CWVAbOXrKH9kPpaJlxUf2HevIkDE%2Fts3wbDLqUdjhj5au%2F%2FYsTWWV5sQFUUn0JYIB0GjZXOXV96954HndNRk2pUnjH6Bl%2FfKBFfFxgsT7fNfdngnhnbXhIg%2BKPBIXJhK2oQrdNI2Bs1x4zREdU1cq1DJNzVzUHGCmG4NHWxT83vUSD37bpjxfPSmePUeo5Rmtq8PcFaGnVEhGRajxFTME9GyCBJyOMh5F%2BrOIZSRXTtSWE3ndssFTlCwG6UgOh%2FKvh1Qm4Beqbl7fhXMHhW0yldEQiloxYzB4b0AXlNTUfwxU6gBQqm8Vsj%2B4ahRjESQ396RJDo1itchbQhN8aAw7833yQY6pgFtFOHBf8MvcXaKC5iom6%2FK6nZcs7D1SZ3GGfV6JbMjr%2FufzY%2B5vMMjvNMDYXkc8qFap1xzw6%2FwBx13985gE9FH3MPPP3Ro5sbiCL4GfS4GShmVvMgI2yOk3VIvi0u8Z2ypWN3gVQaq7mir0%2FUU9oKfp5fca8YkRQe%2BbT9tawLSBFDEw4Hw%2BDlWD7REb%2FlT6e8pthyStnIKcRp%2B2QOO3GkNacgDCbjR&X-Amz-Signature=7c0d331778027f54082a0e39d584c8ec52237a85b96205d3c0f2e4b188f1639a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/52e3e193-b95c-41d4-9068-e65439fb4bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX3OIMW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICvYCnhaVhXXUYXBxWhqPxrapN8tgXsSES4lwZhAM94tAiAeuZpeonktxvEXemumHJsoTOpA%2F7dVs2432hlTBOjy9ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMSJJJ3%2FEc9aNH866mKtwDNZYWCq23TpXKyBqYrTYHY7A0fgsr0PFXkpqJMTotCbTQseGlc0pmFFQ10RIgQoXoTh5GmxbbBfNAm2sqCP173SaXrQRhmqceBxp1FIaX2ZG%2FIwj6zVa4A2nPZN0b4eWespgm3jJ5zhIBIjMlKvHtZd4DoXPBxMgi4c3f03oOiL6RHqqp%2BISyJkG1vFJnBYnVJp9zLL1ZONW6Tm69z5O8oarMkAzw2q%2FVD9Ye86XCSaGOLawao1hKeQcprdBKQyg0s7DPvJGQjAlDTNEWbcIV2fM6e1OkA9riw6saHL%2B1CWVAbOXrKH9kPpaJlxUf2HevIkDE%2Fts3wbDLqUdjhj5au%2F%2FYsTWWV5sQFUUn0JYIB0GjZXOXV96954HndNRk2pUnjH6Bl%2FfKBFfFxgsT7fNfdngnhnbXhIg%2BKPBIXJhK2oQrdNI2Bs1x4zREdU1cq1DJNzVzUHGCmG4NHWxT83vUSD37bpjxfPSmePUeo5Rmtq8PcFaGnVEhGRajxFTME9GyCBJyOMh5F%2BrOIZSRXTtSWE3ndssFTlCwG6UgOh%2FKvh1Qm4Beqbl7fhXMHhW0yldEQiloxYzB4b0AXlNTUfwxU6gBQqm8Vsj%2B4ahRjESQ396RJDo1itchbQhN8aAw7833yQY6pgFtFOHBf8MvcXaKC5iom6%2FK6nZcs7D1SZ3GGfV6JbMjr%2FufzY%2B5vMMjvNMDYXkc8qFap1xzw6%2FwBx13985gE9FH3MPPP3Ro5sbiCL4GfS4GShmVvMgI2yOk3VIvi0u8Z2ypWN3gVQaq7mir0%2FUU9oKfp5fca8YkRQe%2BbT9tawLSBFDEw4Hw%2BDlWD7REb%2FlT6e8pthyStnIKcRp%2B2QOO3GkNacgDCbjR&X-Amz-Signature=8f7086213dcfc93b88888a3bb8628ad5db9687dfc45fdcaaa3593d1769877c6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5d7fd861-b3a8-4b56-9abc-1a5bf807d1d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JXLRX63%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIALYx7gTmKKePWd37H2xzgScp1SUxRFPY%2BDht%2FQDPBYcAiEA9iWx2FhzrVW5p3MyNktRzNCH%2Bd02iFFtGZauDznB2iEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDCMDX8x2Ie%2BowO1ePSrcAyG7OXYC%2BSdaqGUYwlyz8uEbgSkT95sXjD8kUEEQTbNWpgl1T%2Fi6mEzVpF67%2BzQP9Yhq2Q6AfUsUFFY5NL7%2FLWGRg%2BCE%2BK5zgx7TE07kevUsX1ZaLHPq6eNyPqZbOBAcVYN6jJY8j%2FIlaqt39vIXe26FxVjreu%2FSmbJopCDhsSt%2BCSceh2qbXLTLHljmWRYvmBuLS9NegJDWuU6geRI0YsryhR8o42y02zOtAbOeh9kUMpeczBRDZK4Lya4I%2FFNp0JYXoltteAD0Vu6YJUg6sXw4dfaVUp3lKr2XJkIq%2BhlXURRJJnCAtM84PZ1akkaFLfzOhHQUPA198igSTHP7zmm3Nt%2FUbp11kXue79GTkk2toHzlcl36hYYub6CI0XTiYFR1F3ScCWgPfth0swlzwkWEFduHhUUhVacrWpaUcPmM%2BAlKGDbbQqkEz8rXlsqE2dtcDWvmQYi9XY3TSM7FBM7EM%2BYFGHJARBq0rlo%2BSSOlwG7%2B50wWX4MQWMNVcy9NrM3T3fMXnGeuTgzSiWOosO1Kzwkp2gHnDd7df0oH2xCyAeDOxjpylmrEcSYJ1dZ5vmqjT4oJMoad%2FaRFd%2FYNks0PcmqvJEDQZVBc0WW5h3xSvXF2NKp4Fi93BKUgMNXO98kGOqUB2yCqW%2FIVACvJCaMgpApCgyUNvcHLbLISVj%2FQQ35lfsksMZ%2FcOnDzrvdhbMYMJKkJWoWAUgrOWtEGzrjSzcriPqwRgSO8iuO5HcXxLgo%2BpWUj61%2FiO3p84Y1pG59x5qsp7y6NjyApJtBWOx%2BLz5KXF1qbs679dy0cx%2BStPl7acSXXViEFW44LC6vyKv6dWLLuVZM9ybgkvEoXGeyxBmZ5YYJ6vx5z&X-Amz-Signature=81a07b2daa82af9869850fb95ac514c7c5b1e135a73d02a50c95f4e5ab8d577d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`df_2`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d2043413-8efb-4768-9882-12b859ece727/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6563F6S%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCrzhz%2BzbFWcNJULBX29LjWdqJ5ouo%2BCEo3xaNr%2Bi8cNgIhANw3lRJajFJ8bmoWO%2FlHFM4ROuytSSsX%2BgYuV4vrWVMKKv8DCCcQABoMNjM3NDIzMTgzODA1IgzGzj3JGfmd5RqMbKQq3AMYLhF1kLXlqattGj034uARSBvqh7eK81%2Bjyvxji%2BNTJ6Jb6xl8jENYG3mgx2n4HFBwLIyssf5HTm0jh0CyXg7BswEMmGtRdqFOuN6GTkpAqxuAjMDDzn3F67vaZ%2BGFwEbOl2P4hUHSqQAtGfqCblHALuC1aiCjYuWilILvdiRN2w9NG%2BL57MbEYcWRUZiFt5UQLKTkEZ8oT7e0peMsWzmdh3HeqxTbVzVT5mxmDI%2BQiajckIOhcc9aRIanwRHZKQEhncADcMIshsLeK6TIKFt8BoIQ8MsLmPyi0w1%2F8sd5CDPH8whkTOSF15Eu6%2BJaDPAFiDSmbxc0LDeB8TfmqZgZixMi9YjGiJ5sNfhEO4A6iR2jkL5rvWSFq2mL%2FUYXkU6LYKPddwI%2FXbj%2BG4%2BX0IfsLafjfvRdr%2FN5Q2nOQIRA5reX1qdypSI4iOglwYzu4KtyAxsiYzOx2dokKRiZXx96UWqKNju41q781Uc2F73SHGfHTwUSglm8kW54ZCYGvmTcbxNQlo%2F%2Fqzipq2o8L3Mj3uAbdzHXSMscwI%2FwU%2Fiy8WmXq26kjTvQkM6m5KootrIced0awsfQblBie1md4RvNPOHd7NBrOExQRrQG4tEJoVZ%2FISIA9GVG5z%2BAFTCKzvfJBjqkAX0SsVVzMrDzHjHs29YMrcjl0Npafy1ttSwdXIRx20MS5CWOdS9BWWIJiEoFSppDSXxagw0CzEoJuNOgTd0RBObTfadUeUGyKMjMJFxcxHJoJZ5M0KMw1HsSiGCJIlWWjKfZ%2B1UfHft3Kf2N6pWWycOWY3s%2F900Rn50Jb2dIs%2F7hFhH0blfjJwPEP76Azy2xtZfvgt2mYqm2YHwJslMcLwYvOcPO&X-Amz-Signature=d112287bc2ec66eaac86a245aaa7b045bbfd6baac77ac7907f47c2e47f36b192&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
pd.merge(df_1, df_2, how='inner', left_index=True, right_index=True)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d262f978-a18e-4296-a813-c33347c27d56/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632M27HJ5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQC%2FRSKG19mrdCxziRe%2Ff9VFwOpEVxYUNZqttS6baYacqgIgIq9%2BkJ4fnkx3N2%2BPcZftJfvmYt3Ux%2FvSN4KKtaxRdo4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDH7WZcaG4w6DaZYYqSrcA92YXOoc9H6j8MWXeF8fB4aiyqzZiOozHmaYgdoagXt3S2mxgih6nUC0bCirWi%2FnDv6PovgBsxExXDMzQKTDch9v34nB6MByBvx779TtVuBvphObDtDwd1AZq11mt45duTKxEikls2mKYdwdSMoEylawtpzo49npnZkLau%2FADPQ9HuCmszemHElLONjDMHdSYn0gNwdpe%2FTntdfIxraZ%2BMOj%2FNKJq7snAeCqmoVu06Rzyft5B0bgOpGW7R2D%2BSo4H1QPN%2B4FH1xtPKOYCHMgFFbedimegAsnY5QIRK14tuXnw7ppOelDkMDajRb15iXHS62xU%2BwaC6lLue3qDSOLaJHQuLfALYu2jayQmIS3RKuZgj8YQaYy1o%2Fr6SwVatEX14BZwDP3k1fXH0Xao4r%2Bxr5cJoaDzUiGAw3N%2BGcSlMSaLPceU7sxqoanZWSXhUQyE%2FIagrYElGNB4uUUKZAfTSPdAlbMuntT36lAhz3Cq%2FU0Z9UFxNpFxhqzzekLSVGWh9wbbGibg1qTDT29tDdzgJFHRqC%2F09xF7Zrf7HUUhEwnO37eaJTIOGbOgLSkiiIWCH%2F8mPS7rI%2F0enwZjjfFES2DQvaBfu4rVy8RjysV5StyccaxFJ%2B%2F%2FrnOSkgpMIPO98kGOqUBNxFeZ7r%2BSn8lTFw6cKUGuLVdyzjdnKnepd42kvpKophEE%2FIykrUuSyCICf9p%2Fc0xs2kZlsl54QDYwjQa0WGK5e82mofXLjLhLEErN0DhAMu7CNhW8Ncgef9GxGFVzjYJ%2FSET4Q3bFXZf0KMmmwXqQD79hlDFeHGcjVZxMFs4zeLLpLnRJoleiXdovqvYPDqI6r72QAEpRndTDu5gD3ljoXRk%2FcYh&X-Amz-Signature=4ace2334fc38df0ca2003834e0cfb6904b1d26a77765342495875fd799aed86a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
pd.merge(df_1, df_2, how='left', left_index=True, right_index=True)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6cc540cc-de55-4b1d-877f-c5c27aecff43/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PBSOHD6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2B38rR60loA9%2FuiOfcxGTBbIAB%2F9%2FY4QEJKsWE9bfj8QIhAINoT%2BqzwHb0Sp0y6hS%2BJ%2BEXbeLLMHWaXyT2NtIP2iiTKv8DCCcQABoMNjM3NDIzMTgzODA1IgyqK7MoSrrJb%2Bsy1MAq3AN6CtXVmo6BFaR2cnqyvPRnCp%2BmFTaRFYQ5d%2FD8HdttCMtYDKW6gyCTeh5od0oudSMU1%2BCIIraCI5Kl3ImMnVazUKysZmoOlLXBD30Vwg2z%2BRDpjKHsuinRTvo0aZcJORo7ANVAib7mf%2BneXs8MAk34KyRBSQaL0ZhVFLTnQQmV6k1So1MwQ0X%2BS30bJc4LGFvuiYjnxc60S60BsfQb0KJIYXbHXnx4nWrttcgSTpskq5fZgN4XZs2vc4uMP3GgauagAL2EfyCQaN%2BZqFRkznotcwkdBNZ0bZmW%2FPmtcSk3kzlczGeiJgr3SQkXbM9RmrpvWgzmqbd45o3ntQ1D0PpYQpaJ4lyIe96KTUnZ1TnFsMgzWHNyAeHyNMBGSLLTBqhmzNjI0KFuQ7xytiXFrUqkhTmXBsTjrKmh6VW0cAB7AR8ecNpZHLSPD%2B92aUdseTeuHXKzTCDOQ%2FO7pL4gbu4ySVv5nGjQqq4SdtFuWLbh9BukpVIPyOdUSwcDnFndBs0ovG3WgqPcITZE37r38Nx2d1MWg2bpA%2BCDvadGFTbR8wfAl6eOxHTrv%2BgE2rRwN2pyDkkH%2FcGDoy5%2BCNlDoNvLjW%2FF9BMarjAkNB9eeJe1U8oxTl%2B80yT%2FSnUWOTCKzvfJBjqkAZnnTJXo%2B9LU%2F4dd8xAq0fuG4o3gJ19NbLYJKHnmUpTHeZ0Eku30mceWT5358WM582xYw52wYM%2BzgRsraUXoQxg9uv4CnvfqXcai2sZuHXGso8Rxs3GRGnRQ7uGClZaZV458f5tE%2FHd6cxl0ED%2B%2B13rFjk7vjkHBDDtKFB%2BVbQxxI3aJd6tFBCVdbW6e9UhxHKjPDgOs9nQRE4o9q90QtTdBDB0P&X-Amz-Signature=fc3b4dee9989319beae0e12f1b0dc1d6f63ca3f023ff6f38c68fb53024802020&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
pd.merge(df_1, df_2, how='outer', left_index=True, right_index=True)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4ae29da2-7977-439d-ab2d-7205c92b2709/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZ7K5J63%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIG%2FPBgGST9byyrmpCcn4pZnz5LU3NW3qixdWu0DizOCiAiB3hAI5dHSTidhPIYi11npOry8WVQ7uj0RDfcl%2BUt5IYyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM08zDce2PMWVU9tbcKtwDkWdXZUorpKetoqPJ9EwiyDTZbK04IvKKx7yTRUiDsYg%2BGoVr%2BJYeTRhgQoxGPTmZldGjZWmmUG%2BBMwocSjz5Dc29Vcb5PKUwsbWw1d7sWHccPcr6rpzRyNzyXNocYBIC5Zn%2BvgkDerYOVapfACVe64jM4gQ1GhVed60h7RLldkCpkPbK9bZWc7%2FxhSdVAb7O6sSQxTtoANpDL7QWYgltPrlJkqwJko6Z1z%2B2PgWmTauFTE44pvfi6nNbZ%2FTwySdH63FVmHRFThUK7XGAHfj2ujdOVtXNiAXIn7meuEoBpKAKHMB9yIZOGep1rApSxTwWiIZBTH5IMen2lw3SrQeRARRpLt5J9055d%2Bmld6A1sDtdLwxZLXP04IFYCdpiKdyae1nGX5j0mNNct2PbKxLP3YieRl9dzUy4RIrPRz9gfU9%2F4V03CvegMhJuY1zhbt5hOYBc3VzKeS066B90dspNC5Ly4uQnJr4tEskdY%2Bl4r5W8gSk2%2BC%2BjX%2FQthEHnUEkmR%2Bg9S%2BAn7vZSV8kTnzHXR9Tw128fbqxhZJMPz%2FpsCtlleWu3MIXC%2FyeDeeS1nQbtJ%2F2gfZM6vvA5HgFAk51xCGo20D6Xf4F3N0MxnBsEa6f0rJjXkhfB0t6wU1Uw8s33yQY6pgHOGTs%2B%2FWoFHHn5TXGGTHwOkSZTIslZ8J%2B7vmj9GNU7x69VDy3mYPiW2XOaYspiRfNSeHulmwmckh3PAYCMoes2P6fYQLRudeegcqOzALcYwgEF7XkB7UsPYGHkuP80jBC4%2BhiY7NlfPFmrkv2S3ADjjT%2FtReb4L1Qcl2RegwLZx7OnA73Rr2TanGLn4C6LV5p8HKJB%2FnDrHO%2B6Ibk7rkWCzBXBJ8Mi&X-Amz-Signature=de559947b6b6eed9ffb4140a7ebf417fa19db69d95d5eff071d652260c835ff6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
```python
pd.merge(df_1, df_2, how='right', left_index=True, right_index=True)
```
<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e6aeec1c-4904-4224-b35e-a2a08d34d259/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625UDBNWF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T223755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCrNRaGsBehb%2B9h2RKMIt5IhYx0fXAQWC6sVQboRgWRxgIhAKruoqZlH8JTmVduMOVE31%2BDYp%2FI%2F6G7ZNOTEDMSd05%2BKv8DCCcQABoMNjM3NDIzMTgzODA1IgxQROAAVe1CzgtLK1sq3AMIMhtvZlLzHMINLcRYaXwBigxA2o4QB0lhnDqca%2F%2Fx0vUAaqRJZWkWcVk1kkLyZebnFdympto3z9hF7TojxNhAuLHfH1n6etnyB9I4GRzwih0JS1jEC2QfPTCZyWlNPzKrYTGex%2B48sBoISRBx7lkETPHBQs0JBiaee9BUd2BFPLBubYFyifr1HulVlhFVXpKM06JvLskyJYlkkvjNBhf00YhFeQ%2BRP1dDnwEce5JTZk%2FJgYbNd5VLJOtvjxksNhOUt015tBPPIJ88RQg%2BjyFAwx%2FycVfUgEBrG9R%2Fw6EugOU6cr%2B9PDx5cEmRBGCVNheXDC9eFH1T5%2BXwygG5V1wnVDSfdqoytOHaafRUAUjfT6Z6Wc9OqPmiJWKn92LNjcshX8oJz55LwTe54vMkIonFeQF41Dvvlo9u1yg%2FZPrm%2FdOzjsRSHXffxZVlkZjPTfoUzZ8JU8GfSyYGP2%2BL7oiqFi2BUlgzEqyloUoz6G%2B5wF7vp3T79jHxkMUacSbCZqnlfR0fLY%2FYpgkLCLTbgwv926qFQK%2FQRl1loJhLIkMnUpWN8MA8kSqT2BZgpierrKGzvcUtlOem4CbodxFfMIEsjaAEwrspovGumuGWKDIB1OI36v5UHrW%2F75NXcDDnzffJBjqkATzR%2B%2BoJ6sj5cfX390Q9aTAq31u25hEOp6zWNutrGYCtyp45vPl07GK1SNK015DdpW8pox4d2RrLpOmwJSR5HZtb0M5CKFlcZxXSzsQEiU2gxR2KRpX01fmOeS2IU9UbwUVQ5TdZyTqW6Qz0vTDDcjJamaMPiLjDf0DwcDPaenA4N0Ch9QXaWvywb5Rb5R7eCVBmVaMhx9EIt9BC%2BV0Gbgy3cWoU&X-Amz-Signature=8fec899fc9a2f1d1ff548268eb17d5b5185dd42dd05c9d901ae4b04fd5c07bc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---

---
📄 **[Pen & paper coding]** (subpage)
📄 **[Loops]** (subpage)
## Question 1 - For loop
Write a Python function called `sum_even_numbers` that takes a list of integers as an argument. The function should use a `for` loop to iterate through the list, find all even numbers, and return the sum of all the even numbers. If the list is empty or there are no even numbers, the function should return 0.

<details>
<summary>Solution</summary>

```python
def sum_even_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**: We define a function called `sum_even_numbers` which takes a single parameter `numbers` (a list of integers).
1. **Initialize Total**: We initialize a variable `total` to 0. This variable will be used to accumulate the sum of even numbers.
1. **For Loop**: We use a `for` loop to iterate over each `number` in the `numbers` list.
1. **Check Even Number**: Inside the loop, we use an `if` statement to check if the current `number` is even by using the modulus operator (`%`). If `number % 2 == 0` is true, it means the number is even.
1. **Add to Total**: If the current `number` is even, we add it to the `total` using `total += number`.
1. **Return Total**: After the loop has iterated through all the numbers in the list, we return the `total`, which now holds the sum of all even numbers. If there were no even numbers or the list was empty, `total` remains 0.
</details>
</details>
---
## Question 2 - For loop
Write a Python program that processes a list of positive integers and performs the following operations by using for-loops:
1. Create a list of squares of the integers in the original list.
1. Filter the original list to include only even numbers.
1. Calculate the sum of all integers in the original list.
1. Print the results of each operation.
Use a `for` loop to achieve each of these tasks. Provide the Python code and a brief explanation of how your code works.

<details>
<summary>Solution</summary>

```python
# Original list of positive integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Create a list of squares of the integers in the original list
squares = []
for number in numbers:
    squares.append(number ** 2)

# 2. Filter the original list to include only even numbers
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

# 3. Calculate the sum of all integers in the original list
total_sum = 0
for number in numbers:
    total_sum += number

# 4. Print the results of each operation
print("Original list:", numbers)
print("List of squares:", squares)
print("List of even numbers:", evens)
print("Sum of all integers:", total_sum)
```
<details>
<summary>Line-by-line explanation</summary>

1. **Initialize the List**: We start by defining a list of positive integers called `numbers`.
1. **Create List of Squares**:
- **Initialize an Empty List**: We create an empty list `squares` to store the square of each integer from the original list.
- **For Loop to Compute Squares**: The `for` loop iterates through each integer in the `numbers` list. In each iteration, the square of the current integer (`number ** 2`) is computed and appended to the `squares` list.
1. **Filter Even Numbers**:
- **Initialize an Empty List**: We create an empty list `evens` to store the even integers from the original list.
- **For Loop to Filter Evens**: The `for` loop iterates through each integer in the `numbers` list. If the integer is even (`number % 2 == 0`), it is appended to the `evens` list.
1. **Calculate Sum of Integers**:
- **Initialize Sum Variable**: We initialize a variable `total_sum` to 0.
- **For Loop to Calculate Sum**: The `for` loop iterates through each integer in the `numbers` list. In each iteration, the current integer (`number`) is added to `total_sum`.
1. **Print Results**: Finally, we print the original list of numbers, the list of squares, the list of even numbers, and the sum of all integers using the `print` function.
</details>
---


</details>
---
## Question 3 - Nested for loops
Write a Python program that prints a pattern of numbers in the form of a right-angled triangle. The number of rows in the triangle should be specified by a variable `n`. Each row should contain the row number repeated that many times. For example, if `n = 4`, the output should be:
```plain text
1
22
333
4444
```

<details>
<summary>Solution</summary>

```python
n = 4  # You can change this value to print more or fewer rows

for i in range(1, n+1):
    for j in range(i):
        print(i, end="")
    print()
```
<details>
<summary>Line-by-line explanation</summary>

1. **Variable Initialization (****`n = 4`****)**: Initializes the number of rows (`n`) in the triangle. In this case, it's set to 4. You can change this value to print more or fewer rows.
1. **Outer Loop for Rows (****`for i in range(1, n+1)`****)**: Starts a loop that runs from `1` to `n` (inclusive). The outer loop controls the number of rows.
1. **Inner Loop for Columns (****`for j in range(i)`****)**: Starts another loop inside the outer loop, which runs from `0` to `i-1`. The inner loop controls the number of times a number is printed in each row.
1. **Print Current Row Number (****`print(i, end="")`****)**: Prints the current row number (`i`), but stays on the same line due to the `end=""` argument which prevents the print function from moving to a new line.
1. **Move to Next Line (****`print()`****)**: Moves the cursor to the next line after finishing the inner loop. This ensures that the next row of numbers starts on a new line.
This solution uses nested loops to build the desired number pattern. The outer loop handles each row, and the inner loop handles the number of times each number is printed in its respective row.
</details>
</details>
---
## Question 4 - For loop
Write a Python function named `even_numbers_up_to_n` that takes a single integer `n` as its parameter. The function should iterate through numbers from 1 to `n`, and:
1. If the current number is odd, skip it and continue to the next number.
1. If the current number is even, print it.
Use the `continue` statement inside a `for` loop to achieve this.
For example, if you call the function as follows:
```python
even_numbers_up_to_n(10)
```
The output should be:
```plain text
2
4
6
8
10
```
<details>
<summary>Solution</summary>

```python
def even_numbers_up_to_n(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            continue
        print(i)
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def even_numbers_up_to_n(n):
```
This line defines a function named `even_numbers_up_to_n` which takes an integer `n` as its parameter.
1. **For Loop**:
```python
for i in range(1, n + 1):
```
This line begins a `for` loop that iterates `i` from 1 to `n` inclusive.
1. **If Condition to Check Odd Numbers**:
```python
if i % 2 != 0:
```
This line checks if the current number `i` is odd (i.e., the remainder when `i` is divided by 2 is not zero).
1. **Continue Statement**:
```python
continue
```
If the condition in the previous line is true (i.e., the number is odd), this `continue` statement will skip the rest of the code inside the loop and jump to the next iteration.
1. **Print Even Number**:
```python
print(i)
```
If the number `i` is not odd (i.e., it is even), this line will print the number.
</details>
</details>
---
## Question 5 - While loop
Create a Python function named `guess_the_number` that implements a simple guessing game using a `while` loop. The game should have the following features:
1. Use the `random` module to generate a random integer between 1 and 100.
1. Prompt the user to guess the number.
1. If the user's guess is too high, print "Too high!".
1. If the user's guess is too low, print "Too low!".
1. The loop should continue until the user guesses the correct number.
1. Once the correct number is guessed, print "Congratulations. You've guessed the correct number."

<details>
<summary>Solution</summary>

```python
import random

def guess_the_number():
  
    secret_number = random.randint(1, 100)
    guess = None

    while guess != secret_number:
        guess = int(input("Enter your guess (between 1 and 100): "))
        
        if guess > secret_number:
            print("Too high!")
            
        elif guess < secret_number:
            print("Too low!")
            
    print("Congratulations. You've guessed the correct number.")

```
<details>
<summary>Line-by-line explanation</summary>

1. **Import the ****`random`**** module**: This module is used to generate random numbers.
1. **Function Definition**: We define a function named `guess_the_number`.
1. **Generate a Random Number**: `random.randint(1, 100)` generates a random integer between 1 and 100, inclusive, which is stored in `secret_number`.
1. **Initialize Variable**: We initialize `guess` to `None` so that it can be used in the `while` loop condition.
1. **`while`**** Loop Begins**: The loop runs as long as the user's guess is not equal to `secret_number`.
1. **Get User Input**: `input()` prompts the user to enter a guess, which is then converted to an integer and stored in `guess`.
1. **Check if Guess is Too High**: If the guess is greater than `secret_number`, print "Too high!".
1. **Check if Guess is Too Low**: If the guess is less than `secret_number`, print "Too low!".
1. **Correct Guess**: When the loop exits, it means the user's guess matches `secret_number`. Print a congratulatory message to the user.
</details>
</details>
---
## Question 6 - While loop
Write a Python function called `sum_of_evens` that calculates the sum of all even numbers from 1 to a given positive integer `n` (inclusive). Use a while loop to accomplish this task. 
For example, if you call the function as follow:
```python
sum_of_evens(10)
```
The function should return **30 **(2 + 4 + 6 + 8 + 10).

<details>
<summary>Solution</summary>

```python
def sum_of_evens(n):
    total_sum = 0
    current_number = 1

    while current_number <= n:
        if current_number % 2 == 0:
            total_sum += current_number
        current_number += 1

    return total_sum


```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**: We define a function `sum_of_evens` that takes one parameter `n`.
1. **Initialize ****`total_sum`**: We initialize a variable `total_sum` to 0. This will hold the sum of all even numbers.
1. **Initialize ****`current_number`**: We initialize a variable `current_number` to 1. This is the current number we are checking in the loop.
1. **While Loop**: We start a while loop that runs as long as `current_number` is less than or equal to `n`.
1. **Check Even**: Inside the loop, we check if `current_number` is even using the modulus operator (`%`).
1. **Add to Sum**: If `current_number` is even, we add it to `total_sum`.
1. **Increment**: We increment `current_number` by 1 to move to the next number.
1. **Return**: After the loop ends, we return the `total_sum`, which now contains the sum of all even numbers from 1 to `n`.
</details>
</details>
---
## Question 7 - For loop with range function
Write a Python function named `print_square_of_numbers` that takes a single integer `n` as its parameter. The function should iterate through numbers from 1 to `n`, and for each number:
1. Compute its square.
1. Print the square.
Use the `for` loop and the `range` function to iterate over the numbers.
For example, if you call the function as follows:
```python
print_square_of_numbers(5)
```
The output should be:
```plain text
1
4
9
16
25
```
<details>
<summary>Solution</summary>

```python
def print_square_of_numbers(n):
    for i in range(1, n + 1):
        print(i ** 2)
```
<details>
<summary>Explanation</summary>

1. **Function Definition**:
```python
def print_square_of_numbers(n):
```
This line defines a function named `print_square_of_numbers` which takes an integer `n` as its parameter.
1. **For Loop**:
```python
for i in range(1, n + 1):
```
This line begins a `for` loop that iterates `i` from 1 to `n` inclusive.
1. **Print Square of the Number**:
```python
print(i ** 2)
```
This line computes the square of the current number `i` using the exponentiation operator `**` and prints the result.
</details>
</details>
---
## Question 8 - For loop with range function
Write a Python function named `sum_of_squares_up_to_n` that takes a single integer `n` as its parameter. The function should calculate the sum of the squares of all integers from 1 to `n` (inclusive) and return the result.
For example, if you call the function as follows:
```python
print(sum_of_squares_up_to_n(4))
```
The output should be:
```plain text
30
```
Explanation: 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30

<details>
<summary>Solution</summary>

```python
def sum_of_squares_up_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total
```
<details>
<summary>Explanation</summary>

1. **Function Definition**:
```python
def sum_of_squares_up_to_n(n):
```
This line defines a function named `sum_of_squares_up_to_n` which takes an integer `n` as its parameter.
1. **Initialize Total Variable**:
```python
total = 0
```
This line initializes a variable named `total` to zero. This variable will be used to accumulate the sum of the squares.
1. **For Loop**:
```python
for i in range(1, n + 1):
```
This line begins a `for` loop that iterates `i` from 1 to `n` inclusive using the `range` function.
1. **Update Total**:
```python
total += i ** 2
```
Inside the loop, this line updates the `total` by adding the square of the current number `i`. The `**` operator is used for exponentiation (raising to a power).
1. **Return Result**:
```python
return total
```
After the loop completes, this line returns the accumulated sum of the squares stored in `total`.
</details>
</details>
---

📄 **[Math operations]** (subpage)
## Question 1 - Modulo operator
Create a Python function `mod_div` that uses the modulo operator to determine divisibility and prints a custom message for each case. The function should:
1. Take two arguments, an integer `num` and an integer `divisor`.
1. Use the modulo operator to check if `num` is divisible by `divisor`.
1. Print "num is divisible by divisor" if `num` is divisible by `divisor`.
1. Print "num is not divisible by divisor" if `num` is not divisible by `divisor`.
Write the definition of the function and some example calls to the function for values `num = 10` and `divisor = 2`, as well as `num = 10` and `divisor = 3`.
For example, calling the function as mod_div(20, 5) should print “*20 is divisible by 5”.*
<details>
<summary>Solution</summary>

```python
def mod_div(num, divisor):
    if num % divisor == 0:
        print(f"{num} is divisible by {divisor}")
    else:
        print(f"{num} is not divisible by {divisor}")

# Example calls to the function:
mod_div(10, 2)
mod_div(10, 3)
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition (****`def mod_div(num, divisor):`****)**: Define a function named `mod_div` that takes two parameters, `num` and `divisor`.
1. **Modulo Check** (`if num % divisor == 0:`): Use the modulo operator `%` to check if the remainder of `num` divided by `divisor` is zero. This determines if `num` is divisible by `divisor`.
1. **Print Statement for Divisibility** (`print(f"{num} is divisible by {divisor}")`): If the above condition is true, print a message indicating that `num` is divisible by `divisor`.
1. **Else Statement** (`else:`): If the modulo operation does not yield zero, the control goes to the else block.
1. **Print Statement for Non-Divisibility** (`print(f"{num} is not divisible by {divisor}")`): In the else block, print a message indicating that `num` is not divisible by `divisor`.
1. **Example Call 1** (`mod_div(10, 2)`): Call the function with `num = 10` and `divisor = 2`. This should print "10 is divisible by 2".
1. **Example Call 2** (`mod_div(10, 3)`): Call the function with `num = 10` and `divisor = 3`. This should print "10 is not divisible by 3".
</details>
</details>
---
## Question 2 - floor division
Write a Python function named `floor_division_pairs` that takes two lists of integers `list1` and `list2` as parameters. The function should iterate through each pair of elements (one from each list at the same index) and perform a floor division of the elements. Specifically, for each index `i`, compute `list1[i] // list2[i]`, and store the result in a new list called `result`. Finally, return the `result` list.
Ensure the lengths of the two lists are equal. If not, print an error message saying "The lists must have the same length."
For example, if you call the function as follows:
```python
floor_division_pairs([10, 20, 30], [3, 4, 5])
```
The return value should be:
```plain text
[3, 5, 6]
```
<details>
<summary>Solution</summary>

```python
def floor_division_pairs(list1, list2):
    if len(list1) != len(list2):
        print("The lists must have the same length.")
        return None

    result = []
    for i in range(len(list1)):
        result.append(list1[i] // list2[i])

    return result
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def floor_division_pairs(list1, list2):
```
This line defines a function named `floor_division_pairs` which takes two lists `list1` and `list2` as its parameters.
1. **Length Check**:
```python
if len(list1) != len(list2):
```
This line checks if the lengths of `list1` and `list2` are not equal.
1. **Error Message and Return**:
```python
print("The lists must have the same length.")
return None
```
If the lengths are not equal, an error message is printed and the function returns `None`.
1. **Result List Initialization**:
```python
result = []
```
This line initializes an empty list `result` which will store the results of the floor divisions.
1. **For Loop**:
```python
for i in range(len(list1)):
```
This line begins a `for` loop that iterates through the indices of the lists.
1. **Floor Division and Append**:
```python
result.append(list1[i] // list2[i])
```
This line performs the floor division of the elements from `list1` and `list2` at index `i`, then appends the result to the `result` list.
1. **Return Result**:
```python
return result
```
Finally, this line returns the `result` list that contains the floor division results of pairs of elements from the input lists.
</details>
</details>
---


📄 **[Functions]** (subpage)
## Question 1 - Optional parameters
Write a Python function named `greet` that takes a name as a required parameter and a greeting message as an optional parameter. The optional greeting message should have a default value of `"Hello"`. The function should print a greeting message in the format: `"message, name!"`.
For example:
1. Calling `greet("John")` should print:
```plain text
Hello, John!
```
1. Calling `greet("John", "Good morning")` should print:
```plain text
Good morning, John!
```

<details>
<summary>Solution</summary>

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition with Parameters**:
```python
def greet(name, message="Hello"):

```
This line defines a function named `greet` which takes two parameters: `name` (required) and `message` (optional with a default value "Hello").
1. **Print Statement with Formatted String**:
```python
print(f"{message}, {name}!")

```
This line prints the greeting message by using an f-string to include the `message` and `name` parameters in the format `"message, name!"`. For example, if the name is `"John"` and the message is `"Good morning"`, it prints `"Good morning, John!"`. If the message is not provided when the function is called, it uses the default value `"Hello"`.
</details>
</details>
---
## Question 2 - Optional parameters
Write a Python function named `introduction` that introduces a person. This function should have two parameters: `name` and `age`. The `age` parameter should be optional and have a default value of `None`.
The function should print a different message depending on whether the `age` parameter is provided:
1. If `age` is provided, it should print: `"Hello, my name is <name> and I am <age> years old."`
1. If `age` is not provided, it should print: `"Hello, my name is <name>."`
For example:
1. Calling `introduction("Alice", 30)` should print: 
```plain text
Hello, my name is Alice and I am 30 years old.
```
- Calling `introduction("Bob")` should print: 
```plain text
Hello, my name is Bob.
```

<details>
<summary>Solution</summary>

```python
def introduction(name, age=None):
    if age is not None:
        print(f"Hello, my name is {name} and I am {age} years old.")
    else:
        print(f"Hello, my name is {name}.")
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition:**
```python
def introduction(name, age=None):
```
This line defines a function named `introduction` that takes two parameters `name` and `age`. The `age` parameter has a default value of `None`.
1. **If Condition to Check if Age is Provided:**
```python
if age is not None:
```
This line checks whether the `age` parameter has been provided (i.e., it is not `None`).
1. **Print Message with Age:**
```python
print(f"Hello, my name is {name} and I am {age} years old.")
```
If the `age` parameter is provided, this line executes and prints the message with the person's age included.
1. **Else Block for When Age is Not Provided:**
```python
else:
```
This line starts the `else` block which runs if `age` is `None`.
1. **Print Message without Age:**
```python
print(f"Hello, my name is {name}.")
```
If the `age` parameter is not provided, this line executes and prints the message without including the age.
</details>
</details>
---
## Question 3 - map()
Write a Python function named `square_numbers` that uses the `map()` function to apply a provided function to each element in a list. The `square_numbers` function should:
1. Take a list of integers, `numbers`, as its only parameter.
1. Use the `map()` function to square each number in the `numbers` list.
1. Return the resulting list of squared numbers.
For example, if you call the function as follows:
```python
square_numbers([1, 2, 3, 4, 5])
```
The output should be:
```plain text
[1, 4, 9, 16, 25]
```

<details>
<summary>Solution</summary>

```python
def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def square_numbers(numbers):

```
This line defines a function named `square_numbers` which takes a single parameter, `numbers`, that is expected to be a list of integers.
1. **map() Function with Lambda**:
```python
return list(map(lambda x: x ** 2, numbers))

```
- **map() Function**: The `map` function takes two arguments: a function and a sequence (in this case, the list `numbers`). It applies the provided function to each item in the sequence.
- **Lambda Function**: The lambda function `lambda x: x ** 2` takes one argument `x` and returns `x` squared.
- **Conversion to List**: The `map` function returns an iterator, so we use `list()` to convert the iterator into a list of squared numbers.
- **Return Statement**: Finally, the resulting list is returned by the `square_numbers` function.
</details>
</details>
---
## Question 4 - filter()
Write a Python function named `filter_odd_numbers` that takes a list of integers as its parameter, and returns a new list containing only the odd numbers from the original list. Use the `filter()` function to achieve this.
For example, if you call the function as follows:
```python
filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```
The output should be:
```plain text
[1, 3, 5, 7, 9]
```

<details>
<summary>Solution</summary>

```python
def filter_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def filter_odd_numbers(numbers):
```
This line defines a function named `filter_odd_numbers` which takes a list of integers `numbers` as its parameter.
1. **Filter Function with Lambda**:
```python
return list(filter(lambda x: x % 2 != 0, numbers))
```
- `filter(lambda x: x % 2 != 0, numbers)`:
- `lambda x: x % 2 != 0`: This is a lambda function that takes an integer `x` and returns `True` if `x` is odd (i.e., when the remainder when `x` is divided by 2 is not zero).
- `filter(...)`: This function applies the lambda function to each element in the `numbers` list and filters out the elements that do not satisfy the condition (i.e., the even numbers).
- `list(...)`: This converts the result from the `filter` function (which is a filter object) back into a list.
- `return`: This returns the filtered list containing only the odd numbers.
</details>
</details>
---
## Question 5 - filter()
Write a Python function named `filter_strings_with_a` that takes a list of strings as its parameter. The function should use the `filter()` function to create a new list that contains only the strings from the original list that have the letter 'a' in them. The function should return this new list.
For example, if you call the function as follows:
```python
filter_strings_with_a(["apple", "banana", "cherry", "date", "fig"])
```
The output should be:
```plain text
['apple', 'banana', 'date']
```

<details>
<summary>Solution</summary>

```python
def filter_strings_with_a(strings):
    def has_a(string):
        return 'a' in string

    result = list(filter(has_a, strings))
    return result
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def filter_strings_with_a(strings):
```
This line defines a function named `filter_strings_with_a` which takes a single parameter `strings`, expected to be a list of strings.
1. **Helper Function Definition**:
```python
def has_a(string):
    return 'a' in string
```
This line defines a helper function `has_a` which will check if the given string contains the letter 'a'. The `in` operator is used for this purpose.
1. **Using ****`filter`**** Function**:
```python
result = list(filter(has_a, strings))
```
This line uses the `filter` function to apply the `has_a` function to each item in the `strings` list. The `filter` function returns an iterator of the items for which the `has_a` function returns `True`. The `list()` function is then used to convert this iterator into a list.
1. **Return the Result**:
```python
return result
```
This line returns the new list containing only the strings that have the letter 'a' in them.
</details>
</details>
---
## Question 6 - reduce()
Write a Python function called `product_of_list` that takes a list of integers as its only parameter. The function should use the `reduce()` function from the `functools` module to compute the product of all the numbers in the list.
Here's what the function should do:
1. Import the `reduce` function from the `functools` module.
1. Define the `product_of_list` function.
1. Use the `reduce()` function to multiply all the integers in the list together.
1. Return the final product.
For example, calling the function as follows:
```python
product_of_list([1, 2, 3, 4])
```
Should return:
```plain text
24
```

<details>
<summary>Solution</summary>

```python
from functools import reduce

def product_of_list(numbers):
    return reduce(lambda x, y: x * y, numbers)
```
<details>
<summary>Line-by-line explanation</summary>

1. **Import reduce**:
```python
from functools import reduce
```
This line imports the `reduce` function from the `functools` module, which allows us to apply a specific function (in this case, multiplication) cumulatively to the items in the list.
1. **Function Definition**:
```python
def product_of_list(numbers):
```
This defines a function named `product_of_list` that takes one parameter `numbers`, which is expected to be a list of integers.
1. **Using reduce with a Lambda Function**:
```python
return reduce(lambda x, y: x * y, numbers)
```
This line uses the `reduce` function to multiply all the numbers in the list. The `reduce` function takes two arguments: a function and a sequence. Here, the function is a lambda function, `lambda x, y: x * y`, which takes two arguments and returns their product. The sequence is the list `numbers`.
1. **Return Final Product**:
This line returns the final product obtained after applying the multiplication cumulatively to all the items in the list.
</details>
</details>
---
## Question 7 - reduce()
Write a Python function named `sum_of_squares` that takes a list of integers as its parameter. The function should use the `reduce()` function from the `functools` module to calculate and return the sum of the squares of the integers in the list.
For example, if you call the function as follows:
```python
sum_of_squares([1, 2, 3, 4])

```
The output should be:
```plain text
30
```

<details>
<summary>Solution</summary>

```python
from functools import reduce

def sum_of_squares(lst):
    return reduce(lambda x, y: x + y**2, lst, 0)

```
<details>
<summary>Explanation</summary>

1. **Import the Required Module**:
```python
from functools import reduce
```
This line imports the `reduce` function from the `functools` module. The `reduce` function is used to apply a function of two arguments cumulatively to the items of a list.
1. **Function Definition**:
```python
def sum_of_squares(lst):
```
This line defines a function named `sum_of_squares` which takes a single parameter `lst`, a list of integers.
1. **Apply ****`reduce`**** with Lambda Function**:
```python
return reduce(lambda x, y: x + y**2, lst, 0)
```
This line uses the `reduce` function with a lambda function as its first argument. The lambda function takes two arguments `x` and `y` and returns the sum of `x` and the square of `y` (`x + y**2`). The `reduce` function applies this lambda cumulatively to the items of the list `lst`, starting with an initial value of 0. In essence, this expression computes the sum of the squares of the integers in the list. The `reduce` function iterates over each element in the list, applies the lambda function, and accumulates the result.
</details>
</details>
---
## Question 8 - map() and filter()
Write a Python function named `square_even_numbers` that takes a list of integers as its parameter. The function should:
1. Use the `filter()` function to filter out all the odd numbers from the list.
1. Use the `map()` function to square each of the remaining even numbers.
1. Return the list of the squared even numbers.
For example, if you call the function as follows:
```python
square_even_numbers([1, 2, 3, 4, 5, 6])
```
The output should be:
```plain text
[4, 16, 36]
```

<details>
<summary>Solution</summary>

```python
def square_even_numbers(numbers):
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squared_even_numbers = map(lambda x: x ** 2, even_numbers)
    return list(squared_even_numbers)
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def square_even_numbers(numbers):
```
This line defines a function named `square_even_numbers` which takes a list of integers as its parameter.
1. **Filter Even Numbers**:
```python
even_numbers = filter(lambda x: x % 2 == 0, numbers)
```
This line uses the `filter()` function to create an iterator that contains only the even numbers from the input list `numbers`. The `lambda` function `lambda x: x % 2 == 0` is used to test whether each number is even.
1. **Map Squaring Function to Even Numbers**:
```python
squared_even_numbers = map(lambda x: x ** 2, even_numbers)
```
This line uses the `map()` function to create an iterator that contains the squares of the even numbers obtained from the `filter()` function. The `lambda` function `lambda x: x ** 2` is used to square each even number.
1. **Convert to List and Return**:
```python
return list(squared_even_numbers)
```
Finally, this line converts the iterator `squared_even_numbers` to a list and returns it.
</details>
</details>
---
## Question 10 - Check datatype
Write a Python function called `classify_elements` that takes a list of mixed data types as its parameter. The function should classify each element in the list and print whether it is an integer, a float, a string, or of some other data type. Use the `isinstance()` function to achieve this.
Here is the function signature:
```python
def classify_elements(mixed_list):
```
For example, if you call the function as follows:
```python
classify_elements([1, 2.0, 'three', [4, 5], (6, 7), {'eight': 8}])
```
The output should be:
```plain text
1 is an integer.
2.0 is a float.
'three' is a string.
[4, 5] is of some other type.
(6, 7) is of some other type.
{'eight': 8} is of some other type.
```

<details>
<summary>Solution </summary>

```python
def classify_elements(mixed_list):
    for element in mixed_list:
        if isinstance(element, int):
            print(f"{element} is an integer.")
        elif isinstance(element, float):
            print(f"{element} is a float.")
        elif isinstance(element, str):
            print(f"'{element}' is a string.")
        else:
            print(f"{element} is of some other type.")
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def classify_elements(mixed_list):
```
This line defines a function named `classify_elements` which takes a list `mixed_list` as its parameter.
1. **For Loop**:
```python
for element in mixed_list:
```
This line begins a `for` loop that iterates over each `element` in the `mixed_list`.
1. **Check if Element is an Integer**:
```python
if isinstance(element, int):
```
This line uses the `isinstance()` function to check if the current `element` is an instance of `int` (an integer).
1. **Print Statement for Integer**:
```python
print(f"{element} is an integer.")
```
If the `element` is an integer, this line will print that the `element` is an integer.
1. **Check if Element is a Float**:
```python
elif isinstance(element, float):
```
This line uses the `isinstance()` function to check if the current `element` is an instance of `float`.
1. **Print Statement for Float**:
```python
print(f"{element} is a float.")
```
If the `element` is a float, this line will print that the `element` is a float.
1. **Check if Element is a String**:
```python
elif isinstance(element, str):
```
This line uses the `isinstance()` function to check if the current `element` is an instance of `str` (a string).
1. **Print Statement for String**:
```python
print(f"'{element}' is a string.")
```
If the `element` is a string, this line will print that the `element` is a string. Notice the single quotes around `{element}` to differentiate it visually as a string.
1. **Print Statement for Other Data Types**:
```python
else:
    print(f"{element} is of some other type.")
```
If the `element` is none of the above types (not an integer, float, or string), this block will execute, printing that the `element` is of some other type.
</details>
</details>
---
📄 **[Logical statements]** (subpage)
## Question 1 - if/elif/else statements
Write a Python function named `check_number` that takes a single integer `x` as its parameter. The function should:
1. Check if `x` is greater than zero.
- If it is, print "Positive".
1. Otherwise, check if `x` is less than zero.
- If it is, print "Negative".
1. If `x` is neither greater than zero nor less than zero, then it must be zero, so print "Zero".
For example, if you call the function as follows:
```python
check_number(5)
check_number(-3)
check_number(0)
```
The output should be:
```plain text
Positive
Negative
Zero
```
<details>
<summary>Solution</summary>

```python
def check_number(x):
    if x > 0:
        print("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def check_number(x):
```
This line defines a function named `check_number` which takes an integer `x` as its parameter.
1. **First If Condition to Check if Positive**:
```python
if x > 0:
```
This line checks if `x` is greater than zero.
1. **Print Statement for Positive Number**:
```python
print("Positive")
```
If the condition in the previous line is true (i.e., `x` is greater than zero), this line will print "Positive".
1. **Elif Condition to Check if Negative**:
```python
elif x < 0:
```
This line checks if `x` is less than zero, executed if the first `if` condition is false.
1. **Print Statement for Negative Number**:
```python
print("Negative")
```
If the condition in the previous line is true (i.e., `x` is less than zero), this line will print "Negative".
1. **Else Clause for Zero**:
```python
else:
```
If neither of the above conditions are true (i.e., `x` is not greater than zero and not less than zero), this else clause will be executed.
1. **Print Statement for Zero**:
```python
print("Zero")
```
Since `x` is neither greater than zero nor less than zero, this line will print "Zero".
</details>
</details>
---
## Question 2 - if/elif/else statements
Write a Python function named `temperature_check` that takes a single parameter `temp` (an integer), which represents the temperature in degrees Celsius. The function should:
1. Print "It's cold!" if the temperature is below 15 degrees.
1. Print "It's nice!" if the temperature is between 15 and 25 degrees (inclusive).
1. Print "It's hot!" if the temperature is above 25 degrees.
For example, if you call the function as follows:
```python
temperature_check(10)
```
The output should be:
```plain text
It's cold!
```
<details>
<summary>Solution</summary>

```python
def temperature_check(temp):
    if temp < 15:
        print("It's cold!")
    elif 15 <= temp <= 25:
        print("It's nice!")
    else:
        print("It's hot!")
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def temperature_check(temp):
```
This line defines a function named `temperature_check` which accepts one parameter `temp`, representing the temperature in degrees Celsius.
1. **First If Statement (Check for Cold Temperature)**:
```python
if temp < 15:
```
This line checks if the temperature `temp` is below 15 degrees Celsius.
1. **Print for Cold Temperature**:
```python
print("It's cold!")
```
If the temperature is below 15 degrees, this line will print "It's cold!" to indicate it.
1. **Elif Statement (Check for Nice Temperature)**:
```python
elif 15 <= temp <= 25:
```
This line checks if the temperature `temp` falls between 15 and 25 degrees Celsius, inclusive.
1. **Print for Nice Temperature**:
```python
print("It's nice!")
```
If the temperature is between 15 and 25 degrees, this line will print "It's nice!" to indicate it.
1. **Else Statement (Check for Hot Temperature)**:
```python
else:
```
This line is executed if none of the previous conditions (below 15 or between 15 and 25) are true, which means the temperature is above 25 degrees Celsius.
1. **Print for Hot Temperature**:
```python
print("It's hot!")
```
If the temperature is above 25 degrees, this line will print "It's hot!" to indicate it.
</details>
</details>
---
## Question 3 - Complex boolean expressions
Write a Python function named `classify_person` that takes three parameters: `age` (an integer), `is_student` (a boolean), and `income` (a float representing annual income in dollars). The function should classify the person into one of the following categories and print out the category based on the provided criteria:
1. "Minor": If the person is younger than 18 years old.
1. "Adult Student": If the person is 18 years old or older, is a student, and their income is less than $20,000.
1. "Low Income Adult": If the person is 18 years old or older, is not a student, and their income is less than $20,000.
1. "High Income Adult": If the person is 18 years old or older and their income is $20,000 or more, regardless of student status.
You should use a combination of `if`, `elif`, and `else` statements along with complex boolean expressions.
For example, calling the function as follows:
```python
classify_person(16, True, 0.0)
```
Should produce the output:
```plain text
Minor
```

<details>
<summary>Solution</summary>

```python
def classify_person(age, is_student, income):
    if age < 18:
        print("Minor")
    elif age >= 18 and is_student and income < 20000:
        print("Adult Student")
    elif age >= 18 and not is_student and income < 20000:
        print("Low Income Adult")
    else:
        print("High Income Adult")
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def classify_person(age, is_student, income):
```
This line defines a function named `classify_person` which takes three parameters: `age`, `is_student`, and `income`.
1. **First If Condition**:
```python
if age < 18:
    print("Minor")
```
This condition checks if the `age` is less than 18. If true, it prints "Minor".
1. **Elif Condition for Adult Student**:
```python
elif age >= 18 and is_student and income < 20000:
    print("Adult Student")
```
This condition checks if the `age` is 18 or older, the person is a student (`is_student` is `True`), and the `income` is less than $20,000. If all these conditions are true, it prints "Adult Student".
1. **Elif Condition for Low Income Adult**:
```python
elif age >= 18 and not is_student and income < 20000:
    print("Low Income Adult")
```
This condition checks if the `age` is 18 or older, the person is not a student (`is_student` is `False`), and the `income` is less than $20,000. If all these conditions are true, it prints "Low Income Adult".
1. **Else Condition for High Income Adult**:
```python
else:
    print("High Income Adult")
```
This else block captures all other cases. It prints "High Income Adult" if none of the previous conditions are met, which implies the income is $20,000 or more.
</details>
</details>
---
## Question 4 - Complex boolean expressions
Write a Python function named `categorize_number` that takes a single integer `x` as its parameter. The function should categorize the number based on the following criteria and rules:
1. If `x` is both positive and divisible by 3, print "Positive and Divisible by 3".
1. If `x` is negative or completely divisible by 5, print "Negative or Divisible by 5".
1. If `x` is exactly 0, print "Zero".
1. If none of the above conditions is met, print "Other".
For example, calling the function with different values:
```python
categorize_number(9)
categorize_number(-10)
categorize_number(0)
categorize_number(7)
```
The output should be:
```plain text
Positive and Divisible by 3
Negative or Divisible by 5
Zero
Other
```

<details>
<summary>Solution </summary>

```python
def categorize_number(x):
    if x > 0 and x % 3 == 0:
        print("Positive and Divisible by 3")
    elif x < 0 or x % 5 == 0:
        print("Negative or Divisible by 5")
    elif x == 0:
        print("Zero")
    else:
        print("Other")
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def categorize_number(x):
```
This line defines a function named `categorize_number` that takes a single integer `x` as its parameter.
1. **If Condition to Check Positivity and Divisibility by 3**:
```python
if x > 0 and x % 3 == 0:
```
This line checks if `x` is both positive (greater than 0) and divisible by 3 (remainder when divided by 3 is 0).
1. **Print When Condition is Met**:
```python
print("Positive and Divisible by 3")
```
If the above condition is true, this line prints "Positive and Divisible by 3".
1. **Elif Condition to Check Negativity or Divisibility by 5**:
```python
elif x < 0 or x % 5 == 0:
```
If the first condition is not met, this line checks if `x` is either negative (less than 0) or divisible by 5 (remainder when divided by 5 is 0).
1. **Print When Elif Condition is Met**:
```python
print("Negative or Divisible by 5")
```
If the above condition is true, this line prints "Negative or Divisible by 5".
1. **Elif Condition for Zero**:
```python
elif x == 0:
```
If the first and second conditions are not met, this line checks if `x` is exactly 0.
1. **Print When Elif Condition is Met**:
```python
print("Zero")
```
If the above condition is true, this line prints "Zero".
1. **Else Statement for Any Other Condition**:
```python
else:
```
If none of the above conditions are met, this block handles all remaining possible values for `x`.
1. **Print When None of the Above Conditions are Met**:
```python
print("Other")
```
This line prints "Other" for all values of `x` that do not satisfy any of the previous conditions.
</details>
</details>
---
## Question 5 - Conditional statements and for loop
Write a Python function named `find_vowels` that takes a single string `s` as its parameter. The function should iterate through each character of the string `s` and:
1. If the current character is a vowel (a, e, i, o, u), print it.
1. If the current character is not a vowel, skip it and continue to the next character.
For example, if you call the function as follows:
```python
find_vowels("hello world")
```
The output should be:
```plain text
e
o
o
```
<details>
<summary>Solution</summary>

```python
def find_vowels(s):
    for char in s:
        if char not in 'aeiouAEIOU':
            continue
        print(char)
```
<details>
<summary>Line-by-line explanation</summary>

1. **Function Definition**:
```python
def find_vowels(s):
```
This line defines a function named `find_vowels` which takes a single string `s` as its parameter.
1. **For Loop**:
```python
for char in s:
```
This line begins a `for` loop that iterates through each character `char` in the string `s`.
1. **If Condition to Check Non-Vowels**:
```python
if char not in 'aeiouAEIOU':
```
This line checks if the current character `char` is not a vowel by checking if it is not in the string 'aeiouAEIOU'.
1. **Continue Statement**:
```python
continue
```
If the condition in the previous line is true (i.e., the character is not a vowel), this `continue` statement will skip the rest of the code inside the loop and jump to the next iteration.
1. **Print Vowel Character**:
```python
print(char)
```
If the character `char` is a vowel, this line will print the character.
</details>
</details>
---

📄 **[OOP]** (subpage)
## Question 1 - Inheritance
Create a simple Python program using inheritance. Define a base class called `Animal` with the following attributes and methods:
- Attributes:
- `name` (string)
- `age` (integer)
- Methods:
- `speak()` (prints "Animal sound")
Then, create a derived class called `Dog` that inherits from `Animal` and adds the following:
- Methods:
- `speak()` (overrides the base class method and prints "Bark")
Finally, create an instance of the `Dog` class, set its `name` to "Buddy" and `age` to 3, and call its `speak()` method. Write the complete code by hand.

<details>
<summary>Solution</summary>

```python
# Define the base class Animal
class Animal:
    # Constructor to initialize name and age attributes
    def __init__(self, name, age):
        self.name = name  # Set the name attribute
        self.age = age    # Set the age attribute

    # Method to print a generic animal sound
    def speak(self):
        print("Animal sound")  # Print the generic animal sound

# Define the derived class Dog that inherits from Animal
class Dog(Animal):
    # Override the speak method to print "Bark"
    def speak(self):
        print("Bark")  # Print the sound specific to dogs

# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)  # Initialize the Dog object with name "Buddy" and age 3

# Call the speak method on the Dog instance
my_dog.speak()  # This should print "Bark"

```
<details>
<summary>Line-by-line explanation</summary>

1. **Define the base class ****`Animal`**:
```python
class Animal:

```
- This line defines a new class named `Animal`.
1. **Constructor to initialize ****`name`**** and ****`age`**** attributes**:
```python
def __init__(self, name, age):
    self.name = name
    self.age = age

```
- The `__init__` method is a special method called a constructor. It initializes the `name` and `age` attributes for an instance of the `Animal` class.
1. **Method to print a generic animal sound**:
```python
def speak(self):
    print("Animal sound")

```
- The `speak` method in the `Animal` class prints "Animal sound".
1. **Define the derived class ****`Dog`**** that inherits from ****`Animal`**:
```python
class Dog(Animal):

```
- This line defines a new class named `Dog` that inherits from the `Animal` class.
1. **Override the ****`speak`**** method to print "Bark"**:
```python
def speak(self):
    print("Bark")

```
- The `speak` method in the `Dog` class overrides the `speak` method in the `Animal` class to print "Bark".
1. **Create an instance of the ****`Dog`**** class**:
```python
my_dog = Dog("Buddy", 3)

```
- This line creates an instance of the `Dog` class named `my_dog` with `name` set to "Buddy" and `age` set to 3.
1. **Call the ****`speak`**** method on the ****`Dog`**** instance**:
```python
my_dog.speak()

```
- This line calls the `speak` method on the `my_dog` instance, which prints "Bark" because the `Dog` class's `speak` method overrides the `Animal` class's `speak` method.
</details>
</details>
---
## Question 2 - Inheritance
Create a simple class hierarchy to represent different types of vehicles. Follow these steps:
1. Define a base class called `Vehicle` with the following attributes:
- `make` (string)
- `model` (string)
- `year` (integer)
- `mileage` (integer)
Include a method called `display_info` that prints out the vehicle's information in a formatted string.
1. Create a subclass called `Car` that inherits from `Vehicle` and adds the following attribute:
- `number_of_doors` (integer)
Override the `display_info` method to include the number of doors in the printed information.
1. Create another subclass called `Motorcycle` that inherits from `Vehicle` and adds the following attribute:
- `type_of_handlebars` (string)
Override the `display_info` method to include the type of handlebars in the printed information.
1. Instantiate an object of the `Car` class and an object of the `Motorcycle` class. Use the `display_info` method to print their information.
Write down the code for the classes and the instantiation of objects.

<details>
<summary>Solution</summary>

```python
# Base class
class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")

# Subclass Car
class Car(Vehicle):
    def __init__(self, make, model, year, mileage, number_of_doors):
        super().__init__(make, model, year, mileage)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.number_of_doors}")

# Subclass Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage, type_of_handlebars):
        super().__init__(make, model, year, mileage)
        self.type_of_handlebars = type_of_handlebars

    def display_info(self):
        super().display_info()
        print(f"Type of handlebars: {self.type_of_handlebars}")

# Instantiate objects
car = Car("Toyota", "Corolla", 2020, 15000, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, 8000, "Cruiser")

# Display information
car.display_info()
motorcycle.display_info()

```
<details>
<summary>Line-by-line explanation</summary>

1. **Define the base class ****`Vehicle`****:**
```python
class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

```
- The `__init__` method initializes the attributes `make`, `model`, `year`, and `mileage`.
1. **Define the ****`display_info`**** method in ****`Vehicle`****:**
```python
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")

```
- This method prints the vehicle's information in a formatted string.
1. **Define the ****`Car`**** subclass that inherits from ****`Vehicle`****:**
```python
class Car(Vehicle):
    def __init__(self, make, model, year, mileage, number_of_doors):
        super().__init__(make, model, year, mileage)
        self.number_of_doors = number_of_doors

```
- The `__init__` method initializes the attributes from the base class using `super()` and adds the `number_of_doors` attribute.
1. **Override the ****`display_info`**** method in ****`Car`****:**
```python
    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.number_of_doors}")

```
- This method calls the base class's `display_info` method using `super()` and then prints the additional attribute `number_of_doors`.
1. **Define the ****`Motorcycle`**** subclass that inherits from ****`Vehicle`****:**
```python
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage, type_of_handlebars):
        super().__init__(make, model, year, mileage)
        self.type_of_handlebars = type_of_handlebars

```
- The `__init__` method initializes the attributes from the base class using `super()` and adds the `type_of_handlebars` attribute.
1. **Override the ****`display_info`**** method in ****`Motorcycle`****:**
```python
    def display_info(self):
        super().display_info()
        print(f"Type of handlebars: {self.type_of_handlebars}")

```
- This method calls the base class's `display_info` method using `super()` and then prints the additional attribute `type_of_handlebars`.
1. **Instantiate objects of ****`Car`**** and ****`Motorcycle`****:**
```python
car = Car("Toyota", "Corolla", 2020, 15000, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, 8000, "Cruiser")

```
- Create instances of `Car` and `Motorcycle` with specific attributes.
1. **Display the information of the ****`Car`**** and ****`Motorcycle`**** objects:**
```python
car.display_info()
motorcycle.display_info()

```
- Call the `display_info` method on both objects to print their information.
</details>
</details>
---
## Question 3 - Special methods
Create a class named `Book` that represents a book. The class should have the following attributes:
- `title` (a string representing the title of the book)
- `author` (a string representing the author of the book)
- `year` (an integer representing the year the book was published)
Additionally, implement the `__str__()` and `__repr__()` methods for this class.
1. The `__str__()` method should return a string in the format: `Title by Author`.
1. The `__repr__()` method should return a string in the format: `Book(title='Title', author='Author', year=Year)`.
Instantiate an object of the `Book` class and print it using both `print()` and `repr()` functions to demonstrate the difference between `__str__()` and `__repr__()`.

<details>
<summary>Explanation</summary>

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # The __str__() method provides a readable string representation of the object
        return f"{self.title} by {self.author}"

    def __repr__(self):
        # The __repr__() method provides an unambiguous string representation of the object
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

# Create an instance of the Book class
book = Book("1984", "George Orwell", 1949)

# Using print() to call the __str__() method
print(book)  # Output: 1984 by George Orwell

# Using repr() to call the __repr__() method
print(repr(book))  # Output: Book(title='1984', author='George Orwell', year=1949)

```
<details>
<summary>Line-by-line explanation</summary>

1. **Class Definition and Initializer:**
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

```
- This defines a class `Book` with an initializer method `__init__()` that sets up the instance attributes `title`, `author`, and `year` when a new object is created.
1. **`__str__()`**** Method:**
```python
def __str__(self):
    return f"{self.title} by {self.author}"
```
- This method returns a readable string representation of the object, formatted as `Title by Author`. This is typically what you want to show to end-users.
1. **`__repr__()`**** Method:**
```python
def __repr__(self):
    return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
```
- This method returns an unambiguous string representation of the object, which could be used to recreate the object. This is useful for debugging and development.
1. **Creating an Instance:**
```python
book = Book("1984", "George Orwell", 1949)
```
- This line creates an instance of the `Book` class with the title "1984", author "George Orwell", and year 1949.
1. **Printing the Object:**
```python
print(book)  # Output: 1984 by George Orwell
```
- This line calls the `__str__()` method, producing a user-friendly string.
1. **Representing the Object:**
```python
print(repr(book))  # Output: Book(title='1984', author='George Orwell', year=1949)
```
- This line calls the `__repr__()` method, producing a detailed and unambiguous string.
</details>
</details>
---
## Question 4 - Getter and setter methods
Create a Python class `Rectangle` that represents a rectangle. The class should have the following features:
1. A private attribute `__length` to store the length of the rectangle.
1. A private attribute `__width` to store the width of the rectangle.
1. A getter method `get_length` to access the value of the private attribute `__length`.
1. A setter method `set_length` to modify the value of the private attribute `__length`. Ensure that the new value is positive, and if not, set the length to 0.
1. A getter method `get_width` to access the value of the private attribute `__width`.
1. A setter method `set_width` to modify the value of the private attribute `__width`. Ensure that the new value is positive, and if not, set the width to 0.
1. A method `area` that calculates and returns the area of the rectangle.
1. A method `perimeter` that calculates and returns the perimeter of the rectangle.

<details>
<summary>Solution</summary>

```python
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            self.__length = 0

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            self.__width = 0

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

```
<details>
<summary>Line-by-line explanation</summary>

1. **Class Definition**: We define a class `Rectangle`.
1. **Initializer Method (****`__init__`****)**: This method initializes the object with `length` and `width`.
1. **Private Attributes**: `__length` and `__width` are set as private attributes.
1. **Getter Method for Length (****`get_length`****)**: This method returns the value of `__length`.
1. **Setter Method for Length (****`set_length`****)**: This method sets the value of `__length` to a new value if it's positive; otherwise, it sets `__length` to 0.
1. **Getter Method for Width (****`get_width`****)**: This method returns the value of `__width`.
1. **Setter Method for Width (****`set_width`****)**: This method sets the value of `__width` to a new value if it's positive; otherwise, it sets `__width` to 0.
1. **Area Method (****`area`****)**: This method calculates and returns the area of the rectangle as `length * width`.
1. **Perimeter Method (****`perimeter`****)**: This method calculates and returns the perimeter of the rectangle as `2 * (length + width)`.
</details>
</details>
---
## Question 5 - Getter and setter methods
Create a Python class `Circle` that represents a circle. The class should have the following features:
1. A private attribute `__radius` to store the radius of the circle.
1. A public attribute `color` to store the color of the circle.
1. An initializer method to initialize the radius and color.
1. A getter method `get_radius` to access the value of the private attribute `__radius`.
1. A setter method `set_radius` to modify the value of the private attribute `__radius`. Ensure that the new value is positive; if not, set the radius to 0.
1. A method `area` that calculates and returns the area of the circle.
1. A method `circumference` that calculates and returns the circumference of the circle. Use [math.pi](https://www.w3schools.com/python/ref_math_pi.asp) to implement the calculation.
Write your solution by hand with a pen on paper.

<details>
<summary>Solution</summary>

```python
class Circle:
    def __init__(self, radius, color):
        self.__radius = radius
        self.color = color

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            self.__radius = 0

    def area(self):
        import math
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        import math
        return 2 * math.pi * self.__radius
```
<details>
<summary>Line-by-line explanation</summary>

1. **Class Definition**: We define a class `Circle`.
1. **Initializer Method (****`__init__`****)**: This method initializes the object with the radius and color.
1. **Private Attribute (****`__radius`****)**: `__radius` is set as a private attribute to store the radius.
1. **Public Attribute (****`color`****)**: `color` is a public attribute to store the color of the circle.
1. **Getter Method for Radius (****`get_radius`****)**: This method returns the value of the private attribute `__radius`.
1. **Setter Method for Radius (****`set_radius`****)**: This method sets the value of `__radius` to a new value if it's positive; otherwise, it sets `__radius` to 0.
1. **Area Method (****`area`****)**: This method calculates and returns the area of the circle using the formula `π * radius^2`. Importing the `math` module to get the value of `π`.
1. **Circumference Method (****`circumference`****)**: This method calculates and returns the circumference of the circle using the formula `2 * π * radius`. Again, importing the `math` module to get the value of `π`.
</details>
</details>
---
## Question 5 - Private and public attributes
Create a Python class `BankAccount` that represents a bank account. The class should have the following features:
1. A private attribute `__balance` to store the balance of the account.
1. A public attribute `account_holder` to store the name of the account holder.
1. A method `deposit(amount)` to deposit a given amount into the account. Ensure that the amount is positive, and if not, print an error message.
1. A method `withdraw(amount)` to withdraw a given amount from the account. Ensure that the amount does not exceed the current balance and is positive, otherwise print an error message.
1. A method `get_balance()` to retrieve the current balance of the account.

<details>
<summary>Solution</summary>

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.__balance = initial_balance
        self.account_holder = account_holder

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Error: Insufficient funds.")
        else:
            print("Error: Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance
```
<details>
<summary>Line-by-line explanation</summary>

1. **Class Definition**: We define a class `BankAccount`.
1. **Initializer Method (****`__init__`****)**: This method initializes the object with an `account_holder` name and an optional initial balance (default is 0).
1. **Private Attribute**: `__balance` is set as a private attribute to store the balance of the account.
1. **Public Attribute**: `account_holder` is a public attribute to store the name of the account holder.
1. **Deposit Method (****`deposit`****)**:
- This method takes an `amount` as an argument.
- If the `amount` is positive, it adds the `amount` to the `__balance`.
- If the `amount` is not positive, it prints an error message.
1. **Withdraw Method (****`withdraw`****)**:
- This method takes an `amount` as an argument.
- If the `amount` is positive, it checks if the `amount` is less than or equal to the `__balance`.
- If yes, it subtracts the `amount` from the `__balance`.
- If no, it prints an error message for insufficient funds.
- If the `amount` is not positive, it prints an error message.
1. **Get Balance Method (****`get_balance`****)**: This method returns the current balance stored in `__balance`. This allows controlled access to the private attribute `__balance`.
</details>
</details>
---

📄 **[SQL statements]** (subpage)
## Question 1 - Basic queries
Write a SQL query to retrieve specific information from a 'students' table. The table has the following columns: `id`, `name`, `age`, `grade`, and `city`.
1. Write a query to select all the columns for students who are older than 20.
1. Write a query to select the `name` and `grade` columns for students who have a grade higher than 75.
1. Write a query to select the `name` column for students who are from the city 'New York'.
Here is what the `students` table looks like:
```plain text
Students
-------------------------------------------
| id | name     | age | grade | city      |
|----|----------|-----|-------|-----------|
| 1  | Alice    | 19  | 85    | New York  |
| 2  | Bob      | 21  | 78    | Los Angeles|
| 3  | Charlie  | 22  | 90    | New York  |
| 4  | David    | 20  | 65    | Chicago   |
| 5  | Eve      | 23  | 72    | New York  |
```

<details>
<summary>Solution Query 1 </summary>

```sql
SELECT *
FROM students
WHERE age > 20;
```
<details>
<summary>Line-by-line explanation</summary>

1. *SELECT :*
This line indicates that all columns should be selected.
```sql
SELECT *
```
1. **FROM students:**
This line specifies that the data is being retrieved from the 'students' table.
```sql
FROM students
```
1. **WHERE age > 20:**
This line specifies the condition for selecting rows where the `age` column is greater than 20.
```sql
WHERE age > 20;
```
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT name, grade
FROM students
WHERE grade > 75;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT name, grade:**
This line specifies that only the `name` and `grade` columns should be selected.
```sql
SELECT name, grade
```
1. **FROM students:**
This line specifies that the data is being retrieved from the 'students' table.
```sql
FROM students
```
1. **WHERE grade > 75:**
This line specifies the condition for selecting rows where the `grade` column is greater than 75.
```sql
WHERE grade > 75;
```
</details>
---
</details>
<details>
<summary>Solution Query 3</summary>

```sql
SELECT name
FROM students
WHERE city = 'New York';
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT name:**
This line specifies that only the `name` column should be selected.
```sql
SELECT name
```
1. **FROM students:**
This line specifies that the data is being retrieved from the 'students' table.
```sql
FROM students
```
1. **WHERE city = 'New York':**
This line specifies the condition for selecting rows where the `city` column is equal to 'New York'.
```sql
WHERE city = 'New York';
```
</details>
</details>
---
## Question 2 - Basic queries
You are given a table named `Sales` with the following schema:
```plain text
Sales
-------------------------
| id | product | amount |
-------------------------
| 1  | A       | 100    |
| 2  | B       | 200    |
| 3  | A       | 150    |
| 4  | C       | 300    |
| 5  | B       | 100    |
| 6  | C       | 200    |
| 7  | A       | 250    |
| 8  | B       | 300    |
-------------------------
```
Write two SQL queries:
1. Write a query to find all the unique products sold.
Sample output:
```plain text
| product |
-----------
| A       |
| B       |
| C       |
```
1. Write a query to find the total sales amount for each product.
Sample output:
```plain text
| product | total_sales |
-------------------------
| A       | 500         |
| B       | 600         |
| C       | 500         |
```

<details>
<summary>Solution Query 1</summary>

```sql
SELECT DISTINCT product
FROM Sales;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT DISTINCT Clause**:
```sql
SELECT DISTINCT product
```
This part of the query selects unique (distinct) values of the `product` column from the `Sales` table. The `DISTINCT` keyword ensures that duplicate values are removed from the result set.
1. **FROM Clause**:
```sql
FROM Sales;
```
This part of the query specifies the table from which to retrieve the data, which is the `Sales` table.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT product, SUM(amount) as total_sales
FROM Sales
GROUP BY product;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause with Aggregation**:
```sql
SELECT product, SUM(amount) as total_sales
```
This part of the query selects the `product` column and calculates the sum of the `amount` column for each product. The `SUM` function is used to compute the total sales amount, and the result is given an alias `total_sales`.
1. **FROM Clause**:
```sql
FROM Sales
```
This specifies the table from which to retrieve the data, which is the `Sales` table.
1. **GROUP BY Clause**:
```sql
GROUP BY product;
```
This part of the query groups the rows in the `Sales` table by the `product` column. For each group, the `SUM(amount)` function calculates the total sales amount.
</details>
</details>
---
## Question 3 - Basic queries
Imagine you are given a table named `students` with the following structure and sample data:
```plain text
Students
| id  | name   | age | major        |
|-----|--------|-----|--------------|
| 1   | Alice  | 20  | Computer Sci |
| 2   | Bob    | 21  | Math         |
| 3   | Carol  | 20  | Computer Sci |
| 4   | Dave   | 21  | Engineering  |
| 5   | Eve    | 22  | Math         |
| 6   | Frank  | 20  | Engineering  |
| 7   | Grace  | 21  | Computer Sci |
```
Write two SQL queries based on this table:
1. Write a query using the `SELECT DISTINCT` statement to find all unique majors in the `students` table.
1. Write a query using the `GROUP BY` statement to find the count of students in each major.

<details>
<summary>Solution Query 1</summary>

```sql
SELECT DISTINCT major
FROM students;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT DISTINCT Clause**:
```sql
SELECT DISTINCT major
```
This line specifies that you want to select unique values from the `major` column. The `DISTINCT` keyword ensures that duplicate values are removed from the result set.
1. **FROM Clause**:
```sql
FROM students;
```
This line indicates that the data is being selected from the `students` table.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT major, COUNT(*) AS student_count
FROM students
GROUP BY major;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT major, COUNT(*) AS student_count
```
This line specifies that you want to select the `major` column and the count of rows for each major. The `COUNT(*)` function counts the number of rows in each group, and the result is aliased as `student_count` for readability.
1. **FROM Clause**:
```sql
FROM students
```
This line indicates that the data is being selected from the `students` table.
1. **GROUP BY Clause**:
```sql
GROUP BY major;
```
This line groups the result set by the `major` column. The `COUNT(*)` function counts the number of rows in each group.
</details>
</details>
---
## Question 4 - Basic queries
You are given a table named `Orders` with the following schema:
```plain text
Orders
--------------------------------
| order_id | customer_id | status |
--------------------------------
| 1        | 101         | shipped |
| 2        | 102         | pending |
| 3        | 103         | shipped |
| 4        | 101         | pending |
| 5        | 104         | shipped |
| 6        | 105         | canceled |
| 7        | 102         | shipped |
| 8        | 104         | pending |
--------------------------------
```
Write two SQL queries:
1. Write a query to count the total number of orders that have been shipped.
Sample output:
```plain text
| total_shipped |
-----------------
| 4             |
```
1. Write a query to count the number of orders placed by each customer.
Sample output:
```plain text
| customer_id | order_count |
-----------------------------
| 101         | 2           |
| 102         | 2           |
| 103         | 1           |
| 104         | 2           |
| 105         | 1           |
```

<details>
<summary>Solution Query 1</summary>

```sql
SELECT COUNT(*) as total_shipped
FROM Orders
WHERE status = 'shipped';
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT COUNT(*) Clause**:
```sql
SELECT COUNT(*) as total_shipped
```
This part of the query counts all rows in the result set. The `COUNT(*)` function calculates the total number of rows, and the result is given an alias `total_shipped`.
1. **FROM Clause**:
```sql
FROM Orders
```
This specifies the table from which to retrieve the data, which is the `Orders` table.
1. **WHERE Clause**:
```sql
WHERE status = 'shipped';
```
This filters the rows to include only those where the `status` column is equal to 'shipped'.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT customer_id, COUNT(*) as order_count
FROM Orders
GROUP BY customer_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause with Aggregation**:
```sql
SELECT customer_id, COUNT(*) as order_count
```
This part of the query selects the `customer_id` column and calculates the number of orders for each customer. The `COUNT(*)` function is used to count the number of rows for each group, and the result is given an alias `order_count`.
1. **FROM Clause**:
```sql
FROM Orders
```
This specifies the table from which to retrieve the data, which is the `Orders` table.
1. **GROUP BY Clause**:
```sql
GROUP BY customer_id;
```
This part of the query groups the rows in the `Orders` table by the `customer_id` column. For each group, the `COUNT(*)` function calculates the number of orders.
</details>
</details>
---
## Question 5 - Basic queries
You are given a table named `StudentGrades` with the following schema:
```plain text
StudentGrades
-----------------------------------
| student_id | course | grade     |
-----------------------------------
| 1          | Math   | 85        |
| 2          | Math   | 90        |
| 3          | Physics| 75        |
| 4          | Math   | 88        |
| 5          | Physics| 95        |
| 6          | Math   | 92        |
| 7          | Physics| 80        |
| 8          | Chemistry | 70     |
| 9          | Chemistry | 60     |
-----------------------------------
```
Write two SQL queries:
1. Write a query to find the average grade for each course.
Sample output:
```plain text
| course    | average_grade |
-----------------------------
| Math      | 88.75         |
| Physics   | 83.33         |
| Chemistry | 65.00         |
```
1. Write a query to find the average grade for courses where the average grade is above 80.
Sample output:
```plain text
| course  | average_grade |
---------------------------
| Math    | 88.75         |
| Physics | 83.33         |
```

<details>
<summary>Solution 1</summary>

```sql
SELECT course, AVG(grade) as average_grade
FROM StudentGrades
GROUP BY course;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause with Aggregation**:
```sql
SELECT course, AVG(grade) as average_grade
```
This part of the query selects the `course` column and calculates the average of the `grade` column for each course. The `AVG` function is used to compute the average grade, and the result is given an alias `average_grade`.
1. **FROM Clause**:
```sql
FROM StudentGrades
```
This specifies the table from which to retrieve the data, which is the `StudentGrades` table.
1. **GROUP BY Clause**:
```sql
GROUP BY course;
```
This part of the query groups the rows in the `StudentGrades` table by the `course` column. For each group, the `AVG(grade)` function calculates the average grade.
</details>
---
</details>
<details>
<summary>Solution 2</summary>

```sql
SELECT course, AVG(grade) as average_grade
FROM StudentGrades
GROUP BY course
HAVING AVG(grade) > 80;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause with Aggregation**:
```sql
SELECT course, AVG(grade) as average_grade
```
This part of the query selects the `course` column and calculates the average of the `grade` column for each course. The `AVG` function is used to compute the average grade, and the result is given an alias `average_grade`.
1. **FROM Clause**:
```sql
FROM StudentGrades
```
This specifies the table from which to retrieve the data, which is the `StudentGrades` table.
1. **GROUP BY Clause**:
```sql
GROUP BY course
```
This part of the query groups the rows in the `StudentGrades` table by the `course` column. For each group, the `AVG(grade)` function calculates the average grade.
1. **HAVING Clause**:
```sql
HAVING AVG(grade) > 80;
```
This part of the query filters the grouped results to include only those groups (courses) where the average grade is greater than 80. The `HAVING` clause is used to apply this condition after the groups have been formed.
</details>
</details>
---
## Question 6 - Basic queries
You are given a table named `Employees` with the following schema:
```plain text
Employees
--------------------------------------------
| id | name       | department | salary |
--------------------------------------------
| 1  | John Doe   | HR         | 50000  |
| 2  | Jane Smith | IT         | 75000  |
| 3  | Bob Brown  | IT         | 72000  |
| 4  | Alice Blue | Finance    | 55000  |
| 5  | Carol White| IT         | 73000  |
| 6  | Eve Black  | HR         | 51000  |
| 7  | Frank Gray | Finance    | 54000  |
| 8  | Grace Green| IT         | 70000  |
--------------------------------------------
```
Write two SQL queries:
1. Write a query to find the top 3 highest paid employees.
Sample output:
```plain text
| id | name       | department | salary |
----------------------------------------
| 2  | Jane Smith | IT         | 75000  |
| 5  | Carol White| IT         | 73000  |
| 3  | Bob Brown  | IT         | 72000  |
```
1. Write a query to list all employees in the IT department, ordered by their salary in descending order.
Sample output:
```plain text
| id | name       | department | salary |
----------------------------------------
| 2  | Jane Smith | IT         | 75000  |
| 5  | Carol White| IT         | 73000  |
| 3  | Bob Brown  | IT         | 72000  |
| 8  | Grace Green| IT         | 70000  |
```

<details>
<summary>Solution Query 1</summary>

```sql
SELECT id, name, department, salary
FROM Employees
ORDER BY salary DESC
LIMIT 3;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT id, name, department, salary
```
This part of the query selects the `id`, `name`, `department`, and `salary` columns from the `Employees` table.
1. **FROM Clause**:
```sql
FROM Employees
```
This specifies the table from which to retrieve the data, which is the `Employees` table.
1. **ORDER BY Clause**:
```sql
ORDER BY salary DESC
```
This part of the query orders the rows in the result set by the `salary` column in descending order (i.e., highest salary first).
1. **LIMIT Clause**:
```sql
LIMIT 3;
```
This part of the query limits the result set to only the top 3 rows, which are the highest paid employees.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT id, name, department, salary
FROM Employees
WHERE department = 'IT'
ORDER BY salary DESC;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT id, name, department, salary
```
This part of the query selects the `id`, `name`, `department`, and `salary` columns from the `Employees` table.
1. **FROM Clause**:
```sql
FROM Employees
```
This specifies the table from which to retrieve the data, which is the `Employees` table.
1. **WHERE Clause**:
```sql
WHERE department = 'IT'
```
This part of the query filters the result set to include only those rows where the `department` is 'IT'.
1. **ORDER BY Clause**:
```sql
ORDER BY salary DESC;
```
This part of the query orders the rows in the result set by the `salary` column in descending order (i.e., highest salary first).
</details>
</details>
---
## Question 7 - Basic queries
You are given a table named `Employees` with the following schema:
```plain text
Employees
--------------------------------
| id | name    | position | salary |
--------------------------------
| 1  | Alice   | Manager  | 90000  |
| 2  | Bob     | Engineer | 75000  |
| 3  | Charlie | Engineer | 76000  |
| 4  | David   | Manager  | 88000  |
| 5  | Eve     | Engineer | 72000  |
--------------------------------
```
1. Write an SQL query to update the salary of all Engineers by increasing it by 10%.
Sample output after the update:
```plain text
Employees
--------------------------------
| id | name    | position | salary |
--------------------------------
| 1  | Alice   | Manager  | 90000  |
| 2  | Bob     | Engineer | 82500  |
| 3  | Charlie | Engineer | 83600  |
| 4  | David   | Manager  | 88000  |
| 5  | Eve     | Engineer | 79200  |
--------------------------------
```
1. Write an SQL query to update the position of the employee `David` to `Senior Manager`.
Sample output after the update:
```plain text
Employees
--------------------------------
| id | name    | position       | salary |
--------------------------------
| 1  | Alice   | Manager        | 90000  |
| 2  | Bob     | Engineer       | 82500  |
| 3  | Charlie | Engineer       | 83600  |
| 4  | David   | Senior Manager | 88000  |
| 5  | Eve     | Engineer       | 79200  |
--------------------------------
```

<details>
<summary>Solution Query 1</summary>

```sql
UPDATE Employees
SET salary = salary * 1.1
WHERE position = 'Engineer';
```
<details>
<summary>Line-by-line explanation</summary>

1. **UPDATE Clause**:
```sql
UPDATE Employees
```
This part of the query specifies the table to be updated, which is the `Employees` table.
1. **SET Clause**:
```sql
SET salary = salary * 1.1
```
This part sets the new value for the `salary` column. It multiplies the current `salary` by 1.1 to increase it by 10%.
1. **WHERE Clause**:
```sql
WHERE position = 'Engineer';
```
This part of the query specifies the condition for the rows to be updated. Only the rows where the `position` is 'Engineer' will have their salaries updated.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
UPDATE Employees
SET position = 'Senior Manager'
WHERE name = 'David';
```
<details>
<summary>Line-by-line explanation</summary>

1. **UPDATE Clause**:
```sql
UPDATE Employees
```
This part of the query specifies the table to be updated, which is the `Employees` table.
1. **SET Clause**:
```sql
SET position = 'Senior Manager'
```
This part sets the new value for the `position` column. It changes the `position` to 'Senior Manager'.
1. **WHERE Clause**:
```sql
WHERE name = 'David';
```
This part of the query specifies the condition for the rows to be updated. Only the row where the `name` is 'David' will have its position updated.
</details>
</details>
---
## Question 8 - Basic queries
You are given a table named `Students` with the following schema:
```plain text
Students
-------------------------
| id | name    | grade  |
-------------------------
| 1  | Alice   | A      |
| 2  | Bob     | B      |
| 3  | Charlie | C      |
| 4  | Diana   | B      |
-------------------------
```
Write two SQL queries:
1. Write a query to add a new student named "Eve" with an id of 5 and a grade of "A".
1. Write a query to add two new students, "Frank" with an id of 6 and a grade of "B", and "Grace" with an id of 7 and a grade of "A" in one single query.

<details>
<summary>Solution Query 1</summary>

```sql
INSERT INTO Students (id, name, grade)
VALUES (5, 'Eve', 'A');
```
<details>
<summary>Line-by-line explanation</summary>

1. **INSERT INTO Clause**:
```sql
INSERT INTO Students (id, name, grade)
```
This part of the query specifies that we are inserting a new row into the `Students` table. The columns `id`, `name`, and `grade` are listed to indicate where the new values should be inserted.
1. **VALUES Clause**:
```sql
VALUES (5, 'Eve', 'A');
```
This part of the query provides the values to be inserted into the specified columns. Here, `5` is the `id`, `'Eve'` is the `name`, and `'A'` is the `grade`.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
INSERT INTO Students (id, name, grade)
VALUES
    (6, 'Frank', 'B'),
    (7, 'Grace', 'A');
```
<details>
<summary>Line-by-line explanation</summary>

1. **INSERT INTO Clause**:
```sql
INSERT INTO Students (id, name, grade)
```
Similar to the first query, this part of the query specifies that we are inserting new rows into the `Students` table. The columns `id`, `name`, and `grade` are listed to indicate where the new values should be inserted.
1. **VALUES Clause**:
```sql
VALUES
    (6, 'Frank', 'B'),
    (7, 'Grace', 'A');
```
This part of the query provides the values to be inserted into the specified columns. Here, two sets of values are provided, `(6, 'Frank', 'B')` for the first new student and `(7, 'Grace', 'A')` for the second new student. Both sets of values are separated by commas and enclosed within parentheses, allowing multiple rows to be inserted in a single `INSERT INTO` statement.
</details>
</details>
---
## Question 9 - Basic queries
You are given two tables named `Customers` and `Orders` with the following schema:
```plain text
Customers
-------------------------
| id | name         | age |
-------------------------
| 1  | John Doe     | 30  |
| 2  | Jane Smith   | 25  |
| 3  | Sam Brown    | 40  |
| 4  | Lucy Green   | 35  |
-------------------------
```
```plain text
Orders
----------------------------------
| order_id | customer_id | amount |
----------------------------------
| 101      | 1           | 250    |
| 102      | 2           | 150    |
| 103      | 2           | 200    |
| 104      | 3           | 300    |
| 105      | 5           | 350    |
----------------------------------
```
Write the following SQL queries:
1. Write a query to find all customers who have placed an order.
Sample output:
```plain text
| id | name       | age | order_id | amount |
---------------------------------------------
| 1  | John Doe   | 30  | 101      | 250    |
| 2  | Jane Smith | 25  | 102      | 150    |
| 2  | Jane Smith | 25  | 103      | 200    |
| 3  | Sam Brown  | 40  | 104      | 300    |
```
1. Write a query to find all customers and their orders.
Sample output:
```plain text
| id | name       | age | order_id | amount |
---------------------------------------------
| 1  | John Doe   | 30  | 101      | 250    |
| 2  | Jane Smith | 25  | 102      | 150    |
| 2  | Jane Smith | 25  | 103      | 200    |
| 3  | Sam Brown  | 40  | 104      | 300    |
| 4  | Lucy Green | 35  | NULL     | NULL   |
```
1. Write a query to find all orders and their customers.
Sample output:
```plain text
| id | name       | age | order_id | amount |
---------------------------------------------
| 1  | John Doe   | 30  | 101      | 250    |
| 2  | Jane Smith | 25  | 102      | 150    |
| 2  | Jane Smith | 25  | 103      | 200    |
| 3  | Sam Brown  | 40  | 104      | 300    |
| NULL | NULL    | NULL | 105      | 350    |

```
1. Write a query to combine all data from both tables.
Sample output:
```plain text
| id  | name       | age  | order_id | amount |
----------------------------------------------
| 1   | John Doe   | 30   | 101      | 250    |
| 2   | Jane Smith | 25   | 102      | 150    |
| 2   | Jane Smith | 25   | 103      | 200    |
| 3   | Sam Brown  | 40   | 104      | 300    |
| 4   | Lucy Green | 35   | NULL     | NULL   |
| NULL| NULL       | NULL | 105      | 350    |

```

<details>
<summary>Solution Query 1</summary>

```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
FROM Customers
INNER JOIN Orders ON Customers.id = Orders.customer_id;

```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.customer_id, Customers.customer_name, Orders.order_id, Orders.amount
```
This part of the query selects the `customer_id` and `customer_name` columns from the `Customers` table, and the `order_id` and `amount` columns from the `Orders` table.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies the `Customers` table as the source table for the query.
1. **LEFT JOIN Clause**:
```sql
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id;
```
This part of the query performs a LEFT JOIN between the `Customers` and `Orders` tables based on the `customer_id` column that they have in common. It returns all rows from the `Customers` table and the matching rows from the `Orders` table. If there is no match, the result is NULL on the side of the `Orders` table.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
FROM Customers
LEFT JOIN Orders ON Customers.id = Orders.customer_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
```
This part specifies the columns to be retrieved from the `Customers` and `Orders` tables.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies the primary table from which to retrieve data, which is the `Customers` table.
1. **LEFT JOIN Clause**:
```sql
LEFT JOIN Orders ON Customers.id = Orders.customer_id;
```
This part specifies the `LEFT JOIN` operation between the `Customers` table and the `Orders` table on the `id` column of `Customers` and `customer_id` column of `Orders`. It retrieves all rows from the `Customers` table and the matching rows from the `Orders` table. If there is no match, NULL values are returned for columns from the `Orders` table.
</details>
---
</details>
<details>
<summary>Solution Query 3</summary>

```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
FROM Customers
RIGHT JOIN Orders ON Customers.id = Orders.customer_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
```
This part specifies the columns to be retrieved from the `Customers` and `Orders` tables.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies the primary table from which to retrieve data, which is the `Customers` table.
1. **RIGHT JOIN Clause**:
```sql
RIGHT JOIN Orders ON Customers.id = Orders.customer_id;
```
This part specifies the `RIGHT JOIN` operation between the `Customers` table and the `Orders` table on the `id` column of `Customers` and `customer_id` column of `Orders`. It retrieves all rows from the `Orders` table and the matching rows from the `Customers` table. If there is no match, NULL values are returned for columns from the `Customers` table.
</details>
---
</details>
<details>
<summary>Solution Query 4</summary>

```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
FROM Customers
FULL OUTER JOIN Orders ON Customers.id = Orders.customer_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
```
This part specifies the columns to be retrieved from the `Customers` and `Orders` tables.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies the primary table from which to retrieve data, which is the `Customers` table.
1. **FULL OUTER JOIN Clause**:
```sql
FULL OUTER JOIN Orders ON Customers.id = Orders.customer_id;
```
This part specifies the `FULL OUTER JOIN` operation between the `Customers` table and the `Orders` table on the `id` column of `Customers` and `customer_id` column of `Orders`. It retrieves all rows when there is a match in one of the tables. If there is no match, NULL values are returned for columns from the non-matching table.
</details>
</details>
---
## Question 10 - Basic queries
You are given three tables: `Customers`, `Orders`, and `Products` with the following schema and 
```plain text
Customers
-------------------------
| id | name   | city    |
-------------------------
| 1  | Alice  | New York|
| 2  | Bob    | Boston  |
| 3  | Carol  | Chicago |
| 4  | Dave   | Dallas  |
-------------------------
```
```plain text
Orders
-------------------------------
| id | customer_id | date      |
-------------------------------
| 1  | 1           | 2023-01-01|
| 2  | 3           | 2023-01-03|
| 3  | 2           | 2023-02-01|
| 4  | 1           | 2023-02-15|
-------------------------------
```
```plain text
Products
-------------------------------
| id | order_id | product_name |
-------------------------------
| 1  | 1        | Laptop       |
| 2  | 1        | Mouse        |
| 3  | 2        | Keyboard     |
| 4  | 3        | Monitor      |
| 5  | 4        | Laptop       |
-------------------------------
```
Write a query to find the name of customers and the products they have ordered. The result should include the customer's name and the product name.
Expected output:
```plain text
-----------------------------
| customer_name | product_name |
-----------------------------
| Alice         | Laptop       |
| Alice         | Mouse        |
| Carol         | Keyboard     |
| Bob           | Monitor      |
| Alice         | Laptop       |
-----------------------------
```

<details>
<summary>Solution</summary>

```sql
SELECT
    Customers.name AS customer_name,
    Products.product_name
FROM
    Customers
JOIN
    Orders ON Customers.id = Orders.customer_id
JOIN
    Products ON Orders.id = Products.order_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.name AS customer_name, Products.product_name
```
This part of the query selects the `name` column from the `Customers` table and the `product_name` column from the `Products` table. The `AS` keyword is used to give an alias `customer_name` for the `name` column.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies that the query will start selecting data from the `Customers` table.
1. **JOIN Clause**:
```sql
JOIN Orders ON Customers.id = Orders.customer_id
```
This joins the `Customers` table with the `Orders` table based on the condition that the `id` column in `Customers` matches the `customer_id` column in `Orders`. This combines rows from both tables where the condition is true.
1. **JOIN Clause**:
```sql
JOIN Products ON Orders.id = Products.order_id;
```
This further joins the resulting table with the `Products` table based on the condition that the `id` column in `Orders` matches the `order_id` column in `Products`. This completes the join across all three tables.
</details>
</details>
---
---

---

