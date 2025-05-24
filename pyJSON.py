# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.

# Parse JSON - Convert from JSON to Python
# Convert from JSON to Python
# import json
# x =  '{ "name":"Gopal Nepal", "age":41, "city":"Kathmandu"}'
# parse x:
# y = json.loads(x) # method to convert to python from JSON
# print(y["name"]) 

# Convert from Python to JSON
# import json
# a Python object (dict):
# x = {
#   "name": "Gopal Nepal",
#   "age": 41,
#   "city": "Kathmandu"
# }
# convert into JSON:
# y = json.dumps(x)
# print(y)

# Convert Python objects into JSON strings, and print the values
# import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None)) 

# When you convert from Python to JSON, Python objects are converted into 
# the JSON (JavaScript) equivalent
# Python 	        JSON
# dict 	        Object
# list 	        Array
# tuple 	        Array
# str 	        String
# int 	        Number
# float 	        Number
# True 	        true
# False 	        false
# None 	        null

# Convert a Python object containing all the legal data types
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# print(json.dumps(x))

# Format the Result
# Use the indent parameter to define the numbers of indents
# print(json.dumps(x, indent=2))

# Use the separators parameter to change the default separator:
# print(json.dumps(x, indent=2, separators=(". ", " = ")))

# Order the Result
# Use the sort_keys parameter to specify if the result should be sorted or not
print(json.dumps(x, indent=2, sort_keys=True, separators=(". ", " = ")))




