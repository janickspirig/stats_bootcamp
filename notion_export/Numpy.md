---
title: "Numpy"
notion_id: "ccc5737d-c7c6-4936-bced-118aca375cf9"
notion_url: "https://www.notion.so/Numpy-ccc5737dc7c64936bced118aca375cf9"
exported_at: "2025-12-13T22:02:57.868012"
---

# Numpy

# Motivation
Numpy stands for **Num**erical **Py**thon. It is a package that enables us to do large computations over matrices at a very high speed. This is one reason why numpy is often used in the context of Data Science / Machine Learning, i.e., where there is a huge amount of data.
Another reason is that numpy arrays are n-dimensional, meaning we can create a numpy array of 1, 2, 3 or 9 dimensions and still do relatively fast computations. If we would use a list instead the computation speed would be much slower.
---
# Functions
---
Below you can find an overview and examples of the most important numpy functions that you should be aware of.
*`Priority functions`
## [`.array()`](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
---
**What: **Creates a new n-dimensional numpy array. 
**Input:**
`<< any array-like object >>` : required
- Something that can be converted to an array, usually we provide a List.
**Output: **Numpy array → n-dimensional numpy array.
---
```python
import numpy as np

my_array = np.array([1, 2, 3, 4])

my_array
array([1, 2, 3, 4])
```
```python
import numpy as np

my_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

my_array
array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10]])
```
> 💡 **To figure out how many dimensions a numpy array has, you can just count the number of opening and closing brackets.**
---
## [`.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html)
---
**What: **Determines the type of data stored in the numpy array.
**Input: **-
**Output:** String → The data type of the elements stored in the numpy array.
---
```python
import numpy as np

my_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

my_array.dtype
dtype('int64')
```
```python
import numpy as np

my_array = np.array(['Janick', 'Spirig'])

my_array.dtype
dtype('<U6')
```
---
## [`.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html)
---
**What:** Determines the number of dimensions of a n-dimensional numpy array.
**Input:** -
**Output:** Integer → the number of dimensions of the numpy array.
---
```python
import numpy as np

my_array = np.array(['Janick', 'Spirig'])

my_array.ndim
1
```
```python
import numpy as np

my_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

my_array.ndim
2
```
```python
import numpy as np

my_array = np.array([[[[[2, 3], [4, 6 ]]]]])

my_array.ndim
5
```
---
## [`.shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html)
---
**What: **Determines the shape of a n-dimensional numpy array.
**Input:** -
**Output:** Tuple → the number of rows and columns of the array:
`(<< number of rows >>, << number of columns >>)`
---
```python
import numpy as np

my_array = np.array(['Janick', 'Spirig'])

my_array.shape
(2,)
```
```python
import numpy as np

my_array = np.array([[1, 2, 3, 4, 5],	[6, 7, 8, 9, 10]])

my_array.shape
(2, 5)
```
---
## [`.size`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html)
---
**What:** Determines the size of a n-dimensional numpy array.
**Input:** - 
**Output:** Integer → number of elements that are stored in the numpy array.
---
```python
import numpy as np

my_array = np.array(['Computer', 'Science', 'is', 'fun'])

my_array.size
4
```
```python
import numpy as np

my_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

my_array.size
10
```
---
## [`.itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.itemsize.html)
---
**What: **Determines the number of bytes used by a n-dimensional numpy array.
**Input:** -
**Output:** Integer → number of bytes used by the array 
*Disclaimer: I don’t think you need to know how to calculate the output yourself.*
---
```python
import numpy as np

my_array = np.array([1, 2, 3, 4, 5])

my_array.itemsize
8
```
```python
import numpy as np

my_array = np.array(['Computer', 'Science', 'is', 'fun'])

my_array.itemsize
32
```
---
## [`.zeros()`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
---
**What:** Creates a new numpy array containing the value 0.0 (float) only.
**Input:** 
`<< dimension >>` : required
- Integer → number of zeros to be included in the array
**OR**
- Tuple → dimensions of the array as `(<< no. of rows >>, << no. of columns >>)`
**Output:** Numpy array → a new array wither one or multi-dimensional containing 0’s only. 
---
```python
import numpy as np

my_array = np.zeros(8)

my_array
array([0., 0., 0., 0., 0., 0., 0., 0.])
```
```python
import numpy as np

my_array = np.zeros((5, 2))

my_array
array([[0., 0.],
       [0., 0.],
       [0., 0.],
       [0., 0.],
       [0., 0.]])
```
---
## [`.ones()`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
---
**What:** Creates a new numpy array containing the value 1.0 (float) only.
**Input:**
 `<< dimension >>` : required
- Integer → number of ones to be included in the array
**OR**
- Tuple → dimensions of the array as `(<< no. of rows >>, << no. of columns >>)`
**Output:** Numpy array → a new array, one or multi-dimensional, containing 1’s only. 
---
```python
import numpy as np

my_array = np.ones(8)

my_array
array([1., 1., 1., 1., 1., 1., 1., 1.])
```
```python
import numpy as np

my_array = np.ones((5, 2))

my_array
array([[1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.],
       [1., 1.]])
```
---
## [`.full()`](https://numpy.org/doc/stable/reference/generated/numpy.full.html)
---
**What:** Creates a new numpy array and fills it with a specific value that can be anything.
**Input:**
`<< shape >>` : required
- Integer → number of elements of the `<< fill_value >>` to be included in the array
**OR**
- Tuple → dimensions of the array as `(<< no. of rows >>, << no. of columns >>)`
`<< fill_value >>` : required
- Any (Integer, String etc.) → the value with which the array should be filled
**Output: **Numpy array → a new array, one or multi-dimensional, containing the fill_value only 
---
```python
import numpy as np

my_array = np.full(5, 'Janick')

my_array
array(['Janick', 'Janick', 'Janick', 'Janick', 'Janick'], dtype='<U6')
```
```python
import numpy as np

my_array = np.full((6,4), 'CS')

my_array
array([['CS', 'CS', 'CS', 'CS'],
       ['CS', 'CS', 'CS', 'CS'],
       ['CS', 'CS', 'CS', 'CS'],
       ['CS', 'CS', 'CS', 'CS'],
       ['CS', 'CS', 'CS', 'CS'],
       ['CS', 'CS', 'CS', 'CS']], dtype='<U2')
```
---
## [`.arange()`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)
---
**What:** Creates a [range object](/1e485dd6e1754338bb05ff87ff4153ad) and directly converts it to a numpy array.
**Input:**
`<< start >>` : optional
- Integer → the first element to be <u>*included*</u> in the range, if not provided value 0 is used by default
`<< stop >>` : required
- Integer → the first element to be <u>*excluded*</u> in the range
`<< step >>` : optional
- Integer → step size that should be used in order to over-jump elements in the range
**Output:** Numpy array → a new array that contains the specified number range
---
```python
import numpy as np

my_array = np.arange(7)

my_array
array([0, 1, 2, 3, 4, 5, 6])
```
```python
import numpy as np

my_array = np.arange(4, 11)

my_array
array([ 4,  5,  6,  7,  8,  9, 10])
```
```python
import numpy as np

my_array = np.arange(4, 11, 2)

my_array
array([ 4,  6,  8, 10])
```
---
## [`.linspace()`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
---
**What:** Creates a new numpy array containing an evenly spaced number range.
**Input:**
`<< start >>` : required
- Integer → the first element to be <u>*included*</u> in the range
`<< stop >>` : required
- Integer → the last element to be <u>*included*</u> in the range
> 💡 **When we use `.arange()`, `<< stop >>` is the **first** element to be **excluded.
W**ith `.linspace()`, `<< stop >>` is the **last** element to be **included****
`<< # elements >>` : optional
- Integer → number of elements that should be evenly spaced between `<< start >>` and `<< stop >>`, if not provided the value 50 is used by default
**Output:** Numpy array → a new array that contains an evenly spaced number range
---
```python
import numpy as np

my_array = np.linspace(0, 80, 11)

my_array
array([ 0.,  8., 16., 24., 32., 40., 48., 56., 64., 72., 80.])
```
```python
import numpy as np

my_array = np.linspace(0, 80)

my_array
array([ 0.        ,  1.63265306,  3.26530612,  4.89795918,  6.53061224,
        8.16326531,  9.79591837, 11.42857143, 13.06122449, 14.69387755,
       16.32653061, 17.95918367, 19.59183673, 21.2244898 , 22.85714286,
       24.48979592, 26.12244898, 27.75510204, 29.3877551 , 31.02040816,
       32.65306122, 34.28571429, 35.91836735, 37.55102041, 39.18367347,
       40.81632653, 42.44897959, 44.08163265, 45.71428571, 47.34693878,
       48.97959184, 50.6122449 , 52.24489796, 53.87755102, 55.51020408,
       57.14285714, 58.7755102 , 60.40816327, 62.04081633, 63.67346939,
       65.30612245, 66.93877551, 68.57142857, 70.20408163, 71.83673469,
       73.46938776, 75.10204082, 76.73469388, 78.36734694, 80.        ])
```
---
## [`.reshape()`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
---
**What:** Re-shapes an existing array, i.e., changes number of rows and columns.
**Input:**
`<< array >>` : required
- Numpy array → the array that should be re-shaped
`<< new_shape >>` : required
- Tuple → new dimensions of array as  `(<< no. of rows >>, << no. of columns >>)`
**Output:** Numpy array → a new array with the same data as before but in different shape
---
```python
import numpy as np

my_array = np.arange(4, 10)

my_array
array([4, 5, 6, 7, 8, 9])

# option 1
np.reshape(my_array, (3, 2))
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 2
my_array.reshape((3, 2))
array([[4, 5],
       [6, 7],
       [8, 9]])
```
---
## [`.sum()`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)
---
**What:** Calculates the sum over all elements in the array over a specific axis (rows or columns).
**Input:**
`<< array >>` : required
- Numpy array → the array for which the sum should be calculated.
`<< axis >>` : optional
- Integer → the axis over which the sum should be calculated
- `0` → sum is calculated over columns (vertically)
- `1` → sum is calculated over rows (horizontally)
If no value is provided (or array is 1-dimensional anyway), `axis = None` is used, meaning that all values in the array are simply summed up.
**Output:**
- Numpy array → an array of integers as the calculated sum values
**OR**
- Integer → single sum value (when `axis=None` or 1-dimensional array)
---
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.sum()
39

# option 2
np.sum(my_array)
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.sum(0)
array([18, 21])

# option 2
np.sum(my_array, 0)
array([18, 21])
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.sum(1)
array([9, 13, 17])

# option 2
np.sum(my_array, 1)
array([9, 13, 17])
```
---
## [`.min()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html)
---
**What:** Identifies the smallest value of the elements in the array over a specific axis (rows or columns).
**Input:**
`<< array >>` : required
- Numpy array → the array in which the smallest value(s) should be identified.
`<< axis >>` : optional
- Integer → the axis over which the smallest value should be identified.
- `0` → smallest value per column is identified (vertically)
- `1` → smallest value per row is identified (horizontally)
If no value is provided (or array is 1-dimensional anyway), `axis = None` is used, meaning that the smallest value overall is identified.
**Output:**
- Numpy array → an array of integers as the smallest values per row or column
**OR**
- Integer → the smallest value overall (when `axis=None` or 1-dimensional array)
---
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.min()
4

# option 2
np.min(my_array)
4
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.min(0)
array([4, 5])

# option 2
np.min(my_array, 0)
array([4, 5])
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.min(1)
array([4, 6, 8])

# option 2
np.min(my_array, 1)
array([4, 6, 8])
```
---
## [`.max()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html)
---
**What:** Identifies the biggest value of the elements in an array over a specific axis (rows or columns).
**Input:**
`<< array >>` : required
- Numpy array → the array in which the biggest value(s) should be identified.
`<< axis >>` : optional
- Integer → the axis over which the biggest value should be identified.
- `0` → biggest value per column is identified (vertically)
- `1` → biggest value per row is identified (horizontally)
If no value is provided (or array is 1-dimensional anyway), `axis = None` is used, meaning that the biggest value overall is identified.
**Output:**
- Numpy array → an array of integers as the biggest values per row or column
**OR**
- Integer → the biggest value overall (when `axis=None` or 1-dimensional array)
---
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.max()
9

# option 2
np.max(my_array)
9
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.max(0)
array([8, 9])

# option 2
np.max(my_array, 0)
array([8, 9])
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.max(1)
array([5, 7, 9])

# option 2
np.max(my_array, 1)
array([5, 7, 9])
```
---
## [`.mean()`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)
---
**What:** Calculates the mean of the elements in an array over a specific axis (rows or columns).
**Input:**
`<< array >>` : required
- Numpy array → the array for which the mean should be calculated
`<< axis >>` : optional
- Integer → the axis over which the mean should be calculated
- `0` → mean is calculated per column (vertically)
- `1` → mean is calculated per row (horizontally)
If no value is provided (or array is 1-dimensional anyway), `axis = None` is used, meaning that mean over all elements is calculated.
**Output:**
- Numpy array → an array of floats as the mean value per row or column
**OR**
- Float → the mean value overall (when `axis=None` or 1-dimensional array)
---
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.mean()
6.5

# option 2
np.mean(my_array)
6.5
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.mean(0)
array([6., 7.])

# option 2
np.mean(my_array, 0)
array([6., 7.])
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.mean(1)
array([4.5, 6.5, 8.5])

# option 2
np.mean(my_array, 1)
array([4.5, 6.5, 8.5])
```
---
## [`.std()`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)
---
**What:** Calculates the standard deviation of the elements in an array over a specific axis (rows or columns).
**Input:**
`<< array >>` : required
- Numpy array → the array for which the standard deviation should be calculated
`<< axis >>` : optional
- Integer → the axis over which the mean should be calculated
- `0` → standard deviation is calculated per column (vertically)
- `1` → standard deviation is calculated per row (horizontally)
If no value is provided (or array is 1-dimensional anyway), `axis = None` is used, meaning that standard deviation over all elements is calculated.
**Output:**
- Numpy array → an array of floats as the stdv. value per row or column
**OR**
- Float → the stdv. value overall (when `axis=None` or 1-dimensional array)
> 💡 **I don’t think that it is expected from you to know how to calculate standard deviations by hand / manually as this is rather a statistics topic.**
---
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.std()
1.707825127659933

# option 2
np.std(my_array)
1.707825127659933
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.std(0)
array([1.63299316, 1.63299316])

# option 2
np.std(my_array, 0)
array([1.63299316, 1.63299316])
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.std(1)
array([0.5, 0.5, 0.5])

# option 2
np.std(my_array, 1)
array([0.5, 0.5, 0.5])
```
---
## [`.var()`](https://numpy.org/doc/stable/reference/generated/numpy.var.html)
---
**What:** Calculates the variance of the elements in an array over a specific axis (rows or columns).
**Input:**
`<< array >>` : required
- Numpy array → the array for which the variance should be calculated
`<< axis >>` : optional
- Integer → the axis over which the variance should be calculated
- `0` → variance is calculated per column (vertically)
- `1` → variance is calculated per row (horizontally)
If no value is provided (or array is 1-dimensional anyway), `axis = None` is used, meaning that the variance over all elements is calculated.
**Output:**
- Numpy array → an array of floats as the variance value per row or column
**OR**
- Float → the variance value overall (when `axis=None` or 1-dimensional array)
> 💡 **I don’t think that it is expected from you to know how to calculate the variance by hand / manually as this is rather a statistics topic.**
---
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.var()
2.9166666666666665

# option 2
np.var(my_array)
2.9166666666666665
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.var(0)
array([2.66666667, 2.66666667])

# option 2
np.var(my_array, 0)
array([2.66666667, 2.66666667])
```
```python
import numpy as np

my_array = np.arange(4, 10).reshape((3,2))

my_array
array([[4, 5],
       [6, 7],
       [8, 9]])

# option 1
my_array.var(1)
array([0.25, 0.25, 0.25])

# option 2
np.var(my_array, 1)
array([0.25, 0.25, 0.25])
```
---
## [`.isnan()`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html)
---
**What:** Checks for `NaN` (Not a Number) values in a NumPy array. Useful for data cleaning or handling missing values.
**Input:**
`<< array >>` : required
- Numpy array → the array for which the variance should be calculated
**Output:**
- Numpy array containing booleans → an array of the same shape as the input, where each element is True if the corresponding element in the input array is `NaN` and False otherwise.
---
```python
import numpy as np

arr = np.array([1, np.nan, 3])

np.isnan(arr)
[False, True, False] # output
```
```python
arr_2d = np.array([[1, np.nan], [3, 4]])

np.isnan(arr_2d)
[[False, True], [False, False]] # output
```
```python
arr = np.array([1, np.nan, 3])

arr[np.isnan(arr)] = 0

arr
[1, 0, 3] # output
```
---

