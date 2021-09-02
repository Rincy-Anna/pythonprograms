list=[1,2,34,5,6,95]
index=int(input("enter the index position "))
try:
    print(list[index])
except:
    print("index not exist in list")
finally:
    print("inside finally")