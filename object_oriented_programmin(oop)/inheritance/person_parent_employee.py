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
class Employee(Person,Parent):
    def print(self,salary,company):
        self.salary=salary
        self.company=company
        print(self.salary,self.company)
em=Employee()
em.setval("Anugraha",28,"Anugraha Villa")
em.set("Software Engineer")
em.print(45000,"infopark")