"""
list.py

The Beatles and Songwriting credits
"""

import sys

songwriters = (
    None,

    ("Lennon", (
        ("Beatles For Sale", 1964, (
            "No Reply",
        )),
        ("Revolver", 1964, (
            "Tomorrow Never Knows",
        )),
        ("Help!", 1965, (
            "Help",
        )),
        ("A Hard Day's Night", 1964, (
            "A Hard day's Night",
        )),
        ("Abbey Road", 1969, (
           "Come Together",
        )),
        ("Magical Mystery Tour", 1966, (
            "Strawberry Fields Forever",
        ))
    )),

    ("McCartney", (
        ("Revolver", 1966, (
            "Got to Get You Into My Life",
        )),
        ("Help!", 1965, (
            "The Nght Before",
        )),
        ("A Hard Day's Night", 1964, (
            "Things We Said Today",
        )),
        ("With the Beatles", 1964, (
            "All My Loving",
        )),
        ("Revolver", 1966, (
            "For No One",
        )),
        ("Please Please Me", 1963, (
            "I Saw Her Standing There",
        )),
        ("Help!", 1965, (
            "Yesterday",
        ))
    )),

    ("Starr", (
        ("Abbey Road", 1969, (
            "Octopus's Garden",
        )),
        ("The Beatles", 1968, (
            "Don't Pass Me By",
        ))
    )),

    ("Harrison", (
        ("The Beatles", 1968, (
            "While My Guitar Gently Weeps",
        )),
        ("Abbey Road", 1969, (
            "Something",
        )),
        ("Sgt. Pepper's Lonely Hearts Club Band", 1967, (
            "Within You Without You",
        ))
    )),

    ("McCartney/Lennon", (
        ("Rubber Soul", 1966, (
            "Drive My Car",
        )),
        ("Help!", 1965, (
            "Ticket To Ride",
        )),
        ("Rubber Soul", 1965, (
            "Norwegian Wood (This Bird Has Flown)",
        )),
        ("Rubber Soul", 1965, (
             "In My Life",
        )),
        ("Sgt. Pepper's Lonely Hearts Club Band", 1967, (
            "A Day in the Life",
        ))
    ))
)

while True:
    while True:
        print("Enter")
        for i, songwriter in enumerate(songwriters[1:], start = 1):
            print("'", i, "' ", "for ", songwriter[0], sep = "")

        try:
            s = input()
        except EOFError:
            sys.exit(0)

        try:
            i = int(s)
        except ValueError:
            print("Sorry,", s, "is not an integer.  Please try again.")
            continue

        if 0 <= i < len(songwriters):
            break

        print("Sorry, must be in range 0 to", len(songwriters)-1, "inclusive.")
        print("Please try again.")

    songwriter = songwriters[i]
    print("Songwriter:", songwriter[0])
    for album in songwriter[1]:
        print("    Album: ", album[0], " (", album[1], ")", sep = "")
        for title in album[2]:
            print("       ", title)

    print()
