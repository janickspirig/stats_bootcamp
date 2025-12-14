---
title: "scikit-learn"
notion_id: "9e4a7807-4aea-481c-a4c7-5e506d4671c7"
notion_url: "https://www.notion.so/scikit-learn-9e4a78074aea481ca4c75e506d4671c7"
exported_at: "2025-12-13T22:57:24.129117+00:00"
---

# scikit-learn

# Motivation
---
[scikit-learn](https://scikit-learn.org/stable/) is a library that provides tools to do predictive data analysis (Machine Learning) out of the box. Basically, scikit-learn allows us to make predictions from our data out of the box. The image below provides a nice overview about the classifiers that can be used with scikit-learn.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/77f3458e-500d-4307-9700-27c68b3a5aee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KPLI2U4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICtZZdOjR7pupTgUCajQRgiri6tlT9T8c7PDhlTovtiQAiBzd8RXN3fnBQnoX7fISe7N1RN2a2HsgxyFU6Ea7ibcMCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM1OqpyAsyTHueVfB7KtwD1ai2smAVwCKSE%2B%2FhM1LzHHnh86SXiH8pEHNZSkyErhk8jYGRV5BasuZ76w9zBe3Osl16UyNxRJjCWJ39r5DVuU6T6EyRqDp%2B0z6yxWC4fxwaOSTgqYj9Il1mKJrBGx%2F3SaxcR6o2IbuiVEHEOX8fI6sdwMyp0%2F%2BUpP6x9e59nTpaQHYkLHrBaMr2DTs%2Br0HhJdFSNUBnvaVqXRkgtheou3%2BO4gMGVqB5CfFkzRwyJCzCQ6WlPcnw3WZew2duvI5BC8%2BoXWSPWjfbOiGXyLgr3g0baqy%2Fzd3DxfoNyQaXy08ZDDLQZlbn7jKkP2bTZc%2FkQPJc3vAPaklfuKXhVxufRIFvTtDRZI8XI1u9O391KXRIk%2F9N9xfoFjspBF3hy9VAKuVYSLH5gK2iVeHjRFKTmkIaAyWS7DbK3hxgNPP6rnzFzp6WcLGRBNNu5VOeiLbCVeGgD47KMawJX42J2M%2FdQfYSOMxTgDWYqxKt0ou%2FRwQEt6uo03jmE%2Bv9wm%2BB3FYkDmXeW7%2Bj1nB7R8yf88HjTDBnu5hVjADGia8ioEHuXqfhOcmXiDcua1O1vop32ovB5yl5k6qzJisnS6%2FQUsycG6JDCzjptrhyGOo95EFbVUFb%2Fj5oa8%2F%2FVaFfon8whM73yQY6pgFbVHMWgP0I4Xwq2G2%2BzWcefJS2ZDtXNAR70dhHJxs5CwyOaie5eDKxafo5lIBqTeu1PuZSMHGGdT3MNES4FZuJbIUHD4WQ3g21tYsrWxrFcNpT9eEEBG7VLVwX02YxHjOc0Mnmsr%2F%2BltXHwNw3%2FHpQ1oNpagbbdG3HoGGKkSle%2Bt2wcZsgmF4w7imK6%2BqQ%2FDP%2BeTvl5BlHoiQl1wouus9r39ScEiQa&X-Amz-Signature=d4c20cd559d8b82ef9f0ae179a8eeed1f664aa173774402740b1318bd85aa75c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The image shows a few important criteria that matter when we need to choose a classifier.
1. Do we want to predict a **Category** or a **Numerical value**?
1. **Category**: [Categorical data](/8abd5dae91fc4e90b63453e6d4a80952#058e2f9345364edcb90e0a46f4ba6c36)
1. Do we have labeled data?
1. <u>No</u> → clustering → [unsupervised learning](/9b19eda74fac4ffb8e48b36dde3b47a4)
Possible Algorithms
1. k-Means
1. <u>Yes</u> → classification → [supervised learning](/9b19eda74fac4ffb8e48b36dde3b47a4)
Possible algorithms
1. [kNN](/4e55bc27409940e98f9a060821d07644)
1. Naive Bayes (text data)
1. etc.
1. **Numerical value**: [Numeric data](/8abd5dae91fc4e90b63453e6d4a80952#058e2f9345364edcb90e0a46f4ba6c36)
1. Do we want to predict something or simplify the data?
1. <u>Predict</u> → regression
Possible algorithms
1. [OLS regression](/3b0dfaa603e642b498b666d147d66714)
1. <u>Simplify</u> → dimensionality reduction
Possible algorithms
1. PCA
---
# Functions
---
> 💡 **I think it is important to know what each function is doing in scikit-learn.
However, I think it is more important to understand how the functions work together and when to apply which one. Therefore, make sure you understand how the [general procedure](/9e4a78074aea481ca4c75e506d4671c7#068c4b1030ac48509d58a7a4b0979626) as well as the [TF-IDF procedure](/9e4a78074aea481ca4c75e506d4671c7#6c293d5c082449dda1dc09435e86db8b) work.**
## [`LinearSVC()`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)
---
**Syntax**
This function allows us to create a new [Linear Support Vector Classifier](https://www.youtube.com/watch?v=efR1C6CvhmE) that is commonly used in classification tasks (supervised learning). As you can see from the scikit-learn documentation there are many options to adjust this classifier to our specific needs.
`LinearSVC()`
**Input**
A lot
**Output**
A Linear Support Vector Classifier
---
## [`KFold(`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html)[*`k_fold`*](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html)[`)`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html)
---
**Syntax**
This function creates a KFold object that can be then further used to split the train and test data into k-folds in order to do cross validation.
`KFold(<< n_folds >>)`
**Input**
`<< n_folds >>` : optional (default 5)
- Integer
*→ the number of folds we want to create*
**Output**
A KFold object that can be then further used to split the data into folds by using [`.split()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold.split)
---
## [`MultinominalNB()`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)
---
**Syntax**
This function allows us to create a new [Mutinominal Naive Bayes Classifier](https://www.youtube.com/watch?v=km2LoOpdB3A) that is commonly used in text classification tasks (supervised learning). As you can see from the sklearn documentation there are many options to adjust this classifier to our specific needs.
`MutinominalNB()`
**Input**
A lot
**Output**
A Multinominal Naive Bayes Classifier
---
## [`KNeighborsClassifier()`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
---
**Syntax**
This function allows us to create a new [k-Nearest-Neighbors Classifier](/4e55bc27409940e98f9a060821d07644). that is commonly used in classification tasks (supervised learning).
`KNeighborsClassifier(<< n_neighbors >>)`
**Input**
`<< n_neighbors >>` : optional (default 5)
- Integer
*→ the number of neighbors that we should be looked at (should be odd number)*
**Output**
A k-Nearest-Neighbors Classifier
---
## [`MinMaxScaler()`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
---
**Syntax**
This functions creates a Scaler object that can be used to scale values into a specific value range. Usually, we do such scaling when the values are very spread out (e.g. from 0.05 to 10’000). Then, we scale them usually down into a specific range, e.g., 0 to 1.
`MinMaxScaler(<< feature_range >>)`
**Input**
`<< feature_range >>` : optional (default (0,1))
- Tuple
*→ desired value range in format **`( << min_value >>, << max_value >>)`*
**Output**
A new Scaler object for the defined value range, which can be used to transform the data.
---
**Scale data to defined value range**
Let’s assume we have collected the height and width of 12 fruits. However, the value vary heavily, from very small to very big. 
```python
dimensions = np.array(
  [
		(0.1, 3.4), (74.1, 3.4), (1.1, 3.4), (2.1, 49.4),
		(3.1, 47.4), (31.1, 4.4), (32.1, 4.4), (3.1, 45.4),
		(49.1, 5.4), (88.1, 5.4), (48.1, 52.4), (45.1, 5.4)
  ]
)
```
For this reason, we want to scale the data into a defined value range so that all data points lay between 0 and 1. 
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaler.fit_transform(dimensions)

array([[0.        , 0.        ],
       [0.84090909, 0.        ],
       [0.01136364, 0.        ],
       [0.02272727, 0.93877551],
       [0.03409091, 0.89795918],
       [0.35227273, 0.02040816],
       [0.36363636, 0.02040816],
       [0.03409091, 0.85714286],
       [0.55681818, 0.04081633],
       [1.        , 0.04081633],
       [0.54545455, 1.        ],
       [0.51136364, 0.04081633]])
```
---
## [`TfidfVectorizer()`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
---
**Syntax**
This functions creates a new TF-IDF Vectorizer that helps transforming text data into processable features and applying TF-IDF.
`TfidfVectorizer(<< stop_words >>) `
**Input**
`<< stop_words >>` : optional (default None)
- String
*→ the stop words of which language that should be excluded*
**Output**
A new TF-IDF Vectorizer. We can use this object now to transform documents into features using [`.fit_transform()`](/9e4a78074aea481ca4c75e506d4671c7#16f816916fcc43318154a1b6b6ea38ae) (for training data) and [`.transform()`](/9e4a78074aea481ca4c75e506d4671c7#3c583c11477d480d89e97c4211ae4d7b) (for test data).
---
## [`LabelEncoder()`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
---
**Syntax**
This functions creates a new Label Encoder that helps transforming text labels into processable numerical labels.
`LabelEncoder()`
**Input**
None
**Output**
A new Label Encoder object. We can use this object now to transform text labels into numerical ones by using [`.fit()`](/9e4a78074aea481ca4c75e506d4671c7#313da2a2e0b0484184c75f977db9e51c) and [`.transform()`](/9e4a78074aea481ca4c75e506d4671c7#af25fc640d4b4de78a54e6a66f85909b) methods.
---
**Transform text labels into numerical labels**
Assume we have a dataset of ten fruits that are of three different types: Apple, Pear and Orange.
```python
fruits = ['Apple', 'Orange', 'Pear', 'Apple', 'Apple',
					'Apple', 'Orange', 'Pear', 'Apple', 'Apple']
```
Now, we want to implement a classifier that is able to predict a the type of a fruit. To do so, in the pre-processing stage we need to transform the text labels (Apple, Pear, Orange) to numerical labels (0, 1, 2).
First, we need to fit the Label Encoder on our dataset by using the [`.fit()`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.fit) method. 
```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(fruits)
```
Now, we can transform the labels of the ten fruits to numerical ones using the [`.transform()`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.transform) method. 
```python
le.transform(fruits)

array([0, 1, 2, 0, 0, 0, 1, 2, 0, 0])
```
Or we can do everything in one function call using the [`.fit_transform()`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder.fit_transform) method. 
```python
le.fit_transform(fruits)

array([0, 1, 2, 0, 0, 0, 1, 2, 0, 0])
```
And in case we have forgotten the original labels, we can recall them over the `.classes_` attribute.
```python
le.classes_

array(['Apple', 'Orange', 'Pear'], dtype='<U6')
```
---
## [`train_test_split()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
---
**Syntax**
This functions helps us to split the features and labels into a training and test set. 
`train_test_split(<< features >>, << labels >>, << train_size >>)`
**Input**
`<< features >>` : required
- Numpy Array **OR **Pandas Dataframe
*→ the features of our data, e.g., the dimensions of fruits (height, width)*
`<< labels >>` : required
- Numpy Array **OR **Pandas Dataframe
*→ the labels of our data, e.g., the names of fruits (Apple, Orange, Pear)*
`<< train_size >>` : required
- Float
*→ percentage of data that should be assigned to training set*
**Output**
Four chunks of data:
1. `X_train` → features of data observations that were assigned to training
1. `y_train` → labels of the data in `X_train`
1. `X_test` → features of data observations that were assigned to testing
1. `y_test` → labels of the data in `X_test`
---
**Split dataset**
Let’s assume we have measured the height and width of 4 apples, 4  oranges and 4 pears.
```python
import numpy as np

dimensions = np.array(
  [
		(2.1, 3.4), (2.1, 3.4), (2.1, 3.4), (2.1, 3.4),
		(3.1, 4.4), (3.1, 4.4), (3.1, 4.4), (3.1, 4.4),
		(4.1, 5.4), (4.1, 5.4), (4.1, 5.4), (4.1, 5.4)
  ]
)

labels = [
	'Apple', 'Apple', 'Apple', 'Apple',
	'Orange', 'Orange', 'Orange', 'Orange',
	'Pear', 'Pear', 'Pear', 'Pear'
]
```
We now want to implement a classifier that is able to predict whether a new fruit is an apple, orange or pear based on the height and width of the fruit.
To do so, we must first split the data into train and test set. We want 75% of the data, i.e., 9 fruits to be in our training set and 3 fruits in our test set. We can do the split by using the [`train_test_split()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) method.
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(dimensions, labels, train_size = 0.75)
```
We get now four chunks of data:
`X_train`
```python
array([[4.1, 5.4],
       [4.1, 5.4],
       [3.1, 4.4],
       [3.1, 4.4],
       [2.1, 3.4],
       [4.1, 5.4],
       [4.1, 5.4],
       [3.1, 4.4],
       [2.1, 3.4]])
```
`y_train`
```python
['Pear',
 'Pear',
 'Orange',
 'Orange',
 'Apple',
 'Pear',
 'Pear',
 'Orange',
 'Apple']
```
`X_test`
```python
array([[3.1, 4.4],
       [2.1, 3.4],
       [2.1, 3.4]])
```
`y_test`
```python
['Orange',
 'Apple',
 'Apple']
```
However, before we can start now with the training process, we must transform the labels (`y_train`, `y_test`) to numerical ones using a [Label Encoder](/9e4a78074aea481ca4c75e506d4671c7#a7dc9116d40c4e3093dbbd3bade9d18d).
---
## [`.fit()`](https://stackoverflow.com/questions/45704226/what-does-the-fit-method-in-scikit-learn-do) 
---
**Syntax**
This function allows us to train a classifier on the training data.
`<< classifier >>.fit(<< X_train >>, << y_train >>)`
**Input**
`<< X_train >>` : required
- Numpy array **OR **Pandas Dataframe
*→ the features of the training data*
`<< y_train >>` : required
- Numpy Array **OR **Pandas Dataframe
*→ the labels of the training data*
**Output**
A trained classifier.
---
**Train classifier**
Assume that we have chosen to use a k-Nearest-Neighbors classifier and have split our data into train and test. Now we want to train our classifier on the training data consisting of features and labels of 9 fruits. 
```python
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier()

clf.fit(X_train, y_train)
```
---
## [`.fit_transform()`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.fit_transform)
---
This is a general method to do data transformation, we can use it for example in combination with a [Label Decoder](/9e4a78074aea481ca4c75e506d4671c7#2fd8408ec287411d803cb964a4c79930), [TF-IDF Vectorizer](/9e4a78074aea481ca4c75e506d4671c7#3ee2c858054541ceaf0dadbfdb3c3ea6), or [MinMax Scaler](/9e4a78074aea481ca4c75e506d4671c7#00e33fd077624e76afff478d86621717).
The method does two things:
- `fit` → fit scaler to data
- `transform` → transform the data
For example if we [scale the values using MinMax Scaler](/9e4a78074aea481ca4c75e506d4671c7#00e33fd077624e76afff478d86621717) into a specific value range, the fit part calculates the value range boundaries and the transform part does the transformation for all the values.
---
## [`.transform()`](https://towardsdatascience.com/what-and-why-behind-fit-transform-vs-transform-in-scikit-learn-78f915cf96fe)
---
This is a general method and is very similar to [`.fit_transform()`](/9e4a78074aea481ca4c75e506d4671c7#16f816916fcc43318154a1b6b6ea38ae).
The difference is that it only does the **transform **part, but leaves out the **fit** part, so it does not *learn* anything from the data.
This is why we usually apply this method on the test data only. If we would do the **fit** part on our test data, the model would be **biased** as it would have learnt something about the test data, before making its predictions.
For example, in TF-IDF this method [transforms the test data into a spare matrix](/9e4a78074aea481ca4c75e506d4671c7#0938c2e76ed04d34939215b25c31691b), but does not apply any TF-IDF calculations.
---
## [`.predict()`](https://machinelearningmastery.com/make-predictions-scikit-learn/)
---
**Syntax**
With this function a trained classifier ([`.fit()`](/9e4a78074aea481ca4c75e506d4671c7#20d78b49859941fc86e5fb9b559b130a)) can make predictions for the test data. 
`<< trained_classifier >>.predict(<< X_test >>)`
**Input**
`<< X_test >>` : required
- Numpy Array **OR **Pandas Dataframe
*→ The features of the test data*
**Output**
The predicted class labels.
> 🚨 **Here we don’t provide `y_test` as an input to `.predict()` because this is exactly what we want the classifier to predict. Otherwise, we would tell it the solutions before solving the exam and the classifier would be heavily biased.**
---
**Predict labels for test data**
Let’s assume that after the classifier has been trained, we now want to make some predictions on the test data. Specifically, for the three fruits we want to predict whether they are an Apple, Orange or Pear.
```python
y_pred = clf.predict(X_test)

y_pred
array([1, 1, 1])
```
We can see that the classifier predicted all three fruits to be oranges.
---
## [`accuracy_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)
---
**Syntax**
With this function we can calculate the [accuracy score](/3ca737faa7034fb9b1150be74f7f4430#979124e37b4e4554ab728e4e63e99c10) on the predictions made by a classifier.
`accuracy_score(<< y_test >>, << y_pred >>)`
**Input**
`<<< y_test >>` : required
- Numpy array
*→ the *<u>*actual*</u>* class labels of the test data*
`<<< y_pred >>` : required
- Numpy array
*→ the *<u>*predicted*</u>* class labels for the test data*
**Output**
[Accuracy score](/3ca737faa7034fb9b1150be74f7f4430#979124e37b4e4554ab728e4e63e99c10)
---
**Calculate accuracy score**
Let’s assume we want to evaluate our fruit classifier. Fort this reason we calculate the recall. 
```python
from sklearn.metrics import accuracy_score

y_test
array([1, 0, 0])

y_pred
array([2, 2, 0])

accuracy_score(y_test, y_pred)
0.3333333333333333
```
We see that the classifier achieves an accuracy score of 33%.
---
## [`precision_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html)
---
**Syntax**
With this function we can calculate the [precision score](/3ca737faa7034fb9b1150be74f7f4430#8f3e40c59c36482197bc746cf80dbc50) on the predictions made by a classifier.
`precision_score(<< y_test >>, << y_pred >>, << average >>)`
**Input**
`<<< y_test >>` : required
- Numpy array
*→ the *<u>*actual*</u>* class labels of the test data*
`<<< y_pred >>` : required
- Numpy array
*→ the *<u>*predicted*</u>* class labels for the test data*
`<< average >>` : optional
- String
*→ how scores should be averaged if there are multiple classes, options:*
- `'micro'`
- `'macro'`
- `'weighted'`
**Output**
[Precision score](/3ca737faa7034fb9b1150be74f7f4430#8f3e40c59c36482197bc746cf80dbc50)
---
**Calculate precision score**
Let’s assume we want to evaluate our fruit classifier. Fort this reason we calculate the precision. 
```python
from sklearn.metrics import precision_score

y_test
array([1, 0, 0])

y_pred
array([2, 2, 0])

precision_score(y_test, y_pred, average='macro')
0.16666666666666666
```
We see that the classifier achieves an unsatisfying precision score of 16%.
---
## [`recall_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html)
---
**Syntax**
With this function we can calculate the [recall score](/3ca737faa7034fb9b1150be74f7f4430#5ef7c9301e424eaf85bdfe87d032c836) on the predictions made by a classifier.
`recall_score(<< y_test >>, << y_pred >>)`
**Input**
`<<< y_test >>` : required
- Numpy array → the <u>actual</u> class labels of the test data
`<<< y_pred >>` : required
- Numpy array → the <u>predicted</u> class labels for the test data
`<< average >>` : optional
- String → how scores should be averaged if there are multiple classes, options:
- `'micro'`
- `'macro'`
- `'weighted'`
**Output**
[Recall score](/3ca737faa7034fb9b1150be74f7f4430#5ef7c9301e424eaf85bdfe87d032c836)
---
**Calculate recall score**
Let’s assume we want to evaluate our fruit classifier. Fort this reason we calculate the recall. 
```python
from sklearn.metrics import recall_score

y_test
array([1, 0, 0])

y_pred
array([2, 2, 0])

recall_score(y_test, y_pred, average='macro')
0.5
```
We see that the classifier achieves a recall score of 50%.
---
## [`f1_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
---
**Syntax**
With this function we can calculate the [F1-score](/3ca737faa7034fb9b1150be74f7f4430#9aabbb38114445a694155a99c1818adf) on the predictions made by a classifier.
`f1_score(<< y_test >>, << y_pred >>)`
**Input**
`<<< y_test >>` : required
- Numpy array
*→ the *<u>*actual*</u>* class labels of the test data*
`<<< y_pred >>` : required
- Numpy array
*→ the *<u>*predicted*</u>* class labels for the test data*
**Output**
[F1-score](/3ca737faa7034fb9b1150be74f7f4430#9aabbb38114445a694155a99c1818adf)
---
**Calculate F1-score**
Let’s assume we want to evaluate our fruit classifier. Fort this reason we calculate the recall. 
```python
from sklearn.metrics import f1_score

y_test
array([1, 0, 0])

y_pred
array([2, 2, 0])

f1_score(y_test, y_pred)
0.25
```
We see that the classifier achieves a F1 score of 25%.
---
## [`precision_recall_fscore_support()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)
---
**Syntax**
With this function we can calculate precision, recall and F1 score in one go.
`precision_recall_fscore_support(<< y_test >>, << y_pred >>, << average >>)`
**Input**
`<<< y_test >>` : required
- Numpy array
*→ the *<u>*actual*</u>* class labels of the test data*
`<<< y_pred >>` : required
- Numpy array
*→ the predicted class labels for the test data*
`<< average >>` : optional
- String
*→ how scores should be averaged if there are multiple classes, options:*
- `'micro'`
- `'macro'`
- `'weighted'`
**Output**
Numpy array containing
(1) [Precision](/3ca737faa7034fb9b1150be74f7f4430#8f3e40c59c36482197bc746cf80dbc50), (2) [Recall](/3ca737faa7034fb9b1150be74f7f4430#5ef7c9301e424eaf85bdfe87d032c836), (3) [F1-score](/3ca737faa7034fb9b1150be74f7f4430#9aabbb38114445a694155a99c1818adf) & (4) number of observations
---
**Calculate support**
Let’s assume we want to evaluate our fruit classifier. For this reason we want to calculate precision, recall and F1-score in one go.
```python
from sklearn.metrics import accuracy_score

y_test
array([1, 0, 0])

y_pred
array([2, 2, 0])

precision_recall_fscore_support(y_test, y_pred, average='macro')
(0.16666666666666666, 0.5, 0.25, None)
```
We see that the metrics that were calculated before separately are now returned in one single array and can easily be processed further.
For number of observations there is the value `None`, as we averaged the scores over the classes.
---
## [`classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)
---
**Syntax**
With this function we can calculate precision, recall and F1 score in one go. Compared to [`precision_recall_fscore_support()`](/9e4a78074aea481ca4c75e506d4671c7#012cc7ddd13e49508121fd0e5735ed9f), this function give us an output that is easily readable.
`classification_report(<< y_test >>, << y_pred >>)`
**Input**
`<<< y_test >>` : required
- Numpy array
*→ the *<u>*actual*</u>* class labels of the test data*
`<<< y_pred >>` : required
- Numpy array
*→ the *<u>*predicted*</u>* class labels for the test data*
**Output**
Metrics report
---
**Produce report**
Let’s assume we want to evaluate our fruit classifier. For this reason we want to produce a metrics report.
```python
from sklearn.metrics import classification_report

y_test
array([1, 0, 0])

y_pred
array([2, 2, 0])



print(classification_report(y_test, y_pred))
```
![Metrics report](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/677d8baa-a959-4a16-80b0-34f5cafe2a12/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMQKCGLW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAoZVVRRj7AK0u4sBsnBe6DimY2cQ47QK6EjO2pMNCFZAiAsp2d8e%2Bnc%2BEZ9fkdPSfXQ5M8FbTEANH4Leunkh6MnUSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMsIjf94eYc%2FK6ezkzKtwDaeG1iA7OAUcxGwmoCHfGeHhESGAzlv%2FWX4gUtIlFzPYEoHXTIjQBOIdOUsaA2QuXrdrwFw7rDwAMh69f%2Fc2Vqy%2FzTgpAcoZzVOTXdEioYv77Sv9RC%2Fdq8yRmjkTv5Ltu5iY%2B%2F832ti2FFjGUyMZmYExkG1FX9G%2B7sYJbBWzkKfuvwiHOnfeYFEwpT4q87I1kjEtZjjbJwtklTD1DbBxxDngaj9b%2F3%2BBXyU9ENGj1VnppYahZ9MigO8RP6pmsgA0vjHbL%2F3Jx8wbQ85myXXElqimki32vMnXp3sXqKpXH8pNYprouqIMEqgCB5clWfP26WJybWCgmDhTedDFMoM2As643jEz6W1a7tMShppAe2MrXxWC7uEw5RXXZOpl4B28MKEV2w83mqPMp8K5wqlHYvfyNil6gwvDpaAm7cy176%2Bm%2BLv5uhuvetqr4ChGYaAp%2F1agYclYBj3rXPEs53yA8DXKJwmxJfQVS%2F%2FNxbIeq93EbHPEwteIcpdopHv9xrWLzAVTxrPIS7xle7JF9j4q53HAn%2FBP1gCFLDyvNsN69EFLld0m15T0C28lX04LJKOpJYA47h3vGw0pHdIklV5GWLSaYxyxOS6L%2B6XTEdWfI%2FUbRGHlCBCS9qtrWB9kw4M73yQY6pgH5fTZZb5B4jUPD%2B7cOVai8oxyPrO8ABitr0xnbFYZs0WVjnh%2FzwAE%2BFbDqPi7Ntu6B%2FoKmahUHpyqymlZzE3UV9vEfqZx50pS7d0E4PPNHvj8JJnChZpkIslWPIqXSjmhcaEZwEtSiBbe81dtHekBG214vnMjSwguhZkmUfcy9c9nstfcgFEI9bY%2F%2BVUvR%2Bign7oneQc9PipfPECql9Zo6Ped41d4Y&X-Amz-Signature=67dce57156ba44acacce0c732db82fd11132b08742110426dea69a0eeb585c2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**support** → number of observations
[**macro avg**](/4e55bc27409940e98f9a060821d07644#55b1c5f00cef4e9490b75034767993ad)** **→ average over classes
[**weighted avg**](/4e55bc27409940e98f9a060821d07644#55b1c5f00cef4e9490b75034767993ad) → averages are weighted by number of observations per class
---
# General procedure
---
> 🔗 **[Jupyter Notebook with code](https://colab.research.google.com/drive/17zsoItdQ_7-NdjnUdOfyQyU14N5_CsvV?usp=sharing)**
---
Let’s assume we want to implement a classifier that is able to classify the type of an [Iris flower](https://www.almanac.com/plant/irises). There are three types of Iris flowers: 
![Types of Iris flowers](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d623a813-48e5-459a-8265-dcb419dc0623/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SILYV7F%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICFDoS%2F28nSivxk2x4ZOBAw4rVsXwWNd1twMbcXYloSUAiEAgyTlIct8mIZuroKJ7AcIv1vanaw9t5qRO9Uhuv%2Frxhoq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIWvtPpE7wO8dNuyDyrcA6ICYDMVEh9Dto%2BRO%2BNKxDtdI24JwSiDTx19bUQQnjaViApAmTLSC5Q%2B1oE1l8ELH6sz1HoYPOsdTYTvOjng6GUq6jVR%2FSgbzv1ibPrf9TetvmLSOniFIMmeVMl4xNvggfn84IOC78pA2qPB8C46cqxCRwHJS5UTH5e2wxJbylLBnsEpxFzJYrWEj%2BL011U%2F6n13GtUg%2Byu9Zz3jfF7AIr%2Flt42N8J1zd7M56TL5Y1l%2BPLdDJaDmDtbo%2Fec3G1SkKXRfHDCYOtj8WtwA1R7gZDMsY6%2BpRR9%2FyP0exCGR2cGVqNgIsUMg6sIJE2kmLLQ8Vo5nZVsxYovneD%2Fc9Uf6nHL8ZB6JbU9mdG5JZKQWUAojDaECeqSAFvjsc6BhGpAf2W4kkGrku3zcn6ByYcqQPIUOWtENsHV5iLwgYi9k6pohy7I%2BwhcvvAS6XVNkMtMify7m2ldlqRg%2FBlo%2Fv8j5tUv53HHzESxoxbNsRayJAhfQTmCBFn4tIqt79rze2ijHA4bBTnJ1gxPuDh1rt6a5k28MPuCaI2HfRF54rQpVvKbI0pbAhBjzx5b83iVto1t9SBfLJ1F1FwBV6VwJ23%2B4yc23dNK%2B0bHFvH9eNqBBrLQ43v6xeVsVDZ9xUaueMOLN98kGOqUBmFqtGKus%2BP7Vx6myTJMAcwdrMhysNset8dGKwskWss1d5fm7QGyUVL%2FQ%2Fs0JkAnHjaO3WrcDdv2ZmYc1j4JECShCwFkjx9Bi%2BHJQYi3g1pyAX5n0bRs%2FYlivDeugn%2F7oOHtvEiMsSl1lpw7YqK%2FbyGhaLhZCXCcNIzA0N5zTU%2BTVivNxSnVAhAC%2FQ0diveBxEj4UEJ6ft6Mzoaz%2FCg61N5YFugDQ&X-Amz-Signature=b135ce5e3627361550ae4fd68f14f2be37d9609f6dffc831d599c071219de399&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

To which type a flower belongs to is determined by the following four features:
- Petal length
- Petal width
- Sepal length
- Sepal width

The dataset contains 150 flowers for which the Petal & Sepal length and width has been measured and were classified.
![Extract from the dataset](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f38bd756-87d5-4de7-bcfb-2ad5afc4b71f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SILYV7F%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICFDoS%2F28nSivxk2x4ZOBAw4rVsXwWNd1twMbcXYloSUAiEAgyTlIct8mIZuroKJ7AcIv1vanaw9t5qRO9Uhuv%2Frxhoq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIWvtPpE7wO8dNuyDyrcA6ICYDMVEh9Dto%2BRO%2BNKxDtdI24JwSiDTx19bUQQnjaViApAmTLSC5Q%2B1oE1l8ELH6sz1HoYPOsdTYTvOjng6GUq6jVR%2FSgbzv1ibPrf9TetvmLSOniFIMmeVMl4xNvggfn84IOC78pA2qPB8C46cqxCRwHJS5UTH5e2wxJbylLBnsEpxFzJYrWEj%2BL011U%2F6n13GtUg%2Byu9Zz3jfF7AIr%2Flt42N8J1zd7M56TL5Y1l%2BPLdDJaDmDtbo%2Fec3G1SkKXRfHDCYOtj8WtwA1R7gZDMsY6%2BpRR9%2FyP0exCGR2cGVqNgIsUMg6sIJE2kmLLQ8Vo5nZVsxYovneD%2Fc9Uf6nHL8ZB6JbU9mdG5JZKQWUAojDaECeqSAFvjsc6BhGpAf2W4kkGrku3zcn6ByYcqQPIUOWtENsHV5iLwgYi9k6pohy7I%2BwhcvvAS6XVNkMtMify7m2ldlqRg%2FBlo%2Fv8j5tUv53HHzESxoxbNsRayJAhfQTmCBFn4tIqt79rze2ijHA4bBTnJ1gxPuDh1rt6a5k28MPuCaI2HfRF54rQpVvKbI0pbAhBjzx5b83iVto1t9SBfLJ1F1FwBV6VwJ23%2B4yc23dNK%2B0bHFvH9eNqBBrLQ43v6xeVsVDZ9xUaueMOLN98kGOqUBmFqtGKus%2BP7Vx6myTJMAcwdrMhysNset8dGKwskWss1d5fm7QGyUVL%2FQ%2Fs0JkAnHjaO3WrcDdv2ZmYc1j4JECShCwFkjx9Bi%2BHJQYi3g1pyAX5n0bRs%2FYlivDeugn%2F7oOHtvEiMsSl1lpw7YqK%2FbyGhaLhZCXCcNIzA0N5zTU%2BTVivNxSnVAhAC%2FQ0diveBxEj4UEJ6ft6Mzoaz%2FCg61N5YFugDQ&X-Amz-Signature=8b320b5a57f415220d3c8372de4213fcc7d2f51d456de4e9a4d3a13c94ab16a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We now want to implement a classifier that, based on the Petal and Sepal data, is able to predict the Iris flower type of a new flower that we have collected.
## 1️⃣ Load data
---
We first load the IRIS dataset using the [`.load_iris()`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html) function.
```python
from sklearn.datasets import load_iris

data = load_iris()
```
The data variable is a dictionary containing:
**Feature data of 150 flowers in ****`data.data`**
![Feature data of the 150 flowers visualised in a Pandas DataFrame](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3729280f-b818-40b8-958c-e38fa79117c4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3LUMM5H%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCzX8ZOKhJ0LyATVnwMfdSSBI9aKXW%2Fw4PBjaC%2B4ie0ggIhAM9zD%2B1vQyuSrfQwhnMmiOlZqvSBMQzoCTgdTXnfQx0FKv8DCCcQABoMNjM3NDIzMTgzODA1Igzm72EvX05nnmBJ8yoq3APOhaP6fffw7VjNENeJNaXgLEtnYJnXI3et0yfHicq3ge%2FsEFTHhrw6zqX2SzXg8sc4pEgRNOHo3IITgTbZy9ap1ne503AaaZFTn07aOa7OeBT%2BBmgMbNqUormHXFmkIlrKjKjY9lZxTjNO%2BmFVy3cPHMwGU3w%2B0Dr0Z7HyBWArHMfL0UHqW28CoXdFtw6AoyTlPci%2F3SyJFFLd2xcBIlXW9BrIX6pAtk37m2mqhLFMg2ZF7dhJOggUUDi%2BzwP0g3HnIZaHt7oFyuR2Mm%2Fiq3TJM%2FqrlsbxTxAboH3QR2eKptRHDIiAVM5ukFm1fvdEzZd14ZQrgLwrYqpKyj88mmQzT0h3mSjaOd2g9voXqSbAkIMhwvRC4c1oF2IBk0JU%2FoGs95eRdlkYwpgelrFpdf06nMFvOiLQ9XAQBcx7us2UEGAfmjmYZNSSTZyNLzac29RtxEYHafEePVILLNPGfGQqvOsaJ%2BpIejK%2BHJTN3QMK64EumTrcCRMs%2FKMQICCGiKyX3JtsMxskaPbNddWryq3mq9nFeluZYT%2BGCjMq70XaXD4xp84xmcJ7dR6k8977UXmh0%2BYqgtMe2RDgfG8jkjUTBMGfPV5HoWIsE4g7jMckR6lieVMKE4tVwVOjETCYzvfJBjqkATwvHqXvwx48M5OFF7rO0BC73p9o2efFT%2BoQeYc%2BPZKbzFKOAdAoV91illNSZJp3R99OSEuI7SFCZgGalL5zYHUBkHbs4qZCFwmcYOHMIX4NnlBA0%2FPQkSyQ4SOWSJ0mIxNPgkEyIrQm7chu0SlI%2FggfeVm7zBYP6IjkKVuzKWPKM%2B4ZPsqr%2Bp7bZwNiZHXVkZggNZnQPUCAMurFrgJE6Wn4I1e3&X-Amz-Signature=7bbd6e1b5c0ae10f8b60e41792439cd2c736a69e742335939abefb986ebce959&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**Class numbers of 150 flowers in ****`data.target`**
```python
data.target 

[
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
	2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2
]
```
**Class labels in ****`data.target_names`**
We can see, that each flower is assigned a class numbers. This is something very common we do as it simplify things: We just assign unique numbers to each class. 
- 0 → Setosa
- 1 → Versicolor
- 2 → Virginica
However, we still have the class labels stored:
```python
data.target_names

['setosa', 'versicolor', 'virginica']
```
---
## 2️⃣ Split dataset
---
After having loaded the data we must now split it into training and test data so that we can:
1. Train a classifier for predicting the IRIS flower type
1. Test a classifier to verify whether the classifier does its job well enough
But first let’s save the data we need in new variables: `features` and `labels`
```python
features = data.data
labels = data.target
```
We can now call the function `train_test_split()` to split our data into training and test. Let’s assume we want 80% of the data to be  used as training data and 20% as test data. Therefore, we set parameter `train_size` to `0.8`.
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, labels, random_state = 23, train_size = 0.8)
```
In the variables `X_*` we have now saved the features and in the variables `y_*` the class numbers (all Numpy arrays):
`X_train`
```python
array([[4.9, 3.1, 1.5, 0.1],
       [5.2, 2.7, 3.9, 1.4],
       [5.4, 3.9, 1.3, 0.4],
       [7.7, 2.8, 6.7, 2. ],
       [5. , 3.4, 1.5, 0.2],
       [5.4, 3.9, 1.7, 0.4],
       [6.5, 2.8, 4.6, 1.5],
       [5. , 2.3, 3.3, 1. ],
       [5.7, 3. , 4.2, 1.2],
       [6.3, 3.3, 6. , 2.5],
       [6.9, 3.2, 5.7, 2.3],
       [4.8, 3.4, 1.9, 0.2],
       [5.5, 2.4, 3.7, 1. ],
       [4.6, 3.2, 1.4, 0.2],
       [6.3, 2.3, 4.4, 1.3],
       [6.3, 2.5, 5. , 1.9],
       [4.9, 2.5, 4.5, 1.7],
       [7.9, 3.8, 6.4, 2. ],
       [4.9, 3.1, 1.5, 0.2],
       [5.7, 2.8, 4.1, 1.3],
       [7.4, 2.8, 6.1, 1.9],
       [6.2, 3.4, 5.4, 2.3],
       [5.5, 4.2, 1.4, 0.2],
       [6.1, 2.6, 5.6, 1.4],
       [5.4, 3. , 4.5, 1.5],
       [7. , 3.2, 4.7, 1.4],
       [7.7, 3.8, 6.7, 2.2],
       [5.9, 3. , 4.2, 1.5],
       [5. , 3.6, 1.4, 0.2],
       [6.5, 3.2, 5.1, 2. ],
       [6.7, 3. , 5. , 1.7],
       [4.7, 3.2, 1.6, 0.2],
       [5.8, 2.6, 4. , 1.2],
       [5.1, 3.3, 1.7, 0.5],
       [6.4, 2.8, 5.6, 2.1],
       [5.5, 2.3, 4. , 1.3],
       [6.8, 2.8, 4.8, 1.4],
       [6.4, 2.8, 5.6, 2.2],
       [5.8, 2.8, 5.1, 2.4],
       [6.3, 2.5, 4.9, 1.5],
       [4.9, 3.6, 1.4, 0.1],
       [5. , 3.4, 1.6, 0.4],
       [6.3, 3.4, 5.6, 2.4],
       [4.9, 3. , 1.4, 0.2],
       [4.8, 3.4, 1.6, 0.2],
       [6.8, 3. , 5.5, 2.1],
       [5.8, 2.7, 5.1, 1.9],
       [5.5, 2.5, 4. , 1.3],
       [4.4, 2.9, 1.4, 0.2],
       [5.6, 3. , 4.1, 1.3],
       [6.4, 2.7, 5.3, 1.9],
       [6.2, 2.2, 4.5, 1.5],
       [6.5, 3. , 5.8, 2.2],
       [7.6, 3. , 6.6, 2.1],
       [6.2, 2.9, 4.3, 1.3],
       [4.4, 3.2, 1.3, 0.2],
       [6.1, 2.8, 4. , 1.3],
       [5.6, 2.8, 4.9, 2. ],
       [6.1, 3. , 4.9, 1.8],
       [6. , 2.2, 4. , 1. ],
       [5.2, 3.5, 1.5, 0.2],
       [5.7, 2.8, 4.5, 1.3],
       [6. , 3.4, 4.5, 1.6],
       [5.8, 2.7, 3.9, 1.2],
       [6. , 2.2, 5. , 1.5],
       [5.9, 3.2, 4.8, 1.8],
       [5.5, 2.4, 3.8, 1.1],
       [5.8, 2.7, 5.1, 1.9],
       [7.3, 2.9, 6.3, 1.8],
       [7.2, 3.6, 6.1, 2.5],
       [5.8, 4. , 1.2, 0.2],
       [6.7, 3.3, 5.7, 2.1],
       [5.1, 2.5, 3. , 1.1],
       [5.2, 4.1, 1.5, 0.1],
       [6.8, 3.2, 5.9, 2.3],
       [6. , 3. , 4.8, 1.8],
       [5.1, 3.5, 1.4, 0.2],
       [6. , 2.9, 4.5, 1.5],
       [5.6, 2.7, 4.2, 1.3],
       [6.5, 3. , 5.2, 2. ],
       [4.4, 3. , 1.3, 0.2],
       [4.6, 3.6, 1. , 0.2],
       [5. , 2. , 3.5, 1. ],
       [4.3, 3. , 1.1, 0.1],
       [6.3, 3.3, 4.7, 1.6],
       [5.7, 2.9, 4.2, 1.3],
       [5. , 3.2, 1.2, 0.2],
       [6.7, 2.5, 5.8, 1.8],
       [6.4, 2.9, 4.3, 1.3],
       [5.6, 3. , 4.5, 1.5],
       [5. , 3. , 1.6, 0.2],
       [7.7, 2.6, 6.9, 2.3],
       [6.6, 2.9, 4.6, 1.3],
       [5.9, 3. , 5.1, 1.8],
       [6.3, 2.9, 5.6, 1.8],
       [6.7, 3.1, 4.7, 1.5],
       [5.7, 4.4, 1.5, 0.4],
       [5. , 3.5, 1.6, 0.6],
       [6.5, 3. , 5.5, 1.8],
       [7.2, 3. , 5.8, 1.6],
       [6.7, 3.1, 4.4, 1.4],
       [5.5, 3.5, 1.3, 0.2],
       [6.7, 3. , 5.2, 2.3],
       [4.9, 2.4, 3.3, 1. ],
       [6.7, 3.3, 5.7, 2.5],
       [5.7, 2.6, 3.5, 1. ],
       [4.5, 2.3, 1.3, 0.3],
       [5.3, 3.7, 1.5, 0.2],
       [5.1, 3.7, 1.5, 0.4],
       [6.9, 3.1, 5.1, 2.3],
       [5. , 3.3, 1.4, 0.2],
       [4.8, 3. , 1.4, 0.1],
       [6.3, 2.7, 4.9, 1.8],
       [4.6, 3.4, 1.4, 0.3],
       [5.5, 2.6, 4.4, 1.2],
       [5.1, 3.4, 1.5, 0.2],
       [6.1, 3. , 4.6, 1.4],
       [5.4, 3.4, 1.5, 0.4],
       [5. , 3.5, 1.3, 0.3],
       [6. , 2.7, 5.1, 1.6]])
```
`y_train`
```python
array([0, 1, 0, 2, 0, 0, 1, 1, 1, 2, 2, 0, 1, 0, 1, 2, 2, 2, 0, 1, 2, 2,
       0, 2, 1, 1, 2, 1, 0, 2, 1, 0, 1, 0, 2, 1, 1, 2, 2, 1, 0, 0, 2, 0,
       0, 2, 2, 1, 0, 1, 2, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 1, 1, 2, 1,
       1, 2, 2, 2, 0, 2, 1, 0, 2, 2, 0, 1, 1, 2, 0, 0, 1, 0, 1, 1, 0, 2,
       1, 1, 0, 2, 1, 2, 2, 1, 0, 0, 2, 2, 1, 0, 2, 1, 2, 1, 0, 0, 0, 2,
       0, 0, 2, 0, 1, 0, 1, 0, 0, 1])
```




































































`X_test`
```python
array([[6.9, 3.1, 5.4, 2.1],
       [7.2, 3.2, 6. , 1.8],
       [5.8, 2.7, 4.1, 1. ],
       [4.6, 3.1, 1.5, 0.2],
       [5.7, 2.5, 5. , 2. ],
       [6.9, 3.1, 4.9, 1.5],
       [5.7, 3.8, 1.7, 0.3],
       [6.4, 3.1, 5.5, 1.8],
       [5.4, 3.4, 1.7, 0.2],
       [5.6, 2.9, 3.6, 1.3],
       [6.1, 2.8, 4.7, 1.2],
       [4.8, 3.1, 1.6, 0.2],
       [7.1, 3. , 5.9, 2.1],
       [5.1, 3.8, 1.5, 0.3],
       [5.4, 3.7, 1.5, 0.2],
       [6.3, 2.8, 5.1, 1.5],
       [6.4, 3.2, 4.5, 1.5],
       [6.1, 2.9, 4.7, 1.4],
       [7.7, 3. , 6.1, 2.3],
       [5.2, 3.4, 1.4, 0.2],
       [6.4, 3.2, 5.3, 2.3],
       [4.8, 3. , 1.4, 0.3],
       [5.1, 3.8, 1.6, 0.2],
       [4.7, 3.2, 1.3, 0.2],
       [6.7, 3.1, 5.6, 2.4],
       [5.1, 3.5, 1.4, 0.3],
       [5.1, 3.8, 1.9, 0.4],
       [6.2, 2.8, 4.8, 1.8],
       [6.6, 3. , 4.4, 1.4],
       [5.6, 2.5, 3.9, 1.1]])
```
`y_test`
```python
array([2, 2, 1, 0, 2, 1, 0, 2, 0, 1, 1, 0, 2, 0, 0, 2, 1, 1, 2, 0, 2, 0,
       0, 0, 2, 0, 0, 2, 1, 1])
```
---
## 3️⃣ Choose classifier
---
Now since we have our data ready, we can start thinking about the classifier we want to use. This heavily depends on a few factors such as availability of class labels, if data is numeric or text, how much data we have, computational power available, etc.
Thus, it is impossible to say one classifier is always better than the other. In fact, often we train and test multiple classifier, compare their results and then choose the best performing eventually.
As we have the class labels available (supervised Machine Learning), we can use for example a Linear Support Vector Classifier. To create / initialise the classifier we can call the [`LinearSVC()`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html) method.
```python
from sklearn.svm import LinearSVC

clf = LinearSVC()
```
---
## 4️⃣ Train classifier
---
Now the time has come to train our classifier with our training data.
To do so, we can call the [`.fit()`](/9e4a78074aea481ca4c75e506d4671c7#20d78b49859941fc86e5fb9b559b130a) method and provide the features of the training data ([`X_train`](/9e4a78074aea481ca4c75e506d4671c7#b37b9b49267148dbaa73a1553a0c7cf6)) and the corresponding class numbers ([`y_train`](/9e4a78074aea481ca4c75e506d4671c7#0c4061bfb62347eb8c629e15ea500e22)).
```python
clf.fit(X_train, y_train)
```
---
## 5️⃣ Test classifier
---
As our classifier has been trained now we can finally let the classifier to do some magic, i.e., predict something.
To do so, we can use the [`.predict()`](/9e4a78074aea481ca4c75e506d4671c7#b8b1c284765541e6ae0dc2fe30e2f985) method and we provide the features of the test data ([`X_test`](/9e4a78074aea481ca4c75e506d4671c7#6288f1765a994e4e96cec3c5ef3deccf)). Here it is important to note that we don’t provide the class numbers of the test data ([`y_test`](/9e4a78074aea481ca4c75e506d4671c7#5f22e9c6c56847bebc46740cdeb74d08)). Because we want the classifier to predict those. Otherwise it would be as if we would give the student the solutions right away together with the exam, which causes 100% bias. 
```python
y_pred = clf.predict(X_test)
```
We have now saved the predicted class numbers for the 30 test flowers in `y_pred`.
```python
array([2, 2, 1, 0, 2, 1, 0, 2, 0, 1, 1, 0, 2, 0, 0, 2, 1, 1, 2, 0, 2, 0,
       0, 0, 2, 0, 0, 2, 1, 1])
```
---
## 6️⃣ Evaluate classifier
---
Now after the classifier has predicted the class numbers, we must evaluate how well it has done its job. 
Essentially we need to compare whether the predicted classes in `y_pred` are the same as the actual classes (ground truth) of these 30 flowers, which are saved in `y_test`.
`y_pred`
```python
array(
	[
		2, 2, 1, 0, 2,
		1, 0, 2, 0, 1,
		1, 0, 2, 0, 0,
		2, 1, 1, 2, 0,
		2, 0, 0, 0, 2,
		0, 0, 2, 1, 1
	]
)
```
`y_test`
```python
array(
	[
		2, 2, 1, 0, 2,
		1, 0, 2, 0, 1,
		1, 0, 2, 0, 0,
		2, 1, 1, 2, 0,
		2, 0, 0, 0, 2,
		0, 0, 2, 1, 1
	]
)
```
To perform this check efficiently, we can use the [`classification_report()`](/9e4a78074aea481ca4c75e506d4671c7#edb6797681d048229c93d351b77b476b) function.
```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred, target_names=class_names))
```
![Classification report of the LinearSVC classifier](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/68c20306-1172-44bc-857f-84d71a29282a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LLUVVKI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCKFnyXkjMs0tJOpPxtGXI0uq2yDiuOT%2FdX5dVaup6Y4wIgUkyvjjf70T1CvpwtRcnf%2BQlmL2zIRw1qFLSgOw%2F%2FsAYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJEyhotBWER2wyk9oyrcAzP%2BoRVwNeqIXL4%2FwOFbnirY22AJ274avAEJoLWdUqbA8wnikBvtUcifnM2CWkf3JW5lFiPzKtHnb1kbDwJCRv4Kt2J4PPdCsK5dOuSzTH81Z476RzLqqsAuVsoaWcNYlguC4nmJjssW7RE81z%2FduvuMEOKucqGPUuXYH11FKAA0XdG5IYqvH8yHcLmnHIokktureRiiyC1cZCOZDiD%2BB%2F5zqDisXXcg1aZJgmV0UIHLU9hzpRDx8bAThB%2BEAjS2AEnIny9rmRU2dMHgbnkW2aPqe%2Fmv8rvvf%2BLKSRqcKdiKz7ibM4PUGxUPBiqeuCprKcOzVc3mtGyjDv6CQ5JIuLDy%2BB1%2F8blHqNSpELkuZiiaT7cpFetTHQwH%2FxXjY%2BgfiDuuW%2FzH6fVYca4XYK1KPs6eJw7KvAtb6r1T9zcS%2BNqxK43QKD7c%2FG3Me%2BZaGhAiucKxU%2B0BFku%2BUk0vGAZbNbCdLwaArCodOTjCFfiMPccPYdcXwDoeZUkKVFJ3Z9E048QHNfeolxCmY%2BDXVfwTxcNU0EHeuIX0%2BWfncXWDFrzYxBiiZ14VLfOUGQdWq9ozTGlkf2NDiWJdqsQiWR4PbZig5arGPcZ%2FYvINEQqQ4Y49YJIDWyr1JBlmCHlrMODN98kGOqUBzkOt%2BHwU3%2FHC4iin12ItFyZXoiCj1nUCYl4jKlAWz%2BFGnvQMfxgBc2%2BZY6hSTJOxIkV4C4IFh6APbKuXKuLqw6Vp39OeoKjAr6m2tLQzWmbIuL3JUj3ZRV43GepxmaE%2Fjce8aoN%2BUnW1hNkcnP8uUFWcu16LhNQuaFRRdcHdQP11Otytp6Lc73DPFr9ugbSBwx0%2BbOtfOupCSUDcO%2F337wfUtmuX&X-Amz-Signature=78f74887fa15165892125c01da042189680c092d1ffb2f1dd905b82e5a5708ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see, that the classifier is performing quite well as all three key metrics are 96% and above. 
However, can we improve the classifier further? We have at least two options:
- [Perform cross validation](/ce8b46807fc14f28839eb7b27e773558) and / or [hyperparameter tuning](/6f3849438ae34a63b08483bec1d2a14d)
- Run another classifier on the same dataset and compare its result
---
If we run another classifier over the data, for example, [k-Nearest-Neighbor](/4e55bc27409940e98f9a060821d07644), we can see that the results are better / perfect.
```python
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier()

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred, target_names=class_names))
```
![Classification report of the kNN classifier](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2732fc10-9524-4c97-9fd6-9b0b64e458fe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LLUVVKI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCKFnyXkjMs0tJOpPxtGXI0uq2yDiuOT%2FdX5dVaup6Y4wIgUkyvjjf70T1CvpwtRcnf%2BQlmL2zIRw1qFLSgOw%2F%2FsAYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJEyhotBWER2wyk9oyrcAzP%2BoRVwNeqIXL4%2FwOFbnirY22AJ274avAEJoLWdUqbA8wnikBvtUcifnM2CWkf3JW5lFiPzKtHnb1kbDwJCRv4Kt2J4PPdCsK5dOuSzTH81Z476RzLqqsAuVsoaWcNYlguC4nmJjssW7RE81z%2FduvuMEOKucqGPUuXYH11FKAA0XdG5IYqvH8yHcLmnHIokktureRiiyC1cZCOZDiD%2BB%2F5zqDisXXcg1aZJgmV0UIHLU9hzpRDx8bAThB%2BEAjS2AEnIny9rmRU2dMHgbnkW2aPqe%2Fmv8rvvf%2BLKSRqcKdiKz7ibM4PUGxUPBiqeuCprKcOzVc3mtGyjDv6CQ5JIuLDy%2BB1%2F8blHqNSpELkuZiiaT7cpFetTHQwH%2FxXjY%2BgfiDuuW%2FzH6fVYca4XYK1KPs6eJw7KvAtb6r1T9zcS%2BNqxK43QKD7c%2FG3Me%2BZaGhAiucKxU%2B0BFku%2BUk0vGAZbNbCdLwaArCodOTjCFfiMPccPYdcXwDoeZUkKVFJ3Z9E048QHNfeolxCmY%2BDXVfwTxcNU0EHeuIX0%2BWfncXWDFrzYxBiiZ14VLfOUGQdWq9ozTGlkf2NDiWJdqsQiWR4PbZig5arGPcZ%2FYvINEQqQ4Y49YJIDWyr1JBlmCHlrMODN98kGOqUBzkOt%2BHwU3%2FHC4iin12ItFyZXoiCj1nUCYl4jKlAWz%2BFGnvQMfxgBc2%2BZY6hSTJOxIkV4C4IFh6APbKuXKuLqw6Vp39OeoKjAr6m2tLQzWmbIuL3JUj3ZRV43GepxmaE%2Fjce8aoN%2BUnW1hNkcnP8uUFWcu16LhNQuaFRRdcHdQP11Otytp6Lc73DPFr9ugbSBwx0%2BbOtfOupCSUDcO%2F337wfUtmuX&X-Amz-Signature=35c119f66d885e01503a4875395fd6c19da60a761b0ab5f1dd73d5e50018e6d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Thus, in this scenario it seems to make more sense to go with the kNN classifier.
---
## 7️⃣ Sanity check
---
It is always good to do a quick sanity-check in the end. 
Let’s assume we have the following flower collected.
| Feature | Value |
| --- | --- |
| Sepal length | 5.1 |
| Sepal width | 4.2 |
| Petal length | 1.3 |
| Petal width | 0.6 |
This flower is relatively small as it is of type Setosa. 
Let’s see what the two classifiers tell us. 
```python
# small example flower
flower = np.array([[5.1, 4.2, 1.3, 0.6]])

clf_svc.predict(flower)
array([0]) # predicted class

clf_knn.predict(flower)
array([0]) # predicted class
```
We can see that both classifiers predict class 0 / Setosa. Thus, it seems that everything is working fine. 
---
# TF-IDF procedure
---
> 🔗 **[Jupyter Notebook with code](https://colab.research.google.com/drive/1siYpsW7C3jSt3QSHX6asa3Lot-K985_c?usp=sharing), [dataset](https://drive.google.com/file/d/1bEmTPv7NA05Rx2Loa_t5-_FO1CTB79VG/view?usp=sharing)**
---
Let’s assume we want to implement a classifier that is able to classify whether a movie review is positive or negative. 
![One of 2000 movie reviews in the dataset](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1d633cf8-7c10-463b-8923-8ecc30dcc90b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S52LKJZF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBMNKQZbfIEP3i111Vy12MEIRJpC3KgV2MHYZdcUL9LdAiEAlSuLvpPYWk8JtbnJPbU7%2BFIA3HLDtL%2BOHDYFXrnam6cq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIL0OvT%2BXyN9kZaPtCrcA28MoYwziaPLzq9QZxp8xWl8WoqESI8ddfMd8scydoW87DNbUoM%2BfJ28jqunc9UCKBOou1YU3C5hHkf%2BWnzlQkpmm85o1ZPtaLe8i%2BOlRGPlsFVpYdLcbc41IKxw5IDScs5Y8VbpkNdro2DsI178mSKybyUUE%2FO33wX%2FtR5CQhuNe1cOQhQwHJNAhKdSWbt7g27YsmOmVsxjhE%2BWdzAGolOboxz7zvFBksfzYWphxbOpfkC1e5xNCiqxwKpJPxi0uWWd9NITzSkDbYLsXndY8cO8U5tWhWPHN8zuu5jxbrfX1uywWHzYrAqMPOKHTe6Oc8fhTIeEkBVrMSO7qQ5gNc%2BrUrPrwV0T7V7wl2RmnCmBc1yUpR%2FLJIh82wq6nE383eqgsU7HmEUzhwhx9h63MzPpHgXPwE13thbSjDLfFrPPPOZPC3VRCFmiAlhYSaDJdY6h%2FDJCDdGFad4lBQS4G%2Bdk0tUBjSJDk0gNUBcbFTGMu%2BRJwEPYmQXE9mG%2Ba3eb3QE7xzVH7LDa%2FMSrEwi8VRyoeWJdeLIlC4vcxD%2FYpFe5x8Cbb9ZS3wmwl%2FdD76T2zBa3Ct22F7Dy42FO0PqM78RD5Vn5rTbUNMQzQPpGe7pHuDXl8PK1x%2Bk4MFzfMIbO98kGOqUB87DlBBp3ek9Rc5sWQIJeAc%2BA08tfPF%2F3LxPQLWhfLNYQeea5zRLFB5SWFdf1FPI31Ug4GZwue%2FhO3O2PLypSzvPjUwRmG9nvZKuC92xHWxUoWI%2FEeLraDy88wneWXvOGqAmCngGXQArcu6OYp4hDbn4rP%2BPqOW4FFRbAlG%2BAs%2FWZ%2FOtLqG%2BxNp5wDTEhez%2F8P4%2F8RkGoc3M8I7E85Md22NatebCK&X-Amz-Signature=347cae4fe13e5368cc4847f5af6400a18b650240ce4bdfb045b90c00d787afc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the value in column `text` is the feature, and the value in column `class` (positive or negative) is the information we want to predict with our classifier for a new, previously unknown movie review.
The [dataset](/8c2570fa05b8485fb1e5acf97e094f83) contains 2000 movie reviews, 1000 positive and 1000 negative ones.
We now want to implement a classifier that, based on a movie review text can predict whether the review is positive or negative. We can do that by using the [Bag of Words and TF-IDF approach](/ac27cea2b4b741a7b9ad41c16767e1d5).
## 1️⃣ Load data
---
We first load the dataset from a csv-file by using the [`.read_csv()`](/1867045b058343e1a66b677961515907#bb02198699ce440f948c4c281f1957ac) function.
```python
import pandas as pd

movie_data = pd.read_csv('movie_data.csv')
```
The data is now stored in a Pandas DataFrame:
![movie_data](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ce566bab-2ce5-4ad8-92d4-cb766029c962/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5EXI7VK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGaq1Caaj6sPRwcEjuH15PDC1mNkVw%2BRtPFW4UPPodbbAiEA02xmVh%2BtlM0BfsAv4QW0LD6kzaU%2FpfVVwIq0WgD93JAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDPnUCvISvo7QBvCpVircAziFBnoFnDOdPUBNzwNHBlqBJUvgMsvNoy8LobfUPVJH7SYXEenbbrfVhDB%2Bk1N%2FC4e%2FYLGyVePU%2FzVD0s4sSJkk0evlE84jcNR02Waa9Ki9W5jKXGGrp8SturRj9Dmk9vVemvLJLjkfzj4hfNCEHkWAQhLKGF38NxDKhkYltDTyhpNUGko%2B0KP9M7kbjtevvsV%2B6zDRbRDJAvkKfwQFFlBjs6ri7TiYJQ34ISzezFxYqn4KFAAStSA%2BMCdBtkRQ16gS9ePDmChabRXCQUh3kRok94X7yrUBxQJ79zKAkXGepTfghILZafAkeWsEJDgn4hsw4wN0bGKwA90FSPtHskSHzozKemO4Uy%2B1YbWk%2B5QhEHH7H6a5Md70xy%2FFV%2FcuR4bM32%2F5tHQaa52hxA2c9RK6yj25LqIkLidmVfO%2BcBH6Oe%2Bl9h0x%2FiztfFpvB2TEXzFfYXqbCJ2gePkJI%2Fxx7JRBP0tRS%2Fo6RETV30O8u%2F6NLkWX8g7%2BtBlCJsv1waA%2FwpNOJiOGcB2XLwYkjF6M494M%2FP5fAh77wLgDIwanOmMEChn63m2pZgfJseag9Sszn6Yr%2FipGUgj%2B0IBvsAImBvvJ5ktW7KMmHzq09h03mXugM1oFQa173rptR73nMLTO98kGOqUBSuXkjWpEMfRrlv718lM8Ymug45Swa6hP8bYDOva7UYS6tyg2QcsELJyca8vIm4XrgYlbHgfpR%2F5V%2F05pKa40zV2ESDXXAGVNwOta2%2BSRtKAV0Bi9q52IukuDSGeUzPGt%2BvOmhQl2exarlFDcIqpSQoxFp%2FbXxUTQQgInHQa6OmL4hydGvBu%2FJ86%2FnxG2I%2F%2F%2FJPj2WfpfLYwVv%2FivtVigjc2LLkOj&X-Amz-Signature=197cc36bef309d03126ea25c3edc15855fbd56b307172d7bdd1fc661486f4e45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## 2️⃣ Data transformation
---
Before we can split the data, some transformation is necessary.
**Label ****encoding**
Firstly, we need to create a Label Encoder that is able to transform the text class labels (Pos & Neg) to numerical class labels (0 & 1). We can do that by using the [`LabelEncoder()`](/9e4a78074aea481ca4c75e506d4671c7#a7dc9116d40c4e3093dbbd3bade9d18d) method.
```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(sorted(movie_data['class'].unique()))
```
Now when the Label Encoder is created and knows the dataset, we can transform the ‘Pos’ and ‘Neg’ labels of the 2000 movie reviews.
```python
labels = le.transform(movie_data['class'])

labels
array([1, 1, 1, ..., 0, 0, 0])
```
 As we can see, the labels have been transformed successfully. The text ‘Pos’ was replaced with integer `1` and the text ‘Neg’ with integer `0`.
**Fearture extraction**
Secondly, we need to extract the features, i.e., the movie reviews from the dataframe, which we can do very easily. We simply save all the movie text reviews in a new variable `features`.
```python
features = movie_data['text']
```
---
## 3️⃣ Split dataset
---
After having transformed the data we can now split it into training and test data so that we can:
1. Train a classifier for predicting the class of a movie review
1. Test a classifier to verify whether the classifier does its job well enough
We can now call the function `train_test_split()` to split our data into training and test. Let’s assume we want 80% of the data to be used as training data and 20% as test data. Therefore, we set parameter `train_size` to `0.8`.
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, labels, random_state = 23, train_size = 0.8)
```
In the variables `X_*` we have now saved the features and in the variables `y_*` the class numbers (all Numpy arrays):
`X_train`
```python
1417     the marvelous british actor derek jacobi star...
1075     it was with great anticipation that i sat dow...
929      one of the more unusual and suggestively viol...
788         you leave little notes on my pillow    i t...
748      a movie that s been as highly built up as the...
                              ...                        
950      >from the man who presented us with henry   t...
1993     salaries of hollywood top actors are getting ...
1064     rated   r for strong violence   language   dr...
742      the party is one of those classic slapstick c...
595      hollywood is a pimp    a fat   cigar smoking ...
Name: text, Length: 1600, dtype: object
```
`y_train`
```python
array([0, 0, 1, ..., 0, 1, 1])
```
`X_test`
```python
1945     perhaps best remembered as the recently depar...
912      review  peter jackson s the frighteners has r...
1069     the recent onslaught of film noir that has po...
517      the happy bastard s 30 second review  notting...
1135        dreamworks skg   running time   2 hours st...
                              ...                        
568      eric rohmer s   pauline at the beach     is o...
1860     i guess that if a very wild bachelor party ha...
1872     fact that charles bronson represents one of t...
789      ingredients   lost parrot trying to get home ...
1463     synopsis   melissa   a mentally disturbed wom...
Name: text, Length: 400, dtype: object
```

`y_test`
```python
array([0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
       0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0,
       1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0,
       0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1,
       0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1,
       1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1,
       1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
       0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1,
       0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0,
       1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0,
       1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0,
       1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1,
       1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0,
       0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1,
       0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1,
       0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1,
       1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1,
       0, 0, 1, 0])
```
---
## 4️⃣ Create sparse matrices and apply TF-IDF
---
Now since we are dealing with text data, we need to transform the text into numerical representations, which we can do by using Bag of [Words / Sparse Matrix and TF-IDF](/ac27cea2b4b741a7b9ad41c16767e1d5).
We can do this transformation by using a TfIdfVectorizer. 
```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english')
```
As we can see, we set the parameter `stop_words` to `'english'`. Thus, the vectorizer will ignore and leave out any stop words (and, if, but, etc.) in english that are neutral.
Using the `vectorizer`, we can now transform the training (`X_train`) and test (`X_test`) data separately.
---
**Training data (****`X_train`****)**
To create a sparse matrix and apply TF-IDF to the training data, we can use the [`.fit_transform()`](/9e4a78074aea481ca4c75e506d4671c7#16f816916fcc43318154a1b6b6ea38ae) method. 
```python
X_train = vectorizer.fit_transform(X_train)
```
After the transformation the data is wrapped into a Sparse Matrix and the TF-IDF approach has been applied.
![First, the words in the BoW are put into a Sparse Matrix (transform)](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/410744da-5930-4c2a-88de-7e442a44c4a4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RNE6AUU%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCID5yYuAjVNOCBaBrNcqo%2B1MqwhY5acZCy%2FqTyV%2FiVpQXAiEAyOeDu43i%2F17%2BsKfTz2%2B0D0Yhoe0gEm3smfkbZYNwwHwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOH5or1VaCEvUvkhLCrcA1WpQcGZJzQ42dLlAYnW4uLtwGn3Pw6e1cWe%2B7MT9lzdEr5FgM7vSuBbxBZ9Qqe0gurxtOsAepm1MXQ7v%2Fv6BqlY6vIU1tJig3hHTrFDa2Z3O13HEGKnPgZUi40BCFAubVGNTUu6DMkMk9mXHZismx51g2PZpaUu1PGfLZp50UanhE9sZ4FtYbLKeawSY8oZCDRqrr3%2BAAoHMMR0oX6IyRajtxIp8ZTURzwtYILcYkjOywPl%2BZnF6tFr5tLFBcZracnsuooDNK9DcIi7YCREtSUxJf2DGrCwGZbNohd9MgRlBJ%2FepOgiH4%2FDhPrdY9Bata9F%2BYvPqA4ndWWAHENDlWrQdZYuD%2BPrB7QwLEBYuHa7J6ncwdTIGFPFi0NqyJOOK%2B0k71Mz7qrDouR2LO9VAjlUaNVveOIddJ%2FUsUerjyQbQfLnq9RTZm3TKK4EqHxMmew5%2BUt6zJmlYXVRrmJo0e159M2VELSwqVtrv1YApivN7jyYr8acon6WDeox87VqcSlmXGRHsrxMpoSh0V80Ew0nnPhC8VIuFmys%2BDStSaK1ZAKszBxefiRFmx%2FwE4hqrKoOBggFMA0UpQ7BMpKL7VXtg6NOYEjjUUGHjxxExsth5W3fx0yzq9P66treMLPO98kGOqUBaURFIEAuyMdLc%2F%2BruA21X4nX8%2BUJHQkmIqufH7xkoQrYXkCns6YR2BysoaUHwcKwrsEzHj2Wmoh%2BPZpRjugnGGRrEa4ybnaqIqVhruTV9Ae5lB7VIdhRe9vNuMNYQ35h%2FJr7U8rh0lF0KFl6ydiINrxGDdymI6Ap4hrMgw0794utFzJPUsMsvk0M6gsEeJrWQTiSylzVpudU5XEndSoC%2BIYmrn8i&X-Amz-Signature=fd4cb2be9fa9c80162da9e481230bbe82f07fb553b5439ce0b96f7fa22562d4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Second, the weights are updates according to TF-IDF (fit)](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8e047809-aa29-4893-8fe1-85a8ef6cfc5c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RNE6AUU%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCID5yYuAjVNOCBaBrNcqo%2B1MqwhY5acZCy%2FqTyV%2FiVpQXAiEAyOeDu43i%2F17%2BsKfTz2%2B0D0Yhoe0gEm3smfkbZYNwwHwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOH5or1VaCEvUvkhLCrcA1WpQcGZJzQ42dLlAYnW4uLtwGn3Pw6e1cWe%2B7MT9lzdEr5FgM7vSuBbxBZ9Qqe0gurxtOsAepm1MXQ7v%2Fv6BqlY6vIU1tJig3hHTrFDa2Z3O13HEGKnPgZUi40BCFAubVGNTUu6DMkMk9mXHZismx51g2PZpaUu1PGfLZp50UanhE9sZ4FtYbLKeawSY8oZCDRqrr3%2BAAoHMMR0oX6IyRajtxIp8ZTURzwtYILcYkjOywPl%2BZnF6tFr5tLFBcZracnsuooDNK9DcIi7YCREtSUxJf2DGrCwGZbNohd9MgRlBJ%2FepOgiH4%2FDhPrdY9Bata9F%2BYvPqA4ndWWAHENDlWrQdZYuD%2BPrB7QwLEBYuHa7J6ncwdTIGFPFi0NqyJOOK%2B0k71Mz7qrDouR2LO9VAjlUaNVveOIddJ%2FUsUerjyQbQfLnq9RTZm3TKK4EqHxMmew5%2BUt6zJmlYXVRrmJo0e159M2VELSwqVtrv1YApivN7jyYr8acon6WDeox87VqcSlmXGRHsrxMpoSh0V80Ew0nnPhC8VIuFmys%2BDStSaK1ZAKszBxefiRFmx%2FwE4hqrKoOBggFMA0UpQ7BMpKL7VXtg6NOYEjjUUGHjxxExsth5W3fx0yzq9P66treMLPO98kGOqUBaURFIEAuyMdLc%2F%2BruA21X4nX8%2BUJHQkmIqufH7xkoQrYXkCns6YR2BysoaUHwcKwrsEzHj2Wmoh%2BPZpRjugnGGRrEa4ybnaqIqVhruTV9Ae5lB7VIdhRe9vNuMNYQ35h%2FJr7U8rh0lF0KFl6ydiINrxGDdymI6Ap4hrMgw0794utFzJPUsMsvk0M6gsEeJrWQTiSylzVpudU5XEndSoC%2BIYmrn8i&X-Amz-Signature=539bcf0c8fa02a4922c044a0d5f580cedbc991bfb35a435258a309e40e4f60b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Test data (****`X_test`****)**
For the test data, we only want to create a Sparse Matrix, but not apply TF-IDF, because otherwise the classifier would do something with the data, learn something from it and thus be biased. For this reason, we use the [`.transform()`](/9e4a78074aea481ca4c75e506d4671c7#3c583c11477d480d89e97c4211ae4d7b) method, which puts the word into a Sparse Matrix, but does not apply TF-IDF.
```python
X_test = vectorizer.transform(X_test)
```
![With .transform(), the words are put into a Sparse Matrix only, i.e., no TF-IDF transformation is applied](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/410744da-5930-4c2a-88de-7e442a44c4a4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RNE6AUU%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCID5yYuAjVNOCBaBrNcqo%2B1MqwhY5acZCy%2FqTyV%2FiVpQXAiEAyOeDu43i%2F17%2BsKfTz2%2B0D0Yhoe0gEm3smfkbZYNwwHwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOH5or1VaCEvUvkhLCrcA1WpQcGZJzQ42dLlAYnW4uLtwGn3Pw6e1cWe%2B7MT9lzdEr5FgM7vSuBbxBZ9Qqe0gurxtOsAepm1MXQ7v%2Fv6BqlY6vIU1tJig3hHTrFDa2Z3O13HEGKnPgZUi40BCFAubVGNTUu6DMkMk9mXHZismx51g2PZpaUu1PGfLZp50UanhE9sZ4FtYbLKeawSY8oZCDRqrr3%2BAAoHMMR0oX6IyRajtxIp8ZTURzwtYILcYkjOywPl%2BZnF6tFr5tLFBcZracnsuooDNK9DcIi7YCREtSUxJf2DGrCwGZbNohd9MgRlBJ%2FepOgiH4%2FDhPrdY9Bata9F%2BYvPqA4ndWWAHENDlWrQdZYuD%2BPrB7QwLEBYuHa7J6ncwdTIGFPFi0NqyJOOK%2B0k71Mz7qrDouR2LO9VAjlUaNVveOIddJ%2FUsUerjyQbQfLnq9RTZm3TKK4EqHxMmew5%2BUt6zJmlYXVRrmJo0e159M2VELSwqVtrv1YApivN7jyYr8acon6WDeox87VqcSlmXGRHsrxMpoSh0V80Ew0nnPhC8VIuFmys%2BDStSaK1ZAKszBxefiRFmx%2FwE4hqrKoOBggFMA0UpQ7BMpKL7VXtg6NOYEjjUUGHjxxExsth5W3fx0yzq9P66treMLPO98kGOqUBaURFIEAuyMdLc%2F%2BruA21X4nX8%2BUJHQkmIqufH7xkoQrYXkCns6YR2BysoaUHwcKwrsEzHj2Wmoh%2BPZpRjugnGGRrEa4ybnaqIqVhruTV9Ae5lB7VIdhRe9vNuMNYQ35h%2FJr7U8rh0lF0KFl6ydiINrxGDdymI6Ap4hrMgw0794utFzJPUsMsvk0M6gsEeJrWQTiSylzVpudU5XEndSoC%2BIYmrn8i&X-Amz-Signature=fd4cb2be9fa9c80162da9e481230bbe82f07fb553b5439ce0b96f7fa22562d4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## 5️⃣ Choose classifier
---
Now since we have our data ready, we can start thinking about the classifier we want to use.
Since we are dealing with text data, a Naive Bayes classifier is a good option to use, [Multinominal Naive Bayes](https://www.google.com/search?client=safari&rls=en&q=multinominal%20naive%20bayes&ie=UTF-8&oe=UTF-8) specifically.
To create / initialise the classifier we can call the [MultinominalNB()](/9e4a78074aea481ca4c75e506d4671c7#b625a93454cc46a99191cae86fa4d7e9) method.
```python
from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
```
---
## 6️⃣ Train classifier
---
Now the time has come to train our classifier with our training data.
To do so, we can call the [`.fit()`](/9e4a78074aea481ca4c75e506d4671c7#20d78b49859941fc86e5fb9b559b130a) method and provide the features of the training data ([`X_train`](/9e4a78074aea481ca4c75e506d4671c7#dbad861bd4d1484db84b255893f8ebf4)) and the corresponding class numbers ([`y_train`](/9e4a78074aea481ca4c75e506d4671c7#709e41fe5e494797b8c135f33fcea5bc)).
```python
clf.fit(X_train, y_train)
```
---
## 7️⃣ Test classifier
---
As our classifier has been trained now we can finally let the classifier do some magic, i.e., predict something.
To do so, we can use the [`.predict()`](/9e4a78074aea481ca4c75e506d4671c7#b8b1c284765541e6ae0dc2fe30e2f985) method and we provide the features of the test data ([`X_test`](/9e4a78074aea481ca4c75e506d4671c7#f9aee208e0f64806948f3e08ce0147e9)). Here it is important to note that we don’t provide the class numbers of the test data ([`y_test`](/9e4a78074aea481ca4c75e506d4671c7#80073099cb3743e091bc30c9168fec57)). Because we want the classifier to predict those. Otherwise it would be as if we would give the student the solutions right away together with the exam, which causes 100% bias. 
```python
y_pred = clf.predict(X_test)
```
In the end, the class whose sum of weights is higher will be assigned to a review in the test data set. We know the weights per word from the [TF-IDF adjusted Sparse Matrix](/9e4a78074aea481ca4c75e506d4671c7#8b164bdaa66c43b7b7df096e006d68f8).
We have now saved the predicted class numbers for the 400 movie reviews in `y_pred`.
```python
array([0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1,
       0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0,
       0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
       0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1,
       0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1,
       1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
       0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0,
       0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1,
       0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0,
       1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0,
       1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0,
       1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
       1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
       0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1,
       0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0,
       0, 0, 0, 0])
```
---
## 8️⃣ Evaluate classifier
---
Now after the classifier has predicted the class numbers, we must evaluate how well it has done its job. 
Essentially we need to compare whether the predicted classes in `y_pred` are the same as the actual classes (ground truth) of these 30 flowers, which are saved in `y_test`.
`y_pred`
```python
array([0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1,
       0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0,
       0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
       0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1,
       0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1,
       1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
       0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0,
       0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1,
       0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0,
       1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0,
       1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0,
       1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
       1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
       0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1,
       0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0,
       0, 0, 0, 0])
```
`y_test`
```python
array([0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
       0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0,
       1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0,
       0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1,
       0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1,
       1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1,
       1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
       0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1,
       0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0,
       1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0,
       1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0,
       1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1,
       1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0,
       0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1,
       0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1,
       0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1,
       1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1,
       0, 0, 1, 0])
```
To perform this check efficiently, we can use the [`classification_report()`](/9e4a78074aea481ca4c75e506d4671c7#edb6797681d048229c93d351b77b476b) function.
```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred, target_names=le.classes_))
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f1266592-6478-4eca-9fee-675f35a3d861/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663G2QITN5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCmSNkhi7q5aFW7Lrs3JySSXKPvkSvjKWqFq2wKgT%2F81gIgJq47CVKxhcXDXrTTtSufupYtmk87QE6Tn1wJCSbBytcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDCaIGLxMPX0kaouyCircA%2BPoyMq5ZSezj4VRyzN3VR7dgGkHVgnCaEowgrl46o8WolaD3LS30gXkSN8MqK31GgqPEJEikWxqWYEHsyGR5%2BceLfJMNYUvcZPJZE4bhRp2JR0bedWrk7wEPhxgkdCZZmYQLg0fliUl5tNhs%2FK4lzanI5gl4IH6JepiPse54cu191bAUlI0kYn10u3maAmR2a0tkuiNNpRwyYaZnV61RVFA4d%2BT%2FwZpLg%2FFqwY1ICCdn7VVKx6mNtV1fIpJ77yZKpT7JfGiqtaCRzsn8o%2F6g%2FEN48WSb3neXznUzvgELKpcJEtXCEese9qqpzxtYfA7KclTGOV%2FboXumE94iBgr3kBCHidViJ2nn5RyFvs8cPcx6U1p%2FKeOX6bl5Iu%2FVRwU07ptKZ2p46f%2F5xQfO3gQ1cgwiGEcFRbzuishvWHijdhANoibxHDX%2BkytFzgDl%2BrdERrl%2BdiW4h5Xk6lhZ4WMGdQCLg5NxhhoX4vEQmtseQFefzeqTLH%2B6aO4nf%2BdP8pwGMHt3pHqAxEbhi1Xv8Dye6sGu3PDoxg%2FIYVXwfNQONCG1aNc3IrxzWZLmPacNz3X1Q9C1%2BCVC0QPOsnvylDO5v290fBSbZf4CwNrbmTo1tWE0AXPEWCRCgkXaju9MLTO98kGOqUBxjPTwdBg%2By2dNC3qhIn9OGabof6U5Eq0IzBqu8bSuwFrHRjqORSk17TolDWlXyDkJm4w278t%2B%2F%2BFCXt6G%2BXZVrTn5hllAcjS2Mmgr9zH54eySepl9Xx6AQj18odt4xEv7lM%2Ft%2BtWJShBIR8GQn24bVbQSreH4sRsLujtyQNt7fTTbnACT6QwZUNR%2BNQ%2FxFFeIDSeseZ40slrvcD7UKyFILufEs2h&X-Amz-Signature=ec6dbbca9a0425e11d1991e6b3324a51c9c52c594c9235edcf65686b987d794b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see, that the classifier is performing well as all three key metrics are 78% and above. 
However, can we improve the classifier further? We have at least two options:
- [Perform cross validation](/ce8b46807fc14f28839eb7b27e773558) and / or [hyperparameter tuning](/6f3849438ae34a63b08483bec1d2a14d)
- Run another classifier on the same dataset and compare its result
---
## 9️⃣ Sanity check
---
It is always good to do a quick sanity-check in the end. 
Let’s say we want to classify a simple text:
*‘This movie was one of the most interesting ones that I have seen in the last few years.’*
If we read this review, then obviously we interpret is as a positive one. But what does the classifier say?
```python
# create random movie review
review = np.array(['This movie was one of the most interesting ones that I have seen in the last few years.'])

# put text into Sparse Matrix
text = vectorizer.transform(review)

# make prediction
clf.predict(text)

# prediction made by classifier
array([1])
```
We can see that the classifier predicted our movie review to be positive. Thus, it seems that we can approve the sanity check.
---

