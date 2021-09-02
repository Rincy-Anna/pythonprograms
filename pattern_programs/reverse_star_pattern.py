for i in range(6):
    for j in range(6-1, i, -1):
        print("*", end=" ")  #end=" " is using for spacing
    #print("\r")
    print()



for i in range(5,0,-1):  #5,4,3,2,1,0
    for j in range(i):   #4,3,2,1,0
        print("*", end=" ")
    print()