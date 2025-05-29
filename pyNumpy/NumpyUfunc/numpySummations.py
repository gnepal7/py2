# NumPy Summations

# Addition is done between two arguments whereas summation happens over n elements.

# Add the values in arr1 to the values in arr2:
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
# newarr = np.add(arr1, arr2)
# print(newarr) 

# Sum the values in arr1 and the values in arr2:
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr) 
# Perform summation in the following array over 1st axis:
newarr2 = np.sum([arr1, arr2], axis = 1)
print(newarr2)

# Perform cummulative summation in the following array:
import numpy as np
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr) 
