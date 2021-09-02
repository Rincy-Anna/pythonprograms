# class Person:
#     def set(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Child(Person):
#     def set(self,address):
#         self.address=address
#         print(self.address)
# ch=Child()
# ch.set("abc",1)


class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
    def num(self,n3):
        self.n3=n3
        print(self.n3)

op=Operators()
op.num(6,7)