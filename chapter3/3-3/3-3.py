""" 3-3 -- Conditional Print.

Write a program that prints a message if a variable is less than or equal to 
10, another message if the variable is greater than 10 but less than or equal 
to 25, and another message if the variable is greater than 25.
"""


value = 30

if value <= 10:
    print("value is less than or equal to 10")
elif value <= 25:
    print("value is greater than 10, and less than or equal to 25")
else:
    print("value is greater than 25")
