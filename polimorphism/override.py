class Parent:
    def setv(self,num1,num2):
        self.num1=num1
        print(self.num1)

class Child(Parent):
    def set(self,class1):
        self.class1=class1
        print(self.class1)
c=Child()
c.set(5)
