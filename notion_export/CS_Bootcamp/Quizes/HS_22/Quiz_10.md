---
title: "Quiz 10"
notion_id: "ad01aed2-0dea-4a5b-bb37-343027165fb3"
notion_url: "https://www.notion.so/Quiz-10-ad01aed20dea4a5bbb37343027165fb3"
exported_at: "2025-12-13T23:16:20.840788+00:00"
---

# Quiz 10

## Question 1
How many *axes* are created with the statement:
```python
fig, axes = plt.subplots(7, 8)
```
56

<details>
<summary>Explanation</summary>

The subplots function takes two parameters as inputs: (1) No. of rows, (2) No. of columns.
In this code snippet we create a plot with 7 rows and 8 columns. Thus, the plot will in total contain 7 * 8 = **56** subplots that can be filled with data.
</details>
---
## Question 2
We want to create the following line plot with the values from following *pd.DataFrame* **df**.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ba7cae60-975c-45ea-9d4d-d5740d079a09/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=28eacae66c2c41a486a09c617d35f0324fce848db76b6400a349ecc685d8675a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The *pd.DataFrame* **df** looks like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8855b98d-ce33-4262-99e5-5ab81fcf48a2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=97c6d423c219d516458f6455293c7ea69947bd2aa52ea65c6f250b138fda7bce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can you get the x-values and y-values for the **blue** line?
x-values: `df.columns`
y-values: `df.loc['Banana']`

<details>
<summary>Explanation</summary>

**x-values**
The x-values are the ones that are displayed on the horizontal axis, i.e., the weekdays. We see that in the DataFrame **df**, the weekdays are the column names. With `.columns` attribute we can select the column names of a DataFrame.
**y-values**
The y-values are the ones that determine how the blue line flows (if it goes up or down). Each line represents a fruit. The blue line represents the fruit Banana. We can see that each fruit has a row in the DataFrame. Thus, we want to select the Banana row which we can do by using `df.loc['banana']` or `df.iloc[1]` (Banana is the second row in the DataFrame).
</details>
---
## Question 3
Given is the following code:
```python
fig, ax = plt.subplots(figsize=(8, 6))

width = 0.3

xticklabels = fruits.columns
xticks = np.arange(0, len(xticklabels))

ax.bar(xticks - width, fruits.loc['Cherry'], width = width, color='green', label='Cherry')
ax.bar(xticks, fruits.loc['Banana'], width=width, colot='blue', label='Banana')
ax.bar(xticks + width, fruits.loc['Apple'], width=width, color='red', label='Apple')

ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

ax.legend()

plt.show()
```
Which figure does the code produce?
**❌ Figure 1**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/695a6b05-f2f8-40a9-bf6a-a39a44b06cb5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=b4cad96127059a229eb2eaf9454adc981911540768afeb38da7e04d2f48549ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 2**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/28f2f2fb-1f68-4c7b-bcd1-b8a02271a5b7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=68a318b3fc7aa85649857066eb2c3779f1f84f5e9d31fb7f4cf9e846a852ec5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**✅ Figure 3**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/671fec9e-0d8b-481a-8e6d-5e86347f6490/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=0210e422092c24d98975a946e7de76275a2ddaea48e42e6328cf20105b30eb06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 4**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3d5de852-f8cf-4ece-88eb-e79c917123e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=f93fadcc1040009d383570ca83f60863745ba030916897d4d83244a934f87b27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

Here the trick is to know how the bars are positioned. We can figure this out by looking at the following lines in the code:
```python
ax.bar(xticks **- width**, fruits.loc['Cherry'], width = width, color='green', label='Cherry')
ax.bar(xticks, fruits.loc['Banana'], width=width, colot='blue', label='Banana')
ax.bar(xticks **+ width**, fruits.loc['Apple'], width=width, color='red', label='Apple')
```
The first parameter of the .bar() method are the x-positions of the bars.
We can see that:
- for the **Cherry** fruit, we deduct the width (-0.3) from `xticks`. Thus, the Cherry bars are positioned to the left. 
- for the **Banana** fruit, we don’t deduct or add any value from `xticks`. Thus, the Banana bars are positioned in the middle. 
- for the **Apple** fruit, we add the width (+0.3) to `xticks`. Thus, the Apple bars are positioned to the right. 
In the third plot, **Cherry** is on the left, **Banana** in the middle and **Apple** on the right. 
</details>
---
## Question 4
Given are the following three boxplots.
In the image, select the region where 50% of the *sepal width* observations for *Versicolor* are visualized.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/74518876-1b87-44f7-b914-783cb42a8308/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=ca32c35340d312902478ec816276e210789eb8f1e54b59b2567c8c21afb792bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

The structure of a box-plot is as follow:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fd06423b-c4cf-4779-842a-ac6488fdb79f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S6DXN7Z%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDdOnQSyeMmbFeXAIhbC365nr%2FXAyLVEX5IkQii%2F3qVqwIgYLcVZE%2FGhvOeW%2B%2Fz%2FdwgysSnDo%2F9jyTNGapbuXsIEVcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDA377E1YLuDyY%2F4tfircA1Xk56p9cqIFq4kPvvRGXk4ISQBYGmFWNK9MFHIJY5K6JAMW3UGbbdv1rh9tz4f9Cin6i%2B8baI09cqxVsSv1PYhuotmbu01OT%2FsxwdLNMpr0KWJ8pJyQbwbbdiWOFNPiWpfRK3AUeHY4wZ81p2ehZ41ClwZzFpF6rR4DZmioMYw%2FdXle8fT7He2joVW8hNso55bw3UJW3%2BdzlZzj%2FxEm7zdYDA%2Bj7RAQGgGH%2F0k3XCrZVhg4LtwBk3xSNjn54khtskl3fHwBvDIZ4GyiiCDNxRQVDR1%2BzjOXxpT1cQuLJVfhrU3FWXlT95Ll%2BQLbsmcEaJAah5Uh1IoR8DBwt0IdY1HRRWoIKkbQMXSXKf2c4%2B4WjWxFdebGvIN%2FlDAYuA%2BXV%2FZfXi6uusmZAlyb70tCX2f8%2FTYCPfPa%2FMtoZEWldHdEuBFPhaUxCdSfpax%2FQvIheXmLE6Jx43hfPDWxXG7FIxN8Y07sev%2B%2BXGAbOCN%2FrZNdnEfhhDc8CQ2bAzUlVDX4Euuj3b5xtxQGv1JaOwNzCbMocp0oHEQWYJtFB4fer7v%2Bfze9p3p%2FWt0emj4g00phyNgCPesvo1j%2BcHfBhtXsAYYeeyKl0yRd7ewwUUIeRKTg7%2FH7OC1hzQr0rMyEMPzN98kGOqUBk0R3%2BB5qmW%2BzrFCezmeCbSD1blwER110mratuXiLJcnh%2FbZRu7qnA7JHC2NE2c1giGkrnoe81FoQLeyOgGJFDmTUuHtOFoklGG%2FCw22eoJuJEe5wQWytxRlE%2F6kho1IDki4N%2BJogeYepiHAEmDj4Hzbmqf9u9vMOBIf7931ip1f6NJErJEi7c42Ku%2F2Uq0Wax8rZkXW0vgTOf%2FlOUNyAPcBR8NKC&X-Amz-Signature=3f637358b2eb7cb7bead491d5c89c05bc8dd09e8f8ac03931dcbe6c6dd5aa05f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Each quartile represents 25% of the data, thus the box in the middle represents 50% of the data.
</details>
---
## Question 5
We want to produce this plot:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5363df47-9e70-4389-9327-e859bf892a00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=247a60c5524d87965c048864432419fe9c80dfa24ab36c43d0be9941103bb0d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Which keyword argument is required to create this plot?
`fig, axes = plt.subplots(3, 1, `**`sharex=True`**`)`

<details>
<summary>Explanation</summary>

With `sharex=True`, the x-ticks are shared amongst the subplots. Thus, the name of the weekdays are only displayed ones. 
The y-ticks, however, are not shared and are displayed in each subplot separately.
</details>
---
## Question 6
We have the following *pd.DataFrame ***df** of fruit sales. The code below was used to create the given figure.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5ecb8592-f208-42fa-ba9a-7e451775c803/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=28b0ed1e0810293d127b10965c8b5860a978971c920b94f5b7aaeacd43169793&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
fig, ax = plt.subplots(figsize=(8,6))

ax.bar(df.columns, df.max(), color='green')
ax.bar(df.columns, df.loc['Banana'], color='blue')
ax.bar(df.columns, df.min(), color='red')

plt.show()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/873e4980-985f-43d3-87ee-044ba976e19a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY24HCNF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDZ5pl4QWWK8OozVzlti6C2soSfJXtePIYpTh4%2BUKf3gQIhAPWx3dIhmmveLTRpEGJY31%2FvVvT5dsUAtKIxuSrdSrEkKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8CGpl20w4P8EeY%2BUq3AO2fPxt2C2HnXKoOFEvuV9fxikEW4Q9WAWftJ%2BIxM5sDyEHa1MszaOhFJuGwdfSb%2FqhHxpmeLf58coXDRxe0Uwk%2BJUI0e9AUtojz7usdZ%2FqCWV2xXNzxHcRyrpNmsqrDcIP8Zdlg3LotouALQtYkTomPF%2BwTggV9JQQp8h23ana7Za0Cff379KWMb0BfhEtJaY5P22i4KazhzHrlf9uB7ERGiAY6yKs7y2e1rjICroI9pfudF%2BzAzCJuVTk1k%2FrZ06Qx9aKoD9eWHNPeYarKDEcSc%2BZt9EqHxdrN5p7gpsbWoXbMgVz7rl3IDIl3wie0zN5EtdGBIAXRSUFXDsWQScvWOiBsCXL%2BOhcOmITaC6VVvjsaFXcgGWjSlbIB3umV1cAiiPJgWv9ibgKjINDw1Hu0Jael%2BFvVKUgGD1ROQlKrLliBeW3ukgSRjX2xF7tuj%2BoZ8hkYn3SOgYAoWLfXpLO%2FVJig%2FUxKppFnOChalDoRhnCaKbkN6eFsMRF2%2FyQeRB0RJ72AeSGZp1cPKfKwpHX9r2fQGlNwFhmVL4qc34bPVVGCJP0HYNU0A3y%2BZtHCXX%2BGc2g7SqKVP817uk3bd7DsmIaM5HuYo11eOJavK0R7JlK%2F6aEbeV%2FdSituzDAzvfJBjqkAYFASzxgUsDC1BTcqFvUHkg94R5123AG4xIAA%2F%2FZOwvU7ybKpxvOepvyWOI%2BoVkFf8aC7mFKYdtBpltsXuue36UiS1tBsg511eDY6taafgfdIB89wLc%2FeyhCTMz%2FiPQeTY%2BsZzEn45CnXQZPHyKscSyOIZ8%2FMD1gl8W5EO9xzzbU1dGnFsJuJiXzQusvyqGKIEGb%2BRb%2BbKJAgQMQ5YYlIX2u9ykL&X-Amz-Signature=05a569fc7cbf28552ddc82891760b0a5e5525bc6a76b3b69b3fe83d3a5d18c88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Mark <u>all</u> the statement that are true.
✅ From the plot, it is impossible to know how many bananas were sold on Friday. 
❌ Relative to the other fruits on the same day, most bananas were sold on Wednesday. 
❌ On Thursday, Friday, and Saturday, the sales for bananas were 0. 
❌ Friday is the day with fewest sales in total.
✅ Bananas were the most sold fruit on Tuesday because the blue bar is the largest there. 
✅ Sunday is the day with the fewest sales in total.
❌ This is a stacked bar plot. 

<details>
<summary>Explanation</summary>

✅ **Correct**, because the green and the red bar are overlapping the blue bar, thus we can not infer from the plot how many bananas were sold on that day.
❌ **Incorrect**, most bananas were sold on Tuesday. 
❌ **Incorrect**, the sales was not zero, the bars are simply not visible in the plot as they are overlapped by the other bars.
❌ **Incorrect**, Sunday is the day with the lowest sales.
✅ **Correct**, the blue bars represent the sales of bananas.
✅ **Correct**, don’t get irritated by the heights of the bars, as they are not stacked on each other but rather just overlapping.
❌ **Incorrect**, it is a simple multiple bar plot. The bars are just overlapping each other, which is why it appears like a stacked bar chart. If we want to create a stacked bar chart we would need to define the `bottom=` parameter.
</details>
---
