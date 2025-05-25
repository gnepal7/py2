# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method

# Find the indexes where the value is 4
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 3)
# print(x) 

# Find the indexes where the values are even
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(f"Even values are indexing at: {x}") 
# Find the indexes where the values are odd
# y = np.where(arr%2 == 1)
# print(f"Odd values are indexing at: {y}") 

# The searchsorted() method is assumed to be used on sorted arrays
# Find the indexes where the value 7 should be inserted
# import numpy as np
# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7)
# print(x) 

# Search From the Right Side
# By default the left most index is returned, but we can give side='right' 
# to return the right most index instead.
# Find the indexes where the value 7 should be inserted, starting from the right
# import numpy as np
# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7, side='right')
# print(x) 

# Multiple Values
# To search for more than one value, use an array with the specified values

# Find the indexes where the values 2, 4, and 6 should be inserted
import numpy as np
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x) 
