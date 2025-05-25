# Chi Square distribution is used as a basis to verify the hypothesis.
# It has two parameters:
# df - (degree of freedom).
# size - The shape of the returned array.

# Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3:
from numpy import random
x = random.chisquare(df=2, size=(2, 3))
print(x) 


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.chisquare(df=3, size=100), kind="kde")
plt.show() 

