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

x = hypotenuse(3,4,True)

d = 0

def hypotenuse(a,b,c):
    if c == True:
        d2 = a**2 + b**2
        d = math.sqrt(d2)
        return d
    elif c == False:
        if a > b:
            d2 = a**2 - b**2
            d = math.sqrt(d2)
            return d
        elif b > a:
            d2 = b**2 - a**2
            d = math.sqrt(d2)
            return d

print(x)