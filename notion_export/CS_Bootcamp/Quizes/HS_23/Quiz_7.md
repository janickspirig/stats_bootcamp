---
title: "Quiz 7"
notion_id: "3cc7e6ab-5df6-4253-89ee-ba411acf7924"
notion_url: "https://www.notion.so/Quiz-7-3cc7e6ab5df6425389eeba411acf7924"
exported_at: "2025-12-13T23:21:35.782272+00:00"
---

# Quiz 7

## Question 1
Given is the following table **students**:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 50792 | Preston Omer | Haumesser | 1998-05-30 |
| 53450 | Julio Quinton | Shain | 1998-07-03 |
| 52819 | Van | Sokoloski | 1999-11-30 |
| 52980 | Lyman Richie Tracey | Elgin | 1998-05-31 |
| 52791 | Dale | Oviatt | 2001-11-11 |
Which query will return the entire tuple of *Van Sokoloski*?
Each empty field must contain exactly one word or entry.
`SELECT * FROM students WHERE id = 52819`

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#9f49f1d27402470bb2f991902699a137), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb)**
The table 'students' contains data about students, including their `id`, `first_name`, `last_name`, and `date_of_birth`.
The correct SQL query to return the entire tuple (or row) of Van Sokoloski would be:
```sql
SELECT * FROM students WHERE id = 52819
```
Here's why:
- `SELECT *` is used to select all columns of a row in a table. The asterisk (*) is a wildcard character that represents 'all'.
- `FROM students` specifies the table from which we want to retrieve data, in this case, the 'students' table.
- `WHERE id = 52819` is a condition that selects the row(s) where the 'id' column has the value 52819. Since 'id' values are unique for each student, this condition will return exactly one row, the one of Van Sokoloski.
</details>
---
## Question 2
Given is the following table students:
| id | first_name | last_name | date_of_birth |
| --- | --- | --- | --- |
| 51759 | Megan | Peery | 1996-12-26  |
| 53532 | Lashanda | Maglioli | 1999-11-12 |
| 50399 | Jamey | Sobotka | 1999-01-07 |
| 50587 | Julianna | Ravitz | 1998-03-29 |
| 53646 | Sylvester | Sampere | 2000-07-07 |
What is the numerical result of the following query:
```sql
SELECT COUNT(*)
FROM students
WHERE
date_of_birth < DATE('1999-04-15')
```
**3**

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#9f49f1d27402470bb2f991902699a137), [COUNT](/9f266597386048dd9a967fd9fd8e4b89#f7cb9984cd3a437ab2bdf2f38daaddec), [WHERE](/9f266597386048dd9a967fd9fd8e4b89#b2620d6b2e3847f7a58645a1cc6d5dfb)**
The SQL query is counting the number of rows in the 'students' table where the `date_of_birth` is less than '1999-04-15'.
In simpler terms, it's counting how many students were born before April 15, 1999.
Let's go through the table:
- Megan Peery was born on 1996-12-26, which is before 1999-04-15. → *include*
- Lashanda Maglioli was born on 1999-11-12, which is after 1999-04-15. → *exclude*
- Jamey Sobotka was born on 1999-01-07, which is before 1999-04-15. → *include*
- Julianna Ravitz was born on 1998-03-29, which is before 1999-04-15. → *include*
- Sylvester Sampere was born on 2000-07-07, which is after 1999-04-15. → *exclude*
So, the students who were born before April 15, 1999, are Megan Peery, Jamey Sobotka, and Julianna Ravitz. That's **3 students.**
</details>
---
## Question 3
In your database, you have at least the following five tables (same as in Assignment 07):
- **students(id, first_name, last_name, date_of_birth)**
- **registrations(id, student_id, matriculation, exmatriculation)**
- **courses(id, name, category_id)**
- **enrollments(id, student_id, course_id, semester)**
- **grades(id, enrollment_id, grade)**
Which one of the following queries returns all students that have a grade better than 5 (which numerically is greater than 5) in the course 'Fundamentals of Space-Time-Travel'?

✅ Code-snippet 1
```sql
SELECT
  students.id, grades.grade, students.first_name, students.last_name
FROM
  grades
INNER JOIN enrollments
  ON enrollments.id = grades.enrollment_id
INNER JOIN students
  ON students.id = enrollments.student_id
INNER JOIN courses
  ON courses.id = enrollments.course_id
WHERE
  grades.grade > 5
  AND
  courses.name = 'Fundamentals of Space-Time-Travel'
GROUP BY
  students.id
```
❌ Code-snippet 2
```sql
SELECT
  students.id, grades.grade, students.first_name, students.last_name
FROM
  grades
INNER JOIN students
  ON students.id = grades.id
INNER JOIN courses
  ON courses.id = grades.id
WHERE
  grades.grade > 5
  AND
  courses.name = 'Fundamentals of Space-Time Travel'
GROUP BY
	students.id
```
❌ Code-snippet 3
```sql
SELECT
  students.id, grades.grade, students.first_name, students.last_name
FROM
  grades
INNER JOIN enrollments
  ON enrollments.id = grades.enrollment_id
INNER JOIN students
  ON students.id = grades.student_id
INNER JOIN courses
  ON courses.id = enrollments.course_id
WHERE
  grades.grade > 5
  AND
  courses.name = 'History of Space-Time Travel'
GROUP BY
	students.id
```
❌ Code-snippet 4
```sql
SELECT
  students.id, grades.grade, students.first_name, students.last_name
FROM
  grades
INNER JOIN enrollments
  ON enrollments.id = grades.enrollment_id
INNER JOIN students
  ON students.id = enrollments.student_id
INNER JOIN courses
  ON courses.id = enrollments.course_id
WHERE
  grades.grade < 5
  AND
  courses.name = 'Fundamentals of Space-Time Travel'
GROUP BY
	courses.id
```
❌ It is not posisble in one query

<details>
<summary>Explanation</summary>

> ↪️ **Check the [explanation here](/3a3a4b5dac8647878840f77390b282f7#fcc5c6466396409ebabc499c8a893092).**
</details>
---
## Question 4
You have an SQL-compatible relational database system.
Please mark all correct answers for this context.
❌ A database contains the table **courses**. The SQL query **SELECT * FROM courses LIMIT 10** always returns exactly 10 tuples.
✅ The number of tuples returned by a **SELECT** query is *always* independent of which storage engine is used according to the ANSI-SPARC model.
✅ If a database with exactly three tables has *composite primary keys* in each of these tables, then the database does NOT necessarily have to have *foreign keys*.
✅ *SQL injections* never help to keep SQL queries performant, even if they are implemented in Python, which is otherwise known for its rather slow execution.
❌ Tables **A** and **B** each contain three tuples. Then the SQL query **SELECT * FROM A INNER JOIN B** also returns exactly three tuples.
❌ The query **SELECT DISTINCT * FROM tablename** of a table **tablename** always returns fewer tuples than the query **SELECT * FROM tablename** of the same table.

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#9f49f1d27402470bb2f991902699a137), [SELECT DISTINCT](/9f266597386048dd9a967fd9fd8e4b89#add7d3de22c14a809cb3c15bb7685bb4), [INNER JOIN](/9f266597386048dd9a967fd9fd8e4b89#f3ac72183aeb4fe7b12ff4cf12928a64), LIMIT**
❌ **Incorrect**, the SQL query `SELECT * FROM courses LIMIT 10` will return **up to** 10 tuples, not always exactly 10. If the table `courses` contains fewer than 10 tuples/rows, then the query will return all tuples/rows, which would be less than 10.
✅ **Correct**, the ANSI-SPARC model is a theoretical model of data management, and the storage engine doesn't affect the number of tuples returned by a **SELECT** query. The query's result depends on the data in the database, not the way it's stored.
✅ **Correct**, having composite primary keys in a table doesn't necessarily mean that the table will have foreign keys. Composite primary keys and foreign keys serve different purposes. Primary key is used to uniquely identify a record in a table, while foreign key is used to link two tables together.
✅ **Correct**, SQL injections are a security vulnerability, not a performance optimization technique. They occur when untrusted data is inserted into a query without proper validation or escaping, allowing an attacker to manipulate the query and the stored data eventually.
❌ **Incorrect**, 🤯 Unclear? check the [explanation here](/38843c4404ca477c83d9fd80c24f7870#148b03a8dfdc41b496623b69a0c64de2).
❌ **Incorrect**, the `SELECT DISTINCT` query eliminates duplicate rows from the result. If the table doesn't have any duplicate rows, then `SELECT DISTINCT * FROM tablename` will return the same number of tuples as `SELECT * FROM tablename`. 🤯 Still unclear? Check the [explanation here](/38843c4404ca477c83d9fd80c24f7870#6a3170a75ba54ce9a7b1f77d1784ff38).
</details>
---
## Question 5
Please assume that the table **persons** exists, with a non-null column **grade** that has correct numerical values and a column **course** that contains one course name in each tuple as a String.
Fill in the missing keywords to compute and return the *mean value* of **grades** for the ten best graded **courses** in the table **persons**.
```sql
SELECT course, AVG(grade)
FROM persons
GROUP BY course
ORDER BY AVG(grade) DESC
LIMIT 10
```

<details>
<summary>Explanation</summary>

> 💡 **[SELECT](/9f266597386048dd9a967fd9fd8e4b89#9f49f1d27402470bb2f991902699a137), [GROUP BY](/9f266597386048dd9a967fd9fd8e4b89#01c3d00f4a9e49c483728e10edd3deba), [AVG](/9f266597386048dd9a967fd9fd8e4b89#dc656637e4ae4f128577dd14c9f56303), LIMIT**
The task here is to compute and return the mean value of grades for the ten best graded courses in the table `persons`.
Here is the explanation of each keyword:
- `SELECT`: This keyword is used to select columns from a database tables. In this case, we are selecting `course` column and create a new column `AVG(grade)` that contains the mean grade of each course.
- `AVG(grade)`: This is an aggregate function that returns the average value of a numeric column. Here it is used to calculate the average grade of each course.
- `FROM`: This keyword is used to specify the table from which to retrieve the data. Here, the data is retrieved from the `persons` table.
- `GROUP BY`: This keyword is used in collaboration with the aggregate function `AVG(grade)` to group the result by `course`.
- `ORDER BY`: This keyword is used to sort the result in ascending or descending order. Here, it's used to sort the results by `AVG(grade)` in descending order (`DESC`), so that the course with the higest average grade will appear on top.
- `LIMIT`: This keyword is used to specify the maximum number of records/rows to return. Here, it's used to limit the result to the top 10 courses with the highest average grades.
> 🤯 **Still unclear? Check the[ explanation here](/3a3a4b5dac8647878840f77390b282f7#7a6d3430603d44e4a8e93510b54eb953).**
</details>
---
## Question 6
What happens if there is <u>no</u> **WHERE** statement in an **UPDATE** query?
❌ There is no restriction, so no entry in the chosen table will be overwritten.
❌ A syntax error will appear because updating entries in a table is done with the **INSERT** query.
❌ A syntax error will appear because an **UPDATE** query requires a **WHERE** statement.
✅ There is no restriction, so all entries in the chosen table will be overwritten.

<details>
<summary>Explanation</summary>

> 💡 **[UPDATE](/9f266597386048dd9a967fd9fd8e4b89#3ebedba97a0549f3b646cef4edebfbc4)**
❌ **Incorrect**, because without a **WHERE** clause, the **UPDATE** query will apply to all rows in the table, not none.
❌ **Incorrect**, because the **UPDATE** query is used to update existing data in a table, not the **INSERT** query. **INSERT** is used to add new rows to a table.
❌ **Incorrect**, because while it's good practice to include a **WHERE** clause in an **UPDATE** query to specify which rows should be updated, it's not a syntax requirement. If no **WHERE** clause is included, the **UPDATE** will apply to all rows.
✅ **Correct**, without a WHERE clause, the UPDATE query will apply to all rows in the table.
</details>
---


