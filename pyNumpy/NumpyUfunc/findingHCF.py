# Finding GCD (Greatest Common Devisor)

# Find the HCF of the following two numbers:
# import numpy as np
# n1 = 6
# n2 = 9
# n3 = 12
# x = np.gcd(n2, n3)
# print(x)

# Find the GCD for all of the numbers in the following array:
import numpy as np
arr1 = ([14, 4, 6, 8, 10, 12, 16])
y = np.gcd.reduce(arr1)
print(y)