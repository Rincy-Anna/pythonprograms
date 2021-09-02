#create a calculator with functions
#(addition,subtraction,multiplication,division,floor division,exponent)?

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b
def floordivision(a, b):
    return a//b
def exponent(a,b):
    return a**b
print("Select an operations")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. floordivision")
print("6. exponent")


while True:
    choice = input("enter the choice(1,2,3,4,5,6): ")
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    if choice == '1':
        print(add(num1, num2))
    elif choice == '2':
        print(subtract(num1, num2))

    elif choice == '3':
        print(multiply(num1, num2))
    elif choice == '4':
        print(divide(num1, num2))
    elif choice == '5':
        print(floordivision(num1,num2))
    elif choice == '6':
        print(exponent(num1,num2))
    else:
        print("Invalid Input")
    break