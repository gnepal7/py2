# Python String Formatting

# F-Strings
# F-string allows you to format selected parts of a string
# create an f"string
# txt = f"The price is 49 dollars"
# print(txt)

# Placeholders and Modifiers
# Add a placeholder for the price variable
# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# Display the price with 2 decimals
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# You can also format a value directly without keeping it in a variable:
# Display the value 95 with 2 decimals
# txt = f"The price is {95:.2f} dollars"
# print(txt)

# Perform Operations in F-Strings
# txt = f"The price is {20 * 59} dollars"
# print(txt)

# You can perform math operations on variables:
# price = 59
# tax = 0.25
# txt = f"The price is {price + (price * tax)} dollars"
# print(txt)

# You can perform if...else statements inside the placeholders
# Return "Expensive" if the price is over 50, otherwise return "Cheap"
# price = 52
# txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
# print(txt)

# Execute Functions in F-Strings
# Use the string method upper()to convert a value into upper case letters
# fruit = "apples"
# txt = f"I love {fruit.upper()}"
# print(txt)

# Create a function that converts feet into meters
# def myconverter(x):
#   return x * 0.3048
# txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
# print(txt)

# More Modifiers
# There are several other modifiers that can be used to format values
# Use a comma as a thousand separator
# price = 59000
# txt = f"The price is {price:,} dollars"
# print(txt)

# String format()
# Before Python 3.6 we used the format() method to format strings.The format() 
# method can # still be used, but f-strings are faster and the preferred 
# way to format strings
# Add a placeholder where you want to display the price
# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))

# Multiple Values
# Add more placeholders
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# Index Numbers
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# Also, if you want to refer to the same value more than once, use the index number
# age = 36
# name = "John"
# txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name))

# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))


