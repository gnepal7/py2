# Bootstrap Aggregation (Bagging)
# Bootstrap Aggregation (bagging) is a ensembling method that attempts to resolve 
# overfitting for classification or regression problems. Bagging aims to improve 
# the accuracy and performance of machine learning algorithms.

# Import the necessary data and evaluate base classifier performance.
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.tree import DecisionTreeClassifier
# data = datasets.load_wine(as_frame = True)

# X = data.data
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 22)
# dtree = DecisionTreeClassifier(random_state = 22)
# dtree.fit(X_train,y_train)
# y_pred = dtree.predict(X_test)

# print("Train data accuracy:",accuracy_score(y_true = y_train, y_pred = dtree.predict(X_train)))
# print("Test data accuracy:",accuracy_score(y_true = y_test, y_pred = y_pred))


# BaggingClassifier 
# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.ensemble import BaggingClassifier

# data = datasets.load_wine(as_frame = True)

# X = data.data
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 22)

# estimator_range = [2,4,6,8,10,12,14,16]

# models = []
# scores = []

# for n_estimators in estimator_range:
#     # Create bagging classifier
#     clf = BaggingClassifier(n_estimators = n_estimators, random_state = 22)
#     # Fit the model
#     clf.fit(X_train, y_train)
#     # Append the model and score to their respective list
#     models.append(clf)
#     scores.append(accuracy_score(y_true = y_test, y_pred = clf.predict(X_test)))

# # Generate the plot of scores against number of estimators
# plt.figure(figsize=(9,6))
# plt.plot(estimator_range, scores)

# # Adjust labels and font (to make visable)
# plt.xlabel("n_estimators", fontsize = 18)
# plt.ylabel("score", fontsize = 18)
# plt.tick_params(labelsize = 16)

# # Visualize plot
# plt.show()


# Another Form of Evaluation
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import BaggingClassifier

# data = datasets.load_wine(as_frame = True)

# X = data.data
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 22)

# oob_model = BaggingClassifier(n_estimators = 12, oob_score = True,random_state = 22)

# oob_model.fit(X_train, y_train)

# print(oob_model.oob_score_)

# Generating Decision Trees from Bagging Classifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import plot_tree

# Load the dataset
data = datasets.load_iris()  # Example: Using the Iris dataset

X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=22)

# Create and fit the Bagging classifier
clf = BaggingClassifier(n_estimators=12, oob_score=True, random_state=22)
clf.fit(X_train, y_train)

# Plot the first decision tree in the ensemble
plt.figure(figsize=(10, 15))
plot_tree(clf.estimators_[0], feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.show()



