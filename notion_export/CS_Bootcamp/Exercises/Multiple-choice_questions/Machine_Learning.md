---
title: "Machine Learning"
notion_id: "06366e57-5d79-4b37-8560-3409f5d49b77"
notion_url: "https://www.notion.so/Machine-Learning-06366e575d794b3785603409f5d49b77"
exported_at: "2025-12-13T22:54:45.029549+00:00"
---

# Machine Learning

---
**Machine Learning**
When I have categorial data we usually deal with a Regression problem and when we have numerical data we usually deal with a Classification problem. True or False?

<details>
<summary>Solution</summary>

False
When we have categorial data we mostly apply classification algorithms as we want to put things into categories and when we have numerical data we want to predict something numeric and thus we can use Regression.
</details>
---
**Machine Learning**
In supervised learning we have labelled data available while in unsupervised learning we don’t have the labels available and thus often apply clustering algorithms to get first insights about data. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**k-Nearest-Neighbour**
We have collected 1521 samples of flowers. Now we receive a new flower that we want to classify. To calculate the euclidean distance it takes 0.02 seconds. To initialize the model it takes another 0.8 seconds. A model initialization is required before the whole classification process of a flower can be started. How many flowers can our model classify in one day?

<details>
<summary>Solution</summary>

2767 flowers
To calculate 1521 distances, the model requires 30.42 seconds (1521 samples * 0.02 seconds). On top of that comes 0.8 seconds for model initialisation. 30.42 + 0.8 = 31.22 seconds to classify one flower
A days has 24 * 60 * 60 = 86’400 seconds.
Thus in one day we can classify 86’400 / 31.22 = 2767.45 flowers → round down → 2767 flowers
</details>
---
**k-nearest-Neighbour**
Look at the code snippet below. What is missing at ############# ?
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/84b596ef-d755-48f5-bda8-bcbbeaae8b51/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3LG7LVS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIARfq00%2Fcaa2611TOOpnemuHgv21Rj3gbQkUA9BubfygAiEAkDKsAjjVKsMy1ZCl1uEOSrXGXXzHGjfjT%2BIeG1bJwT0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMjQRkOy6vQVdo10GyrcA0WOTI8o9TsLJVCA9YKcON9xWOooyjxvTJeBbWoozc9jcN0Y%2BRPjAZ3%2FztSsLp%2BFfYyGrKM0EUX07uaDOkVfxQje18Dx524bmADre%2BX10K45UAGPcL5bFs0fA49C8%2FnEmPhndatebC6v710IYWF6JFa5Fvi3v8zLiy3WvyNSHpvERO72fpMrDmz0fpnmDb2V1MYl2Jh4JQc1zCHpgqtMBUXME8%2BMiUVopJS9uzbijVKEPL4CiUCPr5xKAen0WHiTK9MUDYKhVkU8eTTIUeHtFwdcUzC2xYkfhXrIEBfLJD%2FPr367bjtxdZyqlq3tDb%2Fge2MyUjIyJ0Xdn5eNUzRxEmqDBDU3oVCTG4K7AuXHJsqGvkDlXIv2XLubPUk7tnshuBggGpQNruMdC9XcUyajz66t7K509sKdmxReT%2Fj3UDXqMuvlfZifngGql3oLOJbJAJnt5u%2FTQKd6HljhfZ1tcHuicbngnAb8eNnPtwBDh3B1VoAy%2Bxug00cxwBjHIocAU9SaKwKbtJAIpGg7WgYCkuGwmTrTy9NgCWRnUgGOi4w2oZR4JvlhsG%2BkdklyCApqxADpLephPn7JTQ6PGJs6zAMd1DyyDzKQ0zKYur23d6%2FNn7UoVYFE5vJkP6nMMOHN98kGOqUB%2FkxmLf1jL0vCWd0LvQGj%2BiHPdGsYmT%2BHwRfm3yJ0uc7iEmudRmxKTnZfW%2BB8bP6PEOXUslcjmirN84JVFUXqorIs93pYedm9R25%2FQC8gupcSYuEsOkcb%2FXYgh8hhcq4vGPYr6eqY6NrdS7Z7WgnjHXQ2fZJuYbROW56vBqh7OJbfYSHfy8%2B2JVQEotvc%2BtkWm8yDtRHlOB%2FSnnNXa4s3RzeVfxIx&X-Amz-Signature=00b57054dfc950b8c6412ae760149585b6af4865519c382e2b302cf616ad83fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Solution</summary>

```python
k_neighbors = [n[1] for n in distances[:k]]
```
We need to select the k closest neighbours in order to perform a majority voting in the next line.

</details>
---
**Macro & Micro Average**
From a model we got the following confusion matrix after having classified  the test dataset which consists of 1000 flowers. 
|  |  | Actual |  |  |
| --- | --- | --- | --- | --- |
|  |  | Setosa | Versicolor | Virginica |
| Predicted | Setosa | 100 | 100 | 50 |
|  | Versicolor | 50 | 200 | 50 |
|  | Virginica | 150 | 250 | 50 |
- What is the Precision of the model for Setosa?
- What is the Recall of the model for Versicolor?
- What is the F1 score of the model for Virginica?
- What is the Precision and Recall of the overall model when following the Macro Average approach?

<details>
<summary>Solution</summary>

40% → 100/(100+100+50)
36% → 200/(100+200+250)
17% → Recall = 33.33%, Precision = 11.11%
Precision = 39.26%, Recall = 34.34%
</details>
---
**Precision vs. Recall**
If you would need to implement a classifier that is able to predict whether a person is infected with a deadly virus or not, on which performance metric would you focus more: Precision or Recall? Why?

<details>
<summary>Solution</summary>

Recall
We would most likely focus more on Recall, as the cost of misclassification is very high; if we don’t capture a person that is infected with the virus then this person could potentially die. If we send a person to the doctor because the classifier predicts an infection, but it turns out that there is no infection, then this isn’t too bad.
</details>
---
**Precision vs. Recall **
If you would need to implement a classifier that is able to detect spam emails based on the email content and move them to the spam folder automatically, on which performance metric would you focus more: Precision or Recall? Why?

<details>
<summary>Solution</summary>

Precision
We would rather focus on Precision because we when we classify an email as spam we want to be really sure that it actually is spam. Because otherwise the chance that from time to time an important email from our boss lands in the spam folder is much higher. Contrarily, if a spam email lands in the regular inbox the consequences are not very drastic. We can simply delete the email manually. 
</details>
---
**F1 score**
What happens to the F1 score if we optimise towards one of the performance metrics, Precision or Recall?
- [ ] 1) F1 score increases
- [ ] 2) F1 score stays the same
- [ ] 3) F1 score decreases

<details>
<summary>Solution</summary>

3
Let’s assume we optimise towards Recall and set the threshold for positive class very low. As a result we classify many samples as positive and capture almost all samples that actually are positive. However, at the same time the numbers of samples classified as positives that are actually negative (False Positive) goes up as well, which drives Precision down. Consequently F1 score goes down as there is now a bigger difference between Recall and Precision (Recall went up, Precision came down).
</details>
---
**TF-IDF**
If a word appears across many documents in the dataset, what happens to its TF-IDF score?
- [ ] 1) TD-IDF goes down
- [ ] 2) TD-IDF stays the same
- [ ] 3) TD-IDF goes up

<details>
<summary>Solution</summary>

1
The document frequency (the number of documents in which the term appears) is in the denominator of the IDF formula. Thus, IDF decreases and TD stays the same. As we multiply TF with IDF, the TF-IDF score goes down.
</details>
---
**TF-IDF**
If a TF-IDF score of a term is higher than its term frequency its expressiveness has decreased through the TF-IDF transformation. True or False?

<details>
<summary>Solution</summary>

False
If TD-IDF is higher than TF before, its expressiveness has increased and thus has in the classification higher ‘saying’ compared to other terms.
</details>
---
**scikit-learn**
What does the scikit-learn function `.fit_transform()` do for us?
- [ ] 1) It trains a classifier
- [ ] 2) It tests a classifier
- [ ] 3) It does data transformation and is usually applied on the training dataset only
- [ ] 4) It does data transformation and is usually applied on the test dataset only
- [ ] 5) It does data transformation and is usually applied on the training and the test dataset

<details>
<summary>Solution</summary>

1, 3
We use it on the training data, otherwise we would ‘learn’ something from the test data and our model would be biased. When we need to do data transformation only we use `.transform()`
</details>
---
**scikit-learn **
When applying TF-IDF, we apply the `.fit_transform()` method on the training and on the test data set. True or False?

<details>
<summary>Solution</summary>

False
On the training data we apply [`.fit_transform()`](/9e4a78074aea481ca4c75e506d4671c7#16f816916fcc43318154a1b6b6ea38ae) which creates a Sparse Matrix and adjusts the weights according to TF-IDF.
On the test data we apply [`.transform()`](/9e4a78074aea481ca4c75e506d4671c7#3c583c11477d480d89e97c4211ae4d7b) which creates a Sparse Matrix only, to prevent bias.
</details>
---
**scikit-learn**
In which order would you apply the following functions in a machine learning use case? Note: Some functions may not exist at all.
- [ ] 1) `classification_report()`
- [ ] 2) `.fit()`
- [ ] 3) `.ResultReport()`
- [ ] 4) `KNeighborsClassifier(k_neighbors)`
- [ ] 5) `.fit_transform()`
- [ ] 6) `.test()`
- [ ] 7) `.transform()`
- [ ] 8) `.predict()`

<details>
<summary>Solution</summary>

1. `KNeighborsClassifier(k_neighbors)` → Create classifier
1. `.fit_transform()` → Transform training data
1. `.transform()` → Transform test data
1. `.fit()` → Train classifier
1. `.predict()` → make predictions on test data
1. `classification_report()` → Evaluate performance

`.test()` and `.ResultReport()` do not exist
</details>
---
**scikit-learn**
Put the following actions in the order in which we usually perform them when we want to implement a general classifier, which for example predicts an Iris flower’s type.
- Choose classifier
- Load data
- Evaluate classifier
- Sanity check
- Test classifier
- Split dataset
- Train classifier

<details>
<summary>Solution</summary>

1️⃣ Load data
2️⃣ Split dataset
3️⃣ Choose classifier
4️⃣ Train classifier
5️⃣ Test classifier
6️⃣ Evaluate classifier
7️⃣ Sanity check
</details>
---
**scikit-learn**
Put the following actions in the order in which we usually perform them when we want to implement a text classifier, which for example predicts whether a movie review is positive or negative.
- Create sparse matrices and apply TF-IDF
- Split dataset
- Train classifier
- Evaluate classifier
- Sanity check
- Test classifier
- Load data
- Choose classifier

<details>
<summary>Solution</summary>

1️⃣ Load data
2️⃣ Split dataset
3️⃣ Create sparse matrices and apply TF-IDF
4️⃣ Choose classifier
5️⃣ Train classifier
6️⃣ Test classifier
7️⃣ Evaluate classifier
8️⃣ Sanity check
</details>
---
**Overfitting** 
When we train a classifier for too long, the risk of overfitting increases and thus our classifier has high Bias and low Variance. True or False?

<details>
<summary>Solution</summary>

False
The risk does indeed increase when we train the classifier for too long. However, when we have an overfitted model, it has low Bias and high Variance as with every test dataset its performance varies significantly as it is highly tailored towards one specific set of training data.
</details>
---
**Underfitting**
Decide for each metric below whether they are low or high when we have an underfitted model. 
- Bias
- Variance
- Train error
- Test error

<details>
<summary>Solution</summary>

High, Low, High, High
We have high test error because we assume that test data is similar to train data and when we have an underfitted model, our model has not learned anything from the training data.
</details>
---
**Overfitting**
Decide for each metric below whether they are low or high when we have an overfitted model. 
- Bias
- Variance
- Train error
- Test error

<details>
<summary>Solution</summary>

Low, High, Low, High
Now we have low training error and high test error because the model is now highly specialised on the training data.
</details>
---
**k-Fold Cross Validation**
Order the actions below into the right sequence, i.e., how they are usually executed when doing k-Fold Cross Validation
- [ ] 1) Think about Hyperparameter tuning
- [ ] 2) Divide data into k-folds
- [ ] 3) Average performance metrics
- [ ] 4) Think about how input data could be improved
- [ ] 5) Run train / test runs

<details>
<summary>Solution</summary>

2, 5, 3, 1 & 4 (simultaneously)

</details>
---
**Hyperparameters**
A Hyperparameter distinguishes itself from a Parameter that it is not provided during the creation of a classifier as they can be learned from the model. True or False?

<details>
<summary>Solution</summary>

False
Hyperparameters must be provided when creating the model. Normal parameters can be learned from the data. Hyperparameters not.
</details>
---
**Hyperparameters**
When the performance of our classifier is not satisfactory, we can consider performing Hyperparameter tuning. True or False? How could we do it?

<details>
<summary>Solution</summary>

True
We coudl again use k-Fold Cross Validation, for each fold we would run separate k-Fold Cross Validation to find the ideal Hyperparameters for this specific fold and in the end we can have a look at all performance metric ↔ Hyperparameter conditions to select the ones that performed best.
</details>
---
