#Remove vowels from the input string given by user
string=input("enter the string: ")
vowels="aeiou"
for i in string:
    if i not in vowels:
        print(i)
