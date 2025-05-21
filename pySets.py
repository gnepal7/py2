# Sets are written with curly brackets.
# thisset = {"apple", "banana", "cherry"}
# print(thisset) 

#  Set items are unchangable and Unordered
# Duplicates Not Allowed
# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# True and 1 is considered the same value:
# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# False and 0 is considered the same value
# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)

# Get the Length of a Set
# thisset = {"apple", "banana", "cherry"}
# print(len(thisset)) 

# Set Items - Data Types
# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False} 
# print(set3)
# print(type(set3))

# Constructor
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset) 

# access set Items
neighbourSet = {"brother", "sister", "uncle", "aunty", "causion"}
# for n in neighbourSet:
#     print(n)
# if "sister2" in neighbourSet:
#     print("Yes, it is in the set")
# elif "unclee" in neighbourSet:
#     print("Yes, it is too in this set")
# elif "banana" not in neighbourSet:
#     print("No, It is not here")
# else:
#     print("Add more items in this set")
# neighbourSet.add("niece")
# for d in neighbourSet:
#     print(d)

# add set items
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset) 

# Add Any Iterable
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset) 

# Remove Item
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset) 

# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset) 

# pop also remove items from set randomly
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset) 

# The clear() method empties the set
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset) 

# The del keyword will delete the set completely
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset) 

# Loop Sets
# for c in neighbourSet:
#     print(c)

# Join Sets, Union
# Join set1 and set2 into a new set
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3) 
# Use | to join two sets:
# set3 = set1 | set2
# print(set3) 

# Join Multiple Sets
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)
# print(myset) 
# Use | to join two sets:
# myset = set1 | set2 | set3 |set4
# print(myset) 

# Join a Set and a Tuple
# x = {"a", "b", "c"}
# y = (1, 2, 3)
# z = x.union(y)
# print(z) 

# Update
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1) 
# Note: Both union() and update() will exclude any duplicate items

# Intersection
# Join set1 and set2, but keep only the duplicates:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3) 
# Use & to join two sets
# set3 = set1 & set2
# print(set3)

# The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1) 

# Join sets that contains the values True, False, 1, and 0, and see 
# what is considered as duplicates
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)

# Difference
# Keep all items from set1 that are not in set2
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3) 
# Use - to join two sets
# set3 = set1 - set2
# print(set3)
# Use the difference_update() method to keep the items 
# that are not present in both sets:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1) 

# Symmetric Differences: It symmetric_difference() method will keep only the elements 
# that are NOT present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3) 
# Use ^ to join two sets
set3 = set1 ^ set2
print(set3) 
# Use the symmetric_difference_update() method to keep the 
# items that are not present in both sets
set1.symmetric_difference_update(set2)
print(set1)