#lambda function to check whether a number is even or not?
n = int(input("Enter a number: "))
even = lambda : "Even Number" if n % 2 == 0 else "Not Even"
print(even())