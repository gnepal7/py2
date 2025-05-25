# Multinomial Distribution
# Multinomial distribution is a generalization of binomial distribution.
# It has three parameters:
# n - number of times to run the experiment.
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] 
# for dice roll).
# size - The shape of the returned array.

# Draw out a sample for dice roll:
from numpy import random
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x) 


# Note: Multinomial samples will NOT produce a single value! They will 
# produce one value for each pval.

# Note: As they are generalization of binomial distribution their visual 
# representation and similarity of normal distribution is same as that of 
# multiple binomial distributions

