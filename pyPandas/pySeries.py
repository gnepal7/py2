# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# Create a simple Pandas Series from a list:
# import pandas as pd
# set1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# var1 = pd.Series(set1)
# print(var1)
# print(var1[3])

# With the index argument, you can name your own labels.
# create youe own label
# var2 = pd.Series(set1, index = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
# print(var2)
# print(var2["e"])

# Key/Value Objects as Series
# Create a simple Pandas Series from a dictionary:
# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390, "day4": 370, "day5": 350}
# myvar = pd.Series(calories)
# print(myvar)
# Create a Series using only data from "day1" and "day2":
# myvar2 = pd.Series(calories, index = ["day1", "day2", "day3"])
# print(myvar2)

# Pandas DataFrames
# A Pandas DataFrame is a 2 dimensional data structure, 
# like a 2 dimensional array, or a table with rows and columns.

# Create a simple Pandas DataFrame:
# import pandas as pd
# data = {
#   "calories": [420, 380, 390, 380, 350, 340, 320],
#   "duration": [50, 40, 45, 42, 38, 36, 43]
# }
# myvar = pd.DataFrame(data)
# print(myvar)
# Locate Row
# print(myvar.loc[1])
# Return row 0 and 1:
# print(myvar.loc[[0, 2]])

# Note: When using [], the result is a Pandas DataFrame.

# Named Indexes
# With the index argument, you can name your own indexes

# Add a list of names to give each row a name:
# import pandas as pd
# data = {
#   "calories": [420, 380, 390, 370, 350],
#   "duration": [50, 40, 45, 38, 43]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3", "day4", "day5"])
# print(df) 
# Locate Named Indexes
# print(df.loc["day3"])

# Load Files Into a DataFrame
import pandas as pd
df = pd.read_csv('Student.csv')
print(df) 

