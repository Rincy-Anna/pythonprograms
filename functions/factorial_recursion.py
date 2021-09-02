def factorial(x):
    """This is a recursive function
    to fin the factorial of an integer"""

    if x==1:
        return 1
    else:
        return x * factorial(x-1) #6*5*4*3*2
num = int(input("enter the number "))
print("The factorial is ", factorial(num))

#print("The factorial is ", factorial(5))