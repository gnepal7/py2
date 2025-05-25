# Poisson Distribution
# Poisson Distribution is a Discrete Distribution
# It has two parameters:
# lam - rate or known number of occurrences e.g. 2 for above problem.
# size - The shape of the returned array.

# Generate a random 1x10 distribution for occurrence 2:
# from numpy import random
# x = random.poisson(lam=2, size=7)
# print(x) 

# Visualization of Poisson Distribution
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.displot(random.poisson(lam=2, size=500))
# plt.show() 

# Difference Between Normal and Poisson Distribution
# Normal distribution is continuous whereas poisson is discrete
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# data = {
#   "normal": random.normal(loc=50, scale=7, size=1000),
#   "poisson": random.poisson(lam=50, size=1000)
# }
# sns.displot(data, kind="kde")
# plt.show() 

# Difference Between Binomial and Poisson Distribution 
# Binomial distribution only has two possible outcomes, whereas poisson 
# distribution can have unlimited possible outcomes
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
data = {
  "binomial": random.binomial(n=1000, p=0.01, size=1000),
  "poisson": random.poisson(lam=10, size=1000)
}
sns.displot(data, kind="kde")
plt.show() 


