# ufuncs stands for "Universal Functions" and they are NumPy functions 
# that operate on the ndarray object.

# ufuncs also take additional arguments, like:
# where boolean array or condition defining where the operations should take place.
# dtype defining the return type of elements.
# out output array where the return value should be copied.

# Converting iterative statements into a vector based operation is 
# called vectorization.

# Without ufunc, we can use Python's built-in zip() method:
# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = []
# for i, j in zip(x, y):
#   z.append(i + j)
# print(z) 

# With ufunc, we can use the add() function
import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z) 