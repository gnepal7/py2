# Consider a module to be the same as a code library
# import myModule
# myModule.greeting("Shobhit Nepal")

# myModule.location(" Mid Baneswor")

# Note: When using a function from a module, use the syntax: module_name.function_name
# name = myModule.person1["name"]
# age = myModule.person1["age"]
# country = myModule.person1["country"]
# print(name)
# print(age)
# print(country)

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword
# Create an alias for mymodule called mx

# import myModule as mm
# name = mm.person2["Name"]
# age = mm.person2["Age"]
# country = mm.person2["Country"]
# district = mm.person2["District"]
# print(district)

# Built-in Modules
# Import and use the platform module
# import platform
# x = platform.system()
# print(x) 

# Using the dir() Function
# List all the defined names belonging to the platform module
# import platform
# x = dir(platform)
# print(x) 
# Note: The dir() function can be used on all modules, also the ones you 
# create yourself.

# Import only the person1 dictionary from the module
from myModule import person2, location
print(location("Anamnager \n Kathmandu \n"))
print (person2["Country"])
