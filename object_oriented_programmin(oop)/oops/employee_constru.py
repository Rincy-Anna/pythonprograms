class Employee:
    def __init__(self,id,name,company_name,department):
        self.id=id
        self.name=name
        self.company_name=company_name
        self.department=department
    def printvalue(self):
        print("id: ",self.id)
        print("name: ",self.name)
        print("company name: ",self.company_name)
        print("department: ",self.department)
ob=Employee(10180,"Jyothis","Subhakiran Capital","Internal Auditor")
ob.printvalue()