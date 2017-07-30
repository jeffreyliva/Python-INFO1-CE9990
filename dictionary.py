"""

dictionary.py

NFL Head Coaches

"""


import sys

coaches = {
    "Arizona Cardinals": "Bruce Arians",
    "Atlanta Falcons": "Dan Quinn",
    "Baltimore Ravens": "John Harbaugh",
    "Buffalo Bills": "Sean McDermot",
    "Carolina Pathers": "Ron Rivera",
    "Chicago Bears": "John Fox",
    "Cincinnati Bengals": "Marvin Lewis",
    "Cleveland Browns": "Hue Jackson",
    "Denver Broncos": "Vance Joseph",
    "Detroit Lions":"Jim Caldwell",
    "Green Bay Packers":"Mike McCarthy",
    "Houston Texans":"Bill O'Brian",
    "Indianapolic Colts":"Chuck Pagano",
    "Jacksonville Jaguars":"Doug Marron",
    "Kansas City Chiefs":"Andy Reid",
    "Los Angeles Chargers":"Anthony Lynn",
    "Los Angeles Rams":"Sean McVay",
    "Miami Dolphins":"Adam Gase",
    "Minnesota Vikings":"Mike Zimmer",
    "New England Patriots":"Bill Belichick",
    "New Orleans Saints":"Sean Payton",
    "New York Giants":"Ben McAdoo",
    "New York Jets":"Todd Bowles",
    "Oakland Raiders":"Jack Del Rio",
    "Philadelphia Eagles":"Doug Pederso",
    "Pittsburgh Steelers":"Mike Tomlin",
    "San Francisco 49ers":"Kyle Shanahan",
    "Seatle Seahawks":"Pete Carroll",
    "Tampa Bay Buchaneers":"Dirk Koette",
    "Tennessee Titans":"Mike Mularkey",
    "Washington Redskins":"Jay Gruden"
}

while True:
    try:
        team = input("Please enter a NFL Team: ")
        print()
    except EOFError:
        sys.exit(0)

    try:
        definition = coaches[team]
    except KeyError:
        print("Sorry, \"", team, "\" is not a team in the NFL.", sep = "")
        print()
        continue   #Go back up to the word "while".
    
    print("The coach of the NFL team is ",team.capitalize()," is: ", definition, ".", sep = "")
    print()
   

sys.exit(0)
