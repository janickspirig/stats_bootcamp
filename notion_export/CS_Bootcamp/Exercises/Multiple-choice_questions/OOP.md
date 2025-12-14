---
title: "OOP"
notion_id: "c5521300-9175-44a9-892f-1d93068ce08f"
notion_url: "https://www.notion.so/OOP-c5521300917544a9892f1d93068ce08f"
exported_at: "2025-12-13T22:56:15.250800+00:00"
---

# OOP

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
