
    # Equals: a == b
    # Not Equals: a != b
    # Less than: a < b
    # Less than or equal to: a <= b
    # Greater than: a > b
    # Greater than or equal to: a >= b
# a = 50
# b = 69
# if a < b:
#     print("Yes, is less than")
# elif a == b:
#     print("They are equal")
# else:
#     print("No, a is greater than")
# Short Hand If
# if a > b: print("a is greater than b")
# Short Hand If ... Else
# a = 2
# b = 330
# print("A") if a > b else print("B") 

# This technique is known as Ternary Operators, or Conditional Expressions.
# 3 condition ternary
# a = 330
# b = 331
# print("A") if a > b else print("=") if a == b else print("B") 

# The and keyword is a logical operator, and is used to combine conditional statements
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

# The or keyword is a logical operator, and is used to combine conditional statements
# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement
# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")

# You can have if statements inside if statements, this is called nested if statements
# x = 41
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.") 

# if statements cannot be empty, but if you for some reason have an if statement 
# with no content, put in the pass statement to avoid getting an error
a = 33
b = 200
if b > a:
  pass
