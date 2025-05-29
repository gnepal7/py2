# Viewing the Data
# One of the most used method for getting a quick overview of the 
# DataFrame, is the head() method.
# The head() method returns the headers and a specified number of 
# rows, starting from the top.

# Get a quick overview by printing the first 10 rows of the DataFrame:
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.head(20)) 
# Print the first 5 rows of the DataFrame:
# print(df.head())

# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, 
# starting from the bottom

# Print the last 5 rows of the DataFrame:
import pandas as pd
df = pd.read_csv('data.csv')
# print(df.tail(10))

# Info About the Data
print(df.info())

