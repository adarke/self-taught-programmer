""" 12-4 -- Hexagon Perimeter.

Make a Hexagon class with a method called calculate_perimeter that calculates 
and returns its perimeter. Then create a Hexagon object, call 
calculate_perimeter on it, and print the result.
"""


class Hexagon():
    def __init__(self, one, two, three, four, five, six):
        """ Hexagon Initializer Method.
        
        Args:
            one: Length of side one.
            two: Length of side two.
            three: Length of side three.
            four: Length of side four.
            five: Length of side five.
            six: Length of side six.
            
        Returns:
            None.
        """
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six


    def calculate_perimeter(self):
        """ Calculate Perimeter Of Hexagon.
        
        Args:
            None.
        
        Returns:
            The perimeter of the hexagon.
        """
        return self.one + self.two + self.three + self.four + self.five + self.six


hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())
