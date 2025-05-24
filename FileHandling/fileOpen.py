# The open() function takes two parameters; filename, and mode

#There are four different methods (modes) for opening a file
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

import os
import pandas as pd

# Check current working directory
print(os.getcwd())
# List files in the current directory
print(os.listdir(os.getcwd()))
# Read the Excel file
file_path = "D:\\MSCITM\\5th-Python\\py2\\FileHandling\\student.xlsx"
df = pd.read_excel(file_path)
# Display the contents of the DataFrame
print(df)


