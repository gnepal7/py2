# Logistic Regression
# Logistic regression aims to solve classification problems. It does this by 
# predicting categorical outcomes, unlike linear regression that predicts 
# a continuous outcome.

# import numpy
# from sklearn import linear_model
# #Reshaped for Logistic function. The values in X are independent and Y are dependent.
# X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
# y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
# logr = linear_model.LogisticRegression()
# logr.fit(X,y)
# predicted = logr.predict(numpy.array([3.46]).reshape(-1,1))
# print(predicted)


# Coefficient
# In logistic regression the coefficient is the expected change in log-odds of 
# having the outcome per unit change in X.

# import numpy
# from sklearn import linear_model
# X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
# y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
# logr = linear_model.LogisticRegression()
# logr.fit(X,y)
# log_odds = logr.coef_
# odds = numpy.exp(log_odds)
# print(odds)

# Probability
# The coefficient and intercept values can be used to find the probability that 
# each tumor is cancerous.

import numpy
from sklearn import linear_model
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
logr = linear_model.LogisticRegression()
logr.fit(X,y)
def logit2prob(logr, X):
  log_odds = logr.coef_ * X + logr.intercept_
  odds = numpy.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)
print(logit2prob(logr, X))