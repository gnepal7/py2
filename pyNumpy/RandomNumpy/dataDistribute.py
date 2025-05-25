# Random Data Distribution
# Data Distribution is a list of all possible values, and how often each value occurs.
# Such lists are important when working with statistics and data science.
# The random module offer methods that returns randomly generated data distributions

# Probability Density Function: A function that describes a continuous probability. 
# i.e. probability # of all values in an array.

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9
# from numpy import random
# x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.5, 0.1], size=(50))
# print(x) 

# Same example as above, but return a 2-D array with 3 rows, each containing 5 values
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x) 
