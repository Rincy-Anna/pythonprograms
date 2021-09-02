#6create a function with arguments and return type which find
# sum of prime numbers between 1 - 50?

def sumprime(min,max):
    sum=0
    for a in range(min,max):
        if a>1:
            for i in range(2, a):
                if(a%i)==0:
                    break
            else:
                sum=sum+a

    return sum
print(sumprime(1,10))


