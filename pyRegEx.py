# Python RegEx
# A RegEx, or Regular Expression, is a sequence of characters 
# that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx in Python
# When you have imported the re module, you can start using regular expressions
# Search the string to see if it starts with "The" and ends with "Spain"
# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt) 
# print(x)

# The re module offers a set of functions that allows us to search a string for a match
# Function 	Description
# findall 	Returns a list containing all matches
# search 	    Returns a Match object if there is a match anywhere in the string
# split 	    Returns a list where the string has been split at each match
# sub 	    Replaces one or many matches with a string

# The findall() Function
# import re
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x) 
# If no matches are found, an empty list is returned:
# x = re.findall("Portugal", txt)
# print(x) 

# The search() Function
# import re
# txt = "In Spain, there is raining"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start()) 

# The split() Function
# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x) 

# Split the string only at the first occurrence
# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x) 

# The sub() Function
# import re
# txt = "The rain in Spain"
# x = re.sub("\s", "N", txt)
# print(x) 

# You can control the number of replacements by specifying the count parameter
# import re
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x) 

# Print the string passed into the function:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) 

# The regular expression looks for any words that starts with an upper case "S"
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) 
