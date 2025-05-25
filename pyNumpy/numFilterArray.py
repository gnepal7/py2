# Filtering Arrays
# Getting some elements out of an existing array and creating a 
# new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.

# Create an array from the elements on index 0 and 2
# import numpy as np
# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr) 

# Create a filter array that will return only values higher than 42
# import numpy as np
# arr = np.array([41, 42, 43, 44])
# Create an empty list
# filter_arr = []
# go through each element in arr
# for element in arr:
#   if element > 42:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr) 

# Create a filter array that will return only even elements from the original array
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Create an empty list
# filter_arr = []
# go through each element in arr
# for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
#   if element % 2 == 0:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr) 

# Creating Filter Directly From Array
# Create a filter array that will return only values higher than 42
# import numpy as np
# arr = np.array([41, 42, 43, 44])
# filter_arr = arr > 42
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr) 

# Create a filter array that will return only even elements from the original array
import numpy as np
arr = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr = np.array(arr)
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)





