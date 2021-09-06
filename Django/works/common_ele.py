lst1=[10,20,11,21,22,15]
lst2=[15,22,31,12,10,33]
lst3=[]
lst3.sort()
common_element=list(filter(lambda common:lst1==lst2,lst3))
print(common_element)