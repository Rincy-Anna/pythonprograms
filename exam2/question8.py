#8. When is the finally block executed.Explain with example?
list=[1,32,34,5,16,95,26,33,88,99,12]
index=int(input("enter the index position "))
try:
    print(list[index])
except:
    print("index not exist in list")
finally:
    print("inside finally")