#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(a,b):
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    x = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return x
