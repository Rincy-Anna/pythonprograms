#Combination of uppercase and lowercase letters and end with a number

import re
a=input("enter a string: ")
x="[a-zA-Z]+\d$"
match=re.fullmatch(x, a)
if match is not None:
    print("Valid")
else:
    print("Invalid")