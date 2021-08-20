""" 13-2 -- Change Square Size.

Define a method in your Square class called change_size that allows you to pass
in a number that increases or decreases (if the number is negative) each side of
a Square object by that number.
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


    def change_size(self, new_length):
        """ Change Length Of Square Sides.

        Args:
            new_length: New length of each side of the square.

        Returns:
            None.
        """
        self.length += new_length


square = Square(10)
square.change_size(5)

print(square.calculate_perimeter())
print(square.calculate_perimeter())
