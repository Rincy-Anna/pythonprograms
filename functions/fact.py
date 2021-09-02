#function with arguments and return

def factorial(fact):
    n=1
    if fact>0:
        for i in range(1, fact+1):
            n=n*i
        return n
    elif fact==0:
        return ("factorial of zero is one")
    else:
        return ("factorial is doesnot exist")


print(factorial(5))