---
title: "Quiz 9"
notion_id: "e1a14712-985b-4466-992e-86be0e4cd8bc"
notion_url: "https://www.notion.so/Quiz-9-e1a14712985b4466992e86be0e4cd8bc"
exported_at: "2025-12-14T01:02:37.397723+00:00"
---

# Quiz 9

# Question 1
Gegeben sind zwei pd.DataFrame-Objekte ORDERS und PERSONS.
Die Ausführung folgender Code-Zeile führt zu nachfolgender Ausgabe:
```python
print(ORDERS.columns, PERSONS.columns, sep="\n")
```
Ausgabe:
Index['products, 'purchase-id'], dtype='object')
Index|'name, birthdate, 'purchase-id'], dtype='object')
Sie wollen beide Dataframes so zusammenführen (merge), dass der resultierende Dataframe alle Personen aus **PERSONS** enthält und bei den Personen, die eine Bestellung (order) getätigt haben, ausserdem auch die zugehörigen Informationen des **ORDERS** Dataframes enthält. Bestellungen, die zu keiner Person aus PERSONS zugeordnet werden können, sollen nicht enthalten sein. Bei der Zuordnung der Einträge aus PERSONS und ORDERS fungiert die Spalte purchase-id als Schlüssel.
Bitte vervollständigen Sie dazu den folgenden Code:
pd.merge(PERSONS, **ORDERS**,
how=**’left’**,
left_on=**’purchase_id’**,
right_on=**’purchase_id’,**
)

<details>
<summary>Explanation</summary>

> 💡 **[.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
Let’s assume that the two DataFrame look as follow:
**ORDERS**
![Example DataFrame ORDERS](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/428b68ca-d506-48fe-b030-0891d8209a74/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZUP75R3%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIEgXuCIUyC2D2Vqh4bEPENfSK7oEa0WQW9ne%2BnLpFrVDAiEA1DX74EAFWu31Nm0oQr5vymgyXwkPfAO7Q0xdN600F%2BQq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDAo1f2KVgW3IqG1PRSrcA2m8l2iX0icxaK%2BcAjmGNDfYL9AElDu%2BPaLfq6HB%2FU1AZp%2BMMTtCqKe5XIB7sZjC1ibr5%2FLr6pVxEBkpnUU78dn%2F%2BSQxYXaaBsc%2Fk84PB6qoAxIMPbFSTtpfaJ3fjZWuGb4EEjWijUoeCr39jIjK9x3fjZoT2mSJy7bS7LIvt9GjWjQ4onVbA4JnwOxra8be3EDGlgTUSHX9P7L0Ht6k0oTfBPyNXZ6lC832zjAh90cEsCRHplvAJQ4dt0Vg4DIJ9ra%2BMYNL5Gxd4jmhEGus0vIWQ4hZStMqZWmjUZl2T1b1R7dPS0ZJhffiXTsXb2aDPYEwEKWCDv1wjRmaR8hkMqZPXZeMeaAelRxMc3O8dnXP7T5Khtk5Yx01YdAAXNH220RQGIbHp38FVdh2Dxa0YqUxq303NUDpPfGPDVboXYx6Dy3r%2BJxhCpQWhB8cz2GKMDqdxtMnVmxWvA%2FT0WV200qfuL2Js9Dy4e7IEVVHC5LTvFq3QehF1zL2DLpX1RxTWy7K6X1bA5gemrUmHgIg9inzKRmsAftTVwCS8bk%2BmxXNX5F0rcLHP8PXLVynFWALTn%2FXSN54Bjt9ueY7LsFZmv8wQIJXWfZChqDtdryfO4xMUpozeIjQl5dMuhrTMPCW%2BMkGOqUBVo0RO%2FGxsYGuoDHs2R4rPdKEcSCxfVZTUUGvKfCQEWq5xOW6HaZ8h7oq1k%2BiI1jhE7ML48Be%2FwmL6i49Z00vxvd4ih8YVrXEq7NF35wsSZIF9HdmKdpnr2F3Z7gN3C0NR%2FqJM9WZvtu6cm0a1klrxSDVN017X%2B5lIFpsRQaBSqTu2Cycod5xEAgitUAWSkXArXsnGIZ9uzakWvlnHVJs0qhiognh&X-Amz-Signature=22b245b9b92e2e3fd6891ab60f77798210a5942e26c4d4a74a06c2a560284551&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the **ORDERS** DataFrame contains an entry for each purchase that was made. The column **products** contains a list of all the products id’s that were purchased.
**PERSONS**
![Example DataFrame PERSONS](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7775f2c6-d1e4-401c-b175-f0c94da4f9e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZUP75R3%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIEgXuCIUyC2D2Vqh4bEPENfSK7oEa0WQW9ne%2BnLpFrVDAiEA1DX74EAFWu31Nm0oQr5vymgyXwkPfAO7Q0xdN600F%2BQq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDAo1f2KVgW3IqG1PRSrcA2m8l2iX0icxaK%2BcAjmGNDfYL9AElDu%2BPaLfq6HB%2FU1AZp%2BMMTtCqKe5XIB7sZjC1ibr5%2FLr6pVxEBkpnUU78dn%2F%2BSQxYXaaBsc%2Fk84PB6qoAxIMPbFSTtpfaJ3fjZWuGb4EEjWijUoeCr39jIjK9x3fjZoT2mSJy7bS7LIvt9GjWjQ4onVbA4JnwOxra8be3EDGlgTUSHX9P7L0Ht6k0oTfBPyNXZ6lC832zjAh90cEsCRHplvAJQ4dt0Vg4DIJ9ra%2BMYNL5Gxd4jmhEGus0vIWQ4hZStMqZWmjUZl2T1b1R7dPS0ZJhffiXTsXb2aDPYEwEKWCDv1wjRmaR8hkMqZPXZeMeaAelRxMc3O8dnXP7T5Khtk5Yx01YdAAXNH220RQGIbHp38FVdh2Dxa0YqUxq303NUDpPfGPDVboXYx6Dy3r%2BJxhCpQWhB8cz2GKMDqdxtMnVmxWvA%2FT0WV200qfuL2Js9Dy4e7IEVVHC5LTvFq3QehF1zL2DLpX1RxTWy7K6X1bA5gemrUmHgIg9inzKRmsAftTVwCS8bk%2BmxXNX5F0rcLHP8PXLVynFWALTn%2FXSN54Bjt9ueY7LsFZmv8wQIJXWfZChqDtdryfO4xMUpozeIjQl5dMuhrTMPCW%2BMkGOqUBVo0RO%2FGxsYGuoDHs2R4rPdKEcSCxfVZTUUGvKfCQEWq5xOW6HaZ8h7oq1k%2BiI1jhE7ML48Be%2FwmL6i49Z00vxvd4ih8YVrXEq7NF35wsSZIF9HdmKdpnr2F3Z7gN3C0NR%2FqJM9WZvtu6cm0a1klrxSDVN017X%2B5lIFpsRQaBSqTu2Cycod5xEAgitUAWSkXArXsnGIZ9uzakWvlnHVJs0qhiognh&X-Amz-Signature=fbe2aa54cb89c9c3b4445c087f2bb56bce5b2c4b1fe992d7c1f28baec6b0e7e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the **PERSONS** DataFrame contains an entry for each registered person. The column purchase-id is a foreign-key from the **ORDERS** table which tells us which purchase a person has made. We can see that everyone except Hans have made a purchase.
Now the questions asks to get the following output by merging the two tables:
![Desired output](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8f70aadf-d2dd-452b-b332-09702065ca4a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZUP75R3%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIEgXuCIUyC2D2Vqh4bEPENfSK7oEa0WQW9ne%2BnLpFrVDAiEA1DX74EAFWu31Nm0oQr5vymgyXwkPfAO7Q0xdN600F%2BQq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDAo1f2KVgW3IqG1PRSrcA2m8l2iX0icxaK%2BcAjmGNDfYL9AElDu%2BPaLfq6HB%2FU1AZp%2BMMTtCqKe5XIB7sZjC1ibr5%2FLr6pVxEBkpnUU78dn%2F%2BSQxYXaaBsc%2Fk84PB6qoAxIMPbFSTtpfaJ3fjZWuGb4EEjWijUoeCr39jIjK9x3fjZoT2mSJy7bS7LIvt9GjWjQ4onVbA4JnwOxra8be3EDGlgTUSHX9P7L0Ht6k0oTfBPyNXZ6lC832zjAh90cEsCRHplvAJQ4dt0Vg4DIJ9ra%2BMYNL5Gxd4jmhEGus0vIWQ4hZStMqZWmjUZl2T1b1R7dPS0ZJhffiXTsXb2aDPYEwEKWCDv1wjRmaR8hkMqZPXZeMeaAelRxMc3O8dnXP7T5Khtk5Yx01YdAAXNH220RQGIbHp38FVdh2Dxa0YqUxq303NUDpPfGPDVboXYx6Dy3r%2BJxhCpQWhB8cz2GKMDqdxtMnVmxWvA%2FT0WV200qfuL2Js9Dy4e7IEVVHC5LTvFq3QehF1zL2DLpX1RxTWy7K6X1bA5gemrUmHgIg9inzKRmsAftTVwCS8bk%2BmxXNX5F0rcLHP8PXLVynFWALTn%2FXSN54Bjt9ueY7LsFZmv8wQIJXWfZChqDtdryfO4xMUpozeIjQl5dMuhrTMPCW%2BMkGOqUBVo0RO%2FGxsYGuoDHs2R4rPdKEcSCxfVZTUUGvKfCQEWq5xOW6HaZ8h7oq1k%2BiI1jhE7ML48Be%2FwmL6i49Z00vxvd4ih8YVrXEq7NF35wsSZIF9HdmKdpnr2F3Z7gN3C0NR%2FqJM9WZvtu6cm0a1klrxSDVN017X%2B5lIFpsRQaBSqTu2Cycod5xEAgitUAWSkXArXsnGIZ9uzakWvlnHVJs0qhiognh&X-Amz-Signature=c4aeda7b4fb05b2af6610e761dd5d0dba25f27743dc8ae0f2f6c3e9c917a2121&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that from the table **PERSONS**, all persons should be included in the output, **regardless** if the person has made a purchase already or not. From the table **ORDERS** however, only the orders should be included **that were made by a person** in the **PERSONS** table. As the second order id (**10111**) does **not appear anywhere** in the column purchase-id of the **PERSONS** table, this record should be **excluded**. 
Therefore, a **left** merge is done which selects all persons in the **PERSONS** table and only the matching ones in the **ORDERS** table.
```python
pd.merge(
	PERSONS,
	ORDERS,
	how='left'
	left_on='purchase-id',
	right_on='purchase-id'
)
```
</details>
---
# Question 2
Gegeben ist ein *pd.DataFrame* mit den Spalten **x, y, Anzahl** und sehr vielen Zeilen. Dabei kann es gut vorkommen, dass mehrere Zellen die jeweils gleichen Werte für **x** und **y** aufweisen. Die Spalte Anzahl weist beliebige Zahlenwerte auf.
Sie möchten nun gerne die durchschnittliche Anzahl für alle Kombinationen von x und y herausfinden. Welche Funktion/Methode kann das leisten?
❌ *melt()*
❌ *count()*
✅ *pivot_table()*
❌ *len()*
❌ *merge()*
❌ *keine der anderen genannten*

<details>
<summary>Explanation</summary>

> 💡 **[melt()](/1867045b058343e1a66b677961515907#5e95974d66444f179b205b86fa56a92d), [count()](/1867045b058343e1a66b677961515907#8d4d0ed1fc114482978e4da5f21b429f), [pivot_table()](/1867045b058343e1a66b677961515907#b7e324abb8a749b38b4a2386f6d4dbf7), len(), [merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
Let’s assume the DataFrame looks as follow:
![Example DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/668dc5b1-a998-4f9a-b59c-f1a2d1e0d096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EG3XXZA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQC7eVZyf4hOY%2Bj8LlowRZYdOcl5f59hb1V6enx99yFelAIgSXMRkPJlTfu4nqzkE%2Ba4tShQ6zCzUUX3J04W2jtDBT0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDO2ldZBDTMcErnM%2BZircA6irxDpfzIapdk14VSycHi8YKyAKjOQpXI833TnXhG4j5C%2B6HmGZbvAlsFtImtMP%2BvPsXzAbQSctlHoAHbIgAOdXVtI5m%2BXaOBX1BWcSX2460ny7kivnXNG0MbopzT9DnLtLvja1Sjf5Sj1ysOB2ic5NBL0idsbjNvZR7hdHz6kTJX5dBXRs3GzYMavYFd2i2aVO3r8YTPnm8SeMUuuSrPZcKXida%2F5IzSFcq0Tf4cKDRD7xLgHiT0b5HWN7DguR8NJ2cqxQbwhFK0jXges1QGVxwWL49jM30PYbmkVXbNZrtK%2F7x7xBhUyLGyU%2FxF4N11qk6WQcphgXuh8VP%2FEHzxjEVW293BO508wkHO8JyBNPA7WPP7DQf39JuA1GyvzaaWlRy%2FPA%2FiqL9a383fuxYrdez5GBGpF%2FKUT0QnIiPo%2Fu%2FKnqj%2BY92n4%2F0EOzYsgBx05qNGSWQ9FzhrFgvfW45r62XEsFfhwX9K3zHcfnY3%2Bbb7YhcWeRSe4sdb6YOLg5uS8fC6F%2FbrzbtbnI87q1YfQGLqLlw4vTt8x%2FEoucGRcIrKip6JDndRXg74Uay5%2BS0rSXKSJ7HoDPWRUkcS%2Bp2Uk3TPmK1IqWslUd4Ua9lLkqGZrVHJqSiYRpGajSMJCW%2BMkGOqUBvCCV7wdDIUVaRI4scxVwRgon3j%2BijcKdC6wKUu6VQLbI4Vss2wfHM8iG6PrBG0QA8a%2BP0UQoKVtj4%2B9SakdtOQxNj5kJUNoE%2FtdOyc7CIAW4tE6TOB5QSQNpmFRbsWKfCp4N6hH4O2gkxHQovc%2BjCdyv5aODVEdTNm%2BzrhHkx9VyAukYedgSLZMSHnfcAcRltrgFmnKPGi0pJo8JuEcXfTiR36lj&X-Amz-Signature=e803f19358dd41011f4bbccf45c70d3f29c8088ae4122c7a94e6cd4101f89890&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The question is asking now to identify the **unique combinations** for **x** and **y** values and then compute the **average** in column `Anzahl` of these combinations. 
Whenever something ***summarizing*** for data in a DataFrame should be computed (e.g., count how many times a value x appears etc.), the `pivot_table()` function **can** be used.
Using the `pivot_table()` function we can get the desired output
![Desired Output](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2aaab5c7-af83-4dbc-9e8e-d67005019193/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EG3XXZA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQC7eVZyf4hOY%2Bj8LlowRZYdOcl5f59hb1V6enx99yFelAIgSXMRkPJlTfu4nqzkE%2Ba4tShQ6zCzUUX3J04W2jtDBT0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDO2ldZBDTMcErnM%2BZircA6irxDpfzIapdk14VSycHi8YKyAKjOQpXI833TnXhG4j5C%2B6HmGZbvAlsFtImtMP%2BvPsXzAbQSctlHoAHbIgAOdXVtI5m%2BXaOBX1BWcSX2460ny7kivnXNG0MbopzT9DnLtLvja1Sjf5Sj1ysOB2ic5NBL0idsbjNvZR7hdHz6kTJX5dBXRs3GzYMavYFd2i2aVO3r8YTPnm8SeMUuuSrPZcKXida%2F5IzSFcq0Tf4cKDRD7xLgHiT0b5HWN7DguR8NJ2cqxQbwhFK0jXges1QGVxwWL49jM30PYbmkVXbNZrtK%2F7x7xBhUyLGyU%2FxF4N11qk6WQcphgXuh8VP%2FEHzxjEVW293BO508wkHO8JyBNPA7WPP7DQf39JuA1GyvzaaWlRy%2FPA%2FiqL9a383fuxYrdez5GBGpF%2FKUT0QnIiPo%2Fu%2FKnqj%2BY92n4%2F0EOzYsgBx05qNGSWQ9FzhrFgvfW45r62XEsFfhwX9K3zHcfnY3%2Bbb7YhcWeRSe4sdb6YOLg5uS8fC6F%2FbrzbtbnI87q1YfQGLqLlw4vTt8x%2FEoucGRcIrKip6JDndRXg74Uay5%2BS0rSXKSJ7HoDPWRUkcS%2Bp2Uk3TPmK1IqWslUd4Ua9lLkqGZrVHJqSiYRpGajSMJCW%2BMkGOqUBvCCV7wdDIUVaRI4scxVwRgon3j%2BijcKdC6wKUu6VQLbI4Vss2wfHM8iG6PrBG0QA8a%2BP0UQoKVtj4%2B9SakdtOQxNj5kJUNoE%2FtdOyc7CIAW4tE6TOB5QSQNpmFRbsWKfCp4N6hH4O2gkxHQovc%2BjCdyv5aODVEdTNm%2BzrhHkx9VyAukYedgSLZMSHnfcAcRltrgFmnKPGi0pJo8JuEcXfTiR36lj&X-Amz-Signature=39be10356924ecf3cdbe0bc1f347de08db0890288c2cd4473571eb858c666cfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>*Note*</summary>

I actually didn’t use the `pivot_table()` function here because in my opinion it makes much more sense to do a simple group by:
```python
df.groupby(['x', 'y']).agg(
    {'Anzahl' : 'mean'}
)
```
</details>
</details>
---
# Question 3
Gegeben ist folgender *pd.DataFrame* **df:**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8a98d285-ea0b-43af-860e-020ddd35c49c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYB2CSW7%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDZKjI%2FHBJRKUdO%2FSLc4R5Vq0nu3xLV1lnlp9UYbELnjQIhAL%2FqKd43bqB8DiAhtZbtIOUe9Emdn%2BkhJsYXg5nP5F45Kv8DCCoQABoMNjM3NDIzMTgzODA1IgzJtgEJi5bbYjRpc8Iq3AOU%2FnEd4qLAeeyrC0olJoqUj0txmO%2BNJOWfg1Isnf3eVrbbnewOSx45AQoa6aQnYYl8j6OlVzfNsPCN1BMifT6V3YbNclx6zTpTLEjK6DDCta%2FQ83m5Xjgok1xebs4meX5N1QOlGzUgM5fh8y6zplyo34cK%2FFRtFgvMJJxfZnszX3ea1nfwXR2j%2FilWgf0zaTH41oUuEGP3Ef9e%2BMCf4l8AMiLFN6CFNzJmbN5TZHwcq5S6yW1zfZpcE2hqugruNVvzGX9GLlVajgczgbAFprTBVECkVPPOgqWg4HEh7XBc7mtozoE5ZcAR2gk3qePS7pQAH1XGMKnNGct4wk2Jqx9FWLqLZOFkKypWTUZnuLKL3QuY964yrwednBg%2Brl1lDtEEREiyRY1m%2FLFHhPTw%2Fgo5Do5NyCOHuZFREbt%2Bj9IabM0%2FD2dPFOtPnjL0Tr1kxzm%2FICn13maYYCNGn1KWN92%2BDCLfGmpx2P4uVTVBEdKEXkW6KyxRhnw3qk4xjMsw%2BQ9DGW8pYwf4xIkq6WIZvp1vIelZLGJdyi3My8gMfIuKVZJI1q0qGANaPvwXsPSfR1v4NL%2FXRLzBzGpJHeI7tPZtKv9J%2BmLQl2teKbxxFov4hTZyc1Wpx87iHtFBvTDgl%2FjJBjqkAbC4NGAX0Tn8F553IPwi9cn8RoE5%2FP%2Bd%2FjCvMHkaDXRfW887BFLIIz6g98lf%2BH0jsDug6gno8jF%2FT%2BbZPr0CCcBmsIBWnGQzWg%2FVJe39SjRX1brN4rW6NmDVQxdbYSDMzr2RtkMg4RCc3LTczPBhQ%2BP2MxqIZ19DqnpgTWmBN00Qe71dzvD63lIMJx76NTus33%2B6Haj3iUkz8sblG7erAAduzAPB&X-Amz-Signature=da38f5761618a1f62c9fd0a7b9485f5b4bced18b6f5485628c5eee819aa58ac1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Welche der folgenden Codezeilen gibt das Durchschnittsalter je Geschlecht zurück?
❌ df['Alter'].mean()
❌ dt.groupby('Alter').mean()
❌ df['Geschlecht'].value_counts()
✅ df.groupby('Geschlecht')['Alter'].mean()
❌ df.groupby('Alter')['Geschlecht'].mean()
❌ keine der anderen genannten

<details>
<summary>Explanation</summary>

> 💡 **[groupby()](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15), [value_counts()](/1867045b058343e1a66b677961515907#b585cb62f9dd4878aa31acb88e071f0e), [mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
❌ **Incorrect**. Only the average age across **both genders** is returned.
```python
df['Alter'].mean()
36
```
❌ **Incorrect**. The average age for **each unique age** is returned, which is of course the age itself as there are **not more than one person** with the same age.
```python
dt.groupby('Alter').mean()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/14cd5803-adf1-44ab-99ee-6770a9d73201/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO7W72XX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIF0JXHlmEoiqEfTCWQA3GKI6ahXVzh1y5nZJgOqjiCk8AiBun%2BqYzKIZjobHVOSRWT10OQxE3M2SbaSa%2FBhPV4iGzCr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMRT2vHd2b7UkUF2f5KtwD3qPKJZHLehCTD2Oh88uQ3PuuOonbxLjGUsgzYaPXKFZRcug4H22W0tE5tAvnWUrnSYWU8A2iqX3zxb1AoW2CHTQW9gyAPgqBooLVup1Rvp5B9tvjWq8gXJOyaYs8U9eDobYc3vYsODzqgICR5ZHh%2Bq812SDSppPl5Q4%2B2p4%2BKMjXGAZ3HJFc7BssLw1oM3LfwA0bCYxWAeN97LF8sF%2Boy2GXOydNPr3MKJyMQ67EgDj4ZL%2FMkvECjOZrn64Ri8ydv862clhw0NiAz%2BIpYtCgCQ5fU86uUIDI2MDRKSVnpI8OQMM5cLJ4tw6QQlZNQJ%2FvW1tGg1ICcI6uURhypKaJKq8r%2BnKM%2FjlIxh5jUvOaOdsZ2CC%2BwCQATXZYtTfQEfsn8S%2FW8skNS5Zqg54Shf3276d%2B8KD1s%2BDbFoUwBGJQQvKHzkulbF%2F%2Fy4%2BkO9gvg6fnzwtzzyNwQtdxysKY2kEopZKPiZ%2F4ILijQ%2Bo7%2B0AzqLQUgeWON7N%2BXIoQLg1IBxrDMx%2FF0bfnZfQeNSoHg2xYZkcBunfbnLF%2FaZFwRmld7wb2HrIJij0fn5jNxN7IsA1e6jgyqiUtUkZ5uWT%2FFTXaJeJ5g3g8FskqgvEFus3yUuxCFX8qXgIRDLweKfswkpb4yQY6pgGqI2imyxRBRFWNBLXqf%2BNlOS7JnxZKERWwWd0XuE2YKTD9J8w0jgL2jfSo%2FkuI7brzlxC5a34OkaLG25q%2FRfj7dQBba2nPwqLs6IovNhP554%2BZAO60f0Gb%2BzKsZCHpsoqRDWAWmXVdjX9TOx4jaqnBr2NyXjEVTUgjBS8jwFZqOd6va8wYea2voqPIBy0n%2F35529j1K1MfnP1pASYgUqPtcgORG4QY&X-Amz-Signature=4c6b5e2fe9455633a64db9b49a1afd956961dd78bf94c16c87567354c3af9247&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. A series containing the **number of persons** for both genders is returned.
```python
df['Geschlecht'].value_counts()

m    5
w    5
Name: Geschlecht, dtype: int64
```
✅ **Correct**. A series containing the **average age** for both genders is returned.
```python
df.groupby('Geschlecht')['Alter'].mean()

Geschlecht
m    33.6
w    39.4
Name: Alter, dtype: float64
```
❌ **Incorrect**. A `TypeError` is returned as **gender is a string** and it is not possible to compute an arithmetic mean (average) with text data (strings).
❌ **Incorrect**. [Statement 4](/e1a14712985b4466992e86be0e4cd8bc) is correct.
</details>
---
# Question 4
Gegeben ist eine CSV-Datei mit dem Namen "data.csv', die die folgenden Informationen enthält:
```plain text
Name,Alter,Land
John,25,USA
Emily,38,UK
Karin,33,Switzerland
Michael,35,USA
Sophia,28,Germany
Urs,25,Switzerland
Maximilian,20,Germany
```
Diese Informationen werden in folgendem Programm verwendet, welches das Durchschnittsalter aller Personen aus der Schweiz (Switzerland) berechnen und ausgeben sol:
```python
df = pd.read_csv('data.csv')
CH_data= df[df['Land'] == 'CH']
print("Durchschnittsalter der Personen aus der Schweiz:", df['Alter'].mean())
```
✅ Das Programm kann ausgeführt werden, ohne dass Python einen Fehler wirft.
❌ Das Programm gibt das Durchschnittsalter der Personen aus der Schweiz (Switzerland) korrekt aus.
✅ Das Programm ist in Zeile 2 fehlerhaft.
❌ Das Programm ist in Zeile 1 fehlerhaft.
✅ DasProgramm ist in Zeile 3 fehlerhaft.

<details>
<summary>Explanation</summary>

> 💡 **[read_csv()](/1867045b058343e1a66b677961515907#bb02198699ce440f948c4c281f1957ac), [mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5), [selecting rows based on condition](/1867045b058343e1a66b677961515907#a61901eaa28c4a7da25d80a1223b80f7)**
Let’s go through the code line-by-line to understand what is happening. 
First, the data is read from the csv file.
```python
df = pd.read_csv('data.csv')
```
![DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3482174a-0b14-479d-a944-3953a3e7bc02/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622R5Q6ZU%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCypuDkf73HikbFJ%2FW9jOzWVoK3yaL%2FI2pal41MXhMk1QIgF%2BkuhuKCEP1fJ4RaEHBoe8jtsHSt1CSaL2p3Tc%2FZllgq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDErccOAAML%2FvGSKKLCrcA3m8UJzmMKaZhUfhXL3DqkgowErW2uc9o4BnkIns0DWFaDNaDG5P40HcX%2BxVQnArzl0dSww8%2FP1qpOPCO92OEfRXMNNdbzKjGijSpWnn0sXVvlxoPv1QUzYlhunCjdyG8HANV6QMW832CV0Egz2zrVtjY%2BfGWXTis4ZMrj4X9KWLdaSkGxkB2LBBpcm2KNMm2ovPtztu8J3zghAaIl7dsxoE06kEO%2FWQWYN%2FCTDtC5EywDKIvQC3veoONGfiQx1E91vfiTKQwCcCyIY%2B7Z%2Bcg%2B4ZRZaHcSD%2Fu1rRDt8bUJZQqjE7TGCVweeeKRBZ9%2FIowoc7x9T3EhxXmfIpaywmjyQ5%2BHnL2ZOl%2BxBZ7U1eUhbPrOiQRBycQM2AbyVwKdhtrXYIkLVH05i%2BTUb1dB%2FYHS1aPaT2Fdp1%2F3vrooiSE0vFgcJqH2AHBomPl1GvjYWVD%2FwiGoqTKustzfeDxEzSaqtp9jmq5in1aPp9whutsiLuk9X%2B942L9OitNnAtfNbqs6NP44f%2Fh3muDh2U87wBHZc8%2FGMxMqPrG%2FsAn2j1e%2B13x9vilXyRKGGSZjb%2FFJZ33ujxgSuHrmJm3D28pcMdSSMP4%2F%2FNr%2FVNqzF2m8p9AWEKAEnIC%2BVPcORKq%2BGfML%2BW%2BMkGOqUBMZP0CVne6smD85I8y7DuqEmaH2YteO0tFYqOCJe6GOA2IXIcHdYnS9eag5UuM2wyYVzfrr4qzQGrir%2BYZiuCBEFd8AoYdh5QKHH%2F1RVic4Q1ToichTw8EJCW6mPUTEUpLKsCjMfTlYHZ8BSI29%2Fk%2FF2oemcEapyeVLnRPzef5XxeOHxyp%2FnPzCxCBLcxBl2YfqFoC5JQMJ5p%2BDJgeapkj3pTNOBd&X-Amz-Signature=b4c5f13d08cc61cd54b479a9354e92c0a3a635bb7a900c2a9564bc24365652fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Next, all records are selected that contain the value `'CH'` in column `Land`.
```python
CH_data = df[df['Land'] == 'CH']
```
However, as no record contains the value `'CH'` in column `Land` the DataFrame **CH_data** is **empty**.
![Empty DataFrame CH_data](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f7a4b601-3675-4abc-b01d-3486ce99183e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622R5Q6ZU%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCypuDkf73HikbFJ%2FW9jOzWVoK3yaL%2FI2pal41MXhMk1QIgF%2BkuhuKCEP1fJ4RaEHBoe8jtsHSt1CSaL2p3Tc%2FZllgq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDErccOAAML%2FvGSKKLCrcA3m8UJzmMKaZhUfhXL3DqkgowErW2uc9o4BnkIns0DWFaDNaDG5P40HcX%2BxVQnArzl0dSww8%2FP1qpOPCO92OEfRXMNNdbzKjGijSpWnn0sXVvlxoPv1QUzYlhunCjdyG8HANV6QMW832CV0Egz2zrVtjY%2BfGWXTis4ZMrj4X9KWLdaSkGxkB2LBBpcm2KNMm2ovPtztu8J3zghAaIl7dsxoE06kEO%2FWQWYN%2FCTDtC5EywDKIvQC3veoONGfiQx1E91vfiTKQwCcCyIY%2B7Z%2Bcg%2B4ZRZaHcSD%2Fu1rRDt8bUJZQqjE7TGCVweeeKRBZ9%2FIowoc7x9T3EhxXmfIpaywmjyQ5%2BHnL2ZOl%2BxBZ7U1eUhbPrOiQRBycQM2AbyVwKdhtrXYIkLVH05i%2BTUb1dB%2FYHS1aPaT2Fdp1%2F3vrooiSE0vFgcJqH2AHBomPl1GvjYWVD%2FwiGoqTKustzfeDxEzSaqtp9jmq5in1aPp9whutsiLuk9X%2B942L9OitNnAtfNbqs6NP44f%2Fh3muDh2U87wBHZc8%2FGMxMqPrG%2FsAn2j1e%2B13x9vilXyRKGGSZjb%2FFJZ33ujxgSuHrmJm3D28pcMdSSMP4%2F%2FNr%2FVNqzF2m8p9AWEKAEnIC%2BVPcORKq%2BGfML%2BW%2BMkGOqUBMZP0CVne6smD85I8y7DuqEmaH2YteO0tFYqOCJe6GOA2IXIcHdYnS9eag5UuM2wyYVzfrr4qzQGrir%2BYZiuCBEFd8AoYdh5QKHH%2F1RVic4Q1ToichTw8EJCW6mPUTEUpLKsCjMfTlYHZ8BSI29%2Fk%2FF2oemcEapyeVLnRPzef5XxeOHxyp%2FnPzCxCBLcxBl2YfqFoC5JQMJ5p%2BDJgeapkj3pTNOBd&X-Amz-Signature=b7bab6d49d1f7c9144b4d8448a87f6c41a8bea6406ff0dc840d1ee087bab1376&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now the average value of column `Alter` in DataFrame **df** is calculated.
```python
print("Durchschnittsalter der Personen aus der Schweiz:", df['Alter'].mean())

Durchschnittsalter der Personen aus der Schweiz: 29.142857142857142
```
However, is the average age for persons from Switzerland really **29.14** years?
We can see that **Karin** and **Urs** are from Switzerland. Karin is 33 years and Urs 25 years old. Thus the average age is **exactly** (33 + 25) / 2 = **29** **years**.
Hence, the code has some errors. 
The **first error** is in **line 2** where we are aiming to select only the persons from Switzerland. Instead of using `'CH'` as criteria we should us `'Switzerland'` as the column Land does not contain country abbreviations but rather the **full names** of the countries.
If we update the code in line 2 accordingly, the DataFrame **CH_data** is no longer empty.
```python
CH_data = df[df['Land'] == 'Switzerland']
```
![DataFrame CH_data](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b1e07a43-f2b1-481b-ba63-0c69398aa0da/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622R5Q6ZU%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCypuDkf73HikbFJ%2FW9jOzWVoK3yaL%2FI2pal41MXhMk1QIgF%2BkuhuKCEP1fJ4RaEHBoe8jtsHSt1CSaL2p3Tc%2FZllgq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDErccOAAML%2FvGSKKLCrcA3m8UJzmMKaZhUfhXL3DqkgowErW2uc9o4BnkIns0DWFaDNaDG5P40HcX%2BxVQnArzl0dSww8%2FP1qpOPCO92OEfRXMNNdbzKjGijSpWnn0sXVvlxoPv1QUzYlhunCjdyG8HANV6QMW832CV0Egz2zrVtjY%2BfGWXTis4ZMrj4X9KWLdaSkGxkB2LBBpcm2KNMm2ovPtztu8J3zghAaIl7dsxoE06kEO%2FWQWYN%2FCTDtC5EywDKIvQC3veoONGfiQx1E91vfiTKQwCcCyIY%2B7Z%2Bcg%2B4ZRZaHcSD%2Fu1rRDt8bUJZQqjE7TGCVweeeKRBZ9%2FIowoc7x9T3EhxXmfIpaywmjyQ5%2BHnL2ZOl%2BxBZ7U1eUhbPrOiQRBycQM2AbyVwKdhtrXYIkLVH05i%2BTUb1dB%2FYHS1aPaT2Fdp1%2F3vrooiSE0vFgcJqH2AHBomPl1GvjYWVD%2FwiGoqTKustzfeDxEzSaqtp9jmq5in1aPp9whutsiLuk9X%2B942L9OitNnAtfNbqs6NP44f%2Fh3muDh2U87wBHZc8%2FGMxMqPrG%2FsAn2j1e%2B13x9vilXyRKGGSZjb%2FFJZ33ujxgSuHrmJm3D28pcMdSSMP4%2F%2FNr%2FVNqzF2m8p9AWEKAEnIC%2BVPcORKq%2BGfML%2BW%2BMkGOqUBMZP0CVne6smD85I8y7DuqEmaH2YteO0tFYqOCJe6GOA2IXIcHdYnS9eag5UuM2wyYVzfrr4qzQGrir%2BYZiuCBEFd8AoYdh5QKHH%2F1RVic4Q1ToichTw8EJCW6mPUTEUpLKsCjMfTlYHZ8BSI29%2Fk%2FF2oemcEapyeVLnRPzef5XxeOHxyp%2FnPzCxCBLcxBl2YfqFoC5JQMJ5p%2BDJgeapkj3pTNOBd&X-Amz-Signature=dacc650e56a2af27e0a65d1218443e418115241b6f07a4df5d0597723c13a377&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we can compute the average age in line three based on this DataFrame. To do so, we must **correct the code**: We must access the column `Alter` in **CH_data** and not in **df**.
```python
print("Durchschnittsalter der Personen aus der Schweiz:", CH_data['Alter'].mean())

Durchschnittsalter der Personen aus der Schweiz: 29.0
```
We can see, by **correcting the errors in line 2 and line 3**, the code works now as intended: it returns the average age of all persons from Karin and Urs, the two Swiss people in DataFrame **df**.
</details>
---
# Question 5
Welche der folgenden Datentypen kann die Abfrage von Inhalten einer *pd.Series* zurückgeben?
✅ str
✅ pd.Series
✅ int
✅ Car
✅ float
✅ pd.DataFrame

<details>
<summary>Explanation</summary>

> 💡 **[Python datatypes](/5b0832dbf9454eb1941b7632e68a9abb#d1c2e1bb9bac46b8afbe6f4f6950edd9), [Pandas datatypes](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
✅ **Correct**. It is possible to store strings in a DataFrame cell / Series.
✅ **Correct**. It is possible to store a Series object in a DataFrame cell / Series. 
✅ **Correct**: It is possible to store integers in a DataFrame cell / Series.
✅ **Correct**. It is possible to store object variables of custom datatypes in a DataFrame cell / Series.
✅ **Correct**. It is possible to store a float in a DataFrame cell / Series.
✅ **Correct**. It is possible to store a variable in a DataFrame cell / Series that contains another DataFrame.
</details>
---
