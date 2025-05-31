# Creating Bars
# With Pyplot, you can use the bar() function to draw bar graphs:

# Draw 4 bars:
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x,y)
# plt.show()

# Horizontal Bars
# If you want the bars to be displayed horizontally instead of vertically, 
# use the barh() function:

# Draw 4 horizontal bars:
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.barh(x, y)
# plt.show()

# Bar Color
# The bar() and barh() take the keyword argument color to set the color of the bars:

# Draw 4 red bars:
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y, color = "red")
# plt.show()

# Color Names
# You can use any of the 140 supported color names.

# Draw 4 "hot pink" bars:
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
# with color pink
# plt.bar(x, y, color = "hotpink")

# with hex color and bar width
plt.bar(x, y, color = "#4CAF50", width = 0.2)
plt.show()
# The default width value is 0.8

# Note: For horizontal bars, use height instead of width.

# Bar Height
# The barh() takes the keyword argument height to set the height of the bars:

# Draw 4 very thin bars:
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y, height = 0.1)
plt.show()





