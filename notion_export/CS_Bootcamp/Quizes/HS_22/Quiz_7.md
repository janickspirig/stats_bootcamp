---
title: "Quiz 7"
notion_id: "3a3a4b5d-ac86-4787-8840-f77390b282f7"
notion_url: "https://www.notion.so/Quiz-7-3a3a4b5dac8647878840f77390b282f7"
exported_at: "2025-12-13T23:17:02.825025+00:00"
---

# Quiz 7

## Question 1
Please assume that the table **persons** exists, with a non-null column **grade** that has correct numerical values and a column **course** that contains one course name in each tuple as a String.
Fill in the missing keywords to compute and return the *mean value* of **grades** for the ten best graded courses in the table **persons**.
```sql
**SELECT** course, **AVG(grade)**
FROM **persons**
**GROUP BY** course
ORDER BY **AVG(grade)** **DESC**
**LIMIT** 10
```

<details>
<summary>Explanation</summary>

Whenever you need to answer a SQL question it is important to first make sure you understand the data structure. In this database there is only one table, with at least two columns:
| ID | name | course | grade |
| --- | --- | --- | --- |
| 1 | Max Müller | Micro II | 3.9 |
| 2 | Marie Meier | Statistics | 5.1 |
| 3 | Alex Muster | Micro II | 4.0 |
| 4 | Lea Kälin | FCS | 5.4 |
| 5 | Marco Bühler | FCS | 4.3 |
| 6 | Anna Friedrich | Statistics | 4.9 |
From the example data above, we see that each record / row in the table represents a student’s grade for a specific course. 
Now the question asks us to select the top 10 courses by average grade. Thus, we want to calculate the average of the values in column grade per course.
Assuming the example data and that we want to select the top 2 courses, the output from our query should look like this:
| course | AVG(grade) |
| --- | --- |
| Statistics | 5.00 |
| FCS | 4.85 |
Now that we are clear on what the output should look like, we can think about the query we have to write. Below, you can see that happens in the query line-by-line.
**Query**
```sql
SELECT course
FROM persons
```

**Output**
| ID | course |
| --- | --- |
| 1 | Micro II |
| 2 | Statistics |
| 3 | Micro II |
| 4 | FCS |
| 5 | FCS |
| 6 | Statistics |
```sql
SELECT course, AVG(grade)
FROM persons
GROUP BY course
```

| course | AVG(grade) |
| --- | --- |
| FCS | 4.85 |
| Micro II | 3.95 |
| Statistics | 5.00 |
```sql
SELECT course, AVG(grade)
FROM persons
GROUP BY course
ORDER BY AVG(grade) DESC
```

| course | AVG(grade) |
| --- | --- |
| Statistics | 5.00 |
| FCS | 4.85 |
| Micro II | 3.95 |
```sql
SELECT course, AVG(grade)
FROM persons
GROUP BY course
ORDER BY AVG(grade) DESC
LIMIT 2 # 10 (in exercise)
```

| course | AVG(grade) |
| --- | --- |
| Statistics | 5.00 |
| FCS | 4.85 |

We see that the key-statement we are using is `GROUP BY`. Whenever we use `GROUP BY`, we are aggregating data rows in a table, i.e., reducing the number of rows. To do so, we have to tell SQL two things:
- **Grouping column **→ Column `x` in the table should be reduced to unique values only. In our example, we wanted to have unique values only in column `course`, thus we used `GROUP BY course`.
- **Aggregation function** → How duplicate values in grouping column `x` should be aggregated / put into each other. In our example, `AVG(grade)` was the aggregation function, which calculated the mean value in column `grade`.
</details>
---
## Question 2
Given is the following table students:
| **id** | **first_name** | **last_name** | **date_of_birth** |
| --- | --- | --- | --- |
| 51759 | Meghan | Peery | 1996-12-26 |
| 53532 | Lashanda | Maglioli | 1999-11-12 |
| 50399 | Jamey | Sobotta | 1999-01-07 |
| 59587 | Julianna | Ravitz | 1998-03-29 |
| 53646 | Sylvester | Sampere | 2000-07-07 |
What is the numerical result of the following query?
```sql
SELECT COUNT(*)
FROM students
WHERE date_of_birth < DATE('1999-04-15')
```
3

<details>
<summary>Explanation</summary>

Here the output should be the numbers of students that were born before the 15th of April 1999. Let’s go through the code step-by-step.
**Query**
```sql
SELECT *
FROM students
```

**Output**
| **id** | **first_name** | **last_name** | **date_of_birth** |
| --- | --- | --- | --- |
| 51759 | Meghan | Peery | 1996-12-26 |
| 53532 | Lashanda | Maglioli | 1999-11-12 |
| 50399 | Jamey | Sobotta | 1999-01-07 |
| 59587 | Julianna | Ravitz | 1998-03-29 |
| 53646 | Sylvester | Sampere | 2000-07-07 |

```sql
SELECT *
FROM students
WHERE date_of_birth < DATE('1999-04-15')
```

```sql
SELECT COUNT(*)
FROM students
WHERE date_of_birth < DATE('1999-04-15')
```
| **id** | **first_name** | **last_name** | **date_of_birth** |
| --- | --- | --- | --- |
| 51759 | Meghan | Peery | 1996-12-26 |
| 50399 | Jamey | Sobotta | 1999-01-07 |
| 59587 | Julianna | Ravitz | 1998-03-29 |
3

</details>
---
## Question 3
In your database, you have at least the following five tables (same as in Assignment 07):
- **students (id, first_name, last_name, date_of_birth)**
- **registrations (id, student_id, immatriculation, exmatriculation)**
- **courses (id, name, category)**
- **enrollments (id, student_id, course_id, semester)**
- **grades (id, enrollment_id, grade)**

Which one of the following queries returns all students that have a grade better than 5 (which numerically is greater than 5) in the course ‘Fundamentals of Space-Time-Travel’?

❌ **Query 1**
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade < 5
	AND
	courses.name = 'Fundamentals of Space-Time-Travel'
GROUP BY
	courses.id
```
✅ **Query 2**
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade > 5
	AND
	courses.name = 'Fundamentals of Space-Time-Travel'
GROUP BY
	students.id
```
❌ **Query 3**
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = grades.id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade > 5
	AND
	courses.name = 'History of Space-Time-Travel'
GROUP BY
	students.id
```
❌ **Query 4**
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
	courses.name = 'History of Space-Time-Travel'
GROUP BY
	students.id
```

<details>
<summary>Explanation</summary>

We want the students with a higher grade than 5.0 in the course History of Space-Time-Travel. Thus, we must look into the different code snippets and check where we find the condition:
```sql
grades.grade > 5
AND
courses.name = 'History of Space-Time-Travel'
```
We can find this condition in the **second** and **fourth** code snippet.
When looking at the fourth code-snippet we can see that the first join is not going to work, as there is no direct relation between **students** and **grades** table. This makes sense as one student can be enrolled into multiple courses and thus have multiple grades and a specific grade, e.g., 5.0, can be achieved by many students. This is why there is a table **enrollments **in between.
To validate, that the second query is correct, let’s execute it step by-step.
1. We join enrollments and grades to know all the grades of all the students.
```sql
SELECT *
FROM grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
```

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f8640f82-72d0-485f-ac2d-1c5b0a940cce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MQ5BXZV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIE6Gb6bX2Bp0hBSWNK%2FZe3sQkmMk9YCVTAlJHU83FBMPAiB4%2BQ6%2FZM8Daa8mTNa1Z%2BYJ0jpGqZ%2F1UzNmZuEwnw4K%2BSr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIM57uDmys8IqP1WK2WKtwDLI4kkS4Na0JL7dQumYjNvRvUV9remo6ItpRn7%2BVqPrYrjZ%2FoZcdfB%2FkJH0eKUQHLD35eKEj4eiVCR3kOJAI26%2F2FbKcIcifyTjJHPPrnpCEuGuwJuUo08zW56S17VC32spxD%2FiRJADAqqa0xkq0V8AVE6LlRLkaetLqFCC19NONFsPVFrglaSvAK%2BQT1xhKte7Fnkn8bZVzWTeUKxD6oOph%2BDRSGVHggpZfqkL%2FmcWNE6pH%2BWXZ2QAWkrNyzFcm2Kno60ukDB0E%2FlC1sIaOmYJVJTaXfIhoiPfUI70zFxaQnDgeLMlvP2b65su7sZb2KYIOLL7lB91B5X0x43Qy6SvURdvnDDGqiMaAF31LIOcCdx4ieE%2BR2ytQyTxhXtNfwmsG4vsY%2Brw86yjmMXFd20RykQgzuYsYncQk%2BOmZQeVcPxRBjVklgUuAAAWcrxnZ67UqkmdLYV5RANH%2B1zpmBraa0uzWNF5WxexxrFlq4ra4RZKwIOCFG0KtPTJNbJM6wjMNmXt7xeeGTgElD%2BGTuJDnNCM%2B1LV9tpQTFCKzA6O1zCw9pYYMI1y2yL%2F80sMuCQHFOMEhXu8F4NjQdLsLSIfs%2BDtV%2F1F7LuQsiSM%2BOQs72YcnrRehifj6U%2B5owvs73yQY6pgG6nJ3mChfm6GNamyYgE0QAFe51Nm9AA54OUwu9TkTQ64VOi04KVIXamkTraZ4v3cHqlHpY0E0CIqLMb1RFMP%2Bu0ReQTkBd8dYX2v2rRHXHiB%2BXN1T%2FEBvCe%2F8okLwV8Ek99h07Jdlrz%2BizFsz8dMrf68jb8zQv76SzXkvUt8uJAxKLyw%2Fxw7G%2BZCLSlRvjzSlP2WOOpwQkUp%2FGRbRg%2Bx0Wx8Cr2Eh2&X-Amz-Signature=74e7fb09c40fdde974b22b84c5b999dbd4c6530ffdcbc6a0d25dafde0f41a8c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join courses with enrollments to know which student has achieved which grade.
```sql
SELECT *
FROM grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fcd7ff2b-aa13-486f-b950-463a2c9048b6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y626XCDN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIHAHiX4SCPdbYGv6Fi4wSRjXgWlY0hW9LUEEeVtAdByIAiEAu5Y83gy7ACwho80YRu5%2Bje8%2BYYfqfDyHYTvmb5ZS6%2BYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBoNMTM352eHzNeaWyrcA6IUh0PCiWJW6PcRZiTDOW2NOaijhtu4ad2izrKt7fwTIxFoSteMr%2Bj%2F3fvpNgT8iiQMCOWsTnmoaYi0Dhg7fZf3w2B%2F%2FmrHjPKBKeoUSob5EHdXNAN1LzlDD8YBcRNTFsNLqQtBwvIar7qf3p71jMKnI4YuZ3mZEZLZqDF4Y6qx2NqoNRRAwJVDClkdJ9KGtr8QcxKtcz9%2FVvd7vvxDpGwcn5FtTAt2Q5TmnJ0SB%2FAjoZ%2BLDFHJfyDKBaotIsLTVMupHPE3jRqZ6FEDgf4hVP7p7brQklRWcKuS%2FZG%2BYlUyECL74iCaEv0okv9hADZp3LBTUDhBX0KfZhKd2PGhUURuneQXBEcu5yRq44dpFQ2vwjBXt%2FiUbApEyqXOysDtOT7yW5jDDoossYLVVqLYQESzWupUHA0CSwlkMhOAg%2FHLDePN3%2B1FUMK2Rm2iDxHdQC7G78qjt9XtpuaihBBjyEODVyxbXgPHDGJZFHzscaR%2BmruTs70ebHav0piRYriAqkzyOoUCJGEYl%2FLOps114nom9egqmUsTt46cb9RRceQRw2QSshynxpQdZTiS1L31VIQHNBlSQBTcu%2F2Q%2BikQLmOPLXUmUUnc4jdIaFIgXE9gk8d%2BqpJj07GcgqufMLbO98kGOqUB5uQpPXquxLgV%2BjbI3qHnql80cyU%2FAYylAVeWc93BHOnVO4EDGE9NeaApMaEf8ojYI71Y76QnmO4XasIDV3x4MtdGFPFQm2AIY6omBlH6SV2FvkFJf%2Fedcxjci5pgXBsuXw2tKNiE7GvsRh8UWN%2Fxj3lhhbtEfz7msHtxrx%2FTg3Ssh7%2BESfbfILBYNteboPR1YGB3E6908DsnsUoAEHQldhTXuKnM&X-Amz-Signature=cef584b4808a5e71a6f6042871d7b0fc0cb863a19dc66cad76d805b3d703e4cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join the courses table to see in which course the grade was achieved.
```sql
SELECT *
FROM grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8ab9b52d-3764-4ef5-9bec-045d82960315/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEW5TWXK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCykZuV5%2FNp2w02dYtp%2FVIOCEmkEllS5vWFKAcudxu%2FKAIhAMxQC4TKOTJH7E2bWfLbrjsUh%2BEMUCmXdG04B9JMLDz8Kv8DCCgQABoMNjM3NDIzMTgzODA1Igwx7U2eNivImjlg5ukq3ANNcoQ9dqLHImYeb01U7sMY4Ij7o1HUU56QJHYo3R9fk3SiB%2F%2FUBmmdQVprU15rSkh4s22u8wcx1GcgQqpo31DSq3LBMX8hRpOtFyCJsfOD%2BvwFl%2BCyxj%2F8Kul2cZGRTAZj4BIgBSL7c5rOfE4oqnmq9OrTJ6eD%2FaXu%2BXp2t1KvqpYAioLWVvc7uiffUZtiz86Qz85PGkZipQBojXjGmoyRvG%2FLYCi2xSeqgZGh9Q1o06WU1UQT9CE4c%2BK2tutBgnqYq4goKetM1XXwJDuKRp3nNH4x5ByR95F1yW8RefhPADJhc3IRw6Xd6QuUu3xYrc8Cx0%2FlyzgnBoAfnJfX9GBUPEFFD2J8SzZXDemAHkoB%2FmVWcb7%2B8Nc5AW4T%2F2kMdQdnzse7lo%2B6mqT%2FW%2Bwul23aJJO1AcVy1l8NBt%2BjY7KJ%2BeUskjuSh6oyohP392WB8DLKm1hhWlSEARiwFvikAM6ux35XV%2FzXbimkAsCTD28NzyMSVgxLPMzblnNpRMH1swRfGyIn86CY5WvC9FsUkv%2FNK4kSStHeivhrd3HsPvJdpsv2bYmDrUA9URObNzh0j4fyqAD5z59%2F9og55G6W6JpCMl3PxFJ4kFUrYoMYGps0t3jrzpHYcGrzwvnmJDC%2BzvfJBjqkAdj0IWW1MoTHkolLMhPciZQUzVba7eA4PtEKWMdofP16u973UACk3WBTgKVyPN4tBEIRRMnb5Qx8%2B41iPzeUFBnOdjBNG7lB%2FiEg%2FPvyOHJobkT5B8D1cKKeEz0behrCgx%2BkEI67TT9b9nOFrwidUkb1ZxY%2BOS88CZ1mFkrWZcN2jTqD9hdDonmFbC%2F%2FQAGHpDkdcYJ%2BQvpOIcvhUbDb9nTPK4ni&X-Amz-Signature=46be4b62dc939d49f9eb9d6d62d77780e105675a33cb640c08b09411e63aee51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We can now start filtering our data table and select only the records that have a grade higher than 5.0 in the course 'History of Space-Time-Travel'.
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade > 5
	AND
	courses.name = 'Fundamentals of Space-Time-Travel'
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/236210d3-f5a0-47d4-abe4-d2c76f246867/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBGAH2IZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIENjvp1u6Hr%2BVGDvOI2ZAEr98dTFWEl%2Fm7ZTe7iiUundAiEAzsWYCW7zB0B4XkftlJDY%2Bu%2BHeedyg38ojcNDkbvWGZIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJsBphh7KpIco75ZNircA8aRUvhLq5yIFdHmsuTLOba2xhdklFPCMtRuCroWqCmVwPlqQPS3u5rNYT4pc11%2FC3gv1zcX%2BRULw%2F3HBAy8WgHZVnoKt1ic3cTPdvC90DmfAnvIP0m8BllHkZq0DBNVQWR2Zu7N7d4vcbp17DgwwHMs5Gu5MLVjoIKw0JHvZnA9iCviYadVwLk%2FQrwVk34qT9cb3B5Tkue87%2FwPjMr9V5pzXBSDefxrHYn%2FikGYnY%2Blsib%2Bb6EjSWLAUanDvOfb3UH6qZkI8arnF7ElXlVBpkKhMGftS%2FyUgYJlXIqB8Z1MgVbp3KQ4dvWpMdkmMb8O7NKCvtXJMCVn%2FhdwY%2FheMznZmSoEZtiOH5EW0%2F3BrTzryX07De8b63R44JEdfZ1fZ9xQCda9TWfo9xROJqV5GI8XQwOBN5gvZTXtizD7QYCcW6CMcyke4FI%2BroL7ssGB9aWj5BgP%2Fe2Jj3LpvQS0Hdy60g73KqA57rYqjKVAsrZxcTr61gXukkb78iY625e6YZ8aCqqR14TonwI75rac2U%2FsWvr5anwtMBM2oO6cCk3RosdhOHmy0YCYrUEW4OBjJMsGCNEbFX9x6jF1FxDsKKa9RyEp3LmuGeT%2Fyi9iVOamnc%2FFZRERYuriY36MMJjO98kGOqUBTIOuomz%2Bj8zwgyFQMQnpo5l1L8lptchbkQDsy5FocXeTQCmoCrafg4o44QHh6ewAqrcxA5%2F%2FMJctTMZv0J4aKqGXAfzJyILm0kFpQUH9ykCcnp4sqF0JPtlPmztbZrqbTjBAUopXy62lYTttDBXsETfMHkwEPlXAU4PEpuRtskhkEpHWQ7LLIWcVF2qwjeTlCAebmL7Xkw8yPOpGROIBimjZmZi7&X-Amz-Signature=7e1feb64c75452a88d3de1c4155c47b93d4c98030e20931c29844552ea0dde53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We can now group the records by student and select the relevant columns only.
```sql
SELECT
	students.id, grades.grade, students.first_name, students.last_name
FROM
	grades
INNER JOIN enrollments
	ON enrollments.id = grades.enrollment_id
INNER JOIN students
	ON sutdents.id = enrollments.student_id
INNER JOIN courses
	ON courses.id = enrollments.course_id
WHERE
	grades.grade > 5
	AND
	courses.name = 'Fundamentals of Space-Time-Travel'
GROUP BY
	students.id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b033da62-45a0-473a-b625-896edcb536f3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W3JJ6RX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICH4Si%2FjGN7OybU4RozIjhKp5GG2ypsnIRH1bKPsTbO4AiBjRRPbsRQnbZH41GuUmF%2FlJWGl1WvbOubhEEyuSQWtJSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMdrL%2FILZNDHZlY5AZKtwDXfreS%2BIGsFbODrUA%2FgVH8Ep1JUXNdS2wH5Dihpry8%2FM%2Fv2pmA3Wgdv%2FKFhxT%2B4sGqhNz4zfKnBV6PsRvSkz3MFcIDTgd4TvIwSsO3xbmYWXxGEAkGTD97N48ixZ0fRkOYPC%2FBYDLMqK0ljT6zHezs54LORDcUahlXFmPQihcZA4cqlDt09eOk0Wq%2B3KTezAUNOidL1bYVx9mwhLPZKSbld8yhQDbyYhiuQmNxy%2BCdHft%2FFMffAVtrBEa%2FS6HZLgbCevpucdb78wqWtZVS9Q8TGjbmdchTpZ2yihnt4nqsqKH%2FRADasaXF2G%2FZxTsPS7nJjMqIC2kohpgqk0WkVNHy%2FdbWJAJgyvPRgBO4V68%2FJocMaxnODfZEtXcVhyvENOZBi0vpwpffE5TxxanKUcEBUTGVmURtlbSUk%2Bbc%2Fy2hL8mRVHVl4PLLdtFPePRWkrp0RQW9dwwjBDIn9j9g0%2FsoKaZJiBVsMWzhjmAqaLC6qFPFb98r9VFHRy2%2Fzm66%2BJk5LFdPn9iGZEab9Fj3o%2F6H%2FqtbX11KA0Y0sBwX2MlJfQZ%2FZpNJTQDafruf02K632tIKTxqRybxrFL7l9ghXtlatvs0lmfcN%2BFLj%2FvvvNdNY0lVOVbDD5RXDkvQTAw5s33yQY6pgHAokIqvRlJfhWP3iCayJayn%2Bf1Q6QAbSiqMffwHF33H4AHcPtr5VD1qFZ0uz0EyMQy8qC%2FNOAurduIc5ZjyZtyld2x2XNw3zIXKiwubRm%2FZvaDiXewz9%2B%2B2vN70Gqe5Yqvp7Qsgjwfllluo6e7xeESjLIRqabMBroJlZl1xirdp5OO8wjX4%2BXQ1iAvJstJzuHraFCsX0S7IuEKPbre4U14gXTp4jMB&X-Amz-Signature=842c07f4739f26f59ffefcba68ade244b94a6c8e675053f983232ba7052fb3b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
## Question 4
What happens if there is <u>no</u> **WHERE** statement in an **UPDATE** query?
❌ There is no restriction, so no entry in the chosen table will be overwritten.
✅ There is no restriction, so all entries in the chosen table will be overwritten.
❌ A syntax error will appear because updating entries in a table id done with the **INSERT** query.
❌ A syntax error will appear because an **UPDATE** query requires a **WHERE** statement.

<details>
<summary>Explanation</summary>

❌ **Incorrect**, because the second statement is correct.
✅ **Correct.** [Check this](https://stackoverflow.com/questions/12163047/update-query-without-where-clause).
❌ **Incorrect.** We use `INSERT` to add a new record to a data table
❌ **Incorrect**. It is** **not mandatory to define `WHERE` statement.
</details>
---
## Question 5
Given the following table students:
| **id** | **first_name** | **last_name** | **date_of_birth** |
| --- | --- | --- | --- |
| 51759 | Preston Omer | Haumesser | 1998-05-30 |
| 53532 | Julio Quinton | Shain | 1998-07-03 |
| 50399 | Van | Sokoloski | 1999-11-30 |
| 59587 | Lyman Richie Tracey | Elgin | 1998-05-31 |
| 53646 | Dale | Oviatt | 2001-11-11 |
Which query will return the entire tuple *Van Sokoloski*?
```sql
**SELECT** *
**FROM** students
**WHERE **id = **52819**
```

<details>
<summary>Explanation</summary>

Here we can simply select the student Van Sokoloski over its ID. So SQL looks into the column **id** and returns the row / tuple that contains **52819 **as value of that column.
</details>
---
