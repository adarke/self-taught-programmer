""" 12-3 -- Triangle Area.

Create a Triangle class with a method called area that calculates and returns 
its area. Then create a Triangle object, called area on it, and print the 
result.
"""


class Triangle():
    def __init__(self, base, height):
        """ Triangle Initializer Method.
        
        Args:
            base: Length of base of triangle.
            height: Height of triangle.
            
        Returns:
            None.
        """
        self.base = base
        self.height = height


    def area(self):
        """ Calculate Area Of Triangle.
        
        Args:
            None.
            
        Returns:
            The area of the triangle.
        """
        return self.base * self.height / 2


triangle = Triangle(10, 5)
print(triangle.area())
