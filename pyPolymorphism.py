# Function Polymorphism
# An example of a Python function that can be used on different objects 
# is the len() function

# For strings len() returns the number of characters
# x = "Hello World!"
# print(len(x)) 

# For tuples len() returns the number of items in the tuple
# mytuple = ("apple", "banana", "cherry")
# print(len(mytuple)) 

# For dictionaries len() returns the number of key/value pairs in the dictionary
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(len(thisdict)) 

# Different classes with the same method
class Student:
    def __init__(self, level, grade):
        self.level = level
        self.grade = grade

    def levelInfo(self):
        print("Primary level: 1 to 5 class")

class SecondaryStudent:
    def __init__(self, level, grade):
        self.level = level
        self.grade = grade

    def levelInfo(self):
        print("It is from grade 6 to 10")

class PlusTwoStudent:
    def __init__(self, level, grade):
        self.level = level
        self.grade = grade

    def levelInfo(self):
        print("It is grade 11 and 12")

class Bachelor:
    def __init__(self, level, grade):
        self.level = level
        self.grade = grade

    def levelInfo(self):
        print("It is from grade 13 to 15")

class Master:
    def __init__(self, level, grade):
        self.level = level
        self.grade = grade

    def levelInfo(self):
        print("It is assumed as class 16 and 17") 

# Create instances
prime1 = Student("Primary", "Classes from one - five")
sec2 = SecondaryStudent("Secondary", "Classes from six - ten")
plus2 = PlusTwoStudent("PlusTwo", "Classes eleven and twelve")
bachelor = Bachelor("Bachelor Level", "Classes from thirteen - fifteen")
master = Master("Master Level", "Classes sixteen and seventeen")

# Iterate through instances and print information
for s in (prime1, sec2, plus2, bachelor, master):
    print(s.level + "\n")
    print(s.grade)
    s.levelInfo()

# Inheritance Class Polymorphism
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle
# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       
# boat1 = Boat("Ibiza", "Touring 20") 
# plane1 = Plane("Boeing", "747")     

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()




