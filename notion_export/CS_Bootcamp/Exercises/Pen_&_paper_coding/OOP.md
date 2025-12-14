---
title: "OOP"
notion_id: "9140a541-df2a-40c2-ac7b-95ad0a1451eb"
notion_url: "https://www.notion.so/OOP-9140a541df2a40c2ac7b95ad0a1451eb"
exported_at: "2025-12-13T22:48:59.423554+00:00"
---

# OOP

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

