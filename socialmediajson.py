"""

Leading causes of Death in NYC

json.py

"""

import sys
import urllib.request
import json

url= "https://data.cityofnewyork.us/api/views/" \
     "jb7j-dtam/rows.json?accessType=DOWNLOAD"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = infile.read()         #Read the entire input file.
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8") #s is a string.
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)


try:
    dictionary = json.loads(s)          #dictionary is a dictionary.
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)



cause = collections.defaultdict(lambda: [0])


for cause in dictionary["data"]:
    try:
        total = int(data[0])
    except TypeError:
        continue

        
for total in sorted(cause):
    cause.sort(reverse = True)
    print(cause)
    print("Total Number of Deaths : ", cause[data][0][4])
    print()

sys.exit(0)
