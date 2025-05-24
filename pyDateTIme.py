# Import the datetime module and display the current date
import datetime
x = datetime.datetime.now()
# print(x) 

# Return the year and name of weekday:
print(x.year)
print(x.strftime("%a")) #day name in 3 letter
print(x.strftime("%A")) # day name in full

# Creating Date Objects
y = datetime.datetime(2025, 5, 24)
print(y) 

# The strftime() Method
# Display the name of the month
print(x.strftime("%B"))
print(x.strftime("%b"))

print(x.strftime("%A %B %Y, %H: %M:%S:%f%p"))



