# Cross Validation

# K-Fold
# The training data used in the model is split, into k number of smaller sets, 
# to be used to validate the model. The model is then trained on k-1 folds 
# of training set

# Run k-fold CV:
# from sklearn import datasets
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import KFold, cross_val_score
# X, y = datasets.load_iris(return_X_y=True)
# clf = DecisionTreeClassifier(random_state=42)
# k_folds = KFold(n_splits = 5)
# scores = cross_val_score(clf, X, y, cv = k_folds)
# print("Cross Validation Scores: ", scores)
# print("Average CV Score: ", scores.mean())
# print("Number of CV Scores used in Average: ", len(scores))

# Stratified K-Fold
# from sklearn import datasets
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import StratifiedKFold, cross_val_score
# X, y = datasets.load_iris(return_X_y=True)
# clf = DecisionTreeClassifier(random_state=42)
# sk_folds = StratifiedKFold(n_splits = 5)
# scores = cross_val_score(clf, X, y, cv = sk_folds)
# print("Cross Validation Scores: ", scores)
# print("Average CV Score: ", scores.mean())
# print("Number of CV Scores used in Average: ", len(scores))

# Leave-One-Out (LOO)
# from sklearn import datasets
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import LeaveOneOut, cross_val_score
# X, y = datasets.load_iris(return_X_y=True)
# clf = DecisionTreeClassifier(random_state=42)
# loo = LeaveOneOut()
# scores = cross_val_score(clf, X, y, cv = loo)
# print("Cross Validation Scores: ", scores)
# print("Average CV Score: ", scores.mean())
# print("Number of CV Scores used in Average: ", len(scores))


# Leave-P-Out (LPO)
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeavePOut, cross_val_score
X, y = datasets.load_iris(return_X_y=True)
clf = DecisionTreeClassifier(random_state=42)
lpo = LeavePOut(p=2)
scores = cross_val_score(clf, X, y, cv = lpo)
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))


# Shuffle Split
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import ShuffleSplit, cross_val_score
X, y = datasets.load_iris(return_X_y=True)
clf = DecisionTreeClassifier(random_state=42)
ss = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits = 5)
scores = cross_val_score(clf, X, y, cv = ss)
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))