#inbuilt method

# my_list = [111,-15,-26,-19,2,8,9,22,55,99,-88,77]
# my_list.sort()
# print(my_list)

#without inbuilt method
my_list = [111,-15,-26,-19,2,8,9,22,55,99,-88,77]
new_list = []

while my_list:
    min = my_list[0]
    for i in my_list:
        if i < min: #111<111
            min = i
    new_list.append(min)
    my_list.remove(min)

print(new_list)
print(my_list)