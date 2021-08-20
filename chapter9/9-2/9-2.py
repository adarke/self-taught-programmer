""" 9-2 -- Write To File.

Write a program that asks a user a question, and saves their answer to a file.
"""


import os, sys

path = os.path.join(sys.path[0], "answer.txt")
answer = input("What is your name? ")

with open(path, "w") as f:
    f.write(answer)
