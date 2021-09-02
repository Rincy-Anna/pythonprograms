class Person:
    def setv(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)
class Child(Person):
    def setva(self,standard,school):
        self.standard=standard
        self.school=school
class Student(Child):
    def printva(self,roll_no,mark):
        self.roll_no=roll_no
        self.mark=mark
        print(self.roll_no,self.mark)
st=Student()
st.setv("Chaithanya",15,"Chaithanya Villa")
st.setva(10,"SSHSS")
st.printva(3,95)

