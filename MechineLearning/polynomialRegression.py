# Polynomial regression, like linear regression, uses the relationship between 
# the variables x and y to find the best way to draw a line through the data points

# Import numpy and matplotlib then draw the line of Polynomial Regression:
# import numpy as np
# import matplotlib.pyplot as plt

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# mymodel = np.poly1d(np.polyfit(x, y, 3))
# myline = np.linspace(1, 22, 100)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show() 


# R-Squared
# It is important to know how well the relationship between the values of 
# the x- and y-axis is, if there are no relationship the polynomial 
# regression can not be used to predict anything.
# The relationship is measured with a value called the r-squared.
# The r-squared value ranges from 0 to 1, where 0 means no relationship, 
# and 1 means 100% related

# How well does my data fit in a polynomial regression?
# import numpy
# from sklearn.metrics import r2_score
# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# print(r2_score(y, mymodel(x)))
# Note: The result 0.94 shows that there is a very good relationship, 
# and we can use polynomial regression in future predictions.

# Predict Future Values
# Predict the speed of a car passing at 17:00:
# import numpy
# from sklearn.metrics import r2_score
# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# speed = mymodel(17)
# print(speed) 

# Bad Fit?

# Let us create an example where polynomial regression would not be the 
# best method to predict future values.

# These values for the x- and y-axis should result in a very bad fit for 
# polynomial regression:
# import numpy
# import matplotlib.pyplot as plt
# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# myline = numpy.linspace(2, 95, 100)
# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show() 

# And the r-squared value?

# You should get a very low r-squared value.
import numpy
from sklearn.metrics import r2_score
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print(r2_score(y, mymodel(x)))