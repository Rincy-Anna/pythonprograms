import re

x = "a$"  # Check ending with a
r = "aaa abc aaaaa cga"
matcher = re.finditer(x, r)
for match in matcher:
    print(match.start())
    print(match.group())


# import re
#
# x = "a$"  # Check ending with a
# r = "aaa abc aaaaa cgah"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
