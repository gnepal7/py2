# Reshaping arrays

# Reshape From 1-D to 2-D
# Convert the following 1-D array with 12 elements into a 2-D array
# The outermost dimension will have 4 arrays, each with 3 elements
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr) 

# Reshape From 1-D to 3-D
# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, 
# each with 2 elements
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr) 

# Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.

# Returns Copy or View?
# Check if the returned array is a copy or a view
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(arr.reshape(2, 4).base) 

# Unknown Dimension
# Convert 1D array with 8 elements to 3D array with 2x2 elements
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(2, 2, -1)
# print(newarr) 
# Note: We can not pass -1 to more than one dimension

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this
# Convert the array into a 1D array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr) 

