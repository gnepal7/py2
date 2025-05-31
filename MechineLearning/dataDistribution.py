# Data Distribution
# How Can we Get Big Data Sets?
# To create big data sets for testing, we use the Python module NumPy, 
# which comes with a number of methods to create random data sets, of any size.

# Create an array containing 250 random floats between 0 and 5:
# import numpy
# x = numpy.random.uniform(0.0, 5.0, 250)
# print(x) 

# Histogram
# To visualize the data set we can draw a histogram with the data we collected

# Draw a histogram:
# import numpy
# import matplotlib.pyplot as plt
# x = numpy.random.uniform(0.0, 5.0, 100)
# plt.hist(x, 5)
# plt.show() 

# Big Data Distributions
# An array containing 250 values is not considered very big, but now you know 
# how to create a random set of values, and by changing the parameters, you 
# can create the data set as big as you want.

# Create an array with 100000 random numbers, and display them using a 
# histogram with 100 bars:
import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 10.0, 100000)
plt.hist(x, 100)
plt.show() 