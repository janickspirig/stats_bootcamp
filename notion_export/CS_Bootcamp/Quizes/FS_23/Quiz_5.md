---
title: "Quiz 5"
notion_id: "57a6ad83-8ae7-469f-9ea3-a663c2e29032"
notion_url: "https://www.notion.so/Quiz-5-57a6ad838ae7469f9ea3a663c2e29032"
exported_at: "2025-12-14T01:01:32.173615+00:00"
---

# Quiz 5

## Question 1
Gehen Sie davon aus, dass **management_student** (ein Objekt der Klasse **Superhero** aus dem Assignment) gegeben ist. Was passiert, wenn Sie folgenden Python-Code ausführen?
`print(management_student)`

❌ Nichts passiert, solange die Methode .__*init*()__ kein return statement hat.
❌ Es wird immer die Methode .__*repr*()__ ausgeführt, sofern sie definiert ist.
❌ Python versucht das Objekt darzustellen, zeigt aber nur die Klassenbezeichnung und das erste Attribut.
✅ Es wird immer die Methode .*__str()__* ausgeführt, sofern sie definiert ist.

<details>
<summary>Explanation</summary>

> 💡 **[string representation](/83479909f70b47e491c55c9a6178291a#d6adf9d285e743288d38c01044065158), [object representation](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073), [constructor](/83479909f70b47e491c55c9a6178291a#49c076e6f99740dcb067ca6026d9a60d)**
❌ **Incorrect**. The constructor, i.e., the `__init__()` method is executed when a **new object of a class** (class instance) is created. For example, if we would create a new superhero we can do `Superhero()`, and this calls the `__init__()` method inside the **Superhero** class.
❌ **Incorrect**. The object representation, i.e., the `__repr__()` method is executed when the variable in which the reference address to the object is stored is **outputted on the console**.
For example, if we would simply write `management_student` in a code cell and hit shift+enter, then the `__repr__()` method inside the Superhero class is executed.
❌ **Incorrect**. Python will call the `__str__()` method. If the method it is not implemented in the class, then the **memory reference address** of this object is returned and printed.
✅ **Correct**. Inside the `__str__()` method we can specify what should happen when `print(management_student)` is called.
</details>
---
## Question 2
Die Instanz einer Unterklasse **U **(*sub class*) ist auch immer eine Instanz der Superklasse **S **(*super class*) von welcher **U** erbt.
✅ Wahr
❌ Falsch

<details>
<summary>Explanation</summary>

> 💡 **[class inheritance](/c991314990fa47e19addaf16235213db)**
✅ **Correct**. Inheritance is a `is-a` relationship. This means: ***sub class*** **`is-a`** ***super class*** as it inherits the attributes and methods of the ***super class***.
</details>
---
## Question 3
Markieren Sie **alle** zutreffenden Aussagen.
Methoden, die in Python innerhalb von Klassendefinitionen definiert werden:
✅ sind, zum Beispiel im Fall von Getter-/Setter-Methoden, beim Aufruf durch Client-Code, oft nicht als Methoden erkennbar.
❌ dürfen *nicht* genauso heissen, wie Methoden ihrer *Superklasse*.
✅ können Funktionalität von Methoden der jeweiligen Superklasse wiederverwenden.
✅ können, wie Funktionen auch, *optionale* Argumente besitzen.
❌ müssen, wie auch Funktionen, immer ein **return** Statement haben. Ein **print()** ist nicht ausreichend.
✅ können, wie Funktionen auch, Argumente mit *Default*-Werten definieren.
✅ können, wie Funktionen auch, Argumente an *bestimmten Positionen* (positional arguments) erwarten.
✅ definieren, im Gegensatz zu Funktionen, meist eine Referenz zum aufrufenden Objekt (*self*) als Argument.

<details>
<summary>Explanation</summary>

> 💡 **[getter](/83479909f70b47e491c55c9a6178291a#4d9fcd781fd5450697ba15e0c6989f20) & [setter](/83479909f70b47e491c55c9a6178291a#0fd3908f13ee4acf9601894aeebbcb56) method, [access class attributes](/83479909f70b47e491c55c9a6178291a#72cd5f486f4b455093b47d3a2115ff49), [class inheritance](/c991314990fa47e19addaf16235213db), [optional & required parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc), [polymorphism](/1847b80cf96b485da5725e3cd1b35ca9)**
✅ **Correct**. A setter-method (if implemented) is called when a new value is assigned to an attribute of a class instance. However, a setter-method does not change anything on how the new value is assigned in the client code. This means we can still follow the pattern of:
`<< variable >>.<< attribute_name >> = << new_value >>`
For example, if we want to change the name of the management student we would call:
`management_student.name = "Marco"`
And we don’t know if there is a setter method implemented and being executed inside the class **Superhero**.
❌ **Incorrect**. If a method in the sub class is called the same as in the parent class, then the **method is overwritten** by the sub class. Python always tries to execute the **most specific **method of an object (Polymorphism).
For example, let’s assume that the Superhero class is a sub class of Hero and both classes have a method implemented called `get_hero_level()`.
If we now create a new Superhero `management_student = Superhero()` and call `management_student.get_hero_level()` then Python sees that there are **two** methods with this name: the **one** from **Superhero** class and the **one** from **Hero** class. However, the `Superhero.get_hero_level()` **overwrites** `Hero.get_hero_level()` which is why the `Superhero.get_hero_level()` method gets executed.
✅ **Correct**. A sub class i**nherits all methods and attributes** from its super class. For example, if only the Hero class has a `get_hero_level()` method, then we can still call `management_student.get_hero_level()` as the `Hero.get_hero_level()` method is executed automatically.
✅ **Correct**. Each method can have **required** and/or **optional** arguments. No matter if that method is defined inside a class or outside.
❌ **Incorrect**. A method inside a class is conceptually **nothing different** than a regular function. Thus, a return statement is not a necessity.
For example, inside the `get_hero_level()` we can either do `return self.hero_level` to **give the hero level back** to the client-code or **print the hero level** to the console directly using `print(self.hero_level)`.
✅ **Correct**. We learned already that class methods, just as regular functions, can have **required and optional** parameters. Whenever we have optional parameters we have **default values **defined as well. Because we must Python tell **which value to use** if from the client-code no value for the optional parameter is provided.
✅ **Correct**. Just as with regular functions, there can be positional arguments (usually in combination with optional parameters).
✅ **Correct**. This is why in any class method we need to provide the keyword **`self`** in the function header. For example, inside the `Hero.get_hero_level()` method we need to put the `self` parameter as first argument `def get_hero_level(`**`self`**`):` so that the method can then access the current hero level of the management student by calling `self.hero_level`.
</details>
---
## Question 4
Gegeben ist das folgende Programm. Es wurde fehlerfrei ausgeführt.
```python
class Person:
	def __init__(self, name, year_of_birth):
	# Bitte nenmen Sie for the init Methode an, das die Variablen
	# self._name und self._year_of_birth mit den zugehörigen Argumenten
	# name und year_of_birth korrekt initialisiert wurden

	@property
	def name(self):
		return selt._name
	@property
	def year_of_birth(self):
		return self._year_of_birth
	
	def compute_age (self):
		return 2023 - self.year_of_birth
	
	def __str__(self):
		return f"{self.name} ({self. compute_age()})"
	
	def __repr__(self):
		return "Person('(self.name}', (self.compute_age()})"

class Student(Person):
	def __init__(self, name, year_of_birth, courses):
		# Bitte nehmen Sie for the init_ , Methode an, das die
		# Argumente name und year_of_birth korrekt via super().__init__ (...)
		# weitergegeben wurden und dass self.courses mit dem
		# zugehörigen Argument courses korrekt initialisiert wurde

	@property
	def courses (self):
		return self._courses
	
	@courses.setter
	def courses (self, courses):
		if isinstance(courses, list):
			self._courses = courses
		else:
			raise TypeError('courses need to be provided as list obiects')

	def __str__(self):
		return f"{super().__str__()), courses: (', '.join(self.courses)}"
	
	def __repr__(self):
		return "Student('(self.name}', {self.compute_age ()), (self.courses})"

p = Person('Max', 2001)
s = Student('Lena', 2000, ['Travel at the speed of light', 'Harnessing complexity'])
```
Bitte markieren Sie **alle** korrekten Aussagen zu obigem Programm:
✅ Statement 1
Der Aufruf
`s`
gibt folgenden Wert zurück:
Student ('Lena', 23, ['Travel at the speed of light', 'Harnessing complexity'])
✅ Statement 2
**Student** ist eine Klasse.
❌ Statement 3
Der Aufruf
`s.compute_age()
`führt zu einem Fehler, da für die Klasse Student die Methode **.compute_age() **nicht definiert wurde.
✅ Statement 4
Der Aufruf
`s.courses.append('Bending rooms')`
kann fehlerfrei ausgeführt werden, da **.append()** eine list Methode ist, welche Elemente an Listen anhängt.
✅ Statement 5
**Student** ist eine Unterklasse (*sub class*) von **Person**.
✅ Statement 6
Es wurde eine Instanz von **Student** erstellt.
✅ Statement 7
Es wurden zwei Instanzen von **Person** erstellt.
❌ Statement 8
Der Aufruf
`p.name = 'Michaela'`
kann fehlerfrei ausgeführt werden, da das Attributname einen String erwartet.
❌ Statement 9
**Person** erbt von **Student**.

<details>
<summary>Explanation</summary>

> 💡 **[object representation](/83479909f70b47e491c55c9a6178291a#2ba4b82345404a34bdd7b89089b9e073), [append method](/5b0832dbf9454eb1941b7632e68a9abb#2561c3326d19459292a03dea27a7eda1), [class inheritance](/c991314990fa47e19addaf16235213db), [private attributes](/83479909f70b47e491c55c9a6178291a#612dfd274bbe4cb9bb0de56eabc4538d), [setter method](/83479909f70b47e491c55c9a6178291a#0fd3908f13ee4acf9601894aeebbcb56)**
✅ **Correct**. Check the code execution below to understand what is happening.
<details>
<summary>`s` →  **('Lena', 23, ['Travel at the speed of light', 'Harnessing complexity'])**</summary>

<details>
<summary>`def __repr__(self):`</summary>

`return "Student('(self.name}', {self.compute_age ()), (self.courses})"`
→ **('Lena', 23, ['Travel at the speed of light', 'Harnessing complexity'])**
`self.name` → **“Lena”**
<details>
<summary>`self.compute_age()` → **23** </summary>

<details>
<summary>`return 2023 - self.year_of_birth` → **2023 - 2000** → **23**</summary>

`self.year_of_birth` → **2000**
</details>
</details>
`self.courses` → ['Travel at the speed of light', 'Harnessing complexity']
</details>
</details>
✅ **Correct**. There is `class Student` defined.
❌ **Incorrect**. As seen in the [first answer](/57a6ad838ae7469f9ea3a663c2e29032), the method is implemented correctly and thus does not lead to an error.
✅ **Correct**. As the courses variable stores a list containing all the courses in which the student is enrolled, we can simply **access this list** with `s.courses` and then **append to this list **any element, i.e., course using the `.append()` method.
✅ **Correct**. We can see that **Student** is a sub class of **Person** by looking at the class header: `class Student(Person)`. 
✅ **Correct**. `Student()` was called and thus a new instance of **Student** class got created.
✅ **Correct**. One instance of Person was created by calling `Person()` and another instance by calling `Student()`. As **Student** is a sub-class of **Person** and the constructor of the **Person** class is called inside the **Student** class `super().__init__(name, year_of_birth)`, whenever a **Student** object is created also a **Person** object is created at the same time.
❌ **Incorrect**. From the descriptions inside the code we can see that a name attribute exists only on the **Person** class. And on the **Person** class this attribute is called `_name` and not `name`. Thus, when the value for the `_name` attribute is set with `p.name` an **error is raised**. We could set the value with `p._name`, however this is not best practice as `_name` is a **private** attribute (leading underline `_`). Thus, we should modify its value by using a setter method:
```python
@name.setter
def name(self, name):
	self._name = name
```
How we can modify the name by doing `p.name = "Michaela"`. This calls the setter method defined above and inside the setter method the value of the private attribute `_name` is modified. 
❌ **Incorrect**. It is the other way around: **Student** `is-a` **Person**. **Student** `is-a` subclass of **Person**. **Student** inherits from **Person**.
</details>
---
