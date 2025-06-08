# What is a confusion matrix?
# It is a table that is used in classification problems to assess where errors 
# in the model were made.
# The rows represent the actual classes the outcomes should have been. 
# While the columns represent the predictions we have made. Using this 
# table it is easy to see which predictions are wrong

# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn import metrics
# actual = np.random.binomial(1,.9,size = 1000)
# predicted = np.random.binomial(1,.9,size = 1000)
# confusion_matrix = metrics.confusion_matrix(actual, predicted)
# cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])
# cm_display.plot()
# plt.show()


# Accuracy
# How to Calculate
# (True Positive + True Negative) / Total Predictions

# import numpy
# from sklearn import metrics
# actual = numpy.random.binomial(1,.9,size = 1000)
# predicted = numpy.random.binomial(1,.9,size = 1000)
# Accuracy = metrics.accuracy_score(actual, predicted)
# print(Accuracy)

# Precision
# How to calculate
# True Positive / (True Positive + False Positive)

# import numpy
# from sklearn import metrics
# actual = numpy.random.binomial(1,.9,size = 1000)
# predicted = numpy.random.binomial(1,.9,size = 1000)
# Precision = metrics.precision_score(actual, predicted)
# print(Precision)


# Sensitivity (Recall)
# How to Calculate
# True Positive / (True Positive + False Negative)

# import numpy
# from sklearn import metrics
# actual = numpy.random.binomial(1,.9,size = 1000)
# predicted = numpy.random.binomial(1,.9,size = 1000)
# Sensitivity_recall = metrics.recall_score(actual, predicted)
# print(Sensitivity_recall)

# Specificity
# How to Calculate
# True Negative / (True Negative + False Positive)

# import numpy
# from sklearn import metrics
# actual = numpy.random.binomial(1,.9,size = 1000)
# predicted = numpy.random.binomial(1,.9,size = 1000)
# Specificity = metrics.recall_score(actual, predicted, pos_label=0)
# print(Specificity)

# F-score
# F-score is the "harmonic mean" of precision and sensitivity.
# How to Calculate
# 2 * ((Precision * Sensitivity) / (Precision + Sensitivity))

# import numpy
# from sklearn import metrics
# actual = numpy.random.binomial(1,.9,size = 1000)
# predicted = numpy.random.binomial(1,.9,size = 1000)
# F1_score = metrics.f1_score(actual, predicted)
# print(F1_score)

# all in same print
import numpy
from sklearn import metrics
actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)
Accuracy = metrics.accuracy_score(actual, predicted)
Precision = metrics.precision_score(actual, predicted)
Sensitivity_recall = metrics.recall_score(actual, predicted)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)
F1_score = metrics.f1_score(actual, predicted)

#metrics:
print({"Accuracy":Accuracy,"recision":Precision,"Sensitivity_recall":Sensitivity_recall,"Specificity":Specificity,"F1_score":F1_score})