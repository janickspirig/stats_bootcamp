---
title: "Loops"
notion_id: "479b4475-7292-4d2c-81fb-3d66cb3bb655"
notion_url: "https://www.notion.so/Loops-479b447572924d2c81fb3d66cb3bb655"
exported_at: "2025-12-13T22:47:54.755493+00:00"
---

# Loops

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

