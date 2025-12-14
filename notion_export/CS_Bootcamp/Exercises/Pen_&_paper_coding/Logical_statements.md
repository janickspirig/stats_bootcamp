---
title: "Logical statements"
notion_id: "d9088a2e-2494-4ef6-b872-41b0a4d52c17"
notion_url: "https://www.notion.so/Logical-statements-d9088a2e24944ef6b87241b0a4d52c17"
exported_at: "2025-12-13T22:48:28.175149+00:00"
---

# Logical statements

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

