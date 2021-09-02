num1=int(input("enter no1: "))
num2=int(input("enter no2: "))
try:
    print(num1/num2)
except Exception as a:
    print(a.args)
# finally:
#     print("inside")