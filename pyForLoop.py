# Python For Loops
# familyMember = ["Gopal", "Urmila", "Freshiya", "Yashika"]
# for c in familyMember:
#     print(c)

# Looping Through a String
# for n in "Shobhit Nepal":
#     print(n)

# The break Statement
# fruits = ["Apple", "Banana", "Cherry", "DragonFruit", "Litchee" ]
# for y in fruits:
#     print(y)
#     if y == "Cherry":
#         break
# break between
# for t in fruits:
#     if t == "Banana":
#         break
#     continue
# print(t)
# The continue Statement
# for x in fruits:
#   if x == "Banana":
#     continue
#   print(x)

# The range() Function
# for b in range(7):
#     print(f"{b}, This is range line {b}")
# Using the start parameter
# for c in range(3, 9):
#     print(f"{c}. is in range line {c}")
# The range() function defaults to increment the sequence by 1, however it is 
# possible to specify the increment value by adding a third parameter: range(2, 30, 3)
# for x in range(5, 30, 5):
#   print(f"{x}, is added '5' in ranga between '30' of {x}")

# Else in For Loop
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!") 
# Note: The else block will NOT be executed if the loop is stopped by a break statement
# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!") 

# Nested Loops
adj = ["red", "big", "tasty", "pineapple"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) 


