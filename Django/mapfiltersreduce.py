employees = [
    {"e_id": 1000, "e_name": "ram", "salary": 25000, "department": "testing", "exp": 1},
    {"e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1},
    {"e_id": 1002, "e_name": "raj", "salary": 20000, "department": "mrkt", "exp": 1},
    {"e_id": 1003, "e_name": "nikil", "salary": 26000, "department": "developer", "exp": 1},
    {"e_id": 1004, "e_name": "nivi", "salary": 28000, "department": "developer", "exp": 2},
]

#print employee name only    @map

# for employee in employees:
#     print(employee["e_name"])

#using lambda    @map
e_names=list(map(lambda employee:employee["e_name"],employees))
print(e_names)

#print employee names in uppercase

# for employee in employees:
#     print(employee["e_name"].upper())

#using lambda     @map case

e_upper=list(map(lambda emp:emp["e_name"].upper(),employees))
print(e_upper)

#print employee name who are working as developer   @filter

# for employee in employees:
#     if(employee["department"]=="developer"):
#         print("developer",employee["e_name"])


#using lambda     @filter

developers=list(filter(lambda empl:empl["department"]=="developer",employees))
print(developers)

#print name only in developers

developers_name=list(map(lambda dev:dev["e_name"],developers))
print(developers_name)

#print total of salary       @reduce

total=0
for employee in employees:
    total+=employee["salary"]

print(total)


salary=sum(list(map(lambda emp:emp["salary"],employees)))
print(salary)


salary=max(list(map(lambda emp:emp["salary"],employees)))
print(salary)


salary=min(list(map(lambda emp:emp["salary"],employees)))
print(salary)
