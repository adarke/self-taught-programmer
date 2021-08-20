""" 21-2.py -- Reverse List.

Use a stack to create a new list with the items in the following list reversed: 
[1, 2, 3, 4, 5].
"""


class Stack:
    def __init__(self):
        """ Stack Initializer Method.
        
        Args:
            None.
            
        Returns:
            None.
        """
        self.items = []


    def is_empty(self):
        """ Check If Stack Is Empty.
        
        Args:
            None.

        Returns:
            True if stack is empty, False if stack is not empty.
        """
        return self.items == []


    def push(self, item):
        """ Push Item Onto Stack.
        
        Args:
            item: Item to push onto stack.
            
        Returns:
            None.
        """
        self.items.append(item)


    def pop(self):
        """ Pop Item From Stack.
        
        Args: 
            None.
            
        Returns:
            Item that has been popped from stack.
        """
        return self.items.pop()


    def peek(self):
        """ Check Next Item On Stack.
        
        Args:
            None.
            
        Returns:
            Next item on stack.
        """
        next = len(self.items)-1
        return self.items[next]


    def size(self):
        """ Size Of Stack.
        
        Args:
            None.
            
        Returns:
            Number of items on stack.
        """
        return len(self.items)


stack = Stack()
original = [1, 2, 3, 4, 5]
reverse = []

for item in original:
    stack.push(item)
for i in range(stack.size()):
    reverse.append(stack.pop())

print(reverse)
