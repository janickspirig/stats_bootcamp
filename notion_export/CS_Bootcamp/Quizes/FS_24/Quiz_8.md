---
title: "Quiz 8"
notion_id: "34c652ab-87c8-4988-8e67-a6cf346e40bf"
notion_url: "https://www.notion.so/Quiz-8-34c652ab87c849888e67a6cf346e40bf"
exported_at: "2025-12-13T23:10:06.261069+00:00"
---

# Quiz 8

## Question 1
Sie sind im Darknet auf alle Noten der letzten FCS-Kurse gestossen. Darin ist detailliert aufgeschlüsselt, wie engagiert sich die jeweiligen Studierenden vorbereitet haben. Es ist die Anwesenheit in den Vorlesungen und Übungen aufgezeichnet, (anwesend/nicht anwesend), die Verweildauer auf *Canvas*, sowie die jeweiligen Quizresultate, und natürlich die erreichte Note (1.0 bis 6.0, in 0.25-Schritten).
Sie möchten nun Ihre Note durch ein KNN-Modell vorhersagen lassen.
Markieren Sie **alle korrekten Aussagen**:
✅ Zur Validierung Ihres Ansatzes sollten Sie scikit-learns train_test_split-Funktion benutzen, um den Datensatz in zwei Teile zu teilen.
❌ Die Aufgabe ist ein *unsupervised Clustering*.
✅ Da der Datensatz mehrere tausend Einträge beinhaltet und damit als *gross* gilt, ist KNN nicht besonders gut als Modell geeignet.
❌ Das Training eines KNN-Modells ist nicht möglich, da die Features mehr als zwei Dimensionen (Anwesenheit, Verweildauer, Ergebnis Quiz 1, Ergebnis Quiz 2, ...) besitzen.
✅ Die Aufgabe ist eine Klassifikation.
❌ Die Aufgabe ist eine Regression.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[train_test_split()](/9e4a78074aea481ca4c75e506d4671c7#4929175cb8d34b8f97fbaca1a2271458), [supervised vs. unsupervised learning](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617), [KNN algorithm](/4e55bc27409940e98f9a060821d07644)**
Let's break down the provided statements and understand why the correct answers are marked as they are.
✅ **Correct, **when working with machine learning models, it's important to validate your approach to ensure it performs well on unseen data. The `train_test_split` function from the `scikit-learn` library is commonly used to split the dataset into a training set and a testing set. This helps in evaluating the model's performance.
❌ **Incorrect,** unsupervised clustering is used when you want to group data points into clusters without predefined labels. In this case, you have labeled data (grades), and you want to predict these labels based on features like attendance and quiz results. This is a supervised learning task, not unsupervised clustering.
✅ **Correct,** K-Nearest Neighbors (KNN) can be computationally expensive, especially with large datasets. This is because KNN requires calculating the distance between the query point and all points in the dataset to find the nearest neighbors. With thousands of entries, this can become very slow and resource-intensive.
❌ **Incorrect,** KNN can handle datasets with multiple dimensions (features). The number of dimensions does not prevent the training of a KNN model. In fact, KNN can work with any number of features, although the computational cost increases with the number of dimensions.
✅ **Correct,** the task is to predict the grade, which falls into discrete categories (e.g., 1.0, 1.25, 1.5, etc.). This makes it a classification problem because you are predicting a categorical outcome based on the input features.
❌ **Incorrect,** Regression is used when the target variable is continuous. In this case, the grades are discrete and fall into specific categories, making it a classification problem rather than a regression problem.
</details>
---
## Question 2
Sie haben in der Vorlesung *k-fold Cross-Validation* kennengelernt. Welche der folgenden Aussagen treffen zu?
Markieren Sie alle richtigen Aussagen.
❌ Jeder Datenpunkt kann mehrmals als Testdatenpunkt in der gesamten *K-Fold Cross-Validation* auftreten.
❌ Bei *K-Fold Cross-Validation* wird ein Modell erstellt, das iterativ auf den jeweiligen Folds trainiert wird.
✅ Bei der *K-Fold Cross-Validation* wird jeder Fold genau einmal als Testset verwendet.
❌ Bei *K-Fold Cross-Validation* wird das Modell nur einmal trainiert und dann auf einem einzigen Testset ausgewertet.
✅ *Cross-Validation* hilft Overfitting zu erkennen und zu vermeiden.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[k-fold Cross-Validation](/ce8b46807fc14f28839eb7b27e773558#bb510ed5d50e4570bd1cdc371c4d549c)**
### What is k-fold Cross-Validation?
K-fold Cross-Validation is a technique used in machine learning to evaluate the performance of a model. It involves splitting the dataset into `k` equally sized folds (subsets). The model is trained `k` times, each time using a different fold as the test set and the remaining `k-1` folds as the training set. This process helps in getting a more reliable estimate of the model's performance.
### Explanation of the Answer Options
❌ **Incorrect, i**n k-fold Cross-Validation, each data point is used exactly once as a test data point. This ensures that every data point is tested for its predictive power, but it does not appear more than once in the test set.
❌ **Incorrect,** while it is true that a model is trained iteratively on different folds, the statement is misleading because it suggests that a single model is iteratively updated. In reality, separate models are trained from scratch on each fold. Therefore, this statement is not entirely accurate.
✅ **Correct,** this is a fundamental property of k-fold Cross-Validation. Each fold is used exactly once as the test set, ensuring that every data point is tested once.
❌ **Incorrect,** this statement describes a simple train-test split, not k-fold Cross-Validation. In k-fold Cross-Validation, the model is trained `k` times, each time on a different training set and evaluated on a different test set.
✅ **Correct,** Cross-Validation, including k-fold Cross-Validation, helps in detecting and preventing overfitting. By evaluating the model on multiple test sets, it ensures that the model's performance is consistent and not just tailored to a specific subset of the data.
</details>
---
## Question 3
Ordnen Sie folgende Probleme der entsprechenden Kategorie zu.
**Klassifikation**
- Vorhersage von Aktienkurs (Steigend/Sinkend)
- IRIS-Datensatz

**Regression**
- Vorhersage von Aktienwerten
- Kreditrisikovorhersage (0-100%)
- Vorhersage der Länge der Blüten für den IRIS-Datensatz

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Classification vs. regression](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617)**
### Klassifikation (Classification)
Classification problems involve predicting a category or class label from a set of possible categories. Here are the examples given:
- **Vorhersage von Aktienkurs (Steigend/Sinkend)** 
This problem involves predicting whether a stock price will go up (steigend) or down (sinkend). There are only two possible outcomes, making it a binary classification problem.
- **IRIS-Datensatz** 
The IRIS dataset is a famous dataset in machine learning used for classification. It involves predicting the species of an iris flower (Setosa, Versicolor, or Virginica) based on features like petal length, petal width, etc. This is a multi-class classification problem.
### Regression
Regression problems involve predicting a continuous value. Here are the examples given:
- **Vorhersage von Aktienwerten
**This problem involves predicting the actual value of a stock price, which is a continuous number. Therefore, it is a regression problem.
- **Kreditrisikovorhersage (0-100%)
**This problem involves predicting the credit risk as a percentage between 0 and 100. Since the output is a continuous value, it is a regression problem.
- **Vorhersage der Länge der Blüten für den IRIS-Datensatz
**This problem involves predicting the length of the petals or sepals of iris flowers, which are continuous values. Therefore, it is a regression problem.
</details>
---
## Question 4
Markieren Sie alle wahren Aussagen bezüglich *Supervised Machine Learning* ("überwachtes maschinelles Lernen").
❌ Eine Regression ist kein *Supervised Machine Learning* ("überwachtes Lernverfahren"), da es keine diskreten Klassen, sondern stetige ("continuous") Zielwerte hat.
✅ Für ein glaubwürdiges Modell, das in einem *Supervised Machine Learning*-Ansatz trainiert werden soll, muss zwingend mindestens ein Train/Test-Split des Datensatzes durchgeführt werden.
❌ *Supervised Learning* hat die Bezeichnung daher, dass nach jedem Trainingsbeispiel eine menschliche Interaktion nötig ist.
❌ Die Erkennung von statistischen Ausreissern ("outlier") wird üblicherweise *supervised* ausgeführt.
✅ Wenn ein Datensatz neben den Features auch jedem Eintrag eine Klasse zugeordnet, kann darauf ein *supervised Machine Learning* Modell trainiert werden.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Supervised machine learning](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617)**
❌ **Incorrect,** Regression is indeed a type of Supervised Machine Learning. In supervised learning, the model is trained on labeled data, which means each training example is paired with an output label. Regression deals with continuous target values (like predicting house prices), while classification deals with discrete classes (like identifying if an email is spam or not). Both are forms of supervised learning.
✅ **Correct, **in supervised learning, it is essential to split the dataset into at least two parts: a training set and a test set. The training set is used to train the model, and the test set is used to evaluate its performance. This helps ensure that the model generalizes well to new, unseen data and is not just memorizing the training data.
❌ **Incorrect,** the term "supervised" in supervised learning does not imply that human interaction is needed after each training example. Instead, it means that the learning algorithm is provided with input-output pairs (labeled data) during training. The "supervision" comes from these labels, not from human intervention during the learning process.
❌ **Incorrect, **outlier detection is typically an unsupervised learning task. It involves identifying data points that deviate significantly from the rest of the dataset. Since outliers are not usually labeled in the data, unsupervised methods are often used to detect them.
✅ **Correct**, because supervised learning requires labeled data. If each entry in the dataset has associated features (input variables) and a class label (output variable), then a supervised learning model can be trained on this data. The model learns to map the features to the corresponding class labels.
</details>
---

