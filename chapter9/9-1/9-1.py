""" 9-1 -- Print File.

Find a file on your computer and print its contents using Python.
"""


import os, sys

path = os.path.join(sys.path[0], "test.txt")

with open(path, "r") as f:
    print(f.read())
