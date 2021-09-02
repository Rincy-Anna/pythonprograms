# no1=int(input("enter no1 "))
# no2=int(input("enter no2 "))
# no3=int(input("enter no3 number "))
#
# if no1>no2 and no3<no1:
#     print("no1 is greater")
# elif no1==no2 or no3==no2:
#     print("both are equal")
# else:
#     print("no2 number is greater")

no1=int(input("enter no1 "))
no2=int(input("enter no2 "))
no3=int(input("enter no3 "))

if no1>no2 and no1>no3:
    print("no1 is greater")
if no2>no1 and no2>no3:
    print("no2 is greater")
elif no1==no2==no3:
    print("both are equal")
else:
    print("no3 number is greater")
