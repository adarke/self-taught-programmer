""" 4-4 -- Two Functions. 

Write a program with two functions. The first function should take an integer
as a parameter and return the result of the integer divided by 2. The second
function should take an integer as a parameter and return the result of the
integer multiplied by 4. Call the first function, save the result as a
variable, and pass it as a parameter to the second function.
"""


def half(x):
    """ Divide the argument by 2 and return the result.

    Args:
        x: The integer to divide by 2.

    Returns: 
        The value of x divided by 2.
    """
    return x / 2


def quadrupal(x):
    """ Multiply the argument by 4 and return the result.

    Args:
        x: The integer to multiply by 4.

    Returns:
        The value of x multiplied by 4.
    """
    return x * 4


x = half(10)
print(quadrupal(x))
