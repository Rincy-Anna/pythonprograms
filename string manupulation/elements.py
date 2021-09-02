punctuations = ",./;'[]\()*&^%$#@!|}{/-+"
my_string = input("enter a string: ")

#remove punctuations from the string
no_punct= ""
for char in my_string:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)