d = {1:10, 2:20,3:30}
def is_key_present(x):
    if x in d:
        print(x,"is present in the dictionary")
    else:
        print(x,'is not present in the dictionary')

x=int(input("eneter a key: "))
is_key_present(x)

#or
is_key_present(5)
