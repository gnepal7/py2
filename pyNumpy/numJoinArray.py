# Joining NumPy Arrays
# Joining means putting contents of two or more arrays in a single array
# We pass a sequence of arrays that we want to join to the concatenate()
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr) 

# Join two 2-D arrays along rows (axis=1)
# import numpy as np
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr) 

# Joining Arrays Using Stack Functions

# Stacking is same as concatenation, the only difference is that 
# stacking is done along a new axis
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.stack((arr1, arr2), axis=1)
# print(arr) 

# Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.hstack((arr1, arr2))
# print(arr) 

# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.vstack((arr1, arr2))
# print(arr) 

# Stacking Along Height (depth)

# NumPy provides a helper function: dstack() to stack along height, 
# which is the same as depth
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)