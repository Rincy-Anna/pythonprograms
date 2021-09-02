import re
x="[a-z]" # Check small letters a-z
matcher = re.finditer(x,"abt9 c@5kzabAc")
for match in matcher:
    print(match.start())
    print(match.group())