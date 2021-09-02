# a={1,2,3,4,5}
# print(a)
# print(type(a))
# b={5,6,7,8,9}
# print(b)
#
# # 1. set doesnt keep order
# b={9,5,8,0,1,3,6,2}
# print(b)
#
#
# # 2. heterogenous
#
# a=set()
# a.add(2)
# a.add(3)
# a.add(5)
# a.add("hello")
# a.add(7.8)
# a.add(True)
# print(a)
# print(type(a))
#
#
# # 3.doesnt support duplicate elements
# a={1,2,3,1,2}
# print(a)

b={1,"hello",2,5,6,7,9.5,4,False}
print(b)
for i in b:
    print(i)


#mutable
s={1,2,3,4,3,5}
s.remove(5) #remove one element
s.clear() #clear whole element
del s  # delete set
print(s)

#nesting not possible
a={1,{2,3}}
print(a)