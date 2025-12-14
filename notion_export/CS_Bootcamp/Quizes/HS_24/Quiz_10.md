---
title: "Quiz 10"
notion_id: "17074ffd-3319-8088-959f-f1202ef6a283"
notion_url: "https://www.notion.so/Quiz-10-17074ffd33198088959ff1202ef6a283"
exported_at: "2025-12-13T23:03:33.454475+00:00"
---

# Quiz 10

## Question 1
We learned about *K-Fold Cross Validation*.
Which of the following statements are true? Select all!
❌ K-Fold Cross-Validation will improve the model performance because it is trained on all available data. 
❌ A 1-Fold Cross-Validation is the same as a *train_test_split* with a *train_size* of 50%. 
✅ In a 3-Fold Cross-Validation, each data sample is used 2 times for training and 1 time for validation.
✅ With K-Fold Cross-Validation, the model is trained each fold/split and evaluated on the remaining folds/splits. 
❌ With K-Fold Cross-Validation, the model is trained once and evaluated on multiple data sets.

<details>
<summary>Explanation</summary>

> 💡 **[k-fold cross validation](/ce8b46807fc14f28839eb7b27e773558)**
❌ **Incorrect**, K-Fold Cross-Validation is a technique used to evaluate the performance of a model, not to improve it directly. It helps in assessing how the model will generalize to an independent dataset by splitting the data into K subsets (or folds). The model is trained on K-1 folds and tested on the remaining fold. While it uses all data for training and validation across different iterations, it doesn't inherently improve the model's performance.
❌ **Incorrect**, a 1-Fold Cross-Validation doesn't make sense in the context of K-Fold Cross-Validation because it implies using the entire dataset for both training and testing, which is not possible. In contrast, a *train_test_split* with a *train_size* of 50% means splitting the data into two halves, using one half for training and the other for testing, which is a valid approach but not equivalent to 1-Fold Cross-Validation.
✅ **Correct**, in 3-Fold Cross-Validation, the dataset is divided into 3 equal parts. For each fold, the model is trained on 2 parts and validated on the remaining 1 part. This means each data sample is used twice for training and once for validation across the 3 iterations.
✅ **Correct**, in K-Fold Cross-Validation, the dataset is split into K parts. The model is trained on K-1 parts and evaluated on the remaining part. This process is repeated K times, with each part being used once as the validation set. This helps in getting a more reliable estimate of the model's performance.
❌ **Incorrect**, in K-Fold Cross-Validation, the model is not trained just once. Instead, it is trained K times, each time on a different combination of K-1 folds, and evaluated on the remaining fold. This ensures that every data point gets a chance to be in the validation set exactly once, and in the training set K-1 times.
</details>
---
## Question 2
You're developing a machine learning system to predict the medical needs of patients. You have 100 different distinct possible treatments you can assign based on patient information. You have noticed that the prediction accuracy tends to be lower for patients with rare allergies. With this in mind, mark all true correct statements.
✅ This is a classification task. 
❌ This is a unsupervised clustering task. 
❌ This is a regression task. 
✅ To improve the model's performance, it might be beneficial to do a stratified *train_test_split*. 
✅ Training, Validation, and Test set must be disjunct (no data examples must be in more than one set.) 

<details>
<summary>Explanation</summary>

> 💡 **[Types of machine learning](/9b19eda74fac4ffb8e48b36dde3b47a4)**
✅ **Correct**, in machine learning, a classification task involves predicting a discrete label or category for each input. In this scenario, you have 100 different distinct possible treatments, which are categories. The goal is to assign one of these treatments to a patient based on their information. Since you're predicting categories (treatments), this is indeed a classification task.
❌ **Incorrect**, unsupervised clustering involves grouping data points into clusters based on their similarities without using labeled outcomes. In this case, you have specific labels (treatments) that you want to predict for each patient, which means you are working with labeled data. Therefore, this is not an unsupervised clustering task.
❌ **Incorrect**, regression tasks involve predicting a continuous value, such as predicting a patient's blood pressure or temperature. Since you are predicting discrete categories (treatments) rather than continuous values, this is not a regression task.
✅ **Correct**, A stratified train-test split ensures that each subset of the data (training and testing) has the same proportion of each class as the original dataset. This is particularly useful when dealing with imbalanced data, such as patients with rare allergies, to ensure that the model is trained and tested on a representative sample of each class. This can help improve the model's performance by providing a balanced view of the data.
✅ **Correct**, in machine learning, it's important to keep the training, validation, and test sets separate to ensure that the model is evaluated on unseen data. This helps to prevent overfitting, where the model performs well on the training data but poorly on new, unseen data. By keeping these sets disjoint, you ensure that the model's performance is a true reflection of its ability to generalize to new data.
</details>
---
## Question 3
Which of the listed items are required to correctly define a KNN model.
❌ The problem with this ML model is the non-interpretability of the results (it is a *black box*). 
❌ The data must be scaled. 
✅ A distance metric.
❌ At least a two-dimensional feature set. 
✅ Method for aggregating the classes (simple majority vote, ...).
✅ The value of K.

<details>
<summary>Explanation</summary>

> 💡 **[kNN](/4e55bc27409940e98f9a060821d07644)**
❌ **Incorrect**, while KNN can be considered less interpretable than some models, it is not typically classified as a "black box" model like neural networks. KNN's decision-making process is based on the proximity of data points, which can be visualized and understood.
❌ **Incorrect**, while scaling the data is often recommended for KNN models to ensure that all features contribute equally to the distance calculations, it is not a strict requirement for defining a KNN model. However, without scaling, features with larger ranges can disproportionately affect the distance metric.
✅ **Correct**, a distance metric is essential for a KNN model because it determines how the "closeness" of data points is calculated. Common distance metrics include Euclidean distance, Manhattan distance, and others.
❌ **Incorrect**, KNN can work with any number of dimensions, including one-dimensional data. The requirement is not about the number of dimensions but rather having a feature set to compare.
✅ **Correct**, KNN requires a method to determine the class of a new data point based on its nearest neighbors. A common method is a simple majority vote among the neighbors' classes.
✅ **Correct**, the value of K, which represents the number of nearest neighbors to consider, is a crucial parameter in defining a KNN model. It affects the model's performance and needs to be chosen carefully.
</details>
---
## Question 4
Given is this example dataset with three classes (blue, red, and green):
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9f019e08-7fb9-4758-80a3-943fcb5402db/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XMJM3HV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCID3I7u05ZZnrIJjnmPdwTKJCOR7RCr7gvlc%2B3VyiRDInAiEAoeQyMUdYSSNlzQR0t%2FZWGkvSMMhrpBhAqWsyPlp091Uq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKUqCAFs9ElT29JX%2FircA9ifONRHdwBBIS%2FcSZXSDyWaHFx4wqDoTqIA7ZglsatVInbFnIsd60ufwjVh3O2Yge8YSiAv8W6rUl11btVWjXNeN6ERZgEzHJ5qs%2FjK0cLhME7odRqF2XOWp%2FN6wMX5ZQCeb7ZH0R%2F3SxAEuJK5oGnSR8BTF72KdI%2ByeeWMAzt4gWOPtu8RtYKI8X5cW8MwmZyNjcgAgSmBPv0zWmKYPFWDEu86y3iuvWRjtqUnlUsnbB6XR6mjd9P00VluD0GrYHY78BRrubszNUtIuWekuC16PYwNJ8FZy7hbX53MA%2BYcQ9in8%2BQftllJXkSZqooLwLcK70381t7K1hw6sIT6VRBPJF7saPAyLJi0P3Ib7n9afc45IZtuQl9YOlxNSsay6T%2Fx1zhqjt1QMcRLXUyfWEcZopKz6i5OWCu2MPRknTx3DRjHUyGItUxuFbWoPudEJvXprxcpBr6wX9XJEd9j0ZXdqGbfTuddh2CsvWvBBvJ9lDAo%2FWSbZdsCQsI8NNMlrjhVjx70qrqozkxXFzECGiTTz9Phg%2BfLol8xj9GV3%2BAapExKPK%2FNc6O3Cy1uTLi%2F7lkEl7H6fiQztIhje2TSe68GUU9HZKiKkcffL8ilLF6ZHEu6rjGH6D%2FaFiPMMNHO98kGOqUBu%2F8euU%2F6jNt3jMCQ0pZBant8jlhIhrIcX90pTSvteetl3qqP2MME87SMw%2BpcK46m7ENN58Z93ClvQ7iCeN6qV9e1jCZTs4AKGEOoA0GEjhkWOTLkDlf5vPJHQJ3nNLORQxn8VeA524TrjE%2F8%2FAUnfQCcz0x9CEUsNQswc%2FP5HjV72%2B3iwayeDIFnBZdkejTmmqq0L1UEqdq152GhE4umU5dugqhf&X-Amz-Signature=c0aadecb72d906d0c5fdde86a4e589671de35cba10f81f75d2a0e00bfd50fd74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Which class does a KNN-Model with **k=3** assign to the middle black dot?
✅ green
❌ red
❌ blue
❌ *There is no majority, the classifier with not assign a class.*

<details>
<summary>Explanation</summary>

> 💡 **[kNN](/4e55bc27409940e98f9a060821d07644)**
KNN is a simple, supervised machine learning algorithm used for classification and regression. In classification, it works by finding the "k" closest data points (neighbors) to a given point and assigning the most common class among those neighbors to the point.
Let’s identify first the k (3) closest neighbors of the black dot.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/01426bae-49c9-44e7-83be-c8c729b4aa38/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QZOX67C%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC4VjvEOlEXYW6qkVwjtpAF1tuP5qRQxdKfCO8bFOxrqgIhAImRE%2F5O2VG8rsPddXnJoDPjTI5Gn8ityE7YSN0vXYndKv8DCCcQABoMNjM3NDIzMTgzODA1Igzbdc5cBqu5ZYAfNGgq3AP01VfB2mdytrV9KNV1WhS%2Fo9SNdD5Ppta9VohF5sN2EzeTqEnGzXsN3ZiIHdGabfygIqp2KnupSw%2BWr8HU%2BSE%2BWy3AKykXX23XYmqEh42XeHdF7%2Fc%2BPk8DFVaYHEkQ5nAzN2wq4j9og7jGonHTZeL9LLBnEX1wI4yUPLj0%2BDuhCWvetd7VcQooHjZSBGVAzO5UYpTz4d0IjitzLE1RZ1X1PAq4%2BTNcMLFVbuhLsjBKyZ7totxSJ33VS4YwkyNw3BtwtIRCXUZkqlJUGtowkedBxqlbsBsm2eiQwqQe6b1O%2BpYIumr8WyODfqFNKVTHRJ4zkFHOXL3ARVT%2F3WeIOgvjV%2BkWQRYI3KdUohqNL6ik2O2YFcq7eDHaMXIPrZTSs4ZRG%2FlZEnLo1NeWIglprZTClkXlWaktP9VF3LfV9hCtc2K1OVUBH0PDDsterduNf6oRBMemqjxA4G05uVzICrElgaCsF1XUH85Lf%2FIMTo2RSsFUmftS3SiHoyQodhepOsJurBTLhgzIf7M7N09bL94ukPvo4oj3Blrs36RSeyQJmc%2BUWWh%2B63vielhy6SIluQHPS696kIzp1c0Gd0UJq%2F%2F48Sox6FzX1%2FBh7eaY2SbreGAJAoFZLjIbM9nR8DCIzvfJBjqkAYo1rxRRgnxhoYM3%2BHDxi7m6%2FiWuYjaftEe2hL5DrOshnKZLhiWrwHTsmaRaS4LZVRfNk9S5IDe04TcsYHreVs3HUK1D6MXXeExTgGYHMwXYaFda7FQIYSSJZNPrahuccz6iWrplGdkTLaD%2B%2BbSxYQVVDw8JG5mVHx%2Ft0SpHZV9VxBXkbHWbAYXcnxvG7rFJhLaOC7y84lbEcPY6qyxJxAwxYK8N&X-Amz-Signature=c45895aca433df942ba5801beb694b081981a441c47420e13bcd710a64bdbf99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we can identify the most common class amongst the 3 closest neighbors that we have identified. We can see that 2 of the neighbors are **green** class and 1 neighbor is of **red** class. As **green** is the most common class, the KNN model will assign the **green** class to the black dot.
</details>
---
## Question 5
From the fruits dataset, we can visualize two features in a two-dimensional space, e.g. the *width* on the x-axis, and the *color_score* on the y-axis:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/49a357f6-1f18-4dd4-bf94-36007a183b17/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XMJM3HV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCID3I7u05ZZnrIJjnmPdwTKJCOR7RCr7gvlc%2B3VyiRDInAiEAoeQyMUdYSSNlzQR0t%2FZWGkvSMMhrpBhAqWsyPlp091Uq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKUqCAFs9ElT29JX%2FircA9ifONRHdwBBIS%2FcSZXSDyWaHFx4wqDoTqIA7ZglsatVInbFnIsd60ufwjVh3O2Yge8YSiAv8W6rUl11btVWjXNeN6ERZgEzHJ5qs%2FjK0cLhME7odRqF2XOWp%2FN6wMX5ZQCeb7ZH0R%2F3SxAEuJK5oGnSR8BTF72KdI%2ByeeWMAzt4gWOPtu8RtYKI8X5cW8MwmZyNjcgAgSmBPv0zWmKYPFWDEu86y3iuvWRjtqUnlUsnbB6XR6mjd9P00VluD0GrYHY78BRrubszNUtIuWekuC16PYwNJ8FZy7hbX53MA%2BYcQ9in8%2BQftllJXkSZqooLwLcK70381t7K1hw6sIT6VRBPJF7saPAyLJi0P3Ib7n9afc45IZtuQl9YOlxNSsay6T%2Fx1zhqjt1QMcRLXUyfWEcZopKz6i5OWCu2MPRknTx3DRjHUyGItUxuFbWoPudEJvXprxcpBr6wX9XJEd9j0ZXdqGbfTuddh2CsvWvBBvJ9lDAo%2FWSbZdsCQsI8NNMlrjhVjx70qrqozkxXFzECGiTTz9Phg%2BfLol8xj9GV3%2BAapExKPK%2FNc6O3Cy1uTLi%2F7lkEl7H6fiQztIhje2TSe68GUU9HZKiKkcffL8ilLF6ZHEu6rjGH6D%2FaFiPMMNHO98kGOqUBu%2F8euU%2F6jNt3jMCQ0pZBant8jlhIhrIcX90pTSvteetl3qqP2MME87SMw%2BpcK46m7ENN58Z93ClvQ7iCeN6qV9e1jCZTs4AKGEOoA0GEjhkWOTLkDlf5vPJHQJ3nNLORQxn8VeA524TrjE%2F8%2FAUnfQCcz0x9CEUsNQswc%2FP5HjV72%2B3iwayeDIFnBZdkejTmmqq0L1UEqdq152GhE4umU5dugqhf&X-Amz-Signature=4019502155e5257a5fc2d74a512e5682499fb7a0cc333683d46be17e40f39ebc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Select all true statements.
✅  While not being a perfect solution, a narrow square function (parabola) could be found to separate at least the *mandarin* class from the others.
❌  This visualization clearly shows at least one clearly linearly separable class.
❌  This data combination does not seem useful, it would be better to remove one of the features for a better performing classifier.
✅  While this data combination does not look very useful, removing one of the features could still hurt the performance of a classifier.

<details>
<summary>Explanation</summary>

✅ **Correct, i**n a two-dimensional space, a parabola is a curved line that can be used to separate data points. Even if the data points are not perfectly separable by a straight line, a curved line like a parabola might be able to separate one class (like *mandarin*) from others. This means that while it might not perfectly separate all classes, it can still be useful for distinguishing at least one class.
❌ **Incorrect, **linear separability means that you can draw a straight line to separate one class of data points from others. If the visualization does not show any class that can be separated by a straight line, then this statement is incorrect. The data might be too mixed or overlapping for a straight line to work.
❌ **Incorrect, **even if the data combination doesn't look very useful at first glance, removing a feature might not always improve performance. Sometimes, multiple features together might provide valuable information that isn't obvious when looking at them separately. Removing a feature could lead to losing important information.
✅ **Correct,** even if the data doesn't seem useful, all features might still contribute valuable information. Removing one feature could potentially reduce the classifier's ability to make accurate predictions, as it might lose important context provided by the combination of features.
</details>
---

