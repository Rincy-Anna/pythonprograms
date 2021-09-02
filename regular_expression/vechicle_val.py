import re
v=input("enter vechicle registration number for validation: ")
x="[K][L]\d{2}[A-Z]{2}\d{4}$"
#"[A-Z]\d"
match=re.fullmatch(x, v)
if match is not None:
    print("Valid")
else:
    print("Invalid")