class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age

    def printvalue(self):
        print("name: ",self.name)
        print("age : ",self.age)
pe=Person()
pe.setvalue("Rincy", 28)
pe.printvalue()
pe.setvalue("Jyothis", 31)
pe.printvalue()

