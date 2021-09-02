# 1. Create a child class Bus that will inherit all of the variables and methods of Vehicle class?

class Vehicle:
    def setval(self,name,color,reg_no):
        self.name=name
        self.color=color
class Bus(Vehicle):
    def setv(self,reg_no,name,color):
        self.reg_no = reg_no
        self.name=name
        self.color=color
    def print(self):
        print(self.reg_no)
        print(self.name)
        print(self.color)

ve=Bus()
ve.setv("KL69B2089","Bus","Green")
ve.print()
