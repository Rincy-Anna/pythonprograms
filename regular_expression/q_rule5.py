import re

x = 'a{1,3]'  # minimum 1 a and maximum 3 a
r = "aaa abc aaaaa cga"
matcher = re.finditer(x, r)
for match in matcher:
    print(match.start())
    print(match.group())


import re

x = 'a{2,3]'  # minimum 2 a and maximum 3 a
r = "aaa abc aaaaa cga"
matcher = re.finditer(x, r)
for match in matcher:
    print(match.start())
    print(match.group())

