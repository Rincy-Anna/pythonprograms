dict = {"Name" : "Zara", "Age" : 7, "class" : "First"}
print(dict)
print(type(dict))
print(dict["Name"])
print("dict['Name']: ", dict["Name"])
print("dict['Age'): ", dict["Age"])

#updating

#dict = {"Name" : "Zara", "Age" : 7, "class" : "First"}
dict['Age']=8
print(dict)


#add elements in dictionary
dict = {"Name" : "Zara", "Age" : 7, "class" : "First"}
dict['School']="DPS School"

#add elements in dictionary using update keyword
dict.update({'location' : 'kochi'})
print((dict))


#empty dictionary
dict={}
print(dict)
print(type(dict))


#mutable

# del dict['Name']  #remove entry with key
# dict.clear()  #remove all elements in dictionary
# del dict #delete entire dictionary
# print(dict)

#nesting possible
d={1:"hello", 2:{2:3,4:6}}
print(d)
