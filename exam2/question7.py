#7. Create a valid phone numbers file from the following file?
#   +915678905432 +914567890321 765432167 123450987765 +919976532456

import re
f=open("phn_num","r")
x="[+][9][1]\d{10}$"
for i in f:
    number=i.rstrip("\n")
    matcher=re.fullmatch(x, number)
    if matcher!=None:
        print(i)
