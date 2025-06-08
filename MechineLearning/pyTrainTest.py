# Evaluate Your Model

# Train/Test is a method to measure the accuracy of your model.
# It is called Train/Test because you split the data set into two sets: 
# a training set and a testing set.

# Start With a Data Set
# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(2)
# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100) / x
# # plt.scatter(x, y)

# # train_x = np.random.normal(3, 1, 50)  
# # train_y = np.random.normal(150, 40, 50)

# # test_x = np.random.normal(3, 1, 50)  
# # test_y = np.random.normal(150, 40, 50)

# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

# # Display the Training Set
# # plt.scatter(train_x, train_y)
# # displaying the test set
# plt.scatter(test_x, test_y)
# plt.show() 


# Draw a polynomial regression line through the data points:
# import numpy
# import matplotlib.pyplot as plt
# numpy.random.seed(2)

# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100) / x

# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

# mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

# myline = numpy.linspace(0, 6, 100)

# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))
# plt.show() 


# Remember R2, also known as R-squared?
# It measures the relationship between the x axis and the y axis, and the value 
# ranges from 0 to 1, where 0 means no relationship, and 1 means totally related.
# The sklearn module has a method called r2_score() that will help us 
# find this relationship.

# How well does my training data fit in a polynomial regression?
# import numpy
# from sklearn.metrics import r2_score
# numpy.random.seed(2)

# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100) / x

# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

# mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
# r2 = r2_score(train_y, mymodel(train_x))
# print(r2)
# Note: The result 0.799 shows that there is a OK relationship.

# Bring in the Testing Set
# Let us find the R2 score when using testing data:
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
r2 = r2_score(test_y, mymodel(test_x))
print(r2) 

# Note: The result 0.809 shows that the model fits the testing set as well, 
# and we are confident that we can use the model to predict future values.