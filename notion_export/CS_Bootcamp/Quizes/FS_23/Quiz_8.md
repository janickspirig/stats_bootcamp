---
title: "Quiz 8"
notion_id: "6da39bd8-ae5b-48f8-9afb-46080f1fe947"
notion_url: "https://www.notion.so/Quiz-8-6da39bd8ae5b48f89afb46080f1fe947"
exported_at: "2025-12-14T01:04:16.720918+00:00"
---

# Quiz 8

# Question 1
Gegeben ist die pd.Series **x** wie folgt:
```python
0 1.0
1 2.0
2 7.0
3 NaN
4 2.0
   ...
72 3.0
73 23.0
74 3.0
75 23.0
76 3.0
Length: 77, dtype: float64
```
Die Auswertung von **x.sum()** ergibt 770.0
Markieren Sie alle Ausdrücke die fehlerfrei ausgeführt werden können UND wahr sind.
✅ Code snippet 1
```python
total=0
counter = 0
for f in x:
	if not np.isnan(f):
		counter =+ 1
		total =+ f
x.mean() == total / counter
```
✅ Code snippet 2
```python
x.mean() == x.sum() / x.count()
```
✅ Code snippet 3
```python
x.mean() == x.iloc[:len(x)].mean()
```
❌ Code snippet 4
```python
x.mean () == x.sum () / len (x)
```
❌ Code snippet 5
```python
x.mean() == x. iloc[1:].mean()
```
✅ Code snippet 6
```python
x.mean() == x.iloc[:].mean()
```

<details>
<summary>Explanation</summary>

> 💡 **[.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5), [.iloc[]](/1867045b058343e1a66b677961515907#659a00c8972e48a992e0dcabacb0cd4f), [.sum()](/1867045b058343e1a66b677961515907#6f1bd7bccbe24ecf8bcb37abc05b0550), [.count()](/1867045b058343e1a66b677961515907#8d4d0ed1fc114482978e4da5f21b429f), [for loop](/5b0832dbf9454eb1941b7632e68a9abb#c7a72e5314c643378df185a01e9ceede), [.isnan()](/ccc5737dc7c64936bced118aca375cf9#2d995d983b82436a8d0af9d54c34d7ed), [len()](/5b0832dbf9454eb1941b7632e68a9abb#e097ab624af04d18b7f69088dff7d5f2)**
For simplicity, let’s assume we are dealing with the following series that is stored in **x**.
```python
0   1.0
1   2.0
2   4.0
3   6.0
4   10.0
Length: 5, dtype: float64
```
✅ **Correct**. Check the line-by-line execution below.
`total = 0`
`counter = 0`
`for f in x:` → `total = 23.0`, `counter = 5`
<details>
<summary>1st run → `total = 1.0`, `counter = 1`</summary>

`f = 1.0`
`if not np.isnan(f):` → `not np.isnan(1.0)` → `not False` → `True`
`counter = counter + 1` → `0 + 1` → `1`
`total = total + 1.0` → `0 + 1.0` → `1.0`
</details>
<details>
<summary>2nd run → `total = 3.0`, `counter = 2`</summary>

`f = 2.0`
`if not np.isnan(f):` → `not np.isnan(2.0)` → `not False` → `True`
`counter = counter + 1` → `1 + 1` → `2`
`total = total + 2.0` → `1.0 + 2.0` → `3.0`
</details>
<details>
<summary>3rd run → `total = 7.0`, `counter = 3`</summary>

`f = 4.0`
`if not np.isnan(f):` → `not np.isnan(4.0)` → `not False` → `True`
`counter = counter + 1` → `2 + 1` → `3`
`total = total + 4.0` → `3.0 + 4.0` → `7.0`
</details>
<details>
<summary>4th run → `total = 13.0`, `counter = 4`</summary>

`f = 6.0`
`if not np.isnan(f):` → `not np.isnan(6.0)` → `not False` → `True`
`counter = counter + 1` → `3 + 1` → `4`
`total = total + 6.0` → `7.0 + 6.0` → `13.0`
</details>
<details>
<summary>5th run → `total = 23.0`, `counter = 5`</summary>

`f = 10.0`
`if not np.isnan(f):` → `not np.isnan(10.0)` → `not False` → `True`
`counter = counter + 1` → `4 + 1` → `5`
`total = total + 10.0` → `13.0 + 10.0` → `23.0`
</details>
`x.mean() == total / counter` → `4.6 == 23.0 / 5` → `4.6 == 4.6` → `True`
✅ **Correct**. 
`x.mean()` returns the mean of the series → **4.6**
`x.sum()` returns the sum of the series → **23**
`x.count()` returns the number of elements in the series → **5**
`4.6 == 23 / 5` → ` 4.6 == 4.6` → **`True`** 
✅ **Correct**.
`x.mean()` returns the mean of the series → **4.6**
`x.iloc[:len(x)]` is equal to `x.iloc[:5]` which returns all elements in the series
`4.6 == x.iloc[:5].mean()` 
→ `4.6 == [1.0, 2.0, 4.0, 6.0, 10.0].mean()`
→ `4.6 == 4.6`
→ **`True`**
✅ **Correct**. (I don’t know why this is marked as incorrect in the solution).
`x.mean()` returns the mean of the series → **4.6**
`x.sum()` returns the sum of the series → **23**
`len(x)` returns the number of elements in the series → **5**
`4.6 == 23 / 5` → ` 4.6 == 4.6` → **`True`** 
❌ **Incorrect**.
`x.mean()` returns the mean of the series → **4.6**
`x.iloc[1:]` selects all elements after the first one in the series (**1.0** is excluded)
`4.6 == x.iloc[1:].mean()`
→ `4.6 == [2.0, 4.0, 6.0, 10.0].mean()`
→ `4.6 == 5.5` 
→ **`False`**
✅ **Correct**.
`x.mean()` returns the mean of the series → **4.6**
`x.iloc[:]` returns all elements in the series
`4.6 == x.iloc[:].mean()`
→ `4.6 == [1.0, 2.0, 4.0, 6.0, 10.0].mean()`
→ `4.6 == 4.6`
→ **`True`**
</details>
---
# Question 2
Gegeben ist eine *pd.Series ***s** deren Werte mit **np.arange(100)** erzeugt wurden und deren zugehörige Indizes im selben Aufruf mit **np.arange(100, 0, -1)** erzeugt wurden.
Was passiert nun, wenn wir folgenden Code ausführen:
**s[100] = 99**
❌ Es wird eine Fehlermeldung erzeugt, da nur die *Indizes* von 0 bis 99 existieren.
✅ Der erste Wert von **s** wird verändert.
❌ Bereits die Erstellung von **s** schlägt fehl, da die Anzahl derIndizes ungleich der Anzahl der Werte ist.
❌ Es wird eine Fehlermeldung erzeugt, da die Indizes nicht mehr eindeutig sind.
❌ Der letze Wert von **s** wird verändert.
Die Series hat nun einen zusätzlichen Wert, d.h. die Länge von **s** wurde um ein Elementerweitert.

<details>
<summary>Explanation</summary>

> 💡 **[.arange()](/ccc5737dc7c64936bced118aca375cf9#82ad4caa17294f6a89ccfeb254bcf289), [value assignment](/5b0832dbf9454eb1941b7632e68a9abb#e5cea5d982c844e28376879cb9c3a696)**
The command `np.arange(100, 0, -1)` creates the following numpy array:
```python
array([100,  99,  98,  97,  96,  95,  94,  93,  92,  91,  90,  89,  88,
        87,  86,  85,  84,  83,  82,  81,  80,  79,  78,  77,  76,  75,
        74,  73,  72,  71,  70,  69,  68,  67,  66,  65,  64,  63,  62,
        61,  60,  59,  58,  57,  56,  55,  54,  53,  52,  51,  50,  49,
        48,  47,  46,  45,  44,  43,  42,  41,  40,  39,  38,  37,  36,
        35,  34,  33,  32,  31,  30,  29,  28,  27,  26,  25,  24,  23,
        22,  21,  20,  19,  18,  17,  16,  15,  14,  13,  12,  11,  10,
         9,   8,   7,   6,   5,   4,   3,   2,   1])
```
We can see that an array in descending order from **100** to **1** is created. This is because we are applying a step size of **-1**. Thus, **100** is the **first** element to be **included** and **0** the **first** element to be **excluded**. 
However, for the index position nothing changes, meaning that the first element (**100**) is at index position **0** and the last one (**1**) at index position **99**.
✅ **Correct**. There is **no** index position 100. Python therefore returns an `IndexError`. I don’t know why this answer is market as incorrect in the solution. 😄
❌ **Incorrect**. An `IndexError` is returned.
❌ **Incorrect**. The `arange()` function takes care of that by creating a new array with the size that is necessary to store all elements between **[100, 1]**.
❌ **Incorrect**. Indizes are always **unique**, meaning that at one specific index position **only one **element can be stored. 
❌ **Incorrect**. An `IndexError` is returned.
❌ **Incorrect**. As we are using value assignment (square brackets `[]`) we are trying to **update an existing element** in the array and not adding a new one.
</details>
---
# Question 3
Gegeben ist folgender *pd.DataFrame* **df**. Die Spalte index ist definiert als der Index von **df**.
| index | value0 | value1 |
| --- | --- | --- |
| 2 | 701 | 411 |
| 21 | 483 | 26 |
| 8 | 897 | 62 |
| 6 | 327 | 8 |
| 29 | 458 | 164 |
| 4 | 34 | 652 |
| 11 | 810 | 961 |
| 14 | 432 | 492 |
| 34 | 422 | 307 |
Welcher Wert wird von folgendem Code zurückgegeben: **df.iloc[6][value1]**
961

<details>
<summary>Explanation</summary>

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#659a00c8972e48a992e0dcabacb0cd4f)**
`df.iloc[6]` returns the row with index position 6 as **Series**. In the DataFrame above, **row 11 **is at index position **6** (remember that the first row has index position **0**).
```python
value0    810
value1    961
Name: 11, dtype: int64
```
By adding `['value1']` we can access the value that is stored under **value1**.
Thus, `df.iloc[6]['value1']` returns **961**.
You can see that in the answer `[value1]` is used without putting the column label into **apostrophes**, thus Python would actually raise a `NameError` as there is **no variable** declared as `value1`. Thus, it is important to give `value1` as **string** into the selector → `'value1'`
</details>
---
# Question 4
In Assignment 8 haben wir aus der Datei movies.csv den pd.DataFrame **DF** geladen. Dieser enthält diverse Informationen über viele Filme. Wir nehmen an, dass er in der Spalte imdb score die Bewertung professioneller Kritiker auf einer Skala von 0 (schlechtester Wert) bis 10 (bester Wert) enthält und in der Spalte movie facebook likes die absolute Anzahl von Likes des Filmpublikums.
Hier wollen wir die Funktionen aus dem Assignment um eine weitere Funktion **top_x_overrated_movies** erweitern. Die Idee ist es herauszufinden, welche Filme von den professionellen Kritikern (im Vergleich zur Bewertung durch das Filmpublikum) besser bewertet (überbewertet, overrated) wurden. Die Funktion soll einige Details zu den Top x (also zum Beispiel den x=5 am meisten) überbewerteten Filmen auflisten. Wir haben diese Funktion wie folgt implementiert:
```python
def top_x_overrated_movies(×=5):
	df = DF.copy()
	
	df = df[df['movie_facebook_likes'] > 0]
	
	df['facebook_audience_score'] = (df['movie_facebook_likes'] / df['movie_facebook_likes'].max(axis=0)) * 10

	df['imdb_fb_ratio'] = df['imdb_score'] / df['facebook_audience_score']

	df = df.sort_values(by="imdb_fb_ratio", ascending=False)
	
	return df.head(x)
```

❌ In Zeile 23 müsste es **tail** (statt *head*) heissen, sonst stimmt die Sortierung nicht.
❌ Es ist nicht klar, mit welchem **DataFrame** wir eigentlich arbeiten, da wir mal df und mal DF nutzen, Python-Variablen aber **case sensitive** sind.
❌ Zeile 14 ist problematisch, da es keine Spalte **imdb_fb_ratio** in df oder DF gibt.
❌ In Zeile 10 sind die Klammern falschgesetzt, denn wir wollen ja die Multiplikation mit 10 in jede Zeile broadcasten.
✅ Dei Aussage ist falsch, denn tatsächlich funktioniert die vervollständigte Funktion wie beschrieben.
❌ Es werden nicht die **Top-x** der überbewerteten Filme zurückgegeben sondern faktisch immer die **Top-5**, da in Zeile 1 *x=5* fixiert wird.
❌ In Zeile 10 müsste es **axis=1**(statt axis=0) heissen, da wir nur eine Spalte selektieren und der *DataFrame* somit zu *pd.Series *wird.

<details>
<summary>Explanation</summary>

> 💡 **[.copy()](/1867045b058343e1a66b677961515907#3ee249c7635744768a6ac56eb7e7f728), [.sort_values()](/1867045b058343e1a66b677961515907#f4a6d6bc54ed4a2e885dd225270c2ccc), [optional parameters](/5b0832dbf9454eb1941b7632e68a9abb#fc201a14463f48b3b6e719c4c0773bbc)**
To understand better what is happening let’s assume the DataFrame **DF** looks as follows:
![Simplified DataFrame DF](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4290dfdb-615f-4850-a456-ff3e1af2658a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5QJQJRH%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDqE0O%2FIavvj5onrHw1WECZU0ZRPveImb893o8kryTkUQIhAKSPCfrdMBIi5MRAnWecPMGsLoFhfpVr9sOvV8TCBeBSKv8DCCoQABoMNjM3NDIzMTgzODA1Igw66hoHPWfSUeR39pMq3AMUNtZqaS7quX00TvwhJTU9j3YckfLe1FGNPCLeXkKmtgoWHUuj4nmHJWbxnMXzyQ%2B1OyFU0BYYgZS70pevCNgN2oN70uXms0CHr37z8Cq4kxXsKcYTjLon9cX0camcNWK7a%2BWdJLX%2FAg8VejkSM%2FudHRVEacebGxSXXwGtTmMs%2FsTEIaWYY625iVANurei8XTFu0aGcnuhR8iJ5w9cjR3k0QBwQzZ3gCKV0sNQyzDx%2BFUR23C8RWvr%2F8278Hsqzynll6bDF3BXRQq9Dt4ogddPNMxKx9yYkAA9%2BdWNrX0gWbw%2FXzPxV6ciz%2Fgzw9VrUSWpFMfExnndaKKfm%2FFYYJVXnh02Dqrf43KvubjT2X4W%2Bb04k%2Fm7GJWu6JU6Dx8Tjok2CbkUerJAg9o4gQUb2Fl7j759RZBISI%2Bas0vaTbSJgaTs0GQtrRAeHv5CQIqc5NTlEmK3MBZwTpbEZgijH5QqcxRfBhLP6LM1wqv%2FZK0Lb1AcTUfYuM4uhe1DwKOhMxWWs0kwbh21ozf0kKkY%2F6DJ1l3RTS8QxEL3kBnVHpCeEtv7ydl0T486FEqUTU%2FI8%2BGI1RDxzKfjbGMStjrLL%2FladKDJc7sPGvlVCGCnBDQR1AYxb3MfeyHuGMVIjjCOl%2FjJBjqkAdkhLiOlsztsEM18QMHG2Iq0B8IzH8cL5f6zMtkWYGU4Fa%2Bo%2Fw6idfhgCh8JcBdQus1XTN%2BaTqS8MRwwW%2Fo4Smmk5NPL82htb1ZEBQiITA8hrajdeIK%2FEkvD6IolusZoDGIL7RLY%2F%2BDzI0tTcE%2BKhtynrTypbw3h7XQAokdeBqod6xa3y8B8PbLRbRelEX8mJCF7LOgxahFG94Jt%2BMdo5GUu4nO9&X-Amz-Signature=1ba39bdc20be536374db820ed981f3b148f0af62c3ed20d776a6a0be5978312e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Let’s call the function `top_x_overrated_movies()` and see what happens line-by-line. Please note that because we are calling the function with no parameter value, the **default value** `x=5` is used.
Inside the function, first a copy of **DF** is created and stored in **df**. so that the original DataFrame **DF** is kept unchanged.
```python
df = DF.copy()
```
![Copied DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4290dfdb-615f-4850-a456-ff3e1af2658a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5QJQJRH%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDqE0O%2FIavvj5onrHw1WECZU0ZRPveImb893o8kryTkUQIhAKSPCfrdMBIi5MRAnWecPMGsLoFhfpVr9sOvV8TCBeBSKv8DCCoQABoMNjM3NDIzMTgzODA1Igw66hoHPWfSUeR39pMq3AMUNtZqaS7quX00TvwhJTU9j3YckfLe1FGNPCLeXkKmtgoWHUuj4nmHJWbxnMXzyQ%2B1OyFU0BYYgZS70pevCNgN2oN70uXms0CHr37z8Cq4kxXsKcYTjLon9cX0camcNWK7a%2BWdJLX%2FAg8VejkSM%2FudHRVEacebGxSXXwGtTmMs%2FsTEIaWYY625iVANurei8XTFu0aGcnuhR8iJ5w9cjR3k0QBwQzZ3gCKV0sNQyzDx%2BFUR23C8RWvr%2F8278Hsqzynll6bDF3BXRQq9Dt4ogddPNMxKx9yYkAA9%2BdWNrX0gWbw%2FXzPxV6ciz%2Fgzw9VrUSWpFMfExnndaKKfm%2FFYYJVXnh02Dqrf43KvubjT2X4W%2Bb04k%2Fm7GJWu6JU6Dx8Tjok2CbkUerJAg9o4gQUb2Fl7j759RZBISI%2Bas0vaTbSJgaTs0GQtrRAeHv5CQIqc5NTlEmK3MBZwTpbEZgijH5QqcxRfBhLP6LM1wqv%2FZK0Lb1AcTUfYuM4uhe1DwKOhMxWWs0kwbh21ozf0kKkY%2F6DJ1l3RTS8QxEL3kBnVHpCeEtv7ydl0T486FEqUTU%2FI8%2BGI1RDxzKfjbGMStjrLL%2FladKDJc7sPGvlVCGCnBDQR1AYxb3MfeyHuGMVIjjCOl%2FjJBjqkAdkhLiOlsztsEM18QMHG2Iq0B8IzH8cL5f6zMtkWYGU4Fa%2Bo%2Fw6idfhgCh8JcBdQus1XTN%2BaTqS8MRwwW%2Fo4Smmk5NPL82htb1ZEBQiITA8hrajdeIK%2FEkvD6IolusZoDGIL7RLY%2F%2BDzI0tTcE%2BKhtynrTypbw3h7XQAokdeBqod6xa3y8B8PbLRbRelEX8mJCF7LOgxahFG94Jt%2BMdo5GUu4nO9&X-Amz-Signature=1ba39bdc20be536374db820ed981f3b148f0af62c3ed20d776a6a0be5978312e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Next, from the DataFrame **df** only the records (movies) are selected that have **more than 0 **facebook likes. Thus, the movies *Pirates of the Caribbean At World’s End*, *Star Wars*, *Spiderman 3*, *Superman returns*, *Quantum of Solace* are removed.
```python
df = df[df['movie_facebook_likes'] > 0]
```
![Updated DataFrame df containing only movies with more than 0 facebook likes](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/57961bc0-b6a5-45f4-a3b6-c3abcde37f6c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5QJQJRH%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDqE0O%2FIavvj5onrHw1WECZU0ZRPveImb893o8kryTkUQIhAKSPCfrdMBIi5MRAnWecPMGsLoFhfpVr9sOvV8TCBeBSKv8DCCoQABoMNjM3NDIzMTgzODA1Igw66hoHPWfSUeR39pMq3AMUNtZqaS7quX00TvwhJTU9j3YckfLe1FGNPCLeXkKmtgoWHUuj4nmHJWbxnMXzyQ%2B1OyFU0BYYgZS70pevCNgN2oN70uXms0CHr37z8Cq4kxXsKcYTjLon9cX0camcNWK7a%2BWdJLX%2FAg8VejkSM%2FudHRVEacebGxSXXwGtTmMs%2FsTEIaWYY625iVANurei8XTFu0aGcnuhR8iJ5w9cjR3k0QBwQzZ3gCKV0sNQyzDx%2BFUR23C8RWvr%2F8278Hsqzynll6bDF3BXRQq9Dt4ogddPNMxKx9yYkAA9%2BdWNrX0gWbw%2FXzPxV6ciz%2Fgzw9VrUSWpFMfExnndaKKfm%2FFYYJVXnh02Dqrf43KvubjT2X4W%2Bb04k%2Fm7GJWu6JU6Dx8Tjok2CbkUerJAg9o4gQUb2Fl7j759RZBISI%2Bas0vaTbSJgaTs0GQtrRAeHv5CQIqc5NTlEmK3MBZwTpbEZgijH5QqcxRfBhLP6LM1wqv%2FZK0Lb1AcTUfYuM4uhe1DwKOhMxWWs0kwbh21ozf0kKkY%2F6DJ1l3RTS8QxEL3kBnVHpCeEtv7ydl0T486FEqUTU%2FI8%2BGI1RDxzKfjbGMStjrLL%2FladKDJc7sPGvlVCGCnBDQR1AYxb3MfeyHuGMVIjjCOl%2FjJBjqkAdkhLiOlsztsEM18QMHG2Iq0B8IzH8cL5f6zMtkWYGU4Fa%2Bo%2Fw6idfhgCh8JcBdQus1XTN%2BaTqS8MRwwW%2Fo4Smmk5NPL82htb1ZEBQiITA8hrajdeIK%2FEkvD6IolusZoDGIL7RLY%2F%2BDzI0tTcE%2BKhtynrTypbw3h7XQAokdeBqod6xa3y8B8PbLRbRelEX8mJCF7LOgxahFG94Jt%2BMdo5GUu4nO9&X-Amz-Signature=11567eb4f34740c5a8f35c6f6ba8945bc784a7b7a8193eb3e8c97e537574f95d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Next, a **new column** is added to the DataFrame which contains the number** 10** for the movie with the most facebook likes. The facebook likes for the other movies are then scaled in ratio to that movie.
`df['movie_facebook_likes'].max(axis=0)`
returns the highest value in column `movie_facebook_likes` 
→ `197000` (Batman v Superman)
`.max(axis=`**`0`**`)` → select highest value in column
`.max(axis=`**`1`**`)` → select highest value in row
```python
df['facebook_audience_score'] = (df['movie_facebook_likes'] / df['movie_facebook_likes'].max(axis=0)) * 10
```
![Updated DataFrame df with new column facebook_audience_score](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2a2d2196-7e79-4ca1-a7f4-de6a0924e86b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5QJQJRH%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDqE0O%2FIavvj5onrHw1WECZU0ZRPveImb893o8kryTkUQIhAKSPCfrdMBIi5MRAnWecPMGsLoFhfpVr9sOvV8TCBeBSKv8DCCoQABoMNjM3NDIzMTgzODA1Igw66hoHPWfSUeR39pMq3AMUNtZqaS7quX00TvwhJTU9j3YckfLe1FGNPCLeXkKmtgoWHUuj4nmHJWbxnMXzyQ%2B1OyFU0BYYgZS70pevCNgN2oN70uXms0CHr37z8Cq4kxXsKcYTjLon9cX0camcNWK7a%2BWdJLX%2FAg8VejkSM%2FudHRVEacebGxSXXwGtTmMs%2FsTEIaWYY625iVANurei8XTFu0aGcnuhR8iJ5w9cjR3k0QBwQzZ3gCKV0sNQyzDx%2BFUR23C8RWvr%2F8278Hsqzynll6bDF3BXRQq9Dt4ogddPNMxKx9yYkAA9%2BdWNrX0gWbw%2FXzPxV6ciz%2Fgzw9VrUSWpFMfExnndaKKfm%2FFYYJVXnh02Dqrf43KvubjT2X4W%2Bb04k%2Fm7GJWu6JU6Dx8Tjok2CbkUerJAg9o4gQUb2Fl7j759RZBISI%2Bas0vaTbSJgaTs0GQtrRAeHv5CQIqc5NTlEmK3MBZwTpbEZgijH5QqcxRfBhLP6LM1wqv%2FZK0Lb1AcTUfYuM4uhe1DwKOhMxWWs0kwbh21ozf0kKkY%2F6DJ1l3RTS8QxEL3kBnVHpCeEtv7ydl0T486FEqUTU%2FI8%2BGI1RDxzKfjbGMStjrLL%2FladKDJc7sPGvlVCGCnBDQR1AYxb3MfeyHuGMVIjjCOl%2FjJBjqkAdkhLiOlsztsEM18QMHG2Iq0B8IzH8cL5f6zMtkWYGU4Fa%2Bo%2Fw6idfhgCh8JcBdQus1XTN%2BaTqS8MRwwW%2Fo4Smmk5NPL82htb1ZEBQiITA8hrajdeIK%2FEkvD6IolusZoDGIL7RLY%2F%2BDzI0tTcE%2BKhtynrTypbw3h7XQAokdeBqod6xa3y8B8PbLRbRelEX8mJCF7LOgxahFG94Jt%2BMdo5GUu4nO9&X-Amz-Signature=ddbda1d7ce2ae1ef81affc3f7e68082413c7370a395cd48d8afcb81cc71168a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Next, another column is added to the DataFrame which stores the **ratio** between the imbd score and the facebook score. The **higher** the value in **imdb_fb_ratio** is, the **more** imdb and the facebook audience disagree.
```python
df['imdb_fb_ratio'] = df['imdb_score'] / df['facebook_audience_score']
```
![Updated DataFrame df with new column imdb_fb_ratio](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3486a0e8-d8aa-44b2-b767-c3fb85bb80dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5QJQJRH%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDqE0O%2FIavvj5onrHw1WECZU0ZRPveImb893o8kryTkUQIhAKSPCfrdMBIi5MRAnWecPMGsLoFhfpVr9sOvV8TCBeBSKv8DCCoQABoMNjM3NDIzMTgzODA1Igw66hoHPWfSUeR39pMq3AMUNtZqaS7quX00TvwhJTU9j3YckfLe1FGNPCLeXkKmtgoWHUuj4nmHJWbxnMXzyQ%2B1OyFU0BYYgZS70pevCNgN2oN70uXms0CHr37z8Cq4kxXsKcYTjLon9cX0camcNWK7a%2BWdJLX%2FAg8VejkSM%2FudHRVEacebGxSXXwGtTmMs%2FsTEIaWYY625iVANurei8XTFu0aGcnuhR8iJ5w9cjR3k0QBwQzZ3gCKV0sNQyzDx%2BFUR23C8RWvr%2F8278Hsqzynll6bDF3BXRQq9Dt4ogddPNMxKx9yYkAA9%2BdWNrX0gWbw%2FXzPxV6ciz%2Fgzw9VrUSWpFMfExnndaKKfm%2FFYYJVXnh02Dqrf43KvubjT2X4W%2Bb04k%2Fm7GJWu6JU6Dx8Tjok2CbkUerJAg9o4gQUb2Fl7j759RZBISI%2Bas0vaTbSJgaTs0GQtrRAeHv5CQIqc5NTlEmK3MBZwTpbEZgijH5QqcxRfBhLP6LM1wqv%2FZK0Lb1AcTUfYuM4uhe1DwKOhMxWWs0kwbh21ozf0kKkY%2F6DJ1l3RTS8QxEL3kBnVHpCeEtv7ydl0T486FEqUTU%2FI8%2BGI1RDxzKfjbGMStjrLL%2FladKDJc7sPGvlVCGCnBDQR1AYxb3MfeyHuGMVIjjCOl%2FjJBjqkAdkhLiOlsztsEM18QMHG2Iq0B8IzH8cL5f6zMtkWYGU4Fa%2Bo%2Fw6idfhgCh8JcBdQus1XTN%2BaTqS8MRwwW%2Fo4Smmk5NPL82htb1ZEBQiITA8hrajdeIK%2FEkvD6IolusZoDGIL7RLY%2F%2BDzI0tTcE%2BKhtynrTypbw3h7XQAokdeBqod6xa3y8B8PbLRbRelEX8mJCF7LOgxahFG94Jt%2BMdo5GUu4nO9&X-Amz-Signature=80ce366ecf9900875df9f2190a895ca258d33dd2745d7340ab1a86e56c94f060&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
To identify the **top x (5)** movies for which the facebook audience and imdb **disagree**, the values must be sorted in **descending** order:
```python
df = df.sort_values(by="imdb_fb_ratio", ascending=False)
```
![Sorted DataFrame df in descending order based on column imdb_fb_ratio](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c9b50c6c-c2f1-49a7-b632-df0fb399c1ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5QJQJRH%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDqE0O%2FIavvj5onrHw1WECZU0ZRPveImb893o8kryTkUQIhAKSPCfrdMBIi5MRAnWecPMGsLoFhfpVr9sOvV8TCBeBSKv8DCCoQABoMNjM3NDIzMTgzODA1Igw66hoHPWfSUeR39pMq3AMUNtZqaS7quX00TvwhJTU9j3YckfLe1FGNPCLeXkKmtgoWHUuj4nmHJWbxnMXzyQ%2B1OyFU0BYYgZS70pevCNgN2oN70uXms0CHr37z8Cq4kxXsKcYTjLon9cX0camcNWK7a%2BWdJLX%2FAg8VejkSM%2FudHRVEacebGxSXXwGtTmMs%2FsTEIaWYY625iVANurei8XTFu0aGcnuhR8iJ5w9cjR3k0QBwQzZ3gCKV0sNQyzDx%2BFUR23C8RWvr%2F8278Hsqzynll6bDF3BXRQq9Dt4ogddPNMxKx9yYkAA9%2BdWNrX0gWbw%2FXzPxV6ciz%2Fgzw9VrUSWpFMfExnndaKKfm%2FFYYJVXnh02Dqrf43KvubjT2X4W%2Bb04k%2Fm7GJWu6JU6Dx8Tjok2CbkUerJAg9o4gQUb2Fl7j759RZBISI%2Bas0vaTbSJgaTs0GQtrRAeHv5CQIqc5NTlEmK3MBZwTpbEZgijH5QqcxRfBhLP6LM1wqv%2FZK0Lb1AcTUfYuM4uhe1DwKOhMxWWs0kwbh21ozf0kKkY%2F6DJ1l3RTS8QxEL3kBnVHpCeEtv7ydl0T486FEqUTU%2FI8%2BGI1RDxzKfjbGMStjrLL%2FladKDJc7sPGvlVCGCnBDQR1AYxb3MfeyHuGMVIjjCOl%2FjJBjqkAdkhLiOlsztsEM18QMHG2Iq0B8IzH8cL5f6zMtkWYGU4Fa%2Bo%2Fw6idfhgCh8JcBdQus1XTN%2BaTqS8MRwwW%2Fo4Smmk5NPL82htb1ZEBQiITA8hrajdeIK%2FEkvD6IolusZoDGIL7RLY%2F%2BDzI0tTcE%2BKhtynrTypbw3h7XQAokdeBqod6xa3y8B8PbLRbRelEX8mJCF7LOgxahFG94Jt%2BMdo5GUu4nO9&X-Amz-Signature=4df446ddc77a1cf4823ecf653cae9636115160759739c9f55701e726878afe2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Finally, to return the **top x (5) overrated movies** the** first x (5) rows** in the sorted DataFrame must be selected and then returned to the function caller.
```python
return df.head(5)
```
![Final DataFrame containing the top 5 overrated movies is returned to the function caller](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6bbdbd4b-844c-4521-90b8-51f0369547a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5QJQJRH%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDqE0O%2FIavvj5onrHw1WECZU0ZRPveImb893o8kryTkUQIhAKSPCfrdMBIi5MRAnWecPMGsLoFhfpVr9sOvV8TCBeBSKv8DCCoQABoMNjM3NDIzMTgzODA1Igw66hoHPWfSUeR39pMq3AMUNtZqaS7quX00TvwhJTU9j3YckfLe1FGNPCLeXkKmtgoWHUuj4nmHJWbxnMXzyQ%2B1OyFU0BYYgZS70pevCNgN2oN70uXms0CHr37z8Cq4kxXsKcYTjLon9cX0camcNWK7a%2BWdJLX%2FAg8VejkSM%2FudHRVEacebGxSXXwGtTmMs%2FsTEIaWYY625iVANurei8XTFu0aGcnuhR8iJ5w9cjR3k0QBwQzZ3gCKV0sNQyzDx%2BFUR23C8RWvr%2F8278Hsqzynll6bDF3BXRQq9Dt4ogddPNMxKx9yYkAA9%2BdWNrX0gWbw%2FXzPxV6ciz%2Fgzw9VrUSWpFMfExnndaKKfm%2FFYYJVXnh02Dqrf43KvubjT2X4W%2Bb04k%2Fm7GJWu6JU6Dx8Tjok2CbkUerJAg9o4gQUb2Fl7j759RZBISI%2Bas0vaTbSJgaTs0GQtrRAeHv5CQIqc5NTlEmK3MBZwTpbEZgijH5QqcxRfBhLP6LM1wqv%2FZK0Lb1AcTUfYuM4uhe1DwKOhMxWWs0kwbh21ozf0kKkY%2F6DJ1l3RTS8QxEL3kBnVHpCeEtv7ydl0T486FEqUTU%2FI8%2BGI1RDxzKfjbGMStjrLL%2FladKDJc7sPGvlVCGCnBDQR1AYxb3MfeyHuGMVIjjCOl%2FjJBjqkAdkhLiOlsztsEM18QMHG2Iq0B8IzH8cL5f6zMtkWYGU4Fa%2Bo%2Fw6idfhgCh8JcBdQus1XTN%2BaTqS8MRwwW%2Fo4Smmk5NPL82htb1ZEBQiITA8hrajdeIK%2FEkvD6IolusZoDGIL7RLY%2F%2BDzI0tTcE%2BKhtynrTypbw3h7XQAokdeBqod6xa3y8B8PbLRbRelEX8mJCF7LOgxahFG94Jt%2BMdo5GUu4nO9&X-Amz-Signature=2a914309dd18802578d71ed991e7828275ab5cb9649f3e5734e268622e7251c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we can see the code works as intended.
</details>
---
# Question 5
Gegeben ist ein *pd.DataFrame* **df**, sowie der folgende Code:
**x = df.loc[42]**
Markieren Sie alle richtigen Aussagen.
✅ Die Variable **x **kann nach der Ausführung des Codes den Datentyp *pd.Series* haben.
❌ Der Datentyp von **x** kann von der Anzahl Spalten von **df** abhängen.
✅ Die Codeausführung kann mit einem Fehler abbrechen.
❌ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *int* haben.
❌ DieVariable **x** kann nach der Ausführung des Codes den Datentyp *string* haben.
❌ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *float64* haben.
✅ Die Variable **x** kann nach der Ausführung des Codes den Datentyp *pd.DataFrame* haben.
❌ Der Datentyp von **x** kann vom Inhalt der *NICHT-Index*-Werte von **df** abhängen.
✅ Der Datentyp von **x** kann vom Inhalt der *Index*-Werte (*label*) von **df** abhängen.
✅ Die Auswertung von **x.sum() **kann eine Gleitkommazahl (z.B. 6.2) ergeben.

<details>
<summary>Explanation</summary>

> 💡 **[.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.sum()](/1867045b058343e1a66b677961515907#6f1bd7bccbe24ecf8bcb37abc05b0550)**
✅ **Correct**. If there is only **one row** with index label 42, `df.loc[42]` will return a Series.
For example, if we have the following DataFrame: 
![Example DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2142b4f1-fcb5-4540-b3c8-76840cdbf1a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ARJ3TCP%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDmy2t2grgaWGVwUqUPoOlmOOL5XAkElL3WmobIGuCSsgIhAJCELnqttXImWggTE3dkWroSgieD%2FrIh38ROUsyguh%2FXKv8DCCoQABoMNjM3NDIzMTgzODA1Igw%2BIARUolCFwyn9TFUq3AMuT2gv9ekUSV8eNWZnMB53DvOmXqf8SQ%2FrQYsysCYWBmrRf2klTbZEE1Gfg%2FyUtkpZ8uVrbpiPGqkdxtemp6F7uspjm5pCiMKnGXRJ8KGFG2wjGId7DV897%2FYLDyUGSDQfJyCDbPX0Vw%2BBLhLK%2BFLIveL6dI1008tG3%2BS9WlLvge%2Ft%2BxATKSxd24uVgta9OCKI6lDQ%2B2Gm4wKB2ydpMHkL5iMewwhQBj5M57iLD9fBmpyjABQawynjy63y3Nwxhtg4sQYdmn9UuTBv%2BdVPAqTo0eQSsMEixFhQlKsXGLLDypdNmO4EcH7s7%2Bb6pVj3JbtkuVwQ%2FUt920yn7zQLfHuMiXTWePyks6dCiA1NYgYD8UvKgGwLUmAOy6X0iThkoDtb5zVsBrmSGpJ4QXUf6r6vsp75zYvFmpIaSKuyVe9IbL%2BpAzZWrinRAJ7FHIeWFoR9KfS553K2boYAGHtNml%2F9rLaYdUhGqJUvmgQjBnuVHfMHwhZLOpEAotqlnZSEv4V3CfJ15EoRfVm4zVH3YvMXZ%2FfY9x2dC4SKwB%2FhewyqyF9ciEQcX4zxjrQle5ix1iGbP8NCug0wsPdnne18g2NTbVZ7kSW9jDaIaYhrmtmikB6rHQbbduNYvY83LTCJlvjJBjqkAX%2BJ%2FE9DAefz%2F2gI12mPEqEsnvWFMSstLGzIXKbamnCClOXw0x1pj%2Bxu%2By9w2M1WpauODL5fDYVPvSQXOG%2FRP7aJN1to5qD3QzF%2Bs1ACqqyq644wb4%2BE1GBIQNULxGe82f3zFT049sLM7K8VEpekpGmbA8tEgQx%2BHuZjT2zPQ06s%2BL7%2B%2FPe5VQBIU%2Bhtqk64x7YX5AzGSRcUhz10UJDHx4YD4PF3&X-Amz-Signature=c736f8164dc5588fd6b177f7f901febf37eb54436b326c5fbc8510e356dbe32f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we do `df.loc[42]`, then the result will be a **Series** as only the first row has the index label **42**.
```python
value1    5
value2    6
Name: 42, dtype: int64
```
❌ **Incorrect**. Does not depend on the number of columns there are. `.loc[]` is a row-wise selector, meaning it selects data from a DataFrame by the **index labels** and not by the column labels.
❌ **Incorrect**. `.loc[]` will always return a Series or a DataFrame.
❌ **Incorrect**. `.loc[]` will always return a Series or a DataFrame.
❌ **Incorrect**. `.loc[]` will always return a Series or a DataFrame.
✅ **Correct**. If there are multiple rows with index label **42**, `df.loc[42]` will return a DataFrame.
For example, if we have the following DataFrame: 
![Example DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/58bb62ce-4582-4538-81dd-f048a0eb0441/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ARJ3TCP%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDmy2t2grgaWGVwUqUPoOlmOOL5XAkElL3WmobIGuCSsgIhAJCELnqttXImWggTE3dkWroSgieD%2FrIh38ROUsyguh%2FXKv8DCCoQABoMNjM3NDIzMTgzODA1Igw%2BIARUolCFwyn9TFUq3AMuT2gv9ekUSV8eNWZnMB53DvOmXqf8SQ%2FrQYsysCYWBmrRf2klTbZEE1Gfg%2FyUtkpZ8uVrbpiPGqkdxtemp6F7uspjm5pCiMKnGXRJ8KGFG2wjGId7DV897%2FYLDyUGSDQfJyCDbPX0Vw%2BBLhLK%2BFLIveL6dI1008tG3%2BS9WlLvge%2Ft%2BxATKSxd24uVgta9OCKI6lDQ%2B2Gm4wKB2ydpMHkL5iMewwhQBj5M57iLD9fBmpyjABQawynjy63y3Nwxhtg4sQYdmn9UuTBv%2BdVPAqTo0eQSsMEixFhQlKsXGLLDypdNmO4EcH7s7%2Bb6pVj3JbtkuVwQ%2FUt920yn7zQLfHuMiXTWePyks6dCiA1NYgYD8UvKgGwLUmAOy6X0iThkoDtb5zVsBrmSGpJ4QXUf6r6vsp75zYvFmpIaSKuyVe9IbL%2BpAzZWrinRAJ7FHIeWFoR9KfS553K2boYAGHtNml%2F9rLaYdUhGqJUvmgQjBnuVHfMHwhZLOpEAotqlnZSEv4V3CfJ15EoRfVm4zVH3YvMXZ%2FfY9x2dC4SKwB%2FhewyqyF9ciEQcX4zxjrQle5ix1iGbP8NCug0wsPdnne18g2NTbVZ7kSW9jDaIaYhrmtmikB6rHQbbduNYvY83LTCJlvjJBjqkAX%2BJ%2FE9DAefz%2F2gI12mPEqEsnvWFMSstLGzIXKbamnCClOXw0x1pj%2Bxu%2By9w2M1WpauODL5fDYVPvSQXOG%2FRP7aJN1to5qD3QzF%2Bs1ACqqyq644wb4%2BE1GBIQNULxGe82f3zFT049sLM7K8VEpekpGmbA8tEgQx%2BHuZjT2zPQ06s%2BL7%2B%2FPe5VQBIU%2Bhtqk64x7YX5AzGSRcUhz10UJDHx4YD4PF3&X-Amz-Signature=f3ea671c3666774dd69352ee068a79bdab725e75fd125368d299179d2437617c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And we do `df.loc[42]`, then the result will be a **DataFrame** as the first and the third row have the index label **42**.
![Output of `df.loc[42]`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/79b591db-0f3b-41d2-ab52-6b47f480b5ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ARJ3TCP%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDmy2t2grgaWGVwUqUPoOlmOOL5XAkElL3WmobIGuCSsgIhAJCELnqttXImWggTE3dkWroSgieD%2FrIh38ROUsyguh%2FXKv8DCCoQABoMNjM3NDIzMTgzODA1Igw%2BIARUolCFwyn9TFUq3AMuT2gv9ekUSV8eNWZnMB53DvOmXqf8SQ%2FrQYsysCYWBmrRf2klTbZEE1Gfg%2FyUtkpZ8uVrbpiPGqkdxtemp6F7uspjm5pCiMKnGXRJ8KGFG2wjGId7DV897%2FYLDyUGSDQfJyCDbPX0Vw%2BBLhLK%2BFLIveL6dI1008tG3%2BS9WlLvge%2Ft%2BxATKSxd24uVgta9OCKI6lDQ%2B2Gm4wKB2ydpMHkL5iMewwhQBj5M57iLD9fBmpyjABQawynjy63y3Nwxhtg4sQYdmn9UuTBv%2BdVPAqTo0eQSsMEixFhQlKsXGLLDypdNmO4EcH7s7%2Bb6pVj3JbtkuVwQ%2FUt920yn7zQLfHuMiXTWePyks6dCiA1NYgYD8UvKgGwLUmAOy6X0iThkoDtb5zVsBrmSGpJ4QXUf6r6vsp75zYvFmpIaSKuyVe9IbL%2BpAzZWrinRAJ7FHIeWFoR9KfS553K2boYAGHtNml%2F9rLaYdUhGqJUvmgQjBnuVHfMHwhZLOpEAotqlnZSEv4V3CfJ15EoRfVm4zVH3YvMXZ%2FfY9x2dC4SKwB%2FhewyqyF9ciEQcX4zxjrQle5ix1iGbP8NCug0wsPdnne18g2NTbVZ7kSW9jDaIaYhrmtmikB6rHQbbduNYvY83LTCJlvjJBjqkAX%2BJ%2FE9DAefz%2F2gI12mPEqEsnvWFMSstLGzIXKbamnCClOXw0x1pj%2Bxu%2By9w2M1WpauODL5fDYVPvSQXOG%2FRP7aJN1to5qD3QzF%2Bs1ACqqyq644wb4%2BE1GBIQNULxGe82f3zFT049sLM7K8VEpekpGmbA8tEgQx%2BHuZjT2zPQ06s%2BL7%2B%2FPe5VQBIU%2Bhtqk64x7YX5AzGSRcUhz10UJDHx4YD4PF3&X-Amz-Signature=5c9d545751e37cbc9b0379c035b072145555bde623fe4901ae9fe414563e5c3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. As `.loc[]` is a row-wise selector, meaning it selects data from a DataFrame by the **index labels**, its output always depends on the values in the index column.
✅ **Correct.** As seen in [statement 1](/6da39bd8ae5b48f89afb46080f1fe947) and [statement 6](/6da39bd8ae5b48f89afb46080f1fe947), based on **how many times** the number **42** appears in the index column the data type of the return value **can vary**.
✅ **Correct**. `x.sum()` sums up the values in each column for the row with the index label **42**, i.e., that were selected by `df.loc[42]`. If the values in the DataFrame are **floats**, then the result of `x.sum()` will be a **float** value as well.
For example, let’s assume we have the following DataFrame:
![Example DataFrame df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a6a5c483-92c9-40c1-bd03-ac7db58b2b10/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ARJ3TCP%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDmy2t2grgaWGVwUqUPoOlmOOL5XAkElL3WmobIGuCSsgIhAJCELnqttXImWggTE3dkWroSgieD%2FrIh38ROUsyguh%2FXKv8DCCoQABoMNjM3NDIzMTgzODA1Igw%2BIARUolCFwyn9TFUq3AMuT2gv9ekUSV8eNWZnMB53DvOmXqf8SQ%2FrQYsysCYWBmrRf2klTbZEE1Gfg%2FyUtkpZ8uVrbpiPGqkdxtemp6F7uspjm5pCiMKnGXRJ8KGFG2wjGId7DV897%2FYLDyUGSDQfJyCDbPX0Vw%2BBLhLK%2BFLIveL6dI1008tG3%2BS9WlLvge%2Ft%2BxATKSxd24uVgta9OCKI6lDQ%2B2Gm4wKB2ydpMHkL5iMewwhQBj5M57iLD9fBmpyjABQawynjy63y3Nwxhtg4sQYdmn9UuTBv%2BdVPAqTo0eQSsMEixFhQlKsXGLLDypdNmO4EcH7s7%2Bb6pVj3JbtkuVwQ%2FUt920yn7zQLfHuMiXTWePyks6dCiA1NYgYD8UvKgGwLUmAOy6X0iThkoDtb5zVsBrmSGpJ4QXUf6r6vsp75zYvFmpIaSKuyVe9IbL%2BpAzZWrinRAJ7FHIeWFoR9KfS553K2boYAGHtNml%2F9rLaYdUhGqJUvmgQjBnuVHfMHwhZLOpEAotqlnZSEv4V3CfJ15EoRfVm4zVH3YvMXZ%2FfY9x2dC4SKwB%2FhewyqyF9ciEQcX4zxjrQle5ix1iGbP8NCug0wsPdnne18g2NTbVZ7kSW9jDaIaYhrmtmikB6rHQbbduNYvY83LTCJlvjJBjqkAX%2BJ%2FE9DAefz%2F2gI12mPEqEsnvWFMSstLGzIXKbamnCClOXw0x1pj%2Bxu%2By9w2M1WpauODL5fDYVPvSQXOG%2FRP7aJN1to5qD3QzF%2Bs1ACqqyq644wb4%2BE1GBIQNULxGe82f3zFT049sLM7K8VEpekpGmbA8tEgQx%2BHuZjT2zPQ06s%2BL7%2B%2FPe5VQBIU%2Bhtqk64x7YX5AzGSRcUhz10UJDHx4YD4PF3&X-Amz-Signature=cd0e1d6cb8f7d8a86b95c61fc5b081654a4900ad2000188c5eebad2a380a1acb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we execute `x = df.loc[42]`:
```python
value1    5.2
value2    6.7
Name: 42, dtype: float64
```
Finally, we sum up the values by executing `x.sum()`:
**11.9**
We can see that the result is 11.9 → a float
</details>
---

