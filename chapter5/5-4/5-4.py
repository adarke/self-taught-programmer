""" 5-4 -- Ask A Question.

Write a program that lets the user ask your height, favourite color, or 
favourite author, and returns the result from the dictionary that you created in
the previous challenge. 
"""


me = {
    "height": 180,
    "age": 25,
    "favourite colour": "green",
    "favourite author": "Haruki Murakami",
    }

question = input("What would you like to know about me? ")

if question in me:
    print(me[question])
else:
    print("Sorry, I don't know that.")
