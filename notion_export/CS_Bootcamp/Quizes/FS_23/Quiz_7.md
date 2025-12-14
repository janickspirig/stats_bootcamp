---
title: "Quiz 7"
notion_id: "38843c44-04ca-477c-83d9-fd80c24f7870"
notion_url: "https://www.notion.so/Quiz-7-38843c4404ca477c83d9fd80c24f7870"
exported_at: "2025-12-14T01:03:24.459405+00:00"
---

# Quiz 7

## Question 1
Gegeben ist die folgende Tabelle **students**:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
Welche SQL-Abfrage liefert alle der gezeigten Tupel (tuple) der Tabelle, nicht jedoch potentiell weitere vorhandene Tupel, bei denen der last name nicht mit 'S' beginnt?
**SELECT** * **FROM** students **WHERE** last_name LIKE **‘S%’**

<details>
<summary>Explanation</summary>

> 💡 **[regular expressions](https://dataschool.com/how-to-teach-people-sql/how-regex-works-in-sql/), [SELECT](/9f266597386048dd9a967fd9fd8e4b89#f1c1f44f49aa4d76944c2d427c07c08f), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb)**
The question asks to write a query which retrieves all students with a last name that begins with letter **S**. 
As you can see from the table, all students have a last name that begins with letter **S**. Thus, the entire table as it is is returned, i.e., the `WHERE` condition does not filter out anything. 
Therefore, let’s assume we have the following data with some students that don’t have a last name beginning with letter **S**.
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | **Braun** | 1998-05-30 |
| 53450 | Julio Quinton | **Meier** | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | **Richard** | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
We can see that Preston, Julio and Lyman have last names that do not begin with **S**.
Thus, our expected output from the query should be the following:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
To figure out how the query gets to this table, let’s break it down into pieces:
```sql
SELECT * FROM student
```
returns all columns and records in the student table:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Braun | 1998-05-30 |
| 53450 | Julio Quinton | Meier | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Richard | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
To select Van and Dale only, we can extend the query now with a **WHERE** condition:
```sql
SELECT *
FROM
	student
WHERE
	last_name LIKE "S%**"**
```
returns all students with a last_name beginning with S:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
The **WHERE** condition goes into the column `last_name` and checks for each record / student if the condition `LIKE "S%"`** **applies. 
The condition `LIKE "S%"`** **checks if the last name matches the pattern**  **`"S%"`**.**
Pattern `"S%"`** **means that the string, i.e., last name of a student, must start with a capital **S**.
</details>
---
## Question 2
Sie schreiben mit SQL genau **eine** syntaktisch korrekte und zu den Tabellenstrukturen passende **SQL UPDATE** Anfrage inkl. einer **WHERE** Bedingung.
Markieren Sie bitte **alle** korrekten Aussagen.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, können mit genau einer solchen Anfrage alle Tupel (*tuple*) der entsprechenden Tabelle verändert werden.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE **Bedingung, kann mit genau einer solchen Anfragegenau ein Tupel (tuple) der entsprechenden Tabelle verändert werden.
❌ Die **WHERE** Bedingung kann nur im Zusammenhang mit **SELECT** Abfragen genutzt werden, nicht jedoch mit **UPDATE** Anfragen.
❌ Unabhängig vom Tabelleninhalt, wird mit genau einer solchen Anfrage immer genau ein Tupel (tuple) der entsprechenden Tabelle verändert.
❌ Mit Hilfe der **WHERE** Bedingung lassen sich die zu aktualisierenden Tabellenspalten festlegen.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, kann mit genau einer solchen Anfrage auch gar kein Tupel (*tuple*)der entsprechendenTabelle verändert werden.

<details>
<summary>Explanation</summary>

> 💡 **[UPDATE](/9f266597386048dd9a967fd9fd8e4b89#3ebedba97a0549f3b646cef4edebfbc4), [SELECT](/9f266597386048dd9a967fd9fd8e4b89#f1c1f44f49aa4d76944c2d427c07c08f), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb)**
Let’s assume we are dealing with the same data table as in the previous question.
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
✅ **Correct**. It can be that the `WHERE` condition evaluates to **True** for **all records** (students in this case) in the table. Then, **all records** will get updated. 
For example, the following query overwrite the first name of all students to **Marco**, because all students have a last name that begins with a capital **S**. Thus, `WHERE LIKE "S%"` evaluates to **True** for **all** **records**
Query:
```sql
UPDATE
	student
SET
	first_name = "Marco"
WHERE
	last_name LIKE "S%"
```
Output:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | **Marco** | Schaunmesser | 1998-05-30 |
| 53450 | **Marco** | Sa | 1998-07-03 |
| 52819 | **Marco** | Schokoloski | 1999-11-30 |
| 52980 | **Marco** | Schaan | 1998-05-31 |
| 52791 | **Marco** | Schauviatt | 2001-11-11 |
✅ **Correct**. It can also be that the where condition evaluates to **True** for only **one record **in the table. Then, only this record will get updated.
For example, the following query overwrites the last name of Preston to **Braun**. Because there is only one student called Preston, thus `WHERE frist_name = "Preston"` evaluates to **True** for only **one record**.
Query:
```sql
UPDATE
	student
SET
	last_name = "Braun"
WHERE
	first_name = "Preston"
```
Output: 
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | **Braun** | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
❌ **Incorrect**. The first two answers show that a **WHERE** condition can be used in combination with both, **SELECT** and **UPDATE**.
❌ **Incorrect**. The first two answers show that the number of records that get modified depends on the **WHERE** condition. The condition can evaluate to **True** for any number of records. 
❌ **Incorrect**. With the **SET** keyword we define the columns that should be modified, i.e., in which column the new value should be inserted. With the **WHERE** keyword we select the records that should be affected by the update. And the two in combination give us back one or multiple single cells. Then, using **UPDATE**, the update is executed, i.e., the new value is inserted into the one or multiple cells that were selected by **SET** and **WHERE**.
![How UPDATE, SET AND WHERE work in combination](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c9113f15-ab06-407c-a276-4e90fa691d3e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R76VFOEA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQD%2FFEvJfUxOOMlrEcM6480Xb7KiWvEhF6l87GKSMOWldwIhANHthaj4DPo9GZYv6%2FyHRHtUGtAsG2SydVQlEFhfUZ7NKv8DCCoQABoMNjM3NDIzMTgzODA1Igyxxfu2kHtI3P5zHxkq3AMK2iTpGA27zjvXYP%2BR02IKZct3Z4Of0Ktiu4hVh%2FNNY5MTkIRTe4cLL16QN%2F47%2Fg6ZLSJoExEnSgrbSqAPxfuT5uUPLz7gOzcfJhWh70HvOaYPtqqd1ClnVAh7CSOE89NxA5lKqYCsV%2BlwYNGi9bPcss0Qh7y96ZPcgRjQowZQaETakzvj7gTbJG5d9zLmqBZqTs78FYnxrhMbEm7X4yfowBRcgNDnfFb8ylVrewEhxPGzAJpMHkpHrpsRlIhSnGbUmmwMF8696xVcHCE9vXRKH%2FWRH%2BlXo4umcFdQATS1oyxXqR3Tce1ijnJZMqqqvvZ%2FopQSMz5yzO2mqdLVPUF4fuWZzIaZ%2FgrsbeGFPuz3mBhzmOmZ%2Bl2x%2BE7Iv%2FjsuT%2BJdellFqmnaT61k4BU5uA66%2F%2Bzf5xpHd7MT3nitFqY6YYY8LuUvqb6xdnr9UyMqQtEX2CgJFspO0bFQu5hPwGT8oNkhvVgTSys8hYKrwvz59OLCxfXPpkIhY48T4k04HbLp673az5zZOpzmRSK5p3KNlZfMGrwUlfMOCYuLMEc%2FvWRXEl%2FtQBjfp72fgb1mrnVvWFqjR5JlIsxmmsVUkcnGnhwxWbYbYb2ey6v%2FKxL7AGFngVk%2FPGHyIBHGjCklvjJBjqkAU7dsLjn2RTz%2F4kdlrWMOltHTZENnvEb1kA8S%2B97wooQudfKlE5B%2BQB2ELG4lwYJ9svuzOrKZFvNFbrU97o5LANljq5cp4eMJrF%2Bt9drGxxiDw5v9bdCZDUsteBw1IBpOeZE4GOg6dfuQ6bj531Q48lkyAtYzpT1SSb2Iu0TExB0by6xBO0nd6JhDrG%2F0MvsynsreoB0ZKMMbAKnBiGLvXglSEWB&X-Amz-Signature=b315bdf9c94e1df6e01b177ffae5df6a0aac61167400d46eeae6c385c8c622cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
✅ **Correct**. Of course it can also be that the **WHERE** condition does **not evaluate to True** for any record in the table. As a result, nothing changes.
For example, the following query aims to overwrite the first name to **Marco** for all students with a last name that starts with a capital **A**. However, as there is no student with a last name that starts with a capital **A**, `WHERE LIKE "A%"` evaluates to **False** for **all** **records** and nothing changes.
Query: 
```sql
UPDATE
	student
SET
	first_name = "Marco"
WHERE
	last_name LIKE "A%"
```
Output:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
</details>
---
## Question 3
Sie haben ein SQL-fähiges relationales Datenbanksystem.
Bitte markieren Sie für diesen Kontext alle korrekten Antworten.
❌ Die Abfrage **SELECT DISTINCT * FROM tabellenname** einer Tabelle **tabellenname** liefert immer weniger Tupel zurück als die Abfrage **SELECT * FROM tabellenname** der gleichen Tabelle.
✅ SQL-Injections helfen nie, SQL-Abfragen performant zuhalten, auch wenn diese in Python implementiert werden, welches ansonsten für seine eher langsame Ausführung bekannt ist.
✅ Die Anzahl, der von einer **SELECT** Abfrage zurückgegebenen Tupel, ist immer unabhängig davon, welche Storage- Engine gemäss ANSI-SPARC-Modell verwendet wird.
❌ In einer Datenbank gibt es die Tabelle **courses**. Der SQL- Befehl **SELECT *FROM courses LIMIT 10 **liefert dann immer genau 10 Tupel zurück.
❌ Die Tabellen **A** und **B** beinhalten jeweils drei Tupel. Dann gibt die SQL-Anfrage **SELECT * FROM A INNER JOIN B** ebenfalls genau drei Tupel zurück.

<details>
<summary>Explanation</summary>

> 💡 **[SELECT DISTINCT](/9f266597386048dd9a967fd9fd8e4b89#add7d3de22c14a809cb3c15bb7685bb4), [SELECT](/9f266597386048dd9a967fd9fd8e4b89#f1c1f44f49aa4d76944c2d427c07c08f), [LIMIT](/9f266597386048dd9a967fd9fd8e4b89#ca64b7e9f8c14563a40cd4d464dc5809), [INNER JOIN](/9f266597386048dd9a967fd9fd8e4b89#f3ac72183aeb4fe7b12ff4cf12928a64)**
Let’s assume we are dealing with the same data table as in the previous questions.
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
❌ **Incorrect**. If every entry in the table that is queried is unique, the two queries will return the exact same result. 
For example, in the data above **every student exists only once**, i.e., there are now duplicates. Thus, the two queries below will return the same number of records (5).
**Query 1**
```sql
SELECT DISTINCT *
FROM student
```

**Output 1**
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
**Query 2**
```sql
SELECT *
FROM student
```


**Output 2**
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
If there were two students with the same last name:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | **Schaunmesser** | 1998-05-30 |
| 53450 | Julio Quinton | **Schaunmesser** | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
Then the following queries would not return the same number of records.
**Query 1**
```sql
SELECT DISTINCT last_name
FROM student
```
**Output 1**
| last_name |
| --- |
| **Schaunmesser** |
| Schokoloski |
| Schaan |
| Schauviatt |

**Query 2**
```sql
SELECT last_name
FROM student
```

**Output 2**
| last_name |
| --- |
| **Schaunmesser** |
| **Schaunmesser** |
| Schokoloski |
| Schaan |
| Schauviatt |
✅ **Correct**. This does not depend on the programming language being used.
✅ **Correct**. Querying data **does not depend on the underlying data structure**. That’s exactly why the structured query language (SQL) is so popular as it can be used for multiple database architectures and technologies (e.g., mySQL, MongoDB, SQL Server, Databricks Lakehouse etc.)
❌ **Incorrect**. In case there are **less than 10 records** stored in the the **courses** table, the query will return all records that are available.
For example, the following query returns less than 10 records.
Query:
```sql
SELECT * FROM student
LIMIT 10
```
Output: 
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 |
| 53450 | Julio Quinton | Sa | 1998-07-03 |
| 52819 | Van | Schokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Schaan | 1998-05-31 |
| 52791 | Dale | Schauviatt | 2001-11-11 |
This is because there are only 5 students, thus there is no need to filter out any records with `LIMIT 10` as there are fewer students anyway
❌ **Incorrect**. An **INNER JOIN** returns the **intersection** between two tables, i.e., the records that can be found in both tables.
Let’s assume we have the following table **student**:
| id | first_name | last_name | date_of_birth | course_id |
| --- | --- | --- | --- | --- |
| 50792 | Preston Omer  | Schaunmesser | 1998-05-30 | 1 |
| 53450 | Julio Quinton | Sa | 1998-07-03 | 2 |
| 52819 | Van | Schokoloski | 1999-11-30 | 4 |
And the following table **course**: 
| id | course_name | level |
| --- | --- | --- |
| 1 | Computer Science | bachelor |
| 2 | Statistics | bachelor |
| 3 | Finance Advanced | master |
By looking at column `course_id` in the **student** table we can see that Preston is enrolled in the Computer Science course, Julio in the Statistics course and for Van we don’t know as there is **no course with id 4** in the table **course**. Also, we can see that no student is enrolled in the course Finance Advanced.
If we now execute the following query, we will get back the intersection of the two tables. That is Preston and Julio as for both a course could be found in the **course** table.
Query:
```sql
SELECT student.first_name, student.last_name, course.course_name
FROM student
INNER JOIN 
	course
ON
	student.course_id = course.id 
```
Output:
| first_name | last_name | course_name | level |
| --- | --- | --- | --- |
| Preston Omer  | Schaunmesser | Computer Science | bachelor |
| Julio Quinton | Sa | Statistics | bachelor |
As you can see the output has **two** records, while the two tables **student** and **course **both have **three** records.
</details>
---
## Question 4
In einer Datenbank haben Sie mindestens die folgenden Tabellen (wie in Assignment 07):
- **students (id, first_name, last name, date _of_birth)**
- **registrations(id, student id, immatriculation, exmatriculation) **
- **courses (id, name, category)**
- **enrollments (id, student id, course_id, semester)**
- **grades (id, enrollment id, grade)**
Welche der folgenden Abfragen (queries) gibt die durchschnittliche Note (average grade) für eine/n Studierende/n pro Kurskategorie aus, von welcher/m Sie nur den Vor- (first name) und Nachnamen (last name) kennen?
❌ Query 1
```sql
SELECT category, AVG(grade) as average_grade
FROM grades
INNER JOIN enrollments ON enrollments.id = grades.enrollment_id
INNER JOIN courses ON courses.id = enrollments.course_id
WHERE students.first_name = ?
AND students.last_name = ?
GROUP BY grade
```
❌ Query 2
```sql
SELECT category, AVG(grade)
FROM grades g
INNER JOIN enrollments e ON e.id = g.enrollment_id
INNER JOIN courses c ON c.id = e.course id
INNER JOIN students s ON s.id = e.student_id
WHERE s.first_name = ?
AND s.last_name = ?
GROUP BY category
```
❌ Query 3
```sql
SELECT category, AVG(grade)
FROM grades
GROUP BY category
WHERE students.first_name = ?
AND students.last_name = ?
```
❌ Query 4
```sql
SELECT category, AVG(grade)
FROM grades
INNER JOIN enrollments ON enrollments.id = grades.enrollment_id
INNER JOIN courses ON courses.id = enrollments.course_id
INNER JOIN students ON students.id = enrollments.student_id
WHERE students.first_name = ?
AND students.last_name
GROUP BY students.id
```
✅ Query 5
```sql
SELECT category, AVG(grade)
FROM grades g
INNER JOIN enrollments e ON e.id = g.enrollment_id
INNER JOIN courses c ON c.id = e.course_id
INNER JOIN students s ON s.id= e.student_id
WHERE s.first_name = ? 
AND s.last_name = ?
GROUP BY category
```
❌ Das ist in einer einzigen Abfrage nicht möglich.
❌  Die Verteilung von Primär- (primary keys) und Fremdschlüsseln (foreign keys) ist in den gegebenen Tabellen auf keinen Fall ausreichend, um die gewünschten Ergebnisse zu erzielen.

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#f1c1f44f49aa4d76944c2d427c07c08f), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb), [AVG](/9f266597386048dd9a967fd9fd8e4b89#ca64b7e9f8c14563a40cd4d464dc5809), [GROUP BY](/9f266597386048dd9a967fd9fd8e4b89#01c3d00f4a9e49c483728e10edd3deba), [INNER JOIN](/9f266597386048dd9a967fd9fd8e4b89#f3ac72183aeb4fe7b12ff4cf12928a64)**
The question asks to write a query that computes the average grade of a specific student per course category. As we are looking for a value per course category, we expect **each course category to have one record** in the output table. Thus, we must look into the different code snippets and check where we find the following **GROUP BY** statement:
```sql
GROUP BY category
```
We can find this **GROUP BY** statement in the **fifth** code snippet.
To validate, that the fifth query is correct, let’s execute it step by-step.
1. We join **enrollments** and **grades** to know all the grades of all the students.
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
```

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9a3dd2fc-d3d3-4f80-a3d1-2525d393e718/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S436ZCGM%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCID89KDYOwCAVmhahBQPLPxkON8%2Bmi%2B8ME9NhYBYhjmYHAiEA0WFKoj0BTvAzu53Nf0rIv6pg0h7t3a4rsM954L9MRxIq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDMrTelsdxVRIzZZf0SrcA%2FOcqHra9zdIGf%2BzeynOYqopuAOJbGsr%2Ffj9TyviaPwJs9I%2BfCqgqFmDJIBUEAJB7rIagGrMnH%2FVsaNwUEQn3dRSExm1FNA4cPnehR3%2FU8%2FRjcTtpQDnbW4w6rpFqkBHzEsVeIDBXH6GtHMowRXzlVtzl79TUx4rj%2FqCZLqcxpL1Bsc5qDM%2Fgd1sHPF36ds4Zt5s8H%2FPKHUJTnoWKHAzPOupf7Ctib%2BDUoW5Pjjn5okkbHGsqEwIn709c5R4airtz8erQBbsGrFs6Tid2TSUJFgciTbkpvCO2mED2KNwmXfUCECqFFEJUJ4Jy8qcALZsg6YndNlzj6S8MYAfHU79FP%2BUD4jS5VXHEts8iSf%2FCbpLctlW5gDZf3WiHNui2t8gntlS2uq0J1DF%2Fdr0TmOdS5mL8giMQpJwAWTgpWsvvO7yRA2dmHxI2hrooBDHfsKNm%2BlJBUl2BbV7s4db2uSzF7CNBH96UuzHEEIpQrL%2FJc%2BSLWBufzMz7KHaWVPeTTvLd5MdOsi6afWBivN36jpYTaaFOMdZuoQgcUFdhWrDbsoauvqA5wZao08F5WfHhk77rij85DX9bzTkBC0R%2FkMja2pO3hO7YsHS7GC3RRywMqhUaYX5uw7WcLLi4jNoMIiW%2BMkGOqUBh35EM7dCL7vCOi5uVTuyxWUSgqX4Gjc4MbS5TwbHfa6T96bZeu4iqo91yfnh9zQro6IT0JxAwHnmVCz8S3WeXnDU3Y%2B%2FPxwBOmXGXh%2BnHwOdgsBzK1L49jju61ki%2FYEuOGo%2FHUXYoTbbsdAcRJckztdI%2BElY1Y9l9iclXQHhIzN4FmZu96VglHtZ9rvjLKBvyZyswNBDZN2pvqbdj6Hm00fQ%2Faie&X-Amz-Signature=bcb7e9c7b74a0e29c5de865c3e0e29d7ae23a0c7ce16454285bd499315c21eb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join **enrollments** with **courses** to know in which course category the grade was achieved.
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bb58391f-28e2-4b87-9dfa-efb93b3c38dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRNBWL5W%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIGLtCfsES1%2FGsNWV63ZMOvMJBVJSbMffHiBXFrlIU9d3AiEAn%2Fci166XHR3rTijrUyvTwbStp759b5aW1m3PZfn0wf0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDGbrTnfQ3plSYzWbqircAwlvxKEobdb%2F07DwCCq762PgyPzddGzQNUM09dc%2Bu4VuSAN1E4xCsNW1Djm5zqPTZWs3OkV3R8sYMm2zAhKS9Bvf2XEUNfG4DW3JjfReXjVahwGgTrstbProudIYImoQ4Sn26h%2FyP1IxbVrYSnnHqUONT2vKjVPCPTFV6KxjEBsVVUgKqLcRsBEon6kisjRRLs7%2Bg7rylsfxBflzpSGBXYE9698TAMw%2BKDwfjsR%2FoZgYWGAU4wS5T5XaCLeldKYLPipBg2NVM%2BT%2F0Vj9sMIC8oomBSeQ6HUsNwJ5fYSldbg6Q6WqG8ecZ90rrreMgoL8XcvkL%2FqvVcBrTZfB1ig18pLWesznUSs6RsAbYw5siQ13hXnnKmjrtNY0p%2FRyBsBg9xNh3yM%2FlnkLsQ4wFqMhEYSifY4mvASi0yDyKWycat75Ik2UkwnG%2BMasrUC8%2Bfp0wRUwYfpL95nIBZksn%2FWi9VMgesp7dpTZE%2FI98vwl34uUfPiHfXw9utfDrqM%2Blt53k1zxUNV9rCHmSCNvIomgaKbloVwVYamanuxsV7Tn4Aw4FvXhmgvWYfjD0kayuwPcmCN%2FuIiduOQxeVu8Xttd40vHrZFj3tCrpOLZOtrN%2FbvQH0Uc56jFuFxB%2B3D%2BMOOW%2BMkGOqUBjgbfHc8buSmM%2BlPrw5j5rV7QjgS94TTtCjzvEm4FQEf1aXbYlqqMOJ5EaFsBTUXIDcbXGFd%2F1w0ZDGMZKn%2FXPEXsHpoPUoSfpaEEjJjmZ%2B5EZVVo9cZ00WlxIeAmmaHd0PUtB8dBu29ffabh%2BrzzqvmRjstEAbQ1MiTMQQVoxY60cOkvIOPcjmlCJrV8ZPAqFx7LrZ59YOyvUq7Fi5STgAfnJI5f&X-Amz-Signature=5835b5e87f7e078b763f0937bf1d5f22d5a91b588ce42d1185172833973a120d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join **enrollments** with **students** to get the first and last names of the students.
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
INNER JOIN students s
	ON s.id = e.student_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/34d7ccd1-9629-46da-ab0a-5e19d5df29c6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S3NGZGC%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQD%2Fl0Yyp0JmCnIfpqVOPUikcX0T%2BlMLU%2Bp4hsaMZ76T6wIhAMS6mGk3sxPlV5NA1p16sDDGbRr6YdyQB2XQ%2BdfBxiGoKv8DCCoQABoMNjM3NDIzMTgzODA1Igw%2BsdTsgwz72VXpweUq3AP3p9oRdMJFZQXKTPvSLxSPyIZgGaXINiRQAXk4UpsPdHTs5YeP6KPujeJp%2Fk5is0mXA%2BQdp8zleUFlcjx9AFjfVYPD2jYQBoU0qITlNaaw6H5rdOU9AX8Ngb4wbByrcbk6vSaFX2fc2fUGVSjF9ljVyHWUp3odvCer%2Fnzbuz7YUAfbNe6o14Yznt5%2F12Sc22t4YFNdFzgf0NnCF0KeLM6sqKfSkUxv%2BB%2BlGAgobnF3xdpEwSmQsuxfJfb411MaUZnaiphINsWWiqKJKeBO3T%2BiVYL%2FsTKI3L%2BCpg2GqIHufZUVAof9HBor80vaXWeBED%2FXjcQQRO0hU%2FtMsRI6fa%2F8%2BJyzWEs3rVAnvQY%2Fin0SkcLT7N5u3AvKebXhgz35JFjZGjrTwjZ9D6lO9RYf59pkImMmDzojsLDHPZmmVlXlojqCCRdoKFe%2B4II7cLa%2FPNzcyuwpeTnzFNBTpjP2mSwYzEDSAgPZeYdcbg%2FArosk%2FUxbOF6C5me6v1sEwLKUlI6%2BERT4o01gMms83K%2FHvgDdRixNPsYbeQfMuvO9WNHDkBPxF9hqfNO11v3XzLvgdHI3bshW%2FHfbnvpLhaeqkHARO2iI69KSsWjaR5XmEHwb48shtUuKMKEgR6k1gjDclvjJBjqkAUAR4BDnsVa%2BK2X2nBizDhP4OfIFNARwFyQPXE61OgTSQmtNYaixCAtxZbZQiVc35qt%2BbldU8CG80d2xKXw6aLTMAZXGX81ACWhvICXsE1levtp50TOXTmmQLUvUxw7xuJuyZ%2Fl%2F7ZaiZld63QI%2FKyQ16dvwQzKr6GYDU42PVeeldACwVnniV6p5IMsL1%2FitVwlUJKX8cujv5q%2FRQdoWRpwyvGrx&X-Amz-Signature=766f27a82c175e8599eacb518325d7b57f18e04b9d62591aff03d2de7f839167&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. As we have all the data in one table we can select now **one specific student** (Alanna Elrick in this case).
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
INNER JOIN students s
	ON s.id = e.student_id
WHERE
	s.first_name = "Alanna"
AND
	s.last_name = "Elrick"
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1966400c-2622-49f8-a0af-a4452434e8b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJFV4Q2N%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIFL9l1OHA8uAEQZR2ARUfITPJn5P3CxOEj7rpOd%2FzZibAiBGWSDBDW%2FIntbOQkScAIYnO5AERIt1XAJGd3G0DhS63Sr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMPrUElBT1Gk6S3evVKtwDPvJMPXa9MZBHhyTU6Aqaci7y1VEnATV5omTzpFUQKwoa8C3QnMOpSMrtsKoXrLH%2B8X38y2lNo1RV3F8ck%2FilCh0tldJHhqKpqDzV1h%2Fvm1nxzbGlXwfIjObu4bT9hiJSoceuq3nhXVNjfQzLLYz%2FAk%2FXdZ8BMLVmI%2Fw4XYPzi0QjhFp4kS1W29byqC%2FS8fLDcTavJe%2FlbWtM3AS%2BZBzbClummqnlo4qTeYPCqeLmjTFhs%2BJVxFrP1sUpDGv%2B0Ail6P6LBGcQUELllyPgAvn7B7SNCVYAZYFNZT2%2BBc1UGs8KqBayT0gZyGZhhX95CVYjNBn6%2B8QXzDGDWQJOLizuSU80dYHRhBX8XtrLCJk084ogphtXwcKcN71fDyDvFdn%2BqXucmqPkWmRWHsk%2BMnTcbDtjJ1HZQEVl1i0Oyg%2BzMZGcCov3w%2BO5C8RewqFkA%2Brvs7Lkxh6MG9NQQ1KOY0vNPYiCvshhJT7a7QCOrh9ixsK%2Bo5gUA6oVF%2FbdlVOt1pIay2C5ZrmQuCJ8qkDzW%2FFQRkgV%2FAjnrMVtODGT4koLpCmccoh0hypk42q8HGsUhBA6vAQjMDOI9efLMU9LbJPpMp9Pgjm8B%2BvYBGixkG9xSPEpz7y9%2FmiytdZt9wswlZf4yQY6pgFL8%2BhauTqpKeyKdTg2JPnurdVEXKTofG%2Fj1eYOIIPLwJFq9MdcBsS%2FxuGVbZ%2FfV1IBxho%2FyIF791%2BONtHUhpK%2FVVSoknrRcbW672TX%2FGYqRMKoCtC0VC0ElTHQLNX5zPJWWyrDjocMamieZuVcWznL%2Bj6eHd%2F5tXO8dGljj4x0bKOp0SZCGg7ikq5D0S2wyVJTq1IZFsTISTz4%2FX0%2FiU8V%2BN%2B6n0hN&X-Amz-Signature=677d42ea6f301ec83ca55fbb3d567fb04d45a54e6a8f8d9ee3673940cdb07af0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. As we have now all the grades and course categories of Alanna Elrick together, we can now **group by course category**, compute the average and select the relevant columns.
```sql
SELECT category, AVG(grade)
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
INNER JOIN students s
	ON s.id= e.student_id
WHERE
	s.first_name = "Alanna"
AND
	s.last_name = "Elrick"
GROUP BY category
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4508adda-64be-46b5-af4e-75e75a13807d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UKBIKT6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDSjNxZWLrjFddgYXwR2wc2hHzeuhsMj2k8NMm2KlYhTgIhAJp8x20Nl4BVeQYOj%2BROqXflbbhjJJWafSLZuHKkk%2FZBKv8DCCoQABoMNjM3NDIzMTgzODA1IgyidJuF4LVzr9%2F%2FTtsq3APMK931v%2FAbPVOtO%2BaOVhb2Un4rQQGlNCBnuyJpaOCWDM9Dgv4vvSJyX%2Bvju7Cim5wLbYwQytO95OUyP%2BPuPMxICIUei0eFmbzWIncnqK2LTt%2FrIhcglJ9H6B%2BnHdMp0fREVq0ODeWSkXQddlPvoQ7HOpqjOC0VcB6YRWid%2BZ%2FMNDvTK80aq%2BRGvxRO8VZ%2F2CDysb5qa32wZep1Zu06ZXUgegss%2Fl2ZmXYbwdgLoEfnCN9WZpK5AIS5TTEKOi7PJzzp4SiweUvDjQWXxaQh09LwBg0RMpzJgdFNUmjQo7wFF%2FmEfeqOo3oNEjWXhL1zQJ0jYJZ1uEwUXY9SNUR%2FKjR6ie9Ty6Jp8HLe4JhFYf1LbN6QgooFg1szI0KKVm7OsDNHgbG1y6%2FQZUH7iEhoV3FZMTtf7MqRGBeK64XMjy8fmnJQGU7So30jTU9RSCf7QGezaaq8ymFOwV3ICUClQ7t%2BuO5PR5CUpjkftTRSVz3%2FdF8mEhe6aHGpEbB1luu6xNmV9RBKIcCkDomvQSaLDAAYRpZ%2F1k7SiIpfzn6Q5EQK%2BgXVoDurMvoiHdhnDOP25lKJxVDo9ND%2Ff4En8vaVKMWAcCgqqHCSIreq%2B%2BZ%2FilanKCm8BtRTaPXlBoQlGjCGlvjJBjqkAT7SllVq%2BTnAJgPzFdBSZUB%2BcnwsG7qW%2FXPuqSzxQZk%2FpYvE6ZVxQiKiBlsRPu7UWO1d2SsRRQ0v7XQ7m12V%2F4JVPdB6EiUAlgm2wJ3%2FjvYfwkrGozRddrVcVJpfhfdxofFa4ePlNtuoDeug5YnJS5EFx7ZzetYQYWFsysvaRf%2F0FUaoa33Qt57yqVrDX5sx422MtNbPSTRWOPGIFk7B1xO3PKZb&X-Amz-Signature=9d9b3e63c1c6e2163b0a626a945b7a2067f6c12fbe2f2e3a64ed67a476e577c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
---

