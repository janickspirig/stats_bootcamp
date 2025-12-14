---
title: "FAQ"
notion_id: "3fc0d056-5a51-4584-bc20-9716276436c3"
notion_url: "https://www.notion.so/FAQ-3fc0d0565a514584bc209716276436c3"
exported_at: "2025-12-13T22:28:40.785411+00:00"
---

# FAQ

<details>
<summary>What is an iterable? </summary>

> [Iterable](https://www.analyticsvidhya.com/blog/2021/07/everything-you-should-know-about-iterables-and-iterators-in-python-as-a-data-scientist/) is a parent class of datatypes like list, tuple, range or dictionary. The methods that these datatypes inherit from their parent iterable make them .. well iterable. 🙂 This means basically that we can iterate through them using a for loop, list comprehension or whatever mechanism. So whenever we talk about an iterable we refer to all datatypes that can store multiple elements and thus be used in combination with a for-loop.
</details>

<details>
<summary>What is the difference between TLS and SSL?</summary>

> TLS is the newer version of SSL and thus the successor protocol. Very often, both terms are used interchangeably.
</details>

<details>
<summary>What is the difference between HTTPS and TLS/SSL?</summary>

> HTTPS ensures secure data transfer on the application layer and TLS/SSL ensure secure data transfer on the transport layer. TLS/SSL makes sure that the e-banking server to which our computer is talking to is trustful and that the connection is secure and reliable. HTTPS makes sure that the e-banking password we entered on the website is encrypted, i.e., that the actual data we send as part of the request is secured.
</details>

<details>
<summary>What is the difference between an URI and an URL?</summary>

> **URL → Uniform Ressource Locator**
> A location / web address where multiple resources can be stored.
> **URI → Uniform Ressource Identifier
> **An identifier of a specific resource on the server, i.e., a specific image, text, song, etc.
> [Full explanation](https://www.hostinger.com/tutorials/uri-vs-url)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/98e56c44-45e0-4762-a6a1-f1e89eb0d41a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLTI7NM3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD04NmRtr7%2FwaEKPSyuVLYZKPNXzsEJS6tbcZfxZmcITQIhAPfVfcqw4h7iDX67zC46o7FydoA9MctF4EiSlL%2BAN%2FSZKv8DCCcQABoMNjM3NDIzMTgzODA1IgwDcIckQI6jWg%2BdYCoq3AM1blfa0ScL7JbkHq0tkeQhARYRs25SZI9kGALEOqq1fgv7XBngoK7jEtpPA7rS7%2FeH3CCXvFwQ3fnewBVe94FO0rGlO%2FCRlsXsT2f4LK3iJ6rFXVHdLLGA3vB%2BmU2uPUF0KwBBnoz%2FPnBVJizJ64Fm1%2FwBwLE%2BLcnDkEjkI%2Fv59MOKzW2FNEZY68HZ3lzuJiwFYCz%2F2K2GMZKtYZUnOrlldYq4u%2FeHYVF04KadYgA9DbIfAskp4MevuHRgBUwVr0G%2BiH2vsbgqshVKulzBnAXuuGtoJ9LEEdGjveBJGwioS15XsREvAjQRhV%2FC0OA3e0Yx8vJdivKQIshdvKJwdER5N05LgqL%2FzwqN%2BvPK0uiH%2BSrqOJowXGvdcUnnppmeGgIl%2B2SCksb7L%2Bq23Ck4Oxy0YUF0KrwpKSZSEHeg%2ByTEgrhb2jHyVFXauSu9rvlp%2B0cY%2FjpCI2Tr9%2BgDN4uCTpSMa38BjfoTwNM65QAGnx4Eftex9MtpR7BhhK1qzxU%2BUMNZ3d%2FWTO1P%2B0%2FxOiJASXOxNhLQ5FAYECuGI6lapfWd%2FesgmmcStbm9yq3e3Gz8lt%2Fl5Yzqey%2BsXugpquj1AT0TO2yzVvNnLkdlhuvbJtNBUWbWLnI1bW%2BDoImBHjDfzffJBjqkASd3lBzZapBvTZxzHFPcmlnZbnmKJdvOd8xR6G1qmZ6%2B2vdHTY3DeYaYj3MblEugvdbTT73Rj0S8HrO4ZUqb5TLvujnvIwfrfWQSC2FvHxn2PYlIznMZw%2Frhh9ywFJesNDWbTPeeJL78WeltDcXm4rym30yRbRmYu49vwrMYZNTIihcNfxr09Y3dw13SbjyJmNRALfMF9O%2FUa6Ey2nyajpHSwDVS&X-Amz-Signature=798680ea6d748bbbc02c66bd751c1d9a53fae04fba2971dc701194b3d886ba5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>

<details>
<summary>What is the difference between a Tuple and a List?</summary>

> A list is mutable, meaning we can add and remove elements in a list whereas a tuple is immutable, meaning we cannot add and remove elements in tuple once it has been created.
</details>

<details>
<summary>What is the difference between a List and a Set?</summary>

> A list can contain duplicate values (same value of same datatype), whereas a set cannot contain duplicate values. When we create a set and we provide duplicate values, Python automatically removes all the duplicates.
</details>

<details>
<summary>Why can we use the Modulo `%` operator to check if a number is even or odd?</summary>

> All even numbers are dividable by 2 without rest. If a number is dividable by another number without rest, modulo returns 0. Thus, when we do `<<any even number>> % 2` we get **0** which is equal to **False**. 
> When we divide an odd number by 2 we always get a rest of 1. Thus, when we do `<<some odd number>> % 2` we get **1** which is equal to **True**. 
> With this two modulo operations we can define an if / else statement which checks whether a number is even or odd. We have two options to do so:
```python
### first option ###

# 0 (False) if number is even, 1 (True) if number is odd
if <<some number>> % 2: 
	# number is odd
else:
	# number is even

### second option ###

# 1 (True) if number is even, 0 (False) if number is odd
if not <<some number>> % 2: 
	# number is even
else:
	# number is odd
```
> From the code snippet above you see that when we add the `not` keyword, the whole things gets inverted, meaning that the if-body is now executed when the number is even and the else-body when the number is odd. Important is that you don’t learn this if-else construct to check even and odd numbers by heart but rather focus on understanding what 0 and 1 signify and how the modulo operator works. 
</details>

<details>
<summary>Why do we use Numpy and don’t stick to standard Python datatypes such as lists?</summary>

> Numpy allows us to do numerical calculation with a lot of data in very quick time. Imagine we want to train an Object Detection algorithm with 500’000 images. We could represent the images using lists, however the training time would be very long. 
> If we use Numpy arrays to represent images, the processing can be done much quicker and thus the training time is shorter. So as soon as we deal with lots of numerical values, it is better to use Numpy arrays. 
</details>

<details>
<summary>Can we store different types of data in a single numpy array? E.g. can I store two integers and three strings in the same array?</summary>

> Yes and no. Yes because you can create the array itself without error. No because numpy arrays are homogenous, meaning that they can only store one type of data in a single array. Therefore, the two integers will be converted to strings when creating the array.
```python
import numpy as np

my_array = np.array(['Janick', 1, 2])

my_array
array(['Janick', '1', '2'])
```

</details>

<details>
<summary>What is the difference between a Pandas DataFrame and a Pandas Series?</summary>

> [DaraFrame](/3fc0d0565a514584bc209716276436c3) and [Series](https://www.machinelearningplus.com/pandas/pandas-series-in-python/) are two datatypes of the Pandas library. A DataFrame is an entire table made up of multiple columns and rows. A Pandas Series on the other hand represents a one-dimensional row or column in a DataFrame. So whenever we extract one row or column we get a Series. It is important to note, that we can also build Series from scratch, i.e., extracting data from a DataFrame is not the only option to get a Pandas Series.
</details>

<details>
<summary>What is the difference between Recall and Precision?</summary>

> Precision tells us what fraction the observations in the test data that our classifier assigned with the positive class are actually positive.
> Recall tells what fraction of all positive observations in the test data our classifier identified correctly.
</details>

<details>
<summary>Why do we split our dataset into training and test data?</summary>

> Before we can use a classifier we need to train it. For the training process we need some data. Once we have trained the classifier we want to evaluate how good our classifier is before we deliver it to our client. Thus, we need some more data for testing. This is why we split the data into training and test data. If we would not split the data and train and test our classifier with the same data, it would be very biased. Because the classifier has seen the solutions before solving the exam and thus, obviously, achieves a good mark. So we want to test our classifier with an exam for which the classifier does not know the solutions beforehand so that we have a result that reflect  our classifiers’ abilities truthfully.
</details>

<details>
<summary>What is the difference between a regular parameter and a hyperparameter?</summary>

> Paramters are learned by the classifier from the data during the training process. Thus, how the values for parameters are chosen depends on the training data.
> Hyperparameters on the other hand are chosen and set before the training process and are thus independent from the training data. An example for a hyperparameter is the number of neighbours (k) to consider in the k-nearest-Neighbour algorithm.
</details>

<details>
<summary>How do we know which are the best hyperparameters?</summary>

> There is no magic-formula to this challenge. Often we run the training and testing of our classifier with multiple hyperaparameter values to then identify the settings with which the classifier performed best. Thus, very often it is a bit of trial & error.
</details>

<details>
<summary>How do I read a Boxplot?</summary>

> **Boxplot**
```sql
 		Q1-1.5IQR    Q1  median  Q3    Q3+1.5IQR
                  |-----:-----|
  o      |--------|     :     |--------|    o  o
                  |-----:-----|
outlier           <----------->            outlier
                       IQR
```

</details>
