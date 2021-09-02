import re
e=input("enter the email id for validation: ")
x="[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$"
match=re.fullmatch(x, e)
if match is not None:
    print("Valid")
else:
    print("Invalid")
