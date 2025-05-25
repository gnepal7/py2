# Binomial Distribution
# Binomial Distribution is a Discrete Distribution.
# It describes the outcome of binary scenarios, e.g. toss of a coin, 
# it will either be head or tails.
# It has three parameters:
# n - number of trials.
# p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.

# Given 10 trials for coin toss generate 10 data points
# from numpy import random
# x = random.binomial(n=10, p=0.5, size=10)
# print(x) 

# Visualization of Binomial Distribution
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.displot(random.binomial(n=10, p=0.5, size=500))
# plt.show() 

# Difference Between Normal and Binomial Distribution
# The main difference is that normal distribution is continous whereas binomial 
# is discrete, but if there are enough data points it will be quite similar to 
# normal distribution with certain loc and scale.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
data = {
  "normal": random.normal(loc=50, scale=5, size=500),
  "binomial": random.binomial(n=100, p=0.5, size=500)
}
sns.displot(data, kind="kde")
plt.show() 



