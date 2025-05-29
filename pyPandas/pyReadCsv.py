# Read CSV Files

# Load the CSV into a DataFrame:
# import pandas as pd
# df = pd.read_csv('output.csv')
# print(df.to_string()) 
# Tip: use to_string() to print the entire DataFrame.

# max_rows for printing maximum rows
import pandas as pd
pd.options.display.max_rows = 10
df = pd.read_csv('output.csv')
df2 = pd.read_csv('DatasetTasks.csv')
print(df2) 