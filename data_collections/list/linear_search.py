#linear serch algorithm

list = [1,2,3,4,9,8,9,6,5,6,2,8,2,8]
def search(list):
    element = int(input("enter element to search: "))
    flag=0
    for i in list:
        if i == element:
            flag=1
            break
    if flag==0:
        print("not found")
    else:
        print("found")
search(list)