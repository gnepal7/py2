# Dictionaries are used to store data values in key:value pairs. # A dictionary 
# is a collection which is ordered*, changeable and do not allow duplicates
# firstDict = {
#     "Name" : "Gopal Nepal",
#     "Age" : 40,
#     "Profession": "Web Designer",
#     "Address" : "Mid Baneswor",
#     # Duplicates Not Allowed
#     "Address": "Anamnagar"
# }
# print(firstDict)
#length
# print(len(firstDict))
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and 
# earlier, dictionaries are unordered. -Duplicates Not Allowed

# Data Types
# The values in dictionary items can be of any data type
# thisdict =	{
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# } 
# print(type(thisdict))

# The dict() Constructor
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# Accessing Items
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)
# Get Keys
# x = thisdict.keys()
# print(x)
# Get Values
# y = thisdict.values()
# print(y)
# Get Items
# z = thisdict.items()
# print(z)
# Check if Key Exists
# if "brand" in thisdict:
#     print("Yes, it is")
# Change Values
# thisdict["year"] = 2025
# print(z)
# Update Dictionary
# thisdict["model"] = "Volvo"
# print(z)
# Adding Items
# thisdict["color"] = "green"
# print(z)
# Removing Items
# thisdict.pop("model")
# print(thisdict)
# The popitem() method removes the last inserted item
# thisdict.popitem()
# print(z)
# The del keyword removes the item with the specified key name:
# del thisdict["brand"]
# print(thisdict) 
# The clear() method empties the dictionary
# thisdict.clear()
# print(thisdict)
# The del keyword can also delete the dictionary completely

# Loop Through a Dictionary
# newThings = {
#     "book" : "New Habit",
#     "pencil" : "DOMS",
#     "copy" : "everest",
#     "ereasor" : "doms"
# }
# for b in newThings:
#     print(b)
# Print all values in the dictionary, one by one:
# for c in newThings:
#     print(newThings[c])
# You can also use the values() method to return values of a dictionary
# for d in newThings.values():
#     print(d)
# You can use the keys() method to return the keys of a dictionary
# for e in newThings.keys():
#     print(e)
# for x, y in newThings.items():
#     print(x, y)

# Copy a Dictionary
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)
# Another way to make a copy is to use the built-in function dict()
# thisdict2 =	{
#   "brand": "Volvo",
#   "model": "Yellow",
#   "year": 2025
# }
# mydict2 = dict(thisdict2)
# print(mydict2) 

# Nested Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 
print(myfamily["child2"]["name"]) 
# Loop Through Nested Dictionaries
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])

