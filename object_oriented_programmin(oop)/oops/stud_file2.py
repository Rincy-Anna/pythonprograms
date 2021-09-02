class Student:
    def set(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def print(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.mark)
    def __str__(self):
        return self.name
f1=open('student_details','r')
for i in f1:
    data=i.split(",")
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=data[3]
    stn=Student(name,rollno,course,mark)
    stn.print()