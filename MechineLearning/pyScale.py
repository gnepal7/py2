# Scale Features
# There are different methods for scaling data, in this tutorial we will use a 
# method called standardization.

# The standardization method uses this formula:
# z = (x - u) / s
# Where z is the new value, x is the original value, u is the mean and s is the 
# standard deviation.

# Scale all values in the Weight and Volume columns:
# import pandas
# from sklearn import linear_model
# from sklearn.preprocessing import StandardScaler
# scale = StandardScaler()
# df = pandas.read_csv("data.csv")
# X = df[['Weight', 'Volume']]
# scaledX = scale.fit_transform(X)
# print(scaledX) 

# Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df = pandas.read_csv("data.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
scaledX = scale.fit_transform(X)
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)
scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2) 





