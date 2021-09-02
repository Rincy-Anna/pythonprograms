# Two rules are applied in this program that are:
# a to z and a to z including group

import re
n="hello"
x = "[a-z]+"
match = re.fullmatch(x, n)
if match is not None:
    print("Valid")
else:
    print("Invalid")