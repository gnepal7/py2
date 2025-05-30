# Linestyle
# You can use the keyword argument linestyle, or shorter ls, to change 
# the style of the plotted line:

# Use a dotted line:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# dotted line style
# plt.plot(ypoints, linestyle = 'dotted')

# Use a dashed line:
# plt.plot(ypoints, linestyle = 'dashed')

# Shorter Syntax
# The line style can be written in a shorter syntax:
# linestyle can be written as ls.
# dotted can be written as :.
# dashed can be written as --.


# Line Styles
# You can choose any of these styles:
# Style 	            Or
# 'solid' (default) 	'-' 	
# 'dotted' 	        ':' 	
# 'dashed' 	        '--' 	
# 'dashdot' 	        '-.' 	
# 'None' 	'' or       ' '

# plt.plot(ypoints, ls = ':')
# plt.show()


# Line Color
# You can use the keyword argument color or the shorter c to set the color of the line:

# Set the line color to red:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, color = 'r', ls = '--')
# plt.plot(ypoints, c = '#4CAF50', ls = ':')
# plt.show()

# Line Width
# You can use the keyword argument linewidth or the shorter lw to 
# change the width of the line.
# The value is a floating number, in points:

# Plot with a 5pt wide line:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linewidth = '5', c = 'r', ls = '--')
# plt.show()


# Multiple Lines
# You can plot as many lines as you like by simply adding more plt.plot() functions:

# Draw two lines by specifying a plt.plot() function for each line:
# import matplotlib.pyplot as plt
# import numpy as np
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(y1, lw = '3', c = 'r', ls = ':')
# plt.plot(y2, lw = '2', c = 'y', ls = '--')
# plt.show()


# Draw two lines by specifiyng the x- and y-point values for both lines:
import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)
plt.show()