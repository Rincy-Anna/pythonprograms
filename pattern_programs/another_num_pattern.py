# def pattern(n):
#     num=1
#     for i in range(1, 5):
#         for j in range(1, i+1):
#             print(j, end=" ")
#             num+=1
#         print()
# pattern(5)


#another pgm
def pattern(n):
    for i in range(n):
        num=1
        for j in range(i):
            print(num, end=" ")
            num+=1
        print()
pattern(5)