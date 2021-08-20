""" 14-3 -- Object Comparison.

Write a function that takes two objects as parameters and returns True if they 
are the same object, and False if not.
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


def same_test(a, b):
    """ Compare Two Objects.
    
    Check to see if objects provided are the same object.
    
    Args:
        a: First obejct to compare.
        b: Second object to compare.
        
    Return:
        True if objects are the same, False if they are different.
    """
    return s1 is s2


s1 = Square(10)
s2 = Square(10)

print(same_test(s1, s2))
