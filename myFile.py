names = ["Gopal", "Shobhit", "Ram", "Krishna", "Hari", "Sharan", "Gopi"]
# print(names[1])

# Negative Indexing
# print(names[-1])

# Range of Indexes
# print(names[2:6])

# include/exclude
# print(names[:3])
# print(names[2:])
# print(names[-4:-1])

# Check if Item Exists
# if "Gopal" in names:
#     print("Yes, it is in list")

# fruits = ["apple", "banana", "chhery", "dragonFruit", "evacodo", "jackFruit", "kiwi"]
# Change Item Value
# fruits[0] = "guava"
# print(fruits)
# Change a Range of Item Values
# fruits[0:2] = ["mango", "litchee"]
# print(fruits)
# Insert Items
# fruits.insert(7, "straberry")
# print(fruits)

# Add List Items
# things = ["pen", "copy", "stappler", "pin", "pencil"]
# things.append("looseSheet")
# print(things)

# Extend List
# things2 = ["colorBox", "marker", "book"]
# things.extend(things2)
# print(things)
# things2.extend(things)
# print(things2)

# Add Any Iterable
# thingsTuple = ("things1", "things2", "things3")
# things2.extend(thingsTuple)
# print(things2)

# Remove Specified Item
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# Remove Specified Index, last 
# thislist.pop()
# print(thislist)

# Remove the first item
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# clear the list
# thislist.clear()
# print(thislist)

# Loop Through a List
# thislist = ["apple", "banana", "cherry", "jackFruit"]
# for x in thislist:
#   print(x)
# Loop Through the Index Numbers
# for i in range(len(thislist)):
#   print(thislist[i])

# Using a While Loop
# thislist = ["Kiwi", "Cherry", "Pineapple", "Dragon"]
# i = 1
# while i < len(thislist):
#     print (thislist[i])
#     i = i+1

# Looping Using List Comprehension
# things = ["pen", "copy", "stappler", "pin", "pencil"]
# [print(x) for x in things] 

# List Comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for z in fruits:
#     if "o" in z:
#         newlist.append(z)
# print(newlist)

# newlist = [x for x in fruits if "a" in x]
# print(newlist) 
# if not in list
# newlist = [x for x in fruits if x != "apple"] 
# print(newlist)
# in range
# numberList = [x for x in range(10)] 
# print(numberList)
# in range, less than
# decList = [x for x in range(10) if x < 7] 
# print(decList)
# expression changing
# newlist = [x.upper() for x in fruits] 
# print(newlist)
# replace all value by new 
# newlist = ['hello' for x in fruits] 
# print(newlist)

# Sort Lists
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# numerically sort
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)
# Sort Descending
# thislist.sort(reverse = True)
# print(thislist)
# Customize Sort Function
# def myfunc(n):
#   return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)
# Case Insensitive Sort
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)
# sort with lower letter
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)
# Reverse Order
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# Copy Lists
# thislist = ["apple", "banana", "cherry"]
# mylist = ["guava", "cocumber", "radish"]
# newlist  = (thislist + mylist)
# print(newlist)

# Use the slice Operator
# thislist = ["apple", "banana", "cherry", "carrot"]
# mylist = thislist[:]
# print(mylist)

# Join Lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3) 

# another way to joining lists
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1) 

# joining bt extending method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) 



