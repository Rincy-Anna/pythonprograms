a="luminar"
b=input("enter an element to check: ")
flag=0
for i in a:
    if i in b:
        flag=1
if flag==1:
    print("present")
else:
    print("not present")