class Person:         #base class/parent class/upper class
    def setval(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("name: ",self.name)
        print("age: ",self.age)
        print("address: ",self.address)
class Parent:
    def set(self,job):
        self.job=job
        print("job: ",self.job)
class Teacher(Person,Parent):
    def printvalue(self,department,subject):
        self.department=department
        self.subject=subject
        print("department: ",self.department)
        #print("subject: ",subject)
        print("subject: ", self.subject)

te=Teacher()
te.setval("Sruthi",28,"Sruthi Villa")
te.set("Teacher")
te.printvalue("BCA","Python")

