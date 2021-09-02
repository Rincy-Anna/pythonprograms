def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b
print("Select Operations")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. divide")

while True:
    choice = input("enter choice(1,2,3,4): ")
    #if choice in ("1","2","3","4"):
    num1 = float(input("enter num1: "))
    num2 = float(input("enter num2: "))
    if choice == '1':
        print(add(num1, num2))
    elif choice == '2':
        print(subtract(num1, num2))

    elif choice == '3':
        print(multiply(num1, num2))
    elif choice == '4':
        print(divide(num1, num2))
    else:
        print("Invalid Input")
    break