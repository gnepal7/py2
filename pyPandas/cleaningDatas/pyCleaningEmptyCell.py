# Data Cleaning

# Data cleaning means fixing bad data in your data set.
# Bad data could be:
    # Empty cells
    # Data in wrong format
    # Wrong data
    # Duplicates


# Cleaning Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.
# Remove Rows: # One way to deal with empty cells is to remove rows that 
# contain empty cells.
# import pandas as pd
# df = pd.read_csv("D:\\MSCITM\\5th-Python\\py2\\pyPandas\\data.csv")
# print(df.to_string())

# after removing empty cells
# new_df = df.dropna()
# print(new_df.to_string())
# Note: By default, the dropna() method returns a new DataFrame, and 
# will not change the original.

# If you want to change the original DataFrame, use the inplace = True argument:
# df.dropna(inplace = True)
# print(df.to_string()) 
# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it 
# will remove all rows containing NULL values from the original DataFrame.

# Replace Empty Values
# df.fillna(130, inplace = True) 
# print(df.to_string())

# Replace Only For Specified Columns
# Replace NULL values in the "Calories" columns with the number 130:
# import pandas as pd
# df = pd.read_csv("D:\\MSCITM\\5th-Python\\py2\\pyPandas\\data.csv")
# df.fillna({"Calories": 130}, inplace=True) 
# print(df.to_string())

# Replace Using Mean, Median, or Mode
# import pandas as pd
# df = pd.read_csv("D:\\MSCITM\\5th-Python\\py2\\pyPandas\\data.csv")
# x = df["Calories"].mean()
# df.fillna({"Calories": x}, inplace=True) 
# print(df.to_string())
# Mean = the average value (the sum of all values divided by number of values).

# Calculate the MEDIAN, and replace any empty values with it:
# import pandas as pd
# df = pd.read_csv("D:\\MSCITM\\5th-Python\\py2\\pyPandas\\data.csv")
# x = df["Calories"].median()
# df.fillna({"Calories": x}, inplace=True) 
# print(df.to_string())

# Calculate the MODE, and replace any empty values with it:
import pandas as pd 
df = pd.read_csv("D:\\MSCITM\\5th-Python\\py2\\pyPandas\\data.csv")
x = df["Calories"].mode()[0]
df.fillna({"Calories": x}, inplace=True) 
print(df.to_string())
# Mode = the value that appears most frequently.