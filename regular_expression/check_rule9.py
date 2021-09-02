import re
x='\d'     #Check the digits
matcher =re.finditer(x,"abc9t t@5kz")
for match in matcher:
    print(match.start())
    print(match.group())