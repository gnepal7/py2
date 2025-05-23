# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods

# To create a class, use the keyword class
# class MyClass:
#     word = "Hello Nepal"
# print(MyClass)
# Create an object named p1, and print the value of x
# p1 = MyClass
# print(p1.word)

# The __init__() Function
# Create a class named Person, use the __init__() function to 
# assign values for name and age
# class AboutMe:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
# A1 = AboutMe("Gopal Nepal", 41)
# print(A1.name)
# print(A1.age)

# Note: The __init__() function is called automatically every time the class 
# is being used to create a new object

# The __str__() function controls what should be returned when the class object 
# is represented as a string. # If the __str__() function is not set, the string 
# representation of the object is returned
# The string representation of an object WITH the __str__() function
# class ManOne:
#   def __init__(self, name, age, profession):
#     self.name = name
#     self.age = age
#     self.profession = profession

#   def __str__(self):
#     return f"{self.name} {self.age} {self.profession}"

# p1 = ManOne("Urmila Shrestha", 41, "HouseWife")
# print(p1) 

# Object Methods
# Insert a function that prints a greeting, and execute it on the p1 object
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)
#     print(f"I am {self.age} years old.")

# p1 = Person("Gopal Nepal", 41)
# p1.myfunc() 

# The self Parameter
# It does not have to be named self, you can call it whatever you like, 
# but it has to be the first parameter of any function in the class
# class PersonThree:
#   def __init__(myownyobject, name, age):
#     myownyobject.name = name
#     myownyobject.age = age
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#     print(f"My age is {abc.age} years old")

# p1 = PersonThree("Freshiya Nepal", 16)
# p1.myfunc() 
# Modify Object Properties
# p1.age = 15
# p1.myfunc() 
# Delete Object Properties
# del p1.age
# p1.myfunc()
# You can delete objects by using the del keyword:
# del p1

class PersonFour:
  def __init__(myNewInfo, name, profession, address, age):
    myNewInfo.name = name
    myNewInfo.profession = profession
    myNewInfo.address = address
    myNewInfo.age = age

  def newInfo(show):
    print("My name if" + show.name) 
    print("I am" + show.profession) 
    print("I live in" + show.address)
    print(f"I am {show.age} years old")

p4 = PersonFour("Gopal Nepal", "Web Designer/Developer", "Mid Baneswor", "41")
p4.newInfo()



