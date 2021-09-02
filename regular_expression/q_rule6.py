import re

x = '^a'  # check starting with a
r = "aaa abc aaaaa cga"
matcher = re.finditer(x, r)
for match in matcher:
    print(match.start())
    print(match.group())


# import re
#
# x = '^a'  # check starting with a
# r = "vaaa abc aaaaa cga"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

