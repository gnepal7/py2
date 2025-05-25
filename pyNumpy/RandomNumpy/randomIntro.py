# Random number does NOT mean a different number every time. Random means 
# something that can not be predicted logically.

# Pseudo Random and True Random.

# Generate Random Number
# Generate a random integer from 0 to 100
# from numpy import random
# x = random.randint(100)
# print(x) 

# Generate Random Float
# The random module's rand() method returns a random float between 0 and 1
# from numpy import random
# x = random.rand()
# print(x) 

# Generate Random Array
# The randint() method takes a size parameter where you can specify 
# the shape of an array.
# Generate a 1-D array containing 5 random integers from 0 to 100:
# from numpy import random
# x=random.randint(100, size=(5))
# print(x) 

# Generate a 2-D array with 3 rows, each row containing 5 random 
# integers from 0 to 100
# from numpy import random
# x = random.randint(100, size=(3, 5))
# print(x) 

# Floats
# The rand() method also allows you to specify the shape of the array.
# from numpy import random
# x = random.rand(5)
# print(x) 

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
# from numpy import random
# x = random.rand(3, 5)
# print(x) 

# Generate Random Number From Array
# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values

# Return one of the values in an array:
# from numpy import random
# x = random.choice([3, 5, 7, 9])
# print(x) 

# Generate a 2-D array that consists of the values in the array 
# parameter (3, 5, 7, and 9)
from numpy import random
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x) 