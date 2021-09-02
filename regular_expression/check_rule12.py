import re
x='\W'     #For special characters
matcher =re.finditer(x,"abc t@5kz")
for match in matcher:
    print(match.start())
    print(match.group())