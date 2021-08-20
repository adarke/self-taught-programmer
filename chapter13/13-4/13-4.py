""" 13-4 -- Composition

Create a class called Horse and a class called Rider. Use composition to model a
horse that has a rider.
"""


class Rider():
    def __init__(self, name):
        """ Rider Initializer Method.
        
        Args: 
            name: Name of rider.
            
        Returns:
            None.
        """
        self.name = name
    

class Horse():
    def __init__(self, name, rider):
        """ Horse Initializer Method.
        
        Args:
            name: Name of horse.
            rider: Name of rider.
        
        Returns:
            None.
        """
        self.name = name
        self.rider = rider


rider = Rider("John")
horse = Horse("Silver", rider)

print(horse.name)
print(horse.rider.name)
