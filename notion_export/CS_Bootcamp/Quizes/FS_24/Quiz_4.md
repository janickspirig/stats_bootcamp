---
title: "Quiz 4"
notion_id: "7560e9eb-087c-4554-a5e3-b7a75421e243"
notion_url: "https://www.notion.so/Quiz-4-7560e9eb087c4554a5e3b7a75421e243"
exported_at: "2025-12-13T23:11:16.204270+00:00"
---

# Quiz 4

## Question 1
Geben Sie das folgende Programm. Es wurde fehlerfrei ausgeführt.
```python
class Car:
    def __init__(self, brand, year_of_production):
        # Bitte nehmen Sie für die __init__ Methode an, dass die
        # Variablen self._brand und self._year_of_production mit den
        # zugehörigen Argumenten korrekt initialisiert wurden

    @property
    def brand(self):
        # Bitte gehen Sie davon aus, dass diese Methode den Wert
        # von self._brand zurückgibt
    def year_of_production(self):
        # Bitte gehen Sie davon aus, dass diese Methode den Wert
        # von self._year_of_production zurückgibt

    def compute_age(self):
        return 2024 - self._year_of_production

    def __str__(self):
        return f"This is a {self.brand} of age {self.compute_age()}"

    def __repr__(self):
        return f"Car({self.brand}, {self.year_of_production})"

class ElectricCar(Car):
    def __init__(self, brand, year_of_production, battery_capacity):
        # Bitte nehmen Sie für die __init__ Methode an, dass die
        # Argumente brand und year_of_production korrekt via super().__init__(...)
        # weitergegeben wurden und self.battery_capacity mit dem
        # zugehörigen Argument korrekt initialisiert wurde

    @property
    def battery_capacity(self):
        return self._battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        if not (isinstance(battery_capacity, float) or isinstance(battery_capacity, int)):
            raise TypeError('battery capacity needs to be a number (float or int)')
        elif battery_capacity < 0:
            raise ValueError('battery capacity needs to be a positive number')
        else:
            self._battery_capacity = battery_capacity

    def __str__(self):
        return f"{super().__str__()} and a remaining battery capacity of {self.battery_capacity} kWh"

    def __repr__(self):
        return f"ElectricCar({self.brand}, {self.year_of_production}, {self.battery_capacity})"

c = Car('Porsche', 1984)
e = ElectricCar('Porsche', 2022, 108)

```
Bitte markieren Sie alle korrekten Aussagen zu obigem Programm.
1. ✅ Der Aufruf *e.__str__()* kann fehlerfrei ausgeführt werden.
1. ✅ **c** ist eine Instanz von **Car**.
1. ✅ **e** ist eine Instanz von **Car**.
1. ✅ **ElectricCar** erbt von **Car**.
1. ✅ Der Aufruf *print(e)* kann fehlerfrei ausgeführt werden.
1. ✅ Der Aufruf *e._battery_capacity = 'insufficient'* kann fehlerfrei ausgeführt werden.
1. ❌ Der Aufruf *e.battery_capacity = 'insufficient' *kann fehlerfrei ausgeführt werden.
1. ✅ Der Aufruf *e* kann fehlerfrei ausgeführt werden.
1. ❌ **c** ist eine Instanz von **ElectricCar**.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Class inheritance](/c991314990fa47e19addaf16235213db), [repr ](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073)method, [str method](/83479909f70b47e491c55c9a6178291a#d6adf9d285e743288d38c01044065158), [getter](/83479909f70b47e491c55c9a6178291a#4d9fcd781fd5450697ba15e0c6989f20) & [setter](/83479909f70b47e491c55c9a6178291a#0fd3908f13ee4acf9601894aeebbcb56) method, [access class attributes](/83479909f70b47e491c55c9a6178291a#72cd5f486f4b455093b47d3a2115ff49)**
Let's break down the provided code and the answer options to understand why the correct answers are marked as they are.
### Code Explanation
1. **Class Definition: Car**
```python
class Car:
    def __init__(self, brand, year_of_production):
        self._brand = brand
        self._year_of_production = year_of_production

```
- This defines a class `Car` with an initializer method `__init__` that sets the brand and year of production.
```python
    @property
    def brand(self):
        return self._brand
```
- This defines a property `brand` that returns the value of `_brand`.
```python
    def year_of_production(self):
        return self._year_of_production
```
- This method returns the value of `_year_of_production`.
```python
    def compute_age(self):
        return 2024 - self._year_of_production
```
- This method calculates the age of the car by subtracting the year of production from 2024.
```python
    def __str__(self):
        return f"This is a {self.brand} of age {self.compute_age()}"
```
- This method returns a string representation of the car.
```python
    def __repr__(self):
        return f"Car({self.brand}, {self.year_of_production})"
```
- This method returns a more detailed string representation of the car.
1. **Class Definition: ElectricCar**
```python
class ElectricCar(Car):
    def __init__(self, brand, year_of_production, battery_capacity):
        super().__init__(brand, year_of_production)
        self.battery_capacity = battery_capacity
```
- This defines a class `ElectricCar` that inherits from `Car`. It initializes the brand and year of production using `super().__init__` and sets the battery capacity.
```python
    @property
    def battery_capacity(self):
        return self._battery_capacity
```
- This defines a property `battery_capacity` that returns the value of `_battery_capacity`.
```python
    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        if not (isinstance(battery_capacity, float) or isinstance(battery_capacity, int)):
            raise TypeError('battery capacity needs to be a number (float or int)')
        elif battery_capacity < 0:
            raise ValueError('battery capacity needs to be a positive number')
        else:
            self._battery_capacity = battery_capacity
```
- This defines a setter for `battery_capacity` that checks if the value is a positive number and raises errors if not.
```python
    def __str__(self):
        return f"{super().__str__()} and a remaining battery capacity of {self.battery_capacity} kWh"
```
- This method returns a string representation of the electric car, including the battery capacity.
```python
    def __repr__(self):
        return f"ElectricCar({self.brand}, {self.year_of_production}, {self.battery_capacity})"
```
- This method returns a more detailed string representation of the electric car.
1. **Creating Instances**
```python
c = Car('Porsche', 1984)
e = ElectricCar('Porsche', 2022, 108)
```
- These lines create instances of `Car` and `ElectricCar`.
### Answer Explanations
1. ✅ **Correct**, the `__str__` method is defined in both `Car` and `ElectricCar`, and it will return a string representation of the electric car without errors.
1. ✅ **Correct**, `c` is created as an instance of `Car`.
1. ❌ **Correct**, `e` is an instance of `ElectricCar`, which is a subclass of `Car`.
1. ✅ **Correct, **`ElectricCar` is defined as inheriting from `Car`.
1. ✅ **Correct**, the `print` function calls the `__str__` method, which is defined and will execute without errors.
1. ✅ **Correct**, directly setting the `_battery_capacity` attribute bypasses the setter method, so no error is raised.
1. ❌ **Incorrect**, the setter method for `battery_capacity` checks the type and will raise a `TypeError` because 'insufficient' is not a number.
1. ✅ **Correct**, simply referencing `e` will call the `__repr__` method, which is defined and will execute without errors.
1. ❌ **Incorrect**, `c` is an instance of `Car`, not `ElectricCar`.
</details>
---
## Question 2
Gehen Sie davon aus, dass **bbwl_student** (eine Instanz der Klasse **HealingSuperhero** aus dem Assignment) gegeben ist. Was passiert, wenn Sie folgenden Python-Code ausführen?
```python
str(bbwl_student)
```

❌ Python versucht das Objekt darzustellen. Da die Klasse **HealingSuperhero** aber weder eine *__str__* noch eine *__repr__* Methode implementiert, wird nur ein Wert ähnlich dem folgenden zurückgegeben:
```python
<__main__.HealingSuperhero object at Ox1130e3ed0>
```
❌ Keine der anderen Antworten trifft zu.
✅ Es wird eine der implementierten *str()* Methoden ausgeführt.
❌ Es wird die *repr()* Methode ausgeführt.
❌ Nichts passiert, da die implementierte *__str__* Methode zwar ein *return* Statement hat aber die *print()* Funktion nicht aufruft.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 ** [repr ](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073)method, [str](/83479909f70b47e491c55c9a6178291a#d6adf9d285e743288d38c01044065158) method**
❌ **Incorrect,** this would be true if the class `HealingSuperhero` did not implement either the `__str__` or `__repr__` methods. In such a case, Python would fall back to the default representation of the object, which looks like `<__main__.HealingSuperhero object at Ox1130e3ed0>`. However, the correct answer indicates that a `__str__` method is implemented.
❌ **Incorrect,** this is a catch-all option that is not applicable since one of the other answers is correct.
✅ **Correct,** if the class `HealingSuperhero` has an implemented `__str__` method, Python will use this method to convert the object to a string. The `__str__` method is specifically designed to return a "nice" string representation of the object.
```python
class HealingSuperhero:
    def __str__(self):
        return "HealingSuperhero instance"

bbwl_student = HealingSuperhero()
print(str(bbwl_student))  # Output: HealingSuperhero instance
```
- Here, the `__str__` method is defined in the `HealingSuperhero` class.
- When `str(bbwl_student)` is called, it invokes the `__str__` method and returns the string `"HealingSuperhero instance"`.
❌ **Incorrect, t**he `__repr__` method is used to provide an "official" string representation of an object, which can be useful for debugging. If both `__str__` and `__repr__` are implemented, `str()` will use `__str__`. Since the correct answer indicates that `__str__` is implemented, `__repr__` will not be used in this case.
❌ **Incorrect, t**his statement is misleading. The `str()` function does not require the `print()` function to work. The `str()` function will call the `__str__` method and return its result as a string. The `print()` function is only needed if you want to display the string on the screen.
</details>
---
## Question 3
Gegeben ist folgendes Programm
```python
class Car():
    def __init__(self, brand, model, milage, condition):
        self._brand = brand
        self._model = model
        self.milage = milage
        self.condition = condition

    # Bitte gehen Sie in Ihrer Antwort davon aus, dass hier korrekte und hilfreiche
    # Getter-Methoden brand() und model() implementiert sind

    def __str__(self):
        return f"""
        Das Fahrzeug ist das Modell {self.model} der Marke {self.brand},
        hat einen Kilometerstand von {self.milage} km und ist in
        {"gutem" if self.condition > 50 else "schlechtem"} Zustand
        """

print(Car('Porsche', '964', 150000, 41))
```

Bitte markieren Sie alle zutreffenden Aussagen.
✅ Werden passende Getter- und Setter-Methoden für *milage* und *condition* implementiert, kann das Programm ohne zusätzliche Änderungen fehlerfrei ausgeführt werden.
❌ Das Programm kann ohne die Implementierung der Setter-Methoden für *milage* und *condition* nicht fehlerfrei ausgeführt werden, da die **init** Methode diese Setter-Methoden implizit voraussetzt.
❌ Der Aufruf der *print()* Funktion funktioniert so nicht, da keine Referenz zu dem auszugebenden Objekt vorhanden ist.
❌ Das Programm erzeugt eine Ausgabe, die sehr ähnlich zu folgender ist:
```plain text
Das Fahrzeug ist das Modell 964 der Marke Porsche,
hat einen Kilometerstand von 150000 km und ist in
gutem Zustand

Eventuelle Variationen dieser Ausgabe sind auf die konkrete Implementierung der Getter-Methoden *brand()* und *model()* zurückzuführen.
```
✅ Das Programm kann fehlerfrei ausgeführt werden.
❌ Keine der anderen Aussagen trifft zu.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 ** [repr ](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073)method, [str](/83479909f70b47e491c55c9a6178291a#d6adf9d285e743288d38c01044065158) method**
Let's break down the provided code and the answer options to understand why the correct answers are marked as they are.
### Code Explanation
1. **Class Definition and Initialization**
```python
class Car():
    def __init__(self, brand, model, milage, condition):
        self._brand = brand
        self._model = model
        self.milage = milage
        self.condition = condition
```
- This defines a class named `Car`.
- The `__init__` method is a special method called a constructor. It initializes the object's attributes when a new instance of the class is created.
- `self._brand` and `self._model` are prefixed with an underscore, which is a convention to indicate that these attributes are intended to be private.
- `self.milage` and `self.condition` are public attributes.
1. **String Representation Method**
```python
def __str__(self):
    return f"""
    Das Fahrzeug ist das Modell {self.model} der Marke {self.brand},
    hat einen Kilometerstand von {self.milage} km und ist in
    {"gutem" if self.condition > 50 else "schlechtem"} Zustand
    """
```
- The `__str__` method is another special method that defines how the object is represented as a string.
- It uses an f-string to format the output, including the model, brand, milage, and condition of the car.
- The condition is evaluated to be "gutem" (good) if `self.condition` is greater than 50, otherwise "schlechtem" (bad).
1. **Creating an Instance and Printing**
```python
print(Car('Porsche', '964', 150000, 41))
```
- This line creates an instance of the `Car` class with the specified attributes and prints it.
- The `print` function calls the `__str__` method of the `Car` instance to get its string representation.
### Answer Explanations
✅ **Correct,** because the program can already run without errors. Implementing getter and setter methods for `milage` and `condition` would not affect the current functionality.
❌ **Incorrect,** because the `__init__` method directly assigns values to `milage` and `condition` without requiring setter methods. The program runs fine without them.
❌ **Incorrect, **because the `print` function is given a reference to a `Car` object. The `__str__` method of the `Car` class provides the string representation needed for printing.
❌ **Incorrect,** because the provided `__str__` method references `self.brand` and `self.model`, but these attributes are not directly accessible. They should be accessed through the getter methods (e.g., `self.brand()` and `self.model()`). Without the correct getter methods, the program will raise an `AttributeError`.
✅ **Correct,** because the program can run without errors, assuming the correct getter methods for `brand` and `model` are implemented.
❌ **Incorrect, **incorrect because some of the other statements are indeed correct.
</details>
---
## Question 4
Markieren Sie **alle** zutreffenden Aussagen.
Methoden, die in Python innerhalb von Klassendefinitionen definiert werden:
❌ können auch ohne Referenz zum aufrufenden Objekt *(self)* ausgeführt werden.
❌ können nicht ohne Argumente in den runden Klammern aufgerufen werden, z.B. *objekt_name.methoden_name()*, da immer die Referenz auf *self* notwendig ist.
✅ können, wenn sie genauso heissen wie Methoden ihrer *Superklasse***, ***polymorph* aufgerufen werden.
✅ können *Default-Werte* als Argumente besitzen.
✅ können Argumente an *bestimmten Positionen* (*positional arguments*) erwarten.
❌ sind, auch wenn Sie einen Property-Decorator (*@property*) haben, beim Aufruf durch Client-Code immer als Methoden erkennbar.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Class inheritance](/c991314990fa47e19addaf16235213db), [polymorphism](/1847b80cf96b485da5725e3cd1b35ca9)**
❌ **Incorrect**, in Python, methods defined within a class typically require a reference to the instance of the class, which is usually named `self`. This allows the method to access attributes and other methods of the instance. Without `self`, the method wouldn't know which instance's data to operate on.
If `self` is omitted, the method cannot be called on an instance of the class.
```python
class MyClass:
    def my_method(self):
        print("Hello, World!")

obj = MyClass()
obj.my_method()  # This works because my_method takes self as an argument.
```
❌ **Incorrect**, because when you call a method on an object, you do not need to explicitly pass `self`. Python automatically passes the instance as the first argument.
```python
obj.my_method()  # You don't need to pass self explicitly.
```
✅ **Correct**, Polymorphism allows methods in a subclass to have the same name as methods in a superclass. When you call such a method on an instance of the subclass, the subclass's method is executed.
This demonstrates polymorphism, where the method in the subclass overrides the method in the superclass.
```python
class SuperClass:
    def my_method(self):
        print("SuperClass method")

class SubClass(SuperClass):
    def my_method(self):
        print("SubClass method")

obj = SubClass()
obj.my_method()  # This will print "SubClass method"
```
✅ **Correct**, methods in Python can have default values for their parameters. This means that if no argument is provided for that parameter, the default value is used.
Here, `x` has a default value of 10.
```python
class MyClass:
    def my_method(self, x=10):
        print(x)

obj = MyClass()
obj.my_method()  # This will print 10
obj.my_method(20)  # This will print 20
```
✅ Correct, methods can expect positional arguments, which are arguments that need to be provided in a specific order.
In this example, `x` and `y` are positional arguments.
```python
class MyClass:
    def my_method(self, x, y):
        print(x, y)

obj = MyClass()
obj.my_method(1, 2)  # This will print 1 2
```
❌ **Incorrect**, the `@property` decorator in Python allows you to define methods that can be accessed like attributes. This means that when you use a property, it doesn't look like a method call.
```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

obj = MyClass(10)
print(obj.value)  # This will print 10, and it looks like accessing an attribute, not calling a method.
```
</details>
---
## Question 5
In Python ist die Instanz einer Unterklasse U (*sub class*), welche von der Superklasse S (*super class*) erbt, auch immer eine Instanz von *object*.
❌ Die Frage kann mit den gemachten Angaben nicht eindeutig beantwortet werden.
✅ Wahr
❌ Falsch

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Class inheritance](/c991314990fa47e19addaf16235213db)**
### Example Code
Before explaining the answer options, let's look at a simple example to illustrate inheritance:
```python
class S:
    pass

class U(S):
    pass

u_instance = U()
print(isinstance(u_instance, U))      # True
print(isinstance(u_instance, S))      # True
print(isinstance(u_instance, object)) # True
```
- `class S:` defines a superclass `S`.
- `class U(S):` defines a subclass `U` that inherits from `S`.
- `u_instance = U()` creates an instance of the subclass `U`.
- `print(isinstance(u_instance, U))` checks if `u_instance` is an instance of `U`, which is `True`.
- `print(isinstance(u_instance, S))` checks if `u_instance` is an instance of `S`, which is also `True` because `U` inherits from `S`.
- `print(isinstance(u_instance, object))` checks if `u_instance` is an instance of `object`, which is `True` because all classes in Python inherit from `object`.
### Answer Options
❌ **Incorrect,** because the question can be answered with the given information. In Python, all classes inherit from `object`, so an instance of any subclass will also be an instance of `object`.
✅ Correct, as shown in the example, an instance of a subclass is always an instance of `object` because all classes in Python inherit from `object`.
❌ **Incorrect**, because it contradicts the fundamental inheritance structure in Python. Every class, whether it's a subclass or not, is derived from `object`.
</details>
---

