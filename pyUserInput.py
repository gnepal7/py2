# Python User Input
# Ask for user input:
# print("Enter your name:")
# name = input()
# print(f"Hello {name}")

# Python stops executing when it comes to the input() function, 
# and continues when the user has given some input

# using prompt
# Add a message in front of the user input
# name = input("Enter your name:")
# print(f"Hello {name}")

# Multiple Inputs
# name = input("Enter your name:")
# print(f"Hello {name}")
# fav1 = input("What is your favorite animal:")
# fav2 = input("What is your favorite color:")
# fav3 = input("What is your favorite number:")
# print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# Input Number
# import math
# x = input("Enter a number:")
#find the square root of the number:
# y = math.sqrt(float(x))
# print(f"The square root of {x} is {y}")

# Validate Input
# Keep asking until you get a number
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x)
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!") 





