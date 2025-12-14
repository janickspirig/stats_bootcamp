---
title: "Data Science"
notion_id: "56933163-5be6-4b12-9f6a-790023fe2183"
notion_url: "https://www.notion.so/Data-Science-569331635be64b129f6a790023fe2183"
exported_at: "2025-12-13T22:55:31.981078+00:00"
---

# Data Science

---
**Data types**
Define for each item below whether they are Nominal, Ordinal, Interval or Ratio data. 
- Hair colour
- Time
- IQ
- Weight
- Gender
- Job seniority level
- Date
- Weight

<details>
<summary>Solution</summary>

| Hair colour | Nominal |
| --- | --- |
| Time | Interval |
| IQ | Interval |
| Weight | Ratio |
| Gender | Nominal |
| Job seniority level | Ordinal |
| Date | Interval |
| Weight | Ratio |
</details>
---
**Data types**
Define for each statement below whether it is True or False
- [ ] 1) Ordinal data have equal spacing
- [ ] 2) Nominal data can be segmented into categories
- [ ] 3) Ratio data have a true zero
- [ ] 4) Interval data have equal spacing and can be put into a rank order
- [ ] 5) Ordinal data can be segmented into categories, can be put into a rank order but do not have equal spacing

<details>
<summary>Solution</summary>

False → no equal spacing
True
True
True
True

</details>
---
**Numpy**
What is one major advantage of numpy array over conventional lists?
- [ ] 1) In a numpy array we can store even more different kind of data types
- [ ] 2) Numpy arrays are not limited in the number of dimensions they can represent
- [ ] 3) With numpy arrays we can do calculations element-wise over entire arrays

<details>
<summary>Solution</summary>

`C`
</details>
---
**Pandas**
What does the method `.read_csv()` return?
- [ ] 1) DataTable
- [ ] 2) DataFrame
- [ ] 3) DataSeries
- [ ] 4) Numpy Array

<details>
<summary>Solution</summary>

2 → DataFrame
</details>
---
**Pandas**
If the data in a .csv file is not comma separated, we cannot use the `.read_csv()` method. True or False?

<details>
<summary>Solution</summary>

False
We can still use the method, but we must provide a value for the `delimiter=` parameter as this is by default set to comma (`delimiter=','`)
</details>
---
**Pandas**
Which parameter allows us to specify our own column names when using the .read_csv() method?
- [ ] 1) `column_names=`
- [ ] 2) `columns=`
- [ ] 3) `headers=`

<details>
<summary>Solution</summary>

`columns=`
</details>
---
**Pandas**
Which value do we need to assign to the `axis=` parameter if we want to drop a Column or a Row?
- [ ] 1) Column: `axis = 0`, Row: `axis = 0`
- [ ] 2) Column: `axis = 1`, Row: `axis = 0`
- [ ] 3) Column: `axis = 0`, Row: `axis = 1`
- [ ] 4) Column: `axis = 1`, Row: `axis = 1`

<details>
<summary>Solution</summary>

2) Column: `axis = 1`, Row: `axis = 0`
</details>
---
**Pandas**
Which value do we need to assign to the `axis=` parameter if we want to compute the sum for a Column or a Row?
- [ ] 1) Column: `axis = 0`, Row: `axis = 0`
- [ ] 2) Column: `axis = 1`, Row: `axis = 0`
- [ ] 3) Column: `axis = 0`, Row: `axis = 1`
- [ ] 4) Column: `axis = 1`, Row: `axis = 1`

<details>
<summary>Solution</summary>

3) Column: `axis = 0`, Row: `axis = 1`
</details>
---
**Pandas**
How many rows do the functions `.head()` and `.tail()` return?
- [ ] 1) 5
- [ ] 2) 10
- [ ] 3) 15
- [ ] 4) 20

<details>
<summary>Solution</summary>

1
</details>
---
**Pandas**
The `.min()` and `.max()` methods can be applied on an entire DataFrame and on a single column. True or False?

<details>
<summary>Solution</summary>

True
If we apply these methods on the entire DataFrame, e.g., `df.min()`, a Series is returned that contains the minimum value for each column.
</details>
---
**Pandas**
Which information does the `.describe()` method return?
- [ ] 1) Mean value
- [ ] 2) Mode value
- [ ] 3) Variance
- [ ] 4) Median value
- [ ] 5) Number of values
- [ ] 6) First quartile
- [ ] 7) Skewness
- [ ] 8) Second quartile
- [ ] 9) Third quartile
- [ ] 10) Minimum value
- [ ] 11) Maximum value
- [ ] 12) Standard deviation

<details>
<summary>Solution</summary>

1, 2, 4, 5, 6, 8, 9, 10, 11, 12
</details>
---
**Pandas**
![my_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dd540cbb-fbe8-4255-8899-62102dd247c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVPZQDNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGfAPcIFeX0UpyRT0DCz7JT%2Bqyy74pPRTIuasgIXnzEIAiEAtXgNBwKQLEgB3OCpAjhEiOJVpiWpebcIhJXsWhNpL2Qq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGnWsCDIV06NgcDGISrcA80X4MfTOfTzFE9GSNUk8wK%2B5AajYtId7Z5pyHqgEgOKcUYODe0eQ2SfRXm4oWxjHwOCYIluJ8b8J7sWsDhHccubjkEyKtIO3Tp2S0kyMXr%2Fmbo%2BRBvz31QIIgTvU%2Fd89TZ%2FWnlZqBgy3O%2B7upNk5nR%2BmVgV7sCbU6Kdi9ojag5o37%2BtpY%2FFf%2B1fuQ7S0KWSijIgsuSlvvL6gah8mVFnfk7p%2FYeHrC9NxRCmRbwOHBbq%2FrYwLZeCqcEz%2Bvie5BC4Ii2r5df1t3sJ5lyy4T7%2BUWX%2FunWXfcLkXaVbCLiKNTec18w66Fn%2FM4dXIPgklvgHmtBcDUS6D4OMtFljdmqgpZDUly7mCX36%2FfTdJTsMM5k1iGQTHXe4hQJiTajv4QlN%2FNGSGsWFYHtHXsJFpdIsQpxldNYXZzBiOHW4E19Pmv6ILr1HipLWuBIGmLpIL5HQ9aQlzeV538DV55WE6gv8JIllluAzR0CVvx1AeLxz2RP5YSK0JX2xXI%2F8YhFqTjTdAFQMH2RM6Eom26Jmr7%2BFdJMMEw6mXKE2RYJKK9MqnOrH%2F8qZ1gwRHXe4xHld%2BN2UwoDH8HO8UyOT8Y623TTeSY%2FLqsMeyIHYDOq5d%2FkCQy6FoTRQEff9JCKuJ0d3MMDO98kGOqUBmRy90mBp5MIlBAvfDN696%2Ft%2BY6r%2FkGdLKLu4rbAXALRPof0u6GxTcdEtViOI%2F2azu0BYt8UyOZWQPGbfAy1p3Sujj0KaGEnAIVbSeXL0uL1xdMyAziOdenoWwCoHG%2FAVQEimKMX87HeLiwH3Vf%2BZxiqgrZX6i20LItWp8rhDRsyM908%2BXXyNV6aU9udMHSQWnEXzpHnTcr9l9vAFhYQ2E4So8TBS&X-Amz-Signature=f6bf3132e5327ed88b3ec9a6355dfe51307e2a8410c02c34f61dc598dd8dcff8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can we access all rows in `my_df` that have a value for `calories` bigger than 300 and a value for `duration` bigger than 40?

<details>
<summary>Solution</summary>

`df.loc[(df['calories'] > 300) & (df['duration'] > 40)]`
OR
`df[(df['calories'] > 300) & (df['duration'] > 400)]`

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b9273317-ed78-4094-b212-ec015d413af7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCT6VCKZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICQNBtx4xTLO6nKH46UdO0%2B%2BPDb941bGVX6wQuIhfjiRAiBVlh7s7MkBDpZKjO9uLIYTe10OJ751Sb%2FgqUlf08wmkSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMOt63qMP9ywtQAmOSKtwDJAErZApep7144fd4dckrrTmuzJy3jme43V%2FB22UbbR%2FCul%2FNvZ%2FtmoVGj%2BoRjrX%2FYxm6kFed6qBskJ%2BMV3%2FykFQT%2FZHrN3V2wabrwraFb1I%2BD6X8jmPAeZQE7mc%2FTP424%2FqWs0nwTlqMR0luVUlXtwBX4HMC4z%2B%2BxUdXrzWdeUodInYbEtByVLHa2nSFEzCJR%2FXidaBmMFO5I%2BQIP4Lt87XEMqs2V%2FzWFThwIAE3%2BIIsQ2TrB8dgZ37wz121n9NXIV8gvxoVVZPC915xht%2FhlYVhDQVRfqOIZK6FWZcKWtQUOnHHpRfRCeMDiI43JVC7qb9TuxScdb0oxMkiOTQQBgearlhsGQnB7uXk%2BA2aFIiRPbeEz4RMiiFx69m%2B27%2B1Yx9gP%2FtnmFQTkHOCW4NOW7auA%2FLpE30VkHs1HpUWK%2Fmx7%2Bu37YxaRLiSa3XHUQ%2BjAhZISDQK5iA%2BHTXsKKq1M7ZMfY9W8sqUGgiRqijl9WtNAEYT0fAYklEmppL79xs%2BHp%2B6lpYTCEb1vOrVMxpe6SgNit0i%2B8C4ZMfIF0ykV9xluzy0gt%2Fzi910vY9lER7ACpS9SkcWlhXZupyti04cNoT8U8u51YvXK%2B42NPl9pbAfoz1BdQ%2FBHxksDgUwgs73yQY6pgGezrQtEh%2FV7tXV3xfwA13gNQlKJp7QNRzk%2FEim44poATRTXeofUIntiRxmsoWPeoZj7OWWIyrpAIVw3G3m8ZUnQM325Qv4K%2BWkn3URCw3GFSk0tzJ%2FjRSKYJdjZDTXdFXUXHj04C8p3gMYMYsCc5d%2F2KnGJysLeNDHc19Pc1TXOhBMp4t5ShOQs%2B%2B7yXWsJ8XyBmphMz3pz5361z4yD11Um8zeNBEu&X-Amz-Signature=b174381e3904beb33ecbe0c75d1f3010d96eb37bd27122ac8bb38c7938827710&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
**Pandas**
The `.sort_values()` method is case sensitive which is why the value `'Zurich'` would be placed before the value `'basel'`. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Matplotlib**
A Matplotlib figure can have mutiple Axes. True or False?

<details>
<summary>Solution</summary>

True
In a Figure of subplots for example, each subplot is one separate Axes
</details>
---
**Matplotlib**
When we create a Figure of multiple subplots we create first all the empty subplots and then fill them one after the other with data. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Matplotlib**
Let’s assume we want to visualise the Age, Height and Weight of 10 different people. To do so, we create a Multiple Barchart. Thus, the name of each person is displayed at the x-axis and has three bars in this order (from left to right): Age (blue), Height (red), Weight (green). 
In the image below we see the bar groups of the first two persons:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3888d003-fe6a-493c-8a99-7b5b73692a67/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVPZQDNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGfAPcIFeX0UpyRT0DCz7JT%2Bqyy74pPRTIuasgIXnzEIAiEAtXgNBwKQLEgB3OCpAjhEiOJVpiWpebcIhJXsWhNpL2Qq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGnWsCDIV06NgcDGISrcA80X4MfTOfTzFE9GSNUk8wK%2B5AajYtId7Z5pyHqgEgOKcUYODe0eQ2SfRXm4oWxjHwOCYIluJ8b8J7sWsDhHccubjkEyKtIO3Tp2S0kyMXr%2Fmbo%2BRBvz31QIIgTvU%2Fd89TZ%2FWnlZqBgy3O%2B7upNk5nR%2BmVgV7sCbU6Kdi9ojag5o37%2BtpY%2FFf%2B1fuQ7S0KWSijIgsuSlvvL6gah8mVFnfk7p%2FYeHrC9NxRCmRbwOHBbq%2FrYwLZeCqcEz%2Bvie5BC4Ii2r5df1t3sJ5lyy4T7%2BUWX%2FunWXfcLkXaVbCLiKNTec18w66Fn%2FM4dXIPgklvgHmtBcDUS6D4OMtFljdmqgpZDUly7mCX36%2FfTdJTsMM5k1iGQTHXe4hQJiTajv4QlN%2FNGSGsWFYHtHXsJFpdIsQpxldNYXZzBiOHW4E19Pmv6ILr1HipLWuBIGmLpIL5HQ9aQlzeV538DV55WE6gv8JIllluAzR0CVvx1AeLxz2RP5YSK0JX2xXI%2F8YhFqTjTdAFQMH2RM6Eom26Jmr7%2BFdJMMEw6mXKE2RYJKK9MqnOrH%2F8qZ1gwRHXe4xHld%2BN2UwoDH8HO8UyOT8Y623TTeSY%2FLqsMeyIHYDOq5d%2FkCQy6FoTRQEff9JCKuJ0d3MMDO98kGOqUBmRy90mBp5MIlBAvfDN696%2Ft%2BY6r%2FkGdLKLu4rbAXALRPof0u6GxTcdEtViOI%2F2azu0BYt8UyOZWQPGbfAy1p3Sujj0KaGEnAIVbSeXL0uL1xdMyAziOdenoWwCoHG%2FAVQEimKMX87HeLiwH3Vf%2BZxiqgrZX6i20LItWp8rhDRsyM908%2BXXyNV6aU9udMHSQWnEXzpHnTcr9l9vAFhYQ2E4So8TBS&X-Amz-Signature=c9bfdc787cf3b07dcfcbfb1b977b76a332a11cce2e41a811d1b7577746c46a75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Each bar has a width of 0.2
What are the x-axis positions of the four points in the image below?

<details>
<summary>Solution</summary>

-0.2, 0.2, 0.8, 1.2 
The middle of the red bar of the first person is at position 0 and has a width of 0.2. Thus, it leans 0.1 to the left and 0.1 to the right. The half of the blue and green bars also leans to the left and right. Thus, their middle must be placed at -0.2 and 0.2 respectively.
Same calculation for the second person, whose red middle bar is placed at position 1.
</details>
---
**Seaborn**
Seaborn is built on top of Matplotlib and its main benefit is its simplicity to use. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Chart interpretation**
Look at the Boxplot shown below:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ef351802-9321-4c8c-804f-9a26069cb8ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVPZQDNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGfAPcIFeX0UpyRT0DCz7JT%2Bqyy74pPRTIuasgIXnzEIAiEAtXgNBwKQLEgB3OCpAjhEiOJVpiWpebcIhJXsWhNpL2Qq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGnWsCDIV06NgcDGISrcA80X4MfTOfTzFE9GSNUk8wK%2B5AajYtId7Z5pyHqgEgOKcUYODe0eQ2SfRXm4oWxjHwOCYIluJ8b8J7sWsDhHccubjkEyKtIO3Tp2S0kyMXr%2Fmbo%2BRBvz31QIIgTvU%2Fd89TZ%2FWnlZqBgy3O%2B7upNk5nR%2BmVgV7sCbU6Kdi9ojag5o37%2BtpY%2FFf%2B1fuQ7S0KWSijIgsuSlvvL6gah8mVFnfk7p%2FYeHrC9NxRCmRbwOHBbq%2FrYwLZeCqcEz%2Bvie5BC4Ii2r5df1t3sJ5lyy4T7%2BUWX%2FunWXfcLkXaVbCLiKNTec18w66Fn%2FM4dXIPgklvgHmtBcDUS6D4OMtFljdmqgpZDUly7mCX36%2FfTdJTsMM5k1iGQTHXe4hQJiTajv4QlN%2FNGSGsWFYHtHXsJFpdIsQpxldNYXZzBiOHW4E19Pmv6ILr1HipLWuBIGmLpIL5HQ9aQlzeV538DV55WE6gv8JIllluAzR0CVvx1AeLxz2RP5YSK0JX2xXI%2F8YhFqTjTdAFQMH2RM6Eom26Jmr7%2BFdJMMEw6mXKE2RYJKK9MqnOrH%2F8qZ1gwRHXe4xHld%2BN2UwoDH8HO8UyOT8Y623TTeSY%2FLqsMeyIHYDOq5d%2FkCQy6FoTRQEff9JCKuJ0d3MMDO98kGOqUBmRy90mBp5MIlBAvfDN696%2Ft%2BY6r%2FkGdLKLu4rbAXALRPof0u6GxTcdEtViOI%2F2azu0BYt8UyOZWQPGbfAy1p3Sujj0KaGEnAIVbSeXL0uL1xdMyAziOdenoWwCoHG%2FAVQEimKMX87HeLiwH3Vf%2BZxiqgrZX6i20LItWp8rhDRsyM908%2BXXyNV6aU9udMHSQWnEXzpHnTcr9l9vAFhYQ2E4So8TBS&X-Amz-Signature=0644f91ff2af46e9837155bdf0ec05e748a6f7056e4ba191c45ff1f8b6e8c4d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Which education level has:
- the highest median?
- the smallest range?
- most outliers?

<details>
<summary>Solution</summary>

Highest median → unknown
Smallest range → tertiary
Most outliers → secondary
</details>
---
**Chart interpretation**
Look at the Seaborn jointplot shown below.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/984f8797-0e56-4fb4-ad03-41befca8318a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVPZQDNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGfAPcIFeX0UpyRT0DCz7JT%2Bqyy74pPRTIuasgIXnzEIAiEAtXgNBwKQLEgB3OCpAjhEiOJVpiWpebcIhJXsWhNpL2Qq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGnWsCDIV06NgcDGISrcA80X4MfTOfTzFE9GSNUk8wK%2B5AajYtId7Z5pyHqgEgOKcUYODe0eQ2SfRXm4oWxjHwOCYIluJ8b8J7sWsDhHccubjkEyKtIO3Tp2S0kyMXr%2Fmbo%2BRBvz31QIIgTvU%2Fd89TZ%2FWnlZqBgy3O%2B7upNk5nR%2BmVgV7sCbU6Kdi9ojag5o37%2BtpY%2FFf%2B1fuQ7S0KWSijIgsuSlvvL6gah8mVFnfk7p%2FYeHrC9NxRCmRbwOHBbq%2FrYwLZeCqcEz%2Bvie5BC4Ii2r5df1t3sJ5lyy4T7%2BUWX%2FunWXfcLkXaVbCLiKNTec18w66Fn%2FM4dXIPgklvgHmtBcDUS6D4OMtFljdmqgpZDUly7mCX36%2FfTdJTsMM5k1iGQTHXe4hQJiTajv4QlN%2FNGSGsWFYHtHXsJFpdIsQpxldNYXZzBiOHW4E19Pmv6ILr1HipLWuBIGmLpIL5HQ9aQlzeV538DV55WE6gv8JIllluAzR0CVvx1AeLxz2RP5YSK0JX2xXI%2F8YhFqTjTdAFQMH2RM6Eom26Jmr7%2BFdJMMEw6mXKE2RYJKK9MqnOrH%2F8qZ1gwRHXe4xHld%2BN2UwoDH8HO8UyOT8Y623TTeSY%2FLqsMeyIHYDOq5d%2FkCQy6FoTRQEff9JCKuJ0d3MMDO98kGOqUBmRy90mBp5MIlBAvfDN696%2Ft%2BY6r%2FkGdLKLu4rbAXALRPof0u6GxTcdEtViOI%2F2azu0BYt8UyOZWQPGbfAy1p3Sujj0KaGEnAIVbSeXL0uL1xdMyAziOdenoWwCoHG%2FAVQEimKMX87HeLiwH3Vf%2BZxiqgrZX6i20LItWp8rhDRsyM908%2BXXyNV6aU9udMHSQWnEXzpHnTcr9l9vAFhYQ2E4So8TBS&X-Amz-Signature=2fa01bab7eaf85f10e5476b4437b53899f0e1e7c8e4d14b5d9cc732aaf1984fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
For Width and Length, in which range are most of the data points (approximately)?

<details>
<summary>Solution</summary>

We must look at the Histogram on top and to the right.
The highest bar on top of the chart goes from around 2.5 to 5. Thus, for Length most of the values are in this range.
The highest bar on the right goes from around 17.5 to 20. Thus, for Width most of the values are in this range.

</details>
---
**Chart interpretation**
Look at the Scatterplot shown below.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c31ada37-237c-485a-800a-759a40b9f3dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVPZQDNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGfAPcIFeX0UpyRT0DCz7JT%2Bqyy74pPRTIuasgIXnzEIAiEAtXgNBwKQLEgB3OCpAjhEiOJVpiWpebcIhJXsWhNpL2Qq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGnWsCDIV06NgcDGISrcA80X4MfTOfTzFE9GSNUk8wK%2B5AajYtId7Z5pyHqgEgOKcUYODe0eQ2SfRXm4oWxjHwOCYIluJ8b8J7sWsDhHccubjkEyKtIO3Tp2S0kyMXr%2Fmbo%2BRBvz31QIIgTvU%2Fd89TZ%2FWnlZqBgy3O%2B7upNk5nR%2BmVgV7sCbU6Kdi9ojag5o37%2BtpY%2FFf%2B1fuQ7S0KWSijIgsuSlvvL6gah8mVFnfk7p%2FYeHrC9NxRCmRbwOHBbq%2FrYwLZeCqcEz%2Bvie5BC4Ii2r5df1t3sJ5lyy4T7%2BUWX%2FunWXfcLkXaVbCLiKNTec18w66Fn%2FM4dXIPgklvgHmtBcDUS6D4OMtFljdmqgpZDUly7mCX36%2FfTdJTsMM5k1iGQTHXe4hQJiTajv4QlN%2FNGSGsWFYHtHXsJFpdIsQpxldNYXZzBiOHW4E19Pmv6ILr1HipLWuBIGmLpIL5HQ9aQlzeV538DV55WE6gv8JIllluAzR0CVvx1AeLxz2RP5YSK0JX2xXI%2F8YhFqTjTdAFQMH2RM6Eom26Jmr7%2BFdJMMEw6mXKE2RYJKK9MqnOrH%2F8qZ1gwRHXe4xHld%2BN2UwoDH8HO8UyOT8Y623TTeSY%2FLqsMeyIHYDOq5d%2FkCQy6FoTRQEff9JCKuJ0d3MMDO98kGOqUBmRy90mBp5MIlBAvfDN696%2Ft%2BY6r%2FkGdLKLu4rbAXALRPof0u6GxTcdEtViOI%2F2azu0BYt8UyOZWQPGbfAy1p3Sujj0KaGEnAIVbSeXL0uL1xdMyAziOdenoWwCoHG%2FAVQEimKMX87HeLiwH3Vf%2BZxiqgrZX6i20LItWp8rhDRsyM908%2BXXyNV6aU9udMHSQWnEXzpHnTcr9l9vAFhYQ2E4So8TBS&X-Amz-Signature=5855698b8c9856c99e3e5dd00924680a2804a705482807a61b2de989ffc6ba7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
A clear Correlation exists between Goals and Assists. True or False?

<details>
<summary>Solution</summary>

False
</details>
---

