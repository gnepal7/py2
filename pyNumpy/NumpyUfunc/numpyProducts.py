# To find the product of the elements in an array, use the prod() function.

# Find the product of the elements of this array:
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# x = np.prod(arr)
# print(x) 

# Find the product of the elements of two arrays:
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5, 6])
# arr2 = np.array([5, 6, 7, 8, 9, 10])
# x = np.prod([arr1, arr2])
# print(x)
# Product Over an Axis
# newarr = np.prod([arr1, arr2], axis=1)
# print(newarr)

# Take cummulative product of all elements for following array:
import numpy as np
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr) 