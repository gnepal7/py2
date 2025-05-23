# Python Inheritance
# Parent class is the class being inherited from, also called base class
# Child class is the class that inherits from another class, also called derived class

# Create a class named Person, with firstname and 
# lastname properties, and a printname method
class Person:
  def __init__(infoBox, fname, lname):
    infoBox.firstname = fname
    infoBox.lastname = lname
  def printname(infoBox):
    print(infoBox.firstname, infoBox.lastname)
#Use the Person class to create an object, and then execute the printname method:
# x = Person("Gopal", "Nepal")
# x.printname() 

# Create a Child Class
# class Student(Person):
#   pass
# s = Student("Freshiya", "Nepal")
# s.printname() 
# Add the __init__() Function
# class Student(Person):
#   def __init__(self, fname, lname):
#     pass
# When you add the __init__() function, the child class will no longer 
# inherit the parent's __init__() function. 
# Note: The child's __init__() # function overrides the inheritance of the 
# parent's __init__() function.To keep the inheritance of the 
# parent's __init__() function, add a call to the 
# parent's __init__() function

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname) 
# y = Student("Yashika", "Nepal")
# y.printname()

# Use the super() Function
# Python also has a super() function that will make the child class inherit 
# all the methods and properties from its parent
# class SeeStudent(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname) 
# p = SeeStudent("Prajwal", "Aacharya")
# p.printname()
# By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent.

# Add a property called graduationyear to the Student class

# class GraduatedStudent(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
# gs = GraduatedStudent("Gopal", "Nepal", 2017)
# gs.printname()
# print(gs.graduationyear)

# Add Methods
class MethodAddedStudent(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome!", self.firstname, self.lastname, "you are the student of", 
          self.graduationyear, "aren't you?") 
mas = MethodAddedStudent("Urmila", "Shrestha", 2009)
# mas.printname()
mas.welcome()