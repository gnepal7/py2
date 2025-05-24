# Python File Write
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# with open("demofile.txt", "a") as f:
#   f.write("\n Now the file has more content!")
# #open and read the file after the appending:
# with open("demofile.txt") as f:
#   print(f.read()) 

# Overwrite Existing Content
# with open("demofile.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")
# #open and read the file after the overwriting:
# with open("demofile.txt") as f:
#   print(f.read()) 

# Create a New File
# To create a new file in Python, use the open() method, with one of the 
# following parameters:
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists

f = open("myfile.txt", "a")
f.write("These texts are written in the file from another file. It is added sentence.")