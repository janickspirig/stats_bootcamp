---
title: "Functions"
notion_id: "a230d8b8-bf31-499a-aa57-43687590bb7f"
notion_url: "https://www.notion.so/Functions-a230d8b8bf31499aaa5743687590bb7f"
exported_at: "2025-12-13T22:45:32.874558+00:00"
---

# Functions

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
