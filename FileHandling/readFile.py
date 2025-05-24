# Open a File on the Server
# import os
# import pandas as pd

# Check current working directory
# print(os.getcwd())
# Read the Excel file
# file_path = "D:\\MSCITM\\5th-Python\\py2\\FileHandling\\student.xlsx"
# df = pd.read_excel(file_path)
# # Display the contents of the DataFrame
# print(df)

# import os
# import pandas as pd
# print(os.getcwd())
# # Open a file on a different location
# file_path2 = "D:\\MSCITM\\5th-Python\\pyscript\\bs4.html"
# df2 = pd.read_html(file_path2)
# print(df2[0])

# import os
# import pandas as pd
# # Check current working directory
# print(os.getcwd())
# # Open a file on a different location
# file_path2 = "D:\\MSCITM\\5th-Python\\pyscript\\mouseInfoLog.txt"
# # Read the text file (assuming it's comma-separated)
# df2 = pd.read_csv(file_path2, delimiter='\t')  # Change delimiter as needed
# # Display the DataFrame
# print(df2)

# Using the with statement
# with open("D:\\MSCITM\\5th-Python\\pyscript\\errorInfo.txt") as f:
#   print(f.read()) 
# f.close() 

# Read Only Parts of the File
# with open("D:\\MSCITM\\5th-Python\\pyscript\\RomeoAndJuliet.txt") as f:
# #   print(f.read(250)) 
#   print(f.read()) 
#   f.close() 

# Read Lines
# with open("D:\\MSCITM\\5th-Python\\pyscript\\RomeoAndJuliet.txt") as f:
#   print(f.readline()) 
#   print(f.readline()) 
#   print(f.readline()) 
#   f.close()
# Loop through the file line by line
with open("D:\\MSCITM\\5th-Python\\pyscript\\RomeoAndJuliet.txt") as f:
    for ln in f:
        print(ln)
