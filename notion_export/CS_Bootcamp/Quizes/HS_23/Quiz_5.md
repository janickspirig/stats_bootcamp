---
title: "Quiz 5"
notion_id: "fe3ce09d-4820-4d1f-b794-bb4fcd362dc9"
notion_url: "https://www.notion.so/Quiz-5-fe3ce09d48204d1fb794bb4fcd362dc9"
exported_at: "2025-12-13T23:22:19.497857+00:00"
---

# Quiz 5

## Question 1
Please assume that the following program has been executed without any error:
```python
class Vehicle:
    def __init__(self, brand, model, mileage=0, condition=100):
        # Please assume for the __init__ method that the variables
        # self._brand, self._model, self._mileage, self._condition have
        # been correctly initialized with the according arguments

        # please also assume there are getter-methods for brand, model, mileage and
        # condition that just return self._brand, self._model, self._mileage and
        # self._condition

    def drive(self, distance):
        if distance >= 0:
            self._mileage += distance
            self._condition -= self.condition * distance / 10000
            return
        raise ValueError('distance must be a positive number, you have entered', distance)

    def service(self):
        if self._condition + 10 <= 100:
            self._condition += 10
        else:
            self._condition = 100

    def __str__(self):
        return f"{self.brand} {self.model} with {self.mileage} km, a condition of {self.condition}%"

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.mileage}, {self.condition})"

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, mileage=0, condition=100, battery_health=100):
				# Please assume for the __init__ method that the attributes 
				# are also present in the super class are forwarded via super().__init__(...)
				# and that self.battery_health has been initialized with the according argument
		
		# please also assume there is a getter-method for battery_health
		# that just returns self._battery_health

		@battery_health.setter
		def battery_health(self, health_level):
		    if 0 <= health_level <= 100:
		        self._battery_health = health_level
		    else:
		        raise ValueError('health_level must be in the range of 0–100, you have entered', health_level)
		
		def drive(self, distance):
		    if distance >= 0:
		        self._mileage += distance
		        self._condition -= self.condition * distance / 20000
		        return self._mileage
		    else:
		        raise ValueError('distance must be a positive number, you have entered', distance)
		
		def __str__(self):
		    return f"{super().__str__()}, and a battery health level of: {self.battery_health}"
		
		def __repr__(self):
		    return f"ElectricVehicle('{self.brand}', '{self.model}', {self.mileage}, {self.condition}, {self.battery_health})"
		
v = Vehicle('Opel', 'Ascona')
e = ElectricVehicle('Fiat', '500e')
```
Please mark all correct statements regarding this program:
✅ The code *e.drive(2100)* returns 2100.
❌ After executing *v.service()* the code v.condition will return 110.
✅ Trying to execute *e2 = ElectricVehicle(brand='Tesla', model='Model S', mileage=65342, condition=80, battery_health=101)* raises an error.
✅ *e* is an instance of ElectricVehicle.
❌ Trying to execute *e.service()* raises an error.
❌ In the __init__ method of Vehicle we should not initialize *self._model* but rather *self.model*
❌ Vehicles inherits from ElectricVehicle
✅ The code *e = ElectircVehicle(’Fiat’, ‘500e’)* internally calls the __init__ method of Vehicle as well as the __init__ method of ElectricVehicle.

<details>
<summary>Explanation</summary>

> 💡 **[OOP](/83479909f70b47e491c55c9a6178291a), [inheritance](/76bc8240b5c44034a4fde93b7d3158ff)**
✅ **Correct**, `e.drive(2100)` indeed returns 2100. This is because the `drive` method of the `ElectricVehicle` class, which `e` is an instance of, returns `self._mileage` after adding the `distance` to it.
❌ **Incorrect**, `v.service()` will not make `v.condition` return 110. The `service` method of the `Vehicle` class increases the `condition` by 10 only if it's less than 90 (because the condition cannot exceed 100). If it's 100 or more, it just sets it to 100.
✅ **Correct**, trying to execute 
```python
e2 = ElectricVehicle(
		brand='Tesla',
		model='Model S',
		mileage=65342,
		condition=80,
		battery_health=101
)
```
will indeed raise an error. This is because the `battery_health` setter method in the `ElectricVehicle` class raises a `ValueError` if the `health_level` is not between 0–100.
✅ **Correct**, `e` is an instance of `ElectricVehicle`. This is clear from the line `e = ElectricVehicle('Fiat', '500e')`.
❌ **Incorrect**, trying to execute `e.service()` will not raise an error. This method is inherited from the `Vehicle` class and it increases the `condition` by 10 if it's less than 90 and sets it to 100 otherwise.
❌ **Incorrect**, in the `__init__` method of `Vehicle` we should indeed initialize `self._model`. The underscore prefix is a convention in Python indicating that the attribute is intended for internal use (although it can still be accessed directly). The `self.model` would refer to a property or a getter method, not the attribute itself.
❌ **Incorrect**, `Vehicle` does not inherit from `ElectricVehicle`. It's the other way around: `ElectricVehicle` is a subclass of `Vehicle`.
✅ **Correct**, the code `e = ElectricVehicle('Fiat', '500e')` indeed internally calls the `__init__` method of both `Vehicle` and `ElectricVehicle`. This is because `ElectricVehicle` is a subclass of `Vehicle` and its `__init__` method calls `super().__init__(...)` to execute the `__init__` method of the superclass.
</details>
---
## Question 2
One task in the assignment was to implement the *method* **.heal(self, other)** of the class **HealingSuperhero**. HealingSuperhero inherits from **Superhero**.
Let's assume there are two instances of Superhero: **danny** and **hulk**, while **danny** is also an instance of **HealingSuperhero**.
When calling **danny.heal(hulk)**, which one of the following statements is correct?
✅ The **powerlevel** of only the instance **hulk** will be increased, depending on how the *receive_healing()* method is implemented.
❌ The execution stops with an error message because the method **.heal(self, other)** expects two parameters and only one was given.
❌ An error occurs because it is important on which instance the **.heal** method is called. The correct call would have been **hulk.heal(danny)**.
❌ The **powerlevel** of both instances will be increased according to the implemented rule.
❌ The **powerlevel** of **danny** will be increased, depending on how the *receive_healing()* method is implemented.
❌  It is not guaranteed to work because the **powerlevel** on one or both instances could be 0, which will lead to an error (*DivisionByZero*).

<details>
<summary>Explanation</summary>

> 💡 **[Class inheritance](/c991314990fa47e19addaf16235213db)**
Before reviewing the statements let’s look at the relevant code snippet from the assignment:
```python
class HealingSuperhero(Superhero):
		def **init**(self, name, year_of_birth, alias, powerlevel):
				super().**init**(name, year_of_birth, alias, powerlevel)

def heal(self, other):
    other.powerlevel += self.powerlevel
```
We can see that class `HealingSuperhero` inherits from `Superhero` and thus has available all attributes and methods that are defined on the `Superhero` class. 
Also, there is the `.heal()` method which credits the powerlevel of the superhero the method is being called on to the other superhero that is provided as value for the `other` parameter.
For example, we have **hulk** with powerlevel 10 and **danny** with powerlevel 20. 
Now when we call `danny.heal(hulk)`, the new powerlevel of **hulk** will be:
`hulk.powerlevel = hulk.powerlevel + danny.powerlevel`
`hulk.powerlevel = 10 + 20 = 30` 
The powerlevel of **danny** will remain unchanged.
✅ **Correct**, the **powerlevel** of **hulk** will be increased. The second part of the statement, about the *receive_healing()* method is a bit confusing as in the assignment this method was not implemented.
❌ **Incorrect,** because the method `heal(self, other)` does have two parameters and both are provided when calling `danny.heal(hulk)`:
- `self` refers to the instance/superhero on which the method is being called (**danny**)
- `other` refers to the other instance/superhero being passed into the method (**hulk**)
❌ **Incorrect**, because **hulk** is an instance of `Superhero`, not `HealingSuperhero`, therefore **hulk** doesn't have the `.heal()` method. The `.heal()` method can only be called on an instance of `HealingSuperhero`, which **danny** is.
This is because `HealingSuperhero` (child class) inherits from `Superhero` (parent class). Thus, all attrbitues and methods defined on `Superhero` class are inherited and available on `HealingSuperhero` as well.
However, methods and attributes defined on the class `HealingSuperhero` are not available for class `Superhero`.
❌ **Incorrect**, because the `.heal()` method increases the powerlevel of the instance passed as the `other` parameter (**hulk**), not the instance on which the method is being called.
❌ **Incorrect**, the powerlevel of **hulk**, the other superhero, will be increased.
❌ **Incorrect** because there's no division operation happening inside the `.heal()` method.

</details>
---
## Question 3
Which of the following statements are True in the context of **object orientation**? Please mark all True statements:
✅ A subclass can inherit attributes and methods from its superclass.
✅ Objects are instances of classes.
✅ An object that is an instance of a subclass is always also an instance of the subclass' superclass.
❌ Private attributes (e.g., *_variablename*) cannot be directly manipulated in Python by client code. Instead, changing those requires respective setter-methods.
❌ A method in a subclass must not have the same name as a method in the respective superclass. Otherwise it is not clear, which method to execute.
❌ A method, like python functions, always needs to have a return statement. A *print()* is not sufficient.
✅ In Python, classes may inherit from their superclasses over multiple levels of a class hierarchy.

<details>
<summary>Explanation</summary>

> 💡 **[Class inheritance](/c991314990fa47e19addaf16235213db), [private attributes](/83479909f70b47e491c55c9a6178291a)**
✅ **Correct**, a subclass can inherit attributes and methods from its superclass. This is a fundamental aspect of inheritance in object-oriented programming. For example:
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido")
print(fido.name)  # Fido
fido.bark()  # Woof!

```
Here, `Dog` is a subclass of `Animal` and inherits the `name` attribute from it.
✅ **Correct**, objects are instances of classes. An "instance" is a specific object that is created from a particular class. For example, in the code above, `fido` is an instance of the `Dog` class.
✅ **Correct**, an object that is an instance of a subclass is always also an instance of the subclass's superclass. This is due to the inheritance relationship between the subclass and the superclass. In Python, you can use the `isinstance()` function to confirm this:
```python
print(isinstance(fido, Dog))  # True
print(isinstance(fido, Animal))  # True
```
❌ **Incorrect**, private attributes in Python (denoted by a single underscore, e.g., `_variablename`) can be directly manipulated by client code. The underscore is a convention to indicate that the attribute is intended to be private, but Python does not enforce this. So, **although** an attribute has been declared as **private**, it can **still** be accessed **from outside** the class, i.e., by client code.
❌** Incorrect**, a method in a subclass can have the same name as a method in its superclass. This is called method overriding. The subclass's method will be called instead of the superclass's method when the method is invoked on an instance of the subclass, due to [**Polymorphism**](/1847b80cf96b485da5725e3cd1b35ca9).
```python
class Animal:
    def __init__(self, name):
        self.name = name
		def bark(self):
		        print("WUUUUF!")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido")
fido.bark()  # Woof!
```
In the example above we can see that both classes, **Animal** and **Dog** have a method `bark()`. When we call the `bark()` method for **fido**, the one from the **Dog** class is executed.
❌ **Incorrect**, a method, like Python functions, does not always need to have a return statement. If no return statement is present, the function will return `None` by default.
✅ **Correct**, in Python, classes can inherit from their superclasses over multiple levels of a class hierarchy. This is known as multilevel inheritance. For example, you might have a `Mammal` class that inherits from `Animal`, and then a `Dog` class that inherits from `Mammal`. Each level of the hierarchy can add or override attributes and methods.
</details>
---
## Question 4
Please assume that FCS_student1 is an instance of the class Superhero from the Assignment. What is the return value of the following code snippet:
*isinstance(FCS_student1, object)*
❌ An error occurs.
❌ Without further information, the return value cannot be determined.
✅ True
❌ False
<details>
<summary>Explanation</summary>

> 💡 **[Type checking](/5b0832dbf9454eb1941b7632e68a9abb#6f8e8203d09a4c3aafa6f5d78119fe00)**
❌ **Incorrect**, because `isinstance()` is a built-in function in Python that checks if an object is an instance of a specified class or a subclass thereof. It doesn't raise an error in this case.
❌ **Incorrect**, this is incorrect because, as explained earlier, all classes in Python are derived from `object`. Therefore, any instance of any class is also an instance of `object`.
✅ **Correct**. In Python, all classes, including user-defined classes, are derived from the base class `object`. Therefore, an instance of any class in Python is also an instance of the `object` class.
Here, `FCS_student1` is an instance of the `Superhero` class. Since `Superhero` is a class and all classes in Python are derived from `object`, `FCS_student1` is also an instance of `object`. Hence, `isinstance(FCS_student1, object)` returns `True`.
Let's understand this with a simple example:
```python
class Superhero:
    pass

FCS_student1 = Superhero()

print(isinstance(FCS_student1, object))  # Outputs: True
```
In this example, `FCS_student1` is an instance of the `Superhero` class. When we use `isinstance()` to check if `FCS_student1` is an instance of `object`, it returns `True`.
❌ **Incorrect**, because `FCS_student1` is indeed an instance of `object` as explained above.
</details>
---



