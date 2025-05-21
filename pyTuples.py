# Python Tuples, tuples are written in ()
# students = ("Gopal", "Urmila", "Freshiya", "Yashika", "Niroj", "Bimal")
# print(students)

# tuple items are unchalgable and Allow Duplicates
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)
# length
# print(len(thistuple))

# Create Tuple With One Item
# thistuple = ("apple",) #must be seperated by comma
# print(type(thistuple))

# Tuple Items - Data Types
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# type
# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# The tuple() Constructor
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# Access Tuple Items
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])
# Negative Indexing
# print(thistuple[-1])

# Range of Indexes
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])
# Range of Negative Indexes
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# Check if Item Exists
# family = ("Shobhit", "Urmila", "Freshiya", "Yashika")
# if "Yashika" in family:
#     print("Yes, it is")

# Update Tuples
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x) 

# Add Items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# Add tuple to a tuple
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

# Remove Items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

# delete the tuple
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists 

# Unpacking a Tuple
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# Using Asterisk*
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry", "orange")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)

# Loop Through a Tuple
relationSet = ("Husband", "Wife", "Brother", "Sister", "Mother", "Father", "Son")
# for r in relationSet:
#     print(r)
# Loop Through the Index Numbers
# for i in range(len(relationSet)):
#     print(relationSet[i])
# Using a While Loop
# c = 0
# while c < len(relationSet):
#     print(relationSet[c])
#     c = c + 1

# Join Two Tuples
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3) 

# Multiply Tuples
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 3
# print(mytuple) 

