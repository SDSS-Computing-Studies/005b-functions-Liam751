#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(mylist):
    length = len(mylist)
    mylist.sort()
    largest = mylist[length - 1]
    return largest

x = largest([4,6,3,9,24,12,2])
print(x)