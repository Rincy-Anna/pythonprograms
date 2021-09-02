#input min & max number and print only even numbers

min=int(input("enter initial range "))
max=int(input("enter final range "))
for i in range(min,max+1):
    if i%2==0:
        print(i)