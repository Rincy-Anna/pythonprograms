def num_pattern(n):  #n is no.of rows
    num=1
    for i in range(n):  # i = 0,1,2,3
        for j in range(i): # j = 0,1,2
            print(num, end=" ")
            num+=1  #num=2,3,4
        print("\r")
print(num_pattern(5))
