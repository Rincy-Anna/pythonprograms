#First Approach
no1 = int(input("enter the number "))
no2 = int(input("enter the number "))
#
print("value before swapping no1=", no1)
print("value before swapping no2=", no2)
#
# temp = no1
# no1 = no2
# no2 = temp
# print("value after swapping no1=", no1)
# print("value after swapping no2=", no2)

#Second Approach
# (no1,no2)=(no2,no1)
# print("value after swapping no1=", no1)
# print("value after swapping no2=", no2)

#Third Approach

no1=no1+no2
no2=no1-no2
no1=no1-no2
print("value after swapping no1=", no1)
print("value after swapping no2=", no2)