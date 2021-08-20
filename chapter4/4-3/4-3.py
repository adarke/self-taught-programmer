""" 4-3 -- Parameters.

Write a function that takes three required parameters and two optional
parameters.
"""


def req_and_opt(x, y, z, a = 4, b = 5):
    """ Calculate sum of all of the arguments.

    Args:
        x: Required number to sum.
        y: Required number to sum.
        z: Required number to sum.
        a: Optional number to sum.
        b: Optional number to sum.

    Returns:
        The sum of the arguments.
    """
    return x + y + z + a + b


print(req_and_opt(1, 2, 3))
