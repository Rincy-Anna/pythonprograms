import re
x="[a-zA-Z]" #except a, b, c
matcher = re.finditer(x,"abt9 c@5kzabcA")
for match in matcher:
    print(match.start())
    print(match.group())