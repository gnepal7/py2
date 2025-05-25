# Zipf Distribution
# Zipf distributions are used to sample data based on zipf's law.
# Zipf's Law: In a collection, the nth common term is 1/n times of the most 
# common term. E.g. the 5th most common word in English occurs nearly 1/5 
# times as often as the most common word.
# It has two parameters:
# a - distribution parameter.
# size - The shape of the returned array.

# Draw out a sample for zipf distribution with distribution parameter 2 with size 2x3:
from numpy import random
x = random.zipf(a=2, size=(2, 3))
print(x) 

# Visualization of Zipf Distribution
# Sample 200 points but plotting only ones with value < 10 for more meaningful chart.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.zipf(a=2, size=200)
sns.displot(x[x<10])
plt.show() 

