---
title: "Quiz 10"
notion_id: "21274ffd-3319-8083-a90d-e0fce716504e"
notion_url: "https://www.notion.so/Quiz-10-21274ffd33198083a90de0fce716504e"
exported_at: "2025-12-13T23:00:42.302821+00:00"
---

# Quiz 10

## Question 1
Markieren Sie alle wahren Aussagen bezüglich *Supervised Machine Learning* ("überwachtes maschinelles Lernen").
✅ Für ein glaubwürdiges Ergebnis eines trainierten Modells, das in einem Supervised Machine Learning-Ansatz trainiert wurde, muss zwingend mindestens ein Train/Test-Split des Datensatzes durchgeführt werden.
✅ Wenn ein Datensatz neben den Features auch jedem Eintrag eine Klasse zugeordnet, kann darauf ein supervised Machine Learning Modell trainiert werden.
❌ Eine Regression ist kein Supervised Machine Learning ("überwachtes Lernverfahren"), da es keine diskreten Klassen, sondern stetige ("continuous") Zielwerte hat.
❌ Die Erkennung von statistischen Ausreißern ("outlier") wird üblicherweise supervised ausgeführt.
❌ Supervised Learning hat die Bezeichnung daher, dass nach jedem Trainingsbeispiel eine menschliche Interaktion nötig ist.

<details>
<summary>Explanation</summary>

> 💡 **[Supervised vs. unsupervised ML](/9b19eda74fac4ffb8e48b36dde3b47a4)**
✅ For a trained supervised model to be meaningfully evaluated, the data must be split into a training and testing set (or use techniques like cross-validation). Otherwise, there’s no way to assess generalization performance
✅ This is the core idea of supervised learning: labeled data where each input (feature vector) has a corresponding output (label or class). That enables training a classifier.
❌ This is incorrect. Regression is a supervised learning task — the only difference is that the target variable is continuous, not categorical.
❌ Most outlier detection methods (e.g. Isolation Forest, One-Class SVM) are **unsupervised**. Supervised outlier detection exists but is not the norm — especially since labeled anomalies are rare.
❌ “Supervised” refers to labeled data, not human involvement during training. The model trains automatically using the labeled dataset.
</details>
---
## Question 2
Welche der unten aufgelisteten Elemente werden benötigt, um ein KNN-Modell korrekt definieren zu können?
✅ Der Wert von K
✅ Eine Distanzmetrik
❌ Ein mindestens zweidimensionaler Datensatz
❌ Das Problem mit diesem ML-Model ist die fehlende Interpretierbarkeit der Ergebnisse (es ist eine "black box").
✅ Eine Methode zur Aggregation der Klassen (einfache Mehrheit, …)
❌ Die Daten müssten skaliert/normiert sein.

<details>
<summary>Explanation</summary>

> 💡 **[kNN](/4e55bc27409940e98f9a060821d07644)**
✅ KNN relies on measuring how "close" two samples are. A distance metric (e.g. Euclidean, Manhattan) is required to compare data points.
❌ KNN can work with one-dimensional data too. Higher dimensionality is common but not a requirement.
❌ This is inaccurate. KNN is **highly interpretable** — predictions are based on visible, understandable neighbors. It’s the opposite of a black box.
✅ For classification, KNN needs a rule to combine neighbor labels (e.g. majority voting). This is essential for defining how the final prediction is chosen.
❌ Normalization is **highly recommended** to avoid distance bias, but technically not required to define the model. The model still runs without it (though with worse performance).
</details>
---
## Question 3
↪️ [Check here](/7ff79086266b4a54862131d9ff40d70c#76f9fbc811834ce58f354e5d1df3e8af)
---
## Question 4
Sehen Sie sich diesen zweidimensionalen Datensatz mit den drei Klassen **Blau**, **Rot** und **Grün** an.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cb6fc586-4803-43dd-b5c6-9e68e8e50d8d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO2G22VA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T230040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHWNs2%2BqYlZAsLcypC%2FgUd07DeMdfgFztWSDatoHd9tnAiAST2nj9w9mHwuRBJxGodXYLvPgRz0834bxURc%2BXlwH2Sr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMvASDWRc6CFaCcwAeKtwDm1bQdvFoWK6wdW4AyxY5Rgs4BXTejJrO0COaRz3QPdJZEUv5zn6Vd3Q1ii3Odx9bXIMdMqOeBMJNFRZLI5CT%2BbJIzx7JHQ%2BU4Yyf2BVTg7KGuNwWa%2F6d9WanaF73g9Z4NlR91i5j1q6WYeLnZ0L%2FkhWqsc2UK1HYQJsLkX%2FwHnX2GuaGUqgIS2gaRTvfxwdAieuDRw0OLOFZ2oTDmEMdwEHLb6epD%2Fd384eLpQcXqV46GNKpDVS0%2B8I69KnbkpRXi09GtoM24gLlQzWjsB%2BJxQmUcsWk5q%2BEOwH69vrF1caOKAk4jETkXTYupxJ6lraMsBQ40F1LubfqxhkmATtgRV2NGirdjxo2kZ%2FaUx9HWNAXDu80c0azE%2B67scqv9YfFUtneXw%2Fpwo%2Bk7rf6y0pWGaZyyNfWbAYhXtii5T5l3q4H6m2elFMLTFJmcgatMBETz7IIo823R%2FUUDstz9eGqhXr0nxvhakHda%2FP%2BwvXl2fR8yEm%2BayhUgbg2O%2B1M03lfpqqnLSlN3%2FqSPuiEbn%2Bm%2B9lNsJpMP%2BvRqkrDNcGiHHK9szm1gqdsAtV6Bm1QnPjvyEOE%2BzYGgAZo%2FTR903ZNFbxBCWvP46iW1ccFyKy78fvUjXdSTnQrkgzgdREwoM73yQY6pgEzaEnV3hnAOChccrf6EQbW3X1IouTy7TQc0MRuWsxuxUVeYuhjbJLLjtoKnlpoqhi16wfsR25J2UftSz0cTOMZSMYCk0I7HwFSx3EIML%2FQezHqIYbByNXVkEO3Z6My%2BOZWXRwqGnDNykzOlQGNnQFXe7%2BBh5v9B2q5gQOyGewgCTWe3jOOE1konnAHW3MaL7DB15Z2CSJb%2F11KcD8f7RiyApPkvW0M&X-Amz-Signature=87b5f92c179791596718fbf42d6c9bc9b331fc4ba60c9dc2a73a20f8fc862889&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Welche Klasse würde ein KNN-Modell mit k=3 dem mittleren schwarzen Punkt zuweisen?

<details>
<summary>Explanation</summary>

> 💡 **[kNN](/4e55bc27409940e98f9a060821d07644)**
The KNN algorithm with `k = 3` assigns the class label of the **majority** among the **3 closest neighbors**.
In the diagram:
- **Two** of the **three closest points** to the black center point are **green**.
- That means:
- green: 2 votes
- red: 1 vote
- blue: 0 votes
✅ So the majority class is **green**, and the KNN classifier would assign the black point to class **green**.
</details>
---

