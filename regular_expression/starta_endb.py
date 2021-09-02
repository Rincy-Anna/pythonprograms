#start with "a" and end with "b"

import re
n=input("enter a word: ")
x='^a[a-zA-Z0-9\w]*b$'
match=re.fullmatch(x, n)
if match is not None:
    print("Valid")
else:
    print("Invalid")