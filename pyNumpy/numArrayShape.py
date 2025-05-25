# Shape of an Array

# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple 
# with each index having the number of corresponding elements

# Print the shape of a 2-D array:
# import numpy as np
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape) 

# Create an array with 5 dimensions using ndmin using a vector with 
# values 1,2,3,4 and verify that last dimension has value 4
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=4)
print(arr)
print('shape of array :', arr.shape) 


