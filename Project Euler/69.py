# Project Euler
# Problem 69

from math import sqrt

def isPrime(x) :
    if x < 2 :
        return False
    if x == 2 :
        return True
    for i in range(2,int(sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True

primes = []
for num in range(1,200) :
    if isPrime(num) :
        primes.append(num)

ans = 1
for n in primes :
    if n*ans < 1000000 :
        ans=ans*n
    else :
        break
print(ans)

        








    

