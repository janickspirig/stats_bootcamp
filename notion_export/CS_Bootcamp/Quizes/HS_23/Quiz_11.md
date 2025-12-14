---
title: "Quiz 11"
notion_id: "32349b92-872b-4525-af2f-c5285981de5c"
notion_url: "https://www.notion.so/Quiz-11-32349b92872b4525af2fc5285981de5c"
exported_at: "2025-12-13T23:21:17.045709+00:00"
---

# Quiz 11

## Question 1
You have written code that trains and evaluates a **scikit-learn** model. You run the code multiple times but notice that the evaluation results are different each time.
Which of the following answers are possible explanations for this?
Check all that apply.
❌ The **classification_report** function is not deterministic.
❌ All internal parameters of the model are randomly initialized. They always differ.
❌ The model is overfitted.
❌ The model is underfitted.
✅ The **train_test_split** method shuffles the data when not using a random seed.

<details>
<summary>Explanation</summary>

> 💡 **[classification_report](/9e4a78074aea481ca4c75e506d4671c7#edb6797681d048229c93d351b77b476b), [train_test_split](/9e4a78074aea481ca4c75e506d4671c7#4929175cb8d34b8f97fbaca1a2271458)**
❌ **Incorrect**, the `classification_report` function from scikit-learn is deterministic. Given the same input, it will always produce the same output. The function calculates metrics like precision, recall, and F1-score based on the input predictions and true values.
❌ **Incorrect**, while it's true that some machine learning models initialize their parameters randomly, this usually does not lead to significantly different results when training on the same data. However, there are exceptions, such as neural networks, which can end up in different local minima due to random initialization.
❌ **Incorrect**, overfitting refers to a model that has learned the training data too well, to the point where it performs poorly on unseen data. Overfitting would not cause the model to yield different results each time it's run.
❌ **Incorrect**, underfitting refers to a model that has not learned the patterns in the training data well enough, and thus performs poorly on both the training and test data. Like overfitting, underfitting would not cause the model results to vary each time it's run.
✅ **Correct**, the `train_test_split` function from scikit-learn shuffles the dataset before splitting it into training and test sets. If you don't specify a random seed (`random_state` parameter), it will use a different seed each time, resulting in a different split and potentially different results. To get the same results each time, you can set the `random_state` parameter to a fixed number.
</details>
---
## Question 2
You are given the following confusion matrix. The meaning of the rows and columns is the same as in the confusion matrix that can be created with scikit-learn.
For which of the three classes does the predictor perform best? Click on the corresponding image of the class (row image or column image both work).
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f03fe3a2-dff9-4dbb-a4ee-502ad31480aa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MJL6ZAZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIA8phxL2SLE%2BR95hvNoVIB9jBHok9TzW7TDCX5mYGaFSAiBwSa9frVzRKtSqBPkQC8SPQVNGbBKx1V70sbHMee9Koyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM9mDd1C2dWkfmumgVKtwDIkzjBAwti%2BZewGI5edYWKeuMQazZjX1D8Cp3hXLapzL2P3dm4lYnz3WsfIv43UX30ZYPLHAEhV8ZTiEFMrtcoGVfGkrLHZlIZKcHAXx6ixo%2BclkfOtvrJkkHeKBq07wkF5v4EUjwgpCxXpM6F9D0pwbDkUHzOilB57nys6q99m2lGy3BTzOyyHkudd2dT1q1ewJsew3wG09xcOMxA4yUt8%2FpvK4MsTJnyZo%2FjlIbYov%2FENpKpg1o4VV5L755Dn2y7EXjHXvmzX%2Fx5v6t5EQD1ZjKg17KRekPUZ7hPW49sVPUQdyMn63xzXKEZDrdqCmYDz4w2JM%2FpDnACOjaey%2BL%2FuYgSD3wq8M%2F5zwocfBGmGwAOYR3OTj5FqxfQfy1C%2FatiJ1zTv7HoyJpAN4L%2F9AE4vbVcQs05cwca4leRUQzaY7tHGlzl541P80mbjPFwP5D1vUXj07%2F7DbUfm1fxh%2F7jut4v4mbb%2FilNN%2BGjXcvBEpZn%2Fdbx57NddMBCFR%2B7VwUPPc4L%2BEHlVIbFffjrdG8tLL6E8xG2VX0aXzDzEaOtiMzH7dj4lCicm2IleOs0t9AhRN2ye22oHNuHKyjrgHUXz%2FQNnfay%2B9Xawut9%2BzQMc9iJzDVbDALcnARbIcwz873yQY6pgFYaR19iVcBg1CHsKGMd9REuTxR43F9QY9zGg%2FmTE8vLm1NlcbcfUJpwgY52peBSCcscIAt2r4FRCh0TAK42tdEMjp84LRjJsnjjaVVYZcirstNPHwOKWcGICqxLR3a3Wv%2BNONA4%2FZRiYCKfTw2WIxMyiHK0DH67bEnc1IVREJ%2F6YkvqA2sLDAyoFAXht8vpqWIGTHrnbPFe0MZ1XdHWimd%2FZDrfjLp&X-Amz-Signature=9afd8188ebd72ea0479b0a15cabd049aacc118a6880c3359be02fda5aa1950c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

> 💡 **[Confusion matrix](/3ca737faa7034fb9b1150be74f7f4430#88d2ed1628dd4d95be5744e5cbce0680)**
A confusion matrix is a table layout that allows visualization of the performance of an algorithm. Each **row** of the matrix represents the instances in a **predicted** class while each **column** represents the instances in an **actual** class. Thus, the **predicted** labels are on the **x-axis** and the **actual** labels on the **y-axis**.
The **diagonal** elements represent the number of points for which the predicted label is **equal** to the true label, while **off-diagonal** elements are those that are **mislabeled** by the classifier. The higher the diagonal values of the confusion matrix the better, indicating **many correct predictions**.
So we can interpret the confusion matrix in the exercise as follow (we assume that accuracy is the metric we foucus on):
- **Animal 1:** Out of 30 animals, the classifier has identified 10 (33%).
- **Animal 2:** Out of 33 animals, the classifier has identified 30 (90%). ← highest accuracy
- **Animal 3:** Out of 28 animals, the classifier has identified 15 (53%).
</details>
---
## Question 3
The confusion matrix of arbitrary size |C| × |C| (where *C* is the number of classes) of the results of the evaluation of a classifier has only 0 (zeros) in the diagonals. There is at least one sample for each class, but the classes are unbalanced (there is not the same number of samples in every class).
Which of the following statements is correct?
✅ The classifier was **always** wrong.
❌ This situation can never happen.
❌ Every class was predicted at least once (regardless of whether or not that prediction was correct).
❌ The classifier was **always** right.

<details>
<summary>Explanation</summary>

> 💡 **[Confusion matrix](/3ca737faa7034fb9b1150be74f7f4430#88d2ed1628dd4d95be5744e5cbce0680)**
✅ **Correct**, a confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of data for which the true values are known. In the confusion matrix, the **diagonal** from the top left to the bottom right represents the **correct predictions** made by the classifier, while the **rest** of the matrix represents the **errors**.
If all the diagonal elements are zero, it means that the classifier never predicted the correct class. Thus, the classifier was always wrong.
❌ **Incorrect**, because this situation can happen if the classifier is not trained properly or if it's not suitable for the given data.
❌ **Incorrect**, because every class being predicted at least once doesn't necessarily mean that those predictions were correct. The question states that all diagonal elements are zero, which means no class was predicted correctly.
❌ **Incorrect**, because the classifier was not always right. In fact, it was always wrong as explained above.
</details>
---
## Question 4
Which of the following statements are **True**?
❌ Unsupervised learning is preferable over supervised learning because we don't need to label the training data.
✅ Before making a train-test-split it may be a good idea, depending on the data set, to shuffle the samples in the dataset to reduce potential bias in the classifier.
✅ When training a classifier, the data quality of the training data is important, because the classifier does not learn how to deal with wrong data.
❌ In a supervised learning approach, using all of our labeled data for training a classifier is preferable, because we then can assume that the classifier has a good accuracy for classifying additional samples.

<details>
<summary>Explanations</summary>

> 💡 **[Supervised vs. unsupervised learning](/9b19eda74fac4ffb8e48b36dde3b47a4)**
❌ **Incorrect**, unsupervised learning is not necessarily preferable over supervised learning just because we don't need to label the training data. The choice between supervised and unsupervised learning depends on the specific problem and the available data. For instance, if we have a large amount of labeled data and we want to make predictions, supervised learning would be a better choice.
✅ **Correct**, before making a train-test-split, it's a good practice to shuffle the samples in the dataset. This is because the order of the samples can contain biases or patterns that may influence the performance of the classifier. For example, if the samples are sorted by their labels, the classifier might only learn to predict a single class if all samples of a class are in the training set.
✅ **Correct**, the quality of the training data is indeed important when training a classifier. If the training data contains errors or inconsistencies, the classifier might learn wrong patterns and therefore make incorrect predictions. This is especially true for supervised learning approaches, where the classifier learns from the given labels.
❌ **Incorrect**, using all of our labeled data for training is not necessarily preferable. It's important to hold out a portion of the data (known as a test set) to evaluate the performance of the classifier on unseen data. If we use all our data for training, we might overfit the classifier to the training data, meaning it performs well on the training data but poorly on new, unseen data. This would give us an overly optimistic view of the classifier's performance.
</details>
---
## Question 5
Which of the following statements about the Fruits dataset is correct?
- It has four classes.
- It is a dataset for binary classification.
- It is about the color classification of fruits.
- It can not be used to train a k-Nearest Neighbors classifier.

<details>
<summary>Explanation</summary>

> 💡 **[Fruits dataset](https://www.kaggle.com/datasets/shivmuratgupta/fruit-data)**
✅ **Correct**, it has four classes: Apple, Mandarin, orange and Lemon.
❌ **Incorrect**, because binary classification means that there are only two possible categories or outcomes. However, there are more than two types of fruits in the dataset.
❌ **Incorrect**, it is abotut he classficiation of the *type* of fruit.
❌ **Incorrect**, the kNN algorithm is a type of machine learning algorithm that can be used for both classification and regression tasks. As the Fruits dataset contains labels (and thus we are dealing with supervised machine learning), we can use the kNN algorithm
</details>
---
## Question 6
Which of the following statements regarding k-Nearest Neighbors are true and which are false?
❌ k-Nearest Neighbors only works if the data is 2-dimensional
❌ k-Nearest Neighbors is an unsupervised classification algorithm
❌ We can't use 1 (one) as our value for k
✅ In the case of binary classification it is a good idea to use an uneven (odd) number for k
❌ In k-Nearest Neighbors the absolute distance of every of the k nearest neighbors (for k+1) must not be considered for the prediction
✅ k-Nearest Neighbors is deterministic, if the nearest neighbor can be identified unambiguously for every sample.

<details>
<summary>Explanation</summary>

> 💡 **[kNN algorithm](/4e55bc27409940e98f9a060821d07644)**
❌ **False**,** **k-Nearest Neighbors (k-NN) can work with data of any dimensionality, not just 2-dimensional data. The algorithm calculates the distance between data points in a multi-dimensional space.
❌ **False**, k-NN is a supervised learning algorithm, not unsupervised. It requires labeled data to function properly. It uses these labels to classify new, unseen instances based on their proximity to known instances.
❌ **False**,** **We can indeed use 1 as our value for k. In this case, the algorithm classifies an instance based on its closest neighbor.
✅ **True**,** **using an odd number for k in binary classification can help avoid ties, i.e., situations where an equal number of neighbors belong to each class.
❌ **False**, the distance of each of the k nearest neighbors does matter in some variations of k-NN. For example, in a weighted k-NN, the influence of a neighbor on the classification of a new instance is weighted by the inverse of its distance to the new instance.
✅ **True**, k-NN is deterministic in the sense that, given the same dataset and the same parameters, it will always produce the same classification for a given instance. However, this is assuming that the nearest neighbor can be identified unambiguously for every sample. If two neighbors are at the same distance, the classification might depend on the order of the data in the dataset.
</details>
---

