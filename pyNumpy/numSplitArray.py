# Splitting NumPy Arrays
# Splitting is reverse operation of Joining.
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# We use array_split() for splitting arrays, we pass it the array we want to 
# split and the number of splits

# Split the array in 3 parts
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = np.array_split(arr, 4)
# print(newarr) 

# If the array has less elements than required, it will adjust from the 
# end accordingly

# Split the array in 4 parts
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr) 
# Note: We also have the method split() available but it will not adjust the 
# elements when elements are less in source array for splitting like in 
# example above, array_split() worked properly but split() would fail.

# Split Into Arrays
# The return value of the array_split() method is an array containing each 
# of the split as an array.
# If you split an array into 3 arrays, you can access them from the result 
# just like any array element

# Access the splitted arrays
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2]) 

# Splitting 2-D Arrays
# Use the same syntax when splitting 2-D arrays.
# Use the array_split() method, pass in the array you want to split 
# and the number of splits you want to do

# Split the 2-D array into three 2-D arrays
# import numpy as np
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr) 

# Split the 2-D array into three 2-D arrays
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], 
# [16, 17, 18]])
# newarr = np.array_split(arr, 3)
# print(newarr) 

# Split the 2-D array into three 2-D arrays along columns
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], 
# [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr, 3, axis=1)
# print(newarr) 

# Use the hsplit() method to split the 2-D array into three 2-D arrays along columns
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], 
[13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)
# Similar alternates to vstack() and dstack() are available as vsplit() and dsplit()
