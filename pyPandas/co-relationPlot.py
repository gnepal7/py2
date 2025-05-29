# Finding Relationships
# A great aspect of the Pandas module is the corr() method.
# The corr() method calculates the relationship between each column in your data set.

# import pandas as pd
# df = pd.read_csv("data.csv")
# df2 = df.corr() 
# print(df2)

# Perfect Correlation:
# We can see that "Duration" and "Duration" got the number 1.000000, 
# which makes sense, each column always has a perfect relationship with itself.

# Good Correlation:
# "Duration" and "Calories" got a 0.922721 correlation, which is a very good 
# correlation, and we can predict that the longer you work out, the more calories 
# you burn, and the other way around: if you burned a lot of calories, you probably 
# had a long work out.

# Bad Correlation:
# "Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad 
# correlation, meaning that we can not predict the max pulse by just looking 
# at the duration of the work out, and vice versa.


# Plotting
# Pandas uses the plot() method to create diagrams.
# We can use Pyplot, a submodule of the Matplotlib library to visualize the 
# diagram on the screen

# Import pyplot from Matplotlib and visualize our DataFrame:
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('data.csv')
# df.plot()
# plt.show() 

# Scatter Plot
# Specify that you want a scatter plot with the kind argument:
# kind = 'scatter'
# A scatter plot needs an x- and a y-axis.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# plt.show() 


# Histogram
# Use the kind argument to specify that you want a histogram:
# kind = 'hist'
df["Duration"].plot(kind = 'hist')
plt.show()
