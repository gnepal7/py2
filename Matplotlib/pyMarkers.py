# Markers
# You can use the keyword argument marker to emphasize each 
# point with a specified marker:

# Mark each point with a circle:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'p')
# plt.show()

# Mark each point with a star:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = '*')
# plt.show()

# Marker Reference
# You can choose any of these markers:
# Marker 	Description
# 'o' 	    Circle 	
# '*' 	    Star 	
# '.' 	    Point 	
# ',' 	    Pixel 	
# 'x' 	    X 	
# 'X' 	    X (filled) 	
# '+' 	    Plus 	
# 'P' 	    Plus (filled) 	
# 's' 	    Square 	
# 'D' 	    Diamond 	
# 'd' 	    Diamond (thin) 	
# 'p' 	    Pentagon 	
# 'H' 	    Hexagon 	
# 'h' 	    Hexagon 	
# 'v' 	    Triangle Down 	
# '^' 	    Triangle Up 	
# '<' 	    Triangle Left 	
# '>' 	    Triangle Right 	
# '1' 	    Tri Down 	
# '2' 	    Tri Up 	
# '3' 	    Tri Left 	
# '4' 	    Tri Right 	
# '|' 	    Vline 	
# '_' 	    Hline

# Format Strings fmt
# You can also use the shortcut string notation parameter to specify the marker.
# This parameter is also called fmt, and is written with this syntax:
# marker|line|color

# Mark each point with a circle:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'H--g')
# plt.show()

# Line Reference
# Line Syntax 	Description
# '-' 	        Solid line 	
# ':' 	        Dotted line 	
# '--' 	        Dashed line 	
# '-.' 	        Dashed/dotted line

# Color Reference
# Color Syntax 	Description
# 'r' 	        Red 	
# 'g' 	        Green 	
# 'b' 	        Blue 	
# 'c' 	        Cyan 	
# 'm' 	        Magenta 	
# 'y' 	        Yellow 	
# 'k' 	        Black 	
# 'w' 	        White

# Marker Size
# You can use the keyword argument markersize or the shorter version, 
# ms to set the size of the markers:

# Set the size of the markers to 20:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'd--c', ms = 10)
# plt.show()

# Marker Color
# You can use the keyword argument markeredgecolor or the shorter mec to 
# set the color of the edge of the markers:

# Set the EDGE color to red:
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'd--b', ms = 10, mec = 'y')
# Set the FACE color to red:
# plt.plot(ypoints, 'd--b', ms = 20, mfc = 'r', mec = 'r')

# Mark each point with a beautiful green color:
# plt.plot(ypoints, 's--r', ms = 20, mfc = '#4CAF50', mec = '#4CAF50')

# Mark each point with the color named "hotpink":
plt.plot(ypoints, 's-r', ms = 20, mfc = 'hotpink', mec = 'hotpink')
plt.show()