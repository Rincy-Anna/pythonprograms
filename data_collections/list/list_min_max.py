#to find min and max element in a list

# a=[1,2,8,9,92,55,77,66,88,93]
# minimum=min(a)
# maximum=max(a)
# print(minimum,",",maximum)

#to find min and max element in a list without using min max keyword

# a=[3,56,1,2,8,9,92,55,77,66,88,93]
# min=a[0]
# max=a[-1]
# for i in a:
#     if i<min:
#         min=a[i]
#     elif i>max:
#         max=a[i]
# print(min)
# print(max)


#another pgm, simple way
a=[3,56,1,2,8,9,92,55,77,66,88,93]
a.sort()
print(a)
print("minimum element: ",a[0])
print("maximum element: ",a[-1])