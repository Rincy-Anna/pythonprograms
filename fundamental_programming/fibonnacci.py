n=int(input("enter the number: "))
First_Value = 0
Second_Value = 1
for num in range(0, n):
    if (num<=1):
        next = num
    else:
        next = First_Value + Second_Value
    First_Value = Second_Value
    Second_Value = next
    print(next)
