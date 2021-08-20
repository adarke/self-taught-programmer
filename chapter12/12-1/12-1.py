""" 12-1 -- Class Attributes.

Define a class called Apple with four instance variables that represent four 
attributes of an apple.
"""


class Apple():
    def __init__(self, family, colour, size, price):
        """ Apple Initializer Method.
    
        Args:
            family: Family apple belongs to.
            colour: Colour of apple.
            size: Size of apple.
            price: Price of apple.

        Returns:
            None.
        """
        self.family = family
        self.colour = colour
        self.size = size
        self.price = price
