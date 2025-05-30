# What is Interpolation?
# Interpolation is a method for generating points between given points.

# 1D Interpolation
# For given xs and ys interpolate values from 2.1, 2.2... to 2.9:
# from scipy.interpolate import interp1d
# import numpy as np
# xs = np.arange(10)
# ys = 2*xs + 1
# interp_func = interp1d(xs, ys)
# newarr = interp_func(np.arange(2.1, 3, 0.1))
# print(newarr)

# Spline Interpolation
# Find univariate spline interpolation for 2.1, 2.2... 2.9 for the following 
# non linear points:

# from scipy.interpolate import UnivariateSpline
# import numpy as np
# xs = np.arange(7)
# ys = xs**2 + np.sin(xs) + 1
# interp_func = UnivariateSpline(xs, ys)
# newarr = interp_func(np.arange(2, 3, 0.1))
# print(newarr) 

# Interpolation with Radial Basis Function

# Interpolate following xs and ys using rbf and find values for 2.1, 2.2 ... 2.9:
from scipy.interpolate import Rbf
import numpy as np
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = Rbf(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)