---
title: "Quiz 9"
notion_id: "4116b5eb-4ce8-4f10-8458-06cd3d840692"
notion_url: "https://www.notion.so/Quiz-9-4116b5eb4ce84f10845806cd3d840692"
exported_at: "2025-12-13T23:21:25.709912+00:00"
---

# Quiz 9

## Question 1
Which of the following data types can a query on a pd.DataFrame return?
✅ String
✅ Pandas DataFrame
✅ a 64 bit float
✅ Pandas Series

<details>
<summary>Explanation</summary>

> 💡 **[Pandas datatypes](/1867045b058343e1a66b677961515907#466ff2767af14951a462efaa71cc9e86)**
✅ **Correct**, a query on a DataFrame can return a string as it is posisble to store strings inside a DataFrame. Thus, when accessing a single cell in a DataFrame it is posisble to retrieve a string.
✅ **Correct**, a query on a DataFrame can return a new DataFrame that meets the query conditions. For example, if you use the `df[df['column'] > 5]` syntax, it will return a new DataFrame with rows where the value in 'column' is greater than 5.
✅ **Correct**, if your query is designed to return a single value and that value is a float, then yes, it can return a 64-bit float. For example, `df['column'].mean()` would return a 64-bit float if 'column' contains float values.
✅ **Correct**, if your query is designed to return a single column, it will return a Series. For example, `df['column']` would return a Series.
</details>
---
## Question 2
You have the two pd.DataFrame objects persons and addresses with the following columns:
```python
print(addresses.columns)
>>> ["zip", "city", "street", "number"]

print(persons.columns)
>>> ["name", "address_id"]
```
The indices of both DataFrames are continuous non-duplicate integers starting from 0. The column **address_id** in **persons** is supposed to be a *foreign key* for the **index** of the **addresses** DataFrame.
There are some persons that do not have an address, so the value of the **address_id** for these entries will be *np.nan/NaN/pd.NA*.
Additionally, an entry in the **addresses** DataFrame could be referred to by none, one, or multiple persons.
Which of the following statements returns a *pd.DataFrame* with <u>all</u> columns of both DataFrames **persons** and **addresses** with the following restriction:
The resulting DataFrame must contain all entries from the DataFrame **addresses** and their referenced person, if one exists. If no person is referenced for an address, the corresponding values for this row should be set to np.nan/NaN/pd.NA.
If a person is not referenced by an address, the person should not be included in the result.
❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`
❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`
✅ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`

<details>
<summary>Explanation</summary>

> 💡 **[.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
The correct answer is:
✅ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`
Explanation:
The `pd.merge()` function is used to combine two or more dataframes into a single dataframe. The `how` parameter determines the type of merge to be performed. It can be 'left', 'right', 'outer', or 'inner'.
- 'left': use only keys from left frame
- 'right': use only keys from right frame
- 'outer': use union of keys from both frames
- 'inner': use intersection of keys from both frames
In this case, we want to keep all the entries from the `addresses` dataframe and their referenced person, if one exists. If no person is referenced for an address, the corresponding values for this row should be set to np.nan/NaN/pd.NA. This is exactly the behavior of a 'right' merge.
The `left_on` and `right_index` parameters are used to specify the columns or indices on which to merge the dataframes. Here, we are merging on the 'address_id' column from the `persons` dataframe and the index of the `addresses` dataframe.
The other options are incorrect because they either exclude entries from the `addresses` dataframe that are not referenced by a person (inner join), include persons that are not referenced by an address (left join and outer join), or they merge on the wrong columns or indices.
> 🤯 **Sill unclear? Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#5358c79993774a36b6fd71751f8607c6).**
</details>
---
## Question 3
You have the two pd.DataFrame objects persons and addresses with the following columns:
```python
print(addresses.columns)
>>> ["zip", "city", "street", "number"]

print(persons.columns)
>>> ["name", "address_id"]
```
The indices of both DataFrames are continuous non-duplicate integers starting from 0. The column **address_id** in **persons** is supposed to be a *foreign key* for the **index** of the **addresses** DataFrame.
There are some persons that do not have an address, so the value of the **address_id** for these entries will be *np.nan/NaN/pd.NA*.
Additionally, an entry in the **addresses** DataFrame could be referred to by none, one, or multiple persons.
Which of the following statements returns a *pd.DataFrame* with <u>all</u> columns of both DataFrames **persons** and **addresses** with the following restriction:
The resulting DataFrame must contain all entries from the DataFrames **persons** and **addresses.**
❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`
❌ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`
✅ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`

<details>
<summary>Explanation</summary>

> 💡 **[.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
The correct answer is
✅ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`.
Explanation:
In pandas, the `merge` function is used to combine two or more dataframes based on a related column between them. The `how` parameter determines the type of merge to be performed:
- 'left': Use only keys from left frame
- 'right': Use only keys from right frame
- 'outer': Use union of keys from both frames
- 'inner': Use intersection of keys from both frames
The 'outer' merge is the only option that includes all entries from both dataframes, regardless of whether there is a match in the other dataframe. This is why the correct answer is `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`.
The `left_on` and `right_index` parameters specify the columns or indices on which to join the dataframes. In this case, we're joining on the `address_id` column from the **persons** dataframe and the `index` of the **addresses** dataframe. All other options either exclude some entries or incorrectly specify the columns or indices to join on.
> 🤯 **Still unclear? Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#8ec92dddc52c409380bae0890373b33d).**
</details>
---
## Question 4
In Assignment 09, there was the pd.DataFrame **ORDERS** with the column products that encoded the items and their count as a JSON encoded string. 
As a first step, you fixed the error of the **json** module and overwrote the column products now with a dictionary in the correct format. 
Which of the following statement returns a pd.Series with the same index as df and the minimal number of distinct products as values for each purchase?
❌ `df['products'].apply(lambda r: min(r.keys()))`
❌ `df['products'].apply(lambda r: r.values().min())`
❌ `df['products'].apply(lambda r: min(r))`
❌ `df['products'].apply(lambda r: max(r.keys()))`
❌ `df['products'].apply(lambda r: r.values()).min()`
❌ None of the given choices will produce a *pd.Series*.
✅ None of the given choices will produce the wanted result, even though it produces a *pd.Series*.

<details>
<summary>Explanation</summary>

> 💡 **[.apply()](/1867045b058343e1a66b677961515907#9e6d1643dc24411181facc1dd3265ffd)**
> ↪️ **Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#1f6c5f13ae564237afdf9560ace362b5).**
</details>
---
## Question 5
As a nice housemate that you are, you prepared Christmas presents for your family. 
You have measured the height, width, and length of the packages and saved the information in a *pd.DataFrame* **df**. Additionally, for each present, you recorded the name of the recipient in the column recipient which you set as the index for **df**.
How can you aggregate the minimal height, width, and length <u>per recipient</u>?
The result should look something like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/daf59472-35da-4221-aecb-ad0307bc494c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HVGSRG4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDkk4hjaygkMfilMARd1cOsiTce0CgmJ57pidK8pCTYXgIgYgC7jy4PxtFjg2rQ3m7G2MEGpvJr2aeTWwjbj1K7vcAq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDNXr0%2BZmhppBwh8mwyrcA3B%2BRKgbjXkH7woqsN7WkB9XNm0kVjadyyu3vhZq8Vsn%2FDoLoiMPI0TE0PhIDPJGC9%2F63KSRqvcw3vBlbzcvh2oZVRDuJpYe3bEn7aOP7K5YFWbvsng29tmI%2BNNS50OFmD0izpTkIcD7GnBxHAfCr6GNwMwsUo5UHvYvMNvHkNPUVZjrCi4niRwm2OCQOGwCGYH0U3xPN572lr4CW%2FXNxo3L%2BsVHLcJTtQk3LJfKvAwGeCcA7b%2BVk%2BZr9pWfh9gLCRss%2FHGl73IEBvj9rDteNGXRFtT3rBmPGHpGF7JmuJ9RHFMplHsaoOO9FIhPwNQ3tuRHVS8I54qNhm4q7Q5tv9xkmy%2FxA5EG3M1i0c30rZbPi7XJYq8SY%2FS8DgK3w7KLr6uuBIfVW2sdQlfwdfaVwwQOT8Iup92JIB1N7oZ9QXwsqW6k45OsVmquZaVtq%2FNWq9pgAzXpgz8zFBLP66pDpu9RaZgBsV%2BaR5yWaYUF0mVJLqiqMWxa41Vlel7Jubnv%2BmuFELaRsAUx%2F7Cl1MaypNL0yfgFEH0fgMqxja3DOR%2BE4P9RmanbOmU9U0bRGWXW%2BOR4v8Dix42sDk0m%2BVJAM%2BTb0VUy7eo5wxj8SbilGAFMlcjwdBWS7QUk4xOWMLXO98kGOqUB6TEcNJs0EgZc9lA%2FMA5EoQf%2FnwfqZ0FJmk90hoJE81kgF1vx%2FBXRgN5Y1y1C6wrXoEdRRlL9cQhVMlN162A06k%2BCpVkH9In8EAs5%2B2RP2kroMUW0sJc%2BV7uJQBvvk5uAlT0942KHr8sg3j75M2XJWOg0W3XmmwheP9XrC6r%2BdBlL9XJfIVVv1JEzQJ9%2FLuAhKDX9S8TfcusXxyDYUD0bxH1Sa0v0&X-Amz-Signature=990eea54ccb3b59c85849f8441976a197e0e06cbcabf3647c32bf0215c2c4300&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Mark <u>all</u> statements that result in the variable **agg** contain the *pd.DataFrame* as above. The *recipient* must be the index.
❌ `agg = df.agg("min", axis=1).groupby('recipient')`
❌ `agg = df.index.min()`
❌ `agg = df.min('recipients')`
❌ None of the statements will create the wanted DataFrame.
❌ `agg = df.min('index')`
✅ `agg = df.groupby('recipient').agg('min')`
✅ `agg = df.groupby('recipient').min()`
✅ `agg = df.groupby('recipient').agg(np.min)`

<details>
<summary>Explanation</summary>

> 💡 **[.agg()](/1867045b058343e1a66b677961515907#1c8f902fb8774ff7ab8c9bd1d9f76684), [.groupby()](/1867045b058343e1a66b677961515907#006284de429d48c2b72b22f08a3b3b15)**
❌ **Incorrect**, because it tries to aggregate before grouping by 'recipient'. Also, `groupby('recipient')` would not work here because after the aggregation, 'recipient' is no longer a column in the DataFrame.
❌ **Incorrect**, because it will return the minimum value of the index, not the minimum values of the height, width, and length for each recipient.
❌ **Incorrect**, because the `min` function does not take a string argument, it should be used without any arguments to return the minimum values for each column.
❌ **Incorrect**, because there are correct statements.
❌ **Incorrect**, because the `min` function does not take a string argument.
✅ **Correct**, because it groups the DataFrame by 'recipient' and then aggregates the minimum values for each group.
✅ **Correct**, because it is the shorthand version of the previous statement. It groups the DataFrame by 'recipient' and then returns the minimum values for each group.
✅** Correct**, because it groups the DataFrame by 'recipient' and then applies the numpy function `np.min` to aggregate the minimum values for each group. It is equivalent to the previous two correct statements.
> 🤯 **Still unclear? Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#400446c4746144e2b55f111129b3b014).**
</details>
---
## Question 6
In Assignment 9 you implemented the function *study_overview()*, which works on the DataFrame STUDIES. It should give an overview of where which combinations of *courses* and *regions* exist.
Now look at the following implementation of the function:
```python
def study_overview():
	return STUDIES.merge(index='bachelor/master', columns='course', values='region')
```
Mark all the correct statements!
❌ *columns* and values are set incorrectly, correct would be *columns='region'* and *values='course'*.
✅ *index* and *values* are set incorrectly, correct would be *index='region'* and *values='bachelor/master'*.
✅ The function pivot() must be used instead of merge().
❌ The function reshape() must be used instead of merge().
✅ The function cannot be executed successfully.
❌ None of the other functions can be executed on the DataFrame.

<details>
<summary>Explanation</summary>

> 💡 **[.pivot()](/1867045b058343e1a66b677961515907#b7e324abb8a749b38b4a2386f6d4dbf7), [.merge()](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f)**
> ↪️ **Check the [explanation here](/09c7128eaedd43f19a4ccab47219c8a2#9af05826713b446b9ee59383d2362e05).**
</details>
---

