a=int(input("enter no1: "))
b=int(input("enter no2: "))
if b>a:
    raise Exception("no2 is greater")
else:
    print(a/b)