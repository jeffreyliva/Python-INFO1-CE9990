"""
inout.py

Homework 1: Excercise 8

How many days per year spent on Social Media?


"""


import sys

while True:

        try:
            m = input("How many social media accounts do you have? ")
        except EOFError:
            sys.exit(0)

        try:
            account = int(m)
        except ValueError:
            print("Sorry," , m, "is not a whole number.")
            accounts = 0
            print("The number of accounts will default to 0.")

        try:
            m = input("How many hours do you use each account per day? ")
        except EOFError:
            sys.exit (0)

        try:
            hours = int(m)
        except ValueError:
            print ("Sorry," , m, "is not a number.")
            hours = 0
            print("The number of hours will default to 0.")

       

        days = ((account * hours) * 365) / 24

        if days == 1:
            print("That's", int(days), "days per year spent on social media")

        else:
            print("That's", int(days), " days per year spent on social media")

sys.exit(0)

        
        
                   
