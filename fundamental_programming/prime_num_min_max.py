min=int(input("enter min "))
max=int(input("enter max "))
for a in range(min,max+1):
    if a>1:
        for i in range(2, a):
            if a%i==0:
                break
        else:
            print(a)