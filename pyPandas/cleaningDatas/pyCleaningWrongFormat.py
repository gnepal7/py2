# Cleaning Data of Wrong Format

# Convert Into a Correct Format
# In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, 
# the 'Date' column should be a string that represents a date

import pandas as pd
df = pd.read_csv(r"D:\MSCITM\5th-Python\py2\pyPandas\data.csv")
print("Columns in DataFrame:", df.columns)
df.columns = df.columns.str.strip()
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Handle date conversion
else:
    print("Column 'Date' not found.")
print(df.to_string())


# Discovering Duplicates
print(df.duplicated())

# Remove all duplicates
df.drop_duplicates(inplace = True) 

# Replacing Values
# Set "Duration" = 45 in row 7:
 df.loc[7, 'Duration'] = 45

#  If the value is higher than 120, set it to 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120




