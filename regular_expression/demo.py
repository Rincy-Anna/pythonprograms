# import re
# count=0
# matcher = re.finditer('ab','abbaaba')
# #print(matcher)
# for match in matcher:
#     count+=1
# print("count= ",count)



import re
count=0
matcher=re.finditer('ab','abaabbab')
for match in matcher:
    print("match available at ",match.start())
    print("group ",match.group())
    count+=1
    print("count is ",count)