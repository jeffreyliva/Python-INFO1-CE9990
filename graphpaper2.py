"""

graphpaper2.py

Graph paper that doesn't leave the right and bottom edges open

"""

"""
graphpaper.py
"""

import sys

try:
    rows = int(input("How many rows of boxes?"))
    columns = int(input("How many columns of boxes?"))
    rspace = int(input("How many rows of space for each box"))
    cspace = int(input("How amny columns of space for each box"))

except ValueError:
        print("Please input an integer.")



w = 0
while w < rows:
    x = 0
    while x < columns:
        print("+", cspace * "-", sep = "", end = "")
        x += 1
    print()
    y = 0
    while y < rspace:
        z = 0
        while z < columns:
            print("|", cspace * " ", sep = "", end = "")
            z += 1

        print("|")
        y += 1
    w += 1
a = 0
while a < columns:
    print("+", cspace * "-", sep = "", end = "")
    a += 1
print("+")   

sys.exit(0)
