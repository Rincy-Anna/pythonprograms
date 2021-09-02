# #1. keep order
#
# list1=[1,2,3,4,5,6]
# print(list1)
#
# #2. support duplicate element
#
# list2=[1,2,3,4,5,6,2,5]
# print(list2)
#
# #3. heterogeneous

# list3=[1,2,3,4,True,5,6,"hello"]
# print(list3)
#
# #itration
# list4=[1,2,3,4,True,5,6,"hello"]
# print(list4)
# print(type(list4))
# for i in list4:
#     print(i)
#
# #elements add
# list5=[]   #create empty list
# list5.append(2)  #elements adding
# list5.append(8)
# list5.append("hello")
# print(list5)
#
# #4. nesting possible
# list6=[1,2,[4,5,6][7,8,9]]
# print(list6)

#5. list is mutable
list7=[1,2,3,4,5]
list7.append(9) #element add
#list7.clear() #whole element delete
#del list7 #delete list
print(list7)
list7.remove(2)