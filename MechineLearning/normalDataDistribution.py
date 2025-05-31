# Normal Data Distribution

# A typical normal data distribution:
import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(3.0, 5.0, 1000)
plt.hist(x, 100)
plt.show() 

# in the example above 3 is mean value, 5 is standard deviation and 1000 is value
# Note: A normal distribution graph is also known as the bell curve because 
# of it's characteristic shape of a bell.