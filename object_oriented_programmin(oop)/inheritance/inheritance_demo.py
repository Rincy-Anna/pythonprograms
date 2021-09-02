#Single inheritance
class Person:         #base class/parent class/upper class
    def walk(self):
        print("person is walking")
    def read(self):
        print("person is reading")
class Student(Person): #derived class/child class/sub class
    def exam(self):
        print("Student is attending exam")
pe=Person()
pe.walk()
pe.read()

st=Student()
st.exam()
st.walk()
st.read()
