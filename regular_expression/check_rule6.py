import re
x="[0-9]" #
matcher = re.finditer(x,"abt9 c@5kzabAc")
for match in matcher:
    print(match.start())
    print(match.group())