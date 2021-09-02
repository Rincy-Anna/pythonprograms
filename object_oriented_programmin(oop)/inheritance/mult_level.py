#Multilevel Inheritance/Hierachial Inheritance

class A:
    def printA(self):
        print("inside A")
class B(A):
    def printB(self):
        print("inside B")
class C(B):
    def printC(self):
        print("inside C")
a=A()
a.printA()
b=B()
b.printA()
b.printB()
c=C()
c.printA()
c.printB()
c.printC()