# NumPy provides the ufuncs sin(), cos() and tan() that take values in radians 
# and produce the corresponding sin, cos and tan values.

# import numpy as np
# x = np.sin(np.pi/2)
# print(x)

# Find sine values for all of the values in arr:
# import numpy as np
# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
# x = np.sin(arr)
# print(x) 

# Convert all of the values in following array arr to radians:
# import numpy as np
# arr = np.array([90, 180, 270, 360])
# x = np.deg2rad(arr)
# print(x) 

# Convert all of the values in following array arr to degrees:
# import numpy as np
# arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
# x = np.rad2deg(arr)
# print(x)

# Finding Angles
import numpy as np
x = np.arcsin(1.0)
print(x) 

# Angles of Each Value in Arrays
import numpy as np
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x) 

# Find the hypotenues for 4 base and 3 perpendicular:
import numpy as np
base = 3
perp = 4
x = np.hypot(base, perp)
print(x) 