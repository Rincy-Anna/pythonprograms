#Constructor

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printv(self):
        print("name: ", self.name)
        print("age: ",self.age)

class Student(Person):
    def __init__(self,rollno,mark,name,age): #parent class attributes also adding in
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def printva(self):
        print("rollno: ",self.rollno)
        print("mark: ",self.mark)
        print("name: ", self.name)
        print("age: ", self.age)

cr=Student(2,34,"anu",22)
cr.printva()