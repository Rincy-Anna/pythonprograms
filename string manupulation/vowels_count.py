# vowels = "aeiou"
# a = input("enter a word: ")
# count=0
# for i in vowels:
#     if i in a:
#         count=count+1
# print(count)

#another format

a=input("enter the string: ")
count=0
for i in a:
    if i in "aeiou":
        count+=1
    else:
        pass
print("the count of vowels in" , a ,"is:", count)