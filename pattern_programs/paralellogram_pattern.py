def paralell(n):
    k=n
    for i in range(0, n):
        for r in range(0, k):
            print(end=" ")
        k=k+1  #space increment
        for j in range(0, n):
            print("*", end=" ")
        print()
paralell(5)
