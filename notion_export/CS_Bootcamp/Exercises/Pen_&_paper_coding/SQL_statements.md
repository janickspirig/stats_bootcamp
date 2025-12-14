---
title: "SQL statements"
notion_id: "2fd2d572-4a76-49b6-a79b-4f09a37fc554"
notion_url: "https://www.notion.so/SQL-statements-2fd2d5724a7649b6a79b4f09a37fc554"
exported_at: "2025-12-13T22:47:29.340540+00:00"
---

# SQL statements

## Question 1 - Basic queries
Write a SQL query to retrieve specific information from a 'students' table. The table has the following columns: `id`, `name`, `age`, `grade`, and `city`.
1. Write a query to select all the columns for students who are older than 20.
1. Write a query to select the `name` and `grade` columns for students who have a grade higher than 75.
1. Write a query to select the `name` column for students who are from the city 'New York'.
Here is what the `students` table looks like:
```plain text
Students
-------------------------------------------
| id | name     | age | grade | city      |
|----|----------|-----|-------|-----------|
| 1  | Alice    | 19  | 85    | New York  |
| 2  | Bob      | 21  | 78    | Los Angeles|
| 3  | Charlie  | 22  | 90    | New York  |
| 4  | David    | 20  | 65    | Chicago   |
| 5  | Eve      | 23  | 72    | New York  |
```

<details>
<summary>Solution Query 1 </summary>

```sql
SELECT *
FROM students
WHERE age > 20;
```
<details>
<summary>Line-by-line explanation</summary>

1. *SELECT :*
This line indicates that all columns should be selected.
```sql
SELECT *
```
1. **FROM students:**
This line specifies that the data is being retrieved from the 'students' table.
```sql
FROM students
```
1. **WHERE age > 20:**
This line specifies the condition for selecting rows where the `age` column is greater than 20.
```sql
WHERE age > 20;
```
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT name, grade
FROM students
WHERE grade > 75;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT name, grade:**
This line specifies that only the `name` and `grade` columns should be selected.
```sql
SELECT name, grade
```
1. **FROM students:**
This line specifies that the data is being retrieved from the 'students' table.
```sql
FROM students
```
1. **WHERE grade > 75:**
This line specifies the condition for selecting rows where the `grade` column is greater than 75.
```sql
WHERE grade > 75;
```
</details>
---
</details>
<details>
<summary>Solution Query 3</summary>

```sql
SELECT name
FROM students
WHERE city = 'New York';
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT name:**
This line specifies that only the `name` column should be selected.
```sql
SELECT name
```
1. **FROM students:**
This line specifies that the data is being retrieved from the 'students' table.
```sql
FROM students
```
1. **WHERE city = 'New York':**
This line specifies the condition for selecting rows where the `city` column is equal to 'New York'.
```sql
WHERE city = 'New York';
```
</details>
</details>
---
## Question 2 - Basic queries
You are given a table named `Sales` with the following schema:
```plain text
Sales
-------------------------
| id | product | amount |
-------------------------
| 1  | A       | 100    |
| 2  | B       | 200    |
| 3  | A       | 150    |
| 4  | C       | 300    |
| 5  | B       | 100    |
| 6  | C       | 200    |
| 7  | A       | 250    |
| 8  | B       | 300    |
-------------------------
```
Write two SQL queries:
1. Write a query to find all the unique products sold.
Sample output:
```plain text
| product |
-----------
| A       |
| B       |
| C       |
```
1. Write a query to find the total sales amount for each product.
Sample output:
```plain text
| product | total_sales |
-------------------------
| A       | 500         |
| B       | 600         |
| C       | 500         |
```

<details>
<summary>Solution Query 1</summary>

```sql
SELECT DISTINCT product
FROM Sales;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT DISTINCT Clause**:
```sql
SELECT DISTINCT product
```
This part of the query selects unique (distinct) values of the `product` column from the `Sales` table. The `DISTINCT` keyword ensures that duplicate values are removed from the result set.
1. **FROM Clause**:
```sql
FROM Sales;
```
This part of the query specifies the table from which to retrieve the data, which is the `Sales` table.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT product, SUM(amount) as total_sales
FROM Sales
GROUP BY product;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause with Aggregation**:
```sql
SELECT product, SUM(amount) as total_sales
```
This part of the query selects the `product` column and calculates the sum of the `amount` column for each product. The `SUM` function is used to compute the total sales amount, and the result is given an alias `total_sales`.
1. **FROM Clause**:
```sql
FROM Sales
```
This specifies the table from which to retrieve the data, which is the `Sales` table.
1. **GROUP BY Clause**:
```sql
GROUP BY product;
```
This part of the query groups the rows in the `Sales` table by the `product` column. For each group, the `SUM(amount)` function calculates the total sales amount.
</details>
</details>
---
## Question 3 - Basic queries
Imagine you are given a table named `students` with the following structure and sample data:
```plain text
Students
| id  | name   | age | major        |
|-----|--------|-----|--------------|
| 1   | Alice  | 20  | Computer Sci |
| 2   | Bob    | 21  | Math         |
| 3   | Carol  | 20  | Computer Sci |
| 4   | Dave   | 21  | Engineering  |
| 5   | Eve    | 22  | Math         |
| 6   | Frank  | 20  | Engineering  |
| 7   | Grace  | 21  | Computer Sci |
```
Write two SQL queries based on this table:
1. Write a query using the `SELECT DISTINCT` statement to find all unique majors in the `students` table.
1. Write a query using the `GROUP BY` statement to find the count of students in each major.

<details>
<summary>Solution Query 1</summary>

```sql
SELECT DISTINCT major
FROM students;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT DISTINCT Clause**:
```sql
SELECT DISTINCT major
```
This line specifies that you want to select unique values from the `major` column. The `DISTINCT` keyword ensures that duplicate values are removed from the result set.
1. **FROM Clause**:
```sql
FROM students;
```
This line indicates that the data is being selected from the `students` table.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT major, COUNT(*) AS student_count
FROM students
GROUP BY major;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT major, COUNT(*) AS student_count
```
This line specifies that you want to select the `major` column and the count of rows for each major. The `COUNT(*)` function counts the number of rows in each group, and the result is aliased as `student_count` for readability.
1. **FROM Clause**:
```sql
FROM students
```
This line indicates that the data is being selected from the `students` table.
1. **GROUP BY Clause**:
```sql
GROUP BY major;
```
This line groups the result set by the `major` column. The `COUNT(*)` function counts the number of rows in each group.
</details>
</details>
---
## Question 4 - Basic queries
You are given a table named `Orders` with the following schema:
```plain text
Orders
--------------------------------
| order_id | customer_id | status |
--------------------------------
| 1        | 101         | shipped |
| 2        | 102         | pending |
| 3        | 103         | shipped |
| 4        | 101         | pending |
| 5        | 104         | shipped |
| 6        | 105         | canceled |
| 7        | 102         | shipped |
| 8        | 104         | pending |
--------------------------------
```
Write two SQL queries:
1. Write a query to count the total number of orders that have been shipped.
Sample output:
```plain text
| total_shipped |
-----------------
| 4             |
```
1. Write a query to count the number of orders placed by each customer.
Sample output:
```plain text
| customer_id | order_count |
-----------------------------
| 101         | 2           |
| 102         | 2           |
| 103         | 1           |
| 104         | 2           |
| 105         | 1           |
```

<details>
<summary>Solution Query 1</summary>

```sql
SELECT COUNT(*) as total_shipped
FROM Orders
WHERE status = 'shipped';
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT COUNT(*) Clause**:
```sql
SELECT COUNT(*) as total_shipped
```
This part of the query counts all rows in the result set. The `COUNT(*)` function calculates the total number of rows, and the result is given an alias `total_shipped`.
1. **FROM Clause**:
```sql
FROM Orders
```
This specifies the table from which to retrieve the data, which is the `Orders` table.
1. **WHERE Clause**:
```sql
WHERE status = 'shipped';
```
This filters the rows to include only those where the `status` column is equal to 'shipped'.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT customer_id, COUNT(*) as order_count
FROM Orders
GROUP BY customer_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause with Aggregation**:
```sql
SELECT customer_id, COUNT(*) as order_count
```
This part of the query selects the `customer_id` column and calculates the number of orders for each customer. The `COUNT(*)` function is used to count the number of rows for each group, and the result is given an alias `order_count`.
1. **FROM Clause**:
```sql
FROM Orders
```
This specifies the table from which to retrieve the data, which is the `Orders` table.
1. **GROUP BY Clause**:
```sql
GROUP BY customer_id;
```
This part of the query groups the rows in the `Orders` table by the `customer_id` column. For each group, the `COUNT(*)` function calculates the number of orders.
</details>
</details>
---
## Question 5 - Basic queries
You are given a table named `StudentGrades` with the following schema:
```plain text
StudentGrades
-----------------------------------
| student_id | course | grade     |
-----------------------------------
| 1          | Math   | 85        |
| 2          | Math   | 90        |
| 3          | Physics| 75        |
| 4          | Math   | 88        |
| 5          | Physics| 95        |
| 6          | Math   | 92        |
| 7          | Physics| 80        |
| 8          | Chemistry | 70     |
| 9          | Chemistry | 60     |
-----------------------------------
```
Write two SQL queries:
1. Write a query to find the average grade for each course.
Sample output:
```plain text
| course    | average_grade |
-----------------------------
| Math      | 88.75         |
| Physics   | 83.33         |
| Chemistry | 65.00         |
```
1. Write a query to find the average grade for courses where the average grade is above 80.
Sample output:
```plain text
| course  | average_grade |
---------------------------
| Math    | 88.75         |
| Physics | 83.33         |
```

<details>
<summary>Solution 1</summary>

```sql
SELECT course, AVG(grade) as average_grade
FROM StudentGrades
GROUP BY course;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause with Aggregation**:
```sql
SELECT course, AVG(grade) as average_grade
```
This part of the query selects the `course` column and calculates the average of the `grade` column for each course. The `AVG` function is used to compute the average grade, and the result is given an alias `average_grade`.
1. **FROM Clause**:
```sql
FROM StudentGrades
```
This specifies the table from which to retrieve the data, which is the `StudentGrades` table.
1. **GROUP BY Clause**:
```sql
GROUP BY course;
```
This part of the query groups the rows in the `StudentGrades` table by the `course` column. For each group, the `AVG(grade)` function calculates the average grade.
</details>
---
</details>
<details>
<summary>Solution 2</summary>

```sql
SELECT course, AVG(grade) as average_grade
FROM StudentGrades
GROUP BY course
HAVING AVG(grade) > 80;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause with Aggregation**:
```sql
SELECT course, AVG(grade) as average_grade
```
This part of the query selects the `course` column and calculates the average of the `grade` column for each course. The `AVG` function is used to compute the average grade, and the result is given an alias `average_grade`.
1. **FROM Clause**:
```sql
FROM StudentGrades
```
This specifies the table from which to retrieve the data, which is the `StudentGrades` table.
1. **GROUP BY Clause**:
```sql
GROUP BY course
```
This part of the query groups the rows in the `StudentGrades` table by the `course` column. For each group, the `AVG(grade)` function calculates the average grade.
1. **HAVING Clause**:
```sql
HAVING AVG(grade) > 80;
```
This part of the query filters the grouped results to include only those groups (courses) where the average grade is greater than 80. The `HAVING` clause is used to apply this condition after the groups have been formed.
</details>
</details>
---
## Question 6 - Basic queries
You are given a table named `Employees` with the following schema:
```plain text
Employees
--------------------------------------------
| id | name       | department | salary |
--------------------------------------------
| 1  | John Doe   | HR         | 50000  |
| 2  | Jane Smith | IT         | 75000  |
| 3  | Bob Brown  | IT         | 72000  |
| 4  | Alice Blue | Finance    | 55000  |
| 5  | Carol White| IT         | 73000  |
| 6  | Eve Black  | HR         | 51000  |
| 7  | Frank Gray | Finance    | 54000  |
| 8  | Grace Green| IT         | 70000  |
--------------------------------------------
```
Write two SQL queries:
1. Write a query to find the top 3 highest paid employees.
Sample output:
```plain text
| id | name       | department | salary |
----------------------------------------
| 2  | Jane Smith | IT         | 75000  |
| 5  | Carol White| IT         | 73000  |
| 3  | Bob Brown  | IT         | 72000  |
```
1. Write a query to list all employees in the IT department, ordered by their salary in descending order.
Sample output:
```plain text
| id | name       | department | salary |
----------------------------------------
| 2  | Jane Smith | IT         | 75000  |
| 5  | Carol White| IT         | 73000  |
| 3  | Bob Brown  | IT         | 72000  |
| 8  | Grace Green| IT         | 70000  |
```

<details>
<summary>Solution Query 1</summary>

```sql
SELECT id, name, department, salary
FROM Employees
ORDER BY salary DESC
LIMIT 3;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT id, name, department, salary
```
This part of the query selects the `id`, `name`, `department`, and `salary` columns from the `Employees` table.
1. **FROM Clause**:
```sql
FROM Employees
```
This specifies the table from which to retrieve the data, which is the `Employees` table.
1. **ORDER BY Clause**:
```sql
ORDER BY salary DESC
```
This part of the query orders the rows in the result set by the `salary` column in descending order (i.e., highest salary first).
1. **LIMIT Clause**:
```sql
LIMIT 3;
```
This part of the query limits the result set to only the top 3 rows, which are the highest paid employees.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT id, name, department, salary
FROM Employees
WHERE department = 'IT'
ORDER BY salary DESC;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT id, name, department, salary
```
This part of the query selects the `id`, `name`, `department`, and `salary` columns from the `Employees` table.
1. **FROM Clause**:
```sql
FROM Employees
```
This specifies the table from which to retrieve the data, which is the `Employees` table.
1. **WHERE Clause**:
```sql
WHERE department = 'IT'
```
This part of the query filters the result set to include only those rows where the `department` is 'IT'.
1. **ORDER BY Clause**:
```sql
ORDER BY salary DESC;
```
This part of the query orders the rows in the result set by the `salary` column in descending order (i.e., highest salary first).
</details>
</details>
---
## Question 7 - Basic queries
You are given a table named `Employees` with the following schema:
```plain text
Employees
--------------------------------
| id | name    | position | salary |
--------------------------------
| 1  | Alice   | Manager  | 90000  |
| 2  | Bob     | Engineer | 75000  |
| 3  | Charlie | Engineer | 76000  |
| 4  | David   | Manager  | 88000  |
| 5  | Eve     | Engineer | 72000  |
--------------------------------
```
1. Write an SQL query to update the salary of all Engineers by increasing it by 10%.
Sample output after the update:
```plain text
Employees
--------------------------------
| id | name    | position | salary |
--------------------------------
| 1  | Alice   | Manager  | 90000  |
| 2  | Bob     | Engineer | 82500  |
| 3  | Charlie | Engineer | 83600  |
| 4  | David   | Manager  | 88000  |
| 5  | Eve     | Engineer | 79200  |
--------------------------------
```
1. Write an SQL query to update the position of the employee `David` to `Senior Manager`.
Sample output after the update:
```plain text
Employees
--------------------------------
| id | name    | position       | salary |
--------------------------------
| 1  | Alice   | Manager        | 90000  |
| 2  | Bob     | Engineer       | 82500  |
| 3  | Charlie | Engineer       | 83600  |
| 4  | David   | Senior Manager | 88000  |
| 5  | Eve     | Engineer       | 79200  |
--------------------------------
```

<details>
<summary>Solution Query 1</summary>

```sql
UPDATE Employees
SET salary = salary * 1.1
WHERE position = 'Engineer';
```
<details>
<summary>Line-by-line explanation</summary>

1. **UPDATE Clause**:
```sql
UPDATE Employees
```
This part of the query specifies the table to be updated, which is the `Employees` table.
1. **SET Clause**:
```sql
SET salary = salary * 1.1
```
This part sets the new value for the `salary` column. It multiplies the current `salary` by 1.1 to increase it by 10%.
1. **WHERE Clause**:
```sql
WHERE position = 'Engineer';
```
This part of the query specifies the condition for the rows to be updated. Only the rows where the `position` is 'Engineer' will have their salaries updated.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
UPDATE Employees
SET position = 'Senior Manager'
WHERE name = 'David';
```
<details>
<summary>Line-by-line explanation</summary>

1. **UPDATE Clause**:
```sql
UPDATE Employees
```
This part of the query specifies the table to be updated, which is the `Employees` table.
1. **SET Clause**:
```sql
SET position = 'Senior Manager'
```
This part sets the new value for the `position` column. It changes the `position` to 'Senior Manager'.
1. **WHERE Clause**:
```sql
WHERE name = 'David';
```
This part of the query specifies the condition for the rows to be updated. Only the row where the `name` is 'David' will have its position updated.
</details>
</details>
---
## Question 8 - Basic queries
You are given a table named `Students` with the following schema:
```plain text
Students
-------------------------
| id | name    | grade  |
-------------------------
| 1  | Alice   | A      |
| 2  | Bob     | B      |
| 3  | Charlie | C      |
| 4  | Diana   | B      |
-------------------------
```
Write two SQL queries:
1. Write a query to add a new student named "Eve" with an id of 5 and a grade of "A".
1. Write a query to add two new students, "Frank" with an id of 6 and a grade of "B", and "Grace" with an id of 7 and a grade of "A" in one single query.

<details>
<summary>Solution Query 1</summary>

```sql
INSERT INTO Students (id, name, grade)
VALUES (5, 'Eve', 'A');
```
<details>
<summary>Line-by-line explanation</summary>

1. **INSERT INTO Clause**:
```sql
INSERT INTO Students (id, name, grade)
```
This part of the query specifies that we are inserting a new row into the `Students` table. The columns `id`, `name`, and `grade` are listed to indicate where the new values should be inserted.
1. **VALUES Clause**:
```sql
VALUES (5, 'Eve', 'A');
```
This part of the query provides the values to be inserted into the specified columns. Here, `5` is the `id`, `'Eve'` is the `name`, and `'A'` is the `grade`.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
INSERT INTO Students (id, name, grade)
VALUES
    (6, 'Frank', 'B'),
    (7, 'Grace', 'A');
```
<details>
<summary>Line-by-line explanation</summary>

1. **INSERT INTO Clause**:
```sql
INSERT INTO Students (id, name, grade)
```
Similar to the first query, this part of the query specifies that we are inserting new rows into the `Students` table. The columns `id`, `name`, and `grade` are listed to indicate where the new values should be inserted.
1. **VALUES Clause**:
```sql
VALUES
    (6, 'Frank', 'B'),
    (7, 'Grace', 'A');
```
This part of the query provides the values to be inserted into the specified columns. Here, two sets of values are provided, `(6, 'Frank', 'B')` for the first new student and `(7, 'Grace', 'A')` for the second new student. Both sets of values are separated by commas and enclosed within parentheses, allowing multiple rows to be inserted in a single `INSERT INTO` statement.
</details>
</details>
---
## Question 9 - Basic queries
You are given two tables named `Customers` and `Orders` with the following schema:
```plain text
Customers
-------------------------
| id | name         | age |
-------------------------
| 1  | John Doe     | 30  |
| 2  | Jane Smith   | 25  |
| 3  | Sam Brown    | 40  |
| 4  | Lucy Green   | 35  |
-------------------------
```
```plain text
Orders
----------------------------------
| order_id | customer_id | amount |
----------------------------------
| 101      | 1           | 250    |
| 102      | 2           | 150    |
| 103      | 2           | 200    |
| 104      | 3           | 300    |
| 105      | 5           | 350    |
----------------------------------
```
Write the following SQL queries:
1. Write a query to find all customers who have placed an order.
Sample output:
```plain text
| id | name       | age | order_id | amount |
---------------------------------------------
| 1  | John Doe   | 30  | 101      | 250    |
| 2  | Jane Smith | 25  | 102      | 150    |
| 2  | Jane Smith | 25  | 103      | 200    |
| 3  | Sam Brown  | 40  | 104      | 300    |
```
1. Write a query to find all customers and their orders.
Sample output:
```plain text
| id | name       | age | order_id | amount |
---------------------------------------------
| 1  | John Doe   | 30  | 101      | 250    |
| 2  | Jane Smith | 25  | 102      | 150    |
| 2  | Jane Smith | 25  | 103      | 200    |
| 3  | Sam Brown  | 40  | 104      | 300    |
| 4  | Lucy Green | 35  | NULL     | NULL   |
```
1. Write a query to find all orders and their customers.
Sample output:
```plain text
| id | name       | age | order_id | amount |
---------------------------------------------
| 1  | John Doe   | 30  | 101      | 250    |
| 2  | Jane Smith | 25  | 102      | 150    |
| 2  | Jane Smith | 25  | 103      | 200    |
| 3  | Sam Brown  | 40  | 104      | 300    |
| NULL | NULL    | NULL | 105      | 350    |

```
1. Write a query to combine all data from both tables.
Sample output:
```plain text
| id  | name       | age  | order_id | amount |
----------------------------------------------
| 1   | John Doe   | 30   | 101      | 250    |
| 2   | Jane Smith | 25   | 102      | 150    |
| 2   | Jane Smith | 25   | 103      | 200    |
| 3   | Sam Brown  | 40   | 104      | 300    |
| 4   | Lucy Green | 35   | NULL     | NULL   |
| NULL| NULL       | NULL | 105      | 350    |

```

<details>
<summary>Solution Query 1</summary>

```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
FROM Customers
INNER JOIN Orders ON Customers.id = Orders.customer_id;

```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.customer_id, Customers.customer_name, Orders.order_id, Orders.amount
```
This part of the query selects the `customer_id` and `customer_name` columns from the `Customers` table, and the `order_id` and `amount` columns from the `Orders` table.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies the `Customers` table as the source table for the query.
1. **LEFT JOIN Clause**:
```sql
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id;
```
This part of the query performs a LEFT JOIN between the `Customers` and `Orders` tables based on the `customer_id` column that they have in common. It returns all rows from the `Customers` table and the matching rows from the `Orders` table. If there is no match, the result is NULL on the side of the `Orders` table.
</details>
---
</details>
<details>
<summary>Solution Query 2</summary>

```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
FROM Customers
LEFT JOIN Orders ON Customers.id = Orders.customer_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
```
This part specifies the columns to be retrieved from the `Customers` and `Orders` tables.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies the primary table from which to retrieve data, which is the `Customers` table.
1. **LEFT JOIN Clause**:
```sql
LEFT JOIN Orders ON Customers.id = Orders.customer_id;
```
This part specifies the `LEFT JOIN` operation between the `Customers` table and the `Orders` table on the `id` column of `Customers` and `customer_id` column of `Orders`. It retrieves all rows from the `Customers` table and the matching rows from the `Orders` table. If there is no match, NULL values are returned for columns from the `Orders` table.
</details>
---
</details>
<details>
<summary>Solution Query 3</summary>

```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
FROM Customers
RIGHT JOIN Orders ON Customers.id = Orders.customer_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
```
This part specifies the columns to be retrieved from the `Customers` and `Orders` tables.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies the primary table from which to retrieve data, which is the `Customers` table.
1. **RIGHT JOIN Clause**:
```sql
RIGHT JOIN Orders ON Customers.id = Orders.customer_id;
```
This part specifies the `RIGHT JOIN` operation between the `Customers` table and the `Orders` table on the `id` column of `Customers` and `customer_id` column of `Orders`. It retrieves all rows from the `Orders` table and the matching rows from the `Customers` table. If there is no match, NULL values are returned for columns from the `Customers` table.
</details>
---
</details>
<details>
<summary>Solution Query 4</summary>

```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
FROM Customers
FULL OUTER JOIN Orders ON Customers.id = Orders.customer_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.id, Customers.name, Customers.age, Orders.order_id, Orders.amount
```
This part specifies the columns to be retrieved from the `Customers` and `Orders` tables.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies the primary table from which to retrieve data, which is the `Customers` table.
1. **FULL OUTER JOIN Clause**:
```sql
FULL OUTER JOIN Orders ON Customers.id = Orders.customer_id;
```
This part specifies the `FULL OUTER JOIN` operation between the `Customers` table and the `Orders` table on the `id` column of `Customers` and `customer_id` column of `Orders`. It retrieves all rows when there is a match in one of the tables. If there is no match, NULL values are returned for columns from the non-matching table.
</details>
</details>
---
## Question 10 - Basic queries
You are given three tables: `Customers`, `Orders`, and `Products` with the following schema and 
```plain text
Customers
-------------------------
| id | name   | city    |
-------------------------
| 1  | Alice  | New York|
| 2  | Bob    | Boston  |
| 3  | Carol  | Chicago |
| 4  | Dave   | Dallas  |
-------------------------
```
```plain text
Orders
-------------------------------
| id | customer_id | date      |
-------------------------------
| 1  | 1           | 2023-01-01|
| 2  | 3           | 2023-01-03|
| 3  | 2           | 2023-02-01|
| 4  | 1           | 2023-02-15|
-------------------------------
```
```plain text
Products
-------------------------------
| id | order_id | product_name |
-------------------------------
| 1  | 1        | Laptop       |
| 2  | 1        | Mouse        |
| 3  | 2        | Keyboard     |
| 4  | 3        | Monitor      |
| 5  | 4        | Laptop       |
-------------------------------
```
Write a query to find the name of customers and the products they have ordered. The result should include the customer's name and the product name.
Expected output:
```plain text
-----------------------------
| customer_name | product_name |
-----------------------------
| Alice         | Laptop       |
| Alice         | Mouse        |
| Carol         | Keyboard     |
| Bob           | Monitor      |
| Alice         | Laptop       |
-----------------------------
```

<details>
<summary>Solution</summary>

```sql
SELECT
    Customers.name AS customer_name,
    Products.product_name
FROM
    Customers
JOIN
    Orders ON Customers.id = Orders.customer_id
JOIN
    Products ON Orders.id = Products.order_id;
```
<details>
<summary>Line-by-line explanation</summary>

1. **SELECT Clause**:
```sql
SELECT Customers.name AS customer_name, Products.product_name
```
This part of the query selects the `name` column from the `Customers` table and the `product_name` column from the `Products` table. The `AS` keyword is used to give an alias `customer_name` for the `name` column.
1. **FROM Clause**:
```sql
FROM Customers
```
This specifies that the query will start selecting data from the `Customers` table.
1. **JOIN Clause**:
```sql
JOIN Orders ON Customers.id = Orders.customer_id
```
This joins the `Customers` table with the `Orders` table based on the condition that the `id` column in `Customers` matches the `customer_id` column in `Orders`. This combines rows from both tables where the condition is true.
1. **JOIN Clause**:
```sql
JOIN Products ON Orders.id = Products.order_id;
```
This further joins the resulting table with the `Products` table based on the condition that the `id` column in `Orders` matches the `order_id` column in `Products`. This completes the join across all three tables.
</details>
</details>
---
