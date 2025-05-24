# The array object in NumPy is called ndarray, it provides a lot of 
# supporting functions that make working with ndarray very easy.

# Data Science: is a branch of computer science where we study how to store, 
# use and analyze data for deriving information from it.

# Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, 
# so processes can access and manipulate them very efficiently. This behavior is 
# called locality of reference in computer science. This is the main reason why 
# NumPy is faster than lists. Also it is optimized to work with 
# latest CPU architectures.

# Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python, but most of the parts 
# that require fast computation are written in C or C++

# Where is the NumPy Codebase?
# The source code for NumPy is located at this github 
# repository https://github.com/numpy/numpy

import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

# NumPy as np
# Now the NumPy package can be referred to as np instead of numpy
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)

# Checking NumPy Version
import numpy as np
print(np.__version__)


