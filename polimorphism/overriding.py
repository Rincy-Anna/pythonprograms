#overriding.... same method name and same number of arguments

#Overriding is same method and same number of arguments.
# child class method is override parent class method

class Person:
    def print(self,name):
        self.name=name
        print("inside person methode",self.name)
class Child(Person):
    def print(self,class1):
        self.class1=class1
        print("inside child method",self.class1)
ch=Child()
ch.print("ABC")

#child class method overrides parent class method