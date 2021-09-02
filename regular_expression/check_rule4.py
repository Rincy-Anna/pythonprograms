import re
x='[A-Z]'  #
matcher = re.finditer(x,"abt9D c@5kzabAc")
for match in matcher:
    print(match.start())
    print(match.group())