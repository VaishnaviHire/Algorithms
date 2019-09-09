# Arrays

The problems in this module cover concepts of array manipulation, matrix, range queries.
## Description

An array is a collection of data which can be represented or accessed by single pointer.
A single data point of the array is accessed by its index(position) which starts from 0.

For e.g:
```
a = [1,2,3,4]
a.index(1) returns 0 
a.index(2) returns 1 and so on. 
```

## General Complexity

Most of the array problems require entire array traversal, exceptions may include already sorted array and binary search.
So the time complexity is <b>O(n)</b> where n is the length of the array.


## Representation 

Arrays in Python can be represented as lists or numpy array structures

#### Lists
```
a = [1,2,3,4,5] // Uniform list representation
b = [1,"a","xyz",4.5, 6] // Hybrid list
c = [[1,2],[3,4]] // 2D lists
```

#### Numpy Array
```
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([1,"a","xyz",4.5, 6]) // Hybrid list
c = np.array([[1,2],[3,4]]) // 2D lists
```

