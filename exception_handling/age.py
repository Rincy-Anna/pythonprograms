# age=int(input("enter your age: "))
# if age<18:
#     raise Exception("you are not eligible for getting vaccination")
# else:
#     print("you are eligible for getting vaccination")


age=int(input("enter your age: "))
if age>=18:
    print("you are eligible for getting vaccination")
else:
    raise Exception("you are not eligible for getting vaccination")
