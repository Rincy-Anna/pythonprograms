#write a code to validate -string starting and ending with a uppercase letter -except special characters
# -minimum length 5 -maximum length 10

import re
m=input("enter a word: ")
x="[A-Z\w]{5,10}[A-Z]$"
match=re.fullmatch(x, m)
if match is not None:
    print("Valid")
else:
    print("Invalid")