import re
x="\w"
matcher = re.finditer(x,"abt9A c@5kzabAc")
for match in matcher:
    print(match.start())
    print(match.group())