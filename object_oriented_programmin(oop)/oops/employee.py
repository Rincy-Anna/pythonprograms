class Employee:
    def setvalue(self,id,name,salary,age,company_name,department):
        self.id=id
        self.name=name
        self.salary=salary
        self.age=age
        self.company_name=company_name
        self.department=department
    def printvalue(self):
        print("id: ",self.id)
        print("name: ", self.name)
        print("salary: ",self.salary)
        print("age: ",self.age)
        print("company name: ",self.company_name)
        print("department: ",self.department)
em=Employee()
em.setvalue(101801,"Jyothis",25000,31,"Subhakiran Capitals","Internal Auditor")
em.printvalue()