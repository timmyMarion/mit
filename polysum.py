# imports the function tan and pi from the math module
from math import tan, pi


def polysum(n, s):
    """ This function adds the area of a polygon to the length of a polygon returning
    the value with an accuracy of 4 places to the right of the decimal point.

    The function accepts 2 parameters.
    n is the number of sides the polygon has.
    s is the length of each side
    """

    # calculate the area
    area = (.25 * n * (s**2)) / tan(pi/n)

    # calculate the perimeter
    perimeter = (n * s) ** 2

    # return the value of area + perimeter, rounded to 4 places to the right of the decimal point
    return round(area + perimeter, 4)
