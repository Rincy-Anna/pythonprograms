#functions without arguments

def add():
    num1 = int(input("enter the num1 "))
    num2 = int(input("enter the num2 "))
    res=num1+num2
    print("result", res)
add()



#functions with arguments

# def add(num1,num2):
#     print(num1+num2)
#
# add(10, 15)
# add(20, 30)
# add(55,65)


#functions with arguments and return

def add(num1,num2):
    return (num1+num2)

print(add(10, 15))
print(add(20, 30))