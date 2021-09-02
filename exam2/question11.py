#11. Write a Python program that matches a string that has an 'a' followed by numbers, ending in 'b'?

import re
a=input("enter a string: ")
x="^a\d+b$"
match=re.fullmatch(x, a)
if match is not None:
    print("Valid")
else:
    print("Invalid")