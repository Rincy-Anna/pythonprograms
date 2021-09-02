class Employee:
    company_name="St. Sebastians college"
    def setvalue(self,id,name,subject,salary):
        self.id=id
        self.name=name
        self.subject=subject
        self.salary=salary
    def printvalue(self):
        print(self.id)
        print(self.name)
        print(self.subject)
        print(self.salary)
        print(Employee.company_name)
em=Employee()
em.setvalue(1,"Mobin","operating system and system programming",56000)
em.printvalue()
em1=Employee()
em1.setvalue(2,"Arya","oracle",52000)
em1.printvalue()
em2=Employee()
em2.setvalue(3,"Ashily","vishual basic",53000)
em2.printvalue()