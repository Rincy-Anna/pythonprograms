class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def print(self):
        print("name: ",self.name)
        print("age: ",self.age)
        print("adrees: ",self.address)

class Employee(Person):
    def __init__(self,empid,department,salary,name,age,address):
        super().__init__(name,age,address)
        self.empid=empid
        self.department=department
        self.salary=salary

    def printv(self):
        print("empid: ",self.empid)
        print("department: ",self.department)
        print("salary: ",self.salary)

emp=Employee(123,"Python Developer",88000,"Nakshathra",28,"Nakshathra(H)")
emp.print()
emp.printv()