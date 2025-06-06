# Matlab Arrays
# SciPy provides us with the module scipy.io, which has functions for 
# working with Matlab arrays.

# Exporting Data in Matlab Format
# The savemat() function allows us to export data in Matlab format.
# The method takes the following parameters:
    # filename - the file name for saving data.
    # mdict - a dictionary containing the data.
    # do_compression - a boolean value that specifies whether to compress 
    # the result or not. Default False.

# Export the following array as variable name "vec" to a mat file:
# from scipy import io
# import numpy as np
# arr = np.arange(10)
# io.savemat('arr.mat', {"vec": arr})

# Note: The example above saves a file name "arr.mat" on your computer.
# To open the file, check out the "Import Data from Matlab Format" example below:

# Import Data from Matlab Format
# The loadmat() function allows us to import data from a Matlab file

# Import the array from following mat file.:
from scipy import io
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])
# Export:
io.savemat('arr.mat', {"vec": arr})
# Import:
# mydata = io.loadmat('arr.mat')
# print(mydata) 

# Use the variable name "vec" to display only the array from the matlab data:
# print(mydata['vec']) 

mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec']) 



