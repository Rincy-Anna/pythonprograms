s={1,2,3,4,5,6,7,8,9}
prime=set()
not_prime=set()
for i in s:
    if i>=1:
        for j in range(2, i):
            if i % j == 0:
                not_prime.add(i)
                break
        else:
            prime.add(i)
print(prime)
print(not_prime)
