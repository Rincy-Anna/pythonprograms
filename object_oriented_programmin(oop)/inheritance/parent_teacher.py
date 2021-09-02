class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print(self):
        print(self.name,self.age)

class Teacher(Parent):
    def __init__(self,id, department,subject,name,age):
        super().__init__(name,age)
        self.id=id
        self.department=department
        self.subject=subject
    def printv(self):
        print(self.id,self.department,self.subject)

    def __str__(self):
        return self.name+" "+ str(self.id)

te=Teacher(1018,"BCA","Python","Megha",28)
te.print()
te.printv()
print(te)
