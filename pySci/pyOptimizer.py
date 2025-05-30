# Optimizers in SciPy
# Optimizers are a set of procedures defined in SciPy that either find the 
# minimum value of a function, or the root of an equation

# Find root of the equation x + cos(x):
# from scipy.optimize import root
# from math import cos
# def eqn(x):
#     return x + cos(x)
# myroot = root(eqn, 0)
# print(myroot.x)
# # Note: The returned object has much more information about the solution.
# print(myroot)

# Minimizing a Function
# Minimize the function x^2 + x + 2 with BFGS:
from scipy.optimize import minimize
def eqn(x):
  return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin)