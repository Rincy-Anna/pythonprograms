class Student:
    school_name="St.sebastian's"
    def setvalue(self,roll_no,name,age,standard):
        self.roll_no=roll_no
        self.name=name
        self.age=age
        self.standard=standard
    def printvalue(self):
        print("roll_no: ",self.roll_no)
        print("name: ",self.name)
        print("age:" ,self.age)
        print("standard: ",self.standard)
        print("school_name: ", Student.school_name)
s=Student()
s.setvalue(42,"Rincy",15,10)
s.printvalue()
s1=Student()
s1.setvalue(41,"Pooja",15,10)
s1.printvalue()
s2=Student()
s2.setvalue(25,"Aswathy",16,11)
s2.printvalue()