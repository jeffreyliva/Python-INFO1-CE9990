"""

forif.py
get the first 10 numbers of the fibonacci sequence

"""

import sys

def fibonacci(n):
    x = 0
    y = 1
    for i in range(0, n):
        current = x
        x = y
        y = current + y
    return x


for z in range(0, 10):
    print(fibonacci(z))

sys.exit(0)
