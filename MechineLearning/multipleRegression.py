# Multiple Regression

# Multiple regression is like linear regression, but with more than one 
# independent value, meaning that we try to predict a value based on 
# two or more variables

# Tip: It is common to name the list of independent values with a upper case X, and the 
# list of dependent values with a lower case y.

# import pandas
# from sklearn import linear_model
# df = pandas.read_csv("data.csv")
# X = df[['Weight', 'Volume']]
# y = df['CO2']
# regr = linear_model.LinearRegression()
# regr.fit(X, y)
# #predict the CO2 emission of a car where the weight is 2300kg, 
# # and the volume is 1300cm3:
# predictedCO2 = regr.predict([[2300, 1300]])
# print(predictedCO2) 

# The coefficient is a factor that describes the relationship with an unknown variable.
# Example: if x is a variable, then 2x is x two times. x is the unknown variable, and 
# the number 2 is the coefficient

# Print the coefficient values of the regression object:
# import pandas
# from sklearn import linear_model
# df = pandas.read_csv("data.csv")

# X = df[['Weight', 'Volume']]
# y = df['CO2']
# regr = linear_model.LinearRegression()
# regr.fit(X, y)
# print(regr.coef_) 

# Copy the example from before, but change the weight from 2300 to 3300:
import pandas
from sklearn import linear_model
df = pandas.read_csv("data.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2) 