# Lists, tuples, dictionaries, and sets have a iter() method which 
# is used to get an iterator

# Return an iterator from a tuple, and print each value
# tupleOne = ("Pen", "Pencil", "Book", "Copy", "Stapler")
# itterOne = iter(tupleOne)
# print(next(itterOne))
# print(next(itterOne))
# print(next(itterOne))
# print(itterOne)

# Strings are also iterable objects, containing a sequence of characters
# strOne = "Shobhit"
# itOne = iter(strOne)
# print(next(itOne))
# print(next(itOne))
# print(next(itOne))
# print(next(itOne))
# print(next(itOne))
# print(next(itOne))
# print(next(itOne))

# Looping Through an Iterator
# family = ("Gopal", "Urmila", "Freshiya", "Yashika")
# for m in family:
#     print(f"{m} Nepal")

# Iterate the characters of a string
# name = "Gopal"
# for letter in name:
#     print(letter)

# The for loop actually creates an iterator object and 
# executes the next() method for each loop

# Create an Iterator
# The __iter__() method acts similar, you can do operations (initializing etc.), 
# but must always return the iterator object itself.The __next__() method also 
# allows you to do operations, and must return the next item in the sequence

# Create an iterator that returns numbers, starting with 1, and each sequence will 
# increase by one (returning 1,2,3,4,5 etc.)
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter)) 

# StopIteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)

