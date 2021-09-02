class Person:         #base class/parent class/upper class
    def setval(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("name: ",self.name)
        print("age: ",self.age)
        print("address: ",self.address)
class Employee(Person): #derived class/child class/sub class
    def setvalue(self,id,salary,department):
        self.id=id
        self.salary=salary
        self.department=department
        print("id: ",self.id)
        print("salary: ",self.salary)
        print("department: ",self.department)
em=Employee()
em.setval("Pooja",28,"Pooja Villa")
em.setvalue(101801,85000,"Python Developer")