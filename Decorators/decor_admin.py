def admin_required(func):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("You are not allowed")
        else:
            return func(a,b)
    return wrapper

@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin

@admin_required
def delete_acc(user,acc_no):
    return str(acc_no)+"delete"

print(change_pin("admin",2585))
print(delete_acc("user1",2232))   #exception working