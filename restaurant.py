"""

restaurant.py

Output the inspection results for Veselka Restaurant in the East Village

"""


import sys
import csv
import urllib.request


url = "https://data.cityofnewyork.us/api/views/xx67-kt59/rows.csv" \
    "?accessType=DOWNLOAD"


try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)



def score(line):
    """
    Return the line's datestamp, but with the format changed from "12/31/2017"
    to "2017/12/31".  That makes alphabetical order the same as chronological
    order.
    """
    fields = line[8].split("/")
    return fields[2] + "/" + fields[0] + "/" + fields[1]


veselkaLines = []                   

for line in lines:
    try:
        s = line.decode("utf-8")    
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)

    r = csv.reader([s])                          
    fields = next(r)                               
    if fields[0] == "40384528":  
        veselkaLines.append(fields)

lines.close()

for line in veselkaLines:
    print(line[1], line[8])              #name and inspection date
    print(line[11])                      #violation description
    print()

print()

sys.exit(0)
