class Teacher:
    college = "st.sebastians"
    def __init__(self,id,name,department,subject):
        self.id=id
        self.name=name
        self.department=department
        self.subject=subject
    def printvalue(self):
        print(self.id)
        print(self.name)
        print(self.department)
        print(self.subject)
        print(Teacher.college)
t=Teacher(1,"Mobin","BCA","operating system and system programming")
t.printvalue()
t1=Teacher(2,"Arya","BCA","oracle")
t1.printvalue()
t2=Teacher(3,"Ashily","BCA","vishual basic")
t2.printvalue()
t3=Teacher(4,"Aswathy","B.Com","Accountancy")
t3.printvalue()