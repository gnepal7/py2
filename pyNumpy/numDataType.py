# Data Types in Python
# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

# Data Types in NumPy
    # i - integer
    # b - boolean
    # u - unsigned integer
    # f - float
    # c - complex float
    # m - timedelta
    # M - datetime
    # O - object
    # S - string
    # U - unicode string
    # V - fixed chunk of memory for other type ( void )

# The NumPy array object has a property called dtype that 
# returns the data type of the array
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr.dtype) 

# Get the data type of an array containing strings:
# import numpy as np
# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype) 

# Creating Arrays With a Defined Data Type
# Create an array with data type string
# import numpy as np
# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype) 

# Create an array with data type 4 bytes integer
# import numpy as np
# arr = np.array([1, 2, 3, 4], dtype='i8')
# print(arr)
# print(arr.dtype) 

# What if a Value Can Not Be Converted?
# If a type is given in which elements can't be casted then NumPy will 
# raise a ValueError.
# ValueError: In Python ValueError is raised when the type of 
# passed argument to a function is unexpected/incorrect.
# A non integer string like 'a' can not be converted to integer (will raise an error):
# import numpy as np
# arr = np.array(['a', '2', '3'], dtype='i') 

# Converting Data Type on Existing Arrays
# Change data type from float to integer by using 'i' as parameter value
# import numpy as np
# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i8')
# print(newarr)
# print(newarr.dtype) 

# Change data type from float to integer by using int as parameter value
# import numpy as np
# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype) 

# Change data type from integer to boolean
import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype) 
