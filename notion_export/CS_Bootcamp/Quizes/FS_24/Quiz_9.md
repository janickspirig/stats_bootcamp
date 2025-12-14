---
title: "Quiz 9"
notion_id: "0c05ec58-e033-483b-843b-dcdc7262822e"
notion_url: "https://www.notion.so/Quiz-9-0c05ec58e033483b843bdcdc7262822e"
exported_at: "2025-12-13T23:09:27.534084+00:00"
---

# Quiz 9

# Question 1
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

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9a3dd2fc-d3d3-4f80-a3d1-2525d393e718/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR4RNIHU%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICKT2GI84sTc0XFjCwL57YmuTVdXcnbVpHCoWAJk7y89AiEAyZAN2UuRXNrYerqo2QIrl04LOrO0zCqV9qHJ2B%2FW%2B3Yq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNMhQh0iCw7EZ1DByircA3erk8%2BvwxvmLd8KseplLvrlOaW4zhISSd8SAcmwCK84NN%2FFGEsudSXkYKMDwC5e6X%2Berqk2PuRyjZ9vO75wfKuLBO3CJ2P6pDArZW1J5t46KAru8aD52svPf9zCPzeNDo170aduKhnIBfd562nG1VzxBFuDxauU3Gh7lfsekNOUZHYVCTbGRfj3QCouW6UGKD%2BjfrdsWt91Et69szRYDqgcupoNxZAycnErzkVc35KZMfuDrP45r9pMZV9refkMJ%2BXL3p5t7SHmHjALuIFoavcvLxfOXTMuQplww5ftGOFoJDunNw5ief0HZ7gZQrwkyrrF91HulMB2rzzWM7Hn4ed7V7GEaj8BJO005DgwTHog5qUYSrk9PBsBp9nzsHRL0TQs8jejezCJJul6uiARlPRxr67Yzn8L7ygfMoukR9PbX0Q%2FwOkuagbLcubQR3Pngy9G4I77fJaEDyYZGf87EBHELuwHX%2BBynhdgI67TY3L7SdOHeRnDn0C8zqaEqW04qNQhx7enSreEadAoNpXGSBxYfp7f8vu94VXmFN%2BUFBpLO%2FdcoWGODoQE63TcwyqBmdw46Y3Gn1kirjszQhPt7Q1ai3aoCCTRiippAFsuzZe%2Fw9fjtT1E3i0iDEFuMMXO98kGOqUBBKd101UHjk4IjKpfVeLMq1x4PuXM0gqld6xDd9gKs%2FmXIM0xnYUHYVBqKOmRW%2F%2F4z7zKffbsVS%2BSCDnl1T5JY9hziusTKNiw4Nq0BGnuu2CUGW%2Bf6LXn90qDNPuzRFtKO7rw%2FO60Po3pEDMASOIaUoJHPRTxJcIe3p32xgaVdhFK%2F4E8NjR6Jps%2BfdVOWE%2FQu3bCT5j6wgR1B35Ul6I3Ix%2BZw5p1&X-Amz-Signature=0d3f16e7b8146209df4a3c3364c1a37bc405ee905175611ea455d2d74d4d2a39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. We join **enrollments** with **courses** to know in which course category the grade was achieved.
```sql
SELECT *
FROM grades g
INNER JOIN enrollments e
	ON e.id = g.enrollment_id
INNER JOIN courses c
	ON c.id = e.course_id
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bb58391f-28e2-4b87-9dfa-efb93b3c38dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P2TPYWX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDk8eexPS%2BUyjuT8pBbYue0iXmqGfzYJ3W5X2vq07ZYJwIhANcrEu9ywWgHxFoPxIMnO5C9dgG3JpjYhVNS1lqSxEP4Kv8DCCcQABoMNjM3NDIzMTgzODA1IgxF9sl5vqSLxtTyRsUq3AMLbsdErzGZe3ViTpwovYpuA2Z2pqW7D4xoDO0IwTdEPI9Z1UX3jSBP4B2epXa6%2B1HDnA2LhXKF2oL6%2Bm%2F4lzvE%2F6UClx%2BL3qGFHSoQNEr%2Bn58iS8F4DyBvA2%2FiFyM69CdOVPZTwjyC%2Bz%2F7ewNGrTu6%2F8luF%2FIX%2F%2B%2BOZLkKJccKWVGY9KwVg%2FcHjJyR%2F9hrcznry7laC3GJE7nD47%2FCkElQY4IkV5s76QOqiMq7HuLHjEsxNCzb5pPN6W00QARUMw5ZjVg5BUeXVdvrJiqYlEgj8LdNRf%2Fqj9kd8ioGswR5sCo9N%2B31ClTC4g1NRS6VSkyKnlxJl%2FnAQZUuL6pooymy62J49EjTcVCdvX2Kc5PcTeesiKTAFtr0y7qS2tK2fuIARJM63mslpRwIkhtcPQEyeq%2Bf55s%2FruHGm%2BDFniPjOWY0uJtH0IU5seoPUQwLekApCliRsiro0lkeb6q4m1GjXWnpLMmJOeG3JbyDaSjlxC1QvnHuFJXiqi6nZwm7BLBp%2FaN3RvRSJK3I4nBn5ziUERRAlR%2BZHCiBHzH0fk8LNEUxnuYUFgrQtuuLyXDWPOkw6Di4f4%2FkeCUXA2JtCMzG0l%2BZGJGcCEnfF6s%2BzGSgE5mqst8ONu0iTnUSyjDHzvfJBjqkAaus3pm4kIjGmcMJOH60fT0uJevp88S5Cn4bML%2BOnZgQwSCU6jK4v3lBqem55tZtWq3MwTzw9RaMQ2ymd9Tsc90BY3tDJATrs0a4CM6b5WECSaijS%2FG8lxPAnD694ZJeJUu0j%2BYPAND356G%2FuP32Fuz%2FX2XUUjg%2FOlScHEMy%2Bm4EmDXpgkApTIMYbUSAZ304aJqgwsLhJUhpuDjEK9lrS6aUs1Zf&X-Amz-Signature=5071a1480162767f264fedd42c7179bbf985ff3093078d8f7f05469accf13c62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/34d7ccd1-9629-46da-ab0a-5e19d5df29c6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E7SJINT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDWnwaVLP%2BMKjsGJevrcNbG2nODOetHJtp1Sw3xAFzKcQIhAKtkT6HRc3PaKTdTzpkDpHdw%2FFIoDV9yLQzBKMikLVsMKv8DCCcQABoMNjM3NDIzMTgzODA1IgwmUVKUdvVHO5f5lzsq3AN9LkYwj9HXZ31HXMRTBMR1T7N0zRu23YnIUqZlNk38gbuCpmKLGnDBJPreKAw%2BMnlXzeTBmmhI6EWtYJl9%2Bt%2BrozGsCXXPzLREaRU1e6W3hErE%2FU%2BilkPH60vLa2wIYZGARUK%2BsyOU%2BIqCGwXdswnb2Vax58weyf%2Bl9mSFN7FZbU%2BFa%2FCBtD8agDGr78WR5p%2FQ9r4qm3YmL%2FNqeMGRmPSFvcPabWYDxEUS0k%2B2s0PJjmcsVFyFvhSbOBT4kWR5aXujt9N0NTefRsVvvdEIlAtPjlF3y%2FRW%2BYkV%2Fl67yXRaIQKU9Il%2FoYTAyC3U5xMEP6WPhL3YxY6vMXyySctei3BvItG9ixqF9OupF5%2BdG6C5jfBasANpzWjdDMJovJSCgB7mRZ0cRdLoAi84bdy6pLcmbxAYrvytKN5XQ9hytpvYt7mSDuHHnx7xT%2B2whXMt%2Bk%2B4BC%2FpTEs4%2B51sregI9A5PED4VOljyfvwPh5iVnpA1hQaEAwXxLWiD6LTuK1Ge%2FWWISLFvwK8nT3AvDp7KduJ%2BBGe5LcDo8611A%2FM6iAVc7HuJEl2qrSKwYQaW36f%2FDAY4yy4d7mcy9b%2BHe3q8rdxh6kJJxfPK7nFoN98lStX016Zv05EiYOOO6Y2TZzCzzvfJBjqkAaW%2BqpYQBoyqjFDcleaQQ9synVSLcik%2B0IvcBLnHiSR3H6mkQ6JJmiJ9LUSU3%2BD1Hfwj5ubucwuOVKzlMxj%2B6%2FTgEaRm9aiUsLn8GxFzgkna5rBEzYTV5du9cl%2BID0zJz1PG7tSU5hEbFifMEMRncsiG5qcWCx2kvvilQMqc%2F2K39pUjJuMTK2GrklJQTtDiYX3Wr2g2pGZhlsZWQta%2BqDm31x1P&X-Amz-Signature=0e510bf33acb4594378d037be7f5e3385ad1bf9b15d1d8c7415efc5d0acc99d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1966400c-2622-49f8-a0af-a4452434e8b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CCVNJTE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDUuCPV%2Bab%2By0EzQqVWBclu2S62eib4%2F6sMyhvtVR6CDwIgVlAP0YieXCgWX3fN9MnWIMk8yN7oJGz6IIjcVQrFNjcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBpe6PiZwSk%2FlKftIyrcA6kAqVKElyrGuzELj%2BwvEXd0itAGg%2BpE4Jx5V%2FNlm9LgSzPG4JzzHAHk9RN4APWVR0%2FMviGE7bnb1VaybYpw0Ei7oh%2FiXyNoP%2BXoAlo2u%2FSMhVREgL74pccgFyMnURPChnGeVzfZoJc2Y4f%2F1rkSFrF2sXW4YKZC8CLpPUxZS7JhlooH2Blm1iZ9yuznuLN3ujsVvBeSAYpJlyVu9RFrul%2BuvypQTCs7xe02pbM6Le0zm6zggfeqvheMJ%2B7TuysCoNNa4a16Y7nqYortRqj%2FYgQrM5tna1amYSTItmz4T2vBFe1FAcxS6PWUh9b2kA5nKJY%2BIY58GKJbJ0BwW5AZSveblWV67jS3wD3uvLRmUBW69tFrHj1dGx3UJr5ibDnGkKMNJim70zrk9bymsY9xaAaKNEg4GxZwflLwqjln5bG%2BybJ325b7o7n4m5QCGipV%2BLkYaMz%2Fl%2BKwXT7164nT62M1%2BetBD9puDgaZh%2B%2FUwW5FBtsh2Tbm%2BkysJ2ISjp7dFY2SBlE1ylHOTe%2FtjsReL9DLJxdcnd7aCz8uuTUpOMFnDExTaSGQbp83YW0ZQttIANYKBi%2Fy1hpt91oGj1aIzYEth1lcEEj6VNiPDGlLxNhKoTBVa%2FCUOaY1CZOpMPDN98kGOqUBHGroiVhbhZmSNhTs%2F%2F0S75I%2BlNF4lF1fFik4dLLtVmuGcU3HUXKzhfe4%2BXXEBdtPIclgF2K8EeqWNyanKnuiqkDsMvPHJ98beQ0H5%2Bi3fF680lcJb4Wqw0Mco8IroTZs8tTXhgLAZC8Ndc4IltcyroMrQ4yRh29q83r9hUAmFEeBZ7BPQXz55IfY%2B8JxpdSD1td1QO3o%2FqFxJXjxgxZNRBo6cZrN&X-Amz-Signature=2288908ec96d7d7084aecaf71a2d97879968edb85e05946fa292b548098496e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4508adda-64be-46b5-af4e-75e75a13807d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQASE7VF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDUoP2VbxWuKJ5g9XPR2p8c7Dh5DX4zIn6P2P%2FhY9oS5gIhALqa3jQtPkNpOZwiOuDBkbPWPJpg1Lc4hQovrouX00cKKv8DCCcQABoMNjM3NDIzMTgzODA1IgwR%2BRo%2BEX6a3YjmhZ0q3AP1IEElsd%2BPs80iQHcCuXSSLMx6WLIXNxAyi3Up92CAryo9h5aN%2FMEHOznKyFRjReDP4wCwiGrPL%2F8x%2BtpugOZlru7CU7KNksYZmN4GvI%2FAA%2BNSf0mDAQQfrw8tYL%2BDsogyQuf%2BmENroQz715LaoDWjSTRnJ6kOEgljUuMwPwUdIN44j%2F4pmn99huQOH2aH3uMkh20z%2BBX%2FlRh8oeX%2BgrfgNuK70ZcsxjOyExxqh2qt8RWrx0cabHsXPwiuC5a1QqQ1tCpIQY%2BmLracTiKXsndTd5%2F4pYeLFRW0KU0h8UQLwB3rPZy8fFLDJt8g87IUDb47zHUkt7ewX0nz2advofCxuN0vC8UtOj6lCyGoJM1F7gK5Jlv3LGmJ6yibXB83DhKb7vdG0XN9H5C7%2Flr%2BYYUwerAqB8vDKKUxiBjhSAdIGjgEJay%2FnjLsfJE%2BJRP9WuiJ1G%2FRKTY9IxCvWSkeFQvyBqNMZf2WSpmn7RPgg%2BRbE8RvLGiJp7zqzZeZ78PJfQmLSpd6al62HuLSMGUbu2Rf6Dhf%2FgLed0m8gb2C1AeUfij5SY4j6OdqI0XU3xw48JM%2FIvH1T3i01yu43LVJiXeM1Pvqgy7sAZtFcFIR4Zot%2FVe5Ks8dII9kkyhkPTCWzvfJBjqkAb%2BsNHGShOboSiBVz0aB5dCyse5OR7TmcmRnElV%2ByMwFtuqe7OtXyba18NUdo7X6hMR3iqmfhvVJC8xUhKXmq72DtSXQ4LvuRjtjDCvwL7Or8t4AQSzmIg067bvDE3MoZbTaQv%2B%2F9lmcv1S4oytfRTfOpBl7bDJvBEoUC3Jqk%2BaGQu%2FnixuKZQ95PjMYZDTP7AcnWFWAGt30DZRC1gHw91sXXHUM&X-Amz-Signature=f1a9d60d3a85e98e0bda34f4e813de85b178232726dc12c0036989ba61c491d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
---
## Question 2
Sie schreiben mit SQL genau **eine** syntaktisch korrekte und zu den Tabellenstrukturen passende SQL **UPDATE** Anfrage inkl. einer **WHERE** Bedingung.
Markieren Sie bitte **alle** korrekten Aussagen.
❌ Mit Hilfe der **WHERE** Bedingung lassen sich die zu aktualisierenden Tabellenspalten festlegen.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, kann mit genau einer solchen Anfrage auch gar kein Tupel (tuple) der entsprechenden Tabelle verändert werden.
❌ Die **WHERE** Bedingung kann nur im Zusammenhang mit **SELECT** Abfragen genutzt werden, nicht jedoch mit **UPDATE** Anfragen.
❌ Unabhängig vom Tabelleninhalt, wird mit genau einer solchen Anfrage immer genau ein Tupel (tuple) der entsprechenden Tabelle verändert.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, kann mit genau einer solchen Anfrage genau ein Tupel (tuple) der entsprechenden Tabelle verändert werden.
✅ Abhängig vom Tabelleninhalt sowie von der **WHERE** Bedingung, können mit genau einer solchen Anfrage alle Tupel (tuple) der entsprechenden Tabelle verändert werden.

<details>
<summary>Explanation</summary>

Let's break down the provided SQL-related statements and understand why the correct answers are marked as they are.
❌ **Incorrect**, the `WHERE` clause in SQL is used to specify which rows (tuples) should be updated, not which columns (tabellenspalten). The columns to be updated are specified directly in the `UPDATE` statement.
- Example:
```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;

```
- Here, `column1` and `column2` are the columns being updated, and `condition` specifies which rows to update.
✅ **Correct**, if the `WHERE` condition does not match any rows in the table, then no rows will be updated.
- Example:
```sql
UPDATE employees
SET salary = 5000
WHERE employee_id = 9999;

```
- If there is no employee with `employee_id = 9999`, then no rows will be updated.
❌ **Incorrect**, the `WHERE` clause can be used with `UPDATE`, `DELETE`, and `SELECT` statements in SQL to specify conditions.
- Example:
```sql
UPDATE employees
SET salary = 5000
WHERE employee_id = 1;

```
- This updates the salary of the employee with `employee_id = 1`.
❌ **Incorrect**, the number of rows updated depends on the `WHERE` condition. It could update zero, one, or multiple rows.
- Example:
```sql
UPDATE employees
SET salary = 5000
WHERE department = 'Sales';

```
- This could update multiple rows if there are multiple employees in the 'Sales' department.
✅ **Correct**, if the `WHERE` condition matches exactly one row, then exactly one row will be updated.
- Example:
```sql
UPDATE employees
SET salary = 5000
WHERE employee_id = 1;

```
- If there is exactly one employee with `employee_id = 1`, then only that row will be updated.
❌ **Correct**, while it's possible to update all rows in a table, it depends on the `WHERE` condition. If the `WHERE` condition is omitted or matches all rows, then all rows will be updated.
- Example:
```sql
UPDATE employees
SET salary = 5000;

```
- This updates the salary for all employees because there is no `WHERE` condition.
</details>
---
## Question 3
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
