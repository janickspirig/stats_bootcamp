---
title: "Quiz 7"
notion_id: "70c60c9e-3f87-4967-97b6-fe98ea0b459b"
notion_url: "https://www.notion.so/Quiz-7-70c60c9e3f87496797b6fe98ea0b459b"
exported_at: "2025-12-13T23:10:28.530348+00:00"
---

# Quiz 7

## Question 1
Gegeben ist der IRIS-Datensatz aus Assignment 9. Die Daten sind im DataFrame IRIS wie im Assignment geladen.

Ihr Ziel ist es, für jede Variable (*feature*) mit Verhältnisskala (*ratio scale*) der einzelnen Beobachtungen und gruppiert nach Untergattungen (*species*) jeweils den Minimal-, Maximal- und Durchschnittswert auszugeben. Die gewünschte Ausgabe soll also ähnlich der folgenden Darstellung sein:
```plain text
   variable 1
             min       max        mean

species A       4.3         5.8       5.006
species B       4.9         7.0       5.936
species C       4.9         7.9       6.588
```

```plain text
   variable 2
             min        max       mean

species A        2.3        4.4       3.418
species B        2.0        3.4       2.770
species C        2.2        3.8       2.974

                           variable n
                ...
```
Dazu haben Sie den nachfolgenden Code geschrieben. Dieser funktioniert allerdings überhaupt nicht wie gewünscht. Wo befindet sich der eine Fehler? Bitte geben Sie die Zeilennummer als ganze Zahl an.
```python
1    for col in IRIS.columns:
2        if col == 'species':
3            print(
4                IRIS.groupby('species').agg(
5                    {
6                        col:
7                        [
8                            'min',
9                            'max',
10                           'mean'
11                       ]
12                   }
13               ),
14               '\\n'
15           )
```

**2**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[for-loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [if-statement](/5b0832dbf9454eb1941b7632e68a9abb#244a89d427db41da893178dcdf8d51d8), [.groupby()](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15), [.agg()](/1867045b058343e1a66b677961515907#1c8f902fb8774ff7ab8c9bd1d9f76684)**
Let's break down the provided code and the answer options to understand why the correct answer is marked as it is.
### Code Explanation
1. `for col in IRIS.columns:`
- This line starts a loop that iterates over each column name in the DataFrame `IRIS`.
1. `if col == 'species':`
- This line checks if the current column name is `'species'`.
1. `print(`
- This line starts a `print` statement to output the results.
1. `IRIS.groupby('species').agg(`
- This line groups the DataFrame `IRIS` by the `'species'` column and applies aggregation functions.
1. `{`
- This line starts a dictionary to specify the aggregation functions.
1. `col:`
- This line uses the current column name as the key in the dictionary.
1. `[`
- This line starts a list of aggregation functions.
1. `'min',`
- This line specifies the `min` function.
1. `'max',`
- This line specifies the `max` function.
1. `'mean'`
- This line specifies the `mean` function.
1. `]`
- This line closes the list of aggregation functions.
1. `}`
- This line closes the dictionary.
1. `),`
- This line closes the `agg` function and the `groupby` function.
1. `'\\n'`
- This line adds a newline character for formatting.
1. `)`
- This line closes the `print` statement.
### Identifying the Error
The code is intended to print the minimum, maximum, and mean values for each feature, grouped by species. However, the code only prints the results when the column name is `'species'`, which is not what we want. We want to skip the `'species'` column and process the other columns instead.
### Correct Answer
✅ **2**
The error is in line 2: `if col == 'species':`. This line should be changed to `if col != 'species':` to skip the `'species'` column and process the other columns.
### Corrected Code
Here is the corrected code:
```python
1    for col in IRIS.columns:
2        if col != 'species':  # Change this line to skip the 'species' column
3            print(
4                IRIS.groupby('species').agg(
5                    {
6                        col:
7                        [
8                            'min',
9                            'max',
10                           'mean'
11                       ]
12                   }
13               ),
14               '\\n'
15           )
```
Now, the code will correctly print the minimum, maximum, and mean values for each feature, grouped by species, excluding the `'species'` column itself.
</details>
---
## Question 2
**Gegeben sind zwei pd.DataFrame-Objekte ORDERS und PERSONS. Die Ausführung folgender Code-Zeile führt zu nachfolgender Ausgabe:**
```python
print(ORDERS.columns, ORDERS.index, PERSONS.columns, PERSONS.index, sep='\\n')
```
**Ausgabe:**
```python
Index(['products'], dtype='object')
Index([2, 3, 7, 8, 10, 13, 14, 15, 16,
...
99983, 99984, 99985, 99989, 99991, 99993, 99994, 99998, 99999],
dtype='int64', name='purchase-id', length=69703)
Index(['name',  'birthdate'], dtype='object')
Index([0, 1, 0, 3, 5, 8, 9, 10, 15, 16,
...
99979, 99980, 99981, 99984, 99987, 99991, 99992, 99995, 99997, 99998],
dtype='int64', name='purchase-id', length=59805)
```
Sie wollen beide Dataframes so zusammenführen (*merge*), dass der resultierende Dataframe alle Personen aus **PERSONS** enthält und bei den Personen, die eine Bestellung (*order*) getätigt haben, ausserdem auch die zugehörigen Informationen des **ORDERS** Dataframes enthält. Bestellungen, die zu keiner Person aus **PERSONS** zugeordnet werden können, sollen nicht enthalten sein. Bei der Zuordnung der Einträge aus **PERSONS** und **ORDERS** fungiert purchase-id als Schlüssel.
Bitte ersetzen Sie die im Programm mit AAA - EEE markierten Stellen so, dass die gewünschte Funktionalität erreicht wird.
```python
pd.merge(
    AAA,
    ORDERS,
    BBB_index=CCC,
    right_DDD=True,
    how=EEE
)
```
| AAA | ✅ PERSONS |
| --- | --- |
| BBB | ✅ left |
| CCC | ✅ True |
| DDD | ✅ index |
| EEE | ✅ 'left' |

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
Let's break down the provided code and the answer options to understand why the correct answer is marked as it is.
### Understanding the Code and Output
1. **Code to Print DataFrame Attributes:**
```python
print(ORDERS.columns, ORDERS.index, PERSONS.columns, PERSONS.index, sep='\\n')
```
- This code prints the column names and index values of the `ORDERS` and `PERSONS` DataFrames.
- `sep='\\n'` ensures that each attribute is printed on a new line.
1. **Output Explanation:**
```python
Index(['products'], dtype='object')
Index([2, 3, 7, 8, 10, 13, 14, 15, 16,
...
99983, 99984, 99985, 99989, 99991, 99993, 99994, 99998, 99999],
dtype='int64', name='purchase-id', length=69703)
Index(['name', 'birthdate'], dtype='object')
Index([0, 1, 0, 3, 5, 8, 9, 10, 15, 16,
...
99979, 99980, 99981, 99984, 99987, 99991, 99992, 99995, 99997, 99998],
dtype='int64', name='purchase-id', length=59805)
```
- `ORDERS` DataFrame has one column named `'products'` and an index named `'purchase-id'` with 69703 entries.
- `PERSONS` DataFrame has two columns named `'name'` and `'birthdate'` and an index named `'purchase-id'` with 59805 entries.
### Merging DataFrames
To merge the DataFrames as described, we need to:
- Include all rows from `PERSONS`.
- Include matching rows from `ORDERS` based on the `purchase-id`.
- Exclude rows from `ORDERS` that do not have a corresponding `purchase-id` in `PERSONS`.
### Correct Answer Breakdown
1. **AAA: ****`PERSONS`**
- We start with the `PERSONS` DataFrame because we want to include all persons.
- ✅ **Correct**: `PERSONS`
1. **BBB: ****`left`**
- We perform a left join to include all rows from the left DataFrame (`PERSONS`) and only matching rows from the right DataFrame (`ORDERS`).
1. **CCC: ****`True`**
- We specify that the join should be done on the index of the left DataFrame (`PERSONS`).
1. **DDD: ****`index`**
- We specify that the join should be done on the index of the right DataFrame (`ORDERS`).
1. **EEE: ****`'left'`**
- We specify the type of join as a left join to include all rows from `PERSONS`.
### Final Code
```python
pd.merge(
    PERSONS,  # AAA
    ORDERS,  # ORDERS DataFrame
    left_index=True,  # BBB_index=CCC
    right_index=True,  # right_DDD=True
    how='left'  # EEE
)
```
### Explanation of the Correct Answer
- **AAA: ****`PERSONS`**: We start with the `PERSONS` DataFrame because we want to include all persons.
- **BBB: ****`left`**: We perform a left join to include all rows from the left DataFrame (`PERSONS`) and only matching rows from the right DataFrame (`ORDERS`).
- **CCC: ****`True`**: We specify that the join should be done on the index of the left DataFrame (`PERSONS`).
- **DDD: ****`index`**: We specify that the join should be done on the index of the right DataFrame (`ORDERS`).
- **EEE: ****`'left'`**: We specify the type of join as a left join to include all rows from `PERSONS`.
By using these parameters, we ensure that all persons from the `PERSONS` DataFrame are included in the result, along with their corresponding orders from the `ORDERS` DataFrame, if any.
</details>
---
## Question 3
Gegeben ist folgende *txt-Datei*, sie liegt in einem Unterverzeichnis *data*:
### Daten.txt
```plain text
Name,Alter,Land
John,25,USA
Emily,30,UK
Karin,33,Switzerland
Michael,35,USA
Sophia,28,Germany
Urs,25,Switzerland
Maximilian,20,Germany
```
Diese Informationen werden in folgendem Programm verwendet, welches das Durchschnittsalter aller Personen aus den USA berechnen und ausgeben soll:
```python
print(f"""
Durchschnittsalter der Personen aus den USA:
{
    pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']['Alter'].mean()
}
""")
```
Bitte markieren Sie **alle korrekten** Aussagen:
✅ Das Programm kann ausgeführt werden, ohne dass Python einen Fehler wirft.
❌ Die `read_csv`-Funktion braucht weitere Parameter, um mit den gegebenen Daten das richtige Ergebnis zu erzeugen.
❌ Das Programm müsste statt der aktuellen Lösung in Zeile 4 zuerst die Spalte Alter selektieren, statt gleich den Wert USA zuzuweisen.
❌ Die `read_csv`-Funktion benötigt eine csv-Datei. Die hier genutzte txt-Datei ist dafür ungeeignet.
✅ Das Programm gibt das Durchschnittsalter der Personen aus den USA korrekt aus.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.read_csv()](/1867045b058343e1a66b677961515907#bb02198699ce440f948c4c281f1957ac), [.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
Let's break down the provided code and the answer options to understand why the correct answers are marked as they are.
### Provided Code Explanation
```python
print(f"""
Durchschnittsalter der Personen aus den USA:
{
    pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']['Alter'].mean()
}
""")
```
1. **`pd.read_csv('data/Daten.txt')`**:
- This function reads the file `Daten.txt` located in the `data` directory and loads it into a DataFrame.
- The file is in CSV format (Comma-Separated Values), which `read_csv` can handle even if the file extension is `.txt`.
1. **`pd.read_csv('data/Daten.txt')['Land'] == 'USA'`**:
- This part filters the DataFrame to include only the rows where the 'Land' column has the value 'USA'.
1. **`pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']`**:
- This applies the filter to the DataFrame, resulting in a new DataFrame containing only the rows where 'Land' is 'USA'.
1. **`pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']['Alter']`**:
- This selects the 'Alter' column from the filtered DataFrame.
1. **`pd.read_csv('data/Daten.txt')[pd.read_csv('data/Daten.txt')['Land'] == 'USA']['Alter'].mean()`**:
- This calculates the mean (average) of the 'Alter' column for the filtered rows.
1. **`print(f"""\\nDurchschnittsalter der Personen aus den USA:\\n{ ... }\\n""")`**:
- This prints the average age of people from the USA using an f-string for formatting.
### Answer Explanations
✅ **Correct,** the code uses valid syntax and functions from the `pandas` library, so it will run without errors as long as the `pandas` library is installed and the file path is correct.
❌ **Incorrect, **the `read_csv` function works correctly with the default parameters for this file format. No additional parameters are needed.
❌ **Incorrect, t**he current approach is correct. It first filters the rows by 'Land' and then selects the 'Alter' column, which is the correct sequence to get the average age of people from the USA.
❌ **Incorrect, **the `read_csv` function can read files with any extension as long as the content is in CSV format. The `.txt` extension does not make the file unsuitable.
✅ **Correct, **the code correctly filters the DataFrame and calculates the mean of the 'Alter' column for rows where 'Land' is 'USA', so it will output the correct average age.
</details>
---
## Question 4
Sie haben erfolgreich aus einer relationalen Datenbank Kundendaten (*customers*) in einen DataFrame *df* geladen. Der folgende Code gibt die nachfolgenden Werte zurück:
```python
df = pd.read_sql('SELECT * FROM customers', DB)
df.tail()
```
| CustomerId | FirstName | LastName | Company | Address | City | State | Country | PostalCode | Phone | Fax | Email | SupportRepId |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 54 | 55 | Mark | Taylor | None | 421 Bourke Street | Sidney | NSW | Australia | 2010 | +61 (02) 9332 3633 | None | [mark.taylor@yahoo.au](mailto:mark.taylor@yahoo.au) |
| 55 | 56 | Diego | Gutiérrez | None | 307 Macacha Güemes | Buenos Aires | None | Argentina | 1106 | +54 (0)11 4311 4333 | None | [diego.gutierrez@yahoo.ar](mailto:diego.gutierrez@yahoo.ar) |
| 56 | 57 | Luis | Rojas | None | Calle Lira, 198 | Santiago | None | Chile | None | +56 (0)2 635 4444 | None | [luisrojas@yahoo.cl](mailto:luisrojas@yahoo.cl) |
| 57 | 58 | Manoj | Pareek | None | 12,Community Centre | Delhi | None | India | 110017 | +91 0124 38983988 | None | [manoj.pareek@rediff.com](mailto:manoj.pareek@rediff.com) |
| 58 | 59 | Puja | Srivastava | None | 3,Raj Bhavan Road | Bangalore | None | India | 560001 | +91 080 22289999 | None | [puja_srivastava@yahoo.in](mailto:puja_srivastava@yahoo.in) |
Für das Jubiläumsfest der Firma wollen Sie nun den/die erste/n Kunden/in aus jedem Land (*Country*) ausfindig machen. Dabei gehen Sie davon aus, dass diese Person die niedrigste Kundennummer (*CustomerId*) für das jeweilige Land hat.
Schreiben Sie Python-Code welcher eine *pandas.Series* zurückgibt, welche die Ländernamen als Label und die entsprechende Kundennummer als Werte enthält.
Schreiben Sie den Code in einer Zeile und halten Sie den Code minimal, d.h. verzichten Sie auf unnötige Sortierungen, etc. Wo notwendig verwenden Sie ausschließlich* Single Quotes* ( ' ' ), anstatt *Double* ( " " ) oder *Triple Quotes* ( """ """ ).
Auch wenn die Ausgabe es nahelegen scheint, können Sie nicht davon ausgehen, dass die Kundennummern in *df* in irgendeiner Weise sortiert sind.
Tip: Die groupby()-Methode wird hier hilfreich sein.

**Code:**
```python
df.groupby('Country')['CustomerId'].min()
```

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.groupby()](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15), [.min()](/1867045b058343e1a66b677961515907#dbdb31a72fac4ce0bc52e49458a2bf93)**
### Code Explanation
```python
df.groupby('Country')['CustomerId'].min()
```
1. **`df.groupby('Country')`**:
- This part of the code groups the DataFrame `df` by the 'Country' column. Grouping means that all rows with the same country name are put together.
1. **`['CustomerId']`**:
- After grouping by 'Country', this part selects the 'CustomerId' column from each group. So now, we are focusing only on the customer IDs within each country group.
1. **`.min()`**:
- This function calculates the minimum value of the 'CustomerId' column for each country group. Since we want the first customer (the one with the lowest customer ID) from each country, this function is perfect for our needs.
### Example DataFrame and Output
Given the example DataFrame:
| CustomerId | FirstName | LastName | Country |
| --- | --- | --- | --- |
| 54 | Mark | Taylor | Australia |
| 55 | Diego | Gutiérrez | Argentina |
| 56 | Luis | Rojas | Chile |
| 57 | Manoj | Pareek | India |
| 58 | Puja | Srivastava | India |
The output of the code would be a pandas Series like this:
```plain text
Country
Argentina    55
Australia    54
Chile        56
India        57
Name: CustomerId, dtype: int64
```
This Series shows the lowest 'CustomerId' for each country, which is exactly what we need for the company's anniversary event.
</details>
---

