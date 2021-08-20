""" 14-2 -- Alternative Print.

Change the Square class so that when you print a Square object, a message prints
telling you the len of each of the four sides of the shape. For example, if you 
create a square with Square(29) and print it, Python should print 29 by 29 by 29
by 29.
"""


class Square():
    square_list = []

    def __init__(self, length):
        """ Square Initializer Method.
        
        Args:
            length: Length of square sides.
            
        Returns:
            None.
        """
        self.length = length
        Square.square_list.append(self)


    def __repr__(self):
        """ Square Printable Representation.

        Args:
            None.

        Returns:
            None.
        """
        return "{} by {} by {} by {}".format(self.length, self.length, self.length, self.length)


square = Square(10)

print(square)
