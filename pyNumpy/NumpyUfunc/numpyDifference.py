# NumPy Differences
# To find the discrete difference, use the diff() function.

# Compute discrete difference of the following array:
# import numpy as np
# arr = np.array([10, 15, 25, 5])
# newarr = np.diff(arr)
# print(newarr) 

# Compute discrete difference of the following array twice:
import numpy as np
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=3)
print(newarr) 