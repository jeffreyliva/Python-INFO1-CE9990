"""

list.py

The Beatles and Songwriting credits 

"""



import sys

Lennon = [
    ["No Reply",                                1964,
        ["Beatles For Sale"]
    ],

    ["Tomorrow Never Knows",                    1964,  
        ["Revolver"]
    ],

    ["Help",                                    1965,  
        ["Help!"]
    ],

    ["A Hard Day's Night",                      1964,  
        ["A Hard Day's Night"]
    ],

    ["Come Together",                           1969,  
        ["Abbey Road"]
    ]
    ["Strawberry Fields Forever",               1966,
        ["Magical Mystery Tour"],
    ]
    
]

McCartney = [
     ["Got to Get You Into My Life",            1966,
        ["Revolver"]
     ],
     ["The Night Before",                       1965,
        ["Help!"]
     ],
     ["Things We Said Today",                   1964,
        ["A Hard Days Night"]
     ],
     ["All My Loving",                          1964,
        ["With the Beatles"]
     ],
     ["For No One",                             1966,
        ["Revolver"]
     ],
     ["I Saw Her Standing There",               1963,
        ["Please Please Me"]
     ],
     ["Yesterday",                              1965,
        ["Help!"],
     ],
]

Starr = [
     ["Octopus's Garden",                       1969,  
        ["Abey Road"]
     ],
     ["Don't Pass me By",                       1968,
        ["The Beatles"]
     ]

]


Harrison = [
     ["While My Guitar Gently Weeps",           1968,  
        ["The Beatles"]
     ],

     ["Something",                              1969,  
        ["Abbey Road"]
     ],

     ["Within You Without You",                 1967,  
        ["Sgt. Pepper's Lonely Hearts Club Band"]
     ]

     
]

McCartney-Lennon = [
    ["Drive my Car",                            1966,
         ["Rubber Soul"]
    ],

    ["Ticket to Ride",                          1965,
         ["Help!"]
    ],
    ["Norwegian Wood (This Bird Has Flown",     1965,
         ["Rubber Soul"]
    ],
    ["In My Life",                              1965,
         ["Rubber Soul"],
    ],
    ["A Day in the Life",                       1967,
         ["Stg. Pepper's Lonely Hearts Club Band"],
    ]
     
]    

beatles = [
    Lennon,           #0
    McCartney,        #1
    Starr,            #2
    Harrison,         #3
    McCartney-Lennon, #4
    
]

print("Enter")
for i, beatle in enumerate(beatles):
    print("'", i, "' ", "for ", beatle[0][3][0], sep = "")

f = """\
Title: {}
Year: {}
Album: """

while True:

    while True:
        try:
            songwriter = input()
        except EOFError:
            sys.exit(0)

        try:
            songwriter = int(songwriter)
        except ValueError:
            print()
            print("Sorry,", songwriter, "is not a valid selection. Please try again.")
            print()
            continue   #Go back up to the second "while"

        if 0 <= songwriter and songwriter < len(beatles):
            break;

        print()
        print("Sorry,", songwriter, "is not a valid selection. Please try again.")
        print()

    print() #Skip a line

    for title in beatles[songwriter]:
        print(f.format(title[0], title[1], title[2]), end = "")
        songwriter = title[3]

        for i, album in enumerate(albums):
            if i == len(albums) - 1:
                print(album)             #the last star
            else:
                print(album, end = ",") #the other stars
            print() #Skip a line

sys.exit(0)
