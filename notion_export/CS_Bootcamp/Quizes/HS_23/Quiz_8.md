---
title: "Quiz 8"
notion_id: "f16ceda6-d964-4f36-a2f9-07243ba61929"
notion_url: "https://www.notion.so/Quiz-8-f16ceda6d9644f36a2f907243ba61929"
exported_at: "2025-12-13T23:22:08.091957+00:00"
---

# Quiz 8

## Question 1
Given is the pd.Series x:
```python
0     1.0
1     2.0
2     7.0
3     NaN
4     2.0
...
72    3.0
73    23.0
74    3.0
75    23.0
76    3.0
Length: 77, dtype: float64
```
The evaluation of **x.sum()** returns *770.0*
Please mark **all** statements that can be executed without raising an error **AND** that are True.
❌ x.mean() == x.iloc[1:].mean()
✅ x.mean() == x.sum() / x.count()
✅  Code snippet
```python
total = 0
counter = 0
for f in x:
		if not np.isnan(f):
				counter += 1
				total += f
x.mean() == total / counter
```
✅ x.mean() == x.iloc[:len(x)].mean()
✅ x.mean() == x.iloc[:].mean()
❌ x.mean() == x.sum() / len(x)

<details>
<summary>Explanation</summary>

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.isnan()](/ccc5737dc7c64936bced118aca375cf9#2d995d983b82436a8d0af9d54c34d7ed), [.mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
❌ **Incorrect**, because `x.iloc[1:]` means the series starting from index 1 (value **2.0**), i.e., excluding the first element (value **1.0**). The mean of this series will be different from the mean of the whole series.
✅ **Correct**, because the mean is calculated as the sum of all elements divided by the number of all non-NaN elements in the series (`x.count()`).
✅ **Correct**, because this loop calculates the sum of all non-NaN elements and divides it by the number of non-NaN elements, which is again the definition of mean.
✅ **Correct**, because `x.iloc[:len(x)]` is `x.iloc[:77]` which includes all elements up to index position 76 (including), which representes the entire series.
✅ **Correct**, because `x.iloc[:]` also represents the entire series.
❌ **Incorrect**, because `len(x)` gives the total length of the series including NaN values (e.g., index position 3), but the mean is calculated as the sum of all elements divided by the number of non-NaN elements.
</details>
---
## Question 2
We have the following pd.DataFrame df. The column index is defined as the index of df.
| index | value1 | value2 |
| --- | --- | --- |
| 0 | 1 | z |
| 21 | b | y |
| 11 | c | x |
| 24 | d | w |
| 29 | e | v |
| 6 | f | u |
| 9 | g | t |
| 15 | h | s |
| 33 | i | r |
Which **index** does the command return: **df.iloc[6]**
**9**

<details>
<summary>Explanation</summary>

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d)**
The `iloc` function in Pandas is used to select rows by their integer location. It's a zero-based indexing method, meaning that the first row is at position 0, the second row is at position 1, and so on.
In this case, `df.iloc[6]` is asking for the 7th row in the Dataframe (remember, it starts from 0), regardless of the actual index label of that row.
So, the command `df.iloc[6]` will return the row with index **9** as it is the 7th row in the DataFrame.
Here's a breakdown of the DataFrame rows and their integer locations:
- postion 0, 1st row: index = 0, value1 = 'a', value2 = 'z'
- position 1, 2nd row: index = 21, value1 = 'b', value2 = 'y'
- position 2, 3th row: index = 11, value1 = 'c', value2 = 'x'
- position 3, 4th row: index = 24, value1 = 'd', value2 = 'w'
- position 4, 5th row: index = 29, value1 = 'e', value2 = 'v'
- position 5, 6th row: index = 6, value1 = 'f', value2 = 'u'
- **position 6, 7th row: index = 9, value1 = 'g', value2 = 't'** <- Row returned by `df.iloc[6]`
- position 7, 8th row: index = 15, value1 = 'h', value2 = 's'
- position 8, 9th row: index = 33, value1 = 'i', value2 = 'r'
</details>
---
## Question 3
Given is the DataFrame DF from Assignment 8.
Which of the following code snippets returns a ***list*** of genres for the movie at the given integer position ***position***?
Remember that the genres for a movie are saved in the column ***genres***, and are in a format like in the following example: "Action|Adventure|Fantasy".
✅ Code snippet 1
```python
def get_genres(position):
    genres = DF.iloc[position]['genres']
    if pd.isna(genres):
        return []
    else:
        return genres.split("|")
```
❌ Code snippet 2
```python
def get_genres(position):
    genres = DF.genres[position]
    if pd.isna(genres):
        return []
    else:
        return genres.split(" | ")
```
❌ Code snippet 3
```python
def get_genres(position):
    genres = DF[position]['genres']
    if pd.isna(genres):
        return []
    else:
        return genres.split("|")
```
❌ Code snippet 4
```python
def get_genres(position):
    genres = DF.iloc[position]['genres']
    if pd.isna(genres):
        return []
    else:
        return genres
```

<details>
<summary>Explanation</summary>

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.isna()](/1867045b058343e1a66b677961515907#228f2dfad24349f9a7156edde17dc6b3)**
✅ **Correct.** This function uses the `iloc` function to access the row at the given `position` and then fetches the `genres` column. If the genre is not available (NaN), it returns an empty list. Otherwise, it splits the genres string on the **"|"** character and returns the list of genres.
❌ **Incorrect.** This function correctly fetches the `genres` for the given `position` and checks for NaN. However, it tries to split the genres string on **" | "** (note the spaces) instead of **"|"**. This will not correctly split the genres.
❌ **Incorrect.** This function tries to fetch the `genres` by using `position` directly on the DataFrame, which is not correct. It should use either `iloc` or `loc` to access rows by position or index respectively.
❌ Incorrect**.** This function is almost identical to the first one and correctly fetches the `genres`, checks for NaN, but does not split the strings and thus returns the string as-is (e.g. "Action|Adventure|Fantasy") instead of splitting it (e.g. ["Action", "Adventure", "Fantasy"])
> 🤯 **Still unclear? Check also the [explanation here](/b0908e82d8704e3b802a93e78912a002#16b59bc9e99c4a82b529e743aa0725cf).**
</details>
---
## Question 4
Given is a pd.DataFrame df with a fixed and default index, several rows and the four columns a, b, c, and d in that exact order.
Which of the following statements will always return a pd.Series that contains the full column a of df? (There could me more than one.)
`df.T.loc['a']`
`df.iloc['a']`
`df.T.iloc[0]`
`df.loc[:, 'a']`
`df.loc['a']`
`df.iloc[:, ['a']]`
`df['a']`

<details>
<summary>Explanation</summary>

> 💡 **[.T](/1867045b058343e1a66b677961515907#b65f0a7a58214e66ba42846c09b6dbdd),[ .loc[]](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7), [.iloc[]](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7)**
✅  **Correct**, because `df.T` transposes the DataFrame, swapping rows and columns. `loc['a']` then selects the 'a' row, which was previously the 'a' column in the original DataFrame.
❌  **Incorrect**, because `iloc` is used for indexing by integer location, not by labels. Therefore, it cannot accept a string argument like 'a'.
✅  **Correct**, because `df.T` transposes the DataFrame, making the first row to be 'a'. `iloc[0]` then selects this first row, which was previously the 'a' column in the original DataFrame.
✅  **Correct**, because `loc` is used for indexing by labels. The colon `:` selects all rows, and 'a' selects the 'a' column.
❌  **Incorrect**, because `loc` is used for indexing by labels, but 'a' is not a row label, it's a column label. This would throw a KeyError if 'a' is not an index in the DataFrame.
❌  **Incorrect**, because `iloc` is used for indexing by integer location, not by labels. Therefore, it cannot accept a string argument like 'a'.
✅  **Correct**, because this is a common way to select a single column from a DataFrame. It returns the 'a' column as a pd.Series.
> 🤯 **Still unclear? Check the [notebook here](https://colab.research.google.com/drive/1jksSqoNvzO-X_2E7ExeRbWjKqufELMNT?usp=sharing).**
</details>
---
## Question 5
Given is the following code snippet from Assignment 8.
The function should compute the ratio of gross/budget for each movie and return a DataFrame with that information. Why is it not working as intended (there may be several reasons)?
Remember that the resulting DataFrame must fulfill all of the following criteria:
- The columns must only be "director_name", "movie_title", "gross", "budget", and finally "gross/budget" (and the index column)
- The value in the column "gross/budget" must be the result of the row-wise division of the column "gross" and "budget".
- There must not be any NaN (empty) values in the resulting dataframe.
- The dataframe must be sorted in descending order by the newly created "gross/budget" column. Do not reset the index.
- The original dataframe (DF) must not be modified.
```python
def gross_per_budget():
	df = DF.copy()
	df = df[['director_name', 'movie_title', 'gross', 'budget', 'duration']]
	df['gross/budget'] = df['gross'] / df['budget']
	df = df.sort_values(by='movie_title', ascending=False)
	return df
```

✅ In line 5, the dataframe needs to be sorted by the column "gross/budget":
```python
df = df.sort_values(by='gross/budget', ascending=False)
```
❌ There is nothing wrong with this code. It works perfectly.
❌ After line 3, empty values (NaN) need to be removed like this:
```python
df = df.dropna(axis="columns")
```
✅ The resulting DataFrame also contains the column 'duration' which is not included in the above mentioned criteria and therefore should be removed in line 3.
❌ The original dataframe F is modified in the current code. Line 2 needs to be changed to
```python
df = DF
```
✅ After line 3, empty values (NaN) need to be removed like this:
```python
df = df.dropna(axis=0)
```

<details>
<summary>Explanation</summary>

✅ **Correct**, the DataFrame should be sorted by the column "gross/budget", not "movie_title". This is because the criteria specifies that the DataFrame must be sorted in descending order by "gross/budget".
❌ **Incorrect**, because there are several issues with the code. For example, it doesn't sort the DataFrame by the correct column, it doesn't remove NaN values, and it includes an unnecessary "duration" column.
❌ **Incorrect**, the `dropna(axis="columns")` function would remove any column that contains at least one NaN value. This is not what we want, because it could remove columns that are required in the result. Instead, we want to remove rows with NaN values, which can be done using `dropna(axis=0)`.
✅ **Correct**, the "duration" column is not required in the final DataFrame, so it should be removed.
❌ **Incorrect**, the original DataFrame (DF) is not modified in the current code. The `copy()` function is used to create a copy of DF, which is then modified. This leaves the original DataFrame unchanged.
✅ **Correct**, the `dropna(axis=0)` function will remove any row that contains at least one NaN value, which is what we want. This will ensure that there are no NaN values in the resulting DataFrame.
</details>
---
## Question 6
Given is a *pd.DataFrame* as **df**.
Which datatype(s) can end up in variable **x** after the following statement:
**x = df.iloc[42]**
Assume, that the queried entry exists, meaning that **x** is not empty.
✅ **x** will have exclusively the datatype *pd.Series*.
❌ None of the other options.
❌ **x** will have exclusively the datatype *pd.DataFrame*.
❌ **x** can be of datatype pd.Series and *pd.DataFrame*.

<details>
<summary>Explanation</summary>

> 💡 **[.iloc[]](/1867045b058343e1a66b677961515907#8f4b38311f9a416cb5d610212ac2d3e7), [pandas datatypes](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
The `iloc` function is used in pandas to select rows by their position. If you select a single row using `df.iloc[42]`, the result is a **pd.Series** object, which contains the data of the row. So, `x` will have exclusively the datatype `pd.Series`.
Here is an example:
```python
import pandas as pd

# Create a simple dataframe
df = pd.DataFrame({
   'A': ['foo', 'bar', 'baz'],
   'B': ['qux', 'quux', 'quuz'],
   'C': ['corge', 'grault', 'garply']
})

x = df.iloc[1]
print(type(x))
```
This will output:
```python
<class 'pandas.core.series.Series'>
```
This shows that x is a pd.Series. The other options are incorrect because `df.iloc[42]` will not return a pd.DataFrame and it can't be both pd.Series and pd.DataFrame at the same time.
</details>
---
## Question 7
Given is a *pd.DataFrame* **df** with 100 rows and a continuous index starting from 0 to 99.
What happens if we add a new row with an index that already exists (e.g., 42)?
❌ Adding to the end will result in an automatic matching index: Here, the added row will have the index 100.
❌ Pandas recognizes that you add the same index twice and will automatically create a *MultiIndex*, hence use the next column additionally as an index.
❌ Similar to SQL/Databases, the index is a *primary key*, so the new row can't be added and it will fail with an error.
✅ The new row is added, non-unique indices are no problem.

<details>
<summary>Explanation</summary>

> 💡 **[DataFrames](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
❌ **Incorrect**, because when you add a row with a specific index, pandas will use that index number, not auto-increment the index to 100.
❌ **Incorrect**, because pandas does not automatically convert to a MultiIndex when duplicate indices are added.
❌ **Incorrect**, because unlike SQL/Databases, pandas allows non-unique indices. It doesn't treat index as a primary key.
✅ **Correct**, because in pandas, it's possible to have duplicate indices. If you add a new row with an index that already exists, the new row will be added with the same index. For example:
Let’s assume we have the following DataFrame:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f038a20b-3964-4a36-98d5-34b37f2597a4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZYS7JPV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHCEVks2pzJ0PIaSRKseVB9Z8PrgGezBP0X5JVRGlM66AiAhgfWk5oJWOV9n9U6tqTd5P1nu%2FYDdpgQOETAHfBgADir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMKvvLh4Cdm%2FOzWZd9KtwDXHkWVspR0Qq%2FaRh1Q2Jt1SC22vd40pXaKJg1%2FCP6bW2GVbCusz4hMVOJsIoHCvhyjzLEOu1842JDNF%2BbhvwLPC9nUXt4VElWz8X6SUblx%2FTU8QltbGusImlxaltD6H93F0rNnAMd1n70UChbwLVyyAOblbawaAt5FaRBHVnxIg6LoF38GwlfAQINVW%2BiMHST0FqRtrNlc3zVREh%2FKbCfw0%2FD5Xj%2Folb569NxMyExT6WfT%2BKjwE4722UmzJuxcPbfMLl6jjfaSzzE7XtLElb9kIub48V40gDU8T01Xu2RzWCRbmFLRC5AKOAAbpGWHF8c0oCHU8kuEyhlons0D%2FEY0AZE%2BCCUudBikg%2B%2Fta3kgAsXcdegCUm795mDd%2FPbjn%2Bu5Q%2FbpH8A3bRCCfAgmX%2Bjwj%2FGZVzxkLJTR4DJAydaBB6OhDQYpYnTJKODkYMRe3PyKlfnbUZ8jDh4Ea5Y6BPw7cSGSJcgKPKkMqOghRnkd3odKAcdxj%2F34xCWCvmRJEAzchlxQ8B0i4nyyGrBR9e%2Bhyw3i089RulThRvNAKtJUtwPB7SOxEoFwRwYAiv%2BVIeu%2F8CTRdqMqCZKKkxuZTgFMdbUpF0SlxC6C1N6ELX1gZgiuTAysGLH%2F5CMi%2FQw%2Bs33yQY6pgHsCqUfpTv8FeH0M48fN16FSfbUhl7A%2Fyntswnj0dx6oA6yWQ%2BIkHyeuWW1YQEFJ2CXDqgXq0%2F%2Bt31DDufZW7oyBN6YOaT01dvvX2AtugDc18qmG%2FnxlXEzd8L51UWhjtdSCWOvuNsmmLpz2YGXSz0XYJg8UetlhYs8UVozEHX%2FfxSn8P1zSoxLqL7qijmKyaj12cr7GnLHTHhs7F%2FR%2FCVwXCTBS9qb&X-Amz-Signature=6fdf7eb4381d8c3b4a77b58b6e625069f86a32e81e86e480ad34b16a6862aabd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now if we create a new Series with the index 42 again
```python
new_row = pd.Series({"A": 4}, name=42)
```
And add this new row to the DataFrame:
```python
df = df.append(new_row)
```
We can see that the same index 42 exists now twice in the DataFrame:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/58fb90e3-3ad4-4c32-98ce-b9b7591acf0d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZYS7JPV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHCEVks2pzJ0PIaSRKseVB9Z8PrgGezBP0X5JVRGlM66AiAhgfWk5oJWOV9n9U6tqTd5P1nu%2FYDdpgQOETAHfBgADir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMKvvLh4Cdm%2FOzWZd9KtwDXHkWVspR0Qq%2FaRh1Q2Jt1SC22vd40pXaKJg1%2FCP6bW2GVbCusz4hMVOJsIoHCvhyjzLEOu1842JDNF%2BbhvwLPC9nUXt4VElWz8X6SUblx%2FTU8QltbGusImlxaltD6H93F0rNnAMd1n70UChbwLVyyAOblbawaAt5FaRBHVnxIg6LoF38GwlfAQINVW%2BiMHST0FqRtrNlc3zVREh%2FKbCfw0%2FD5Xj%2Folb569NxMyExT6WfT%2BKjwE4722UmzJuxcPbfMLl6jjfaSzzE7XtLElb9kIub48V40gDU8T01Xu2RzWCRbmFLRC5AKOAAbpGWHF8c0oCHU8kuEyhlons0D%2FEY0AZE%2BCCUudBikg%2B%2Fta3kgAsXcdegCUm795mDd%2FPbjn%2Bu5Q%2FbpH8A3bRCCfAgmX%2Bjwj%2FGZVzxkLJTR4DJAydaBB6OhDQYpYnTJKODkYMRe3PyKlfnbUZ8jDh4Ea5Y6BPw7cSGSJcgKPKkMqOghRnkd3odKAcdxj%2F34xCWCvmRJEAzchlxQ8B0i4nyyGrBR9e%2Bhyw3i089RulThRvNAKtJUtwPB7SOxEoFwRwYAiv%2BVIeu%2F8CTRdqMqCZKKkxuZTgFMdbUpF0SlxC6C1N6ELX1gZgiuTAysGLH%2F5CMi%2FQw%2Bs33yQY6pgHsCqUfpTv8FeH0M48fN16FSfbUhl7A%2Fyntswnj0dx6oA6yWQ%2BIkHyeuWW1YQEFJ2CXDqgXq0%2F%2Bt31DDufZW7oyBN6YOaT01dvvX2AtugDc18qmG%2FnxlXEzd8L51UWhjtdSCWOvuNsmmLpz2YGXSz0XYJg8UetlhYs8UVozEHX%2FfxSn8P1zSoxLqL7qijmKyaj12cr7GnLHTHhs7F%2FR%2FCVwXCTBS9qb&X-Amz-Signature=37a026e00eb67c5d99fad8f4e2824b912af0980b54529886a52ea4b638f76302&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
