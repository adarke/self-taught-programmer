""" 7-4 -- Infinite Loop.

Write a program with an infinite loop (with the option to type q to quit) and a 
list of numbers. Each time through the loop ask the user to guess a number on 
the list and tell them whether or not they guessed correctly.
"""


numbers = [1, 2, 3, 4, 5]

while True:
    selection = input("Guess a number (q to quit): ")
    if selection == "q":
        break
    try:
        selection = int(selection)
    except ValueError:
        print("Please input a number or q to quit.")
    else:
        if selection in numbers:
            print("number is in list.")
        else:
            print("number is not in list.")
