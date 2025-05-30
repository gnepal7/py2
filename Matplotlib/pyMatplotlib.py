# Matplotlib is a low level graph plotting library in python that serves 
# as a visualization utility.
# Matplotlib was created by John D. Hunter.
# Matplotlib is open source and we can use it freely.
# Matplotlib is mostly written in python, a few segments are written in C, 
# Objective-C and Javascript for Platform compatibility.

import matplotlib
print(matplotlib.__version__)

# Note: two underscore characters are used in __version__.

# Pyplot
# Most of the Matplotlib utilities lies under the pyplot submodule, and are 
# usually imported under the plt alias:

# Draw a line in a diagram from position (0,0) to position (6,250):
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0, 1])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()