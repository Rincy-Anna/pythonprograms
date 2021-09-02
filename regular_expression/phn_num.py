import re
a=input("enter phone number to validate: ")
x="[+][9][1]\d{10}$"
match=re.fullmatch(x,a)
if match is not None:
    print("Valid")
else:
    print("Invalid")