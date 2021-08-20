""" 14-1 -- Class Variable.

Add a square_list class variable to a class called Square so that every time you
create a new Square object, the new object gets added to the list.
"""


class Square():
    square_list = []

    def __init__(self, length):
        """ Square Initializer Method.
        
        Args:
            length: Length of square sides.
            
        Return:
            None.
        """
        self.length = length
        Square.square_list.append(self)


square_1 = Square(10)
square_2 = Square(5)

print(Square.square_list) 
