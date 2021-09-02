num=int(input("enter a number "))
factorial = 1
if (num>0):
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)
elif(num==0):
    print("factorial of zero is one")
else:
    print("factorial does not exist")
