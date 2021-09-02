import re
x='\D'     #Except digits
matcher =re.finditer(x,"abc9t t@5kz")
for match in matcher:
    print(match.start())
    print(match.group())