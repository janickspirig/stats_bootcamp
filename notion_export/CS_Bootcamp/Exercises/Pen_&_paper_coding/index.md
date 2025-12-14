---
title: "Pen & paper coding"
notion_id: "0c35412e-4046-4530-9ea2-7fb354c17e83"
notion_url: "https://www.notion.so/Pen-paper-coding-0c35412e404645309ea27fb354c17e83"
exported_at: "2025-12-13T22:44:51.958019+00:00"
---

# Pen & paper coding

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

