#function with arguments

def factorial(fact):
    n=1
    if fact>0:
        for i in range(1, fact+1):
            n=n*i
        print("factorial", n)
    elif fact==0:
        print("factorial of zero is one")
    else:
        print("factorial is doesnot exist")


factorial(5)
