---
title: "Numpy"
notion_id: "26a96163-59df-4930-ab93-344d8bed0c1c"
notion_url: "https://www.notion.so/Numpy-26a9616359df4930ab93344d8bed0c1c"
exported_at: "2025-12-13T22:52:06.172710+00:00"
---

# Numpy

---
Filtering
```python
import numpy as np

my_array = np.array([4, 2, 5, 6])
my_array[my_array >= 4] ** 2
```
<details>
<summary>Solution</summary>

`array([16, 25, 36])`
</details>
---
Broadcasting
```python
import numpy as np

my_array = np.array([4, 2, 5, 6])
my_array[my_array >= 4] ** 2
```
<details>
<summary>Solution</summary>

`array([16, 25, 36])`
</details>
---
[`.shape`](/ccc5737dc7c64936bced118aca375cf9#3332a8d6e6f040dcb5d7a9aa86174b6b)
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array.shape
```
<details>
<summary>Solution</summary>

`(4, 3)`
</details>
---
[**`.full()`**](/ccc5737dc7c64936bced118aca375cf9#8a83f4b13478461f88b3eaa6fd43315e)
```python
import numpy as np

np.full([3, 2], 'Hello')
```
<details>
<summary>Solution</summary>

```python
array(
	[	
		['Hello', 'Hello'], 
		['Hello', 'Hello'],
		['Hello', 'Hello']
	]
)
```
</details>
---
[**`.reshape()`**](/ccc5737dc7c64936bced118aca375cf9#b266475fda3a493383e07eece2ec3510)
```python
import numpy as np

my_array = np.full([3, 2], 2)
my_array = np.reshape(my_array, (2,3))
my_array * 4
```
<details>
<summary>Solution</summary>

```python
array(
	[	
		[8, 8, 8], 
		[8, 8, 8]
	]
)
```
</details>
---
[**`.ndim`**](/ccc5737dc7c64936bced118aca375cf9#3e82f815ed7741db9931a437f7c2d5ce)
```python
import numpy as np

my_array = np.array([[[0, 1, 2, 3, 4]]])
my_array.ndim
```
<details>
<summary>Solution</summary>

`3`
</details>
---
[**`.mean()`**](/ccc5737dc7c64936bced118aca375cf9#64a39ed9c00c4e64a2f0e20e33cd0d8a)
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
np.mean(my_array[3, :])
```
<details>
<summary>Solution</summary>

`6.0`
</details>
---
Accessing
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array[1:3, 1:][0][1]
```
<details>
<summary>Solution</summary>

`8`
</details>
---
Filtering
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array2 = np.array([True, False, False, True])
my_array[:, 1][my_array2]
```
<details>
<summary>Solution</summary>

`array([2, 2])`
</details>
---
Accessing
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array[1:3, 1:][0][1]
```
<details>
<summary>Solution</summary>

`8`
</details>
---
Filtering
```python
import numpy as np

my_array = np.array([[0, 2, 4], [4, 6, 8], [3, 5, 7], [7, 2, 9]])
my_array2 = np.array([True, False, False, True])
my_array[:, 1][my_array2]
```
<details>
<summary>Solution</summary>

`array([2, 2])`
</details>
---

