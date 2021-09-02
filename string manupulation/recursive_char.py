#First recursive(repeated) character in a string

a=input("enter a string: ")
repeated_char = " "
for i in a:
    if i not in repeated_char:
        repeated_char=repeated_char+i
    else:
        print("first recursive character in ",a,"is: ", i)