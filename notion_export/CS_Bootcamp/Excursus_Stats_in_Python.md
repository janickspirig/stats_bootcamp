---
title: "Excursus: Stats in Python"
notion_id: "0443da65-47e4-4f5b-aad9-c9f8e68d5723"
notion_url: "https://www.notion.so/Excursus-Stats-in-Python-0443da6547e44f5baad9c9f8e68d5723"
exported_at: "2025-12-13T22:26:44.953143+00:00"
---

# Excursus: Stats in Python

[TOC]
# Motivation
After loading, manipulating and visualising data in DataFrames we may want to draw scientifically based conclusions from the data. For this purpose, various packages exist that provide functions to perform statistical tests. Below we are going to cover the most important statistical tests and how we can conduct them. 
# T-test
A t-test allows us to determine if there is a significant difference between the means of two groups.
## [One sample](https://datatab.net/tutorial/one-sample-t-test)
**Is there a difference between a group and the population?**
This is the most basic scenario of a t-test in which we compare the mean in a sample with a fixed value such as a population mean, target quality standard etc.
Let’s assume a new teaching method has been introduced at university. Before the average test score was always at 28. Now, we are interested if the new teaching method improved the average test score of the students. As data we have available the most recent test scores of 12 students.
![df_scores](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/10424780-e86a-47fb-b5d3-cc1b655c93a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQIZLQN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDfApEE%2BsG7CIJrjzYN4LMGF9k2cyaYVxAKgoHaK5m81QIgd64tuioz81SFl8B8RXOl9%2BZZ6pQW0VtMVGo1Hnz%2FWIIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWoZiLipVErw%2BUOZCrcAwFH2%2FPC5eIdeqMrSQet3SPPRuJtAOM0RarFCdErAU9aKAa7qMkDM8SmgE4hEaoYrCNh738szrvmbQwEBc1TsDGMa9ZOkVXMElHHZXk9zwedEuWEYxb1bRRo3BJLP9GuXQQfoQXHV4eEqssQVbuCZ2G%2BLwky%2F48XH70%2Bq%2FQ7UI3iCoA40e6lyndw2FxyOjUtD4YhDRy%2BxJH4uUq5TopzIVazXsK0FaR1pMN3iRg%2BpJZx21krxDIGEoGTIwj0kgW0WbXtdQCe2E2hZhhl0OZgeXoxQ6VC6qVLwpnub7mEbTaZ4IaRndIblvP9CpzLzESQxhfIwmnblDAcyBCqWYEUqKoLMMUXZjb8XE9WWTUakPd6b3FVnSq4rxYybhdV4dy0fLX5vTFL%2BpxlIxzcq6FacL9NkqAfxML8jtQYGa2HU5%2BtgU%2FDKpdabAd99cIxZgYMIPSVXwr8CiXdV9iQzB1Bcq%2B9y8Z2o1LkzffmjwzYNBK4%2BWPGHOjUjmukqUeiwTENEt%2Fb4Z0cH%2B%2BuuHXws%2BibP%2B4igjiVc4OEvK0GBb5wvM0sCaqejtsowQdIHzinv2FWJQZH%2FZrB3yv7JigtqrGvQZ1bUpIkrQl9e%2Fbu9U62VaFAPyQsj213yzrwRYceMNLO98kGOqUBdpLzA5CTlb8rqQGRoIlwtYzT%2BZPDGuwcQ3o7T7aFhMVx8fqVajSWtgwOWiQwpV4hxyYtGTwNs3S974zQvRhWnRKFseMOQY5%2BnmXEVEl1zPsFOqGv3X7KBF6hDUVG95B73EnOoaBz9%2FMdVNtoCOYtBv0BSabwhUVdj5fwm%2FuvCtmQKw%2BjJ0I5d0s6fA8ylsOP7aSsOqFITVR8ehl0OJHXUHMmvtqm&X-Amz-Signature=db9acd45fb3774f937fb6f4530a3af72e33bfb4c7f0d0e275ef54cc7ef801498&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now perform a one sample t-test using the [`.ttest_1samp()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html#scipy.stats.ttest_1samp) method from the scipy package. The method has the following syntax:
**`.ttest_1samp(a, popmean, alternative='two-sided')`**
`a` → an array-like object such as a column in a Data Frame
`popmean` → fixed value against which we want to compare the sample mean
`alternative=` → can be `'two-sided'` `'less'` or `'greater'`
We can now run our t-test with the following command:
```python
import scipy.stats as sp

sp.ttest_1samp(df_scores['Score'], 28, alternative='greater')

# output
Ttest_1sampResult(statistic=array([2.74619412]), pvalue=array([0.00950982]))
```
We see that as a return value we get the test-statistics as well as the p-value. Because the p-value is smaller than 5% (0.05) we can reject the Null Hypothesis of equal values between population and sample. Thus, we can infer that the test score of the students has significantly improved through the new teaching method.
We set `alternative='greater'` because we wanted to perform a one-sided t-test since we are not interested in whether the average score has decrease but only whether it has improved.
---
## [Unpaired t-test (independent samples)](https://datatab.net/tutorial/unpaired-t-test)
**Is there a difference between two groups?**
In many scenarios we conduct an experiment with two groups in which we treat the two groups differently but simultaneously observe a dependent variable. After the experiment we now want to know whether the dependent variable differs between the two groups. To check this, we can use an unpaired t-test.
Let’s assume we perform an experiment in which we examine the effect of a drug on weight loss. To do so, we gave one group  the drug and another group the placebo. Now we measured over one year / twelve months how much weight the two groups have lost on average each month.
![df_weight](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0104ab85-c525-47a0-bd62-356194eb1be1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQIZLQN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDfApEE%2BsG7CIJrjzYN4LMGF9k2cyaYVxAKgoHaK5m81QIgd64tuioz81SFl8B8RXOl9%2BZZ6pQW0VtMVGo1Hnz%2FWIIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWoZiLipVErw%2BUOZCrcAwFH2%2FPC5eIdeqMrSQet3SPPRuJtAOM0RarFCdErAU9aKAa7qMkDM8SmgE4hEaoYrCNh738szrvmbQwEBc1TsDGMa9ZOkVXMElHHZXk9zwedEuWEYxb1bRRo3BJLP9GuXQQfoQXHV4eEqssQVbuCZ2G%2BLwky%2F48XH70%2Bq%2FQ7UI3iCoA40e6lyndw2FxyOjUtD4YhDRy%2BxJH4uUq5TopzIVazXsK0FaR1pMN3iRg%2BpJZx21krxDIGEoGTIwj0kgW0WbXtdQCe2E2hZhhl0OZgeXoxQ6VC6qVLwpnub7mEbTaZ4IaRndIblvP9CpzLzESQxhfIwmnblDAcyBCqWYEUqKoLMMUXZjb8XE9WWTUakPd6b3FVnSq4rxYybhdV4dy0fLX5vTFL%2BpxlIxzcq6FacL9NkqAfxML8jtQYGa2HU5%2BtgU%2FDKpdabAd99cIxZgYMIPSVXwr8CiXdV9iQzB1Bcq%2B9y8Z2o1LkzffmjwzYNBK4%2BWPGHOjUjmukqUeiwTENEt%2Fb4Z0cH%2B%2BuuHXws%2BibP%2B4igjiVc4OEvK0GBb5wvM0sCaqejtsowQdIHzinv2FWJQZH%2FZrB3yv7JigtqrGvQZ1bUpIkrQl9e%2Fbu9U62VaFAPyQsj213yzrwRYceMNLO98kGOqUBdpLzA5CTlb8rqQGRoIlwtYzT%2BZPDGuwcQ3o7T7aFhMVx8fqVajSWtgwOWiQwpV4hxyYtGTwNs3S974zQvRhWnRKFseMOQY5%2BnmXEVEl1zPsFOqGv3X7KBF6hDUVG95B73EnOoaBz9%2FMdVNtoCOYtBv0BSabwhUVdj5fwm%2FuvCtmQKw%2BjJ0I5d0s6fA8ylsOP7aSsOqFITVR8ehl0OJHXUHMmvtqm&X-Amz-Signature=48e027927ddf61f5db794db87d2da167911c6b773b2823960213ff53fcbefd9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now perform an unpaired t-test using the [`.ttest_ind()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html#scipy.stats.ttest_1samp) method from the scipy package. The method has the following syntax:
**`scipy.stats.ttest_ind(a, b, equal_var=True, alternative='two-sided')`**
`a` → an array-like object that contains the observed values of the first group
`b` → an array-like object that contains the observed values of the second group
`equal_var` → defines whether equal variances in the two populations are assumed, if this parameter is set to False, then a [Welch’s t-test](https://www.statology.org/welchs-t-test/) is performed
`alternative=` → can be `'two-sided'` `'less'` or `'greater'`
We can now run our t-test with the following command:
```python
import scipy.stats as sp

sp.ttest_ind(df_weight['Drug'], df_weight['Placebo'], alternative='greater')

# output
Ttest_indResult(statistic=-1.3585424483219573, pvalue=0.9059701436136729)
```
Because the p-value is not smaller than 5% (0.05) we can not reject the Null Hypothesis of equal population means. Thus, we cannot infer that the drug has lead to significant more weight-loss.
We set `alternative='greater'` because we wanted to check whether the drug leads to higher weight-loss, i.e., a higher average value of weight-loss of the drug group compared to the placebo group.
---
## [Paired t-test (dependent samples)](https://datatab.net/tutorial/paired-t-test)
**Is there a difference in a group between two points in time?**
Often we form only one group for an experiment which we then observe over time. During this time we treat the participants in a certain way and observe a dependent variable before and after the treatment. We now want to know whether the observed dependent variable has significantly changed amongst the participants.
Let’s assume we want to find out how summer holidays affect the students fitness level. Therefore, we conducted a fitness test with 10 students before and after the holidays. In this test the students can achieve a maximum score of 100.
![df_fitness](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/53b12b22-7589-436e-8cfa-d00320c8478e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQIZLQN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDfApEE%2BsG7CIJrjzYN4LMGF9k2cyaYVxAKgoHaK5m81QIgd64tuioz81SFl8B8RXOl9%2BZZ6pQW0VtMVGo1Hnz%2FWIIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWoZiLipVErw%2BUOZCrcAwFH2%2FPC5eIdeqMrSQet3SPPRuJtAOM0RarFCdErAU9aKAa7qMkDM8SmgE4hEaoYrCNh738szrvmbQwEBc1TsDGMa9ZOkVXMElHHZXk9zwedEuWEYxb1bRRo3BJLP9GuXQQfoQXHV4eEqssQVbuCZ2G%2BLwky%2F48XH70%2Bq%2FQ7UI3iCoA40e6lyndw2FxyOjUtD4YhDRy%2BxJH4uUq5TopzIVazXsK0FaR1pMN3iRg%2BpJZx21krxDIGEoGTIwj0kgW0WbXtdQCe2E2hZhhl0OZgeXoxQ6VC6qVLwpnub7mEbTaZ4IaRndIblvP9CpzLzESQxhfIwmnblDAcyBCqWYEUqKoLMMUXZjb8XE9WWTUakPd6b3FVnSq4rxYybhdV4dy0fLX5vTFL%2BpxlIxzcq6FacL9NkqAfxML8jtQYGa2HU5%2BtgU%2FDKpdabAd99cIxZgYMIPSVXwr8CiXdV9iQzB1Bcq%2B9y8Z2o1LkzffmjwzYNBK4%2BWPGHOjUjmukqUeiwTENEt%2Fb4Z0cH%2B%2BuuHXws%2BibP%2B4igjiVc4OEvK0GBb5wvM0sCaqejtsowQdIHzinv2FWJQZH%2FZrB3yv7JigtqrGvQZ1bUpIkrQl9e%2Fbu9U62VaFAPyQsj213yzrwRYceMNLO98kGOqUBdpLzA5CTlb8rqQGRoIlwtYzT%2BZPDGuwcQ3o7T7aFhMVx8fqVajSWtgwOWiQwpV4hxyYtGTwNs3S974zQvRhWnRKFseMOQY5%2BnmXEVEl1zPsFOqGv3X7KBF6hDUVG95B73EnOoaBz9%2FMdVNtoCOYtBv0BSabwhUVdj5fwm%2FuvCtmQKw%2BjJ0I5d0s6fA8ylsOP7aSsOqFITVR8ehl0OJHXUHMmvtqm&X-Amz-Signature=f186382603d892cdf9fa13c57e5fc98bec223f16598adab74c34722da5116fd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now perform a paired t-test using the [`.ttest_rel()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html#scipy.stats.ttest_rel) method from the scipy package. The method has the following syntax:
**`scipy.stats.ttest_rel(a, b, alternative='two-sided')`**
`a` → an array-like object that contains the values of the first measurement
`b` → an array-like object that contains the values of the second measurement
`alternative=` → can be `'two-sided'` `'less'` or `'greater'`
We can now run our t-test with the following command:
```python
import scipy.stats as sp

sp.ttest_rel(df_fitness['Before Holidays'], df_fitness['After Holidays'])

# output
Ttest_relResult(statistic=4.512097436177516, pvalue=0.001463296096476316)
```
Because the p-value is smaller than 5% (0.05) we can reject the Null Hypothesis of equal population means. Thus, we can infer that the holidays affected the students fitness level significantly.
In this example we did not specify the `alternative=` parameter. Thus the default value `'two-sided'` was used as we wanted to check if there was an effect on the fitness level in general. When looking at the data closely though we can observe that the fitness level of the students has gone down during the holidays.
---
# ANOVA
**An**alysis **O**f **Va**riance allows us to determine if significant differences exist between more than two groups. So whenever we have more than two groups that we want to analyse, we cannot use a t-test anymore and must use ANOVA instead.
## [One-factorial ANOVA](/d544437a1f244245887e218737eba36d)
**Are there significant differences between more than two independent samples?**
This is the extension of the [unpaired t-test](/d544437a1f244245887e218737eba36d#0cfd550dc8bc4156b4da44515713b78a) with the difference that we are comparing now more than two groups.
Let’s assume we want to improve the student fitness level after their holidays again and therefore launch three different therapies. 1️⃣ One-time personal discussion on how to intensify training, 2️⃣ Development of individual meal plan and 3️⃣ Presence of a personal coach during training. 10 students get assigned to each therapy. After 6 months of therapy we want to check whether the effect on the fitness level differs amongst the three therapies. Thus, all 30 students participated in a fitness test in which they could reach a maximum score of 100.
![df_fitness](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2cefe169-264e-48c5-a579-ea48af186ff3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQIZLQN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDfApEE%2BsG7CIJrjzYN4LMGF9k2cyaYVxAKgoHaK5m81QIgd64tuioz81SFl8B8RXOl9%2BZZ6pQW0VtMVGo1Hnz%2FWIIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWoZiLipVErw%2BUOZCrcAwFH2%2FPC5eIdeqMrSQet3SPPRuJtAOM0RarFCdErAU9aKAa7qMkDM8SmgE4hEaoYrCNh738szrvmbQwEBc1TsDGMa9ZOkVXMElHHZXk9zwedEuWEYxb1bRRo3BJLP9GuXQQfoQXHV4eEqssQVbuCZ2G%2BLwky%2F48XH70%2Bq%2FQ7UI3iCoA40e6lyndw2FxyOjUtD4YhDRy%2BxJH4uUq5TopzIVazXsK0FaR1pMN3iRg%2BpJZx21krxDIGEoGTIwj0kgW0WbXtdQCe2E2hZhhl0OZgeXoxQ6VC6qVLwpnub7mEbTaZ4IaRndIblvP9CpzLzESQxhfIwmnblDAcyBCqWYEUqKoLMMUXZjb8XE9WWTUakPd6b3FVnSq4rxYybhdV4dy0fLX5vTFL%2BpxlIxzcq6FacL9NkqAfxML8jtQYGa2HU5%2BtgU%2FDKpdabAd99cIxZgYMIPSVXwr8CiXdV9iQzB1Bcq%2B9y8Z2o1LkzffmjwzYNBK4%2BWPGHOjUjmukqUeiwTENEt%2Fb4Z0cH%2B%2BuuHXws%2BibP%2B4igjiVc4OEvK0GBb5wvM0sCaqejtsowQdIHzinv2FWJQZH%2FZrB3yv7JigtqrGvQZ1bUpIkrQl9e%2Fbu9U62VaFAPyQsj213yzrwRYceMNLO98kGOqUBdpLzA5CTlb8rqQGRoIlwtYzT%2BZPDGuwcQ3o7T7aFhMVx8fqVajSWtgwOWiQwpV4hxyYtGTwNs3S974zQvRhWnRKFseMOQY5%2BnmXEVEl1zPsFOqGv3X7KBF6hDUVG95B73EnOoaBz9%2FMdVNtoCOYtBv0BSabwhUVdj5fwm%2FuvCtmQKw%2BjJ0I5d0s6fA8ylsOP7aSsOqFITVR8ehl0OJHXUHMmvtqm&X-Amz-Signature=a78c781a5c65baae3162159745f962e7863bf71db5e88b74faaf86ee23ac5f54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now perform a one-factorial ANOVA using the [`.f_oneway()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html#scipy.stats.f_oneway) method from the scipy package. The method has the following syntax:
**`scipy.stats.f_oneway(sample1, sample2, sample3, sample n)`**
We see that we must just include all the values from the different groups.
We can now run our ANOVA test with the following command:
```python
import scipy.stats as sp

sp.f_oneway(df_fitness['Discussion'], df_fitness['Meal plan'], df_fitness['Personal coach'])

# output
F_onewayResult(statistic=7.617283473692342, pvalue=0.0023817282171092577)
```
Because the p-value is smaller than 5% (0.05) we can reject the Null Hypothesis of equal variances amongst the groups. Thus, we can infer that a significant difference in fitness level exist amongst the different types of therapies.
If we visualise the average fitness level per therapy, it becomes obvious why we can reject the Null hypothesis, i.e., that significant differences exist.
![Shows that students that got assigned a personal coach have the highest fitness level.](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/23240cd9-a1a6-421f-95be-51d8f9fc5c21/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQIZLQN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDfApEE%2BsG7CIJrjzYN4LMGF9k2cyaYVxAKgoHaK5m81QIgd64tuioz81SFl8B8RXOl9%2BZZ6pQW0VtMVGo1Hnz%2FWIIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWoZiLipVErw%2BUOZCrcAwFH2%2FPC5eIdeqMrSQet3SPPRuJtAOM0RarFCdErAU9aKAa7qMkDM8SmgE4hEaoYrCNh738szrvmbQwEBc1TsDGMa9ZOkVXMElHHZXk9zwedEuWEYxb1bRRo3BJLP9GuXQQfoQXHV4eEqssQVbuCZ2G%2BLwky%2F48XH70%2Bq%2FQ7UI3iCoA40e6lyndw2FxyOjUtD4YhDRy%2BxJH4uUq5TopzIVazXsK0FaR1pMN3iRg%2BpJZx21krxDIGEoGTIwj0kgW0WbXtdQCe2E2hZhhl0OZgeXoxQ6VC6qVLwpnub7mEbTaZ4IaRndIblvP9CpzLzESQxhfIwmnblDAcyBCqWYEUqKoLMMUXZjb8XE9WWTUakPd6b3FVnSq4rxYybhdV4dy0fLX5vTFL%2BpxlIxzcq6FacL9NkqAfxML8jtQYGa2HU5%2BtgU%2FDKpdabAd99cIxZgYMIPSVXwr8CiXdV9iQzB1Bcq%2B9y8Z2o1LkzffmjwzYNBK4%2BWPGHOjUjmukqUeiwTENEt%2Fb4Z0cH%2B%2BuuHXws%2BibP%2B4igjiVc4OEvK0GBb5wvM0sCaqejtsowQdIHzinv2FWJQZH%2FZrB3yv7JigtqrGvQZ1bUpIkrQl9e%2Fbu9U62VaFAPyQsj213yzrwRYceMNLO98kGOqUBdpLzA5CTlb8rqQGRoIlwtYzT%2BZPDGuwcQ3o7T7aFhMVx8fqVajSWtgwOWiQwpV4hxyYtGTwNs3S974zQvRhWnRKFseMOQY5%2BnmXEVEl1zPsFOqGv3X7KBF6hDUVG95B73EnOoaBz9%2FMdVNtoCOYtBv0BSabwhUVdj5fwm%2FuvCtmQKw%2BjJ0I5d0s6fA8ylsOP7aSsOqFITVR8ehl0OJHXUHMmvtqm&X-Amz-Signature=57192bd55ba02662b1420e388de3d0c2f0e4232d1eb2e72da4a49b697b5963ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [Repeated Measures ANOVA](https://datatab.net/tutorial/anova-with-repeated-measures)
**Are there significant differences between more than two dependent samples?**
This is the extension of the [paired t-test](/d544437a1f244245887e218737eba36d#5f34acf8a82a49869b43afc973cf8ed1) with the difference that we are comparing now more than two groups.
Let’s assume that 10 patients with a slipped disk were reported. Now we want to examine if the therapy for slipped disk leads to a difference in pain perception over time. For this reason we measure the pain perception of the 10 patients at three different points in time: Before the therapy, in the middle of the therapy and after the therapy. Thus, in total we have 30 measurement values.
![df_pain](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/193a2e6c-0d3e-4c4c-bed5-20567d751dbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQIZLQN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDfApEE%2BsG7CIJrjzYN4LMGF9k2cyaYVxAKgoHaK5m81QIgd64tuioz81SFl8B8RXOl9%2BZZ6pQW0VtMVGo1Hnz%2FWIIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWoZiLipVErw%2BUOZCrcAwFH2%2FPC5eIdeqMrSQet3SPPRuJtAOM0RarFCdErAU9aKAa7qMkDM8SmgE4hEaoYrCNh738szrvmbQwEBc1TsDGMa9ZOkVXMElHHZXk9zwedEuWEYxb1bRRo3BJLP9GuXQQfoQXHV4eEqssQVbuCZ2G%2BLwky%2F48XH70%2Bq%2FQ7UI3iCoA40e6lyndw2FxyOjUtD4YhDRy%2BxJH4uUq5TopzIVazXsK0FaR1pMN3iRg%2BpJZx21krxDIGEoGTIwj0kgW0WbXtdQCe2E2hZhhl0OZgeXoxQ6VC6qVLwpnub7mEbTaZ4IaRndIblvP9CpzLzESQxhfIwmnblDAcyBCqWYEUqKoLMMUXZjb8XE9WWTUakPd6b3FVnSq4rxYybhdV4dy0fLX5vTFL%2BpxlIxzcq6FacL9NkqAfxML8jtQYGa2HU5%2BtgU%2FDKpdabAd99cIxZgYMIPSVXwr8CiXdV9iQzB1Bcq%2B9y8Z2o1LkzffmjwzYNBK4%2BWPGHOjUjmukqUeiwTENEt%2Fb4Z0cH%2B%2BuuHXws%2BibP%2B4igjiVc4OEvK0GBb5wvM0sCaqejtsowQdIHzinv2FWJQZH%2FZrB3yv7JigtqrGvQZ1bUpIkrQl9e%2Fbu9U62VaFAPyQsj213yzrwRYceMNLO98kGOqUBdpLzA5CTlb8rqQGRoIlwtYzT%2BZPDGuwcQ3o7T7aFhMVx8fqVajSWtgwOWiQwpV4hxyYtGTwNs3S974zQvRhWnRKFseMOQY5%2BnmXEVEl1zPsFOqGv3X7KBF6hDUVG95B73EnOoaBz9%2FMdVNtoCOYtBv0BSabwhUVdj5fwm%2FuvCtmQKw%2BjJ0I5d0s6fA8ylsOP7aSsOqFITVR8ehl0OJHXUHMmvtqm&X-Amz-Signature=d8a54ef4ff2f1dbf1b5baa3b7849c54e2faf54be1f2ee6cae79603d5ca803fa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now perform a Repeated Measures ANOVA using the [`AnovaRM()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.AnovaRM.html#generated-statsmodels-stats-anova-anovarm--page-root) method from the statsmodel package. The method has the following syntax:
**`statsmodels.stats.anova.AnovaRM(data, depvar, subject, within=None)`**
`data` → the DataFrame that contains all the measured data
`depvar` → the dependent variable that we are interested in
`subject` → the subjects for which multiple measurements of the dependent variable exist 
`within` → within-subject factors 
We can now run our ANOVA test with the following command:
```python
from statsmodels.stats.anova import AnovaRM

print(
	AnovaRM(
		data=df_pain,
		depvar='Pain perception',
		subject='Patient',
		within=['Measurement']
	).fit()
)
```
**Output**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5845c4ed-36d9-4229-aef2-c484be2e23b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQIZLQN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDfApEE%2BsG7CIJrjzYN4LMGF9k2cyaYVxAKgoHaK5m81QIgd64tuioz81SFl8B8RXOl9%2BZZ6pQW0VtMVGo1Hnz%2FWIIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWoZiLipVErw%2BUOZCrcAwFH2%2FPC5eIdeqMrSQet3SPPRuJtAOM0RarFCdErAU9aKAa7qMkDM8SmgE4hEaoYrCNh738szrvmbQwEBc1TsDGMa9ZOkVXMElHHZXk9zwedEuWEYxb1bRRo3BJLP9GuXQQfoQXHV4eEqssQVbuCZ2G%2BLwky%2F48XH70%2Bq%2FQ7UI3iCoA40e6lyndw2FxyOjUtD4YhDRy%2BxJH4uUq5TopzIVazXsK0FaR1pMN3iRg%2BpJZx21krxDIGEoGTIwj0kgW0WbXtdQCe2E2hZhhl0OZgeXoxQ6VC6qVLwpnub7mEbTaZ4IaRndIblvP9CpzLzESQxhfIwmnblDAcyBCqWYEUqKoLMMUXZjb8XE9WWTUakPd6b3FVnSq4rxYybhdV4dy0fLX5vTFL%2BpxlIxzcq6FacL9NkqAfxML8jtQYGa2HU5%2BtgU%2FDKpdabAd99cIxZgYMIPSVXwr8CiXdV9iQzB1Bcq%2B9y8Z2o1LkzffmjwzYNBK4%2BWPGHOjUjmukqUeiwTENEt%2Fb4Z0cH%2B%2BuuHXws%2BibP%2B4igjiVc4OEvK0GBb5wvM0sCaqejtsowQdIHzinv2FWJQZH%2FZrB3yv7JigtqrGvQZ1bUpIkrQl9e%2Fbu9U62VaFAPyQsj213yzrwRYceMNLO98kGOqUBdpLzA5CTlb8rqQGRoIlwtYzT%2BZPDGuwcQ3o7T7aFhMVx8fqVajSWtgwOWiQwpV4hxyYtGTwNs3S974zQvRhWnRKFseMOQY5%2BnmXEVEl1zPsFOqGv3X7KBF6hDUVG95B73EnOoaBz9%2FMdVNtoCOYtBv0BSabwhUVdj5fwm%2FuvCtmQKw%2BjJ0I5d0s6fA8ylsOP7aSsOqFITVR8ehl0OJHXUHMmvtqm&X-Amz-Signature=bf07f373146bad54e0fdd20ecf54c2a138e860150f9ce721fb841d3eaad01497&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Because the p-value (0.5224) is not smaller than 5% (0.05) we cannot reject the Null Hypothesis of equal variances. Thus, we cannot infer that over time the therapy leads to significant differences in pain perception.
---
Let’s assume that we have 4 drugs that were given to 5 patients which supposedly lead to different reaction times. We therefore conducted an experiment in which the reaction time after having taken each of the drug was tested. Thus, we have 20 measurements in total.
![df_drugs](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0c611430-98a3-4933-b29b-ff356bae854c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQIZLQN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDfApEE%2BsG7CIJrjzYN4LMGF9k2cyaYVxAKgoHaK5m81QIgd64tuioz81SFl8B8RXOl9%2BZZ6pQW0VtMVGo1Hnz%2FWIIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWoZiLipVErw%2BUOZCrcAwFH2%2FPC5eIdeqMrSQet3SPPRuJtAOM0RarFCdErAU9aKAa7qMkDM8SmgE4hEaoYrCNh738szrvmbQwEBc1TsDGMa9ZOkVXMElHHZXk9zwedEuWEYxb1bRRo3BJLP9GuXQQfoQXHV4eEqssQVbuCZ2G%2BLwky%2F48XH70%2Bq%2FQ7UI3iCoA40e6lyndw2FxyOjUtD4YhDRy%2BxJH4uUq5TopzIVazXsK0FaR1pMN3iRg%2BpJZx21krxDIGEoGTIwj0kgW0WbXtdQCe2E2hZhhl0OZgeXoxQ6VC6qVLwpnub7mEbTaZ4IaRndIblvP9CpzLzESQxhfIwmnblDAcyBCqWYEUqKoLMMUXZjb8XE9WWTUakPd6b3FVnSq4rxYybhdV4dy0fLX5vTFL%2BpxlIxzcq6FacL9NkqAfxML8jtQYGa2HU5%2BtgU%2FDKpdabAd99cIxZgYMIPSVXwr8CiXdV9iQzB1Bcq%2B9y8Z2o1LkzffmjwzYNBK4%2BWPGHOjUjmukqUeiwTENEt%2Fb4Z0cH%2B%2BuuHXws%2BibP%2B4igjiVc4OEvK0GBb5wvM0sCaqejtsowQdIHzinv2FWJQZH%2FZrB3yv7JigtqrGvQZ1bUpIkrQl9e%2Fbu9U62VaFAPyQsj213yzrwRYceMNLO98kGOqUBdpLzA5CTlb8rqQGRoIlwtYzT%2BZPDGuwcQ3o7T7aFhMVx8fqVajSWtgwOWiQwpV4hxyYtGTwNs3S974zQvRhWnRKFseMOQY5%2BnmXEVEl1zPsFOqGv3X7KBF6hDUVG95B73EnOoaBz9%2FMdVNtoCOYtBv0BSabwhUVdj5fwm%2FuvCtmQKw%2BjJ0I5d0s6fA8ylsOP7aSsOqFITVR8ehl0OJHXUHMmvtqm&X-Amz-Signature=df286282dabf679199e57effa28ba360a6ee590806396db627efba259039e33c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now again perform a Repeated Measures ANOVA using the [`AnovaRM()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.AnovaRM.html#generated-statsmodels-stats-anova-anovarm--page-root) method from the statsmodel package.
```python
from statsmodels.stats.anova import AnovaRM

print(
	AnovaRM(
		data=df_drugs,
		depvar='response',
		subject='Patient',
		within=['drug']
	).fit()
)
```
**Output**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cdee0534-362e-40c5-9676-8d530905350f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQIZLQN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDfApEE%2BsG7CIJrjzYN4LMGF9k2cyaYVxAKgoHaK5m81QIgd64tuioz81SFl8B8RXOl9%2BZZ6pQW0VtMVGo1Hnz%2FWIIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJWoZiLipVErw%2BUOZCrcAwFH2%2FPC5eIdeqMrSQet3SPPRuJtAOM0RarFCdErAU9aKAa7qMkDM8SmgE4hEaoYrCNh738szrvmbQwEBc1TsDGMa9ZOkVXMElHHZXk9zwedEuWEYxb1bRRo3BJLP9GuXQQfoQXHV4eEqssQVbuCZ2G%2BLwky%2F48XH70%2Bq%2FQ7UI3iCoA40e6lyndw2FxyOjUtD4YhDRy%2BxJH4uUq5TopzIVazXsK0FaR1pMN3iRg%2BpJZx21krxDIGEoGTIwj0kgW0WbXtdQCe2E2hZhhl0OZgeXoxQ6VC6qVLwpnub7mEbTaZ4IaRndIblvP9CpzLzESQxhfIwmnblDAcyBCqWYEUqKoLMMUXZjb8XE9WWTUakPd6b3FVnSq4rxYybhdV4dy0fLX5vTFL%2BpxlIxzcq6FacL9NkqAfxML8jtQYGa2HU5%2BtgU%2FDKpdabAd99cIxZgYMIPSVXwr8CiXdV9iQzB1Bcq%2B9y8Z2o1LkzffmjwzYNBK4%2BWPGHOjUjmukqUeiwTENEt%2Fb4Z0cH%2B%2BuuHXws%2BibP%2B4igjiVc4OEvK0GBb5wvM0sCaqejtsowQdIHzinv2FWJQZH%2FZrB3yv7JigtqrGvQZ1bUpIkrQl9e%2Fbu9U62VaFAPyQsj213yzrwRYceMNLO98kGOqUBdpLzA5CTlb8rqQGRoIlwtYzT%2BZPDGuwcQ3o7T7aFhMVx8fqVajSWtgwOWiQwpV4hxyYtGTwNs3S974zQvRhWnRKFseMOQY5%2BnmXEVEl1zPsFOqGv3X7KBF6hDUVG95B73EnOoaBz9%2FMdVNtoCOYtBv0BSabwhUVdj5fwm%2FuvCtmQKw%2BjJ0I5d0s6fA8ylsOP7aSsOqFITVR8ehl0OJHXUHMmvtqm&X-Amz-Signature=57ba68915a82c5b45bac6fdef37b4cf5493694282ab7f177b5ee1a8d979962b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Because the p-value (0.0) is not smaller than 5% (0.05) we can reject the Null Hypothesis of equal variances. Thus, we can infer that the type of drug used leads to significant differences in response time.
---
