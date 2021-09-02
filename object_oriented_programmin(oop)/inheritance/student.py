# class Student:
#     def __init__(self,name,rollno,department,college):
#         self.name=name
#         self.rollno=rollno
#         self.department=department
#         self.college=college
#     def print(self):
#         print("Name: ",self.name,"\n","Rollno: ",self.rollno,"\n","Department: ",self.department,"\n",
#               "College: ",self.college)
#     def __str__(self):
#         return self.name+self.department
#
# stu=Student("Shreya",19,"BCA","SSCAS")
# stu.print()
# print(stu)



class Student:
    college="SSCAS"
    def __init__(self,name,rollno,department):
        self.name=name
        self.rollno=rollno
        self.department=department
    def print(self):
        print("Name: ",self.name,"\n","Rollno: ",self.rollno,"\n","Department: ",self.department,"\n",
              "College: ",Student.college)
    def __str__(self):
        return self.name+self.department

stu=Student("Shreya",19,"BCA")
stu.print()
print(stu)