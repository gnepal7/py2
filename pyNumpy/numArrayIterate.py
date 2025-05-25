# Iterating Arrays

# Iterate on the elements of the following 1-D array
# import numpy as np
# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x) 

# Iterate on the elements of the following 2-D array
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x) 

# If we iterate on a n-D array it will go through n-1th dimension one by one
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   for y in x:
#     print(y) 

# Iterating 3-D Arrays
# Iterate on the elements of the following 3-D array
# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   print(x) 
# Iterate down to the scalars
# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   for y in x:
#     for z in y:
#       print(z) 

# Iterating Arrays Using nditer()
# The function nditer() is a helping function that can be used from very 
# basic to very advanced iterations. It solves some basic issues 
# which we face in iteration, lets go through it with examples
# Iterate through the following 3-D array
# import numpy as np
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#   print(x) 

# Iterating Array With Different Data Types
# Iterate through the array as a string
# import numpy as np
# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x) 

# Iterating With Different Step Size
# Iterate through every scalar element of the 2D array skipping 1 element
# import numpy as np
# arr = np.array([[1, 2, 3, 4, 9, 10], [5, 6, 7, 8, 11, 12]])
# for x in np.nditer(arr[:, ::2]):
#   print(x) 

#  Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one
# Enumerate on following 1D arrays elements
# import numpy as np
# arr = np.array([1, 2, 3])
# for idx, x in np.ndenumerate(arr):
#   print(idx, x) 

# Enumerate on following 2D array's elements
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x) 
