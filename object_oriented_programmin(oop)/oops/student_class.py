class Student:
    def setvalue(self,roll_no,name,age,standard,school_name):
        self.roll_no=roll_no
        self.name=name
        self.age=age
        self.standard=standard
        self.school_name=school_name
    def printvalue(self):
        print("roll_no: ",self.roll_no,"\n","name: ",self.name,"\n","age:" ,self.age,"\n","standard: ",self.standard,"\n",
              "school_name: ", self.school_name)
s=Student()
s.setvalue(42,"Rincy",15,10,"St.sebastian's")
s.printvalue()