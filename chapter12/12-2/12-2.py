""" 12-2 -- Circle Area.

Create a Circle class with a method called area that calculates and returns its 
area. Then create a Circle object, call area on it, and print the result. Use 
Python's pi function in the built-in math module. 
"""


import math

class Circle():
    def __init__(self, radius):
        """ Circle Initializer Method.

        Args:
            radius: Radius of circle.

        Returns:
            None.
        """
        self.radius = radius


    def area(self):
        """ Calculate Area Of Circle.
        
        Args:
            None.

        Returns:
            The area of the circle.
        """
        return math.pi * self.radius ** 2


circle = Circle(10)
print(circle.area())
