#starting with a uppercase letter and then numbers,lowercase letters, symbols

import re
u=input("enter a word: ")
x="([^A-Z][a-z0-9\W]*)"
match=re.fullmatch(x, u)
if match is not None:
    print("Valid")
else:
    print("Invalid")