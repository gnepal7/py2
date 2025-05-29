# Find the LCM of the following two numbers:
import numpy as np
np1 = 5
np2 = 20
result = np.lcm(np1, np2)
print(result)

# Find the LCM of the values of the following array:
num1 = ([5, 10, 15, 20])
y = np.lcm.reduce(num1)
print(y)

# Find the LCM of all values of an array where the array contains
# all integers from 1 to 10:
import numpy as np
arr = np.arange(1, 9)
x = np.lcm.reduce(arr)
print(x) 