class Person:
    def setval(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)
class Child:
    def set(self,standard,school):
        self.standard=standard
        self.school=school
        print(self.standard,self.school)
class Student(Person,Child):
    def printval(self,roll_no,mark):
        self.roll_no=roll_no
        self.mark=mark
        print(self.roll_no,self.mark)
st=Student()
st.setval("Nakshathra",10,"Nakshatravilla")
st.set(5,"St.sebastians")
st.printval(14,95)