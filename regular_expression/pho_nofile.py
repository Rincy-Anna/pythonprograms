import re
f=open("pho_no","r")
x="[+][9][1]\d{10}$"
for i in f:
    #print(i)
    number=i.rstrip("\n")
    #print(number)
    matcher=re.fullmatch(x, number)
    if matcher!=None:
        print(i)
