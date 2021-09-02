#4. Create an Animal class using constructor and build a child class for Dog?

class Animal:
    def __init__(self,animal_name,color):
        self.animal_name=animal_name
        self.color=color
    def print(self):
        print("animal_name: ", self.animal_name)
        print("color: ", self.color)
class Dog(Animal):
    def __init__(self,category,life_span,animal_name,color):
        super().__init__(animal_name,color)
        self.category=category
        self.life_span=life_span
    def printv(self):
        print("category: ",self.category)
        print("life_span: ",self.life_span)
        print("animal_name: ", self.animal_name)
        print("color: ", self.color)
do=Dog("Husky","12-14 years","Dog","Gray & White")
do.printv()



