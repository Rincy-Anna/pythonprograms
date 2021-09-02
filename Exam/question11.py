#what is the deference between append and extend,explain with example?
#Append keyword is used to add one element in a list
a=[1,2,3,4]
a.append(8)
print(a)

#Extend keyword is Iterates over its argument and adding each element to the list and extending
# the list. The length of the list increases by number of elements in it’s argument.
first_list=["python","django","pycharm"]
second_list=[2020,3.8]
first_list.extend(second_list)
print(first_list)