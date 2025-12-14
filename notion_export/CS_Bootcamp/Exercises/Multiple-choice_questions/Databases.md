---
title: "Databases"
notion_id: "d82f1c2a-d852-4253-b55d-c1260d18c4d7"
notion_url: "https://www.notion.so/Databases-d82f1c2ad8524253b55dc1260d18c4d7"
exported_at: "2025-12-13T22:55:46.990569+00:00"
---

# Databases

---
**1:m relationship**
Let’s assume we have two data tables: Parents and Children. We know that a parent can have multiple children but a child can only belong to one parent. How can we connect the two tables together? 
- [ ] 1) Insert the Primary Key in the Children table into the Parents table
- [ ] 2) Insert the Primary Key in the Parents table into the Children table
- [ ] 3) Insert the Primary Key in the Children table into the Parents table and the Primary Key in the Parents table into the Children table

<details>
<summary>Solution</summary>

2
A parent can have multiple children. With inserting the Parent Primary Key into the Children table we can associate the same parent with multiple kids.
</details>
---
**m:n relationship**
Let’s assume that we have two tables: Girls and Boys. We want to insert another table called Relationships. This table should store all past and current relationships that existed or exist between the Girls and the Boys. How many Foreign Keys would that table have?
- [ ] 0
- [ ] 1
- [ ] 2

<details>
<summary>Solution</summary>

2
We deal with an m:n relationship between Boys and Girls. One Girl could have had multiple relationships in the past and the same is true for one Boy. Thus, the relationship table is our mapping table. We can store all couples that existed or exist by inserting the Girls Primary Key and the Boys Primary Key in the Relationships table. Thus, the table then has two Foreign Keys.
</details>
---
**JOINs**
Which type of JOIN usually results in the highest number of records in the output table?
- [ ] 1) Inner
- [ ] 2) Left
- [ ] 3) Right
- [ ] 4) Outer

<details>
<summary>Solution</summary>

4
The outer join includes all records from the left table and all records from the right table in the output. Where no data is found, #NaN is inserted. Thus, this type of join results usually in the highest number of records. 
If all records in the left table are associated to a record in the right table and vice-versa, all JOINs would yield the same number of records in the output table.
</details>
---
**SQL queries**
We have this table called Students:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bf7650b6-881f-4352-af87-8479d2a11196/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=38673b0635803e1aa78a2da39ee1b13c3e0e0d1888bef5a54a37aeabfdd9c759&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we want to have this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e812d65a-f8b9-4756-9d4e-9c2351985a16/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=cb3d5043ef2ac36b9010a3419a7d61d95df0adeb1baa2ff30f9e7a6f05ed44f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Write a query that does the necessary.

<details>
<summary>Solution</summary>

```sql
SELECT COUNT(*) as 'no_of_students'
FROM students
```
</details>
---
**SQL queries**
We have this table called Students:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bf7650b6-881f-4352-af87-8479d2a11196/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=ac689439bc1b9ceddcfa55f164de09498772d4c34d0c027d162c5483bc39c777&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we want to have this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/35b45d58-c46d-4039-952f-492de3ea98a3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=8fc1817a3e7839648ff53094e5d08cf98d7b3ec93885ca6c1d25cd384f47abbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Write a query that does the necessary.

<details>
<summary>Solution</summary>

```sql
SELECT date_of_birth, COUNT(*) as 'number of people born'
FROM students
WHERE date_of_birth = '1997-04-23'
```
</details>
---
**SQL queries**
We have this table called Enrolments:
We have this table called Courses:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1706f8e7-a234-40f0-aba2-dbd75215db31/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GRSH5MQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBs1Fm%2FemHn6pwJFPD1v%2BYfRuXAJE9LXKHc%2BvFpz5EKcAiAwhSmrFM4KBBzO2gDAww5N0x16%2F0taeDE5MX9awv7tfCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM%2Fj5Xy04NU5HyyhMNKtwDOtapcfVf2jFIUZIPHsJdjDpf3MgQ%2FiUwKewpAWxnX5L%2BZmV5GGFOl6ULLZrHo%2FyI6az9CZa%2FzYLn8nsdWgevp3IMeDJmwkUItsIwPzin1kRxnFjJdbZFU2S%2FW9pMNKHcpUtowXqdz4xmnU33Myf6OJJe3wbZMXiTmWD2GtI2iDp2vRT7LDaiIkPMQMjXNTnQ9BoMaHUbj2b2%2FKKP1omqsm2KTiY%2FjoKbWoXYtQC2IhJ13%2B1TmRdQpndW7N2zbS1l%2FNMrNnZj78Yp5plsvTocHri219BIlEcZ869ZExgfWtjXFirLvmhWwStAO3Bv0YXQXWeYvrBfB%2F%2Bkujo1Dpf1HHlgv%2FboaUZFvmlQAifETDOFmI19m1kkk6qdFnR9rPG%2Frrftix0kTBfNIEbo0Pc3S2n96AeCQwgaxUB57OVAOPFC5eAXY5%2FAuwQhem%2FGDthLBb0ymnHI%2FMhkIEFQbgP3l2hlamle68pSpF3qW6rMsmgDPsb67er4Lv1SH5wXUXcDSioD0krI9gIRzXFHaSLDrY9IPmKGXS9t3Tm8gmrUSPZMnrDNShR16UTMx15jKBnkknm%2Fc4u5FqL3i%2Bnxop0X9EK4JhiNKBpWsKygjNejT%2FL6kvwy8suxzo0Ib7gw8M33yQY6pgFqiFBPwYawH5O3ZUzVGWrk1T%2FWa5ZECuP7WFQB8ATiI0AX%2FrKowpYBiMOefUYeUYZ0H9dlrt41JIrsnZ7vggM8Fi3vkh8E10qGhQwmdjJwBoj6sry7KGk6Zd9JIBfSmknpyn17KDPvOvq3owowM4Rb%2B4bWyYw%2BQuv7K%2BNMo5Hf17r0s2H6jdvDAtmXeI08TzWHAN8UuyGCn39wQPIytlB3zaTyukn4&X-Amz-Signature=6bfc2fc00ad1907fb7388bee0c6d93d18837058b668d9d37d1137e9b77daa085&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/655ae48c-f696-4775-9b67-321fc8af6a1f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKQGPFOW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIEnkVgiZBEg%2FEnSwjfGN9Wic6%2FqLjriMJe5pztW1Yz2BAiBMClUVBk9yGhB%2F%2FqDpCOWntpHImnFuwLpciebyIq8SgSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMFn6TqC8VjsTLI0A2KtwDbv3YwVLEDanvXQUfW%2FJ622rwiKOipY4Mp%2FGjFF2lP8sQiavWcV3IiE%2FTGIn%2B2guo99V%2Biu00CoEHpJVIdWpJ6QypPn9Xr%2BwkJoNdP5yNvQCD8ZEksJpvTlOZZ18kmkJJcFF5ydV2lhrzNDE9TyysONNWGc%2FYYf5DylM5Y6eTWLJfstIhW%2B%2BCdigvHC33Fg2CaNlDBny8ZdgdysyxjFZH9f3yogA9s%2FwdRuwFKaODcqqYmS3hxcwX4z9qe0KR9675gXCEx%2B1jrCw8pNr4Etc6qMPWHY7q5uvdy3lGX74FQdKKjmsAqA3nPDH00Vr7em%2FB4Nlg%2Fmy5dL1db0U9ohTyhClFnJLL2dU9vKMRUUZhc9eSOvtU%2F80e6lxvO4Qnj9ydRiAntM63rOXx0FkieQyatG6Fts5eh8RxAhH4eQ45TMFLQBiM2a6OepoSoQozRsaA9WPW6h81tKr%2BxHgwMr%2BvRFxbTnIx3nImVcnznauHk4BByUupca2N8idChDF%2BLFgqvCXQQh1DuGEM29OrndzBABql%2BNrr8ur8fEp4iqLJhYJv440AIPAm2fZAspnLocOpRSa%2F5yc1DntL3JGIluWZcsbdfrwkQc6p6MW5dlfjMh2VaNZi%2FnNgtyU%2FI48w%2FM33yQY6pgGYzvfh6Y1QarwjHabzSPVHCINLwMMnENafzoWVZU4%2FVjY4m5H%2F%2FAw1DkNivok6QtMenPD3jA6STpflLLYZu6NoN4r4yf9BDKOt5z4F9dVeL%2FrYEunI4HdMvXDk%2Fxe2HatkyYvwvpuJJSH3VuL5NpVFFE%2FIbylGVTMzHHu2YzlluOWwf4ctHp5tydGNeJcB1EOKQVvDrDvOHh4z%2F5ESqB4sj86N0H1y&X-Amz-Signature=36d0ec931b88225918445e5a7c97087d693343849406ed5febf13dec685b2e30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we want to have this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8dcd1760-888e-4e2f-938e-8902a8c020d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=c3b1d387377dc782eca033aed83a9a41e2b7a1014b6150942a576bd382bf7565&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Write a query that does the necessary.

<details>
<summary>Solution</summary>

```sql
SELECT courses.name as 'course name', COUNT(*) as 'number of students'
FROM courses
INNER JOIN
   ENROLLMENTS
        ON courses.id = enrollments.course_id
GROUP BY courses.name
ORDER BY COUNT(*) DESC
```
</details>
---
**SQL queries**
Which of the four queries below produces the following output: 
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/42243842-134c-402b-8764-bc2bac3684d2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=0669a4de72f245b9683461c5208648fbde2f8a418aee82f328e4bbf37efb33b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<u>Query 1</u>
<u>Query 2</u>
```sql
SELECT COUNT(DISTINCT category)
	as 'number of courses'
FROM courses
```

<u>Query 3</u>
```sql
SELECT name
	as 'number of courses'
FROM courses
GROUP BY COUNT(*)
```

<details>
<summary>Solution</summary>

Query 1
</details>
```sql
SELECT COUNT(*)
	as 'number of courses'
FROM courses
```

<u>Query 4</u>
```sql
SELECT DISTINCT COUNT(*)
	as 'number of courses'
FROM courses
```
---
**SQL queries**
Which of the four queries below produces the following output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/afb3d2ea-66c0-4a3c-8b6c-1aed883fd9a7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USKROLU4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBvS0Ddvt5dGcz5J7mq%2FHcrnPpWI415tkJNhI4Y5CSvOAiBoZjlf3xN02%2BcOL99suC0H1ATGJ4DhWXFveUPiA9Xsjir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIML4yEUZPdD5FEnR4lKtwDw6RdnypFG8b5coBdz%2B%2BRdh6xoiDGSuqekBY6dTl7YDSk165Ih89FS2l0BG4IBiVJQ7vxpIbjRfGSRx8H8APnjysvfgCh77X80CcP9zXpIIdMWKN6%2BNEQpLonRnMq1fSAKu8L1z%2BzUlnNSHwSaa%2BGFLGyj4icXfOjMtJT6HN16FAOf0tzlqEKuVg8zdPR8WiHGheZcaU17O7ddFu3Yy9G0k%2B4iDwjviYlPaswaOn%2BCbDll6BzoMDJt%2BIOO%2FIGlbKCiEr2N61j3QdNz%2F9OEBOhhJRmdpaIhVxQ6SoxE8lEN5PaPVOLgLT9SBi59jSQQUrTMSNjKCMGsDZAbgr48ZMoIcSKbhmJPsV1kdZsrOb4xRL%2FMevehhiHyKg%2Fkz8QE3pr9k56xZ%2B3gx5bjcDGXZr7zKN6gSVMxGcYpZln6pfKCS93GLRg5ahQ6NMQkyMQLixlISaZ4RX2ukq9zG%2FM3R1MgZtRy7DvrTFVLOG41LJRzxvHNvgo2DL%2FZT5F%2Bmfp0voe5ZU%2BHzCshVV7yVSdAIyBZbn69PdEX0DG%2F%2BPQUFne1bnRHmDuvAkTUSWfMIld0wU3qJLJeJoLiDjb7ZkxTax0ggtHV8XbEEbTdj3gVL5GbYtLkInIkBDOw%2Bsl8gowqM73yQY6pgF0wLddtFu%2FUDLuQH%2FMlfmSXRGNYqKwvxJLHaqQr4d2M6KLEiZshFud%2FL4QnXqRtQoOxznB0IsdJBo6xk446ndiO2mProNplGRtBraihVS3KZb%2FuL3gkMqo1EVgGH5IkfKIXHEkN0sBC%2BJiq8bF808VQPUZz2o2cq5zGBdGvQMsBy8nWSIjqX9uWFEM0yCrPai%2FFrEP72g9edej2CfaQRAUbfiQBQjS&X-Amz-Signature=c4b7476346e3d9c0a8617b1b88c5136499003aac5820c0bef785945ef67028e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Remember the relationships between the tables:
- Courses `1:m` Enrolments
- One course can have many enrolments
- One enrolment belongs to one course
- Students `1:m` Enrolments
- One student can have many enrolments
- One enrolment belongs to one student
- Grades `1:1` Enrolments
- One grade belongs to one enrolment
- One enrolment has one grade

<u>Query 1</u>
```sql
SELECT students.first_name, students.last_name, AVG(grades.grade) as 'avg_grade'
FROM courses
INNER JOIN
	enrollments
		ON courses.id = enrollments.course_id
INNER JOIN
	students
		ON students.enrollment_id = enrollments.id
INNER JOIN
	grades
		ON grades.id = enrollments.grade_id
GROUP BY students.id
ORDER BY AVG(grades.grade) DESC
LIMIT 10
```
<u>Query 2</u>
```sql
SELECT students.first_name, students.last_name, AVG(grades.grade) as 'avg_grade'
FROM courses
INNER JOIN
	enrollments
		ON courses.id = enrollments.course_id
INNER JOIN
	students
		ON students.enrollment_id = enrollments.id
INNER JOIN
	grades
		ON grades.enrollment_id = enrollments.id
GROUP BY students.id
ORDER BY AVG(grades.grade) DESC
LIMIT 10
```
<u>Query 3</u>
```sql
SELECT students.first_name, students.last_name, AVG(grades.grade) as 'avg_grade'
FROM courses
INNER JOIN
	enrollments
		ON courses.enrollment_id = enrollments.id
INNER JOIN
	students
		ON students.id = enrollments.student_id
INNER JOIN
	grades
		ON grades.enrollment_id = enrollments.id
GROUP BY students.id
ORDER BY AVG(grades.grade) DESC
LIMIT 10
```
<u>Query 4</u>
```sql
SELECT students.first_name, students.last_name, AVG(grades.grade) as 'avg_grade'
FROM courses
INNER JOIN
	enrollments
		ON courses.id = enrollments.course_id
INNER JOIN
	students
		ON students.id = enrollments.student_id
INNER JOIN
	grades
		ON grades.enrollment_id = enrollments.id
GROUP BY students.id
ORDER BY AVG(grades.grade) DESC
LIMIT 10


```

<details>
<summary>Solution</summary>

Query 4
Based on the information about the relationships between the tables you must think about which table has what Foreign Keys to establish these relationships.
For example, in query 3 we join on `courses.enrollment_id = enrollments_id`
This would imply that one enrolment can have many courses and one course only one enrolment as `enrollment_id` is a Foreign Key in table Courses. However, the opposite is the case: `course_id` is a Foreign Key in Enrollments table (see query 4).
</details>
---
**Relationships between tables**
Look at the three tables below and answer the following questions.
- What type of relationship exists between table Students and Courses?
- What type of relationship exists between table Students and Enrolments?
- What type of relationship exists between table Courses and Enrolments?
- In table Enrolments, which column(s) are Primary Key(s) and which are Foreign Key(s)?
- What was the reason why table Enrolments was created?
<u>Table Students</u>
<u>Table Enrolments</u>
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7860251e-e68c-4a7f-a413-d6ddfd5fd578/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E3TYDIE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHF2aQagK57n9eVnkrX3KPY0%2FfMP0oV4kcwKwm1LefrFAiBDAnY2IihBXgvMbHX0F%2BeXerp7GNGuJWrxQFK%2F3KX01Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMrMjQwIzFmEDtiepVKtwDEfzM3I19RKtyhcdIEGJLMJUxXx2uorek6HtU892s4Uw8U2msI5DEfQWsBYXT3Z5Mrqrf%2BSJr6FFhWugWmVyRJgaQkREaG%2BlgArdlxUXG0nH6AedWXyFRGM6d3IxZVRsQiU3pIL8I51dKKPap7F%2FFlCcZYzu8ezBLILAImZTYn5p%2FcBtgrZ%2BaYM3ER17hXuyGCip9mzs6VYZW0kkYqzntDX7mG6NVUb%2Fw6dqcA0bmNinGbmdIre7DxKtET9xnzVD3zSpHyOv9C2bgPuFIh3lUmeskqvjFARAyn8OypQvFckwnnS9w5bEpX9F9OSPdPZchfYMWUNkA2Y%2FkGo%2B5rOBKmOkdt9lb2IyIaFs%2FevjNExTA2N8kU71SucNcOo5s9sDYeLugWjNlTjzh%2FPswyHL3JHpO3VPP%2BZMLyxGAdkrc%2BDDxtfjV8ZTvB1P3GPIgnFXU8DxZV3FZmWbXwNmTU0FKcWB1VO0pm99hu%2Fma3sjuuwHN1lGd3xbVAY8RNGZAJ0JOeE5dtXmub49wYkCg7MuVip0KS%2FuySrbm2QSN21aYyWdrKSbwxX1jrWLMB7oENck%2FVF1MyMHFmjly3NxN52XgyKciAk%2BNPu50qaFwmgQxocxDFaNqXpWyqdA5dY4wyM73yQY6pgHKY80GJdkqO%2F0GxJLTRET1ssAR6ghErp40xsZOyyUbhbhXnXAeOkUQJL8rwFPmV8DQDZLxqJbyaogasTsbm2lPLW39hLtJBzhag9%2BUbhTpo4XIoUjaBe5vpinLqhBQh%2BkBqfbsX3uxBDyTXQUeT%2B0GAv1ZEHaU7KENOvkq5Xj10TmTowLPV4XvRu3ktWTmIG8xdv2%2FDwpTrE7ljMzjJAKaGO3dRLFf&X-Amz-Signature=109e15d2c35c589efe49c64196726bc6052bc0a6c6d11232d31192c0a6e712ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<u>Table Courses</u>
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cbabca09-d632-450b-9e21-c60709d4161d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E3TYDIE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHF2aQagK57n9eVnkrX3KPY0%2FfMP0oV4kcwKwm1LefrFAiBDAnY2IihBXgvMbHX0F%2BeXerp7GNGuJWrxQFK%2F3KX01Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMrMjQwIzFmEDtiepVKtwDEfzM3I19RKtyhcdIEGJLMJUxXx2uorek6HtU892s4Uw8U2msI5DEfQWsBYXT3Z5Mrqrf%2BSJr6FFhWugWmVyRJgaQkREaG%2BlgArdlxUXG0nH6AedWXyFRGM6d3IxZVRsQiU3pIL8I51dKKPap7F%2FFlCcZYzu8ezBLILAImZTYn5p%2FcBtgrZ%2BaYM3ER17hXuyGCip9mzs6VYZW0kkYqzntDX7mG6NVUb%2Fw6dqcA0bmNinGbmdIre7DxKtET9xnzVD3zSpHyOv9C2bgPuFIh3lUmeskqvjFARAyn8OypQvFckwnnS9w5bEpX9F9OSPdPZchfYMWUNkA2Y%2FkGo%2B5rOBKmOkdt9lb2IyIaFs%2FevjNExTA2N8kU71SucNcOo5s9sDYeLugWjNlTjzh%2FPswyHL3JHpO3VPP%2BZMLyxGAdkrc%2BDDxtfjV8ZTvB1P3GPIgnFXU8DxZV3FZmWbXwNmTU0FKcWB1VO0pm99hu%2Fma3sjuuwHN1lGd3xbVAY8RNGZAJ0JOeE5dtXmub49wYkCg7MuVip0KS%2FuySrbm2QSN21aYyWdrKSbwxX1jrWLMB7oENck%2FVF1MyMHFmjly3NxN52XgyKciAk%2BNPu50qaFwmgQxocxDFaNqXpWyqdA5dY4wyM73yQY6pgHKY80GJdkqO%2F0GxJLTRET1ssAR6ghErp40xsZOyyUbhbhXnXAeOkUQJL8rwFPmV8DQDZLxqJbyaogasTsbm2lPLW39hLtJBzhag9%2BUbhTpo4XIoUjaBe5vpinLqhBQh%2BkBqfbsX3uxBDyTXQUeT%2B0GAv1ZEHaU7KENOvkq5Xj10TmTowLPV4XvRu3ktWTmIG8xdv2%2FDwpTrE7ljMzjJAKaGO3dRLFf&X-Amz-Signature=41894d117961c82f2915d9e700dafee0191af8e76e5e86ddc8c53a30cf8a0b16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7e1c0470-ce21-4d6a-a1a7-16214fa6fc4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEO2HZF3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC5ys%2BbioAXNTMMOsaW%2BtjVpCjH2nyLyQ4MqCAoiInE3QIhALxGpleRRwsNQ7Pg50TgD1CdUDpZt8NZiBOVy4TjPJ8QKv8DCCcQABoMNjM3NDIzMTgzODA1IgxqJtNsS6jLX5SliPcq3AMmWT%2B6zSRmc4Irr3yeIlvEm1BLVupdc5whPcJmEVP4sJ59XZTqn1wqr0QH%2BDv22VkRgDWQ8PA2Oq1zvkf5XF4aNvXZMY4h7c4jH4nrt5xg7WCqj8HSXvAEYNYDup8afizacWCcvXMqPkYPSn24nchW7x%2BJSrFROtEDfemvVCesEysZ8W0tyGJqymQr3rBv07iNNwEreTCxeQFF4nD8b0pz6p9s4%2BAGaoxkefKgPb1tJKmyhD2fbdEV8Ld5jbQUaRUibMbSW33NvIB8w%2FoVeOPvjiN8HA05%2FBa%2F4xYCRzFfgrdtI2O2na3i2xta5stVyiQx05KOISfNGBbXdoOsWMW9r1n7tIcmUdZ8G8qUMLnz29JglnqjxoIU1R0njAS8lLzFcdzGd4RAWfRsvItubhs73JCzqe0FeOc5PsBxaEfU6hSRQjLbuHG7t1HGicfz288%2FIner5EoMLQAOX4TeWpDsDxSjfB8wA3ZUcBqT9sYtGh%2FAzCeU2qH1EtoBYoZ1rcUSeeC8UqmX7CeMTBu9tCwOI9Jpa4iCRiMWNRyvb3N1q0nk3%2B%2FW2w2J1FDygAqvxZeMyu5RiSGHS4TH3Ua7LMVLDDAE5mKWQ5oO1yi9ndNVCgDb1RQyz9HixjeHYjDvzffJBjqkAVKtDp9dPpqSafTjUrboMDbZ%2FGMTnSExq9bI%2Bl79cNvEzpl%2FAPw%2FuWCWA44I4MsjeB0oL9Reho0nh%2Fi5htNYWQkNmGdq%2Ftqb7a%2B3TQV6GEr5yrW5Tct%2B%2BpmCt5mPwl%2F%2FcZQe6ffHLsRbNTH8ODEsdX63kg0w4TM%2BJA17cPDk8QKMnU%2F16Os15AN9rfvK1JI8fM%2BwsNuzubmJzaIKN6g5uoJj73jv&X-Amz-Signature=323302aab273eb92ee6113566328c95391fbf2dc29a696599ec2aaebc62d9604&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Solution</summary>

- m:n → One student can visit multiple courses and one course can be visited by multiple students
- 1:m → One enrolment belongs to exactly one student. One student can have many enrolments
- 1:m → One enrolment belongs to exactly one course. One course can have many enrolments.
- Foreign Keys: `student_id` and `course_id`, Primary Key: `id`
- Because there is an m:n relationship between Students and Courses. Therefore it was necessary to create this mapping table Enrolments in between so that the relationship is split up into two 1:m relationships.
</details>
---

