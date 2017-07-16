"""


control.py


"""


import sys


print(
"""

What New York City sports team are you watching?

""")

stadium = input("What stadium are you at? ")

if stadium == "yankee stadium":
    print("You are watching the New York Yankees.")

elif stadium == "citi field":
    print("You are watching the New York Mets. ")

elif stadium == "madison square garden":
    print("You are watching the New York Rangers.")

elif stadium == "met life":
    print("You are watching the New York Giants. ")
    
sys.exit(0)
