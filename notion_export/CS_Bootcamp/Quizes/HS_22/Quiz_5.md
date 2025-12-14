---
title: "Quiz 5"
notion_id: "1fc79937-e649-4e4d-81b5-ad6c98c5da49"
notion_url: "https://www.notion.so/Quiz-5-1fc79937e6494e4d81b5ad6c98c5da49"
exported_at: "2025-12-13T23:19:37.064157+00:00"
---

# Quiz 5

## Question 1
What is printed by the following code cell assuming that the **__init__** method of the class **Person** was appropriately implemented according to its comment?
```python
class Person:

	def __init__(self, name, year_of_birth):
		# for the __init__ method, please assume that the variables
		# self._name and self._year_of_birth would be appropriately
		# initialized with the respective arguments

	@property
	def name(self):
		return self._name.upper()

	@property
	def year_of_birth(self):
		return int(self.year_of_birth)

	def __str__(self):
		return f'{self.name} is born in the year {self.year_of_birth}'

print(Person('Max', '2000'))
```
❌ *Nothing will be printed. Instead an error will be raised because ****year_of_birth**** should be an integer value.*
❌ *Nothing will be printed. Instead an error will be raised due to the missing ****setter methods.***
✅ MAX is born in the year 2000
❌ *Nothing will be printed. Instead an error will be raised because ****_year_of_birth**** and ****year_of_birth**** should be integer values.*
❌ Max is born int he year 2000
❌ *Nothing will be printed. Instead an error will be raised because we directly manipulate private attributed (****_name****, etc.) in the ****__init__**** method.*
❌ Person(’May’, ‘2000’)
❌ ’Max’ is born in the year ‘2000’
❌ Nothing will be printed. Instead an error will be raised because _ year_of_birth should be an integer value.

<details>
<summary>Explanation</summary>

❌ **Incorrect**,** **because we are free to store any value in any variable, i.e., it is technically possible to store a string in a variable `age` and the number 1 in a variable `name`. Thus, Python does not check if the value submitted for ***year_of_birth*** is an integer or not. It just stores the value in the variable.
❌ **Incorrect**, because we are not obliged to define setter methods, although we are suing getter methods (`@property`), as these are two different / separate constructs.
✅ **Correct**. Here we must now have a look on what is actually happening inside the code. Again, it is important to read the code from the inside to the outside:
<details>
<summary>`Person(’Max’, ‘2000)` → `x_606102`</summary>

1. The person class is called with the parameter values  ‘Max’ and ‘2000’
1. Python executes the code inside the constructor / `__init__` function
1. ‘Max’ is saved in variable `_name`
1. ‘2000’ is saved in variable `_year_of_birth`
1. Python returns memory address (`x_606102`) of this newly created class instance
</details>
<details>
<summary>`print(x_606102)` → ‘MAX is born int he year 2000’</summary>

1. The object that is stored at the address `x_606102` (Max) is accessed
1. Whenever we call `print()` for an object, Python checks if there is a `__str__` method implemented. If yes, the code inside this same method is executed.
1. Python executes the `def __str__` method
1. The person’s name is accessed with `self.name`
1. As we implemented a getter method `@property name`, the code inside this method is executed which returns the upper case version of the person’s name (’MAX’).
1. The person’s year of birth is accessed with self.year_of_birth
1. Again, we have the getter method `@property year_of_birth`. Inside this method, Python transform the value stored in variable `_year_of_birth` to an integer and returns it.
1. The string containing the upper case name (’MAX’) and the year of birth (2000) is returned
1. Python prints the string ‘MAX is born in the year 2000’ to the console.
</details>
❌ **Incorrect**. See explanation one → we are not bound to a specific data type that we can store in variables. Also, the code produces a valid output as we have seen.
❌ **Incorrect**. Yes, we modify the attributes directly. However, we do it within the class. Because `__init__` method lives inside the class Person, which we can see from the indentation. The whole idea behind getter and setter is to prevent data manipulation from outside the class, but from inside the class is entirely fine.
❌ **Incorrect**, because the name is printed in capitalised letters. 
❌ **Incorrect**, because the data of birth is printed as integer and not as string.
❌ **Incorrect**, because see explanation 1).
</details>
---
## Question 2
Given is the following code snippet:
```python
class Person:
	def __init__(self, name='Max', age=2, year_of_birth=2020):
		self.name = name
		self.year_of_birth = year_of_birth
	
	def age(self, current_year):
		return current_year - self.year_of_birth
```
Please *mark all* of the following code cells that, when executed after the class definition of Person, return an **integer value of 2**.
❌ `p = Person('Max', 2, 2020)`
❌ `Person('Max', 2, 2020).age`
✅ `Person('Max', 3, 2020).age(2022)`
✅ `Person('Max', 2020).age(2022)`
❌ `Person('Max', 2, 2020).age()`
✅ `Person('Max', 2, 2020).age(2022)`

<details>
<summary>Explanation</summary>

❌ **Incorrect**, because `age` is not an attribute of the Person class in the first place. I.e., nowhere inside the constructor a value is assigned to a variable called `age`. However, age is a function and if we want to call this function we must do so by using brackets, `p.age()`.
❌ **Incorrect**, age is still not an attribute but rather a function. And a function we can only call with brackets `<< function_name >>.()`.
✅ **Correct**, because first a new object for Max is created and the value 2020 is stored in the variable `year_of_birth`.
Now, we chain function calls together by immediately calling the `.age()` function for the person Max and submit the value 2022 as parameter.
Inside the function the difference between the value received as parameter (`current_year`) and the person’s `year_of_birth` is calculated: `2022 - 2022`, which yields `2`.
✅ **Correct**, the only difference to the previous example is that we only provide two values to the constructor instead of three. However, from the header of the constructor we can see that all parameters are optional. Thus, if we don’t provide a value for one or more parameters, the default values are used (the ones after the equal `=` sign).
After creating the class instance, the object has following values:
`name = 'Max'` → first value that we provided and the first value is stored in name
`age = 2020` → second value that we provided and the second value is stored in age
`year_of_birth = 2020` → default value was used as we only provided two values
And this creates the same situation as before: We call .age() function in which `2022 - 2020` is calculated and the number `2` is returned.
❌ **Incorrect**, it would yield an error. In the function header we see that we have a mandatory parameter, `current_year`. However, we call the function without a providing any value (`.age()`). Thus, Python is missing this value and throws an error.
✅ **Correct**, it’s basically the same as code snippet three. With the only difference that we provide 2 as value for `age`. However, when calculating the difference between `current_year` and `year_of_birth`, the variable `age` does not matter.
</details>
---
## Question 3
What is the output of the following code snippet?
```python
numbers = [5, 6, 1, 4]
sum(list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers))))
```
Output: **20**

<details>
<summary>Explanation</summary>

We get to the solution by reading the code from the inside to the outside.
<details>
<summary>1) `filter(lambda x: x % 2 == 0, numbers)` → **[6, 4]**</summary>

<details>
<summary>1st run: `x = 5` → **False**** **→** **exclude number 5</summary>

<details>
<summary>`1 == 0` → **False**</summary>

<details>
<summary>`lambda 5: 5 % 2` → **1**</summary>

`5 % 2` → **1**
</details>
</details>
</details>
<details>
<summary>2nd run: `x = 6` → **True** → include number 6</summary>

<details>
<summary>`0 == 0` → **True**</summary>

<details>
<summary>`lambda 6: 6 % 2` → **0**</summary>

`6 % 2` → **0**
</details>
</details>
</details>
<details>
<summary>3rd run: `x = 1` → **False**** **→** **exclude number 1</summary>

<details>
<summary>`1 == 0` → **False**</summary>

<details>
<summary>`lambda 1: 1 % 2` → **1**</summary>

`1 % 2` → **1**
</details>
</details>
</details>
<details>
<summary>4th run: `x = 4` → **True**** **→** **include number 4</summary>

<details>
<summary>`0 == 0` → **True**</summary>

<details>
<summary>`lambda 4: 4 % 2` → **0**</summary>

`4 % 2` → **0**
</details>
</details>
</details>
</details>
<details>
<summary>2) `map(lambda x: x * 2, [6, 4])` → **map([12, 8])**</summary>

<details>
<summary>1st run: `x = 6` → **12**</summary>

<details>
<summary>`lambda 6: 6 * 2` → **12**</summary>

`6 * 2` → **12**
</details>
</details>
<details>
<summary>2nd run: `x = 4` → **8**</summary>

<details>
<summary>`lambda 4: 4 * 2` → **8**</summary>

`4 * 2` → **8**
</details>
</details>
</details>
<details>
<summary>3) `list(map([12, 8])` → **[12, 8]**</summary>

simple conversion from map object to a list
</details>
<details>
<summary>4) `sum([12, 8])` → <u>**20**</u></summary>

`12 + 8 = 20` → <u>**20**</u>
</details>
</details>
---
## Question 4
What is printed by following code cell assuming that **__init__** method of the class **Person** was appropriately implemented according to its comment?
```python
class Person:

	def __init__(self, name, year_of_birth):
		# for the __init__ method, please assume that the variables
		# self._name and self._year_of_birth would be appropriately
		# initialized with the respective arguments

	def __str__(self):
		return f'{self.name} is born in the year {self.year_of_birth}'

class Student(Person):

	def __init__(self, name, year_of_birth, subject_of_study):
		super().__init__(name, year_of_birth)
		self.subject_of_study = subject_of_study

	def __str__(self):
		return f'{super().__str__()} and studies {self.subject_of_study}'

everyone = [Person('Max', 2000), Student('Max', 2000, 'Management')]

for i, e in enumerate(everyone):
	print(f'Person {i}: {everyone[i]}')
```
❌ Person 0: Max is born in the year 2000
     Person 1: Max is born in the year 2000
✅ Person 0: Max is born in the year 2000
     Person 1: Max is born in the year 2000 and studies Management
❌ Person 0: person 0
     Person 1: person 1
❌ Max is born in the year 2000
     Max is born in the year 2000 and studies Management
❌ Max is born in the year 2000
     and studies Management
❌ *Nothing will be printed because an error will be raised.*
❌ Person 0: Max is born in the year 2000
     Person 1: and studies Management
❌ Max is born in the year 2000 and studies Management

<details>
<summary>Explanation</summary>

To identify the correct answer we must understand 1️⃣ how the magic method **__str__()**, 2️⃣ inheritance, Polymorphism specifically, and 3️⃣ keyword **super()** work.
1️⃣ **__str__() **method is called whenever we use **print() **or we access the object inside a string**.** Python then executes the code that is inside the **__str__() **method. In the code above the **__str__() **method is implemented for both classes.
**Person****.__str__() **→ ** **the name of the person is printed and its year of birth
**Student****.__str__() **→  the method** ****Person****.__str__() **is called (which returns a text containing the name and year of birth of the person) and the subject of study is attached to that text
2️⃣ When looking at the class header `class Student(Person)` we see that **Student** is a child of the class **Person**. Thus, whenever we create a student it inherits all attributes (`_name` & `_year_of_birth`) and methods (`__str__()`)** **of the **Person **class. So, for a student object, we can also access the attributes and methods that are implemented by the **Person** class, without creating another person object.
However, we see that Student and Person class both have the **__str__() **method. So, when we have a student object `student_janick` and we call `print(student_janick)`, should the code inside **Person****.__str__() **or **Student****.__str__() **be executed? Due to Polymorphism, Python will execute the code that is *more specific* to this object. As **Person** is a generalisation of a student, **Student** class is more specific to `student_janick` and thus the method **Student****.__str__() **will be executed.
3️⃣ With the keyword **super()** we can access the attributes and methods of the parent class (**Person**) from within the child class (**Student**). In our example, this allows us to access the a person’s name and year of birth form within the class **Student**. Also, it allows us to execute the method **Person****.__str__()**. 
If we look now in the code, this is exactly what is happening inside **Student****.__str__()**. We call the method **Person****.__str__() **using** **`super().__str__()` which returns a text containing the person’s name and year of birth. We take now this string and extend it with the student’s subject of study. This final string is then returned from the **Student****.__str__() **method.
---
After having understood these three concepts, we can now dive into the code.
We see that for Max we create one instance of class **Person** and one instance of class **Student**. We store both class instances in the list `everyone`.
Now we iterate over the list using **enumerate()** function. This function returns the index position of the current object and stores it in `i` as well as the actual class instance object which is stored in `e`. 
<details>
<summary>1st run → Person 0: Max is born in the year 2000</summary>

We have the following values assigned to `i` and `e`.
<details>
<summary>`i = 0`</summary>

Because it is the first run
</details>
<details>
<summary>`e = Person.Max`</summary>

`e._name = 'Max'`
`e._year_of_birth = 2000`
`e.__str__()`
</details>
Now the output string has two parts:
<details>
<summary>‘Person {`i`}’ → returns ‘Person 0’</summary>

Integer 0 is saved in variable `i`
</details>
<details>
<summary>{everyone[`i`]} → returns ‘Max is born in the year 2000’</summary>

- Max is an object of class **Person**
- We access the object, thus **Person****.__str__() **is executed
- This returns** **the string ‘Max is born in the year 2000’
</details>
If we concatenate these two parts together we get:
Person 0: Max is born in the year 2000
</details>
<details>
<summary>2nd run → Person 1: Max is born in the year 2000 and studies Management</summary>

We have the following values assigned to `i` and `e`.
<details>
<summary>`i = 1`</summary>

Because it is the second run
</details>
<details>
<summary>`e = Student.Max`</summary>

`e.subject_of_study = 'Management'` 
`e.Student.__str__()`
`e._name = 'Max'` → inherited from **Person** class
`e._year_of_birth = 2000` → inherited from **Person** class
`e.Person.__str__()` → inherited from **Person** class
</details>
Now the output string has two parts:
<details>
<summary>‘Person {`i`}’ → returns ‘Person 1’</summary>

Integer 0 is saved in variable `i`
</details>
<details>
<summary>{everyone[`i`]} → returns ‘Max is born in the year 2000 and studies Management’</summary>

- Max is an object of class **Student**
- We access the object, thus **Student****.__str__() **is executed
- Inside **Student****.__str__() **we concatenate
- **super().__str__() **
- which calls **Person****.__str__()**
- This returns the string ‘Max is born in the year 2000’ is returned
- and studies **{self.subject_of_study}**
- which accesses the attribute **Student****.subject_of_study**
- This returns the string ‘and studies Management’
</details>
If we concatenate these two parts together we get:
Person 1: Max is born in the year 2000 and studies Management
</details>
</details>
---
## Question 5
One task in the assignment was to implement the *instance method ***.heal(self, other) **of the class **HealingSuperhero**. **HealingSuperhero** inherits from **Superhero**.
Let’s assume there are two instances of Superhero: **danny** and **hulk**, while **danny** is also an instance of HealingSuperhero.
When calling **danny.heal(hulk)**, which one of the following statement is correct?
❌ An error occurs because it is important on which instance the **.heal** method is called. The correct call would have been **hulk.heal(danny)**.
❌ The execution stops with an error message because the instance method **.heal(self, other)** expects two parameters and only one was given. 
❌ It is not guaranteed to work because the **powerlevel** on one or both instances could be 0, which will lead to an error (*DivisionByZero*).
❌ The powerlevel of both instances will be increased according to the implemented rule.
✅ The **powerlevel** of only the instance **hulk** will be increased according to the implemented rule.

<details>
<summary>Explanation</summary>

❌ **Incorrect**. danny is an instance of class **HealingSuperhero**. This class implements  the method **.heal(self, other)**. Thus, the call **danny.heal(hulk)** is correct.
**hulk.heal(danny)** would throw an error because **hulk** is an instance of **Superhero** class only, thus **hulk** has the method **.heal(self, other)** not available.
❌ **Incorrect**. The method expects only one parameter: **other**. **self** is the default parameter which tells Python to execute the method on the object from which the method is being called from.
❌ **Incorrect**. Inside the method **.heal()** we do an addition and no division.
`other.powerlevel += self.powerlevel`
❌ Incorrect. Only the powerlevel of the superhero saved in the other parameter will be increased.
✅ Correct. **hulk** is provided as value for parameter **other**.
</details>
---
## Question 6
Which of the following statements are True in the context of **object orientation**? Please *mark all* True statements. 
✅ A subclass can inherit attributes and methods from its superclass.
❌ Classes are instances of objects
❌ A method in a subclass must both have the same name as a method in the subclass’ superclass. Otherwise it is not clear, which method to execute. 
✅ In Python, classes may inherit from their superclasses over multiple levels of a class hierarchy. 
✅ While private attributes (e.g., *_variablename*) can be directly manipulated in Python by client code, they should not be directly manipulated by client code.
❌ If an object is an instance of a subclass it cannot be an instance of the subclass’ superclass at the same time. 

<details>
<summary>Explanation</summary>

✅ **Correct**. That’s the definition of inheritance 🙂
❌ **Incorrect**. Objects are instances of classes. Multiple instances (and thus multiple objects) of the same class can be created.
❌ **Incorrect**. As we have seen in [Question 4](/1fc79937e6494e4d81b5ad6c98c5da49#4a5cfb1647154934bc2bfd83bf745f48), [Polymorphism](/1fc79937e6494e4d81b5ad6c98c5da49#8e66b9f440dc4520beadca7059fee6cd) takes care of which method to execute when. For example, when a method with the same name exists in the subclass and the superclass, then the more specific method, i.e., the one in the subclass is executed.
✅ Correct. We can have multiple levels in the class hierarchy.
For example: 
               Person
               Student
 Undergrad      Postgrad
✅ **Correct**. Although an attribute is private, it can technically still be accessed and modified from outside the class. For this reason, we create getter and setter methods.
This is also because Python is an interpreted language. In a compiled language like Java, when declaring an attribute as private it is technically not possible to access it from outside the class.
❌ **Incorrect**. An instance of a subclass is automatically an instance of the subclass’ superclass, i.e., whenever an instance of the subclass is created, an instance of the subclass’ superclass is created simultaneously.
</details>
---

