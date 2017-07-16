"""
forurl.py

Burning Down the House

"""

import sys
import urllib.request

url = "https://raw.githubusercontent.com/jeffreyliva/Python-INFO1-CE9990/master/Burningdownthehouse.txt"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

for line in lines:
    try:
        s = line.decode("utf-8")
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)

    print(s, end = "")           

lines.close()
sys.exit(0)
