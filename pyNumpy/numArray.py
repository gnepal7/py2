# Create a NumPy ndarray Object
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function

# use array for creating numpy array
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 0])
# print(arr1)
# print(type(arr1))

# Use a tuple to create a NumPy array
# import numpy as np
# arr = np.array((1, 2, 3, 4, 5))
# print(arr) 
# print(type(arr1))

# Dimensions in Arrays
# A dimension in arrays is one level of array depth (nested arrays). 
# nested array: are arrays that have arrays as their elements

# 0-D Arrays
# Create a 0-D array with value 42
# import numpy as np
# arr = np.array(42)
# print(arr) 

# 1-D Arrays
# Create a 1-D array containing the values 1,2,3,4,5
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr) 

# 2-D Arrays
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr) 

# Create a 3-D array with two 2-D arrays, both containing two arrays with the 
# values 1,2,3 and 4,5,6
# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr) 

# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells 
# us how many dimensions the array have
# import numpy as np
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim) 

# Higher Dimensional Arrays
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by 
# using the ndmin argument.
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=4)
print(arr)
print('number of dimensions :', arr.ndim) 


