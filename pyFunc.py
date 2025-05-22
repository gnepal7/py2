# In Python a function is defined using the def keyword
# def my_function():
#   print("Hello from a function")
# my_function()

# Information can be passed into functions as arguments
# def my_function(fname):
#   print(fname + " Refsnes")
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus") 
# Arguments are often shortened to args in Python documentations

# This function expects 2 arguments, and gets 2 arguments
# def my_function(fname, lname):
#   print(fname + " " + lname)
# my_function("Emil", "Refsnes") 

# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name
# def my_function(*kids):
#   print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus") 

# Keyword Arguments, You can also send arguments with the key = value syntax. This 
# way the order of the arguments does not matter
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

# Arbitrary Keyword Arguments, **kwargs
# If the number of keyword arguments is unknown, add a double ** before the 
# parameter name
# def my_function(**kid):
#   print(f"His name is {kid['fname']} {kid['lname']} ")
# my_function(fname = "Tobias", lname = "Refsnes") 
# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations

# Default Parameter Value
# def my_function(country = "Norway"):
#   print("I am from " + country)
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil") 
# print(my_function())

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), 
# and it will be treated as the same data type inside the function
# def family_func(members):
#   for m in members:
#     print(m)
# family_members = ["Gopal", "Urmila", "Freshiya", "Yashika"]
# family_func(family_members)

# Return Values
# To let a function return a value, use the return statement
# def my_function(x, y):
#   return 9 * x + y
# print(my_function(3, 2))
# print(my_function(5, 4))
# print(my_function(9, 3)) 

# The pass Statement
def myfunction():
  pass

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or 
# ONLY keyword arguments. # To specify that a function can have only 
# positional arguments, add , / after the arguments
# def my_function(x, /):
#   print(x)
# my_function(3) 

# Without the , / you are actually allowed to use keyword arguments 
# even if the function expects positional arguments:
# def my_function(x):
#   print(x)
# my_function(x = 3) 

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments
# def my_function(*, x):
#   print(x)
# my_function(x = 7) 

# Without the *, you are allowed to use positional arguments even 
# if the function expects keyword arguments:
# def my_function(x):
#   print(x)
# my_function(3) 

# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.Any argument before the / , 
# are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8) 

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
#In this example, tri_recursion() is a function that we have defined to 
# call itself ("recurse"). We use the k variable as the data, which 
# decrements (-1) every time we recurse. The recursion ends when the 
# condition is not greater than 0 (i.e. when it is 0)
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results:")
tri_recursion(6)

