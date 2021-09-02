class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printvalue(self):
        print(self.name,self.age,self.address)
obj=Person("rincy",28,"parackal(h),nedumkandam")
obj.printvalue()