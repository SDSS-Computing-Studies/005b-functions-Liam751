#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math

def hypotenuse(a,b,c):
    if c == True:
        d = a**2 + b**2
        d = math.sqrt(d)
        return d
    elif c == False:
        if a > b:
            d = a**2 - b**2
            d = math.sqrt(d)
            return d
        elif b > a:
            d = b**2 - a**2
            d = math.sqrt(d)
            return d

