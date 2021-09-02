x=5
def foo():
    global x
    x+=10
    print("local x is ", x)

foo()
print("global x is ", x)