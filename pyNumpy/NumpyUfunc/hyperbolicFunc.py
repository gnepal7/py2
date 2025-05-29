# Hyperbolic Func
# NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in 
# radians and produce the corresponding sinh, cosh and tanh values.

# Find sinh value of PI/2:
import numpy as np
x = np.sinh(np.pi/2)
print(x) 

# Find cosh values for all of the values in arr:
import numpy as np
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x) 

# Finding Angles
import numpy as np
x = np.arcsinh(1.0)
print(x) 

# Find the angle for all of the tanh values in array:
import numpy as np
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x) 


