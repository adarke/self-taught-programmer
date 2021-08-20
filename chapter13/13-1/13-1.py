""" 13-1 -- Rectangle And Square Perimeters.

Create Rectangle and Square classes with a method called calculate_perimeter 
that calculates the perimeter of the shapes they represent. Create Rectangle and
Square objects and call the method on both of them. 
"""


class Square():
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


class Rectangle():
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
rect = Rectangle(2, 4)

print(square.calculate_perimeter())
print(rect.calculate_perimeter())
