class Vehicle:
    def __init__(self,model,reg_no,color):
        self.model = model
        self.reg_no = reg_no
        self.color = color
    def print(self):
        print("Model: ",self.model)
        print("Reg_No: ",self.reg_no)
        print("Color: ",self.color)
ve=Vehicle("Grand I10","KL69B 9291","Red")
ve.print()
