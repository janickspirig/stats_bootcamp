---
title: "Quiz 6"
notion_id: "73d1ad1d-44a7-40a9-93f4-ba6f9e8f51e4"
notion_url: "https://www.notion.so/Quiz-6-73d1ad1d44a740a993f4ba6f9e8f51e4"
exported_at: "2025-12-13T23:10:43.387669+00:00"
---

# Quiz 6

## Question 1 
Gegeben ist folgender *pd.DataFrame df*. Die Spalte **index** ist definiert als der Index von df.
| index | value0 | value1 |
| --- | --- | --- |
| 2 | 947 | 363 |
| 22 | 926 | 30 |
| 10 | 403 | 66 |
| 25 | 581 | 10 |
| 31 | 714 | 513 |
| 5 | 897 | 604 |
| 13 | 118 | 827 |
| 14 | 56 | 514 |
| 33 | 154 | 82 |
Welcher **Wert** wird von folgendem Code zurückgegeben: *df.loc[25].sum()*
**591**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.sum()](/1867045b058343e1a66b677961515907#6f1bd7bccbe24ecf8bcb37abc05b0550)**
1. **DataFrame Structure**:
- The DataFrame `df` has three columns: `index`, `value0`, and `value1`.
- The `index` column is set as the index of the DataFrame, meaning it is used to label the rows.
```plain text
| index | value0 | value1 |
|-------|--------|--------|
| 2     | 947    | 363    |
| 22    | 926    | 30     |
| 10    | 403    | 66     |
| 25    | 581    | 10     |
| 31    | 714    | 513    |
| 5     | 897    | 604    |
| 13    | 118    | 827    |
| 14    | 56     | 514    |
| 33    | 154    | 82     |
```
1. **Code Explanation**:
- `df.loc[25]`:
- This line accesses the row in the DataFrame where the index is `25`.
- The row with index `25` is:
```plain text
| index | value0 | value1 |
|-------|--------|--------|
| 25    | 581    | 10     |
```
- `.sum()`:
- This method sums up all the values in the selected row.
- For the row with index `25`, the values are `581` and `10`.
- Summing these values:
```plain text
581 + 10 = **591**
```
</details>
---
## Question 2
In Assigment 8 haben wir aus der Datei *movies.csv* den pd.DataFrame **DF** geladen. Dieser enthält diverse Informationen über viele Filme. Wir nehmen an, dass er in der Spalte color die Information enthält, ob es sich um einen Farbfilm oder einen schwarz/weiss-Film handelt. In der Spalte *movie_facebook_likes* gibt es die absolute Anzahl von Likes des Filmplakiums für jeden Film und in der Spalte budget das Invest in einen Film in US-Dollar.
Hier wollen wir die Funktionen aus dem Assigment um eine weitere Funktion **black_and_white_or_color()** erweitern. Die Idee ist es herauszufinden, welche Filme (Gruppiert nach Werten von *color*) das bessere Invest sind - gemessen in Facebook-Likes pro Million US-Dollar Budget. Die Funktion soll einige Details zur Analyse auflisten und den vorteilhaftesten Wert für *color* zurückgeben.
Wir haben diese Funktion wie folgt implementiert:
```python
1  def black_and_white_or_color():
2      df = DF.copy()
3
4      # wir wollen keine Filme ohne Likes, da es das Ergebnis verzerren könnte
5      df = df[df['movie_facebook_likes'] > 0]
6
7      # hier bilden wir das Verhältnis zwischen den Facebook-Likes und
8      # dem Budget eines Films in Millionen Dollar
9      df['likes_per_million_budget'] = (df['movie_facebook_likes'] / df['budget']) * 1_000_000
10
11     # dann brauchen wir noch zwei Hilfsvariablen
12     colors = df['color'].unique().dropna()
13     color_rating = pd.Series()
14
15     # hier iterieren wir über alle gültigen Werte von 'colors'
16     # und geben das durchschnittliche Verhältnis 'likes_per_million_budget'
17     # für 'color' aus bzw. speichern diese in unserer Hilfsvariable
18     # color_rating. Wir nutzen zudem die .strip()-Methode
19     # um Datenuntypische Abstände zu beheben (Leerzeichen am Anfang oder Ende)
20     # der Werte in df['color'] bzw. 'colors'.
21     for color in colors:
22         print(f"""{color.strip(' ')} movies we get an average number of like.                                             per million dollar of
23     budget of {df[df['color'] == color]['likes_per_million_budget'].mean().round(0)}\\n""")
24         color_rating[color.strip(' ')] = df[df['color'] == color]['likes_per_million_budget'].mean().round(0)
25
26     # und ein Fazit:
27     print(f'Thus, {color_rating.idxmax().strip(' ')} movies may be a better invest')
28
29     return color_rating.idxmax().strip(' ')
```

Die Frage ist nun, warum funktioniert die Funktion nicht wie gewünscht?
1. ❌ In Zeile 21 darf die Target-Variable nicht *color* heissen, da es diesen Variablennamen schon in *df* bzw *DF* gibt.
1. ❌ In Zeile 12 braucht es ein axis Keyword-Argument, um die richtige Dimension zu wählen.
1. ❌ Zeile 23: Man kann einen DataFrame so nicht runden (round(0)).
1. ✅ Die Aussage ist falsch, denn tatsächlich funktioniert die vervollständigte Funktion wie beschrieben.
1. ❌ Die Aussage ist falsch, denn tatsächlich funktioniert die vervollständigte Funktion wie beschrieben.
1. ❌ In den Zeilen 22 und 23 sind die Anführungszeichen durcheinander geraten und es sind auch zu viele.
1. ❌ In Zeile 9 sind die Klammern falsch gesetzt, d.h. die Python-Syntax ist falsch.
1. ❌ Es ist nicht klar, mit welchem DataFrame wir eigentlich arbeiten, da wir mal df und mal DF nutzen, Python-Variablen aber case sensitive sind.
1. ❌ Es besteht ein anderes als die vorgenannten Probleme mit dem Code.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.copy()](/1867045b058343e1a66b677961515907#3ee249c7635744768a6ac56eb7e7f728), [.strip()](/5b0832dbf9454eb1941b7632e68a9abb#979e1c6634f843ffb1b7c6b31d78c060), [.round()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html), [.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
Let's break down the provided code and the answer options to understand why the correct answer is marked as it is.
### Code Explanation
1. **Function Definition and DataFrame Copy**
```python
def black_and_white_or_color():
    df = DF.copy()
```
- This defines a function named `black_and_white_or_color`.
- It creates a copy of the DataFrame `DF` and assigns it to `df`.
1. **Filtering Out Movies Without Likes**
```python
df = df[df['movie_facebook_likes'] > 0]
```
- This line filters out rows where the `movie_facebook_likes` column has a value of 0 or less.
1. **Calculating Likes Per Million Dollar Budget**
```python
df['likes_per_million_budget'] = (df['movie_facebook_likes'] / df['budget']) * 1_000_000
```
- This calculates the number of Facebook likes per million dollars of budget for each movie and stores it in a new column `likes_per_million_budget`.
1. **Unique Colors and Helper Variables**
```python
colors = df['color'].unique().dropna()
color_rating = pd.Series()
```
- `colors` stores unique values from the `color` column, excluding any `NaN` values.
- `color_rating` is an empty Pandas Series that will store the average likes per million budget for each color.
1. **Iterating Over Colors and Calculating Averages**
```python
for color in colors:
    print(f"""{color.strip(' ')} movies we get an average number of likes per million dollar of
budget of {df[df['color'] == color]['likes_per_million_budget'].mean().round(0)}\\n""")
    color_rating[color.strip(' ')] = df[df['color'] == color]['likes_per_million_budget'].mean().round(0)
```
- This loop iterates over each unique color.
- It prints the average likes per million budget for movies of that color.
- It also stores this average in the `color_rating` Series.
1. **Finding and Printing the Best Investment**
```python
print(f'Thus, {color_rating.idxmax().strip(' ')} movies may be a better invest')
return color_rating.idxmax().strip(' ')
```
- This prints which color of movies has the highest average likes per million budget.
- It returns the color with the highest average.
### Answer Options
1. ❌ **Incorrect, t**he variable `color` in the loop does not conflict with the column name `color` in the DataFrame.
1. ❌ **Incorrect, **the `unique()` method does not require an `axis` argument.
1. ❌ Inc**orrect, **the `round(0)` method is being applied on a single value (the mean of likes per million budget) which does not cause any issue.
1. ✅ **Correct,** the function works as described.
1. ❌ **Incorrect, **repeated incorrect statement.
1. ❌ **Incorrect, **the quotation marks are correctly used for the f-string.
1. ❌ **Incorrect, **the parentheses in line 9 are correctly placed.
1. ❌ **Incorrect,** the code consistently uses `df` after copying `DF`.
1. ❌ **Incorrect,** because the code works.
</details>
---
## Question 3
Gegeben ist ein *pd.DataFrame* **df**. Dieser hat neben einem Index eine Spalte **value0** und eine Spalte **value1**. Die beiden Spalten enthalten ganzzahlige (integer) Werte, jedoch fehlen auch einige Werte (NaN).
Bitte schreiben Sie Python-Code, welcher den Durchschnittswert (mean) der Werte in Spalte **value1** zurückgibt. Bei der Berechnung sollen nur die Werte von **value1** berücksichtigt werden, welche grösser als **10** sind. Schreiben Sie unter Verwendung der *mean()*-Methode aus Pandas nur eine Codezeile und verwenden Sie keine anderen zusätzlichen Libraries als Pandas. Sie können davon ausgehen, dass Pandas als *pd* importiert wurde.

**df.loc[df['value1']>10,'value1'].mean()**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
1. **Understanding the Task:**
- We need to calculate the mean of the values in the column `value1` of a DataFrame `df`.
- Only consider values in `value1` that are greater than 10.
- Use the `mean()` method from Pandas.
1. **Correct Code Analysis:**
- `df.loc[df['value1'] > 10, 'value1'].mean()`
- `df['value1'] > 10` creates a boolean Series where each element is `True` if the corresponding element in `value1` is greater than 10, and `False` otherwise.
- `df.loc[df['value1'] > 10, 'value1']` uses `.loc` to filter the DataFrame `df` to include only rows where `value1` is greater than 10, and then selects the `value1` column.
- `.mean()` calculates the mean of the filtered `value1` values.
</details>
---
## Question 4
Gegeben ist ein pd.*DataFrame* **df**, welcher mindestens eine Spalte mit dem eindeutigen Spaltennamen **spalte_1** hat, sowie der folgende Code:
**x = df['spalte_1'].iloc[42]**

Markieren Sie **alle** richtigen Aussagen.
1. ❌ Der Datentyp von **x** kann von der der Anzahl Spalten von **df** abhängen.
1. ✅ Die Codeausführung kann mit einem Fehler abbrechen.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *str* haben.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *int* haben.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *float64* haben.
1. ✅ Der Datentyp von **x** kann vom Inhalt der *NICHT-Index-Werte* von **df** abhängen.
1. ✅ Die Auswertung von **x.sum()** kann eine Gleitkommazahl (z.B. 7.2) ergeben.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *pd.DataFrame* haben.
1. ❌ Der Datentyp von **x** kann vom Inhalt der *Zeilen-Label* von **df** abhängen.
1. ✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *pd.Series* haben.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[.iloc[]](/1867045b058343e1a66b677961515907#659a00c8972e48a992e0dcabacb0cd4f), [pandas data types](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
### Code Explanation
```python
x = df['spalte_1'].iloc[42]
```
1. `df['spalte_1']`
- This part of the code selects the column named `'spalte_1'` from the DataFrame `df`.
- The result is a `pd.Series` object containing all the values from the column `'spalte_1'`.
1. `.iloc[42]`
- The `.iloc` method is used for integer-location based indexing.
- `iloc[42]` selects the 43rd element (since indexing starts at 0) from the `pd.Series` obtained in the previous step.
### Answer Explanations
1. ❌ Incorrect, the datatype of `x` depends on the value in the 43rd row of the column `'spalte_1'`, not on the number of columns in `df`.
1. ✅ Correct, if the DataFrame `df` has fewer than 43 rows, trying to access `iloc[42]` will result in an `IndexError`.
1. ✅ **Correct, i**f the value in the 43rd row of the column `'spalte_1'` is a string, then `x` will be of type `str`.
1. ✅ **Correct, **if the value in the 43rd row of the column `'spalte_1'` is an integer, then `x` will be of type `int`.
1. ✅ **Correct, **if the value in the 43rd row of the column `'spalte_1'` is a float, then `x` will be of type `float64`.
1. ✅ **Correct,** the datatype of `x` depends on the value in the 43rd row of the column `'spalte_1'`, which is a non-index value.
1. ✅ **Correct, **if `x` is a numeric type (like `int` or `float`), calling `x.sum()` will return the value itself, which can be a floating-point number.
1. ❌ **Incorrect, **`x` is a single value from a `pd.Series`, so it cannot be a `pd.DataFrame`.
1. ❌ **Incorrect, **the datatype of `x` depends on the value in the 43rd row of the column `'spalte_1'`, not on the row labels.
1. ❌ **Incorrect, **`x` is a single value from a `pd.Series`, so it cannot be a `pd.Series` itself.
</details>
---

