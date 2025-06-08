# Grid Search

# One method is to try out different values and then pick the value that gives the 
# best score. This technique is known as a grid search

# from sklearn import datasets
# from sklearn.linear_model import LogisticRegression
# iris = datasets.load_iris()
# X = iris['data']
# y = iris['target']
# logit = LogisticRegression(max_iter = 10000)
# print(logit.fit(X,y))
# print(logit.score(X,y))

# Implementing Grid Search
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
iris = datasets.load_iris()
X = iris['data']
y = iris['target']
logit = LogisticRegression(max_iter = 10000)
C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]

scores = []

for choice in C:
  logit.set_params(C=choice)
  logit.fit(X, y)
  scores.append(logit.score(X, y))
print(scores)





