---
title: "Quiz 11"
notion_id: "080c929e-3ecc-45e5-aedf-cbf04ea3664d"
notion_url: "https://www.notion.so/Quiz-11-080c929e3ecc45e5aedfcbf04ea3664d"
exported_at: "2025-12-13T23:15:56.241874+00:00"
---

# Quiz 11

## Question 1
Which of the following statements regarding k-Nearest Neighbors are true and which are false?
❌ kNN only works if our data is 2-dimensional
✅ In the case of binary classification it is a good idea to use an uneven (odd) number of k
✅ kNN is deterministic, if the nearest neighbor can be identified unambiguously for every sample
❌ In kNN the absolute distance of every of the k nearest neighbors (for k>1) must not be considered for the prediction.
❌ kNN ia an unsupervised classification algorithm.
❌ We can’t use 1 (one a sour value for k).

<details>
<summary>Explanation</summary>

❌ **Incorrect**, we can also use kNN when there are more than two dimensions in the data (e.g. Wine dataset).
✅ **Correct**, because then we can guarantee that there is always a majority class that wins and that we don’t end up with a tie in the majority voting.
✅ **Correct.**
❌ **Incorrect**, to select the k nearest neighbors we first compute the distances to all known observations. Thus, we must consider all datapoints.
❌ **Incorrect**, it is a supervised classification algorithm as we have to provide the class labels of the training data, otherwise no prediction is possible. 
❌ **Incorrect**, we can use any value we want for k (k>0), however, using k=1 does not make a lot of sense as there can be an outlier next to the unknown observation and then the class of this outlier would be assigned.
</details>
---
## Question 2
You are given the following confusion matrix. The meaning of the rows and columns is the same as in the confusion matrix that can be created with scikit-learn. 
For which of the three classes does the predictor perform best? Click on the corresponding image of the class.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f03fe3a2-dff9-4dbb-a4ee-502ad31480aa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYEPCDIM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICen2H6qNPMC8p%2B%2BBKRs4b3cJc9kslem%2F8kcxJc4CJc9AiAz0SlTbMhRbkoxBRCNtNFBHPzaG56H2wf8RmlfMk95mCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM6wyZGpwifWl%2FjxpRKtwDZzpnHHaVeopSbdZbFN%2Fm5vQNnEp7xxDHRXDjG1AIX2f44ce3IMlFpyFoc5KHO%2BwBZwkdDsFKb41iv1b%2F77sCZrq2Kn3kMo0AXGtCr1YNebUWwuwuxgNgx9HCx5XdugaGEWmZp3v0%2BbhcQTYpSRLBRKezGHVzw0XBLb9qjH6tVR5u1RS9jURm9L3w5fuhicFkFZBWKYn%2FgIQWAmv3La4iGZai0kczFoe0iNtTc6gNwZITxj8yy%2BR3KQXvIpxU2Ws%2BTNCvk4f%2Fx5tOkxrE6ofp6t7le9fwEO7BlXGBe8mSirBuCWNK2b1YqOAVHaNbrf1NojoQzTxbamgC1jSsJ1NXmf9ck6TWmKyW2oJ0QqjC7uR2iMFBAFRJoYzawQPXGE6Y0O8nlkobKxc6w6RvUJwQGcw0JJwqV8CpYPkB3mRwYywrLcWHlAF6wCKxLvPUITJVN189%2BlYhEA4a7qjwY78mxbkZ0C2NGe8%2BawkJOCstSKcLSHf8XTk9TnVJLwVYPgwWr99yTpwEjFez26BKDmeggzn0BiJppOneL1myPYmSXmDWRZeHVKqxJ%2BY8EvyEZTN027yluqr0prYONZdsnfvj6VsMbHAcYUo%2BgVvOwunxGTvRih5lqlC1g5TR%2FKcwxc73yQY6pgGQCY%2BMxvgC1NRahONZoZ4m4le%2BOa2Yx5oqNghA6JcFMhsmdI9tTIb7KAiTSnMdt1AIxURuoT7YWrSJSg61PGaL20KhME7uE%2B3SR2ZAPIksnckPmX77sSdRZilw92%2FzEO6ZQjzdxGsuXXq4EeA%2FxBf8OsLXCpc6vMqFLEm%2BQc0StM8m35r4bEEw6ADz70drKQ7uEBo4BgbLJX9R8iotC7sRRz9wLdrR&X-Amz-Signature=cce2aee0d37be6c89f566cede6bde8805f83cae13239a2b24446047efc55b5e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

The structure of the scikit-learn confusion matrix is as follow:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b2996f9d-91d3-41fa-84bd-f3c4f27c6cc8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662D4GXZB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCGMsP2I8BAtHJIjGnP8suce6jU0d21naxlCka3LZ1UjQIgChR8WfH41nVBtDEn5v8P7aZ27SGDA9UWL8kkti0DgoEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBn5CdSfCf1qn1PFDSrcA%2FB6Uim%2FtqhQuWxntWoPo3SNUI6Fawc3kHWV5aAPmC3AYQai6RfvfL9PjvqLXLvGARncO9zRDpMFpIYkKcI49rXFRYhUU79Mjnlmj4fshfejy%2FRZaJspT%2BHByxOfaw%2B6Kyv6WHoC1s%2F7dyiYZIVJDUcIL4lpbQ47haRP7HwCmKPrThQH9OjRUkax2ZDRHaMN%2BcGa7NvKp2VpEfSr8FZrTcef9Qv60ENiB7agb3K7kWCYvYjuZUhCgmBtqjY5Nret3UCLZtKBuwiQPUiYATThpNAdE4R0SS4gtU3%2BjyPwrRbF1l9UzLRdvDA0QZQa%2BJa4UWeh74xGaoA5buS%2BDvUyn4YWtdXKEEsOB9eKINLNKpnhRFzUE7yWxB3T%2F4lbgV8mtRbfVb%2BjMJuLTKGRBrl2gz6CIFx72LVsEVQYtOipB2UrEKYUvE8zhMYkowPR14O6aasTdlpOmfHveRmQz6gFknJF11RBA3M80cfaxr%2BmhcI%2FiWi71v%2Fxau3nP6%2BebTdtzl0izlrFyL76jIOUOlz%2Fiv8W3HwnI6%2BFc%2Fap913xAN6eIA5gQf121xJFxsOVrYRBc4ExqKK7mNgW51NY9TOSzYinaiDFa99i1eLmZ772p%2FE3kBcJnz37ThhmU1GRMNjO98kGOqUBcQkp9T4iogI6JQQ92QFfmIBF6ZBH%2FRilQGYNicgi4Xrj6306TjhFBbV8I5ArQLXsCoCixzerHQjyQG3uHadcKB9nJM9tChyOiLN%2FZZfG3ophls8MnsvYQNn5x3srNHyOY5yCyReN2Vp6zeFKzWMDSE0C41hDM%2BQHC6wpNEBrixs0X5Cx1kCt68iRfk103eqocynpvJFK5G1XqnQptlnmWYCBciM%2B&X-Amz-Signature=407418defaf95fc20eab34028d150c0df4aa5f1a3323b2cf6dcff9759c346e68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the predicted labels are on the x-axis and the actual labels on the y-axis.
So we can interpret the confusion matrix in the exercise as follow: (we assume that accuracy is the metric we foucus on)
- **Animal 1:** Out of 30 animals, the classifier has identified 10 (33%).
- **Animal 2:** Out of 33 animals, the classifier has identified 30 (90%).
- **Animal 3:** Out of 28 animals, the classifier has identified 15 (53%).
</details>
---
## Question 3
The confusion matrix of arbitrary size of the results of the evaluation of a classifier has only 0s in the diagonals. There is at least one sample for each class, but the classes are unbalanced (there is not the same number of samples in every class). 
Which of the following statements is correct? 
❌ The situation can never happen.
✅ The classifier was **always** wrong.
❌ The classifier was **always** right.
❌ Every class was predicted at least once (regardless of whether or not that prediction was correct). 

<details>
<summary>Explanation</summary>

A confusion matrix described like this would look as follow. Let’s assume in the test dataset there are 50 observation.
|  | True | False |
| --- | --- | --- |
| True | 0 | 30 |
| False | 20 | 0 |
We can see that the classifier did not predict the True or the False label for one time correctly. 
The classifier classified all the True’s as False’s and all the False’s as True’s and was thus always wrong.
</details>
---
## Question 4
Which of the following statements about the IRIS dataset is correct?
❌ It is a dataset for binary classification.
❌ It is about classification of flower colours. 
✅ It has three classes. 
❌ It can not be used to train a kNN classifier.

<details>
<summary>Explanation</summary>

❌ **Incorrect**, it has three classes and is thus not binary.
❌ **Incorrect**, it is about the classification of the type of flower.
✅ **Correct**
❌ **Incorrect**, we can use multi-class datasets with kNN. And the data is also two dimensional (sepal and petal length).
</details>
---
## Question 5
You have written code that trains and evaluates a scikit-learn model. You run the code multiple times but notice that the evaluation results are different each time. Which of the following answers are possible explanations for this? Check all that apply.
❌ The **classification_report** function is not deterministic. 
✅ You have changed some or all of the parameters of the model between runs. 
✅ The **train_test_split** method shuffles the data.
❌ The model is overfitted. 

<details>
<summary>Explanation</summary>

❌ **Incorrect**, as it is deterministic (it does what it should and produces the output that we expect).
✅ **Correct**, often we change the parameters of a model based on the result it achieved, we call this hyperparemeter tuning. 
✅ **Correct**, the data is shuffled according to the train / test ratio to prevent unwanted bias from happening.
❌ **Incorrect**, if the model would be overfitted then we would get consistently the same bad performance on the test dataset.
</details>
---
## Question 6
Which of the following statements are **True**?
❌ Unsupervised learning is preferable over supervised learning because we don’t need to label the training data. 
✅ When training a classifier, the data quality of the training data is important, because the classifier does not learn how to deal with wrong data. 
❌ In a supervised learning approach, using all of our labeled data for training a classifier is preferable, because we then can assume that the classifier ha s a good accuracy for classifying additional samples.
✅ Before making a train-test-split it may be a good idea, depending on the data set, to shuffle the samples in the dataset to reduce potential bias of the predictor.

<details>
<summary>Explanation</summary>

❌ **Incorrect**. It always depends on the use-case for which we are building a model. Sometimes we have labeled data available other times not, etc.
✅ **Correct**. If we put garbage into the model it will give us garbage back. 😄
❌ **Incorrect**. We never use all the data for training. Otherwise we couldn’t check the performance of our model as the model knows already all the data from the training process and is therefore heavily biased. 
✅ **Correct**. Yes, shuffling is often a good idea to prevent that, for example, all outliers are in the training set and not a single one in the test set which results in very high bias.
</details>
---

