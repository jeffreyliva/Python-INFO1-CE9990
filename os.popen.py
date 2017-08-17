"""

os.popen.py

"""
import sys
import os
import csv

infile = os.popen("tasklist /fo csv /nh")  
lines = csv.reader(infile)
lines = sorted(set([line[0] for line in lines]))

status = infile.close()
if status != None:
    print("status =", status)   
    sys.exit(1)


print("Programs Running")

for i, line in enumerate(lines, start = 1):
    print("{:3} {}".format(i, line)) 

sys.exit(0)
