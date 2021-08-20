""" 4-5 -- String to Float.

Write a function that converts a string to a float and returns the result. Use
exception handling to catch the exception that could occur.
"""


def string_to_float(x):
    """ Convert string to float and print the result.

    Args:
        x: String to convert to a float.

    Returns:
        Result of conversion from string to float.

    Raises:
        ValueError: Conversion to float failed.
    """
    try:
        return float(x)
    except ValueError:
        print("Please enter valid input")


result = string_to_float("10.5")
print(result)
