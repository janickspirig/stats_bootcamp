---
title: "Quiz 11"
notion_id: "7ff79086-266b-4a54-8621-31d9ff40d70c"
notion_url: "https://www.notion.so/Quiz-11-7ff79086266b4a54862131d9ff40d70c"
exported_at: "2025-12-14T01:03:58.580954+00:00"
---

# Quiz 11

# Question 1
In je mehr Dokumenten ein Wort vorkommt, umso höher ist die Inverse *Dokumentenfrequenz (idf)*. Wahr oder Falsch?
❌ Wahr
✅ Falsch

<details>
<summary>Explanation</summary>

> 💡 **[tf-idf](/ac27cea2b4b741a7b9ad41c16767e1d5#3380ebe081cf4aa9b9e54fe6714fc829)**
The more a word appears across documents the **less meaningful** it is for assigning a class (e.g. positive or negative) to the document. Thus, the **idf-score** of a word that appears often will be **lower** compared to a word that rarely occurs.
</details>
---
## Question 2
Sie entwickeln ein maschinelles Lernsystem, um den medizinischen Bedarf von Patienten vorherzusagen. Sie haben 100 verschiedene mögliche Behandlungen, die Sie aufgrund von Patienteninformationen zuweisen können. Sie haben festgestellt, dass die Vorhersagegenauigkeit für Patienten mit seltenen Allergien tendenziell geringer ist.
Welche der folgenden Aussagen treffen zu? Markieren Sie alle richtigen Aussagen.
❌ Die seltenen Allergien der Patienten werden besser ignoriert und nicht in das Modell zur Vorhersage einbezogen.
❌ Accuracy wird als einzige Metrik verwendet, um die Leistung des Modells bei der Vorhersage von seltenen Allergien zu bewerten.
✅ Training- und Test-Set sollten disjunkt sein (kein Datenpunkt befindet sich in mehr als einem der zwei Sets).
✅ Sie verwenden eine stratifizierte Aufteilung zwischen dem Training und dem Testset, um die Genauigkeit der Vorhersagen für Patienten mit seltenen Allergien zu verbessern.
❌ Bei dieser Aufgabe handelt es sich um eine Regressionsanalyse.
✅ Bei dieser Aufgabe handelt es sich um eine Klassifikationsaufgabe.

<details>
<summary>Explanation</summary>

> 💡 **[accuracy with imbalanced dataset](/3ca737faa7034fb9b1150be74f7f4430#78718402c90345c3b48288c2366ce503), [train-test split](/ac27cea2b4b741a7b9ad41c16767e1d5#3f214527ee3f4c38bc6e506187a44555), [classification vs. regression](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617)**
❌ **Incorrect**. We should be **very careful** with excluding outliers, i.e., patients with rare allergies. Being able to predict rare allergies was maybe the core motivation for developing a classifier in the first place, so by excluding these patients there is no reason for developing a classifier.
❌ **Incorrect**. The rare allergies will likely be **under-represented** in the test data. Thus, the classes will be **imbalanced**. Whenever we are dealing with an imbalanced dataset Accuracy is likely **not the best metric** to measure model performance.
Let’s assume there are **100 patients** in out rest dataset. **95** patients have a **common** allergy and **5** patients a **rare** allergy. Now, in all cases the model predicts the common allergy and we get an accuracy score of:
$$
\text{Accuracy} = \frac{95}{95 + 5} = 95\%
$$
In this case the accuracy score of 95% indicates that the model is performing very well. However, our model actually has **mis-classified all patients with a rare allergy** and thus performs **very poorly**. Hence, the accuracy score of 95% is **misleading**, which is caused by the **imbalanced** dataset.
✅ **Correct**. If observations are in both, test and training data, our model will be **biased** as it has seen the solution before solving the exam.
✅ **Correct**. It is advisable to split the data between training and test dataset with some degree of **randomness**.
❌ **Incorrect**. This is a **supervised** classification task. We have a **predefined set of classes **(the different allergies) that should be assigned to observations (patients). Regression analysis is used to predict a numerical value such as the remaining days the patients have left to live. 😢
---
</details>
---
# Question 3
Gegeben ist folgender (partieller) Classification Report aus *scikit-learn*.
|  | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
| setosa | 0,85 | 0,92 | 0,76 | 18 |
| versicolor | 0,93 | 0,93 | 0,93 | 14 |
| virginica | 0,89 | 0,85 | 0,87 | 13 |
Einer der F1-Score-Werte in der Tabelle ist falsch. Berechnen Sie den richtigen F1-Score für die entsprechende Zeile. Geben Sie das Ergebnis auf zwei Dezimalstellen korrekt an.
**0,88**

<details>
<summary>Explanation</summary>

> 💡 **[f1-score](/3ca737faa7034fb9b1150be74f7f4430#9aabbb38114445a694155a99c1818adf), [precision](/3ca737faa7034fb9b1150be74f7f4430#8f3e40c59c36482197bc746cf80dbc50), [recall](/3ca737faa7034fb9b1150be74f7f4430#5ef7c9301e424eaf85bdfe87d032c836)**
Check below the calculation for each class in the IRIS dataset.
**Setosa**
$$
\text{f1-score} = \frac{2 * 0.85 * 0.92}{0.85 + 0.92} = 0.88
$$
**Versicolor**
$$
\text{f1-score} = \frac{2 * 0.93 * 0.93}{0.93 + 0.93} = 0.93
$$
**Virginica**
$$
\text{f1-score} = \frac{2 * 0.89 * 0.85}{0.89 + 0.85} = 0.87
$$
We can now see that the f1-score for **Setosa** was not correct. It is **0.88** and not 0.76.
</details>
---
# Question 4
Ordnen Sie folgende Probleme der entsprechenden Kategorie zu. 
Klassifizierung
- Wine-Datensatz
- IRIS-Datensatz
Regression
- Vorhersage des Aktienkurs
- Kreditrisikovorhersage
- Vorhersage der Länge der Blüten für den IRIS-Datensatz

<details>
<summary>Explanation</summary>

> 💡 **[types of machine learning](/9b19eda74fac4ffb8e48b36dde3b47a4#01794db861444cd59c57237ad722e617), [datatypes](/8abd5dae91fc4e90b63453e6d4a80952#058e2f9345364edcb90e0a46f4ba6c36), [regression](/3b0dfaa603e642b498b666d147d66714)**
Here we need to ask ourselves what kind of data type we want to predict?
- type of wine → <u>categories</u> → **classification** 
- type of flower → <u>categories</u> → **classification** 
- stock price → <u>numerical value</u> → **regression** 
- risk score → <u>numerical value</u> → **regression**
- length of flower → <u>numerical value</u> → **regression**
</details>
---
# Question 5
Sie haben in der Vorlesung *k-fold Cross-Validation* kennengelernt. Welche der folgenden Aussagen treffen zu? Markieren Sie alle richtigen Aussagen.
✅ Cross-Validation kann helfen Overfitting zu erkennen und zu vermeiden.
✅ Bei der *K-Fold Cross-Validation* wird jeder Fold genau einmal als Testset verwendet.
❌ Jeder Datenpunkt kann mehrmals als Testdatenpunkt in K-Fold Cross-Validation auftreten.
❌ Bei *K-Fold Cross-Validation* wird das Modell nur einmal trainiert und dann auf einem einzigen Testset ausgewertet.

<details>
<summary>Explanation</summary>

> 💡 **[k-Fold Cross-Validation](/ce8b46807fc14f28839eb7b27e773558), [Overfitting](/ce8b46807fc14f28839eb7b27e773558)**
✅ **Correct**. By splitting the training and test data into **multiple folds** and running them through **multiple training and test iterations**, the risk of having similar data in the training data decreases. As a result, the performance metrics (accuracy, precision, recall, f1-score) are more **robust** / **representative**.
✅ **Correct**. Each fold is used once as test dataset. In the other training-test iterations the fold is part of the training data.
❌ **Incorrect**. Observations are not duplicated, i.e., the underlying data is not modified.
❌ **Incorrect**. The model will be trained and testes **k**-times. Each fold becomes the test data in one iteration.
</details>
---

