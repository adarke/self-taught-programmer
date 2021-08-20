""" 13-3 -- Class Inheritance.

Create a class called Shape. Define a method in it called what_am_i that prints 
"I am a shape" when called. Change your Square and Rectangle classes from the 
previous challenges to inherit from Shape, create Square and Rectangle objects, 
and call the new method on both of them.
"""


class Shape():
    def what_am_i(self):
        """ Print I Am A Shape.
        
        Args:
            None.

        Returns:
            None.
        """
        print("I am a shape")


class Square(Shape):
    def __init__(self, length):
        """ Square Initializer Method.
        
        Args:
            length: Length of square sides.
            
        Returns:
            None.
        """
        self.length = length


    def calculate_perimeter(self):
        """ Calculate Perimeter Of Square.
        
        Args:
            None.
            
        Returns:
            The perimeter of the square.
        """
        return self.length * 4


    def change_size(self, new_length):
        """ Change Length Of Square Sides.

        Args:
            new_length: New length of each side of the square.

        Returns:
            None.
        """
        self.length += new_length


class Rectangle(Shape):
    def __init__(self, width, height):
        """ Rectangle Initializer Method.
        
        Args:
            width: Width of rectangle.
            height: Height of rectangle.
            
        Returns:
            None.
        """
        self.width = width
        self.height = height


    def calculate_perimeter(self):
        """ Calculate Perimeter Of Rectangle.
        
        Args:
            None.
            
        Returns:
            The perimeter of the rectangle.
        """
        return (self.width * 2) + (self.height * 2)


square = Square(10)
rectangle = Rectangle(2, 4)

square.what_am_i()
rectangle.what_am_i()
