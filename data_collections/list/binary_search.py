list=[1,7,8,9,3,2,5,11,12,13,63,58,98,21,71,10]
def binary_search():
    list.sort()
    print(list)
    element = int(input("enter the element: "))
    flag = 0
    low = 0  #initial index(0)
    upp = len(list)-1 #final index(-1)
    while low <= upp:
        mid = (low+upp)//2 #using // is eleminate fraction
        if element > list[mid]:
            low = mid + 1
        elif element<list[mid]:
            flag=1
            break
    if flag == 1:
        print("found")
    else:
        print("not found")
binary_search()

