list=[1,2,5,3,6,5,2,9,6,8,9,1,5]
dupli=[]
for i in list:
    if i not in dupli:
        dupli.append(i)
    else:
        print(i)