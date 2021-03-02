#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance( [x1,y1] , [x2,y2] ):
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return a

x = distance( (2,4) , (6,3))
print(x)