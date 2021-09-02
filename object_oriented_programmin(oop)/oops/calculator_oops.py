class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
a=int(input("enter"))
b=int(input("enter"))
obj=Calculator(a,b)
print(obj.addition())
print(obj.subtraction())
print(obj.multiplication())
print(obj.division())