def sum_args(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum_args(3,6,7,8,9))
