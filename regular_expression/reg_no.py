import re
f2=open("validreg","w")
x="[L][U][M]\d{2}[P][Y]\d{3}$"
f=open("reg_no","r")
for i in f:
    n=i.rstrip("\n")
    matcher=re.fullmatch(x, n)
    if matcher!=None:
        f2.write(n)
        f2.write("\n")
