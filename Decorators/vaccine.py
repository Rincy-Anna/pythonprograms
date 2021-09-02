def vaccine_eligibility(func):
    def wrapper(a,b,c):
        if b<18:
            raise Exception("you are not eligible for getting vaccination")
        else:
            return func(a,b,c)
    return wrapper

@vaccine_eligibility
def vaccine(name,age,place):
    return "you are eligible for getting vaccination"
print(vaccine("Sruthi",22,"idukki"))

