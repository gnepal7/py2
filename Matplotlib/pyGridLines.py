# Add Grid Lines to a Plot
# With Pyplot, you can use the grid() function to add grid lines to the plot.

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)
# plt.grid()
# plt.show() 


# Specify Which Grid Lines to Display
# You can use the axis parameter in the grid() function to specify which 
# grid lines to display.
# Legal values are: 'x', 'y', and 'both'. Default value is 'both'.

# Display only grid lines for the x-axis:
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)
# plt.grid(axis = 'x', c = '#eeeeee', lw = '1', ls = '--')
# plt.show() 

# Display only grid lines for the y-axis:
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid(axis = 'y', c = '#bbbbbb', lw = '3', ls = ':' )
plt.show() 