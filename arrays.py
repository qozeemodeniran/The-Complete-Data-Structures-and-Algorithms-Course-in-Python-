# using the array module:
import array

arr1 = array.array('i')
print(arr1)

arr2 = array.array('i', [1,2,3,4])
print(arr2)

# using the numpy module:
import numpy as np

arr3 = np.array([])
print(arr3)

arr4 = np.array([1,2,3,4], dtype=int)
print(arr4)